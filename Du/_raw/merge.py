# -*- coding: utf-8 -*-
"""
语雀 Java 笔记清洗合并脚本 v2

处理内容（仅作用于代码块外）：
1. 文本用途 HTML 标签转义为实体（保留 font / br/ / 成对字符级格式标签）
2. HTML 注释转义
3. 反引号内 font 剥壳（语雀"代码样式+颜色"导出失真）
   - `**<font ...>X</font>**` → **`X`**
   - `<font ...>X</font>` → `X`
4. 反引号外 font：
   - 深色系（近黑/暗灰）→ 剥离（避免深色主题下文字隐形）
   - 浅色底（代码样式）→ 转为反引号 `X`
   - 彩色 → 保留
5. 标题降一级（源 doc title 作为 H1）
6. 块外连续空行压缩为最多 1 个
7. 按 17 个分类合并输出
"""
import json
import re
import os
from collections import defaultdict, Counter

RAW = r'D:/MyNotes/Du/_raw'
OUT = r'D:/MyNotes/Du'
BT = chr(96)  # 反引号

BOOK = [
    ("01-JavaSE", ["na23g2vnz7cgzzdi", "rw03xkpkadgaw7u7", "gqhbqtrtg7ruutad", "ohod7qvxq1z36ocz",
                   "qhagel2niihaqfl0", "osb8y2l2q8urmtn9", "hmquiuye1fg6irwy", "tpq5h36k7huw6lmg",
                   "mqhcc1lh1m94713v", "cagtgrmuzx9ig14e", "rgb5uru34dzbwpse", "txtiia405xiq5g3k",
                   "sl7071kp08h6zlwq", "qnodco6rtzwg62sg", "oh8efg7v4gfcuvbx", "piphoczi1zmhhduz",
                   "cxnnnxpt8ubmiqle"]),
    ("02-MySQL", ["uzw5g4gtnuew49yp"]),
    ("03-JDBC", ["cy7vu9zsa0gmpprp"]),
    ("04-Web前端", ["gr1diu", "uqkric", "lk3u4vr4uc1ekxbk"]),
    ("05-XML&JSON", ["anghr4"]),
    ("06-JavaWeb", ["rd3n67sf9bnakih9"]),
    ("07-Ajax&axios", ["szlh0l"]),
    ("08-Maven", ["hp5bllxqf7g9gmn5"]),
    ("09-MyBatis", ["udots9ngcd97pyui"]),
    ("10-Spring", ["lyvg9x9hf3u22s7e"]),
    ("11-SpringMVC", ["myxi54xu063hgsl4"]),
    ("12-SpringBoot", ["uwxe0halgc03tm93"]),
    ("13-MyBatis-Plus", ["qgp36l3entp30hp2"]),
    ("14-TypeScript", ["mt5sq6akfcx5fr5g"]),
    ("15-Vue3", ["vu082c"]),
    ("16-ElementPlus", ["yw2xscrz4thagw34"]),
    ("17-Linux", ["nurwunyse629kzwy"]),
]

TAG_RE = re.compile(r'</?([a-zA-Z][a-zA-Z0-9:._-]*)((?:\s[^<>]*)?)/?>')
COMMENT_RE = re.compile(r'<!--[\s\S]*?-->')
HEADING_RE = re.compile(r'^(#{1,6})\s')
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
FONT_OPEN_RE = re.compile(r'<font\s+style="([^"]*)"[^<>]*>')
FONT_CLOSE_RE = re.compile(re.escape('</font>'))
STYLE_TAGS = {'sup', 'sub', 'u', 'del', 'ins', 'em', 'i', 'b', 'strong',
              'small', 'mark', 's', 'big', 'kbd', 'var', 'cite', 'abbr',
              'dfn', 'time', 'q'}


def backtick_spans(line):
    spans = []
    i, n = 0, len(line)
    while i < n:
        if line[i] == BT:
            j = i
            while j < n and line[j] == BT:
                j += 1
            k = line.find(BT * (j - i), j)
            if k == -1:
                spans.append((i, n))
                break
            spans.append((i, k + (j - i)))
            i = k + (j - i)
        else:
            i += 1
    return spans


def esc(s):
    return s.replace('<', '&lt;').replace('>', '&gt;')


def parse_color(v):
    v = v.strip()
    m = re.match(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', v)
    if m:
        return tuple(int(x) for x in m.groups())
    m = re.match(r'#([0-9a-fA-F]{6})$', v)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.match(r'#([0-9a-fA-F]{3})$', v)
    if m:
        h = m.group(1)
        return tuple(int(c * 2, 16) for c in h)
    return None


def is_dark_style(style):
    """近黑/暗灰色文字（深色主题下不可读）→ 需剥离"""
    m = re.search(r'(?<!background-)color:\s*([^;"]+)', style)
    if not m:
        return False
    rgb = parse_color(m.group(1))
    if not rgb:
        return False
    mx, mn = max(rgb), min(rgb)
    return mx < 128 and (mx - mn) < 40


def is_bg_light_style(style):
    """浅色底（语雀代码样式）→ 转为反引号"""
    m = re.search(r'background-color:\s*([^;"]+)', style)
    if not m:
        return False
    rgb = parse_color(m.group(1))
    if not rgb:
        return False
    return min(rgb) > 200


def font_pass(lines, stats):
    """Pass1：全文档 font 事件配对，生成按行的操作 {line_no: [(s,e,repl)]}"""
    ops_by_line = defaultdict(list)
    in_fence = False
    fs_char = None
    fs_len = 0
    stack = []
    for i, line in enumerate(lines):
        if in_fence:
            if re.match(r'^\s{0,3}' + re.escape(fs_char) + '{' + str(fs_len) + r',}\s*$', line):
                in_fence = False
                fs_char = None
            continue
        m = FENCE_RE.match(line)
        if m:
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            continue
        spans = backtick_spans(line)
        comment_spans = [(cm.start(), cm.end()) for cm in COMMENT_RE.finditer(line)]

        def in_mask(pos):
            return (any(a <= pos < b for a, b in spans)
                    or any(a <= pos < b for a, b in comment_spans))

        events = []
        for m2 in FONT_OPEN_RE.finditer(line):
            if in_mask(m2.start()):
                continue
            events.append(('open', m2.start(), m2.end(), m2.group(1)))
        for m2 in FONT_CLOSE_RE.finditer(line):
            if in_mask(m2.start()):
                continue
            events.append(('close', m2.start(), m2.end(), None))
        events.sort(key=lambda x: x[1])
        for kind, s, e, style in events:
            if kind == 'open':
                stack.append((i, s, e, style))
            else:
                if not stack:
                    stats['font_solo_close'] += 1
                    continue
                i0, s0, e0, st0 = stack.pop()
                # 紧邻空对（<font ...></font> 无内容）→ 整体删除
                if i0 == i and e0 == s:
                    ops_by_line[i].append((s0, e, ''))
                    stats['font_empty_removed'] += 1
                    continue
                if is_bg_light_style(st0):
                    ops_by_line[i0].append((s0, e0, BT))
                    ops_by_line[i].append((s, e, BT))
                    stats['font_to_code'] += 1
                elif is_dark_style(st0):
                    ops_by_line[i0].append((s0, e0, ''))
                    ops_by_line[i].append((s, e, ''))
                    stats['font_delete_dark'] += 1
                else:
                    stats['font_keep_color'] += 1
    stats['font_solo_open'] += len(stack)
    return ops_by_line


def rebuild_span(seg):
    """反引号 span（含分隔符）内 font 剥壳"""
    dl = 0
    while dl < len(seg) and seg[dl] == BT:
        dl += 1
    if dl == 0 or len(seg) < 2 * dl:
        return seg
    trailing = 0
    while trailing < len(seg) - dl and seg[len(seg) - 1 - trailing] == BT:
        trailing += 1
    if trailing != dl:
        return seg
    delim = seg[:dl]
    inner = seg[dl:len(seg) - dl]
    if '<font' not in inner:
        return seg
    inner2 = FONT_OPEN_RE.sub('', inner).replace('</font>', '')
    if inner2.startswith('**') and inner2.endswith('**') and inner2.count('**') == 2 and len(inner2) >= 4:
        core = inner2[2:-2]
        if BT not in core and core.strip() != '':
            return '**' + delim + core + delim + '**'
        inner3 = inner2.replace('**', '')
    else:
        inner3 = inner2.replace('**', '')
    if inner3.strip() == '':
        return ''
    return delim + inner3 + delim


def fix_heading_fence(lines, stats):
    """Obsidian 严格模式下：标题行紧跟代码块 fence 会导致代码块不被识别。
    在标题行与 fence 行之间插入空行。"""
    out = []
    in_fence = False
    fs_char = None
    fs_len = 0
    prev_heading = False
    for line in lines:
        if in_fence:
            out.append(line)
            if re.match(r'^\s{0,3}' + re.escape(fs_char) + '{' + str(fs_len) + r',}\s*$', line):
                in_fence = False
            prev_heading = False
            continue
        m = FENCE_RE.match(line)
        if m:
            if prev_heading:
                out.append('')
                stats['heading_fence_fixed'] += 1
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            out.append(line)
            prev_heading = False
            continue
        prev_heading = bool(HEADING_RE.match(line))
        out.append(line)
    return out


def process_doc(text, diag):
    lines = text.split('\n')
    font_ops = font_pass(lines, diag)

    out = []
    in_fence = False
    fs_char = None
    fs_len = 0
    blank_run = 0
    for i, line in enumerate(lines):
        if in_fence:
            out.append(line)
            if re.match(r'^\s{0,3}' + re.escape(fs_char) + '{' + str(fs_len) + r',}\s*$', line):
                in_fence = False
                fs_char = None
            continue
        m = FENCE_RE.match(line)
        if m:
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            out.append(line)
            blank_run = 0
            continue
        if line.strip() == '':
            blank_run += 1
            if blank_run <= 1:
                out.append(line)
            continue
        # 语雀空样式残留行（独立 "``" / "**``**"）→ 清空为空白
        if re.fullmatch(r'(?:\*\*)?`{2}(?:\*\*)?', line.strip()):
            blank_run += 1
            if blank_run <= 1:
                out.append('')
            diag['empty_span_line_removed'] += 1
            continue
        blank_run = 0

        # ---- 行内处理 ----
        spans = backtick_spans(line)
        comment_spans = [(cm.start(), cm.end()) for cm in COMMENT_RE.finditer(line)]
        ops = []

        # 1) span 重构
        for a, b in spans:
            seg = line[a:b]
            if '<font' in seg:
                new_seg = rebuild_span(seg)
                if new_seg != seg:
                    ops.append((a, b, new_seg))
                    diag['span_rebuilt'] += 1

        # 2) 标签转义（反引号外、注释外）
        def masked(pos):
            return (any(a <= pos < b for a, b in spans)
                    or any(a <= pos < b for a, b in comment_spans))

        events = []
        for m2 in TAG_RE.finditer(line):
            if masked(m2.start()):
                continue
            raw = m2.group(0)
            events.append([m2.start(), m2.end(), m2.group(1).lower(), raw.startswith('</'), raw])
        keep = set()
        stack = []
        for ev in events:
            if ev[2] not in STYLE_TAGS:
                continue
            if ev[3]:
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k][2] == ev[2]:
                        op = stack.pop(k)
                        keep.add(op[0])
                        keep.add(ev[0])
                        break
            else:
                stack.append(ev)
        for ev in events:
            s, e, name, is_close, raw = ev
            if name == 'font':
                continue
            if raw in ('<br/>', '<br />'):
                continue
            if s in keep:
                diag['kept'] += 1
                continue
            ops.append((s, e, esc(raw)))
            diag['escaped'] += 1

        # 3) HTML 注释转义
        for cm in COMMENT_RE.finditer(line):
            if any(a <= cm.start() < b for a, b in spans):
                continue
            ops.append((cm.start(), cm.end(), esc(cm.group(0))))
            diag['comments'] += 1

        # 4) font 操作
        ops.extend(font_ops.get(i, []))

        # 5) 倒序应用
        if ops:
            ops.sort(key=lambda x: x[0], reverse=True)
            prev_start = None
            for s, e, rep in ops:
                if prev_start is not None and e > prev_start:
                    diag['overlap'] += 1
                prev_start = s
                line = line[:s] + rep + line[e:]

        # 标题降级
        hm = HEADING_RE.match(line)
        if hm:
            line = '#' + line
            diag['headings'] += 1
        out.append(line)
    return '\n'.join(fix_heading_fence(out, diag))


def main():
    log_lines = []
    totals = Counter()
    for fname, slugs in BOOK:
        parts = []
        for slug in slugs:
            with open(os.path.join(RAW, slug + '.json'), encoding='utf-8') as f:
                d = json.load(f)
            data = d['data']
            title = data['title']
            sc = data['sourcecode'].strip('\n')
            diag = Counter()
            body = process_doc(sc, diag).strip('\n')
            # 特判修复：个别语雀导出残留（多余反引号导致字面显示）
            if '`ctrl+``组合键' in body:
                body = body.replace('`ctrl+``组合键', '`ctrl+`组合键')
                diag['bt_ctrl_fixed'] = 1
            parts.append('# ' + title + '\n\n' + body)
            totals.update(diag)
            log_lines.append('=' * 70)
            log_lines.append(f'[{fname}] {title}')
            log_lines.append('  ' + ' | '.join(f'{k}={v}' for k, v in sorted(diag.items())))
        content = '\n\n'.join(parts) + '\n'
        out_path = os.path.join(OUT, fname + '.md')
        with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f'[OK] {fname}.md ({len(content)} chars)')
        log_lines.append(f'  ==> {out_path}')

    log_lines.append('=' * 70)
    log_lines.append('TOTAL: ' + ' | '.join(f'{k}={v}' for k, v in sorted(totals.items())))
    with open(os.path.join(RAW, '_escape_log_v2.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(log_lines))
    print('TOTAL:', dict(totals))


if __name__ == '__main__':
    main()

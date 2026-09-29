# -*- coding: utf-8 -*-
"""最终验证 v3：全部检查项"""
import re
import glob
import os
from collections import Counter

OUT = r'D:/MyNotes/Du'
BT = chr(96)
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
TAG_RE = re.compile(r'</?([a-zA-Z][a-zA-Z0-9:._-]*)((?:\s[^<>]*)?)/?>')
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


r = Counter()
issues = []
for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    in_fence = False
    fs_char = None
    fs_len = 0
    for i, line in enumerate(lines):
        if in_fence:
            if re.match(r'^\s{0,3}' + re.escape(fs_char) + '{' + str(fs_len) + r',}\s*$', line):
                in_fence = False
            continue
        m = FENCE_RE.match(line)
        if m:
            r['fence'] += 1
            # 检查 heading-fence 碰撞
            if i > 0:
                prev = lines[i - 1]
                if re.match(r'^#{1,6}\s', prev):
                    r['heading_fence_collision'] += 1
                    issues.append(f'[{fname}] L{i}: 标题碰撞 {prev[:40]!r}')
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            continue
        spans = backtick_spans(line)
        # 反引号内 font
        for a, b in spans:
            if '<font' in line[a:b]:
                r['bt_font'] += 1
        # 空 font 对 / 反引号外 font
        mask = list(line)
        for a, b in spans:
            for k in range(a, b):
                mask[k] = ' '
        masked = ''.join(mask)
        for fm in re.finditer(r'<font\b[^>]*></font>', masked):
            r['empty_font'] += 1
        for fm in re.finditer(r'<font\s+style="([^"]*)"', masked):
            cm2 = re.search(r'(?<!background-)color:\s*([^;"]+)', fm.group(1))
            r['font_color_' + (cm2.group(1).strip() if cm2 else '-')] += 1
        # 独立空 span 行
        if re.fullmatch(r'(?:\*\*)?`{2}(?:\*\*)?', line.strip()):
            r['empty_span_line'] += 1
        # 注释残留
        for cm in re.finditer(r'<!--', line):
            if not any(a <= cm.start() < b for a, b in spans):
                r['comment_residual'] += 1
        # 裸标签
        cspans = [(cm.start(), cm.end()) for cm in re.finditer(r'<!--[\s\S]*?-->', line)]
        events = []
        for tm in TAG_RE.finditer(line):
            if any(a <= tm.start() < b for a, b in spans):
                continue
            if any(a <= tm.start() < b for a, b in cspans):
                continue
            raw = tm.group(0)
            events.append((tm.start(), tm.end(), tm.group(1).lower(), raw.startswith('</'), raw))
        stack = []
        keep = set()
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
            if name == 'font' or raw in ('<br/>', '<br />') or s in keep:
                continue
            r['residual_tag'] += 1
            if r['residual_tag'] <= 10:
                issues.append(f'[{fname}] L{i+1}: 裸标签 {raw}')

print('检查结果:')
checks = [
    ('heading_fence_collision', '标题-fence 碰撞（应 0）'),
    ('bt_font', '反引号内 font（应 0）'),
    ('empty_font', '空 font 对残留（应 0）'),
    ('empty_span_line', '独立空 span 行（应 0）'),
    ('comment_residual', '注释残留（应 0）'),
    ('residual_tag', '非预期裸标签（应 0）'),
]
all_ok = True
for k, name in checks:
    v = r.get(k, 0)
    status = 'OK' if v == 0 else '!! 异常'
    if v != 0:
        all_ok = False
    print(f'  {name}: {v}  [{status}]')
print()
print('统计:')
print('  fence 行数:', r.get('fence', 0))
for k in sorted(r):
    if k.startswith('font_color_'):
        print(f'  {k}: {r[k]}')
print()
print('issue 明细（若有）:')
for x in issues[:20]:
    print(' ', x)
if not issues:
    print('  （无）')
print()
print('=== 总体:', 'ALL PASS' if all_ok else 'HAS ISSUES', '===')

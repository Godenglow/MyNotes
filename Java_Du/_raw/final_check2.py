# -*- coding: utf-8 -*-
"""最终验证 v4：含星号闭环检查"""
import re
import glob
import os
import json

OUT = r'D:/MyNotes/Du'
BT = chr(96)
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')


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


# 1) 残留 4+ 星扫描
non_idle = []
idle = 0
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
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            continue
        spans = backtick_spans(line)
        for sm in re.finditer(r'\*{4,}', line):
            if any(a <= sm.start() < b for a, b in spans):
                continue
            # IDLE 判定
            s, e = sm.start(), sm.end()
            left = line[s - 1] if s > 0 else None
            right = line[e] if e < len(line) else None
            lsp = left is None or left.isspace()
            rsp = right is None or right.isspace()
            if lsp and rsp:
                idle += 1
            else:
                non_idle.append((fname, i + 1, line[max(0, s - 50):e + 50]))

print('1) 残留 4+ 星: IDLE(独立/hr 行) =', idle, '| 非 IDLE(应为 0) =', len(non_idle))
for f, ln, ctx in non_idle[:15]:
    print(f'   [{f}] L{ln}: {ctx}')

# 2) 导出 349 行的当前内容供 Node 复验
rows = []
for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    for i, line in enumerate(lines):
        if re.search(r'\*{4,}', line):
            rows.append({'file': fname, 'ln': i + 1, 'text': line})
with open(os.path.join(OUT, '_raw', '_star_recheck.json'), 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False)
print()
print('2) 待复验行（含 4+ 星）:', len(rows))

# 3) 原有 6 项检查快速复核
TAG_RE = re.compile(r'</?([a-zA-Z][a-zA-Z0-9:._-]*)((?:\s[^<>]*)?)/?>')
STYLE_TAGS = {'sup', 'sub', 'u', 'del', 'ins', 'em', 'i', 'b', 'strong',
              'small', 'mark', 's', 'big', 'kbd', 'var', 'cite', 'abbr',
              'dfn', 'time', 'q'}
c = {'heading_fence': 0, 'bt_font': 0, 'empty_font': 0, 'comment': 0, 'bare_tag': 0}
for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
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
            if i > 0 and re.match(r'^#{1,6}\s', lines[i - 1]):
                c['heading_fence'] += 1
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            continue
        spans = backtick_spans(line)
        for a, b in spans:
            if '<font' in line[a:b]:
                c['bt_font'] += 1
        mask = list(line)
        for a, b in spans:
            for k in range(a, b):
                mask[k] = ' '
        masked = ''.join(mask)
        c['empty_font'] += len(re.findall(r'<font\b[^>]*></font>', masked))
        for cm in re.finditer(r'<!--', line):
            if not any(a <= cm.start() < b for a, b in spans):
                c['comment'] += 1
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
            s2, e2, name, is_close, raw = ev
            if name == 'font' or raw in ('<br/>', '<br />') or s2 in keep:
                continue
            c['bare_tag'] += 1

print()
print('3) 原有检查:', c)

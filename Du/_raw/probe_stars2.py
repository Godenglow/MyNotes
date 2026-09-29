# -*- coding: utf-8 -*-
"""区分代码块内外的 4+ 连星统计 + 关键样本"""
import re
import glob
import os
from collections import Counter

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


in_code = 0
in_bt = 0
outside = 0
pats = Counter()
samples = {}

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    in_fence = False
    fs_char = None
    fs_len = 0
    for i, line in enumerate(lines):
        if in_fence:
            in_code += len(re.findall(r'\*{4,}', line))
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
                in_bt += 1
                continue
            outside += 1
            s, e = sm.start(), sm.end()
            left = line[max(0, s - 1):s] if s > 0 else 'EDGE'
            right = line[e:e + 1] if e < len(line) else 'EDGE'

            def c(ch):
                if ch == '':
                    return 'EDGE'
                if ch.isspace():
                    return 'SPACE'
                if ch == '*':
                    return '*'
                if ch == BT:
                    return 'BT'
                return 'TEXT'
            key = (len(sm.group(0)), c(left), c(right))
            pats[key] += 1
            if key not in samples:
                samples[key] = (fname, i + 1, line[max(0, s - 55):e + 55])

print('代码块内 4+连星:', in_code, '| 行内代码内:', in_bt, '| 代码块外:', outside)
print()
print('=== 代码块外的形态分布 ===')
for k, v in pats.most_common(30):
    print(f'  {k}: {v}')
print()
print('=== 样例 ===')
for k in sorted(pats, key=lambda x: -pats[x]):
    f, ln, ctx = samples[k]
    print(f'  {k} x{pats[k]} [{f}] L{ln}:')
    print(f'      {ctx}')

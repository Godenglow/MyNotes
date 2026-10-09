# -*- coding: utf-8 -*-
"""统计：反引号 span 内包含 <font 标签的情况"""
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
                spans.append((i, n, 'unclosed'))
                break
            spans.append((i, k + (j - i), 'ok'))
            i = k + (j - i)
        else:
            i += 1
    return spans


total = 0
samples = []
per_file = Counter()
for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    in_fence = False
    fs_char = None
    fs_len = 0
    for i, line in enumerate(text.split('\n')):
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
        for a, b, kind in backtick_spans(line):
            seg = line[a:b]
            if '<font' in seg:
                total += 1
                per_file[fname] += 1
                if len(samples) < 40:
                    samples.append((fname, i + 1, seg[:150]))

print('反引号内包含 <font 的数量:', total)
print()
print('按文件:')
for f, c in per_file.most_common():
    print(f'  {f}: {c}')
print()
print('样例（前 40）:')
for f, ln, seg in samples:
    print(f'  [{f}] L{ln}: {seg}')

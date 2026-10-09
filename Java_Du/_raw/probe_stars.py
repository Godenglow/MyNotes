# -*- coding: utf-8 -*-
"""分析输出文件中 4+ 连星号的语境形态"""
import re
import glob
import os
from collections import Counter

OUT = r'D:/MyNotes/Du'

pats = Counter()
samples = {}
total = 0

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    for i, line in enumerate(lines):
        for m in re.finditer(r'\*{4,}', line):
            total += 1
            s, e = m.start(), m.end()
            left = line[max(0, s-1):s]
            right = line[e:e+1]
            # 分类：左/右邻字符类型
            def c(ch):
                if ch == '':
                    return 'EDGE'
                if ch.isspace():
                    return 'SPACE'
                if ch == '*':
                    return '*'
                if ch == '`':
                    return '`'
                return 'TEXT'
            key = (len(m.group(0)), c(left), c(right))
            pats[key] += 1
            if key not in samples:
                samples[key] = (fname, i + 1, line[max(0, s-60):e+60])

print('4+ 连星号总数:', total)
print()
print('形态分类 (连数, 左邻, 右邻):')
for k, v in pats.most_common(30):
    print(f'  {k}: {v}')
print()
print('样例:')
for k in pats:
    if k in samples:
        f, ln, ctx = samples[k]
        print(f'  {k} [{f}] L{ln}:')
        print(f'      {ctx[:160]}')

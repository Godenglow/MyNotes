# -*- coding: utf-8 -*-
"""应用星号修复清单到输出文件"""
import json
import os
from collections import defaultdict

FIX = r'D:/MyNotes/Du/_raw/_star_fixes.json'
MANUAL = r'D:/MyNotes/Du/_raw/_star_manual.json'
OUT = r'D:/MyNotes/Du'

with open(FIX, encoding='utf-8') as f:
    fixes = json.load(f)
with open(MANUAL, encoding='utf-8') as f:
    manual = json.load(f)

# manual 4 个假警报（列表行）：采用 norm 版本
for m in manual:
    fixes.append({'file': m['file'], 'ln': m['ln'], 'final': m['norm']})

by_file = defaultdict(list)
for fx in fixes:
    by_file[fx['file']].append((fx['ln'], fx['final']))

total = 0
for fname, items in sorted(by_file.items()):
    fp = os.path.join(OUT, fname)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    for ln, final in items:
        assert 0 < ln <= len(lines), f'{fname} L{ln} 越界'
        lines[ln - 1] = final
        total += 1
    with open(fp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print(f'{fname}: {len(items)} 行已修复')

print('总计修复行数:', total)

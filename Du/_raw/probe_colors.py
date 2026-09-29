# -*- coding: utf-8 -*-
"""统计反引号外 font 的 (color, background) 组合分布"""
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


combos = Counter()

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    in_fence = False
    fs_char = None
    fs_len = 0
    for line in text.split('\n'):
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
        # mask 反引号区间
        spans = backtick_spans(line)
        masked = list(line)
        for a, b in spans:
            for k in range(a, b):
                masked[k] = ' '
        masked = ''.join(masked)
        for fm in re.finditer(r'<font style="([^"]*)"', masked):
            style = fm.group(1)
            cm = re.search(r'color:\s*([^;"]+)', style)
            bm = re.search(r'background-color:\s*([^;"]+)', style)
            color = cm.group(1).strip() if cm else '-'
            bg = bm.group(1).strip() if bm else '-'
            combos[(color, bg)] += 1

print('=== (color, background) 组合 Top 40 ===')
for (c, b), n in combos.most_common(40):
    print(f'  color={c:22s} bg={b:22s} : {n}')
print()
print('总计:', sum(combos.values()))

# 亮暗分类
def parse(v):
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

dark_total = 0
light_total = 0
colorful_total = 0
bg_total = 0
for (c, b), n in combos.items():
    rgb = parse(c)
    if rgb:
        mx, mn = max(rgb), min(rgb)
        if mx < 128 and (mx - mn) < 40:
            dark_total += n
        elif (mx - mn) < 40:
            light_total += n
        else:
            colorful_total += n
    if b != '-':
        bg_total += n

print()
print('分类统计（按 color）:')
print('  深色系(近黑/暗灰):', dark_total)
print('  浅灰色系:', light_total)
print('  彩色(有色相):', colorful_total)
print('  带 background 的:', bg_total)

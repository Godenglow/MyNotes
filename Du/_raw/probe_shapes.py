# -*- coding: utf-8 -*-
"""统计反引号内 font 的形态变体 + 反引号外 font 颜色分布"""
import re
import glob
import os
from collections import Counter

OUT = r'D:/MyNotes/Du'
BT = chr(96)
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
FONT_RE = re.compile(r'</?font\b[^<>]*>')


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


# ---- 反引号内 font span 形态 ----
shapes = Counter()
samples = {}
total_span = 0
color_outside = Counter()

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
        spans = backtick_spans(line)
        for a, b in spans:
            seg = line[a:b]
            if '<font' not in seg:
                continue
            total_span += 1
            # 去掉 delimiters
            dl = 0
            while a + dl < b and line[a + dl] == BT:
                dl += 1
            inner = line[a + dl: b - dl]
            n_font = len(FONT_RE.findall(inner))
            n_star = inner.count('**')
            st = None
            if n_star == 0:
                st = 'no-star'
            elif inner.startswith('**') and inner.endswith('**') and inner.count('**') == 2:
                st = 'stars-both-ends'
            elif inner.count('**') == 2 and not inner.startswith('**') and not inner.endswith('**'):
                st = 'stars-middle'
            elif inner.startswith('**') and inner.count('**') == 1:
                st = 'star-start-only'
            elif inner.endswith('**') and inner.count('**') == 1:
                st = 'star-end-only'
            else:
                st = f'other({n_star}stars)'
            key = (st, n_font)
            shapes[key] += 1
            if key not in samples:
                samples[key] = (fname, i + 1, seg[:160])

        # 反引号外的 font 颜色
        masked = list(line)
        for a, b in spans:
            for k in range(a, b):
                masked[k] = ' '
        masked = ''.join(masked)
        for fm in re.finditer(r'<font style="([^"]*)"', masked):
            style = fm.group(1)
            cm = re.search(r'color:\s*([^;"]+)', style)
            color_outside[cm.group(1) if cm else '(no-color)'] += 1

print('=== 反引号内 font span 总数:', total_span, '===')
print()
print('形态统计 (star-pattern, font-count):')
for k, c in shapes.most_common(30):
    print(f'  {k}: {c}')
print()
print('样例:')
for k, (fname, ln, seg) in sorted(samples.items(), key=lambda x: -shapes[x[0]])[:25]:
    print(f'  {k} [{fname}] L{ln}:')
    print(f'      {seg}')
print()
print('=== 反引号外 font 颜色 Top 25 ===')
for col, c in color_outside.most_common(25):
    print(f'  {col}: {c}')

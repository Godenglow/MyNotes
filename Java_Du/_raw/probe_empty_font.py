# -*- coding: utf-8 -*-
"""统计空 font 对（<font ...></font> 无内容）的形态与颜色分类"""
import re
import glob
import os
from collections import Counter

OUT = r'D:/MyNotes/Du'
BT = chr(96)
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
FONT_OPEN_RE = re.compile(r'<font\s+style="([^"]*)"[^<>]*>')
COMMENT_RE = re.compile(r'<!--[\s\S]*?-->')


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


def parse_color(v):
    v = v.strip()
    m = re.match(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', v)
    if m:
        return tuple(int(x) for x in m.groups())
    m = re.match(r'#([0-9a-fA-F]{6})$', v)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return None


def is_bg_light(style):
    m = re.search(r'background-color:\s*([^;"]+)', style)
    if not m:
        return False
    rgb = parse_color(m.group(1))
    return rgb is not None and min(rgb) > 200


def is_dark(style):
    m = re.search(r'(?<!background-)color:\s*([^;"]+)', style)
    if not m:
        return False
    rgb = parse_color(m.group(1))
    if not rgb:
        return False
    mx, mn = max(rgb), min(rgb)
    return mx < 128 and (mx - mn) < 40


same_line_empty = 0
cross_line_empty = 0
classif = Counter()
samples = []

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    in_fence = False
    fs_char = None
    fs_len = 0
    stack = []
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
        cspans = [(cm.start(), cm.end()) for cm in COMMENT_RE.finditer(line)]

        def in_mask(pos):
            return (any(a <= pos < b for a, b in spans)
                    or any(a <= pos < b for a, b in cspans))

        events = []
        for m2 in FONT_OPEN_RE.finditer(line):
            if in_mask(m2.start()):
                continue
            events.append(('open', m2.start(), m2.end(), m2.group(1)))
        for m2 in re.finditer(re.escape('</font>'), line):
            if in_mask(m2.start()):
                continue
            events.append(('close', m2.start(), m2.end(), None))
        events.sort(key=lambda x: x[1])
        for kind, s, e, style in events:
            if kind == 'open':
                stack.append((i, s, e, style))
            else:
                if not stack:
                    continue
                i0, s0, e0, st0 = stack.pop()
                # 空内容判定
                if i0 == i and e0 == s:
                    same_line_empty += 1
                    c = 'bg_light' if is_bg_light(st0) else ('dark' if is_dark(st0) else 'color')
                    classif[c] += 1
                    if len(samples) < 10:
                        samples.append((fname, i + 1, c, st0))
                else:
                    # 检查跨行情况是否中间无内容
                    if i0 != i and all(lines[k].strip() == '' for k in range(i0 + 1, i)):
                        cross_line_empty += 1
                        c = 'bg_light' if is_bg_light(st0) else ('dark' if is_dark(st0) else 'color')
                        classif['cross_' + c] += 1

print('同行紧邻空 font 对:', same_line_empty, dict(classif))
print('跨行空 font 对:', cross_line_empty)
print()
for f, ln, c, st in samples:
    print(f'  [{f}] L{ln} [{c}]: {st[:90]}')

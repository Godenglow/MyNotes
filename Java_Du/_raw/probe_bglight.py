# -*- coding: utf-8 -*-
"""抽查浅底 font 与跨行分布"""
import re
import glob
import os

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
    bm = re.search(r'background-color:\s*([^;"]+)', style)
    if not bm:
        return False
    brgb = parse_color(bm.group(1).strip())
    return brgb is not None and min(brgb) > 200


samples = []
cross_line = 0
same_line = 0
inner_bt = 0
inner_star = 0

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    in_fence = False
    fs_char = None
    fs_len = 0
    stack = []  # (line_no, kind_bglight)
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
        mask = list(line)
        for a, b in backtick_spans(line):
            for k in range(a, b):
                mask[k] = ' '
        for cmm in COMMENT_RE.finditer(line):
            for k in range(cmm.start(), cmm.end()):
                mask[k] = ' '
        masked = ''.join(mask)
        events = []
        for m2 in FONT_OPEN_RE.finditer(masked):
            events.append((m2.start(), m2.end(), 'open', is_bg_light(m2.group(1)), m2.group(1)))
        for m2 in re.finditer(re.escape('</font>'), masked):
            events.append((m2.start(), m2.end(), 'close', None, None))
        events.sort()
        for s, e, kind, bglight, style in events:
            if kind == 'open':
                stack.append((i + 1, bglight, s, e, line))
            else:
                if stack:
                    ln, bg, os_, oe, oline = stack.pop()
                    if bg:
                        inner = oline[oe: line.find('</font>', s)] if ln == i + 1 else None
                        if ln == i + 1:
                            same_line += 1
                            content = oline[oe:s]
                            if BT in content:
                                inner_bt += 1
                            if '**' in content:
                                inner_star += 1
                            if len(samples) < 15:
                                samples.append((fname, ln, content[:100]))
                        else:
                            cross_line += 1
                            if len(samples) > 0 and cross_line <= 5:
                                samples.append((fname, f'@{ln}-{i+1}', f'CROSSLINE: {oline[oe:oe+80]}'))
                    # else dark/color 不管

print('浅底 font 对: same-line =', same_line, '| cross-line =', cross_line)
print('内容含反引号:', inner_bt, '| 内容含 **:', inner_star)
print()
print('样例:')
for f, ln, c in samples:
    print(f'  [{f}] L{ln}: {c}')

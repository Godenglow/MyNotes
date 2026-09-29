# -*- coding: utf-8 -*-
"""文档级 font 配对分析：配对性、嵌套、颜色分类统计（跳过代码块）"""
import re
import glob
import os
from collections import Counter

OUT = r'D:/MyNotes/Du'
BT = chr(96)
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
FONT_OPEN_RE = re.compile(r'<font\s+style="([^"]*)"[^<>]*>')
FONT_CLOSE = '</font>'
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
    m = re.match(r'#([0-9a-fA-F]{3})$', v)
    if m:
        h = m.group(1)
        return tuple(int(c * 2, 16) for c in h)
    return None


def classify(style):
    cm = re.search(r'color:\s*([^;"]+)', style)
    bm = re.search(r'background-color:\s*([^;"]+)', style)
    color = cm.group(1).strip() if cm else None
    bg = bm.group(1).strip() if bm else None
    rgb = parse_color(color) if color else None
    info = {'color': color, 'bg': bg, 'dark': False, 'bg_light': False}
    if rgb:
        mx, mn = max(rgb), min(rgb)
        if mx < 128 and (mx - mn) < 40:
            info['dark'] = True
    if bg:
        brgb = parse_color(bg)
        if brgb and min(brgb) > 200:  # 浅色底
            info['bg_light'] = True
    return info


stats = Counter()
max_depth = 0
unpaired_open = 0
unpaired_close = 0
depth_samples = []

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    in_fence = False
    fs_char = None
    fs_len = 0
    stack = []
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
        # 掩码区：反引号 + 注释
        mask = list(line)
        for a, b in backtick_spans(line):
            for k in range(a, b):
                mask[k] = ' '
        for cmm in COMMENT_RE.finditer(line):
            for k in range(cmm.start(), cmm.end()):
                mask[k] = ' '
        masked = ''.join(mask)
        # 事件
        events = []
        for m2 in FONT_OPEN_RE.finditer(masked):
            events.append((m2.start(), 'open', classify(m2.group(1)), m2.group(0)))
        for m2 in re.finditer(re.escape(FONT_CLOSE), masked):
            events.append((m2.start(), 'close', None, FONT_CLOSE))
        events.sort()
        for pos, kind, info, raw in events:
            if kind == 'open':
                stack.append(info)
                stats['open'] += 1
                if info['dark']:
                    stats['open_dark'] += 1
                if info['bg_light']:
                    stats['open_bglight'] += 1
                max_depth = max(max_depth, len(stack))
            else:
                if stack:
                    op = stack.pop()
                    stats['paired'] += 1
                    if op['dark']:
                        stats['paired_dark'] += 1
                    if op['bg_light']:
                        stats['paired_bglight'] += 1
                else:
                    unpaired_close += 1
    unpaired_open += len(stack)
    if stack and len(depth_samples) < 10:
        depth_samples.append((fname, len(stack)))

print('开标签:', stats['open'], '| 配对成功:', stats['paired'], '| 悬空开:', unpaired_open, '| 悬空闭:', unpaired_close)
print('开标签中: dark =', stats['open_dark'], '| bg_light =', stats['open_bglight'])
print('配对中对: dark =', stats['paired_dark'], '| bg_light =', stats['paired_bglight'])
print('最大嵌套深度:', max_depth)
print('文件尾残留栈样例:', depth_samples)

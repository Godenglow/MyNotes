# -*- coding: utf-8 -*-
"""验证输出文件：扫描残留裸标签（应只有 font/br//白名单成对样式）"""
import re
import glob
import os
from collections import Counter, defaultdict

OUT = r'D:/MyNotes/Du'
BT = chr(96)

TAG_RE = re.compile(r'</?([a-zA-Z][a-zA-Z0-9:._-]*)((?:\s[^<>]*)?)/?>')
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
STYLE_TAGS = {'sup', 'sub', 'u', 'del', 'ins', 'em', 'i', 'b', 'strong',
              'small', 'mark', 's', 'big', 'kbd', 'var', 'cite', 'abbr',
              'dfn', 'time', 'q'}


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


residual = []          # 非预期残留（需要为 0）
expected_kept = 0      # 白名单成对样式
font_cnt = 0
br_cnt = 0
comment_residual = 0

for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')
    in_fence = False
    fs_char = None
    fs_len = 0
    for i, line in enumerate(lines):
        if in_fence:
            if re.match(r'^\s{0,3}' + re.escape(fs_char) + '{' + str(fs_len) + r',}\s*$', line):
                in_fence = False
                fs_char = None
            continue
        m = FENCE_RE.match(line)
        if m:
            in_fence = True
            fs_char = m.group(2)[0]
            fs_len = len(m.group(2))
            continue
        # 残留 HTML 注释检查
        if '<!--' in line:
            # 检查是否在反引号内
            spans = backtick_spans(line)
            for cm in re.finditer(r'<!--', line):
                if not any(a <= cm.start() < b for a, b in spans):
                    comment_residual += 1
                    residual.append((fname, i + 1, 'COMMENT', line.strip()[:100]))
        spans = backtick_spans(line)
        events = []
        for tm in TAG_RE.finditer(line):
            if any(a <= tm.start() < b for a, b in spans):
                continue
            raw = tm.group(0)
            name = tm.group(1).lower()
            events.append((tm.start(), tm.end(), name, raw.startswith('</'), raw))
        # 配对白名单
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
            s, e, name, is_close, raw = ev
            if name == 'font':
                font_cnt += 1
                continue
            if raw in ('<br/>', '<br />'):
                br_cnt += 1
                continue
            if s in keep:
                expected_kept += 1
                continue
            residual.append((fname, i + 1, name, line.strip()[:120]))

print('=== 残留非预期裸标签:', len(residual), '===')
for fname, ln, name, ctx in residual[:80]:
    print(f'  [{fname}] L{ln} <{name}> || {ctx}')
print()
print('预期保留: 白名单成对样式 =', expected_kept, '| font =', font_cnt, '| br/ =', br_cnt)
print('注释残留:', comment_residual)

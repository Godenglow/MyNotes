# -*- coding: utf-8 -*-
"""最终综合验证 v2"""
import re
import glob
import os
from collections import Counter

OUT = r'D:/MyNotes/Du'
BT = chr(96)
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
TAG_RE = re.compile(r'</?([a-zA-Z][a-zA-Z0-9:._-]*)((?:\s[^<>]*)?)/?>')
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


issues = []
bt_font = 0          # 反引号内残留 font（应为 0）
outside_font_colors = Counter()
residual_tags = []
comment_residual = 0

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
        # 1) 反引号内 font 残留
        for a, b in spans:
            if '<font' in line[a:b]:
                bt_font += 1
                if bt_font <= 5:
                    issues.append(f'[{fname}] L{i+1} 反引号内 font 残留: {line[a:b][:100]}')
        # 2) 反引号外 font 颜色
        mask = list(line)
        for a, b in spans:
            for k in range(a, b):
                mask[k] = ' '
        masked = ''.join(mask)
        for fm in re.finditer(r'<font\s+style="([^"]*)"', masked):
            cm2 = re.search(r'(?<!background-)color:\s*([^;"]+)', fm.group(1))
            outside_font_colors[cm2.group(1).strip() if cm2 else '-'] += 1
        # 3) 注释残留
        for cm in re.finditer(r'<!--', line):
            if not any(a <= cm.start() < b for a, b in spans):
                comment_residual += 1
                issues.append(f'[{fname}] L{i+1} 注释残留: {line[:80]}')
        # 4) 裸标签残留
        comment_spans = [(cm.start(), cm.end()) for cm in re.finditer(r'<!--[\s\S]*?-->', line)]
        events = []
        for tm in TAG_RE.finditer(line):
            if any(a <= tm.start() < b for a, b in spans):
                continue
            if any(a <= tm.start() < b for a, b in comment_spans):
                continue
            raw = tm.group(0)
            events.append((tm.start(), tm.end(), tm.group(1).lower(), raw.startswith('</'), raw))
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
                continue
            if raw in ('<br/>', '<br />'):
                continue
            if s in keep:
                continue
            residual_tags.append((fname, i + 1, raw, line[:100]))

print('1. 反引号内 font 残留:', bt_font)
print()
print('2. 反引号外 font 颜色分布:')
for c, n in outside_font_colors.most_common(30):
    print(f'   {c}: {n}')
print('   合计:', sum(outside_font_colors.values()))
print()
print('3. 注释残留:', comment_residual)
print('4. 非预期裸标签残留:', len(residual_tags))
for f, ln, raw, ctx in residual_tags[:20]:
    print(f'   [{f}] L{ln}: {raw} || {ctx}')
print()
print('5. 其它 issue:')
for x in issues[:10]:
    print('   ', x)
if not issues:
    print('    （无）')

# 6. 抽查关键样本行
print()
print('6. 关键样本抽查:')
samples = [
    ('04-Web前端.md', 'head>标签'),
    ('01-JavaSE.md', 'iterator();'),
    ('08-Maven.md', '配置站点部署'),
    ('01-JavaSE.md', 'Bean的循环依赖'),
    ('01-JavaSE.md', '²'),
]
for fname, key in samples:
    fp = os.path.join(OUT, fname)
    with open(fp, encoding='utf-8') as f:
        for ln_no, line in enumerate(f, 1):
            if key in line:
                print(f'   [{fname}] L{ln_no}: {line.strip()[:150]}')
                break

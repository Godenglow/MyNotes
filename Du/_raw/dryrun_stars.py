# -*- coding: utf-8 -*-
"""dry-run：对全部输出文件的 4+ 连星做规范化预演，导出 JSON 供 Node 渲染验证"""
import re
import glob
import os
import json

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


def normalize_line(line, stats):
    spans = backtick_spans(line)
    changes = []
    for m in re.finditer(r'\*{4,}', line):
        if any(a <= m.start() < b for a, b in spans):
            continue
        s, e = m.start(), m.end()
        left = line[s - 1] if s > 0 else None
        right = line[e] if e < len(line) else None
        lsp = (left is None) or left.isspace()
        rsp = (right is None) or right.isspace()
        if lsp and rsp:
            action = 'idle'
            rep = m.group(0)
        elif not lsp and not rsp:
            action = 'mid'
            rep = ''
        else:
            action = 'open' if lsp else 'close'
            rep = '**'
        stats[action] += 1
        changes.append((s, e, rep))
    if not changes:
        return line
    for s, e, rep in sorted(changes, key=lambda x: -x[0]):
        line = line[:s] + rep + line[e:]
    return line


lines_out = []
stats = {'open': 0, 'close': 0, 'mid': 0, 'idle': 0}
for fp in sorted(glob.glob(os.path.join(OUT, '*.md'))):
    fname = os.path.basename(fp)
    with open(fp, encoding='utf-8') as f:
        lines = f.read().split('\n')
    in_fence = False
    fs_char = None
    fs_len = 0
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
        if re.search(r'\*{4,}', line):
            norm = normalize_line(line, stats)
            lines_out.append({'file': fname, 'ln': i + 1, 'orig': line, 'norm': norm,
                              'changed': norm != line})

with open(os.path.join(OUT, '_raw', '_star_dryrun.json'), 'w', encoding='utf-8') as f:
    json.dump(lines_out, f, ensure_ascii=False)

print('含 4+ 星的行数:', len(lines_out))
print('规则命中:', stats)
print('会改变的行数:', sum(1 for x in lines_out if x['changed']))

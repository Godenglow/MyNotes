# -*- coding: utf-8 -*-
"""探查 Vue3 L7757 反引号结构"""
import json

BT = chr(96)  # 反引号

with open(r'D:/MyNotes/Du/_raw/vu082c.json', encoding='utf-8') as f:
    sc = json.load(f)['data']['sourcecode']
line = sc.split('\n')[7756]
print('FULL L7757:')
print(repr(line))
print()
print('反引号位置:', [i for i, c in enumerate(line) if c == BT])
print('长度:', len(line))
print()

# 模拟解析
spans = []
i = 0
n = len(line)
while i < n:
    if line[i] == BT:
        j = i
        while j < n and line[j] == BT:
            j += 1
        k = line.find(BT * (j - i), j)
        if k == -1:
            spans.append((i, n, 'unclosed'))
            break
        spans.append((i, k + (j - i), 'ok'))
        i = k + (j - i)
    else:
        i += 1
print('解析出的 span:', spans)
for a, b, kind in spans:
    print(f'  span [{a}:{b}] ({kind}): {line[a:b][:120]!r}')

# <Suspense> 位置
pos = line.find('<Suspense>')
print()
print('<Suspense> 位置:', pos)
for a, b, kind in spans:
    if a <= pos < b:
        print('=> 在 span 内（视作代码，不处理）')
        break
else:
    print('=> 在 span 外（会被处理）')

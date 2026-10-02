# -*- coding: utf-8 -*-
"""检查 vivo 健康 HTML 结构"""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = sys.argv[1]
html = open(path, encoding='utf-8').read()
print('FILE:', path, 'len:', len(html))

# 按顺序输出结构大纲
for m in re.finditer(r'<h([123])[^>]*>(.*?)</h\1>|<div class="firstline">(.*?)</div>|<div class="card">(.*?)</div>|<div class="box ([^"]*)">(.*?)</div>|<div class="chart">(.*?)</svg></div>|<table>(.*?)</table>|<div class="foot">(.*?)</div>|<div class="meta">(.*?)</div>', html, re.S):
    if m.group(1):
        t = re.sub(r'<[^>]+>', '', m.group(2))
        print(f'H{m.group(1)}: {t.strip()}')
    elif m.group(3) is not None:
        print('FIRSTLINE:', m.group(3))
    elif m.group(4) is not None:
        k = re.search(r'<div class="k">(.*?)</div>', m.group(4))
        v = re.search(r'<div class="v"[^>]*>(.*?)</div>', m.group(4))
        d = re.search(r'<div class="d">(.*?)</div>', m.group(4))
        print(f'  CARD: {k.group(1) if k else "?"} = {v.group(1) if v else "?"} | {d.group(1) if d else ""}')
    elif m.group(5) is not None:
        t = re.sub(r'<[^>]+>', ' ', m.group(6))
        print(f'  BOX[{m.group(5)}]:', re.sub(r'\s+', ' ', t).strip()[:150])
    elif m.group(7) is not None:
        texts = re.findall(r'<text[^>]*>([^<]*)</text>', m.group(7))
        print('  CHART texts:', texts[:20])
    elif m.group(8) is not None:
        rows = re.findall(r'<tr>(.*?)</tr>', m.group(8), re.S)
        print(f'  TABLE: {len(rows)} rows')
        for r in rows[:3]:
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, re.S)
            print('    ', [re.sub(r'<[^>]+>', '', c).strip() for c in cells])
    elif m.group(9) is not None:
        print('FOOT:', re.sub(r'<[^>]+>', ' ', m.group(9)).strip()[:200])
    elif m.group(10) is not None:
        print('META:', re.sub(r'<br\s*/?>', ' | ', m.group(10)))

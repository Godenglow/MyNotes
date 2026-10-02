# -*- coding: utf-8 -*-
import re, io
from collections import Counter
for f in ['说明文件.html', 'vivo健康数据分析报告.html']:
    raw = io.open('D:/Private-Note/vivo健康/' + f, encoding='utf-8').read()
    bm = re.search(r'<body[^>]*>', raw)
    body = raw[bm.end():raw.index('</body>')]
    toks = re.findall(
        r'<div class="(firstline|hd|cards|chart|box [a-z-]+|foot)"'
        r'|<h1[^>]*>|<h2[^>]*>|<h3[^>]*>|<table[^>]*>|<pre[^>]*>|<p>|<ul[^>]*>|<ol[^>]*>|<svg[^>]*>',
        body)
    c = Counter(t if t else 'DIV-NOGROUP' for t in toks)
    print(f, dict(c), 'len', len(body))
    # 看看 body 前 500 字符
    print(body[:400].replace('\n', ' ')[:400])
    print('---')

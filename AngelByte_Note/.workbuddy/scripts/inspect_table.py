"""Inspect PPTX slides for the table-like content the user flagged."""
import re
import zipfile
from pathlib import Path

pptx = Path(r'D:\BaiduNetdiskDownload\document\03-第二章 Java基础语法.pptx')

with zipfile.ZipFile(pptx) as z:
    slide_names = sorted(
        [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)],
        key=lambda n: int(re.search(r'(\d+)', n).group(1)),
    )
    for name in slide_names:
        xml = z.open(name).read().decode('utf-8')
        texts = re.findall(r'<a:t[^>]*>(.*?)</a:t>', xml, re.S)
        cleaned = [re.sub(r'<[^>]+>', '', t).strip() for t in texts]
        cleaned = [t.replace('&quot;', '"').replace('&amp;', '&')
                       .replace('&lt;', '<').replace('&gt;', '>')
                   for t in cleaned if t.strip()]
        joined = ' '.join(cleaned)
        # find the slides with table data (姓名/年龄) and code (short s = 100)
        if ('姓名' in joined and '年龄' in joined) or '浮点型数据两种表示' in joined:
            print(f'== {name} ==')
            for t in cleaned:
                print(f'  | {t!r}')
            print()
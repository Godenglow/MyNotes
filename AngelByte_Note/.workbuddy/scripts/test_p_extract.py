"""Test how extracting per <a:p> paragraph looks vs per <a:t>."""
import re
import zipfile
from pathlib import Path

pptx = Path(r'D:\BaiduNetdiskDownload\document\03-第二章 Java基础语法.pptx')

PARA_RE = re.compile(r'<a:p\b[^>]*>(.*?)</a:p>', re.S)
TEXT_RE = re.compile(r'<a:t[^>]*>(.*?)</a:t>', re.S)
INLINE_RE = re.compile(r'<[^>]+>')
ENTITIES = {'&quot;': '"', '&apos;': "'", '&amp;': '&', '&lt;': '<', '&gt;': '>', '&nbsp;': ' '}
ENT_RE = re.compile(r'&(?:quot|apos|amp|lt|gt|nbsp);')


def per_p_extraction(xml: str) -> list[str]:
    out = []
    for m in PARA_RE.finditer(xml):
        para = m.group(1)
        texts = TEXT_RE.findall(para)
        cells = []
        for t in texts:
            t = INLINE_RE.sub('', t)
            t = ENT_RE.sub(lambda m: ENTITIES[m.group(0)], t).strip()
            if t:
                cells.append(t)
        if cells:
            out.append('\t'.join(cells))
    return out


def per_t_extraction(xml: str) -> list[str]:
    out = []
    for m in TEXT_RE.finditer(xml):
        t = INLINE_RE.sub('', m.group(1))
        t = ENT_RE.sub(lambda m: ENTITIES[m.group(0)], t).strip()
        if t:
            out.append(t)
    return out


# show slides 10 (basic info), 33 (table-like), 46 (作业题table)
with zipfile.ZipFile(pptx) as z:
    for n in ['ppt/slides/slide10.xml', 'ppt/slides/slide33.xml', 'ppt/slides/slide46.xml']:
        xml = z.open(n).read().decode('utf-8')
        print(f'== {n} ==')
        p_lines = per_p_extraction(xml)
        t_lines = per_t_extraction(xml)
        print(f'  per-<a:p>: {len(p_lines)} lines')
        for line in p_lines[:15]:
            print(f'    P| {line!r}')
        print(f'  per-<a:t>: {len(t_lines)} frags')
        for line in t_lines[:15]:
            print(f'    T| {line!r}')
        print()
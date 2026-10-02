#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""vivo 健康 2026 HTML → Notion Markdown 转换器（基于 2025 版改造，兼容根级文件）"""
import re, html, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SRC = Path("D:/Private-Note/vivo健康/2026")
OUT = Path("D:/MyNotes/.vivo_mig_tmp/2026_out")
ROOT_FILES = ["说明文件.html", "vivo健康数据分析报告.html"]
ROOT_OUT = Path("D:/MyNotes/.vivo_mig_tmp/2026_root_out")
ESCAPE = set('\\*~`$[]<>{}|^')

def esc(t):
    return ''.join('\\' + c if c in ESCAPE else c for c in t)

def detag(s):
    """去标签 + 折叠空白（box 内多行 p 需折叠为单行）"""
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()

def find_balanced(s, start):
    """s[start:] 以 <div 开头，返回匹配 </div> 之后的索引"""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            return start + m.end()
    return len(s)

def conv_cards(block):
    rows = ['<table fit-page-width="true" header-row="true">',
            '<tr><th>指标</th><th>数值</th><th>说明</th></tr>']
    for p in re.split(r'<div class="card"[^>]*>', block)[1:]:
        k = re.search(r'<div class="k"[^>]*>(.*?)</div>', p, re.S)
        v = re.search(r'<div class="v"[^>]*>(.*?)</div>', p, re.S)
        d = re.search(r'<div class="d"[^>]*>(.*?)</div>', p, re.S)
        cells = [detag(k.group(1)) if k else '',
                 detag(v.group(1)) if v else '',
                 detag(d.group(1)) if d else '']
        rows.append('<tr>' + ''.join(f'<td>{esc(x)}</td>' for x in cells) + '</tr>')
    rows.append('</table>')
    return '\n'.join(rows)

def conv_table(tbl):
    lines = ['<table fit-page-width="true" header-row="true">']
    for rm in re.finditer(r'<tr[^>]*>(.*?)</tr>', tbl, re.S):
        cells = re.findall(r'<t([hd])[^>]*>(.*?)</t\1>', rm.group(1), re.S)
        lines.append('<tr>' + ''.join(f'<t{tag}>{esc(detag(c))}</t{tag}>'
                                      for tag, c in cells) + '</tr>')
    lines.append('</table>')
    return '\n'.join(lines)

def conv_chart(block, has_table_after):
    svg = block
    if '<text' not in svg:
        return ''
    tm = re.search(r'<text[^>]*>([^<]*)</text>', svg)
    title = html.unescape(tm.group(1)).strip() if tm else '图表'
    legend = []
    dates, vals = [], []
    for m in re.finditer(r'<text ([^>]*)>([^<]*)</text>', svg):
        attrs = m.group(1)
        content = html.unescape(m.group(2)).strip()
        if re.fullmatch(r'.+?\(\d+-\d+\) ?\d+%', content):
            legend.append(content)
        am = re.search(r'text-anchor="(\w+)"', attrs)
        if am and am.group(1) == 'middle':
            if re.fullmatch(r'周. ?\d+/\d+', content):
                dates.append(content)
            elif re.fullmatch(r'[\d,]+(\.\d+)?', content) and content not in ('0',):
                vals.append(content)
    out = []
    if '走势' in title or '趋势' in title or '时间序列' in title:
        out.append(f'> 图表「{esc(title)}」为 SVG 折线图，无法原生迁移；每日数值详见对应周页/明细表。')
        return '\n'.join(out)
    if '时段分布' in title or legend:
        out.append(f'**{esc(title)}**')
        lt = ['<table fit-page-width="true" header-row="true">',
              '<tr><th>时段</th><th>步数占比</th></tr>']
        for item in legend:
            mm = re.fullmatch(r'(.+?\(\d+-\d+\)) ?(\d+)%', item)
            if mm:
                lt.append(f'<tr><td>{esc(mm.group(1))}</td><td>{mm.group(2)}%</td></tr>')
        lt.append('</table>')
        out.append('\n'.join(lt))
        return '\n'.join(out)
    if dates and vals and not has_table_after:
        out.append(f'**{esc(title)}**')
        bt = ['<table fit-page-width="true" header-row="true">',
              '<tr><th>日期</th><th>数值</th></tr>']
        for d, v in zip(dates, vals):
            bt.append(f'<tr><td>{esc(d)}</td><td>{esc(v)}</td></tr>')
        bt.append('</table>')
        out.append('\n'.join(bt))
        return '\n'.join(out)
    if dates and vals and has_table_after:
        out.append(f'> 图表「{esc(title)}」数据与下方明细表一致，不再重复。')
        return '\n'.join(out)
    out.append(f'> 图表「{esc(title)}」无法原生迁移，相关数据见明细表格。')
    return '\n'.join(out)

def conv_box(block):
    tm = re.search(r'<div class="t"[^>]*>(.*?)</div>', block, re.S)
    title = detag(tm.group(1)) if tm else ''
    rest = block[tm.end():] if tm else block
    rest = re.sub(r'</div>\s*$', '', rest.strip())
    lines = []
    if title:
        lines.append(f'> **{esc(title)}**')
    seg_pos = 0
    items = []
    for m in re.finditer(r'<ul[^>]*>(.*?)</ul>|<ol[^>]*>(.*?)</ol>|<p[^>]*>(.*?)</p>', rest, re.S):
        head = detag(rest[seg_pos:m.start()])
        if head:
            items.append(('p', head))
        if m.group(1) is not None:
            for li in re.findall(r'<li[^>]*>(.*?)</li>', m.group(1), re.S):
                items.append(('ul', detag(li)))
        elif m.group(2) is not None:
            for i, li in enumerate(re.findall(r'<li[^>]*>(.*?)</li>', m.group(2), re.S), 1):
                items.append(('ol', detag(li)))
        else:
            t = detag(m.group(3))
            if t:
                items.append(('p', t))
        seg_pos = m.end()
    tail = detag(rest[seg_pos:])
    if tail:
        items.append(('p', tail))
    for kind, txt in items:
        txt = esc(txt)
        if kind == 'ul':
            lines.append(f'> - {txt}')
        elif kind == 'ol':
            lines.append(f'> 1. {txt}')
        else:
            lines.append(f'> {txt}')
    return '\n'.join(lines) if lines else f'> {esc(detag(rest))}'

def convert(raw, rel):
    """rel: 相对 D:/Private-Note/vivo健康/ 的路径，如 2026/01/月度总结.html"""
    raw = re.sub(r'<style.*?</style>', '', raw, flags=re.S)
    raw = re.sub(r'<script.*?</script>', '', raw, flags=re.S)
    bm = re.search(r'<body[^>]*>', raw)
    body = raw[bm.end(): raw.index('</body>')]
    out = []
    pos = 0
    block_re = re.compile(
        r'<div class="(firstline|hd|cards|chart|box [^"]*|foot)"|<h2[^>]*>|<h3[^>]*>|<table[^>]*>|<pre[^>]*>|<p>|<ul[^>]*>|<ol[^>]*>'
    )
    while pos < len(body):
        m = block_re.search(body, pos)
        if not m:
            break
        tok = m.group(0)
        if tok.startswith('<div class="firstline"'):
            end = find_balanced(body, m.start())
            out.append(f"**{esc(detag(body[m.start():end]))}**\n")
        elif tok.startswith('<div class="hd"'):
            end = find_balanced(body, m.start())
            blk = body[m.start():end]
            sub = re.search(r'<div class="sub"[^>]*>(.*?)</div>', blk, re.S)
            if sub:
                out.append(esc(detag(sub.group(1))) + '\n')
            meta = re.search(r'<div class="meta"[^>]*>(.*?)</div></div>', blk, re.S)
            if meta:
                txt = html.unescape(re.sub(r'<br\s*/?>', ' · ', meta.group(1)))
                out.append(esc(detag(txt)) + '\n')
        elif tok.startswith('<div class="cards"'):
            end = find_balanced(body, m.start())
            out.append(conv_cards(body[m.start():end]) + '\n')
        elif tok.startswith('<div class="chart"'):
            end = find_balanced(body, m.start())
            after = body[end:]
            has_table = bool(re.match(r'\s*(<h3[^>]*>.*?</h3>\s*)?<table[^>]*>', after, re.S))
            out.append(conv_chart(body[m.start():end], has_table) + '\n')
        elif tok.startswith('<div class="box'):
            end = find_balanced(body, m.start())
            out.append(conv_box(body[m.start():end]) + '\n')
        elif tok.startswith('<div class="foot"'):
            end = find_balanced(body, m.start())
            out.append('---\n')
            out.append('> ' + esc(detag(body[m.start():end])))
            out.append('')
            out.append(f'源文件：D:/Private-Note/vivo健康/{rel} · 迁移自 WorkBuddy · 2026-10-03')
        elif tok.startswith('<h2'):
            end = body.index('</h2>', m.start())
            inner = body[m.end():end]
            hm = re.match(r'(?:<span class="n"[^>]*>(.*?)</span>)?(.*)', inner, re.S)
            n, t = detag(hm.group(1) or ''), detag(hm.group(2) or '')
            out.append(f'## {n + " " if n else ""}{esc(t)}\n')
        elif tok.startswith('<h3'):
            end = body.index('</h3>', m.start())
            out.append('### ' + esc(detag(body[m.end():end])) + '\n')
        elif tok.startswith('<table'):
            end = body.index('</table>', m.start()) + 8
            out.append(conv_table(body[m.start():end]) + '\n')
        elif tok.startswith('<pre'):
            end = body.index('</pre>', m.start()) + 6
            inner = body[m.start():end]
            inner = re.sub(r'^<pre[^>]*>', '', inner)
            inner = re.sub(r'</pre>$', '', inner.strip())
            code = html.unescape(re.sub(r'<[^>]+>', '', inner))
            out.append('```\n' + code.rstrip() + '\n```\n')
        elif tok == '<p>':
            end = body.index('</p>', m.start()) + 4
            t = esc(detag(body[m.start() + 3:end - 4]))
            if t:
                out.append(t + '\n')
        elif tok.startswith('<ul'):
            end = body.index('</ul>', m.start()) + 5
            for li in re.findall(r'<li[^>]*>(.*?)</li>', body[m.start():end], re.S):
                t = esc(detag(li))
                if t:
                    out.append(f'- {t}')
            out.append('')
        elif tok.startswith('<ol'):
            end = body.index('</ol>', m.start()) + 5
            for i, li in enumerate(re.findall(r'<li[^>]*>(.*?)</li>', body[m.start():end], re.S), 1):
                t = esc(detag(li))
                if t:
                    out.append(f'{i}. {t}')
            out.append('')
        pos = end
    return '\n'.join(out)

def main():
    OUT.mkdir(exist_ok=True)
    ROOT_OUT.mkdir(exist_ok=True)
    total = 0
    for month in sorted(p.name for p in SRC.iterdir() if p.is_dir()):
        for fp in sorted((SRC / month).glob('*.html')):
            raw = fp.read_text(encoding='utf-8')
            md = convert(raw, f'2026/{month}/{fp.name}')
            name = fp.stem
            (OUT / f'{month}_{name}.md').write_text(md, encoding='utf-8')
            total += 1
            print(f'OK 2026/{month}/{fp.name} -> {len(md)} chars')
    for name in ROOT_FILES:
        fp = Path("D:/Private-Note/vivo健康") / name
        raw = fp.read_text(encoding='utf-8')
        md = convert(raw, name)
        (ROOT_OUT / (fp.stem + '.md')).write_text(md, encoding='utf-8')
        total += 1
        print(f'OK (root)/{name} -> {len(md)} chars')
    print(f'\n共 {total} 个文件')

if __name__ == '__main__':
    main()

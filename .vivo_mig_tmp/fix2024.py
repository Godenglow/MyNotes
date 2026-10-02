# -*- coding: utf-8 -*-
"""修正表格格式：<table> 标签独占一行 + 表头 <th>（对齐 ScrePipe 成功格式），并修复 01 月已写入内容"""
import io, os, re, sys, json

sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

OUT = 'D:/MyNotes/.vivo_mig_tmp/2024_out'
CKPT = 'D:/MyNotes/.vivo_mig_tmp/ckpt2024.json'

def fix_md(text):
    out = []
    for line in text.split('\n'):
        m = re.match(r'^<table ([^>]*)>(<tr>.*</tr>)$', line)
        if m:
            header = m.group(2).replace('<td>', '<th>').replace('</td>', '</th>')
            out.append(f'<table {m.group(1)}>')
            out.append(header)
        else:
            out.append(line)
    return '\n'.join(out)

def fix_all():
    for f in sorted(os.listdir(OUT)):
        if not f.endswith('.md'):
            continue
        p = os.path.join(OUT, f)
        t = io.open(p, encoding='utf-8').read()
        t2 = fix_md(t)
        if t2 != t:
            io.open(p, 'w', encoding='utf-8').write(t2)
            print('fixed', f)

def repair_01():
    ck = json.load(io.open(CKPT, encoding='utf-8'))
    MONTH01 = '3ed68f11-3d2d-8198-be2b-e61856bc85d3'
    info = ck['01']
    md = io.open(os.path.join(OUT, '01_月度总结.md'), encoding='utf-8').read()
    tags = '\n'.join(f'<page url="https://app.notion.com/p/{pid.replace("-", "")}">{title}</page>'
                     for title, pid in info['weeks'].items())
    call('notion-update-page', {'page_id': MONTH01, 'command': 'replace_content',
                                'new_str': md + '\n' + tags})
    print('01 月页 repaired')
    for title, pid in info['weeks'].items():
        md = io.open(os.path.join(OUT, f'01_{title}.md'), encoding='utf-8').read()
        call('notion-update-page', {'page_id': pid, 'command': 'replace_content', 'new_str': md})
        print('01', title, 'repaired', pid)

if __name__ == '__main__':
    fix_all()
    repair_01()

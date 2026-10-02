# -*- coding: utf-8 -*-
"""修复 2025/01 已写入但表格格式错误的页面：replace_content 重写"""
import io, json, os, sys

sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

OUT = 'D:/MyNotes/.vivo_mig_tmp/2025_out'
CKPT = 'D:/MyNotes/.vivo_mig_tmp/ckpt2025.json'

def rd(name):
    return io.open(os.path.join(OUT, name), encoding='utf-8').read()

ck = json.load(io.open(CKPT, encoding='utf-8'))
m = '01'
pid = '3ed68f11-3d2d-810c-b8a3-f8676281e1c8'
md = rd(f'{m}_月度总结.md')
# 保留子周页标签，避免 replace_content 删除子页
tags = '\n'.join(f'<page url="https://app.notion.com/p/{wpid.replace("-", "")}">{t}</page>'
                 for t, wpid in ck[m]['weeks'].items())
md = md + '\n' + tags + '\n'
call('notion-update-page', {'page_id': pid, 'command': 'replace_content', 'new_str': md})
print(m, '月页重写 ok')

for title, wpid in ck[m]['weeks'].items():
    md = rd(f'{m}_{title}.md')
    call('notion-update-page', {'page_id': wpid, 'command': 'replace_content', 'new_str': md})
    print(m, title, '重写 ok')

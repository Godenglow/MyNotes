# -*- coding: utf-8 -*-
"""迁移驱动：Phase A 根级页 / B 月页 / C 周页 / D 日报页"""
import io, json, os, sys, re
from notion_call import call

OUT = 'D:/MyNotes/.tmp_notion_mig/out'
SRC = 'D:/Private-Note/ScrePipe日报'
CKPT = 'D:/MyNotes/.tmp_notion_mig/ckpt.json'

ROOT = '3ed68f113d2d805382abde77bea49c83'
YEAR = '3ed68f11-3d2d-812f-8179-f948b2fc45ac'
M08 = '3ed68f11-3d2d-8179-97ed-dbb95d410e46'
M09 = '3ed68f11-3d2d-8110-a1c6-c800691ffac7'
M10 = '3ed68f11-3d2d-81d6-b1db-efbb06c12bcb'

def rd(rel):
    return io.open(os.path.join(OUT, rel), encoding='utf-8').read()

def load_ckpt():
    if os.path.exists(CKPT):
        return json.load(io.open(CKPT, encoding='utf-8'))
    return {}

def save_ckpt(c):
    io.open(CKPT, 'w', encoding='utf-8').write(json.dumps(c, ensure_ascii=False, indent=1))

def parse_created(txt):
    """从 create-pages 返回文本解析新页 id 列表（按顺序）"""
    ids = re.findall(r'app\.notion\.com/p/([0-9a-f]{32})', txt)
    seen = []
    for i in ids:
        if i not in seen:
            seen.append(i)
    return seen

WEEKS = [
    # (rel_week_dir, parent_month, title)
    ('2026/08/第4周(08.24-08.30)', M08, '第4周(08.24-08.30)'),
    ('2026/09/第1周(08.31-09.06)', M09, '第1周(08.31-09.06)'),
    ('2026/09/第2周(09.07-09.13)', M09, '第2周(09.07-09.13)'),
    ('2026/09/第3周(09.14-09.20)', M09, '第3周(09.14-09.20)'),
    ('2026/09/第4周(09.21-09.27)', M09, '第4周(09.21-09.27)'),
    ('2026/10/第1周(09.28-10.04)', M10, '第1周(09.28-10.04)'),
]

def phase_a(ck):
    if ck.get('A'):
        print('A done'); return
    pages = [
        {'properties': {'title': '说明文件'}, 'icon': '📄',
         'content': rd('说明文件.html')},
        {'properties': {'title': 'screenpipe-memories'}, 'icon': '🧠',
         'content': rd('screenpipe-memories.md')},
        {'properties': {'title': '长期记忆-手动维护'}, 'icon': '🧠',
         'content': rd('长期记忆-手动维护.md')},
        {'properties': {'title': '补做清单-2026-10-02'}, 'icon': '📋',
         'content': rd('补做清单-2026-10-02.md')},
    ]
    t = call('notion-create-pages', {'parent': {'type': 'page_id', 'page_id': ROOT}, 'pages': pages})
    ck['A'] = parse_created(t)
    save_ckpt(ck)
    print('A ids:', ck['A'])

def phase_b(ck):
    if ck.get('B'):
        print('B done'); return
    for rel, pid in [('2026/08/月度总结.html', M08), ('2026/09/月度总结.html', M09), ('2026/10/月度总结.html', M10)]:
        txt = call('notion-update-page', {'page_id': pid, 'command': 'replace_content', 'new_str': rd(rel)})
        print('B ok', rel, txt[:120])
    ck['B'] = True
    save_ckpt(ck)

def phase_c(ck):
    if ck.get('C'):
        print('C done'); return
    ck['C'] = {}
    for rel, parent, title in WEEKS:
        content = rd(rel + '/周总结.html')
        t = call('notion-create-pages', {
            'parent': {'type': 'page_id', 'page_id': parent},
            'pages': [{'properties': {'title': title}, 'icon': '🗓', 'content': content}]})
        ids = parse_created(t)
        ck['C'][title] = ids[0] if ids else None
        save_ckpt(ck)
        print('C ok', title, ck['C'][title])

if __name__ == '__main__':
    ck = load_ckpt()
    ph = sys.argv[1] if len(sys.argv) > 1 else 'ABC'
    if 'A' in ph: phase_a(ck)
    if 'B' in ph: phase_b(ck)
    if 'C' in ph: phase_c(ck)
    print(json.dumps(ck, ensure_ascii=False, indent=1))

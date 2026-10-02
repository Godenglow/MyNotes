# -*- coding: utf-8 -*-
"""vivo健康 2025 迁移驱动：月页 replace_content + 周页批量 create-pages"""
import io, json, os, re, sys

sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

OUT = 'D:/MyNotes/.vivo_mig_tmp/2025_out'
CKPT = 'D:/MyNotes/.vivo_mig_tmp/ckpt2025.json'

MONTHS = {
    '01': '3ed68f11-3d2d-810c-b8a3-f8676281e1c8',
    '02': '3ed68f11-3d2d-81ae-bfb8-d01d50960f5f',
    '03': '3ed68f11-3d2d-8120-bddc-fa40b524177a',
    '04': '3ed68f11-3d2d-81cb-bfb2-eda1082b1f59',
    '05': '3ed68f11-3d2d-810f-9b6c-cc75d2fec253',
    '06': '3ed68f11-3d2d-815c-9d0d-d7cd72b145d0',
    '07': '3ed68f11-3d2d-81bc-8042-dbac74d0d1cb',
    '08': '3ed68f11-3d2d-815e-8b2a-c1af07a9527a',
    '09': '3ed68f11-3d2d-8186-8681-f0466f067323',
    '10': '3ed68f11-3d2d-8168-800a-c09e83a5633b',
    '11': '3ed68f11-3d2d-8185-8a59-e3230ddc8117',
    '12': '3ed68f11-3d2d-81c7-9f5c-f29f13a7e740',
}

def rd(name):
    return io.open(os.path.join(OUT, name), encoding='utf-8').read()

def load_ckpt():
    if os.path.exists(CKPT):
        return json.load(io.open(CKPT, encoding='utf-8'))
    return {}

def save_ckpt(c):
    io.open(CKPT, 'w', encoding='utf-8').write(json.dumps(c, ensure_ascii=False, indent=1))

def parse_created(txt):
    ids = re.findall(r'app\.notion\.com/p/([0-9a-f]{32})', txt)
    seen = []
    for i in ids:
        if i not in seen:
            seen.append(i)
    return seen

def month_empty(pid):
    txt = call('notion-fetch', {'id': pid})
    return '<blank-page>' in txt

def run_month(m, pid, ck):
    if ck.get(m):
        print(m, 'done, skip'); return
    ck[m] = {'month': False, 'weeks': {}}
    # 1. 月页
    if not month_empty(pid):
        raise RuntimeError(f'{m} 月页非空，中止（需人工确认）')
    md = rd(f'{m}_月度总结.md')
    call('notion-update-page', {'page_id': pid, 'command': 'replace_content', 'new_str': md})
    ck[m]['month'] = True
    save_ckpt(ck)
    print(m, '月页 ok,', len(md), 'chars')
    # 2. 周页（一次批量）
    files = sorted(f for f in os.listdir(OUT) if f.startswith(f'{m}_第'))
    pages = [{'properties': {'title': f[len(m) + 1:-3]}, 'icon': '💪',
              'content': rd(f)} for f in files]
    t = call('notion-create-pages', {
        'parent': {'type': 'page_id', 'page_id': pid}, 'pages': pages})
    ids = parse_created(t)
    for f, i in zip(files, ids):
        ck[m]['weeks'][f[len(m) + 1:-3]] = i
    save_ckpt(ck)
    print(m, '周页 ok:', len(files), '个, ids:', len(ids))

if __name__ == '__main__':
    ck = load_ckpt()
    only = sys.argv[1:] or sorted(MONTHS)
    for m in only:
        run_month(m, MONTHS[m], ck)
    n_month = sum(1 for v in ck.values() if v.get('month'))
    n_week = sum(len(v.get('weeks', {})) for v in ck.values())
    print(f'\n== 完成：月页 {n_month}/12，周页 {n_week}/52 ==')

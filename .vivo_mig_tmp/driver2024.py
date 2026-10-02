# -*- coding: utf-8 -*-
"""vivo健康 2024 迁移驱动：月页 replace_content + 周页批量 create-pages"""
import io, json, os, re, sys

sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

OUT = 'D:/MyNotes/.vivo_mig_tmp/2024_out'
CKPT = 'D:/MyNotes/.vivo_mig_tmp/ckpt2024.json'

MONTHS = {
    '01': '3ed68f11-3d2d-8198-be2b-e61856bc85d3',
    '02': '3ed68f11-3d2d-81fa-ae81-d8de639dc9de',
    '03': '3ed68f11-3d2d-814b-a35b-e622bdce93e2',
    '04': '3ed68f11-3d2d-81b9-8d83-d47dc7b8a5a3',
    '05': '3ed68f11-3d2d-818f-b782-c9e73797b457',
    '06': '3ed68f11-3d2d-81cc-b83d-e2408b5d7123',
    '07': '3ed68f11-3d2d-8112-9de7-e1d07e2c10f0',
    '08': '3ed68f11-3d2d-8174-8473-dcf06c2a9751',
    '09': '3ed68f11-3d2d-813b-91c3-d4d515aa90e3',
    '10': '3ed68f11-3d2d-8177-a50a-c11817d81741',
    '11': '3ed68f11-3d2d-8101-b211-f2bcbe40c34f',
    '12': '3ed68f11-3d2d-81b8-9e9c-d32b08765d8d',
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

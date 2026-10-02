# -*- coding: utf-8 -*-
"""vivo健康 2023 表格格式修复驱动：月页+周页 replace_content，保留子页标签"""
import io, json, os, re, sys, time

sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

OUT = 'D:/MyNotes/.vivo_mig_tmp/2023_out'
CKPT = 'D:/MyNotes/.vivo_mig_tmp/ckpt2023fix.json'

MONTHS = {
    '08': '3ed68f11-3d2d-81de-a4b1-fc8fc70aaa41',
    '09': '3ed68f11-3d2d-817f-b3c9-d6f57c8e7a82',
    '10': '3ed68f11-3d2d-8160-9b1d-d7b76aeba6a5',
    '11': '3ed68f11-3d2d-81bc-842b-d319b31c0f7f',
    '12': '3ed68f11-3d2d-8145-b633-f61061bf7d92',
}

PAGE_TAG = re.compile(r'<page url="https://app\.notion\.com/p/[0-9a-f]+">[^<]*</page>')

def rd(name):
    return io.open(os.path.join(OUT, name), encoding='utf-8').read()

def load_ckpt():
    if os.path.exists(CKPT):
        return json.load(io.open(CKPT, encoding='utf-8'))
    return {}

def save_ckpt(c):
    io.open(CKPT, 'w', encoding='utf-8').write(json.dumps(c, ensure_ascii=False, indent=1))

def fetch(pid):
    raw = call('notion-fetch', {'id': pid})
    try:
        return json.loads(raw).get('text') or raw
    except Exception:
        return raw

def child_tags(txt):
    return PAGE_TAG.findall(txt)

def replace(pid, md):
    res = call('notion-update-page', {
        'page_id': pid, 'command': 'replace_content', 'new_str': md})
    if 'async_task' in res:
        print('  async:', res[:120])
    return res

def fix_page(pid, md, label):
    txt = fetch(pid)
    tags = child_tags(txt)
    new = md if not tags else md + '\n' + '\n'.join(tags)
    replace(pid, new)
    print(f'{label}: ok, 子页 {len(tags)} 个保留')

def run_month(m, pid, ck):
    if ck.get(m, {}).get('done'):
        print(m, 'done, skip'); return
    ck.setdefault(m, {'month': False, 'weeks': {}})
    # 1. 月页
    fix_page(pid, rd(f'{m}_月度总结.md'), f'{m} 月页')
    ck[m]['month'] = True
    save_ckpt(ck)
    # 2. 周页：按标题映射
    txt = fetch(pid)
    ids = re.findall(r'<page url="https://app\.notion\.com/p/([0-9a-f-]+)">([^<]*)</page>', txt)
    for wpid, title in ids:
        key = f'{m}_{title}'
        fn = key + '.md'
        if not os.path.exists(os.path.join(OUT, fn)):
            print(f'  !! 找不到 {fn}，跳过周页 {title}')
            continue
        fix_page(wpid, rd(fn), f'{m}/{title}')
        ck[m]['weeks'][title] = wpid
        save_ckpt(ck)
    ck[m]['done'] = True
    save_ckpt(ck)

if __name__ == '__main__':
    ck = load_ckpt()
    only = sys.argv[1:] or sorted(MONTHS)
    for m in only:
        run_month(m, MONTHS[m], ck)
    n_month = sum(1 for v in ck.values() if v.get('month'))
    n_week = sum(len(v.get('weeks', {})) for v in ck.values())
    print(f'\n== 完成：月页 {n_month}/5，周页 {n_week} ==')

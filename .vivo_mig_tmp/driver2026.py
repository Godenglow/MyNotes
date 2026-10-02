# -*- coding: utf-8 -*-
"""vivo健康 2026 迁移驱动：月页 replace_content + 周页批量 create-pages"""
import io, json, os, re, sys

sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

OUT = 'D:/MyNotes/.vivo_mig_tmp/2026_out'
CKPT = 'D:/MyNotes/.vivo_mig_tmp/ckpt2026.json'

MONTHS = {
    '01': '3ed68f11-3d2d-81d1-8a46-c5fe0a42366f',
    '02': '3ed68f11-3d2d-8151-aca6-cb6a3772288d',
    '03': '3ed68f11-3d2d-814c-9e1b-d37c7ed716a3',
    '04': '3ed68f11-3d2d-81dd-96d1-c508557baa62',
    '05': '3ed68f11-3d2d-8119-a029-ec10033289c1',
    '06': '3ed68f11-3d2d-8129-a85b-dcffc9922d21',
    '07': '3ed68f11-3d2d-81f3-864f-f19cf6181c85',
    '08': '3ed68f11-3d2d-81ef-a259-dabcb3bd8695',
    '09': '3ed68f11-3d2d-8107-b101-fd9c3fb6d5ab',
    '10': '3ed68f11-3d2d-8162-9ab0-d7b6439f18ee',
    '11': '3ed68f11-3d2d-816d-a13f-d9afcbb93725',
    '12': '3ed68f11-3d2d-81c1-a149-c37520e1928f',
}

EMPTY_MONTHS = {'11', '12'}
# 10 月仅第1周有真实数据（截至 10-02）
EMPTY_WEEKS = {('10', '第2周'), ('10', '第3周'), ('10', '第4周'), ('10', '第5周')}

EMPTY_WEEK_TMPL = ('⚠️ 源文件为预生成的空模板（周期未到，数据天数 0/7）。\n\n---\n\n'
                   '源文件：D:/Private-Note/vivo健康/2026/{m}/{name}.html · 迁移自 WorkBuddy · 2026-10-03')
EMPTY_MONTH_TMPL = ('⚠️ 源文件为预生成空模板（周期未到，无数据）。\n\n---\n\n'
                    '源文件：D:/Private-Note/vivo健康/2026/{m}/月度总结.html · 迁移自 WorkBuddy · 2026-10-03')

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
    return ('<blank-page>' in txt), txt

def month_content(m):
    if m in EMPTY_MONTHS:
        return EMPTY_MONTH_TMPL.format(m=m)
    md = rd(f'{m}_月度总结.md')
    if m == '10':
        # 保留月页下已有子页（健康日报 · 2026-10-01）
        _, txt = month_empty(MONTHS['10'])
        children = [c.replace('\\"', '"')
                    for c in re.findall(r'<page [^>]*>[^<]*</page>', txt)]
        if children:
            md = md + '\n\n' + '\n'.join(children)
    return md

def run_month(m, pid, ck):
    if ck.get(m):
        print(m, 'done, skip'); return
    ck[m] = {'month': False, 'weeks': {}}
    # 1. 月页
    empty, _ = month_empty(pid)
    if not empty and m not in ('10',):
        raise RuntimeError(f'{m} 月页非空，中止（需人工确认）')
    md = month_content(m)
    call('notion-update-page', {'page_id': pid, 'command': 'replace_content', 'new_str': md})
    ck[m]['month'] = True
    save_ckpt(ck)
    print(m, '月页 ok,', len(md), 'chars')
    # 2. 周页（一次批量）
    files = sorted(f for f in os.listdir(OUT) if f.startswith(f'{m}_第') and f.endswith('.md'))
    pages = []
    for f in files:
        name = f[len(m) + 1:-3]  # 第N周
        if (m, name) in EMPTY_WEEKS or m in EMPTY_MONTHS:
            content = EMPTY_WEEK_TMPL.format(m=m, name=name)
        else:
            content = rd(f)
        pages.append({'properties': {'title': name}, 'icon': '💪', 'content': content})
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
    print(f'\n== 完成：月页 {n_month}/12，周页 {n_week} ==')

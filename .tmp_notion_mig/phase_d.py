# -*- coding: utf-8 -*-
"""Phase D: 29 篇日报页创建（复盘速览 + 转换正文）"""
import io, json, os, re, sys
from notion_call import call

OUT = 'D:/MyNotes/.tmp_notion_mig/out'
CKPT = json.load(io.open('D:/MyNotes/.tmp_notion_mig/ckpt.json', encoding='utf-8'))
REVIEWS = json.load(io.open('D:/MyNotes/.tmp_notion_mig/reviews.json', encoding='utf-8'))
WIDS = CKPT['C']

WEEK_DAYS = {
    '第4周(08.24-08.30)': ['2026-08-30'],
    '第1周(08.31-09.06)': ['2026-08-31', '2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04', '2026-09-05', '2026-09-06'],
    '第2周(09.07-09.13)': ['2026-09-07', '2026-09-08', '2026-09-09', '2026-09-10', '2026-09-11', '2026-09-12', '2026-09-13'],
    '第3周(09.14-09.20)': ['2026-09-14', '2026-09-15', '2026-09-16', '2026-09-17', '2026-09-18', '2026-09-19', '2026-09-20'],
    '第4周(09.21-09.27)': ['2026-09-21', '2026-09-22', '2026-09-25', '2026-09-26', '2026-09-27'],
    '第1周(09.28-10.04)': ['2026-09-28', '2026-09-29'],  # 2026-10-02 已有页面，跳过
}

WEEK_MONTH = {
    '第4周(08.24-08.30)': '08',
    '第1周(08.31-09.06)': '09',
    '第2周(09.07-09.13)': '09',
    '第3周(09.14-09.20)': '09',
    '第4周(09.21-09.27)': '09',
    '第1周(09.28-10.04)': '10',
}

def week_of(date):
    for w, ds in WEEK_DAYS.items():
        if date in ds:
            return w
    return None

def src_rel(date):
    w = week_of(date)
    return 'D:/Private-Note/ScrePipe日报/2026/%s/%s/日报-%s.html' % (WEEK_MONTH[w], w, date)

def pipe_esc(t):
    return t.replace('|', '\\|')

def parse_body(txt):
    lines = txt.split('\n')
    # cards table
    tbl = []
    ti = next((i for i, l in enumerate(lines) if l.startswith('<table')), None)
    if ti is not None:
        j = ti
        while j < len(lines) and not lines[j].startswith('</table>'):
            tbl.append(lines[j]); j += 1
        tbl.append(lines[j])
    head = [l for l in lines[:ti] if l.strip()] if ti is not None else [l for l in lines if l.strip() and not l.startswith('## ')]
    # 数据口径 quote
    calib = None
    for l in lines:
        if l.startswith('> **数据口径说明'):
            calib = re.sub(r'^> \*\*数据口径说明(（重要）)?\*\* ?', '', l)
            break
    # main body: from first '## '
    mi = next((i for i, l in enumerate(lines) if l.startswith('## ')), len(lines))
    main = '\n'.join(lines[mi:]).strip()
    return tbl, head, calib, main

def build_page(date):
    w = week_of(date)
    txt = io.open(os.path.join(OUT, '2026', WEEK_MONTH[w], w, '日报-%s.html' % date), encoding='utf-8').read()
    tbl, head, calib, main = parse_body(txt)
    r = REVIEWS[date]
    out = []
    # 1 复盘速览
    rows = [
        ('今日评分', '%d / 10（AI 估分：依据当日工作占比与任务完成度评估，非报告原始数据）' % r['score']),
        ('今日核心目标', r['goal']),
        ('实际结果与差距', r['gap']),
        ('做的好的', r['good']),
        ('需改进的', r['improve']),
    ]
    if r.get('stop'):
        rows.append(('需停止的', r['stop']))
    if r.get('action'):
        rows.append(('解决方案 / 行动任务', r['action']))
    if r.get('insight'):
        rows.append(('灵感与思考', r['insight']))
    out.append('## 复盘速览')
    out.append('<table fit-page-width="true" header-row="true">')
    out.append('<tr><th>字段</th><th>内容</th></tr>')
    for k, v in rows:
        out.append('<tr><td>%s</td><td>%s</td></tr>' % (k, pipe_esc(v)))
    out.append('</table>')
    out.append('')
    # 2 当日概览
    out.append('## 当日概览')
    for hl in head:
        out.append('> ' + hl)
    out.append('')
    out.append('**当日主线**：' + r['goal'])
    out.append('')
    # 3 时长统计
    out.append('## 时长统计')
    if tbl:
        out.extend(tbl)
    else:
        out.append('（当日为首版日报，未含概览统计卡）')
    out.append('')
    # 4 正文
    out.append(main)
    out.append('')
    # 5 数据口径说明
    if calib:
        out.append('## 数据口径说明')
        for seg in re.split(r'；|。(?=\D|$)', calib):
            seg = seg.strip().strip('。')
            if seg:
                out.append('- ' + seg)
        out.append('')
    # footer
    out.append('---')
    out.append('')
    out.append('源文件：%s · 迁移自 WorkBuddy · 2026-10-03' % src_rel(date))
    return '\n'.join(out)

def main():
    dry = '--dry' in sys.argv
    only = None
    for a in sys.argv[1:]:
        if a.startswith('--week='):
            only = a.split('=', 1)[1]
    created = {}
    for w, days in WEEK_DAYS.items():
        if only and w != only:
            continue
        parent = WIDS[w]
        pages = []
        for d in days:
            content = build_page(d)
            if dry:
                io.open('D:/MyNotes/.tmp_notion_mig/preview-%s.md' % d, 'w', encoding='utf-8').write(content)
                continue
            pages.append({'properties': {'title': '日报-' + d}, 'icon': '📺', 'content': content})
        if dry:
            continue
        t = call('notion-create-pages', {'parent': {'type': 'page_id', 'page_id': parent}, 'pages': pages})
        ids = re.findall(r'app\.notion\.com/p/([0-9a-f]{32})', t)
        seen = []
        for i in ids:
            if i not in seen:
                seen.append(i)
        created[w] = seen
        print(w, '->', len(seen), 'pages', seen[:2], '...')
    if not dry:
        io.open('D:/MyNotes/.tmp_notion_mig/ckpt.json', 'w', encoding='utf-8').write(
            json.dumps(dict(CKPT, D=created), ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()

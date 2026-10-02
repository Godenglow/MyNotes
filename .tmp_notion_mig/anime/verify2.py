# -*- coding: utf-8 -*-
"""全量字段级比对：Notion 库 vs 本地 rows.json（按 subject_id 对齐）"""
import io, json, sys
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

DS = 'collection://182ba37b-48ea-4676-ba7c-5fa4be46c307'
rows = json.load(io.open('D:/MyNotes/.tmp_notion_mig/anime/rows.json', encoding='utf-8'))

def sql(q, params=None):
    d = {'mode': 'sql', 'data_source_urls': [DS], 'query': q}
    if params:
        d['params'] = params
    return json.loads(call('notion-query-data-sources', {'data': d}))['results']

COLS = ('"Bangumi链接","片名","原名","观看状态","我的评分","Rank","集数",'
        '"date:发行日期:start" AS air,"date:收藏日期:start" AS fav')
notion = []
for off in range(0, 500, 200):
    res = sql('SELECT %s FROM "%s" LIMIT 200 OFFSET %d' % (COLS, DS, off))
    notion.extend(res)
print('notion rows fetched:', len(notion))

by_url = {}
for r in notion:
    sid = r['Bangumi链接'].rsplit('/', 1)[-1]
    by_url[sid] = r

errs = []
for i, r in enumerate(rows):
    sid = r['subject_id']
    n = by_url.get(sid)
    if n is None:
        errs.append('row %d (%s): missing in notion' % (i, r['name_cn'] or r['name_jp']))
        continue
    def eq(a, b, label):
        if a != b:
            errs.append('row %d %s: notion=%r csv=%r' % (i, label, a, b))
    eq(n['片名'], r['name_cn'] if r['name_cn'] else r['name_jp'], 'title')
    eq(n['原名'], r['name_jp'], 'orig')
    eq(n['观看状态'], r['watch_status'], 'status')
    eq(n['我的评分'], r['my_score'], 'my_score')
    eq(n['Rank'], r['csv_rank'], 'rank')
    eq(n['集数'], r['eps'], 'eps')
    eq(n['air'], r['air_date'] or None, 'air_date')
    eq(n['fav'], r['fav_date'] or None, 'fav_date')

print('mismatches:', len(errs))
for e in errs[:20]:
    print(' ', e)

# 星标换算函数自测（官方评分缺失未应用，但验证算法本身）
import math
def stars(score):
    n = int(math.floor(score + 0.5))
    n = max(0, min(10, n))
    return '⭐️' * (n // 2) + ('½' if n % 2 else '')
for s, want in [(7.3, '⭐️⭐️⭐️½'), (9.5, '⭐️⭐️⭐️⭐️⭐️'), (8.0, '⭐️⭐️⭐️⭐️'), (6.4, '⭐️⭐️⭐️'), (2.1, '⭐️')]:
    got = stars(s)
    print('stars(%.1f) = %s %s' % (s, got, 'OK' if got == want else 'MISMATCH want ' + want))

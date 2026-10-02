# -*- coding: utf-8 -*-
"""核对：行数、分组统计、抽样比对、字段空值统计"""
import io, json, sys
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

DS = 'collection://182ba37b-48ea-4676-ba7c-5fa4be46c307'

def sql(q, params=None):
    d = {'mode': 'sql', 'data_source_urls': [DS], 'query': q}
    if params:
        d['params'] = params
    return json.loads(call('notion-query-data-sources', {'data': d}))

r1 = sql('SELECT COUNT(*) AS n FROM "%s"' % DS)
print('total rows:', r1)

r2 = sql('SELECT "观看状态" AS s, COUNT(*) AS n FROM "%s" GROUP BY "观看状态" ORDER BY n DESC' % DS)
print('group by watch:', json.dumps(r2, ensure_ascii=False))

r3 = sql('SELECT COUNT(*) AS n FROM "%s" WHERE "我的评分" IS NOT NULL' % DS)
print('rows with my_score:', r3)

r4 = sql('SELECT COUNT(*) AS n FROM "%s" WHERE "官方评分" IS NOT NULL' % DS)
print('rows with api_score:', r4)

r5 = sql('SELECT COUNT(*) AS n FROM "%s" WHERE "Rank" IS NOT NULL' % DS)
print('rows with rank:', r5)

r6 = sql('SELECT COUNT(*) AS n FROM "%s" WHERE "评分" IS NOT NULL' % DS)
print('rows with star rating:', r6)

r7 = sql('SELECT COUNT(*) AS n FROM "%s" WHERE "集数" IS NOT NULL' % DS)
print('rows with eps:', r7)

# 抽样：第1行(想看无评分)、第2行(想看)、以及三行有我的评分的、Rank 缺失的行
r8 = sql('SELECT "片名","原名","观看状态","我的评分","Rank","集数","Bangumi链接",'
         '"date:发行日期:start" AS air,"date:收藏日期:start" AS fav '
         'FROM "%s" WHERE "我的评分" IS NOT NULL LIMIT 5' % DS)
print('sample scored:', json.dumps(r8, ensure_ascii=False))

r9 = sql('SELECT "片名","观看状态","我的评分","Rank","集数" FROM "%s" WHERE "Rank" IS NULL LIMIT 6' % DS)
print('rows without rank (should be 4):', json.dumps(r9, ensure_ascii=False))

r10 = sql('SELECT "片名" FROM "%s" WHERE "观看状态" = ? LIMIT 3' % DS, ['想看'])
print('want-watch sample:', json.dumps(r10, ensure_ascii=False))

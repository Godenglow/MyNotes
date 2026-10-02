# -*- coding: utf-8 -*-
"""最终核对：只认目标库中的页；cover 用原文匹配"""
import io, json, sys
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

rows = json.load(io.open('D:/MyNotes/.tmp_notion_mig/anime/rows.json', encoding='utf-8'))
DS_MARK = '182ba37b-48ea-4676-ba7c-5fa4be46c307'
picks = [0, 59, 81]

for i in picks:
    r = rows[i]
    q = r['name_cn'] if r['name_cn'] else r['name_jp']
    res = call('notion-search', {'query': q})
    j = json.loads(res)
    target_pid = None
    for it in j.get('results', []):
        if it.get('title') != q:
            continue
        pid = it['id'].replace('-', '')
        pf = json.loads(call('notion-fetch', {'id': pid}))
        text = pf.get('text', '')
        if DS_MARK in text:
            target_pid = pid
            target_text = text
            break
    if not target_pid:
        print('[%d] %s: NOT FOUND in target ds' % (i, q))
        continue
    text = target_text
    import re
    checks = []
    for label, want in [('片名', q), ('原名', r['name_jp']), ('观看状态', r['watch_status']),
                        ('链接', 'bgm.tv/subject/' + r['subject_id']),
                        ('收藏日期', r['fav_date'])]:
        checks.append('%s:%s' % (label, 'OK' if (want or '') in text else 'MISS'))
    if r['my_score'] is not None:
        checks.append('my_score:%s' % ('OK' if ('"我的评分"' in text and str(int(r['my_score'])) in text) else 'MISS'))
    else:
        checks.append('my_score:OK(empty)')
    if r['csv_rank'] is not None:
        checks.append('rank:%s' % ('OK' if str(r['csv_rank']) in text else 'MISS'))
    if r['eps'] is not None:
        checks.append('eps:%s' % ('OK' if str(r['eps']) in text else 'MISS'))
    if r['air_date']:
        checks.append('air:%s' % ('OK' if r['air_date'] in text else 'MISS'))
    else:
        checks.append('air:OK(empty)')
    checks.append('cover:%s' % ('OK' if r['cover'] in text else 'MISS'))
    print('[%d] %s pid=%s' % (i, q, target_pid[:8]))
    print('   ', '; '.join(checks))

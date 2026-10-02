# -*- coding: utf-8 -*-
"""用正确 pid 精确核对抽样行属性 + 封面"""
import io, json, re, sys
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

rows = json.load(io.open('D:/MyNotes/.tmp_notion_mig/anime/rows.json', encoding='utf-8'))

# 从库中精确取 3 行的 pid：row0, 59(钢炼,有评分), 81(呼唤少女,air Null,无eps)
picks = [0, 59, 81]
for i in picks:
    r = rows[i]
    q = r['name_cn'] if r['name_cn'] else r['name_jp']
    res = call('notion-search', {'query': q})
    j = json.loads(res)
    pid = None
    for it in j.get('results', []):
        if it.get('title') == q and '182ba37b' not in it.get('url', ''):
            # 需确认父级是目标库：fetch 后判断
            pid = it['id'].replace('-', '')
            break
    if not pid:
        print('[%d] %s: NOT FOUND' % (i, q)); continue
    pf = json.loads(call('notion-fetch', {'id': pid}))
    text = pf.get('text', '')
    is_target = '182ba37b-48ea-4676-ba7c-5fa4be46c307' in text
    props_m = re.search(r'<properties>\n(\{.*?\})\n</properties>', text, re.S)
    props = json.loads(props_m.group(1)) if props_m else {}
    exp = {
        '片名': q,
        '原名': r['name_jp'],
        '观看状态': r['watch_status'],
        'Bangumi链接': 'https://bgm.tv/subject/' + r['subject_id'],
        'Rank': r['csv_rank'],
        '集数': r['eps'],
        '我的评分': r['my_score'],
        'date:发行日期:start': r['air_date'] or None,
        'date:收藏日期:start': r['fav_date'] or None,
    }
    print('=== [%d] %s pid=%s target_ds=%s' % (i, q, pid[:8], is_target))
    for k, want in exp.items():
        got = props.get(k)
        status = 'OK' if got == want else 'DIFF got=%r want=%r' % (got, want)
        if want is None and got is None:
            status = 'OK(both empty)'
        print('   %-22s %s' % (k, status))
    cov_m = re.search(r'<cover>(.*?)</cover>', text, re.S)
    cov = cov_m.group(1) if cov_m else ''
    print('   cover                  %s' % ('OK' if r['cover'] in cov else 'DIFF got=%r want=%r' % (cov[:80], r['cover'])))

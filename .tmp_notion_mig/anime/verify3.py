# -*- coding: utf-8 -*-
"""抽样核对：搜索页 id -> fetch 页面 -> 比对属性与封面"""
import io, json, sys
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

rows = json.load(io.open('D:/MyNotes/.tmp_notion_mig/anime/rows.json', encoding='utf-8'))
ratings = json.load(io.open('D:/MyNotes/.tmp_notion_mig/anime/ratings.json', encoding='utf-8'))

# 抽 5 行：0=想看无评分；有评分(找 my_score 非 null 且看过)；想看有评分；Rank 缺失(81 呼唤少女)；在看
picks = [0]
scored_idx = [i for i, r in enumerate(rows) if r['my_score'] is not None][:2]
picks += scored_idx
picks += [81]                        # Rank/eps 缺失 + air_date Null
picks += [i for i, r in enumerate(rows) if r['watch_status'] == '在看'][:1]
seen = set()
picks = [p for p in picks if not (p in seen or seen.add(p))]
print('picks:', [(i, rows[i]['name_cn'] or rows[i]['name_jp']) for i in picks])

for i in picks:
    r = rows[i]
    q = r['name_cn'] if r['name_cn'] else r['name_jp']
    res = call('notion-search', {'query': q})
    j = json.loads(res)
    # 从搜索结果中找精确匹配标题的页
    pid = None
    items = j.get('results') or j.get('data') or []
    if isinstance(items, dict):
        items = items.get('results', [])
    for it in items:
        t = json.dumps(it, ensure_ascii=False)
        if q in t and '/p/' in t:
            import re
            m = re.search(r'app\.notion\.com/p/([0-9a-f]{32})', t)
            if m:
                pid = m.group(1)
                break
    if not pid:
        print('[%d] %s: PAGE NOT FOUND via search' % (i, q))
        continue
    pf = json.loads(call('notion-fetch', {'id': pid}))
    text = pf.get('text', '')
    ok_flags = []
    for label, want in [
            ('片名', q), ('原名', r['name_jp']), ('观看状态', r['watch_status']),
            ('链接', 'https://bgm.tv/subject/' + r['subject_id']),
            ('收藏日期', r['fav_date'])]:
        ok_flags.append('%s=%s' % (label, 'OK' if (want or '') in text else 'MISSING'))
    if r['my_score'] is not None:
        ok_flags.append('my_score=%s' % ('OK' if str(int(r['my_score'])) in text else 'CHECK'))
    if r['air_date']:
        ok_flags.append('air=%s' % ('OK' if r['air_date'] in text else 'MISSING'))
    if r['csv_rank'] is not None:
        ok_flags.append('rank=%s' % ('OK' if str(r['csv_rank']) in text else 'CHECK'))
    if r['eps'] is not None:
        ok_flags.append('eps=%s' % ('OK' if str(r['eps']) in text else 'CHECK'))
    has_cover = r['cover'] in text if r['cover'] else None
    print('[%d] %s (pid %s): %s cover=%s' % (i, q, pid[:8], '; '.join(ok_flags), has_cover))

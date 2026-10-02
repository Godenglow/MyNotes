# -*- coding: utf-8 -*-
"""批量写入 398 行到「🎬 我的追番」：直连 Notion MCP HTTP 端点，断点续传"""
import io, json, math, re, sys, time
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

DIR = 'D:/MyNotes/.tmp_notion_mig/anime'
DS = '182ba37b-48ea-4676-ba7c-5fa4be46c307'
CKPT = DIR + '/ckpt_write.json'

rows = json.load(io.open(DIR + '/rows.json', encoding='utf-8'))
ratings = json.load(io.open(DIR + '/ratings.json', encoding='utf-8'))

try:
    ck = json.load(io.open(CKPT, encoding='utf-8'))
except Exception:
    ck = {'done_batches': 0}

def stars(score):
    n = int(math.floor(score + 0.5))
    n = max(0, min(10, n))
    return ('★' * (n // 2)).replace('★', '⭐️') + ('½' if n % 2 else '')

def build(r):
    sid = r['subject_id']
    rt = ratings.get(sid) or {}
    props = {
        '片名': r['name_cn'] if r['name_cn'] else r['name_jp'],
        '原名': r['name_jp'],
        '观看状态': r['watch_status'],
        'Bangumi链接': 'https://bgm.tv/subject/' + sid,
    }
    if r['my_score'] is not None:
        props['我的评分'] = r['my_score']
    api_score = rt.get('score') if rt.get('_done') else None
    if api_score is not None:
        props['官方评分'] = api_score
        props['评分'] = stars(api_score)
    api_rank = rt.get('rank') if rt.get('_done') else None
    rank_val = api_rank if api_rank is not None else r['csv_rank']
    if rank_val is not None:
        props['Rank'] = rank_val
    if r['eps'] is not None:
        props['集数'] = r['eps']
    if r['air_date']:
        props['date:发行日期:start'] = r['air_date']
    if r['fav_date']:
        props['date:收藏日期:start'] = r['fav_date']
    page = {'properties': props}
    if r['cover']:
        page['cover'] = r['cover']
    return page

BATCH = 30
n_batches = (len(rows) + BATCH - 1) // BATCH
for b in range(n_batches):
    if b < ck['done_batches']:
        continue
    chunk = [build(r) for r in rows[b * BATCH:(b + 1) * BATCH]]
    for attempt in (1, 2, 3):
        try:
            call('notion-create-pages', {
                'parent': {'type': 'data_source_id', 'data_source_id': DS},
                'pages': chunk, 'allow_async': False})
            ck['done_batches'] = b + 1
            io.open(CKPT, 'w', encoding='utf-8').write(json.dumps(ck))
            print('batch %d/%d ok (%d rows)' % (b + 1, n_batches, len(chunk)))
            break
        except Exception as e:
            print('batch %d attempt %d FAIL: %s' % (b + 1, attempt, str(e)[:300]))
            if attempt == 3:
                raise
            time.sleep(3.0)
print('ALL DONE, batches:', ck['done_batches'])

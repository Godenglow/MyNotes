# -*- coding: utf-8 -*-
"""Bangumi API 批量抓取官方评分：rating{rank,score,total}"""
import io, json, time, urllib.request, urllib.error

ROWS = 'D:/MyNotes/.tmp_notion_mig/anime/rows.json'
OUT = 'D:/MyNotes/.tmp_notion_mig/anime/ratings.json'
UA = 'Godenglow-NotionSync/1.0 (https://github.com/Godenglow)'

rows = json.load(io.open(ROWS, encoding='utf-8'))
ids = [r['subject_id'] for r in rows if r['subject_id']]

try:
    ratings = json.load(io.open(OUT, encoding='utf-8'))
except Exception:
    ratings = {}

def fetch(sid):
    url = 'https://api.bgm.tv/v0/subjects/' + sid
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    rt = data.get('rating') or {}
    return {'rank': rt.get('rank'), 'score': rt.get('score'), 'total': rt.get('total')}

ok = fail = 0
failed_ids = []
for i, sid in enumerate(ids, 1):
    if sid in ratings and ratings[sid].get('_done'):
        continue
    got = None
    for attempt in (1, 2):
        try:
            got = fetch(sid)
            got['_done'] = True
            break
        except Exception as e:
            if attempt == 2:
                failed_ids.append(sid)
                print('FAIL', sid, repr(e)[:120])
            time.sleep(1.0)
    if got:
        ratings[sid] = got
        ok += 1
    else:
        fail += 1
    if i % 20 == 0 or i == len(ids):
        io.open(OUT, 'w', encoding='utf-8').write(
            json.dumps(ratings, ensure_ascii=False, indent=1))
        print('progress %d/%d ok=%d fail=%d' % (i, len(ids), ok, fail))
    time.sleep(0.35)

io.open(OUT, 'w', encoding='utf-8').write(json.dumps(ratings, ensure_ascii=False, indent=1))
print('DONE ok=%d fail=%d' % (ok, fail))
print('failed ids:', failed_ids)

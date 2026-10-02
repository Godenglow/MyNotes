# -*- coding: utf-8 -*-
"""回填官方评分/评分/Rank 到「🎬 我的追番」：逐页 update_properties，断点续传"""
import io, json, math, sys, time
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

DIR = 'D:/MyNotes/.tmp_notion_mig/anime'
CKPT = DIR + '/ckpt_update.json'

rows = json.load(io.open(DIR + '/rows.json', encoding='utf-8'))
ratings = json.load(io.open(DIR + '/ratings.json', encoding='utf-8'))
mp = json.load(io.open(DIR + '/map.json', encoding='utf-8'))

try:
    ck = json.load(io.open(CKPT, encoding='utf-8'))
except Exception:
    ck = {'done': []}
done = set(ck['done'])

def stars(score):
    n = int(math.floor(score + 0.5))
    n = max(0, min(10, n))
    return ('★' * (n // 2)).replace('★', '⭐️') + ('½' if n % 2 else '')

def build_props(sid):
    rt = ratings.get(sid) or {}
    props = {}
    sc = rt.get('score') if rt.get('_done') else None
    if sc is not None:
        props['官方评分'] = sc
        props['评分'] = stars(sc)
    else:
        props['评分'] = None  # 清空
    rk = rt.get('rank') if rt.get('_done') else None
    if rk is not None:
        props['Rank'] = rk
    return props

todo = [r for r in rows if r['subject_id'] in mp and r['subject_id'] not in done]
print('todo:', len(todo), flush=True)
BATCH = 30
ok = 0; fails = []
for bi in range(0, len(todo), BATCH):
    chunk = todo[bi:bi + BATCH]
    for r in chunk:
        sid = r['subject_id']
        pid = mp[sid]
        props = build_props(sid)
        for attempt in (1, 2, 3):
            try:
                call('notion-update-page', {'page_id': pid, 'command': 'update_properties',
                                            'properties': props})
                done.add(sid); ok += 1
                break
            except Exception as e:
                print('update fail %s attempt %d: %s' % (sid, attempt, str(e)[:200]), flush=True)
                if attempt == 3:
                    fails.append(sid)
                else:
                    time.sleep(3)
        time.sleep(0.3)
    ck['done'] = sorted(done)
    io.open(CKPT, 'w', encoding='utf-8').write(json.dumps(ck))
    print('batch %d/%d done, total=%d fail=%d' % (min(bi + BATCH, len(todo)), len(todo), ok, len(fails)), flush=True)

io.open(DIR + '/update_fail.json', 'w', encoding='utf-8').write(json.dumps(fails))
print('UPDATE DONE: ok=%d fail=%d mapped_total=%d' % (ok, len(fails), len(mp)))

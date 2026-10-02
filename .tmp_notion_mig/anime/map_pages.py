# -*- coding: utf-8 -*-
"""建立 subject_id -> page_id 映射：限定数据源搜索标题，重名时 fetch 消歧"""
import io, json, re, sys, time
sys.path.insert(0, 'D:/MyNotes/.tmp_notion_mig')
from notion_call import call

DIR = 'D:/MyNotes/.tmp_notion_mig/anime'
DS_URL = 'collection://182ba37b-48ea-4676-ba7c-5fa4be46c307'
DS_MARK = '182ba37b-48ea-4676-ba7c-5fa4be46c307'
MAPF = DIR + '/map.json'
FAILF = DIR + '/map_fail.json'

rows = json.load(io.open(DIR + '/rows.json', encoding='utf-8'))
try:
    mp = json.load(io.open(MAPF, encoding='utf-8'))
except Exception:
    mp = {}

def search(title):
    res = call('notion-search', {'query': title, 'data_source_url': DS_URL})
    j = json.loads(res)
    return [it for it in j.get('results', []) if it.get('title') == title]

def resolve(r, title):
    cands = search(title)
    if len(cands) == 1:
        return cands[0]['id'].replace('-', '')
    if len(cands) > 1:
        # 重名：fetch 用 Bangumi链接 消歧
        want = 'bgm.tv/subject/' + r['subject_id']
        for c in cands:
            pid = c['id'].replace('-', '')
            pf = call('notion-fetch', {'id': pid})
            j = json.loads(pf)
            m = re.search(r'"Bangumi链接":"([^"]*)"', j.get('text', ''))
            if m and want in m.group(1):
                return pid
        return None
    return None

fails = []
todo = [r for r in rows if r['subject_id'] not in mp]
print('todo:', len(todo), flush=True)
for i, r in enumerate(todo):
    sid = r['subject_id']
    q = r['name_cn'] if r['name_cn'] else r['name_jp']
    pid = None
    for attempt in (1, 2, 3):
        try:
            pid = resolve(r, q)
            if not pid and r['name_cn'] and r['name_jp']:
                pid = resolve(r, r['name_jp'])
            break
        except Exception as e:
            print('search fail %s attempt %d: %s' % (sid, attempt, str(e)[:150]), flush=True)
            time.sleep(5)
    if pid:
        mp[sid] = pid
    else:
        fails.append(sid)
        print('[%d/%d] %s %s: NO MATCH' % (i + 1, len(todo), sid, q), flush=True)
    if (i + 1) % 10 == 0 or i + 1 == len(todo):
        io.open(MAPF, 'w', encoding='utf-8').write(json.dumps(mp, ensure_ascii=False))
        io.open(FAILF, 'w', encoding='utf-8').write(json.dumps(fails))
        print('progress %d/%d mapped=%d fail=%d' % (i + 1, len(todo), len(mp), len(fails)), flush=True)
    time.sleep(0.5)

io.open(MAPF, 'w', encoding='utf-8').write(json.dumps(mp, ensure_ascii=False))
io.open(FAILF, 'w', encoding='utf-8').write(json.dumps(fails))
print('MAPPING DONE: mapped=%d fail=%d' % (len(mp), len(fails)))

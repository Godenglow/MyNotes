# -*- coding: utf-8 -*-
import csv, io, json, re
from collections import Counter
SRC = 'D:/BaiduNetdiskDownload/导出收藏-2026-10-03.csv'
rows = []
with io.open(SRC, encoding='utf-8-sig', newline='') as f:
    for r in csv.DictReader(f):
        m = re.search(r'/subject/(\d+)', r['地址'])
        eps = re.search(r'eps:\s*(\d+)', r['其它信息'])
        rank = re.search(r'Rank\s*(\d+)', r['其它信息'])
        rows.append({
            'name_jp': r['名称'],
            'name_cn': r['别名'].strip(),
            'air_date': r['发行日期'].strip(),
            'subject_id': m.group(1) if m else None,
            'cover': r['封面地址'].strip(),
            'fav_date': r['收藏日期'].strip(),
            'my_score': float(r['我的评分']) if r['我的评分'].strip() else None,
            'eps': int(eps.group(1)) if eps else None,
            'csv_rank': int(rank.group(1)) if rank else None,
            'watch_status': r['观看状态'].strip(),
        })
json.dump(rows, io.open('D:/MyNotes/.tmp_notion_mig/anime/rows.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('total', len(rows))
print(Counter(x['watch_status'] for x in rows))
print('no subject_id:', [x['name_jp'] for x in rows if not x['subject_id']])
print('eps missing:', sum(1 for x in rows if x['eps'] is None))
print('rank missing:', sum(1 for x in rows if x['csv_rank'] is None))
print('my_score missing:', sum(1 for x in rows if x['my_score'] is None))
print('cn empty:', sum(1 for x in rows if not x['name_cn']))
print('cover empty:', sum(1 for x in rows if not x['cover']))
print('sample:', json.dumps(rows[0], ensure_ascii=False))

# -*- coding: utf-8 -*-
"""下载 Du 笔记中的全部语雀 CDN 图片到 assets/"""
import json
import os
import re
import glob
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

DOCS = r'D:/MyNotes/Du'
ASSETS = os.path.join(DOCS, 'assets')
MANIFEST = os.path.join(DOCS, '_raw', 'img_manifest.json')
os.makedirs(ASSETS, exist_ok=True)

curl = shutil.which('curl') or r'C:/Windows/System32/curl.exe'
print('curl:', curl)

# 1) 收集全部 cdn URL（从 md 现文）
urls = set()
for fp in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    for m in re.finditer(r'https://cdn\.nlark\.com/[^\s)\"\'<>]+', text):
        urls.add(m.group(0))
urls = sorted(urls)
print('待下载 URL:', len(urls))

# 2) 已下载的跳过（支持续传）
def target_name(u):
    fn = u.split('/')[-1].split('?')[0]
    fn = re.sub(r'[^A-Za-z0-9._-]', '_', fn)
    return fn

todo = []
for u in urls:
    out = os.path.join(ASSETS, target_name(u))
    if os.path.exists(out) and os.path.getsize(out) > 0:
        continue
    todo.append(u)
print('已存在跳过:', len(urls) - len(todo), '| 本次下载:', len(todo))

def dl(u):
    fn = target_name(u)
    out = os.path.join(ASSETS, fn)
    for attempt in range(3):
        try:
            r = subprocess.run(
                [curl, '-s', '-o', out, '--max-time', '90', '-w', '%{http_code} %{size_download}',
                 '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', u],
                capture_output=True, text=True, timeout=120)
            parts = (r.stdout or '').strip().split()
            if len(parts) == 2 and parts[0] == '200' and int(parts[1]) > 0:
                return (u, fn, 'ok', int(parts[1]))
        except Exception:
            pass
    return (u, fn, 'fail', 0)

results = []
done = 0
fail = 0
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = {ex.submit(dl, u): u for u in todo}
    for fu in as_completed(futs):
        u, fn, st, size = fu.result()
        results.append({'url': u, 'file': fn, 'status': st, 'size': size})
        done += 1
        if st != 'ok':
            fail += 1
        if done % 200 == 0 or done == len(todo):
            print(f'进度 {done}/{len(todo)} | 失败 {fail}', flush=True)

# 合并已有记录
old = []
if os.path.exists(MANIFEST):
    try:
        with open(MANIFEST, encoding='utf-8') as f:
            old = json.load(f)
    except Exception:
        old = []
# 重建完整 manifest：扫描 assets 目录实际文件
final = []
allmap = {}
for r in old:
    allmap[r['url']] = r
for r in results:
    allmap[r['url']] = r
ok_files = set(os.listdir(ASSETS))
for u in urls:
    r = allmap.get(u)
    if r is None:
        fn = target_name(u)
        exists = fn in ok_files
        r = {'url': u, 'file': fn, 'status': 'ok' if exists else 'missing', 'size': 0}
    final.append(r)

with open(MANIFEST, 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=1)

okc = sum(1 for r in final if r['status'] == 'ok')
bad = [r for r in final if r['status'] != 'ok']
print()
print(f'完成: 成功 {okc} / {len(final)} | 失败 {len(bad)}')
for r in bad[:20]:
    print('  FAIL:', r['url'])

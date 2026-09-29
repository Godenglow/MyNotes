# -*- coding: utf-8 -*-
"""将 md 中的语雀 CDN 图片链接替换为本地 assets/ 相对路径（含备份）"""
import json
import os
import re
import glob
import shutil

DOCS = r'D:/MyNotes/Du'
ASSETS = os.path.join(DOCS, 'assets')
MANIFEST = os.path.join(DOCS, '_raw', 'img_manifest.json')
BACKUP = os.path.join(DOCS, '_raw', 'md_backup_before_localize')

with open(MANIFEST, encoding='utf-8') as f:
    manifest = json.load(f)

ok = {r['url']: r['file'] for r in manifest if r['status'] == 'ok'}
bad = [r for r in manifest if r['status'] != 'ok']
print(f'manifest: ok={len(ok)} | 未成功={len(bad)}')
for r in bad[:10]:
    print('  未成功:', r['url'][:100])

# 备份原文件
os.makedirs(BACKUP, exist_ok=True)
for fp in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
    shutil.copy2(fp, os.path.join(BACKUP, os.path.basename(fp)))
print('已备份 17 个 md 到 _raw/md_backup_before_localize/')

total_repl = 0
for fp in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    orig = text
    n = 0
    for url, fn in ok.items():
        if url in text:
            cnt = text.count(url)
            text = text.replace(url, 'assets/' + fn)
            n += cnt
    if text != orig:
        with open(fp, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
    total_repl += n
    print(f'{os.path.basename(fp)}: 替换 {n} 处')

print()
print('总替换:', total_repl)

# 残留检查
leftover = 0
for fp in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    leftover += len(re.findall(r'cdn\.nlark\.com', text))
print('残留 cdn.nlark.com 引用:', leftover, '(应为 0)')

# 引用完整性检查：md 中每个 assets/xxx 是否都存在
missing = set()
refs = 0
for fp in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
    with open(fp, encoding='utf-8') as f:
        text = f.read()
    for m in re.finditer(r'\]\(assets/([^)\s]+)\)', text):
        refs += 1
        if not os.path.exists(os.path.join(ASSETS, m.group(1))):
            missing.add(m.group(1))
print('assets 引用数:', refs, '| 缺失文件:', len(missing))
for m in list(missing)[:10]:
    print('  缺失:', m)

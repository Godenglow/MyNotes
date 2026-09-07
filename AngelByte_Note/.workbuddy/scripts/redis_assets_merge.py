# -*- coding: utf-8 -*-
"""redis_assets_merge.py — 10-Redis 三个图片目录合并为单个 assets/
同名文件 MD5 相同→去重；不同→重命名 _2 并同步改 HTML src。"""
import hashlib, os, re, shutil

D = r"D:\MyNotes\AngelByte_Note\10-Redis"
ASSETS = os.path.join(D, "assets")
HTML = os.path.join(D, "Redis.html")

def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()

s = open(HTML, encoding="utf-8").read()
moved = dedup = renamed = 0
for sub in ["Redis.assets", "Redis实战篇.assets"]:
    src_dir = os.path.join(D, sub)
    for n in os.listdir(src_dir):
        src = os.path.join(src_dir, n)
        dst = os.path.join(ASSETS, n)
        if not os.path.exists(dst):
            shutil.move(src, dst); moved += 1; continue
        if md5(src) == md5(dst):
            os.remove(src); dedup += 1; continue
        stem, ext = os.path.splitext(n)
        i = 2
        while os.path.exists(dst2 := os.path.join(ASSETS, f"{stem}_{i}{ext}")):
            i += 1
        shutil.move(src, dst2); renamed += 1
        s = s.replace(f"{sub}/{n}", f"assets/{stem}_{i}{ext}")
    os.rmdir(src_dir)

open(HTML, "w", encoding="utf-8").write(s)
print(f"移入 {moved} | MD5 重复去重 {dedup} | 冲突改名 {renamed}")
print("剩余目录:", [d for d in os.listdir(D) if os.path.isdir(os.path.join(D, d))])

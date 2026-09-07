# -*- coding: utf-8 -*-
"""redis_cleanup.py — 10-Redis 冗余图片目录清理（幂等收尾步）
把 Redis.assets/、Redis实战篇.assets/ 并回 assets/（MD5 去重、冲突改名），
同步双向改写 Redis.html 里的 src（原文/URL 编码两种形式），删空目录。
放在管线最后跑，保证结束态只剩 Redis.html + assets/ + pptx。"""
import hashlib
import os
import shutil
from urllib.parse import quote

D = r"D:\MyNotes\AngelByte_Note\10-Redis"
ASSETS = os.path.join(D, "assets")
HTML = os.path.join(D, "Redis.html")

def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()

if not (os.path.isdir(D) and os.path.isfile(HTML)):
    print("redis_cleanup: 10-Redis 结构不符，跳过")
    raise SystemExit(0)

s = open(HTML, encoding="utf-8").read()
moved = dedup = renamed = 0
for sub in ("Redis.assets", "Redis实战篇.assets"):
    src_dir = os.path.join(D, sub)
    if not os.path.isdir(src_dir):
        continue
    for n in os.listdir(src_dir):
        src = os.path.join(src_dir, n)
        dst = os.path.join(ASSETS, n)
        if not os.path.exists(dst):
            shutil.move(src, dst)
            moved += 1
            continue
        if md5(src) == md5(dst):
            os.remove(src)
            dedup += 1
            continue
        stem, ext = os.path.splitext(n)
        i = 2
        while os.path.exists(dst2 := os.path.join(ASSETS, f"{stem}_{i}{ext}")):
            i += 1
        os.rename(src, dst2)
        renamed += 1
        # 冲突改名：两种 src 形态都指向新名
        for pre in (sub + "/", quote(sub) + "/"):
            s = s.replace(pre + n, "assets/" + f"{stem}_{i}{ext}")
    if not os.listdir(src_dir):
        os.rmdir(src_dir)

# src 双形式前缀归一
s = s.replace("Redis.assets/", "assets/").replace("Redis实战篇.assets/", "assets/")
s = s.replace(quote("Redis.assets") + "/", "assets/").replace(quote("Redis实战篇.assets") + "/", "assets/")
open(HTML, "w", encoding="utf-8").write(s)
print(f"redis_cleanup: 移入 {moved} | 去重 {dedup} | 改名 {renamed} | "
      f"剩余目录: {[d for d in os.listdir(D) if os.path.isdir(os.path.join(D, d))]}")

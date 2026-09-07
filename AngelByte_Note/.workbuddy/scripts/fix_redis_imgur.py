# -*- coding: utf-8 -*-
"""fix_redis_imgur.py — Redis 两份 HTML 的 imgur 死链转占位"""
import os, re

TARGETS = [
    r"D:\MyNotes\AngelByte_Note\10-Redis\Redis入门\讲义\Redis.html",
    r"D:\MyNotes\AngelByte_Note\10-Redis\Redis入门\代码\Redis注释版\Redis.html",
]
PLACEHOLDER = '<div class="img-missing">🖼 原图缺失（imgur 图床已删除该图，实测 404）</div>'

for p in TARGETS:
    s = open(p, encoding="utf-8").read()
    s, n = re.subn(r"<img[^>]+i\.imgur\.com[^>]*>", PLACEHOLDER, s)
    open(p, "w", encoding="utf-8").write(s)
    name = os.path.basename(os.path.dirname(p)) + "/" + os.path.basename(p)
    print(name, "->", n, "处占位；剩余 imgur 引用:", s.count("i.imgur.com"))

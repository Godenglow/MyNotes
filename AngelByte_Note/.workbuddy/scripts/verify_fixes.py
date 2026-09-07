# -*- coding: utf-8 -*-
"""verify_fixes.py — 核查三项修复的最终状态"""
import os, re
from urllib.parse import unquote

os.chdir(r"D:\MyNotes\AngelByte_Note")

f = "01-HTML+CSS.html"
s = open(f, encoding="utf-8").read()
real_rel = s.count('rel="noopener noreferrer"')
escaped_touched = len(re.findall(r"&lt;a [^&]*rel=", s))
escaped_pure = len(re.findall(r"&lt;a href=\"https://news\.cctv\.com/\" target=\"_blank\"&gt;", s))
print(f"1) 01-HTML+CSS: 真实链接带 rel = {real_rel} (预期1) | 教学示例被误改 = {escaped_touched} (预期0) | 示例原样 = {escaped_pure} (预期6)")

f = "02-Java Web.html"
s = open(f, encoding="utf-8").read()
print(f"2) 02-Java Web: img-missing 占位 = {s.count(chr(34).join(['class=', 'img-missing']))} 个 (预期3)")

total_bad = 0
for root, dirs, files in os.walk("."):
    if ".workbuddy" in root:
        continue
    for name in files:
        if not name.endswith(".html"):
            continue
        p = os.path.join(root, name)
        out_dir = os.path.dirname(os.path.abspath(p))
        s = open(p, encoding="utf-8").read()
        miss = [m.group(1) for m in re.finditer(r'<img[^>]+src="(?!https?:|data:)([^"]+)"', s)
                if not os.path.exists(os.path.normpath(os.path.join(out_dir, unquote(m.group(1)).split("?")[0])))]
        if miss:
            total_bad += len(miss)
            print(f"   断图: {p} -> {miss[:3]}")
print(f"3) 全库本地断图总数 = {total_bad} (预期0)")

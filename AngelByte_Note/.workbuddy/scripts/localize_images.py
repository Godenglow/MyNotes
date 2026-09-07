# -*- coding: utf-8 -*-
"""localize_images.py — 外链图批量本地化
- 根目录 9 个 HTML 移入同名文件夹（HTML + assets/ 同居，对齐 11-RMQ 结构）
- 语雀/博客园外链图下载到 <文件夹>/assets/，src 改写为相对路径
- imgur（上游已删，实测 404）→ img-missing 占位框
- 失败的外链保留原 src 并输出清单
"""
import concurrent.futures as cf
import html as H
import os
import re
import shutil
import sys
import urllib.request

VAULT = r"D:\MyNotes\AngelByte_Note"
MOVES = [
    ("01-HTML+CSS.html", "01-HTML+CSS"),
    ("02-Java Web.html", "02-Java Web"),
    ("03-JDBC.html", "03-JDBC"),
    ("04-MySQL.html", "04-MySQL"),
    ("05-MVC 架构模式.html", "05-MVC 架构模式"),
    ("06-Mybatis.html", "06-Mybatis"),
    ("07-Spring6框架.html", "07-Spring6框架"),
    ("08-SpringMVC笔记.html", "08-SpringMVC笔记"),
    ("Git.html", "Git"),
]
SEATA = ("12-Seata", "Seata.html")   # (文件夹, html 名)，已在文件夹内
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
MAGIC = (b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n", b"GIF8", b"RIFF")
EXT_BY_MAGIC = {b"\xff\xd8\xff": ".jpg", b"\x89PNG\r\n\x1a\n": ".png", b"GIF8": ".gif", b"RIFF": ".webp"}

def magic_ok(data):
    return any(data.startswith(m) for m in MAGIC)

def fetch(url, dest):
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
            if not magic_ok(data):
                raise ValueError(f"非图片内容: {data[:24]!r}")
            with open(dest, "wb") as f:
                f.write(data)
            return True, len(data)
        except Exception as e:  # noqa
            last = e
    print(f"    FAIL {url[:90]} -> {last}", flush=True)
    return False, 0

def localize(html_path, assets_dir):
    s = open(html_path, encoding="utf-8").read()
    os.makedirs(assets_dir, exist_ok=True)

    # 1) imgur 死链 → 占位框
    s, n_imgur = re.subn(
        r'<img[^>]+i\.imgur\.com[^>]*>',
        '<div class="img-missing">🖼 原图缺失（imgur 图床已删除该图，实测 404）</div>',
        s,
    )

    # 2) 收集其余外链
    tasks = {}   # clean_url -> (attr原文, 本地文件名)
    for m in re.finditer(r'<img[^>]+src="(https?://[^"]+)"', s):
        attr = m.group(1)
        clean = H.unescape(attr).split("#")[0]
        if "i.imgur.com" in clean:
            continue
        if clean not in tasks:
            base = os.path.basename(urllib.parse.urlparse(clean).path) or "img"
            tasks[clean] = [attr, base]

    # 3) 并发下载
    results = {}
    def work(item):
        clean, (attr, base) = item
        dest = os.path.join(assets_dir, base)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return clean, True, base
        ok, _ = fetch(clean, dest)
        return clean, ok, base

    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for clean, ok, base in ex.map(work, tasks.items()):
            results[clean] = (ok, base)
    n_ok = sum(1 for ok, _ in results.values() if ok)
    fails = [clean for clean, (ok, _) in results.items() if not ok]

    # 4) src 改写（含扩展名嗅探修正）
    fixed = []
    for clean, (ok, base) in results.items():
        attr_forms = {clean, H.escape(clean)}
        p = os.path.join(assets_dir, base)
        if ok:
            with open(p, "rb") as f:
                head = f.read(12)
            for mk, ext in EXT_BY_MAGIC.items():
                if head.startswith(mk) and not base.lower().endswith(ext):
                    new = base + ext
                    os.rename(p, os.path.join(assets_dir, new))
                    base = new
                    break
            for a in attr_forms:
                s = s.replace(a, "assets/" + base)
            fixed.append(base)
        else:
            fixed.append("FAIL:" + clean)

    open(html_path, "w", encoding="utf-8").write(s)
    return n_imgur, len(tasks), n_ok, fails, fixed

print("== 移动根目录 HTML 进文件夹 ==", flush=True)
jobs = []
for html_name, folder in MOVES:
    src = os.path.join(VAULT, html_name)
    dst_dir = os.path.join(VAULT, folder)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, html_name)
    if os.path.exists(src):
        shutil.move(src, dst)
    jobs.append((dst, os.path.join(dst_dir, "assets"), folder))
jhtml, jfolder = SEATA
jobs.append((os.path.join(VAULT, jhtml, jhtml if False else jhtml), None, jfolder))
jobs[-1] = (os.path.join(VAULT, "12-Seata", "Seata.html"), os.path.join(VAULT, "12-Seata", "assets"), "12-Seata")

print("== 下载并改写 ==", flush=True)
report, all_fails = [], []
for html_path, assets_dir, label in jobs:
    n_imgur, n_total, n_ok, fails, _ = localize(html_path, assets_dir)
    line = f"{label:20s} 外链 {n_total:4d} | 成功 {n_ok:4d} | 失败 {len(fails):2d} | imgur占位 {n_imgur}"
    print(line, flush=True)
    report.append(line)
    all_fails += [(label, u) for u in fails]

fail_log = os.path.join(VAULT, ".workbuddy", "localize_failures.txt")
with open(fail_log, "w", encoding="utf-8") as f:
    for label, u in all_fails:
        f.write(f"{label}\t{u}\n")
print(f"\n完成。失败 {len(all_fails)} 个，清单: {fail_log}", flush=True)

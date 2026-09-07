# -*- coding: utf-8 -*-
"""redis_merge.py — 10-Redis 整理：合并为一个 Redis.html，代码/杂物归档
结构结果:
  10-Redis/
    Redis.html            (课程介绍 + 基础篇 + 实战篇 三章)
    assets/               (基础篇图片)
    Redis实战篇.assets/    (实战篇图片)
    01-Redis快速入门.pptx / 02-Redis企业实战.pptx
归档:
  .workbuddy/notes_backup_20260907_095204/redis_archive/
"""
import io, os, re, shutil, subprocess, sys

VAULT = r"D:\MyNotes\AngelByte_Note\10-Redis"
BK = r"D:\MyNotes\AngelByte_Note\.workbuddy\notes_backup_20260907_095204"
ARCH = os.path.join(BK, "redis_archive")
SKILL = r"C:\Users\29074\.workbuddy\skills\md-to-dark-html\scripts\md2dark_html.py"
PY = r"C:\Users\29074\.workbuddy\binaries\python\envs\default\Scripts\python.exe"
BKR = os.path.join(BK, "10-Redis")   # 备份里的 md（拍平命名）

def J(*a): return os.path.join(VAULT, *a)

# ---------- 1) 归档（move，不销毁） ----------
os.makedirs(ARCH, exist_ok=True)
moves = [
    (J("Redis入门", "代码"), os.path.join(ARCH, "代码_Redis入门")),          # redis-demo 项目
    (J("Redis实战", "代码"), os.path.join(ARCH, "代码_Redis实战")),          # hm-dianping 项目
    (J("Redis入门", "代码", "Redis注释版", "Redis.assets"),
     os.path.join(ARCH, "注释版_Redis.assets")),
    (J("Redis入门", "讲义", "01.快速入门.assets"),
     os.path.join(ARCH, "快速入门_Redis.assets")),
]
for src, dst in moves:
    if os.path.exists(src):
        shutil.move(src, dst)
        print("归档:", os.path.relpath(src, VAULT), "->", os.path.relpath(dst, BK))

# ---------- 2) 图片目录集中 ----------
if os.path.isdir(J("Redis入门", "讲义", "assets")):
    if os.path.isdir(J("assets")):
        # 已有则并入（同名同大小跳过）
        for n in os.listdir(J("Redis入门", "讲义", "assets")):
            s, d = J("Redis入门", "讲义", "assets", n), J("assets", n)
            if not os.path.exists(d):
                shutil.move(s, d)
        os.rmdir(J("Redis入门", "讲义", "assets"))
    else:
        shutil.move(J("Redis入门", "讲义", "assets"), J("assets"))
    print("图片集中: assets/ <- Redis入门/讲义/assets")
if os.path.isdir(J("Redis实战", "讲义", "Redis实战篇.assets")):
    shutil.move(J("Redis实战", "讲义", "Redis实战篇.assets"), J("Redis实战篇.assets"))
    print("图片集中: Redis实战篇.assets/ <- Redis实战/讲义")
if os.path.isdir(J("Redis入门", "讲义", "Redis.assets")):
    shutil.move(J("Redis入门", "讲义", "Redis.assets"), J("Redis.assets"))
    print("图片集中: Redis.assets/ <- Redis入门/讲义")

# pptx 提到顶层
for root, dirs, files in os.walk(VAULT):
    for n in files:
        if n.endswith(".pptx") and os.path.dirname(root) or (n.endswith(".pptx") and os.path.dirname(os.path.abspath(root)) != VAULT):
            pass
for sub in [("Redis入门", "讲义"), ("Redis实战", "讲义")]:
    d = J(*sub)
    if os.path.isdir(d):
        for n in os.listdir(d):
            if n.endswith(".pptx"):
                shutil.move(os.path.join(d, n), J(n))
                print("pptx 提顶层:", n)

# ---------- 3) 合并 md（3 章；代码块内标题不降级） ----------
def chapter(md_path, fallback):
    text = io.open(md_path, encoding="utf-8").read()
    lines = text.splitlines()
    ch, idx = None, None
    for i, l in enumerate(lines):
        m = re.match(r"^# (.+)$", l)
        if m:
            ch = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", m.group(1)).strip()
            idx = i
            break
    if not ch:
        ch = fallback
    else:
        lines = lines[:idx] + lines[idx + 1:]
    fence = False
    out = []
    for l in lines:
        if l.strip().startswith("```"):
            fence = not fence
            out.append(l); continue
        if not fence:
            l = re.sub(r"^(#{1,5}) ", r"#\1 ", l)
        out.append(l)
    return ch, "\n".join(out).strip()

parts = []
for md_name, fb, dst_name in [
    ("00.课程介绍.md", "课程介绍", None),          # 备份拍平名
    ("Redis.md", "基础篇", None),
    ("Redis实战篇.md", "实战篇", None),
]:
    ch, body = chapter(os.path.join(BKR, md_name), fb)
    parts.append(f"# {ch}\n\n{body}")
merged = "\n\n---\n\n".join(parts)
tmp = J("_merged.md")
io.open(tmp, "w", encoding="utf-8").write(merged)
print(f"合并 md: 3 章, {len(merged)//1024}KB")

# ---------- 4) 转换 ----------
r = subprocess.run([PY, SKILL, tmp, "-o", J("Redis.html"), "--keep-first-h1"], capture_output=True, text=True)
print((r.stdout or r.stderr).strip().splitlines()[-1])
os.remove(tmp)
if r.returncode != 0:
    sys.exit("转换失败，中止清理")

# ---------- 5) 删除已被合并替代的旧文件 ----------
for old in [J("Redis入门", "讲义", "Redis.html"),
            J("Redis入门", "讲义", "00.课程介绍.html"),
            J("Redis实战", "讲义", "Redis实战篇.html")]:
    if os.path.exists(old):
        os.remove(old)
        print("删除旧 html:", os.path.relpath(old, VAULT))

# ---------- 6) 清空壳目录（pptx 已提顶层，assets 已集中） ----------
for sub in [("Redis入门", "讲义"), ("Redis实战", "讲义"),
            ("Redis入门",), ("Redis实战",)]:
    d = J(*sub)
    if os.path.isdir(d) and not os.listdir(d):
        os.rmdir(d)
        print("移除空目录:", os.path.relpath(d, VAULT))

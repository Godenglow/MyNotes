# -*- coding: utf-8 -*-
"""regen_all.py — 从 .workbuddy 备份全量重生成 AngelByte_Note 的 18 个 HTML
用法: python regen_all.py
依赖: skill md-to-dark-html（C:/Users/29074/.workbuddy/skills/md-to-dark-html）
"""
import glob, io, os, re, subprocess, sys

VAULT = r"D:\MyNotes\AngelByte_Note"
BK_MAIN = os.path.join(VAULT, ".workbuddy", "notes_backup_20260907_095204")
BK_JAVASE = os.path.join(VAULT, ".workbuddy", "notes_backup_20260907_085106")
SKILL = r"C:\Users\29074\.workbuddy\skills\md-to-dark-html\scripts\md2dark_html.py"
PY = r"C:\Users\29074\.workbuddy\binaries\python\envs\default\Scripts\python.exe"

ROOT_NOTES = ["01-HTML+CSS", "02-Java Web", "03-JDBC", "04-MySQL", "05-MVC 架构模式",
              "06-Mybatis", "07-Spring6框架", "08-SpringMVC笔记", "Git"]

def run(src, out, extra=()):
    flat = []
    for a in extra:
        if isinstance(a, (list, tuple)):
            flat += [str(x) for x in a]
        elif a:
            flat.append(str(a))
    args = [PY, SKILL, str(src), "-o", str(out)] + flat
    r = subprocess.run(args, capture_output=True, text=True)
    tail = (r.stdout or r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else "?"
    print(f"{os.path.basename(out):44s} {tail}")
    return r.returncode == 0

def merge_rmq():
    """备份里的 23 个 Operation*.md -> 正式目录 RMQ.md（首 h1 作章标题并移除，其余降级，代码块内不动）"""
    bak = os.path.join(BK_MAIN, "11-RMQ")
    files = sorted(glob.glob(os.path.join(bak, "Operation*.md")))
    out = []
    for f in files:
        text = io.open(f, encoding="utf-8").read()
        lines = text.splitlines()
        ch_title, h1_idx = None, None
        for i, l in enumerate(lines):
            m = re.match(r"^# (.+)$", l)
            if m:
                ch_title = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", m.group(1)).strip()
                h1_idx = i
                break
        if not ch_title:
            ch_title = os.path.splitext(os.path.basename(f))[0].replace("Operation", "")
        else:
            lines = lines[:h1_idx] + lines[h1_idx + 1:]
        fence = False
        demoted = []
        for l in lines:
            if l.strip().startswith("```"):
                fence = not fence
                demoted.append(l); continue
            if not fence:
                l = re.sub(r"^(#{1,5}) ", r"#\1 ", l)
            demoted.append(l)
        out.append(f"# {ch_title}\n\n" + "\n".join(demoted).strip() + "\n")
    dst = os.path.join(VAULT, "11-RMQ", "RMQ.md")
    io.open(dst, "w", encoding="utf-8").write("\n\n---\n\n".join(out))
    return dst

ok = fail = 0
# 根目录 9 个 + Seata + Q&A
for n in ROOT_NOTES:
    ok += run(os.path.join(BK_MAIN, n + ".md"), os.path.join(VAULT, n, n + ".html"))
for src, out, *extra in [
    (os.path.join(BK_MAIN, "12-Seata", "Seata.md"), os.path.join(VAULT, "12-Seata", "Seata.html"), []),
    (os.path.join(BK_MAIN, "00-JavaSE", "JavaSE Q&A.md"),
     os.path.join(VAULT, "00-JavaSE", "JavaSE Q&A.html"),
     ["--embed-dir", os.path.join(VAULT, "00-JavaSE", "assets")]),
    (os.path.join(BK_JAVASE, "JavaSE.md"), os.path.join(VAULT, "00-JavaSE", "JavaSE.html"),
     ["--embed-dir", os.path.join(VAULT, "00-JavaSE", "document")]),
    # Redis 5 个（备份拍平，映射回原目录）
    (os.path.join(BK_MAIN, "10-Redis", "Redis.md"), os.path.join(VAULT, "10-Redis", "Redis入门", "讲义", "Redis.html"), []),
    (os.path.join(BK_MAIN, "10-Redis", "01.快速入门.md"), os.path.join(VAULT, "10-Redis", "Redis入门", "讲义", "01.快速入门.html"), []),
    (os.path.join(BK_MAIN, "10-Redis", "00.课程介绍.md"), os.path.join(VAULT, "10-Redis", "Redis入门", "讲义", "00.课程介绍.html"), []),
    (os.path.join(BK_MAIN, "10-Redis", "Redis实战篇.md"), os.path.join(VAULT, "10-Redis", "Redis实战", "讲义", "Redis实战篇.html"), []),
    (os.path.join(BK_MAIN, "10-Redis", "Redis注释版.md"), os.path.join(VAULT, "10-Redis", "Redis入门", "代码", "Redis注释版", "Redis.html"), []),
]:
    ok += run(src, out, extra)

# RMQ：合并 + 转换 + 删临时 md
if merge_rmq():
    if run(os.path.join(VAULT, "11-RMQ", "RMQ.md"), os.path.join(VAULT, "11-RMQ", "RMQ.html")):
        os.remove(os.path.join(VAULT, "11-RMQ", "RMQ.md"))
        ok += 1
    else:
        fail += 1

print(f"\n完成: 成功 {ok} / 失败 {fail}")
print("提醒: 根目录 9 个笔记重生成后需再跑 localize_images.py 恢复图片本地化")
sys.exit(1 if fail else 0)

# -*- coding: utf-8 -*-
"""JavaSE.md -> dark GitHub style HTML (matches ScrePipe日报 / vivo健康 visual style)."""
import os, re, sys
import markdown
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

SRC = r"D:\MyNotes\AngelByte_Note\00-JavaSE\JavaSE.md"
DOC_DIR = r"D:\MyNotes\AngelByte_Note\00-JavaSE\document"
OUT = r"D:\MyNotes\AngelByte_Note\00-JavaSE\JavaSE.html"

text = open(SRC, encoding="utf-8").read()

# ---------- 1. split off intro block (before first chapter) ----------
m = re.search(r"(?m)^# 🚀", text)
intro_block, body = text[: m.start()], text[m.start():]
intro_lines = [l.strip() for l in intro_block.splitlines() if l.strip()]
intro_sub = intro_lines[1] if len(intro_lines) > 1 else "JavaSE 课程笔记"

# ---------- 2. wiki embeds  ![[name]]  -> mermaid diagram card ----------
def embed_repl(mo):
    name = mo.group(1).strip()
    p = os.path.join(DOC_DIR, name + ".md")
    if os.path.exists(p):
        src = open(p, encoding="utf-8").read()
        mm = re.search(r"```mermaid\n(.*?)```", src, re.S)
        if mm:
            code = (mm.group(1)
                    .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            return (
                f'\n<div class="diagram-card"><div class="diagram-title">'
                f'<span class="dt-ico">📊</span>{name}'
                f'<span class="dt-src">源文件 {name}.mdj</span></div>'
                f'<pre class="mermaid">\n{code}</pre></div>\n'
            )
    return mo.group(0)

body = re.sub(r"!\[\[([^\]]+)\]\]", embed_repl, body)

# ---------- 3. wiki links  [[target|alias]] / [[target]]  -> styled span ----------
def link_repl(mo):
    inner = mo.group(1)
    alias = inner.split("|", 1)[1].strip() if "|" in inner else inner.split("#")[0].strip()
    return f'<span class="wl" title="Obsidian 内链：{inner.strip()}">🔗 {alias}</span>'

body = re.sub(r"\[\[([^\]]+)\]\]", link_repl, body)

# ---------- 4. GFM task list -> unicode ----------
body = re.sub(r"^(\s*[-*]) \[ \] ", r"\1 ☐ ", body, flags=re.M)
body = re.sub(r"^(\s*[-*]) \[[xX]\] ", r"\1 ☑ ", body, flags=re.M)

# ---------- 5. per-chapter conversion ----------
md_exts = ["fenced_code", "tables", "sane_lists", "toc", "codehilite"]
md_cfg = {
    "codehilite": {"guess_lang": False, "pygments_style": "one-dark"},
    "toc": {"permalink": False},
}
try:
    get_style_by_name("one-dark")
    PYG_STYLE = "one-dark"
except Exception:
    PYG_STYLE = "github-dark"
    md_cfg["codehilite"]["pygments_style"] = PYG_STYLE

chapters_raw = re.split(r"(?m)^# ", body)[1:]  # drop leading empty
chapters = []
for i, ch in enumerate(chapters_raw, 1):
    nl = ch.find("\n")
    title, content = ch[:nl].strip(), ch[nl + 1 :]
    html = markdown.markdown(content, extensions=md_exts, extension_configs=md_cfg)
    # wrap tables for horizontal scroll
    html = html.replace("<table>", '<div class="tbl-wrap"><table>').replace(
        "</table>", "</table></div>"
    )
    chapters.append({"id": f"ch-{i:02d}", "title": title, "html": html})

n_code = len(re.findall(r"```", body)) // 2
n_diagrams = len(re.findall(r'class="diagram-card"', " ".join(c["html"] for c in chapters)))
n_sections = sum(
    len(re.findall(r"<h[23] ", c["html"])) for c in chapters
)

# ---------- 6. assemble ----------
pyg_css = HtmlFormatter(style=PYG_STYLE).get_style_defs(".codehilite")
toc_items = "\n".join(
    f'<a class="toc-item" href="#{c["id"]}"><span class="toc-idx">{i:02d}</span>'
    f'<span>{c["title"]}</span></a>'
    for i, c in enumerate(chapters, 1)
)
chapter_html = "\n".join(
    f'<section class="chapter" id="{c["id"]}">\n'
    f'<div class="ch-head"><span class="ch-num">{i:02d}</span>'
    f'<h1>{c["title"]}</h1></div>\n{c["html"]}\n</section>'
    for i, c in enumerate(chapters, 1)
)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:24px}
body{background:#0d1117;color:#e6edf3;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;line-height:1.75}
a{color:#58a6ff;text-decoration:none}
a:hover{text-decoration:underline}
/* ---------- sidebar ---------- */
.sidebar{position:fixed;inset:0 auto 0 0;width:272px;background:#010409;border-right:1px solid #262d38;overflow-y:auto;padding:22px 14px 40px;z-index:50}
.sidebar .brand{display:flex;align-items:center;gap:9px;padding:2px 8px 16px;border-bottom:1px solid #21262d;margin-bottom:14px}
.sidebar .brand .logo{width:32px;height:32px;border-radius:8px;background:#21262d;display:flex;align-items:center;justify-content:center;font-size:17px}
.sidebar .brand b{font-size:15px}
.sidebar .brand .cnt{color:#8b949e;font-size:11px}
.toc-item{display:flex;align-items:center;gap:9px;padding:7px 9px;border-radius:7px;color:#8b949e;font-size:12.5px;line-height:1.4}
.toc-item:hover{background:#161b22;color:#e6edf3;text-decoration:none}
.toc-item.active{background:#161b22;color:#58a6ff}
.toc-idx{font-size:10.5px;font-variant-numeric:tabular-nums;color:#6e7681;min-width:18px}
.toc-item.active .toc-idx{color:#58a6ff}
.side-note{margin:18px 8px 0;color:#6e7681;font-size:11px;line-height:1.6;border-top:1px solid #21262d;padding-top:12px}
/* ---------- main ---------- */
.main{margin-left:272px;padding:34px 46px 140px;max-width:1060px}
.hero{border-bottom:1px solid #262d38;padding-bottom:22px;margin-bottom:10px}
.hero .crumb{color:#8b949e;font-size:12px;margin-bottom:10px}
.hero h1.title{font-size:30px;font-weight:750;letter-spacing:-.5px;display:flex;align-items:center;gap:12px}
.hero .sub{color:#8b949e;font-size:13.5px;margin-top:8px;max-width:720px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:11px;margin:22px 0 6px}
.card{background:#161b22;border:1px solid #262d38;border-radius:9px;padding:12px 14px}
.card .k{color:#8b949e;font-size:11px}
.card .v{font-size:20px;font-weight:680;margin-top:3px;line-height:1.25}
.card .d{color:#8b949e;font-size:11px;margin-top:3px}
/* ---------- chapter ---------- */
.chapter{margin:46px 0 10px}
.ch-head{display:flex;align-items:center;gap:13px;padding:14px 18px;background:linear-gradient(90deg,#161b22,#0d1117);border:1px solid #262d38;border-radius:10px;margin-bottom:18px;position:sticky;top:0;z-index:10}
.ch-num{display:inline-flex;align-items:center;justify-content:center;min-width:38px;height:38px;border-radius:9px;background:#21262d;color:#58a6ff;font-size:14px;font-weight:750;font-variant-numeric:tabular-nums}
.ch-head h1{font-size:21px;font-weight:700}
.chapter h2{font-size:18px;font-weight:680;margin:30px 0 12px;padding-bottom:8px;border-bottom:1px solid #262d38;display:flex;align-items:center;gap:8px}
.chapter h3{font-size:15.5px;font-weight:660;margin:22px 0 9px;color:#79c0ff}
.chapter h2:target,.chapter h3:target{color:#ffa657}
.chapter h4{font-size:14px;margin:16px 0 7px;color:#8b949e}
.chapter p{margin:10px 0;font-size:14px}
.chapter ul,.chapter ol{margin:9px 0 9px 22px}
.chapter li{margin:5.5px 0;font-size:14px}
.chapter li::marker{color:#6e7681}
strong{color:#f0f6fc}
.chapter blockquote{border-left:3px solid #58a6ff;background:#161b22;border-radius:0 8px 8px 0;padding:10px 16px;margin:13px 0;color:#b6c2cf;font-size:13.5px}
.chapter blockquote p{margin:5px 0}
/* inline code */
code{background:#21262d;padding:1.5px 6px;border-radius:4px;font-size:12.5px;color:#bc8cff;font-family:"Cascadia Code",Consolas,"JetBrains Mono",monospace}
/* code block */
.codehilite{background:#161b22;border:1px solid #262d38;border-radius:9px;padding:13px 15px;margin:13px 0;overflow-x:auto;position:relative}
.codehilite pre{margin:0;background:transparent!important}
.codehilite code{background:transparent;padding:0;font-size:12.8px;line-height:1.62;color:#c9d1d9}
/* tables */
.tbl-wrap{overflow-x:auto;margin:13px 0;border:1px solid #262d38;border-radius:9px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:8px 11px;text-align:left;border-bottom:1px solid #21262d;vertical-align:top}
th{color:#8b949e;font-weight:600;font-size:12px;background:#161b22;position:sticky;top:0}
tr:last-child td{border-bottom:none}
tr:hover td{background:#10161f}
td code{white-space:nowrap}
/* diagram card */
.diagram-card{background:#161b22;border:1px solid #262d38;border-radius:10px;margin:16px 0;overflow:hidden}
.diagram-title{display:flex;align-items:center;gap:8px;padding:10px 15px;border-bottom:1px solid #262d38;font-size:13px;font-weight:650;color:#79c0ff}
.dt-src{margin-left:auto;color:#6e7681;font-size:11px;font-weight:400}
.diagram-card .mermaid{display:flex;justify-content:center;padding:16px 12px;background:#0d1117;overflow-x:auto}
.diagram-card pre.mermaid{font-family:Consolas,monospace;font-size:12px;color:#8b949e;white-space:pre-wrap}
.diagram-card svg{max-width:100%;height:auto}
/* misc */
.wl{color:#58a6ff;background:rgba(88,166,255,.1);padding:1px 7px;border-radius:20px;font-size:12.5px}
.top-btn{position:fixed;right:26px;bottom:26px;width:40px;height:40px;border-radius:50%;background:#21262d;border:1px solid #30363d;color:#8b949e;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:60;opacity:0;pointer-events:none;transition:opacity .25s}
.top-btn.show{opacity:1;pointer-events:auto}
.top-btn:hover{color:#58a6ff;border-color:#58a6ff}
.foot{margin-top:60px;padding-top:18px;border-top:1px solid #262d38;color:#6e7681;font-size:11.5px;line-height:1.8}
.menu-btn{display:none;position:fixed;left:14px;top:14px;z-index:70;width:38px;height:38px;border-radius:8px;background:#21262d;border:1px solid #30363d;color:#e6edf3;font-size:17px;cursor:pointer}
@media (max-width:960px){
  .sidebar{transform:translateX(-100%);transition:transform .25s;width:280px}
  .sidebar.open{transform:translateX(0);box-shadow:0 0 40px rgba(0,0,0,.6)}
  .main{margin-left:0;padding:24px 18px 120px;padding-top:64px}
  .menu-btn{display:flex;align-items:center;justify-content:center}
  .ch-head{position:static}
}
"""

JS = """
const items=[...document.querySelectorAll('.toc-item')];
const secs=[...document.querySelectorAll('.chapter')];
const spy=new IntersectionObserver(es=>{
  es.forEach(e=>{ if(e.isIntersecting){
    items.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+e.target.id));
  }});
},{rootMargin:'-20% 0px -70% 0px'});
secs.forEach(s=>spy.observe(s));
const btn=document.getElementById('topBtn');
addEventListener('scroll',()=>btn.classList.toggle('show',scrollY>600));
btn.onclick=()=>scrollTo({top:0,behavior:'smooth'});
const sb=document.getElementById('sidebar');
document.getElementById('menuBtn').onclick=()=>sb.classList.toggle('open');
document.addEventListener('click',e=>{
  if(sb.classList.contains('open')&&!sb.contains(e.target)&&e.target.id!=='menuBtn')sb.classList.remove('open');
});
"""

HTML = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JavaSE 课程笔记</title>
<style>{pyg_css}{CSS}</style>
</head>
<body>
<button class="menu-btn" id="menuBtn">☰</button>
<nav class="sidebar" id="sidebar">
  <div class="brand"><span class="logo">☕</span><div><b>JavaSE 笔记</b><div class="cnt">15 章 · 完整目录</div></div></div>
  {toc_items}
  <div class="side-note">由 JavaSE.md 转换生成 · 2026-09-07<br>深色 GitHub 风格 · 点击章节跳转</div>
</nav>
<main class="main">
<header class="hero">
  <div class="crumb">AngelByte_Note › 00-JavaSE › <b>JavaSE</b></div>
  <h1 class="title">☕ JavaSE 课程笔记</h1>
  <div class="sub">{intro_sub}</div>
  <div class="cards">
    <div class="card"><div class="k">章节</div><div class="v" style="color:#58a6ff">15</div><div class="d">环境搭建 → Java 新特性</div></div>
    <div class="card"><div class="k">知识点小节</div><div class="v" style="color:#3fb950">{n_sections}</div><div class="d">h2 / h3 标题合计</div></div>
    <div class="card"><div class="k">代码块</div><div class="v" style="color:#a371f7">{n_code}</div><div class="d">语法高亮 · 可横向滚动</div></div>
    <div class="card"><div class="k">类图 / 图表</div><div class="v" style="color:#bc8cff">{n_diagrams}</div><div class="d">Mermaid 渲染（需联网加载一次）</div></div>
    <div class="card"><div class="k">篇幅</div><div class="v" style="color:#ffa657">{len(text)//1000}K</div><div class="d">字符 · 约 8268 行</div></div>
  </div>
</header>
{chapter_html}
<div class="foot">JavaSE 课程笔记 · 转换自 JavaSE.md（原 md 已归档备份）· 生成于 2026-09-07 · 样式参照 ScrePipe日报 / vivo健康 深色风格<br>⚠️ Mermaid 类图需联网加载 mermaid.js，加载失败时将直接显示图源码</div>
</main>
<button class="top-btn" id="topBtn" title="回到顶部">↑</button>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>if(typeof mermaid==='undefined')document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js"><\\/script>');</script>
<script>
if(typeof mermaid!=='undefined'){{mermaid.initialize({{startOnLoad:true,theme:'dark',themeVariables:{{background:'#0d1117',primaryColor:'#21262d',primaryTextColor:'#e6edf3',primaryBorderColor:'#58a6ff',lineColor:'#8b949e',fontFamily:'-apple-system,Microsoft YaHei,sans-serif'}},class:{{htmlLabels:true}}}});}}
{JS}
</script>
</body>
</html>"""

open(OUT, "w", encoding="utf-8").write(HTML)
print(f"OK -> {OUT}  ({os.path.getsize(OUT)//1024} KB, chapters={len(chapters)}, diagrams={n_diagrams})")

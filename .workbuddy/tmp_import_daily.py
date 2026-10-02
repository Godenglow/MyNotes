# -*- coding: utf-8 -*-
"""把本地 30 篇日报 HTML 批量导入 Notion「📔 日报」数据库。

直连 API（integration weiguowu10.2），绕开 MCP 数组参数限制。
每条记录 = 标题 + 复盘速览/核心指标结构化文本 + 原始 HTML embed。
"""
import json
import os
import re
import time
import urllib.request
import urllib.error
import glob

TOKEN = "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"
DS = "collection://3a868f11-3d2d-82ff-9c3e-8794fa6c4021"
ROOT = r"D:\Private-Note\ScrePipe日报"
API = "https://api.notion.com/v1"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2025-09-03",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
}

WD = "一二三四五六日"
ATTACH_DIR = os.path.join(os.environ.get("TEMP", "."), "notion_attach")
os.makedirs(ATTACH_DIR, exist_ok=True)


def post(path, payload):
    req = urllib.request.Request(API + path, data=json.dumps(payload).encode("utf-8"),
                                 headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:  # noqa
        return -1, str(e)


def patch(path, payload):
    req = urllib.request.Request(API + path, data=json.dumps(payload).encode("utf-8"),
                                 headers=HEADERS, method="PATCH")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:  # noqa
        return -1, str(e)


def rt(text, bold=False, code=False, size=None, color=None):
    ann = {}
    if bold:
        ann["bold"] = True
    if code:
        ann["code"] = True
    if size:
        ann["font_size"] = size
    if color:
        ann["color"] = color
    o = {"type": "text", "text": {"content": text}}
    if ann:
        o["text"]["annotations"] = ann
    return o


def para(text=None, bold=False, code=False, children=None):
    blk = {"object": "block", "type": "paragraph",
           "paragraph": {"rich_text": [rt(text, bold, code)] if text else []}}
    if children:
        blk["paragraph"]["children"] = children
    return blk


def head(text, level=2):
    k = f"heading_{level}"
    return {"object": "block", "type": k, k: {"rich_text": [rt(text)]}}


def bullet(text):
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [rt(text)]}}


def divider():
    return {"object": "block", "type": "divider", "divider": {}}


def callout(text, icon="📺", color="blue_background"):
    return {"object": "block", "type": "callout",
            "callout": {"rich_text": [rt(text)], "icon": {"type": "emoji", "emoji": icon},
                        "color": color}}


def quote(lines, color=None):
    out = []
    for i, ln in enumerate(lines):
        if i:
            out.append(rt("\n"))
        out.append(rt(ln))
    q = {"object": "block", "type": "quote", "quote": {"rich_text": out}}
    if color:
        q["quote"]["color"] = color
    return q


def table(headers, rows):
    ch = [{"object": "block", "type": "table_row",
           "table_row": {"cells": [[rt(h, bold=True)] for h in headers]}}]
    for r in rows:
        ch.append({"object": "block", "type": "table_row",
                   "table_row": {"cells": [[rt(str(c))] for c in r]}})
    return {"object": "block", "type": "table",
            "table": {"table_width": len(headers), "has_column_header": True,
                      "has_row_header": False, "children": ch}}


def embed(file_upload_id, caption):
    return {"object": "block", "type": "embed",
            "embed": {"url": f"file-upload://{file_upload_id}", "caption": [rt(caption)]}}


# ---------- 解析 HTML ----------
def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", s).strip()


def parse_cards(html):
    """从 .cards 里抽 5 个指标卡的 k / v / d。"""
    out = []
    for m in re.finditer(r'<div class="card">(.*?)</div>\s*(?=<div class="card">|</div>)',
                         html, re.S):
        blk = m.group(1)
        k = re.search(r'<div class="k">(.*?)</div>', blk, re.S)
        v = re.search(r'<div class="v"[^>]*>(.*?)</div>', blk, re.S)
        d = re.search(r'<div class="d">(.*?)</div>', blk, re.S)
        if k and v:
            out.append((strip_tags(k.group(1)),
                        strip_tags(v.group(1)),
                        strip_tags(d.group(1))[:300] if d else ""))
    return out


def parse_meta(html):
    m = re.search(r'<div class="meta">(.*?)</div></div>', html, re.S)
    return strip_tags(m.group(1)) if m else ""


def parse_sub(html):
    m = re.search(r'<div class="sub">(.*?)</div>\s*\n', html, re.S)
    return strip_tags(m.group(1)) if m else ""


def parse_items(html):
    """抽 .it 时间事项条目。"""
    out = []
    for m in re.finditer(r'<div class="it"><span class="tm">(.*?)</span><div class="ib">'
                         r'<b class="t">(.*?)</b>(.*?)</div></div>', html, re.S):
        tm, title, body = m.group(1), strip_tags(m.group(2)), strip_tags(m.group(3))
        out.append((tm.strip(), title, body[:900]))
    return out


def parse_boxes(html):
    """抽问题与阻塞的 box。"""
    out = []
    for m in re.finditer(r'<div class="box b-\w+"><div class="t">(.*?)</div>(.*?)</div>\s*(?=<div class="box|<h)',
                         html, re.S):
        title = strip_tags(m.group(1))
        body = strip_tags(m.group(2))
        st = ""
        sm = re.search(r"当前状态.{0,30}?——(.*)", body)
        if sm:
            st = sm.group(1)[:120]
        out.append((title, body[:800], st))
    return out


def parse_kv_table(html, after):
    """从 <h2>「after」标题之后取第一张表（跳过卡片区里的小标题同名匹配）。"""
    m = re.search(r"<h2>(?:<span[^>]*>.*?</span>)?" + re.escape(after), html)
    i = m.start() if m else -1
    if i < 0:
        return [], []
    j = html.find("<table", i)
    if j < 0:
        return [], []
    k = html.find("</table>", j)
    seg = html[j:k]
    rows = re.findall(r"<tr>(.*?)</tr>", seg, re.S)
    hs, ds = [], []
    for ri, r in enumerate(rows):
        cells = [strip_tags(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)]
        if not cells:
            continue
        if ri == 0:
            hs = cells
        else:
            ds.append(cells)
    return hs, ds


def parse_ol(html, after):
    """从 <h2>「after」之后取第一个 <ol>/<ul> 列表。"""
    m = re.search(r"<h2>(?:<span[^>]*>.*?</span>)?" + re.escape(after), html)
    if not m:
        return []
    i = m.end()
    mo = re.search(r"<(ol|ul)>(.*?)</\1>", html[i:], re.S)
    if not mo:
        return []
    return [strip_tags(li) for li in re.findall(r"<li>(.*?)</li>", mo.group(2), re.S)]


def upload_html(path):
    st, res = post("/file_uploads", {
        "filename": os.path.basename(path),
        "content_type": "text/html; charset=utf-8",
        "mode": "single_part",
    })
    if st >= 300:
        return None, f"create {st} {str(res)[:120]}"
    up_url = res["upload_url"]
    hdrs = dict(res.get("upload_headers") or {})
    boundary = "----wbboundary" + hashlib_str()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{os.path.basename(path)}"\r\n'
        f"Content-Type: text/html; charset=utf-8\r\n\r\n"
    ).encode("utf-8") + open(path, "rb").read() + f"\r\n--{boundary}--\r\n".encode("utf-8")
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    headers.update(hdrs)
    req = urllib.request.Request(up_url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            r.read()
    except Exception as e:  # noqa
        return None, f"put {e}"
    st, fin = post(f"/file_uploads/{res['id']}", {})
    if st >= 300:
        return None, f"finish {st} {str(fin)[:120]}"
    return res["id"], None


def hashlib_str():
    import hashlib
    return hashlib.md5(str(os.getpid() + time.time()).encode()).hexdigest()


# ---------- 主流程 ----------
def main():
    files = sorted(glob.glob(os.path.join(ROOT, "**", "日报-*.html"), recursive=True))
    print(f"found {len(files)} html files")

    for i, fp in enumerate(files, 1):
        base = os.path.basename(fp)[3:-5]  # 日报-YYYY-MM-DD.html -> YYYY-MM-DD
        y, m, d = base.split("-")
        dt = f"{y}-{m}-{d}"
        wd = WD[datetime_wd(y, m, d)]
        title = f"@{y}年{int(m)}月{int(d)}日的日报·周{wd}"

        html = open(fp, encoding="utf-8", errors="replace").read()

        # 1) 建记录
        st, pg = post("/pages", {
            "parent": {"type": "data_source_id", "data_source_id": DS},
            "properties": {"名称": {"title": [{"text": {"content": title}}]}},
            "icon": {"type": "emoji", "emoji": "📔"},
        })
        if st >= 300:
            print(f"[{i}/{len(files)}] {dt} CREATE FAIL {st} {str(pg)[:160]}")
            continue
        pid = pg["id"]

        # 2) 上传 HTML
        fid, err = upload_html(fp)
        if fid is None:
            print(f"[{i}/{len(files)}] {dt} UPLOAD FAIL {err}")

        # 3) 组装内容
        cards = parse_cards(html)
        meta = parse_meta(html)
        sub = parse_sub(html)
        items = parse_items(html)
        boxes = parse_boxes(html)
        _, ongoing = parse_kv_table(html, "进行中")
        tomorrow = parse_kv_table(html, "明日计划")[1]
        if not tomorrow:
            tomorrow = [[t] for t in parse_ol(html, "明日计划")]

        blocks = [callout(f"**screenpipe 屏幕记录自动归纳** · {dt} · "
                          f"源文件 `{os.path.basename(fp)}` · 时长均为约 / 估算值，"
                          f"无录制时段如实标注为缺，不编造、不内插。")]

        if cards:
            blocks.append(head("核心指标", 2))
            blocks.append(table(["指标", "数值", "说明"],
                                [[c[0], c[1], c[2]] for c in cards]))
        if meta:
            blocks.append(quote([meta], color="gray_background"))
        if sub:
            blocks.append(head("当日主线", 2))
            blocks.append(quote([sub[:1500]]))

        if items:
            blocks.append(head("今日完成", 2))
            for tm, ttl, body in items[:20]:
                blocks.append(bullet(f"**{tm}** {ttl} — {body[:400]}"))

        if ongoing:
            blocks.append(head("进行中", 2))
            blocks.append(table(["事项", "当前进展", "还差什么"],
                                [r[:3] for r in ongoing[:8]]))
        if boxes:
            blocks.append(head("问题与阻塞", 2))
            for t, b, stt in boxes:
                blocks.append(quote([f"**{t}**", b[:700]]))
        if tomorrow:
            blocks.append(head("明日计划", 2))
            if len(tomorrow[0]) >= 3:
                blocks.append(table(["#", "计划", "依据 / 跟进"],
                                    [r[:3] for r in tomorrow[:12]]))
            else:
                for j, row in enumerate(tomorrow[:12], 1):
                    blocks.append(bullet(f"{j}. {row}"))

        blocks.append(divider())
        blocks.append(head("原始报告（暗色卡片版）", 2))
        if fid:
            blocks.append(callout("下方为原始 HTML 报告原文嵌入，保留暗色卡片、"
                                  "四色状态标签与进度条的完整排版；上方文本层可搜索、可引用。",
                                  icon="🖼", color="gray_background"))
            blocks.append(embed(fid, f"{dt} 原始 HTML 报告"))
        else:
            blocks.append(para("（HTML 上传失败，此处留空）"))

        st, res = patch(f"/blocks/{pid}/children", {"children": blocks})
        print(f"[{i}/{len(files)}] {dt} {title} -> {'OK' if st < 300 else str(res)[:160]}")
        time.sleep(0.4)


def datetime_wd(y, m, d):
    import datetime
    return datetime.date(int(y), int(m), int(d)).weekday()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""补灌：清空并重写使用旧版模板的 6 篇日报（09-10 ~ 09-17）。"""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
exec(open("tmp_import_daily.py", encoding="utf-8").read().split("def main():")[0])


def datetime_wd(y, m, d):
    import datetime
    return datetime.date(int(y), int(m), int(d)).weekday()


TARGETS = ["2026-09-10", "2026-09-11", "2026-09-12",
           "2026-09-15", "2026-09-16", "2026-09-17"]

# 建立 标题 -> page_id 映射
index = {}
for p in query_all():
    index[title_of(p)] = p["id"]

for dt in TARGETS:
    y, m, d = dt.split("-")
    title = f"@{y}年{int(m)}月{int(d)}日的日报·周{WD[datetime_wd(y, m, d)]}"
    pid = index.get(title)
    if not pid:
        print("MISS", dt)
        continue
    fp = [p for p in glob.glob(os.path.join(ROOT, "**", f"日报-{dt}.html"), recursive=True)][0]
    html = open(fp, encoding="utf-8", errors="replace").read()

    cards = parse_legacy_cards(html) or parse_cards(html)
    items = parse_items(html)
    boxes = parse_boxes(html)
    _, ongoing = parse_kv_table(html, "进行中")
    tomorrow = parse_kv_table(html, "明日计划")[1] or [[t] for t in parse_ol(html, "明日计划")]
    print(f"{dt}: cards={len(cards)} items={len(items)} boxes={len(boxes)} "
          f"ongoing={len(ongoing)} tomorrow={len(tomorrow)}")

    # 清空现有内容
    st, ch = get(f"/blocks/{pid}/children?page_size=100")
    kids = [b["id"] for b in ch.get("results", [])] if isinstance(ch, dict) else []
    for k in kids:
        patch(f"/blocks/{k}", {"archived": True})
    time.sleep(0.3)

    fid, err = upload_html(fp)
    if err:
        print("  upload fail", err)

    blocks = [callout(f"**screenpipe 屏幕记录自动归纳** · {dt} · "
                      f"源文件 `日报-{dt}.html` · 时长均为约 / 估算值，"
                      f"无录制时段如实标注为缺，不编造、不内插。")]
    if cards:
        blocks.append(head("核心指标", 2))
        blocks.append(table(["指标", "数值", "说明"], [[c[0], c[1], c[2]] for c in cards]))
    meta = parse_meta(html)
    if meta:
        blocks.append(quote([meta], color="gray_background"))
    sub = parse_sub(html)
    if sub:
        blocks.append(head("当日主线", 2))
        blocks.append(quote([sub[:1500]]))
    if items:
        blocks.append(head("今日完成", 2))
        for tm, ttl, body in items[:20]:
            blocks.append(bullet(f"**{tm}** {ttl} — {body[:400]}"))
    if ongoing:
        blocks.append(head("进行中", 2))
        blocks.append(table(["事项", "当前进展", "还差什么"], [r[:3] for r in ongoing[:8]]))
    if boxes:
        blocks.append(head("问题与阻塞", 2))
        for t, b, stt in boxes:
            blocks.append(quote([f"**{t}**", b[:700]]))
    if tomorrow:
        blocks.append(head("明日计划", 2))
        if len(tomorrow[0]) >= 3:
            blocks.append(table(["#", "计划", "依据 / 跟进"], [r[:3] for r in tomorrow[:12]]))
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

    st, res = patch(f"/blocks/{pid}/children", {"children": blocks})
    print(f"  -> {'OK' if st < 300 else str(res)[:200]}")
    time.sleep(0.4)

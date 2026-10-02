# -*- coding: utf-8 -*-
"""清理「📔 日报」库：删测试页与同标题重复页（保留 blocks 最多的那条）。"""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = open("tmp_import_daily.py", encoding="utf-8").read().split("def main():")[0]
exec(src)

rows = query_all()
print("清理前页数:", len(rows))

groups = {}
for p in rows:
    t = title_of(p)
    pid = p["id"]
    if t.startswith("__TEST") or t == "":
        print("trash test/empty", pid, repr(t))
        trash(pid)
        continue
    groups.setdefault(t, []).append(pid)

for t, pids in groups.items():
    if len(pids) <= 1:
        print("keep  ", pids[0], t)
        continue
    scored = []
    for pid in pids:
        st, ch = get(f"/blocks/{pid}/children?page_size=100")
        n = len(ch.get("results", [])) if isinstance(ch, dict) else 0
        scored.append((n, pid))
    scored.sort(reverse=True)
    keeper = scored[0][1]
    for n, pid in scored[1:]:
        print(f"trash dup ({n} blk) {pid} {t}")
        trash(pid)
    print(f"KEEP  ({scored[0][0]} blk) {keeper} {t}")

print("清理后页数:", len(query_all()))
for p in query_all():
    print("  ", p["id"], title_of(p))

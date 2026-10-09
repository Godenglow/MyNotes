#!/bin/bash
# 语雀 Java 全套笔记抓取脚本
export PATH="/c/Windows/System32:/usr/bin:/bin:/c/Users/29074/.workbuddy/binaries/PortableGit/versions/1.2.0/usr/bin"
BOOK_ID=19864958
OUT="/d/MyNotes/Du/_raw"
cd "$OUT" || exit 1

# 01-JavaSE (17章)
SLUGS="na23g2vnz7cgzzdi rw03xkpkadgaw7u7 gqhbqtrtg7ruutad ohod7qvxq1z36ocz qhagel2niihaqfl0 osb8y2l2q8urmtn9 hmquiuye1fg6irwy tpq5h36k7huw6lmg mqhcc1lh1m94713v cagtgrmuzx9ig14e rgb5uru34dzbwpse txtiia405xiq5g3k sl7071kp08h6zlwq qnodco6rtzwg62sg oh8efg7v4gfcuvbx piphoczi1zmhhduz cxnnnxpt8ubmiqle"
# 02-MySQL 03-JDBC 04-Web前端(3) 05-XML&JSON 06-JavaWeb 07-Ajax 08-Maven 09-MyBatis 10-Spring 11-SpringMVC 12-SpringBoot 13-MyBatis-Plus 14-TypeScript 15-Vue3 16-ElementPlus 17-Linux
SLUGS="$SLUGS uzw5g4gtnuew49yp cy7vu9zsa0gmpprp gr1diu uqkric lk3u4vr4uc1ekxbk anghr4 rd3n67sf9bnakih9 szlh0l hp5bllxqf7g9gmn5 udots9ngcd97pyui lyvg9x9hf3u22s7e myxi54xu063hgsl4 uwxe0halgc03tm93 qgp36l3entp30hp2 mt5sq6akfcx5fr5g vu082c yw2xscrz4thagw34 nurwunyse629kzwy"

FAILED=""
for slug in $SLUGS; do
  if [ -f "$slug.json" ] && [ -s "$slug.json" ]; then
    echo "SKIP $slug (already exists)"
    continue
  fi
  for attempt in 1 2 3; do
    curl -sS "https://www.yuque.com/api/docs/$slug?book_id=$BOOK_ID&mode=markdown" \
      -H "Accept: application/json" -H "User-Agent: Mozilla/5.0" \
      -o "$slug.json" --max-time 90
    # 校验是否为有效 JSON 且含 sourcecode
    if grep -q '"sourcecode"' "$slug.json" 2>/dev/null; then
      size=$(wc -c < "$slug.json")
      echo "OK $slug ($size bytes, attempt $attempt)"
      break
    else
      echo "RETRY $slug (attempt $attempt invalid)"
      sleep 2
      if [ "$attempt" = "3" ]; then FAILED="$FAILED $slug"; fi
    fi
  done
  sleep 0.3
done

echo "=== DONE ==="
if [ -n "$FAILED" ]; then
  echo "FAILED SLUGS:$FAILED"
else
  echo "ALL OK"
fi
ls "$OUT"/*.json | wc -l

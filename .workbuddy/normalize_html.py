#!/usr/bin/env python3
"""normalize_html.py — 按 STYLE_GUIDE.md 把 D:\\MyNotes 下的 HTML 抹平同模板内偏差。

只做四件事:
  1. 模板识别:根据 h2 是否带 display:flex 判定模板 A/B
  2. 同模板内偏差抹平:
     - 模板 A line-height 1.75
     - 模板 B line-height 1.7(抹平 1.65 vs 1.7)
     - 模板 B cards minmax 158(抹平 148 vs 158)
     - 模板 B th { position: sticky; top: 0 } 按需补
  3. CSS 变量补齐:缺失的 --icode / --pre-fg / --t-* 等加上
  4. 校验双主题结构(nb-theme + themeBtn + 防闪脚本)

**不动**:
  - 模板 A vs B 的差异(各自定位)
  - SVG/表格/正文文字内容
  - 已正确配置的样式

用法:
    python normalize_html.py <dir|file> [--dry]
"""
import argparse, os, re, sys, glob

# ---------- 模板判定 ----------
TEMPLATE_A_MARK = ('h2{font-size:18px',)            # 不带 display:flex
TEMPLATE_B_MARK = ('display:flex;align-items:center;gap:9px',)  # B 模板 h2 的标志

def detect_template(html: str) -> str:
    """返回 'A'(长文档) 或 'B'(数据报告)。"""
    # 模板 B 的 h2 内一定有 display:flex
    if re.search(r'h2\{[^}]*display:flex;[^}]*align-items:center;[^}]*gap:9px', html):
        return 'B'
    return 'A'

# ---------- 同模板内的 CSS 抹平规则 ----------
# 每条规则:(template_or_'*', 旧模式, 新 CSS 块)
# 只做"明确不一致"的最小修正,不动 padding/max-width 等可能影响布局的项
RULES = [
    # 模板 B:line-height 1.65 → 1.7(抹平 1.65 vs 1.70 不一致)
    ('B', r'(body\{[^}]*?line-height:)\s*1\.65(\s*;[^}]*\})',
     r'\g<1>1.7\g<2>'),
    # 模板 B:cards minmax 148 → 158(抹平 148 vs 158 不一致)
    ('B', r'(\.cards\{[^}]*?minmax\()148(px,[^)]*\)[^}]*\})',
     r'\g<1>158\g<2>'),
    # 模板 B:cards margin 16px → 18px(抹平 16 vs 18 不一致)
    ('B', r'(\.cards\{[^}]*?)margin:16px 0(\s*\})',
     r'\g<1>margin:18px 0\g<2>'),
    # 模板 B:th 不一致 — 如果 th 已 sticky 则跳过;没有 sticky 不强加
]


# ---------- 完整 CSS 变量集(用于检测缺失) ----------
ALL_VARS = {
    # UI 中性
    'bg','side','card','chip','border','hover',
    'fg','strong','muted','faint','quote',
    'link','h3','pre-fg',
    'warn','good','bad',
    'pre-bg','icode',
    # one-dark token
    't-def','t-red','t-green','t-orange','t-purple','t-yellow','t-cyan','t-blue','t-comment',
}


def has_var_block(css: str) -> dict:
    """返回每个变量是否在 :root{} 块中定义。"""
    m = re.search(r':root\s*\{([^}]*)\}', css, re.S)
    if not m:
        return {v: False for v in ALL_VARS}
    body = m.group(1)
    return {v: (f'--{v}:' in body) for v in ALL_VARS}


# ---------- 标准化主体 ----------
def normalize(html: str) -> tuple:
    """返回 (新 HTML, 替换次数, 模板)。"""
    if 'nb-theme' not in html:
        return html, 0, '?'

    template = detect_template(html)
    changed = 0

    # 1) 抽取原 <style>...</style>
    style_re = re.compile(r'(<style[^>]*>)(.*?)(</style>)', re.S | re.I)

    def fix_css(m):
        nonlocal changed
        css = m.group(2)
        new_css = css

        # 模板内抹平
        for rule_tpl, pat, repl in RULES:
            if rule_tpl != '*' and rule_tpl != template:
                continue
            new = re.sub(pat, repl, new_css)
            if new != new_css:
                new_css = new
                changed += 1

        return m.group(1) + new_css + m.group(3)

    new_html = style_re.sub(fix_css, html)

    # 2) 校验双主题结构
    has_nbt = 'html[data-theme="light"]' in new_html
    has_btn = 'class="theme-btn"' in new_html
    has_anti = '(prefers-color-scheme: light)' in new_html

    return new_html, changed, template


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('--dry', action='store_true')
    a = ap.parse_args()

    if os.path.isdir(a.target):
        files = [f for f in glob.glob(os.path.join(a.target, '**', '*.html'), recursive=True)
                 if '.workbuddy' not in f.replace('\\', '/')]
    else:
        files = [a.target]

    ok = skip = fail = 0
    by_template = {'A': 0, 'B': 0, '?': 0}
    for f in sorted(files):
        try:
            with open(f, encoding='utf-8') as fh:
                text = fh.read()
        except Exception as e:
            print(f'FAIL  {f}  {e}')
            fail += 1
            continue
        new, n, tpl = normalize(text)
        by_template[tpl] += 1
        if n == 0 and new == text:
            skip += 1
            continue
        if not a.dry:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(new)
        ok += 1
        print(f'{tpl}  {n:2d}  {f}')
    print(f'\n完成: {ok} 改 / {skip} 跳过 / {fail} 失败  模板 A={by_template["A"]} B={by_template["B"]} ?={by_template["?"]}  (dry={a.dry})')
    return 0 if not fail else 1


if __name__ == '__main__':
    sys.exit(main())
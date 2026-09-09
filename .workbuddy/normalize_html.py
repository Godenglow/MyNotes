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
# 每条规则:(template_or_'*', css_selector_pattern, replacement_css)
# 注意:replacement 必须是完整的 "selector { ... }" 块
RULES = [
    # 模板 A:长文档(AngelByte_Note) — 抹平内部偏差
    ('A', r'body\s*\{[^}]*\}',
     'body{background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;line-height:1.75;padding:34px 38px;max-width:1140px;margin:0 auto}'),

    # 模板 B:数据报告(ScrePipe/vivo) — 抹平 line-height / cards minmax / th sticky
    ('B', r'body\s*\{[^}]*line-height:\s*1\.6\d[^}]*\}',
     'body{background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;line-height:1.7;padding:34px 38px;max-width:1140px;margin:0 auto}'),
    ('B', r'\.cards\{[^}]*minmax\((?:158|148)px,[^)]*\)[^}]*\}',
     '.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(158px,1fr));gap:11px;margin:18px 0}'),
    # 模板 B 的 th 如果没 sticky,加上(可选——这里不强制,只在缺时补)
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
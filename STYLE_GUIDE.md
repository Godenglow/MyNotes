# D:\MyNotes 笔记样式规范

> 适用范围:`D:\MyNotes\AngelByte_Note\`、`D:\MyNotes\ScrePipe日报\`、`D:\MyNotes\vivo健康\` 下所有 HTML 笔记文件。
> 制定时间:2026-09-09
> 配套脚本:`normalize_html.py`(同目录)

---

## 0. 速查(选模板)

| 你是… | 用哪个模板 |
|---|---|
| 课程笔记、技术文档、长教程(章节多 / 代码块多) | **模板 A:长文档** |
| 日报、周报、月报、数据分析(图表 / 异常提示多) | **模板 B:数据报告** |

两套模板的**基础规范完全一致**,只在字号 / 行高 / 间距 / 特色组件上有差。**不要混搭**——同一文件只能属于一种模板。

---

## 1. 基础规范(三套模板通用)

### 1.1 字体

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
               "Microsoft YaHei", sans-serif;
}
code, pre, .codehilite, kbd, samp {
  font-family: "Cascadia Code", Consolas, "JetBrains Mono", monospace;
}
```

- 中文优先 PingFang SC / Microsoft YaHei
- 英文优先系统 UI 字体(-apple-system 系列,免安装、无字体下载)
- 代码用 Cascadia Code / Consolas / JetBrains Mono

### 1.2 颜色与双主题

所有颜色**必须**走 CSS 变量,**禁止**在 body 内联 `style="color:#xxx"`(除 hero 统计卡片数字以外,见 1.5)。

变量定义(`<style>` 内,所有文件统一):

```css
:root{
  --bg:#0d1117; --side:#010409; --card:#161b22; --chip:#21262d;
  --border:#262d38; --hover:#10161f;
  --fg:#e6edf3; --strong:#f0f6fc; --muted:#8b949e; --faint:#6e7681; --quote:#b6c2cf;
  --link:#58a6ff; --h3:#79c0ff; --pre-fg:#c9d1d9;
  --warn:#d29922; --good:#3fb950; --bad:#f85149;
  --pre-bg:#282c34;
  --icode:#bc8cff;          /* 行内 code 紫 */
  --t-def:#abb2bf; --t-red:#e06c75; --t-green:#98c379; --t-orange:#d19a66;
  --t-purple:#c678dd; --t-yellow:#e5c07b; --t-cyan:#56b6c2; --t-blue:#61afef;
  --t-comment:#7f848e;
}
html[data-theme="light"]{
  --bg:#ffffff; --side:#f6f8fa; --card:#f6f8fa; --chip:#eff2f5;
  --border:#d0d7de; --hover:#eef1f4;
  --fg:#1f2328; --strong:#1f2328; --muted:#57606a; --faint:#8c959f; --quote:#57606a;
  --link:#0969da; --h3:#0550ae; --pre-fg:#24292f;
  --warn:#9a6700; --good:#1a7f37; --bad:#cf222e;
  --pre-bg:#f6f8fa;
  --icode:#8250df;
  --t-def:#24292f; --t-red:#cf222e; --t-green:#116329; --t-orange:#953800;
  --t-purple:#8250df; --t-yellow:#9a6700; --t-cyan:#0550ae; --t-blue:#0550ae;
  --t-comment:#6e7781;
}
```

**主题切换**:`html` 元素 `data-theme="dark"` / `"light"`。
- 默认:**跟随系统** `prefers-color-scheme`
- 用户手动切换按钮:右下角圆形 `☀️` / `🌙`,持久化到 `localStorage('nb-theme')`
- 切换时 reload 页面(让 mermaid 重渲染)+ `sessionStorage('nb-scroll')` 恢复滚动位置

> 实现细节见 `md-to-dark-html` skill。SVG 图表的 `fill` / `stroke` **也必须**用 CSS 变量(由 `inject_theme.py` 自动替换)。

### 1.3 标题层级

- 每个文件**只能有一个 `<h1>`**(文档主标题)
- 章节用 `<h2>`(章)/ `<h3>`(节)/ `<h4>`(小节),**不要跳级**
- h2 下沿用细 border 隔开:
  ```css
  h2 { border-bottom: 1px solid var(--border); padding-bottom: 8-9px; }
  ```
- h3 在长文档里加色强调(`color:var(--h3)`),数据报告里不加(让正文更显平稳)

### 1.4 列表

- 用 markdown 原生 `-` / `1.`
- 嵌套缩进 2 字符
- 列表项之间不强制空行(密集型)
- 任务列表 `- [ ]` / `- [x]` → ☐ / ☑

### 1.5 卡片 / 统计数字

```css
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(<N>px, 1fr)); gap: 11px; }
.card  { background: var(--card); border: 1px solid var(--border); border-radius: 9px; padding: 12px 14px; }
.card .k { color: var(--muted); font-size: 12px; }
.card .v { font-size: 22-26px; font-weight: 700; line-height: 1.3; margin: 4px 0; }
.card .d { color: var(--muted); font-size: 11.5-12px; }
```

`.card .v`(大数字)**允许**用内联 `style="color:#58a6ff"` 等(用 4 个标准强调色,见 1.6),但**禁止**写死 hex 让浅色变不见——用 `filter:brightness(.72) saturate(1.5)` 兜底或直接用 CSS 变量。

### 1.6 强调色板(只允许用这 6 个)

| 用途 | dark hex | light hex | 变量 |
|---|---|---|---|
| 主链接 / 主数据 | `#58a6ff` | `#0969da` | `--link` |
| 警告 / 待改进 | `#d29922` | `#9a6700` | `--warn` |
| 正常 / 达标 | `#3fb950` | `#1a7f37` | `--good` |
| 异常 / 风险 | `#f85149` | `#cf222e` | `--bad` |
| 次要强调(青色) | `#39c5cf` | `#0550ae` | `--h3` |
| 行内 code / 紫色 | `#bc8cff` | `#8250df` | `--icode` |

### 1.7 代码块 / 行内 code

**行内 code**:
```css
code { background: var(--chip); padding: 1-1.5px 5-6px; border-radius: 4px;
       font-size: 12-12.5px; color: var(--icode);
       font-family: "Cascadia Code", Consolas, "JetBrains Mono", monospace; }
```

**代码块**(由 markdown pygments 插件生成):
- 背景 `var(--pre-bg)`
- 卡片样式 `background: var(--pre-bg); border: 1px solid var(--border); border-radius: 9px;`
- 行高 `1.62`(紧凑)
- 暗色模式用 pygments **one-dark** 主题
- 浅色模式用 pygments **default** 主题,通过 `html[data-theme="light"] .codehilite { ... }` 前缀提高特异性
- 悬停右上角复制按钮(默认隐藏,hover 显示)

### 1.8 引用 blockquote

```css
blockquote {
  border-left: 3px solid var(--link);
  background: var(--card);
  border-radius: 0 8px 8px 0;
  padding: 10px 16px;
  margin: 13px 0;
  color: var(--quote);
  font-size: 13.5px;
}
```

### 1.9 表格

```css
table { width: 100%; border-collapse: collapse; font-size: <按模板>; margin: 11px 0; }
th    { color: var(--muted); font-weight: 600; font-size: <按模板>; background: var(--card); }
td    { border-bottom: none; background: var(--card); }
```

**长表头 sticky**(数据报告里的"逐日"表可加):
```css
th { position: sticky; top: 0; z-index: 1; }
```

### 1.10 图片 / SVG

- `<img>` 最大宽 100%,最大高 540px,圆角 6px
- `<svg>` 内联图表用 `width:100%;height:auto;display:block`,**`fill` / `stroke` 必须用 CSS 变量**
- `<svg>` 内文字 `fill="var(--muted)"` / `var(--strong)` / `var(--good)` 等
- 远程图床挂了的占位(imgur 上游已删)在卡片上标注"本地 x / 远程 y"

---

## 2. 模板 A:长文档(AngelByte_Note)

适用于:课程笔记、技术教程、含大量代码块的文档。

```css
body     { line-height: 1.75; }
h1       { font-size: 21px; font-weight: 700; }
h2       { font-size: 18px; font-weight: 680; margin: 30px 0 12px; padding-bottom: 8px;
           border-bottom: 1px solid var(--border); }
h3       { font-size: 15.5px; font-weight: 660; margin: 22px 0 9px; color: var(--h3); }
p        { margin: 10px 0; font-size: 14px; }
code     { font-size: 12.5px; padding: 1.5px 6px; }
.cards   { minmax(150px, 1fr); margin: 22px 0 6px; }
table    { font-size: 13px; }
th       { font-size: 12px; }
```

**必备组件**:
- **hero**(顶部标题卡):含主标题 / 副标题 / 章节统计 / 代码块数 / 图片数 / 图表数
- **左侧目录**(章节多时):固定 220px,滚动高亮当前章,顶部含过滤框
- **codehilite**:每段代码带复制按钮
- **TOC 自动滚动 spy**

---

## 3. 模板 B:数据报告(ScrePipe + vivo)

适用于:日报 / 周报 / 月报 / 数据分析报告(图表密集、异常提示多)。

```css
body     { line-height: 1.7; }
h1       { font-size: 26px; font-weight: 700; letter-spacing: -.4px; }
h2       { font-size: 19px; font-weight: 650; margin: 34-38px 0 14px; padding-bottom: 9px;
           border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 9px; }
h3       { font-size: 15px; font-weight: 620; margin: 22px 0 9px; }
p        { margin: 4px 0; }
code     { font-size: 12px; padding: 1px 5px; }
.cards   { minmax(158px, 1fr); margin: 18px 0; }
table    { font-size: 12.5px; }
th       { font-size: 11.5px; }
```

**必备组件**:

```css
.box {
  border-left: 3px solid; border-radius: 0 7px 7px 0;
  padding: 11px 15px; margin: 13px 0;
  background: var(--card); font-size: 13.5px;
}
.box.b-warn { border-color: var(--warn); }
.box.b-bad  { border-color: var(--bad); }
.box.b-good { border-color: var(--good); }
.box .t     { font-weight: 700; margin-bottom: 6px; }

.chart {
  background: var(--card); border: 1px solid var(--border); border-radius: 9px;
  padding: 14px 12px 8px; margin: 13px 0;
}

.tag { display: inline-block; padding: 1px 7px; border-radius: 20px;
       font-size: 11px; font-weight: 600; }
.tag.t-warn { background: rgba(210,153,34,.15); color: var(--warn); }
.tag.t-bad  { background: rgba(248,81,73,.15);  color: var(--bad); }
.tag.t-good { background: rgba(63,185,80,.15);  color: var(--good); }
.tag.t-ok   { background: rgba(63,185,80,.15);  color: var(--good); }
```

- **box**(异常提示框):左 border 颜色区分 warn/bad/good,可放 `.t`(标题)+ 任意说明
- **chart**(SVG 卡片):所有内联 SVG 用此包裹,统一内边距
- **tag**(状态标签):圆角胶囊,3 色

---

## 4. 应用方式

### 4.1 自动规范化

跑一遍 `normalize_html.py`:
```bash
PY="C:/Users/29074/.workbuddy/binaries/python/envs/default/Scripts/python.exe"
"$PY" D:/MyNotes/.workbuddy/normalize_html.py "D:/MyNotes" [--dry]
```

作用:
1. 校验每个文件属于哪种模板(检测 `h2` 是否带 `display:flex` → 模板 B)
2. 同模板内的轻微偏差抹平(line-height、cards minmax、th 是否 sticky 等)
3. 补齐缺失的 CSS 变量定义(让所有文件包含完整变量集)
4. 校验双主题结构(nb-theme + themeBtn + 防闪脚本)

**不动**:
- 模板 A 与模板 B 之间的差异(各自定位不同,不应合并)
- `<style>` 内已有但未被调用的旧变量
- SVG 内容、表格内容、文字内容(只动 CSS,不改正文)

### 4.2 新建文件

- **课程笔记 / 技术文档** → 用 `md-to-dark-html` skill 生成(默认模板 A)
- **日报 / 数据分析** → 用现有 `日报-YYYY-MM-DD.html` 复制后改日期/内容
- **新增图表** → 用 `<div class="chart">` 包裹,SVG `fill` / `stroke` 用 CSS 变量

### 4.3 维护清单

- 修改规范前:先在 1 个文件试改,确认无误再批量
- 备份:任何批量改动前必须先 `cp -r D:/MyNotes D:/MyNotes/.workbuddy/backup_<TS>/`
- 验证:`verify_theme.py`(同目录)扫全库

---

## 5. 历史

- 2026-09-09:三套 HTML 调研完成,制定本规范
  - 调研脚本:`_audit_templates.py` / `_audit_css.py`
  - 模板 A(长文档)= `00-JavaSE` `04-MySQL` 等课程笔记
  - 模板 B(数据报告)= `ScrePipe日报/*` `vivo健康/*`
  - 基础规范(字体/颜色/代码块/表格/引用/双主题)三套已统一,无需改
  - normalize 仅抹平同模板内的偏差,不动跨模板差异
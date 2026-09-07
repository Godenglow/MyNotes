# Workspace Memory — D:\MyNotes\AngelByte_Note

## 用户笔记的处理偏好

- 用户用 **Obsidian** 浏览这些 .md 笔记。
- 用户在意"格式乱用 / 代码块没识别"——所以格式清理要按 Obsidian 兼容来做
  (空行统一、列表符号统一、`<br/>` 当作分隔去掉、嵌套列表不能误伤)。
- 不轻易改用户的 emoji 标题(`## 🌊 xxx`)——他没说要改。

## 已有脚本(2026-08-27 创建)

- `.workbuddy/scripts/format_notes.py`:批量格式化 .md,跑前会自动跳过 .workbuddy/ 目录,
  改动覆盖原文件。备份目录格式:`.workbuddy/notes_backup_<YYYYMMDD_HHMMSS>/`。
- 用法:`python .workbuddy/scripts/format_notes.py`,产出 `.workbuddy/format_report.md`。

## 不要踩的坑

- 备份是**手工**用 PowerShell `Get-ChildItem` + `Copy-Item` 做的,不要让脚本删 .workbuddy。
- 文件很大(最大 ~430KB),用 Python 一次跑完没问题,但**永远先备份再覆盖**。
- 散装代码(=无围栏缩进代码)在这批文件里**几乎都是嵌套列表**,不要强行围栏化。

## md → 深色 HTML 转换体系（2026-09-07 起）

- 笔记夹"大改"方向：md 笔记 → 深色 GitHub 风格 HTML（#0d1117 卡片风），转完删源 md。
- 已沉淀为用户级 skill `md-to-dark-html`（~/.workbuddy/skills/），脚本 `scripts/md2dark_html.py`，
  用法/规则/边界/删除流程全在 SKILL.md，触发词"笔记转 HTML / md 转网页"。
- 已完成（2026-09-07）：全部 18 个 HTML 就位——根目录 9 个、00-JavaSE 2 个、10-Redis 3 个
  （基础篇/注释版/课程介绍；快速入门因被基础篇完全覆盖已删）、11-RMQ（23 碎片合并）、12-Seata。
  09-Docker/Docker.md 为 192B 存根，按用户决定不转。源 md 已删，备份在 .workbuddy/notes_backup_*。
- 一键重生成：`.workbuddy/scripts/regen_all.py`（从备份重建 18 个 HTML + RMQ 重合并）；
  终验脚本 `.workbuddy/scripts/verify_fixes.py`（断图/rel/占位三重校验）。
- venv（C:/Users/29074/.workbuddy/binaries/python/envs/default）已装 markdown + pygments，勿全局装。
- 10-Radis/（拼错目录）已删：182 文件与 10-Redis 逐文件 MD5 全同，纯冗余。

## skill md-to-dark-html v2 要点（2026-09-07）

- skill 自带 `assets/mermaid.min.js`（2.9MB, mermaid 10.9.1），**默认内联**进 HTML → 离线可渲染，不再依赖 CDN。
- 参数：路径必须 `D:/...` 风格；`--mermaid auto|inline|copy|cdn`；`--embed-dir` 可多次。
- 三个必须保持的修复：同名图加序号防覆盖 / title 走 clean_title+escape / 首个 h1 是主标题时跳过。
- 无 h1 的 md（如 Seata）→ 单章不渲染标题条，属预期导航退化。

## 库结构（2026-09-07 图片本地化后）

- 根目录 9 个课程笔记各自独立文件夹：`<名>/<名>.html + assets/`（如 01-HTML+CSS/）。
- 全库图片已本地化（1017 张下载，0 外链）；imgur 58 处为死链占位（上游已删）。
- 完整管线：regen_all.py → localize_images.py → verify_fixes.py（顺序执行，均幂等）。

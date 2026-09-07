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
- 已完成：00-JavaSE（JavaSE.html，源 md 已删）。候选：01-HTML+CSS、02-Java Web、03-JDBC、04-MySQL、
  05-MVC、06-Mybatis、07-Spring6、08-SpringMVC、Git.md、09-Docker、10-Redis、11-RMQ、12-Seata。
- venv（C:/Users/29074/.workbuddy/binaries/python/envs/default）已装 markdown + pygments，勿全局装。

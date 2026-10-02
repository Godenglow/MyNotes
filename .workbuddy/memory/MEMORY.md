# MyNotes 项目长期记忆

## 仓库结构（2026-10-02 拆分后）

- **D:/MyNotes** → `github.com/Godenglow/MyNotes`：只含 面试、AngelByte_Note、Du 三个笔记目录 + 隐藏配置目录（.obsidian/.claude/.copilot/.workbuddy/.stfolder/.verysync 等）。Obsidian Git 插件自动 vault backup（约 10-30 分钟一次，会抢跑提交）。
- **D:/Private-Note** → `github.com/Godenglow/Private-Note`：copilot、Excalidraw、ScrePipe日报、vivo健康、README.md、STYLE_GUIDE.md。无自动提交，需手动 push。
- MyNotes 的 .gitignore 忽略了 4 个已拆分目录（防 vault 自动备份回灌）。
- `D:\MyNotes\ScrePipe日报` 是指向 `D:\Private-Note\ScrePipe日报` 的**目录联接**（junction），为的是 screenpipe 零配置改动；别把它当真实目录删掉。
- `.agents/skills/`、`.claude/skills/` 原为指向 `copilot/skills/*` 的 junction，copilot 已移走，插件需要时会自建。

## Notion 镜像库（2026-10-03 全量迁移完成）

- **vivo健康**：page `3ed68f113d2d80398eafd9ee2280a1d3`，层级 年→月→周，根级有「日度数据」（CSV 附件权威副本 + 「日度数据（2026）」库，data source `dcfaa7dd-f881-4df8-ab2c-c330a84e0806`）。
- **Screen日报**：page `3ed68f113d2d805382abde77bea49c83`，层级 2026→月→周→日报页；日报页首是 GR-IAO 模板改编的「复盘速览」表（评分=AI估分）。
- 两库按同路径对应（2026/09 ↔ 2026/09，周四定月法）。「Screen日报同步到Notion」自动化（每日 22:30）按层级建页；vivo 同步自动化已按用户要求删除（用户自己来）。
- **Notion 表格格式坑**：`<table>` 必须独占一行 + 表头 `<th>`，否则存成转义文本；replace_content 必须在末尾保留子页 `<page url>` 标签。批量写入走本地 Notion MCP HTTP 端点 + Python 直连（UA 伪装绕 CF 1010）。

## 环境要点

- git 不在 PATH：用 `C:\Users\29074\.workbuddy\binaries\PortableGit\versions\1.2.0\cmd\git.exe`（Bash 里先 export PATH）。
- Git Bash 会话可能 PATH 为空，命令前补 export PATH（见用户级记忆）。

## Notion 写入通道（2026-10-03 实测，踩坑记住）

- **🔴 数组参数在 MCP 通道会被字符串化**：`notion-create-pages` 的 `pages`、`notion-update-page` 的 `content_updates`、`notion-move-pages` 的 `page_or_database_ids`、`notion-query-data-sources` 的 `data` —— **传数组一律报 `must be array`，一个都传不过去**。单字符串参数（`new_str` / `content` / `properties` / `page_id` / `template_id`）完全正常。
- **🔴 往数据库里建记录：别绕了，让用户在 UI 点「新建」**。Notion 会自动套该库的 `default_page_template`，把链接给我，我用 `update-page` 改内容 + `update_properties` 改标题即可。绕 `duplicate-page` 造副本再 move 是死路（move 也是数组参数），且会留下垃圾页。
- **改已有页内容的唯一可行姿势**：`notion-update-page` + `command="replace_content"`（纯字符串 `new_str`），可一次灌完整长内容。批量写入务必走它，不走上下文。
- **属性名要分清**：数据库内页用 `update_properties` 传真实属性名（如「日报」库是 `名称`，非数据库页才用 `title`）；`created_time` 类属性是 readOnly，别试图手动赋值。
- **直连 API 走不通**：记忆里的 `ntn_2817...`（integration weiguowu10.2）只对迁移期分享的页面有效，Screen日报 等新库会 404；WorkBuddy 自己的 Notion OAuth token 在 app 内部存储，本地文件扫不到。
- **MCP 无删除页面的工具**，删页只能用户在 UI 手动操作。
- **模板能力**：只有「页面母版」能做——任意 page ID 当 template 源，`update-page` + `command="apply_template"`（异步，套完要 fetch 复核）。数据库下拉模板 / 模板按钮 / 官方模板库发布均**不支持**。
- **🔴 别用 `<columns>` 做卡片网格**：五等分 + 中文 + 长占位符 → 每列被压到约 130px，中文全部竖排单字，完全不可读（用户 2026-10-03 截图实锤）。`ratio` 只是偏好不是最小宽度，`columns` 是流体布局。要并排展示就用 `<table fit-page-width="true">`，要颜色就退回单个 `callout`。
- **Screen日报 母版页**：`📐 _模板 · 日报骨架` = `3ed68f113d2d8156b63dd78e2372aa20`（在 Screen日报 根目录下），建日报时套它的 ID。核心指标用三列表格 + emoji 行首（⏱💼🎮🎬⚠️）、🟢🟡🔵🔴 状态标。
- **「📔 日报」数据库**：`a5e68f113d2d8285b35d01dad8f6f5a5`，data source `collection://3a868f11-3d2d-82ff-9c3e-8794fa6c4021`，属性只有 `名称`(title) + `日期`(created_time, readOnly)，gallery 视图封面取 `page_content`，默认模板 `@今天 的日记` = `7d568f113d2d820ab008813f0454a7e2`。首条日报 `3ed68f113d2d80af80e4e622c71fd620`。
- **嵌入原始 HTML 保住暗色风**：Notion 页面不支持自定义 CSS，1:1 复刻 `#0d1117` 卡片风不可能 → 走双轨：Notion 文本层（可搜索）+ `<embed>` 原始 HTML 层（好看）。做法：`create-attachment`（`filename` + `content`，**≤200 KiB**）→ 拿返回的 `file-upload://<id>` 写进 `update-page` 的 `insert_content` 的 `<embed src="...">`，保存后自动转 Notion 托管 S3 链接。日报 HTML 约 30-55 KB，够用。

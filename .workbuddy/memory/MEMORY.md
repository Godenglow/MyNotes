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

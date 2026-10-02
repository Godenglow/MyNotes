# MyNotes 项目长期记忆

## 仓库结构（2026-10-02 拆分后）

- **D:/MyNotes** → `github.com/Godenglow/MyNotes`：只含 面试、AngelByte_Note、Du 三个笔记目录 + 隐藏配置目录（.obsidian/.claude/.copilot/.workbuddy/.stfolder/.verysync 等）。Obsidian Git 插件自动 vault backup（约 10-30 分钟一次，会抢跑提交）。
- **D:/Private-Note** → `github.com/Godenglow/Private-Note`：copilot、Excalidraw、ScrePipe日报、vivo健康、README.md、STYLE_GUIDE.md。无自动提交，需手动 push。
- MyNotes 的 .gitignore 忽略了 4 个已拆分目录（防 vault 自动备份回灌）。
- `D:\MyNotes\ScrePipe日报` 是指向 `D:\Private-Note\ScrePipe日报` 的**目录联接**（junction），为的是 screenpipe 零配置改动；别把它当真实目录删掉。
- `.agents/skills/`、`.claude/skills/` 原为指向 `copilot/skills/*` 的 junction，copilot 已移走，插件需要时会自建。

## 环境要点

- git 不在 PATH：用 `C:\Users\29074\.workbuddy\binaries\PortableGit\versions\1.2.0\cmd\git.exe`（Bash 里先 export PATH）。
- Git Bash 会话可能 PATH 为空，命令前补 export PATH（见用户级记忆）。

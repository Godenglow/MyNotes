---
title: screenpipe memories
tags:
  - screenpipe
  - memory
---

## screenpipe memories

Auto-synced by screenpipe from this user's local memory store. These are durable facts and preferences observed across the user's screens and meetings. Treat them as ambient context for Obsidian, not as a task list.

### 用户画像

- 用户 Godenglow，大四软件工程专业学生（2026-09 起大四上），位于中国江西（就读新余学院）。 _(src: agent-profile · #user-profile)_
- 中文（简体）交流；结论前置、结构化输出（编号/表格/代码块）；需要可执行步骤而非空泛建议；选择类问题给推荐 + 理由。 _(src: agent-profile · #preference)_
- 偏好便携化工具链：便携 Git（未进 PATH）、Watt Toolkit（MITM 代理 GitHub）、PixPin 截图、npm 安装的 Claude Code CLI、Obsidian + Copilot 插件（Claude 笔记内对话）。应用统一装 D 盘。 _(src: agent-profile · #environment)_

### 本机环境（Windows 11，用户名 29074）

- 代理内核 clash.meta（mihomo），混合端口 127.0.0.1:7890；2026-09-01 起由 Clash Verge Rev 2.5.2 接管（Service Mode + TUN，Mihomo 网卡 198.18.0.1，混合端口 7897），EdgeGo 已退役（profile 备份在 D:\Apps\clash-verge-rev\EdgeGo-kept）。 _(src: agent-profile · #environment #proxy)_
- 排查限制（踩坑结论）：PowerShell 工具不回传 stdout（写文件再读）；reg.exe/wmic.exe 不可用（用 PowerShell 注册表提供程序）；Add-Type 被拦；删文件用 Bash 的 rm 而非 Remove-Item；tasklist/wevtutil 输出 GBK 需 iconv。 _(src: agent-profile · #troubleshooting)_
- API 账户：DeepSeek（付费，已开自动充值）+ Zhipu bigmodel.cn（GLM-4-flash 等免费档常用）。 _(src: agent-profile · #api)_

### 进行中的长期项目（截至 2026-09-04）

- **ScrePipe日报**（本项目）：screenpipe 自动工作日报体系，目录 年/月/周(自然周) 三级，HTML 格式，规则见 `D:/MyNotes/ScrePipe日报/说明文件.html`。 _(src: manual · #daily-report)_
- **QQ AI Bot**：NapCatQQ-Desktop + AstrBot Desktop（WebUI :6185 / 反向 WS :6199 / NapCat :6099），DeepSeek API 驱动，全链路 2026-09-02 跑通；《QQ AI Bot 项目全景》手册已定稿，收尾 4 项 + bot-projects 备份未完成。项目目录 `D:\Projects\bot-projects\`。 _(src: agent-profile · #qq-bot)_
- **AUTO-MAS**（明日方舟自动化）：未决问题 = 启动时把 submodule repo/ 同步覆盖到 app/ 导致手写修复被还原（2026-09-02 定位根因，修复未实施）；基线漂移 v5.4.0/a227c8d vs 文档 v5.5.0-beta.1/7a62b56。 _(src: agent-profile · #auto-mas)_
- **Java 学习**：2026-08-31 复习至第三章面向对象（JavaSE Q&A 笔记约 4.5k 字），第四章未开始；大四课程 + 毕设主线。 _(src: agent-profile · #study)_
- **家用服务器**：计划旧笔记本装 Ubuntu Server 22.04 + Docker + Cloudflare Tunnel（毕设后端公网访问），Trae Solo 已生成命令清单，未实操；备选 N100 小主机。 _(src: agent-profile · #homelab)_

### 日报格式偏好（daily-work-report pipe）

- 每日工作日报的文本要点部分要尽量详细（保留完整时间段，含文件/笔记标题、字数、版本号、错误码、具体步骤与产出，便于日后回忆）；每个部分仍附带 Markdown 表格统计但保持精简：表格去掉时间段列、加"时长（约）"与"占比"列（今日完成：序号|事项|时长（约）|占比；进行中：事项|当前进展|还差什么；问题与阻塞：现象|时长（约）|占比|状态；游戏娱乐：游戏|时长（约）|占比|类型|说明 + 其他娱乐：类别|时长（约）|占比；明日计划：序号|计划|依据/跟进），表末给"小计/合计"（项数、合计时长、状态分布），占比为该项占对应部分合计时长的比例（约）。表格须 Obsidian 兼容：列头用"序号"而非"#"，单元格内容保持简短（长描述留在要点列表），表内不出现未转义的竖线，表格前后必须各空一行（Obsidian 不识别紧贴段落后面的表格）。 _(src: agent-profile · #user-profile #daily-report #preference #format)_
- 2026-09-04 起日报落盘为 **HTML**（非 md）：`ScrePipe日报/{年}/{月}/第N周(MM.DD-MM.DD)/日报-{Date}.html`，周 = 自然周（周一~周日，跨月归多数天数所在月，8 月为 4 周）；每周文件夹含 周总结.html，每月文件夹含 月度总结.html；样式对齐 vivo健康数据分析报告（暗色 #0d1117 卡片风）。 _(src: manual · #daily-report #format #structure)_

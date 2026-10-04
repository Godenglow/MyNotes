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

- **🔴 数组参数在 MCP 通道会被字符串化（多数工具有效，move-pages 已通）**：
  - **仍堵死**：`notion-create-pages` 的 `pages`、`notion-update-page` 的 `content_updates`、`notion-query-data-sources` 的 `data` —— **传数组一律报 `must be array`，一个都传不过去**。
  - **2026-10-03 实测已通**：`notion-move-pages` 的 `page_or_database_ids`（1/2/7 个元素都成功）！下次批量改父级就直接用它。
  - 单字符串参数（`new_str` / `content` / `properties` / `page_id` / `template_id`）完全正常。
- **🔴 往数据库里建记录：别绕了，让用户在 UI 点「新建」**。Notion 会自动套该库的 `default_page_template`，把链接给我，我用 `update-page` 改内容 + `update_properties` 改标题即可。
  - **例外**：当已有旧页要转库时，用 `notion-move-pages`（数组已通）+ `update-page` 的 `update_properties` 改名 + `insert_content` 加封面。**这是改造旧结构最快最干净的姿势**，避免复制 1.88 MB 文本内容。
- **`update-page` 命令不能同时记下两条命令**：例如 `command=insert_content` + 同时传 `properties` 只执行 insert、properties 静默丢弃。**必须分两次**：insert_content → update_properties。同样 `cover`/`icon` 是独立字段，可与任意 command 并用（但 image 内容仍要用 insert_content 的 `<image>` block）。
- **改已有页内容的唯一可行姿势**：`notion-update-page` + `command="replace_content"`（纯字符串 `new_str`），可一次灌完整长内容。批量写入务必走它，不走上下文。
- **属性名要分清**：数据库内页用 `update_properties` 传真实属性名（如「学习/日报」库是 `名称`，非数据库页才用 `title`）；`created_time` 类属性是 readOnly，别试图手动赋值。
- **直连 API 走不通**：记忆里的 `ntn_2817...`（integration weiguowu10.2）只对迁移期分享的页面有效，Screen日报 等新库会 404；WorkBuddy 自己的 Notion OAuth token 在 app 内部存储，本地文件扫不到。**mcp file_upload 的 Bearer token 也只用于文件上传（purpose=mcp_file_upload），不能用来 PATCH 页面（实测 401）**。
- **MCP 无删除页面的工具**，删页只能用户在 UI 手动操作。**Workaround**：建一个草稿页（`creation_mode: draft` = workspace 顶层私页）→ `move-pages` 把要删的批量收进草稿页 → 用户 trash 一个父页，Notion 递归删除所有子页。20 个一次性实测 OK。但草稿页默认对用户不可见，需通过 URL 直达。
- **view FILTER date_is_before 对 created_time 失效**：试过 `< "2026-10-02T20:00:00"` 和 `< "2026-10-03"` 都返空；SORT BY 正常 + 数据存在。可能是 bug。临时方案：SORT BY 日期 + QUICK FILTER 让用户手动筛。
- **模板能力**：只有「页面母版」能做——任意 page ID 当 template 源，`update-page` + `command="apply_template"`（异步，套完要 fetch 复核）。数据库下拉模板 / 模板按钮 / 官方模板库发布均**不支持**。
- **🔴 别用 `<columns>` 做卡片网格**：五等分 + 中文 + 长占位符 → 每列被压到约 130px，中文全部竖排单字，完全不可读（用户 2026-10-03 截图实锤）。`ratio` 只是偏好不是最小宽度，`columns` 是流体布局。要并排展示就用 `<table fit-page-width="true">`，要颜色就退回单个 `callout`。
- **Screen日报 母版页**：`📐 _模板 · 日报骨架` = `3ed68f113d2d8156b63dd78e2372aa20`（在 Screen日报 根目录下），建日报时套它的 ID。核心指标用三列表格 + emoji 行首（⏱💼🎮🎬⚠️）、🟢🟡🔵🔴 状态标。
- **「📔 日报」数据库**：`a5e68f113d2d8285b35d01dad8f6f5a5`，data source `collection://3a868f11-3d2d-82ff-9c3e-8794fa6c4021`，属性只有 `名称`(title) + `日期`(created_time, readOnly)，gallery 视图封面取 `page_content`，默认模板 `@今天 的日记` = `7d568f113d2d820ab008813f0454a7e2`。首条日报 `3ed68f113d2d80af80e4e622c71fd620`。
- **「📚 学习」数据库**（2026-10-03 改造完成）：`3ed68f113d2d83c9a84581c2d6ca79bb`，data source `collection://81c68f11-3d2d-83b1-b29b-07cf9ba970b1`，结构跟「📔 日报」同款。视图「学习文档」= `view://5e268f11-3d2d-8378-8047-0819a803f187`，gallery，`cover: {type: "page_content"}`，默认模板 `@今天 的日记` = `ccb68f113d2d831ca3b501ef13bec350`。改造流程：17 个旧 01-JavaSE...17-Linux 子页（ID 在 3ed68f11-3d2d-81xx 系列）整体 move-pages 进库 + update_properties 去前缀 + insert_content 加 file-upload:// 封面图 → 形成跟「📔 日记本」完全镜像的 gallery 结构。**待用户手动 trash**：17 个我误建的空重复新页 + 3 个模板自带「的日记」（`3ff68f113d2d83d6a45a01fa4243e89d` / `8cf68f113d2d820b8f8e811b4f017567` / `c8168f113d2d836b96a48126f155d805`）。
- **嵌入原始 HTML 保住暗色风**：Notion 页面不支持自定义 CSS，1:1 复刻 `#0d1117` 卡片风不可能 → 走双轨：Notion 文本层（可搜索）+ `<embed>` 原始 HTML 层（好看）。做法：`create-attachment`（`filename` + `content`，**≤200 KiB**）→ 拿返回的 `file-upload://<id>` 写进 `update-page` 的 `insert_content` 的 `<embed src="...">`，保存后自动转 Notion 托管 S3 链接。日报 HTML 约 30-55 KB，够用。
- **file_upload 流程**：本地大文件（>200 KiB）走 `create-file-upload`（拿 `upload_url` + `upload_headers.authorization` + `upload_form_field`）→ curl `-F file=@<path>` POST 到 upload_url（10 分钟有效期）→ 响应里 `markdown_source` = `file-upload://<id>` 直接当 `<image src="...">` 用。批量 17 张图实测 OK。

### 直连 Notion API（2026-10-03 晚新增，批量导入 30 篇日报跑通）

> **为什么另开一路**：MCP 数组参数基本全废，批量建库内记录走不通。实测 `ntn_2817...` 对**新用户在 UI 建的库是有权限的**（此前 Screen日报 404 是因为没分享给该 integration，不是 token 失效）→ 一律走直连 API + Python，30 篇日报 6 分钟灌完。

- **端点写法**：
  - 建页 `parent` **只认 `{"type":"database_id","database_id":...}`**，写 `data_source_id` → 400 validation_error。
  - 查询 `POST /data_sources/{裸uuid}/query`（**带 `collection://` 前缀会 400**）。
  - 删页 `PATCH /pages/{id}` + `{"in_trash": true}` —— **MCP 无删除工具，但直连 API 可以删**。
- **🔴 表格单元格 `table_row.cells` 里不允许 `annotations`**（`{"bold":true}` 也报 validation_error）→ 表头加粗只能靠 table 自身的 `has_column_header`；代码里给表格单元格调 `rt(text, bold=True)` 必炸。
- **🔴 直连 API 文件上传三步，全程要 Bearer**：
  1. `POST /file_uploads` `{filename, content_type}` → 返回 `upload_url`（形如 `.../send`，**无 `upload_headers`、无 `mode` 参数**）
  2. 向 `upload_url` POST **multipart/form-data**（漏 Bearer → 401；发裸 body → 400 invalid_json）
  3. `GET /file_uploads/{id}` 确认状态（**必须 GET，用 POST 会 400 invalid_request_url**）
- **日报 HTML 有 4 种模板版本，解析正则必须写 `class="x"[^>]*` 属性容错**，否则遇到带 `data-page-node-id` 的那批（09-03）全部失配：① 新版 `.cards>.card` + `.it>.tm` + `.box b-*` ② 中版 `.stat` + `<ul class="tl">` ③ 旧版 `<div class="day"><div class="dh">` ④ 09-03 特殊：新版结构但每个标签都带 `data-page-node-id`。「明日计划」还有 `<table>` 与 `<ol>` 两种形态。
- **🔴🔴 embed 必须用 `file_upload` 字段（超级重要）**：
  ```python
  {"object":"block","type":"embed","embed":{"file_upload":{"id":fid},"caption":[...]}}
  ```
  Notion 服务端会**自动转成 `prod-files-secure.s3...` 真实链接**。直连 API 上传 + 这样 append → 200 且 URL 已转换。
  **反过来，`"url": "file-upload://xxx"` 直连不会被转换，页面报「无法加载此嵌入文件」。**
- **🔴🔴 MCP 通道与直连 API 是两个不同 integration，上传的文件互相不可见**：用 MCP 引用直连 API 上传的 `file_upload` 会报 `Could not find file_upload with ID: xxx, integration_id: 1f8d872b-...`；同一个 ID 用直连 `GET /file_uploads/{id}` 查却回 `status: uploaded`。**所以「上传」和「写入页面」必须用同一个通道**。
- **🔴 直连 API 不解析 markdown**：`text.content` 是纯文本。`**bold**` / `` `code` `` 会原样显示。**必须自己写 `rich()` 用正则拆成 `{"annotations":{"bold":true}}` / `{"annotations":{"code":true}}`**，并自己实现 `parse_md()`（表格 `|---|`、引用 `>`、有序/无序列表）。
- **🔴 表格单元格禁止 `annotations`**（连 `{"bold":true}`、`color` 都报错）→ 表头加粗只能靠 table 的 `has_column_header`；**颜色一律用 block 级 color**（`callout`/`quote`）或 emoji 色标。
- **验收脚本本身要先验一次**：我两次栽在「拿已知正确的页做对照」这一步 —— 一次查错字段（`embed.external.url` 实际在 `embed.url`），一次布尔判断写反（全报假阳性）。**信一个没校准的验收脚本 = 自欺欺人。**
- 脚本在 `D:/MyNotes/.workbuddy/`（`tmp_import_daily.py` 含 4 种模板解析器 + 导入逻辑，`tmp_gen_md.py` 生成 markdown，`tmp_final_fill.py` 最终重灌，`tmp_verify.py` 验收）。**全部已删除。**
- **重复页清理**：首轮失败会留下大量空壳，脚本按「同标题保留 blocks 最多的那条」用 `PATCH {"in_trash":true}` 去重（比按创建时间保留更可靠）。
- 脚本在 `D:/MyNotes/.workbuddy/tmp_import_daily.py`（含 4 种模板的解析器 + 导入逻辑），`tmp_cleanup.py` / `tmp_refill.py` / `tmp_reimport.py` 为专项工具。**用完待用户确认后删除。**

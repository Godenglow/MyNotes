# Git 完整笔记

> 来源：[菜鸟教程 - Git 教程](https://www.runoob.com/git/git-tutorial.html)
> 整理日期：2026-08-27
> 适用：Obsidian 阅读

---

## 目录

1. [Git 简介](#一-git-简介)
2. [Git 与 SVN 区别](#二-git-与-svn-的区别)
3. [Git 工作流程](#三-git-工作流程)
4. [Git 安装与配置](#四-git-安装与配置)
5. [Git 工作区、暂存区和版本库](#五-git-工作区暂存区和版本库)
6. [Git 创建仓库](#六-git-创建仓库)
7. [Git 基本操作](#七-git-基本操作)
8. [Git 分支管理](#八-git-分支管理)
9. [Git 查看提交历史](#九-git-查看提交历史)
10. [Git 标签](#十-git-标签)
11. [Git Flow 工作流](#十一-git-flow-工作流)
12. [Git 远程仓库（GitHub）](#十二-git-远程仓库github)
13. [Git 远程仓库（Gitee）](#十三-git-远程仓库gitee)
14. [Git 服务器搭建](#十四-git-服务器搭建)
15. [Git GUI 使用方法](#十五-git-gui-使用方法)
16. [Git 常用命令速查](#十六-git-常用命令速查)

---

## 一、Git 简介

- **Git** 是一个开源的 **分布式版本控制系统**，用于敏捷高效地处理任何或小或大的项目。
- Git 是 **Linus Torvalds** 为了帮助管理 **Linux 内核开发** 而开发的一个开放源码的版本控制软件。
- Git 与常用的版本控制工具 CVS、Subversion 等不同，它采用了 **分布式版本库** 的方式，不必服务器端软件支持。

---

## 二、Git 与 SVN 的区别

Git 不仅仅是个版本控制系统，它也是个内容管理系统（CMS）、工作管理系统等。

| 特性 | Git | SVN |
| --- | --- | --- |
| 架构 | **分布式** | 集中式 |
| 存储方式 | 按 **元数据** 存储 | 按 **文件** 存储 |
| 分支 | 分支开销极低，是核心功能 | 分支就是版本库中的另一个目录 |
| 全局版本号 | **没有** | 有 |
| 内容完整性 | 使用 **SHA-1 哈希算法** | 相对较弱 |

**五大核心差异：**

1. **Git 是分布式的，SVN 不是** —— 这是 Git 与 SVN 最核心的区别。
2. **Git 把内容按元数据方式存储，SVN 是按文件** —— 元信息隐藏在 `.svn`、`.cvs` 等文件夹中。
3. **Git 分支和 SVN 的分支不同** —— 分支在 SVN 中就是个普通目录。
4. **Git 没有全局版本号，SVN 有** —— 这是 Git 相对 SVN 缺少的最大特征。
5. **Git 的内容完整性优于 SVN** —— 使用 SHA-1 哈希算法确保完整性。

---

## 三、Git 工作流程

下图展示了 Git 的工作流程（可想象为"写作业并交给老师"的过程）：

### 1. 工作区（Working Directory）—— 你的书桌

实际修改文件的地方。写代码、删删改改都在这里完成。

### 2. 暂存区（Staging Area）—— 待邮寄篮子

- 关键指令：`git add`
- 意义：告诉 Git，这些改动确认要提交，先帮忙记着。

### 3. 本地仓库（Local Repository）—— 个人保险箱

- 关键指令：`git commit`
- 意义：改动正式成为项目历史的一部分。

### 4. 远程仓库（Remote）—— 老师的收件箱（如 GitHub/GitLab）

- 关键指令：`git push`
- 意义：备份代码，与团队共享进度。

**辅助知识点：**

- `git stash`（贮藏区）：作业写一半要改别的急活，可把代码藏进抽屉，忙完再 `pop` 出来。
- `git pull`：从远程拉取更新同步到本地。
- `git fetch & merge`：先查看远程更新（`fetch`），确认后再合并（`merge`）。

**简单总结：** 修改代码 → `add`（放篮子）→ `commit`（存箱子）→ `push`（寄远方）。

### 完整工作流命令

```bash
# 1. 克隆仓库
git clone https://github.com/username/repo.git
cd repo

# 2. 创建新分支
git checkout -b new-feature

# 3. 编辑文件

# 4. 暂存文件
git add filename   # 或 git add .

# 5. 提交更改
git commit -m "Add new feature"

# 6. 拉取最新更改
git pull origin main

# 7. 推送更改
git push origin new-feature

# 8. 在 GitHub 上创建 Pull Request（PR）

# 9. PR 审核通过合并后，同步主分支
git checkout main
git pull origin main
git merge new-feature

# 10. 删除分支
git branch -d new-feature
git push origin --delete new-feature
```

---

## 四、Git 安装与配置

### 1. Linux 平台安装

```bash
# Debian/Ubuntu
apt-get install git

# CentOS/RedHat
yum -y install git-core

# Fedora 21 及之前
yum install git

# Fedora 22 及之后
dnf install git

# FreeBSD
pkg install git

# OpenBSD
pkg_add git

# Alpine
apk add git
```

**源码安装：**

```bash
# 从 GitHub 克隆源码
git clone https://github.com/git/git

# 解压编译
$ tar -zxf git-1.7.2.2.tar.gz
$ cd git-1.7.2.2
$ make prefix=/usr/local all
$ sudo make prefix=/usr/local install
```

### 2. Windows 平台安装

- 下载地址：<https://gitforwindows.org/> 或 <https://git-scm.com/download/win>
- 双击安装包一路 Next
- 安装完成后可在开始菜单找到 **Git → Git Bash** 进行操作
- 包含 ssh 客户端和图形界面工具

```powershell
# 使用 winget 安装
winget install --id Git.Git -e --source winget
```

### 3. Mac 平台安装

```bash
# Homebrew 安装
brew install git

# 安装 git-gui 和 gitk
brew install git-gui

# 或下载图形化安装工具
# https://sourceforge.net/projects/git-osx-installer/
```

### 4. Git 配置（git config）

Git 配置可存放在三个不同位置：

| 范围 | 路径 | 参数 |
| --- | --- | --- |
| 系统级（所有用户） | `/etc/gitconfig` | `--system` |
| 用户级（当前用户） | `~/.gitconfig` | `--global` |
| 项目级（仅当前项目） | `.git/config` | 无 |

> 每一个级别的配置都会覆盖上层的相同配置。

**用户信息配置：**

```bash
git config --global user.name "runoob"
git config --global user.email test@runoob.com
```

**文本编辑器：**

```bash
git config --global core.editor "code --wait"   # VS Code
```

**差异分析工具：**

```bash
git config --global merge.tool vimdiff
```

> Git 可理解 kdiff3、tkdiff、meld、xxdiff、emerge、vimdiff、gvimdiff、ecmerge、opendiff 等合并工具。

**查看配置：**

```bash
git config --list
# 查阅某个变量
git config user.name
```

**生成 SSH 密钥：**

```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

**验证安装：**

```bash
git --version
git config --list
```

---

## 五、Git 工作区、暂存区和版本库

### 基本概念

- **工作区**：你在电脑里能看到的目录。
- **暂存区**：英文叫 stage 或 index。一般存放在 `.git` 目录下的 index 文件（`.git/index`）中。
- **版本库**：工作区有一个隐藏目录 `.git`，这个不算工作区，而是 Git 的版本库。

### 关系图说明

- 左侧为工作区，右侧为版本库。
- 标记为 `index` 的区域是暂存区（stage/index），标记为 `master` 的是 master 分支所代表的目录树。
- `HEAD` 实际是指向 master 分支的一个"游标"，可用 `master` 替换。
- `objects` 标识的区域为 Git 的对象库，实际位于 `.git/objects` 目录下。

### 关键操作对各区域的影响

| 操作 | 影响 |
| --- | --- |
| `git add` | 暂存区目录树被更新，对象库写入新对象，ID 记录到暂存区文件索引 |
| `git commit` | 暂存区目录树写入版本库，master 分支做相应更新 |
| `git reset HEAD` | 暂存区目录树被重写，被 master 分支指向的目录树替换（工作区不变） |
| `git rm --cached <file>` | 直接从暂存区删除文件（工作区不变） |
| `git checkout .` / `git checkout -- <file>` | 用暂存区全部或指定文件替换工作区文件（**会清除未暂存改动，危险**） |
| `git checkout HEAD .` / `git checkout HEAD <file>` | 用 HEAD 指向的 master 分支中的文件替换暂存区和工作区文件（**危险**） |

### 数据流转关系

```
工作区 → git add → 暂存区 → git commit → 本地版本库
                                     ↓ git push
                                远程仓库
                                     ↓ git pull / fetch
工作区 ← git merge ← 本地版本库
```

### 实例演示

```bash
# 1. 工作区：修改 file.txt
# 2. 暂存区
git add file.txt

# 3. 版本库
git commit -m "Update file.txt"

# 4. 远程仓库
git push origin main
```

---

## 六、Git 创建仓库

### 1. git init（初始化）

```bash
# 进入目标目录
mkdir my-project
cd my-project

# 当前目录初始化
git init

# 指定目录作为 Git 仓库
git init newrepo
```

> 执行完成后会在目录生成一个 `.git` 目录，包含资源的所有元数据。

**添加文件到版本控制：**

```bash
git add *.c
git add README
git commit -m '初始化项目版本'
```

> Linux 用单引号 `'`，Windows 用双引号 `"`。

### 2. git clone（克隆远程仓库）

```bash
# 克隆默认目录
git clone <repo>

# 克隆到指定目录
git clone <repo> <directory>

# 实例：克隆 Ruby 的 Git 仓库
git clone git://github.com/schacon/grit.git

# 自定义目录名
git clone git://github.com/schacon/grit.git mygrit
```

---

## 七、Git 基本操作

Git 的工作就是创建和保存项目快照及与之后的快照进行对比。

### 常用六大命令

`git clone`、`git push`、`git add`、`git commit`、`git checkout`、`git pull`

### 创建仓库命令

| 命令 | 说明 |
| --- | --- |
| `git init` | 初始化仓库 |
| `git clone` | 拷贝远程仓库（下载项目） |

### 提交与修改命令

| 命令 | 说明 |
| --- | --- |
| `git add` | 添加文件到暂存区 |
| `git status` | 查看仓库当前状态，显示有变更的文件 |
| `git diff` | 比较文件的不同（暂存区和工作区差异） |
| `git difftool` | 使用外部差异工具查看和比较 |
| `git range-diff` | 比较两个提交范围之间的差异 |
| `git commit` | 提交暂存区到本地仓库 |
| `git reset` | 回退版本 |
| `git rm` | 将文件从暂存区和工作区中删除 |
| `git mv` | 移动或重命名工作区文件 |
| `git notes` | 添加注释 |
| `git checkout` | 分支切换 |
| `git switch`（Git 2.23+） | 更清晰地切换分支 |
| `git restore`（Git 2.23+） | 恢复或撤销文件的更改 |
| `git show` | 显示 Git 对象的详细信息 |

### 提交日志命令

| 命令 | 说明 |
| --- | --- |
| `git log` | 查看历史提交记录 |
| `git blame <file>` | 以列表形式查看指定文件的历史修改记录 |
| `git shortlog` | 生成简洁的提交日志摘要 |
| `git describe` | 生成可读的字符串描述当前提交 |

### 远程操作命令

| 命令 | 说明 |
| --- | --- |
| `git remote` | 远程仓库操作 |
| `git fetch` | 从远程获取代码库 |
| `git pull` | 下载远程代码并合并 |
| `git push` | 上传远程代码并合并 |
| `git submodule` | 管理包含其他 Git 仓库的项目 |

### Git 文件状态

Git 的文件状态分为 **3 大区域、4 种状态**：

| 状态 | 说明 |
| --- | --- |
| 未跟踪（Untracked） | 新创建的文件，未被 Git 记录 |
| 已修改（Modified） | 已被 Git 跟踪的文件发生了更改，未提交 |
| 已暂存（Staged） | 修改已添加到暂存区，等待提交 |
| 已提交（Committed） | 暂存区内容提交到本地仓库 |

**状态转换流程：**

```bash
# 1. 未跟踪（Untracked）— 新建文件
touch newfile.txt
git status  # 显示未跟踪

# 2. 已跟踪（Tracked）— 添加到暂存区
git add newfile.txt

# 3. 已修改（Modified）— 改文件后
echo "Hello, World!" > newfile.txt
git status  # 显示已修改

# 4. 已暂存（Staged）— 重新添加
git add newfile.txt

# 5. 已提交（Committed）— 提交
git commit -m "Added newfile.txt"
```

---

## 八、Git 分支管理

Git 分支管理是 Git 强大功能之一，能让多个开发人员 **并行工作**，开发新功能、修复 bug 或进行实验，而不影响主代码库。

> 有人把 Git 的分支模型称为**必杀技特性**，正是因为它将 Git 从版本控制系统家族里区分出来。

**核心思想**：Git 分支实际上是指向更改快照的 **指针**。

### 1. 创建分支

```bash
# 创建并切换
git checkout -b feature-xyz

# 仅切换
git checkout main
```

> 切换分支时，Git 会用该分支的最后提交的快照替换你的工作目录内容。

### 2. 查看分支

```bash
git branch         # 本地分支
git branch -r      # 远程分支
git branch -a      # 所有本地和远程分支
```

### 3. 合并分支

```bash
git checkout main
git merge feature-xyz
```

### 4. 解决合并冲突

当合并过程中出现冲突时，Git 会标记冲突文件：

```bash
# 1. 手动编辑冲突文件
# 2. 标记冲突解决完成
git add <conflict-file>
# 3. 提交合并结果
git commit
```

### 5. 删除分支

```bash
git branch -d <branchname>              # 删除本地分支
git branch -D <branchname>              # 强制删除未合并分支
git push origin --delete <branchname>   # 删除远程分支
```

### 完整实例

```bash
$ mkdir gitdemo
$ cd gitdemo/
$ git init
$ touch README
$ git add README
$ git commit -m '第一次版本提交'
```

---

## 九、Git 查看提交历史

Git 提供了多个命令查看历史记录，常用 `git log` 系列。

```bash
# 查看历史提交记录
git log

# 简洁模式（每条一行）
git log --oneline

# 显示图形化分支历史
git log --graph

# 显示装饰（分支、标签）
git log --decorate

# 查看指定文件历史
git log -- <file>

# 查看指定作者的提交
git log --author="username"

# 查看指定时间范围的提交
git log --since="2026-01-01" --until="2026-08-27"

# 查看文件修改记录（追溯每行作者）
git blame <file>
```

---

## 十、Git 标签

> 当你达到一个重要的阶段，希望永远记住提交的快照时，可以使用 `git tag` 给它打上标签。

Git 标签（Tag）用于给仓库中的特定提交点加上标记，通常用于 **发布版本**（如 v1.0, v2.0）。

### 1. 创建标签

```bash
# 轻量标签
git tag v1.0

# 附注标签（推荐）— 包含创建者、日期、注释
git tag -a v1.0 -m "runoob.com标签"

# PGP 签名标签
git tag -s v1.0 -m "runoob.com标签"

# 给历史提交打标签
git tag -a v0.9 85fc7e7
```

> 不使用 `-a` 选项创建的标签为**轻量标签**，不会记录打标签时间、作者和注释。

### 2. 查看标签

```bash
# 列出所有标签
git tag

# 查看标签信息
git show v1.0

# 查看历史时显示标签
git log --decorate
```

### 3. 推送标签到远程

```bash
# 推送单个标签
git push origin v1.0

# 推送所有标签
git push origin --tags
```

> 默认情况下，`git push` 不会推送标签。

### 4. 删除标签

```bash
# 本地删除
git tag -d v1.0

# 远程删除
git push origin --delete v1.0
```

### 附注标签 vs 轻量标签

| 类型 | 存储信息 | 适用场景 |
| --- | --- | --- |
| 轻量标签 | 仅是提交的引用 | 临时标记 |
| 附注标签 | 创建者、日期、注释、PGP 签名 | 正式发布版本 |

---

## 十一、Git Flow 工作流

> Git Flow 是一种基于 Git 的 **分支模型**，由 Vincent Driessen 在 2010 年提出，旨在帮助团队更好地管理和发布软件。

### 1. 五类分支

| 分支 | 作用 | 命名规范 |
| --- | --- | --- |
| `master` | 永远保持稳定可发布状态，每次发布合并自 develop | — |
| `develop` | 集成所有开发分支，代表最新开发进度 | — |
| `feature` | 开发新功能，从 develop 创建，合并回 develop | `feature/feature-name` |
| `release` | 准备新版本发布，从 develop 创建，合并回 develop 和 master | `release/release-name` |
| `hotfix` | 修复紧急问题，从 master 创建，合并回 master 和 develop | `hotfix/hotfix-name` |

### 2. 安装 Git Flow

```bash
# Linux Debian/Ubuntu
sudo apt-get install git-flow

# Fedora
sudo dnf install gitflow

# macOS
brew install git-flow

# 源码安装
git clone https://github.com/nvie/gitflow.git
cd gitflow
sudo make install

# Windows (Git for Windows 自带 / Scoop / Chocolatey)
scoop install git-flow
choco install gitflow

# 验证
git flow version
```

### 3. 工作流程

**初始化：**

```bash
git flow init
```

**功能分支：**

```bash
git flow feature start feature-name
# 开发完成
git flow feature finish feature-name
```

**发布分支：**

```bash
git flow release start v1.0.0
# 测试和修复完成
git flow release finish v1.0.0   # 合并到 master 和 develop，打 Tag
```

**修复分支：**

```bash
git flow hotfix start hotfix-1.0.1
# 修复完成
git flow hotfix finish hotfix-1.0.1  # 合并到 master 和 develop，打 Tag
```

### 4. 优缺点

**优点：**

- 明确的分支模型，开发过程井然有序
- 隔离开发和发布，减少不确定性
- 每次发布和修复打上版本标签，方便回溯

**缺点：**

- 对于小型团队或简单项目过于复杂
- 频繁合并可能导致冲突增加

---

## 十二、Git 远程仓库（GitHub）

### 1. 什么是 GitHub

- **GitHub** 是一个基于 git 的代码托管平台，付费用户可建私人仓库，免费用户只能使用公共仓库。
- 由 Chris Wanstrath、PJ Hyett、Tom Preston-Werner 三位开发者在 **2008 年 4 月** 创办。
- 是拥有 143 万开发者的社区，全球最流行的开源托管服务，已托管 431 万 git 项目。
- alexa 全球排名 414 的网站。

### 2. SSH Key 配置

```bash
# 1. 生成 SSH Key
$ ssh-keygen -t rsa -C "your_email@youremail.com"
# 生成的公钥在 ~/.ssh/id_rsa.pub

# 2. 复制公钥内容，添加到 GitHub Account Settings → SSH and GPG keys → New SSH key

# 3. 验证连接
$ ssh -T git@github.com
# 成功提示：Hi username! You've successfully authenticated...
```

### 3. Git 配置

```bash
git config --global user.name "your name"
git config --global user.email "your_email@youremail.com"
```

### 4. 推送到 GitHub 完整流程

```bash
# 1. 在 GitHub 上 Create a New Repository（获得仓库地址）

# 2. 本地初始化
$ mkdir runoob-git-test
$ cd runoob-git-test/
$ echo "# 菜鸟教程 Git 测试" >> README.md
$ git init
$ git add README.md
$ git commit -m "添加 README.md 文件"

# 3. 添加远程地址并推送
$ git remote add origin git@github.com:yourName/yourRepo.git
$ git push -u origin master
```

### 5. 远程操作命令

```bash
# 查看当前远程库
git remote
git remote -v   # 显示实际链接地址

# 提取远程更新
git fetch                  # 仅下载，需要手动 merge
git merge origin/master    # 合并到当前分支

# 一步到位：下载并合并
git pull origin master

# 推送到远程
git push origin master

# 添加远程仓库
git remote add origin git@github.com:user/repo.git

# 删除远程仓库
git remote rm origin
```

### 6. Git 简明指南（核心命令一览）

```bash
# 检出仓库
git clone /path/to/repository
git clone username@host:/path/to/repository

# 添加与提交
git add <filename>
git add *
git commit -m "代码提交信息"

# 推送改动
git push origin master

# 关联远程服务器
git remote add origin <server>

# 分支操作
git checkout -b feature_x        # 创建并切换
git checkout master              # 切回主分支
git branch -d feature_x          # 删除分支
git push origin <branch>         # 推送到远端

# 更新与合并
git pull                         # 获取并合并远端改动
git merge <branch>               # 合并其他分支到当前
git diff <source> <target>       # 预览差异

# 标签
git tag 1.0.0 1b2e1d63ff         # 1b2e1d63ff 是提交 ID 前 10 位

# 替换本地改动
git checkout -- <filename>       # 用 HEAD 替换工作区文件
git fetch origin
git reset --hard origin/master   # 丢弃所有本地改动

# 实用小贴士
gitk                                          # 内建图形化 git
git config color.ui true                      # 彩色输出
git config format.pretty oneline              # 单行显示历史
git add -i                                    # 交互式添加文件
```

---

## 十三、Git 远程仓库（Gitee）

> Gitee（码云）是国内常用的 Git 代码托管平台，访问速度快，适合国内开发者。

**基本流程与 GitHub 类似：**

1. 注册 Gitee 账号：<https://gitee.com/>
2. 配置 SSH 公钥（同 GitHub）
3. 创建远程仓库
4. 本地关联推送

```bash
# 添加 Gitee 远程地址
git remote add gitee git@gitee.com:username/repo.git

# 推送到 Gitee
git push -u gitee master
```

**同时推送到 GitHub 和 Gitee（一个本地仓库多个远程）：**

```bash
# 添加两个远程
git remote add github git@github.com:user/repo.git
git remote add gitee git@gitee.com:user/repo.git

# 分别推送
git push github master
git push gitee master
```

---

## 十四、Git 服务器搭建

> GitHub 公开项目免费，2019 年起私有存储库也可无限制使用。也可自己搭建 Git 服务器作为私有仓库。

### 方案一：使用裸存储库（小型团队）

**1. 安装 Git 并创建用户：**

```bash
sudo apt install git
groupadd git
useradd git -g git
```

**2. 创建裸存储库：**

```bash
sudo su - git
cd /home
mkdir gitrepo
chown git:git gitrepo/
cd gitrepo
git init --bare runoob.git    # 通常以 .git 结尾
chown -R git:git runoob.git
```

**3. 配置证书登录：**

```bash
cd /home/git/
mkdir .ssh
chmod 755 .ssh
touch .ssh/authorized_keys
chmod 644 .ssh/authorized_keys
# 在 authorized_keys 中添加允许登录用户的公钥（一行一个）
```

**4. 克隆仓库：**

```bash
git clone git@192.168.45.4:/home/gitrepo/runoob.git
```

### 方案二：使用 GitLab（中大型团队）

GitLab 功能强大，适合中大型团队，提供用户管理、CI/CD、代码审查等功能。

**1. 安装 GitLab（Ubuntu）：**

```bash
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
sudo EXTERNAL_URL="http://yourdomain" apt-get install gitlab-ee
```

**2. 获取初始 root 密码：**

```bash
sudo cat /etc/gitlab/initial_root_password
```

**3. 生成 SSH 密钥对：**

```bash
ssh-keygen
cat .ssh/id_rsa.pub   # 复制公钥添加到 GitLab
```

**4. 配置使用 Git 仓库：**

```bash
git config --global user.name "testname"
git config --global user.email "abc@example.com"

# 克隆项目
git clone git@101.132.XX.XX:root/mywork.git
cd mywork/

# 上传文件
echo "test" > test.sh
git add test.sh
git commit -m "test.sh"
git push -u origin main
```

---

## 十五、Git GUI 使用方法

> 适合不熟悉命令行的初学者，10 分钟上手 Git。

### 1. 前期准备（一次性操作）

**Step 1：安装 Git**

- 下载地址：<http://git-scm.com/download/>

**Step 2：创建 SSH 密钥**

- 启动 GUI → 菜单 → 帮助 → 【Step1-创建密钥】Generate SSH KEY

**Step 3：添加密钥到代码托管服务器**

- 去 GitHub/GitLab 的账号设置中，添加公钥
- title 随意，如 Home、company

**Step 4：保存账号密码（避免每次提交都询问）**

- 4.1 添加环境变量：
  - 变量名：`HOME`
  - 变量值：`%USERPROFILE%`
- 4.2 在 `%Home%` 目录创建 `_netrc` 文件：

```
machine github.com
login your_username
password your_password
```

### 2. 日常操作流程

| 步骤 | 操作 | 说明 |
| --- | --- | --- |
| 初始化 | `Git init` | 新建项目，右键文件夹创建 |
| 添加 | `Git add` | 缓存改动，选择要提交的文件 |
| 忽略 | `.gitignore` | 忽略不需要提交的文件/文件夹 |
| 提交 | `Git commit` | 提交时必须写备注 |
| 上传 | `Git push` | 上传至远端服务器 |
| 获取 | `Git remote/fetch` | 设置关联并获取远程代码 |
| 合并 | `Git merge` | 将获取的改动合并到本地 |
| 冲突 | `Conflict` | GUI 中右键可选择 Use local/remote version |

### 3. .gitignore 忽略规则

将不需要提交的大文件、临时文件统一放在忽略文件夹中：

```
# 忽略 .psd 文件
*.psd

# 忽略临时文件夹
temp/
```

### 4. 冲突处理

合并时出现红色文件与叹号：

- 不需慌张，不是程序坏了，只是有冲突
- 在 GUI 界面正文区右键 → `Use local version`（用本地）或 `Use remote version`（用远程），或自己整合

---

## 十六、Git 常用命令速查

### 1. 配置与初始化

```bash
# 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 初始化本地仓库
git init
git init <dir>

# 克隆远程仓库
git clone <url>
git clone <url> <dir>
```

### 2. 提交与查看

```bash
git status                              # 查看仓库状态
git add <file>                          # 添加指定文件
git add .                               # 添加所有修改
git commit -m "提交说明"                # 提交到本地
git commit -a -m "提交说明"             # 提交所有已跟踪修改
git log                                 # 查看历史
git log --oneline --graph --decorate    # 图形化历史
git diff                                # 工作区 vs 暂存区
git diff --cached                       # 暂存区 vs 最后提交
git blame <file>                        # 文件历史
```

### 3. 撤销与回退

```bash
git checkout -- <file>                  # 撤销工作区修改
git reset HEAD <file>                   # 取消暂存
git reset --soft <commit_id>            # 回退（保留修改）
git reset --hard <commit_id>            # 回退（丢弃修改）
git rm --cached <file>                  # 从暂存区删除
```

### 4. 分支操作

```bash
git branch                              # 查看本地分支
git branch -r                           # 查看远程分支
git branch -a                           # 查看所有分支
git branch <name>                       # 创建分支
git checkout <name>                     # 切换分支
git checkout -b <name>                  # 创建并切换
git switch <name>                       # 切换分支（Git 2.23+）
git switch -c <name>                    # 创建并切换
git merge <name>                        # 合并分支
git branch -d <name>                    # 删除分支
git branch -D <name>                    # 强制删除
```

### 5. 远程操作

```bash
git remote -v                           # 查看远程仓库
git remote add <name> <url>             # 添加远程仓库
git remote rm <name>                    # 删除远程仓库
git fetch <name>                        # 从远程获取
git pull <name> <branch>                # 拉取并合并
git push <name> <branch>                # 推送到远程
git push -u origin master               # 首次推送并关联
git push origin --delete <branch>       # 删除远程分支
```

### 6. 标签操作

```bash
git tag                                 # 列出所有标签
git tag <name>                          # 创建轻量标签
git tag -a <name> -m "message"          # 创建附注标签
git tag -s <name> -m "message"          # PGP 签名标签
git tag -a <name> <commit>              # 给历史提交打标签
git show <tag>                          # 查看标签信息
git push origin <tag>                   # 推送单个标签
git push origin --tags                  # 推送所有标签
git tag -d <tag>                        # 删除本地标签
git push origin --delete <tag>          # 删除远程标签
```

### 7. Stash 暂存

```bash
git stash                               # 暂存当前修改
git stash list                          # 查看暂存列表
git stash pop                           # 恢复并删除
git stash apply                         # 恢复但不删除
git stash drop                          # 删除暂存
```

---

## 常见问题

### Q1：如何解决冲突？

当多个分支修改同一文件时，`git merge` 会产生冲突。需要手动编辑冲突文件（搜索 `<<<<<<<` 标记），然后 `git add` 标记为已解决，最后 `git commit` 提交。

### Q2：如何忽略文件？

在仓库根目录创建 `.gitignore` 文件：

```gitignore
# 忽略所有 .log 文件
*.log

# 忽略 node_modules 目录
node_modules/

# 不忽略 specific.log
!specific.log

# 忽略临时文件夹
temp/
*.tmp
```

### Q3：commit 信息用什么引号？

- **Linux 系统**：使用单引号 `'`
- **Windows 系统**：使用双引号 `"`

### Q4：Git 2.23+ 的 checkout / switch / restore 区别？

| 命令 | 用途 |
| --- | --- |
| `git checkout <branch>` | 切换分支（旧命令） |
| `git switch <branch>` | 切换分支（新命令，更清晰） |
| `git restore <file>` | 恢复文件（替代 checkout --） |

---

## 相关文章与资源

### 菜鸟教程

- [Git 五分钟教程](https://www.runoob.com/w3cnote/git-five-minutes-tutorial.html)
- [Git GUI 使用方法](https://www.runoob.com/w3cnote/git-gui-window.html)
- [GitHub 简明教程](https://www.runoob.com/w3cnote/git-guide.html)
- [Git 简明指南](https://www.runoob.com/manual/git-guide/)
- [PDF 命令手册](https://www.runoob.com/manual/github-git-cheat-sheet.pdf)

### 官方与社区

- [Git 官方文档](http://git-scm.com/docs)
- [GitHub](https://github.com/)
- [Gitee（码云）](https://gitee.com/)
- [GitLab](https://about.gitlab.com/)
- [图解 Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)
- [Pro Git 中文版](http://progit.org/book/)

### 图形化客户端

- [SourceTree](https://www.sourcetreeapp.com/)（免费）
- [GitHub Desktop](https://desktop.github.com/)
- [Git for Windows](https://gitforwindows.org/)
- Tower（OSX，付费）

---

#git #版本控制 #工具 #教程 #SVN #GitHub #Gitee #GitLab

# GitHub 仓库索引生成脚本

## 功能说明

基于 GitHub CLI (`gh`) 为你的所有 GitHub 仓库生成结构化索引，便于 AI 检索使用。

## 功能特性

- 自动获取所有 GitHub 仓库信息
- 生成 Markdown 和 JSON 两种格式的索引文件
- 包含仓库详细信息：描述、语言、stars、forks、许可证等
- 生成统计数据：仓库类型、语言分布等
- 可选获取 README 内容和文件结构
- 自动创建最新版本的符号链接

## 前置要求

1. 安装 GitHub CLI
   ```bash
   # macOS
   brew install gh

   # Linux
   # 参考 https://github.com/cli/cli#installation
   ```

2. 安装 jq (JSON 处理工具)
   ```bash
   # macOS
   brew install jq

   # Linux
   sudo apt-get install jq  # Debian/Ubuntu
   sudo yum install jq      # CentOS/RHEL
   ```

3. 登录 GitHub
   ```bash
   gh auth login
   ```

## 使用方法

### 基本用法

```bash
bash github-repo-idx.sh
```

### 高级用法

```bash
# 自定义输出目录
OUTPUT_DIR=./my-indexes bash github-repo-idx.sh

# 启用 README 获取（仅前10个仓库）
FETCH_README=true bash github-repo-idx.sh

# 启用文件结构获取（仅前5个仓库）
FETCH_STRUCTURE=true bash github-repo-idx.sh

# 组合使用
OUTPUT_DIR=./output FETCH_README=true bash github-repo-idx.sh
```

## 输出文件

脚本会在输出目录中生成以下文件：

1. **repo-index-TIMESTAMP.md** - Markdown 格式的索引文件
   - 包含仓库概览表格
   - 详细的仓库信息
   - 统计数据

2. **repo-index-TIMESTAMP.json** - JSON 格式的索引文件
   - 结构化的仓库数据
   - 适合程序化处理和 AI 工具集成

3. **符号链接**
   - `repo-index-latest.md` -> 指向最新的 Markdown 文件
   - `repo-index-latest.json` -> 指向最新的 JSON 文件

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `OUTPUT_DIR` | 输出目录路径 | `./repo-index` |
| `FETCH_README` | 是否获取 README 内容 | `false` |
| `FETCH_STRUCTURE` | 是否获取文件结构 | `false` |

## API 速率限制

脚本使用 GitHub API，需要注意以下限制：

- **GraphQL API**: 5000 次请求/小时
- **REST API**: 5000 次请求/小时

为避免超过 API 限制：
- 默认情况下不获取 README 和文件结构
- 启用 `FETCH_README` 时仅获取前 10 个仓库
- 启用 `FETCH_STRUCTURE` 时仅获取前 5 个仓库

查看当前 API 状态：
```bash
gh api rate_limit
```

## 输出示例

### Markdown 示例

```markdown
# GitHub 仓库索引

> 生成时间: 2026-01-29 14:30:00
> 仓库总数: 42

## 仓库概览

| 仓库名 | 描述 | 主要语言 | Stars | Forks |
|--------|------|----------|-------|-------|
| [user/repo1](https://github.com/user/repo1) | 项目描述 | TypeScript | 10 | 2 |
| ...
```

### JSON 示例

```json
[
  {
    "nameWithOwner": "user/repo1",
    "description": "项目描述",
    "url": "https://github.com/user/repo1",
    "primaryLanguage": {
      "name": "TypeScript"
    },
    "stargazerCount": 10,
    "forkCount": 2,
    ...
  }
]
```

## 与 AI 工具集成

生成的索引文件特别适合与 AI 工具（如 Claude Code）集成使用：

1. **添加到项目上下文**
   ```bash
   # 在 Claude Code 中引用索引文件
   # 请先阅读 repo-index-latest.md 了解我的所有项目
   ```

2. **快速查找项目**
   ```bash
   # 搜索特定语言的仓库
   cat repo-index-latest.json | jq '.[] | select(.primaryLanguage.name == "Python")'
   ```

3. **生成项目报告**
   ```bash
   # 统计各语言的仓库数量
   cat repo-index-latest.json | jq '[.[].primaryLanguage.name] | group_by(.) | map({language: .[0], count: length})'
   ```

## 定时任务

可以设置定时任务定期更新索引：

### 使用 cron（Linux/macOS）

```bash
# 编辑 crontab
crontab -e

# 每天凌晨 2 点运行
0 2 * * * cd /path/to/scripts && bash github-repo-idx.sh
```

### 使用 launchd（macOS）

创建 `~/Library/LaunchAgents/com.user.github-repo-index.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.github-repo-index</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/path/to/scripts/github-repo-idx.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>WorkingDirectory</key>
    <string>/path/to/scripts</string>
</dict>
</plist>
```

## 故障排除

### 问题：GraphQL API rate limit exceeded

**解决方案**：等待 API 限制重置（通常 1 小时）或减少 API 调用量

```bash
# 查看 API 状态
gh api rate_limit

# 等待一段时间后重试
# 或者禁用额外的 API 调用
bash github-repo-idx.sh  # 默认不获取 README 和文件结构
```

### 问题：gh: command not found

**解决方案**：安装 GitHub CLI

```bash
# macOS
brew install gh

# Linux
# 参考 https://github.com/cli/cli#installation
```

### 问题：jq: command not found

**解决方案**：安装 jq

```bash
# macOS
brew install jq

# Debian/Ubuntu
sudo apt-get install jq
```

## 贡献

欢迎提交问题和改进建议！

## 许可证

MIT License
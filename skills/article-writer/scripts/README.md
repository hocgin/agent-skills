# Article Writer 自动化脚本

Article Writer 提供了一系列 Bash 脚本，支持从需求定义到配图建议的完整自动化流程。

## 快速开始

### 1. 初始化项目

```bash
# 在项目目录中运行
./scripts/article-writer.sh init my-article
```

这会创建必要的目录结构：
```
project/
├── .article-writer         # 项目标记
├── _briefs/                # 需求文档
├── _knowledge_base/        # 调研结果
│   ├── raw/               # 原始数据
│   └── indexed/           # 索引文件
└── draft.md               # 文章草稿
```

### 2. 创建需求文档

```bash
./scripts/article-writer.sh brief
```

会创建一个新的 brief 文件，编辑填写你的需求。

### 3. 完整写作流程

```bash
# 3.1 信息调研
./scripts/article-writer.sh research

# 3.2 快速写作
./scripts/article-writer.sh write

# 3.3 三遍审校（一键执行）
./scripts/article-writer.sh review-all

# 3.4 配图建议
./scripts/article-writer.sh images
```

## 单独使用脚本

### research.sh - 信息调研

```bash
# 使用最新的 brief
./scripts/research.sh

# 指定 brief 文件
./scripts/research.sh _briefs/001-brief.md
```

### write.sh - 快速写作

```bash
# 基于最新的 brief 和调研结果写作
./scripts/write.sh

# 指定文件
./scripts/write.sh _briefs/001-brief.md _knowledge_base/research-xxx.md
```

### review.sh - 三遍审校

```bash
# 内容审校
./scripts/review.sh content

# 风格审校
./scripts/review.sh style

# 细节审校
./scripts/review.sh detail
```

### images.sh - 配图建议

```bash
# 基于当前草稿生成配图方案
./scripts/images.sh

# 指定草稿文件
./scripts/images.sh /path/to/draft.md
```

## 主入口命令

```bash
./scripts/article-writer.sh <命令> [参数]

可用命令:
  init [name]          初始化项目
  brief                创建/编辑需求文档
  research [brief]     信息调研
  write [brief]        快速写作
  review [mode]        三遍审校
    mode: content | style | detail
  review-all           完整三遍审校（推荐）
  images [draft]       配图建议
  status               显示项目状态
  help                 显示帮助信息
```

## 脚本说明

### common.sh - 通用函数库

提供以下功能：
- `get_project_root()` - 获取项目根目录
- `get_current_draft()` - 获取当前草稿文件
- `get_latest_brief()` - 获取最新的 brief 文件
- `count_chinese_words()` - 中文字数统计
- `show_word_count_info()` - 显示字数信息
- `ensure_file()` - 确保文件存在
- `create_numbered_dir()` - 创建带编号的目录
- `output_json()` - 输出 JSON（与 AI 通信）

### text-audit.sh - AI 味检测

自动检测文章中的 AI 味道，包括：
- 书面化词汇
- AI 句式
- 机械对称结构
- 空洞表达

## 项目状态查看

```bash
./scripts/article-writer.sh status
```

输出：
- 项目根目录
- 需求文档数量和最新文件
- 调研报告数量和最新文件
- 当前草稿字数
- 审校记录状态

## 与 AI 助手集成

所有脚本都支持输出 JSON 格式，方便与 AI 助手（如 Claude Code）集成：

```bash
# 脚本会输出类似这样的 JSON
{
  "brief_file": "/path/to/brief.md",
  "research_file": "/path/to/research.md",
  "draft_file": "/path/to/draft.md",
  "target_words": 3000
}
```

AI 助手可以解析这些 JSON 并继续执行后续步骤。

## 注意事项

1. **Git 仓库**：建议在 git 仓库中使用，方便版本管理
2. **备份**：重要文档会自动保存，建议定期提交
3. **路径**：所有脚本必须在项目根目录中运行
4. **权限**：确保所有 `.sh` 文件有执行权限（`chmod +x`）

## 故障排查

### 脚本无法执行

```bash
chmod +x scripts/*.sh
```

### 找不到项目根目录

确保当前目录包含 `SKILL.md` 或 `.article-writer` 文件。

### 字数统计不准确

`count_chinese_words` 函数已优化，会排除 Markdown 标记和格式符号。

## 完整示例

```bash
# 1. 初始化
./scripts/article-writer.sh init my-first-article

# 2. 创建 brief
./scripts/article-writer.sh brief
# 编辑 _briefs/001-brief.md

# 3. 调研
./scripts/article-writer.sh research

# 4. 写作
./scripts/article-writer.sh write

# 5. 三遍审校
./scripts/article-writer.sh review-all

# 6. 配图
./scripts/article-writer.sh images

# 7. 查看状态
./scripts/article-writer.sh status
```

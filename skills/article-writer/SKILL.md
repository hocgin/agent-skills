---
name: article-writer
description: AI驱动的智能写作系统，专注于创作高质量、低AI检测率的文章内容
compatibility: Requires wenyan-cli
metadata:
  author: hocgin
  version: "3.0"
  ai-detection-target: "< 25%"
  primary-mode: fast (自动生成)
  dependencies: wenyan-cli (可选，用于AI生图)
---

## 核心特性

- **独立工作区**：每篇文章都有独立的工作区（`编号.文章标题`），文件互不干扰
- **快速写作模式**：AI自动生成初稿，无需人工介入，适合高效内容创作
- **智能信息调研**：支持网页搜索、文档爬取、PDF提取，建立知识库
- **三遍审校机制**：内容审校 → 风格审校 → 细节审校，系统化降低AI味
- **配图自动化**：AI生成配图建议 + AI生图 + 自动嵌入
- **通用文章类型**：支持自媒体文章、技术博客、正式文档等多种类型
- **质量优先**：AI检测率目标 < 25%

## 完整写作流程（14步）

### 阶段1：准备
1. **工作区创建** - 创建"编号.文章标题"格式的工作区
2. **需求定义** - 明确文章类型、目标读者、字数要求
3. **选题讨论** - 提供选题方向，确定文章结构
4. **配置加载** - 读取 article.config.md 配置文件

### 阶段2：收集
5. **信息调研** - 搜索资料、爬取文档、建立知识库
6. **素材收集** - （可选）搜索个人素材库，融入真实案例
7. **经历提取** - （可选）提取真实经历，增强真实性

### 阶段3：写作
8. **快速写作** - AI生成完整初稿，支持迭代修改

### 阶段4：检查
9. **真实性检查** - 检查温度、个性、细节、思想等维度
10. **三遍审校** - 内容/风格/细节三轮审校，降低AI味

### 阶段5：配图
11. **配图建议** - 分析文章内容，生成3-5张配图方案
12. **图片生成** - 使用 wenyan-cli 或其他工具生成配图

### 阶段6：发布
13. **图片嵌入** - 将生成的图片嵌入到文章合适位置
14. **发布检查** - 最终质量检查，准备发布

## 规则文件说明

### 核心规则

- **[rules/workspace.md](rules/workspace.md)** - 工作区管理
  - 为每篇文章创建独立工作区
  - 命名规则：`编号.文章标题`
  - 工作区生命周期管理

- **[rules/research.md](rules/research.md)** - 信息搜索与调研
  - 支持URL检测，自动识别文档网站并爬取
  - 支持PDF文档提取
  - 支持常规Web搜索和调研
  - 自动整理调研报告，保存到知识库

- **[rules/write.md](rules/write.md)** - 快速写作模式
  - 基于调研结果和brief生成完整初稿
  - 支持3轮迭代修改
  - 自动引用调研数据和真实素材
  - 口语化表达，降低AI味

- **[rules/review.md](rules/review.md)** - 三遍审校机制
  - 第一遍：内容审校（事实、逻辑、结构）
  - 第二遍：风格审校（降AI味、增强真实感）
  - 第三遍：细节审校（格式、标点、排版）
  - 使用反AI检测规则库系统化优化

- **[rules/image.md](rules/image.md)** - 配图建议与生成
  - 分析文章内容，生成3-5张配图方案
  - 包含配图描述、尺寸建议、位置建议
  - 集成AI 生图，提供生成命令

- **[rules/embed.md](rules/embed.md)** - 图片嵌入
  - 将生成的图片嵌入到文章合适位置
  - 支持多种图片语法（Markdown/HTML/公众号）
  - 自动添加图片说明和样式

## 使用方式

### 方式1：完整流程（推荐）

从工作区创建开始，完整执行14步流程：

```
1. 创建工作区 → 2. 定义需求 → 3. 选题讨论 → 4. 配置加载 → 5. 信息调研 → 8. 快速写作 → 10. 三遍审校 → 11. 配图建议 → 12. 图片生成 → 13. 图片嵌入
```

### 方式2：单独使用规则

也可以只调用特定功能模块：

- **只做调研**：调用 rules/research.md
- **只写作**：调用 rules/write.md（需要已有调研结果）
- **只审校**：调用 rules/review.md（需要已有草稿）
- **只配图**：调用 rules/image.md（需要已有文章）
- **只嵌入**：调用 rules/embed.md（需要已有文章和图片）

## 项目结构

```
article-writer/           # 根目录即为工作区目录
├── 001.claude-code完全指南/
│   ├── article.config.md       # 文章配置
│   ├── brief.md                # 需求文档
│   ├── research.md             # 调研报告
│   ├── draft.md                # 文章草稿
│   ├── review-log.md           # 审校日志
│   ├── images-plan.md          # 配图方案
│   ├── images/                 # 配图目录
│   │   ├── 01-cover.png
│   │   ├── 02-data.png
│   │   └── ...
│   ├── draft-with-images.md    # 嵌入图片后的文章
│   └── final.md                # 最终文章
├── 002.2024年AI编程工具对比/
└── 003.rust内存安全深度解析/
```

**工作区命名规则**：`编号.文章标题`（如 `001.claude-code完全指南`）

详见：[rules/workspace.md](rules/workspace.md)

## 质量目标

- **AI检测率**：< 25%（快速模式）
- **内容准确性**：事实准确，逻辑严密
- **可读性**：口语化表达，自然流畅
- **完整性**：覆盖所有核心论点

## 适用文章类型

- 自媒体文章（公众号、头条、百家号等）
- 技术博客（教程、技术总结、知识分享）
- 正式文档（项目报告、技术方案等）
- 通用文章（可根据brief配置不同风格）

---

## 快速开始示例

### 完整写作流程

```bash
# 1. 创建工作区
调用 rules/workspace.md

# 2. 信息调研（基于 brief）
调用 rules/research.md

# 3. 快速写作（基于调研结果）
调用 rules/write.md

# 4. 三遍审校（降低 AI 味）
调用 rules/review.md

# 5. 配图建议（含 AI 生图）
调用 rules/image.md

# 6. 图片嵌入（将图片插入文章）
调用 rules/embed.md
```

### 单独使用

每个规则也可以独立调用：

- **工作区管理**：调用 `rules/workspace.md`
- **只做调研**：调用 `rules/research.md`
- **只写作**：调用 `rules/write.md`（需要已有调研结果）
- **只审校**：调用 `rules/review.md`（需要已有草稿）
- **只配图**：调用 `rules/image.md`（需要已有文章）
- **只嵌入**：调用 `rules/embed.md`（需要已有文章和图片）

---

## 下一步

1. 阅读 [rules/workspace.md](rules/workspace.md) 了解工作区管理
2. 阅读 [rules/research.md](rules/research.md) 了解信息调研流程
3. 阅读 [rules/write.md](rules/write.md) 了解快速写作流程
4. 阅读 [rules/review.md](rules/review.md) 了解三遍审校机制
5. 阅读 [rules/image.md](rules/image.md) 了解配图建议与生图
6. 阅读 [rules/embed.md](rules/embed.md) 了解图片嵌入流程


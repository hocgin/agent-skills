---
name: article-writer
description: AI驱动的智能写作系统，专注于创作高质量、低AI检测率的文章内容
compatibility: Requires wenyan-cli
metadata:
  author: hocgin
  version: "2.0"
  ai-detection-target: "< 25%"
  primary-mode: fast (自动生成)
  dependencies: wenyan-cli (可选，用于AI生图)
---

## 核心特性

- **快速写作模式**：AI自动生成初稿，无需人工介入，适合高效内容创作
- **智能信息调研**：支持网页搜索、文档爬取、PDF提取，建立知识库
- **三遍审校机制**：内容审校 → 风格审校 → 细节审校，系统化降低AI味
- **通用文章类型**：支持自媒体文章、技术博客、正式文档等多种类型
- **质量优先**：AI检测率目标 < 25%

## 完整写作流程（13步）

### 阶段1：准备
1. **需求定义** - 明确文章类型、目标读者、字数要求
2. **选题讨论** - 提供选题方向，确定文章结构
3. **配置加载** - 读取 article.config.md 配置文件

### 阶段2：收集
4. **信息调研** - 搜索资料、爬取文档、建立知识库
5. **素材收集** - （可选）搜索个人素材库，融入真实案例
6. **经历提取** - （可选）提取真实经历，增强真实性

### 阶段3：写作
7. **快速写作** - AI生成完整初稿，支持迭代修改

### 阶段4：检查
8. **真实性检查** - 检查温度、个性、细节、思想等维度
9. **三遍审校** - 内容/风格/细节三轮审校，降低AI味

### 阶段5：配图
10. **配图建议** - 分析文章内容，生成3-5张配图方案
11. **图片生成** - 使用 wenyan-cli 或其他工具生成配图

### 阶段6：发布
12. **图片嵌入** - 将生成的图片嵌入到文章合适位置
13. **发布检查** - 最终质量检查，准备发布

## 规则文件说明

### 核心规则

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
  - 集成 wenyan-cli AI 生图，提供生成命令

- **[rules/embed.md](rules/embed.md)** - 图片嵌入
  - 将生成的图片嵌入到文章合适位置
  - 支持多种图片语法（Markdown/HTML/公众号）
  - 自动添加图片说明和样式

## 使用方式

### 方式1：完整流程（推荐）

从需求定义开始，完整执行13步流程：

```
1. 定义需求 → 2. 选题讨论 → 3. 配置加载 → 4. 信息调研 → 7. 快速写作 → 9. 三遍审校 → 10. 配图建议 → 11. 图片生成 → 12. 图片嵌入
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
project/
├── _briefs/              # 需求文档（brief）
├── _knowledge_base/      # 调研结果和知识库
│   ├── raw/             # 原始数据
│   └── indexed/         # 索引文件
├── images/               # 配图目录
│   ├── 01-cover.png     # 封面图
│   ├── 02-data.png      # 数据对比图
│   └── ...              # 其他配图
├── draft.md              # 文章草稿
├── images-plan.md        # 配图方案
├── review-log.md         # 审校日志
├── draft-with-images.md  # 嵌入图片后的文章
└── final.md              # 最终文章
```

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

## 与参考项目的主要差异

相比 [article-writer-cn](https://github.com/wordflowlab/article-writer)：

1. **简化工作区系统**：只保留通用工作区，不区分 wechat/video/general
2. **专注快速模式**：以无人工介入的快速模式为主，不实现教练模式
3. **简化素材系统**：素材收集为可选功能，不强制要求
4. **保留核心功能**：调研、写作、审校、配图等核心功能完整保留
5. **集成 wenyan-cli**：支持使用 wenyan-cli 进行 AI 生图

---

## 快速开始示例

### 完整写作流程

```bash
# 1. 信息调研（基于 brief）
调用 rules/research.md

# 2. 快速写作（基于调研结果）
调用 rules/write.md

# 3. 三遍审校（降低 AI 味）
调用 rules/review.md

# 4. 配图建议（含 wenyan-cli AI 生图）
调用 rules/image.md

# 5. 图片嵌入（将图片插入文章）
调用 rules/embed.md
```

### 单独使用

每个规则也可以独立调用：

- **只做调研**：调用 `rules/research.md`
- **只写作**：调用 `rules/write.md`（需要已有调研结果）
- **只审校**：调用 `rules/review.md`（需要已有草稿）
- **只配图**：调用 `rules/image.md`（需要已有文章）
- **只嵌入**：调用 `rules/embed.md`（需要已有文章和图片）

---

## 下一步

1. 阅读 [article.config.md](article.config.md) 了解配置文件的使用
2. 阅读 [rules/research.md](rules/research.md) 了解信息调研流程
3. 阅读 [rules/write.md](rules/write.md) 了解快速写作流程
4. 阅读 [rules/review.md](rules/review.md) 了解三遍审校机制
5. 阅读 [rules/image.md](rules/image.md) 了解配图建议与 wenyan-cli AI 生图
6. 阅读 [rules/embed.md](rules/embed.md) 了解图片嵌入流程


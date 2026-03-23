# Article Writer 自动化脚本 - 快速开始

## 脚本列表

✅ 所有脚本已就绪，支持完整自动化流程：

| 脚本 | 功能 | 状态 |
|------|------|------|
| article-writer.sh | 主入口，一键执行 | ✅ |
| common.sh | 通用函数库 | ✅ |
| research.sh | 信息调研 | ✅ |
| write.sh | 快速写作 | ✅ |
| review.sh | 三遍审校 | ✅ |
| images.sh | 配图建议 | ✅ |
| text-audit.sh | AI 味检测 | ✅ |

## 快速开始（5分钟）

### 1️⃣ 初始化项目

```bash
./scripts/article-writer.sh init
```

### 2️⃣ 创建需求文档

```bash
./scripts/article-writer.sh brief
# 编辑生成的 _briefs/001-brief.md
```

### 3️⃣ 信息调研

```bash
./scripts/article-writer.sh research
```

### 4️⃣ 快速写作

```bash
./scripts/article-writer.sh write
```

### 5️⃣ 三遍审校

```bash
./scripts/article-writer.sh review-all
```

### 6️⃣ 配图建议

```bash
./scripts/article-writer.sh images
```

## 查看项目状态

```bash
./scripts/article-writer.sh status
```

## 完整命令参考

```bash
./scripts/article-writer.sh help
```

## 目录结构

执行 `init` 后会创建：

```
project/
├── .article-writer           # 项目标记
├── SKILL.md                  # Skill 主文档
├── scripts/                  # 自动化脚本
│   ├── article-writer.sh    # 主入口
│   ├── common.sh            # 通用函数
│   ├── research.sh          # 信息调研
│   ├── write.sh             # 快速写作
│   ├── review.sh            # 三遍审校
│   ├── images.sh            # 配图建议
│   └── text-audit.sh        # AI 味检测
├── rules/                    # 规则文件
│   ├── research.md
│   ├── write.md
│   ├── review.md
│   └── image.md
├── _briefs/                  # 需求文档
├── _knowledge_base/          # 调研结果
│   ├── raw/
│   └── indexed/
└── draft.md                  # 文章草稿
```

## 自动化特性

✅ **自动检测项目根目录** - 支持 SKILL.md 或 .article-writer 标记
✅ **自动编号** - brief 和调研文件自动编号
✅ **JSON 输出** - 支持与 AI 助手集成
✅ **字数统计** - 准确的中文字数统计
✅ **错误检查** - 输入验证和友好的错误提示
✅ **一键审校** - review-all 自动执行三遍审校

## 与 AI 助手配合使用

在 Claude Code / Cursor 中：

1. 调用规则文件获取指导
2. 调用脚本执行具体操作
3. 脚本输出 JSON 供 AI 解析
4. AI 继续执行下一步骤

示例对话：

```
你: 基于这个 brief 进行信息调研
AI: [调用 research.sh]
AI: 已创建调研文件: _knowledge_base/research-xxx.md

你: 现在开始写文章
AI: [调用 write.sh]
AI: 正在基于调研结果生成初稿...

你: 进行三遍审校
AI: [调用 review-all]
AI: 正在执行完整的三遍审校...
```

## 故障排查

### 脚本无法执行

```bash
chmod +x scripts/*.sh
```

### 找不到项目根目录

确保当前目录包含 `SKILL.md` 文件。

### 需要更多帮助

查看完整文档：
- scripts/README.md - 脚本详细说明
- SKILL.md - Skill 主文档
- rules/*.md - 各规则文件说明

#!/usr/bin/env bash
# 快速写作 - 基于调研结果生成初稿

set -e

SCRIPT_DIR=$(dirname "$0")
source "$SCRIPT_DIR/common.sh"

SCRIPT_DIR=$(dirname "$0")
source "$SCRIPT_DIR/common.sh"

# 解析参数
BRIEF_FILE="$1"
RESEARCH_FILE="$2"

PROJECT_ROOT=$(get_project_root)
DRAFT_FILE="$PROJECT_ROOT/draft.md"

# 如果没有指定 brief，使用最新的
if [ -z "$BRIEF_FILE" ]; then
    BRIEF_FILE=$(get_latest_brief)
fi

# 如果没有指定调研文件，查找最新的
if [ -z "$RESEARCH_FILE" ]; then
    RESEARCH_FILE=$(find "$PROJECT_ROOT/_knowledge_base" -name "research-*.md" -type f 2>/dev/null | head -1)
fi

# 验证输入
if [ -z "$BRIEF_FILE" ] || [ ! -f "$BRIEF_FILE" ]; then
    echo "❌ 错误: 未找到 brief 文件"
    echo "用法: write.sh [brief文件路径] [调研文件路径]"
    echo ""
    echo "提示："
    echo "  1. 创建 brief 文件到 _briefs/ 目录"
    echo "  2. 或运行 research.sh 先进行调研"
    exit 1
fi

echo "✅ 快速写作模式"
echo ""
echo "📋 Brief 来源: $BRIEF_FILE"
if [ -n "$RESEARCH_FILE" ] && [ -f "$RESEARCH_FILE" ]; then
    echo "📚 调研来源: $RESEARCH_FILE"
else
    echo "⚠️  警告: 未找到调研文件，写作时可能缺少事实依据"
fi
echo ""

# 提取 brief 中的关键信息
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Brief 分析"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 尝试从 brief 中提取标题
TITLE=$(grep -E "^#.*|^标题[：:]" "$BRIEF_FILE" | head -1 | sed 's/^#*[[:space:]]*//' | sed 's/^标题[：:][[:space:]]*//')
if [ -z "$TITLE" ]; then
    TITLE="未命名文章"
fi

echo "文章标题: $TITLE"
echo ""

# 提取字数要求
WORD_COUNT_TARGET=$(grep -E "字数[：:]" "$BRIEF_FILE" | grep -oE "[0-9]+" | head -1)
if [ -z "$WORD_COUNT_TARGET" ]; then
    WORD_COUNT_TARGET=3000
fi
echo "目标字数: $WORD_COUNT_TARGET"
echo ""

# 检查是否已存在草稿
if [ -f "$DRAFT_FILE" ]; then
    EXISTING_WORDS=$(count_chinese_words "$DRAFT_FILE")
    echo "⚠️  发现已有草稿: $DRAFT_FILE (已写 $EXISTING_WORDS 字)"
    echo ""
    read -p "是否覆盖现有草稿？(y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "❌ 取消写作"
        exit 0
    fi
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ 准备开始写作"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "写作模式: 快速模式（AI自动生成）"
echo "目标AI检测率: < 25%"
echo ""
echo "💡 写作要点:"
echo "   1. 严格遵循 brief 要求"
echo "   2. 引用调研数据（如有）"
echo "   3. 口语化表达，降低 AI 味"
echo "   4. 避免 AI 套话和机械结构"
echo "   5. 支持 3 轮迭代修改"
echo ""

# 创建写作日志文件
WRITE_LOG="$PROJECT_ROOT/write-log.md"
cat > "$WRITE_LOG" << EOF
# 写作记录

**开始时间**: $(date '+%Y-%m-%d %H:%M:%S')
**Brief**: $(basename "$BRIEF_FILE")
**调研**: ${RESEARCH_FILE:+$(basename "$RESEARCH_FILE")}
**目标字数**: $WORD_COUNT_TARGET

---

## 写作过程

<!-- 记录每轮迭代 -->

EOF

echo "✅ 写作环境已准备"
echo ""
echo "📝 接下来:"
echo "   AI 将基于 brief 和调研结果生成文章初稿"
echo "   草稿将保存到: $DRAFT_FILE"
echo "   写作日志: $WRITE_LOG"
echo ""

# 输出 JSON 供 AI 使用
output_json "{\"brief_file\": \"$BRIEF_FILE\", \"research_file\": \"${RESEARCH_FILE:-}\", \"draft_file\": \"$DRAFT_FILE\", \"write_log\": \"$WRITE_LOG\", \"target_words\": $WORD_COUNT_TARGET, \"title\": \"$TITLE\"}"

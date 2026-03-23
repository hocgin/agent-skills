#!/usr/bin/env bash
# Article Writer - 主入口脚本

set -e

SCRIPT_DIR=$(dirname "$0")
source "$SCRIPT_DIR/common.sh"

# 显示用法
show_usage() {
    cat << EOF
Article Writer - AI 驱动的智能写作系统

用法: article-writer.sh <命令> [参数]

命令:
  init [name]          初始化项目（创建必要的目录结构）
  brief                创建/编辑需求文档
  research [brief]     信息调研
  write [brief]        快速写作
  review [mode]        三遍审校
    mode: content | style | detail
  review-all           完整三遍审校
  images [draft]       配图建议
  status               显示当前项目状态
  help                 显示此帮助信息

示例:
  article-writer.sh init my-article
  article-writer.sh brief
  article-writer.sh research
  article-writer.sh write
  article-writer.sh review style
  article-writer.sh review-all
  article-writer.sh images

完整流程:
  1. brief      → 创建需求文档
  2. research   → 信息调研
  3. write      → 快速写作
  4. review-all → 三遍审校
  5. images     → 配图建议

EOF
}

# 显示项目状态
show_status() {
    PROJECT_ROOT=$(get_project_root)

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📊 Article Writer 项目状态"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "项目根目录: $PROJECT_ROOT"
    echo ""

    # 检查 brief
    BRIEF_COUNT=$(ls -1 "$PROJECT_ROOT/_briefs"/*.md 2>/dev/null | wc -l)
    echo "📋 需求文档: $BRIEF_COUNT 个"
    if [ "$BRIEF_COUNT" -gt 0 ]; then
        LATEST_BRIEF=$(ls -t "$PROJECT_ROOT/_briefs"/*.md 2>/dev/null | head -1)
        echo "   最新: $(basename "$LATEST_BRIEF")"
    fi
    echo ""

    # 检查调研
    RESEARCH_COUNT=$(ls -1 "$PROJECT_ROOT/_knowledge_base"/research-*.md 2>/dev/null | wc -l)
    echo "🔍 调研报告: $RESEARCH_COUNT 个"
    if [ "$RESEARCH_COUNT" -gt 0 ]; then
        LATEST_RESEARCH=$(ls -t "$PROJECT_ROOT/_knowledge_base"/research-*.md 2>/dev/null | head -1)
        echo "   最新: $(basename "$LATEST_RESEARCH")"
    fi
    echo ""

    # 检查草稿
    DRAFT_FILE="$PROJECT_ROOT/draft.md"
    if [ -f "$DRAFT_FILE" ]; then
        WORD_COUNT=$(count_chinese_words "$DRAFT_FILE")
        echo "✅ 当前草稿: $WORD_COUNT 字"
        echo "   文件: $DRAFT_FILE"
    else
        echo "❌ 未找到草稿"
    fi
    echo ""

    # 检查审校日志
    AUDIT_LOG="$PROJECT_ROOT/audit-log.md"
    if [ -f "$AUDIT_LOG" ]; then
        echo "📝 审校记录: 存在"
    else
        echo "📝 审校记录: 未开始"
    fi
    echo ""

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# 初始化项目
init_project() {
    PROJECT_ROOT=$(get_project_root)
    PROJECT_NAME="${1:-article-writer-project}"

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🚀 初始化 Article Writer 项目"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "项目根目录: $PROJECT_ROOT"
    echo "项目名称: $PROJECT_NAME"
    echo ""

    # 创建目录结构
    mkdir -p "$PROJECT_ROOT/_briefs"
    mkdir -p "$PROJECT_ROOT/_knowledge_base/raw"
    mkdir -p "$PROJECT_ROOT/_knowledge_base/indexed"

    # 创建 .article-writer 标记文件
    touch "$PROJECT_ROOT/.article-writer"

    echo "✅ 目录结构已创建"
    echo ""
    echo "📁 已创建目录:"
    echo "   _briefs/              - 需求文档"
    echo "   _knowledge_base/      - 调研结果"
    echo "   _knowledge_base/raw/ - 原始数据"
    echo "   _knowledge_base/indexed/ - 索引文件"
    echo ""
    echo "💡 下一步:"
    echo "   1. 运行: article-writer.sh brief"
    echo "   2. 创建你的第一个需求文档"
    echo ""
}

# 创建/编辑 brief
create_brief() {
    PROJECT_ROOT=$(get_project_root)
    ensure_directories

    BRIEF_NUMBER=$(create_numbered_dir "$PROJECT_ROOT/_briefs" "brief")
    BRIEF_FILE="$PROJECT_ROOT/_briefs/$BRIEF_NUMBER-brief.md"

    cat > "$BRIEF_FILE" << 'EOF'
# 文章需求

**创建时间**:
**文章类型**: 评测/教程/观点/技术

---

## 文章主题
<!-- 描述你想写什么主题 -->

## 目标读者
<!-- 谁会读这篇文章？ -->

## 核心观点
<!-- 你想传达的核心信息是什么？ -->

## 字数要求
<!-- 建议字数: 1000-5000 字 -->

## 风格要求
<!-- 正式/轻松/专业/幽默 -->

## 必须覆盖的要点
1.
2.
3.

## 参考资料（如有）
<!-- 链接或文件 -->

---

## 备注
<!-- 其他特殊要求 -->

EOF

    echo "✅ 已创建 brief 文件: $BRIEF_FILE"
    echo ""
    echo "💡 请编辑该文件，填写你的需求"
    echo "   然后运行: article-writer.sh research"
    echo ""

    # 尝试用编辑器打开
    if [ -n "$EDITOR" ]; then
        "$EDITOR" "$BRIEF_FILE"
    fi
}

# 主程序
main() {
    # 检查是否在 git 仓库中（可选）
    # check_git_repo

    case "${1:-help}" in
        init)
            init_project "$2"
            ;;
        brief)
            create_brief
            ;;
        research)
            bash "$SCRIPT_DIR/research.sh" "$2"
            ;;
        write)
            bash "$SCRIPT_DIR/write.sh" "$2" "$3"
            ;;
        review)
            if [ -z "$2" ]; then
                echo "❌ 错误: 请指定审校模式 (content/style/detail)"
                echo ""
                show_usage
                exit 1
            fi
            bash "$SCRIPT_DIR/review.sh" "$2" "$3"
            ;;
        review-all)
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "🔄 开始完整三遍审校"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""

            echo "📋 第1遍: 内容审校"
            bash "$SCRIPT_DIR/review.sh" "content"
            echo ""
            read -p "按 Enter 继续第2遍审校..."

            echo "📋 第2遍: 风格审校"
            bash "$SCRIPT_DIR/review.sh" "style"
            echo ""
            read -p "按 Enter 继续第3遍审校..."

            echo "📋 第3遍: 细节审校"
            bash "$SCRIPT_DIR/review.sh" "detail"
            echo ""

            echo "✅ 三遍审校完成！"
            ;;
        images)
            bash "$SCRIPT_DIR/images.sh" "$2"
            ;;
        status)
            show_status
            ;;
        help|--help|-h)
            show_usage
            ;;
        *)
            echo "❌ 未知命令: $1"
            echo ""
            show_usage
            exit 1
            ;;
    esac
}

main "$@"

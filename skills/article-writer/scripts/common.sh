#!/usr/bin/env bash
# 通用函数库 - Article Writer

# 检查是否在 git 仓库中
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo "❌ 错误: 当前目录不是 git 仓库" >&2
        echo "提示: 请在 article-writer 项目根目录中运行" >&2
        exit 1
    fi
}

# 获取项目根目录（包含 .article-writer 标记或 SKILL.md）
get_project_root() {
    local current=$(pwd)

    # 检查当前目录
    if [ -f "$current/SKILL.md" ] || [ -f "$current/.article-writer" ]; then
        echo "$current"
        return 0
    fi

    # 向上查找
    while [ "$current" != "/" ]; do
        if [ -f "$current/SKILL.md" ] || [ -f "$current/.article-writer" ]; then
            echo "$current"
            return 0
        fi
        current=$(dirname "$current")
    done

    echo "错误: 未找到 article-writer 项目根目录（需要包含 SKILL.md 或 .article-writer 文件）" >&2
    exit 1
}

# 获取当前文章目录（最近的包含 draft.md 的目录）
get_current_article_dir() {
    PROJECT_ROOT=$(get_project_root)

    # 查找包含 draft.md 的目录
    local draft_dir=$(find "$PROJECT_ROOT" -name "draft.md" -type f 2>/dev/null | head -1)
    if [ -n "$draft_dir" ]; then
        dirname "$draft_dir"
    fi
}

# 获取当前草稿文件路径
get_current_draft() {
    PROJECT_ROOT=$(get_project_root)

    # 优先查找项目根目录的 draft.md
    if [ -f "$PROJECT_ROOT/draft.md" ]; then
        echo "$PROJECT_ROOT/draft.md"
        return 0
    fi

    # 查找最近的 draft.md
    local draft=$(find "$PROJECT_ROOT" -name "draft.md" -type f 2>/dev/null | head -1)
    if [ -n "$draft" ]; then
        echo "$draft"
    fi
}

# 获取最新的 brief 文件
get_latest_brief() {
    PROJECT_ROOT=$(get_project_root)
    local BRIEFS_DIR="$PROJECT_ROOT/_briefs"

    if [ -d "$BRIEFS_DIR" ]; then
        local latest=$(ls -t "$BRIEFS_DIR"/*.md 2>/dev/null | head -1)
        if [ -n "$latest" ]; then
            echo "$latest"
        fi
    fi
}

# 创建带编号的目录
create_numbered_dir() {
    local base_dir="$1"
    local prefix="$2"

    mkdir -p "$base_dir"

    # 找到最高编号
    local highest=0
    for dir in "$base_dir"/*; do
        [ -d "$dir" ] || continue
        local dirname=$(basename "$dir")
        local number=$(echo "$dirname" | grep -o '^[0-9]\+' || echo "0")
        number=$((10#$number))
        if [ "$number" -gt "$highest" ]; then
            highest=$number
        fi
    done

    # 返回下一个编号
    local next=$((highest + 1))
    printf "%03d" "$next"
}

# 输出 JSON（用于与 AI 助手通信）
output_json() {
    echo "$1"
}

# 确保文件存在
ensure_file() {
    local file="$1"
    local template="$2"

    if [ ! -f "$file" ]; then
        if [ -f "$template" ]; then
            cp "$template" "$file"
        else
            touch "$file"
        fi
    fi
}

# 准确的中文字数统计
# 排除Markdown标记、空格、换行符，只统计实际内容
count_chinese_words() {
    local file="$1"

    if [ ! -f "$file" ]; then
        echo "0"
        return
    fi

    # 移除Markdown标记和格式符号，然后统计字符
    local word_count=$(cat "$file" | \
        sed '/^```/,/^```/d' | \
        sed 's/^#\+[[:space:]]*//' | \
        sed 's/\*\*//g' | \
        sed 's/__//g' | \
        sed 's/\*//g' | \
        sed 's/_//g' | \
        sed 's/\[//g' | \
        sed 's/\]//g' | \
        sed 's/(http[^)]*)//g' | \
        sed 's/^>[[:space:]]*//' | \
        sed 's/^[[:space:]]*[-*][[:space:]]*//' | \
        sed 's/^[[:space:]]*[0-9]\+\.[[:space:]]*//' | \
        tr -d '[:space:]' | \
        tr -d '[:punct:]' | \
        grep -o . | \
        wc -l | \
        tr -d ' ')

    echo "$word_count"
}

# 显示友好的字数信息
show_word_count_info() {
    local file="$1"
    local min_words="${2:-0}"
    local max_words="${3:-999999}"
    local actual_words=$(count_chinese_words "$file")

    echo "字数：$actual_words"

    if [ "$min_words" -gt 0 ]; then
        if [ "$actual_words" -lt "$min_words" ]; then
            echo "⚠️ 未达到最低字数要求（最小：${min_words}）"
        elif [ "$actual_words" -gt "$max_words" ]; then
            echo "⚠️ 超过最大字数限制（最大：${max_words}）"
        else
            echo "✅ 符合字数要求（${min_words}-${max_words}）"
        fi
    fi
}

# 检查命令是否存在
check_command() {
    if ! command -v "$1" > /dev/null 2>&1; then
        echo "❌ 错误: 未找到命令 '$1'" >&2
        echo "请安装后重试" >&2
        exit 1
    fi
}

# 确保必要的目录存在
ensure_directories() {
    PROJECT_ROOT=$(get_project_root)

    mkdir -p "$PROJECT_ROOT/_briefs"
    mkdir -p "$PROJECT_ROOT/_knowledge_base/raw"
    mkdir -p "$PROJECT_ROOT/_knowledge_base/indexed"
}

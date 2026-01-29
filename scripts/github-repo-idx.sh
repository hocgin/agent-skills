#!/bin/bash

# GitHub 仓库索引生成脚本
# 用途：为所有 GitHub 仓库生成结构化索引，便于 AI 检索使用

set -e

# 配置
OUTPUT_DIR="${OUTPUT_DIR:-./repo-index}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
INDEX_FILE="$OUTPUT_DIR/repo-index-$TIMESTAMP.md"
JSON_FILE="$OUTPUT_DIR/repo-index-$TIMESTAMP.json"

# 颜色输出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}开始生成 GitHub 仓库索引...${NC}"
echo ""

# 获取所有仓库
echo -e "${YELLOW}正在获取仓库列表...${NC}"
REPOS=$(gh repo list --limit 1000 --json name,nameWithOwner,description,url,primaryLanguage,stargazerCount,forkCount,createdAt,updatedAt,isPrivate,licenseInfo,defaultBranchRef,repositoryTopics,homepageUrl --jq '.')
TOTAL_COUNT=$(echo "$REPOS" | jq '. | length')

echo -e "${GREEN}找到 $TOTAL_COUNT 个仓库${NC}"
echo ""

# 创建临时文件存储单个仓库信息
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# 初始化 JSON 数组
echo "[]" > "$JSON_FILE.tmp"

# 初始化 Markdown 文件
cat > "$INDEX_FILE" << 'EOF'
# GitHub 仓库索引

> 生成时间: {TIMESTAMP}
> 仓库总数: {TOTAL_COUNT}

## 目录

- [仓库概览](#仓库概览)
- [仓库详情](#仓库详情)
- [统计数据](#统计数据)

---

## 仓库概览

| 仓库名 | 描述 | 主要语言 | Stars | Forks |
|--------|------|----------|-------|-------|
EOF

# 替换占位符
sed -i '' "s/{TIMESTAMP}/$(date '+%Y-%m-%d %H:%M:%S')/" "$INDEX_FILE"
sed -i '' "s/{TOTAL_COUNT}/$TOTAL_COUNT/" "$INDEX_FILE"

# 计数器
COUNT=0
PUBLIC_COUNT=0
PRIVATE_COUNT=0
FORK_COUNT=0
LANGUAGE_STATS=""

echo -e "${YELLOW}正在分析仓库...${NC}"
echo ""

# 遍历每个仓库
echo "$REPOS" | jq -c '.[]' | while read -r repo; do
    COUNT=$((COUNT + 1))

    # 解析仓库信息
    NAME=$(echo "$repo" | jq -r '.nameWithOwner')
    DESCRIPTION=$(echo "$repo" | jq -r '.description // "无描述"')
    URL=$(echo "$repo" | jq -r '.url')
    LANGUAGE=$(echo "$repo" | jq -r '.primaryLanguage.name // "未指定"')
    STARS=$(echo "$repo" | jq -r '.stargazerCount // 0')
    FORKS=$(echo "$repo" | jq -r '.forkCount // 0')
    CREATED=$(echo "$repo" | jq -r '.createdAt // "未知"')
    UPDATED=$(echo "$repo" | jq -r '.updatedAt // "未知"')
    IS_PRIVATE=$(echo "$repo" | jq -r '.isPrivate // false')
    LICENSE=$(echo "$repo" | jq -r '.licenseInfo.name // "无"')
    DEFAULT_BRANCH=$(echo "$repo" | jq -r '.defaultBranchRef.name // "main"')
    TOPICS=$(echo "$repo" | jq -r '.repositoryTopics // []' | jq -r 'join(", ")')
    HOMEPAGE=$(echo "$repo" | jq -r '.homepageUrl // ""')

    # 统计
    if [ "$IS_PRIVATE" = "true" ]; then
        PRIVATE_COUNT=$((PRIVATE_COUNT + 1))
    else
        PUBLIC_COUNT=$((PUBLIC_COUNT + 1))
    fi

    # 添加到概览表格
    echo "| [$NAME]($URL) | ${DESCRIPTION:0:50} | $LANGUAGE | ⭐ $STARS | 🍴 $FORKS |" >> "$INDEX_FILE"

    # 收集语言统计
    if [ -n "$LANGUAGE" ] && [ "$LANGUAGE" != "null" ]; then
        LANGUAGE_STATS="$LANGUAGE_STATS,$LANGUAGE"
    fi

    # 获取 README 内容（如果存在）
    echo -e "\r${BLUE}处理进度: [$COUNT/$TOTAL_COUNT]${NC} $NAME"

    README_CONTENT=""
    # 默认禁用 README 获取以避免 API 限制，可通过环境变量启用
    if [ "${FETCH_README:-false}" = "true" ] && [ "$COUNT" -le 10 ]; then
        README=$(gh repo view "$NAME" --json readme --jq '.readme' 2>/dev/null || echo "")
        if [ "$README" != "null" ] && [ -n "$README" ]; then
            README_CONTENT=$(echo "$README" | jq -r '. // empty')
            # 清理 README（移除过多空行，限制长度）
            if [ -n "$README_CONTENT" ]; then
                README_CONTENT=$(echo "$README_CONTENT" | sed '/^$/N;/^\n$/D' | head -c 2000)
                README_CONTENT="
<details>
<summary>README 预览</summary>

\`\`\`
$README_CONTENT
\`\`\`

</details>
"
            fi
        fi
    fi

    # 获取主要文件结构（如果有权限）
    FILE_STRUCTURE=""
    # 默认禁用文件结构获取以避免 API 限制，可通过环境变量启用
    if [ "${FETCH_STRUCTURE:-false}" = "true" ] && [ "$COUNT" -le 5 ]; then
        STRUCTURE=$(gh repo view "$NAME" --json defaultBranchRef --jq '.defaultBranchRef.name' 2>/dev/null || echo "")
        if [ -n "$STRUCTURE" ]; then
            FILE_STRUCTURE=$(gh api "repos/$NAME/git/trees/$STRUCTURE?recursive=1" 2>/dev/null | jq -r '.tree[] | select(.type == "blob") | .path' | head -20 || echo "")
            if [ -n "$FILE_STRUCTURE" ]; then
                FILE_STRUCTURE="
<details>
<summary>主要文件结构</summary>

\`\`\`
$FILE_STRUCTURE
\`\`\`

</details>
"
            fi
        fi
    fi

    # 保存单个仓库详情到临时文件
    cat > "$TEMP_DIR/${COUNT}.md" << EOF
### $COUNT. [$NAME]($URL)

**描述**: $DESCRIPTION

**基本信息**
- 📂 语言: $LANGUAGE
- ⭐ Stars: $STARS
- 🍴 Forks: $FORKS
- 🔒 可见性: $( [ "$IS_PRIVATE" = "true" ] && echo "私有" || echo "公开" )
- 📄 许可证: $LICENSE
- 🌿 默认分支: $DEFAULT_BRANCH
- 📅 创建时间: $CREATED
- 🔄 更新时间: $UPDATED

**标签**: $TOPICS

**主页**: ${HOMEPAGE:-无}

$FILE_STRUCTURE
$README_CONTENT

---
EOF

    # 添加到 JSON
    TMP=$(mktemp)
    jq --argjson newobj "$(echo "$repo" | jq -c '{
        nameWithOwner,
        description,
        url,
        primaryLanguage,
        stargazerCount,
        forkCount,
        createdAt,
        updatedAt,
        isPrivate,
        licenseInfo,
        defaultBranchRef,
        repositoryTopics,
        homepageUrl,
        readmePreview: (if .readme then .readme[0:500] else null end)
    }')" '. += [$newobj]' "$JSON_FILE.tmp" > "$TMP"
    mv "$TMP" "$JSON_FILE.tmp"
done

echo ""
echo -e "${GREEN}仓库分析完成${NC}"
echo ""

# 合并所有详情到 Markdown 文件
echo "" >> "$INDEX_FILE"
echo "---" >> "$INDEX_FILE"
echo "" >> "$INDEX_FILE"
echo "## 仓库详情" >> "$INDEX_FILE"
echo "" >> "$INDEX_FILE"

# 合并临时文件
for file in "$TEMP_DIR"/*.md; do
    cat "$file" >> "$INDEX_FILE"
    echo "" >> "$INDEX_FILE"
done

# 添加统计部分
cat >> "$INDEX_FILE" << 'EOF'

---

## 统计数据

### 仓库类型
EOF

echo "- 公开仓库: $PUBLIC_COUNT" >> "$INDEX_FILE"
echo "- 私有仓库: $PRIVATE_COUNT" >> "$INDEX_FILE"
echo "- 总仓库数: $TOTAL_COUNT" >> "$INDEX_FILE"

echo "" >> "$INDEX_FILE"
echo "### 语言分布" >> "$INDEX_FILE"
echo "" >> "$INDEX_FILE"

# 统计语言使用
echo "$LANGUAGE_STATS" | tr ',' '\n' | sort | uniq -c | sort -rn | head -20 | \
    awk '{print "- "$2": "$1" 个仓库"}' >> "$INDEX_FILE"

# 完成 JSON 文件
mv "$JSON_FILE.tmp" "$JSON_FILE"

echo ""
echo -e "${GREEN}✓ 索引生成完成！${NC}"
echo ""
echo -e "${BLUE}输出文件:${NC}"
echo "  - Markdown: $INDEX_FILE"
echo "  - JSON: $JSON_FILE"
echo ""
echo -e "${BLUE}统计信息:${NC}"
echo "  - 总仓库数: $TOTAL_COUNT"
echo "  - 公开仓库: $PUBLIC_COUNT"
echo "  - 私有仓库: $PRIVATE_COUNT"
echo ""

# 可选：创建最新的符号链接
LATEST_MD="$OUTPUT_DIR/repo-index-latest.md"
LATEST_JSON="$OUTPUT_DIR/repo-index-latest.json"
ln -sf "$(basename "$INDEX_FILE")" "$LATEST_MD"
ln -sf "$(basename "$JSON_FILE")" "$LATEST_JSON"

echo -e "${GREEN}✓ 已创建最新版本链接:${NC}"
echo "  - $LATEST_MD"
echo "  - $LATEST_JSON"
echo ""

echo -e "${YELLOW}使用说明:${NC}"
echo "  基本用法: bash github-repo-idx.sh"
echo ""
echo "  环境变量:"
echo "    OUTPUT_DIR            - 输出目录（默认: ./repo-index）"
echo "    FETCH_README=true     - 启用 README 获取（默认: false，避免 API 限制）"
echo "    FETCH_STRUCTURE=true  - 启用文件结构获取（默认: false，避免 API 限制）"
echo ""
echo "  示例:"
echo "    OUTPUT_DIR=./output FETCH_README=true bash github-repo-idx.sh"
echo ""
echo "  注意:"
echo "    - Markdown 版本适合人类阅读和作为项目文档"
echo "    - JSON 版本适合程序化处理和 AI 工具集成"
echo "    - 启用 README 或文件结构会消耗额外的 GitHub API 配额"
echo ""

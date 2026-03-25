#!/usr/bin/env bash

set -u

DEFAULT_AGENT="codex"
DEFAULT_REPO="hocgin/agent-skills"
DEFAULT_REF="main"

AGENT="$DEFAULT_AGENT"
BUNDLE_NAME=""
REPO_SLUG="$DEFAULT_REPO"
REF_NAME="$DEFAULT_REF"
ASSUME_YES=true
DRY_RUN=false
LIST_ONLY=false

usage() {
  cat <<'EOF'
Usage:
  install.sh --with <bundle> [--agent <agent>] [--repo <owner/repo>] [--ref <git-ref>] [--dry-run]
  install.sh --list [--repo <owner/repo>] [--ref <git-ref>]

Options:
  --with <bundle>   指定要安装的 bundle 名称
  --agent <agent>   指定目标 agent，默认 codex
  --repo <repo>     指定仓库，默认 hocgin/agent-skills
  --ref <ref>       指定分支或标签，默认 main
  --dry-run         只打印命令，不执行安装
  --list            列出可用 bundle
  -y, --yes         安装时自动确认
  -h, --help        显示帮助
EOF
}

log() {
  printf '%s\n' "$*"
}

err() {
  printf 'Error: %s\n' "$*" >&2
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    err "缺少依赖命令: $1"
    exit 1
  fi
}

raw_url() {
  local path="$1"
  printf 'https://raw.githubusercontent.com/%s/%s/%s' "$REPO_SLUG" "$REF_NAME" "$path"
}

fetch_text() {
  local url="$1"
  curl -fsSL "$url"
}

read_source() {
  local path="$1"
  local local_path
  local_path="./${path}"

  # 本地开发时优先读取仓库文件，远程执行时再回退到 raw 地址。
  if [ -f "$local_path" ]; then
    cat "$local_path"
    return 0
  fi

  fetch_text "$(raw_url "$path")"
}

list_bundles() {
  # 通过索引统一暴露可用 bundle，避免远程脚本扫描目录。
  if ! read_source "bundle/index.json" | python3 -c '
import json
import sys

data = json.load(sys.stdin)
for item in data.get("bundles", []):
    name = item.get("name", "")
    description = item.get("description", "")
    if description:
        print(f"{name}\t{description}")
    else:
        print(name)
'
  then
    err "无法读取 bundle 索引"
    exit 1
  fi
}

parse_bundle() {
  python3 -c '
import json
import sys

data = json.load(sys.stdin)
for item in data.get("skills", []):
    if item.get("enabled", True) is False:
        continue
    repo = item.get("repo", "").strip()
    skill = item.get("skill", "").strip()
    agent = item.get("agent", "").strip()
    if not repo or not skill:
        continue
    print("\t".join([
        repo,
        skill,
        agent,
    ]))
'
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --with)
      BUNDLE_NAME="${2:-}"
      shift 2
      ;;
    --agent)
      AGENT="${2:-}"
      shift 2
      ;;
    --repo)
      REPO_SLUG="${2:-}"
      shift 2
      ;;
    --ref)
      REF_NAME="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --list)
      LIST_ONLY=true
      shift
      ;;
    -y|--yes)
      ASSUME_YES=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      err "未知参数: $1"
      usage
      exit 1
      ;;
  esac
done

require_cmd curl
require_cmd python3

if [ "$LIST_ONLY" = true ]; then
  list_bundles
  exit 0
fi

if [ -z "$BUNDLE_NAME" ]; then
  err "必须通过 --with 指定 bundle"
  usage
  exit 1
fi

require_cmd npx

bundle_path="bundle/${BUNDLE_NAME}/skills.json"

log "Bundle: $BUNDLE_NAME"
log "Agent: $AGENT"
if [ -f "./${bundle_path}" ]; then
  log "Source: ./${bundle_path}"
else
  log "Source: $(raw_url "$bundle_path")"
fi

if ! bundle_content="$(read_source "$bundle_path")"; then
  err "无法读取 bundle: $BUNDLE_NAME"
  exit 1
fi

success_count=0
failed_count=0
failed_items=""

# 逐条执行安装，失败时继续，最后统一汇总。
while IFS=$'\t' read -r repo skill item_agent; do
  [ -z "$repo" ] && continue

  effective_agent="$AGENT"
  if [ -n "$item_agent" ]; then
    effective_agent="$item_agent"
  fi

  cmd=(npx skills add "$repo" --skill "$skill" -a "$effective_agent")
  if [ "$ASSUME_YES" = true ]; then
    cmd+=(-y)
  fi

  log ""
  log "Installing: $skill <- $repo"
  printf 'Command:'
  printf ' %q' "${cmd[@]}"
  printf '\n'

  if [ "$DRY_RUN" = true ]; then
    success_count=$((success_count + 1))
    continue
  fi

  # 避免安装命令消费 while read 的标准输入，导致后续 skill 被跳过。
  if "${cmd[@]}" </dev/null; then
    success_count=$((success_count + 1))
  else
    failed_count=$((failed_count + 1))
    failed_items="${failed_items}\n- ${skill} (${repo})"
  fi
done < <(printf '%s' "$bundle_content" | parse_bundle)

log ""
log "Summary: success=${success_count}, failed=${failed_count}"

if [ "$failed_count" -gt 0 ]; then
  printf 'Failed items:%b\n' "$failed_items" >&2
  exit 1
fi

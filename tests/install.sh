#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
FAKE_BIN="$TMP_DIR/bin"
mkdir -p "$FAKE_BIN"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

assert_contains() {
  local haystack="$1"
  local needle="$2"
  local message="$3"

  if [[ "$haystack" != *"$needle"* ]]; then
    printf 'Assertion failed: %s\n' "$message" >&2
    exit 1
  fi
}

assert_equals() {
  local expected="$1"
  local actual="$2"
  local message="$3"

  if [[ "$expected" != "$actual" ]]; then
    printf 'Assertion failed: %s\nExpected: %s\nActual: %s\n' "$message" "$expected" "$actual" >&2
    exit 1
  fi
}

run_test() {
  local name="$1"
  shift

  printf 'Running %s\n' "$name"
  "$@"
}

test_list_uses_local_index() {
  local output
  output="$(cd "$ROOT_DIR" && bash install.sh --list)"
  assert_contains "$output" $'ios-dev\tiOS 开发常用 skill 集合' "应列出 ios-dev bundle"
  assert_contains "$output" $'frontend\t前端设计与工程常用 skill 集合' "应列出 frontend bundle"
  assert_contains "$output" $'nextjs\t静态站点与 Next.js 常用 skill 集合' "应列出 nextjs bundle"
  assert_contains "$output" $'browser-extension\t浏览器插件开发常用 skill 集合' "应列出 browser-extension bundle"
  assert_contains "$output" $'video-production\t视频制作常用 skill 集合' "应列出 video-production bundle"
  assert_contains "$output" $'cloudflare\tCloudflare 站点与 Workers 常用 skill 集合' "应列出 cloudflare bundle"
}

test_file_installs_all_skills() {
  cat > "$FAKE_BIN/npx" <<'EOF'
#!/usr/bin/env bash
cat >/dev/null
printf '%s\n' "$*" >> "$TEST_LOG"
exit 0
EOF
  chmod +x "$FAKE_BIN/npx"

  local output
  output="$(
    cd "$ROOT_DIR" && \
    TEST_LOG="$TMP_DIR/npx.log" PATH="$FAKE_BIN:$PATH" bash install.sh --agent codex --file ./bundle/ios-dev/skills.json
  )"

  local line_count
  line_count="$(wc -l < "$TMP_DIR/npx.log" | tr -d ' ')"
  assert_equals "10" "$line_count" "应通过 --file 安装完整的 10 个 skill"
  assert_contains "$output" "Bundle: ios-dev" "--file 模式应优先显示清单中的 bundle 名称"
  assert_contains "$output" "Summary: success=10, failed=0" "应汇总 10 个安装成功"
}

test_file_and_with_conflict() {
  local output
  set +e
  output="$(cd "$ROOT_DIR" && bash install.sh --with ios-dev --file ./bundle/ios-dev/skills.json 2>&1)"
  local status=$?
  set -e

  assert_equals "1" "$status" "--with 与 --file 同时传入时应失败"
  assert_contains "$output" "--file 与 --with 不能同时使用" "应提示参数冲突"
}

run_test "list_uses_local_index" test_list_uses_local_index
run_test "file_installs_all_skills" test_file_installs_all_skills
run_test "file_and_with_conflict" test_file_and_with_conflict

printf 'All tests passed\n'

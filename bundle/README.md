# Bundle 说明

`bundle` 目录用于维护可批量安装的 skill 清单，供根目录的 [install.sh](/Users/hocgin/Projects/agent-skills/install.sh) 读取。

## 目录约定

```text
bundle/
  README.md
  index.json
  ios-dev/
    skills.json
  frontend/
    skills.json
```

- `index.json`：声明可用 bundle 列表，供 `install.sh --list` 使用
- `bundle/<name>/skills.json`：某个 bundle 的具体 skill 清单

## index.json 格式

```json
{
  "bundles": [
    {
      "name": "ios-dev",
      "description": "iOS 开发常用 skill 集合"
    }
  ]
}
```

字段说明：

- `name`：bundle 名称，对应 `--with <name>`
- `description`：bundle 描述，会在 `--list` 时展示

## skills.json 格式

```json
{
  "name": "ios-dev",
  "description": "iOS 开发常用 skill 集合",
  "skills": [
    {
      "repo": "https://github.com/obra/superpowers",
      "skill": "executing-plans"
    },
    {
      "repo": "https://github.com/hocgin/agent-skills",
      "skill": "swift-private-bundle",
      "agent": "codex",
      "enabled": true
    }
  ]
}
```

字段说明：

- `repo`：`npx skills add` 使用的 skill 仓库地址
- `skill`：要安装的 skill 名称
- `agent`：可选，覆盖命令行传入的 `--agent`
- `enabled`：可选，设为 `false` 时跳过该项

## 使用方式

列出 bundle：

```shell
bash install.sh --list
```

按 bundle 安装：

```shell
bash install.sh --agent codex --with ios-dev
```

通过本地文件安装：

```shell
bash install.sh --agent codex --file ./bundle/ios-dev/skills.json
```

仅预览命令：

```shell
bash install.sh --agent codex --with frontend --dry-run
```

## 新增 bundle 步骤

1. 新建 `bundle/<name>/skills.json`
2. 在 `bundle/index.json` 中追加对应条目
3. 执行 `bash install.sh --with <name> --dry-run` 验证输出
4. 如需本地文件验证，可执行 `bash install.sh --file ./bundle/<name>/skills.json --dry-run`

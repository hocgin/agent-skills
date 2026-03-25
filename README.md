# agent-skills

## 安装

### Use Skills

```shell
npx skills add hocgin/agent-skills
```

**OR**

### Bundle Installer

```shell
curl -fsSL https://raw.githubusercontent.com/hocgin/agent-skills/main/install.sh | bash -s -- --list
curl -fsSL https://raw.githubusercontent.com/hocgin/agent-skills/main/install.sh | bash -s -- --agent codex --with ios-dev
curl -fsSL https://raw.githubusercontent.com/hocgin/agent-skills/main/install.sh | bash -s -- --agent codex --with ios-dev --dry-run
bash install.sh --agent codex --file ./bundle/ios-dev/skills.json
```

### Claude Code Cli
```shell
/plugin marketplace add

/plugin install swift-skills
```


## 资料
- [Skills 命令使用文档](https://github.com/vercel-labs/skills)
- [Claude Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)

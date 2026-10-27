# 全局上下文与使用说明

本 skill 将 gpt-image-bridge 的可执行桥接脚本直接纳入 `bin/gpt-image-2`，可随 skill 独立分发，不需要运行时克隆上游。适用于有 shell 执行能力的编码代理。

## 来源

- 上游：[oakplank/gpt-image-bridge](https://github.com/oakplank/gpt-image-bridge)。
- main 基线：`5c49f1a36d91ba411b5cec96859cd0a3f0a5c2dc`。
- 集成：[PR #5 — Add --ref option for reference images](https://github.com/oakplank/gpt-image-bridge/pull/5)。
- PR head：`d6b51cbb562e4710fbb0060f02a23b32519f78fa`。截至导入时（2026-10-27），PR 仍未合并。
- 代码使用 MIT 许可，原始版权声明见 [LICENSE](../LICENSE)。

从 PR head 导入完整运行脚本，包含 main 的功能和 PR 的参考图支持；本地增加 `--ref` / `--size` 缺少值时的清晰错误，避免 Bash `set -u` 导致未绑定变量报错。移除注释中的固定图片模型版本承诺。使用说明改为适配当前 skill 所在目录，不绑定 Claude 安装路径。

上游根目录的 `install.sh` 只负责复制到 `~/.claude/skills`，本仓库沿用已有 skill 安装方式，因此不复制该安装器，也不附带与执行无关的宣传图片。

## 文件与入口

| 文件 | 用途 |
| --- | --- |
| `SKILL.md` | 代理工作流程 |
| `bin/gpt-image-2` | 实际运行脚本 |
| `docs/01_API_REFERENCE.md` | 参数、输出、退出码 |
| `docs/02_ARCHITECTURE.md` | 临时目录与参数传递逻辑 |
| `docs/03_GUIDES/quick-start.md` | 安装与文生图示例 |
| `docs/03_GUIDES/reference-images.md` | 单图编辑与多参考图 |
| `docs/04_CHANGELOG.md` | 导入与修改记录 |

## 验证

在 agent-skills 仓库根目录运行：

```bash
bash -n skills/gpt-image-bridge/bin/gpt-image-2
python3 -m unittest discover -s tests -p 'test_gpt_image_bridge.py' -v
```

测试通过隔离 PATH 中的模拟 `codex` 验证命令参数、输出及失败语义，不访问真实服务或消耗账户额度。端到端可用性仍取决于本机 Codex 版本、登录账户和图片工具权限。

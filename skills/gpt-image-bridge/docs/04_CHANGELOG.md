# 版本更新记录

## 2026-10-27

- 从 oakplank/gpt-image-bridge main `5c49f1a36d91ba411b5cec96859cd0a3f0a5c2dc` 引入运行脚本和 MIT 许可。
- 集成 PR #5 head `d6b51cbb562e4710fbb0060f02a23b32519f78fa`：可重复 `--ref`、文件存在检查、绝对路径解析、Windows 路径转换，以及参考图提示词和 `--image=` 传递。
- 补充缺少 `--ref` / `--size` 值的参数错误处理，保留 Bash 3.2 兼容写法。
- 增加中文 skill 指令、按仓库规范组织的文档、模拟 Codex 的命令行回归测试。
- 在 Codex 和 Claude 插件市场的图片技能组注册此 skill。

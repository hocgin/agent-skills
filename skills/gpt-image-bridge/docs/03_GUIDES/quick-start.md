# 快速入门

## 安装 skill

在任意目录使用本仓库的 skill 安装方式：

```bash
npx skills add hocgin/agent-skills --skill gpt-image-bridge
```

本地开发时也可直接使用仓库里的 `skills/gpt-image-bridge`，无需运行上游的 Claude 专用安装脚本。

## 检查 Codex

确认 `codex` 在 PATH，并使用有图片生成权限的 ChatGPT 账户登录：

```bash
codex --version
codex login status
```

如未登录，运行 `codex login` 完成交互认证。若当前版本报告图片工具不可用，检查该版本能力及账户权限。

## 生成图片

下面在 agent-skills 仓库根目录运行；安装到其他位置时改为实际脚本路径：

```bash
mkdir -p /tmp/gpt-image-bridge-output
./skills/gpt-image-bridge/bin/gpt-image-2 \
  "A red balloon floating above a quiet seaside town, warm morning light, hand-painted watercolor, no text" \
  /tmp/gpt-image-bridge-output/balloon.png \
  --size 1024x1024
```

等待进程完成，读取 stdout 返回的图片进行检查。尺寸是生成请求，需要检查实际结果。调用真实 Codex 会消耗当前登录账户的额度。参考图操作见 [参考图指南](reference-images.md)。

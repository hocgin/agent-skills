---
name: bitrig-simulator-use
description: 操作 macOS Bitrig 的内置模拟器，包括查看和测试运行中的 App、切换机型、操作 iPhone Duo 铰链、截图、录屏、录制带机身的 3D 预览及读取运行日志。用户明确指定 Bitrig 或其 Simulator Use 插件时使用。
---

# Bitrig 模拟器操作

按交付画面选择入口。测试模拟器内的 App、读日志，以及只含屏幕像素的截图或 MP4，使用 Bitrig 的 Simulator Use MCP。需要机身、边框、铰链动画或 3D 场景时，操作 Bitrig 桌面窗口的 **Recording Mode**。

## Simulator Use MCP

在 Bitrig 自带 Agent 会话中使用 `simulator_exec`。有明确 ID 时调用 `simulator.getSimulator(id)`，否则先用 `simulator.listSimulators()`。获取目标会自动返回初始无障碍状态。每批交互后读取最新 AX 状态，再从其中选取元素索引。

操作、机型切换、截图、录屏、权限和外部会话衔接见 [Simulator Use MCP](references/simulator-mcp.md)。用户只要求控制已运行的 App 时，沿用现有预览。

## 录制 3D 预览

以下路径在 Bitrig 0.34.0（构建 3400）验证过。

1. 通过 macOS Computer Use 选中 Bitrig 的活动项目窗口。确认预览正在运行，并用 AX 确认机型及录制控件。Duo 有 **Closed**、**Partially Open**、**Fully Open** 三个控件。
2. 点击预览的 **Recording Mode**，或从菜单栏选择 **Preview → Enter Recording Mode**。构图、分辨率和背景按用户要求设置。
3. 点击 **Start Recording**。等倒计时结束并出现 **Stop Recording** 后开始演示。用最新 AX 树定位折叠和录制按钮。
4. 点击 **Stop Recording**，读取 **Recording Saved** 通知。通知消失时，在 Bitrig 配置的录制目录按本次开始时间查找新 MP4。先确认文件存在且可解码；涉及外壳、铰链或特定交互时，抽查对应画面。用户指定输出路径时，将已验证的产物保存到该处，避免覆盖现有文件。

Duo 的合拢至展开演示可复用 [录制脚本](scripts/record-duo-3d.js)。在 Codex Computer Use 的 JavaScript 会话中先绑定 Bitrig App，再执行脚本定义。每次 `next()` 单独调用，直到 `done: true`。这样可避开单次 Computer Use 调用的交互上限。脚本按 Bitrig 的设置保存，`filename: null` 表示没有读到短暂的保存通知，需在录制目录核验文件。

在已检查版本中，3D 录制使用桌面 Recording Mode。内置 Swift 命令属于当前预览的进程内回调，安装版没有已验证的外部 3D 录制 MCP、CLI 或 URL 入口。

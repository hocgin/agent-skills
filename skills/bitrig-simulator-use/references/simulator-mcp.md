# Simulator Use MCP

按当前 Bitrig 版本核对内置说明。以默认安装路径为例：

```text
/Applications/Bitrig.app/Contents/Resources/BitrigAI_BitrigAI.bundle/Contents/Resources/bitrig-simulator-use-plugin/skills/simulator-use/SKILL.md
```

插件通过 `bitrigMCP simulator-use` 启动并继承 `BITRIG_MCP_SOCKET`。在 0.34.0 中，独立客户端即使连上运行中的 socket，也可能只得到空的 `tools/list`。可将任务交给 Bitrig 自带 Agent 会话运行 `simulator_exec`，再核对其工具结果和产物。对 Bitrig 桌面界面或 3D 录制控件，使用 macOS Computer Use。

## 目标与操作

- `simulator.listSimulators()` 返回目标 ID、状态和兼容机型。实例处于 `off` 时，`getSimulator(id)` 会尝试启动并等待。切换机型需要 `deviceModels` 中的精确名称，`changeDevice(name)` 后重新读取状态。
- `getAXState()` 默认返回增量。需要完整树时传 `{ disableDiffing: true }`。截图观察后，重新读完整树再使用元素索引。通过 `getScreenshot()` 或 `getAXStateAndScreenshot()` 核对视觉结果。
- 优先用最新的元素索引调用 `tap()`、`touchHold()`、`scroll()` 和 `setValue()`。没有可用元素时，根据截图用坐标 `tap()` 或 `drag()`。`typeText()` 的换行会模拟 Return，可能触发表单提交。`pressKey("command+c")` 支持组合键。
- `performAction()` 支持 `home`、`app_switcher`、`lock`、`siri`。`getSettings()` / `setSetting()` 可控制外观、方向、文字大小及部分辅助功能。
- iPhone Duo 支持 `duo.getHingeState()` 和 `duo.setHingeState({ orientation: "portrait", angleDegrees: 120 })`。角度范围为 0–180°，读取结果反映最后请求的角度。核对实际显示时使用截图。
- `getRunLog({ glob, pattern })` 读取模拟器运行日志，允许省略任一筛选条件。

如果工具明确要求访问权限，在单独的 `simulator_exec` 调用里运行 `simulator.requestAccess()`，并设置 `timeout_ms: 610000`。权限获准后再继续。

## 保存截图与屏幕录制

- `saveScreenshot({ path })` 保存 PNG。显式路径须为绝对路径且以 `.png` 结尾。
- `startRecording({ path, display })` 开始屏幕录制。显式路径须为绝对路径且以 `.mp4` 结尾，已有同名文件可能被覆盖。Duo 的 `display` 可选 `inner` 或 `outer`，省略时录制当前显示屏。
- 在同一个 Bitrig Agent 回合调用 `stopRecording()` 完成保存。可跨多次 `simulator_exec` 操作。录制最多捕获 5 分钟，回合结束时仍在录制的内容会被丢弃。切换机型前先停止录制。
- 截图和录屏支持 `applyStatusBarOverrides` 和 24 小时格式的 `statusBarTime`。优先沿用默认值。
- `stopRecording()` 返回路径、时长和播放尺寸。需要核验交付时检查落盘结果。视频轨的编码宽高可能受旋转元数据影响。

```js
// 在同一 Agent 回合中分步运行。目标 ID 取自 listSimulators()。
const sim = await simulator.getSimulator("builtin/iphone");
await sim.startRecording({ path: "/absolute/path/demo.mp4", display: "inner" });
// 通过 sim 操作界面，按需读取新的 AX 状态。
text(await sim.stopRecording());
```

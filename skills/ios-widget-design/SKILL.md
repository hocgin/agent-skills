---
name: ios-widget-design
description: 依据 Apple Human Interface Guidelines 设计与实现 iOS/iPadOS/macOS/watchOS/visionOS 小组件（WidgetKit）。适用于：创建或修改主屏幕/锁屏/桌面小组件、选择小组件尺寸（system small/medium/large/extra large、accessory circular/rectangular/inline/corner）、处理渲染模式（fullColor/accented/vibrant）与外观（tinted/clear/深浅色）、设计小组件视觉稿、编写 SwiftUI WidgetKit 代码、交互式小组件（按钮/开关/深链）、适配 StandBy/CarPlay/Apple Watch Smart Stack 与表盘复杂功能。触发词：widget、小组件、WidgetKit、Lock Screen widget、Home Screen widget、锁屏组件、桌面小组件、complication、Smart Stack。
---

# iOS 小组件设计（Apple HIG Widgets）

基于 Apple Human Interface Guidelines（2025-12 更新版）整理。设计小组件时按以下流程执行，细节按需查阅 references。

## 第一步：确定平台与出现位置

先明确小组件出现在哪里，再决定支持的尺寸。不同位置的系统外观处理完全不同。

**System family（系统尺寸族）出现位置：**

| 尺寸 | iPhone | iPad | Mac | Apple Vision Pro |
|---|---|---|---|---|
| systemSmall | 主屏、Today 视图、StandBy、CarPlay | 主屏、Today 视图、锁屏 | 桌面、通知中心 | 水平/垂直表面 |
| systemMedium | 主屏、Today 视图 | 主屏、Today 视图 | 桌面、通知中心 | 水平/垂直表面 |
| systemLarge | 主屏、Today 视图 | 主屏、Today 视图 | 桌面、通知中心 | 水平/垂直表面 |
| systemExtraLarge | 不支持 | 主屏、Today 视图 | 桌面、通知中心 | 水平/垂直表面 |

**Accessory（附件族，信息量极小）：**

| 尺寸 | iPhone/iPad | Apple Watch |
|---|---|---|
| accessoryCircular | 锁屏 | 表盘复杂功能 + Smart Stack |
| accessoryRectangular | 锁屏 | 表盘复杂功能 + Smart Stack |
| accessoryInline | 锁屏（时钟上方文字行） | 表盘复杂功能 |
| accessoryCorner | 不支持 | 表盘复杂功能 |

完整设计准则见 [references/design-guidelines.md](references/design-guidelines.md)（含 visionOS 挂载/处理风格、watchOS Smart Stack、StandBy/CarPlay、Always-On 等平台特化规则）。

## 第二步：布局的硬性数值

- **边距**：标准 16pt；仅在图形、按钮分组或背景形状需要时收窄到 11pt。Mac 桌面与锁屏（含 StandBy）系统边距更小。
- **圆角**：内容圆角跟随容器圆角，实现用 `ContainerRelativeShape`，不要写死数值。
- **字号**：不小于 11pt。优先系统字体（SF Pro）+ SF Symbols；自定义字体仅用于大号文字，小字仍用系统字体。
- **Dynamic Type**：iOS/iPadOS/visionOS 需支持 Large 到 AX5。
- **深浅色**：用语义色（`.systemBackground` 等）或 asset catalog 双外观变体，同时支持 light/dark。
- **内容适配**：设计稿按大设备尺寸提供，系统会自动缩放；生产实现必须用 SwiftUI 弹性布局，不要为单一机型写死尺寸。

各机型精确尺寸（pt）见 [references/specifications.md](references/specifications.md)。速查：iPhone 393×852 机型 small=158×158、medium=338×158、large=338×354；锁屏 circular=72×72、rectangular=160×72、inline=234×26。

## 第三步：外观与渲染模式

用户可能给小组件选择不同外观，系统按位置应用三种渲染模式：

| 渲染模式 | 何时出现 | 系统处理 | 设计要点 |
|---|---|---|---|
| fullColor 全彩 | 各平台主屏/Today/桌面/Smart Stack | 不改变视图颜色 | 支持深浅色双背景 |
| accented 着色 | iOS 18+ 主屏/Today；visionOS 调色后 | 去背景，替换为着色或 Liquid Glass 效果 | 视图分为 accent 组与 primary 组，用 `.widgetAccentable()` 指定 accent 组 |
| vibrant 鲜活 | iPhone/iPad 锁屏；StandBy 低光 | 去饱和，按像素亮度/透明度混合背景材质 | 内容按不透明灰度渲染：白色/浅灰给主内容，深灰给次要内容 |

主屏另有 4 种外观可选：light、dark、clear（去饱和 + 半透明 + Liquid Glass）、tinted（去饱和后整体着色）。tinted/clear 下系统默认去饱和全彩图片；仅媒体内容（如专辑封面）建议保留全彩，且尺寸小于组件本身。不要仅靠颜色传达信息（watchOS 可能反转颜色）。

## 第四步：内容设计原则

- **每个尺寸一个焦点**：small 通常只放一条信息；尺寸增大时增加信息层级，而不是把小尺寸内容放大填空。
- **一瞥可读（glanceable）**：密度平衡——过疏显得无用，过密降低可读性；信息层级让主要内容一眼可见。
- **内容随时间变化**：静态内容会被移出显眼位置；必要时显示"最后更新时间"。
- **品牌元素适度**：品牌色/字体/字形足以识别，通常无需 logo；确需 logo 时放右上角即可。
- **不要在 App 内复刻小组件外观**：外观像但行为不同会让人困惑。

## 第五步：交互

- 点击组件主体 → 打开 App 并**深链到对应内容**（如点股票组件直达该股票详情页），不要让用户再导航。
- 可用 Button/Toggle 提供组件内交互（如提醒事项勾选完成），保持克制、目标尺寸足够大。
- accessoryInline 只有一个 tap target；small 组件整体只有一个点击目标（用 `.widgetURL`）。
- 数据更新动画时长不超过 2 秒。

## 第六步：预览、占位与描述

- **Gallery 预览**：展示真实或有说服力的模拟数据，清晰体现每个尺寸的能力。
- **占位内容**：数据加载时用静态组件 + 半透明形状（矩形代文字行、圆形代图形）占位。
- **描述**：以动词开头，如"查看某地的当前天气和预报"；不要写"此小组件会…"。多个尺寸共用一条描述并归组展示。

## 第七步：SwiftUI 实现要点

- iOS 17+ 必须用 `containerBackground(for: .widget)` 包裹内容（StandBy、深色模式、Liquid Glass 依赖它）。
- 用 `.widgetAccentable()` 标记 accent 组；用 `\.widgetRenderingMode`、`\.widgetContentMargins` 环境值适配各模式。
- 时间日期交给系统自动刷新（`Text(date, style:)`），节省更新预算；组件不支持实时更新，实时内容用 Live Activities。
- 交互用 `Button(intent:)`/`Toggle(intent:)` + AppIntent；导航用 `.widgetURL` / `Link`。

代码模式与模板见 [references/swiftui-patterns.md](references/swiftui-patterns.md)。

## References

- [references/design-guidelines.md](references/design-guidelines.md) — HIG 完整设计准则：最佳实践、内容更新、交互、文本、颜色、渲染模式细节、预览占位、各平台特化（iOS 锁屏/Always-On/Live Activities、StandBy/CarPlay、visionOS 阈值/挂载/处理风格、watchOS Smart Stack）
- [references/specifications.md](references/specifications.md) — 全平台精确尺寸表：iOS 全机型、iPadOS Canvas/Device、visionOS pt+mm、watchOS Smart Stack
- [references/swiftui-patterns.md](references/swiftui-patterns.md) — WidgetKit/SwiftUI 实现模式：配置、containerBackground、accented/vibrant 适配、交互、深链、占位与预览

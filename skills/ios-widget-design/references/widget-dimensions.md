# WidgetKit 小组件类型与尺寸

此表将 WidgetKit 家族与 Apple 当前的 Widgets HIG 规格对应起来。规范来源：[Widgets — Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/widgets)；家族可用性来源：[Developing a WidgetKit strategy](https://developer.apple.com/documentation/WidgetKit/Developing-a-WidgetKit-strategy)。已核对：2026-08-25。

所有数值均为 **pt**，格式为 **宽 × 高**，而非像素。尺寸随设备屏幕而变；它们用于视觉稿、评审和参考实现，不应用作 SwiftUI 的硬编码布局常量。生产代码应按 `widgetFamily` 创建弹性布局，并让系统进行缩放。

## 家族、平台与情境

| WidgetKit 家族 | 设计类型 | iPhone 可用位置 | iPad 可用位置 | 尺寸来源 |
| --- | --- | --- | --- | --- |
| `.systemSmall` | 小型系统小组件 | 主屏幕、Today View、StandBy | 主屏幕、Today View、锁定屏幕 | 下方 iPhone / iPadOS 系统家族表 |
| `.systemMedium` | 中型系统小组件 | 主屏幕、Today View | 主屏幕、Today View | 下方 iPhone / iPadOS 系统家族表 |
| `.systemLarge` | 大型系统小组件 | 主屏幕、Today View | 主屏幕、Today View | 下方 iPhone / iPadOS 系统家族表 |
| `.systemExtraLarge` | 超大系统小组件 | 不支持 | 主屏幕、Today View | 下方 iPadOS 系统家族表 |
| `.systemExtraLargePortrait` | 超大竖向系统小组件 | 不支持 | 不支持 | visionOS 专用，不属于本 Skill 的 iPhone/iPad 范围 |
| `.accessoryCircular` | 圆形锁屏 accessory | 锁定屏幕 | 锁定屏幕（iPadOS 17+） | iPhone 表；HIG 未列独立 iPadOS pt 表 |
| `.accessoryRectangular` | 矩形锁屏 accessory | 锁定屏幕 | 锁定屏幕（iPadOS 17+） | iPhone 表；HIG 未列独立 iPadOS pt 表 |
| `.accessoryInline` | 行内锁屏 accessory | 锁定屏幕 | 锁定屏幕（iPadOS 17+） | iPhone 表；HIG 未列独立 iPadOS pt 表 |
| `.accessoryCorner` | Apple Watch 表盘角落 complication | 不支持 | 不支持 | 不为 iPhone/iPad 设计 |

`accessoryCircular`、`accessoryRectangular` 和 `accessoryInline` 在 iPad 锁定屏幕上的支持需要 iPadOS 17 或更高版本。Apple 当前 HIG 的 iPadOS 尺寸表只列出 system 家族；不要把下方 iPhone accessory 点数标注为 iPad 的精确尺寸。对 iPad accessory 请在目标系统与设备上验证，或检查最新 Apple Design Resources。

## iPhone（HIG 的 iOS dimensions）

屏幕尺寸为竖屏点数。`N/A` 表示 Apple 的当前规格表未提供该形状；不要自行补算。

| 屏幕（竖屏） | `.systemSmall` | `.systemMedium` | `.systemLarge` | `.accessoryCircular` | `.accessoryRectangular` | `.accessoryInline` |
| --- | --- | --- | --- | --- | --- |
| 430 × 932 | 170 × 170 | 364 × 170 | 364 × 382 | 76 × 76 | 172 × 76 | 257 × 26 |
| 428 × 926 | 170 × 170 | 364 × 170 | 364 × 382 | 76 × 76 | 172 × 76 | 257 × 26 |
| 414 × 896 | 169 × 169 | 360 × 169 | 360 × 379 | 76 × 76 | 160 × 72 | 248 × 26 |
| 414 × 736 | 159 × 159 | 348 × 157 | 348 × 357 | 76 × 76 | 170 × 76 | 248 × 26 |
| 393 × 852 | 158 × 158 | 338 × 158 | 338 × 354 | 72 × 72 | 160 × 72 | 234 × 26 |
| 390 × 844 | 158 × 158 | 338 × 158 | 338 × 354 | 72 × 72 | 160 × 72 | 234 × 26 |
| 375 × 812 | 155 × 155 | 329 × 155 | 329 × 345 | 72 × 72 | 157 × 72 | 225 × 26 |
| 375 × 667 | 148 × 148 | 321 × 148 | 321 × 324 | 68 × 68 | 153 × 68 | 225 × 26 |
| 360 × 780 | 155 × 155 | 329 × 155 | 329 × 345 | 72 × 72 | 157 × 72 | 225 × 26 |
| 320 × 568 | 141 × 141 | 292 × 141 | 292 × 311 | N/A | N/A | N/A |

`.systemExtraLarge` 和 `.systemExtraLargePortrait` 没有 iPhone 尺寸，因为 iPhone 不支持这两个家族。StandBy 使用 `.systemSmall` 并由系统放大；请针对 StandBy 单独检查可读性，不要另造一个固定尺寸。

## iPadOS 系统家族

Apple 的表为同一屏幕给出 `Canvas` 与 `Device` 两个目标。HIG 说明 iPadOS 会先在较大的尺寸上渲染小组件，再缩放到主屏幕显示：因此视觉稿与评审必须保留这两个标签，不能把两者混为一个“真实尺寸”。未列出的未来屏幕尺寸以最新 HIG 和 Apple Design Resources 为准。

| 屏幕（竖屏） | 目标 | `.systemSmall` | `.systemMedium` | `.systemLarge` | `.systemExtraLarge` |
| --- | --- | --- | --- | --- | --- |
| 768 × 1024 | Canvas | 141 × 141 | 305.5 × 141 | 305.5 × 305.5 | 634.5 × 305.5 |
| 768 × 1024 | Device | 120 × 120 | 260 × 120 | 260 × 260 | 540 × 260 |
| 744 × 1133 | Canvas | 141 × 141 | 305.5 × 141 | 305.5 × 305.5 | 634.5 × 305.5 |
| 744 × 1133 | Device | 120 × 120 | 260 × 120 | 260 × 260 | 540 × 260 |
| 810 × 1080 | Canvas | 146 × 146 | 320.5 × 146 | 320.5 × 320.5 | 669 × 320.5 |
| 810 × 1080 | Device | 124 × 124 | 272 × 124 | 272 × 272 | 568 × 272 |
| 820 × 1180 | Canvas | 155 × 155 | 342 × 155 | 342 × 342 | 715.5 × 342 |
| 820 × 1180 | Device | 136 × 136 | 300 × 136 | 300 × 300 | 628 × 300 |
| 834 × 1112 | Canvas | 150 × 150 | 327.5 × 150 | 327.5 × 327.5 | 682 × 327.5 |
| 834 × 1112 | Device | 132 × 132 | 288 × 132 | 288 × 288 | 600 × 288 |
| 834 × 1194 | Canvas | 155 × 155 | 342 × 155 | 342 × 342 | 715.5 × 342 |
| 834 × 1194 | Device | 136 × 136 | 300 × 136 | 300 × 300 | 628 × 300 |
| 954 × 1373* | Canvas | 162 × 162 | 350 × 162 | 350 × 350 | 726 × 350 |
| 954 × 1373* | Device | 162 × 162 | 350 × 162 | 350 × 350 | 726 × 350 |
| 970 × 1389* | Canvas | 162 × 162 | 350 × 162 | 350 × 350 | 726 × 350 |
| 970 × 1389* | Device | 162 × 162 | 350 × 162 | 350 × 350 | 726 × 350 |
| 1024 × 1366 | Canvas | 170 × 170 | 378.5 × 170 | 378.5 × 378.5 | 795 × 378.5 |
| 1024 × 1366 | Device | 160 × 160 | 356 × 160 | 356 × 356 | 748 × 356 |
| 1192 × 1590* | Canvas | 188 × 188 | 412 × 188 | 412 × 412 | 860 × 412 |
| 1192 × 1590* | Device | 188 × 188 | 412 × 188 | 412 × 412 | 860 × 412 |

\* Apple 标注为启用 Display Zoom 的 “More Space” 时的尺寸。

## 标注与实现规则

- 设计稿标注采用：`WidgetFamily`、设备屏幕（竖屏 pt）、目标（iPad 时为 Canvas 或 Device）、宽 × 高 pt。例如：`iPhone 430 × 932 / .systemMedium / 364 × 170 pt`。
- 不要按设备型号猜测屏幕大小；先从设备的竖屏 pt 尺寸匹配表格。若无法匹配，则不输出假精确值。
- 不要在 `.systemSmall`、`.systemMedium` 等 SwiftUI 视图中用上述点数锁死 frame。用 `@Environment(\.widgetFamily)` 选择信息层级，并让容器和系统边距决定最终空间。
- iPad 的 Canvas 与 Device 数值相同并不表示可忽略目标标签；它只说明 Apple 在该特定 Display Zoom 情况下未列出缩放差异。

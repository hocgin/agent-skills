# WidgetKit / SwiftUI 实现模式

把 HIG 设计准则落地为代码的标准模式。目标 iOS 17+（accented 需 iOS 18+）。

## 目录

- [组件声明与配置](#组件声明与配置)
- [containerBackground（必需）](#containerbackground必需)
- [按尺寸族切换布局](#按尺寸族切换布局)
- [边距与圆角](#边距与圆角)
- [导航与深链](#导航与深链)
- [组件内交互（AppIntent）](#组件内交互appintent)
- [渲染模式适配](#渲染模式适配)
- [日期时间自动刷新](#日期时间自动刷新)
- [占位内容与预览](#占位内容与预览)
- [锁屏附件组件](#锁屏附件组件)
- [visionOS 挂载风格](#visionos-挂载风格)

## 组件声明与配置

用 `AppIntentConfiguration` 支持用户配置（如选择要跟踪的股票）；无需配置时用 `StaticConfiguration`：

```swift
import WidgetKit
import SwiftUI

struct StockEntry: TimelineEntry {
    let date: Date
    let symbol: String
    let price: Double
}

struct StockProvider: AppIntentTimelineProvider {
    // watchOS Smart Stack 相关性：可选实现 relevance()，配合 RelevanceKit 的 RelevantContext
    // （位置/体能训练/耳机等线索），帮助系统在恰当时机展示或上浮组件
    func relevance() async -> [WidgetRelevance<StockSelectionIntent>] { [] }

    func placeholder(in context: Context) -> StockEntry {
        StockEntry(date: .now, symbol: "AAPL", price: 189.50)
    }

    func snapshot(for configuration: StockSelectionIntent, in context: Context) async -> StockEntry {
        StockEntry(date: .now, symbol: configuration.symbol ?? "AAPL", price: 189.50)
    }

    func timeline(for configuration: StockSelectionIntent, in context: Context) async -> Timeline<StockEntry> {
        let entry = StockEntry(date: .now, symbol: configuration.symbol ?? "AAPL", price: 189.50)
        return Timeline(entries: [entry], policy: .after(.now.addingTimeInterval(3600))) // 更新预算有限，按数据变化频率定
    }
}

struct StockWidget: Widget {
    var body: some WidgetConfiguration {
        AppIntentConfiguration(
            kind: "StockWidget",
            intent: StockSelectionIntent.self,
            provider: StockProvider()
        ) { entry in
            StockWidgetView(entry: entry)
        }
        .configurationDisplayName("股票")            // Gallery 显示名
        .description("查看自选股票的实时价格走势。")   // 以动词开头，多尺寸共用一条
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}

@main
struct AppWidgets: WidgetBundle {
    var body: some Widget {
        StockWidget()
    }
}
```

## containerBackground（必需）

iOS 17+ 所有组件内容必须包在 `containerBackground(for: .widget)` 里，否则组件以白底渲染，StandBy/深色/Liquid Glass 全部异常。需要纯透明背景（如 StandBy、CarPlay 的去背景渲染）时传 `EmptyView`：

```swift
content
    .containerBackground(for: .widget) {
        Color(.systemBackground)          // 常规：语义色背景，自动适配深浅色
    }

content
    .containerBackground(for: .widget) {} // 透明背景：背景交给系统处理（StandBy/CarPlay）
```

## 按尺寸族切换布局

每个尺寸一个焦点：small 单条信息，尺寸增大扩展层级，而不是放大同一布局：

```swift
struct StockWidgetView: View {
    @Environment(\.widgetFamily) private var family
    let entry: StockEntry

    var body: some View {
        switch family {
        case .systemSmall:
            VStack(alignment: .leading) {
                Text(entry.symbol).font(.headline)
                Text(entry.price, format: .currency(code: "USD"))
                    .font(.system(size: 28, weight: .bold))
                Spacer()
            }
        case .systemMedium:
            HStack {
                VStack(alignment: .leading) { /* 主信息 */ }
                Spacer()
                Image(systemName: "chart.line.uptrend.xyaxis") // 次要层级
            }
        default:
            VStack(alignment: .leading) { /* large：主信息 + 走势图 + 列表 */ }
        }
    }
}
```

## 边距与圆角

标准边距 16pt、紧凑分组 11pt；内容圆角跟随容器，用 `ContainerRelativeShape`，不写死数值：

```swift
content
    .padding(16)                       // 标准 margin
    .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)

// 自定义背景时让填充形状继承组件容器圆角
containerBackground(for: .widget) {
    ContainerRelativeShape().fill(.blue.opacity(0.15))
}
```

锁屏 / Mac 桌面边距更小，需要精确适配时读取环境值：

```swift
@Environment(\.widgetContentMargins) private var margins
// iOS 18: 可用 .contentMarginsDisabled() 后自行布局
```

## 导航与深链

- systemSmall 整体一个点击目标：`.widgetURL`。
- medium/large 可用多个 `Link` 分区导航。
- 深链直达组件对应内容（路由 URL + App 内 `onOpenURL` 处理），不要落在首页。

```swift
content
    .widgetURL(URL(string: "myapp://stock/AAPL"))   // small：唯一 tap target

Link(destination: URL(string: "myapp://stock/AAPL")) { /* medium/large 分区 */ }
Link(destination: URL(string: "myapp://watchlist")) { /* ... */ }
```

## 组件内交互（AppIntent）

iOS 17+ 用 AppIntent 驱动 Button/Toggle，点击不离开组件、系统自动重载时间线：

```swift
struct MarkDoneIntent: AppIntent {
    static let title: LocalizedStringResource = "标记完成"
    @Parameter(title: "提醒 ID") var reminderID: String

    init() {}
    init(reminderID: String) { self.reminderID = reminderID }

    func perform() async throws -> some IntentResult {
        // 更新数据源；系统随后重载组件
        .result()
    }
}

Button(intent: MarkDoneIntent(reminderID: entry.id)) {
    Image(systemName: "circle")
}
.buttonStyle(.plain)

Toggle("完成", isOn: entry.isDone ? .on : .off) // 需要对应的 Intent
    .toggleStyle(.switch)
```

注意目标尺寸足够大、避免误触；accessoryInline 仅一个 tap target。

## 渲染模式适配

```swift
@Environment(\.widgetRenderingMode) private var renderingMode

// accented 模式（tinted/clear 外观）：把关键视图标入 accent 组，其余为 primary 组
Text(entry.price, format: .currency(code: "USD"))
    .widgetAccentable()          // iOS 18+

// 按渲染模式调整（如 vibrant 下换用单色资源）
if renderingMode == .vibrant {
    content.monochrome()
} else {
    content
}
```

- fullColor：保证深浅色双背景（语义色或 asset catalog 变体）。
- vibrant（锁屏）：内容按不透明灰度设计，白色/浅灰为主内容、深灰为次要内容。

## 日期时间自动刷新

时间交给系统渲染，不消耗更新预算：

```swift
Text(entry.date, style: .time)        // 自动刷新时钟
Text(event.startDate, style: .timer)  // 倒计时
```

更新动画不超过 2 秒；`invalidatableContent(_:)` 可在交互期间让依赖内容失效重绘。

## 占位内容与预览

```swift
// TimelineProvider.placeholder(in:) 返回有代表性的占位数据；
// 数据加载中用半透明形状示意布局（矩形代文字行、圆形代图形）
struct LoadingView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            RoundedRectangle(cornerRadius: 4).fill(.quaternary).frame(width: 60, height: 12)
            RoundedRectangle(cornerRadius: 4).fill(.quaternary).frame(width: 120, height: 20)
            Circle().fill(.quaternary).frame(width: 32, height: 32)
        }
    }
}

// Gallery 预览：previewContext 指定尺寸族 + 真实感数据
#Preview("Small", as: .systemSmall) {
    StockWidget()
} timeline: {
    StockEntry(date: .now, symbol: "AAPL", price: 189.50)
}
```

## 锁屏附件组件

在 `supportedFamilies` 中加入附件族；信息量极小，inline 只有一个 tap target：

```swift
.supportedFamilies([.accessoryCircular, .accessoryRectangular, .accessoryInline])

// accessoryCircular：一个数值/图标 + 简短标签
Gauge(value: progress) {
    Text("步数")
} currentValueLabel: {
    Text("\(steps)")
}
```

锁屏为 vibrant 渲染（单色、随背景材质）；Always-On 设备以低亮度渲染，灰阶对比要足够。

## visionOS 挂载风格

```swift
var body: some WidgetConfiguration {
    AppIntentConfiguration(/* ... */) { entry in
        WeatherWidgetView(entry: entry)
    }
    .supportedFamilies([.systemSmall, .systemLarge, .systemExtraLarge])
    .supportedMountingStyles([.elevated, .recessed]) // 默认 elevated
    .widgetTexture(.paper)                            // 可选：.paper 印刷质感 / .glass 玻璃分层
}
```

远/近两个阈值用 `\.levelOfDetail` 环境值判断（`LevelOfDetail.simplified` / `.default`）：远距离隐藏交互元素、放大字号、减少细节；近距离展示完整细节。两个层级间保持共享元素：

```swift
@Environment(\.levelOfDetail) private var levelOfDetail

var body: some View {
    if levelOfDetail == .simplified {
        simplifiedLayout  // 大字号、少细节、无交互
    } else {
        fullLayout
    }
}
```

只支持一种挂载风格的组件需拆分到单独的 WidgetConfiguration。

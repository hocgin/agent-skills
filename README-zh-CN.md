# agent-skills

Claude Code 的专用技能集合,用于增强各个领域的开发工作流程。

## 安装

```shell
npx skills add hocgin/agent-skills
```

## 可用技能

### Commit Organizer (提交组织器)
**位置:** `skills/commit-organizer`

Git 工作流专家,专门分析代码变更并创建清晰、逻辑性强的提交历史。帮助将未提交的变更组织成结构良好的提交,并附带清晰易懂的提交信息。

**使用场景:** 需要将未提交的变更组织成逻辑清晰的提交并编写清晰的提交信息时。

**主要功能:**
- 使用 `git status` 和 `git diff` 分析未提交的变更
- 将变更按逻辑分组(功能、修复、重构、文档、配置、测试)
- 遵循最佳实践创建清晰的提交信息
- 确保每个提交都是独立且可构建的
- 防止敏感数据被提交

**示例:**
```
请帮我将这些未提交的变更整理成逻辑清晰的提交。
```

---

### Swift Composable Architecture (TCA 架构)
**位置:** `skills/swift-composable-architecture`

Point-Free 的 The Composable Architecture (TCA) 专家。帮助开发者编写正确、可测试且可组合的 Swift 代码,遵循 TCA 模式。

**使用场景:** 使用 The Composable Architecture (TCA) 构建、重构、调试或测试 iOS/macOS 功能时。涵盖功能结构、副作用、依赖项、导航模式和 TestStore 测试。

**主要功能:**
- TCA 基础:State、Action、Reducer、Store
- 使用 `@Reducer` 宏的现代 TCA 模式
- 副作用和依赖管理
- 导航模式(基于树和基于栈)
- 使用 TestStore 进行测试
- 用于横切关注点的高阶 Reducer

**核心原则:**
- 单向数据流:Action → Reducer → State → View
- 状态作为值类型
- 显式副作用
- 组合优于继承
- 测试优先

**示例:**
```
帮我使用 TCA 实现一个新功能,包括适当的状态管理和测试。
```

---

### SwiftUI Animations (SwiftUI 动画)
**位置:** `skills/swiftui-animations`

SwiftUI 动画专家,用于创建流畅、高性能且符合 Apple 最佳实践的无障碍动画。

**使用场景:** 在 SwiftUI iOS/macOS 应用中构建、调试或优化动画时。涵盖隐式/显式动画、过渡效果、手势驱动交互以及现代 iOS 17+ API(如 PhaseAnimator 和 KeyframeAnimator)。

**主要功能:**
- 使用 `withAnimation` 和 `.animation()` 的隐式动画
- 使用 `Animatable` 协议的显式动画
- 过渡效果(内置和自定义)
- 手势驱动的动画
- 现代 iOS 17+ API (PhaseAnimator、KeyframeAnimator)
- 弹簧动画和时序曲线
- 无障碍考虑(减弱动态效果)

**核心原则:**
- 动画由状态变化驱动
- 事务沿视图层级向下传播
- 只有可动画数据才能动画化
- 声明式动画方法

**示例:**
```
帮我为此视图过渡创建流畅的弹簧动画,并确保遵循无障碍设置。
```

## 作者

作者信息和参考资料请参见 [AUTHOR.md](./AUTHOR.md)。

## 贡献

本项目欢迎新技能的贡献和对现有技能的改进。

## 许可证

MIT 许可证 - 具体许可信息请参阅各个技能目录。

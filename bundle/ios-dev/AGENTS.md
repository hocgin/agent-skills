# AGENTS.md

## 环境
### 技术栈
- 语言: Swift
- UI: SwiftUI
- 架构: TCA（The Composable Architecture）
- 工程管理: Tuist
- 数据持久化: SQLiteData（基于 SQLite + GRDB）

### 常用命令
- 生成 Xcode 工程配置: `tuist generate`
- 使用 `xcodebuild -list` 查看所有 scheme，避免手动猜测
- 优先通过 Package.swift 管理依赖，而不是手动拖拽

## 规范
### XCode 配置规范
- XCode 相关配置优先使用 Tuist 方式完成，并且需要保证更改后能够通过 `tuist generate` 生成正确配置
- 项目必须支持命令行构建

### 代码规范
- 优先使用 struct，避免 class
- 明确访问控制（public / internal / private）
- 禁止使用强制解包（!）
- 优先使用 async/await，避免回调地狱

### TCA 规范
- Reducer 必须可测试
- 使用 TCA 的 TestStore 编写单元测试
- 非必要不测试 UI

### 数据库操作规范
- 数据库访问必须在 Reducer 中完成
- 不允许在 View / ViewModel 中直接访问数据库
- 所有数据库操作必须走 Effect
- 优先使用数据库查询，而不是加载后过滤
- 避免加载大集合到内存
- 使用索引优化查询性能
- 保持 schema 简洁（规范化设计）

### Testing 规范
- 修复所有：测试失败（assert）、编译错误、并发（MainActor / async）问题

### 版本管理规范
- 项目创建 tag 的时候，需要按照规范重新核对整理项目文档

### 项目文档规范
> 03_GUIDES 文件夹内可根据实际情况，增减功能案例文档

```
docs/
    ├── 00_CONTEXT.md          # [核心] 全局上下文与使用说明
    ├── 01_API_REFERENCE.md    # [核心] 接口定义与类型说明
    ├── 02_ARCHITECTURE.md     # [进阶] 架构设计与核心逻辑
    ├── 03_GUIDES/             # [实操] 分场景的使用指南
    │   ├── quick-start.md     # [实操] 必需,快速入门
    └── 04_CHANGELOG.md        # [版本] 版本更新记录
```

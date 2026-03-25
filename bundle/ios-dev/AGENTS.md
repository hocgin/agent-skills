# AGENTS.md

## 环境
### 常用命令
- 生成 Xcode 工程配置: `tuist generate`
- 使用 `xcodebuild -list` 查看所有 scheme，避免手动猜测
- 优先通过 Package.swift 管理依赖，而不是手动拖拽

## 规范
### XCode 配置规范
- XCode 相关配置优先使用 Tuist 方式完成，并且需要保证更改后能够通过 `tuist generate` 生成正确配置

### Testing 规范
- 测试框架默认使用 XCTest，测试文件位于 `<ProjectName>Tests/`
- 运行全部测试 `xcodebuild test -scheme <SchemeName> -destination 'platform=iOS Simulator,name=iPhone 15'`
- 如果使用 Swift Package `swift test`
- 修复所有：测试失败（assert）、编译错误、并发（MainActor / async）问题

### 版本管理规范
- 项目创建 tag 的时候，需要按照规范重新核对整理项目文档, 03_GUIDES 文件夹内可根据实际情况，增减功能案例文档

### 项目文档规范
```
docs/
    ├── 00_CONTEXT.md          # [核心] 全局上下文与使用说明
    ├── 01_API_REFERENCE.md    # [核心] 接口定义与类型说明
    ├── 02_ARCHITECTURE.md     # [进阶] 架构设计与核心逻辑
    ├── 03_GUIDES/             # [实操] 分场景的使用指南
    │   ├── quick-start.md     # [实操] 必需,快速入门
    └── 04_CHANGELOG.md        # [版本] 版本更新记录
```

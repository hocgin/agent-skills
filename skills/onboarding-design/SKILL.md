---
name: onboarding-design
description: 根据一张或多张参考图片、App 定位和可选指定风格，提取可保存复用的 Style Profile，设计视觉一致且体现产品功能的首次启动 Onboarding，输出引导流程、全局及逐页图像/UI/实现提示词和 SwiftUI 等原生实现建议。适用于 App 首次启动引导页设计、参考图风格转译、命名风格复用和成套提示词生成。
---

# Onboarding Design

**参考图决定设计语言，项目类型决定表达内容，指定风格决定视觉方向，统一约束保证稳定性。**

交付可落地的设计方案与提示词。只有用户要求出图、编辑设计文件或写代码时才继续执行相应任务；生成方案不依赖某个图像服务或设计工具。

## 输入与默认值

| 输入 | 处理方式 |
| --- | --- |
| `project` | 名称、类型、核心功能、目标用户；从现有项目上下文推断，未知名称可用工作名。只有连产品用途都无法判断时才询问 |
| `references` | 0～多张图片，可为 Onboarding、App UI、海报、插画或产品展示图 |
| `style` | 可选，如 `glassmorphism`、`skeuomorphic`、`minimal`、`3d-playful`、`editorial`，也支持自然语言 |
| `style_id` | 可选，复用保存的完整规范；与泛风格名称 `style` 不同 |
| `profile_store` | 默认当前项目的 `.onboarding-design/styles/`；无项目时用当前任务可写目录。保存后给出绝对路径 |
| `screen_count` | 默认 3 页；价值确实需要展开时选 4～5 页，用户明确指定时遵从并记录原因 |
| `platform` / `locale` | 从项目推断；未知时 iPhone、简体中文。画布默认 393×852 **逻辑 pt 的设计基准**，并非设备固定尺寸 |
| `output_dir` | 默认当前项目的 `onboarding-design-output/`；文件与回复语言跟随用户 |

缺少非关键参数时直接继续，在结果中列出假设。推断的功能标为待确认，不把它包装为真实能力。没有参考图时如实标明；看不到图片时不得编造观察证据。若图片是唯一设计依据且不可访问，说明需要可访问的原图；其他内容可先形成草案。

## 工作流程

### 1. 确定风格来源

优先级：**明确指定的风格 > 可见参考图 > 项目适配推荐 > 默认规范**。已保存 Profile 是一份完整参考规范，通常直接复用。

- 有 `style_id` 时先用下文命令加载，不要求重新上传图片。找不到时在给定存储目录查找；仍未找到则说明缺失，不能用同一 ID 静默重建。可继续项目流程设计，但风格复用交付需要原 Profile 或用户同意创建新风格。
- 有图片时先实际查看每张图片，按 [设计原则](references/design-principles.md) 提取七个维度、1～3 个签名特征，分别记录观察、推断、置信度与来源。色值和字号若非测量所得，标为估计/规范化值。
- 多张图先分组；优先用户指定主图，否则选最吻合产品和其他参考共同特征的一组，说明依据。不要把相互冲突的风格平均混合。主风格控制渲染、材质和光照，次风格只能补充明确维度。
- 显式风格与参考不同时，列出 `retained`、`translated`、`dropped`，保留仍兼容的签名特征。风格冲突的维度遵从显式要求，禁止写出相互矛盾的指令。
- 无参考或需要转换时，按需读 [风格预设](references/style-presets.md)。预设是起点，不是把产品塞进固定模板。

### 2. 固化并保存 Style Profile

以 [style-profile.json](templates/style-profile.json) 为可运行的结构示例，填写本次规范。必须保留 `style_id`、`design_tokens`、`visual_language`、`layout_rules`、`component_rules`、`composition_rules`、`motion_rules`、`negative_constraints` 八项；字段约定见 [提示词与复用约束](references/prompt-constraints.md)。

- ID 用可读的 kebab-case，例如 `soft-glass-daylight-v1`；项目名、天气图标、唱片等具体内容不得进入可复用核心。
- 颜色、字体、间距、圆角、阴影、透明度、主次光照、透视、材质、构图变体和动效必须明确，不能只填“高级感”。
- 锁定共同设计基因，预先列出可变主体和允许的布局变体。更换项目只改内容；改核心 token 或视觉语言时保存新 ID，并填写 `derived_from`，不覆盖旧规范。
- 提取完成即保存本地命名 Profile；不把上传原图作为复用前提，不假设跨聊天记忆或云同步。

下文命令相对本 Skill 目录运行，尖括号部分替换为实际路径。脚本仅使用 Python 标准库。

```bash
python3 scripts/onboarding.py save-profile --profile <工作目录>/style-profile.json --store <项目目录>/.onboarding-design/styles
python3 scripts/onboarding.py load-profile --style-id soft-glass-daylight-v1 --store <项目目录>/.onboarding-design/styles
```

### 3. 把产品语义转成引导流程

按 [设计原则](references/design-principles.md) 建立“真实能力 → 用户价值 → 视觉隐喻 → 页面行为”的映射。默认从认识价值、理解关键能力，到开始使用；不要默认以登录、付费或系统权限收尾。

每页一个信息目标，填写 [onboarding-flow.json](templates/onboarding-flow.json)。明确标题、说明、功能、对象、场景、构图、交互、转场、资源及代码分工。每页采用 Profile 中已批准的布局变体与 token；主体、场景和信息必须不同，不能只换标题。若产品仅有一个核心能力，用使用情境/步骤展开，不能发明三个功能。

### 4. 输出 A～F 与可执行提示词

先读 [提示词约束](references/prompt-constraints.md)，使用 [输出模板](templates/prompt-template.md)。脚本将共享风格锁原样注入每个独立页面提示词，并输出图像/UI/代码三类目标的使用方式。

```bash
python3 scripts/onboarding.py validate --profile <工作目录>/style-profile.json --flow <工作目录>/onboarding-flow.json
python3 scripts/onboarding.py build --profile <工作目录>/style-profile.json --flow <工作目录>/onboarding-flow.json --output <工作目录>/design-prompts.md
```

输出必须包括：

- **A. Style Profile**：完整结构化规范、来源证据与风格决策。
- **B. Onboarding Flow**：顺序、目标、文案、视觉和行为，附完整 JSON 文件。
- **C. Global Design Prompt**：全局样式、氛围、材质、光影、构图、字体和禁止事项。
- **D. Screen Prompts**：各页可独立使用的完整提示词；附 UI 整页、纯主视觉资源、代码实现的目标适配指令。
- **E. Negative Prompt**：全局禁用事项及产品相关排除项。不支持独立负向输入时并入正向提示词。
- **F. Implementation Hints**：代码与图片边界、资源清单、安全区、不同屏幕比例、动态文字、Reduce Motion 和原生实现建议。

完整样例见 [example-output.md](examples/example-output.md)，是无参考图情况下的演示，不代表实际看过参考图。模板可直接构建该示例，但每次实际使用都需先填入当前产品事实。

### 5. 检查、修正、交付

逐项执行 [七维验收](references/design-principles.md#七维验收)：风格一致性、产品相关性、构图质量、内容完整性、提示词可执行性、可复用性、可实现性。检查失败时先改 Profile/Flow，再重新构建提示词；不得只把失败项列为最终建议。

脚本只验证结构、引用、同 ID 保存及风格锁拼装，**不能证明视觉质量或文案与产品事实相符**。人工语义检查需逐项给出证据与修正记录；没有实际出图/运行 App 时写明“方案级检查，渲染与运行验收待执行”，不能声称通过视觉或设备测试。若执行了出图，检查整组图片的材质、色彩、光照、主体差异和移动端文字区域后再交付。

交付给用户：A～F 方案、Profile/Flow/提示词文件、`style_id` 和保存路径、假设、七项检查结果及实际验证范围。将 Skill 的安装目录视为只读资源；生成文件和用户风格写入项目输出/存储目录。

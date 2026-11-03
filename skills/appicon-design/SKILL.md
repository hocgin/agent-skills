---
name: appicon-design
description: 从一张或多张 App Icon 案例图中提取设计语言（配色角色、造型语言、材质、光影、质感、细节密度），剥离参考图自身的主体 / 角色 / 布局等 IP，保存为可命名、可复用的「风格主题模板」（设计 DNA + 多版式变体 + 参考 IP 排除），再根据项目名称、类型与核心功能，按指定风格或自动匹配风格，生成原创、不撞脸参考图、符合 iOS App Icon 规范、可直接用于 GPT-Image / Midjourney / SD 等模型的完整提示词（主体描述 + 风格约束 + 版式 + 原创性约束 + 负面约束）。当用户需要设计 App 图标、iOS/macOS 应用图标、备用图标（Alternate App Icon），或想把案例图片沉淀为新的 App Icon 风格时使用。
---

# appicon-design

把案例 App Icon 的视觉语言固化成**风格主题模板（Style）**，再按项目特征生成**风格不漂移、主体不撞脸**的原创 App Icon 提示词。

核心原则：

- **设计语言由风格锁死**：材质、光影、配色角色、质感、细节密度逐字复用。
- **内容必须原创**：主体、角色、轮廓、布局为每个项目重新设计；参考图的主体 / 角色 / 布局属于**参考 IP**，任何项目都不复用。

## 风格主题模板的三层结构

| 层 | 位置 | 作用 | 复用方式 |
|---|---|---|---|
| 设计 DNA | ```style``` 块 | 「怎么画」：渲染、材质、光影、配色角色、质感 | 逐字注入，所有项目一致 |
| 版式变体 | ```composition:<layout>``` 块（2–4 个） | 「放在哪」：视角、占比、焦点与装饰位置 | 每个项目选一个（`--layout`），同系列用同一版式 |
| 参考 IP 排除 | 「参考 IP 排除」章节 + ```avoid``` 块 + `ip_terms` / `ip_labels` | 参考图的原主体、角色、标志性部件、原布局、字样 | 自动并入 negative；主体描述命中时脚本告警 |

脚本还会给每条提示词注入**原创性约束**（只借渲染语言，不借主体 / 角色 / 轮廓 / 布局）与对应负向词。

> 与 `icon-design` 的区别：`icon-design` 面向扁平的功能 / Tab 图标与成套图标；本 skill 面向**整张铺满画布的 App 主图标**，支持拟物、3D、材质、光影等更丰富的风格。

## 目录结构

```
appicon-design/
├── SKILL.md
├── README.md                    # 风格目录（含参考图预览，脚本自动生成）
├── styles/
│   ├── index.md                 # 风格注册表 + 自动匹配规则（必读）
│   ├── _template.md             # 新风格模板
│   └── <style-id>/
│       ├── style.md             # 设计 DNA + 版式变体 + 参考 IP 排除 + 提示词块
│       └── reference*.png|jpg   # 案例原图（风格锚点，可多张）
├── references/
│   ├── extract-style.md         # 从案例图提取并保存新风格的流程
│   ├── subject-design.md        # 项目 → Icon 主体的设计方法
│   └── ios-icon-rules.md        # iOS App Icon 设计规范要点
└── scripts/
    └── build_prompt.py          # 确定性拼装最终提示词 / 管理风格
```

## 工作流 A：从案例图提取风格

用户提供一张或多张案例图并要求「分析 / 提取 / 保存风格」时，按 [references/extract-style.md](references/extract-style.md) 执行：

1. **分组**：先判断多张图是否属于同一设计语言。同一语言 → 合并为一个风格（多张参考图）；不同语言 → 各自建立风格。拿不准时询问用户。
2. **拆分 DNA 与 IP**：七维只提取可迁移的设计语言；参考图的原主体、角色、标志性部件、原布局、字样全部列为**参考 IP**。签名特征必须是「手法」而不是「物件」。
3. **设计版式变体**：从参考构图抽象出原则，写 2–4 个 `composition:<layout>`，不得有任何版式与参考布局一一对应。
4. **命名并创建**：`python3 scripts/build_prompt.py --new <style-id> --name <中文名> --ref <图片路径>...`，然后按 `_template.md` 填写 `style.md`（含 `avoid` 块、`ip_terms` / `ip_labels`）。
5. **注册**：在 [styles/index.md](styles/index.md) 登记，执行 `--catalog` 更新 README。
6. **迁移性自检**：用两个与参考图类型不同的项目、不同版式各拼装一次；用参考原主体拼装应触发 `WARNING`。
7. 向用户汇报：风格 ID / 名称、设计 DNA 摘要、签名手法、版式列表、参考 IP 排除项、适合的项目类型。

## 工作流 B：生成 App Icon 提示词

### 1. 解析需求

| 字段 | 说明 | 缺失时 |
|---|---|---|
| 项目名称 | 如「FocusCamera」 | 必需，缺失则询问 |
| 项目类型 | 相机 / 效率 / 社交 / 游戏 / 金融… | 从描述推断 |
| 核心功能 | 1–3 个关键能力、目标用户、调性 | 从描述推断 |
| 风格 | `style-id` | 自动匹配（步骤 2） |
| 画布形状 | `square`（全出血，交付 Xcode）/ `squircle`（带圆角，展示用） | 默认取风格的 `default_shape`，未设置则 `square`（`real-morph` 的物体本身即圆角方块，默认 `squircle`） |
| 文字 | 图标上是否出现品牌字样 | 默认**无文字**；仅当用户明确要求且风格允许时使用 `--label`。字母标风格（`lettering: required`）文字即主体，必须用 `--label` 传入；`pop-letter` / `jelly-letter` 为 2–4 个字母，`holo-ribbon` 为单个字母 |

### 2. 选择风格

1. 读取 [styles/index.md](styles/index.md)。
2. 用户指定风格 → 直接使用，**不得混入其他风格的任何特征**。
3. 未指定 → 按 index.md 的「自动匹配规则」选出最佳风格，回复中用一句话说明理由。辅助命令：
   ```bash
   python3 scripts/build_prompt.py --auto "项目名 类型 核心功能"
   ```
4. 读取选中风格的 `styles/<id>/style.md`，重点看「主体转译规则」「版式变体」「参考 IP 排除」。必要时可查看参考图确认**渲染细节**，但不要从中取主体或布局。

### 3. 设计主体

按 [references/subject-design.md](references/subject-design.md) 执行：

1. 从项目名称 / 功能中提取 2–3 个候选隐喻。
2. **去 IP 检查**：候选不得是参考图原主体或同类物（如 `retro-stripe` 不画相机、`real-morph` 不画番茄、`cozy-face` 不画星星），也不得与知名图标 / 角色雷同。
3. 按风格的「主体转译规则」改造候选，并从「版式变体」中选一个 `--layout`（`--layouts <id>` 查看）。
4. 选出**一个**在小尺寸下最易识别的方案，用英文写出主体描述：**物体 + 结构 + 焦点元素形态 + 版式里需要具体化的部件**。只写「画什么」，位置交给版式块，不写「怎么画」。

### 4. 拼装提示词

**必须**使用脚本拼装，保证风格段逐字一致：

```bash
python3 scripts/build_prompt.py --style retro-stripe --layout horizontal-band \
  --subject "the front face of a retro portable radio-recorder: ..." \
  [--shape square|squircle] [--label "REC"] [--with-ref] [--format text|json]
```

- 输出中出现 `# WARNING: 主体描述命中参考图 IP 词` 时，**必须**改写主体后重新拼装，不得直接交付。
- 默认**不输出参考图**；只有用户要求或风格还原明显不足时才加 `--with-ref`，脚本会同时注入「参考图仅作风格参考」约束。

其他命令：`--list` 列出全部风格与版式；`--layouts <id>` 查看版式；`--catalog` 重新生成 README.md；`--new` 新建风格骨架。

### 5. 输出

```markdown
**风格**：<中文名>（`<style-id>`）— <选择理由，一句话>
**版式**：`<layout>` — <为什么选这个版式，一句话>
**主体设计**：<隐喻与造型说明，中文 1–3 句；说明它与参考图主体的区别>

**Prompt**
<脚本输出的 prompt>

**Negative Prompt**
<脚本输出的 negative>

**推荐参数**：1024×1024，1:1，<shape>；参考图：默认不附带（如附带，只作低权重 style reference）
```

### 6. 直接出图（可选）

- 若环境中有图像生成 skill / 工具（如 `image-gen`、`gpt-image-bridge`），把 `prompt` + `negative_prompt`，或不支持负向提示词时把 `prompt_with_negatives` 交给它。
- **默认不附带参考图**：图像模型会连主体、角色、布局一起复制，这是「撞脸」的主要来源。风格一致性由逐字注入的 style 块保证。
- 确需附带时（用户要求，或无参考图时风格明显漂移）：用 `--with-ref` 拼装；工具有 style / content 权重之分时只作 style reference 并调低权重（如 Midjourney 用 `--sref` 而非图片提示，`--sw` 取中低值）。
- 出图后对照风格的「验收清单」与 [references/ios-icon-rules.md](references/ios-icon-rules.md) 检查，并**与参考图并排对比**：主体、轮廓、布局任一项明显雷同即不合格。不合格时调整主体描述、换版式或加强负向约束，**不改 style 块**。

## 稳定性规则（必须遵守）

1. **风格块不可改写**：`style.md` 中的 `style` / `composition` / `negative` 块是唯一来源，只能经脚本原样注入，禁止意译、删减或追加形容词。
2. **只改可变元素**：主体内容、焦点元素、装饰元素的具体形态、版式选择；「可变元素」章节以外的一切视为固定。
3. **参考 IP 不可复用**：参考图的原主体、角色、标志性部件、原布局、字样（见各风格「参考 IP 排除」）不得出现在任何项目中；脚本告警必须处理。
4. **颜色只用风格色板**：主体描述中不得出现色板外的颜色词，需要颜色时引用风格中的色名。例外以风格 `style.md` 的「可变元素」为准（如 `cozy-face` 可换角色主色、`real-morph` 色板由物体固有色决定）。
5. **风格隔离**：一次生成只使用一个风格。
6. **同风格多项目**：不同项目使用同一风格时，使用同一个 `--layout`，主体描述保持相近的复杂度，确保系列感——系列感来自风格 + 版式，而不是参考图。
7. **成组主体**：`subject_layout: paired`（如 `buddy-tiles`）表示固定的一主一辅组合。脚本将两者视为一个视觉组，并移除通用的多主体禁令；角色数量、主次与重叠关系仍由风格块约束。

---
name: appicon-design
description: 从一张或多张 App Icon 案例图中提取设计风格（配色、造型、材质、光影、构图、质感、细节），保存为可命名、可复用的「风格模板」，再根据项目名称、类型与核心功能，按指定风格或自动匹配风格，生成符合 iOS App Icon 规范、可直接用于 GPT-Image / Midjourney / SD 等模型的完整提示词（主体描述 + 风格约束 + 构图要求 + 负面约束）。当用户需要设计 App 图标、iOS/macOS 应用图标、备用图标（Alternate App Icon），或想把案例图片沉淀为新的 App Icon 风格时使用。
---

# appicon-design

把案例 App Icon 的视觉语言固化成**风格模板（Style）**，再按项目特征生成**风格不漂移**的 App Icon 提示词。

核心原则：**设计语言由风格锁死，创意只发生在「主体内容」上。**

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
│       ├── style.md             # 风格规范 + style/composition/negative 提示词块
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
2. **七维提取**：配色、造型、材质、光影、构图、质感、细节；区分「固定特征」与「可变元素」，找出 1–3 个**签名特征**。
3. **命名并创建**：`python3 scripts/build_prompt.py --new <style-id> --name <中文名> --ref <图片路径>...`，然后填写生成的 `style.md`。
4. **注册**：在 [styles/index.md](styles/index.md) 登记，执行 `--catalog` 更新 README。
5. **自检**：用案例图中原本的主体写一次主体描述，确认提示词能「复现」案例图。
6. 向用户汇报：风格 ID / 名称、七维摘要、签名特征、适合的项目类型。

## 工作流 B：生成 App Icon 提示词

### 1. 解析需求

| 字段 | 说明 | 缺失时 |
|---|---|---|
| 项目名称 | 如「FocusCamera」 | 必需，缺失则询问 |
| 项目类型 | 相机 / 效率 / 社交 / 游戏 / 金融… | 从描述推断 |
| 核心功能 | 1–3 个关键能力、目标用户、调性 | 从描述推断 |
| 风格 | `style-id` | 自动匹配（步骤 2） |
| 画布形状 | `square`（全出血，交付 Xcode）/ `squircle`（带圆角，展示用） | 默认取风格的 `default_shape`，未设置则 `square`（`real-morph` 的物体本身即圆角方块，默认 `squircle`） |
| 文字 | 图标上是否出现品牌字样 | 默认**无文字**；仅当用户明确要求且风格允许时使用 `--label`。字母标风格（`lettering: required`，如 `pop-letter`）文字即主体，必须用 `--label` 传入 2–4 个字母 |

### 2. 选择风格

1. 读取 [styles/index.md](styles/index.md)。
2. 用户指定风格 → 直接使用，**不得混入其他风格的任何特征**。
3. 未指定 → 按 index.md 的「自动匹配规则」选出最佳风格，回复中用一句话说明理由。辅助命令：
   ```bash
   python3 scripts/build_prompt.py --auto "项目名 类型 核心功能"
   ```
4. 读取选中风格的 `styles/<id>/style.md`，必要时查看参考图确认细节。

### 3. 设计主体

按 [references/subject-design.md](references/subject-design.md) 执行：

1. 从项目名称 / 功能中提取 2–3 个候选隐喻。
2. 按风格的「主体转译规则」改造候选（例如 `retro-stripe` 要把隐喻转译成 70 年代复古塑料实物的正面视角）。
3. 选出**一个**在小尺寸下最易识别的方案，用英文写出主体描述：**物体 + 结构 + 焦点元素位置 + 风格要求的装饰元素位置**。只写「画什么、放在哪」，不写「怎么画」。

### 4. 拼装提示词

**必须**使用脚本拼装，保证风格段逐字一致：

```bash
python3 scripts/build_prompt.py --style retro-stripe \
  --subject "the front face of a retro cream plastic voice recorder ..." \
  [--shape square|squircle] [--label "REC"] [--format text|json]
```

其他命令：`--list` 列出全部风格；`--catalog` 重新生成 README.md；`--new` 新建风格骨架。

### 5. 输出

```markdown
**风格**：<中文名>（`<style-id>`）— <选择理由，一句话>
**主体设计**：<隐喻与造型说明，中文 1–3 句>

**Prompt**
<脚本输出的 prompt>

**Negative Prompt**
<脚本输出的 negative>

**推荐参数**：1024×1024，1:1，<shape>；参考图：styles/<id>/reference*（作为 style reference 附带）
```

### 6. 直接出图（可选）

- 若环境中有图像生成 skill / 工具（如 `image-gen`、`gpt-image-bridge`），把 `prompt` + `negative_prompt`，或不支持负向提示词时把 `prompt_with_negatives` 交给它。
- 工具支持参考图时**务必附带风格参考图**，这是抑制风格漂移最有效的手段。
- 出图后对照风格的「验收清单」与 [references/ios-icon-rules.md](references/ios-icon-rules.md) 检查；不合格时只调整主体描述或加强负向约束，**不改 style 块**。

## 稳定性规则（必须遵守）

1. **风格块不可改写**：`style.md` 中的 `style` / `composition` / `negative` 块是唯一来源，只能经脚本原样注入，禁止意译、删减或追加形容词。
2. **只改可变元素**：主体内容、焦点元素、装饰元素的具体形态与位置；「可变元素」章节以外的一切视为固定。
3. **颜色只用风格色板**：主体描述中不得出现色板外的颜色词，需要颜色时引用风格中的色名。例外以风格 `style.md` 的「可变元素」为准（如 `cozy-face` 可换角色主色、`real-morph` 色板由物体固有色决定）。
4. **风格隔离**：一次生成只使用一个风格。
5. **同风格多项目**：不同项目使用同一风格时，主体描述保持相近的复杂度与构图骨架（焦点位置、装饰位置一致），确保系列感。

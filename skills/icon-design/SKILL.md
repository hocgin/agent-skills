---
name: icon-design
description: 基于参考图片沉淀的「设计主题」生成风格高度统一的 Icon 图像提示词。每个主题对应一张参考图，固化其配色、材质、光影、构图、造型与细节规范，并区分固定风格、可变元素与负向约束。根据项目名称、类型与功能定位设计 Icon 主体，支持指定主题或自动选择主题，输出可直接用于 GPT-Image / Midjourney / SD 等图像生成的提示词。当用户需要设计 App 图标、项目 Logo 图标、Tab/功能图标、成套 Icon，或想把一张参考图固化为新的 Icon 主题时使用。
---

# icon-design

把参考图片的视觉语言固化成**主题（Theme）**，再按项目特征生成**风格不漂移**的 Icon 提示词。

核心原则：**风格由主题锁死，创意只发生在「主体造型」上。**

## 目录结构

```
icon-design/
├── SKILL.md
├── README.md                 # 主题目录（含参考图预览，脚本自动生成）
├── themes/
│   ├── index.md              # 主题注册表 + 自动选择规则（必读）
│   ├── _template.md          # 新主题模板
│   └── <theme-id>/
│       ├── theme.md          # 风格规范 + style/negative 提示词块
│       └── reference.*       # 参考原图（风格锚点，jpg/png）
├── references/
│   ├── subject-design.md     # 项目 → Icon 主体的设计方法
│   └── add-theme.md          # 新增主题流程（从参考图提取特征）
└── scripts/
    └── build_prompt.py       # 确定性拼装最终提示词
```

## 工作流

### 1. 解析需求

从用户输入中提取：

| 字段 | 说明 | 缺失时 |
|---|---|---|
| 项目名称 | 如「云笺」 | 必需，缺失则询问 |
| 项目类型 | App / Web / 小程序 / 插件 / 游戏 / 开源库 | 从描述推断 |
| 功能定位 | 核心功能、目标用户、调性 | 从描述推断 |
| 主题 | `theme-id` | 自动选择（步骤 2） |
| 用途模式 | `showcase` / `standalone` / `app-icon` | 项目主图标默认 `app-icon`，功能图标默认 `showcase` |
| 数量 | 单个 / 成套 | 默认单个 |

### 2. 选择主题

1. 读取 [themes/index.md](themes/index.md)。
2. 用户指定了主题 → 直接使用，**不得混用其他主题的任何特征**。
3. 未指定 → 按 index.md 的「自动选择规则」打分选出最佳主题，并在回复中用一句话说明理由；也可用脚本辅助：
   ```bash
   python3 scripts/build_prompt.py --auto "项目描述关键词"
   ```
4. 读取选中主题的 `themes/<id>/theme.md`，需要时查看该主题的参考图确认细节。

### 3. 设计 Icon 主体

按 [references/subject-design.md](references/subject-design.md) 执行：

1. 从项目名称 / 功能中提取 2–3 个候选隐喻（具象物体、动作、名称谐音）。
2. 选择**最易识别、最适配主题造型规则**的一个（例如 `doodle-buddy` 需要可拟人化的软造型，`line-dot` 需要可用单线表达的几何物体）。
3. 用英文写出主体描述：**物体 + 结构 + 主题要求的细节元素放在哪里**。只描述「画什么」，不描述「怎么画」——风格由主题的 style 块负责。

### 4. 拼装提示词

**必须**使用脚本拼装，保证固定风格段逐字一致：

```bash
# 单个图标
python3 scripts/build_prompt.py --theme doodle-buddy --mode app-icon \
  --subject "a cloud-shaped notebook character with a folded page corner; violet smile arc in the center"

# 成套图标（同一张图内生成，一致性最高）
python3 scripts/build_prompt.py --theme line-dot --mode showcase \
  --subject "a home ..." --subject "a magnifier ..." --subject "a bell ..." --subject "a user bust ..."

# 输出 JSON（含参考图绝对路径、推荐尺寸，便于直接调用生图接口）
python3 scripts/build_prompt.py --theme pop-offset --subject "..." --format json
```

其他命令：`--list` 列出全部主题；`--catalog` 重新生成根目录 `README.md` 预览目录。

### 5. 输出

按以下格式回复用户：

```markdown
**主题**：<中文名>（`<theme-id>`）— <选择理由，一句话>
**主体设计**：<隐喻与造型说明，中文 1–3 句>

**Prompt**
<脚本输出的 prompt>

**Negative Prompt**
<脚本输出的 negative>

**推荐参数**：1:1，<模式>；参考图：themes/<id>/reference.*（作为 style reference）
```

### 6. 直接生成图像（可选）

用户需要直接出图时：

- 若环境中有图像生成 skill / 工具（如 `image-gen`、`gpt-image-bridge`），把 `prompt_with_negatives`（不支持负向提示词的模型）或 `prompt` + `negative_prompt` 交给它。
- 工具支持参考图时，**务必附带主题的参考图（theme.md 的 `reference` 字段）** 作为风格参考，这是抑制风格漂移最有效的手段。
- 生成后对照主题的「验收清单」检查；不合格时只调整主体描述或加强对应负向约束，**不改 style 块**。

## 稳定性规则（必须遵守）

1. **固定风格不可改写**：theme.md 中 `style` 块是风格的唯一来源，只能通过脚本原样注入，禁止意译、删减或追加形容词。
2. **只改可变元素**：主体造型、细节元素的具体形态与位置、用途模式。主题的「可变元素」章节之外的东西都视为固定。
3. **颜色只用主题色板**：主体描述里不得出现色板外的颜色词；需要颜色时引用主题中的色名。
4. **成套优先同图生成**：多个 Icon 需要统一时，优先一次生成网格图，再裁切；分开生成时固定 seed 并附参考图。
5. **主题隔离**：一次生成只使用一个主题。

## 扩展主题

用户提供新参考图并要求新增主题时，按 [references/add-theme.md](references/add-theme.md) 执行：提取六维特征 → 复制 `themes/_template.md` 填写 → 保存参考图 → 在 `themes/index.md` 注册 → 用脚本试生成并自检。

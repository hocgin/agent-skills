# Icon 主体设计方法

目标：用**一个**最易识别的隐喻表达项目，并让它天然适配所选主题的造型规则。

## 1. 提取隐喻

从以下来源各想一个候选，共 2–3 个：

| 来源 | 示例 |
|---|---|
| 核心功能的具象物体 | 记账 → 钱包 / 账本；云盘 → 云朵 / 文件夹 |
| 核心动作 | 翻译 → 对话气泡互换；同步 → 循环箭头 |
| 项目名称字面 / 谐音 | 「番茄钟」→ 番茄；「小鹿笔记」→ 鹿角 + 笔记本 |
| 目标用户 / 场景 | 宠物社区 → 爪印；夜读 → 月亮 + 书 |

可以**组合**两个元素，但必须一主一辅：主元素决定轮廓，辅元素作为内部细节或小附件。

## 2. 筛选

按顺序淘汰：

1. 缩小到 48px 仍能认出吗？不能 → 淘汰。
2. 是否需要文字/字母才能理解？是 → 淘汰（禁止在图标中出现文字）。
3. 是否符合主题的「主体适配要求」（见 `themes/index.md`）？
   - `doodle-buddy`：轮廓能软化成胖乎乎的有机形，并有空间放紫色五官。
   - `pop-offset`：能概括成圆角矩形 / 三角 / 圆等几何骨架，内部能放炭黑粗符号。
   - `line-dot`：能用单线几何结构画出，并能自然找到**一个**放黄色点缀的位置。
   - `solid-knockout`：能做成饱满的实心底板，符号能以白色负形镂空表达。
   - `pastel-layer`：能拆成「主层 + 辅层」两块重叠的圆胖形状。
   - `flat-object`：是有明确固有色的实物，正视剪影即可辨认。
4. 与同类知名产品图标是否撞车？过于雷同 → 换辅元素或换角度。

## 3. 撰写主体描述（英文）

公式：

```
<主体物体> + <结构/轮廓要点> + <主题细节元素的位置与形态> [+ <辅元素>]
```

规则：

- 只写「画什么、放在哪」，**不写**线条粗细、颜色质感、光影等风格词——这些由主题 style 块负责。
- 需要指定颜色时只能引用主题色板中的色名（如 `violet`、`lime-green band`、`yellow dot`）。
- 多色板主题（`solid-knockout`、`pastel-layer`）每个图标只用一种颜色/色相，需在描述中写明，如 `in cobalt blue`、`in the lilac hue family`；成套时各图标轮换不同颜色。
- 控制在 1–2 句、40 词以内，避免细节过多导致风格被稀释。

### 示例

| 项目 | 主题 | 主体描述 |
|---|---|---|
| 「番茄钟」专注计时 App | `doodle-buddy` | a plump tomato character with a small leaf sprout on top; two vertical rectangle eyes and a small smile arc in the center |
| 「派对狼人杀」桌游 App | `pop-offset` | a tilted wolf-head mask shape built from a rounded triangle with two pointed ears; two charcoal dot eyes and a small zigzag mouth, two sparkle stars at the upper right |
| 「轻记账」记账工具 | `line-dot` | an upright rounded-rectangle wallet with a flap line across the top third and a small clasp ring on the right; the clasp center is the yellow dot |
| 「安心备份」云备份工具 | `solid-knockout` | a solid cloud silhouette in periwinkle blue with a white knockout checkmark in the center |
| 「宝宝喂养记」母婴记录 | `pastel-layer` | a baby bottle in the apricot orange hue family: rounded nipple cap as the front layer, lighter bottle body behind, three tiny capsule measurement bars |
| 「零钱包」个人记账 | `flat-object` | a brown leather wallet seen from the front with a darker brown flap on top, green banknotes peeking out of the top edge, and a small dark clasp dot on the right |
| 「云笺」云笔记 | `line-dot` | a rounded cloud outline with a folded page corner on the upper right and two short horizontal text lines inside; the yellow dot sits at the end of the lower line |

## 4. 成套图标

- 同一套图标共享**主体尺寸、视觉重心、细节密度**；在描述里保持相近的结构复杂度。
- 主题若有签名特征（如 `doodle-buddy` 的缺口、`line-dot` 的唯一黄点），每个图标都必须体现。
- 建议每套 4 个，用 2×2 网格一次生成；超过 6 个分批，每批附上参考图与上一批结果。

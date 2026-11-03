# App Icon 主体设计方法

目标：用**一个**最易识别、且**属于这个项目自己**的隐喻表达项目，再按所选风格的「主体转译规则」和「版式变体」改造成该风格下自然的样子。

> 核心区分：风格模板只提供「怎么画」（设计 DNA）；「画什么、放在哪」必须为每个项目重新设计。参考图的主体、角色、轮廓、布局属于参考 IP，一律不复用。

## 1. 提取隐喻

从以下来源各想一个候选，共 2–3 个：

| 来源 | 示例 |
|---|---|
| 核心功能的具象物体 | 记账 → 钱包 / 收银机；笔记 → 笔记本；天气 → 风向标 |
| 核心动作 | 翻译 → 对话气泡；同步 → 循环箭头；专注 → 沙漏 |
| 项目名称字面 / 谐音 | 「晨咖」→ 咖啡豆；「声境」→ 声波 |
| 目标用户 / 场景 | 宠物 → 骨头 / 爪印；夜读 → 月亮 + 书 |

可以组合两个元素，但必须**一主一辅**：主元素决定轮廓与焦点，辅元素作为附件或装饰。

## 2. 去 IP 检查（必做）

对每个候选回答：

1. 是否就是参考图的原主体或同类物（见风格的「参考 IP 排除」）？是 → 换物件，或至少换「物件 + 版式 + 主色」中的两项。
2. 是否与知名产品图标 / 知名角色 / 知名 Logo 雷同（含 Apple 系统图标、SF Symbols 原样）？是 → 换辅元素或换角度。
3. 是否只是「把参考主体换个颜色」？是 → 淘汰。

脚本会根据风格的 `ip_terms` / `ip_labels` 自动检查，命中时打印 `WARNING`，必须改写主体后重新拼装。

## 3. 风格转译 + 选版式

读取风格 `style.md` 的「主体转译规则」与「版式变体」（或 `build_prompt.py --layouts <id>`），把候选隐喻改写为该风格下的形态，并选择一个版式：

| 风格 | 转译方式 | 优先版式 |
|---|---|---|
| `retro-stripe` | 变成 70–80 年代米白塑料器物（**不是相机**）的正面，焦点是喇叭网 / 表盘 / 屏面等凹陷近黑部件 | `diagonal-band` / `horizontal-band` |
| `luxe-skeuo` | 变成高端精密器物（**不是唱机**）的顶面俯视，光泽黑主元素里嵌流体渐变焦点 | `centered-dial` / `split-panel` |
| `cozy-face` | 单色萌脸铺满画布（主色按项目选），奶白圆胖物件（**不是星星**）作为焦点 | `peek` / `side-hold` |
| `real-morph` | 有鲜明固有色的实物（**不是番茄**）塑形为圆角方块，只保留一个特征 | 按特征位置选 |
| `pop-letter` / `jelly-letter` | 项目名缩写 2–4 字母（`--label`），只写位置与颜色分配，避开 DDUP 与绿蓝粉黄顺序 | `bounce` / `stair` |
| `buddy-tiles` | 一对由业务决定形状的拟人贴片（**不是卡片 / 屏幕**） | `side-by-side` / `piggyback` |
| `bold-mascot` | 一个能加五官的业务剪影（**不是拼图**） | 任意 |
| `pastel-spirit` | 由业务决定轮廓的半透明小灵物（**不是幽灵 / 小鸟**） | 任意 |
| `holo-ribbon` | 单个品牌字母的连续宽带字标（避免小写 e） | 任意 |

**同风格多项目**：系列内保持同一版式与相近复杂度，系列感来自风格 + 版式，而不是来自参考图。

## 4. 筛选

按顺序淘汰：

1. 缩小到 60px 仍能认出吗？不能 → 淘汰。
2. 是否必须依赖文字才能理解？是 → 淘汰（字母标风格跳过，改为：缩写能否让用户联想到项目名）。
3. 是否满足风格的「主体适配要求」（见 `styles/index.md`）？
4. 是否通过第 2 步的去 IP 检查？

## 5. 撰写主体描述（英文）

公式：

```
<主体物体（风格转译后）> + <结构/轮廓要点> + <焦点元素：形态> + <版式中需要具体化的部件> [+ <辅元素>]
```

规则：

- 只写「画什么」；**位置交给 `--layout` 的版式块**，主体描述不要再写与版式冲突的方位。
- **不写**材质、光影、质感等风格词——由 style 块负责。
- 颜色只能引用风格色板中的色名（例外以风格「可变元素」为准，如 `cozy-face` 主色、`real-morph` 固有色）。
- 控制在 2–3 句、60 词以内。

### 示例（`retro-stripe`）

| 项目 | `--layout` | 主体描述 |
|---|---|---|
| 「声记」录音 App | `horizontal-band` | the front face of a retro portable radio-recorder: the focal part is a round perforated near-black speaker grille, with a small red record key and a tiny level-meter window on the cream area |
| 「番茄钟」专注计时 | `diagonal-band` | the front face of a retro kitchen timer: the focal part is a near-black dial with bold cream tick marks and one red pointer, with a small chunky start key along the top |
| 「轻记账」记账工具 | `vertical-band` | the front face of a retro desk calculator: the focal part is a near-black rounded-rectangle display showing a simple embossed coin symbol, with a small red total key above it |
| 「复古相册」照片 App | `arc-band` | the front face of a retro slide viewer: the focal part is a near-black rounded-square viewing window with a faint embossed mountain-and-sun symbol, with a small red advance lever |

### 示例（`luxe-skeuo`）

| 项目 | `--layout` | 主体描述 |
|---|---|---|
| DxMusic 音乐播放器 | `split-panel` | the top of a premium mixing console: a glossy black panel with fine perforations holding the gradient element shaped as a rounded square with an embossed note, and a gold fader on the left rail |
| 「声境」播客 App | `centered-dial` | the top of a premium speaker: a glossy black perforated speaker cone with the gradient disc as its center cap bearing an embossed sound-wave mark |
| 「专注时刻」计时 App | `stacked-controls` | the top of a luxury timer: a glossy black dial with fine tick grooves and the gradient disc at its center, three gold controls below |

### 示例（`cozy-face`）

| 项目 | 主色 | `--layout` | 主体描述 |
|---|---|---|---|
| 「稍后读」收藏 App | 樱花粉 | `peek` | a cherry-blossom pink face (#FF9EB5, shadows #E8738F) peeking over a plump creamy bookmark ribbon with a rounded notch |
| 「小猪存钱」储蓄 App | 蜜桃橙 | `side-hold` | a peach orange face (#FFB37A, shadows #F08A4B) holding a plump creamy round coin with one small embossed heart |
| 「早睡」睡眠 App | 香芋紫 | `peek` | a taro purple face (#C3A8FF, shadows #9C7FE6) peeking over a plump creamy crescent moon |
| 「喝水打卡」习惯 App | 天空蓝 | `hug` | a sky blue face (#8CCBFF, shadows #5BA6E8) hugging a plump creamy water drop |

### 示例（`real-morph`）

| 项目 | `--layout` | 主体描述 |
|---|---|---|
| 「专注沙漏」番茄钟 | `corner-feature` | a bright lemon-yellow lemon sculpted into the squircle shape, with its small nub and one glossy green leaf on the upper-right shoulder |
| 「轻食记」饮食 App | `top-feature` | a glossy apple-green apple sculpted into the squircle shape, with a short brown stem and one green leaf at the top |
| 「晨咖」咖啡 App | `inset-feature` | a roasted brown coffee bean sculpted into the squircle shape, with its curved S-shaped groove running through the center |
| 「早安蛋」早餐 App | `inset-feature` | a smooth white eggshell sculpted into the squircle shape, with a small zigzag crack at the center revealing glossy golden yolk |

### 示例（`pop-letter` / `jelly-letter`，两者主体描述通用）

| 项目 | `--label` | `--layout` | 主体描述 |
|---|---|---|---|
| Kiko 键盘 | `KIKO` | `bounce` | letters "K" "I" "K" "O" in one bouncing row; yellow K, pink I, blue K, green O |
| 「Hi 聊」社交 App | `HI` | `stair` | letter "H" at the upper left and "I" stepping down to the lower right; pink H, blue I |
| WordBox 背单词 | `WB` | `hero-letter` | a large "W" on the left with a smaller "B" tucked against its right side; yellow W, green B |
| Fun Kids 儿童学堂 | `FUN` | `grid` | letter "F" on top, "U" and "N" side by side below; blue F, yellow U, pink N |

# App Icon 主体设计方法

目标：用**一个**最易识别的隐喻表达项目，并按所选风格的「主体转译规则」改造成该风格下自然的样子。

## 1. 提取隐喻

从以下来源各想一个候选，共 2–3 个：

| 来源 | 示例 |
|---|---|
| 核心功能的具象物体 | 相机 → 镜头；记账 → 钱包 / 收银机；笔记 → 笔记本 |
| 核心动作 | 翻译 → 对话气泡；同步 → 循环箭头；专注 → 计时器 |
| 项目名称字面 / 谐音 | 「番茄钟」→ 番茄；「FocusCamera」→ 对焦环 + 镜头 |
| 目标用户 / 场景 | 宠物 → 爪印；夜读 → 月亮 + 书 |

可以组合两个元素，但必须**一主一辅**：主元素决定轮廓与焦点，辅元素作为附件或装饰。

## 2. 风格转译

读取风格 `style.md` 中的「主体转译规则」，把候选隐喻改写为该风格下的形态。例如：

| 风格 | 转译方式 |
|---|---|
| `retro-stripe` | 变成 70–80 年代米白塑料消费电子 / 日用品的**正面**，物体正面铺满整个画布；焦点做成大号圆形部件（镜头、表盘、旋钮、喇叭） |
| `luxe-skeuo` | 变成高端精密器物的**顶面俯视图**，机身铺满画布；核心隐喻落在偏左下的大号黑色圆形主体及其中心的流体渐变焦点上，右上伸入金属臂 / 指针 |
| `cozy-face` | 隐喻变成一个奶白色、圆胖、可被「抱住」的简单物件，由铺满画布的单色萌脸用两只小爪抱在下方；可选指定角色主色 |
| `real-morph` | 选有鲜明固有色的实物，主体塑形为铺满画布的圆角方块，只在上部中央保留一个特征部件；主体描述可直接写物体固有色 |
| `pop-letter` / `jelly-letter` | 不用图形隐喻，把项目名缩写成 2–4 个字母（`--label`），主体描述只写排布与颜色分配 |

## 3. 筛选

按顺序淘汰：

1. 缩小到 60px 仍能认出吗？不能 → 淘汰。
2. 是否必须依赖文字才能理解？是 → 淘汰。
3. 是否满足风格的「主体适配要求」（见 `styles/index.md`）？
4. 是否与知名产品图标雷同？是 → 换辅元素或换角度。

字母标风格（`lettering: required`）跳过第 2 条，改为：缩写后的 2–4 个字母能否让用户联想到项目名？

## 4. 撰写主体描述（英文）

公式：

```
<主体物体（风格转译后）> + <结构/轮廓要点> + <焦点元素：形态与位置> + <风格装饰元素：位置> [+ <辅元素>]
```

规则：

- 只写「画什么、放在哪」，**不写**材质、光影、质感等风格词——由风格的 style 块负责。
- 颜色只能引用风格色板中的色名（如 `cream`、`cobalt blue stripe`）。
- 焦点与装饰元素的**位置骨架尽量沿用参考图**（例如 `retro-stripe` 的焦点在中下、彩条从左下扫向右下），这是同风格多项目保持一致的关键。
- 控制在 2–3 句、60 词以内。

### 示例（`retro-stripe`）

| 项目 | 主体描述 |
|---|---|
| FocusCamera 复古相机 | the front face of a retro instant camera: a large black lens with a thick cream bezel at lower center, a square viewfinder and a ribbed flash window along the top, a round red shutter button at the top left, a small round frame counter at the right; rainbow stripes sweep from the left edge across the bottom |
| 「声记」录音 App | the front face of a retro portable cassette voice recorder: a large round perforated speaker grille at lower center, a small cassette window and a row of chunky piano-key buttons along the top, a round red record button at the top left, a small round level meter at the right; rainbow stripes sweep from the left edge across the bottom |
| 「番茄钟」专注计时 | the front face of a retro kitchen timer device: a large round dial with a black face and bold tick marks at lower center, a small rectangular display window along the top, a round red start button at the top left, a small round knob at the right; rainbow stripes sweep from the left edge across the bottom |
| 「轻记账」记账工具 | the front face of a retro desk calculator: a large round black display lens-like dial at lower center showing a coin symbol, a row of chunky square keys along the top, a round red total button at the top left, a small round paper-roll counter at the right; rainbow stripes sweep from the left edge across the bottom |

### 示例（`luxe-skeuo`）

| 项目 | 主体描述 |
|---|---|
| DxMusic 音乐播放器 | the top of a turntable: a large black vinyl record at lower left with the gradient label at its center, a gold tonearm pivot at upper right with a curved arm resting on the record, a small orange-ring knob at upper left, one large and one small gold knob at lower right |
| 「声境」播客 App | the top of a premium speaker: a large black woofer cone at lower left with the gradient disc as its dust cap, a gold pivot at upper right with a slim curved gold microphone boom reaching toward the cone, a small orange-ring knob at upper left, one large and one small gold knob at lower right |
| 「专注时刻」计时 App | the top of a luxury timer: a large glossy black dial at lower left with fine tick grooves and the gradient disc at its center, a gold pivot at upper right with a long curved gold pointer reaching to the dial, a small orange-ring knob at upper left, one large and one small gold knob at lower right |

### 示例（`cozy-face`）

| 项目 | 主体描述 |
|---|---|
| Pocket 收藏 App | a buttery yellow face hugging a plump creamy five-point star with rounded tips |
| 「小猪存钱」储蓄 App | a peach orange face hugging a plump creamy round coin with one small embossed heart in the middle; shadows in deeper coral |
| 「早睡」睡眠 App | a lavender purple face hugging a plump creamy crescent moon; shadows in deeper violet |
| 「喝水打卡」习惯 App | a sky blue face hugging a plump creamy water drop; shadows in deeper blue |

### 示例（`real-morph`）

| 项目 | 主体描述 |
|---|---|
| RemindersPlus 番茄提醒 | a bright red ripe tomato sculpted into the squircle shape, with a green star-shaped calyx of six slender sepals and a short green stem at the top center |
| 「轻食记」饮食 App | a glossy apple-green apple sculpted into the squircle shape, with a short brown stem and one green leaf at the top center |
| 「晨咖」咖啡 App | a roasted brown coffee bean sculpted into the squircle shape, with its curved S-shaped center groove running down from the top center |
| 「早安蛋」早餐 App | a smooth white eggshell sculpted into the squircle shape, with a small zigzag crack at the top center revealing glossy golden yolk |

### 示例（`pop-letter` / `jelly-letter`，两者主体描述通用）

| 项目 | `--label` | 主体描述 |
|---|---|---|
| DD UP 键盘 | `DDUP` | letters "D" "D" on the top row and "U" "P" on the bottom row; green D, blue D, pink U, yellow P |
| 「Hi 聊」社交 App | `HI` | letters "H" and "I" side by side, the I slightly lower; pink H, blue I |
| WordBox 背单词 | `WB` | letters "W" and "B" side by side, the B slightly higher; yellow W, green B |
| Fun Kids 儿童学堂 | `FUN` | letter "F" and "U" on the top row and "N" centered below; blue F, yellow U, pink N |

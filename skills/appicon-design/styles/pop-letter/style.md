---
id: pop-letter
name: 彩泡字块
references: reference.png
keywords: keyboard, input, typing, font, text, chat, message, social, community, kids, education, learning, language, word, game, party, music, sticker, emoji, fun, 键盘, 输入法, 打字, 字体, 文字, 聊天, 消息, 社交, 社区, 儿童, 教育, 学习, 语言, 单词, 游戏, 派对, 贴纸, 表情, 趣味, 潮流
lettering: required
label_style: chunky rounded bubble letters, each letter a different flat color from the palette, with dark letter counters
summary: 纯黑底上 2–4 个圆胖泡泡字母紧密拼成方块，每个字母一种高饱和糖果色，黑色细缝分隔，两侧白色短促动感线。
---

# 彩泡字块 `pop-letter`

> 参考：`reference.png`（键盘 App「DD UP」：四个字母 2×2 拼块）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 背景纯黑 `#000000`；字母为高饱和糖果色，**每个字母一种、互不重复**：薄荷绿 `#33F97E`、亮蓝 `#228EFC`、西瓜粉 `#FD6682`、柠檬黄 `#FFD236`；字母内部负形（字怀）透出黑底；装饰线纯白 `#FFFFFF` |
| 造型 | 极粗、圆胖的泡泡字（bubble letter），笔画几乎填满字身，字怀很小；轮廓略带手绘的不规则感，圆角饱满；每个字母略微旋转（±5–10°），像贴纸 |
| 材质 | 完全扁平的实色填充，无渐变、无高光、无纹理 |
| 光影 | 无光照、无阴影；字母之间仅靠黑色细缝（约画布 1.5%）分隔，形成「描边」错觉 |
| 构图 | 字母组合为紧密的方块（2 字母：左右或上下；3 字母：品字形；4 字母：2×2），整体占画布约 85%，居中；字母彼此几乎相触、轻微咬合 |
| 质感 | 干净矢量，边缘利落 |
| 细节 | 唯一装饰是 2 组白色圆头短线（每组 2 条），位于左侧中上与右侧中下的外沿，像「闪动」符号；不加其他图形 |
| 情绪 | 活泼、潮流、玩趣、年轻 |

**签名特征**：① 纯黑底 + 圆胖泡泡字母铺满成块；② 每个字母一种不同的糖果色；③ 对角两侧的白色动感短线。

## 主体转译规则

主体**就是文字**：取项目名称的首字母 / 缩写 / 短词，共 **2–4 个字母**（超过 4 个字母识别度骤降，需缩写），通过 `--label` 传入。

- 2 个字母：左右并排，略错位；
- 3 个字母：上 2 下 1 或上 1 下 2 的品字形；
- 4 个字母：2×2 网格（如 `DDUP`）。

主体描述只写字母排布与颜色分配（例如 `letters "D" "D" on the top row and "U" "P" on the bottom row; green D, blue D, pink U, yellow P`），不写字体风格。中文项目使用拼音或英文名缩写。

## 可变元素

- 字母内容与数量（2–4）
- 字母排布方式与各自旋转角度
- 色板内的颜色分配（不重复）
- 白色动感线的具体角度（位置固定在对角两侧）

## 风格约束（style）

```style
Bold playful lettermark rendered as flat 2D vector art. Extremely chunky, rounded bubble letters with very thick strokes, tiny counters and soft irregular hand-drawn outlines, each letter slightly rotated like a sticker. Every letter is filled with one solid saturated candy color from this palette only, and no two letters share a color: mint green (#33F97E), bright blue (#228EFC), watermelon pink (#FD6682), lemon yellow (#FFD236). The letter counters show the pure black (#000000) background. Letters are packed tightly into one compact block, nearly touching and slightly overlapping, separated only by thin black gaps that read as an outline. The only decoration is two pairs of short white (#FFFFFF) round-capped motion dashes. Completely flat solid fills, no gradients, no highlights, no shadows, no texture, no 3D. Crisp clean vector edges. Energetic, trendy, fun mood.
```

## 构图要求（composition）

```composition
Pure black background filling the whole canvas. The letter block is centered and fills about 85% of the canvas. Two letters sit side by side, three letters form a pyramid, four letters form a two-by-two grid. One pair of white motion dashes sits just outside the block on the left side slightly above center, and the other pair sits outside the block on the lower right, pointing outward diagonally.
```

## 负面约束（negative）

```negative
3D letters, extruded text, bevel, emboss, glossy highlights, gradient, drop shadow, glow, neon glow, outline stroke in color, thin font, serif font, script font, handwritten cursive, letters of the same color, more than four letters, white background, colored background, pastel colors, dark muted colors, texture, grain, extra icons, stars, hearts, sparkles, illustrations, mascots, misspelled letters, extra letters
```

## 验收清单

- [ ] 纯黑底铺满，字母块居中约占 85%
- [ ] 字母圆胖粗壮、字怀小，内容与 `--label` 完全一致
- [ ] 每个字母一种不同的糖果色，均来自色板
- [ ] 左上、右下各一组白色短线，无其他装饰
- [ ] 完全扁平，无渐变 / 阴影 / 高光

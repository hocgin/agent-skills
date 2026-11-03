---
id: pop-letter
name: 彩泡字块
references: reference.png
keywords: keyboard, input, typing, font, text, chat, message, social, community, kids, education, learning, language, word, game, party, music, sticker, emoji, fun, 键盘, 输入法, 打字, 字体, 文字, 聊天, 消息, 社交, 社区, 儿童, 教育, 学习, 语言, 单词, 游戏, 派对, 贴纸, 表情, 趣味, 潮流
ip_terms: ddup, dd up
ip_labels: DDUP, DD UP
lettering: required
label_style: chunky rounded bubble letters, each letter a different flat color from the palette, with dark letter counters
summary: 纯黑底上 2–4 个圆胖泡泡字母紧密成组，每个字母一种高饱和糖果色、完全扁平，黑色细缝分隔，外沿两组白色动感短线。
---

# 彩泡字块 `pop-letter`

> 参考：`reference.png`。参考图只用于提炼设计语言，它的字样「DDUP」及其配色分配属于参考 IP，见「参考 IP 排除」。

## 设计 DNA（可复用）

| 维度 | 规范 |
|---|---|
| 配色 | 背景纯黑 `#000000`；字母糖果色，每个字母一种、互不重复：薄荷绿 `#33F97E`、亮蓝 `#228EFC`、西瓜粉 `#FD6682`、柠檬黄 `#FFD236`；字怀透出黑底；装饰纯白 `#FFFFFF` |
| 造型语言 | 极粗、圆胖的泡泡字，字怀很小，轮廓略带手绘不规则感；每个字母轻微旋转（±5–10°）像贴纸 |
| 材质 | 完全扁平实色，无渐变、无高光、无纹理 |
| 光影 | 无光照、无阴影；字母之间仅靠黑色细缝（约画布 1.5%）分隔 |
| 构图原则 | 字母紧密成一个视觉组，约占画布 75–85%，居中；具体排布见「版式变体」 |
| 质感 | 干净矢量，边缘利落 |
| 细节密度 | 唯一装饰是 2 组白色圆头短线（每组 2 条），位于字母组外沿的两处相对位置 |
| 情绪 | 活泼、潮流、玩趣、年轻 |

**签名手法**：① 纯黑底 + 圆胖泡泡字母紧密成组；② 每个字母一种不同的扁平糖果色；③ 外沿两组白色动感短线。

## 参考 IP 排除

- 原字样：「DDUP / DD UP」。
- 原配色分配：绿 D、蓝 D、粉 U、黄 P 的 2×2 排布。
- 原布局：严格 2×2 网格 + 左侧中上、右侧中下各一组短线。

## 主体转译规则

主体**就是文字**：取项目名称的首字母 / 缩写 / 短词，共 **2–4 个字母**，通过 `--label` 传入；中文项目用拼音或英文名缩写。

- 主体描述只写版式中每个字母的位置与颜色分配，不写字体风格。
- 颜色分配要避开参考的「绿-蓝-粉-黄」顺序；4 个字母时优先选 `stair` 或 `bounce` 版式，而不是 `grid`。

## 版式变体

```composition:bounce
Pure black background filling the whole canvas. The letters sit in a single row centered horizontally, filling about 85% of the canvas width, alternately bouncing slightly up and down so they interlock like a wave. One pair of white motion dashes sits above the first letter pointing up-left, and the other pair sits below the last letter pointing down-right.
```

```composition:stair
Pure black background filling the whole canvas. The letters step diagonally from the upper left to the lower right like a staircase, each overlapping the previous one slightly, the whole group filling about 80% of the canvas. One pair of white motion dashes sits at the upper right of the group and the other at the lower left, pointing outward.
```

```composition:hero-letter
Pure black background filling the whole canvas. The first letter is large, about 60% of the canvas height, on the left; the remaining letters are smaller and stacked tightly against its right side, the whole group centered and filling about 80% of the canvas. One pair of white motion dashes sits at the top right and the other at the bottom left, pointing outward.
```

```composition:grid
Pure black background filling the whole canvas. The letter block is centered and fills about 80% of the canvas. Two letters sit one above the other with a slight offset, three letters form a pyramid with one letter on top and two below, four letters form a two-by-two grid. One pair of white motion dashes sits outside the block at the top right and the other at the bottom left, pointing outward diagonally.
```

## 可变元素

- 字母内容与数量（2–4）、版式与旋转角度
- 色板内的颜色分配（不重复）
- 白色动感线的具体角度（随版式位置）

## 风格约束（style）

```style
Bold playful lettermark rendered as flat 2D vector art. Extremely chunky, rounded bubble letters with very thick strokes, tiny counters and soft irregular hand-drawn outlines, each letter slightly rotated like a sticker. Every letter is filled with one solid saturated candy color from this palette only, and no two letters share a color: mint green (#33F97E), bright blue (#228EFC), watermelon pink (#FD6682), lemon yellow (#FFD236). The letter counters show the pure black (#000000) background. Letters are packed tightly into one compact group, nearly touching and slightly overlapping, separated only by thin black gaps that read as an outline. The only decoration is two pairs of short white (#FFFFFF) round-capped motion dashes. Completely flat solid fills, no gradients, no highlights, no shadows, no texture, no 3D. Crisp clean vector edges. Energetic, trendy, fun mood.
```

## 负面约束（negative）

```negative
3D letters, extruded text, bevel, emboss, glossy highlights, gradient, drop shadow, glow, neon glow, outline stroke in color, thin font, serif font, script font, handwritten cursive, letters of the same color, more than four letters, white background, colored background, pastel colors, dark muted colors, texture, grain, extra icons, stars, hearts, sparkles, illustrations, mascots, misspelled letters, extra letters
```

## 参考 IP 排除（avoid）

```avoid
letters DDUP, DD UP keyboard icon, green D blue D pink U yellow P arrangement
```

## 验收清单

- [ ] 纯黑底铺满，字母组居中，排布符合所选版式
- [ ] 字母圆胖粗壮、字怀小，内容与 `--label` 完全一致
- [ ] 每个字母一种不同的糖果色，均来自色板
- [ ] 两组白色短线位于外沿相对位置，无其他装饰；完全扁平
- [ ] 与参考图并排对比：字样与配色分配不同，不是 DDUP 的 2×2 翻版

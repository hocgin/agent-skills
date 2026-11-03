---
id: jelly-letter
name: 果冻字块
references: reference.png
keywords: keyboard, input, typing, font, text, chat, message, social, kids, education, learning, language, word, game, puzzle, casual, sticker, emoji, candy, cute, beauty, 键盘, 输入法, 打字, 字体, 文字, 聊天, 消息, 社交, 儿童, 教育, 学习, 语言, 单词, 游戏, 益智, 休闲, 贴纸, 表情, 糖果, 可爱, 美妆
ip_terms: ddup, dd up
ip_labels: DDUP, DD UP
lettering: required
label_style: plump glossy 3D jelly-candy letters, each letter a different candy color from the palette, with deep translucent tinted counters
summary: 近白柔光底上 2–4 个圆胖半透明 3D 果冻字母成组，每个字母一种糖果色、左上弧形高光，向底色晕出同色柔光，外沿两组白色胶囊短线。
---

# 果冻字块 `jelly-letter`

> 参考：`reference.png`。参考图只用于提炼设计语言，它的字样「DDUP」及其配色分配属于参考 IP，见「参考 IP 排除」。与 `pop-letter` 共用版式体系，区别在 3D 果冻材质与浅色底。

## 设计 DNA（可复用）

| 维度 | 规范 |
|---|---|
| 配色 | 背景近白 `#F7FBFE`，字母附近带同色淡晕（如粉紫 `#F5E4F6`、杏黄 `#FAEBD6`）；字母每个一种、互不重复：薄荷绿 `#89FA9A`（暗部 `#69E184`）、天蓝 `#5AA6F6`、草莓粉 `#EC799B`（暗部 `#E84579`）、柠檬黄 `#FAE352`（边缘 `#F4B840`）；字怀为同色深色透光（如深绿 `#357A5D`）；装饰白 `#FAFCFC` |
| 造型语言 | 圆胖泡泡字，笔画极粗、字怀小，像充气软糖般鼓起；每个字母轻微旋转 |
| 材质 | 半透明果冻 / 软糖 / 光泽塑料，内部微透光，颜色由上至下略变深 |
| 光影 | 顶部柔光；每个字母左上一条长弧形镜面高光 + 小点高光；边缘轻微次表面透光；底部同色柔和彩色投影 / 光晕 |
| 构图原则 | 字母紧贴略挤压成一个视觉组，约占画布 75–80%，居中；排布见「版式变体」 |
| 质感 | 干净顺滑的 3D 渲染，无颗粒 |
| 细节密度 | 唯一装饰是 2 组白色立体胶囊短线（每组 2 条），位于字母组外沿的两处相对位置 |
| 情绪 | 甜美、可爱、轻盈、治愈 |

**签名手法**：① 光泽半透明的 3D 果冻字母；② 每个字母一种糖果色，并在白底上晕出同色柔光；③ 外沿两组白色胶囊短线。

## 参考 IP 排除

- 原字样：「DDUP / DD UP」。
- 原配色分配：绿 D、蓝 D、粉 U、黄 P 的 2×2 排布。
- 原布局：严格 2×2 网格 + 左侧中上、右侧中下各一组短线。

## 主体转译规则

同 `pop-letter`：主体**就是文字**，取项目名称的首字母 / 缩写，共 **2–4 个字母**，通过 `--label` 传入。主体描述只写字母位置与颜色分配，不写材质光影；颜色分配避开参考的「绿-蓝-粉-黄」顺序，4 个字母时优先 `stair` 或 `bounce`。

## 版式变体

```composition:bounce
Near-white background filling the whole canvas. The letters sit in a single row centered horizontally, filling about 80% of the canvas width, alternately bouncing slightly up and down and squeezed against each other. One pair of white capsule dashes sits above the first letter pointing up-left, and the other pair sits below the last letter pointing down-right. Straight-on front view with only a hint of depth.
```

```composition:stair
Near-white background filling the whole canvas. The letters step diagonally from the upper left to the lower right like a staircase, each one softly overlapping the previous, the whole group filling about 78% of the canvas. One pair of white capsule dashes sits at the upper right of the group and the other at the lower left, pointing outward. Straight-on front view with only a hint of depth.
```

```composition:hero-letter
Near-white background filling the whole canvas. The first letter is large, about 60% of the canvas height, on the left; the remaining letters are smaller and nestled against its right side, the whole group centered and filling about 78% of the canvas. One pair of white capsule dashes sits at the top right and the other at the bottom left. Straight-on front view with only a hint of depth.
```

```composition:grid
Near-white background filling the whole canvas. The letter block is centered and fills about 78% of the canvas. Two letters sit one above the other with a slight offset, three letters form a pyramid with one letter on top and two below, four letters form a two-by-two grid. One pair of white capsule dashes sits outside the block at the top right and the other at the bottom left, pointing outward diagonally. Straight-on front view with only a hint of depth.
```

## 可变元素

- 字母内容与数量（2–4）、版式与旋转角度
- 色板内的颜色分配（不重复），背景淡晕随字母颜色变化
- 白色胶囊短线的具体角度（随版式位置）

## 风格约束（style）

```style
Cute glossy 3D lettermark render, like soft jelly candy or inflated glossy plastic. Extremely chunky, rounded, puffy bubble letters with very thick strokes and small counters, each letter slightly rotated like scattered candies, softly squeezed against each other. Every letter is one candy color from this palette only, and no two letters share a color: mint green (#89FA9A), sky blue (#5AA6F6), strawberry pink (#EC799B), lemon yellow (#FAE352). Each letter is semi-translucent and smooth, its color deepening slightly toward the bottom, with deep translucent tinted counters. Soft light from above: a long curved specular highlight along the upper-left edge of every letter plus a small dot highlight, subtle subsurface glow at the rims. Each letter casts a soft colored shadow and glow of its own hue that diffuses into the background. The background is an airy near-white (#F7FBFE) with faint pastel color haze near the letters. The only decoration is two pairs of short white glossy 3D capsule dashes. Clean smooth render, no grain, no texture. Sweet, cute, light, cheerful mood.
```

## 负面约束（negative）

```negative
flat 2D vector, black background, dark background, saturated solid background, hard black outline, thin font, serif font, script font, handwritten cursive, letters of the same color, more than four letters, metallic chrome, gold, glitter, matte clay, rough texture, grain, harsh dark shadow, strong perspective, extruded block letters with sharp edges, extra icons, stars, hearts, sparkles, illustrations, mascots, misspelled letters, extra letters
```

## 参考 IP 排除（avoid）

```avoid
letters DDUP, DD UP keyboard icon, green D blue D pink U yellow P arrangement
```

## 验收清单

- [ ] 近白底铺满，带淡淡彩色晕，字母组排布符合所选版式
- [ ] 字母圆胖鼓起、半透明果冻光泽，左上有弧形高光
- [ ] 内容与 `--label` 完全一致，每个字母一种不同糖果色
- [ ] 两组白色胶囊短线位于外沿相对位置，无其他装饰
- [ ] 与参考图并排对比：字样与配色分配不同，不是 DDUP 的 2×2 翻版

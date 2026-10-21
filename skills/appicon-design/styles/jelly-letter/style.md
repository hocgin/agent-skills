---
id: jelly-letter
name: 果冻字块
references: reference.png
keywords: keyboard, input, typing, font, text, chat, message, social, kids, education, learning, language, word, game, puzzle, casual, sticker, emoji, candy, cute, beauty, 键盘, 输入法, 打字, 字体, 文字, 聊天, 消息, 社交, 儿童, 教育, 学习, 语言, 单词, 游戏, 益智, 休闲, 贴纸, 表情, 糖果, 可爱, 美妆
lettering: required
label_style: plump glossy 3D jelly-candy letters, each letter a different candy color from the palette, with deep translucent tinted counters
summary: 白色柔光底上 2–4 个圆胖 3D 果冻字母拼块，每个字母一种糖果色、通透光泽高光，四周晕出同色彩色柔光，两侧白色胶囊短线。
---

# 果冻字块 `jelly-letter`

> 参考：`reference.png`（键盘 App「DD UP」备用图标：四个字母 2×2 拼块）。与 `pop-letter` 同骨架，区别在 3D 果冻材质与浅色底。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 背景近白 `#F7FBFE`，角落带各字母颜色的淡晕（粉紫 `#F5E4F6`、杏黄 `#FAEBD6`）；字母糖果色，**每个字母一种、互不重复**：薄荷绿 `#89FA9A`（暗部 `#69E184`）、天蓝 `#5AA6F6`、草莓粉 `#EC799B`（暗部 `#E84579`）、柠檬黄 `#FAE352`（边缘 `#F4B840`）；字怀为同色深色透光（如深绿 `#357A5D`）；装饰白 `#FAFCFC` |
| 造型 | 圆胖泡泡字，笔画极粗、字怀小，形体像充气 / 软糖般鼓起；每个字母轻微旋转，像散落的糖块 |
| 材质 | 半透明果冻 / 软糖 / 光泽塑料：表面光滑，内部微透光，色彩由上至下略变深 |
| 光影 | 顶部柔和光源；每个字母左上有一条长弧形镜面高光 + 小点高光；边缘有轻微次表面透光；字母底部有同色柔和彩色投影 / 光晕，弥散到白底上 |
| 构图 | 字母紧密拼成方块（2 字母并排、3 字母品字形、4 字母 2×2），约占画布 80%，居中，字母互相紧贴略挤压 |
| 质感 | 干净顺滑的 3D 渲染，无颗粒、无纹理 |
| 细节 | 唯一装饰是 2 组白色立体胶囊短线（每组 2 条），位于左侧中上与右侧中下的外沿；不加其他图形 |
| 情绪 | 甜美、可爱、轻盈、治愈 |

**签名特征**：① 光泽半透明的 3D 果冻字母；② 每个字母一种糖果色，并在白底上晕出同色柔光；③ 对角两侧的白色胶囊短线。

## 主体转译规则

与 `pop-letter` 相同：主体**就是文字**，取项目名称的首字母 / 缩写，共 **2–4 个字母**，通过 `--label` 传入。

- 2 个字母：左右并排，略错位；
- 3 个字母：上 2 下 1 或上 1 下 2 的品字形；
- 4 个字母：2×2 网格。

主体描述只写字母排布与颜色分配（如 `letters "D" "D" on the top row and "U" "P" on the bottom row; green D, blue D, pink U, yellow P`），不写材质光影。

## 可变元素

- 字母内容与数量（2–4）
- 字母排布方式与各自旋转角度
- 色板内的颜色分配（不重复），背景淡晕随字母颜色变化
- 白色胶囊短线的具体角度（位置固定在对角两侧）

## 风格约束（style）

```style
Cute glossy 3D lettermark render, like soft jelly candy or inflated glossy plastic. Extremely chunky, rounded, puffy bubble letters with very thick strokes and small counters, each letter slightly rotated like scattered candies, softly squeezed against each other. Every letter is one candy color from this palette only, and no two letters share a color: mint green (#89FA9A), sky blue (#5AA6F6), strawberry pink (#EC799B), lemon yellow (#FAE352). Each letter is semi-translucent and smooth, its color deepening slightly toward the bottom, with deep translucent tinted counters. Soft light from above: a long curved specular highlight along the upper-left edge of every letter plus a small dot highlight, subtle subsurface glow at the rims. Each letter casts a soft colored shadow and glow of its own hue that diffuses into the background. The background is an airy near-white (#F7FBFE) with faint pastel color haze near the letters. The only decoration is two pairs of short white glossy 3D capsule dashes. Clean smooth render, no grain, no texture. Sweet, cute, light, cheerful mood.
```

## 构图要求（composition）

```composition
Near-white background filling the whole canvas. The letter block is centered and fills about 80% of the canvas. Two letters sit side by side, three letters form a pyramid, four letters form a two-by-two grid. One pair of white capsule dashes sits just outside the block on the left side slightly above center, and the other pair sits outside the block on the lower right, pointing outward diagonally. Straight-on front view with only a hint of depth.
```

## 负面约束（negative）

```negative
flat 2D vector, black background, dark background, saturated solid background, hard black outline, thin font, serif font, script font, handwritten cursive, letters of the same color, more than four letters, metallic chrome, gold, glitter, matte clay, rough texture, grain, harsh dark shadow, strong perspective, extruded block letters with sharp edges, extra icons, stars, hearts, sparkles, illustrations, mascots, misspelled letters, extra letters
```

## 验收清单

- [ ] 近白底铺满，带淡淡彩色晕，字母块居中约占 80%
- [ ] 字母圆胖鼓起、半透明果冻光泽，左上有弧形高光
- [ ] 内容与 `--label` 完全一致，每个字母一种不同糖果色
- [ ] 字母下方有同色柔和彩色投影 / 光晕
- [ ] 左上、右下各一组白色胶囊短线，无其他装饰

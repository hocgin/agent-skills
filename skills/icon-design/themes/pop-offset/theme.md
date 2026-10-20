---
id: pop-offset
name: 波普错位
reference: reference.jpg
keywords: game, entertainment, party, event, fun, video, live, ticket, kids, education, shopping, deal, festival, sport, 游戏, 娱乐, 派对, 活动, 趣味, 视频, 直播, 票务, 少儿, 教育, 购物, 优惠, 节日, 运动, 潮流
tile_color: "#F5F5F5"
summary: 粗炭黑描边 + 柠檬黄主填充 + 薄荷绿侧向错位色块，略带倾斜的几何造型，复古波普的活力感。
---

# 波普错位 `pop-offset`

> 参考：`reference.jpg`（娱乐 / 派对 / 发现 / 我的）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 描边与图形符号炭黑 `#222222`；主填充柠檬黄 `#FFEE3A`；错位色块薄荷绿 `#78F2C2`；展示圆底 `#F5F5F5`。严格 3 色 |
| 材质 | 平面矢量，类似套色印刷的实色块，无纹理、无渐变 |
| 光影 | 无真实光照；薄荷绿作为主体内侧右/下缘的错位色带（像印刷套版偏移），边界锐利，形成侧向立体暗示 |
| 构图 | 单主体居中，占画布约 45%；主体常**轻微倾斜 3–15°**，富动感；可带 1–3 个小装饰（星星、短放射线）在主体外右上 |
| 造型 | 以基础几何为骨架（圆角矩形、三角、圆、人像胸像），边角小圆角，比例略带手作随意感 |
| 线条 | 粗等宽描边，约为图标宽度 6%；圆角连接；允许局部开口或分离线段（如胸像的肩线独立） |
| 细节 | 内部符号用炭黑实心：十字键、圆点、弧形微笑、指针等；符号简洁、粗壮、无描边细节 |
| 情绪 | 活泼、热闹、复古潮流、有能量 |

## 可变元素

- 主体物体与几何骨架
- 倾斜角度（3–15°）与方向
- 内部炭黑符号的内容与布局
- 外部小装饰（星星 / 放射短线）是否出现及数量（0–3）
- 薄荷绿色带位于右侧或下侧

## 固定风格（style）

```style
Rendered in a bold retro pop flat 2D vector style. Thick uniform charcoal (#222222) outline about 6% of the icon width with rounded joins, built on simple geometric forms with small rounded corners and a slightly hand-made, playful proportion; the shape may be tilted a few degrees for energy. Main fill is solid lemon yellow (#FFEE3A). A crisp flat mint-green (#78F2C2) band sits inside the outline along the right or bottom edge, like a misregistered offset print, with sharp clean boundaries and no stroke of its own. Inner symbols are simple, chunky solid charcoal shapes such as dots, plus signs, smile arcs or needles. Optional tiny charcoal sparkle stars or short burst lines outside the upper-right of the shape. Strictly limited palette: charcoal, lemon yellow and mint green only on white. No lighting, no gradients, no texture, no cast shadow. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, halftone dots, noise, drop shadow, cast shadow, glow, thin lines, hairline stroke, variable stroke width, colored outline, extra colors, red, blue, purple, orange, pink, pastel palette, detailed illustration, small intricate details, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 只出现 炭黑 / 柠檬黄 / 薄荷绿（+ 浅灰圆底、白底）
- [ ] 粗炭黑等宽描边，几何骨架
- [ ] 薄荷绿为锐利边界的侧向错位色带
- [ ] 内部符号为炭黑实心粗形
- [ ] 有轻微倾斜或动感装饰，整体活泼

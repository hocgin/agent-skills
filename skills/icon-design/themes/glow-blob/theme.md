---
id: glow-blob
name: 晕染光斑
reference: reference.png
keywords: ai, magic, creative, design, art, plugin, extension, developer, sdk, api, open source, web3, startup, notification, eco, nature, brand, 创意, 设计, 艺术, 魔法, 插件, 扩展, 开发者, 开源, 接口, 区块链, 创业, 通知, 环保, 自然, 品牌, 年轻, 个性, 潮
tile_color: "#FFFFFF"
summary: 粗黑断口线稿 + 独立圆点节点，背后一团边缘柔化的高饱和喷枪色晕溢出轮廓，线与色错位分离，潮酷有设计感。
---

# 晕染光斑 `glow-blob`

> 参考：`reference.png`（魔法棒 / 齿轮 C / 信息 i / 立方体 / 铃铛 / 节点六边形 / 叶子）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 线条暖调近黑 `#201414`；色晕为高饱和单色，**每个图标只取 1 种**：琥珀黄 `#F0C048`、珊瑚橙 `#F89060`、湖蓝 `#30B8D8`、紫罗兰 `#9850E0`、朱红 `#C82818`、柠檬黄 `#F8F008`、青柠绿 `#C8F880`；背景纯白 |
| 材质 | 线稿为干净矢量；色晕为喷枪 / 高斯模糊质感的柔边色块，中心实、边缘羽化 |
| 光影 | 无真实光照；色晕像一团发光光斑，作为唯一的「氛围层」 |
| 构图 | 单主体居中，占画布约 45%；色晕约为主体的 70–85% 大小，**中心相对线稿偏左下或偏中**，且**溢出轮廓线外侧**，不贴合形状 |
| 造型 | 几何（圆、六边形、立方体）与有机（星形、叶子、铃铛）都可；轮廓整体规整 |
| 线条 | 粗等宽黑线，约图标宽度 6%，圆头圆角；**轮廓常有 1–3 处断口**，线段分离（齿轮外圈的分段、六边形的断边）；可带独立实心黑色圆点作为节点/端点 |
| 细节 | 内部符号用同色黑线或实心黑形（字母 C、斜体 i、Y 形棱线、叶脉）；1 个为主 |
| 情绪 | 潮酷、创意、有设计感、年轻 |

## 可变元素

- 主体物体与轮廓形态
- 断口的数量（1–3）与位置，是否带黑色圆点节点
- 色晕颜色（色板 7 选 1，成套时轮换）以及相对线稿的偏移方向
- 内部符号内容

## 固定风格（style）

```style
Rendered as a bold line icon with a soft airbrushed color glow, in a modern 2D vector style. A thick uniform warm near-black (#201414) line about 6% of the icon width, round caps and round joins, drawing a clean outline with one to three deliberate gaps where the stroke breaks into separate segments; optional solid black round dots act as nodes or endpoints. Inner symbols use the same black line or small solid black shapes. Behind the line art sits a single soft blurred color blob, like an airbrush spray or Gaussian-blurred spot, with a solid center and feathered edges, in one vivid saturated color from this palette only: amber (#F0C048), coral (#F89060), cyan (#30B8D8), violet (#9850E0), vermilion red (#C82818), lemon yellow (#F8F008) or lime green (#C8F880). The blob is about 80% of the subject size, slightly offset toward the lower-left or center, and bleeds outside the outline instead of filling the shape exactly. The rest of the interior stays white. Only black line art plus one glow color per icon. No hard color fill, no lighting, no gradients other than the blob's soft edge, no texture, no cast shadow. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp line edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
3D, glossy, realistic, photo, texture, noise, grain, drop shadow, cast shadow, hard-edged color fill, color filling exactly inside the outline, flat solid fill, multiple glow colors in one icon, rainbow gradient, neon outer glow around the lines, colored lines, thin lines, hairline, variable stroke width, sketchy hand-drawn lines, closed perfect outline without gaps, cute face, eyes, mouth, small intricate details, text, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 黑色粗线稿，有 1–3 处断口
- [ ] 每个图标只有 1 团色晕，边缘柔化羽化
- [ ] 色晕相对线稿偏移并溢出轮廓，不是形内平涂
- [ ] 除黑线与色晕外均为白色

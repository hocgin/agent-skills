---
id: mono-thin
name: 极简细线
reference: reference.png
keywords: reader, reading, book, note, docs, document, wiki, knowledge, podcast, audio, subtitle, caption, transcript, ai, assistant, developer, sdk, cli, editor, writing, markdown, minimal, 阅读, 读书, 笔记, 文档, 知识库, 播客, 音频, 字幕, 转写, 智能助手, 开发者, 编辑器, 写作, 极简, 素雅
tile_color: "#FFFFFF"
summary: 单色中灰细线、24px 网格的系统级 UI 图标，无填充无点缀，小圆角、几何克制，像 Lucide / SF Symbols 的轻量线性风。
---

# 极简细线 `mono-thin`

> 参考：`reference.png`（耳机 / 波形 / 字幕 CC / 打开的书 / 笔记本）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 单色中性灰 `#505050`；背景纯白。**只有 1 种颜色** |
| 材质 | 纯线性矢量，无填充、无纹理 |
| 光影 | 完全无光影 |
| 构图 | 单主体居中、正视端正，基于 24px 网格，主体约占画布 45%；结构稀疏，大量留白 |
| 造型 | 功能性 UI 图标的标准几何结构：矩形、圆弧、折线；**圆角小而克制**（约线宽的 1–2 倍），边缘偏方正；不夸张、不卡通 |
| 线条 | 细等宽单线，约 24px 网格上 1.5px（≈ 图标宽度 6%），圆头圆角；线条可开放（波形、书页） |
| 细节 | 内部细节极少（0–2 处），用同线宽的短线或小字形表达（如 CC 字母、书脊中线、笔记本的两条短横线与装订边）；不使用任何点缀色或实心块 |
| 情绪 | 安静、理性、专业、素雅 |

## 可变元素

- 主体物体与其几何结构
- 0–2 处内部细节的内容与位置
- 线条是否开放（开放折线 / 闭合轮廓）

## 固定风格（style）

```style
Rendered as a minimal thin-line system UI icon in flat 2D vector style, like a modern interface glyph drawn on a 24px grid. Single uniform neutral gray (#505050) monoline stroke, thin, about 1.5px on a 24px grid (roughly 6% of the icon width), round caps and round joins, no fills at all. Built from plain functional geometry such as rectangles, arcs and polylines with small restrained corner radius, slightly squarish edges, upright, front-facing and balanced. Very sparse: at most two small inner details drawn with the same stroke, such as a short line or a tiny letterform. Exactly one color, no accent color, no solid areas. No lighting, no gradients, no texture, no shadow. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, pixel-precise, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, noise, drop shadow, glow, filled shapes, solid fill, color accent, yellow dot, multiple colors, black heavy stroke, thick bold lines, chunky, hairline too thin to see, variable stroke width, sketchy hand-drawn lines, wobbly lines, large rounded corners, bubbly cartoon shapes, tilted, rotated, cute face, eyes, mouth, decorative details, text, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 只有一种中性灰，无任何点缀色和实心块
- [ ] 细等宽圆头单线（≈ 24px 网格 1.5px）
- [ ] 圆角小、结构方正、端正
- [ ] 内部细节 ≤ 2 处，整体稀疏

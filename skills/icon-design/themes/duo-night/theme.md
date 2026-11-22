---
id: duo-night
name: 暗夜双色
reference: reference.png
keywords: dark, dark mode, night, sidebar, toolbar, menu, desktop, productivity, notes, bookmark, password, vault, security, privacy, file, download, favorite, collection, reader, ai, assistant, developer, tool, utility, minimal, 深色, 暗色, 夜间, 侧边栏, 工具栏, 菜单, 效率, 笔记, 便签, 书签, 收藏, 密码, 保险箱, 安全, 隐私, 文件, 下载, 阅读, 智能助手, 开发者, 工具, 极简, 克制
tile_color: "#1E1E21"
tile_desc: soft dark charcoal
icon_type: flat duotone glyph icon
background: plain near-black (#101012) background
summary: 近黑背景上的中灰 + 纯白双色实心圆角叠片图标，主体灰块、辅件白块，以背景色细缝分隔，无描边无阴影，深色模式侧边栏般的安静克制。
---

# 暗夜双色 `duo-night`

> 参考：`reference.png`（钥匙孔方块 + 星芒 / 双书签叠页 / 便签叠片 / 下载文件 / 星星魔杖）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 背景近黑 `#101012`；主体中灰 `#707071`；辅件与符号纯白 `#FFFFFF`。**严格 2 色 + 背景**，无任何彩色 |
| 材质 | 纯平面实色块，无纹理、无渐变、无高光 |
| 光影 | 完全无光影、无投影；前后层次只靠灰/白明度差和细缝表达 |
| 构图 | 单主体居中、整体端正（叠片中的单片可轻微倾斜 ±10°），占画布约 45%；轮廓紧凑饱满 |
| 造型 | 大圆角的实心几何片：圆角方块、书签、卡片、文件、圆胖五角星；**签名特征：「灰色主片 + 白色辅件」双层结构**——白色辅件可以是后层错位叠片、折角、角标星芒、白色内部符号；前后片之间用背景色细缝（约图标宽度 4%）分隔 |
| 线条 | 无描边；内部符号（钥匙孔、短横线、箭头）为白色粗圆头线或实心小形，线宽约图标宽度 8% |
| 细节 | 内部符号 0–2 个，极简；角标（四芒星、小棒）最多 1 个，位于右下或右上并压住主片边缘 |
| 情绪 | 安静、克制、现代、夜间专注 |

## 可变元素

- 主片的外形（圆角方 / 卡片 / 文件 / 书签 / 星形等实心剪影）
- 白色辅件的形式：后层错位叠片、折角、角标、内部符号，以及其位置
- 灰/白角色互换（如星星主体为白、手柄为灰），但仍只用这两种颜色
- 叠片的轻微倾斜角度

## 固定风格（style）

```style
Rendered as a flat duotone solid glyph icon in 2D vector style, like a dark-mode sidebar icon. Exactly two flat colors on the dark canvas: medium gray (#707071) for the main shape and pure white (#FFFFFF) for the secondary piece and inner symbol. The signature structure is a chunky solid main shape with large rounded corners plus one white companion element, such as an offset overlapping layer behind it, a folded corner, a small corner badge like a four-pointed sparkle, or a simple white inner symbol. Overlapping pieces are separated by a thin gap of the background color, about 4% of the icon width. Inner symbols are minimal, drawn as bold rounded white strokes about 8% of the icon width or small solid white shapes, at most two of them. No outline stroke, no other colors, no lighting, no gradients, no texture, no shadow, no glow. Mostly upright, individual layered pieces may tilt slightly. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, noise, drop shadow, long shadow, glow, neon, outline stroke, line icon, hollow shape, thin lines, colorful, red, orange, yellow, green, blue, purple, pink, black shapes, light background, white background, more than two colors, sharp corners, intricate details, cute face, eyes, mouth, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 近黑背景上只有中灰 + 纯白两色
- [ ] 灰色主片 + 白色辅件的双层结构，叠放处有背景色细缝
- [ ] 实心大圆角，无描边、无阴影、无渐变
- [ ] 内部符号 ≤ 2 个，简洁粗圆头

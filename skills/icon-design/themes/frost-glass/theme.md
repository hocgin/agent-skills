---
id: frost-glass
name: 磨砂玻璃
reference: reference.png
keywords: glass, glassmorphism, frosted, modern, ios, os, system, productivity, office, document, file, folder, cloud, storage, gallery, photo, chat, message, weather, calendar, wallet, card, payment, finance, saving, bookmark, note, 玻璃, 磨砂, 毛玻璃, 现代, 系统, 办公, 效率, 文档, 文件, 文件夹, 云盘, 相册, 图片, 聊天, 消息, 天气, 日历, 钱包, 银行卡, 支付, 理财, 存钱, 收藏, 书签, 笔记, 通透, 精致
tile_color: "#F4F6FA"
summary: 后层高饱和渐变色块 + 前层半透明磨砂玻璃片，重叠处透出被模糊的后层色彩，无描边、白色极简符号，通透精致的现代系统感。
---

# 磨砂玻璃 `frost-glass`

> 参考：`reference.png`（存钱罐与金币 / 叠放银行卡 / 日历 Sun 8 / 风景图片 / 书签加号 / 叠放文档 / 文件夹 / 双聊天气泡 / 云朵与太阳）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 每个图标取**一个色彩家族**，由「后层浓郁渐变 + 前层浅淡磨砂」组成：<br>暖阳 黄 `#FCE043` → 橙 `#EB9E2D` → 红 `#E25031`<br>天蓝 浅蓝 `#90D6F9` → 宝蓝 `#5594EC`，磨砂层 `#A8CBFC`<br>紫晶 紫罗兰 `#9F3DCC` → 品红 `#D93FA8`，磨砂层 `#B299E8`<br>樱粉 粉 `#E89FAB` + 金币黄 `#EDB934`<br>青绿 `#60ABA0` → 薄荷 `#9EE0C0`（仅作山体/植物等辅色）<br>白色符号 `#FFFFFF`，深色数字 `#3A2A2A`（仅限日历类），背景纯白 |
| 材质 | 玻璃拟态（glassmorphism）：前层为半透明磨砂玻璃，带背景模糊（backdrop blur）；后层为光滑的实心渐变色块；整体柔和、通透，无颗粒纹理 |
| 光影 | 无硬投影；前层边缘有极细的亮色高光边与柔和内发光，局部边缘（尤其底部）轻微虚化、渐隐；后层透过前层呈现被模糊、变浅的色彩 |
| 构图 | 单主体居中，占画布约 50%；典型为「后层偏右上、前层偏左下」的错位叠放，前层遮住后层约 30–60%；不倾斜，正视角 |
| 造型 | 简洁的圆角几何（卡片、气泡、文件、文件夹、书签）或圆胖的有机形（存钱罐、云朵）；中等圆角；**签名特征：两层叠放，前层是磨砂玻璃，重叠区域透出后层的模糊色彩** |
| 线条 | 完全无描边；结构仅靠色块、透明度和模糊区分 |
| 细节 | 前层上放置极简白色实心符号（加号、三个圆点、几条圆头横线）或少量文字数字（如日历的 "Sun 8"）；1 个为主，不超过 2 处 |
| 情绪 | 通透、精致、现代、轻盈 |

## 可变元素

- 主体物体，以及前层 / 后层的拆分方式（后层可以是同类物体的另一张，也可以是金币、太阳等配件）
- 选用哪个色彩家族（成套时各图标轮换）
- 前层上的白色符号内容
- 前后层的错位方向（默认后层右上、前层左下）

## 固定风格（style）

```style
Rendered as a modern glassmorphism icon in a clean 2D vector-meets-soft-render style, with no outlines at all. Each icon is built from two overlapping layers: a back layer that is a smooth, vivid, saturated gradient shape, and a front layer that is a translucent frosted glass pane with backdrop blur, so wherever the front layer overlaps the back layer the back colors show through softened, lighter and blurred. The front glass pane is lightly tinted in a pale tone of the same color family, with a very thin bright highlight edge and a soft inner glow; parts of its edges, especially the bottom, softly fade or blur out. Each icon uses one color family only: warm sunset (yellow #FCE043 to orange #EB9E2D to red #E25031), sky blue (light blue #90D6F9 to royal blue #5594EC, glass tint #A8CBFC), amethyst (violet #9F3DCC to magenta #D93FA8, glass tint #B299E8), blossom pink (#E89FAB with golden #EDB934 accents), with teal #60ABA0 to mint #9EE0C0 allowed only as a secondary accent. Gradients are smooth and run diagonally within each shape. Typical arrangement: the back layer offset toward the upper right, the front layer toward the lower left, covering 30 to 60 percent of the back layer. Shapes are simple with medium rounded corners, plump and friendly, viewed straight on. Inner details on the front pane are minimal solid white symbols such as a plus sign, three dots or a few rounded lines, at most one or two details. No stroke, no hard cast shadow, no harsh specular reflections, no texture, no perspective tilt. Subject centered, occupying about 50% of the canvas, on a pure white background with generous empty space. Soft, airy and premium, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
outline, stroke, black outline, line icon, flat single-color fill, opaque front layer, no transparency, hard drop shadow, long shadow, cast shadow, realistic glass reflections, chrome, metallic, glossy plastic, clay, photorealistic, photo, texture, noise, grain, isometric, perspective tilt, 3D extrusion, neon glow, dark background, black, muddy colors, gray, multiple color families in one icon, rainbow, cute face, eyes, mouth, small intricate details, busy symbols, long text, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 前后两层叠放，前层为半透明磨砂玻璃，重叠区透出模糊的后层颜色
- [ ] 后层为高饱和平滑渐变，单个图标只用一个色彩家族
- [ ] 完全无描边、无硬投影
- [ ] 前层符号为白色极简实心形，不超过 2 处
- [ ] 正视角、圆角简洁造型、白底留白充足

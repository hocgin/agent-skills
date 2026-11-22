---
id: mono-glass
name: 灰阶玻璃
reference: reference.png
keywords: glass, frosted, monochrome, grayscale, neutral, premium, minimal, os, system, launcher, dock, tab bar, toolbar, productivity, office, document, note, message, chat, file, folder, cloud, storage, contact, team, user, account, settings, enterprise, 玻璃, 磨砂, 灰阶, 黑白, 单色, 中性, 高级, 极简, 系统, 桌面, 底栏, 工具栏, 效率, 办公, 文档, 笔记, 消息, 聊天, 文件, 文件夹, 云盘, 联系人, 团队, 用户, 账户, 设置, 企业, 质感, 沉稳
tile_color: "#F7F7F9"
tile_desc: soft near-white
icon_type: monochrome frosted glass icon
background: plain soft cool light gray (#EAE9EE) background
summary: 无彩色的双层叠放图标：后层炭黑渐变实心块 + 前层浅银灰磨砂玻璃片，玻璃顶缘细亮高光，前层上用炭黑短横作符号，冷浅灰背景，沉稳高级的系统质感。
---

# 灰阶玻璃 `mono-glass`

> 参考：`reference.png`（叠放文档便签 / 双人联系人 / 文件夹）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | **完全无彩色**：后层炭黑渐变 `#4B4B4B`（上）→ `#181818`（下）；前层银灰磨砂 `#DADADA`（亮部）→ `#A0A0A0`（中部暗带）；玻璃高光边 `#FFFFFF`；前层符号炭黑 `#2A2A2A`；背景冷浅灰 `#EAE9EE` |
| 材质 | 后层为光滑哑光的实心渐变块；前层为半透明偏不透明的磨砂玻璃 / 缎面银，带轻微背景模糊；无颗粒纹理 |
| 光影 | 柔和顶光：前层玻璃上缘有极细的白色高光边，表面纵向明暗渐变（上亮、中部略暗、底部回亮）；前层下方有极淡的柔和接触阴影；无硬投影、无镜面反射 |
| 构图 | 单主体居中、正视不倾斜，占画布约 45%；**后层偏右上、前层偏左下**错位叠放，前层遮住后层约 40–60% |
| 造型 | 圆胖的大圆角几何：圆角方卡片、圆形头像 + 半圆肩、文件夹；**签名特征：深色后层 + 浅色磨砂玻璃前层的明暗对比叠放**，深浅两层轮廓相同或同类 |
| 线条 | 完全无描边；结构仅靠深浅明度对比与高光边区分 |
| 细节 | 前层上可有 0–2 个炭黑色实心圆头短横 / 小符号；不使用白色符号，不使用任何彩色 |
| 情绪 | 沉稳、高级、克制、现代 |

## 可变元素

- 主体物体，以及前层 / 后层的拆分方式（同类物体的两张、两个人、文件夹前后片等）
- 前层上的炭黑符号内容（0–2 个）
- 前后层的错位程度（方向固定为后层右上、前层左下）

## 固定风格（style）

```style
Rendered as a monochrome frosted glass icon in a clean soft-render 2D style, completely colorless, no outlines at all. Each icon is built from two overlapping layers of the same or related shape: a back layer that is a smooth matte solid charcoal shape with a subtle vertical gradient from dark gray (#4B4B4B) at the top to near black (#181818) at the bottom, and a front layer that is a light silver-gray frosted glass pane, mostly opaque with slight backdrop blur, shaded with a soft vertical gradient from light gray (#DADADA) through a slightly darker mid band (#A0A0A0) and lighter again near the bottom. The front pane has a very thin bright white highlight along its top edge and casts only a faint soft contact shadow onto the back layer. The back layer sits offset toward the upper right and the front layer toward the lower left, covering 40 to 60 percent of the back layer, creating a strong dark-versus-light contrast. Shapes are plump simple geometry with large rounded corners, viewed straight on and upright. Inner details on the front pane are minimal solid charcoal (#2A2A2A) rounded bars or tiny symbols, at most two. Grayscale only, no hue at all, no stroke, no hard cast shadow, no specular reflections, no texture, no perspective tilt. Subject centered, occupying about 45% of the canvas, generous empty space around it. Soft, quiet and premium, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
color, colorful, blue, purple, pink, red, orange, yellow, green, tinted glass, rainbow, outline, stroke, black outline, line icon, flat single-tone fill, white symbols, hard drop shadow, long shadow, cast shadow, mirror reflection, chrome, shiny metal, glossy plastic, clay, photorealistic, photo, texture, noise, grain, isometric, perspective tilt, 3D extrusion, neon glow, dark background, pure white background, sharp corners, cute face, eyes, mouth, small intricate details, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 完全无彩色，只有炭黑 / 银灰 / 白高光
- [ ] 深色后层（右上）+ 浅色磨砂玻璃前层（左下）错位叠放
- [ ] 前层顶缘细白高光，表面柔和纵向渐变，无硬投影
- [ ] 无描边，大圆角圆胖造型，正视端正
- [ ] 前层符号为炭黑色实心短横，≤ 2 个

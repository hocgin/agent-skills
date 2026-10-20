---
id: pastel-layer
name: 柔彩叠层
reference: reference.png
keywords: health, medical, care, beauty, baby, mother, women, food, recipe, reminder, todo, habit, planner, calendar, journal, wellness, fitness, shopping, 健康, 医疗, 护理, 美妆, 母婴, 女性, 美食, 菜谱, 提醒, 待办, 习惯, 计划, 日程, 手账, 养生, 健身, 购物, 温柔, 治愈
tile_color: "#FFFFFF"
summary: 无描边的柔和粉彩同色系双层叠片，前层浓、后层淡，用白色间隙分隔，圆胖可爱的温柔质感。
---

# 柔彩叠层 `pastel-layer`

> 参考：`reference.png`（铃铛 / 日历 / 创可贴 / 储物罐 / 爱心徽章 / 叠层卡片）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 每个图标取**一个色相家族**，含「主色 + 浅色 + 可选深点缀」三阶：<br>杏橙 `#F0AC57` / `#F8DDB9`<br>灰青 `#DBE3E2` / 点缀 `#87A59F`<br>丁香紫 `#E2BDE2` / `#FBE8FA` / 点缀 `#CB8CCA`<br>雾蓝 `#9AA5E2` / `#DDE1F9` / 点缀 `#CFD5F5`<br>珊瑚橙 `#EC6D3E` / `#F19E7C`<br>薰衣草紫 `#A08EF2` / `#D7D0FB`<br>背景纯白 |
| 材质 | 平面粉彩实色块，柔和、轻盈，无纹理、无渐变 |
| 光影 | 无真实光影；层次只靠同色系深浅叠放（前浓后淡） |
| 构图 | 单主体居中，占画布约 45%；可轻微倾斜（如创可贴 45°），整体圆胖紧凑 |
| 造型 | 2 层结构：主体层 + 辅助层（盖子/罐身、前卡/后卡、爱心/徽章、铃身/铃舌）；大圆角、胖乎乎的软几何；**层与层之间用一圈白色间隙分隔**（签名特征） |
| 线条 | 完全无描边；内部细节为同色系实心小形（小圆点、短胶囊条、小爱心、数字） |
| 细节 | 细节少而小：1–4 个同色系点缀；可用极淡的同色光晕/动感弧片衬在主体后方 |
| 情绪 | 温柔、治愈、轻盈、亲和 |

## 可变元素

- 主体物体与两层的拆分方式
- 选用哪个色相家族（成套时各图标轮换不同色相）
- 内部同色系小细节的内容与数量（1–4）
- 是否轻微倾斜、是否有后方淡色衬片

## 固定风格（style）

```style
Rendered as a soft pastel layered flat 2D vector icon with no outlines at all. Each icon uses a single hue family only: a main pastel tone for the front layer, a much lighter tint of the same hue for the back or secondary layer, and optionally a slightly deeper tone of the same hue for tiny details. Choose the hue family from apricot orange, sage gray-teal, lilac, misty periwinkle blue, coral orange or lavender purple. The subject is built from two overlapping chunky rounded shapes with large soft corner radius, plump and friendly; where the layers meet they are separated by a clean white gap ring. Small inner details are simple solid shapes in the same hue family, such as little dots, short capsule bars, a tiny heart or a numeral. Optional faint same-hue tint shapes behind the subject. Light, airy, gentle colors. No stroke, no black, no lighting, no gradients, no texture, no shadow. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, noise, drop shadow, glow, outline, stroke, black outline, line icon, black, dark colors, high contrast, neon, saturated primary colors, multiple hue families in one icon, rainbow, flat single-layer glyph, sharp corners, hard geometric precision, cute face, eyes, mouth, small intricate details, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 单个图标只用一个色相家族（主色 + 浅色 + 可选深点缀）
- [ ] 两层叠放，层间有白色间隙
- [ ] 完全无描边、无黑色
- [ ] 造型圆胖，细节少而小

---
id: bold-line
name: 粗黑线性
reference: reference.png
keywords: todo, task, calendar, schedule, planner, reminder, habit, notification, sync, sort, list, productivity, workflow, automation, shortcut, project, management, office, note, utility, tool, system, ui, 待办, 任务, 日历, 日程, 计划, 提醒, 习惯, 通知, 同步, 排序, 清单, 效率, 工作流, 自动化, 快捷指令, 项目管理, 办公, 工具, 系统, 利落, 清晰
tile_color: "#FFFFFF"
tile_desc: soft white
icon_type: bold line icon
background: plain light gray (#EFEFEF) background
summary: 浅灰背景上的纯黑粗等宽圆头单线 UI 图标，超椭圆般的大圆角轮廓 + 内部小点/对勾/折角细节，无填充无点缀色，利落清晰。
---

# 粗黑线性 `bold-line`

> 参考：`reference.png`（日历省略号 / 文档对勾 / 循环同步 / 降序列表 / 铃铛 / 日历 / 圆形闪电）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 线条纯黑 `#000000`；背景浅灰 `#EFEFEF`。**只有 1 种颜色** |
| 材质 | 纯线性矢量，无填充、无纹理 |
| 光影 | 完全无光影 |
| 构图 | 单主体居中、正视端正，基于 24px 网格，占画布约 45%；结构简洁，留白充足 |
| 造型 | 柔和的超椭圆 / 大圆角矩形轮廓（圆角约边长 30%），圆胖但不卡通；**签名特征：粗黑等宽线 + 少量实心小点与短线细节**（日历省略号三点、铃铛下的短横、列表的点）；箭头为粗短圆头箭头 |
| 线条 | 粗等宽单线，约 24px 网格上 2px（≈ 图标宽度 8–9%），圆头圆角；线条可开放（循环箭头、列表） |
| 细节 | 内部细节 0–2 处：同线宽的对勾、短横、折角，或实心小圆点（≤ 3 个） |
| 情绪 | 利落、清晰、友好、高效 |

## 可变元素

- 主体物体与其几何结构
- 0–2 处内部细节的内容与位置（对勾、点、短横、折角、闪电等）
- 线条开放或闭合
- 是否加外圈（如圆形徽章容器）

## 固定风格（style）

```style
Rendered as a bold line UI icon in flat 2D vector style, like a modern interface glyph drawn on a 24px grid. Single uniform pure black (#000000) monoline stroke, bold, about 2px on a 24px grid (roughly 8% of the icon width), round caps and round joins, no fills except tiny solid dots. Built from soft squircle-like shapes and rounded rectangles with generous corner radius, plus simple arcs and short straight lines; chunky short arrowheads with rounded tips. Upright, front-facing and balanced. Sparse: at most two small inner details drawn with the same stroke, such as a checkmark, a short dash, a folded corner, or up to three small solid dots. Exactly one color, no accent color, no large solid areas. No lighting, no gradients, no texture, no shadow. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, pixel-precise, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, noise, drop shadow, glow, filled shapes, solid fill, large solid areas, color accent, yellow dot, colorful, gray lines, multiple colors, hairline thin lines, variable stroke width, sketchy hand-drawn lines, broken gaps in outline, wobbly lines, sharp square corners, tilted, rotated, cute face, eyes, mouth, decorative details, text, watermark, multiple subjects, dark background, busy background, pattern background
```

## 验收清单

- [ ] 浅灰背景上只有纯黑一色
- [ ] 粗等宽圆头单线（≈ 24px 网格 2px），无大面积填充
- [ ] 大圆角超椭圆轮廓、端正
- [ ] 内部细节 ≤ 2 处，可含 ≤ 3 个实心小点

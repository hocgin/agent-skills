---
id: doodle-buddy
name: 涂鸦萌宠
reference: reference.jpg
keywords: social, community, chat, friend, pet, kids, youth, lifestyle, diary, note, emotion, mood, cute, companion, 社交, 社区, 聊天, 交友, 宠物, 儿童, 年轻, 生活, 日记, 笔记, 情绪, 心情, 可爱, 陪伴, 萌
tile_color: "#F5F5F5"
summary: 粗黑断口手绘轮廓 + 紫色极简表情 + 青柠绿内侧月牙阴影，物体被拟人化为软萌小生物。
---

# 涂鸦萌宠 `doodle-buddy`

> 参考：`reference.jpg`（首页 / 收藏 / 消息 / 我的）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 轮廓近黑 `#1A1A1A`；表情紫 `#6B3CF6`；青柠绿 `#A8F25C`；内部纯白 `#FFFFFF`；展示圆底 `#F5F5F5`。严格 3 色 + 白 |
| 材质 | 纯平面矢量，无纹理、无渐变、无光泽 |
| 光影 | 无真实光照；青柠绿月牙充当「右侧受光/背光」的伪阴影，贴着轮廓内侧右缘，宽度由窄到宽再收尖 |
| 构图 | 单主体居中，占画布约 45%，视觉略偏轻松（可微倾 0–8°）；四周大留白 |
| 造型 | 软胖、略不规则的手绘有机轮廓（圆角五边形、花朵/云朵、铃铛、猫头）；边缘轻微抖动但闭合饱满；**轮廓左上方有一个刻意的短缺口**（签名特征） |
| 线条 | 超粗等宽描边，约为图标宽度 8%；圆头圆角；缺口两端为圆头 |
| 细节 | 紫色实心极简五官，无描边：粗弧形微笑、两个竖向短矩形眼、眨眼的「<」菱形。五官只占主体内部 25–35% 面积 |
| 情绪 | 可爱、友好、俏皮、年轻 |

## 可变元素

- 主体物体与其轮廓形态（必须可被拟人化为软造型）
- 五官的组合（微笑 / 双竖眼 / 眨眼 / 单弧眼）与在主体内的位置
- 轮廓缺口的具体位置（限定在左上 1/4 区域）
- 少量附属结构：耳朵、尖角、底部波浪边等，仍用同一粗黑轮廓

## 固定风格（style）

```style
Rendered as a cute personified doodle character in flat 2D vector style. Chunky hand-drawn outline in near-black (#1A1A1A): one very thick uniform stroke about 8% of the icon width, rounded caps and joins, soft slightly wobbly organic contour that feels plump and friendly. The outline has one deliberate short gap near the upper-left, both ends of the gap rounded. Interior filled plain white. A flat lime-green (#A8F25C) crescent-shaped shading band hugs the inside of the right edge of the outline, tapering at both ends, no stroke of its own. Minimal kawaii face made of solid violet (#6B3CF6) flat shapes with no outline, such as a thick smile arc, two short vertical rectangle eyes, or a winking chevron, kept small in the middle of the body. Strictly limited palette: near-black, violet, lime green and white only. No lighting, no gradients, no texture, no cast shadow. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, noise, drop shadow, cast shadow, glow, thin lines, hairline stroke, variable stroke width, closed perfect geometric outline, sharp corners, colored outline, extra colors, red, blue, orange, pink, yellow, detailed facial features, mouth with teeth, eyebrows, pupils with highlights, nose, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 只出现 黑 / 紫 / 青柠绿 / 白（+ 浅灰圆底）
- [ ] 粗黑轮廓等宽、圆头，左上有缺口
- [ ] 青柠绿月牙位于内侧右缘，无描边
- [ ] 五官为紫色实心极简形，无描边
- [ ] 轮廓软胖不规则，非标准几何形

---
id: bold-mascot
name: 粗线萌徽
references: reference.png
keywords: mascot, badge, outline, gradient, puzzle, modular, doodle, friendly, 粗描边, 萌徽, 徽章, 渐变, 拼图, 模块, 涂鸦, 亲和
label_style:
summary: 暖白底上单个圆润拟人徽章，深梅色极粗圆头描边包住紫粉金纵向渐变，极简眼睛与大弯笑线，浅浮雕投影带来软胶贴章感。
---

# 粗线萌徽 `bold-mascot`

> 参考：`reference.png`，裁自用户四宫格右上图（带笑脸的拼图块）。色值为近似色板；拼图是参考主体，不是所有项目必须沿用的形状。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 背景暖白 `#FFFBF3`；轮廓与五官深梅棕 `#422234`；主体从上至下由紫 `#8771F7` 经粉 `#F39BC0`、珊瑚粉 `#FFA69F` 平滑过渡至金黄 `#FFDA68` |
| 造型 | 单个完整、圆润、略不规则的徽章剪影；深色描边宽约画布 4–5%，圆头圆接角；轮廓可有少量圆凸起与凹槽，负形开口保持宽大；五官嵌在上半部 |
| 材质 | 插画式不透明软胶贴章，正面近乎平面，边缘只有极浅厚度；不是鼓胀果冻，也不是金属珐琅 |
| 光影 | 左上柔光，轮廓边缘细微亮边，下方偏右短而柔的暖灰投影；体积主要来自贴章厚度，正面渐变不是镜面反射 |
| 构图 | 主体居中，占宽约 65–72%，四周暖白留空；轻微倾斜、正面视角；五官在中上区域，笑线连成视觉焦点，无周边装饰 |
| 质感 | 平滑连续渐变、利落轮廓，轻微柔化的投影，无纹理和颗粒 |
| 细节 | 两颗深色短胶囊眼 + 一条宽弧笑线；主体结构最多 3 处凸凹特征，不添加腮红、手脚或散落星星；无文字 |
| 情绪 | 友好、乐观、俏皮、轻松 |

**签名特征**：① 深梅色极粗圆润描边与同色笑脸；② 紫 → 粉 → 金的纵向连续渐变；③ 暖白留空与轻浅软胶贴章投影。

## 主体转译规则

把业务隐喻压缩成一个能加笑脸的徽章剪影：拼图（模块协作）、书签（收藏）、气泡（沟通）、云朵（同步）、文件夹（整理）。保留最多 2–3 处识别结构，所有尖角软化。

五官与轮廓使用相同粗线语言；眼睛与大弯笑线放在上半部，避免遮住主体的核心负形。拼图的卡口可替换为新物件的识别特征，不照搬具体品牌轮廓。

## 可变元素

- 单个徽章的业务剪影、凸凹结构与负形
- 轻微倾斜角度、两眼位置和笑线弧度
- 主体占比在 65–72% 内微调，保留四周留白

## 风格约束（style）

```style
Friendly illustrated mascot badge with an opaque almost-flat soft-rubber face and extremely thick deep plum-brown (#422234) contours, about 4–5% of the canvas width, with fully rounded caps and joins. A smooth continuous vertical fill transitions from violet (#8771F7) at the top through pink (#F39BC0) and coral pink (#FFA69F) to golden yellow (#FFDA68) at the bottom. Use the same deep plum-brown for two short capsule eyes and one broad curved smile. The silhouette is plump, simple and gently irregular with a few large rounded protrusions or cutouts. Very shallow raised edges, faint upper-left edge light and a short soft warm-gray contact shadow below and to the right. Warm off-white (#FFFBF3) background, crisp clean contours, seamless gradients, no grain. Friendly, optimistic and playful mood.
```

## 构图要求（composition）

```composition
Warm off-white background fills the canvas edge to edge. One complete centered emblem occupies about 65–72% of the canvas width with generous breathing room on all sides. Straight-on view, a slight playful tilt and very shallow relief. Keep the entire silhouette visible and place the simple face in its upper half without obscuring the identifying cutout. No surrounding objects or decorative marks.
```

## 负面约束（negative）

```negative
thin outline, pure black outline, angular line joins, sharp spikes, flat single-color fill, disconnected color bands, horizontal rainbow stripes, transparent jelly, inflated balloon, chrome, metallic enamel, strong extrusion, realistic surface texture, grain, blush cheeks, detailed eyelashes, limbs, extra stickers, sparkle decorations, dark background, full-bleed face close-up, cropped silhouette
```

## 验收清单

- [ ] 单个完整剪影居中留白，业务特征与负形清晰
- [ ] 描边与五官均为深梅色、粗圆线条
- [ ] 填色严格为上紫、中粉、下金的连续渐变
- [ ] 只有浅厚度和短柔投影，无透明果冻高光
- [ ] 两短眼与大弯笑线清晰，无多余装饰或文字

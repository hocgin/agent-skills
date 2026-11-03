---
id: clay-soft
name: 软陶立体
reference: reference.png
keywords: 3d, clay, soft, toy, plastic, cute, friendly, home, smart home, launcher, system, setting, search, profile, account, mail, camera, photo, tool, utility, kids, education, family, game, onboarding, 立体, 黏土, 软陶, 玩具, 可爱, 亲和, 家居, 智能家居, 桌面, 启动器, 系统, 设置, 搜索, 个人, 账户, 邮件, 相机, 拍照, 工具, 儿童, 教育, 家庭, 游戏, 温暖, 质感
tile_color: "#EFE8E2"
icon_type: soft 3D clay icon
background: plain warm beige (#E5DBD4) background
summary: 哑光软陶 / 磨砂塑料质感的圆润 3D 小物件，柔和顶光 + 底部软投影，物体固有色，暖米色背景，温暖可触的玩具感。
---

# 软陶立体 `clay-soft`

> 参考：`reference.png`（房子 / 放大镜 / 用户头像 / 齿轮 / 信封 / 相机）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 按**物体固有色**上色，每个图标 1 个主色 + 1–2 个辅色，中等饱和、略带暖调：<br>砖橙红 `#E0633A`（屋顶）、奶油白 `#F2ECE4`（墙体/高光面）、木棕 `#8A5A35`（门）、钴蓝 `#6A92D7` / 暗部 `#567DC8`、铁灰 `#6E6C6D`、暖黄 `#EFC752` / 暗部 `#E2B84D`、炭黑 `#2A2A2C`、银灰 `#B0BDC4`（金属/玻璃）<br>背景暖米色 `#E5DBD4` |
| 材质 | 哑光软陶 / 磨砂塑料 / 黏土，表面光滑细腻、无颗粒；玻璃部件为半透明浅蓝灰，仅有柔和反光 |
| 光影 | 柔和的左上方顶光；同色系明暗过渡塑造体积，边缘有轻微的亮色倒角高光；物体正下方有一小片柔和、扩散的接触阴影 |
| 构图 | 单主体居中，占画布约 55%；正视角略带俯视（约 10–15°），轻微 3/4 侧面体现厚度；不夸张透视 |
| 造型 | 圆胖、敦实的简化 3D 造型，所有边缘大圆角倒角，像软糖或玩具；结构简化到最少部件（2–4 个）；比例偏矮胖 |
| 线条 | 无描边；结构由体块、明暗和倒角区分 |
| 细节 | 极少：门、镜头、齿孔、信封折线等仅保留识别所需的最少结构，用凹陷或凸起的体块表现；无文字、无表情 |
| 情绪 | 温暖、亲和、可触、精致 |

## 可变元素

- 主体物体及其简化后的部件拆分
- 物体固有色（取色板内最贴近物体的颜色）
- 俯视角度在 10–15° 之间微调、是否带轻微 3/4 侧面
- 细节结构的凹凸方式

## 固定风格（style）

```style
Rendered as a soft 3D clay icon, like a small matte toy made of smooth soft-touch plastic or polymer clay. Chunky, plump, simplified shapes built from two to four parts, with generously rounded beveled edges everywhere and slightly squat proportions. Matte smooth surface with no grain, no glossy reflections; any glass part is a pale translucent blue-gray with only a soft sheen. Colors follow the object's natural colors in medium, slightly warm saturation, one main color plus one or two supporting colors per icon, chosen from this palette only: brick orange-red (#E0633A), cream white (#F2ECE4), wood brown (#8A5A35), cobalt blue (#6A92D7), iron gray (#6E6C6D), warm yellow (#EFC752), charcoal black (#2A2A2C) and silver gray (#B0BDC4). Soft diffuse studio lighting from the upper left, gentle same-hue shading for volume, subtle light bevel highlights on the edges, and a small soft diffused contact shadow directly beneath the object. Viewed straight on from slightly above, about 10 to 15 degrees, with a hint of three-quarter depth and no exaggerated perspective. Minimal details expressed as raised or recessed volumes, only what is needed for recognition. No outlines, no text, no face. Subject centered, occupying about 55% of the canvas, on a plain warm beige (#E5DBD4) background with generous empty space. Clean high-quality 3D render, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
flat 2D, vector line art, outline, stroke, black outline, cel shading, cartoon outlines, glossy, shiny chrome, mirror reflections, wet look, metallic sheen, glassmorphism, transparent layers, neon, glow, high saturation, oversaturated, rainbow, gradient background, dark background, hard shadow, long shadow, dramatic lighting, rim light, photorealistic, realistic material texture, wood grain, fabric, grain, noise, sharp edges, hard corners, thin fragile parts, high detail, intricate details, isometric, strong perspective, fisheye, cute face, eyes, mouth, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 哑光软陶 / 磨砂塑料质感，无镜面反射
- [ ] 所有边缘大圆角倒角，造型圆胖简化
- [ ] 左上柔光 + 底部小片柔和接触阴影
- [ ] 物体固有色，色彩中等饱和偏暖
- [ ] 暖米色纯色背景，无描边、无文字、无表情

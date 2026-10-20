---
id: solid-knockout
name: 实色镂空
reference: reference.png
keywords: system, setting, contact, account, cloud, sync, backup, browser, map, file, manager, enterprise, security, mail, calendar, os, launcher, 系统, 设置, 联系人, 通讯录, 账户, 云, 同步, 备份, 浏览器, 地图, 文件, 管理, 企业, 安全, 邮件, 日历, 桌面, 启动器, 稳重
tile_color: "#F9F9F5"
summary: 单色实心圆角剪影 + 白色负形镂空符号，无描边无阴影，每个图标一种沉稳的中饱和色。
---

# 实色镂空 `solid-knockout`

> 参考：`reference.png`（联系人 / 浏览器地球 / 通知方块 / 云同步）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 色板为中饱和沉稳色：森林绿 `#518B53`、钴蓝 `#4576B3`、赭棕 `#AD6C3A`、长春花蓝 `#658BF7`；镂空为纯白 `#FFFFFF`；背景暖米白 `#F9F9F5`。**每个图标只用色板中的 1 种颜色 + 白** |
| 材质 | 纯平面实色，无纹理、无渐变、无高光 |
| 光影 | 完全无光影、无投影 |
| 构图 | 单主体居中、端正不倾斜，占画布约 45%；外轮廓饱满紧凑 |
| 造型 | 外形为简单的实心几何底板：大圆角方块、圆形、云朵等；符号以白色**负形镂空**方式挖出（人像、经纬线大陆、对勾） |
| 线条 | 无描边；白色镂空的线状部分为粗等宽圆头线，约图标宽度 7% |
| 细节 | 附加元素（如右上角通知圆点）与主体同色，并用一圈白色间隙环把它与主体分隔开；符号简洁、1 个为主 |
| 情绪 | 稳重、可靠、系统级、干净 |

## 可变元素

- 主体底板的外形（圆角方 / 圆 / 云 / 其他饱满实心剪影）
- 白色镂空符号的内容
- 色板中选用哪一种颜色（成套时各图标轮换不同颜色）
- 是否带同色附加元素（徽标圆点、小角标）及其位置

## 固定风格（style）

```style
Rendered as a flat solid glyph icon in 2D vector style. The whole shape is one solid flat fill of a single calm medium-saturation color picked from this palette only: forest green (#518B53), cobalt blue (#4576B3), ochre brown (#AD6C3A) or periwinkle blue (#658BF7). The base is a simple compact silhouette such as a rounded square with large corner radius, a circle or a cloud. The symbol is carved out as pure white negative space knockout inside the solid shape, with chunky rounded forms and line parts about 7% of the icon width with round caps. Any attached element, such as a badge dot, uses the same color and is separated from the main shape by a thin white gap ring. No outline stroke, no second color, no lighting, no gradients, no texture, no shadow. Upright and balanced. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, realistic, photo, texture, noise, drop shadow, long shadow, glow, outline stroke, black outline, line icon, hollow shape, multiple colors in one icon, neon, pastel, saturated bright red, yellow, purple, pink, black, gray, tilted, rotated, cute face, eyes, mouth, small intricate details, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 每个图标只有 1 种色板颜色 + 白
- [ ] 实心底板，符号为白色负形镂空
- [ ] 无描边、无阴影、无渐变
- [ ] 附加元素同色，用白色间隙环分隔
- [ ] 端正、轮廓饱满

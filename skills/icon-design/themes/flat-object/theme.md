---
id: flat-object
name: 固有色扁平
reference: reference.png
keywords: finance, wallet, payment, bank, budget, expense, mail, email, calendar, password, security, vault, shop, ecommerce, life, daily, utility, widget, 金融, 钱包, 支付, 银行, 预算, 记账, 账单, 邮件, 日历, 密码, 安全, 保险箱, 购物, 电商, 生活, 日常, 小组件, 直观
tile_color: "#FFFFFF"
summary: 无描边的小巧实物剪影，按物体固有色上色，同色系深浅两阶表现结构，像精简版 emoji，一眼可认。
---

# 固有色扁平 `flat-object`

> 参考：`reference.png`（信封 / 日历 / 钱包 / 锁 / 爱心 / 美元硬币）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | **按物体固有色**上色（钱是绿、爱心是红、钱包是棕），整体中等饱和、略柔和。参考色：浅灰 `#E2E2E2` / `#CFCFCF`、日历蓝 `#5B9BF0` + 灰白 `#DFE0E0`、皮革棕 `#C5866D` / 深棕 `#9A4A30`、钞票绿 `#8DC86A`、薰衣草紫 `#8475E0` / 浅紫 `#DFDAF5`、珊瑚红 `#DB675E`、草绿 `#97C86B` / 深绿 `#4E8A3A`。背景纯白 |
| 材质 | 平面实色块，无纹理、无渐变、无高光 |
| 光影 | 无真实光源；只用**同色系深浅两阶**表现结构面（如信封上浅下深的折叶、钱包深色翻盖） |
| 构图 | 单主体居中、正视端正，占画布约 45%；轮廓紧凑饱满 |
| 造型 | 真实物体的高度简化剪影（emoji 式），大圆角、比例敦实；保留 1–2 个最具辨识度的结构（日历的顶部色条与装订环、钱包露出的钞票、锁的锁梁） |
| 线条 | 完全无描边；结构靠色块分割表达 |
| 细节 | 每个图标 1–3 个小细节色块（锁孔、按扣、$ 符号、装订环），细节色为主色的深色或浅色，或另一个物体固有色（如钱包内的绿色钞票）；单个图标颜色总数 ≤ 3 |
| 情绪 | 直观、友好、生活化、轻量 |

## 可变元素

- 主体物体（优先选择有明确固有色的实物）
- 主色（取物体固有色，靠近参考色板的饱和度）
- 深浅分面的位置与 1–3 个细节色块
- 成套时各图标颜色天然不同，无需统一色相

## 固定风格（style）

```style
Rendered as a simple flat 2D vector object icon in a minimal emoji-like style. The subject is a highly simplified, chunky, front-facing silhouette of a real object with large rounded corners and sturdy proportions, keeping only one or two of its most recognizable structural parts. It is colored in the object's own natural local color at medium, slightly soft saturation. Structure is shown only by flat color blocks: one main tone plus a darker or lighter tone of the same hue for folds, flaps or panels, and at most one extra natural color for a contained part. One to three small solid detail shapes such as a keyhole, a clasp dot, a currency symbol or binder rings. At most three colors per icon. No outline stroke, no lighting, no gradients, no highlights, no texture, no shadow. Upright and balanced. Subject centered, occupying about 45% of the canvas, generous empty space around it. Crisp clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
gradient, glossy, 3D, isometric, perspective, realistic, photo, texture, noise, drop shadow, long shadow, glow, specular highlight, outline stroke, black outline, line icon, neon, oversaturated colors, pastel washed-out colors, monochrome, more than three colors, white knockout glyph, cute face, eyes, mouth, small intricate details, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 颜色为物体固有色，单图标 ≤ 3 色
- [ ] 无描边，结构由同色系深浅色块表达
- [ ] 正视、端正、圆角敦实的简化剪影
- [ ] 细节 1–3 个，缩小后仍可辨识

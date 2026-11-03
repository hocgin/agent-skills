---
id: ink-block
name: 墨块撞色
reference: reference.png
keywords: shop, shopping, store, ecommerce, retail, mall, market, order, cart, basket, delivery, courier, logistics, takeout, coupon, discount, deal, gift, reward, payment, wallet, bank, money, cash, bill, receipt, invoice, finance, accounting, budget, statistics, chart, inventory, warehouse, merchant, pos, 购物, 商店, 店铺, 电商, 零售, 商城, 订单, 购物车, 购物篮, 外卖, 配送, 快递, 物流, 优惠券, 折扣, 礼品, 奖励, 支付, 钱包, 银行, 现金, 账单, 收据, 发票, 记账, 理财, 预算, 统计, 图表, 库存, 仓库, 商家, 收银, 活泼, 醒目
tile_color: "#F5F5F5"
summary: 明快的中高饱和实色块 + 纯黑实心部件撞色，无描边无光影，略带手工剪纸感的圆胖轮廓，醒目活泼的商业感。
---

# 墨块撞色 `ink-block`

> 参考：`reference.png`（饼图 / 银行 / 礼盒 / 店铺 / 购物篮 / 收据对勾 / 仓库方块 / 快递箱 / 钱包 / 优惠券 % / 叠放钞票 / 外卖踏板车）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 主色每个图标**只取 1 种**：橘橙 `#DC6A37`、宝蓝 `#457EDD`、豆绿 `#72B96C`、芥黄 `#E9BB3F`、豆沙粉 `#DF8D88`；部件与符号为纯黑 `#000000`；背景浅灰 `#F5F5F5`。即「1 个彩色 + 黑」 |
| 材质 | 纯平面实色块，像彩色卡纸剪贴；无纹理、无渐变、无高光 |
| 光影 | 完全无光影、无投影；黑色块本身承担「暗部/结构」的视觉重量 |
| 构图 | 单主体居中、端正，占画布约 55%，外轮廓饱满紧凑、接近方形体量；部分黑色部件可伸出主体轮廓（饼图缺口、钞票后层、车座方块） |
| 造型 | 圆胖的软几何：大圆角，边缘**略带轻微的手工不规则感**（微微鼓起、不完全平直）；**签名特征：彩色主体 + 纯黑实心部件**——黑色作为物体的真实组成部分（屋顶、提手、柱子、扇区、轮子、扣带、后层钞票），而不是描边 |
| 线条 | 无描边；黑色线状部件为粗短的圆头实心条，约图标宽度 8–10% |
| 细节 | 内部符号为黑色实心粗形（对勾、%、三条竖短线、小方块）；细节少而大，1–3 处，可读性极强 |
| 情绪 | 醒目、活泼、直接、有亲和力 |

## 可变元素

- 主体物体，以及哪些部件用黑色表达
- 主色（色板 5 选 1，成套时轮换）
- 黑色符号的内容与数量（1–3）
- 黑色部件是否伸出主体轮廓

## 固定风格（style）

```style
Rendered as a bold flat 2D vector icon made of solid color blocks, with no outlines at all. Each icon uses exactly one bright medium-saturation main color plus pure black (#000000): the main color is chosen from this palette only: burnt orange (#DC6A37), royal blue (#457EDD), leaf green (#72B96C), mustard yellow (#E9BB3F) or dusty rose pink (#DF8D88). The subject is a chunky, plump silhouette with large rounded corners and slightly soft, hand-cut, gently bulging edges, like shapes cut from colored paper. Key parts of the object are drawn as solid pure black shapes that are real components of the object, such as a roof, handle, pillars, a pie slice, wheels, a strap or a back layer, not as outlines; black parts may extend slightly outside the colored body. Inner symbols are thick solid black shapes such as a check mark, a percent sign, short rounded bars or small squares, at most three simple details, large and highly legible. Black bar-like parts are thick with rounded ends, about 9% of the icon width. Flat solid fills only: no stroke, no gradients, no lighting, no highlights, no texture, no shadow, no white details. Subject centered and upright, occupying about 55% of the canvas, compact near-square mass, generous empty space around it. Clean vector edges, consistent with a matched icon set.
```

## 负向约束（negative）

```negative
outline, stroke, black outline around the shape, line icon, thin lines, hairline, gradient, glossy, 3D, realistic, photo, texture, noise, grain, drop shadow, cast shadow, highlight, glow, white symbols, white knockout, negative space cutout, gray, dark muted colors, neon, pastel tints, multiple main colors in one icon, rainbow, sharp corners, perspective, isometric, cute face, eyes, mouth, small intricate details, text, letters, watermark, multiple subjects, busy background, pattern background
```

## 验收清单

- [ ] 每个图标只有 1 种主色 + 纯黑
- [ ] 黑色是实心部件/符号，不是描边
- [ ] 完全无描边、无渐变、无光影、无白色符号
- [ ] 造型圆胖、大圆角，边缘略带手工感
- [ ] 细节粗大、不超过 3 处

---
id: real-morph
name: 实物塑形
references: reference.png
keywords: focus, timer, reminder, todo, habit, fruit, food, recipe, cooking, diet, nutrition, fitness, health, garden, plant, nature, coffee, tea, egg, cookie, 专注, 计时, 提醒, 待办, 习惯, 水果, 食物, 美食, 菜谱, 做饭, 饮食, 营养, 减脂, 健康, 园艺, 植物, 自然, 咖啡, 茶, 鸡蛋, 饼干
ip_terms: tomato, calyx, sepal, sepals, pomodoro, remindersplus, 番茄
label_style:
default_shape: squircle
summary: 真实物体本身被塑形成饱满圆角方块并铺满画布，超写实表皮与固有色，只保留一个最具辨识度的局部特征，左上柔和大高光。
---

# 实物塑形 `real-morph`

> 参考：`reference.png`。参考图只用于提炼设计语言，它的主体（番茄 + 星形萼片）属于参考 IP，见「参考 IP 排除」。

## 设计 DNA（可复用）

| 维度 | 规范 |
|---|---|
| 配色 | **由物体固有色决定**，饱和写实；全图最多「1 主色 + 1 特征色」两种色相，主色占 85% 以上；高光为主色提亮的近白 |
| 造型语言 | 物体整体被塑形为**饱满鼓起的圆角方块**，四边微外凸、四角大圆角，像在图标模具里长成；不是方块上贴图 |
| 材质 | 超写实：真实表皮纹理（毛孔、颗粒、纤维、叶脉、釉面、木纹……随物体），轻微自然光泽 |
| 光影 | 左上柔和主光；左上棱边 2–3 块柔和大高光；右下渐暗形成体积；特征部件投下柔和接触阴影 |
| 构图原则 | 正视略俯视；方块主体铺满画布；**只保留一个**识别特征；特征位置见「版式变体」 |
| 质感 | 照片级产品 / 食物摄影，干净无瑕 |
| 细节密度 | 1 处特征部件，其余为大面积纯净表皮；无文字、无表情、无附加符号 |
| 情绪 | 直观、新鲜、饱满、有趣 |

**签名手法**：① 实物本身被塑形为饱满圆角方块并铺满画布；② 超写实表皮 + 左上柔和大高光；③ 只保留一个局部特征就能认出物体。

## 参考 IP 排除

- 原主体：番茄及其绿色星形萼片、果柄。
- 原布局：萼片在上部中央展开约 65% 宽并压出顶边。
- 品牌：RemindersPlus。

## 主体转译规则

选一个**有鲜明固有色、靠一个局部特征就能认出**的实物（**不得使用番茄**；番茄钟 / 专注类项目改用沙漏木框、柠檬、橙子、咖啡豆、计时用的厨房蛋等）：

| 隐喻 | 主体（塑形为方块） | 特征部件 | 推荐版式 |
|---|---|---|---|
| 健康 / 饮食 | 青苹果 | 果柄 + 一片叶 | `top-feature` |
| 咖啡 | 咖啡豆棕色表皮 | 中央 S 形沟槽 | `inset-feature` |
| 柠檬水 / 清爽 / 专注 | 柠檬黄果皮 | 顶端小凸起 + 一片叶 | `corner-feature` |
| 鸡蛋 / 早餐 | 白色蛋壳 | 一道裂纹露出蛋黄 | `inset-feature` |
| 植物 / 园艺 | 陶土花盆 | 盆口一株嫩芽 | `top-feature` |
| 阅读 / 学习 | 皮革书脊 | 一枚烫金书签带 | `corner-feature` |
| 烘焙 | 曲奇饼 | 一颗巧克力豆 | `inset-feature` |

主体描述可直接写物体固有色（如 `apple green`），这是本风格对「色板」规则的例外，但仍须满足「1 主色 + 1 特征色」。

## 版式变体

```composition:top-feature
Straight-on front view with a slight top-down tilt. The squircle-shaped object fills the whole canvas, its edges nearly touching all four canvas borders. One single identifying feature sits at the top center, compact, about 35–45% of the canvas width, rising slightly above the top edge. The rest of the body is a large clean uninterrupted surface. No background visible except at the very corners.
```

```composition:corner-feature
Straight-on front view with a slight top-down tilt. The squircle-shaped object fills the whole canvas, its edges nearly touching all four canvas borders. One single identifying feature sits on the upper-right shoulder, about 30–40% of the canvas width, tilted outward. The rest of the body is a large clean uninterrupted surface catching the upper-left highlights. No background visible except at the very corners.
```

```composition:inset-feature
Straight-on front view with a slight top-down tilt. The squircle-shaped object fills the whole canvas, its edges nearly touching all four canvas borders. One single identifying feature is part of the surface itself, such as a groove, crack, seam or embedded piece, placed at the center of the face and spanning about 40–55% of the canvas width. Nothing protrudes beyond the silhouette. No background visible except at the very corners.
```

## 可变元素

- 物体种类及其固有色（1 主色 + 1 特征色）
- 特征部件的形态与版式位置
- 表皮纹理细节（随物体真实材质）

## 风格约束（style）

```style
Hyper-realistic 3D render of a real object whose whole body has been sculpted into the shape of a plump iOS app icon: a full rounded square (squircle) with very large rounded corners and gently bulging sides, as if the object grew inside an app icon mold. The object itself is the icon shape, not a picture placed on a tile. True-to-life surface material with fine natural texture appropriate to the object, such as pores, grain, fibers, veins or glaze, and a subtle natural sheen. Rich saturated natural colors: one dominant body color covering more than 85% of the image plus one contrasting color for the single identifying feature. Soft studio key light from the upper left: two or three broad soft highlights along the upper-left edges and shoulders, the body gradually darkening toward the lower-right edge for strong volume, and a soft contact shadow under the identifying feature. Clean, flawless, fresh, like premium food or product photography. No face, no text, no added symbols.
```

## 负面约束（negative）

```negative
round natural shape, irregular organic silhouette, object placed on a tile, icon background behind the object, flat vector illustration, cartoon, clay, plastic toy look, cel shading, outline, face, eyes, smile, mascot, text, labels, stickers, multiple objects, sliced or cut open, rotten, bruises, spots, dirt, water droplets everywhere, harsh specular glare, dark moody lighting, black background, strong perspective, more than two hues
```

## 参考 IP 排除（avoid）

```avoid
tomato, red tomato skin, green star-shaped calyx, six slender green sepals spreading across the top, RemindersPlus icon
```

## 验收清单

- [ ] 物体本身被塑形为饱满圆角方块并铺满画布，不是贴在底板上
- [ ] 超写实表皮纹理，左上柔和大高光、右下渐暗
- [ ] 只有 1 个主色 + 1 个特征色，唯一特征位置符合所选版式
- [ ] 无表情、无文字、无多余物体
- [ ] 与参考图并排对比：不是番茄，没有顶部星形绿萼片

---
id: real-morph
name: 实物塑形
references: reference.png
keywords: tomato, pomodoro, focus, timer, reminder, todo, habit, fruit, food, recipe, cooking, diet, nutrition, fitness, health, garden, plant, nature, coffee, tea, egg, cookie, 番茄, 番茄钟, 专注, 计时, 提醒, 待办, 习惯, 水果, 食物, 美食, 菜谱, 做饭, 饮食, 营养, 减脂, 健康, 园艺, 植物, 自然, 咖啡, 茶, 鸡蛋, 饼干
label_style:
default_shape: squircle
summary: 一个真实物体被「捏」成 iOS 圆角方块形状并铺满整个画布，物体本身就是图标外形；超写实材质与表皮纹理，固有色饱满，顶部保留最具辨识度的特征部件。
---

# 实物塑形 `real-morph`

> 参考：`reference.png`（RemindersPlus 备用图标：番茄被塑形成圆角方块，顶部保留绿色萼片与果柄）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | **由物体固有色决定**，饱和、鲜亮、写实。参考图：番茄红 `#D80801`（暗部 `#9E0804`）、萼片绿 `#558012`（暗部 `#243E02`、亮部 `#466B0C`）、高光近白偏粉 `#FDE6DC`。整体最多「1 个主色 + 1 个特征部件色」两种色相，主色占画面 85% 以上 |
| 造型 | 物体整体被塑形为**饱满鼓起的圆角方块（squircle）**，四边微微外凸、四角大圆角，像实物被装进图标模具；不是方块上贴图，而是物体本身就是方块 |
| 材质 | 超写实：真实的表皮质感（果皮细微颗粒、叶片叶脉与绒毛、果柄纤维）；表面有轻微湿润光泽 |
| 光影 | 左上方柔和主光；左上区域有 2–3 块柔和的大面积高光，沿方块左上棱边形成高光带；右下边缘逐渐变暗形成体积感；特征部件在主体上投下柔和接触阴影 |
| 构图 | 正视、轻微俯视；方块主体铺满整个画布（边缘与画布四边基本贴合）；**一个最具辨识度的特征部件**（萼片 + 果柄）位于上部中央，约占画布宽度 65%，可略微突出顶边 |
| 质感 | 照片级产品 / 食物摄影质感，干净无瑕疵、无污渍 |
| 细节 | 只保留 1 处特征部件；主体其余区域保持大面积纯净；**无文字、无表情、无附加符号** |
| 情绪 | 直观、新鲜、饱满、有趣 |

**签名特征**：① 真实物体本身被塑形成饱满的圆角方块并铺满画布；② 超写实表皮材质 + 左上柔和大高光；③ 顶部中央保留唯一一个最具辨识度的特征部件。

## 主体转译规则

选一个**有鲜明固有色、且靠一个局部特征就能认出**的实物，把它的主体塑形成圆角方块，并只保留那个特征部件：

| 隐喻 | 主体（塑形为方块） | 特征部件（上部中央） |
|---|---|---|
| 番茄钟 / 专注 | 红番茄果肉 | 绿色星形萼片 + 果柄 |
| 健康 / 饮食 | 青苹果 | 果柄 + 一片叶子 |
| 咖啡 | 咖啡豆的棕色表皮 | 豆子中央的 S 形沟槽 |
| 柠檬水 / 清爽 | 柠檬黄果皮（带毛孔纹理） | 顶端小凸起 + 一片叶 |
| 鸡蛋 / 早餐 | 白色蛋壳 | 顶部一道裂纹露出蛋黄 |
| 植物 / 园艺 | 陶土花盆 | 盆口冒出一株嫩芽 |

特征部件必须**位于上部中央**，保持与参考图一致的视觉重心。主体描述中可直接写出物体的固有色（如 `bright red`、`apple green`），这是本风格对「色板」规则的唯一例外——色板由物体决定，但仍需满足「1 主色 + 1 特征色」。

## 可变元素

- 物体种类及其固有色（1 主色 + 1 特征部件色）
- 特征部件的具体形态
- 表皮纹理细节（随物体真实材质）

## 风格约束（style）

```style
Hyper-realistic 3D render of a real natural object whose whole body has been sculpted into the shape of a plump iOS app icon: a full rounded square (squircle) with very large rounded corners and gently bulging sides, as if the object grew inside an app icon mold. The object itself is the icon shape, not a picture placed on a tile. True-to-life surface material with fine natural skin texture, tiny pores and grain, fibers and veins on any leaf or stem, and a slightly moist subtle sheen. Rich saturated natural colors: one dominant body color covering more than 85% of the image plus one contrasting color for the single identifying feature. Soft studio key light from the upper left: two or three broad soft highlights along the upper-left edges and shoulders, the body gradually darkening toward the lower-right edge for strong volume, and a soft contact shadow under the identifying feature. Clean, flawless, fresh, like premium food or product photography. No face, no text, no added symbols.
```

## 构图要求（composition）

```composition
Straight-on front view with a slight top-down tilt. The squircle-shaped object fills the whole canvas, its edges nearly touching all four canvas borders. One single identifying feature, such as a stem with leaves, sits at the top center, spreading about 65% of the canvas width and possibly overlapping the top edge slightly. The rest of the body is a large clean uninterrupted surface. No background visible except at the very corners.
```

## 负面约束（negative）

```negative
round natural shape, irregular organic silhouette, object placed on a tile, icon background behind the object, flat vector illustration, cartoon, clay, plastic toy look, cel shading, outline, face, eyes, smile, mascot, text, labels, stickers, multiple objects, sliced or cut open, rotten, bruises, spots, dirt, water droplets everywhere, harsh specular glare, dark moody lighting, black background, strong perspective, more than two hues
```

## 验收清单

- [ ] 物体本身被塑形为饱满的圆角方块并铺满画布，不是贴在底板上
- [ ] 超写实表皮纹理，左上柔和大高光、右下渐暗
- [ ] 只有 1 个主色 + 1 个特征部件色
- [ ] 唯一特征部件位于上部中央，物体一眼可认
- [ ] 无表情、无文字、无多余物体

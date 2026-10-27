---
id: buddy-tiles
name: 叠贴搭档
references: reference.png
keywords: buddy, duo, companion, multiplayer, pair, collaboration, playful, tile, cyan, 搭档, 双人, 协作, 联机, 互动, 叠贴, 活泼, 拟人卡片
subject_layout: paired
label_style:
summary: 浅青底上蓝绿两块拟人圆角厚贴片错位叠放，一大一小从左下与右下探入，夸张眼神形成互动，白色厚边与星芒短线增强玩趣。
---

# 叠贴搭档 `buddy-tiles`

> 参考：`reference.png`，裁自用户四宫格左上图（蓝色主角与绿色小搭档）。色值为近似色板；原图的圆角及外侧黑色不属于交付画布要求。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 背景浅青 `#AEF0FC`；主角亮青蓝 `#00BFEF`，内面冰蓝 `#DDF8FD`，深青眉线 `#007D9C`；小搭档酸橙绿 `#93D900`，内面淡黄绿 `#F1FFDD`；厚边与眼白近白 `#FAFEFF`；瞳孔近黑 `#161A1C`；唯一跳色为星芒黄 `#FFD000` |
| 造型 | 两个扁厚、圆角很大的卡片状角色，一大一小；外圈宽厚白边，彩色内框包住浅色面部；眼白大、瞳孔大、眉线粗，允许半眯眼与小弯嘴形成表情反差 |
| 材质 | 不透明、光滑的软塑料 / 搪胶厚贴片；面部轻微内凹，白色外沿圆润凸起；不是可读的真实屏幕 |
| 光影 | 左上柔光，白边有柔亮高光，彩色框内侧有轻微遮蔽阴影；贴片重叠处加浅软接触影，不出现长硬投影 |
| 构图 | 大角色从左下斜向探入，占宽约 70%；小角色在右下前景，占宽约 45%，遮住大角色一角；两者合成一个紧凑视觉组，边缘可裁切，眼睛留在安全区；右上保留呼吸空间 |
| 质感 | 干净平滑的 2.5D 卡通渲染，无颗粒、织物、金属或透明玻璃质感 |
| 细节 | 右上 1 枚白厚边四角星芒，周围最多 6 个白色圆头短线 / 圆点；角色内部最多 1 个无文字胶囊标记；不画菜单、按钮文字或状态栏 |
| 情绪 | 机灵、活泼、亲近、互动 |

**签名特征**：① 蓝绿拟人厚贴片 + 宽白色软边；② 左下大角色与右下小搭档错位遮挡；③ 有反差的眼神与右上黄色星芒。

## 主体转译规则

把项目核心能力转成一对有关系的圆角贴片，例如学习卡与复习卡、消息与回复、主任务与完成标记。两者是一个「搭档」标志，不画成两个独立图标。

- 主角保留更大、较松弛的半眯眼，小搭档保留更小、较好奇的睁眼；可轻调眉角与视线表达品牌性格。
- 物件身份靠轮廓的小变化或一个简单内嵌符号表达，避免复制真实应用界面；不要求沿用参考中的具体卡片内容。
- 固定蓝色主角、绿色搭档、左大右小的叠放骨架。业务无双人关系时，可用「能力 + 结果」组成一对。

## 可变元素

- 两个角色所代表的物件及其一个简化功能符号
- 视线、眉角、小弯嘴与轻微旋转角度
- 星芒、圆头短线与圆点在右上区域内的具体位置

## 风格约束（style）

```style
Playful 2.5D cartoon illustration of opaque rounded soft-plastic sticker forms with thick raised near-white (#FAFEFF) rims and gently recessed pale face panels. The dominant form is bright cyan (#00BFEF) with an icy blue (#DDF8FD) face and deep teal (#007D9C) expressive brows; its smaller companion is lime green (#93D900) with a pale yellow-green (#F1FFDD) face. Large near-white eyes, near-black (#161A1C) pupils, broad rounded brows and a tiny curved mouth create contrasting relaxed and curious expressions. Smooth softly beveled edges, soft upper-left lighting, gentle rim highlights and subtle contact shadows at overlaps. Pale cyan (#AEF0FC) background, one yellow (#FFD000) four-point sparkle with a thick white rim and at most six white capsule dashes or dots. Clean polished opaque surfaces, no grain. Lively, cheeky and companionable mood.
```

## 构图要求（composition）

```composition
Pale cyan background fills the canvas edge to edge. One cohesive paired emblem: a large tilted character enters from the lower left and spans about 70% of the canvas width; a smaller character spans about 45% at the lower right in front, overlapping the larger form. Peripheral body edges may be cropped by the left and bottom edges, while both sets of eyes remain within the central 80% safe area. Keep the upper-right area open for the single sparkle and its short radiating dashes. Mostly frontal view with shallow thickness, no scene or distant perspective.
```

## 负面约束（negative）

```negative
isolated non-overlapping characters, more than two characters, equally sized characters, full body limbs, realistic device interface, readable screen content, app window, thin outline, flat monochrome symbol, transparent glass, chrome, metallic finish, realistic skin, furry surface, grain, sharp corners on the characters, dark background, rainbow fill, excessive sparkles, long hard cast shadows
```

## 验收清单

- [ ] 蓝大绿小的两个角色错位叠成一个标志，右下角色在前
- [ ] 宽白色凸边、浅色内面与柔软塑料厚度清晰可见
- [ ] 眼神有互动，关键表情不被圆角遮罩裁掉
- [ ] 浅青背景，右上只有一枚黄星芒与少量白短线 / 点
- [ ] 无真实 UI、无文字，缩到 60px 仍能看清主次

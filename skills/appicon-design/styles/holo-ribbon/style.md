---
id: holo-ribbon
name: 虹彩带标
references: reference.png
keywords: holographic, ribbon, monogram, iridescent, dark, grid, cyan, browser, developer, 虹彩, 丝带, 单字母, 字标, 暗色, 网格, 科技, 浏览器, 开发工具
lettering: required
label_style: one custom curved ribbon monogram with a broad cyan face, shallow iridescent beveled edges and a large open counter; preserve the exact case of the supplied letter
summary: 炭黑细网格底上单个连续带状字母，亮青到冰蓝的宽正面配薄虹彩倒角，深色内侧与细白高光形成浅立体折带感，整体克制而有科技感。
---

# 虹彩带标 `holo-ribbon`

> 参考：`reference.png`，裁自用户四宫格右下图（带状小写 e）。色值为近似色板；暗色圆角底板的外圈是展示效果，方形交付时不烘焙外框或圆角。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 背景炭黑 `#232323`，网格深灰 `#343434`；带面亮青 `#00C8EE` 至冰蓝 `#A4EDFF`；高光近白 `#F3FFFA`；薄边局部出现淡紫 `#BFA5FF`、薄荷 `#C8FFD6`、浅黄 `#FFF5B4`，虹彩只占少量面积 |
| 造型 | 一个可读的单字母标，笔画像连续宽带折弯，形成大字怀与清晰开口；带面宽度稳定，允许一处交叠或斜切穿插；最多一枚内嵌胶囊短笔画，须服务字形 |
| 材质 | 光滑的全息镀膜带材 / 浅挤出亚克力标志；大正面以青蓝为主，虹彩集中在窄倒角与折面，不是整块彩虹液态铬 |
| 光影 | 左上柔光；上缘细白亮线、下右边缘深灰蓝暗边；内侧有短接触影，微弱彩色反射；不用强烈外发光 |
| 构图 | 字标居中，占宽约 63–70%、高约 70%；正面视角带浅厚度，字怀露出暗网格底；网格低对比、间距约画布 15%，始终退后 |
| 质感 | 利落、平滑、精密，窄边有少量色散；底板哑光，网格无噪点；展示模式可见浅深灰倒角外缘，生产方图不加外框 |
| 细节 | 单个字母是唯一识别内容；不额外添加眼睛、笑脸、品牌全称或小标语；参考中顶部胶囊属于抽象字形细节，不作为全风格固定装饰 |
| 情绪 | 清爽、精密、未来、克制 |

**签名特征**：① 单个连续宽带字标与大负形；② 青蓝正面 + 窄边局部虹彩；③ 炭黑低对比网格底与浅立体亮边。

## 主体转译规则

取品牌一个核心拉丁字母，通过 `--label` 传入（大小写按品牌），不拼成单词或多字母块。先保住可读轮廓，再把笔画连成一条宽带：例如 C 保留大开口，S 用上下两段弧带，A 保留三角字怀与一处横向穿插。

- 优先选择靠弧线与负形就能识别的字母；笔画繁密时先简化，不强行复刻小写 e 的具体交叠。
- 主体描述只写字母、带状路径、字怀与交叠位置。材质、虹彩及暗网格由风格块提供。
- 参考 e 顶部的小胶囊仅在复现参考时使用，换字母不添加无意义点缀。本风格与 `pop-letter` / `jelly-letter` 的 2–4 字母拼块不同。

## 可变元素

- 一个拉丁字母及其大小写
- 保持可读性的带状路径、开口、内嵌短笔画和一处穿插位置
- 色板内窄边虹彩的位置与细微比例，主正面始终青蓝

## 风格约束（style）

```style
Precise futuristic single-monogram render built from a continuous broad curved ribbon with stable stroke width, a large readable counter and at most one clean overlap. The broad front face transitions smoothly from vivid cyan (#00C8EE) to icy blue (#A4EDFF). Shallow extrusion and narrow beveled edges carry restrained holographic film reflections in pale lavender (#BFA5FF), mint (#C8FFD6) and pale yellow (#FFF5B4); these accents stay on thin rims and folded side faces rather than covering the main face. Soft upper-left illumination creates a fine near-white (#F3FFFA) upper rim highlight, a dark blue-gray lower-right edge and short inner contact shadows. Smooth polished coated material, crisp edges, no texture or grain, no strong outer glow. Matte charcoal (#232323) background with a very low-contrast dark-gray (#343434) square grid. Cool, precise, clean and quietly futuristic mood.
```

## 构图要求（composition）

```composition
Matte charcoal background fills the canvas edge to edge. A faint evenly spaced square grid sits behind the mark, with cells about 15% of the canvas width. Center one complete readable ribbon monogram, about 63–70% of the canvas width and roughly 70% of its height. Mostly frontal view with shallow visible extrusion; retain a large open counter and clean separation between strokes so the dark grid remains visible through the negative space. Keep all lettering within the central 80% safe area. No outer frame baked into the artwork and no secondary emblems.
```

## 负面约束（negative）

```negative
multiple letters, wordmark, extra caption, bubble-letter block, mascot face, separate decorative dots, bright background, white background, high-contrast grid, dense grid, rainbow covering the main face, liquid chrome, gold metal, thick extrusion, deep perspective, tiny counters, closed unreadable counter, thin wire lettering, fuzzy neon glow, bloom, lens flare, sparkle decorations, rough material, grain, baked-in outer bezel
```

## 验收清单

- [ ] 恰好一个字母，与 --label 的字形与大小写一致
- [ ] 宽带路径、大字怀和开口清晰，60px 下仍可读
- [ ] 青蓝为大正面，虹彩只在窄边与折面少量出现
- [ ] 细白亮边、深色内侧与浅厚度同时可见，无霓虹泛光
- [ ] 炭黑网格低对比；方形交付铺满背景、不带展示外框

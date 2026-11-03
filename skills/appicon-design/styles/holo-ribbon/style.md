---
id: holo-ribbon
name: 虹彩带标
references: reference.png
keywords: holographic, ribbon, monogram, iridescent, dark, grid, cyan, browser, developer, network, tech, 虹彩, 丝带, 单字母, 字标, 暗色, 网格, 科技, 浏览器, 开发工具, 网络
ip_terms: lowercase e, letter e
ip_labels: e
lettering: required
label_style: one custom curved ribbon monogram with a broad cyan face, shallow iridescent beveled edges and a large open counter; preserve the exact case of the supplied letter
summary: 炭黑低对比细网格底上单个连续宽带字母，亮青到冰蓝的宽正面配窄边局部虹彩，细白上亮边与深色内侧形成浅立体折带感，克制科技。
---

# 虹彩带标 `holo-ribbon`

> 参考：`reference.png`。参考图只用于提炼设计语言，它的字形（带状小写 e 与顶部小胶囊）属于参考 IP，见「参考 IP 排除」。

## 设计 DNA（可复用）

| 维度 | 规范 |
|---|---|
| 配色 | 背景炭黑 `#232323`，网格深灰 `#343434`；带面亮青 `#00C8EE` → 冰蓝 `#A4EDFF`；高光近白 `#F3FFFA`；窄边虹彩淡紫 `#BFA5FF`、薄荷 `#C8FFD6`、浅黄 `#FFF5B4`，只占少量面积 |
| 造型语言 | 单个可读字母，笔画为连续宽带折弯，带宽稳定，大字怀与清晰开口；允许一处交叠或斜切穿插 |
| 材质 | 光滑全息镀膜带材 / 浅挤出亚克力；虹彩集中在窄倒角与折面 |
| 光影 | 左上柔光；上缘细白亮线、下右深灰蓝暗边；内侧短接触影；无强外发光 |
| 构图原则 | 一个字标 + 低对比网格底；字怀露出网格；位置见「版式变体」 |
| 质感 | 利落、平滑、精密，窄边少量色散；底板哑光，网格无噪点 |
| 细节密度 | 单个字母是唯一识别内容；不加眼睛、标语、额外点缀 |
| 情绪 | 清爽、精密、未来、克制 |

**签名手法**：① 单个连续宽带字标与大负形；② 青蓝宽正面 + 窄边局部虹彩；③ 炭黑低对比网格底与浅立体亮边。

## 参考 IP 排除

- 原字形：带状小写「e」，含内部交叠与顶部一枚胶囊短笔画。
- 原布局：字标正居中约 65% 宽、正面无倾斜。

## 主体转译规则

取品牌一个核心拉丁字母，通过 `--label` 传入（大小写按品牌）。若品牌首字母正好是 `e`，改用大写 `E` 或品牌中另一个辨识度高的字母，避免复刻参考字形。

- 先保住可读轮廓，再把笔画连成一条宽带：C 保留大开口，S 用上下两段弧带，A 保留三角字怀与一处横向穿插，M 用一次连续折返。
- 主体描述只写字母、带状路径、字怀与交叠位置；不添加参考中的顶部胶囊。
- 本风格与 `pop-letter` / `jelly-letter` 的 2–4 字母拼块不同。

## 版式变体

```composition:centered
Matte charcoal background fills the canvas edge to edge. A faint evenly spaced square grid sits behind the mark, with cells about 15% of the canvas width. Center one complete readable ribbon monogram, about 62–68% of the canvas width. Mostly frontal view with shallow visible extrusion; retain a large open counter and clean separation between strokes so the dark grid remains visible through the negative space. Keep all lettering within the central 80% safe area. No outer frame and no secondary emblems.
```

```composition:tilted
Matte charcoal background fills the canvas edge to edge. A faint evenly spaced square grid sits behind the mark, with cells about 12% of the canvas width. One complete readable ribbon monogram, about 66% of the canvas width, is rotated about 12 degrees counterclockwise and turned slightly in depth so one side of the ribbon shows more of its iridescent edge. Retain a large open counter with the grid visible through it. Keep all lettering within the central 80% safe area. No outer frame and no secondary emblems.
```

```composition:runoff
Matte charcoal background fills the canvas edge to edge. A faint evenly spaced square grid sits behind the mark, with cells about 15% of the canvas width. One large ribbon monogram, about 75% of the canvas width, sits slightly left of center; one stroke of the ribbon continues past its letterform and runs off the right edge of the canvas as a single straight band, while the readable letter itself stays within the central safe area. No outer frame and no secondary emblems.
```

## 可变元素

- 一个拉丁字母及其大小写
- 带状路径、开口、一处穿插位置
- 版式（居中 / 倾斜 / 延伸出画）与窄边虹彩的位置

## 风格约束（style）

```style
Precise futuristic single-monogram render built from a continuous broad curved ribbon with stable stroke width, a large readable counter and at most one clean overlap. The broad front face transitions smoothly from vivid cyan (#00C8EE) to icy blue (#A4EDFF). Shallow extrusion and narrow beveled edges carry restrained holographic film reflections in pale lavender (#BFA5FF), mint (#C8FFD6) and pale yellow (#FFF5B4); these accents stay on thin rims and folded side faces rather than covering the main face. Soft upper-left illumination creates a fine near-white (#F3FFFA) upper rim highlight, a dark blue-gray lower-right edge and short inner contact shadows. Smooth polished coated material, crisp edges, no texture or grain, no strong outer glow. Matte charcoal (#232323) background with a very low-contrast dark-gray (#343434) square grid. Cool, precise, clean and quietly futuristic mood.
```

## 负面约束（negative）

```negative
multiple letters, wordmark, extra caption, bubble-letter block, mascot face, separate decorative dots, bright background, white background, high-contrast grid, dense grid, rainbow covering the main face, liquid chrome, gold metal, thick extrusion, deep perspective, tiny counters, closed unreadable counter, thin wire lettering, fuzzy neon glow, bloom, lens flare, sparkle decorations, rough material, grain, baked-in outer bezel
```

## 参考 IP 排除（avoid）

```avoid
ribbon lowercase e monogram, small capsule stroke floating at the top of the letter
```

## 验收清单

- [ ] 恰好一个字母，与 `--label` 的字形与大小写一致
- [ ] 宽带路径、大字怀和开口清晰，60px 下仍可读
- [ ] 青蓝为大正面，虹彩只在窄边与折面少量出现
- [ ] 炭黑网格低对比；版式符合所选变体，不带展示外框
- [ ] 与参考图并排对比：不是带状小写 e，无顶部胶囊

---
id: retro-stripe
name: 复古彩条
references: reference.png
keywords: camera, photo, film, vintage, retro, nostalgia, music, audio, radio, recorder, cassette, video, timer, clock, calculator, game, toy, lifestyle, 相机, 拍照, 照片, 胶片, 复古, 怀旧, 音乐, 音频, 收音机, 录音, 磁带, 视频, 计时, 时钟, 计算器, 游戏, 玩具, 生活
label_style: bold italic chunky retro display lettering in signal red, slightly slanted upward, printed flat on the cream plastic
summary: 米白磨砂塑料的 70 年代消费电子正面铺满画布，黑色大镜头式焦点 + 左下扫向右下的黄橙红蓝复古彩条，柔和棚拍光与细微印刷颗粒。
---

# 复古彩条 `retro-stripe`

> 参考：`reference.png`（复古一次性相机「SNAP 400」正面）。

## 视觉特征

| 维度 | 规范 |
|---|---|
| 配色 | 机身米白 `#ECDCC5`；彩条从上到下：芥末黄 `#F2BD4B`、橙 `#E97134`、信号红 `#CF312B`、钴蓝 `#15377F`（钴蓝为最底部大色块）；按钮红 `#D9392F`；焦点部件近黑 `#111111`；金属 / 玻璃部件为中性银灰 |
| 造型 | 实物正面，体块敦厚、大圆角；零件为简洁几何（大圆、圆角方、胶囊）；比例夸张：焦点部件约占画布宽度 40% |
| 材质 | 米白磨砂 ABS 塑料；焦点为多层黑色镜筒 + 带紫/琥珀镀膜反光的玻璃；局部有透明棱纹塑料、哑光金属 |
| 光影 | 左上方柔和棚拍光；零件凸起处有细腻倒角高光与 AO；无硬投影；玻璃有真实反射 |
| 构图 | **物体正面铺满整个画布**（不是放在底板上）；正视无透视；焦点大圆部件居中略偏下；顶部一排小部件；左上角一个红色圆按钮；右侧一个小圆形计数 / 指示部件；彩条从左边缘中部扫向右下并覆盖底部 |
| 质感 | 轻微印刷颗粒与纸感噪点，彩条像丝印涂装；整体干净，不脏旧 |
| 细节 | 小部件 3–5 个；可有极少量印刷式装饰短线；**默认无文字**，品牌字样需显式 `--label` |
| 情绪 | 复古、温暖、怀旧、玩趣 |

**签名特征**：① 米白塑料正面铺满画布；② 左下→右下扫过的「黄–橙–红–钴蓝」彩条；③ 近黑大圆形焦点部件 + 左上红色圆按钮。

## 主体转译规则

把项目隐喻转译为**一件 70–80 年代米白塑料消费电子 / 日用器物的正面**（相机、录音机、收音机、计时器、计算器、游戏机、电话、台灯……），保持固定骨架：

- 中下：一个大号近黑圆形焦点部件（镜头、喇叭、表盘、转盘、旋钮），承载项目核心隐喻；
- 顶部：一排 1–2 个小窗口 / 按键；
- 左上：红色圆按钮；右侧：一个小圆形指示部件；
- 彩条：从左边缘扫向右下并铺满底部。

隐喻本身不是实物（如「社交」「AI」）时，把符号做成焦点圆形部件里的浮雕或屏幕图案。

## 可变元素

- 器物类型与外形细节
- 焦点部件的具体内容（镜头 / 喇叭网 / 表盘刻度 / 浮雕符号）
- 顶部小部件与右侧指示部件的具体形态
- 是否出现品牌字样（仅 `--label`）

## 风格约束（style）

```style
Retro 1970s consumer-electronics product render, skeuomorphic and slightly stylized, like a premium vintage gadget photographed in a studio. The body is matte cream (#ECDCC5) ABS plastic with large soft rounded corners, chunky proportions and subtle molded bevels. A bold retro rainbow livery of four smooth parallel bands, mustard yellow (#F2BD4B), orange (#E97134), signal red (#CF312B) and deep cobalt blue (#15377F), is painted on the body as flat screen-printed graphics, sweeping in a gentle wave. Functional parts are simple geometric forms: the main circular part is a recessed near-black (#111111) element built from several concentric rings, and any glass on it shows purple and amber coating reflections; a round glossy signal-red (#D9392F) push button, small windows with ribbed clear plastic, satin silver-gray metal trims. Soft diffused studio key light from the upper left, delicate bevel highlights and ambient occlusion around raised parts, realistic glass reflections, no harsh shadows. Fine print grain and a faint paper-like noise on the plastic and stripes, clean and not dirty or scratched. Palette strictly limited to cream, mustard yellow, orange, signal red, cobalt blue, near-black and neutral silver-gray. Warm, nostalgic, playful mood.
```

## 构图要求（composition）

```composition
Strict front orthographic view with no perspective. The front face of the object fills the entire canvas edge to edge, so the cream body itself is the icon background. One large near-black circular focal part sits at the center, slightly below middle, about 40% of the canvas width, with a thick cream raised bezel. A row of one or two small components runs along the top, a round red button sits at the top left, and one small round indicator sits on the right side. The rainbow bands enter from the middle of the left edge and sweep down to the right, passing behind the focal part and covering the bottom edge, with the cobalt blue band as the largest area at the very bottom.
```

## 负面约束（negative）

```negative
perspective view, three-quarter angle, isometric, side view, object floating on a separate background, white margin around the object, flat vector illustration, cartoon outline, cel shading, neon colors, pastel colors, green, purple body, pink, gradient mesh background, chrome-heavy body, dirty, rust, heavy scratches, glitter, harsh drop shadow, multiple focal circles of equal size, stripes in wrong order, more than four stripe colors, cluttered tiny buttons, photo of a real branded camera
```

## 验收清单

- [ ] 米白塑料正面铺满画布，正视无透视
- [ ] 黄–橙–红–钴蓝四色彩条顺序正确，从左扫向右下、钴蓝在最底
- [ ] 一个近黑大圆焦点部件居中偏下，左上有红色圆按钮
- [ ] 柔和左上光、细腻倒角高光与印刷颗粒，无硬投影
- [ ] 无多余文字 / 乱码

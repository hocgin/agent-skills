# 六种参考图风格

从同一张六屏拼图分别提取。编号按先上后下、从左到右；它们是六个独立 Style Profile，不是一个产品的六页引导。此处只创建风格库，不虚构产品 Flow。

原图：[onboarding-six-styles.png](images/onboarding-six-styles.png)。外侧灰色 `#D1D1D1` 为展示底，不属于任何 App。色值来自 RGB 局部中位数或明确的重建选择；采样区域、来源 SHA-256 和规范化说明保存在各 Profile 中。字体、圆角、渐变 stop 与动效均为重建规范，不宣称识别到原设计参数。

| 位置 | 名称 / style_id | 背景 | 图案与前景 |
| --- | --- | --- | --- |
| 左上 | [薄荷叠片](../styles/mint-photo-stack-v1.json) · `mint-photo-stack-v1` | `#F4F9EE` | 背景只有上浅薄荷、下纯白的轻柔纵向过渡，没有重复纹样；三张白边相片叠放属于独立前景。 |
| 上中 | [晴空奶油](../styles/sky-cream-dissolve-v1.json) · `sky-cream-dissolve-v1` | `#F5F0E8` | 上方是实景蓝天与不规则云团，靠近画布高度 58%～70% 通过奶油色雾化遮罩接到底部纯色；不是整屏蓝白渐变。 |
| 右上 | [瓷白彩格](../styles/porcelain-pastel-grid-v1.json) · `porcelain-pastel-grid-v1` | `#F4F5F7` | 整屏为近瓷白实色，无背景纹样；白色圆角展示框内有 3×3 彩色方格，方格属于前景内容容器。 |
| 左下 | [薄荷悬浮](../styles/mint-photo-orbit-v1.json) · `mint-photo-orbit-v1` | `#F3F7ED` | 背景同属浅薄荷到白的无纹理家族；区别在于中央一张大相片配周围三个悬浮缩略片，背景本身无图案。 |
| 下中 | [炭黑荧光地图](../styles/charcoal-lime-map-v1.json) · `charcoal-lime-map-v1` | `#151512` | 背景为极深橄榄黑向炭黑的轻微纵向变化；地图路网、头像与路线仅在上半部圆角面板内，不能铺进正文。 |
| 右下 | [电影感青蓝摄影](../styles/cinematic-teal-photo-v1.json) · `cinematic-teal-photo-v1` | `#2D4959` | 真实街景摄影铺满全屏，上部灰蓝天空与暖色建筑，下部深青蓝道路；照片本身承载纹理，另用深色可控遮罩保护文字。 |

## 复用

命名风格使用完整 JSON；精确 style_id 对应本 Skill 的 `styles/` 目录。内置规范只读，用户要改 token 时派生新 ID 并存入项目 `.onboarding-design/styles/`。

```bash
# 在仓库根目录运行；跨项目时将 store 改为本 Skill 的绝对目录
python3 skills/onboarding-design/scripts/onboarding.py load-profile \
  --style-id mint-photo-stack-v1 --store skills/onboarding-design/styles
```

自然语言示例：`用 onboarding-design 的「薄荷叠片」mint-photo-stack-v1，为我的实际产品设计 3 页引导；先读取完整 Profile，再填产品 Flow。`


## 1. 薄荷叠片 · 左上

`background: #F4F9EE` / `surface: #FFFFFF` / `primary: #232323` / `text_primary: #171917` / `text_secondary: #4D514D` / `on_primary: #FFFFFF` / `accent: #EAB85C`

**背景**：背景只有上浅薄荷、下纯白的轻柔纵向过渡，没有重复纹样；三张白边相片叠放属于独立前景。

**图形语法**：三层相片卡片：后两张分别旋转 −14° / +11°，前片正置；使用白边、轻阴影和一个小圆贴章。

**底色/摄影提示词**：竖向浅薄荷 #F4F9EE 到纯白 #FFFFFF，stop 0/0.45/0.68/1 对应 #F4F9EE/#FAFCF7/#FFFFFF/#FFFFFF；无纹理、无具象背景、无光斑。

**排版与交互**：标题用衬线类别，拉丁文可选系统 New York，中文用可用宋体回退；正文系统无衬线，字体为实现选择。primary 实色胶囊，on_primary 字；高 52 pt，可随大字号增高；点击目标至少 44 pt。

**避免漂移**：禁止将相片内容烘焙进底色；禁止满屏散片、纸张撕边、颗粒噪点和厚重投影。


## 2. 晴空奶油 · 上中

`background: #F5F0E8` / `surface: #FFFFFF` / `primary: #1B381A` / `text_primary: #181C17` / `text_secondary: #50574E` / `on_primary: #FFFFFF` / `sky: #90B4DA` / `cloud: #F7F6F0`

**背景**：上方是实景蓝天与不规则云团，靠近画布高度 58%～70% 通过奶油色雾化遮罩接到底部纯色；不是整屏蓝白渐变。

**图形语法**：一幅有纵深的自然日光摄影，上半部保留大块天空，中下部主体在雾化边缘前；云团来自摄影，不平铺矢量云。

**底色/摄影提示词**：底色 #F5F0E8；上部蓝天 #90B4DA 与柔白云 #F7F6F0 的真实日光照片，照片下缘用 #F5F0E8 遮罩在全屏 y=0.58/0.64/0.70 的 alpha 0/0.65/1 平滑覆盖。文案区为不透明奶油底。

**排版与交互**：标题用衬线类别，拉丁文可选系统 New York，中文用可用宋体回退；正文系统无衬线，字体为实现选择。primary 实色胶囊，on_primary 字；高 52 pt，可随大字号增高；点击目标至少 44 pt。

**避免漂移**：禁止云朵贴纸、重复云纹、蓝色覆盖正文区、硬切照片边界，以及把原咖啡店当成所有产品的固定主体。


## 3. 瓷白彩格 · 右上

`background: #F4F5F7` / `surface: #FFFFFF` / `primary: #272525` / `text_primary: #181A1C` / `text_secondary: #50555C` / `on_primary: #FFFFFF` / `tile_yellow: #EFC551` / `tile_blush: #EEB8AE` / `tile_coral: #E48865` / `tile_aqua: #BFE5E8` / `tile_sand: #C7BDB2`

**背景**：整屏为近瓷白实色，无背景纹样；白色圆角展示框内有 3×3 彩色方格，方格属于前景内容容器。

**图形语法**：白色圆角框内的三列彩色方格，每格一个独立剪影或产品对象，色彩按已登记色板交替，不把网格平铺成墙纸。

**底色/摄影提示词**：整屏纯色 #F4F5F7，无渐变、无纹理；如需完整 UI，另加白色圆角展示框，框内三列粉彩方格依次取 #EFC551/#EEB8AE/#E48865/#BFE5E8/#C7BDB2。纯背景输出不得包含方格。

**排版与交互**：标题和正文均用系统无衬线；标题 medium/semibold，正文 regular；不声称识别到截图精确字体。primary 实色胶囊，on_primary 字；高 52 pt，可随大字号增高；点击目标至少 44 pt。

**避免漂移**：禁止整屏彩格墙纸、各格随机新增饱和色、彩色正文、将餐盘作为通用固定元素、强 3D 玻璃或金属。


## 4. 薄荷悬浮 · 左下

`background: #F3F7ED` / `surface: #FFFFFF` / `primary: #232323` / `text_primary: #171917` / `text_secondary: #4D514D` / `on_primary: #FFFFFF` / `accent: #EAB85C`

**背景**：背景同属浅薄荷到白的无纹理家族；区别在于中央一张大相片配周围三个悬浮缩略片，背景本身无图案。

**图形语法**：一张正置竖向主相片，外围最多三张小缩略片，分别在上方、左下、右下；只允许一张小片轻旋，不形成堆叠扇形。

**底色/摄影提示词**：竖向浅薄荷 #F3F7ED 到纯白 #FFFFFF，stop 0/0.45/0.70/1 对应 #F3F7ED/#FAFCF7/#FFFFFF/#FFFFFF；干净空白，无纹样。悬浮相片是后续独立前景，不画进纯背景。

**排版与交互**：标题用衬线类别，拉丁文可选系统 New York，中文用可用宋体回退；正文系统无衬线，字体为实现选择。primary 实色胶囊，on_primary 字；高 52 pt，可随大字号增高；点击目标至少 44 pt。

**避免漂移**：禁止三张同等大相片扇形重叠、满屏碎片、持续漂浮干扰阅读、彩色光晕和复杂背景纹样。


## 5. 炭黑荧光地图 · 下中

`background: #151512` / `surface: #34342F` / `primary: #F3F774` / `text_primary: #FFFFFF` / `text_secondary: #CBCDC4` / `on_primary: #151512` / `top_olive: #1D1D17` / `road: #5D5F56` / `route: #E9EF62`

**背景**：背景为极深橄榄黑向炭黑的轻微纵向变化；地图路网、头像与路线仅在上半部圆角面板内，不能铺进正文。

**图形语法**：深灰圆角面板内是斜向不规则路网、一条柠檬黄折线路径、少量圆形节点；原图头像可转译为与产品有关的圆形内容节点。

**底色/摄影提示词**：纵向底色 stop 0/0.55/1 对应 #1D1D17/#151512/#151512，无噪点。若需完整构图，独立加入 #34342F 圆角地图面板、#5D5F56 稀疏不规则路网、单条 #E9EF62 折线路径；纯背景不包含地图。

**排版与交互**：标题和正文均用系统无衬线；标题 semibold，正文 regular；按钮 semibold。primary 实色胶囊，on_primary 字；高 52 pt，可随大字号增高；点击目标至少 44 pt。右侧可内嵌 36 pt 深色圆形箭头，其整体仍为同一按钮。

**避免漂移**：禁止荧光绿色泛滥、赛博霓虹辉光、等距方格代替街道路网、地图布满整屏、真实位置或人物数据的暗示。


## 6. 电影感青蓝摄影 · 右下

`background: #2D4959` / `surface: #FFFFFF` / `primary: #FFFFFF` / `text_primary: #FFFFFF` / `text_secondary: #FFFFFF` / `on_primary: #152E38` / `sky_gray: #A2A3A8` / `shade: #172D35` / `warm_accent: #BD9261`

**背景**：真实街景摄影铺满全屏，上部灰蓝天空与暖色建筑，下部深青蓝道路；照片本身承载纹理，另用深色可控遮罩保护文字。

**图形语法**：单幅纵向环境摄影，地面或路径形成纵深引导，主体中下部可有轻微运动模糊；上部为低细节文字区，底部白色胶囊悬浮。

**底色/摄影提示词**：满版真实环境摄影：上部灰蓝 #A2A3A8，中下部深青蓝 #2D4959，少量暖砂 #BD9261；路面或空间线条产生纵深。标题区域叠加 #172D35 半透明上暗下透明遮罩，底部同色渐暗；没有合适摄影时使用深青蓝实色回退。

**排版与交互**：标题和正文均用系统无衬线；标题 medium，左对齐；按钮居中。白色胶囊，on_primary 深字；高 52 pt，可随大字号增高；点击目标至少 44 pt。

**避免漂移**：禁止把灰蓝到青蓝的纯渐变冒充摄影、描摹原地标或运输品牌、文字直接压在复杂亮部、以固定透明度声称所有照片都可读。


## 验证范围

完成原图观察、局部采样、六份 Profile 的结构校验、保存/加载兼容与跨产品语义检查。结构通过不等于产品页面或设备运行通过；正文对比度、裁切、实际资源与完整流程需在具体产品适配时复核。地图可映射任务路径、彩格可映射产品内容集合、相片款可映射用户真实内容；不要求复制参考中的人物、餐盘或城市。

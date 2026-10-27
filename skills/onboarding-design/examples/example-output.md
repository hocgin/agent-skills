# 晴间 · Onboarding 设计方案

以下 JSON 为本次方案的数据源。来源与推断见 provenance/assumptions；检查证据见文末。

## A. Style Profile

```json
{
  "schema_version": 1,
  "style_id": "soft-glass-daylight-v1",
  "name": "柔光日间玻璃",
  "derived_from": null,
  "provenance": {
    "mode": "explicit-style-without-reference",
    "references": [],
    "observations": [],
    "decisions": {
      "requested_style": "glassmorphism，轻盈、清晰、自然日光",
      "priority": "显式风格优先；本例无参考图，数值均为主动设计的规范值，并非图片测量值",
      "retained": [],
      "translated": [],
      "dropped": [],
      "rationale": "以磨砂玻璃和稳定柔光建立跨产品可复用的语言，具体对象在 Flow 中定义"
    }
  },
  "design_tokens": {
    "colors": {
      "background": "#F3F7FC",
      "surface": "#FFFFFF",
      "primary": "#2456CB",
      "text_primary": "#13243A",
      "text_secondary": "#43576E",
      "on_primary": "#FFFFFF",
      "art_accent_cool": "#8DC9EB",
      "art_accent_warm": "#F4C66A",
      "usage": "冷暖辅助色仅用于主视觉；正文在不透明 background 上，CTA 用 primary/on_primary，不用浅辅助色承载小字"
    },
    "typography": {
      "family": "系统无衬线；iOS 拉丁文使用系统字体，中文使用系统中文回退，不栅格化",
      "title": {
        "size_pt": 30,
        "weight": "semibold",
        "line_height_pt": 38
      },
      "body": {
        "size_pt": 17,
        "weight": "regular",
        "line_height_pt": 26
      },
      "button": {
        "size_pt": 17,
        "weight": "semibold",
        "line_height_pt": 22
      },
      "caption": {
        "size_pt": 13,
        "weight": "medium",
        "line_height_pt": 18
      },
      "alignment": "标题、正文左对齐；按钮居中；跟随系统动态字号"
    },
    "spacing_pt": {
      "unit": 8,
      "small": 8,
      "medium": 16,
      "large": 24,
      "section": 32,
      "page_horizontal": 24
    },
    "radii_pt": {
      "card": 24,
      "button": 16
    },
    "shadows": {
      "card": {
        "color": "#13243A",
        "alpha": 0.1,
        "x_pt": 0,
        "y_pt": 8,
        "blur_pt": 24
      }
    },
    "opacity": {
      "glass_surface": 0.76,
      "glass_border": 0.7,
      "text": 1
    },
    "effects": {
      "glass_blur_pt": 18,
      "border_width_pt": 1,
      "border_color": "#FFFFFF",
      "background_gradient": "无；稳定 background 实色"
    }
  },
  "visual_language": {
    "dominant_style": "glassmorphism",
    "secondary_styles": [],
    "signature_features": [
      "薄磨砂玻璃边缘",
      "左上日光与向右下柔影",
      "大块浅色留白配不透明深色文字"
    ],
    "rendering": "柔和半写实几何，干净轮廓，无厚重轮廓线，最多三个景深层",
    "materials": "主视觉磨砂玻璃；不混入铬金属、皮革、纸噪点或黏土",
    "lighting": "固定左上 45 度宽漫射日光，低对比度，投影向右下，无第二彩色光源",
    "perspective": "正面为主的轻微三分之四视角，固定平行投影，无广角畸变",
    "mood": "清透、安静、可信赖，允许冷暖辅助色平衡，避免霓虹科技感"
  },
  "layout_rules": {
    "baseline_canvas_pt": {
      "width": 393,
      "height": 852
    },
    "safe_area": "由系统动态决定；背景可延伸全屏，文字/CTA/进度始终位于安全区内，不固定刘海或底部高度",
    "regions": "默认安全区内容高度：主视觉 50%、文案 25%、导航 17%、余量 8%；大字号时可调整而非硬裁切",
    "variants": {
      "hero-centered": "上半部主视觉居中，焦点约 x=0.50/y=0.27；下方文案左对齐，底部共享导航",
      "hero-diagonal": "上半部主体沿左下到右上节奏展开，焦点仍在 x=0.50/y=0.27 附近；文案与导航位置保持"
    },
    "responsive": "小屏或大字号缩小主视觉和间隙，必要时文案滚动且 CTA 可达；宽屏居中限制内容宽度，资源等比 fit",
    "typography": "正文最多两段；标题默认两行以内但不截断；标题与正文间距 medium，文案与导航至少 large"
  },
  "component_rules": {
    "button": "共享主按钮高 52 pt（大字号可增高）、圆角 button、primary 底/on_primary 字；禁用态有可读说明，不仅降低透明度",
    "progress": "统一步进点，按实际页数生成；活动点 primary，其他点 text_secondary；读屏为第几页/共几页，不仅依赖颜色",
    "card": "仅在主视觉中使用 glass_surface 透明度、card 圆角、白色 1 pt 细边和共享阴影；正文区域不做透明叠字",
    "navigation": "同一底部区域提供进度与一个主 CTA；继续进入下一页，最后 CTA 进入产品；跳过与末页完成目标一致，不自动申请权限"
  },
  "composition_rules": {
    "focal_point": "主体在安全区上半部，占画布宽约 65%～80%，视觉焦点稳定在 x=0.50/y=0.27 附近",
    "negative_space": "主视觉与文案间至少 24 pt 的视觉间隔；文案背景无装饰，不把装饰挤入导航区",
    "visual_weight": "一主对象或一个对象组、最多两个辅助元素；正文低于主视觉，CTA 清楚但不盖住主体",
    "allowed_variations": "可换主体、功能场景、对象数量与已批准布局变体；不变更材质、光源、镜头、文字层级和底部导航"
  },
  "motion_rules": {
    "transition": "页面 320 ms ease-in-out 淡出淡入并最多 24 pt 横向位移，可中断，不能动画排队",
    "entrance": "主视觉 280 ms ease-out，从下方 12 pt 进入并淡入；文案随后 60 ms 淡入，不持续漂浮",
    "background": "实色背景保持不变，不逐页换背景色或制造闪烁",
    "continuity": "主体锚点、光源、视角稳定；同类形状通过位置/透明度过渡，不强行做不合理物体变形",
    "reduce_motion": "取消位移、缩放和延迟，100 ms 淡入或直接替换；交互和信息保持可用"
  },
  "negative_constraints": [
    "禁止页面之间随机切换色板、字体、材质、光源或渲染技法",
    "禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突",
    "禁止不合理透视、超过三个景深层、过度装饰或无关物体",
    "禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区",
    "禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互"
  ]
}
```

## B. Onboarding Flow

1. **抬眼，就懂此刻天气** — 让用户理解一眼获取当前天气的价值；能力：当前天气。
2. **把出发时间安排好** — 让用户理解逐时变化如何帮助选择出发时间；能力：逐时预报。
3. **雨来之前，心里有数** — 说明提醒价值并让用户进入产品，权限延后申请；能力：降雨提醒。

```json
{
  "schema_version": 1,
  "style_id": "soft-glass-daylight-v1",
  "project": {
    "name": "晴间",
    "type": "天气 App",
    "features": [
      "当前天气",
      "逐时预报",
      "降雨提醒"
    ],
    "audience": "需要安排日常出行的通勤用户",
    "positioning": "以清楚、轻盈的天气信息支持出门决策；这是示例产品设定"
  },
  "platform": "iPhone；393×852 pt 为基准画布，非固定设备尺寸",
  "locale": "zh-Hans",
  "screen_count_reason": "三个已定义能力各一页，从看现在到安排出行，再到理解提醒价值",
  "assumptions": [
    "示例无上传参考图；显式指定 glassmorphism 与轻盈自然日光，所有视觉值为设计选择",
    "当前天气、逐时预报、降雨提醒均为演示产品的能力设定，不代表已连接真实天气服务",
    "引导可跳过；完成或跳过后先手动选城市，再进入首页；定位和通知权限在相应功能实际使用时解释并申请",
    "温度与时间均为示意数据；本次仅交付设计和提示词，未生成图片或运行 App"
  ],
  "screens": [
    {
      "id": "weather-now",
      "goal": "让用户理解一眼获取当前天气的价值",
      "feature": "当前天气",
      "title": "抬眼，就懂此刻天气",
      "description": "温度与天气状态清楚呈现，出门前少一点犹豫。",
      "visual_subject": "一个磨砂玻璃圆盘前方悬浮柔软云形，暖色日光圆片从右后方露出，但全场主光仍来自左上",
      "scene": "上半部集中展示当前天气的一个场景；云形用冷辅助色，日光圆片用暖辅助色；原生叠加示意 24° 与晴转多云，无城市照片、无额外卡片",
      "composition": "圆盘对象组占画布宽约 70%，焦点位于 x=0.50/y=0.27；数字低于主体中心，不与标题相撞；正文和底部导航留白",
      "layout_variant": "hero-centered",
      "token_refs": [
        "colors.background",
        "colors.primary",
        "colors.art_accent_cool",
        "colors.art_accent_warm",
        "typography.title",
        "opacity.glass_surface"
      ],
      "interaction": {
        "primary_label": "继续",
        "primary_action": "next:hourly-outlook",
        "secondary_label": "跳过",
        "secondary_action": "skip:city-picker",
        "progress": "第 1 页，共 3 页；首点活动"
      },
      "motion": "云形与圆盘按统一入口动效进入；进入第二页时保持对象组锚点，淡出圆盘并淡入时间轴；不让太阳成为第二个真实光源；Reduce Motion 只淡入",
      "implementation": {
        "code_components": [
          "背景、标题、说明、24° 与晴转多云为原生文字",
          "共享主按钮、跳过按钮、分页进度",
          "资源等比布局与页面切换"
        ],
        "assets": [
          {
            "id": "hero-weather-now",
            "description": "磨砂玻璃圆盘、云形和日光圆片的对象组；不含数字、文案、按钮或背景",
            "background": "transparent",
            "aspect_ratio": "1:1",
            "export": "PNG alpha，按最大展示约 320 pt × 3 scale 导出 960×960 px；实际设备变化时重算",
            "crop_safe_area": "主体和柔影完整留在中央 80%，四周透明留白，等比 fit"
          }
        ],
        "fallback": "没有 3D 资源时，用同色板原生圆盘与云形路径重建，不改材质语法和光源；模糊不可用时采用不透明 surface"
      }
    },
    {
      "id": "hourly-outlook",
      "goal": "让用户理解逐时变化如何帮助选择出发时间",
      "feature": "逐时预报",
      "title": "把出发时间安排好",
      "description": "沿着逐时预报，看清天气变化，选个合适的时刻出门。",
      "visual_subject": "一条由近到远缓慢抬升的磨砂玻璃弧形时间轨道，三个节点分别呈现日光、云层、细雨的天气变化",
      "scene": "轨道沿左下到右上展开，三节点同属一个对象组；原生叠加 09时、12时、15时示意标签，表达时间而非三张相同卡片",
      "composition": "轨道占画布宽约 78%，对象组焦点仍为 x=0.50/y=0.27，三个节点大小有主次；不挤入下部文案；标题和导航沿用共享网格",
      "layout_variant": "hero-diagonal",
      "token_refs": [
        "colors.background",
        "colors.primary",
        "colors.art_accent_cool",
        "colors.art_accent_warm",
        "typography.caption",
        "shadows.card"
      ],
      "interaction": {
        "primary_label": "继续",
        "primary_action": "next:rain-reminder",
        "secondary_label": "跳过",
        "secondary_action": "skip:city-picker",
        "progress": "第 2 页，共 3 页；第二点活动；允许右滑返回第 1 页"
      },
      "motion": "时间节点沿轨道按顺序出现，总入口不超过共享动效节奏；进入第三页时中间云形在相同锚点交叉淡入雨幕；不改变光源或镜头；Reduce Motion 直接显示全部节点",
      "implementation": {
        "code_components": [
          "09时、12时、15时标签与所有说明采用原生文字",
          "简单轨道可用路径，颜色与阴影来自共享 token",
          "共享导航与可返回的分页状态"
        ],
        "assets": [
          {
            "id": "hero-hourly-outlook",
            "description": "磨砂弧形时间轨道及日光、云、雨三个节点；不含标签文字，轮廓适度简化",
            "background": "transparent",
            "aspect_ratio": "1:1",
            "export": "PNG alpha，最大展示约 320 pt × 3 scale，960×960 px；与第一页统一导出比例",
            "crop_safe_area": "完整轨道、节点和柔影留在中央 80%，避免端点贴边；等比 fit"
          }
        ],
        "fallback": "轨道与节点均可用原生路径和同材质简化几何绘制；保留时间演进语义，不退化成三个无关装饰图标"
      }
    },
    {
      "id": "rain-reminder",
      "goal": "说明提醒价值并让用户进入产品，权限延后申请",
      "feature": "降雨提醒",
      "title": "雨来之前，心里有数",
      "description": "需要时开启降雨提醒，为临时变化多留一点准备。",
      "visual_subject": "一把简洁的磨砂玻璃伞位于细雨云下方，雨线在伞面两侧分开；一个小型铃铛轮廓作为提醒符号",
      "scene": "使用冷辅助色绘制雨与伞，暖辅助色只点亮铃铛符号；不出现已开启通知的成功勾选，不画系统权限弹窗；表达准备行动而非已获授权",
      "composition": "云与伞构成一个垂直对象组，约占画布宽 68%，焦点保持 x=0.50/y=0.27；铃铛为辅助元素，文案区与导航区保持无装饰",
      "layout_variant": "hero-centered",
      "token_refs": [
        "colors.background",
        "colors.primary",
        "colors.text_primary",
        "colors.art_accent_cool",
        "colors.art_accent_warm",
        "radii_pt.button"
      ],
      "interaction": {
        "primary_label": "开始使用",
        "primary_action": "complete:city-picker",
        "secondary_label": "无",
        "secondary_action": "无；允许右滑返回第 2 页",
        "progress": "第 3 页，共 3 页；第三点活动"
      },
      "motion": "云与伞同步轻微淡入，铃铛不摇晃或持续闪动；点击开始使用后按统一转场进入城市选择；Reduce Motion 直接切换，仍保留完成状态",
      "implementation": {
        "code_components": [
          "全部文案、主 CTA 和进度为原生控件",
          "保存 onboardingCompleted 后打开手动城市选择，选完进入天气首页",
          "通知权限仅在用户实际开启降雨提醒时申请"
        ],
        "assets": [
          {
            "id": "hero-rain-reminder",
            "description": "同材质雨云、伞、分开的雨线和一个小铃铛符号；无授权成功标记、文字或控件",
            "background": "transparent",
            "aspect_ratio": "1:1",
            "export": "PNG alpha，最大展示约 320 pt × 3 scale，960×960 px；与前两页统一",
            "crop_safe_area": "伞、铃铛、雨线和柔影均留在中央 80%，保护底部伞柄；等比 fit"
          }
        ],
        "fallback": "资源不可用时用统一色板的原生伞、云路径与简化雨线；不显示虚构的系统授权状态"
      }
    }
  ],
  "negative_constraints": [
    "禁止用无关音乐、机器人、聊天气泡或抽象光球替代天气功能表达",
    "禁止暗示用户已授予定位/通知权限，禁止虚构预报准确率或把演示温度声称为实况",
    "禁止三页都使用相同云朵卡片仅替换标题"
  ],
  "implementation_hints": {
    "native_ui": [
      "SwiftUI 用共享 DesignTokens、数据驱动 OnboardingScreen 和可中断分页容器；背景、真实文案、按钮、进度、时间/温度标签均由代码渲染",
      "玻璃资源已带光照，不再叠加方向冲突的阴影；代码卡片沿用 Profile 的材质与回退，不依赖特定新系统玻璃 API"
    ],
    "assets": [
      "分别导出 hero-weather-now、hero-hourly-outlook、hero-rain-reminder，背景透明、不含文字；以资源清单的比例和安全裁切区验收",
      "960×960 px 是 320 pt@3x 的示例产物；按实际最大展示大小重新核对，并提供原生路径简化回退"
    ],
    "adaptation": [
      "系统读取上下安全区，背景可出血，CTA 及文案不可；393×852 pt 是设计基准，不硬编码传感器区域高度",
      "小屏/大字号先压缩主视觉和间距，再让内容滚动且主 CTA 可达；宽屏限制内容宽度、资源等比 fit，禁止拉伸"
    ],
    "accessibility": [
      "系统动态字号、读屏页码与按钮标签；图像若仅装饰则隐藏读屏，信息由文案提供",
      "按真实合成背景核对正文对比度，交互目标至少 44×44 pt；Reduce Motion 取消位移与延迟，保留状态变化"
    ],
    "state_and_navigation": [
      "继续按 Flow 的 next 目标推进，滑动可返回；前两页跳过与最后页完成均保存完成标记并进入手动城市选择，选城后进入首页",
      "从设置可重新查看引导；重播完成回到设置，不重复触发权限弹窗；引导不承担通知权限申请"
    ]
  },
  "quality_review": {
    "scope": "plan-only",
    "checks": {
      "style_consistency": {
        "status": "pass",
        "evidence": "三页共用同一 Profile 的材质、光源、色板、字体与导航；页面未引入第二套 token",
        "fix": "无需修正"
      },
      "product_relevance": {
        "status": "pass",
        "evidence": "圆盘天气对应当前状态，时间轨道对应逐时预报，雨伞与提醒符号对应降雨提醒",
        "fix": "无需修正；产品为演示设定"
      },
      "composition_quality": {
        "status": "pass",
        "evidence": "三页锚点一致且文案区无装饰，允许居中与对角两种布局，并定义小屏/大字号规则",
        "fix": "无需修正；实际渲染待验收"
      },
      "flow_completeness": {
        "status": "pass",
        "evidence": "认识现在、安排未来、理解提醒后开始使用；下一页、跳过与最终城市选择路径明确",
        "fix": "无需修正"
      },
      "prompt_executability": {
        "status": "pass",
        "evidence": "各页定义主体、位置、准确文案、交互、动效和导出资源；由脚本注入独立风格锁及负向约束",
        "fix": "无需修正；图像模型输出仍需检查"
      },
      "reusability": {
        "status": "pass",
        "evidence": "Style Profile 无天气专属对象；音乐项目可用同一玻璃材质、左上柔光、居中焦点设计唱片播放与收藏场景，只改 Flow",
        "fix": "无需修正"
      },
      "implementability": {
        "status": "pass",
        "evidence": "三个独立透明主视觉与原生文字/控件明确分工，包含资源缺失、模糊降级及延后权限策略",
        "fix": "无需修正；原生运行与设备检查待执行"
      }
    }
  }
}
```

## C. Global Design Prompt

设计一组可实现的移动 App 首次启动引导。逐字遵守同一 STYLE_LOCK，只能在允许范围内改变产品主体、场景和布局变体，不添加另一套颜色/字体/材质/光源。主视觉解释产品能力，文案与导航保持留白和清楚层级，安全区与字号动态适配。

STYLE_LOCK_SHA256: a7c5da98e734a51c173255f5a6ec6b7e925395c0e3534e537d928b05fd3263e8
STYLE_LOCK: {"component_rules":{"button":"共享主按钮高 52 pt（大字号可增高）、圆角 button、primary 底/on_primary 字；禁用态有可读说明，不仅降低透明度","card":"仅在主视觉中使用 glass_surface 透明度、card 圆角、白色 1 pt 细边和共享阴影；正文区域不做透明叠字","navigation":"同一底部区域提供进度与一个主 CTA；继续进入下一页，最后 CTA 进入产品；跳过与末页完成目标一致，不自动申请权限","progress":"统一步进点，按实际页数生成；活动点 primary，其他点 text_secondary；读屏为第几页/共几页，不仅依赖颜色"},"composition_rules":{"allowed_variations":"可换主体、功能场景、对象数量与已批准布局变体；不变更材质、光源、镜头、文字层级和底部导航","focal_point":"主体在安全区上半部，占画布宽约 65%～80%，视觉焦点稳定在 x=0.50/y=0.27 附近","negative_space":"主视觉与文案间至少 24 pt 的视觉间隔；文案背景无装饰，不把装饰挤入导航区","visual_weight":"一主对象或一个对象组、最多两个辅助元素；正文低于主视觉，CTA 清楚但不盖住主体"},"design_tokens":{"colors":{"art_accent_cool":"#8DC9EB","art_accent_warm":"#F4C66A","background":"#F3F7FC","on_primary":"#FFFFFF","primary":"#2456CB","surface":"#FFFFFF","text_primary":"#13243A","text_secondary":"#43576E","usage":"冷暖辅助色仅用于主视觉；正文在不透明 background 上，CTA 用 primary/on_primary，不用浅辅助色承载小字"},"effects":{"background_gradient":"无；稳定 background 实色","border_color":"#FFFFFF","border_width_pt":1,"glass_blur_pt":18},"opacity":{"glass_border":0.7,"glass_surface":0.76,"text":1},"radii_pt":{"button":16,"card":24},"shadows":{"card":{"alpha":0.1,"blur_pt":24,"color":"#13243A","x_pt":0,"y_pt":8}},"spacing_pt":{"large":24,"medium":16,"page_horizontal":24,"section":32,"small":8,"unit":8},"typography":{"alignment":"标题、正文左对齐；按钮居中；跟随系统动态字号","body":{"line_height_pt":26,"size_pt":17,"weight":"regular"},"button":{"line_height_pt":22,"size_pt":17,"weight":"semibold"},"caption":{"line_height_pt":18,"size_pt":13,"weight":"medium"},"family":"系统无衬线；iOS 拉丁文使用系统字体，中文使用系统中文回退，不栅格化","title":{"line_height_pt":38,"size_pt":30,"weight":"semibold"}}},"layout_rules":{"baseline_canvas_pt":{"height":852,"width":393},"regions":"默认安全区内容高度：主视觉 50%、文案 25%、导航 17%、余量 8%；大字号时可调整而非硬裁切","responsive":"小屏或大字号缩小主视觉和间隙，必要时文案滚动且 CTA 可达；宽屏居中限制内容宽度，资源等比 fit","safe_area":"由系统动态决定；背景可延伸全屏，文字/CTA/进度始终位于安全区内，不固定刘海或底部高度","typography":"正文最多两段；标题默认两行以内但不截断；标题与正文间距 medium，文案与导航至少 large","variants":{"hero-centered":"上半部主视觉居中，焦点约 x=0.50/y=0.27；下方文案左对齐，底部共享导航","hero-diagonal":"上半部主体沿左下到右上节奏展开，焦点仍在 x=0.50/y=0.27 附近；文案与导航位置保持"}},"motion_rules":{"background":"实色背景保持不变，不逐页换背景色或制造闪烁","continuity":"主体锚点、光源、视角稳定；同类形状通过位置/透明度过渡，不强行做不合理物体变形","entrance":"主视觉 280 ms ease-out，从下方 12 pt 进入并淡入；文案随后 60 ms 淡入，不持续漂浮","reduce_motion":"取消位移、缩放和延迟，100 ms 淡入或直接替换；交互和信息保持可用","transition":"页面 320 ms ease-in-out 淡出淡入并最多 24 pt 横向位移，可中断，不能动画排队"},"negative_constraints":["禁止页面之间随机切换色板、字体、材质、光源或渲染技法","禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突","禁止不合理透视、超过三个景深层、过度装饰或无关物体","禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区","禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互"],"style_id":"soft-glass-daylight-v1","visual_language":{"dominant_style":"glassmorphism","lighting":"固定左上 45 度宽漫射日光，低对比度，投影向右下，无第二彩色光源","materials":"主视觉磨砂玻璃；不混入铬金属、皮革、纸噪点或黏土","mood":"清透、安静、可信赖，允许冷暖辅助色平衡，避免霓虹科技感","perspective":"正面为主的轻微三分之四视角，固定平行投影，无广角畸变","rendering":"柔和半写实几何，干净轮廓，无厚重轮廓线，最多三个景深层","secondary_styles":[],"signature_features":["薄磨砂玻璃边缘","左上日光与向右下柔影","大块浅色留白配不透明深色文字"]}}

全局禁止事项：
- 禁止风格混乱、页间色彩不统一、随机切换字体/材质/光源
- 禁止错误透视、过度装饰、文字层级混乱、信息密度过高
- 禁止与产品功能无关的视觉对象和机械复制参考图内容
- 禁止页面之间随机切换色板、字体、材质、光源或渲染技法
- 禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突
- 禁止不合理透视、超过三个景深层、过度装饰或无关物体
- 禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区
- 禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互
- 禁止用无关音乐、机器人、聊天气泡或抽象光球替代天气功能表达
- 禁止暗示用户已授予定位/通知权限，禁止虚构预报准确率或把演示温度声称为实况
- 禁止三页都使用相同云朵卡片仅替换标题

## D. Screen Prompts

使用方法：复制单页的完整共同提示词，再追加该页任一目标指令。每页已带相同 STYLE_LOCK 和完整负向约束，可独立使用，无需上一页上下文。

### 1. weather-now · 抬眼，就懂此刻天气

**共同提示词（完整复制）**

```text
设计一组可实现的移动 App 首次启动引导。逐字遵守同一 STYLE_LOCK，只能在允许范围内改变产品主体、场景和布局变体，不添加另一套颜色/字体/材质/光源。主视觉解释产品能力，文案与导航保持留白和清楚层级，安全区与字号动态适配。

STYLE_LOCK_SHA256: a7c5da98e734a51c173255f5a6ec6b7e925395c0e3534e537d928b05fd3263e8
STYLE_LOCK: {"component_rules":{"button":"共享主按钮高 52 pt（大字号可增高）、圆角 button、primary 底/on_primary 字；禁用态有可读说明，不仅降低透明度","card":"仅在主视觉中使用 glass_surface 透明度、card 圆角、白色 1 pt 细边和共享阴影；正文区域不做透明叠字","navigation":"同一底部区域提供进度与一个主 CTA；继续进入下一页，最后 CTA 进入产品；跳过与末页完成目标一致，不自动申请权限","progress":"统一步进点，按实际页数生成；活动点 primary，其他点 text_secondary；读屏为第几页/共几页，不仅依赖颜色"},"composition_rules":{"allowed_variations":"可换主体、功能场景、对象数量与已批准布局变体；不变更材质、光源、镜头、文字层级和底部导航","focal_point":"主体在安全区上半部，占画布宽约 65%～80%，视觉焦点稳定在 x=0.50/y=0.27 附近","negative_space":"主视觉与文案间至少 24 pt 的视觉间隔；文案背景无装饰，不把装饰挤入导航区","visual_weight":"一主对象或一个对象组、最多两个辅助元素；正文低于主视觉，CTA 清楚但不盖住主体"},"design_tokens":{"colors":{"art_accent_cool":"#8DC9EB","art_accent_warm":"#F4C66A","background":"#F3F7FC","on_primary":"#FFFFFF","primary":"#2456CB","surface":"#FFFFFF","text_primary":"#13243A","text_secondary":"#43576E","usage":"冷暖辅助色仅用于主视觉；正文在不透明 background 上，CTA 用 primary/on_primary，不用浅辅助色承载小字"},"effects":{"background_gradient":"无；稳定 background 实色","border_color":"#FFFFFF","border_width_pt":1,"glass_blur_pt":18},"opacity":{"glass_border":0.7,"glass_surface":0.76,"text":1},"radii_pt":{"button":16,"card":24},"shadows":{"card":{"alpha":0.1,"blur_pt":24,"color":"#13243A","x_pt":0,"y_pt":8}},"spacing_pt":{"large":24,"medium":16,"page_horizontal":24,"section":32,"small":8,"unit":8},"typography":{"alignment":"标题、正文左对齐；按钮居中；跟随系统动态字号","body":{"line_height_pt":26,"size_pt":17,"weight":"regular"},"button":{"line_height_pt":22,"size_pt":17,"weight":"semibold"},"caption":{"line_height_pt":18,"size_pt":13,"weight":"medium"},"family":"系统无衬线；iOS 拉丁文使用系统字体，中文使用系统中文回退，不栅格化","title":{"line_height_pt":38,"size_pt":30,"weight":"semibold"}}},"layout_rules":{"baseline_canvas_pt":{"height":852,"width":393},"regions":"默认安全区内容高度：主视觉 50%、文案 25%、导航 17%、余量 8%；大字号时可调整而非硬裁切","responsive":"小屏或大字号缩小主视觉和间隙，必要时文案滚动且 CTA 可达；宽屏居中限制内容宽度，资源等比 fit","safe_area":"由系统动态决定；背景可延伸全屏，文字/CTA/进度始终位于安全区内，不固定刘海或底部高度","typography":"正文最多两段；标题默认两行以内但不截断；标题与正文间距 medium，文案与导航至少 large","variants":{"hero-centered":"上半部主视觉居中，焦点约 x=0.50/y=0.27；下方文案左对齐，底部共享导航","hero-diagonal":"上半部主体沿左下到右上节奏展开，焦点仍在 x=0.50/y=0.27 附近；文案与导航位置保持"}},"motion_rules":{"background":"实色背景保持不变，不逐页换背景色或制造闪烁","continuity":"主体锚点、光源、视角稳定；同类形状通过位置/透明度过渡，不强行做不合理物体变形","entrance":"主视觉 280 ms ease-out，从下方 12 pt 进入并淡入；文案随后 60 ms 淡入，不持续漂浮","reduce_motion":"取消位移、缩放和延迟，100 ms 淡入或直接替换；交互和信息保持可用","transition":"页面 320 ms ease-in-out 淡出淡入并最多 24 pt 横向位移，可中断，不能动画排队"},"negative_constraints":["禁止页面之间随机切换色板、字体、材质、光源或渲染技法","禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突","禁止不合理透视、超过三个景深层、过度装饰或无关物体","禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区","禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互"],"style_id":"soft-glass-daylight-v1","visual_language":{"dominant_style":"glassmorphism","lighting":"固定左上 45 度宽漫射日光，低对比度，投影向右下，无第二彩色光源","materials":"主视觉磨砂玻璃；不混入铬金属、皮革、纸噪点或黏土","mood":"清透、安静、可信赖，允许冷暖辅助色平衡，避免霓虹科技感","perspective":"正面为主的轻微三分之四视角，固定平行投影，无广角畸变","rendering":"柔和半写实几何，干净轮廓，无厚重轮廓线，最多三个景深层","secondary_styles":[],"signature_features":["薄磨砂玻璃边缘","左上日光与向右下柔影","大块浅色留白配不透明深色文字"]}}

全局禁止事项：
- 禁止风格混乱、页间色彩不统一、随机切换字体/材质/光源
- 禁止错误透视、过度装饰、文字层级混乱、信息密度过高
- 禁止与产品功能无关的视觉对象和机械复制参考图内容
- 禁止页面之间随机切换色板、字体、材质、光源或渲染技法
- 禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突
- 禁止不合理透视、超过三个景深层、过度装饰或无关物体
- 禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区
- 禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互
- 禁止用无关音乐、机器人、聊天气泡或抽象光球替代天气功能表达
- 禁止暗示用户已授予定位/通知权限，禁止虚构预报准确率或把演示温度声称为实况
- 禁止三页都使用相同云朵卡片仅替换标题

项目上下文（产品事实与假设）：{"assumptions":["示例无上传参考图；显式指定 glassmorphism 与轻盈自然日光，所有视觉值为设计选择","当前天气、逐时预报、降雨提醒均为演示产品的能力设定，不代表已连接真实天气服务","引导可跳过；完成或跳过后先手动选城市，再进入首页；定位和通知权限在相应功能实际使用时解释并申请","温度与时间均为示意数据；本次仅交付设计和提示词，未生成图片或运行 App"],"locale":"zh-Hans","platform":"iPhone；393×852 pt 为基准画布，非固定设备尺寸","project":{"audience":"需要安排日常出行的通勤用户","features":["当前天气","逐时预报","降雨提醒"],"name":"晴间","positioning":"以清楚、轻盈的天气信息支持出门决策；这是示例产品设定","type":"天气 App"}}

本页完整要求：{"composition":"圆盘对象组占画布宽约 70%，焦点位于 x=0.50/y=0.27；数字低于主体中心，不与标题相撞；正文和底部导航留白","description":"温度与天气状态清楚呈现，出门前少一点犹豫。","feature":"当前天气","goal":"让用户理解一眼获取当前天气的价值","id":"weather-now","implementation":{"assets":[{"aspect_ratio":"1:1","background":"transparent","crop_safe_area":"主体和柔影完整留在中央 80%，四周透明留白，等比 fit","description":"磨砂玻璃圆盘、云形和日光圆片的对象组；不含数字、文案、按钮或背景","export":"PNG alpha，按最大展示约 320 pt × 3 scale 导出 960×960 px；实际设备变化时重算","id":"hero-weather-now"}],"code_components":["背景、标题、说明、24° 与晴转多云为原生文字","共享主按钮、跳过按钮、分页进度","资源等比布局与页面切换"],"fallback":"没有 3D 资源时，用同色板原生圆盘与云形路径重建，不改材质语法和光源；模糊不可用时采用不透明 surface"},"interaction":{"primary_action":"next:hourly-outlook","primary_label":"继续","progress":"第 1 页，共 3 页；首点活动","secondary_action":"skip:city-picker","secondary_label":"跳过"},"layout_variant":"hero-centered","motion":"云形与圆盘按统一入口动效进入；进入第二页时保持对象组锚点，淡出圆盘并淡入时间轴；不让太阳成为第二个真实光源；Reduce Motion 只淡入","scene":"上半部集中展示当前天气的一个场景；云形用冷辅助色，日光圆片用暖辅助色；原生叠加示意 24° 与晴转多云，无城市照片、无额外卡片","title":"抬眼，就懂此刻天气","token_refs":["colors.background","colors.primary","colors.art_accent_cool","colors.art_accent_warm","typography.title","opacity.glass_surface"],"visual_subject":"一个磨砂玻璃圆盘前方悬浮柔软云形，暖色日光圆片从右后方露出，但全场主光仍来自左上"}
```

**目标指令：UI 整页**

输出单张移动 App 内容画布，按本页精确标题、说明、主/次按钮和进度排版；遵从基准比例及安全区。无设备外壳、无拼页、无海报边框。示意数据按项目假设处理；文字误差在实现时用原生排版校正。

**目标指令：纯主视觉资源**

仅绘制本页 implementation.assets 指定的资源；多个资源逐个输出。继承 STYLE_LOCK 的色板、材质、光照、镜头和构图语言，忽略整页文字、按钮与导航的绘制要求。按各资源 background、比例及保护区导出，不含文字、数字、状态栏、CTA、进度或设备外壳。资源数组为空时无需出图，用代码绘制。

**目标指令：原生 UI 实现**

面向 iPhone；393×852 pt 为基准画布，非固定设备尺寸，按项目原生框架实现本页；SwiftUI 项目用共享 DesignTokens、页面数据模型、原生文案与导航控件，按 asset ID 引用资源，不把整屏图作为 UI。实现 primary_action、secondary_action、返回、完成与权限时机，遵守 fallback、动态文字、安全区和 Reduce Motion；具体 API 按部署目标核对。仅在用户要求实现时执行，按 F 节交接。

### 2. hourly-outlook · 把出发时间安排好

**共同提示词（完整复制）**

```text
设计一组可实现的移动 App 首次启动引导。逐字遵守同一 STYLE_LOCK，只能在允许范围内改变产品主体、场景和布局变体，不添加另一套颜色/字体/材质/光源。主视觉解释产品能力，文案与导航保持留白和清楚层级，安全区与字号动态适配。

STYLE_LOCK_SHA256: a7c5da98e734a51c173255f5a6ec6b7e925395c0e3534e537d928b05fd3263e8
STYLE_LOCK: {"component_rules":{"button":"共享主按钮高 52 pt（大字号可增高）、圆角 button、primary 底/on_primary 字；禁用态有可读说明，不仅降低透明度","card":"仅在主视觉中使用 glass_surface 透明度、card 圆角、白色 1 pt 细边和共享阴影；正文区域不做透明叠字","navigation":"同一底部区域提供进度与一个主 CTA；继续进入下一页，最后 CTA 进入产品；跳过与末页完成目标一致，不自动申请权限","progress":"统一步进点，按实际页数生成；活动点 primary，其他点 text_secondary；读屏为第几页/共几页，不仅依赖颜色"},"composition_rules":{"allowed_variations":"可换主体、功能场景、对象数量与已批准布局变体；不变更材质、光源、镜头、文字层级和底部导航","focal_point":"主体在安全区上半部，占画布宽约 65%～80%，视觉焦点稳定在 x=0.50/y=0.27 附近","negative_space":"主视觉与文案间至少 24 pt 的视觉间隔；文案背景无装饰，不把装饰挤入导航区","visual_weight":"一主对象或一个对象组、最多两个辅助元素；正文低于主视觉，CTA 清楚但不盖住主体"},"design_tokens":{"colors":{"art_accent_cool":"#8DC9EB","art_accent_warm":"#F4C66A","background":"#F3F7FC","on_primary":"#FFFFFF","primary":"#2456CB","surface":"#FFFFFF","text_primary":"#13243A","text_secondary":"#43576E","usage":"冷暖辅助色仅用于主视觉；正文在不透明 background 上，CTA 用 primary/on_primary，不用浅辅助色承载小字"},"effects":{"background_gradient":"无；稳定 background 实色","border_color":"#FFFFFF","border_width_pt":1,"glass_blur_pt":18},"opacity":{"glass_border":0.7,"glass_surface":0.76,"text":1},"radii_pt":{"button":16,"card":24},"shadows":{"card":{"alpha":0.1,"blur_pt":24,"color":"#13243A","x_pt":0,"y_pt":8}},"spacing_pt":{"large":24,"medium":16,"page_horizontal":24,"section":32,"small":8,"unit":8},"typography":{"alignment":"标题、正文左对齐；按钮居中；跟随系统动态字号","body":{"line_height_pt":26,"size_pt":17,"weight":"regular"},"button":{"line_height_pt":22,"size_pt":17,"weight":"semibold"},"caption":{"line_height_pt":18,"size_pt":13,"weight":"medium"},"family":"系统无衬线；iOS 拉丁文使用系统字体，中文使用系统中文回退，不栅格化","title":{"line_height_pt":38,"size_pt":30,"weight":"semibold"}}},"layout_rules":{"baseline_canvas_pt":{"height":852,"width":393},"regions":"默认安全区内容高度：主视觉 50%、文案 25%、导航 17%、余量 8%；大字号时可调整而非硬裁切","responsive":"小屏或大字号缩小主视觉和间隙，必要时文案滚动且 CTA 可达；宽屏居中限制内容宽度，资源等比 fit","safe_area":"由系统动态决定；背景可延伸全屏，文字/CTA/进度始终位于安全区内，不固定刘海或底部高度","typography":"正文最多两段；标题默认两行以内但不截断；标题与正文间距 medium，文案与导航至少 large","variants":{"hero-centered":"上半部主视觉居中，焦点约 x=0.50/y=0.27；下方文案左对齐，底部共享导航","hero-diagonal":"上半部主体沿左下到右上节奏展开，焦点仍在 x=0.50/y=0.27 附近；文案与导航位置保持"}},"motion_rules":{"background":"实色背景保持不变，不逐页换背景色或制造闪烁","continuity":"主体锚点、光源、视角稳定；同类形状通过位置/透明度过渡，不强行做不合理物体变形","entrance":"主视觉 280 ms ease-out，从下方 12 pt 进入并淡入；文案随后 60 ms 淡入，不持续漂浮","reduce_motion":"取消位移、缩放和延迟，100 ms 淡入或直接替换；交互和信息保持可用","transition":"页面 320 ms ease-in-out 淡出淡入并最多 24 pt 横向位移，可中断，不能动画排队"},"negative_constraints":["禁止页面之间随机切换色板、字体、材质、光源或渲染技法","禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突","禁止不合理透视、超过三个景深层、过度装饰或无关物体","禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区","禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互"],"style_id":"soft-glass-daylight-v1","visual_language":{"dominant_style":"glassmorphism","lighting":"固定左上 45 度宽漫射日光，低对比度，投影向右下，无第二彩色光源","materials":"主视觉磨砂玻璃；不混入铬金属、皮革、纸噪点或黏土","mood":"清透、安静、可信赖，允许冷暖辅助色平衡，避免霓虹科技感","perspective":"正面为主的轻微三分之四视角，固定平行投影，无广角畸变","rendering":"柔和半写实几何，干净轮廓，无厚重轮廓线，最多三个景深层","secondary_styles":[],"signature_features":["薄磨砂玻璃边缘","左上日光与向右下柔影","大块浅色留白配不透明深色文字"]}}

全局禁止事项：
- 禁止风格混乱、页间色彩不统一、随机切换字体/材质/光源
- 禁止错误透视、过度装饰、文字层级混乱、信息密度过高
- 禁止与产品功能无关的视觉对象和机械复制参考图内容
- 禁止页面之间随机切换色板、字体、材质、光源或渲染技法
- 禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突
- 禁止不合理透视、超过三个景深层、过度装饰或无关物体
- 禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区
- 禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互
- 禁止用无关音乐、机器人、聊天气泡或抽象光球替代天气功能表达
- 禁止暗示用户已授予定位/通知权限，禁止虚构预报准确率或把演示温度声称为实况
- 禁止三页都使用相同云朵卡片仅替换标题

项目上下文（产品事实与假设）：{"assumptions":["示例无上传参考图；显式指定 glassmorphism 与轻盈自然日光，所有视觉值为设计选择","当前天气、逐时预报、降雨提醒均为演示产品的能力设定，不代表已连接真实天气服务","引导可跳过；完成或跳过后先手动选城市，再进入首页；定位和通知权限在相应功能实际使用时解释并申请","温度与时间均为示意数据；本次仅交付设计和提示词，未生成图片或运行 App"],"locale":"zh-Hans","platform":"iPhone；393×852 pt 为基准画布，非固定设备尺寸","project":{"audience":"需要安排日常出行的通勤用户","features":["当前天气","逐时预报","降雨提醒"],"name":"晴间","positioning":"以清楚、轻盈的天气信息支持出门决策；这是示例产品设定","type":"天气 App"}}

本页完整要求：{"composition":"轨道占画布宽约 78%，对象组焦点仍为 x=0.50/y=0.27，三个节点大小有主次；不挤入下部文案；标题和导航沿用共享网格","description":"沿着逐时预报，看清天气变化，选个合适的时刻出门。","feature":"逐时预报","goal":"让用户理解逐时变化如何帮助选择出发时间","id":"hourly-outlook","implementation":{"assets":[{"aspect_ratio":"1:1","background":"transparent","crop_safe_area":"完整轨道、节点和柔影留在中央 80%，避免端点贴边；等比 fit","description":"磨砂弧形时间轨道及日光、云、雨三个节点；不含标签文字，轮廓适度简化","export":"PNG alpha，最大展示约 320 pt × 3 scale，960×960 px；与第一页统一导出比例","id":"hero-hourly-outlook"}],"code_components":["09时、12时、15时标签与所有说明采用原生文字","简单轨道可用路径，颜色与阴影来自共享 token","共享导航与可返回的分页状态"],"fallback":"轨道与节点均可用原生路径和同材质简化几何绘制；保留时间演进语义，不退化成三个无关装饰图标"},"interaction":{"primary_action":"next:rain-reminder","primary_label":"继续","progress":"第 2 页，共 3 页；第二点活动；允许右滑返回第 1 页","secondary_action":"skip:city-picker","secondary_label":"跳过"},"layout_variant":"hero-diagonal","motion":"时间节点沿轨道按顺序出现，总入口不超过共享动效节奏；进入第三页时中间云形在相同锚点交叉淡入雨幕；不改变光源或镜头；Reduce Motion 直接显示全部节点","scene":"轨道沿左下到右上展开，三节点同属一个对象组；原生叠加 09时、12时、15时示意标签，表达时间而非三张相同卡片","title":"把出发时间安排好","token_refs":["colors.background","colors.primary","colors.art_accent_cool","colors.art_accent_warm","typography.caption","shadows.card"],"visual_subject":"一条由近到远缓慢抬升的磨砂玻璃弧形时间轨道，三个节点分别呈现日光、云层、细雨的天气变化"}
```

**目标指令：UI 整页**

输出单张移动 App 内容画布，按本页精确标题、说明、主/次按钮和进度排版；遵从基准比例及安全区。无设备外壳、无拼页、无海报边框。示意数据按项目假设处理；文字误差在实现时用原生排版校正。

**目标指令：纯主视觉资源**

仅绘制本页 implementation.assets 指定的资源；多个资源逐个输出。继承 STYLE_LOCK 的色板、材质、光照、镜头和构图语言，忽略整页文字、按钮与导航的绘制要求。按各资源 background、比例及保护区导出，不含文字、数字、状态栏、CTA、进度或设备外壳。资源数组为空时无需出图，用代码绘制。

**目标指令：原生 UI 实现**

面向 iPhone；393×852 pt 为基准画布，非固定设备尺寸，按项目原生框架实现本页；SwiftUI 项目用共享 DesignTokens、页面数据模型、原生文案与导航控件，按 asset ID 引用资源，不把整屏图作为 UI。实现 primary_action、secondary_action、返回、完成与权限时机，遵守 fallback、动态文字、安全区和 Reduce Motion；具体 API 按部署目标核对。仅在用户要求实现时执行，按 F 节交接。

### 3. rain-reminder · 雨来之前，心里有数

**共同提示词（完整复制）**

```text
设计一组可实现的移动 App 首次启动引导。逐字遵守同一 STYLE_LOCK，只能在允许范围内改变产品主体、场景和布局变体，不添加另一套颜色/字体/材质/光源。主视觉解释产品能力，文案与导航保持留白和清楚层级，安全区与字号动态适配。

STYLE_LOCK_SHA256: a7c5da98e734a51c173255f5a6ec6b7e925395c0e3534e537d928b05fd3263e8
STYLE_LOCK: {"component_rules":{"button":"共享主按钮高 52 pt（大字号可增高）、圆角 button、primary 底/on_primary 字；禁用态有可读说明，不仅降低透明度","card":"仅在主视觉中使用 glass_surface 透明度、card 圆角、白色 1 pt 细边和共享阴影；正文区域不做透明叠字","navigation":"同一底部区域提供进度与一个主 CTA；继续进入下一页，最后 CTA 进入产品；跳过与末页完成目标一致，不自动申请权限","progress":"统一步进点，按实际页数生成；活动点 primary，其他点 text_secondary；读屏为第几页/共几页，不仅依赖颜色"},"composition_rules":{"allowed_variations":"可换主体、功能场景、对象数量与已批准布局变体；不变更材质、光源、镜头、文字层级和底部导航","focal_point":"主体在安全区上半部，占画布宽约 65%～80%，视觉焦点稳定在 x=0.50/y=0.27 附近","negative_space":"主视觉与文案间至少 24 pt 的视觉间隔；文案背景无装饰，不把装饰挤入导航区","visual_weight":"一主对象或一个对象组、最多两个辅助元素；正文低于主视觉，CTA 清楚但不盖住主体"},"design_tokens":{"colors":{"art_accent_cool":"#8DC9EB","art_accent_warm":"#F4C66A","background":"#F3F7FC","on_primary":"#FFFFFF","primary":"#2456CB","surface":"#FFFFFF","text_primary":"#13243A","text_secondary":"#43576E","usage":"冷暖辅助色仅用于主视觉；正文在不透明 background 上，CTA 用 primary/on_primary，不用浅辅助色承载小字"},"effects":{"background_gradient":"无；稳定 background 实色","border_color":"#FFFFFF","border_width_pt":1,"glass_blur_pt":18},"opacity":{"glass_border":0.7,"glass_surface":0.76,"text":1},"radii_pt":{"button":16,"card":24},"shadows":{"card":{"alpha":0.1,"blur_pt":24,"color":"#13243A","x_pt":0,"y_pt":8}},"spacing_pt":{"large":24,"medium":16,"page_horizontal":24,"section":32,"small":8,"unit":8},"typography":{"alignment":"标题、正文左对齐；按钮居中；跟随系统动态字号","body":{"line_height_pt":26,"size_pt":17,"weight":"regular"},"button":{"line_height_pt":22,"size_pt":17,"weight":"semibold"},"caption":{"line_height_pt":18,"size_pt":13,"weight":"medium"},"family":"系统无衬线；iOS 拉丁文使用系统字体，中文使用系统中文回退，不栅格化","title":{"line_height_pt":38,"size_pt":30,"weight":"semibold"}}},"layout_rules":{"baseline_canvas_pt":{"height":852,"width":393},"regions":"默认安全区内容高度：主视觉 50%、文案 25%、导航 17%、余量 8%；大字号时可调整而非硬裁切","responsive":"小屏或大字号缩小主视觉和间隙，必要时文案滚动且 CTA 可达；宽屏居中限制内容宽度，资源等比 fit","safe_area":"由系统动态决定；背景可延伸全屏，文字/CTA/进度始终位于安全区内，不固定刘海或底部高度","typography":"正文最多两段；标题默认两行以内但不截断；标题与正文间距 medium，文案与导航至少 large","variants":{"hero-centered":"上半部主视觉居中，焦点约 x=0.50/y=0.27；下方文案左对齐，底部共享导航","hero-diagonal":"上半部主体沿左下到右上节奏展开，焦点仍在 x=0.50/y=0.27 附近；文案与导航位置保持"}},"motion_rules":{"background":"实色背景保持不变，不逐页换背景色或制造闪烁","continuity":"主体锚点、光源、视角稳定；同类形状通过位置/透明度过渡，不强行做不合理物体变形","entrance":"主视觉 280 ms ease-out，从下方 12 pt 进入并淡入；文案随后 60 ms 淡入，不持续漂浮","reduce_motion":"取消位移、缩放和延迟，100 ms 淡入或直接替换；交互和信息保持可用","transition":"页面 320 ms ease-in-out 淡出淡入并最多 24 pt 横向位移，可中断，不能动画排队"},"negative_constraints":["禁止页面之间随机切换色板、字体、材质、光源或渲染技法","禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突","禁止不合理透视、超过三个景深层、过度装饰或无关物体","禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区","禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互"],"style_id":"soft-glass-daylight-v1","visual_language":{"dominant_style":"glassmorphism","lighting":"固定左上 45 度宽漫射日光，低对比度，投影向右下，无第二彩色光源","materials":"主视觉磨砂玻璃；不混入铬金属、皮革、纸噪点或黏土","mood":"清透、安静、可信赖，允许冷暖辅助色平衡，避免霓虹科技感","perspective":"正面为主的轻微三分之四视角，固定平行投影，无广角畸变","rendering":"柔和半写实几何，干净轮廓，无厚重轮廓线，最多三个景深层","secondary_styles":[],"signature_features":["薄磨砂玻璃边缘","左上日光与向右下柔影","大块浅色留白配不透明深色文字"]}}

全局禁止事项：
- 禁止风格混乱、页间色彩不统一、随机切换字体/材质/光源
- 禁止错误透视、过度装饰、文字层级混乱、信息密度过高
- 禁止与产品功能无关的视觉对象和机械复制参考图内容
- 禁止页面之间随机切换色板、字体、材质、光源或渲染技法
- 禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突
- 禁止不合理透视、超过三个景深层、过度装饰或无关物体
- 禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区
- 禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互
- 禁止用无关音乐、机器人、聊天气泡或抽象光球替代天气功能表达
- 禁止暗示用户已授予定位/通知权限，禁止虚构预报准确率或把演示温度声称为实况
- 禁止三页都使用相同云朵卡片仅替换标题

项目上下文（产品事实与假设）：{"assumptions":["示例无上传参考图；显式指定 glassmorphism 与轻盈自然日光，所有视觉值为设计选择","当前天气、逐时预报、降雨提醒均为演示产品的能力设定，不代表已连接真实天气服务","引导可跳过；完成或跳过后先手动选城市，再进入首页；定位和通知权限在相应功能实际使用时解释并申请","温度与时间均为示意数据；本次仅交付设计和提示词，未生成图片或运行 App"],"locale":"zh-Hans","platform":"iPhone；393×852 pt 为基准画布，非固定设备尺寸","project":{"audience":"需要安排日常出行的通勤用户","features":["当前天气","逐时预报","降雨提醒"],"name":"晴间","positioning":"以清楚、轻盈的天气信息支持出门决策；这是示例产品设定","type":"天气 App"}}

本页完整要求：{"composition":"云与伞构成一个垂直对象组，约占画布宽 68%，焦点保持 x=0.50/y=0.27；铃铛为辅助元素，文案区与导航区保持无装饰","description":"需要时开启降雨提醒，为临时变化多留一点准备。","feature":"降雨提醒","goal":"说明提醒价值并让用户进入产品，权限延后申请","id":"rain-reminder","implementation":{"assets":[{"aspect_ratio":"1:1","background":"transparent","crop_safe_area":"伞、铃铛、雨线和柔影均留在中央 80%，保护底部伞柄；等比 fit","description":"同材质雨云、伞、分开的雨线和一个小铃铛符号；无授权成功标记、文字或控件","export":"PNG alpha，最大展示约 320 pt × 3 scale，960×960 px；与前两页统一","id":"hero-rain-reminder"}],"code_components":["全部文案、主 CTA 和进度为原生控件","保存 onboardingCompleted 后打开手动城市选择，选完进入天气首页","通知权限仅在用户实际开启降雨提醒时申请"],"fallback":"资源不可用时用统一色板的原生伞、云路径与简化雨线；不显示虚构的系统授权状态"},"interaction":{"primary_action":"complete:city-picker","primary_label":"开始使用","progress":"第 3 页，共 3 页；第三点活动","secondary_action":"无；允许右滑返回第 2 页","secondary_label":"无"},"layout_variant":"hero-centered","motion":"云与伞同步轻微淡入，铃铛不摇晃或持续闪动；点击开始使用后按统一转场进入城市选择；Reduce Motion 直接切换，仍保留完成状态","scene":"使用冷辅助色绘制雨与伞，暖辅助色只点亮铃铛符号；不出现已开启通知的成功勾选，不画系统权限弹窗；表达准备行动而非已获授权","title":"雨来之前，心里有数","token_refs":["colors.background","colors.primary","colors.text_primary","colors.art_accent_cool","colors.art_accent_warm","radii_pt.button"],"visual_subject":"一把简洁的磨砂玻璃伞位于细雨云下方，雨线在伞面两侧分开；一个小型铃铛轮廓作为提醒符号"}
```

**目标指令：UI 整页**

输出单张移动 App 内容画布，按本页精确标题、说明、主/次按钮和进度排版；遵从基准比例及安全区。无设备外壳、无拼页、无海报边框。示意数据按项目假设处理；文字误差在实现时用原生排版校正。

**目标指令：纯主视觉资源**

仅绘制本页 implementation.assets 指定的资源；多个资源逐个输出。继承 STYLE_LOCK 的色板、材质、光照、镜头和构图语言，忽略整页文字、按钮与导航的绘制要求。按各资源 background、比例及保护区导出，不含文字、数字、状态栏、CTA、进度或设备外壳。资源数组为空时无需出图，用代码绘制。

**目标指令：原生 UI 实现**

面向 iPhone；393×852 pt 为基准画布，非固定设备尺寸，按项目原生框架实现本页；SwiftUI 项目用共享 DesignTokens、页面数据模型、原生文案与导航控件，按 asset ID 引用资源，不把整屏图作为 UI。实现 primary_action、secondary_action、返回、完成与权限时机，遵守 fallback、动态文字、安全区和 Reduce Motion；具体 API 按部署目标核对。仅在用户要求实现时执行，按 F 节交接。

## E. Negative Prompt

- 禁止风格混乱、页间色彩不统一、随机切换字体/材质/光源
- 禁止错误透视、过度装饰、文字层级混乱、信息密度过高
- 禁止与产品功能无关的视觉对象和机械复制参考图内容
- 禁止页面之间随机切换色板、字体、材质、光源或渲染技法
- 禁止霓虹辉光、厚重黑描边、镜面铬金属、硬阴影和多光源冲突
- 禁止不合理透视、超过三个景深层、过度装饰或无关物体
- 禁止正文置于透明复杂底图、层级混乱、密集小字和按钮侵入系统安全区
- 禁止机械复制参考图品牌/角色/内容、仅换标题重复主视觉、整屏栅格图替代真实交互
- 禁止用无关音乐、机器人、聊天气泡或抽象光球替代天气功能表达
- 禁止暗示用户已授予定位/通知权限，禁止虚构预报准确率或把演示温度声称为实况
- 禁止三页都使用相同云朵卡片仅替换标题

## F. Implementation Hints

### 代码与组件

- SwiftUI 用共享 DesignTokens、数据驱动 OnboardingScreen 和可中断分页容器；背景、真实文案、按钮、进度、时间/温度标签均由代码渲染
- 玻璃资源已带光照，不再叠加方向冲突的阴影；代码卡片沿用 Profile 的材质与回退，不依赖特定新系统玻璃 API

### 视觉资源

- 分别导出 hero-weather-now、hero-hourly-outlook、hero-rain-reminder，背景透明、不含文字；以资源清单的比例和安全裁切区验收
- 960×960 px 是 320 pt@3x 的示例产物；按实际最大展示大小重新核对，并提供原生路径简化回退

### 屏幕适配

- 系统读取上下安全区，背景可出血，CTA 及文案不可；393×852 pt 是设计基准，不硬编码传感器区域高度
- 小屏/大字号先压缩主视觉和间距，再让内容滚动且主 CTA 可达；宽屏限制内容宽度、资源等比 fit，禁止拉伸

### 可访问性与动效

- 系统动态字号、读屏页码与按钮标签；图像若仅装饰则隐藏读屏，信息由文案提供
- 按真实合成背景核对正文对比度，交互目标至少 44×44 pt；Reduce Motion 取消位移与延迟，保留状态变化

### 状态与导航

- 继续按 Flow 的 next 目标推进，滑动可返回；前两页跳过与最后页完成均保存完成标记并进入手动城市选择，选城后进入首页
- 从设置可重新查看引导；重播完成回到设置，不重复触发权限弹窗；引导不承担通知权限申请

## 质量检查与验证范围

方案级检查，未执行图像渲染、原生编译或设备运行验收。

- `style_consistency` · pass：三页共用同一 Profile 的材质、光源、色板、字体与导航；页面未引入第二套 token；修正：无需修正
- `product_relevance` · pass：圆盘天气对应当前状态，时间轨道对应逐时预报，雨伞与提醒符号对应降雨提醒；修正：无需修正；产品为演示设定
- `composition_quality` · pass：三页锚点一致且文案区无装饰，允许居中与对角两种布局，并定义小屏/大字号规则；修正：无需修正；实际渲染待验收
- `flow_completeness` · pass：认识现在、安排未来、理解提醒后开始使用；下一页、跳过与最终城市选择路径明确；修正：无需修正
- `prompt_executability` · pass：各页定义主体、位置、准确文案、交互、动效和导出资源；由脚本注入独立风格锁及负向约束；修正：无需修正；图像模型输出仍需检查
- `reusability` · pass：Style Profile 无天气专属对象；音乐项目可用同一玻璃材质、左上柔光、居中焦点设计唱片播放与收藏场景，只改 Flow；修正：无需修正
- `implementability` · pass：三个独立透明主视觉与原生文字/控件明确分工，包含资源缺失、模糊降级及延后权限策略；修正：无需修正；原生运行与设备检查待执行

复用：将 A 节保存为 `soft-glass-daylight-v1.json`，通过 save-profile 存入本地目录。后续先用 style_id 加载，再针对新产品重写 Flow；无需重新上传原图。相同输入的提示词拼装确定性一致；图像生成仍可能存在随机性。

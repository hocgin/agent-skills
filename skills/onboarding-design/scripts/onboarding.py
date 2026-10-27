#!/usr/bin/env python3
"""Local Style Profile storage, structural validation and deterministic prompt assembly."""

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path


STYLE_KEYS = (
    "style_id", "design_tokens", "visual_language", "layout_rules",
    "component_rules", "composition_rules", "motion_rules", "negative_constraints",
)
CHECKS = (
    "style_consistency", "product_relevance", "composition_quality",
    "flow_completeness", "prompt_executability", "reusability", "implementability",
)
DEFAULT_NEGATIVES = [
    "禁止风格混乱、页间色彩不统一、随机切换字体/材质/光源",
    "禁止错误透视、过度装饰、文字层级混乱、信息密度过高",
    "禁止与产品功能无关的视觉对象和机械复制参考图内容",
]
HINT_KEYS = ("native_ui", "assets", "adaptation", "accessibility", "state_and_navigation")
ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def fields(value, names, path):
    require(isinstance(value, dict), f"{path}: 必须为对象")
    for name in names:
        require(name in value, f"{path}.{name}: 缺失")
    return value


def text_value(value, path, allow_empty=False):
    require(isinstance(value, str) and (allow_empty or value.strip()), f"{path}: 需要字符串")


def string_list(value, path, allow_empty=False):
    require(isinstance(value, list) and (allow_empty or value), f"{path}: 需要字符串数组")
    for i, item in enumerate(value):
        text_value(item, f"{path}[{i}]")


def style_id(value):
    require(isinstance(value, str) and len(value) <= 64 and
            re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value), "style_id: 需要最多 64 字符的 kebab-case")
    return value


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON 重复键: {key}")
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError(f"JSON 不允许非有限数: {value}")


def finite_float(value):
    number = float(value)
    require(math.isfinite(number), f"JSON 不允许非有限数: {value}")
    return number


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"),
                      object_pairs_hook=no_duplicate_keys, parse_constant=invalid_constant,
                      parse_float=finite_float)


def pretty(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def compact(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def validate_profile(profile):
    fields(profile, ("schema_version", "name", "derived_from", "provenance", *STYLE_KEYS), "profile")
    require(type(profile["schema_version"]) is int and profile["schema_version"] == 1,
            "profile.schema_version: 只支持 1")
    style_id(profile["style_id"])
    text_value(profile["name"], "profile.name")
    if profile["derived_from"] is not None:
        style_id(profile["derived_from"])
        require(profile["derived_from"] != profile["style_id"], "derived_from: 必须使用新 style_id")
    provenance = fields(profile["provenance"], ("mode", "references", "observations", "decisions"), "provenance")
    text_value(provenance["mode"], "provenance.mode")
    for key in ("references", "observations"):
        require(isinstance(provenance[key], list), f"provenance.{key}: 需要数组")
    fields(provenance["decisions"], ("retained", "translated", "dropped", "rationale"), "provenance.decisions")
    for key in ("retained", "translated", "dropped"):
        string_list(provenance["decisions"][key], f"decisions.{key}", allow_empty=True)
    text_value(provenance["decisions"]["rationale"], "decisions.rationale")
    tokens = fields(profile["design_tokens"],
                    ("colors", "typography", "spacing_pt", "radii_pt", "shadows", "opacity"), "design_tokens")
    for key, value in tokens.items():
        require(isinstance(value, dict) and value, f"design_tokens.{key}: 需要非空对象")
    colors = fields(tokens["colors"],
                    ("background", "surface", "primary", "text_primary", "text_secondary", "on_primary"), "colors")
    for key, value in colors.items():
        text_value(value, f"colors.{key}")
        if key != "usage":
            require(re.fullmatch(r"#[0-9a-fA-F]{6}", value), f"colors.{key}: 需要 #RRGGBB")
    for key, value in tokens["opacity"].items():
        require(type(value) in (int, float) and 0 <= value <= 1, f"opacity.{key}: 需要 0～1")
    fields(tokens["typography"], ("family", "title", "body", "button", "alignment"), "typography")
    for key in ("family", "alignment"):
        text_value(tokens["typography"][key], f"typography.{key}")
    for key in ("title", "body", "button"):
        role = fields(tokens["typography"][key], ("size_pt", "weight", "line_height_pt"), f"typography.{key}")
        text_value(role["weight"], f"typography.{key}.weight")
        for metric in ("size_pt", "line_height_pt"):
            require(type(role[metric]) in (int, float) and role[metric] > 0, f"typography.{key}.{metric}: 需要正数")
    language = fields(profile["visual_language"],
                      ("dominant_style", "secondary_styles", "signature_features", "rendering", "materials", "lighting", "perspective", "mood"), "visual_language")
    require(isinstance(language["secondary_styles"], list), "secondary_styles: 需要数组")
    string_list(language["signature_features"], "signature_features")
    require(len(language["signature_features"]) <= 3, "signature_features: 最多三项")
    for key in ("dominant_style", "rendering", "materials", "lighting", "perspective", "mood"):
        text_value(language[key], f"visual_language.{key}")
    layout = fields(profile["layout_rules"],
                    ("baseline_canvas_pt", "safe_area", "regions", "variants", "responsive", "typography"), "layout_rules")
    canvas = fields(layout["baseline_canvas_pt"], ("width", "height"), "baseline_canvas_pt")
    for key, value in canvas.items():
        require(type(value) in (int, float) and value > 0, f"baseline_canvas_pt.{key}: 需要正数")
    require(isinstance(layout["variants"], dict) and layout["variants"], "layout_rules.variants: 需要非空对象")
    for key, value in layout["variants"].items():
        text_value(value, f"layout_rules.variants.{key}")
    for key in ("safe_area", "regions", "responsive", "typography"):
        text_value(layout[key], f"layout_rules.{key}")
    groups = {
        "component_rules": ("button", "progress", "card", "navigation"),
        "composition_rules": ("focal_point", "negative_space", "visual_weight", "allowed_variations"),
        "motion_rules": ("transition", "entrance", "background", "continuity", "reduce_motion"),
    }
    for group, keys in groups.items():
        fields(profile[group], keys, group)
        for key in keys:
            text_value(profile[group][key], f"{group}.{key}")
    string_list(profile["negative_constraints"], "negative_constraints")


def validate_review(flow, required=False):
    review = flow.get("quality_review")
    if review is None:
        require(not required, "build: 先完成七项方案语义审查并填写 quality_review")
        return
    fields(review, ("scope", "checks"), "quality_review")
    require(review["scope"] in ("plan-only", "rendered-and-reviewed"), "quality_review.scope: 不支持的范围")
    fields(review["checks"], CHECKS, "quality_review.checks")
    for key in CHECKS:
        item = fields(review["checks"][key], ("status", "evidence", "fix"), f"quality_review.{key}")
        require(item["status"] in ("pass", "revised", "blocked"), f"quality_review.{key}.status: 不支持的状态")
        text_value(item["evidence"], f"quality_review.{key}.evidence")
        text_value(item["fix"], f"quality_review.{key}.fix")
        require(not required or item["status"] != "blocked", f"build: {key} 尚未修正，不能交付最终提示词")


def validate_flow(flow, profile):
    fields(flow, ("schema_version", "style_id", "project", "platform", "locale", "screen_count_reason",
                  "assumptions", "screens", "negative_constraints", "implementation_hints"), "flow")
    require(type(flow["schema_version"]) is int and flow["schema_version"] == 1, "flow.schema_version: 只支持 1")
    require(flow["style_id"] == profile["style_id"], "flow.style_id: 与 Profile 不一致")
    project = fields(flow["project"], ("name", "type", "features", "audience", "positioning"), "project")
    for key in ("name", "type", "audience", "positioning"):
        text_value(project[key], f"project.{key}")
    string_list(project["features"], "project.features")
    for key in ("platform", "locale"):
        text_value(flow[key], f"flow.{key}")
    text_value(flow["screen_count_reason"], "screen_count_reason", allow_empty=True)
    for key in ("assumptions", "negative_constraints"):
        string_list(flow[key], f"flow.{key}", allow_empty=True)
    screens = flow["screens"]
    require(isinstance(screens, list) and screens, "screens: 需要非空数组")
    require(3 <= len(screens) <= 5 or flow["screen_count_reason"].strip(), "screen_count_reason: 非 3～5 页需说明原因")
    ids, subjects, assets = set(), set(), set()
    for i, screen in enumerate(screens):
        path = f"screens[{i}]"
        texts = ("id", "goal", "feature", "title", "description", "visual_subject", "scene", "composition", "layout_variant", "motion")
        fields(screen, (*texts, "token_refs", "interaction", "implementation"), path)
        for key in texts:
            text_value(screen[key], f"{path}.{key}")
        require(screen["id"] not in ids, f"{path}.id: 重复")
        ids.add(screen["id"])
        require(screen["visual_subject"] not in subjects, f"{path}: 主体描述完全重复，需设计不同内容")
        subjects.add(screen["visual_subject"])
        require(screen["feature"] in project["features"], f"{path}.feature: 不在项目能力清单中")
        require(screen["layout_variant"] in profile["layout_rules"]["variants"], f"{path}.layout_variant: 未批准的布局")
        require(not set(screen).intersection(STYLE_KEYS), f"{path}: 不允许页级覆盖风格锁，请修改 Profile")
        string_list(screen["token_refs"], f"{path}.token_refs")
        for ref in screen["token_refs"]:
            node = profile["design_tokens"]
            for part in ref.split("."):
                require(isinstance(node, dict) and part in node, f"{path}.token_refs: 未知 token {ref}")
                node = node[part]
        interaction = fields(screen["interaction"],
                             ("primary_label", "primary_action", "secondary_label", "secondary_action", "progress"), f"{path}.interaction")
        for key, value in interaction.items():
            text_value(value, f"{path}.interaction.{key}")
        implementation = fields(screen["implementation"], ("code_components", "assets", "fallback"), f"{path}.implementation")
        string_list(implementation["code_components"], f"{path}.code_components")
        text_value(implementation["fallback"], f"{path}.fallback")
        require(isinstance(implementation["assets"], list), f"{path}.assets: 需要数组")
        for asset in implementation["assets"]:
            fields(asset, ("id", "description", "background", "aspect_ratio", "export", "crop_safe_area"), f"{path}.asset")
            for key, value in asset.items():
                text_value(value, f"{path}.asset.{key}")
            require(asset["id"] not in assets, f"asset.id: 重复 {asset['id']}")
            assets.add(asset["id"])
            require(asset["background"] in ("transparent", "opaque"), "asset.background: 只支持 transparent/opaque")
    for screen in screens:
        for key in ("primary_action", "secondary_action"):
            action = screen["interaction"][key]
            if action.startswith("next:"):
                target = action[5:]
                require(target in ids and target != screen["id"], f"{screen['id']}.{key}: 无效 next 目标")
    hints = fields(flow["implementation_hints"], HINT_KEYS, "implementation_hints")
    for key in HINT_KEYS:
        string_list(hints[key], f"implementation_hints.{key}")
    validate_review(flow)


def render(profile, flow):
    lock = compact({key: profile[key] for key in STYLE_KEYS})
    digest = hashlib.sha256(lock.encode("utf-8")).hexdigest()
    negatives = list(dict.fromkeys(DEFAULT_NEGATIVES + profile["negative_constraints"] + flow["negative_constraints"]))
    negative = "\n".join(f"- {item}" for item in negatives)
    global_prompt = (
        "设计一组可实现的移动 App 首次启动引导。逐字遵守同一 STYLE_LOCK，"
        "只能在允许范围内改变产品主体、场景和布局变体，不添加另一套颜色/字体/材质/光源。"
        "主视觉解释产品能力，文案与导航保持留白和清楚层级，安全区与字号动态适配。\n\n"
        f"STYLE_LOCK_SHA256: {digest}\nSTYLE_LOCK: {lock}\n\n全局禁止事项：\n{negative}"
    )
    context = compact({key: flow[key] for key in ("project", "platform", "locale", "assumptions")})
    screen_blocks = []
    for i, screen in enumerate(flow["screens"], 1):
        common = f"{global_prompt}\n\n项目上下文（产品事实与假设）：{context}\n\n本页完整要求：{compact(screen)}"
        screen_blocks.append(
            f"### {i}. {screen['id']} · {screen['title']}\n\n"
            f"**共同提示词（完整复制）**\n\n```text\n{common}\n```\n\n"
            "**目标指令：UI 整页**\n\n"
            "输出单张移动 App 内容画布，按本页精确标题、说明、主/次按钮和进度排版；"
            "遵从基准比例及安全区。无设备外壳、无拼页、无海报边框。"
            "示意数据按项目假设处理；文字误差在实现时用原生排版校正。\n\n"
            "**目标指令：纯主视觉资源**\n\n"
            "仅绘制本页 implementation.assets 指定的资源；多个资源逐个输出。"
            "继承 STYLE_LOCK 的色板、材质、光照、镜头和构图语言，"
            "忽略整页文字、按钮与导航的绘制要求。按各资源 background、比例及保护区导出，"
            "不含文字、数字、状态栏、CTA、进度或设备外壳。资源数组为空时无需出图，用代码绘制。\n\n"
            "**目标指令：原生 UI 实现**\n\n"
            f"面向 {flow['platform']}，按项目原生框架实现本页；SwiftUI 项目用共享 DesignTokens、"
            "页面数据模型、原生文案与导航控件，按 asset ID 引用资源，不把整屏图作为 UI。"
            "实现 primary_action、secondary_action、返回、完成与权限时机，遵守"
            " fallback、动态文字、安全区和 Reduce Motion；具体 API 按部署目标核对。"
            "仅在用户要求实现时执行，按 F 节交接。"
        )
    summary = "\n".join(f"{i}. **{s['title']}** — {s['goal']}；能力：{s['feature']}。"
                        for i, s in enumerate(flow["screens"], 1))
    hint_labels = ("代码与组件", "视觉资源", "屏幕适配", "可访问性与动效", "状态与导航")
    hints = "\n\n".join(f"### {label}\n\n" + "\n".join(f"- {v}" for v in flow["implementation_hints"][key])
                         for key, label in zip(HINT_KEYS, hint_labels))
    review = flow["quality_review"]
    review_text = ("方案级检查，未执行图像渲染、原生编译或设备运行验收。"
                   if review["scope"] == "plan-only" else
                   "已声明执行渲染审查；验证范围以以下逐项证据为准，不代表已执行原生编译或设备验收。")
    review_text += "\n\n" + "\n".join(
        f"- `{key}` · {review['checks'][key]['status']}：{review['checks'][key]['evidence']}；"
        f"修正：{review['checks'][key]['fix']}" for key in CHECKS)
    return (ROOT / "templates/prompt-template.md").read_text(encoding="utf-8").format(
        project_name=flow["project"]["name"],
        context="以下 JSON 为本次方案的数据源。来源与推断见 provenance/assumptions；检查证据见文末。",
        style_profile_json=pretty(profile).rstrip(), flow_summary=summary,
        flow_json=pretty(flow).rstrip(), global_prompt=global_prompt,
        screen_prompts="\n\n".join(screen_blocks), negative_prompt=negative,
        implementation_hints=hints, quality_review=review_text,
        reuse_note=f"复用：将 A 节保存为 `{profile['style_id']}.json`，通过 save-profile 存入本地目录。"
        "后续先用 style_id 加载，再针对新产品重写 Flow；无需重新上传原图。"
        "相同输入的提示词拼装确定性一致；图像生成仍可能存在随机性。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "save-profile", "build"):
        p = sub.add_parser(command)
        p.add_argument("--profile", required=True, type=Path)
        if command in ("validate", "build"):
            p.add_argument("--flow", required=command == "build", type=Path)
        if command == "save-profile":
            p.add_argument("--store", required=True, type=Path)
        if command == "build":
            p.add_argument("--output", required=True, type=Path)
    p = sub.add_parser("load-profile")
    p.add_argument("--style-id", required=True)
    p.add_argument("--store", required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == "load-profile":
            source = args.store / f"{style_id(args.style_id)}.json"
            profile = read_json(source)
            validate_profile(profile)
            require(profile["style_id"] == args.style_id, "存储文件名与内部 style_id 不一致")
            sys.stdout.write(pretty(profile))
            return 0
        profile = read_json(args.profile)
        validate_profile(profile)
        flow = None
        if getattr(args, "flow", None):
            flow = read_json(args.flow)
            validate_flow(flow, profile)
        if args.command == "save-profile":
            args.store.mkdir(parents=True, exist_ok=True)
            target = args.store / f"{profile['style_id']}.json"
            if target.exists():
                require(compact(read_json(target)) == compact(profile), f"同 ID 已存在不同内容: {target}；请派生新 style_id")
            else:
                with target.open("x", encoding="utf-8") as handle:
                    handle.write(pretty(profile))
            print(target.resolve())
        elif args.command == "build":
            validate_review(flow, required=True)
            require(args.output.suffix.lower() == ".md", "output: 请使用 .md 扩展名")
            require(args.output.resolve() not in (args.profile.resolve(), args.flow.resolve(),
                    (ROOT / "templates/prompt-template.md").resolve()), "output: 不得覆盖输入文件或模板")
            output = render(profile, flow)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
            print(args.output.resolve())
        else:
            print("结构校验通过；仍需按七维验收检查语义和实际视觉结果。")
        return 0
    except (OSError, ValueError) as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

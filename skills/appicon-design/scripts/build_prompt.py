#!/usr/bin/env python3
"""appicon-design 提示词拼装与风格管理脚本（仅依赖标准库）。

风格段（style / composition:<layout> / negative / avoid）逐字取自 styles/<id>/style.md，保证同一风格下的提示词完全一致。

风格模板 = 可复用的设计 DNA（style）+ 多个版式变体（composition:<layout>）+ 参考图 IP 排除（avoid / ip_terms）。
脚本始终注入「原创性约束」，防止生成结果与参考图的主体、角色、轮廓、布局雷同。

用法:
  build_prompt.py --list
  build_prompt.py --layouts <id>            # 列出某风格的版式变体
  build_prompt.py --auto "项目描述"
  build_prompt.py --catalog                 # 重新生成 README.md 风格目录
  build_prompt.py --new <id> --name <中文名> --ref <图片> [--ref ...]
  build_prompt.py --style <id> --subject "<主体描述>" [--layout NAME] [--shape square|squircle]
                  [--label TEXT] [--with-ref] [--format text|json]
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = ROOT / "styles"

# 画布形状 → 呈现方式
SHAPES = {
    "square": (
        "Full-bleed square 1024x1024 iOS app icon artwork with sharp square corners: the artwork covers the whole canvas, "
        "no rounded corners, no border, no transparency, because the system applies the corner mask later.",
        ["rounded corners", "white border", "frame around the icon", "transparent background"],
    ),
    "squircle": (
        "Presented as a finished iOS app icon: a rounded-square (squircle) tile with smooth continuous corners, "
        "centered on a pure white background with an even margin.",
        ["sharp square corners", "circle-shaped icon"],
    ),
}

# 通用 iOS App Icon 规则（所有风格共享）
IOS_RULES = (
    "Follows iOS app icon design principles: {subject_rule}, "
    "important details kept inside the central 80% safe area and away from the corners, bold readable shapes "
    "and strong value contrast so it stays recognizable at 60px, simple and uncluttered."
)
GENERIC_NEGATIVE = [
    "photo collage", "screenshot", "UI elements", "multiple subjects", "busy background",
    "tiny unreadable details", "blurry", "low resolution", "jpeg artifacts", "watermark", "signature", "brand logo",
]
NO_TEXT_NEGATIVE = ["text", "letters", "words", "numbers", "typography", "gibberish lettering"]
LABEL_NEGATIVE = ["any other text", "extra words", "misspelled letters", "gibberish lettering"]

# 原创性约束（所有风格共享）：只借用渲染语言，不借用参考图的内容
ORIGINALITY = (
    "Original artwork designed for this specific app: borrow only the rendering language described above "
    "(materials, lighting, palette roles, texture, mood), never the subject, character, silhouette, layout "
    "or branding of any existing app icon or reference image."
)
ORIGINALITY_REF = (
    "Any attached reference image is a style reference only: match its materials, lighting and color feel, "
    "but do not reproduce its subject, character, object, silhouette, layout, proportions or any text from it."
)
ORIGINALITY_NEGATIVE = [
    "copy of the reference image", "same subject as the reference", "same character as the reference",
    "same layout as the reference", "existing app icon", "famous logo", "trademarked character",
]


def parse_style(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta = {}
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if fm:
        for line in fm.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"')
    blocks = dict(re.findall(r"```(style|negative|avoid)\n(.*?)\n```", text, re.S))
    missing = {"style", "negative"} - blocks.keys()
    # 版式变体：```composition:<layout>```；兼容旧格式 ```composition```（记为 default）
    layouts = {
        (name or "default"): " ".join(body.split())
        for name, body in re.findall(r"```composition(?::([a-z0-9-]+))?\n(.*?)\n```", text, re.S)
    }
    if not layouts:
        missing.add("composition")
    if missing:
        raise ValueError(f"{path} 缺少代码块: {', '.join(sorted(missing))}")
    for key in ("style", "negative"):
        meta[key] = " ".join(blocks[key].split())
    meta["avoid"] = " ".join(blocks.get("avoid", "").split())
    meta["layouts"] = layouts
    meta["keywords"] = [k.strip().lower() for k in meta.get("keywords", "").split(",") if k.strip()]
    meta["ip_terms"] = [k.strip().lower() for k in meta.get("ip_terms", "").split(",") if k.strip()]
    meta["ip_labels"] = [norm_label(k) for k in meta.get("ip_labels", "").split(",") if k.strip()]
    meta["references"] = [r.strip() for r in meta.get("references", "reference.png").split(",") if r.strip()]
    meta["dir"] = path.parent
    return meta


def load_styles() -> dict:
    styles = {}
    for path in sorted(STYLES_DIR.glob("*/style.md")):
        style = parse_style(path)
        styles[style.get("id", path.parent.name)] = style
    return styles


def norm_label(text: str) -> str:
    return re.sub(r"\s+", "", text).casefold()


def split_terms(text: str) -> list:
    return [t.strip() for t in text.split(",") if t.strip()]


def ip_hits(style: dict, subject: str, label: str) -> list:
    """检查主体描述 / 字样是否命中参考图 IP 词（ip_terms）或参考图原字样（ip_labels）。"""
    joined = f"{subject} {label}".lower()
    hits = [f'label "{label}"'] if label and norm_label(label) in style["ip_labels"] else []
    for term in style["ip_terms"]:
        found = re.search(rf"\b{re.escape(term)}\b", joined) if term.isascii() else term in joined
        if found:
            hits.append(term)
    return hits


def build(style: dict, subject: str, shape: str, label: str | None, layout: str, with_ref: bool) -> dict:
    shape_text, shape_negative = SHAPES[shape]
    composition = style["layouts"][layout]
    paired = style.get("subject_layout") == "paired"
    subject_rule = (
        "one cohesive visual group with a dominant subject and a smaller overlapping companion, balanced as a single focal point"
        if paired else "one clear subject and a single focal point, centered and balanced"
    )
    generic_negative = [t for t in GENERIC_NEGATIVE if not (paired and t == "multiple subjects")]
    negative = split_terms(style["negative"]) + split_terms(style["avoid"])
    if shape == "squircle":
        # 展示模式：「铺满画布」改为「铺满图标底板」，并移除与白色外边距冲突的负向词
        composition = composition.replace("canvas", "icon tile")
        negative = [t for t in negative if not any(k in t for k in ("margin", "white border", "white background"))]

    parts = [f"An iOS app icon. Subject: {subject.rstrip('.')}.", style["style"], composition]
    if style.get("lettering") == "required":
        # 字母标风格：文字即主体
        parts.append(
            f'The letters are exactly "{label}" and nothing else, rendered as {style["label_style"]}, '
            "every letter clearly legible and spelled exactly."
        )
        negative += LABEL_NEGATIVE
    elif label:
        parts.append(
            f'The only lettering on the icon is the word "{label}", rendered as {style["label_style"]}, '
            "kept small and away from the focal part, crisp and spelled exactly."
        )
        negative += LABEL_NEGATIVE
    else:
        parts.append("No text, letters or numbers anywhere on the icon.")
        negative += NO_TEXT_NEGATIVE
    parts.append(ORIGINALITY)
    if with_ref:
        parts.append(ORIGINALITY_REF)
    parts += [IOS_RULES.format(subject_rule=subject_rule), shape_text]
    negative = list(dict.fromkeys(negative + ORIGINALITY_NEGATIVE + generic_negative + shape_negative))

    prompt = " ".join(parts)
    negative_text = ", ".join(negative)
    refs = [str(style["dir"] / r) for r in style["references"] if (style["dir"] / r).exists()] if with_ref else []
    warnings = []
    hits = ip_hits(style, subject, label or "")
    if hits:
        warnings.append(
            f"主体描述命中参考图 IP 词: {', '.join(hits)}。请更换隐喻 / 物件 / 角色，避免与参考图撞脸。"
        )
    return {
        "style": style.get("id"),
        "style_name": style.get("name"),
        "layout": layout,
        "shape": shape,
        "size": "1024x1024",
        "aspect_ratio": "1:1",
        "prompt": prompt,
        "negative_prompt": negative_text,
        "prompt_with_negatives": f"{prompt} Avoid: {negative_text}.",
        "reference_images": refs,
        "warnings": warnings,
    }


def auto_select(styles: dict, text: str) -> list:
    text = text.lower()
    scores = []
    for sid, style in styles.items():
        # 英文关键词按单词边界匹配，避免 "ai" 误中 "email" 之类
        hits = [k for k in style["keywords"] if (re.search(rf"\b{re.escape(k)}\b", text) if k.isascii() else k in text)]
        scores.append((len(hits), sid, hits))
    return sorted(scores, key=lambda x: -x[0])


def create_style(sid: str, name: str, refs: list) -> Path:
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", sid):
        raise ValueError("风格 ID 需为小写短横线格式，如 retro-stripe")
    target = STYLES_DIR / sid
    if target.exists():
        raise ValueError(f"风格 {sid} 已存在: {target}")
    sources = [Path(r).expanduser() for r in refs]
    for src in sources:
        if not src.is_file():
            raise ValueError(f"参考图不存在: {src}")
    target.mkdir(parents=True)
    names = []
    for i, src in enumerate(sources, 1):
        dest = f"reference{'' if i == 1 else f'-{i}'}{src.suffix.lower()}"
        shutil.copyfile(src, target / dest)
        names.append(dest)
    template = (STYLES_DIR / "_template.md").read_text(encoding="utf-8")
    content = (
        template.replace("<style-id>", sid)
        .replace("<中文名>", name)
        .replace("references: reference.png", f"references: {', '.join(names)}")
    )
    out = target / "style.md"
    out.write_text(content, encoding="utf-8")
    return out


def write_catalog(styles: dict) -> Path:
    """生成 skill 根目录的 README.md，便于在 GitHub 等网页直接预览全部风格。"""
    lines = [
        "# App Icon 风格目录",
        "",
        "> 本文件由 `python3 scripts/build_prompt.py --catalog` 自动生成，请勿手动编辑。匹配规则见 [styles/index.md](styles/index.md)。",
        "",
        f"共 {len(styles)} 套风格。",
        "",
        "| 参考图 | 风格 | 描述 | 色板 |",
        "|---|---|---|---|",
    ]
    for sid, style in styles.items():
        imgs = " ".join(
            f'<a href="styles/{sid}/{r}"><img src="styles/{sid}/{r}" height="160" alt="{sid}"></a>'
            for r in style["references"]
        )
        text = (style["dir"] / "style.md").read_text(encoding="utf-8")
        colors = list(dict.fromkeys(re.findall(r"`(#[0-9A-Fa-f]{6})`", text)))
        palette = " ".join(f"`{c}`" for c in colors)
        lines.append(
            f"| {imgs} | **[{style.get('name', sid)}](styles/{sid}/style.md)**<br>`{sid}` "
            f"| {style.get('summary', '')} | {palette} |"
        )
    out = ROOT / "README.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="appicon-design 提示词拼装与风格管理")
    parser.add_argument("--list", action="store_true", help="列出全部风格")
    parser.add_argument("--layouts", metavar="ID", help="列出某风格的版式变体")
    parser.add_argument("--auto", metavar="TEXT", help="按关键词为项目描述推荐风格")
    parser.add_argument("--catalog", action="store_true", help="重新生成 README.md 风格目录")
    parser.add_argument("--new", metavar="ID", help="新建风格骨架")
    parser.add_argument("--name", help="新风格中文名（配合 --new）")
    parser.add_argument("--ref", action="append", default=[], help="新风格参考图路径，可重复（配合 --new）")
    parser.add_argument("--style", help="风格 ID")
    parser.add_argument("--subject", help="主体描述（英文）")
    parser.add_argument("--layout", help="版式变体名（默认取该风格第一个版式，见 --layouts）")
    parser.add_argument("--with-ref", action="store_true",
                        help="输出参考图路径并注入「参考图仅作风格参考」约束（默认不附带参考图，降低 IP 复制风险）")
    parser.add_argument("--shape", choices=SHAPES.keys(), help="画布形状（默认取风格的 default_shape，否则 square）")
    parser.add_argument("--label", help="图标上唯一允许出现的品牌字样（风格需定义 label_style）；字母标风格中即为主体字母，数量见风格规范")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    if args.new:
        if not args.name or not args.ref:
            parser.error("--new 需要同时提供 --name 与至少一个 --ref")
        try:
            out = create_style(args.new, args.name, args.ref)
        except ValueError as e:
            parser.error(str(e))
        print(f"已创建 {out}，请按模板填写后在 styles/index.md 登记并执行 --catalog")
        return 0

    styles = load_styles()

    if args.list:
        for sid, style in styles.items():
            print(f"{sid}\t{style.get('name', '')}\tlayouts={','.join(style['layouts'])}\t{style.get('summary', '')}")
        return 0

    if args.layouts:
        if args.layouts not in styles:
            parser.error(f"未知风格 {args.layouts}，可选: {', '.join(styles)}")
        for name, text in styles[args.layouts]["layouts"].items():
            print(f"[{name}]\n{text}\n")
        return 0

    if args.catalog:
        print(f"已生成 {write_catalog(styles)}")
        return 0

    if args.auto:
        ranking = auto_select(styles, args.auto)
        for score, sid, hits in ranking:
            print(f"{sid}\tscore={score}\thits={','.join(hits) or '-'}")
        if not ranking or ranking[0][0] == 0:
            print("# 无关键词命中，请按 styles/index.md 的调性规则人工判断", file=sys.stderr)
        return 0

    if not args.style or not args.subject:
        parser.error("需要 --style 与 --subject（或使用 --list / --auto / --catalog / --new）")
    if args.style not in styles:
        parser.error(f"未知风格 {args.style}，可选: {', '.join(styles)}")
    style = styles[args.style]
    if args.label and not style.get("label_style"):
        parser.error(f"风格 {args.style} 未定义 label_style，不允许出现文字")
    if style.get("lettering") == "required" and not args.label:
        parser.error(f"风格 {args.style} 是字母标风格，需要用 --label 指定字母，数量见该风格的主体转译规则")

    shape = args.shape or style.get("default_shape") or "square"
    if shape not in SHAPES:
        parser.error(f"风格 {args.style} 的 default_shape 无效: {shape}")
    layout = args.layout or next(iter(style["layouts"]))
    if layout not in style["layouts"]:
        parser.error(f"风格 {args.style} 没有版式 {layout}，可选: {', '.join(style['layouts'])}")
    result = build(style, args.subject, shape, args.label, layout, args.with_ref)
    for w in result["warnings"]:
        print(f"# WARNING: {w}", file=sys.stderr)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"# Style: {result['style_name']} ({result['style']})  Layout: {result['layout']}  "
              f"Shape: {result['shape']}  Size: {result['size']}")
        print(f"# References: {', '.join(result['reference_images']) or '未附带（默认，降低 IP 复制风险；需要时加 --with-ref）'}\n")
        print("## Prompt\n" + result["prompt"] + "\n")
        print("## Negative Prompt\n" + result["negative_prompt"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

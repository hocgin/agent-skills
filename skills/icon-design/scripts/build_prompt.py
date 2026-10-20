#!/usr/bin/env python3
"""icon-design 提示词拼装脚本（仅依赖标准库）。

固定风格段（style / negative）逐字取自 themes/<id>/theme.md，保证同一主题下的提示词完全一致。

用法:
  build_prompt.py --list
  build_prompt.py --auto "项目描述"
  build_prompt.py --theme <id> --subject "<主体描述>" [--subject ...] [--mode showcase|standalone|app-icon] [--format text|json]
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

THEMES_DIR = Path(__file__).resolve().parent.parent / "themes"

# 用途模式 → 背景/容器描述（单个, 成套）
MODES = {
    "showcase": (
        "Placed on a soft light-gray ({tile}) circle centered on a pure white background, like an icon specimen sheet.",
        "Each icon sits on its own soft light-gray ({tile}) circle, all circles the same size, on a pure white background.",
    ),
    "standalone": (
        "On a pure white background with no container, easy to cut out.",
        "On a pure white background with no containers, easy to cut out.",
    ),
    "app-icon": (
        "Presented as an app icon: the subject sits centered on a rounded-square (squircle) tile filled with flat {tile} that fills the whole canvas, with even padding.",
        "Each icon sits on its own rounded-square (squircle) app icon tile filled with flat {tile}, all tiles the same size, on a pure white background.",
    ),
}


def parse_theme(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta = {}
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if fm:
        for line in fm.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"')
    blocks = dict(re.findall(r"```(style|negative)\n(.*?)\n```", text, re.S))
    if "style" not in blocks or "negative" not in blocks:
        raise ValueError(f"{path} 缺少 style 或 negative 代码块")
    meta["style"] = " ".join(blocks["style"].split())
    meta["negative"] = " ".join(blocks["negative"].split())
    meta["keywords"] = [k.strip().lower() for k in meta.get("keywords", "").split(",") if k.strip()]
    meta["dir"] = path.parent
    return meta


def load_themes() -> dict:
    themes = {}
    for path in sorted(THEMES_DIR.glob("*/theme.md")):
        theme = parse_theme(path)
        themes[theme.get("id", path.parent.name)] = theme
    return themes


def build(theme: dict, subjects: list, mode: str) -> dict:
    tile = theme.get("tile_color", "#F5F5F5")
    single_bg, set_bg = MODES[mode]
    n = len(subjects)
    if n == 1:
        head = f"A single flat vector icon of {subjects[0].rstrip('.')}."
        background = single_bg.format(tile=tile)
        size = "1:1"
    else:
        cols = 2 if n <= 4 else 3
        rows = math.ceil(n / cols)
        items = "; ".join(f"({i}) {s.rstrip('.')}" for i, s in enumerate(subjects, 1))
        head = (
            f"A matching set of {n} flat vector icons arranged in an evenly spaced {cols}x{rows} grid, "
            f"every icon drawn in exactly the same style, stroke weight, palette and scale: {items}."
        )
        background = set_bg.format(tile=tile)
        size = "1:1" if cols == rows else f"{cols}:{rows}"
    style, negative = theme["style"], theme["negative"]
    if n > 1:
        # 成套模式：构图占比改为按单元格计算，并移除与网格冲突的负向词
        style = style.replace("Subject centered, occupying about 45% of the canvas", "Each icon centered in its own grid cell, occupying about 45% of the cell")
        negative = ", ".join(t for t in negative.split(", ") if t != "multiple subjects")
    prompt = f"{head} {style} {background}"
    ref = theme["dir"] / theme.get("reference", "reference.jpg")
    return {
        "theme": theme.get("id"),
        "theme_name": theme.get("name"),
        "mode": mode,
        "size": size,
        "prompt": prompt,
        "negative_prompt": negative,
        "prompt_with_negatives": f"{prompt} Avoid: {negative}.",
        "reference_image": str(ref) if ref.exists() else None,
    }


def auto_select(themes: dict, text: str) -> list:
    text = text.lower()
    scores = []
    for tid, theme in themes.items():
        hits = [k for k in theme["keywords"] if k in text]
        scores.append((len(hits), tid, hits))
    return sorted(scores, key=lambda x: -x[0])


def main() -> int:
    parser = argparse.ArgumentParser(description="icon-design 提示词拼装")
    parser.add_argument("--list", action="store_true", help="列出全部主题")
    parser.add_argument("--auto", metavar="TEXT", help="按关键词为项目描述推荐主题")
    parser.add_argument("--theme", help="主题 ID")
    parser.add_argument("--subject", action="append", default=[], help="主体描述（英文），可重复以生成成套图标")
    parser.add_argument("--mode", choices=MODES.keys(), default="showcase", help="用途模式")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    themes = load_themes()

    if args.list:
        for tid, theme in themes.items():
            print(f"{tid}\t{theme.get('name', '')}\t{theme.get('summary', '')}")
        return 0

    if args.auto:
        ranking = auto_select(themes, args.auto)
        for score, tid, hits in ranking:
            print(f"{tid}\tscore={score}\thits={','.join(hits) or '-'}")
        if ranking[0][0] == 0:
            print("# 无关键词命中，请按 themes/index.md 的调性规则人工判断", file=sys.stderr)
        return 0

    if not args.theme or not args.subject:
        parser.error("需要 --theme 与至少一个 --subject（或使用 --list / --auto）")
    if args.theme not in themes:
        parser.error(f"未知主题 {args.theme}，可选: {', '.join(themes)}")
    if len(args.subject) > 6:
        parser.error("单次最多 6 个主体，请分批生成并附参考图保持一致")

    result = build(themes[args.theme], args.subject, args.mode)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"# Theme: {result['theme_name']} ({result['theme']})  Mode: {result['mode']}  Size: {result['size']}")
        print(f"# Reference: {result['reference_image']}\n")
        print("## Prompt\n" + result["prompt"] + "\n")
        print("## Negative Prompt\n" + result["negative_prompt"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

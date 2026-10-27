# 参考图编辑与多图输入

以下示例在 agent-skills 仓库根目录执行，输出父目录需要提前创建。`--ref` 对应 PR #5 的功能，可重复传入，相对路径按调用时工作目录解析。

## 只修改一项

```bash
./skills/gpt-image-bridge/bin/gpt-image-2 \
  "Recreate this image, changing only the balloon color to green. Keep the framing, balloon position, ribbon, lighting and clouds unchanged." \
  /tmp/green-balloon.png \
  --ref /tmp/gpt-image-bridge-output/balloon.png \
  --size 1024x1024
```

图片会整张重新生成，不能保证未修改区域的像素完全一致，也不保证指定尺寸严格生效。不要对用户承诺无损局部编辑。

## 主体和风格分开参考

```bash
./skills/gpt-image-bridge/bin/gpt-image-2 \
  "Use the bottle from the first image as the product. Use the second image only for lighting and color palette. Place the bottle on a marble counter, keeping its shape and label." \
  /tmp/product-hero.png \
  --ref ./shots/bottle.png \
  --ref "./mood board/style.jpg" \
  --size 1792x1024
```

按传入顺序说明图片各自用途。将上例文件路径替换为实际存在的文件；缺失任何参考图时脚本都会在启动 Codex 前退出 `2`。

优先使用当前 Codex 支持的 PNG/JPEG 等格式。若 HEIC 等输入格式不被支持，先转为支持的格式，再传给 `--ref`。

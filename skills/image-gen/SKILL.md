---
name: image-gen
description: 基于 APIMart GPT-Image-2 官方渠道的图像生成。支持文生图、图生图(多参考图融合)、局部重绘(mask)。异步任务模式, 需 APIMART_API_KEY 环境变量。当用户需要生成图片、编辑图片、局部重绘时使用此 skill。
---

# image-gen

基于 **APIMart GPT-Image-2 官方渠道** 的图像生成 skill。支持文生图、图生图、局部重绘, 异步任务模式。

API 文档: https://docs.apimart.ai/cn/api-reference/images/gpt-image-2/official

## 前置条件

### 1. 检查 API Key

```bash
test -n "$APIMART_API_KEY" && echo "OK_KEY" || echo "NO_KEY"
```

### 2. 若无 API Key

引导用户:

> 需要先配置 APIMart API Key:
>
> 1. 访问 [APIMart 控制台](https://apimart.ai) 注册并获取 API Key
> 2. 在终端中设置环境变量:
>
> ```bash
> export APIMART_API_KEY="your_api_key_here"
> ```
>
> 建议将上述命令加入 `~/.zshrc` 或 `~/.bashrc` 持久化。

## API 端点

- **提交任务**: `POST https://api.apimart.ai/v1/images/generations`
- **查询任务**: `GET https://api.apimart.ai/v1/tasks/{task_id}`
- **批量查询**: `POST https://api.apimart.ai/v1/tasks/batch`

## 请求参数

| 参数 | 类型 | 默认值 | 必填 | 说明 |
|------|------|--------|------|------|
| `model` | string | `gpt-image-2-official` | 是 | 固定值 |
| `prompt` | string | - | 是 | 图像描述, 支持中英文, 建议英文 |
| `size` | string | `1:1` | 否 | 画面比例, 见下方映射表 |
| `resolution` | string | `1k` | 否 | 分辨率档位: `1k`/`2k`/`4k` |
| `quality` | string | `auto` | 否 | `auto`/`low`/`medium`/`high` |
| `background` | string | `auto` | 否 | `auto`/`opaque`/`transparent`(不支持, 会降级为 auto) |
| `moderation` | string | `auto` | 否 | `auto`/`low` |
| `output_format` | string | `png` | 否 | `png`/`jpeg`/`webp` |
| `output_compression` | integer | - | 否 | 压缩强度 0-100, 仅 jpeg/webp 有效 |
| `n` | integer | `1` | 否 | 生成张数, 1-4 |
| `image_urls` | array | - | 否 | 参考图 URL, 最多 16 张 |
| `mask_url` | string | - | 否 | 遮罩图 URL, 需搭配 image_urls |

### 支持的比例

`auto`/`1:1`/`3:2`/`2:3`/`4:3`/`3:4`/`5:4`/`4:5`/`16:9`/`9:16`/`2:1`/`1:2`/`3:1`/`1:3`/`21:9`/`9:21`

也支持直接传像素尺寸, 如 `3840x2160`。

### 尺寸 x 分辨率映射表

| size | 1k | 2k | 4k |
|------|------|------|------|
| 1:1 | 1024x1024 | 2048x2048 | 2880x2880 |
| 3:2 | 1536x1024 | 2048x1360 | 3520x2336 |
| 2:3 | 1024x1536 | 1360x2048 | 2336x3520 |
| 4:3 | 1024x768 | 2048x1536 | 3312x2480 |
| 3:4 | 768x1024 | 1536x2048 | 2480x3312 |
| 5:4 | 1280x1024 | 2560x2048 | 3216x2576 |
| 4:5 | 1024x1280 | 2048x2560 | 2576x3216 |
| 16:9 | 1536x864 | 2048x1152 | 3840x2160 |
| 9:16 | 864x1536 | 1152x2048 | 2160x3840 |
| 2:1 | 2048x1024 | 2688x1344 | 3840x1920 |
| 1:2 | 1024x2048 | 1344x2688 | 1920x3840 |
| 3:1 | 1536x512 | 3072x1024 | 3840x1280 |
| 1:3 | 512x1536 | 1024x3072 | 1280x3840 |
| 21:9 | 2016x864 | 2688x1152 | 3840x1648 |
| 9:21 | 864x2016 | 1152x2688 | 1648x3840 |

## 工作流程

### Step 1: 提交任务

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "PROMPT_AQUI",
    "size": "1:1",
    "resolution": "1k",
    "quality": "medium",
    "n": 1
  }'
```

返回:

```json
{
  "code": 200,
  "data": [
    {
      "status": "submitted",
      "task_id": "task_01KPTXXXXXXXXXXXXXXX"
    }
  ]
}
```

### Step 2: 轮询任务状态

等待 10-20 秒后开始查询, 间隔 3-5 秒:

```bash
curl -s "https://api.apimart.ai/v1/tasks/TASK_ID_PLACEHOLDER" \
  -H "Authorization: Bearer $APIMART_API_KEY"
```

任务状态流转: `submitted` -> `in_progress` -> `completed` / `failed`

### Step 3: 获取结果

成功响应:

```json
{
  "code": 200,
  "data": {
    "id": "task_01KPTXXXXXXXXXXXXXXX",
    "status": "completed",
    "progress": 100,
    "actual_time": 46,
    "cost": 0.05279,
    "result": {
      "images": [
        {
          "url": [
            "https://upload.apimart.ai/f/image/xxxxxxxx-gpt_image_2_official_task_xxx_0.png"
          ],
          "expires_at": 1776928569
        }
      ]
    }
  }
}
```

取图地址: `data.result.images[0].url[0]`

### Step 4: 下载图片

```bash
curl -sL -o OUTPUT_PATH "IMAGE_URL"
```

### 完整脚本示例(提交 + 轮询 + 下载)

```bash
API_KEY="$APIMART_API_KEY"
OUT_DIR="${OUT_DIR:-/tmp/apimart-images}"
mkdir -p "$OUT_DIR"

# 1. 提交任务
RESPONSE=$(curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "A serene Japanese garden with cherry blossoms and a stone bridge, golden hour lighting",
    "size": "16:9",
    "resolution": "2k",
    "quality": "medium",
    "n": 1
  }')

TASK_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['task_id'])")
echo "任务已提交: $TASK_ID"

# 2. 等待后开始轮询
sleep 15

for i in $(seq 1 40); do
  RESULT=$(curl -s "https://api.apimart.ai/v1/tasks/$TASK_ID" \
    -H "Authorization: Bearer $API_KEY")

  STATUS=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['status'])")

  if [ "$STATUS" = "completed" ]; then
    echo "生成完成"
    IMAGE_URL=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['result']['images'][0]['url'][0])")
    curl -sL -o "$OUT_DIR/${TASK_ID}.png" "$IMAGE_URL"
    echo "图片已保存: $OUT_DIR/${TASK_ID}.png"
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "任务失败: $RESULT"
    break
  else
    echo "状态: $STATUS (第 $i 次查询)"
    sleep 5
  fi
done
```

## 使用场景

### 文生图(最简)

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-image-2-official", "prompt": "星空下的古老城堡"}'
```

### 2K 高清海报

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "赛博朋克夜景",
    "size": "16:9",
    "resolution": "2k",
    "quality": "high",
    "output_format": "jpeg",
    "output_compression": 90
  }'
```

### 图生图(多参考图融合)

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "将两张参考图融合成一张插画海报，保留主体轮廓",
    "size": "1:1",
    "quality": "high",
    "image_urls": [
      "https://your-cdn.com/input-a.png",
      "https://your-cdn.com/input-b.png"
    ]
  }'
```

### 局部重绘(mask)

遮罩图需有 Alpha 通道, 尺寸需与首张参考图一致。

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "把背景换成沙漠日落",
    "size": "1:1",
    "quality": "medium",
    "image_urls": ["https://your-cdn.com/photo.png"],
    "mask_url": "https://your-cdn.com/mask.png"
  }'
```

### 批量生成(n > 1)

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "Four minimalist poster variations of a red fox",
    "size": "1:1",
    "quality": "low",
    "n": 4
  }'
```

### 4K 壁纸

```bash
curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-official",
    "prompt": "雪山日出全景",
    "size": "16:9",
    "resolution": "4k",
    "quality": "high",
    "n": 1
  }'
```

## Prompt 编写原则

1. **用英文描述**。模型支持中文, 但英文效果更稳定。
2. **具体胜过抽象**。"Space-black MacBook Pro 16-inch M3 on a walnut desk" > "a laptop on desk"。
3. **描述构图而非意图**。"Medium shot, subject centered, banker lamp backlighting" > "dramatic portrait"。
4. **明确排除项**。"No emojis, no gradients, no stock photo aesthetic"。
5. **图片中的文字用引号**。`reads "Hello World"` -- 准确率约 99%。
6. ** cinematographic reference(如果适合风格)**。"In the visual style of Blade Runner 2049 desert scenes"。

## 轮询策略

| 条件 | 建议值 |
|------|--------|
| 首次查询延迟 | 10-20 秒 |
| 查询间隔 | 3-5 秒 |
| 超时时间 | >= 180 秒(high + 2k/4k 可达 130s) |

## Troubleshooting

**`401` 未授权**
API Key 无效或过期。检查 `APIMART_API_KEY` 环境变量, 到 [APIMart 控制台](https://apimart.ai) 重新获取。

**`402` 余额不足**
账户余额不够, 到 APIMart 控制台充值。

**`429` 限流**
请求过于频繁, 降低轮询频率或稍后重试。

**`400` 参数错误**
检查请求参数: model 是否为 `gpt-image-2-official`, size 是否在支持列表中, n 是否为 1-4。

**任务 `failed`**
可能是审核拦截(prompt 违规)或服务端错误。尝试修改 prompt 降低敏感度后重试。

**图片链接过期**
`data.result.images[0].expires_at` 是过期时间戳, 到期后链接失效。需及时下载。

**`high` + `4k` 耗时过长**
正常现象, 耗时可达 130 秒以上。客户端超时建议 >= 180 秒。

## 耗时与质量参考

| 分辨率 | quality | 预计耗时 | 适用场景 |
|--------|---------|----------|----------|
| 1k | low | ~10-20s | 草稿/预览 |
| 1k | medium | ~20-40s | 日常使用 |
| 2k | medium | ~30-60s | 海报/高清 |
| 2k | high | ~60-100s | 高质量输出 |
| 4k | high | ~100-130s | 壁纸/印刷 |

## 参考链接

- [API 文档](https://docs.apimart.ai/cn/api-reference/images/gpt-image-2/official)
- [APIMart 控制台](https://apimart.ai)
- [API Key 管理](https://apimart.ai/dashboard)

---
name: apple-itunes-api
description: |
  Apple iTunes Search API 完整参考指南。用于搜索 iTunes/Apple Music 目录中的音乐、电影、播客、应用、图书等内容。
  触发条件: 用户提及 "iTunes API"、"Apple Music API"、"搜索歌曲"、"查找专辑"、"获取歌词"、
  "搜索 App"、"查找播客"、"iTunes 搜索"、"获取封面"、"album art"、"track lookup" 等。
  涵盖 Search API、Lookup API、Genre API、RSS Feed Generator 四大端点。
source: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
metadata:
  trigger: 搜索 Apple 内容目录、获取 iTunes/App Store 元数据、查找音乐/电影/播客/应用/图书信息
---

# Apple iTunes Search API

无需认证的公开 REST API，用于搜索和获取 Apple 内容目录的元数据。

## 概览

| 端点 | 基础 URL | 用途 |
|------|----------|------|
| Search | `https://itunes.apple.com/search` | 关键词搜索 |
| Lookup | `https://itunes.apple.com/lookup` | 按 ID 精确查询 |
| Genre | `https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres` | 获取分类列表 |
| RSS Feed | `https://rss.itunes.apple.com/api/v1/{country}/{media}/{feed}/{genre}/{limit}/{format}` | 获取排行榜 |

---

## Search API

`GET https://itunes.apple.com/search`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `term` | string | 是 | 搜索关键词，需 URL 编码 |
| `country` | string | 否 | 两位国家代码，如 `US`、`CN`，默认 `US` |
| `media` | string | 否 | 媒体类型，见下表 |
| `entity` | string | 否 | 结果实体类型，需与 media 搭配 |
| `limit` | number | 否 | 返回数量，最大 200，默认 50 |
| `offset` | number | 否 | 分页偏移量 |
| `lang` | string | 否 | 返回结果的语言，如 `en_us`、`zh_cn` |
| `version` | number | 否 | API 版本，默认 2 |
| `callback` | string | 否 | JSONP 回调函数名 |

### media 值

| media 值 | 说明 |
|----------|------|
| `movie` | 电影 |
| `podcast` | 播客 |
| `music` | 音乐 |
| `musicVideo` | 音乐视频 |
| `audiobook` | 有声书 |
| `shortFilm` | 短片 |
| `tvShow` | 电视节目 |
| `software` | 应用 (iOS/Mac) |
| `ebook` | 电子书 |
| `all` | 全部 (默认) |

### entity 值 (与 media 搭配)

**music:**
`musicArtist`, `album`, `song`, `musicVideo`, `mix`, `genre`

**movie:**
`movieArtist`, `movie`, `genre`

**podcast:**
`podcastAuthor`, `podcast`

**software:**
`software`, `softwareDeveloper`, `iPadSoftware` -- 注意: `software` 适用于 iOS，`iPadSoftware` 适用于 iPad

**ebook:**
`ebook`, `audiobook`, `ebookAuthor`, `audiobookAuthor`

**all:**
`allArtist`, `allTrack`

**tvShow:**
`tvEpisode`, `tvSeason`, `tvShow` -- 注意: 默认不返回所有季的剧集，需指定 entity

### attribute 值 (限制搜索字段)

搭配 `media` 使用，限定搜索的匹配字段:

| attribute 值 | 适用 media |
|-------------|-----------|
| `actorTerm` | movie |
| `albumTerm` | music |
| `artistTerm` | music, podcast, musicVideo, shortFilm, tvShow, all |
| `artworkUrlTerm` | all |
| `authorTerm` | ebook |
| `collectionTerm` | all |
| `composerTerm` | all |
| `descriptionTerm` | all |
| `directorTerm` | movie, shortFilm, podcast |
| `editorTerm` | podcast |
| `genreIndex` | all |
| `keywordTerm` | software, ebook |
| `languageTerm` | software |
| `movieArtistTerm` | movie |
| `movieTerm` | movie |
| `podcastAuthorTerm` | podcast |
| `podcastTerm` | podcast |
| `producerTerm` | podcast |
| `ratingIndex` | all |
| `releaseYearTerm` | all |
| `songTerm` | music |
| `softwareDeveloperTerm` | software |
| `titleTerm` | all |
| `tvEpisodeTerm` | tvShow |
| `tvSeasonTerm` | tvShow |
| `tvShowTerm` | tvShow |

### 搜索示例

```bash
# 搜索歌曲
curl "https://itunes.apple.com/search?term=beatles&media=music&entity=song&limit=5"

# 搜索特定艺术家的专辑
curl "https://itunes.apple.com/search?term=radiohead&entity=album&limit=10"

# 搜索应用
curl "https://itunes.apple.com/search?term=wechat&entity=software&country=CN&limit=5"

# 按艺术家名称搜索
curl "https://itunes.apple.com/search?attribute=artistTerm&term=coldplay&entity=song&limit=5"

# 搜索电影
curl "https://itunes.apple.com/search?term=inception&entity=movie&limit=5"

# 搜索播客
curl "https://itunes.apple.com/search?term=true+crime&entity=podcast&limit=5"

# 分页搜索
curl "https://itunes.apple.com/search?term=pop&entity=song&limit=25&offset=50"

# 中文搜索
curl "https://itunes.apple.com/search?term=%E5%91%A8%E6%9D%B0%E4%BC%A6&country=CN&entity=song&limit=5"
```

---

## Lookup API

`GET https://itunes.apple.com/lookup`

通过 ID 精确查询内容详情，支持批量查询。

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | 否 | iTunes ID，多个 ID 用逗号分隔，最多 200 个 |
| `amgArtistId` | string | 否 | All Music Guide 艺术家 ID |
| `isbn` | string | 否 | 图书 ISBN |
| `upc` | string | 否 | 商品 UPC/EAN 码 |
| `entity` | string | 否 | 返回关联实体类型 |
| `limit` | number | 否 | 关联实体返回数量 |
| `country` | string | 否 | 两位国家代码 |
| `lang` | string | 否 | 返回结果的语言 |

> `id`、`amgArtistId`、`isbn`、`upc` 四选一

### Lookup 示例

```bash
# 按单个 ID 查询
curl "https://itunes.apple.com/lookup?id=909253"

# 批量查询 (多个 ID)
curl "https://itunes.apple.com/lookup?id=909253,252013914,294298906"

# 查询艺术家及其专辑
curl "https://itunes.apple.com/lookup?id=909253&entity=album&limit=5"

# 查询艺术家及其歌曲
curl "https://itunes.apple.com/lookup?id=909253&entity=song&limit=10"

# 按 AMG 艺术家 ID 查询
curl "https://itunes.apple.com/lookup?amgArtistId=468749&entity=album&limit=5"

# 按 ISBN 查询图书
curl "https://itunes.apple.com/lookup?isbn=9780316069359&country=US"

# 按 UPC 查询
curl "https://itunes.apple.com/lookup?upc=074646139324&country=US"
```

---

## Genre API

`GET https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres`

获取所有分类及其子分类的层级结构。

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | number | 否 | 媒体类型 ID，获取特定媒体的分类 |

### 媒体类型 ID

| 值 | 媒体 |
|----|------|
| 20 | Music |
| 22 | Podcasts |
| 23 | iBooks |
| 24 | Podcasts (旧) |
| 26 | Podcasts |
| 27 | iBooks |
| 28 | iBooks |
| 33 | Movies |
| 36 | Software (Apps) |
| 0 | 全部 (根节点) |

### Genre 示例

```bash
# 获取所有分类
curl "https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres"

# 获取音乐分类
curl "https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres?id=20"

# 获取应用分类
curl "https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres?id=36"
```

---

## RSS Feed Generator

`GET https://rss.itunes.apple.com/api/v1/{country}/{media}/{feed}/{genre}/{limit}/{format}`

获取各类排行榜数据。

### 路径参数

| 参数 | 说明 | 示例 |
|------|------|------|
| country | 两位国家代码 | `us`、`cn` |
| media | 媒体类型 | `apple-music`、`itunes-music`、`podcasts`、`apps`、`books`、`movies` |
| feed | 排行榜类型 | 见下表 |
| genre | 分类 ID 或 `all` | `all`、`1`、`21` 等 |
| limit | 返回数量，最大 200 | `10`、`50`、`100` |
| format | 返回格式 | `json`、`jsonp` |

### 常用 feed 值

**apple-music / itunes-music:**
`top-albums`, `top-songs`, `top-music-videos`, `new-releases`, `hot-tracks`

**podcasts:**
`top-podcasts`, `top-episodes`

**apps:**
`top-free-apps`, `top-paid-apps`, `top-grossing-apps`, `new-apps-we-love`, `top-free-iPad-apps`, `top-paid-iPad-apps`

**books:**
`top-free-books`, `top-paid-books`

**movies:**
`top-movies`, `top-rentals`

### RSS 示例

```bash
# Apple Music 热门歌曲
curl "https://rss.itunes.apple.com/api/v1/us/apple-music/top-songs/all/10/json"

# 热门免费应用
curl "https://rss.itunes.apple.com/api/v1/us/apps/top-free-apps/all/25/json"

# 热门播客
curl "https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/10/json"

# 中国区 Apple Music 热门专辑
curl "https://rss.itunes.apple.com/api/v1/cn/apple-music/top-albums/all/10/json"

# 特定分类的热门歌曲 (Pop = 14)
curl "https://rss.itunes.apple.com/api/v1/us/apple-music/top-songs/14/10/json"
```

---

## 响应格式

### Search/Lookup 响应

```json
{
  "resultCount": 1,
  "results": [
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 909253,
      "collectionId": 1488095359,
      "trackId": 1488095629,
      "artistName": "Artist Name",
      "collectionName": "Album Name",
      "trackName": "Song Title",
      "collectionCensoredName": "Album Name",
      "trackCensoredName": "Song Title",
      "artistViewUrl": "https://music.apple.com/us/artist/...",
      "collectionViewUrl": "https://music.apple.com/us/album/...",
      "trackViewUrl": "https://music.apple.com/us/song/...",
      "previewUrl": "https://audio-ssl.itunes.apple.com/...",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/.../30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/.../60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/.../100x100bb.jpg",
      "releaseDate": "2020-01-01T08:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 12,
      "trackNumber": 1,
      "trackTimeMillis": 234000,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Pop",
      "isStreamable": true,
      "collectionArtistId": 909253,
      "collectionArtistName": "Artist Name"
    }
  ]
}
```

### 核心响应字段

| 字段 | 说明 |
|------|------|
| `wrapperType` | 结果类型: `track`, `collection`, `artist`, `audiobook` |
| `kind` | 子类型: `song`, `feature-movie`, `podcast`, `software` 等 |
| `trackId` | 曲目/项目唯一 ID |
| `collectionId` | 专辑/合集 ID |
| `artistId` | 艺术家 ID |
| `trackName` | 曲目名称 |
| `collectionName` | 专辑名称 |
| `artistName` | 艺术家名称 |
| `artworkUrl30/60/100` | 封面图 URL (不同尺寸) |
| `previewUrl` | 30 秒预览 URL |
| `trackPrice` | 曲目价格 |
| `collectionPrice` | 专辑价格 |
| `releaseDate` | 发行日期 (ISO 8601) |
| `trackTimeMillis` | 曲目时长 (毫秒) |
| `primaryGenreName` | 主要分类 |
| `isStreamable` | 是否可在 Apple Music 流播放 |
| `trackViewUrl` | iTunes Store 链接 |
| `country` | 商店国家 |
| `currency` | 货币代码 |

### 不同 wrapperType 的特有字段

**track (歌曲/视频):**
`trackNumber`, `trackCount`, `discNumber`, `discCount`, `trackTimeMillis`, `previewUrl`, `isStreamable`

**collection (专辑):**
`collectionPrice`, `collectionExplicitness`, `copyright`, `contentAdvisoryRating`

**artist (艺术家):**
`artistLinkUrl`, `primaryGenreName`, `artistType`

**software (应用):**
`averageUserRating`, `userRatingCount`, `sellerName`, `fileSizeBytes`, `minimumOsVersion`, `screenshotUrls`, `ipadScreenshotUrls`

---

## 关键技巧

### 获取高分辨率封面

API 返回的封面 URL 默认为小尺寸，替换尺寸参数即可获得更大图片:

```javascript
// 原始 URL
const url100 = "https://is1-ssl.mzstatic.com/image/thumb/.../100x100bb.jpg";

// 替换为 600x600 高清
const url600 = url100.replace("100x100bb", "600x600bb");
```

| 尺寸 | URL 后缀 |
|------|----------|
| 30x30 | `30x30bb` |
| 60x60 | `60x60bb` |
| 100x100 | `100x100bb` |
| 200x200 | `200x200bb` |
| 300x300 | `300x300bb` |
| 600x600 | `600x600bb` (推荐) |
| 1200x1200 | `1200x1200bb` (非官方，部分内容可用) |

### Affiliate Token

在搜索或查询 URL 中追加 `at` 参数可追踪推广来源:

```
https://itunes.apple.com/search?term=beatles&at=10l4d7
```

### 分页

使用 `limit` + `offset` 实现分页:

```
第 1 页: limit=25&offset=0
第 2 页: limit=25&offset=25
第 3 页: limit=25&offset=50
```

最大 `limit` 为 200。

### URL 编码

搜索词必须进行 URL 编码，空格编码为 `+` 或 `%20`:

```
# 正确
term=queen+bohemian+rhapsody
term=queen%20bohemian%20rhapsody

# 错误
term=queen bohemian rhapsody
```

---

## 代码示例

### Python

```python
import urllib.parse
import urllib.request
import json
from typing import Any

BASE_URL = "https://itunes.apple.com"


def search(
    term: str,
    *,
    media: str | None = None,
    entity: str | None = None,
    limit: int = 25,
    country: str = "US",
    lang: str | None = None,
) -> dict[str, Any]:
    params: dict[str, str | int] = {"term": term, "limit": limit, "country": country}
    if media:
        params["media"] = media
    if entity:
        params["entity"] = entity
    if lang:
        params["lang"] = lang

    url = f"{BASE_URL}/search?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read())


def lookup(
    id: str | None = None,
    *,
    amg_artist_id: str | None = None,
    entity: str | None = None,
    limit: int = 25,
    country: str = "US",
) -> dict[str, Any]:
    params: dict[str, str | int] = {"limit": limit, "country": country}
    if id:
        params["id"] = id
    elif amg_artist_id:
        params["amgArtistId"] = amg_artist_id
    if entity:
        params["entity"] = entity

    url = f"{BASE_URL}/lookup?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read())


def get_artwork_url(url_100: str, size: int = 600) -> str:
    return url_100.replace("100x100bb", f"{size}x{size}bb")


# 使用示例
result = search("Taylor Swift", media="music", entity="song", limit=5)
for track in result.get("results", []):
    print(f"{track['trackName']} - {track['artistName']}")
    print(f"  封面: {get_artwork_url(track['artworkUrl100'])}")
    print(f"  时长: {track['trackTimeMillis'] / 1000:.1f}s")
```

### JavaScript / TypeScript

```typescript
const BASE_URL = "https://itunes.apple.com";

interface SearchParams {
  term: string;
  media?: string;
  entity?: string;
  limit?: number;
  country?: string;
  lang?: string;
  offset?: number;
}

async function search(params: SearchParams) {
  const url = new URL(`${BASE_URL}/search`);
  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined) url.searchParams.set(key, String(value));
  });
  const resp = await fetch(url);
  return resp.json();
}

function getArtworkUrl(url100: string, size: number = 600): string {
  return url100.replace("100x100bb", `${size}x${size}bb`);
}

// 使用示例
const result = await search({
  term: "Radiohead",
  media: "music",
  entity: "album",
  limit: 5,
});
console.log(result.results);
```

---

## 常见用法

| 场景 | 推荐方法 |
|------|----------|
| 搜索歌曲 | `/search?media=music&entity=song` |
| 搜索专辑 | `/search?media=music&entity=album` |
| 搜索艺术家 | `/search?media=music&entity=musicArtist` |
| 搜索应用 | `/search?entity=software` |
| 搜索播客 | `/search?entity=podcast` |
| 获取专辑曲目 | `/lookup?id={albumId}&entity=song` |
| 获取艺术家专辑 | `/lookup?id={artistId}&entity=album` |
| 批量查询 | `/lookup?id=id1,id2,id3` |
| 获取排行榜 | RSS Feed Generator |
| 获取分类 | Genre API |
| 获取高清封面 | 替换 artworkUrl 中的尺寸参数 |

---

## 注意事项

- 无需认证，但 Apple 保留了速率限制的权利。建议合理控制请求频率，避免高并发
- `limit` 参数最大值为 200
- 搜索词必须进行 URL 编码
- `country` 参数影响返回的价格、可用性、分类等数据
- Lookup 的 `id` 参数支持逗号分隔的批量 ID，最多 200 个
- `entity` 参数必须与 `media` 参数兼容，不兼容的组合会返回空结果
- `isStreamable` 字段表示内容是否在 Apple Music 上可流播放
- RSS Feed 的 `format` 参数仅支持 `json` 和 `jsonp`

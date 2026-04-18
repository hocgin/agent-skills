---
name: browser-store-screenshots
description: Use when building Chrome Web Store screenshot pages, generating exportable marketing screenshots for Chrome extensions, or creating programmatic screenshot generators with Next.js. Triggers on chrome web store, extension screenshots, chrome store, promo tile, marquee, browser screenshot, chrome extension listing.
---

# Chrome Web Store Screenshots Generator

## Overview

Build a Next.js page that renders Chrome Web Store screenshots as **advertisements** (not plain UI captures) and exports them via `html-to-image` at Chrome's required resolutions. Screenshots and promotional images are the primary conversion assets on the Chrome Web Store.

Supported image types out of the box:
- **Screenshot** (1280x800) -- Chrome Web Store listing page
- **Screenshot Small** (640x400) -- Chrome Web Store listing page (smaller variant)
- **Small Promo Tile** (440x280) -- Homepage, category pages, search results (REQUIRED)
- **Marquee** (1400x560) -- Featured carousel banner (OPTIONAL)

## Core Principle

**Screenshots are advertisements, not documentation.** Every screenshot sells one idea. If you're just showing raw UI, you're doing it wrong -- you're selling a *feeling*, an *outcome*, or killing a *pain point*. Chrome Web Store screenshots that look like plain desktop captures get skipped. Your screenshots need to communicate the extension's value before the user even reads the description.

## Step 1: Ask the User These Questions

Before writing ANY code, ask the user all of these. Do not proceed until you have answers:

### Required

1. **Extension screenshots** -- "Where are your extension screenshots? (PNG files of actual browser captures showing your extension in action)"
2. **Extension icon** -- "Where is your extension icon PNG? (128x128 recommended)"
3. **Brand colors** -- "What are your brand colors? (accent color, text color, background preference)"
4. **Font** -- "What font does your extension/brand use? (or what font do you want for the screenshots?)"
5. **Feature list** -- "List your extension's features in priority order. What's the #1 thing your extension does?"
6. **Number of slides** -- "How many screenshots do you want? (Chrome Web Store allows up to 5)"
7. **Style direction** -- "What style do you want? Examples: clean/minimal, dark/moody, bold/colorful, gradient-heavy, flat. Share Chrome Web Store screenshot references if you have any."

### Optional

8. **Small Promo Tile** -- "Do you want a Small Promo Tile (440x280)? This is REQUIRED for your listing and appears in search results and category pages."
9. **Marquee Image** -- "Do you want a Marquee banner (1400x560)? This is optional and used if your extension is featured in the Chrome Web Store carousel."
10. **Additional instructions** -- "Any specific requirements, constraints, or preferences?"

### Derived from answers (do NOT ask -- decide yourself)

Based on the user's style direction, brand colors, and extension aesthetic, decide:
- **Background style**: gradient direction, colors, whether light or dark base
- **Decorative elements**: subtle shapes, glows, or none -- match the style
- **Dark vs light slides**: how many of each, which features suit dark treatment
- **Typography treatment**: weight, tracking, line height -- match the brand personality
- **Color palette**: derive text colors, secondary colors, shadow tints from the brand colors

**IMPORTANT:** If the user gives additional instructions at any point during the process, follow them. User instructions always override skill defaults.

## Step 2: Set Up the Project

### Detect Package Manager

Check what's available, use this priority: **bun > pnpm > yarn > npm**

```bash
# Check in order
which bun && echo "use bun" || which pnpm && echo "use pnpm" || which yarn && echo "use yarn" || echo "use npm"
```

### Scaffold (if no existing Next.js project)

```bash
# With bun:
bunx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
bun add html-to-image

# With pnpm:
pnpx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
pnpm add html-to-image

# With yarn:
yarn create next-app . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
yarn add html-to-image

# With npm:
npx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
npm install html-to-image
```

### File Structure

```
project/
├── public/
│   ├── app-icon.png            # User's extension icon
│   └── screenshots/
│       ├── feature-1.png
│       ├── feature-2.png
│       └── ...
├── src/app/
│   ├── layout.tsx              # Font setup
│   └── page.tsx                # The screenshot generator (single file)
└── package.json
```

**The entire generator is a single `page.tsx` file.** No routing, no extra layouts, no API routes.

### Theme Presets

```tsx
const THEMES = {
  "clean-light": { bg: "#F6F1EA", fg: "#171717", accent: "#5B7CFA", muted: "#6B7280" },
  "dark-bold":   { bg: "#0B1020", fg: "#F8FAFC", accent: "#8B5CF6", muted: "#94A3B8" },
  "warm-editorial": { bg: "#F7E8DA", fg: "#2B1D17", accent: "#D97706", muted: "#7C5A47" },
} as const;

type ThemeId = keyof typeof THEMES;
const [themeId, setThemeId] = useState<ThemeId>("clean-light");
const theme = THEMES[themeId];
```

Use theme tokens everywhere instead of hardcoded colors.

### Font Setup

```tsx
// src/app/layout.tsx
import { YourFont } from "next/font/google";
const font = YourFont({ subsets: ["latin"] });

export default function Layout({ children }: { children: React.ReactNode }) {
  return <html><body className={font.className}>{children}</body></html>;
}
```

## Step 3: Plan the Slides

### Screenshot Framework (Narrative Arc)

Chrome Web Store allows up to 5 screenshots. Adapt this framework:

| Slot | Purpose | Notes |
|------|---------|-------|
| #1 | **Hero / Main Benefit** | Extension icon + tagline + main screen. This is the PRIMARY conversion driver. |
| #2 | **Differentiator** | What makes this extension unique vs competitors |
| #3 | **Core Feature** | The most-used feature, demonstrated in context |
| #4 | **Workflow / Integration** | How it fits into the user's daily browsing routine |
| #5 | **Trust / Summary** | Social proof, permissions transparency, or feature pills listing extras |

**Rules:**
- Each slide sells ONE idea. Never two features on one slide.
- Vary layouts across slides -- never repeat the same template structure.
- Include 1-2 contrast slides (inverted bg) for visual rhythm.
- All screenshots are **landscape** (16:10 ratio) -- use horizontal composition.

## Step 4: Write Copy FIRST

Get all headlines approved before building layouts. Bad copy ruins good design.

### The Iron Rules

1. **One idea per headline.** Never join two things with "and."
2. **Short, common words.** 1-2 syllables. No jargon unless it's domain-specific.
3. **3-5 words per line.** Must be readable at thumbnail size in the store.
4. **Line breaks are intentional.** Control where lines break with `<br />`.

### Three Approaches (pick one per slide)

| Type | What it does | Example |
|------|-------------|---------|
| **Paint a moment** | You picture yourself doing it | "Summarize any page in one click." |
| **State an outcome** | What your life looks like after | "A clutter-free browser, every day." |
| **Kill a pain** | Name a problem and destroy it | "Never lose a tab again." |

### What NEVER Works

- **Feature lists as headlines**: "Block ads, track time, and manage tabs"
- **Two ideas joined by "and"**: "Save time and boost productivity"
- **Vague aspirational**: "Better browsing, reimagined"
- **Marketing buzzwords**: "AI-powered" (unless it's actually AI)

### Bad-to-Better Headline Examples

| Weak | Better | Why it wins |
|------|--------|-------------|
| Block ads and track browsing time | Browse without distractions | one idea, outcome-focused |
| Manage tabs with AI summaries | Find any tab, instantly | specific, sells the outcome |
| Save bookmarks with tags | Your bookmarks, actually organized | relatable pain point |
| Dark mode and custom themes | Make the browser yours | emotional, personal |

### Copy Process

1. Write 3 options per slide using the three approaches
2. Read each at arm's length -- if you can't parse it in 1 second, it's too complex
3. Check: does each line have 3-5 words? If not, adjust line breaks
4. Present options to the user with reasoning for each

### Chrome Web Store Copy Tips

- Extension screenshots are viewed at 1280x800 on desktop -- text can be slightly larger than mobile app screenshots
- Use action-oriented language: verbs first
- Keep it conversational -- Chrome extension users expect utility, not enterprise-speak
- Avoid mentioning "extension" or "Chrome" in copy -- the user already knows where they are

## Step 5: Build the Page

### Architecture

```
page.tsx
├── Constants (canvas dimensions, export sizes)
├── THEMES / COPY
├── Image preload cache (preloadAllImages + img() helper)
├── Browser frame component (CSS-only browser window mockup)
├── Caption component (label + headline, scales from canvasW)
├── Decorative components (blobs, glows -- based on style direction)
├── Slide components (Slide1..N for screenshots)
├── PromoTile component (440x280)
├── Marquee component (1400x560)
├── Slide registry (SCREENSHOT_SLIDES, PROMO_SLIDE, MARQUEE_SLIDE)
├── ScreenshotPreview  -- ResizeObserver scaling + hover export
└── ScreenshotsPage    -- grid + toolbar + export logic
```

### Canvas Dimensions

Design at the **largest** required resolution. Smaller sizes are achieved by re-rendering at the target resolution on export.

```typescript
// Screenshots
const SCREENSHOT_W     = 1280;
const SCREENSHOT_H     = 800;
const SCREENSHOT_SM_W  = 640;
const SCREENSHOT_SM_H  = 400;

// Promo images
const PROMO_TILE_W     = 440;
const PROMO_TILE_H     = 280;
const MARQUEE_W        = 1400;
const MARQUEE_H        = 560;
```

### Export Sizes

```typescript
const SCREENSHOT_SIZES = [
  { label: "Screenshot (recommended)", w: 1280, h: 800 },
  { label: "Screenshot (small)",      w: 640,  h: 400 },
] as const;

const PROMO_TILE_SIZES = [{ label: "Small Promo Tile (required)", w: 440, h: 280 }] as const;
const MARQUEE_SIZES    = [{ label: "Marquee (optional)", w: 1400, h: 560 }] as const;
```

### Image Type

```typescript
type ImageType = "screenshot" | "promo-tile" | "marquee";
```

### Browser Window Mockup (CSS-only)

The browser mockup gives screenshots context -- users immediately understand this is a Chrome extension. Use a clean, modern browser frame rendered entirely with CSS:

```tsx
function BrowserWindow({ src, alt, style }: { src: string; alt: string; style?: React.CSSProperties }) {
  return (
    <div style={{
      width: "100%", height: "100%", position: "relative", borderRadius: "1.2%",
      background: "linear-gradient(180deg, #2C2C2E 0%, #1C1C1E 100%)",
      boxShadow: "0 20px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.08)",
      overflow: "hidden", ...style,
    }}>
      {/* Title bar */}
      <div style={{
        height: "5.5%", display: "flex", alignItems: "center",
        padding: "0 2.5%", gap: "1.5%", background: "linear-gradient(180deg, #3A3A3C 0%, #2C2C2E 100%)",
        borderBottom: "1px solid rgba(0,0,0,0.3)",
      }}>
        {/* Traffic lights */}
        <div style={{ display: "flex", gap: "0.65%" }}>
          <div style={{ width: "0.85%", aspectRatio: "1", borderRadius: "50%", background: "#FF5F57" }} />
          <div style={{ width: "0.85%", aspectRatio: "1", borderRadius: "50%", background: "#FEBC2E" }} />
          <div style={{ width: "0.85%", aspectRatio: "1", borderRadius: "50%", background: "#28C840" }} />
        </div>
        {/* Address bar */}
        <div style={{
          flex: 1, height: "55%", borderRadius: "0.5%",
          background: "rgba(0,0,0,0.25)", margin: "0 2%",
          display: "flex", alignItems: "center", justifyContent: "center",
          padding: "0 1.5%",
        }}>
          <div style={{
            fontSize: "clamp(8px, 1.2vw, 14px)", color: "rgba(255,255,255,0.45)",
            fontFamily: "monospace", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis",
          }}>
            chrome-extension://...
          </div>
        </div>
        {/* Extension icon placeholder */}
        <div style={{
          width: "2.5%", aspectRatio: "1", borderRadius: "20%",
          background: "linear-gradient(135deg, #4285F4, #34A853)", flexShrink: 0,
        }} />
      </div>
      {/* Screen area */}
      <div style={{
        position: "absolute", left: "1.8%", top: "5.5%", width: "96.4%", height: "94.5%",
        borderRadius: "0 0 0.4% 0.4%", overflow: "hidden", background: "#fff",
      }}>
        <img src={src} alt={alt} style={{
          display: "block", width: "100%", height: "100%",
          objectFit: "cover", objectPosition: "top",
        }} draggable={false} />
      </div>
    </div>
  );
}
```

### Minimal Browser Frame (for small canvases)

For the Small Promo Tile (440x280), the full browser mockup is too detailed. Use a minimal frame or no frame at all, focusing on the extension icon + headline + a cropped screenshot:

```tsx
function MinimalFrame({ src, alt, style }: { src: string; alt: string; style?: React.CSSProperties }) {
  return (
    <div style={{
      width: "100%", height: "100%", position: "relative", borderRadius: "2%",
      overflow: "hidden",
      boxShadow: "0 4px 20px rgba(0,0,0,0.3)",
      ...style,
    }}>
      {/* Thin top bar */}
      <div style={{
        height: "3%", display: "flex", alignItems: "center",
        padding: "0 1.5%", gap: "1%",
        background: "linear-gradient(180deg, #3A3A3C, #2C2C2E)",
        borderBottom: "1px solid rgba(0,0,0,0.3)",
      }}>
        <div style={{ display: "flex", gap: "0.6%" }}>
          <div style={{ width: "1.5%", aspectRatio: "1", borderRadius: "50%", background: "#FF5F57" }} />
          <div style={{ width: "1.5%", aspectRatio: "1", borderRadius: "50%", background: "#FEBC2E" }} />
          <div style={{ width: "1.5%", aspectRatio: "1", borderRadius: "50%", background: "#28C840" }} />
        </div>
      </div>
      <img src={src} alt={alt} style={{
        display: "block", width: "100%", height: "97%",
        objectFit: "cover", objectPosition: "top",
      }} draggable={false} />
    </div>
  );
}
```

### Width Formula

For landscape screenshots, the browser window typically fills most of the canvas. Use a simple ratio:

```typescript
type WidthFn = (cW: number, cH: number) => number;

function browserW(cW: number, cH: number, clamp = 0.82) {
  return Math.min(clamp, 0.65 * (cH / cW) * 0.625);
}
```

Usage: `width: \`${browserW(cW, cH) * 100}%\``

### Rendering Strategy

Each image is designed at full resolution. Two copies exist:

1. **Preview**: CSS `transform: scale()` via `ResizeObserver` to fit a grid card
2. **Export**: Offscreen at `position: absolute; left: -9999px` at true resolution

**Critical:** Wrap the entire page in `overflowX: "hidden"` to prevent offscreen export elements from causing horizontal scroll:

```tsx
<div style={{ minHeight: "100vh", background: "#f3f4f6", position: "relative", overflowX: "hidden" }}>
```

### Slide Layout Patterns (Landscape)

Chrome Web Store screenshots are landscape (1280x800). Use these placement patterns -- NEVER repeat the same layout twice in a row:

**Centered browser** (hero, single-feature):
```
Browser centered, vertically aligned to bottom ~80%
Caption above the browser
```

**Left caption + right browser** (feature showcase):
```
Caption: position: absolute, left: 5%, top: 50%, transform: translateY(-50%), width: 30%
Browser: position: absolute, right: 3%, top: 50%, transform: translateY(-50%), width: 55%
```

**Right caption + left browser** (alternate):
```
Browser: position: absolute, left: 3%, top: 50%, transform: translateY(-50%), width: 55%
Caption: position: absolute, right: 5%, top: 50%, transform: translateY(-50%), width: 30%
```

**Full-width browser + overlay caption** (immersive):
```
Browser: full width, slight bottom padding
Caption: position: absolute, top: 8%, left: 5%, with translucent background pill
```

**Feature pills / summary** (last slide):
```
No browser -- dark/contrast background
App icon + "And so much more."
Grid of feature pills (2-3 columns)
```

### Small Promo Tile Layout (440x280)

The promo tile is small and appears in search results. It must communicate the extension's value at a glance:

```tsx
function PromoTileSlide({ cW, cH }: { cW: number; cH: number }) {
  return (
    <div style={{
      width: "100%", height: "100%", position: "relative", overflow: "hidden",
      background: "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)",
      display: "flex", alignItems: "center", justifyContent: "center",
    }}>
      {/* Extension icon */}
      <img src={img("/app-icon.png")} alt="Icon"
        style={{ width: cW * 0.18, height: cW * 0.18, borderRadius: cW * 0.035, flexShrink: 0 }}
        draggable={false} />
      {/* Tagline */}
      <div style={{
        fontSize: cW * 0.065, fontWeight: 700, color: "#fff", marginLeft: cW * 0.05,
        lineHeight: 1.2, maxWidth: "60%",
      }}>
        Your tagline here.
      </div>
    </div>
  );
}
```

### Marquee Layout (1400x560)

The marquee is a wide banner for featured extensions. Use a cinematic layout:

```tsx
function MarqueeSlide({ cW, cH }: { cW: number; cH: number }) {
  return (
    <div style={{
      width: "100%", height: "100%", position: "relative", overflow: "hidden",
      background: "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)",
      display: "flex", alignItems: "center",
      padding: `0 ${cW * 0.06}px`,
    }}>
      {/* Left: icon + name + tagline */}
      <div style={{ display: "flex", alignItems: "center", gap: cW * 0.03, zIndex: 10 }}>
        <img src={img("/app-icon.png")} alt="App Icon"
          style={{ width: cW * 0.08, height: cW * 0.08, borderRadius: cW * 0.015 }}
          draggable={false} />
        <div>
          <div style={{ fontSize: cW * 0.035, fontWeight: 800, color: "#fff", lineHeight: 1.1 }}>ExtensionName</div>
          <div style={{ fontSize: cW * 0.018, color: "rgba(255,255,255,0.7)", marginTop: cW * 0.005 }}>Your tagline here.</div>
        </div>
      </div>
      {/* Right: decorative element or browser preview */}
    </div>
  );
}
```

### Device Dispatch

```typescript
const { cW, cH, currentSizes, slides } = (() => {
  if (imageType === "promo-tile") return { cW: PROMO_TILE_W, cH: PROMO_TILE_H, currentSizes: PROMO_TILE_SIZES, slides: [PROMO_SLIDE] };
  if (imageType === "marquee")   return { cW: MARQUEE_W,    cH: MARQUEE_H,    currentSizes: MARQUEE_SIZES,    slides: [MARQUEE_SLIDE] };
  return { cW: SCREENSHOT_W, cH: SCREENSHOT_H, currentSizes: SCREENSHOT_SIZES, slides: SCREENSHOT_SLIDES };
})();
```

### Toolbar Layout

The toolbar has two sections: a **scrollable controls area** (left, `flex: 1`) and a **fixed export button** (right, always visible):

```tsx
{/* Toolbar */}
<div style={{ position: "sticky", top: 0, zIndex: 50, background: "white", borderBottom: "1px solid #e5e7eb", display: "flex", alignItems: "center" }}>

  {/* Scrollable controls */}
  <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 10, padding: "10px 16px", overflowX: "auto", minWidth: 0 }}>
    <span style={{ fontWeight: 700, fontSize: 14, whiteSpace: "nowrap" }}>My Extension - Screenshots</span>

    {/* Image type tabs */}
    <div style={{ display: "flex", gap: 4, background: "#f3f4f6", borderRadius: 8, padding: 4, flexShrink: 0 }}>
      {(["screenshot", "promo-tile", "marquee"] as ImageType[]).map(t => (
        <button key={t} onClick={() => { setImageType(t); setSizeIdx(0); }}
          style={{ padding: "4px 14px", borderRadius: 6, border: "none", cursor: "pointer", fontSize: 12, fontWeight: 600, whiteSpace: "nowrap", background: imageType === t ? "white" : "transparent", color: imageType === t ? "#2563eb" : "#6b7280" }}>
          {t === "screenshot" ? "Screenshot" : t === "promo-tile" ? "Promo Tile" : "Marquee"}
        </button>
      ))}
    </div>

    {/* Export size */}
    <select value={sizeIdx} onChange={e => setSizeIdx(Number(e.target.value))} style={{ fontSize: 12, border: "1px solid #e5e7eb", borderRadius: 6, padding: "4px 10px" }}>
      {currentSizes.map((s, i) => <option key={i} value={i}>{s.label} -- {s.w}x{s.h}</option>)}
    </select>
  </div>

  {/* Export button -- always at right edge */}
  <div style={{ flexShrink: 0, padding: "10px 16px", borderLeft: "1px solid #e5e7eb" }}>
    <button onClick={exportAll} disabled={!!exporting}
      style={{ padding: "7px 20px", background: exporting ? "#93c5fd" : "#2563eb", color: "white", border: "none", borderRadius: 8, fontSize: 12, fontWeight: 600, cursor: exporting ? "default" : "pointer", whiteSpace: "nowrap" }}>
      {exporting ? `Exporting... ${exporting}` : "Export All"}
    </button>
  </div>
</div>
```

### Typography (Resolution-Independent)

All sizing relative to canvas width `cW`:

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Category label | `cW * 0.02` | 600 | default |
| Headline | `cW * 0.045` to `cW * 0.05` | 700 | 1.0 |
| Hero headline | `cW * 0.055` | 700 | 0.95 |
| Promo tile tagline | `cW * 0.065` | 700 | 1.2 |
| Marquee name | `cW * 0.035` | 800 | 1.1 |

Note: Chrome Web Store screenshots are landscape and viewed on desktop -- text can be larger than mobile app screenshots, but still keep it concise.

## Step 6: Export

### Why html-to-image, NOT html2canvas

`html2canvas` breaks on CSS filters, gradients, drop-shadow, backdrop-filter, and complex clipping. `html-to-image` uses native browser SVG serialization -- handles all CSS faithfully.

### Pre-load Images as Data URIs (CRITICAL)

`html-to-image` clones the DOM into an SVG `<foreignObject>`. During cloning it re-fetches every `<img>` src. These re-fetches are non-deterministic -- some hit the browser cache, some silently fail, causing transparent/black rectangles in exports.

**Fix:** Convert all images to base64 data URIs at page load. Use those as `src` everywhere.

```typescript
const IMAGE_PATHS = [
  "/app-icon.png",
  "/screenshots/feature-1.png",
  "/screenshots/feature-2.png",
  // ... all images used in any slide
];

const imageCache: Record<string, string> = {};

async function preloadAllImages() {
  await Promise.all(IMAGE_PATHS.map(async (path) => {
    const resp = await fetch(path);
    const blob = await resp.blob();
    const dataUrl = await new Promise<string>((resolve) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result as string);
      reader.readAsDataURL(blob);
    });
    imageCache[path] = dataUrl;
  }));
}

// Use in every <img> src:
function img(path: string): string {
  return imageCache[path] || path;
}
```

Gate rendering on preload completion:

```typescript
const [ready, setReady] = useState(false);
useEffect(() => { preloadAllImages().then(() => setReady(true)); }, []);
if (!ready) return <p>Loading images...</p>;
```

### Export Implementation

```typescript
import { toPng } from "html-to-image";

async function captureSlide(el: HTMLElement, w: number, h: number): Promise<string> {
  el.style.left = "0px";
  el.style.opacity = "1";
  el.style.zIndex = "-1";

  const opts = { width: w, height: h, pixelRatio: 1, cacheBust: true };

  // CRITICAL: Double-call -- first warms up fonts/images, second produces clean output
  await toPng(el, opts);
  const dataUrl = await toPng(el, opts);

  el.style.left = "-9999px";
  el.style.opacity = "";
  el.style.zIndex = "";
  return dataUrl;
}
```

### Export All (Bulk)

```typescript
async function exportAll() {
  if (imageType === "promo-tile" || imageType === "marquee") {
    const el = exportRefs.current[0];
    if (!el) return;
    setExporting("...");
    const size = currentSizes[sizeIdx];
    const dataUrl = await captureSlide(el, size.w, size.h);
    const a = document.createElement("a");
    a.href = dataUrl;
    a.download = `${imageType}-${size.w}x${size.h}.png`;
    a.click();
    setExporting(null);
    return;
  }
  const size = currentSizes[sizeIdx];
  for (let i = 0; i < slides.length; i++) {
    setExporting(`${i + 1}/${slides.length}`);
    const el = exportRefs.current[i];
    if (!el) continue;
    const dataUrl = await captureSlide(el, size.w, size.h);
    const a = document.createElement("a");
    a.href = dataUrl;
    a.download = `${String(i + 1).padStart(2, "0")}-${slides[i].id}-${size.w}x${size.h}.png`;
    a.click();
    await new Promise(r => setTimeout(r, 300));
  }
  setExporting(null);
}
```

### Key Export Rules

- **Double-call trick**: First `toPng()` loads fonts/images lazily. Second produces clean output. Without this, exports are blank.
- **On-screen for capture**: Temporarily move to `left: 0` before `toPng` -- offscreen elements don't render.
- **Offscreen container**: Use `position: absolute; left: -9999px` (not `fixed`) inside a `overflowX: hidden` wrapper.
- **300ms delay** between sequential exports -- prevents browser throttling.
- **Numbered filenames**: Zero-padded prefix so files sort correctly: `01-hero-1280x800.png`.
- **Pre-loaded data URIs**: Always use `img()` helper. Never use raw file paths in slide components.
- **RGB source images**: Ensure source screenshots are RGB (not RGBA). RGBA PNGs can produce transparent/black regions in exports.
- **Full bleed, square corners**: Chrome Web Store screenshots must have no rounded corners and no padding.

## Step 7: Final QA Gate

### Chrome Web Store Compliance

- **1280x800 or 640x400**: Screenshots must be exactly these dimensions.
- **Full bleed, square corners**: No rounded corners, no padding, no white borders.
- **Max 5 screenshots**: Do not generate more than 5.
- **Small Promo Tile (440x280)**: Must be provided -- this is REQUIRED by Chrome Web Store.
- **No misleading claims**: No "Editor's Choice", "Number One", etc.
- **Consistent branding**: Screenshots, icon, and promo tiles should share visual identity.

### Message Quality

- **One idea per slide**: if a headline sells two ideas, split it or simplify it
- **First slide is strongest**: the hero slide must communicate the main benefit immediately
- **Readable in one second**: if you cannot parse it instantly, the headline is too complex

### Visual Quality

- **No repeated layouts in sequence**: adjacent slides should not feel templated
- **Browser mockup looks realistic**: traffic lights, address bar, proper proportions
- **Decorative elements support the story**: add energy without covering the extension UI
- **Visual rhythm exists**: at least one contrast slide when the set is long enough
- **Promo tile works at half size**: the 440x280 tile appears small in search results

### Export Quality

- **No clipped text or assets** after scaling to export size
- **Screenshots correctly aligned** inside the browser frame
- **Filenames sort correctly** with zero-padded numeric prefixes
- **All images export cleanly**: no black rectangles, no missing images
- **Theme tokens applied consistently** across all slides in the same preset

### Hand-off Behavior

When you present the finished work:

1. briefly explain the narrative arc across the slides
2. mention any slides that intentionally use contrast or different layout treatment
3. call out any assumptions you made about brand tone, copy, or missing assets
4. remind the user to upload the Small Promo Tile (440x280) -- it is REQUIRED for the listing

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| All slides look the same | Vary browser position (center, left, right, full-width, no-frame) |
| Copy is too complex | "One second at arm's length" test |
| Floating elements block the browser | Move off-screen edges or above the window frame |
| Plain white/black background | Use gradients -- even subtle ones add depth |
| Headlines use "and" | Split into two slides or pick one idea |
| Export is blank | Use double-call trick; move element on-screen before capture |
| Screenshots black in export | Images not inlined -- use `preloadAllImages()` + `img()` helper |
| Some slides missing images | Non-deterministic fetch race -- same fix as above |
| Export button scrolls off toolbar | Split toolbar: scrollable controls left (`flex: 1`), fixed button right (`flex-shrink: 0`) |
| Page has horizontal scroll | Add `overflowX: "hidden"` on the outermost wrapper div |
| Missing promo tile | Always generate the 440x280 Small Promo Tile -- it is REQUIRED |
| Rounded corners on screenshots | Chrome Web Store requires full bleed, square corners |
| Wrong dimensions | Double-check: screenshots 1280x800 or 640x400, promo 440x280, marquee 1400x560 |

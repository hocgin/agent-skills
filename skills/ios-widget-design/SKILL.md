---
name: ios-widget-design
description: "Design, review, or score iPhone and iPad WidgetKit widgets according to Apple’s Human Interface Guidelines, including Home Screen, Lock Screen, and StandBy variants. Use for widget concepts, visual specifications, and scored widget UI reviews; not for Live Activities, Controls, or full app screens."
---

# iOS Widget Design

Design widgets as glanceable, context-specific extensions of an app — never as compressed app screens. The current source of truth is Apple’s [Widgets Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/widgets). Before making a new design or review recommendation, read [the iOS/iPadOS decision guide](references/apple-widget-hig.md). When a design needs an artboard, measured layout, or a claimed size in points, also read [the WidgetKit family and dimensions reference](references/widget-dimensions.md). If a requested behavior depends on a recently changed WidgetKit API or system appearance, verify it against Apple’s current documentation.

## Scope

Use this skill for WidgetKit widgets on iPhone and iPad: Home Screen, Today View, Lock Screen, and StandBy. It covers product decisions, information hierarchy, visual design, gallery states, accessibility, and SwiftUI handoff.

Do not apply it to Live Activities, Control Center controls, full app screens, watch complications, or macOS/visionOS widgets unless the request explicitly includes them. A live, frequently updating task or event generally calls for a Live Activity rather than a widget.

## Start with the right widget

- Identify the single user need the widget serves, the moment it is viewed, the content that must stay fresh, and the destination or action it enables.
- Choose only the widget families that add a distinct, useful perspective. A larger family must reveal additional meaning, information, or actions; it must not merely scale up a smaller layout.
- Treat each supported context as a separate design condition. State any missing product assumptions rather than inventing a complex feature set.
- Include signed-out, empty, unavailable, stale, and loading states when they can occur. Authentication messaging should explain the value of signing in.

## Design workflow

1. Define a family-and-context map: supported family, primary information, secondary information, action/deep link, and fallback state for each variant.
2. Set a clear glance hierarchy: one dominant takeaway, then only directly relevant supporting data. If the view is dense, move detail to a larger family, simplify it, or use a meaningful graphic.
3. Design the full-color, accented, and vibrant renditions as intentional variants. Do not assume artwork, color, or custom backgrounds survive system rendering unchanged.
4. Specify the Widget Gallery preview, loading placeholder, and concise gallery description alongside the final state.
5. Review at the actual family sizes, with Dynamic Type, light/dark/clear/tinted appearances, Lock Screen/Always-On, and StandBy where applicable. Name the device screen size and the iPad `Canvas` or `Device` target whenever quoting dimensions.

When the user doesn’t request a particular deliverable format, provide a concise design brief containing the context map, per-family hierarchy, interaction/deep-link behavior, rendering-mode treatment, data states, and validation notes.

## Interaction and handoff

- Make every button, toggle, and link simple, relevant, and confidently tappable. Keep complex flows in the app.
- Tapping a noninteractive portion should open the matching detail or action in the app, not its generic home screen. An inline Lock Screen accessory has only one tap target.
- In SwiftUI handoff, preserve system-managed sizing and margins; use semantic/system typography, SF Symbols, real text, `ContainerRelativeShape`, and the appropriate widget rendering mode. Deliberately group content for accented rendering with `widgetAccentable(_:)` when needed.
- Avoid custom sizing or margin removal merely to imitate a mockup. Describe a justified exception when system defaults cannot support the intended content.

## Non-negotiable checks

- The widget remains useful at a glance and still makes sense after the system desaturates, tints, or removes its background.
- Meaning does not rely on color alone, body text is readable (generally 11 pt or larger), and text is not rasterized.
- Brand treatment supports recognition without displacing useful information; an app icon or prominent logo is rarely needed.
- The design does not imply minute-by-minute updates that WidgetKit cannot provide.

## Scored design review

When asked to audit, critique, compare, rate, or refine a widget design, read [Widget design review](references/widget-design-review.md) in addition to the HIG decision guide. Review screenshots, specifications, or SwiftUI views against all five dimensions; score each from 1 to 10 and cite visible evidence or a concrete implementation detail for every score.

- Score the widget in its actual family, screen size, and applicable rendering contexts — never score a generic, enlarged mockup alone.
- Report the five dimension scores, average, strengths, and prioritized fixes. A score below 7 requires a specific fix; an average must not mask a weak dimension.
- Treat all dimensions at 7 or above, with none below 5, as the minimum shipping threshold. If evidence for a required context is missing, label the score provisional and name the test still needed.
- Preserve Apple HIG over generic design-fashion advice. Platform-native restraint is not a lack of originality.

## Reference

Read [Apple widget HIG for iOS and iPadOS](references/apple-widget-hig.md) before design or review work. It contains the family/context matrix, rendering rules, layout constraints, and final review checklist distilled from Apple’s current guidance.

For exact family availability and dimensions in points, read [WidgetKit family and dimensions](references/widget-dimensions.md). Never present a family as having one universal fixed size or infer an unlisted device’s dimensions from a different device.

For a scored audit or review, read [Widget design review](references/widget-design-review.md). It adapts the requested five-dimension SwiftUI review framework to WidgetKit and Apple’s system surfaces.

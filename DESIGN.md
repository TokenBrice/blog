---
name: TokenBrice
description: Brutally Honest DeFi — a sovereign-stack editorial blog with a punk-archival visual register.
colors:
  dissenting-slate: "#34495e"
  dissenting-slate-deep: "#2c3e50"
  paper-bone: "#f5f5fa"
  ink-body: "#595959"
  ink-strong: "#000000"
  ink-secondary: "#747474"
  ink-tertiary: "#767676"
  hairline: "#dadada"
  card-surface: "#ffffff"
  card-surface-hover: "#eaeaea"
  dark-surface: "#303030"
  dark-card: "#424242"
  dark-accent: "#ecf0f1"
  dark-link-blue: "#93c5fd"
  code-ink-light: "#546e7a"
  code-ink-dark: "#90a4ae"
  pre-bg-light: "#fafafa"
  pre-bg-dark: "#272822"
  pre-ink-dark: "#f8f8f2"
  blockquote-bg: "#f8f8f8"
  signal-red: "#e74c3c"
  cat-sage: "#8ea885"
  cat-mauve: "#df7988"
  cat-ocean: "#0177b8"
  cat-ochre: "#806504"
  cat-violet: "#6b69d6"
  difficulty-beginner: "#22c55e"
  difficulty-intermediate: "#fbbf24"
  difficulty-expert: "#f87171"
  difficulty-beginner-dark: "#16a34a"
  difficulty-intermediate-dark: "#ca8a04"
  difficulty-expert-dark: "#dc2626"
  example-tint: "#2f6feb"
  risks-tint: "#d97706"
  faq-tint: "#7c3aed"
  projects-ink: "#f7f1df"
  projects-hull: "#0a1628"
typography:
  display:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(3.6rem, 5.5vw, 5.4rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
    fontFeature: "'kern' 1, 'liga' 1"
  headline:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "2.2rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.005em"
  title:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "2.2rem"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Inter Tight, Lato, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "1.7rem"
    fontWeight: 400
    lineHeight: 1.85
  label:
    fontFamily: "Inter Tight, Lato, -apple-system, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.16em"
  kicker:
    fontFamily: "Inter Tight, Lato, -apple-system, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    letterSpacing: "0.05em"
  code:
    fontFamily: "Menlo, Monaco, Consolas, 'Courier New', monospace"
    fontSize: "0.88em"
    fontWeight: 400
rounded:
  hairline: "4px"
  small: "6px"
  medium: "8px"
  card: "10px"
  badge: "12px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "15px"
  md: "20px"
  lg: "25px"
  xl: "30px"
  section: "40px"
  hero: "50px"
components:
  article-card:
    backgroundColor: "{colors.card-surface}"
    textColor: "{colors.ink-strong}"
    rounded: "{rounded.card}"
    padding: "20px"
  article-card-hover:
    backgroundColor: "{colors.card-surface}"
    textColor: "{colors.ink-strong}"
    rounded: "{rounded.card}"
    padding: "20px"
  category-badge:
    backgroundColor: "{colors.cat-sage}"
    textColor: "{colors.card-surface}"
    rounded: "{rounded.pill}"
    padding: "0.55rem 1.1rem"
  glossary-term-link:
    textColor: "{colors.dissenting-slate}"
    backgroundColor: "transparent"
    padding: "0"
  glossary-popover:
    backgroundColor: "{colors.card-surface}"
    textColor: "{colors.ink-strong}"
    rounded: "{rounded.small}"
    padding: "0.85rem 1rem"
  series-nav:
    backgroundColor: "{colors.card-surface}"
    textColor: "{colors.ink-strong}"
    rounded: "{rounded.card}"
    padding: "1.25rem 1.5rem"
  projects-card:
    backgroundColor: "{colors.projects-hull}"
    textColor: "{colors.projects-ink}"
    rounded: "{rounded.small}"
    padding: "16px"
  difficulty-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink-body}"
    rounded: "{rounded.pill}"
    padding: "0.5rem 1rem"
---

# Design System: TokenBrice

## 1. Overview

**Creative North Star: "The Sovereign Edition"**

This is the visual register of a long-form DeFi blog whose infrastructure is part of its argument. The site runs on a privacy-respecting, open-source stack (Hugo, self-hosted Matomo with IP anonymisation, IPFS replication, no Google Fonts) and the design treats that sovereignty as a first principle, not a backdrop. There is no third-party font, no embedded tracker, no analytics-funded gradient. What you see is what was shipped, and what was shipped is what the author owns end-to-end.

The aesthetic is **punk-archival**: an irreverent editorial voice held inside an unfashionable, durable shell. Fraunces carries the headlines with the gravity of a printed quarterly; Inter Tight carries the body with the restraint of a working notebook. A single accent — *Dissenting Slate* (`#34495e`) — does almost all the chromatic work, ceding the screen to the writing. Where personality erupts, it is local and earned: the projects band's deep-hull navy, the rotating category palette, the difficulty filters' green/amber/red. Nothing animates that does not need to. Nothing rounds that does not need to. Nothing decorates that does not argue.

The system explicitly refuses four registers (carried verbatim from `PRODUCT.md`): corporate-fintech polish, SaaS landing templates, Substack-default blog chrome, and hype-template crypto (gradient mesh, holographic gloss, glow buttons). Each gets a literal "Don't" in §6.

**Key Characteristics:**
- One accent doing 90% of the chromatic work, with five category colors and three difficulty colors as the only sanctioned exceptions.
- Editorial serif (Fraunces) for display + headlines; humanist sans (Inter Tight) for body. Lato preserved on disk as legacy fallback only.
- Flat at rest, lifts on touch — surfaces sit on the page until the reader engages.
- 10px primary radius, 6px / 8px secondary, full-pill (999px) for badges and related-term chips only.
- Both light and dark themes must read in their respective ambient conditions; dark is not a fashion choice.
- Sovereign stack: every asset (fonts, scripts, images, analytics) self-hosted or absent.

## 2. Colors: The Dissenting Slate Palette

A muted, ink-and-paper baseline with a single committed accent and a small, named cast of categorical pops. Restrained color strategy: tinted neutrals carry the surface, *Dissenting Slate* (`#34495e`) carries the brand, and everything else is signal — category, difficulty, callout role, or warning.

### Primary
- **Dissenting Slate** (`#34495e`): the accent that carries the brand. Used on links, the reading-progress bar, the series-nav left rule, blockquote inline-start border, glossary inline-marker text, the difficulty-pill borders when active, the drop-cap on long-form opens. Hover/active deepens to **Dissenting Slate Deep** (`#2c3e50`). In dark mode, the accent flips to **Dark Mode Mercury** (`#ecf0f1`) — light slate on dark, same role.

### Secondary
*(The system has no global secondary accent; it leans on categorical color for variation. See Tertiary for the named category palette.)*

### Tertiary
The category palette — five colors that rotate across article cards and category headers. Each is paired with white text and has been spot-checked for WCAG AA contrast on its assigned role:
- **Sage Council** (`#8ea885`): category 1 — analysis / governance lanes. AA on white (7.6:1 fixed).
- **Mauve Heretic** (`#df7988`): category 2 — opinionated takes, polemics.
- **Ocean Audit** (`#0177b8`): category 3 — technical deep-dives.
- **Ochre Ledger** (`#806504`): category 4 — replaced the original `#ffb900` because it failed AA. Don't put it back.
- **Violet Marginalia** (`#6b69d6`): category 5 — long-tail / experimental.

Difficulty colors (used on difficulty-filter pills and difficulty tags, not for prose accents):
- **Beginner Green** (`#22c55e` / dark `#16a34a`)
- **Intermediate Amber** (`#fbbf24` / dark `#ca8a04`)
- **Expert Red** (`#f87171` / dark `#dc2626`)

Glossary-term callout tints (used inside term pages only, ≤5% surface area):
- **Example Blue** (`#2f6feb`), **Risks Amber** (`#d97706`), **FAQ Violet** (`#7c3aed`).

### Neutral
- **Paper Bone** (`#f5f5fa`): light-mode body background. A bone-warm white tinted toward neutral-cool; never `#ffffff`.
- **Card White** (`#ffffff`): card surfaces sit a hair brighter than the body for separation without a border.
- **Card Hover Stone** (`#eaeaea`): list-item hover surface in light mode.
- **Ink Body** (`#595959`): default body text, raised from the theme default `#707070` for AAA contrast on Paper Bone.
- **Ink Strong** (`#000000`): card titles, primary card text.
- **Ink Secondary** (`#747474`) / **Ink Tertiary** (`#767676`): meta, captions, kicker.
- **Hairline** (`#dadada` at 50% opacity → `rgba(218, 218, 218, 0.5)`): the default separator. Never used as a heavy border.
- **Slate Night** (`#303030`): dark-mode body background — neutral graphite, not pitch black, not blue.
- **Slate Night Card** (`#424242`): dark-mode card surface, one step lifted from the body.

### Named Rules

**The Sovereign Stack Rule.** Every color above is defined locally. No color, font, or asset may be sourced from a third-party CDN or SaaS dependency that contradicts the editorial position (privacy, openness, sovereignty). If a design choice requires importing Google Fonts, Cloudflare Insights, a Tailwind play-CDN, or any tracker-bearing surface, the choice is wrong before it is drawn.

**The Earned Accent Rule.** *Dissenting Slate* is the only chromatic vote on most pages. The five category colors are sanctioned only on category surfaces (article cards, category headers, breadcrumbs). The three difficulty colors are sanctioned only on difficulty pills. Decorative use of any tertiary color — a teal callout for the vibes, an amber underline because the section feels important — is forbidden. Color is signal, never garnish.

**The No-Pure-Black Rule.** Light surfaces use `#f5f5fa` (Paper Bone), never `#ffffff` for the body. Dark surfaces use `#303030` (Slate Night), never `#000000`. Pure black appears only in card title text on light mode.

## 3. Typography

**Display & Headline Font:** Fraunces 700 (Georgia, serif fallback). The system's only serif; carries article titles, glossary term names, the drop-cap on long-form, and the article-card titles. Self-hosted woff2 in `static/fonts/fraunces/`.
**Body Font:** Inter Tight 400/600/700 (Lato as legacy fallback, then system-sans: -apple-system, BlinkMacSystemFont, Segoe UI, …). Carries everything that is not a heading. Self-hosted woff2 in `static/fonts/inter-tight/`. Lato is preserved on disk for any legacy class names that hard-code it, but new components should reach for Inter Tight.
**Code Font:** Menlo, Monaco, Consolas, Courier New (monospace fallback).

**Character.** A working editorial pairing: Fraunces 700 with `letter-spacing: -0.01em` and ligatures on reads sharp and considered, not decorative. Inter Tight 400/1.85 line-height reads as a calm, modern humanist sans — tighter and more technical than Lato, which suits the analyst register. The two together feel like a newspaper supplement printed by someone who does not trust the newspaper.

### Hierarchy

- **Display** (Fraunces, weight 700, `clamp(3.6rem, 5.5vw, 5.4rem)`, line-height 1.2, letter-spacing `-0.01em`): the article title and the glossary term title. The only place the system goes large.
- **Headline** (Fraunces, weight 700, `2.2rem` → `2.4rem` at xl, line-height 1.25): article-card titles in the home and category lists.
- **Title** (Fraunces, weight 700, 1.3 line-height): in-content `h2` / `h3` inside long-form. Margin scale `1.75em 0 0.6em` for h2, decreasing per level.
- **Body** (Inter Tight, weight 400, `1.7rem` at md+, line-height 1.85): article body and most prose. Cap measure at 65–75ch on the article container; the glossary term layout caps at `760px`. Body text rises from the theme default `#707070` to `#595959` for AAA contrast on Paper Bone — do not lower it back.
- **Label** (Inter Tight, weight 700, `1.25rem`, uppercase, letter-spacing `0.16em`): glossary section titles, with the small `8px` accent dot before. Reserved for structural markers, never for in-prose emphasis.
- **Kicker** (Inter Tight, weight 500, `0.875rem`, uppercase, letter-spacing `0.05em`): the article-details strip (date, reading time, tags) that sits above the article title. Appears via `order: -1` on the flex container.

### Named Rules

**The One-Serif Rule.** Fraunces is the only serif. Any future serif need (a pull quote treatment, a callout heading) must use Fraunces at a different weight or size; introducing a second serif breaks the editorial signature.

**The 65-Character Measure Rule.** Body text never exceeds 75 characters per line. The article container caps it; the glossary term layout caps it harder at 760px. If a future component spans a wider grid, the body text inside it does not.

**The Uppercase-Means-Structure Rule.** Uppercase letter-spaced type is reserved for structural labels (glossary section titles, kicker, series-nav title). Never use it for in-prose emphasis. The author's voice is bold and direct; the type does not need to shout the same word.

## 4. Elevation

**Flat at rest, lifts on touch.** Surfaces sit on the page in their default state. Hover and focus pull them forward 2–3px with a quiet ambient shadow. The system has a 4-tier shadow vocabulary (`l1`–`l4`) using stacked, low-opacity blur layers — sourced from the Figma Shadow Picker — and tuned heavier in dark mode to compensate for the dark surface.

### Shadow Vocabulary

- **`--shadow-l1`** (`0px 4px 8px rgba(0,0,0,0.04), 0px 0px 2px rgba(0,0,0,0.06), 0px 0px 1px rgba(0,0,0,0.04)`): the default resting state for cards, sidebar widgets, and series-nav. Almost imperceptible — separation without drama.
- **`--shadow-l2`** (`0px 10px 20px rgba(0,0,0,0.04), 0px 2px 6px rgba(0,0,0,0.04), 0px 0px 1px rgba(0,0,0,0.04)`): article-card hover state. Paired with `translateY(-2px)` and a `0.3s ease` transition.
- **`--shadow-l3`** (custom-tuned to `0px 14px 28px rgba(0,0,0,0.06), 0px 4px 10px rgba(0,0,0,0.04), 0px 0px 1px rgba(0,0,0,0.04)`): heavier elevation — used sparingly, reserved for modal-class surfaces.
- **`--shadow-l4`** (`0px 24px 32px ..., 0px 16px 24px ..., 0px 4px 8px ...`): top of stack; documented but barely used in production. Reserve for true overlays.
- **Glossary popover** (`0 8px 24px rgba(0,0,0,0.18)` light / `0 8px 24px rgba(0,0,0,0.55)` dark): a dedicated heavier shadow for the popover, because it floats over running text and needs to detach.
- **Projects card hover** (`0 12px 26px rgba(0,0,0,0.30)`): a deliberately heavier hover shadow inside the dark projects band, where the baseline elevation is taller and the contrast budget is generous.

### Named Rules

**The Flat-at-Rest Rule.** Surfaces are flat by default; shadows appear only as a response to interaction (hover, focus, popover open) or to detach from a heavily contrasted surface (the dark projects band). A card with a permanent heavy shadow is wrong. The site reads as paper at rest and as paper-being-handled in motion.

**The Dark-Mode-Heavier-Shadow Rule.** Dark-mode shadows are tuned with 3–4× the opacity of light-mode shadows (`rgba(0,0,0,0.14)` vs `0.04`) because dark-on-dark elevation only reads when the shadow is dark enough to register. Do not copy light-mode shadow opacities into dark-mode tokens; the system already accounts for this.

## 5. Components

The system's components feel **calm at baseline, sharp where it counts**. Most surfaces are quiet — 10px radius, hairline borders, ink type on Paper Bone. Where personality erupts, it is local and intentional: the projects band's deep-hull palette, the category-badge color, the difficulty-pill's borrowed difficulty hue.

### Article Cards
- **Shape:** 10px radius (`--card-border-radius`), `overflow: hidden` so the cover image clips cleanly to the corner.
- **Background:** `#ffffff` (Card White) on Paper Bone; `#424242` (Slate Night Card) in dark mode.
- **Cover image:** `object-fit: cover`, 150px (mobile) / 200px (md) / 250px (xl) tall.
- **Title:** Fraunces 700, `2.2rem` → `2.4rem` at xl, with `font-feature-settings: 'kern' 1, 'liga' 1`.
- **Subtitle / excerpt:** Inter Tight 400, `1.75rem` → `2rem` at xl.
- **Meta strip (kicker):** 1.4rem; date, reading time, translation links.
- **State:** `--shadow-l1` at rest → `--shadow-l2` on hover, with `translateY(-2px)` and `transition: box-shadow 0.3s ease, transform 0.2s ease`.

### Category Badges
- **Shape:** `999px` pill (`--rounded.pill`) on glossary-term pages; `4px` (`--tag-border-radius`) on article-card category tags.
- **Color:** one of the five category colors (Sage Council, Mauve Heretic, Ocean Audit, Ochre Ledger, Violet Marginalia) with white text. On glossary-term pages, the background is a tinted overlay via `color-mix(in srgb, var(--category-color) 12%, transparent)` (light) / 22% (dark).
- **Typography:** Inter Tight 700, uppercase, letter-spacing `0.08em` (article-card) / inherited (term page).
- **State:** background-color transition `0.2s ease`. No transform.

### Glossary Term Inline Marker (signature component)
The system's most distinctive interactive primitive. Rendered as a `<button>` reset to read as a link, with a dotted underline indicating "more available on hover."
- **Color:** Dissenting Slate (`#34495e`) light / Dark Link Blue (`#93c5fd`) dark.
- **Underline:** `border-bottom: 1px dotted currentColor`, cursor `help`.
- **State:** color deepens to Dissenting Slate Deep on hover; `:focus-visible` shows `outline: 2px solid var(--accent-color)` with `2px` offset.
- **Behavior:** triggers the glossary popover (see below). Never used as a primary navigation link.

### Glossary Popover
- **Shape:** 6px radius, hairline border.
- **Background:** Card White light / Slate Night Card dark.
- **Padding:** `0.85rem 1rem`.
- **Shadow:** `0 8px 24px rgba(0,0,0,0.18)` light / `0 8px 24px rgba(0,0,0,0.55)` dark — a dedicated heavier shadow so the popover detaches from running text.
- **Width:** `min(320px, 90vw)` — never wider, never breaks the column.
- **Typography:** term name `0.95rem` weight 700 in Dissenting Slate; definition `0.95rem` weight 400 in Ink Strong.

### Series Navigation
- **Shape:** 10px radius card, `border-left: 4px solid Dissenting Slate` — the only sanctioned use of a colored side-stripe in the system, justified because it carries the series identity inline with the reading flow.
- **Padding:** `1.25rem 1.5rem`.
- **Background:** Card White light / `rgba(255,255,255,0.025)` dark (a tonal layer, not a card surface).
- **List items:** counter-styled with a `1.65rem` 50%-radius badge (Ink Strong on `rgba(0,0,0,0.06)`); the current item flips to Dissenting Slate background with white text.
- **Section title:** `0.75rem`, uppercase, weight 700, letter-spacing `0.08em`, Dissenting Slate.

### Projects Banner (signature component)
The single most chromatically committed surface on the site — a deep-navy band with cream type that breaks the calm baseline deliberately. It exists because the projects collection earns the visual emphasis; nothing else gets this treatment.
- **Band:** 8px radius, complex gradient (`linear-gradient(90deg, rgba(12,44,83,0.78), rgba(20,42,78,0.96) 48%, rgba(10,27,54,0.92))`) over `#0a1628` base, with radial overlays and an `inset 0 1px 0 rgba(247,241,223,0.06)` top-edge highlight. Padding 22px.
- **Cards:** 6px radius, dark-navy panel (`rgba(4,13,27,0.62)`), cream borders (`rgba(247,241,223,0.13)`), min-height 118px.
- **Card hover:** `translateY(-3px)`, deeper panel, shadow `0 12px 26px rgba(0,0,0,0.30)`, transition `0.18s ease`.
- **Emblem circle:** 76px (64px mobile), 50% radius, soft radial-gradient halo with `drop-shadow: 0 8px 14px rgba(0,0,0,0.28)`.
- **Type:** name 19px weight 700 in Projects Ink (`#f7f1df`); tagline 13px in Projects Muted (`rgba(222,232,249,0.72)`).

### Difficulty Filter Pills
- **Shape:** `2rem` border-radius (effectively a pill), `1.5px` border in Hairline by default.
- **Padding:** `0.5rem 1rem`.
- **Typography:** `1.4rem`, weight 500 default → weight 700 when active.
- **Active state:** border color flips to the difficulty hue (Beginner Green / Intermediate Amber / Expert Red), background fills with `rgba([hue], 0.08)` light / `0.12` dark. Color is paired with weight increase, not used alone, so the affordance survives color blindness.

### Code Blocks
- **Background:** `#fafafa` light / `#272822` (Monokai) dark.
- **Text:** `#272822` light / `#f8f8f2` dark.
- **Inline code:** `rgba(0,0,0,0.12)` background, `0.88em` font-size, `2px 6px` padding. Code font: Menlo / Monaco / Consolas.
- **Copy button:** `outline: 2px solid var(--accent-color)` on `:focus-visible`.

### Drop-cap (signature flourish)
- Applied only to the first letter of the first paragraph in long-form articles tagged `--has-dropcap`.
- Fraunces, `5em`, line-height `0.85`, color Dissenting Slate. The single most editorial gesture on the page; restraint depends on never adding a second flourish.

### Named Rules

**The Calm-Baseline Rule.** Most components are quiet (10px radius, Card White, single hairline, no shadow at rest). Sharp moments — the projects band, the active difficulty pill, the category badge, the drop-cap — earn their amplitude by being rare. Doubling the loud surfaces halves their force.

**The Series-Nav Stripe Exception.** Side-stripe borders thicker than 1px are banned globally (see §6), with one exception: the 4px Dissenting Slate left border on series-nav, because it functions as a structural rail tying sequential posts to a shared identity. Any future use of a colored side-stripe must clear the same bar: it must encode information, not decorate.

## 6. Do's and Don'ts

Forceful, concrete, citing PRODUCT.md anti-references by name.

### Do:
- **Do** use Dissenting Slate (`#34495e`) as the sole chromatic accent on 90%+ of surfaces. The rarity is the point.
- **Do** use Fraunces 700 with `letter-spacing: -0.01em` and `font-feature-settings: 'kern' 1, 'liga' 1` for every display and headline.
- **Do** keep body text at `1.7rem` Inter Tight, line-height `1.85`, color Ink Body (`#595959`) — the AAA-on-Paper-Bone target. Do not lower the contrast back to the theme default.
- **Do** cap body measure at 65–75ch. The glossary template caps at `760px`; honor it on every prose-bearing component.
- **Do** keep surfaces flat at rest and let `--shadow-l1 → --shadow-l2` + `translateY(-2px)` carry hover. The system reads as paper-at-rest, paper-in-hand.
- **Do** pair the projects band's chromatic commitment with at least one full hover state — it is the one place the design earns the right to feel rich.
- **Do** carry every category color with white text and every difficulty hue with a weight change, so the affordance survives color blindness.
- **Do** maintain dark-light parity. Both themes are first-class; ship neither without testing the other.

### Don't:
- **Don't** import Google Fonts, Cloudflare Insights, a CDN-hosted analytics snippet, or any third-party asset that contradicts the sovereign-stack posture. Privacy is part of the argument; the stack is part of the design.
- **Don't** drift toward **corporate fintech** (PRODUCT.md anti-ref): no navy-and-gold trust palette, no stock-photo team grids, no "trusted by" logo wall. The blog's entire editorial position is *against* the institution-aligned posture; the visual register must not borrow from it.
- **Don't** draft **SaaS landing templates** (PRODUCT.md anti-ref): no hero-metric + small-label headline, no three identical icon+heading+text cards, no gradient-text H1. The category default; refuse the cliché.
- **Don't** ship **Substack-default chrome** (PRODUCT.md anti-ref): plain serif on plain white with no identity is forfeit, not safety. This blog has a voice; the design must too.
- **Don't** slip into **hype-template crypto** (PRODUCT.md anti-ref): no animated mesh gradients, no holographic gloss, no neon-purple-on-pitch-black, no glow buttons, no "future of finance" hero copy. Punk-archival yes, hype-bro no.
- **Don't** use `#000` or `#fff` for body backgrounds or display type. Paper Bone (`#f5f5fa`) and Slate Night (`#303030`) are the canonical surfaces; Card White (`#ffffff`) is the one sanctioned pure-white, on card interiors only.
- **Don't** add a colored side-stripe (`border-left` / `border-right` > 1px in a category hue) anywhere except series-nav. The pattern is banned globally and survives only as the documented exception.
- **Don't** apply `background-clip: text` over a gradient to any heading. Solid color or nothing.
- **Don't** use category colors decoratively. A teal underline because the section "feels analytical" violates the Earned Accent Rule. Color is signal.
- **Don't** introduce a second serif. Fraunces is the only serif; any new editorial flourish uses Fraunces at a new weight or size, never a new family.
- **Don't** add `em dashes` or `--` in UX copy (carried from PRODUCT.md). Use commas, colons, semicolons, periods.
- **Don't** add `prefers-reduced-motion`-violating transforms or animations. The system already respects it; new motion must too.
- **Don't** ship a hover state that animates a CSS layout property (`width`, `padding`, `margin`). Use `transform` and `opacity` exclusively.
- **Don't** wrap every component in a card. Series-nav, glossary popover, and article-cards are cards; running prose, the kicker, the difficulty pills, and the breadcrumb are not.

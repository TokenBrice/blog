---
name: TokenBrice
description: Brutally Honest DeFi, a sovereign-stack editorial blog with a punk-archival visual register.
colors:
  paper: "#f4f6fa"
  surface: "#fcfdff"
  ink: "#171d26"
  ink-2: "#464e58"
  ink-3: "#666c75"
  rule: "#dadee3"
  slate: "#34495e"
  signal: "#cc361e"
  signal-wash: "#ffe0d4"
  dark-paper: "#1d2126"
  dark-surface: "#262b31"
  dark-ink: "#e4e8ed"
  dark-ink-2: "#b9bec6"
  dark-ink-3: "#9a9fa6"
  dark-rule: "#3e4349"
  dark-slate: "#a6c1dd"
  dark-signal: "#f77c56"
  dark-signal-wash: "#4d271d"
typography:
  display:
    fontFamily: '"Fraunces", Georgia, "Times New Roman", serif'
    fontSize: "clamp(3.4rem, 1.4rem + 2.6vw, 5.2rem)"
    fontWeight: 700
  headline:
    fontFamily: '"Fraunces", Georgia, "Times New Roman", serif'
    fontSize: "2.6rem"
    fontWeight: 700
  body:
    fontFamily: '"Inter Tight", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "1.8rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: '"Inter Tight", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "1.2rem"
    fontWeight: 700
rounded:
  card: "10px"
  chip: "3px"
spacing:
  space-1: "4px"
  space-2: "8px"
  space-3: "12px"
  space-4: "16px"
  space-5: "24px"
  space-6: "32px"
  space-7: "48px"
  space-8: "72px"
components:
  article-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
  context-note:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.chip}"
  glossary-chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.chip}"
---

# Design System: TokenBrice

## 1. Overview

**Creative North Star: "The Sovereign Edition"**

A long-form DeFi blog whose infrastructure is part of its argument. Hugo, local fonts and artwork, and self-hosted Matomo support a durable bilingual publication. There is no live IPFS mirror. The aesthetic is **punk-archival**: an irreverent editorial voice inside an unfashionable, durable shell. Fraunces carries the headlines; Inter Tight carries the working notebook.

**Key Characteristics:**
- One structural accent (slate) + one mark (red pen, marks only).
- No homepage masthead: the archive is the homepage.
- Tinted paper and ink, modest radii, quiet rules. No side stripes, including series navigation.
- Both languages and both colour schemes are first-class.
- Self-hosted assets, restrained motion and visible keyboard focus.

## 2. Colors: The Dissenting Slate Palette

`assets/scss/custom/tokens.scss` is the source of truth. Dark mode uses `[data-scheme="dark"]`.

| Role | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#f4f6fa` | `#1d2126` | Page background |
| `--surface` | `#fcfdff` | `#262b31` | Cards and quiet panels |
| `--ink` | `#171d26` | `#e4e8ed` | Primary text |
| `--ink-2` | `#464e58` | `#b9bec6` | Secondary text |
| `--ink-3` | `#666c75` | `#9a9fa6` | Tertiary text |
| `--rule` | `#dadee3` | `#3e4349` | Hairline separators |
| `--slate` | `#34495e` | `#a6c1dd` | Structural links and focus |
| `--signal` | `#cc361e` | `#f77c56` | Red-pen marks |
| `--signal-wash` | `#ffe0d4` | `#4d271d` | Status/warning note wash |

### Primary

Slate carries structure: links, controls, focus rings. The deeper interaction colour is `#2c3e50` light / `#c2d7eb` dark. Selected surfaces use `#e9edf3` light / `#30363d` dark.

### Secondary

Red pen is a mark, not another UI fill colour: drop cap, quote glyph, link-hover underline, reading-progress line, kicker square and OG band. Never red body text or solid red cards/buttons. The separately named signal wash is reserved for status and warning context.

### Tertiary

Category colour (`--cat`) is local to category identity and appears as small squares or bands, never as a text-bearing fill. Category artwork remains. Difficulty dots use green (`#22c55e` / `#16a34a`), amber (`#fbbf24` / `#ca8a04`) and red (`#f87171` / `#dc2626`), always paired with a level label.

### Neutral

Tinted paper, surface and ink roles replace the old white/black theme defaults. Components inherit semantic roles instead of inventing local body-text colours.

### Named Rules

**The Sovereign Stack Rule.** Fonts, scripts, images and analytics are self-hosted or absent. No runtime CDN dependency.

**The Earned Accent Rule.** One structural accent (slate) + one mark (red pen, marks only). Category and difficulty colours communicate identity, never garnish.

## 3. Typography

**Display & Headline Font:** self-hosted Fraunces 700, with Georgia and Times New Roman fallbacks.
**Body Font:** self-hosted Inter Tight 400/600/700, followed by system sans. No legacy font assets or font-host requests.
**Code Font:** Menlo, Monaco, Consolas, Courier New, monospace.

### Hierarchy

The root stays at 62.5%: **1rem = 10px**. No text below 12px. Small spacing, icon dimensions and radii are not text sizes.

| Token | Value | Role |
|---|---|---|
| `--fs-micro` | `1.2rem` | Structural labels, legal lines |
| `--fs-meta` | `1.4rem` | Dates, byline, metadata |
| `--fs-small` | `1.5rem` | Context notes, supporting copy |
| `--fs-body` | `1.8rem` (`1.7rem` at ≤767px) | Article prose |
| `--fs-lede` | `2.1rem` | Lead text |
| `--fs-h3` | `2.2rem` | Subheadings and reading-path titles |
| `--fs-card` | `2.6rem` (`2.8rem` at ≥1280px) | Article-card titles |
| `--fs-h2` | `2.8rem` | Body section headings |
| `--fs-display` | `clamp(3.4rem, 1.4rem + 2.6vw, 5.2rem)` | Page/article titles |
| `--measure` | `64rem` | Prose measure (~70–80 characters at 18px) |

Article line-height is 1.65 light / 1.7 dark. Trust metadata uses 1.5; context notes 1.65; the colophon 1.6.

### Named Rules

**The One-Serif Rule.** Fraunces is the only editorial serif.
**The Reading Measure Rule.** Use `--measure` for prose; never stretch body text to match a wide grid. On single pages the card itself is sized to `--measure` + card padding, so prose fills the card and the freed width is distributed around the columns (glossary index excepted).
**The Uppercase-Means-Structure Rule.** Uppercase is for labels, not shouting inside prose.

## 4. Elevation

**Flat at rest, lifts on touch.** Keep separation quiet and avoid ornamental depth. Existing theme shadow levels support cards; overlays may detach, running prose does not need a shadow. Respect reduced motion and never animate layout dimensions.

### Spacing and Radius Vocabulary

`--space-1` through `--space-8`: **4 / 8 / 12 / 16 / 24 / 32 / 48 / 72px**.
`--radius-card`: **10px**. `--radius-chip`: **3px**. Author portraits are circular; the site emblem is not cropped into a portrait circle.

## 5. Components

### Article Cards

Surface background, ink headings, 10px clipped corners. Fraunces card-scale titles, Inter Tight supporting copy. Cover crops respect `imagePosition`; category identity is a small mark, not white text on a category-colour pill.

### Trust Strip

A wrapping 14px metadata row under the title: author portrait/byline, publication date, meaningful update link, reading time, difficulty, format and translation. The portrait is 32px; the format label is a 12px outlined chip. Post disclosures occupy a separate full-width line when present.

### Context Note / Notice

Dated, sourced context above the body. A full 1px rule, 3px corners, 15px prose and a 12px uppercase label with a red square. Status notes and warning notices use signal wash. Sources remain normal accessible links. Takeaways contain two or three bullets. No side stripes.

### Colophon

Rule-separated groups, not a promotional card: series position, category plus the first eight plain-text tags and an expandable remainder, glossary concepts, author biography/follow links and legal line. Metadata is 14px, legal copy 12px, bio 15px. The author portrait is 48px.

### Keep Reading

At most two related posts plus a relevant guide link. Related-post thumbnails are 96×72px with 3px corners; descriptions are clamped to two lines. The guide link uses a quiet full border. Mobile stacks the layout; desktop makes room for the guide beside the posts.

### Reading Path

Numbered core then historical rows, with local thumbnails (120×80px desktop, 80×54px at ≤600px), Fraunces 22px titles, difficulty/reading-time metadata and explicit EN-fallback labels. Rows without artwork reclaim the thumbnail column. Thin bottom rules replace boxed cards. The guides landing page alone uses artwork tiles. Localized notes remain plain text.

### Disclosure Strip

Home gets a single quiet, bordered line about the author's Pharos and Polaris roles. Posts disclose declared projects in the trust strip. Roles only, never holdings. There is no projects banner or project-card grid.

### OG Cards

Build-generated localized **1200×630 JPEGs**, dark ink artwork with local Fraunces/Inter Tight, a small red-pen mark and the site emblem/wordmark. Posts can use a right-hand cover panel; `og_panel: false` disables it. Hubs, pages and glossary terms are text-only. The OG palette is fixed for sharing, independent of the reader's colour scheme.

### Glossary Chips

Index chips use inline SVG icons rather than emoji. Article concept links use 14px text, surface fill, a full rule, 3px corners and a 32px minimum height. They navigate to term pages; no inline popover system remains. Difficulty states pair colour with text, and filters retain keyboard focus.

### Identity

The purple ant **emblem is the site mark**: sidebar, footer and OG wordmark. The **Anthereum avatar is the author portrait**: byline and colophon. They are not interchangeable.

### Named Rules

**The Calm-Baseline Rule.** A context note, disclosure or legal line must not compete with the argument.
**The No-Side-Stripes Rule.** No coloured side rails on cards, notices or series navigation. Use a full rule, square mark or textual hierarchy.

## 6. Do's and Don'ts

### Do:
- Use semantic tokens in both schemes, not copied local colours.
- Preserve EN/FR parity and visibly label EN-only reading-path fallbacks.
- Keep every text size at least 12px; provide visible focus and roomy mobile controls.
- Pair colour with labels or shape; post tags are plain text.
- Let the writing carry the opinion and the chrome carry the structure.

### Don't:
- Import fonts, trackers or assets from a runtime CDN.
- Add a homepage hero or revive the projects banner.
- Fill buttons/cards with red pen or use it for body text.
- Add side stripes, gradient text, decorative glass or unnecessary motion.
- Drift toward corporate-fintech trust costumes, SaaS hero-metric templates, Substack-default anonymity or hype-template crypto.
- Introduce another serif, text below 12px, linked post tags or UX copy with em dashes.

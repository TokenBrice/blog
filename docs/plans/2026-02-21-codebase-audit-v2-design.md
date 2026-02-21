# Codebase Audit V2 — Design Document

**Date:** 2026-02-21
**Scope:** Code quality, performance, SEO, DRY/KISS/YAGNI compliance
**Approach:** Surgical strikes — strict priority order, one commit per logical change, grouped by risk

## Context

This Hugo blog (0.148.2 Extended, hugo-theme-stack) went through a theme migration and ~100 Hugo versions of evolution. A prior audit (v1, 4 sessions, 48 fixes) addressed the most critical issues. This v2 audit takes a step back to assess architectural health and eliminate remaining tech debt.

**Key decision:** All fixes use root overrides. Theme files in `themes/` are never modified directly.

## Phase 1 — Zero-Risk Quick Wins

No behavioral or visual impact. Pure housekeeping.

### 1.1 Fix .gitignore
- Replace `.gitignore` contents with `.gitignore.new` content
- Delete `.gitignore.new`
- Adds: `resources/_gen/`, `.image-cache/`, `dist/`, `build/`, `*.backup`

### 1.2 Remove tracked .backup files
- `git rm` the 22 `.backup` files in `content/categories/` and `public/categories/`
- Pattern already covered by updated `.gitignore`

### 1.3 Deduplicate glossary.json
- Remove 5 duplicate entries in `data/glossary.json` (EN section):
  - `bid-ask-spread`, `limit-order`, `market-depth`, `market-order`, `volume`
- Keep first occurrence, remove second

### 1.4 Override scrollspy.ts — clean console output
- Copy `themes/hugo-theme-stack/assets/ts/scrollspy.ts` → `assets/ts/scrollspy.ts`
- Change `console.warn()` → `console.debug()` (3 instances, lines 54, 60, 66)

### 1.5 Override main.ts — remove alert()
- Copy `themes/hugo-theme-stack/assets/ts/main.ts` → `assets/ts/main.ts`
- Change `alert(err)` → `console.error(err)` (line 88)
- Remove `console.log('Something went wrong', err)` (line 89, redundant with console.error)

### 1.6 Remove duplicate CSS declaration
- `assets/scss/glossary-links.scss` line 33: remove redundant `max-width: 300px`
- Next line (34) already overrides with `max-width: clamp(200px, 80vw, 300px)`

## Phase 2 — Low-Risk SEO & Accessibility

Semantic HTML changes. No visual impact.

### 2.1 Article title h2 → h1
- File: `layouts/partials/article/components/details.html` (already overridden)
- Change `<h2 class="article-title">` → `<h1 class="article-title">`
- Verify CSS: check if theme styles `.article-title` by tag or class
- Add CSS override if needed to maintain identical sizing

### 2.2 Add alt text to list.html
- Create override: `layouts/_default/list.html`
- Copy from `themes/hugo-theme-stack/layouts/_default/list.html`
- Add `alt="{{ .Title }}"` to `<img>` tags (lines ~35, ~40)

### 2.3 Add og:image:alt
- Create override: `layouts/partials/head/opengraph/provider/base.html`
- Copy from theme, add after og:image block:
  ```html
  <meta property="og:image:alt" content="{{ with .Params.description }}{{ . }}{{ else }}{{ .Title }}{{ end }}" />
  ```

### 2.4 Add twitter:image:alt
- Create override: `layouts/partials/head/opengraph/provider/twitter.html`
- Copy from theme, add:
  ```html
  <meta name="twitter:image:alt" content="{{ with .Params.description }}{{ . }}{{ else }}{{ .Title }}{{ end }}" />
  ```

### 2.5 Move font loading to `<head>`
- Create override: `layouts/partials/footer/components/custom-font.html` (empty file)
- Add to `layouts/partials/head/custom.html`:
  ```html
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap">
  ```
- Place after existing preconnect hints

### 2.6 Add CDN preconnect
- File: `layouts/partials/head/custom.html`
- Add: `<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>`

### 2.7 Add Matomo dns-prefetch
- File: `layouts/partials/head/custom.html`
- Add: `<link rel="dns-prefetch" href="https://ecocrypto.fr">`

## Phase 3 — Medium-Risk CSS Refactor

Visual output must remain pixel-identical.

### 3.1 Convert glossary.css → SCSS
- Move `assets/css/glossary.css` → `assets/scss/glossary.scss`
- 1:1 port (preserve structure)
- Replace hardcoded hex colors with CSS variables from theme
- Replace raw `@media (max-width: 768px)` with `@include respond()` where applicable
- Update imports in glossary layout templates
- Remove `!important` from dark mode selectors (lines 907, 911, 915) by using proper specificity

### 3.2 Convert glossary-term.css → SCSS
- Move `assets/css/glossary-term.css` → `assets/scss/glossary-term.scss`
- Same treatment as 3.1
- Update imports in glossary-term layout template

### 3.3 Extract difficulty color variables
- File: `assets/scss/custom/difficulty-badges.scss`
- Add at top:
  ```scss
  $difficulty-beginner: #22c55e;
  $difficulty-beginner-dark: #16a34a;
  $difficulty-intermediate: #fbbf24;
  $difficulty-intermediate-dark: #ca8a04;
  $difficulty-expert: #f87171;
  $difficulty-expert-dark: #dc2626;
  ```
- Replace all 9+ hardcoded color instances

### 3.4 Extract error color variable
- File: `assets/scss/glossary-links.scss`
- Replace hardcoded `#e74c3c` with `var(--error-color, #e74c3c)`
- Define `--error-color` in `assets/scss/custom.scss` `:root` block

### 3.5 Remove !important in glossary dark mode
- Part of 3.1 conversion
- Fix specificity so dark mode selectors win without `!important`
- Target selectors: `.term-name`, `.full-term`, `.faq-question`

### 3.6 Unify body text color
- File: `assets/scss/custom.scss`
- Change direct `color: #595959` to `--body-text-color: #595959` in `:root`
- Ensures all components reading the variable get the correct value

## Out of Scope (Deferred)

- Matomo submodule dirty state cleanup
- PhotoSwipe 4.1.3 → 5.x upgrade
- Video shortcode attribute improvements
- Missing French translations (29 posts)
- Missing cover images (6 posts)
- Stale remote branch cleanup
- Service worker / PWA
- HTTP caching headers
- Critical CSS inlining

## Verification Strategy

- `hugo server` after each phase to verify no build errors
- Visual comparison on: article page, glossary hub, glossary term, list page, homepage
- Both light and dark mode
- Both desktop and mobile viewport
- Both EN and FR language versions

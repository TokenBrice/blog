---
target: the whole blog design
total_score: 25
p0_count: 3
p1_count: 3
timestamp: 2026-05-18T23-52-05Z
slug: blog-whole-design
---
# Critique — TokenBrice blog (whole design)

## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Reading-progress bar good; sidebar Categories widget doesn't highlight the current category when on a category page. |
| 2 | Match System / Real World | 3 | Domain language is correct (date, reading-time, difficulty). The unexplained 🐜 emoji and the lowercase secondary "tokenbrice" handle read as inside-jokes. |
| 3 | User Control and Freedom | 3 | Skip-to-content present, back paths obvious. No filter combinators (category + difficulty), no clear-search. |
| 4 | Consistency and Standards | **1** | **Documented design system diverges from production CSS.** Fraunces declared in DESIGN.md but `h1.article-title` ships in Lato 22px/600. Inter appears in computed styles but is not in DESIGN.md. Body color is rgb(0,0,0) — the No-Pure-Black Rule is violated on `<body>`. Three tag shapes across the site (pill / 4px tag / plain link). |
| 5 | Error Prevention | 3 | Mostly N/A; search has no empty-query guard, no autosuggest from the 130-term glossary corpus next door. |
| 6 | Recognition Rather Than Recall | 2 | Sidebar nav has icon + label. Glossary index category chips + A–Z bar look like filters and aren't — recognition→recall regression. |
| 7 | Flexibility and Efficiency | 2 | No ⌘K/`/` to open search; no RSS link in chrome (despite RSS being declared sovereignty stack); no copy-permalink/share on posts. |
| 8 | Aesthetic and Minimalist Design | 3 | Article body and term pages are calm and well-measured. Sidebar stack (6 widgets, ~30 link targets) is the minimalism failure. |
| 9 | Error Recognition / Recovery | 2 | Console error on /glossary/ (PhotoSwipe lib not loaded) — unsurfaced but real. Search returns a generic page without "try a glossary term" recovery. |
| 10 | Help and Documentation | 3 | The glossary itself is excellent documentation. No "how to read this blog" intro for first-timers; difficulty filter is undocumented as a mechanism. |
| **Total** | | **25 / 40** | **Acceptable, with significant gaps.** |

## Anti-Patterns Verdict

**LLM assessment.** Not AI slop in the obvious way — no gradient text, no glassmorphism, no icon-grid-of-three. But the design is parked in the second-order editorial-typographic trap the brand register explicitly names (Stripe/Notion-adjacent fingerprint: serif display + uppercase track-spaced labels + cream paper + ruled separators). The PRODUCT.md claim is "punk, irreverent, dissenting"; what ships is archival without the punk. The repeated tiny uppercase tracked labels above every sidebar widget ("CATEGORIES / TAGS / ARCHIVES / EXPERTISE LEVEL") are the precise "AI scaffolding unless it's a deliberate named system" anti-pattern called out in brand.md.

**Deterministic scan.** detect.mjs shim was broken; the underlying engine ran successfully. **3,367 findings** in `public/`, dominated by:
- **3,256× overused-font** — `font-family: Lato` and `font-family: Inter` repeated across every rendered page. Inter ships but is undocumented; Lato is loaded from Google Fonts rather than self-hosted (violates Sovereign Stack Rule).
- **103× side-tab** — 4px-thick colored left-borders on glossary callout blocks (term-definition, term-example, term-risks) and series-nav. DESIGN.md sanctions exactly ONE exception (series-nav); the glossary callouts are 100+ violations of the same absolute ban.
- **5× border-accent-on-rounded** in glossary-term.css (`border-top: 4px solid`).
- **3× layout-transition** in style.css (`transition: width`) — animates a CSS layout property, explicit DESIGN.md "Don't".

**Visual overlays.** None — Assessment B reasonably skipped the live-server overlay flow because targets are https:// URLs, not file://. Fallback signal: detector counts + browser computed-style evidence + screenshots.

**Cross-assessment agreement.** The shipped site does not match the design system documented in DESIGN.md. The most load-bearing rule (Sovereign Stack) and the most identity-defining choice (Fraunces) are both being violated by production CSS.

## Overall Impression

A long-form reading surface that is genuinely excellent mid-post (Lato 1.85 line-height, calm column, restrained accents) wrapped in blog-template chrome the brand explicitly bans (right-rail widget stack, uppercase-label scaffolding, opening above-the-fold self-promotion). The reader's emotional arc is awkward-open → calm-middle → dead-end. The biggest single opportunity isn't a redesign; it's closing the gap between the documented system and the shipped system, then collapsing the sidebar.

## What's Working

1. **Post body typography and measure.** Lato body at 1.85 line-height in the article column with dissenting-slate links, hairline rules, the kicker meta strip. A literate reader will trust the writing because the type respects them. Note: this trust is built on Lato, not Fraunces — the headline-serif identity exists only in the doc.
2. **Glossary term page architecture.** Definition / Example / Risks / Related Terms / Related Articles is a better information design than any DeFi competitor ships. The tinted callouts work as IA. (They violate the side-stripe ban as implementation; the structure itself is good.)
3. **No third-party trackers.** Only Matomo (declared) plus font/CDN regressions. The privacy posture is real even where asset-hosting has slipped.

## Priority Issues

### [P0] Shipped CSS diverges from documented DESIGN.md
- **What.** `h1.article-title` renders in Lato 22px / weight 600 / rgb(0,0,0), not Fraunces weight 700 as specified. Body text computes to rgb(0,0,0), not Ink Body #595959. Inter appears in computed styles and is not in DESIGN.md. Google Fonts (fonts.googleapis.com + fonts.gstatic.com) and jsDelivr (node-vibrant on every page, photoswipe on posts) load from third-party CDNs.
- **Why it matters.** DESIGN.md's first Named Rule is the Sovereign Stack Rule. The site uses three CDNs that violate it. The font system that defines the punk-archival identity (Fraunces headlines + Lato body) is half-applied: Lato yes, Fraunces no. Every future /impeccable command will operate on a spec that doesn't match production, so fixes will compound the drift. rgb(0,0,0) on body explicitly violates the No-Pure-Black Rule.
- **Fix.** Two paths. (a) Build to the spec: self-host Fraunces + Lato woff2 in `static/fonts/`, replace Google Fonts `<link>` with local `@font-face`, audit Inter out of the SCSS pipeline, replace node-vibrant (or self-host the bundle), self-host PhotoSwipe, set body color to #595959. (b) Spec to the build: rewrite DESIGN.md §3 honestly if Lato-only is the intended state. Path (a) is the right answer given the editorial position.
- **Suggested command.** `/impeccable harden` followed by `/impeccable polish` once the divergence is closed.

### [P0] Sidebar widget stack is the brand's antithesis
- **What.** Six right-rail widgets (Search, Archives, Expertise Level, Categories, Tags, dark toggle) totalling ~30 link targets, each prefaced by an uppercase tracked label. Identical visual weight, no progressive disclosure.
- **Why it matters.** Literal "repeated tiny uppercase tracked labels above every section heading" anti-pattern in brand.md. Blows past Miller's Law on every page load. Signals "blog template" louder than dissenting-slate signals identity. Dilutes the Earned Accent Rule.
- **Fix.** Collapse to two widgets at rest: Search and a single Browse panel that toggles among Categories / Archives / Difficulty (one widget, three views, inline tabs). Move Tags to a `/tags/` index page. Drop the uppercase labels on widgets that don't need them.
- **Suggested command.** `/impeccable distill` on the sidebar.

### [P0] Glossary index "filter chips" don't filter
- **What.** The category strip (`💰 Yields & Returns`, `⚠️ Risks & Security`, etc.) and the A–Z bar above the 130-term list look exactly like filter UIs but are decorative.
- **Why it matters.** Affordance violation. A learner taps a chip, nothing happens, trust takes a hit. A practitioner who wants "show me only risk terms" gets a 130-item scroll. The glossary is the blog's most-architected asset; the index page squanders it.
- **Fix.** Make the category chips real single-select filters (URL-hash-persisted so a filtered view is shareable); make the A–Z bar a sticky in-page anchor jump. Add a "Start here" curated cluster above the chip strip for first-timers.
- **Suggested command.** `/impeccable craft` (this is a real feature, not a polish).

### [P1] Side-stripe absolute-ban violations beyond the sanctioned exception
- **What.** Detector found 103 side-tab matches and 5 border-accent-on-rounded matches. Confirmed in browser: `p.term-definition` ships `border-left: 4px solid rgb(52,73,94)`, `div.term-example` ships `border-left: 4px solid rgb(59,130,246)`, `div.term-risks` ships `border-left: 4px solid rgb(245,158,11)`. DESIGN.md §5 sanctions exactly ONE side-stripe exception (series-nav).
- **Why it matters.** The brand register lists side-stripe `border-left > 1px` as an absolute ban. Three callout patterns on every glossary term page = ~100+ visible violations across the site. They're decorative-colored, not informational like series-nav.
- **Fix.** Rewrite callouts with full hairline borders + an 8% background tint, OR with leading icons + a heavier label, OR with simple typographic separation. The series-nav stripe stays; nothing else.
- **Suggested command.** `/impeccable polish`.

### [P1] Homepage opens with the author's own businesses before the editorial position
- **What.** First surface above the fold is a dark Projects banner promoting Pharos and Polaris (the author's businesses) with deep navy + cream — the chromatically loudest moment on the site. "Brutally Honest DeFi" sits in the sidebar where it competes with the banner for first-paint.
- **Why it matters.** A first-time reader sees what reads as a sponsored block before they know who's writing. PRODUCT.md positions the blog as anti-sponsored-takes; the optics undermine the editorial position before it can introduce itself. The Projects banner is a signature component — don't kill it, frame it.
- **Fix.** Either (a) push the Projects banner below the first row of articles, OR (b) keep it on top but add a one-line provenance ("Projects from the author — disclosed by design") so the relationship is explicit. The disclosure IS the punk move.
- **Suggested command.** `/impeccable shape` on the homepage hero.

### [P1] No "next read / subscribe" terminal at end of post
- **What.** A 16-minute long-form ends with nothing. No related posts, no series-nav (where applicable), no newsletter/RSS prompt, no follow CTA.
- **Why it matters.** Success outcome #3 in PRODUCT.md is "Following — convert trust to ongoing readership across social surfaces." Earns trust mid-post then leaves the reader at a dead-end footer. Four social icons are in the sidebar — invisible at the moment of highest engagement.
- **Fix.** End-of-post block: 2 related posts (same category or series) + 4 social follow targets + RSS link, styled as a single calm composition (NOT a SaaS subscribe-hero with gradient).
- **Suggested command.** `/impeccable craft` (new component).

### [P2] No 2-axis filter on category pages
- **What.** Riya can't ask "Expert posts in Lending"; clicking a difficulty pill leaves the category and jumps to a flat difficulty list.
- **Fix.** Compose via URL params (`/categories/lending/?level=expert`); show active filter chips above the post list with one-tap clear.
- **Suggested command.** `/impeccable craft`.

### [P2] Double H1 per page + `transition: width` in CSS
- **What.** Every post has two `<h1>`s in the DOM: `h1.site-name` and `h1.article-title`. Detector flagged 3 `transition: width` declarations in style.css.
- **Why it matters.** Double H1 is an HTML semantic error. Width transition causes layout thrash and is an explicit DESIGN.md "Don't".
- **Fix.** Demote `h1.site-name` to a `<div>` or `<p>`; rewrite the width transition as `transform: scaleX()` or remove it.
- **Suggested command.** `/impeccable harden`.

### [P3] Unexplained signature elements (🐜 ant emoji, "tokenbrice" lowercase tagline)
- **What.** Punk-irreverent only works when the irreverence is legible. The ant has no title attribute, no footnote.
- **Fix.** Give it a one-word context via tooltip or `<abbr>`, or remove. Drop the redundant lowercase handle.

## Persona Red Flags

**Riya (practitioner researching a protocol mid-investigation).** Lands on a post via Google, scans for the verdict, wants to verify the author's history with this protocol. Fails: no inline author micro-bio above the fold; no "more posts on Curve" / "previous coverage" rail to triangulate; the sidebar widget stack is irrelevant to her mid-investigation and burns visual budget; she can't filter the category page to "Lending + Expert" to find prior deep-dives. The Projects banner promoting Polaris on a Lending post is an undisclosed conflict-of-interest tell for her.

**Jordan (learner using the glossary).** Opens /glossary/, sees 130 terms. Fails: the category chips at the top look filterable but aren't (immediate trust hit); the A–Z bar same; no recommended starter cluster / "start here" path; no difficulty marker on glossary entries themselves (terms aren't tagged Beginner/Expert even though the difficulty taxonomy exists site-wide). Once she reaches a term the page is excellent — but the journey there is friction.

**Sam (mobile reader on a phone, 390px).** The homepage compresses the Projects banner into a small dark strip that loses signature impact while keeping its visual weight; the dark-mode toggle and language switch are buried inside the hamburger; no thumb-zone bottom nav; the 🐜 glyph takes ~10% of header width; tap targets on the A–Z bar and difficulty pills look <44pt; long titles wrap to 3–4 lines on cards at 390px with no truncation, eating vertical real estate.

## Minor Observations

- The footer "Theme Stack designed by Jimmy" is honest but breaks the sovereign-authored framing — attribute on /about/ instead of every page.
- cat-ochre (#806504) reads almost as brown-ink at-a-glance vs. brighter siblings — color-as-signal is borderline.
- Series-nav and projects-card radius (6/8px) diverges from system 10px — DESIGN.md sanctions this but it reads as inconsistent on first glance.
- The "Brutally Honest DeFi" tagline exists only in the sidebar — it's the blog's thesis and it's whispered.
- Console error on /glossary/ (PhotoSwipe lib not loaded) — main.ts calls into PhotoSwipe on pages where the lib isn't requested. Cheap fix: guard the call with `if (window.PhotoSwipe)`.
- B's run dumped six screenshot PNGs at the project root (home-1440.png, home-390.png, glossary-1440.png, analysis-1440.png, post-crv-velo-1440.png, glossary-apy-1440.png). Move to lighthouse-reports/ or delete.
- Pagination ("1, 2, …, 9") at homepage bottom is bare-bones; no "page 1 of 9, ~85 posts total."

## Questions to Consider

1. If the writing is the asset, why does the homepage open with two business cards instead of the latest take?
2. What does "punk" cost the design? Right now: nothing visible. There's a drop-cap (which doesn't even render in Fraunces because Fraunces isn't loaded) and a dissenting-slate accent. Where is the gesture a corporate-fintech blog could never make?
3. Was Fraunces ever actually deployed, or did it lapse? Is this an aspiration that was never realised, or a regression?
4. Why does the glossary — your best-architected asset — present as a wall, not a database? 130 entries, 3 difficulty tiers, 8 category facets are already defined.
5. Which P0 do you address first: closing the spec/build gap, or collapsing the sidebar?

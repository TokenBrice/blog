# Product

## Register

brand

## Users

Two overlapping audiences, served in priority order:

1. **DeFi practitioners** — active LPs, farmers, traders, and protocol researchers who land here mid-investigation. They're capital-at-risk and time-constrained: they skim first to gauge whether the take is worth the read, then dive deep when it is. They've seen every hype cycle and have a low tolerance for fluff, sponsored takes, and consensus narratives.
2. **Crypto-literate learners** — readers building foundational understanding via the glossary, tutorials, and difficulty-tagged posts. They're not absolute beginners; they want to graduate into the practitioner audience and use this site as a trusted ramp.

The site also gets read by industry peers and journalists, but design decisions should be made for (1) and (2). If a choice serves practitioners and learners at the cost of peer-friendly polish, take it.

## Product Purpose

TokenBrice.xyz is a personal, long-form DeFi blog with a stated editorial position: *brutally honest*. It exists to publish independent analysis of protocols, liquidity strategies, and the broader DeFi landscape — including takes the rest of the space won't publish because they're sponsored, captured, or conflict-averse.

Success looks like three outcomes, in order:

1. **Trust** — readers return because the calls land and the reasoning holds up over cycles.
2. **Understanding** — readers leave a post able to make a better-informed decision about a specific protocol, strategy, or risk.
3. **Following** — that trust and understanding convert to ongoing readership across the social surfaces (X, YouTube, Telegram, Farcaster, RSS).

The blog is also a statement of practice: it runs on a privacy-respecting, open-source stack (Hugo, Matomo with IP anonymisation, IPFS replication), and that infrastructure is part of the argument, not incidental to it.

## Brand Personality

**Punk, irreverent, dissenting.**

Voice: first-person, sharp, willing to name names. Comfortable with controversy. Treats the reader as a peer who can handle a strong take and verify the work. Allergic to hedging, throat-clearing, and the bureaucratic register that crypto media drifted into.

Emotional goals: the reader should feel like they're getting the inside view from someone who has skin in the game and no incentive to soften it. Confidence without arrogance — the writing earns its tone with rigor, not volume.

Crypto-native energy is welcome; the punk register lives comfortably in the crypto aesthetic lineage (cyber, terminal, irreverent typography). What it must NOT slip into is the hype-template version of that aesthetic (see anti-references).

## Anti-references

What this should NOT look or feel like:

- **Corporate fintech (navy + gold, stock-photo trust signals).** The TradFi safe-mode design that signals trustworthiness through blandness. JPMorgan, Fidelity, "your bank but online." This blog's entire editorial position is *against* that institution-aligned posture, so its visual register must not borrow from it.
- **SaaS landing template.** Hero metric + small label, three identical feature cards, gradient-text headline, "trusted by" logo wall. The category default that screams "I used a Tailwind template." Refuse the cliché.
- **Substack-default newsletter aesthetic.** Plain serif on plain white, generic blog chrome, no identity. The "respectability via blandness" move for the writer crowd. This blog has a voice; the design must too.
- **Hype-template crypto.** Even though crypto-native aesthetics are fair game, the specific failure mode is the generic web3 landing kit: animated mesh gradient backgrounds, holographic gloss, neon-purple-on-pitch-black, glow buttons, "the future of finance" hero copy. Punk yes, hype-bro no.

## Design Principles

1. **Practice what you preach.** The stack embodies the values the writing argues for — privacy, openness, sovereignty. No Google Fonts, no third-party trackers, no surveillance infrastructure. If a design choice requires importing a SaaS dependency that contradicts the editorial position, the choice is wrong.
2. **Brutal honesty over palatability.** The visual register mirrors the editorial register. Strong opinions, no hedging, no consensus aesthetic. Comfortable with friction when friction is honest.
3. **Earned trust, not borrowed authority.** Refuse trust-by-association tropes (corporate-fintech polish, big-publication serif, "trusted by" logo walls). Authority comes from the argument and the track record, not the costume.
4. **Built to outlast the cycle.** Durable typography, restrained motion, an aesthetic that won't date the moment the meta shifts. Punk in attitude, archival in construction. The site is on year 8 and should plausibly run another decade in the same shell.
5. **Practitioner-first, learner-friendly.** Depth is the headline. The glossary, difficulty tags, and bilingual support make the depth accessible without dumbing it down. Never sand a sharp take to be more beginner-friendly; instead, link the prerequisites.

## Accessibility & Inclusion

No formal WCAG target. Best-effort baseline:

- Both light and dark themes should be readable in their respective ambient conditions (`data-scheme` toggle is in place; default is `auto`).
- Honor `prefers-reduced-motion` for any motion added in the future.
- No color-only signaling — pair color with shape, icon, or text in any meaningful state.
- Bilingual EN/FR is a first-class accessibility surface for this audience; treat translation parity as part of inclusion, not a nice-to-have.
- Avoid contrast traps in the punk/dissenting aesthetic (low-contrast "edgy" type, decorative-only color). When the aesthetic and readability conflict, readability wins.

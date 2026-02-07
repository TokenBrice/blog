# Liquity (liquity.org) — Adversarial Due Diligence Report

**Date:** 2026-02-06
**Investigator:** Claude Opus 4.6 (adversarial mode)
**Subject:** Liquity Protocol — V1 (LUSD) and V2 (BOLD) decentralized borrowing on Ethereum
**Verdict:** **CAUTIOUSLY POSITIVE** | Confidence: HIGH

---

# MOST IMPORTANT NOTICE OF THE WHOLE DOCUMENT, PLEASE READ

IMPORTANT NOTICE: THIS REPORT HAS BEEN FULLY OUTPUTED BY CLAUDE - THIS NOTE IS THE ONLY THING MANUALLY ADDED.


---

## 1. Executive Summary

Liquity is one of the most technically credible and genuinely decentralized protocols in DeFi. V1 operated as a fully immutable, governance-free CDP system for 5 years with zero exploits — an exceptional track record. V2 (BOLD) represents a fundamental redesign with user-set interest rates, multi-collateral support, and sustainable yield from borrower interest rather than token emissions. **The protocol is not a scam, not Ponzi-dependent, and generates real revenue from identifiable sources.** This puts it in a small minority of DeFi protocols.

However, Liquity is not without material concerns. V2 launched with a critical Stability Pool vulnerability that escaped 6+ professional audit firms, forcing a full redeployment. LQTY has lost 99.4% of its value from ATH. V1 is in terminal decline ($4.5B peak → $158M). And the BUSL licensing model on V2 introduces centralization tension that contradicts the permissionless ethos.

### Top 3 Risks

1. **V2 Stability Pool bug (Feb 2025)** — Critical vulnerability within 3 weeks of launch, despite multiple audits + formal verification. Required full redeployment. Undermines the "immutable and battle-tested" narrative.
2. **Massive value destruction** — LQTY -99.4% from ATH. V1 TVL -96.5% from peak. LUSD supply collapsed from $1.5B+ to $31M. V2 TVL already -50% from its own peak.
3. **BUSL licensing contradicts decentralization claims** — Liquity AG controls who can deploy V2 code until September 2027, functioning as a centralized gatekeeper.

### Top 3 Positive Signals

1. **Genuine immutability (V1) — verified** — No admin keys, no governance, no upgrade proxy. 5 years of operation without a single exploit. Gold standard for trustless DeFi.
2. **Real revenue, not emissions** — V2 generates ~$200K/month from borrower interest. LQTY is non-inflationary (fixed 100M supply). Yield source is identifiable and sustainable.
3. **Exemplary incident response** — When the V2 bug was found: immediate public disclosure, clear user guidance, 800-researcher Cantina audit contest before relaunch. No funds were lost. This is how responsible teams behave.

---

## 2. Team Assessment

**Verdict: SUBSTANTIALLY CREDIBLE — Moderate-High Confidence**

No lawsuits, regulatory actions, scam associations, criminal records, or deleted content found for any team member. The engineering team has deep, verifiable commit histories that would be extremely difficult to fabricate.

### Robert Lauko — Founder / Head of Research

| Claim | Status |
|-------|--------|
| PhD in Law, University of Zurich | **VERIFIED** (multiple independent sources) |
| EPFL Microengineering studies | **VERIFIED** |
| DFINITY researcher (2017-2019) | **VERIFIED** (cross-referenced via DFINITY Ecosystem Fund investment, Waldburger connection) |
| BIS (Bank for International Settlements) author | **VERIFIED** (author page exists) |

- **GitHub:** `cvalkan` — 103 commits to liquity/dev, mostly documentation/research. Consistent with non-developer founder role.
- **Flag:** Unexplained removal from Liquity AG board (Vice President) in February 2023 per Swiss commercial register. No public announcement. **Severity: Low** — could be routine corporate restructuring.

### Rick Pardoe — Co-Founder / Lead Engineer

| Claim | Status |
|-------|--------|
| Physics + Economics degrees | **UNVERIFIABLE** — no university ever named |
| Self-taught Solidity developer | **VERIFIED** via GitHub trajectory |

- **GitHub:** `RickGriff` — 846 commits to V1, 304 to V2. His repo history shows a clear self-taught trajectory from Ruby beginner (Oct 2017) to advanced Solidity developer (Mar 2019). This evolution is authentic and extremely hard to fake.
- Created `decimath` — a gas-efficient fixed-point math library for Solidity (original research-grade work).
- Possible prior career at TechAlign/JBA Consulting (environmental consulting) based on a second LinkedIn profile.

### Daniel Simon — Top Code Contributor

- **GitHub:** `danielattilasimon` — **#1 contributor to both V1 (1,112 commits) and V2 (742 commits)**. Has written more Liquity code than anyone else.
- Previously at Cognex Corporation (NASDAQ: CGNX) — **VERIFIED** via multiple sources.
- The true technical engine of the project.

### Bingen Eguzkitza — Head of Development

- **GitHub:** `bingen` — 581 commits to V1, 701 to V2. Account since 2011 with 110 followers.
- **Core contributor to Aragon** (major Ethereum DAO project) — **VERIFIED** via Aragon blog posts.
- Personal blog demonstrates real technical depth in Ethereum/Solidity/mathematics.

### Pierre Bertet — V2 Frontend

- **GitHub:** `bpierre` — 617 commits to V2. Account since 2008 with 439 followers.
- Previously at Aragon One and Canonical (Ubuntu) — **VERIFIED**.
- Created the popular `useWallet()` React hook for Ethereum.
- Now at Tempo.xyz (may have left Liquity).

### Corporate & Investor Network

- **Liquity AG** — Swiss-registered company (CHE-184.101.707). SEC CIK 0001826497 — showing compliance awareness unusual for DeFi.
- **DFINITY insider network:** Cedric Waldburger co-founded DFINITY → employed Lauko there → invested in Liquity via Tomahawk.VC (pre-seed) → sits on Liquity's board. DFINITY Ecosystem Fund also invested in seed round. Tight but not unusual for Swiss Crypto Valley.
- **Alameda Research** was a Series A investor. Not evidence of wrongdoing by Liquity, but FTX/Alameda bankruptcy estate likely liquidated LQTY holdings, contributing to sustained sell pressure.

### Team Red Flags

| # | Finding | Severity |
|---|---------|----------|
| 1 | V2 bug escaped multiple audits + formal verification | Medium |
| 2 | Robert Lauko board removal (Feb 2023) unexplained | Low |
| 3 | Rick Pardoe education claims unverifiable | Low |
| 4 | DFINITY-Waldburger-Tomahawk insider network | Low |
| 5 | Alameda Research as Series A investor | Informational |

---

## 3. Third-Party Consensus

**Verdict: GENERALLY POSITIVE with notable caveats**

The ecosystem broadly views Liquity as one of the most decentralized and technically sound lending protocols in DeFi.

### Independent Safety Ratings

- **DeFiSafety:** Among the safest protocols ever reviewed.
- **DeFiScan:** Highest decentralization score.
- **Exponential DeFi:** Grade A.

### Audit Pipeline

**V1:** Trail of Bits (with written invariants), Coinspect, active bug bounty.

**V2 (post-redeployment):** Trail of Bits, ChainSecurity, Dedaub (2 rounds), Coinspect, Certora formal verification, Recon review, Cantina audit competition (5 weeks, 800+ researchers, $350K bounty). This exceeds what most DeFi protocols invest in security.

**Critical caveat:** The initial V2 deployment was ALSO audited by multiple firms and failed within 3 weeks. Dedaub specifically found "a relatively high number of accounting bugs" and recommended additional auditing. Coinspect found an oracle-based BOLD depeg risk (BOLD-05: single oracle failure can halt redemptions across ALL branches).

### Media Coverage

Covered factually by The Defiant, The Block, Blockworks, CoinTelegraph, Messari, Nansen. No publication treats it as suspicious. **No fraud or integrity allegations found anywhere.**

### Community Sentiment

Generally positive among DeFi-native users. Main criticisms from the community:
- LUSD premium problem (consistently trading above $1)
- Redemption mechanism punishing small borrowers
- LQTY tokenomics structurally flawed — one analyst wrote: "The tokenomics doomed the price and adoption of LQTY from day 1"
- Chicken Bonds entered a death spiral (bLUSD price declined → APR collapsed → no rebonding)

### Regulatory Status

No regulatory actions, warnings, or investigations found. The governance-free, immutable design reduces regulatory attack surface.

### Rekt News / Hack Databases

**Zero entries.** No Rekt News article on Liquity. No DeFiLlama hack database entry. This is a genuinely positive signal for a 5-year-old protocol that peaked at $4.5B TVL.

---

## 4. On-Chain Findings

### Protocol Metrics

| Metric | Value | Source |
|--------|-------|--------|
| Combined TVL | $247.74M | DeFiLlama |
| V1 TVL | $157.75M | DeFiLlama |
| V2 TVL | $89.99M | DeFiLlama |
| LQTY Price | $0.35 | CoinGecko |
| Market Cap | $33.84M | DeFiLlama |
| Mcap/TVL | 0.14 | DeFiLlama |
| All-Time Fees (V1) | $84.79M | DeFiLlama |
| All-Time Fees (V2) | $1.93M | DeFiLlama |
| Treasury | $1.36M | DeFiLlama |
| LUSD Supply | $31.07M | DeFiLlama |
| BOLD Supply | $30.44M | DeFiLlama |

### TVL History

**V1:** Peak $4.5B (May 2021) → $158M now. **-96.5% decline.** Terminal, irreversible decline driven by the redemption mechanism creating a borrower death spiral. LUSD supply collapsed from $1.5B+ to $31M.

**V2:** Launched Jan 2025 → Bug/collapse Feb 2025 ($25M) → Relaunched May 2025 ($70M) → Peak $180M (Oct 2025) → $90M now. **Already -50% from its own peak in 4 months.** Product-market fit question remains open.

### Smart Contract Risk Assessment

**V1 Immutability: VERIFIED.** No admin keys, no proxy patterns, no upgrade mechanisms, no governance module. All parameters hardcoded at deployment. Cannot be paused, upgraded, or modified by anyone — including the Liquity team. Independently verified by Trail of Bits and Coinspect. **This is the gold standard for trustless DeFi and is extremely rare.**

**V2 Architecture:** Also immutable post-deployment. Multi-collateral (ETH, wstETH, rETH). User-set interest rates. No Recovery Mode (removed from V1). Troves are ERC-721 NFTs (transferable). **Oracle changed from Tellor (decentralized) to Chainlink (centralized multisig) — a pragmatic but philosophically significant downgrade.**

**Centralization vectors:** Effectively none in V1 or V2. No admin keys, no multisig with special privileges, no governance module. One of Liquity's strongest attributes.

### Token Distribution

| Category | Amount | % |
|----------|--------|---|
| Investors | 33.90M | 33.9% |
| Community Rewards (Stability Pool) | 32.00M | 32.0% |
| Team and Advisors | 23.66M | 23.7% |
| Liquity AG Endowment | 6.06M | 6.1% |
| Community Reserve | 2.00M | 2.0% |
| Uniswap LP Rewards | 1.33M | 1.3% |
| Service Providers | 1.04M | 1.0% |

**57.6% insider allocation** (33.9% investors + 23.7% team). Aggressively high for a protocol marketing itself as community-first. For context: Uniswap 17.8% to investors, Aave ~23%. All investor tokens fully unlocked since March 2022.

### Treasury

**$1.36M** — extremely thin for a protocol with $248M TVL. Compare: Uniswap ~$3B+, Aave ~$100M+, MakerDAO ~$300M+. Direct consequence of governance-free design — no DAO treasury accumulation mechanism. Raises questions about long-term development funding runway.

### Revenue & Sustainability

**V1:** Death spiral. $15K/month in fees. One-time fee model structurally front-loaded.

**V2:** $150-230K/month from ongoing borrower interest. 75% to Stability Pool depositors, 25% to PIL. Annualized ~$2.4M on $90M TVL = 2.7% fee yield. **Sustainable and non-emission-dependent.** Current SP yields (34-66% APY) are real but will compress as more capital enters.

### Stablecoin Assessment

Combined LUSD + BOLD supply: $61M. For context: DAI $4.6B, GHO $527M, crvUSD $279M. Liquity's stablecoins are a rounding error in the market. **Legacy BOLD from the vulnerable first deployment still has $0.38M in circulation** — users who didn't withdraw are stuck, illustrating the double-edged nature of immutability.

### Funding

Series A: $6M led by Pantera Capital (March 2021). Other investors: Nima Capital, Alameda Research, IOSG, AngelDAO, Bo Shen, Meltem Demirors, 1kx, Lemniscap, Greenfield Capital, Tomahawk VC.

---

## 5. Mechanism Design Assessment

### V1 → V2 Evolution

| Feature | V1 | V2 |
|---------|----|----|
| Stablecoin | LUSD | BOLD |
| Collateral | ETH only | ETH, wstETH, rETH |
| Interest | One-time fee (0.5-5%) | User-set ongoing rate (0.5-1000%) |
| Troves per address | 1 | Multiple (ERC-721 NFTs) |
| Recovery Mode | Yes (150% TCR) | Removed |
| Liquidation penalty | 10% | 5% |
| SP yield source | LQTY emissions + liquidation gains | 75% borrower interest + liquidation gains |
| Oracle | Tellor (decentralized) | Chainlink (centralized multisig) |
| License | Open source | BUSL (until Sept 2027) |

**V2's user-set interest rates** are genuinely innovative — borrowers choose their rate, and redemptions target the lowest-rate Troves first. This solves V1's premium problem and creates sustainable SP yield. But the mechanism is novel and untested at scale — game-theoretic edge cases may emerge.

### Known Weaknesses

1. **LUSD premium problem (V1)** — LUSD consistently traded above $1 because demand for censorship-resistant stablecoins outstripped supply. A dollar that costs $1.03 is not a dollar.
2. **Redemption death spiral (V1)** — Borrowers fled because even heavily over-collateralized Troves got redeemed, destroying capital efficiency.
3. **Immutability = unfixability** — When V2 had a bug, the team couldn't pause or patch. Users had to be warned to withdraw manually.
4. **Oracle centralization (V2)** — Moving from Tellor to Chainlink weakens decentralization thesis.
5. **BUSL licensing (V2)** — Liquity AG decides who can deploy the code. Antithetical to permissionless ethos.

### Fork Landscape

~45 V1 forks launched. Near-universal failure:
- **Prisma Finance:** Exploited for $11.6M (March 2024), now decommissioning. $287K TVL from $400M+ peak.
- **Gravita Protocol:** Effectively dead. $454K TVL.
- **Nerite:** Active V2 fork on Arbitrum. $177M+ TVL. Licensed under V2 friendly fork program.

Fork failures stem from custom code modifications, not Liquity's base code. Liquity's core code has never been exploited.

### Competitive Positioning

| Protocol | Stablecoin Supply | Governance | Immutable | RWA Exposure |
|----------|-------------------|------------|-----------|--------------|
| MakerDAO | $4.6B | Full DAO | No | Heavy |
| Aave GHO | $527M | Full DAO | No | Some |
| crvUSD | $279M | Token voting | No | None |
| **Liquity** | **$61M** | **None** | **Yes** | **None** |

Liquity occupies a unique niche: maximum decentralization with reasonable capital efficiency. It will never compete with Maker on scale. Its value proposition is being the protocol you use when you genuinely need censorship resistance and trustlessness.

---

## 6. Red Flags Register

| # | Severity | Finding | Evidence |
|---|----------|---------|----------|
| 1 | **HIGH** | V2 Stability Pool bug required full redeployment — multiple auditors missed it | The Defiant, The Block coverage; Liquity blog |
| 2 | **HIGH** | LQTY -99.4% from ATH ($63 → $0.35) | CoinGecko |
| 3 | **HIGH** | V1 LUSD supply collapsed from $1.5B+ to $31M — terminal decline | DeFiLlama |
| 4 | **HIGH** | BUSL licensing contradicts decentralization claims (AG controls deployment until 2027) | Liquity blog, V2 license |
| 5 | **MEDIUM** | 57.6% insider token allocation (33.9% investors + 23.7% team) | Tokenomist |
| 6 | **MEDIUM** | Oracle downgrade from Tellor (decentralized) to Chainlink (centralized multisig) | Liquity blog |
| 7 | **MEDIUM** | $1.36M treasury — extremely thin for $248M TVL protocol | DeFiLlama |
| 8 | **MEDIUM** | Alameda Research as Series A investor — forced liquidation sell pressure | DeFiLlama raises |
| 9 | **MEDIUM** | V2 TVL declining 50% from peak in 4 months | DeFiLlama |
| 10 | **LOW** | Chicken Bonds dead ($1.49M TVL) — failed product | DeFiLlama |
| 11 | **LOW** | $300K bug bounty vs $90M TVL (0.33%) — underfunded | DeFiSafety |
| 12 | **LOW** | Robert Lauko board removal (Feb 2023) unexplained | Swiss commercial register |
| 13 | **LOW** | Rick Pardoe education claims unverifiable | No university named in any source |

---

## 7. Unresolved Questions

1. **What exactly was the V2 Stability Pool bug?** Technical details were never publicly disclosed. While defensible to protect forks, this prevents independent verification.
2. **How will BOLD perform in a severe ETH crash?** V2 has not been stress-tested through a major downturn.
3. **Will user-set interest rates converge to efficient equilibrium or degenerate under MEV/bot pressure?** Novel mechanism, untested at scale.
4. **What is Liquity AG's development runway?** $1.36M treasury is thin.
5. **What happened to Alameda's LQTY holdings?** Bankruptcy estate disposition unclear.
6. **Why is V2 TVL declining 50% from peak?** Could be market dynamics or product-market fit issues.
7. **What happens to the fork program after BUSL expires in September 2027?** Unlicensed forks become legal.
8. **Coinspect BOLD-05 finding:** Single oracle failure can halt redemptions across ALL branches. Has this been addressed?

---

## 8. Final Verdict

**CAUTIOUSLY POSITIVE.** Liquity stands out as one of the few DeFi protocols where the engineering is genuine, the yield is real, the team is verifiable, and the decentralization is not marketing theater. Zero exploits in 5 years of immutable operation is an achievement almost no other protocol can claim.

The cautionary notes are real: the V2 redeployment is a serious mark against the immutability thesis, the BUSL licensing creates centralization tension, LQTY tokenomics have been value-destructive, and BOLD at $30M supply is still a rounding error in the stablecoin market.

**For users who prioritize decentralization and censorship resistance above all else, Liquity V2 is arguably the best option available — with the caveat that "best available" still comes with material risks from immutability, oracle dependency, and mechanism novelty.**

**This is not a rug pull. This is not a Ponzi. This is a real protocol built by real engineers solving a real problem — with real limitations and real risks that should be understood before depositing capital.**

---

*Report compiled from 4 parallel research agents (300+ tool calls). Supporting detail in `reports/liquity-team-assessment.md` and `reports/liquity-third-party-intel.md`.*

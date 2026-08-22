# PPC 2-Day Report — 18–19 Aug 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, USD)
**Data window:** 18 Aug 2026 – 19 Aug 2026 (2 full days)
**Run date:** 22 Aug 2026 (data ends 48h before run, as Amazon PPC data takes ~48h to finalise)
**Product type:** Sponsored Products

> **Delivery note:** This report was saved to the repo and uploaded to the Google
> Drive "PPC Reports" folder successfully. **The email step could not run** — the
> Gmail connector is not enabled for this automated session (`enabledInChat:
> false`), so no email was sent. To fix: enable the Gmail connector for this
> chat/automation in Settings → Connectors. Until then, retrieve reports from
> Google Drive or the repo.

> **Note on setup:** The `AMZ_PROFILE_ID` provided is an *application ID*, not a
> usable advertising profile. I looked up the account's real profiles and used
> the US seller profile (the only one with live campaigns and budget). No numbers
> were invented — all figures below are pulled directly from the Amazon Ads API.
> I've recorded the fix in my notes so future runs handle it automatically.

---

## Part A — Data Table (by campaign)

Only campaigns that received impressions in the window are shown individually.
The other 43 Sponsored Products campaigns were paused/archived or received zero
impressions, so they contributed nothing to spend or sales. The **Totals** row
covers the entire account.

| Campaign | Impressions | Top-of-Search IS | Clicks | CTR | Purchases | Sales | Total Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 75 | 1% | 4 | 5.33% | 0 | $0.00 | $1.17 | $0.29 | n/a | 0.00 |
| SP PT Pet Odor Eliminator (B0FXW3GW5F) | 14 | 4% | 0 | 0.00% | 0 | $0.00 | $0.00 | — | n/a | n/a |
| SP Isolated Pet Odor Eliminator Phrase (B0FXW3GW5F) | 13 | 14% | 0 | 0.00% | 0 | $0.00 | $0.00 | — | n/a | n/a |
| SP KT \| ST w/ Sales | 3 | 0% | 0 | 0.00% | 0 | $0.00 | $0.00 | — | n/a | n/a |
| SP Home + Eliminator + Brand Root 10-25k SV Exact | 1 | 0% | 0 | 0.00% | 0 | $0.00 | $0.00 | — | n/a | n/a |
| **TOTALS (all campaigns)** | **106** | **~1%** | **4** | **3.77%** | **0** | **$0.00** | **$1.17** | **$0.29** | **n/a** | **0.00** |

*ACOS and ROAS are undefined because there were no sales. Top-of-Search IS for
the totals row is impression-weighted and approximate.*

---

## Part B — Plain-English Summary

**The short version:** Over these two days the account barely spent anything and
made no sales. Total ad spend was **$1.17**, from **106 impressions** and just
**4 clicks**. There were **0 orders** and **$0 in sales**, so ACOS and ROAS
can't be calculated (you need at least one sale for those).

**Why so quiet:** Almost the entire account is switched off. Of 54 Sponsored
Products campaigns, most are paused or archived, and the few that are live have
very small daily budgets ($1.50). Only one campaign actually spent money in this
window. So this isn't a data problem — the ads simply aren't running at any real
scale right now.

**Best campaign:** *SP | Cat Tunnel Bed Pink Only | Exact Ranking* — the only
campaign that got clicks. Its click-through rate (5.33%) is healthy, meaning the
ad is appealing to shoppers; it just hasn't converted to a sale yet on such tiny
volume.

**Worst / wasted spend:** Nothing egregious this window — total spend is only
$1.17, so there's no meaningful waste to cut. The one spend ($1.17 on the Cat
Tunnel Bed campaign) produced 4 clicks and no sale, which is far too little data
to judge a search term as "wasteful." Nothing warrants a negative keyword yet.

**Search terms worth adding as exact-match:** None yet. The only search terms
that drew clicks were "cat tunnel bed" (3 clicks) and "cat tunnel bed for indoor
cats" (1 click), both with **zero sales**. Do **not** promote these to exact
match until at least one converts — right now they'd just be spending without
proof they sell.

**What to do next:**
1. **Decide whether the account should even be active.** Spend this low means the
   ads aren't doing anything for the business. If you want PPC to matter, the live
   campaigns need real daily budgets and bids that actually win impressions.
2. **Raise budgets/bids on your winners.** The Cat Tunnel Bed and Pet Odor
   Eliminator campaigns are the only ones getting seen. If those products are
   priorities, lift their bids so they gather enough clicks to learn from.
3. **Give it time before cutting anything.** 4 clicks over 2 days is not enough
   to declare any keyword good or bad. Let volume build before adding negatives
   or new exact-match keywords.

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists — this is the first run, so it serves as the
baseline.** From the next run onward, this section will show the change in each
headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both a number
and a percentage, with a one-line verdict on whether things improved or worsened.

**Baseline figures to compare against next time:**

| Metric | This report (18–19 Aug) |
|---|---:|
| Impressions | 106 |
| Clicks | 4 |
| CTR | 3.77% |
| Total cost | $1.17 |
| CPC | $0.29 |
| Purchases | 0 |
| Sales | $0.00 |
| ACOS | n/a (no sales) |
| ROAS | 0.00 |

---
*Generated automatically by the PPC Analyst routine. Figures pulled live from the
Amazon Advertising API (Sponsored Products, US profile).*

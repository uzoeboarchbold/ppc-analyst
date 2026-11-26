# PPC 2-Day Report — November 22–23, 2026

**Report type:** 2-day | **Window covered:** Sun 22 Nov – Mon 23 Nov 2026 (UTC)
**Generated:** 26 Nov 2026 | **Account:** Amazon US (Sponsored Products) | **Currency:** USD
**Data source:** Amazon Advertising API (live pull). Amazon finalises data ~48h late, so this window ends 48h before the run.

---

## ⚠️ Read first — two things you need to know

**1. Your ads are not running.** Across the 2-day window — and across the entire last 30 days — your Sponsored Products campaigns served **0 impressions, 0 clicks, $0.00 spend and $0.00 ad sales**. You have **15 "enabled" campaigns** that should be showing, but none of them appeared in a single search. There is nothing to optimise yet because nothing is being spent; the real problem is that the ads aren't delivering at all. See "What to do next" for the likely causes.

**2. A credential was set up wrong (I worked around it).** The `AMZ_PROFILE_ID` value in the environment is not a valid Amazon Ads profile ID — it holds an application-ID string (`amzn1.application.…`) instead of the numeric profile number. I connected successfully, listed your real accounts, and found the only one with campaigns is your **US Seller account (profile `26765323558215`)**, so I reported on that. Your Canada and Mexico accounts exist but have no campaigns. **Please update `AMZ_PROFILE_ID` to `26765323558215`** so future runs don't have to guess.

---

## Part A — Data table

**Account totals, 22–23 Nov 2026**

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **TOTAL (all campaigns)** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

No campaign served any impressions in the window, so Amazon returned no per-campaign rows for these two days. For transparency, below are the **15 enabled campaigns** that were eligible to serve but delivered nothing (verified over both the 2-day window and the trailing 30 days). The other 39 campaigns are **paused (32)** or **archived (7)** and are not expected to run.

| Enabled campaign | Impr. | Clicks | Spend | Sales | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|
| SP Isolated … Cat Deterrent Spray Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated … Pet Odor Eliminator Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated … Cat Deterrent Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated … Cat Deterrent Phrase | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Odor Root 50k+ SV … Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Odor Root 25-50k SV … Phrase | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Odor Root 25-50k SV … Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Cat Root 1-10k SV … Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP Auto … (B0FXW3GW5F) | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP KT \| ST w/ Sales | 0 | 0 | $0.00 | $0.00 | n/a | n/a |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | 0 | $0.00 | $0.00 | n/a | n/a |

*Daily budgets on these campaigns are $1.50/day. Products advertised: Cat Deterrent Spray / Pet Odor Eliminator (ASIN B0FXW3GW5F) and Cat Tunnel Bed / Cat Cave lines.*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00. **Overall ad sales:** $0.00. **ACOS / ROAS:** not applicable — you can't have a cost-of-sales ratio when there's no cost and no sales.
- **Best campaign / worst campaign:** none to name — every campaign performed identically at zero because none served.
- **Wasted spend:** none. You are not wasting money; the opposite problem — the ads aren't spending at all, so they can't be winning you sales.
- **Search terms to add as exact-match:** none available — with zero clicks there are no search terms to harvest yet.
- **Bottom line:** This is a "delivery" problem, not a "performance" problem. Until impressions start, there's no keyword, bid or negative-keyword tuning to do.

### What to do next (in priority order)
1. **Check the product listing is eligible to advertise.** Sponsored Products only run when the ASIN holds the Featured Offer (Buy Box) and is in stock. If B0FXW3GW5F (and the Cat Tunnel Bed ASINs) are out of stock, suppressed, or losing the Buy Box, every ad silently stops. This is the single most common cause of 0 impressions.
2. **Check billing / account status.** An expired card or a payment hold will pause all delivery account-wide even while campaigns show "enabled."
3. **Check bids vs. budget.** $1.50/day with low default bids can struggle to win auctions, but it should still produce *some* impressions over 30 days — 0 across the board points to #1 or #2 rather than bids alone.
4. **Spot-check one campaign in Campaign Manager.** Confirm the ad group, the ad (product), and the targets are all enabled — a campaign can be "enabled" while its ad group or ad is paused.
5. **Fix `AMZ_PROFILE_ID`** to `26765323558215` so this report locks onto the right account automatically.

Once impressions are flowing, the next reports will start delivering real optimisation (wasted-spend negatives, winning search terms to promote, ACOS/ROAS trends).

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run of this report type, so there is nothing to compare against yet.** This report establishes the baseline.

| Metric | This report | Previous | Change |
|---|---:|---:|---:|
| Impressions | 0 | — | — |
| Clicks | 0 | — | — |
| Spend | $0.00 | — | — |
| Sales | $0.00 | — | — |
| ACOS | n/a | — | — |
| ROAS | n/a | — | — |

**Improved or worsened?** Baseline only. From the next run onward, each headline metric will be shown as an absolute change and a percentage versus the prior 2-day report.

---

*Prepared automatically by the PPC Analyst routine. Figures are pulled live from the Amazon Advertising API; where a value is "n/a" it is genuinely undefined (no delivery), not estimated. No numbers were invented.*

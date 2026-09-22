# PPC 2-Day Report — 18–19 September 2026

**Report type:** 2-day | **Days covered:** Fri 2026-09-18 and Sat 2026-09-19 (US marketplace, USD)
**Generated:** 2026-09-22 23:13 UTC (data ends 48h before run, so these are the latest fully-finalised days)
**Account:** Uzoebo Archbold E-Commerce — US (Amazon.com), profile 26765323558215 | **Ad product:** Sponsored Products | **Attribution:** 14-day

---

## ⚠️ Read this first — your ads did not run

Every one of your 15 Sponsored Products campaigns is switched **ENABLED**, but they served **nothing** on both days in this window: **0 impressions, 0 clicks, $0.00 spend, 0 sales.** This is not a data glitch — I checked back further and delivery has been flat at zero **every day since at least 5 September** (14+ days straight).

**Almost certainly why:** the US advertising account shows **no valid payment method on file** (`validPaymentMethod: false`). Amazon stops serving ads when it can't bill them, even while the campaigns look "active." 

**What to do today:** log in to Amazon Seller Central → **Advertising → Billing / Payment settings** and add or update a valid card. Once billing is fixed, delivery normally resumes within a few hours. Until that's done, no amount of bid or keyword tuning will help — the ads simply aren't eligible to show.

*(Two config notes for whoever maintains this bot: the `AMZ_PROFILE_ID` environment variable is set to an `amzn1.application…` LWA app ID instead of the numeric profile ID — I worked around it by looking the account up and using the US profile `26765323558215`. Also, the CA and MX profiles on this account have no Sponsored Products campaigns.)*

---

## Part A — Data table (per campaign)

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Cat Root 1-10k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Odor Root 50k+ SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| **TOTAL (15 campaigns)** | **0** | **—** | **0** | **0.0%** | **0** | **$0.00** | **$0.00** | **$0.00** | **—** | **—** |

*All metrics are genuinely zero for 18–19 Sep because the ads did not deliver. ToS Impr. Share, ACOS and ROAS are "—" because they can't be calculated with no impressions/sales.*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00. **Overall sales (from ads):** $0.00. **ACOS / ROAS:** not applicable — nothing was spent and nothing was sold through ads.
- **Best / worst campaign:** none to pick — all 15 campaigns performed identically at zero because none of them ran.
- **Wasted spend / negatives to add:** none — you can't waste spend when nothing is spending. (No search-term data exists either: with zero clicks there are no search terms to harvest or block yet.)
- **Well-converting search terms to add as exact-match:** none available this period — there were no clicks or conversions to learn from.
- **The one thing that matters:** the account is not delivering ads at all, and the likely reason is the invalid payment method. Everything else is on hold until that's fixed.

### What to do next
1. **Fix billing now** — add/update a valid payment method on the US advertising account (Seller Central → Advertising → Billing). This is the single blocker.
2. **Confirm delivery resumed** — after ~24h, check that impressions and spend are climbing again.
3. **Then re-baseline** — once ads are live for a couple of days, the next reports will finally have real numbers, and I can start recommending negatives, exact-match additions and bid changes.
4. **Sanity-check budgets** — the US account's daily budget was set very low ($40 total); make sure per-campaign budgets are where you want them once spend restarts.

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists** — this is the first automated 2-day report, so there is nothing to compare against yet. From the next run onward this section will show the change in each headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both a number and a percentage, up or down.

| Metric | This report (18–19 Sep) | Previous | Change |
|---|--:|--:|--:|
| Impressions | 0 | n/a | — |
| Clicks | 0 | n/a | — |
| Spend | $0.00 | n/a | — |
| Sales | $0.00 | n/a | — |
| ACOS | n/a | n/a | — |
| ROAS | n/a | n/a | — |

**Verdict:** Baseline run. The headline for now is operational, not performance: **ads are not running because billing is invalid — fix that first.**

---
*Data source: Amazon Advertising API v3 (Sponsored Products, spCampaigns report, US profile 26765323558215). Figures are final for the dates shown.*

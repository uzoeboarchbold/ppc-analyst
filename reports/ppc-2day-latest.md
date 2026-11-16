# PPC 2-Day Report — 12–13 November 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon US (Sponsored Products)
**Reporting window:** Sat 12 Nov 2026 – Sun 13 Nov 2026 (2 full days)
**Generated:** Mon 16 Nov 2026 23:09 UTC (data ends 48h before run, as Amazon finalises ~48h late)
**Attribution:** 14-day click attribution (Amazon SP default)

---

## ⚠️ Headline: the ads are not running

**Every enabled campaign served ZERO impressions, zero clicks and zero spend for 12–13 November.** There were no sales from ads because no ads were shown. I verified this is real — not a data glitch — by also pulling the whole of the last 30 days (15 Oct – 13 Nov): still **zero impressions and zero spend across the account.**

The campaigns are not new and not paused by mistake — 15 are ENABLED with daily budgets ($1.50–$2.50) and have been live for months (most since May 2026, one since Dec 2025). They simply are not being allowed to deliver.

**Most likely cause:** the US advertising account shows **no valid payment method** (`validPaymentMethod: false`). When Amazon can't bill a seller, it suspends all ad delivery while the campaigns still look "active". This single issue would explain the total blackout.

**What to check first (in order):**
1. **Billing** — Seller Central → Settings → Account Info / Advertising billing. Add or update a valid payment method/credit card. This is the #1 suspect.
2. **Listing health for ASIN B0FXW3GW5F** (the main advertised product — a cat deterrent / pet-odour spray). If the listing is suppressed, out of stock, or lost the Buy Box, ads also stop serving. Confirm it's active, in stock and winning the Buy Box.
3. **Account status** — check for any Amazon policy/account-health or ad-account suspension notices.

Until delivery is restored, bids, negatives and keyword tweaks make no difference — fixing delivery is the only thing that matters this week.

---

## Part A — Data Table (per campaign)

All 15 enabled campaigns, 12–13 Nov 2026. CTR, CPC, ACOS and ROAS are "—" because there were no clicks or spend to calculate them from.

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(32 further campaigns are PAUSED and 7 ARCHIVED; none served either.)*

---

## Part B — Plain-English Summary

- **Overall spend:** $0.00. **Overall sales (from ads):** $0.00. **ACOS / ROAS:** not applicable — nothing was spent or sold through ads.
- **Best / worst campaign:** not meaningful this period — all campaigns performed identically at zero because none were allowed to run.
- **Wasted spend / negatives to add:** none — you can't waste spend you didn't spend. (No search-term data exists for this window, so there are no negatives to suggest.)
- **Search terms to add as exact-match:** none available — with no clicks, there are no converting search terms to harvest yet.
- **What to do next:** This is a delivery problem, not an optimisation problem. Fix it in this order:
  1. Add/repair the **payment method** on the US ad account (most likely blocker).
  2. Confirm **ASIN B0FXW3GW5F** is live, in stock and holds the Buy Box.
  3. Clear any **account-health/policy** flags.
  Once impressions start flowing again, the next 2-day report will show real numbers and I can begin the usual bid, negative and keyword work.

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists — this is the first run, so it sets the baseline.** There is nothing to compare against yet. From the next run onward this section will show the change in impressions, clicks, spend, sales, ACOS and ROAS as both a number and a percentage.

For reference, the baseline captured here is: **Impressions 0 · Clicks 0 · Spend $0.00 · Sales $0.00 · ACOS n/a · ROAS n/a.** The goal for the next report is simply: **get these above zero** by restoring ad delivery.

---

### Technical notes (for the record)
- The `AMZ_PROFILE_ID` environment variable was misconfigured (it held an application-ID value, `amzn1.application…`, not a profile ID). I resolved the correct US seller profile (`26765323558215`, USD) automatically from the Ads API and used it. The CA and MX profiles hold no campaigns. **Action for owner:** set `AMZ_PROFILE_ID=26765323558215` so future runs don't depend on auto-detection.
- Data pulled live from the Amazon Ads API v3 (Sponsored Products). Campaign report completed successfully; targeting and search-term reports returned 0 rows, consistent with zero delivery.

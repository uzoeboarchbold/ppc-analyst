# PPC 2-Day Report — 9–10 November 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Amazon.com)
**Product line:** Sponsored Products (Cat Deterrent Spray / Pet Odor Eliminator, ASIN B0FXW3GW5F, + Cat Tunnel Bed)
**Date window covered:** Monday 9 Nov – Tuesday 10 Nov 2026 (2 full days, ending 48h before the run to respect Amazon's data lag)
**Report generated:** 13 Nov 2026 (automated) · Currency: USD

---

## ⚠️ Read this first (2 issues found)

1. **Your ads are not running.** Every Sponsored Products campaign recorded **zero impressions, zero clicks, zero spend and zero sales** for 9–10 Nov. A 21-day check (20 Oct – 10 Nov) shows the same thing every single day — the account has been dark for at least three weeks. The most likely cause: **the US advertising account has no valid payment method on file** (Amazon reports `validPaymentMethod = false`), which stops Amazon from serving your ads. Campaigns being paused or out of budget would do the same. **This is the one thing to fix — nothing else matters until ads are live again.**

2. **Two automation settings need fixing (did not stop this report, but should be corrected):**
   - The `AMZ_PROFILE_ID` setting is invalid (it isn't a real Amazon profile ID). I worked around it by looking up your profiles and using the correct **US** account automatically. Please set `AMZ_PROFILE_ID = 26765323558215`.
   - **The email step could not run.** The Gmail connector isn't switched on for this automated session, so I couldn't auto-email the report. It has still been saved to the repo and uploaded to the "PPC Reports" Google Drive folder. Turn on the Gmail connector for this automation to get future reports by email.

---

## Part A — Data table (per campaign)

All figures are for 9–10 Nov 2026 combined.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto — B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1–10k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10–25k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10–25k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*"—" = cannot be calculated because there were no impressions/clicks/spend. "IS" = impression share. "SV" = search volume.*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales (from ads):** $0.00. **ACOS / ROAS:** not applicable — there was no ad activity to measure.
- **Best / worst campaign:** none to pick — all 15 campaigns were inactive.
- **Wasted spend / negatives to add:** none, because nothing was spent. (The flip side: you also captured none of the sales these ads would normally drive.)
- **Well-converting search terms to add as exact-match:** none available — with no clicks, there is no search-term data to mine this period.
- **What's actually going on:** This isn't a "bad performance" period — it's a "not running at all" period, and it has lasted at least three weeks. The strongest signal is that the US ad account shows **no valid payment method**. Amazon stops delivering ads when billing fails, which fits the data perfectly (a clean zero across every campaign, including the always-on Auto campaign).

### What to do next (in order)
1. **Fix billing first.** Log in to Amazon Ads (or Seller Central → advertising) for the US marketplace and add/update a valid payment method. This is almost certainly why ads stopped.
2. **Confirm campaigns are enabled and funded** — check that campaigns aren't paused and that the $40/day budget (and campaign budgets) are set. Re-enable anything paused.
3. **Re-run this report in ~3 days** once ads are live, so we can see real impressions, spend and sales and start optimising.
4. **Fix the two automation settings** (set `AMZ_PROFILE_ID = 26765323558215`; enable the Gmail connector for emailed reports).

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists — this is the first run**, so there is no prior report to compare against. Headline metrics are all $0 / 0 this period; the next run will show period-over-period change (number and %) for Impressions, Clicks, Spend, Sales, ACOS and ROAS.

| Metric | This report (9–10 Nov) | Previous report | Change |
|---|--:|--:|--:|
| Impressions | 0 | — (no prior report) | n/a |
| Clicks | 0 | — | n/a |
| Spend | $0.00 | — | n/a |
| Sales | $0.00 | — | n/a |
| ACOS | n/a | — | n/a |
| ROAS | n/a | — | n/a |

**Verdict:** Baseline established. Things can only be assessed as improved/worsened once ads are running and a second report exists.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting), US profile 26765323558215. Figures finalised with Amazon's ~48h reporting lag. Sales/purchases use the 7-day attribution window.*

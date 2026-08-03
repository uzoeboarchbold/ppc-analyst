# PPC 2-Day Report — 30 Jul 2026 to 31 Jul 2026

**Account:** Uzoebo Archbold E-Commerce (Amazon.com / US, USD)  
**Ad product:** Sponsored Products  
**Report generated:** 2026-08-03 (data window ends 48h before run to allow Amazon's data to finalise)  
**Attribution:** 7-day (purchases/sales counted within 7 days of click)

> **Data note:** The `AMZ_PROFILE_ID` environment variable held an application ID (`amzn1.application...`), not a numeric advertising profile ID, so the API rejected it. I looked up the account's real profiles via the Ads API and used the active US profile (`26765323558215`). ACOS and ROAS are calculated from cost and sales (the API does not return them as summary columns). See notes-to-self.md.

## Part A — Data Table (by campaign)

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 15 | 0.11% | 1 | 6.67% | 0 | $0.00 | $0.98 | $0.98 | n/a | 0.00 |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 13 | 0.00% | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP PT Pet Odor Eliminator 6K-PZMX-MTDZ B0FXW3GW5F | 12 | 0.01% | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 6 | 0.00% | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 2 | 0.00% | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 1 | 0.00% | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 1 | 0.00% | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | - | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | - | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP KT \| ST w/ Sales | 0 | - | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| SP PT \| ST w/ Sales | 0 | - | 0 | 0.00% | 0 | $0.00 | $0.00 | $0.00 | n/a | - |
| **TOTAL (11 campaigns)** | **50** | — | **1** | **2.00%** | **0** | **$0.00** | **$0.98** | **$0.98** | **n/a** | **0.00** |

*Top-of-search IS = share of top-of-search impressions won. ACOS = ad cost ÷ sales. ROAS = sales ÷ ad cost. "n/a" ACOS means there were no sales to divide by.*

## Part B — Summary (plain English)

- **Overall spend:** $0.98 across all campaigns over the 2 days.
- **Overall sales:** $0.00 — **zero sales** in this window.
- **ACOS:** n/a (can't be calculated with no sales). **ROAS:** 0.00 (no return, because no sales).
- **Traffic:** 50 impressions, 1 click, 2.00% CTR.

**The headline:** the account is barely advertising right now. With a US budget of about $40/day available, only **$0.98 was spent over two whole days** and it produced a single click and no orders. Almost every campaign got little or no impressions, and top-of-search impression share is near 0% everywhere — meaning the ads are essentially not showing.

- **Best campaign:** None stood out — no campaign made a sale. The only one that even drew a click was *SP Isolated … Pet Odor Eliminator Phrase*.
- **Worst campaign:** *SP Isolated … Pet Odor Eliminator Phrase* is the only one that spent money ($0.98) and returned nothing, so on a pure cost-for-nothing basis it's the weakest — but the amount is tiny.
- **Wasted spend / suggested negatives:** Only one search term drew spend: **"pet odor eliminator spray"** (phrase match, 1 click, $0.98, 0 sales). One click is far too little evidence to call it wasteful yet — do **not** add it as a negative on a single no-sale click. Watch it; only negate if it keeps spending with no conversions.
- **Search terms to add as exact-match:** None. No search term converted in this window, so there is nothing proven worth promoting to exact-match yet.

### What to do next
1. **Check why ads aren't serving.** Spending $0.98 of a ~$40/day budget with ~0% top-of-search share usually means bids are too low, campaigns are paused/out of budget by schedule, or products are out of stock / not in the Buy Box. Verify campaign status and stock first.
2. **Raise bids on the core phrase campaigns** (Pet Odor Eliminator, Cat Deterrent) so the ads actually appear — you can't get sales from ads that don't show.
3. **Give it more data before optimising.** With 1 click in 2 days there is nothing statistically meaningful to cut or scale. The priority is getting impressions flowing again.
4. **Re-check the profile ID configuration** so future runs don't have to auto-resolve it.

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists** — this is the first 2-day report in the repo, so there is no prior period to compare against. Headline metrics for this run, which will become the baseline for next time:

| Metric | This period (30–31 Jul) |
|---|--:|
| Impressions | 50 |
| Clicks | 1 |
| CTR | 2.00% |
| Spend | $0.98 |
| Sales | $0.00 |
| Purchases | 0 |
| ACOS | n/a |
| ROAS | 0.00 |

*Next 2-day report will show the change in each of these as a number and a percentage.*

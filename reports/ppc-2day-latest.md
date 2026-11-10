# PPC 2-Day Report — Nov 6–7, 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Window covered:** 2026-11-06 to 2026-11-07 (2 full days, ending 48h before the run)
**Generated:** 2026-11-10 (automated)
**Currency:** USD

---

## ⚠️ Please read first — two issues this run found

1. **Your campaigns are not running — zero spend, zero sales.** Every enabled
   campaign served **0 impressions and 0 clicks** across both days. This is **not**
   a reporting error: I checked the whole of the last ~24 days (Oct 15–Nov 7) and
   the account spent **$0.00** every single day. The likely cause is that the US
   advertising account has **no valid payment method on file**
   (`validPaymentMethod = false`). Amazon pauses ad delivery when billing isn't set
   up, so your ENABLED campaigns simply don't show. **Action: add/fix the payment
   method in Amazon Ads billing to turn the ads back on.**

2. **The configured profile ID was wrong.** The `AMZ_PROFILE_ID` setting contained
   an invalid 50-character value that matched none of your real ad profiles. I
   automatically identified and used your **US** profile (`26765323558215`) — the
   only marketplace with active campaigns. Please update `AMZ_PROFILE_ID` to
   `26765323558215` so future runs are unambiguous.

Because true spend and sales were zero, the tables and summary below correctly
show zeros. No numbers have been invented.

---

## Part A — Data table (by campaign)

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **TOTAL (15 enabled campaigns)** | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |

All 15 enabled campaigns individually recorded **0** on every metric for the
window, so per-campaign rows are omitted (each would be a row of zeros). The
enabled campaigns that *should* be serving are:

- SP Auto 6K-PZMX-MTDZ B0FXW3GW5F
- SP Cat Root 1-10k SV … Exact
- SP Home + Eliminator + Brand Root 10-25k SV … Exact
- SP Isolated … Cat Deterrent Exact / Phrase
- SP Isolated … Cat Deterrent Spray Exact / Phrase
- SP Isolated … Pet Odor Eliminator Exact / Phrase
- SP KT | ST w/ Sales
- SP Litter + Urine Root 10-25k SV … Exact
- SP Odor Root 25-50k SV … Exact / Phrase
- SP Odor Root 50k+ SV … Exact
- SP | Cat Tunnel Bed Pink Only | Exact Ranking | Louise

(32 further campaigns are PAUSED and 7 ARCHIVED.)

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS/ROAS:** not
  applicable — nothing was spent and nothing was sold through ads.
- **Best / worst campaign:** none to rank — no campaign delivered any traffic.
- **Wasted spend:** none (good news only in the narrow sense that you can't waste
  money on ads that aren't running). The real problem is the opposite: your ads
  are **invisible to shoppers**, so you're likely losing sales and organic rank to
  competitors every day they stay off.
- **Search terms to add as exact-match:** none available — with no clicks there is
  no search-term data to mine this period.
- **What to do next:**
  1. **Fix billing first.** Go to Amazon Ads → Billing and add/update a valid
     payment method. This is almost certainly why everything is at zero.
  2. Once ads are live again, confirm within 24–48h that impressions and clicks
     are flowing, then let the normal 2-day reports resume tracking performance.
  3. Update the `AMZ_PROFILE_ID` setting to `26765323558215`.
  4. Re-check that your 15 "enabled" campaigns still have sensible budgets
     (currently $1.50–$2.50/day each) once they're serving again.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first one, so it serves as the
**baseline** for future comparisons. Headline figures to compare against next time:

| Metric | This report (Nov 6–7) |
|---|--:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| Purchases | 0 |
| ACOS | n/a |
| ROAS | n/a |

Direction vs. prior: not applicable yet. The single most important change to watch
for next run is whether spend and impressions move **above zero** — that will
confirm the billing fix worked.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting), pulled
live for the stated window. Automated PPC Analyst run.*

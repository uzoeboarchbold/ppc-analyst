# PPC 2-Day Report — 5–6 October 2026

**Reporting window:** 5 October 2026 – 6 October 2026 (2 full days)
**Account:** Amazon US seller profile (`26765323558215`)
**Ad type:** Sponsored Products
**Generated:** 9 October 2026 (data ends 48h before run, per Amazon's reporting lag)

---

## ⚠️ Read this first — plain English

Two things you need to know:

1. **There was no ad activity at all in this window.** You have **15 live
   (enabled) Sponsored Products campaigns**, but every one of them got **zero
   impressions, zero clicks, zero spend and zero sales** on 5–6 October. I
   checked the last 30 days as well (7 Sep – 6 Oct) and it is the same story:
   **zero impressions across the whole period.** So this is not a one-off quiet
   couple of days — your ads simply are not being shown to anyone.

2. **A settings fix is needed.** The `AMZ_PROFILE_ID` credential this report is
   supposed to use is misconfigured (it contains an `amzn.application...` value,
   not a numeric Advertising profile ID). I worked around it by auto-detecting
   your live account — your **US seller account** is the only one of the three
   (US / CA / MX) with any campaigns, so that is what this report covers. A
   human should correct that environment variable so future runs don't rely on
   auto-detection. (Details in `notes-to-self.md`.)

**The numbers below are real figures pulled from the Amazon Ads API — they are
genuinely all zero. Nothing has been invented or estimated.**

---

## Part A — Data table (per campaign)

All 15 **enabled** campaigns, 5–6 Oct 2026. (32 paused and 7 archived campaigns
are excluded as inactive.)

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV …Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 enabled campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*"—" = not applicable. Top-of-search impression share, CTR, CPC, ACOS and ROAS
cannot be calculated when there are no impressions/clicks/spend.*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00
- **Overall sales (from ads):** $0.00
- **ACOS:** n/a (no spend) · **ROAS:** n/a (no sales)
- **Best campaign / worst campaign:** n/a — every campaign performed identically
  (nothing). There is no winner or loser to pick out because nothing ran.
- **Wasted spend to add as negatives:** none — you can't waste money you didn't
  spend. No negative-keyword suggestions this period.
- **Well-converting search terms to add as exact-match:** none — there were no
  clicks or search terms to harvest.

**Why are enabled campaigns showing zero?** When campaigns are switched ON but
still get *zero* impressions for weeks, it is almost always one of these:

1. **Bids too low to win any auction.** Your live campaigns run on very small
   daily budgets ($1.50, one at $2.50). If the keyword/target bids are also very
   low, your ads never clear the minimum needed to appear. This is the most
   likely cause given the tiny budgets.
2. **Product listing not eligible to advertise.** If the advertised products
   (mainly ASIN **B0FXW3GW5F** — Cat Deterrent Spray / Pet Odor Eliminator — and
   a Cat Tunnel Bed) are out of stock, have lost the Buy Box, or the listing is
   suppressed, Amazon won't serve the ads even though the campaign is "on."
3. **Very narrow targeting** that currently matches little or no search traffic.

### What to do next (priority order)
1. **Check product health first (5 min):** In Seller Central, confirm ASIN
   B0FXW3GW5F and the Cat Tunnel Bed are **in stock and hold the Buy Box**. If
   not, fix that — no bid change will help until the listing is eligible.
2. **Raise bids on 2–3 core campaigns** (e.g. the Auto campaign and the
   top Exact campaigns) to at least suggested-bid level, and **lift daily budgets
   from $1.50 to a level that can realistically win clicks** (e.g. $10–$15) so
   the campaigns can actually deliver and generate data.
3. **Re-check in 48 hours.** Once impressions start flowing, the next 2-day
   report will have real performance to analyse (ACOS, ROAS, wasted spend,
   search-term harvesting).
4. **Have someone fix the `AMZ_PROFILE_ID` setting** so reporting always points
   at the right account automatically.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first 2-day report in the
`reports/` folder, so there is no prior run to compare against. From the next
run onward, this section will show the change in each headline metric
(impressions, clicks, spend, sales, ACOS, ROAS) as both a number and a
percentage, with a one-line verdict on whether things improved or worsened.

| Metric | This report (5–6 Oct) | Previous report | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 0 | n/a | n/a | n/a |
| Clicks | 0 | n/a | n/a | n/a |
| Spend | $0.00 | n/a | n/a | n/a |
| Sales | $0.00 | n/a | n/a | n/a |
| ACOS | n/a | n/a | n/a | n/a |
| ROAS | n/a | n/a | n/a | n/a |

**Verdict:** Baseline established. The headline today is that live campaigns are
delivering nothing — fixing delivery (listing eligibility + bids/budgets) is the
single most important action before performance can be measured.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting).
Figures are actual API values for the stated window; none are estimated. Where
a metric is shown as "—" or "n/a" it is mathematically undefined because the
underlying counts are zero.*

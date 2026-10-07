# PPC 2-Day Report — Oct 3–4, 2026

**Marketplace:** Amazon US (Sponsored Products) · Seller: Uzoebo Archbold E-Commerce
**Dates covered:** 3–4 October 2026 (2 full days)
**Generated:** 7 October 2026 (data ends 48h before run, so Oct 3–4 is the latest finalised window)
**Report type:** 2-day · **Compared against:** previous 2-day report (none yet — this is the first run)

## ⚠️ Read this first
The data pulled cleanly from Amazon — nothing broke. The problem is what the
data shows: **your US Sponsored Products campaigns ran no ads at all.** Across
all 15 campaigns there were **zero impressions, zero clicks, zero spend and
zero sales** — not only on Oct 3–4, but across the whole of the last two weeks
I checked (Sep 24–Oct 5).

The most likely reason: **the US seller account has no valid payment method on
file** (Amazon reports `validPaymentMethod: false` for it). Amazon will not
serve ads without valid billing, so the campaigns sit idle even though they're
built. **Action needed: add/fix the payment method in Seller Central, then
confirm the campaigns are enabled.** Until that's done, future reports will
keep showing zeros.

(Separate technical note: the `AMZ_PROFILE_ID` setting points at an
application ID, not the numeric advertising profile. I worked around it by
looking up the correct US profile automatically. It's logged for a permanent
fix but did not affect these numbers.)

## Part A — Data table (per campaign)

All figures are for Oct 3–4, 2026. Every campaign returned zeros.

| # | Campaign | Impr. | TOS impr. share | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|----------|------:|----------------:|-------:|----:|----------:|------:|------:|----:|-----:|-----:|
| 1 | SP Isolated … Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 2 | SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 3 | SP Isolated … Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 4 | SP Odor Root 50k+ SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 5 | SP Odor Root 25-50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 6 | SP Isolated … Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 7 | SP Isolated … Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 8 | SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 9 | SP Cat Root 1-10k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 10 | SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 11 | SP Litter + Urine Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 12 | SP Odor Root 25-50k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 13 | SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 14 | SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 15 | SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| | **TOTAL (15 campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

"—" means the metric can't be calculated with zero activity (e.g. CTR, CPC,
ACOS, ROAS and top-of-search share all need impressions or clicks to exist).

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  applicable — nothing was spent, so there's no efficiency to measure.
- **Best / worst campaigns:** none stand out, because none ran. All 15 are
  equally idle.
- **Wasted spend / negatives to add:** none to suggest — there was no spend
  and no search-term traffic, so there are no money-wasting terms to block
  this period.
- **Well-converting search terms to add as exact-match:** none available —
  with zero clicks, Amazon returned no search-term data to mine.
- **What to do next (priority order):**
  1. **Fix billing first.** Open Seller Central → check/add a valid payment
     method for the US account. This is almost certainly why nothing is
     serving.
  2. **Then confirm campaign status.** Make sure the campaigns (and their ad
     groups/keywords) are set to *Enabled*, not paused, and that daily
     budgets are above $0. The US profile shows a $40 default daily budget,
     which is fine once billing is live.
  3. **Re-check in 48h.** Once ads start serving, the next 2-day report will
     show real impressions/clicks/spend, and I can start giving genuine
     optimisation advice (negatives, bids, winning search terms).

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** — this is the first run, so there's
nothing to compare against yet. All headline metrics (impressions, clicks,
spend, sales, ACOS, ROAS) start from this baseline of zero. From next run I'll
show the change in each metric as a number and a percentage.

| Metric | This report | Previous | Change |
|--------|------------:|---------:|-------:|
| Impressions | 0 | — | — (no prior report) |
| Clicks | 0 | — | — |
| Spend | $0.00 | — | — |
| Sales | $0.00 | — | — |
| ACOS | n/a | — | — |
| ROAS | n/a | — | — |

---
*Data source: Amazon Advertising API (Sponsored Products, US profile
26765323558215). Window Oct 3–4, 2026 (SUMMARY, 14-day attribution for
sales/ACOS/ROAS). Pulled and verified against the Sep 24–Oct 5 window, which
also showed zero activity.*

# PPC 2-Day Report — 7–8 November 2026

**Reporting window:** 2026-11-07 to 2026-11-08 (2 full days)
**Marketplace:** Amazon US (profile 26765323558215, "Uzoebo Archbold E-Commerce")
**Report generated:** 2026-11-11 (data lags ~48h, so this is the latest finalised window)
**Report type:** 2-day · first run of this type (no prior 2-day report to compare against)

---

## ⚠️ Read this first — the ads are not running

The data pulled cleanly, but it shows **zero advertising activity**: no impressions,
no clicks, no spend and no ad sales across all 15 US campaigns for 7–8 November. A
wider 14-day check (26 Oct – 8 Nov) shows the **same zero** — the account has not
served a single ad impression in over two weeks.

The most likely reason: the US seller profile shows **no valid payment method on
file** (`validPaymentMethod: false`). Amazon stops serving Sponsored Products ads
when billing isn't valid. **This is almost certainly a billing fix in Seller
Central, not a campaign setting** — nothing inside the ad console will restart
delivery until the payment method is sorted.

**Two setup issues were found and fixed automatically this run** (details at the
bottom), so future runs will pull data without manual help.

---

## Part A — Data table (by campaign)

All figures are $0 / zero because nothing served in the window. Campaigns are live
in the account but delivered no impressions.

| Campaign | Impressions | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto … B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*CA and MX seller profiles were also checked — they contain no Sponsored Products
campaigns, so US is the only active marketplace.*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00. **Sales from ads:** $0.00. **ACOS / ROAS:** n/a (no spend).
- **Best / worst campaign:** none — every campaign delivered nothing, so there's
  nothing to rank.
- **Wasted spend / negatives to add:** none. You can't waste money on ads that
  aren't running. No negative-keyword action needed this period.
- **Search terms to add as exact-match:** none available — with zero clicks there
  are no converting search terms to harvest yet.
- **What to do next (priority order):**
  1. **Fix billing in Seller Central.** The US ad profile shows no valid payment
     method, which is the most likely reason nothing is serving. Add/verify a card,
     then confirm campaigns show "Delivering" (not "Out of budget" or a billing
     warning).
  2. **Confirm campaign + budget status.** Once billing is valid, check that the 15
     campaigns are Enabled and have daily budgets (the account default was ~$40/day).
  3. **Re-run this report in 2–3 days.** Once ads serve, data will flow and the next
     report can actually judge ACOS, wasted spend and search terms.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report type, so
there is no prior baseline to compare against. This report establishes the baseline:
15 US campaigns, $0 spend, $0 sales, 0 impressions. Future 2-day reports will show
change vs. this one as a number and a percentage.

---

## Appendix — What went wrong and what was fixed (plain English)

The scheduled credentials had one thing set incorrectly, which this run detected and
worked around automatically:

1. **Wrong profile ID.** `AMZ_PROFILE_ID` was set to an *application* identifier
   (`amzn1.application.…`) instead of the numeric advertising-account ID Amazon
   expects. The API rejected it with "Invalid scope". Fix: the run listed the
   account's real profiles and used the correct US one (`26765323558215`). The
   wrong env var should ideally be corrected at source, but the run no longer
   depends on it.
2. **One unsupported metric combination.** Amazon's campaign report doesn't allow
   the 7-day ACOS/ROAS columns directly, so those are computed from cost and sales
   instead. (No effect this period since everything is zero.)

Both fixes are recorded in `notes-to-self.md` so future runs handle them without
interruption. The remaining issue — **ads not serving, likely due to the missing
payment method — needs the account owner to act in Seller Central**; it can't be
fixed from the API.

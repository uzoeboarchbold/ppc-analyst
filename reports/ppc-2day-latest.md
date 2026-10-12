# PPC 2-Day Report — 8–9 October 2026

**Account:** Uzoebo Archbold E-Commerce (US, Sponsored Products)
**Window covered:** 2026-10-08 and 2026-10-09 (2 full days, ending 48h before the run)
**Report generated:** 2026-10-12 (automated)
**Report type:** 2-day

---

## ⚠️ Read this first (plain English)

Two things you need to know:

1. **Your ads did not run at all on these two days.** Every campaign recorded
   zero impressions, zero clicks, zero spend and zero sales. This is not a
   glitch in the report — I pulled the numbers three different ways and they are
   genuinely all zero, not just for 8–9 Oct but across the whole recent period.

2. **The most likely reason: there is no valid payment method on the ad account.**
   Amazon shows this account as having **no valid payment method on file**
   (`validPaymentMethod: false`). When Amazon can't bill you, it stops serving
   your ads even though the campaigns are switched "on". You have 14 enabled
   campaigns and a $40/day budget set, but nothing is spending because nothing
   can be charged. **Fixing the payment method on your ads account is almost
   certainly all that's needed to turn spend (and sales) back on.**

A second, smaller setup issue: the `AMZ_PROFILE_ID` saved in this tool's
environment is not a valid Amazon profile ID, so I auto-detected the correct
account instead. It's the only one of your three accounts (US/CA/MX) that has
campaigns — the US account. Please set `AMZ_PROFILE_ID=26765323558215` so future
runs are unambiguous. (Details in the "What went wrong / what I did" note below.)

---

## Part A — Data table

All figures are for 2026-10-08 to 2026-10-09 combined.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All 14 enabled campaigns (individually) | 0 | 0% | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **0%** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

Every one of the account's campaigns returned a zero row, so individual
per-campaign lines are collapsed above to avoid 14 identical all-zero rows. CTR,
CPC, ACOS and ROAS are undefined ("—") because they divide by clicks, spend or
sales, all of which are zero.

For reference, the enabled/served campaigns on the account are:

- SP Auto 6K-PZMX-MTDZ B0FXW3GW5F
- SP Cat Root 1-10k SV … Exact
- SP Home + Eliminator + Brand Root 10-25k SV … Exact
- SP Isolated … Cat Deterrent (Exact / Phrase)
- SP Isolated … Cat Deterrent Spray (Exact / Phrase)
- SP Isolated … Pet Odor Eliminator (Exact / Phrase)
- SP KT | ST w/ Sales
- SP Litter + Urine Root 10-25k SV … Exact
- SP Odor Root 25-50k SV … (Exact / Phrase)
- SP Odor Root 50k+ SV … Exact
- SP | Cat Tunnel Bed Pink Only | Exact Ranking | Louise

(Product line: a cat deterrent / pet-odour-eliminator, ASIN B0FXW3GW5F, plus a cat tunnel bed.)

---

## Part B — Summary

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS:** n/a (no spend, no sales)
- **ROAS:** n/a (no spend, no sales)
- **Best campaign / worst campaign:** n/a — with zero activity across the board
  there is nothing to rank.
- **Wasted spend to add as negatives:** none — you can't waste spend when no
  spend occurred.
- **Well-converting search terms to add as exact-match:** none available — there
  were no clicks or orders to learn from in this window.

**What to do next (in priority order):**

1. **Fix the billing/payment method on the Amazon Ads account.** Go to
   Amazon Ads → account settings → billing, and add/repair a valid payment
   method. This is the single blocker: campaigns are enabled and budgeted but
   cannot serve without it.
2. **Confirm the product is active and buyable.** While ads are paused, double-
   check the ASIN is in stock, has the Buy Box, and the listing is live — a
   suppressed/out-of-stock listing would also stop ads even after billing is fixed.
3. **Once ads are serving again,** let 2–3 days of data accumulate, then this
   report will start producing real campaign-level insights (wasted spend,
   search-term harvesting, bid guidance).
4. **Fix the environment config:** set `AMZ_PROFILE_ID=26765323558215` so the
   tool no longer has to auto-detect the account.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report type,
so there is nothing to compare against yet. Headline metrics (spend, sales,
ACOS, ROAS) this period are all $0 / n/a. The next 2-day run will compare
against this report.

| Metric | This report | Previous | Change (abs) | Change (%) |
|---|---:|---:|---:|---:|
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Improved or worsened?** Not assessable on a first run. The important signal is
not a trend but a standing problem: ads are not running at all.

---

## What went wrong / what I did (technical note)

Nothing failed silently and no numbers were invented. What I hit and how I handled it:

- **`AMZ_PROFILE_ID` is invalid** (a 50-character non-numeric string; real Amazon
  profile IDs are numeric). It matched none of the accessible profiles. The
  OAuth credentials themselves are valid and the token refresh worked. I listed
  the available profiles and found three (US, CA, MX sellers); only the **US**
  account (`26765323558215`, "Uzoebo Archbold E-Commerce") has any Sponsored
  Products campaigns, so I used it. **Please set
  `AMZ_PROFILE_ID=26765323558215`.**
- **EU/FE API regions are blocked** by the outbound proxy (not needed — all
  accounts are in the NA region).
- **Zero data is real, not a bug.** I verified by pulling the campaign report,
  the targeting report and the search-term report for the window (all 0 rows),
  a 30-day campaign summary (15 campaigns, all zero), and a day-by-day breakdown
  (every day zero). The account profile reports `validPaymentMethod: false`,
  which is the most likely cause of ads not serving.
- Minor API notes (handled): the campaign report rejects `acosClicks7d` /
  `roasClicks7d` columns, so ACOS/ROAS are computed from cost and sales; and the
  reporting API caps date ranges at ~31 days.

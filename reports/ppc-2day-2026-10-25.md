# PPC 2-Day Report — 21–22 Oct 2026

**Marketplace:** Amazon US (Sponsored Products) · Account: Uzoebo Archbold E-Commerce
**Dates covered:** 21 Oct 2026 – 22 Oct 2026 (2 full days, ending 48h before the run to let Amazon's data finalise)
**Generated:** 25 Oct 2026

---

## ⚠️ Read this first — your ads are not running

For the two days in this report — and in fact for **every one of the last 30 days** — your
Sponsored Products ads served **zero impressions, got zero clicks, and spent $0**. You have
**15 campaigns switched ON** (combined budget **$23.50/day**), but Amazon is not showing any
of them to shoppers.

The most likely cause: **the US advertising account has no valid payment method on file**
(the account flag `validPaymentMethod` is `false`). When Amazon can't bill you, it keeps your
campaigns "enabled" but quietly stops delivering them. So you're paying nothing — but you're
also getting nothing, and any ad-driven sales have been switched off for at least a month.

**What to check today:** Amazon Ads / Seller Central → **Billing & payments** → add or fix the
card on file. Once a valid payment method is accepted, delivery normally resumes within a few
hours. After that, this report will start showing real numbers again.

*Two small housekeeping notes on the automation itself are at the very bottom.*

---

## Part A — Data table (per campaign + totals)

All enabled campaigns delivered nothing in the window, so every metric is zero. The totals row
is shown here; the 15 enabled campaigns are listed in the appendix.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **All enabled campaigns (15)** | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(CTR, CPC, ACOS and ROAS cannot be calculated with zero clicks/spend.)*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00 · **Sales (ad-attributed):** $0.00 · **ACOS / ROAS:** n/a (no spend).
- **Best / worst campaign:** not applicable — none of them ran.
- **Wasted spend / negatives to add:** none to suggest, because there was no spend. (The real
  "waste" here is opportunity: 15 live campaigns reaching nobody.)
- **Well-converting search terms to add as exact-match:** none available — no clicks or search-term
  data were generated in the window.
- **What to do next:**
  1. **Fix billing first.** Add/repair the payment method on the US ad account. Nothing else
     matters until ads can serve.
  2. **Confirm delivery resumes.** A day after fixing billing, check that impressions are
     climbing again (the next 2-day report will show this).
  3. **Then review budgets/bids.** Most campaigns sit at a $1.50/day budget. Once delivery is
     back, we can see which of the 15 campaigns actually earn their keep and shift budget to the
     winners.
  4. **CA and MX:** no Sponsored Products campaigns exist on those marketplaces — nothing to report
     there. US is your only active PPC marketplace.

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists — this is the first run of this report type**, so there is no
prior baseline to compare against. Headline metrics to track going forward: Impressions, Clicks,
Spend, Sales, ACOS, ROAS. From the next run onward this section will show each metric's change as
a number and a percentage.

For context, here's the baseline this run establishes:

| Metric | This report (21–22 Oct) |
|---|--:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| ACOS | n/a |
| ROAS | n/a |

---

## Appendix — the 15 enabled campaigns (all delivered 0 in the window)

Product advertised: ASIN **B0FXW3GW5F** (Cat Deterrent Spray / Pet Odor Eliminator) and one
Cat Tunnel Bed campaign.

| Campaign | Daily budget |
|---|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | $1.50 |
| SP Cat Root 1-10k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | $1.50 |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | $1.50 |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Exact | $1.50 |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | $1.50 |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Exact | $1.50 |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | $1.50 |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Exact | $1.50 |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | $2.50 |
| SP KT \| ST w/ Sales | $1.50 |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | $1.50 |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | $1.50 |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | $1.50 |
| SP Odor Root 50k+ SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | $1.50 |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | $1.50 |
| **Total enabled daily budget** | **$23.50** |

*(32 further campaigns are paused and 7 archived; they are excluded above.)*

---

## Notes on the automation (for the owner)

1. **Email not sent automatically.** This report was saved to the repo and uploaded to the Google
   Drive "PPC Reports" folder, but it could **not be emailed** to you: the Gmail connector is
   connected to your account but is **not enabled for these automated Claude Code sessions**, so no
   send-email tool is available to the run. To turn email on, enable the Gmail connector (with send
   permission) for Claude Code in your claude.ai connector settings.
2. **Profile ID env var is wrong.** `AMZ_PROFILE_ID` is set to an application ID rather than a real
   advertising profile ID; the run auto-corrected by looking up the account's real US profile. Worth
   fixing the stored value to `26765323558215` (US) so future runs don't rely on the workaround.

*Data source: Amazon Advertising API (Sponsored Products reporting v3), 7-day attribution. Figures
are final (data ends 48h before run).*

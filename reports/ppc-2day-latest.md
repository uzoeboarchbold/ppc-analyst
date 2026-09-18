# PPC 2-Day Report — 14–15 Sep 2026

**Marketplace:** Amazon US (Sponsored Products) · **Report generated:** 18 Sep 2026
**Window covered:** 14 Sep 2026 – 15 Sep 2026 (2 full days, ending 48h before run to allow Amazon's data to finalise)
**Compared against:** previous 2-day window (12–13 Sep 2026)

---

## ⚠️ Please read first (two things need your attention)

1. **No ads ran in this window.** Every one of your 15 Sponsored Products campaigns
   recorded **zero impressions, zero clicks and zero spend** on both 14 and 15 Sep.
   These are real figures pulled from Amazon, not missing data. For wider context, the
   whole account delivered only **1,626 impressions, 16 clicks and $3.77 of spend over
   the last 30 days, with $0.00 in sales** — so the account is effectively dormant and
   has not yet produced an attributed order.

2. **A settings fix was needed to run this report.** The `AMZ_PROFILE_ID` credential
   was set to an *application ID* (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`),
   not a valid advertising profile ID, so it could not be used directly. I automatically
   selected your **US seller profile (26765323558215)** — the marketplace with all the
   activity — and the report ran fine. Your CA and MX profiles have no Sponsored Products
   activity. **Action for you:** update `AMZ_PROFILE_ID` to `26765323558215` so future
   runs are unambiguous.

---

## Part A — Data Table (per campaign)

All 15 US Sponsored Products campaigns, 14–15 Sep 2026:

| Campaign | Impr. | ToS Imp. Share | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Isolated … Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10–25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1–10k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10–25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Auto … B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*Dashes (—) mean the metric can't be calculated because there were no impressions/clicks
(e.g. CTR, CPC, ACOS and ROAS all require clicks or spend).*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not applicable (no spend, no sales).
- **Best campaign:** none — nothing delivered, so there is no top performer this window.
- **Worst campaign:** not applicable — you can't "waste" spend when spend is zero. The real
  issue is the opposite: **nothing is running at all.**
- **Wasted spend to add as negatives:** none this window (no clicks were paid for).
- **Well-converting search terms to add as exact-match:** none — there were no clicks or
  conversions to learn from.
- **Why is it all zero?** The campaigns exist but are not delivering. Over the last 30 days
  the account managed only $3.77 of spend and no sales, and the last two days delivered
  nothing. The most common causes are: campaigns **paused / out of budget**, **bids set too
  low** to win any auctions, or the product being **out of stock / not in the Buy Box**
  (ads don't serve without the Buy Box).

### What to do next
1. **Confirm the campaigns are actually enabled** and have daily budgets that aren't
   exhausted (check campaign + ad-group + portfolio status).
2. **Check the product listing is live, in stock, and holds the Buy Box** for ASIN
   B0FXW3GW5F — ads won't show otherwise.
3. **Raise bids** on your priority Exact campaigns. Over 30 days the account got impressions
   but almost no clicks (16 clicks on 1,626 impressions), which points to bids/placements
   too low to be competitive.
4. **Fix `AMZ_PROFILE_ID`** to `26765323558215` (see note above).
5. Once ads are delivering again, this report will start showing real spend, sales and
   search-term data to optimise.

---

## Part C — Comparison vs previous 2-day report

This is the **first 2-day report saved in the repository**, so there is no stored prior
report to diff against. For a like-for-like check I also pulled the immediately preceding
2-day window (12–13 Sep 2026); it was **also entirely zero**, so nothing has changed.

| Metric | This window (14–15 Sep) | Prev window (12–13 Sep) | Change (abs) | Change (%) |
|---|--:|--:|--:|--:|
| Impressions | 0 | 0 | 0 | 0% |
| Clicks | 0 | 0 | 0 | 0% |
| Spend | $0.00 | $0.00 | $0.00 | 0% |
| Purchases | 0 | 0 | 0 | 0% |
| Sales | $0.00 | $0.00 | $0.00 | 0% |
| ACOS | n/a | n/a | — | — |
| ROAS | n/a | n/a | — | — |

**Verdict:** No change — the account was dormant in both windows. Nothing improved or
worsened because no ads delivered in either period. The priority is to get campaigns
serving again (see "What to do next").

---
*Data source: Amazon Advertising API (Sponsored Products v3 reporting), 14-day attribution.
Figures are final for this window (48h lag applied).*

# PPC 2-Day Report — 13–14 September 2026

**Report type:** 2-day | **Window covered:** Sun 13 Sep – Mon 14 Sep 2026 (2 full days, ending 48h before the run)
**Account:** Uzoebo Archbold E-Commerce — US Sponsored Products | **Generated:** 2026-09-17

---

## ⚠️ Read this first — the account is not running any ads

Every active campaign served **zero impressions, zero clicks and zero spend** across
both days of this window. This is **not a data or reporting error** — the Amazon Ads
API is working and returned real figures. The problem is that the ads simply are not
being shown.

Checking the daily history, the account **stopped serving completely on 3 September
2026** and has been dark ever since (14 straight days as of this report). Before that,
traffic in August was already very small (tens to a few hundred impressions a day, 0–2
clicks, under $1/day spend) and produced **no sales at all** in the month.

15 campaigns are switched **ON** with daily budgets of $1.50–$2.50, yet none of them
are getting a single impression. When enabled campaigns show zero impressions across
the *whole account* starting on one specific date, the cause is almost always
account-level, not the campaigns themselves. Most likely one of:

1. **Billing / payment problem** — a failed card or unpaid balance pauses all delivery.
2. **Product out of stock or listing suppressed** — ads can't run if the product isn't
   buyable. Worth checking inventory and listing health for ASIN B0FXW3GW5F.
3. **Bids below the auction floor** — with $1.50 budgets and low bids, ads may never win
   a placement. (Less likely to cause a *hard stop on one date*, but possible.)

**Please check Seller Central → Billing, Inventory, and Listing/Account health.** Until
serving resumes there is no performance to optimise.

*(Config note for the automation: the `AMZ_PROFILE_ID` environment variable holds an
application id, not a valid Ads profile id. This run auto-corrected by using the US
seller profile `26765323558215`. Please update the variable to that value so future runs
are unambiguous.)*

---

## Part A — Data Table (by campaign)

Window: 13–14 Sep 2026. All active campaigns, 7-day sales attribution.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto B0FXW3GW5F | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Cat Root 1-10k SV — Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Home + Eliminator + Brand Root 10-25k SV — Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent Spray Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent Spray Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Pet Odor Eliminator Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Pet Odor Eliminator Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Litter + Urine Root 10-25k SV — Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25-50k SV — Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25-50k SV — Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 50k+ SV — Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*(32 further campaigns are Paused and 7 are Archived; none served in this window either.
"n/a" appears wherever a metric can't be calculated because there were no impressions,
clicks or spend.)*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not applicable —
  you can't have an advertising cost of sale when there was no advertising cost and no
  sales.
- **Best campaign / worst campaign:** none stand out — every campaign performed
  identically (nothing). There is no winner or loser to point to because nothing ran.
- **Wasted spend / negatives to add:** none to suggest — there was no spend to waste and
  no search terms captured, so there is nothing to add as a negative keyword right now.
- **Well-converting search terms to add as exact-match:** none available — with no clicks
  or impressions, the search-term report is empty, so there are no new exact-match terms
  to harvest this period.
- **The real issue:** the ads are switched on but not being shown to anyone, and haven't
  been since **3 September**. This is the one thing that matters this week.

### What to do next
1. **Check billing in Seller Central first** — a failed payment is the most common reason
   all ads stop at once. Fix any outstanding balance or expired card.
2. **Check inventory and listing health for ASIN B0FXW3GW5F** — if the product is out of
   stock or the listing is suppressed, ads cannot run.
3. **If billing and inventory are fine, raise bids and daily budgets** — $1.50/day with
   low bids may be too small to win any placements. Nudge bids up on the core exact-match
   campaigns and set budgets to a level that can actually compete.
4. **Re-run this report once ads are live again** so we finally get real performance data
   to optimise. Note that even in August (when ads did run a little) the account made
   **zero sales** — so once serving resumes, the next priority is conversion: check price,
   images, reviews and relevance of the targeted keywords.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first 2-day report
on record, so it becomes the **baseline** for future runs.

| Headline metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Total spend | $0.00 | — | — | — |
| Total sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |
| Clicks | 0 | — | — | — |
| Purchases | 0 | — | — | — |

**Trend:** Can't be assessed yet (no prior report). For context from the daily history,
the direction is clearly **worse** — the account went from a trickle of paid traffic in
August to a complete stop on 3 September. The next 2-day report will compare against this
baseline.

---
*Prepared automatically by the PPC Analyst. Figures pulled live from the Amazon Ads API
(Sponsored Products, US profile, 7-day attribution). No numbers were estimated or
invented; where activity was zero the report says so.*

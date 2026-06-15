# PPC 2-Day Report — June 11–12, 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products)
**Window covered:** 11 Jun 2026 – 12 Jun 2026 (2 full days, ending 48h before the run)
**Report generated:** 15 Jun 2026
**Data source:** Amazon Advertising API (Sponsored Products, v3 reporting)

---

## ⚠️ Read this first

**The data pulled cleanly — and it shows there was effectively no advertising
activity in this window.** Only two campaigns are currently live (both launched
6 days ago, on 9 Jun); every other campaign in the account is paused or
archived. Across the two days of this report, those two live campaigns served
**zero impressions, took zero clicks, spent $0.00 and made $0.00 in sales.**

This is real data, not a pull error. The takeaway is operational, not
analytical: **your ads are essentially not running.** Details and what to do
below.

**Two delivery notes (one-time setup gaps, not data problems):**
1. The `AMZ_PROFILE_ID` environment variable holds an *application* ID, not a
   usable advertising profile ID. I worked around it by looking up the correct
   numeric US profile (`26765323558215`) automatically. Worth fixing the env
   var so future runs are cleaner.
2. **There is no email-sending tool wired into this environment**, so I could
   not send the formal "PPC 2-Day Report" email. The report is saved in the
   repo and uploaded to the Google Drive 'PPC Reports' folder, and the headline
   is delivered to your inbox via the run notification. To get the proper
   emailed report, an email/Gmail integration needs to be connected.

---

## Part A — Data Table (11–12 Jun 2026)

Only the two **enabled** campaigns are shown (the only ones eligible to serve).
ToS IS = Top-of-search impression share. n/a = not calculable (no impressions /
no clicks / no spend).

| Campaign | Impressions | ToS IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*All other campaigns in the account are Paused or Archived and did not serve in
this window, so they are not listed.*

**Keyword / target breakdown:** empty — no targets received impressions in the
window.
**Search-term breakdown:** empty — no search terms triggered the ads in the
window.

---

## Part B — Plain-English Summary

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS:** not applicable (no spend)
- **ROAS:** not applicable (no sales)
- **Best campaign / Worst campaign:** not distinguishable — both live campaigns
  did nothing.
- **Wasted spend:** none, because nothing was spent. (Good news in the narrow
  sense, but only because the ads aren't running.)
- **Search terms to add as exact-match:** none available — there were no
  converting (or even clicking) search terms to harvest this period.

**What's actually going on:** The account has ~50 campaigns but only two are
switched on, both brand-new ($8/day each, launched 9 Jun). Looking at a slightly
wider window (9–13 Jun) for context, those two campaigns together gathered only
~78 impressions total and **zero clicks** — so even when they do show, they're
barely winning placements and getting no engagement. The most likely causes are
**bids set too low to win auctions** and/or **targeting that is too narrow**
(these are "search terms with sales" campaigns, which by design target a small,
specific set of terms).

**What to do next (priority order):**
1. **Confirm intent.** If advertising is supposed to be live, the current setup
   isn't delivering. If it's intentionally dark, no action needed — but then a
   daily/2-day PPC report has little to measure.
2. **Raise bids** on the two live campaigns enough to start winning impressions
   (small new campaigns usually need competitive opening bids to gather data).
3. **Widen targeting or turn on an Auto campaign** for a few days to discover
   which search terms actually convert, then graduate the winners into
   exact-match — that's the data this report is designed to surface, and right
   now there's none to surface.
4. **Check the daily budgets are actually being consumed** in Seller Central; if
   spend stays at $0 with raised bids, there may be a listing/eligibility issue
   (e.g. suppressed listing, out of stock, or not "Featured Offer").

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists** — this is the first one. There is no
baseline to compare against, so headline-metric changes (number and %) cannot be
shown this time. From the next 2-day run onward, this section will show the
change in Impressions, Clicks, Spend, Sales, ACOS and ROAS versus this report.

| Metric | Previous | This report | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | — | 0 | — | — |
| Clicks | — | 0 | — | — |
| Spend | — | $0.00 | — | — |
| Sales | — | $0.00 | — | — |
| ACOS | — | n/a | — | — |
| ROAS | — | n/a | — | — |

**Direction:** Not assessable yet (no prior data). Baseline established here at
zero activity.

---

*Generated automatically by the PPC Analyst routine. Figures are pulled directly
from the Amazon Advertising API; no numbers are estimated or invented. Where a
metric is "n/a" it is because there was no spend/click/impression to calculate
it from.*

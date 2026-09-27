# PPC 2-Day Report — Sep 23–24, 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (USD)
**Report window:** 23–24 September 2026 (2 full days, ending 48h before the 27 Sep run)
**Ad type:** Sponsored Products
**Generated:** 2026-09-27 (automated)

---

## ⚠️ Read this first — your ads are switched off

There is **no data to report for 23–24 September because no ads ran.** This is not
a glitch in the report — the Amazon Ads API returned successfully and simply shows
**zero** impressions, clicks, spend and sales for every campaign.

Your Sponsored Products campaigns stopped delivering entirely after **2 September 2026**.
From 3 September onward — including this report's window — nothing has been shown to
shoppers and nothing has been spent.

**Most likely cause:** the US advertising account currently has **no valid payment
method on file** (Amazon flags the account `validPaymentMethod: false`). Amazon pauses
all ad delivery when billing fails. This lines up exactly with delivery dropping to
zero right after 2 September.

**One thing to do:** log in to Seller Central → **Advertising / Billing** and add or
update a valid payment method. Nothing else in this report will change until that is fixed —
your campaigns are enabled and waiting, but Amazon won't run them without working billing.

*(Note for the record: the `AMZ_PROFILE_ID` credential provided to this tool was
misconfigured — it held an application ID instead of a profile ID. The tool identified
the correct US advertising profile automatically and used it, so the numbers below are
from the right account. This has been noted so future runs are unaffected.)*

---

## Part A — Data table (23–24 September 2026)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *(no campaign delivered any impressions in this window)* | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

All 50+ Sponsored Products campaigns in the account returned zero delivery for both days.
Metrics that divide by clicks or impressions (CTR, CPC, ACOS, ROAS, Top-of-search
impression share) are undefined because there was no traffic.

---

## Part B — Summary in plain English

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS / ROAS:** not applicable — no spend and no sales.
- **Best / worst campaign:** none — no campaign ran, so there is nothing to rank.
- **Wasted spend / negatives to add:** none this window (you can't waste money on ads
  that aren't running). No search-term data was generated, so there are no new
  exact-match keywords or negatives to recommend from this period.
- **Well-converting search terms to add as exact-match:** none available — no clicks
  or conversions occurred.

### What's actually going on (context beyond the 2-day window)
Delivery has been flat-lined for over three weeks. Here is the last time your ads were
live, from the daily data:

| Date | Impressions | Spend |
|---|---:|---:|
| Aug 26 | 100 | $0.25 |
| Aug 27 | 102 | $0.00 |
| Aug 28 | 136 | $0.25 |
| Aug 29 | 164 | $0.02 |
| Aug 30 | 165 | $0.00 |
| Aug 31 | 166 | $0.25 |
| Sep 1 | 234 | $0.08 |
| Sep 2 | 53 | $0.00 |
| **Sep 3 → Sep 24** | **0** | **$0.00** |

Even in that final active week (Aug 26 – Sep 2), the account got ~1,120 impressions but
almost **no clicks and $0.85 total spend, with 0 sales** — the ads were barely being
clicked even when live. So there are two problems, in priority order:

1. **Billing is blocking everything** (the urgent one).
2. Once ads are live again, **click-through and conversion are very weak** — worth
   reviewing bids, main images, titles and price competitiveness so the restarted
   spend actually earns clicks and sales.

### What to do next
1. **Today:** fix the payment method in Seller Central so campaigns can deliver.
2. **After delivery resumes (give it 48–72h):** re-run this report to get real numbers.
3. **Then:** with live click/search-term data, prune wasted spend, add converting terms
   as exact-match, and add negatives — none of which is possible while spend is $0.
4. Consider whether the $1.50/day budgets are enough to gather meaningful data once ads
   are back on.

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists** — this is the first run of this report type, so there
is nothing to compare against yet. This report becomes the baseline.

For reference, the headline numbers to track next time:

| Metric | This report (Sep 23–24) |
|---|---:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| Purchases | 0 |
| ACOS | n/a |
| ROAS | n/a |

**Trend read:** cannot compute a change yet. The meaningful movement to watch for in the
next report is simply whether spend and impressions return to non-zero — i.e. whether the
billing fix took effect.

---

*Data source: Amazon Advertising API (Sponsored Products v3 reporting), US profile
26765323558215. Figures are final (48-hour data lag respected). Currency: USD.*

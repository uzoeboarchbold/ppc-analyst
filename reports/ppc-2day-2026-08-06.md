# PPC 2-Day Report — Aug 2–3, 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon US (amazon.com), USD
**Report window:** Saturday 2 Aug – Sunday 3 Aug 2026 (2 full days, finalised ≥48h)
**Ad product:** Sponsored Products · **Attribution:** 7-day · **Generated:** 2026-08-06 (automated)

> **Setup note (please fix):** The `AMZ_PROFILE_ID` environment variable holds an
> LWA *application* ID (`amzn1.application.dd42…`), not a numeric Amazon Ads
> profile ID, so it could not be used directly. Login and data pull otherwise
> worked. I listed the account's real profiles and auto-selected the **US
> marketplace** profile (`26765323558215`) — the only actively-managed one (it
> has a real $40/day budget; the CA and MX profiles carry placeholder max
> budgets). Please set `AMZ_PROFILE_ID=26765323558215` so future runs don't have
> to guess. (Details logged in `notes-to-self.md`.)

---

## Part A — Data table (by campaign)

| Campaign | Impr. | ToS IS | Clicks | CTR | Purch. | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Isolated … Pet Odor Eliminator Phrase | 21 | 29% | 1 | 4.8% | 0 | $0.00 | $2.84 | $2.84 | — | 0.00 |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 21 | 0% | 0 | 0.0% | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP PT Pet Odor Eliminator … B0FXW3GW5F | 18 | 1% | 0 | 0.0% | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 5 | 0% | 0 | 0.0% | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP Litter + Urine Root 10-25k SV … Phrase | 2 | 0% | 0 | 0.0% | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP KT \| ST w/ Sales | 2 | 0% | 0 | 0.0% | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP Home + Eliminator + Brand Root 10-25k SV … Phrase | 1 | 0% | 0 | 0.0% | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP Odor Root 25-50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | 0.00 |
| SP PT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | 0.00 |
| **TOTAL** | **70** | **—** | **1** | **1.4%** | **0** | **$0.00** | **$2.84** | **$2.84** | **—** | **0.00** |

*ToS IS = Top-of-search impression share. ACOS shown as "—" where there were no
sales to divide by. Eleven campaigns returned data for the window; the rest of
the account served no impressions.*

---

## Part B — Summary (plain English)

**Headline:** Over these two days the account spent **$2.84**, got **70 ad
views (impressions)**, **1 click**, and made **no sales**. So ACOS can't be
calculated (no sales) and ROAS was **0**.

**The real story is under-delivery, not efficiency.** The daily budget is about
$40, yet total spend across two whole days was under $3. The ads are barely
showing — almost every campaign got only a handful of impressions and zero
clicks. That points to bids that are too low to win placements (and/or
campaigns that are paused or narrowly targeted), rather than a spend problem.

- **"Best" campaign:** *Pet Odor Eliminator (Phrase)* — the only one that did
  anything: 21 impressions, 1 click, a healthy 4.8% click-through rate, and a
  29% top-of-search impression share. It just didn't convert on its single
  click.
- **"Worst" campaign:** Nothing is burning money — there's nothing to flag as
  wasteful. The problem is the opposite: most campaigns are effectively dormant
  (0 clicks, a few or zero impressions).
- **Wasted spend / negatives:** None to recommend. Total spend was $2.84 on a
  single click — far too little data to call any keyword wasteful or to add
  negatives. Doing so now would just choke delivery further.
- **Search terms to add as exact-match:** None yet. Zero purchases means there
  are no converting search terms to harvest. (The one search term that got the
  click — *"pet odor eliminator spray"* — did not sell, so it's not a candidate.)

### What to do next
1. **Fix the delivery gap first.** Raise bids on the priority campaigns (start
   with the Pet Odor Eliminator and Cat Tunnel Bed campaigns) so the ads
   actually win impressions. At current levels there isn't enough traffic to
   learn anything.
2. **Confirm campaigns are live.** Several returned 0 impressions — check they
   aren't paused, out of budget, or bidding below the floor.
3. **Then let it run and re-measure.** Once daily spend is closer to the $40
   budget and clicks are flowing, the next reports can start judging ACOS/ROAS
   and harvesting converting search terms.
4. **Fix `AMZ_PROFILE_ID`** (see setup note above) so runs stop guessing the
   account.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run of this type, so
there is nothing to compare against yet.** This report establishes the
baseline. From the next 2-day run onward, each headline metric (spend, sales,
ACOS, ROAS, clicks, impressions) will be shown as a change vs. this report in
both absolute and percentage terms.

| Metric | This report | Previous | Change |
|---|--:|--:|:--|
| Impressions | 70 | — | baseline |
| Clicks | 1 | — | baseline |
| Spend | $2.84 | — | baseline |
| Sales | $0.00 | — | baseline |
| Purchases | 0 | — | baseline |
| ACOS | — | — | baseline |
| ROAS | 0.00 | — | baseline |

*Verdict:* n/a for a first run. Bottom line to watch next time: is spend rising
toward budget and are clicks converting?

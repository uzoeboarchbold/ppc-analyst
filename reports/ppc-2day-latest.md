# PPC 2-Day Report — 20–21 Sep 2026

**Requested window:** 2 full days ending 48h before the run = **Sat 20 – Sun 21 Sep 2026**
**Run date:** 2026-09-24 (23:19 UTC) · **Account:** Uzoebo Archbold E-Commerce — US (Sponsored Products)
**Report type:** 2-day · **Compares against:** previous 2-day report

---

## ⚠️ Please read first (data availability + account status)

Two things you need to know:

1. **No data is available yet for the requested window (20–21 Sep).** Amazon's
   reporting for this account is currently only finalised up to **18 Sep**. The
   days 19, 20 and 21 Sep returned no data at all — the ~48-hour lag we plan
   around is, right now, running closer to **~6 days** for this account. I did
   not invent any numbers to fill the gap.

2. **Your ads have not been running.** Even for the days that *are* available,
   the account has shown **zero impressions, zero clicks, zero spend and zero
   sales every day since 3 September**. The last time any ad was shown at all was
   1–2 September (a tiny 287 impressions, $0.08 spend, no sales). So the real
   headline isn't "how did the last 2 days perform" — it's **"the ads aren't
   being served."**

What I checked and fixed automatically:
- The `AMZ_PROFILE_ID` setting was pointing at the wrong kind of ID (an
  "application" ID, not an ad-account/profile ID). I identified the correct US
  ad profile and used it, so the connection itself is healthy.
- Confirmed the empty result is genuine (not a broken request) by pulling a
  wider day-by-day history — see the table below.

---

## Part A — Data table

**Requested window — 20–21 Sep 2026 (US Sponsored Products)**

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| _All campaigns_ | — | — | — | — | — | — | — | — | — | — |
| **TOTAL** | **No data available** | — | — | — | — | — | — | — | — | — |

_"—" = Amazon has not yet finalised data for these dates. There is nothing to
report per-campaign because no campaign has data for 20–21 Sep yet._

**Context — most recent available daily activity (whole US account)**

| Date | Impressions | Clicks | Total cost | Sales |
|---|---|---|---|---|
| 2026-09-01 | 234 | 1 | $0.08 | $0.00 |
| 2026-09-02 | 53 | 0 | $0.00 | $0.00 |
| 2026-09-03 → 2026-09-18 | 0 (every day) | 0 | $0.00 | $0.00 |
| 2026-09-19 → 2026-09-21 | not available yet | — | — | — |

_Data currently available only through 18 Sep 2026._

---

## Part B — Summary (plain English)

- **Overall spend:** ~$0.00 in the recent period (last spend of any kind was
  **$0.08 on 1 Sep**). **Sales:** $0.00. **ACOS / ROAS:** not meaningful — there
  are effectively no clicks and no sales to measure.
- **Best / worst campaign:** not applicable — no campaign delivered any
  impressions in the window, so none can be ranked.
- **Wasted spend:** none, because nothing is being spent. That sounds fine, but
  the flip side is worse: **the ads aren't showing at all**, so the account is
  also making **no sales from advertising**.
- **Search terms to add as exact-match:** none available — with no clicks there
  are no converting search terms to harvest yet.
- **Negatives to add:** none needed — there is no wasted spend to cut.

**Why the ads likely aren't serving:** the account has 54 Sponsored Products
campaigns, most of them ENABLED, but on very small budgets (~$1.50/day) and,
based on getting essentially zero impressions, **bids that are too low to win any
ad placements**. Enabled ≠ being shown.

**What to do next (in order):**
1. **Confirm the campaigns are actually eligible to run** in Seller Central /
   Campaign Manager — check for "out of budget," "bid too low," listing not
   buyable, or suppressed-listing warnings.
2. **Raise bids** on a few priority campaigns to a level that can win impressions
   (start of search / rest of search), and lift daily budgets above $1.50 so they
   aren't capped instantly.
3. **Re-check in 2–3 days.** Once impressions and clicks start flowing, this
   report will have real numbers to optimise (harvest converting terms, add
   negatives, manage ACOS).
4. **Data lag:** if the ~6-day lag persists, we should widen the reporting buffer
   so the window always lands on finalised data. I've logged this for future runs.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first 2-day report, so there is
nothing to compare against yet. From the next run onward, this section will show
the change in each headline metric (impressions, clicks, spend, sales, ACOS,
ROAS) as both a number and a percentage, up or down.

---

_Generated automatically by the PPC Analyst routine. No figures were estimated or
invented; blanks mean Amazon had not finalised that data at run time._

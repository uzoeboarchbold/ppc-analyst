# PPC 2-Day Report — 21–22 Sep 2026

**Requested window:** 2 full days ending 48h before the run = **Mon 21 – Tue 22 Sep 2026**
**Run date:** 2026-09-25 (23:19 UTC) · **Account:** Uzoebo Archbold E-Commerce — US (Sponsored Products)
**Report type:** 2-day · **Compares against:** previous 2-day report (run 2026-09-24, window 20–21 Sep)

---

## ⚠️ Please read first (data availability + account status)

Two things you need to know up front:

1. **No data is available yet for the requested window (21–22 Sep).** Amazon's
   reporting for this account is still only finalised up to **18 Sep** — exactly
   the same cut-off as yesterday's run. Nothing new has finalised in the last 24
   hours, so the ~48-hour lag we plan around is currently running at **~7 days**
   for this account. I did not invent any numbers to fill the gap.

2. **Your ads are still not running.** For every day that *is* available
   (10–18 Sep, and in fact every day since 3 Sep), the account shows **zero
   impressions, zero clicks, zero spend and zero sales**. The last time any ad
   was shown at all was 1–2 September. So the real headline again isn't "how did
   the last 2 days perform" — it's **"the ads aren't being served."**

What I checked and fixed automatically:
- Used the correct **US ad profile** (the `AMZ_PROFILE_ID` environment variable
  still points at the wrong kind of ID — an "application" ID, not an ad-account
  ID — so I substituted the known-good US profile). The connection is healthy.
- Confirmed the empty window is genuine (not a broken request) by pulling a wider
  day-by-day history (10–24 Sep). Amazon returned finalised rows only through
  18 Sep, all zero — see tables below.

---

## Part A — Data table

**Requested window — 21–22 Sep 2026 (US Sponsored Products)**

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| _All campaigns_ | — | — | — | — | — | — | — | — | — | — |
| **TOTAL** | **No data available** | — | — | — | — | — | — | — | — | — |

_"—" = Amazon has not yet finalised data for these dates. There is nothing to
report per-campaign because no campaign has data for 21–22 Sep yet._

**Context — most recent available daily activity (whole US account)**

| Date | Impressions | Clicks | Total cost | Sales |
|---|---|---|---|---|
| 2026-09-01 | 234 | 1 | $0.08 | $0.00 |
| 2026-09-02 | 53 | 0 | $0.00 | $0.00 |
| 2026-09-03 → 2026-09-18 | 0 (every day) | 0 | $0.00 | $0.00 |
| 2026-09-19 → 2026-09-22 | not available yet | — | — | — |

_Data currently available only through 18 Sep 2026 (15 campaigns returned in the
daily pull; all zero every day)._

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00 in the recent period (last spend of any kind was
  **$0.08 on 1 Sep**). **Sales:** $0.00. **ACOS / ROAS:** not meaningful — there
  are effectively no clicks and no sales to measure.
- **Best / worst campaign:** not applicable — no campaign delivered any
  impressions in the window, so none can be ranked.
- **Wasted spend:** none, because nothing is being spent. That sounds fine, but
  the flip side is worse: **the ads aren't showing at all**, so advertising is
  producing **no sales**.
- **Search terms to add as exact-match:** none available — with no clicks there
  are no converting search terms to harvest yet.
- **Negatives to add:** none needed — there is no wasted spend to cut.

**Why the ads likely aren't serving:** the account has ~54 Sponsored Products
campaigns, most ENABLED, but on very small budgets (~$1.50/day) and, based on
getting essentially zero impressions, **bids that are too low to win any ad
placements**. Enabled ≠ being shown.

**What to do next (in order):**
1. **Confirm the campaigns are actually eligible to run** in Seller Central /
   Campaign Manager — check for "out of budget," "bid too low," listing not
   buyable, or suppressed-listing warnings.
2. **Raise bids** on a few priority campaigns to a level that can win impressions
   (top of search / rest of search), and lift daily budgets above $1.50 so they
   aren't capped instantly.
3. **Re-check in 2–3 days.** Once impressions and clicks start flowing, this
   report will have real numbers to optimise (harvest converting terms, add
   negatives, manage ACOS).
4. **Data lag:** the lag has now held at ~7 days for two runs. If it persists,
   we should widen the reporting buffer so the window always lands on finalised
   data. Logged for future runs.

---

## Part C — Comparison to previous 2-day report

Previous 2-day report: **run 2026-09-24, window 20–21 Sep 2026**.

| Headline metric | Previous (20–21 Sep) | This report (21–22 Sep) | Change (number) | Change (%) |
|---|---|---|---|---|
| Impressions | No data / 0 | No data / 0 | 0 | 0% |
| Clicks | No data / 0 | No data / 0 | 0 | 0% |
| Total cost | $0.00 | $0.00 | $0.00 | 0% |
| Sales | $0.00 | $0.00 | $0.00 | 0% |
| ACOS | n/a | n/a | — | — |
| ROAS | n/a | n/a | — | — |

**Verdict:** **No change — flat at zero.** Both windows fell inside the
data-lag gap and both sit within the account's ongoing dark period. Nothing has
improved or worsened because nothing is being spent or earned. The situation is
unchanged from yesterday: the priority remains getting ads to serve again, not
performance tuning.

---

_Generated automatically by the PPC Analyst routine. No figures were estimated or
invented; blanks mean Amazon had not finalised that data at run time._

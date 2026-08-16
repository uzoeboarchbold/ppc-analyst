# PPC 2-Day Report — 13–14 Aug 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products)
**Dates covered:** 13 Aug 2026 and 14 Aug 2026 (2 full days)
**Run:** 16 Aug 2026 23:04 UTC (data ends 48h before run, per Amazon's reporting lag)
**Compared against:** No previous 2-day report exists — this is the first/baseline report.

> **Setup note (fixed automatically):** The `AMZ_PROFILE_ID` environment
> variable does not contain a valid Amazon profile ID (it holds a 50-character
> "amzn…" string, not a numeric ID). I looked up the account's profiles and
> used the active **US** profile (`26765323558215`) — the only marketplace with
> a real daily budget set. Please correct `AMZ_PROFILE_ID` to `26765323558215`
> so future runs don't have to guess. Data pulled successfully.

---

## Part A — Data table (per campaign)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Isolated — Pet Odor Eliminator (Phrase) | 7 | 14% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Home+Eliminator+Brand Root — Exact | 27 | 5% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Home+Eliminator+Brand Root — Phrase | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP PT Pet Odor Eliminator | 16 | 1% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 1 | 0% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Tunnel Bed Pink — Exact Ranking (Louise) | 21 | 0% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **72** | **~3%*** | **0** | **0%** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

\* Total Top-of-search impression share is an impressions-weighted approximation.
CPC, ACOS and ROAS are undefined because there was no spend and no sales.

---

## Part B — Summary (plain English)

**The short version: your ads barely ran, and nothing was spent or sold.**

- **Spend:** $0.00 over the two days.
- **Sales:** $0.00.
- **ACOS / ROAS:** Not applicable — you can't have an advertising cost of sale or
  a return on ad spend when there was no spend and no sales.
- **Impressions:** Just 72 in total across all six campaigns — roughly 36 a day.
  That is extremely low. For context, a healthy campaign usually shows thousands
  of impressions a day.
- **Clicks:** Zero. With only 72 impressions, no shopper clicked an ad.

**Best campaign:** None stood out — nothing spent or sold. The most *visible*
was the "Home + Eliminator + Brand Root — Exact" campaign (27 impressions, 5%
top-of-search share), but even that got no clicks.

**Worst campaign:** Also hard to name a worst, since none cost anything. The
"Home + Eliminator + Brand Root — Phrase" campaign got 0 impressions, meaning it
showed to no one at all.

**Wasted spend (negatives to add):** None — there was no spend to waste, so
there are no wasteful search terms to add as negatives this period.

**Well-converting search terms to add as exact-match:** None — the search-term
report came back empty (no clicks means no search-term data), so there is
nothing to promote to exact match this period.

**Why this is happening (most likely):** 72 impressions in two days almost always
means the ads are not really "in the auction." The usual causes are:
1. **Bids too low** to win placements, or
2. **Budgets exhausted/very low** (the account's daily budget is set to $40, but
   spend is $0 — so budget isn't the cap; bids or eligibility likely are), or
3. **Campaigns paused, out of budget window, or ineligible** (e.g. listing/buy-box
   issues), or
4. A genuinely quiet two days for these niches.

### What to do next
1. **Check the campaigns are actually enabled and eligible** (status, and that the
   advertised ASINs hold the Buy Box). Zero impressions on the "Phrase" brand-root
   campaign is the biggest red flag.
2. **Raise bids** on the keyword campaigns. Winning almost no top-of-search share
   (1–14%) with 0 clicks points to bids being under the market clearing price.
3. **Fix `AMZ_PROFILE_ID`** to `26765323558215` (see setup note above).
4. **Re-check in the next report** — if impressions stay near zero, the issue is
   eligibility/bidding, not demand.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first one,
so it serves as the baseline. Headline figures to carry forward:

| Metric | This report | Change vs previous |
|---|---:|---|
| Impressions | 72 | — (baseline) |
| Clicks | 0 | — (baseline) |
| Spend | $0.00 | — (baseline) |
| Sales | $0.00 | — (baseline) |
| ACOS | n/a | — (baseline) |
| ROAS | n/a | — (baseline) |

**Verdict:** Baseline established. The next 2-day report will compare against these
numbers. Right now the standout issue is near-zero ad delivery, not efficiency.

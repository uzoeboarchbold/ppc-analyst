# PPC 2-Day Report — 24–25 October 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, USD) · Sponsored Products
**Report window:** Mon 24 Oct 2026 – Tue 25 Oct 2026 (2 full days)
**Generated:** 28 Oct 2026 (Amazon data finalises ~48h after the fact, so the window ends 48h before the run)
**Compared against:** previous 2-day report — none found; this is the first report (baseline)

---

## ⚠️ Read this first

**The ads are switched on but delivering nothing.** All 15 enabled Sponsored
Products campaigns recorded **zero impressions, zero clicks, zero spend and
zero sales** across the 2-day window. This is not a data error — the Amazon
Ads API connected fine and returned the data cleanly. I checked a wider
31-day window (25 Sep – 25 Oct) as a sanity test and it is **also entirely
zero**, so the campaigns have effectively not served at all for at least a
month.

When enabled campaigns with live budgets get **zero** impressions for weeks,
the cause is almost never the bids alone — it is usually that the product
itself is not eligible to advertise. The most likely reasons, in order:

1. **The listing is out of stock / not in the Buy Box** — Sponsored Products
   ads stop serving the moment the ASIN loses the Buy Box or runs out of
   inventory. This is the single most common cause of "enabled but zero".
2. **The listing is suppressed or inactive** (search-suppressed, a policy
   flag, or a pricing error flag).
3. **Bids far below the current market floor** — possible, but on its own it
   would still produce the odd impression over a month, not a flat zero.
4. **A billing / payment-method problem** pausing delivery account-wide.

**A quick stock + Buy Box check on ASIN B0FXW3GW5F will most likely explain
all of it.**

> Note on setup: the `AMZ_PROFILE_ID` environment variable is misconfigured
> (it holds an `amzn1.…` account identifier, not the numeric advertising
> profile the API needs). I identified the correct profile automatically and
> reported on the active US Sponsored Products account. See the "what to do
> next" section. No numbers were invented.

---

## Part A — Data table (24–25 Oct 2026)

All figures are for the 2-day window. Every enabled campaign served **0**
impressions, so all derived metrics are zero / not applicable.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto — B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10–25k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1–10k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10–25k SV (Exact) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT — ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP — Cat Tunnel Bed Pink (Exact Ranking) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 enabled campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*Also in the account but not serving: 32 paused and 7 archived campaigns.
Combined daily budget across the 15 enabled campaigns is ~$23.50/day — none
of which was spent.*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS:** n/a (no spend) · **ROAS:** n/a (no spend)
- **Best campaign / worst campaign:** none — nothing ran, so there is no
  winner or loser to point at.
- **Wasted spend / negatives to add:** none — but the real waste here is
  *opportunity*: 15 campaigns are switched on with ~$23.50/day of budget
  available and spent $0. The money isn't being wasted, the sales are.
- **Well-converting search terms to add as exact-match:** none available —
  there is no click or search-term data because nothing served.

**What this means:** the account is not losing money, but it is not making
any PPC sales either. For an FBA product that relies on ads for visibility,
a month of zero ad delivery usually means the product has stopped showing to
shoppers entirely (most often an out-of-stock or Buy Box issue). That is
worth checking today.

### What to do next (priority order)

1. **Check ASIN B0FXW3GW5F in Seller Central now:** Is it in stock? Does it
   hold the Buy Box? Is the listing active (not search-suppressed or
   pricing-flagged)? This is the most likely single cause.
2. **Check the Ads account billing / payment method** is valid and not
   declined (a declined card pauses all delivery).
3. **If stock and listing are healthy,** the enabled campaigns' bids are
   probably below the auction floor — raise default bids on the top 2–3
   campaigns to the suggested range and watch for impressions over 48h.
4. **Fix the reporting credential:** set `AMZ_PROFILE_ID` to the numeric US
   advertising profile `26765323558215` so future runs are unambiguous.
   (This run worked around it automatically.)
5. Once ads are serving again, the next report will have real numbers to
   optimise — negatives, exact-match harvesting and ACOS targets.

---

## Part C — Comparison to previous 2-day report

No previous 2-day report exists in the repository — **this is the first run,
so it serves as the baseline.** From the next 2-day report onward this
section will show the change in each headline metric (spend, sales, ACOS,
ROAS, impressions, clicks) as a number and a percentage.

For reference, the baseline headline figures are:

| Metric | This report (24–25 Oct) |
|---|--:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| Purchases | 0 |
| ACOS | n/a |
| ROAS | n/a |

**Direction:** n/a for a baseline. The headline to carry forward: delivery
is at zero and needs to be restored before optimisation can begin.

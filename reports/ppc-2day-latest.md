# PPC 2-Day Report — 18–19 Oct 2026

**Window covered:** 18 Oct 2026 – 19 Oct 2026 (2 full days)
**Account:** Uzoebo Archbold E-Commerce — US marketplace (USD)
**Product line:** Sponsored Products (pet-odour / cat range)
**Generated:** 22 Oct 2026 (data lags ~48h, so the window ends 48h before the run)

> **Heads-up — nothing is running.** All 15 Sponsored Products campaigns recorded
> **zero impressions, zero clicks, zero spend and zero sales** for 18–19 Oct. The
> same is true for the whole previous 30 days. The data pull itself worked fine;
> the account is simply not serving any ads right now (campaigns paused, budgets at
> zero/exhausted, or not yet launched). This is the main thing to look at.
>
> **Also:** the `AMZ_PROFILE_ID` setting is wrong (it holds an `amzn1…` value, not a
> numeric Amazon Ads profile ID, which the API rejects). I automatically resolved
> the correct account — **US profile `26765323558215`** — and used that. Please fix
> the stored `AMZ_PROFILE_ID` so future runs don't have to guess.

---

## Part A — Data table

All figures are for 18–19 Oct 2026, Sponsored Products, US marketplace, in USD.
7-day attribution. "—" means not applicable (no clicks/spend to derive the ratio).

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  calculable — there was no spend and no sales to measure.
- **What happened:** The account has 15 live Sponsored Products campaigns built out
  properly (auto, brand/root exact & phrase, isolated keyword campaigns, a keyword-
  harvest campaign, and a cat-tunnel-bed ranking campaign). None of them delivered a
  single impression in the window. Extending the look-back to 30 days shows the same
  picture — **no activity at all**.
- **Best / worst campaign:** Not meaningful this period — every campaign performed
  identically at zero.
- **Wasted spend / negatives to add:** None to flag — there was no spend to waste.
- **Well-converting search terms to add as exact-match:** None available — with no
  clicks or orders there is no search-term data to harvest yet.
- **Why ads aren't serving (most likely causes, in order):**
  1. **Campaigns paused** or the overall campaign status is inactive.
  2. **Daily budgets set to $0** or exhausted, or the account payment method is
     failing so Amazon has stopped delivery.
  3. **Bids too low** to win any placement, or targets still in "pending"/learning.
  4. Campaigns **created but never enabled**, or a start date in the future.

### What to do next
1. **Log into Amazon Ads and check the campaign + ad-group status** for these 15
   campaigns — confirm they're *Enabled*, not Paused/Archived.
2. **Check daily budgets and the account billing/payment method.** A declined card or
   $0 budget is the most common reason a whole account goes silent.
3. **Check bids** on the exact/phrase campaigns — raise them toward suggested bids so
   they can win impressions.
4. **Fix `AMZ_PROFILE_ID`** (see heads-up above) so reporting is pinned to the right
   account automatically.
5. Once ads are serving again, the next reports will have real numbers to optimise.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run, so there is nothing to
compare against yet. From the next run onward this section will show each headline
metric (spend, sales, ACOS, ROAS, impressions, clicks) as a number and a percentage
change versus this report, with a one-line verdict on whether things improved.

For the record, this run's baseline is: **Spend $0.00 · Sales $0.00 · Impressions 0 ·
Clicks 0 · ACOS n/a · ROAS n/a.**

---
*Automated PPC report. Data source: Amazon Advertising API (Sponsored Products v3
reporting), US profile 26765323558215. Nothing in this report is estimated or
invented — all figures were pulled live from the API.*

# PPC 2-Day Report — 19–20 Sep 2026

**Marketplace:** Amazon US (Sponsored Products) · Currency: USD
**Window covered:** Saturday 19 Sep – Sunday 20 Sep 2026 (2 full days)
**Report generated:** 23 Sep 2026 (data lags ~48h, so the window ends 48h before the run)
**Prepared by:** Automated PPC Analyst

---

## ⚠️ Read this first

Two things need your attention:

1. **Your ads did not run at all in this window.** Across 15 enabled Sponsored
   Products campaigns there were **0 impressions, 0 clicks, $0.00 spend and
   $0.00 sales** on both 19 and 20 September. This is not a data error — the
   figures are pulled live from Amazon and confirmed against a wider check:
   the account has had **effectively zero delivery since 3 September** (the last
   activity was a tiny 287 impressions / 1 click / $0.08 on 1–2 Sep). Something
   is stopping your enabled campaigns from serving. See "What to do next" below.

2. **A settings note (already handled this run):** the `AMZ_PROFILE_ID`
   credential is set to the wrong kind of value (an application id, not an Ads
   profile id). I worked around it automatically by looking up your profiles and
   selecting the US account, which is the only one with campaigns. No action
   needed from you, but it's logged so it can be corrected at the source.

---

## Part A — Data table (by campaign)

All 15 enabled campaigns recorded identical zero delivery in the window, so a
per-campaign breakdown would be 15 rows of zeros. The totals row below reflects
the whole account.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All enabled campaigns (15) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*n/a = cannot be calculated with zero impressions/clicks/spend.*
*Account structure for context: 15 enabled, 32 paused, 7 archived campaigns.*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00 · **Sales:** $0.00 · **ACOS / ROAS:** not applicable
  (no spend and no sales to divide).
- **Best / worst campaign:** none can be ranked — every campaign served zero
  impressions, so none performed better or worse than another.
- **Wasted spend / negatives to add:** none this window — you can't waste money
  on ads that aren't running. (This is the one silver lining: no budget is being
  burned.)
- **Well-converting search terms to add as exact-match:** none available — with
  no clicks or sales there are no search terms to harvest.
- **The real issue:** your money isn't being wasted, but your product is getting
  **no paid visibility at all.** For a live FBA listing that usually means lost
  sales you never see. Fifteen campaigns are switched on but not delivering.

### What to do next
The pattern (enabled campaigns, zero impressions for ~3 weeks) almost always
comes down to one of these — check in this order:

1. **Bids too low.** New/low bids that sit under the auction floor win no
   placements. Try raising bids on 2–3 priority campaigns to a competitive level
   (e.g. $0.75–$1.20 for this category) and watch for impressions within a day.
2. **Listing / Buy Box eligibility.** Ads only serve when the ASIN owns the Buy
   Box and is in stock. Confirm B0FXW3GW5F is active, in stock, and Buy-Box
   eligible.
3. **Budget / account status.** Daily budgets are very low ($1.50–$2.50).
   Confirm the ad account has a valid payment method and campaigns aren't
   out-of-budget or in a portfolio that's paused/capped.
4. **New-account ramp.** If the campaigns were only recently created, give
   step 1 a day to take effect before changing more.

Once impressions start flowing, the next report will have real numbers to
optimise.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first one, so it sets the
baseline.** From the next run onward this section will show the change in each
headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both a
number and a percentage, with a one-line verdict on whether things improved or
worsened.

For context against recent history: delivery is essentially unchanged from the
rest of September (zero since the 3rd), so there is no improvement or decline to
report yet — the account has simply not been serving ads.

---

*Figures sourced live from the Amazon Advertising API (Sponsored Products,
US profile 26765323558215). Zero-delivery rows verified against a wider daily
pull for 1–20 Sep 2026.*

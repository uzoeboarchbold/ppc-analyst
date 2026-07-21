# PPC 2-Day Report — 17–18 July 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Window covered:** 17 July 2026 – 18 July 2026 (2 full days)
**Generated:** 21 July 2026 (data ends 48h before run, per Amazon's ~48h finalisation lag)
**Attribution:** 7-day click attribution

---

## Please read first — two things need your attention

1. **Configuration fix applied automatically.** The `AMZ_PROFILE_ID` credential
   was set to an *application* ID, not a valid Amazon Advertising profile ID, so
   reporting calls were being rejected. The login itself worked, so I looked up
   your profiles and used your **US** seller profile (ID `26765323558215`). You
   also have **Canada** and **Mexico** profiles under the same account — say the
   word and I'll include them. **To remove this workaround, update
   `AMZ_PROFILE_ID` to `26765323558215`.**

2. **Your ads are not running.** Both Sponsored Products campaigns are switched
   **ON (Enabled)** but delivered **zero impressions** on 17–18 July — and, on a
   wider check, **zero impressions for the last 30 days**. No one is seeing these
   ads, so there was no spend and no sales to report. This is the headline of the
   report and the thing to fix first (details below).

---

## Part A — Data table

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP PT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*"—" = not applicable: with zero impressions/clicks/spend there is nothing to
divide. Campaign IDs: SP KT = 51177386692133, SP PT = 258847863221155. "KT" =
keyword-targeting, "PT" = product-targeting.*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  applicable — nothing was spent or sold.
- **Best / worst campaign:** neither campaign delivered, so there is no better or
  worse performer to name. Both are effectively idle.
- **Wasted spend / negatives to add:** none — you can't waste money on ads that
  aren't showing. No negative keywords are needed right now.
- **Search terms to add as exact-match:** none available. Because the ads got no
  impressions, there are no customer search terms to harvest yet.
- **The real issue:** both campaigns are *Enabled* but got **no impressions at all**,
  not just for these two days but for the whole past month. That means Amazon is
  not entering your ads into any auctions. Common reasons, roughly in order of
  likelihood:
  1. **Bids too low** to win any placement — raise the default bid so you start
     winning some auctions.
  2. **Daily budget set to $0 (or effectively nil)** — confirm each campaign has a
     real daily budget.
  3. **No products / ASINs attached**, or the ad group has no active product ads.
  4. **The listings aren't buyable** — out of stock, not in the Buy Box, price/
     suppression issues, or the product is inactive. Ads won't serve for ASINs
     that can't be bought.

### What to do next
1. Open each campaign in Seller Central → Campaign Manager and check, in this
   order: **daily budget > $0**, **bid** (raise it), **products are added and
   active**, and **the listings are in stock and winning the Buy Box**.
2. Fix whichever of the above is blocking delivery. In most "enabled but zero
   impressions for weeks" cases it is bids too low, no budget, or unbuyable
   listings.
3. Please also correct the `AMZ_PROFILE_ID` credential to `26765323558215` so
   future runs don't need the workaround.
4. Once the ads start serving, the next report will have real numbers and I can
   begin the usual work: flag wasted spend, suggest negatives, and harvest good
   search terms as exact-match.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** — this is the first one, so it sets the
baseline. Headline metrics for the record:

| Metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Overall:** No trend can be judged yet. The one clear signal is that the
account has had no ad delivery for the past 30 days, so the priority is simply
to get the campaigns serving. Next 2-day report will compare against this one.

---

*Prepared automatically by the PPC Analyst routine. Data source: Amazon Ads API
(Sponsored Products, v3 reporting). No figures were estimated or invented; every
number above is a direct read from the API for the stated window.*

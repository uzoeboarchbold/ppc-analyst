# PPC 2-Day Report — November 23–24, 2026

**Report window:** 2026-11-23 to 2026-11-24 (2 full days, Sponsored Products)
**Generated:** 2026-11-27 (data ends 48h before run, as Amazon finalises data on a ~48h lag)
**Account used:** US seller profile `26765323558215` (see note below)

---

## ⚠️ Read this first — two problems this run hit

**1. The configured profile ID is invalid.** The `AMZ_PROFILE_ID` setting is a ~50-character
string, but real Amazon profile IDs are short numbers (13–16 digits). It matches no account, so
it cannot be used. The login credentials themselves are fine. I looked up the real profiles on
the account and found three North American seller profiles: **US, Canada, Mexico**. Only the
**US** profile has any campaigns, so I used that as the best available stand-in. **Please fix
`AMZ_PROFILE_ID`** so future runs target the intended account with certainty.

**2. The account shows no advertising activity at all.** The US account has 50 Sponsored
Products campaigns (about 15 switched on) for your cat-deterrent / pet-odor product
(ASIN B0FXW3GW5F). But for the report window — and for every other period I checked (the last
two weeks, and all of October) — every campaign reports **zero impressions, zero clicks, zero
spend and zero sales**. This is not a data-lag or date issue; the ads simply are not being shown.

I did **not** invent any numbers. The zeros below are the real figures the API returned.

**Other note:** if your live, spending account is actually in Europe or the Far East, I can't
reach it from here — those Amazon regions are blocked by this environment's network policy. Only
the North America region is reachable.

---

## Part A — Data table (by campaign)

Because no campaign served a single impression in the window, there is nothing to tabulate per
campaign beyond zeros. The account total for 23–24 Nov:

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All enabled campaigns (15) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

The 15 enabled campaigns (all ASIN B0FXW3GW5F, budgets $1.50–$2.50/day), each with 0 activity:

- SP Auto 6K-PZMX-MTDZ B0FXW3GW5F
- SP Cat Root 1-10k SV … Exact
- SP Home + Eliminator + Brand Root 10-25k SV … Exact
- SP Isolated … Cat Deterrent Exact / Phrase
- SP Isolated … Cat Deterrent Spray Exact / Phrase
- SP Isolated … Pet Odor Eliminator Exact / Phrase
- SP KT | ST w/ Sales
- SP Litter + Urine Root 10-25k SV … Exact
- SP Odor Root 25-50k SV … Exact / Phrase
- SP Odor Root 50k+ SV … Exact
- SP | Cat Tunnel Bed Pink Only | Exact Ranking | Louise

---

## Part B — Plain-English summary

- **Spend:** $0.00. **Sales:** $0.00. **ACOS / ROAS:** not applicable (no spend, no sales).
- **Best / worst campaign:** none stands out — every campaign is flat at zero.
- **Wasted spend / negatives to add:** none — there is no spend to trim and no search-term data.
- **Well-converting terms to add as exact match:** none available — no search-term data was returned.
- **Bottom line:** the campaigns are switched on but Amazon is not showing them to anyone, so
  they are neither costing nor earning anything. The job right now is not optimisation — it's
  getting the ads to actually run.

## What to do next (priority order)

1. **Fix `AMZ_PROFILE_ID`** to the correct account's profile id (the US seller profile is
   `26765323558215`). This removes the guesswork from every future run.
2. **Find out why nothing is serving.** Most likely one of: (a) bids set too low to win any
   auction, (b) the product is out of stock or has lost the Buy Box (ads pause automatically),
   or (c) a billing/payment hold on the account. Check these in Seller Central / the Ads console.
3. **If your real spending account is in the EU or Far East**, tell me — this environment can
   only reach North America, and we'll need the network policy updated to include that region.
4. Once ads are serving and spending, this report will automatically start showing real
   impressions, clicks, spend, sales, ACOS and ROAS, plus negative-keyword and exact-match
   suggestions.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run, so there is nothing to compare
against yet. From the next run onward this section will show the change in each headline metric
(spend, sales, ACOS, ROAS, impressions, clicks) as both a number and a percentage.

| Metric | This report | Previous | Change |
|---|---:|---:|---|
| Impressions | 0 | — | n/a (first run) |
| Clicks | 0 | — | n/a |
| Spend | $0.00 | — | n/a |
| Sales | $0.00 | — | n/a |
| ACOS | — | — | n/a |
| ROAS | — | — | n/a |

---

*Prepared automatically by the PPC Analyst routine. Figures are pulled live from the Amazon
Advertising API; where data could not be obtained, that is stated plainly rather than estimated.*

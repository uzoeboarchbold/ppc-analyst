# PPC 2-Day Report — Sep 29–30, 2026

**Marketplace:** Amazon US (USD) · Sponsored Products
**Dates covered:** 2026-09-29 to 2026-09-30 (2 full days, finalised — data lags ~48h)
**Report generated:** 2026-10-03
**Report type:** 2-day

> **Heads-up (config):** The `AMZ_PROFILE_ID` environment variable is set to an *application id*
> (`amzn1.application.…`), not a numeric Advertising profile id, so it can't be used as-is. I auto-detected
> the account's live profile and used the **US seller profile (`26765323558215`)**, which is the only one with
> campaigns (the CA and MX profiles have none). **Fix:** set `AMZ_PROFILE_ID=26765323558215`.

> **Main finding:** All 15 enabled campaigns served **nothing** in this window — 0 impressions, 0 clicks,
> 0 spend, 0 sales — and the same is true for all of September. The ads are *enabled* but *not delivering*.
> This is almost certainly a delivery problem, not a performance one (see "What to do next").

---

## Part A — Data table (per campaign)

All figures Amazon US, USD. "–" means not applicable because there was no activity to compute a rate from.

| Campaign | Impr. | ToS impr. share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Cat Root 1-10k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP KT \| ST w/ Sales | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 50k+ SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| **TOTAL (15 enabled campaigns)** | **0** | **–** | **0** | **–** | **0** | **$0.00** | **$0.00** | **–** | **–** | **–** |

*Only the 15 ENABLED campaigns are shown. The account also holds 32 paused and 7 archived campaigns, which are
not running and are excluded. Keyword/target and search-term reports were also pulled and were likewise empty
(no served targets, no search terms) for this window.*

---

## Part B — Plain-English summary

**The short version:** Over Sep 29–30 your Amazon US ads spent **$0.00** and made **$0.00 in ad sales**.
That isn't because the campaigns are turned off — 15 of them are switched **on** — it's because they didn't
show to a single shopper. Zero impressions means Amazon never displayed your ads, so ACOS and ROAS can't be
calculated (there's nothing to divide).

**Best / worst campaigns:** Not meaningful this period — every campaign delivered identical zero results, so
none out- or under-performed another.

**Wasted spend / negatives to add:** None to flag. You can't waste money on clicks that never happened, and
there are no search terms to prune because none were triggered.

**Winning search terms to add as exact-match:** None available — no search terms were recorded, because the
ads never served.

**Why this matters more than a normal slow week:** Ads that are *enabled but not serving* usually point to a
problem upstream of the ad itself. The most common causes, roughly in order of likelihood:

1. **The product isn't in the Buy Box / is out of stock / the listing is suppressed.** Sponsored Products
   ads can only run when the product is buyable. If ASIN **B0FXW3GW5F** (and the Cat Tunnel Bed) lost the Buy
   Box, went out of stock, or the listing was suppressed, every campaign stops serving at once — exactly what
   we see here.
2. **Bids are too low to win any auction.** Daily budgets are small ($1.50–$2.50) and if default bids are
   below the market floor, the ads simply never place.
3. **A billing / payment issue** paused delivery account-wide.
4. **Campaigns were only just created** and haven't started — unlikely here, since they already show zero
   across all of September.

**What to do next (in order):**
1. **Check the listing(s) first.** In Seller Central, confirm ASIN B0FXW3GW5F and the Cat Tunnel Bed are
   in stock, winning the Buy Box, and not suppressed. This is the #1 suspect and the fastest to verify.
2. **Confirm the ad account is in good standing** (payment method valid, no account-level suppression).
3. **Check bids vs. suggested bids** on the enabled campaigns; raise toward Amazon's suggested range if they're
   below the floor, and consider lifting the $1.50 daily budgets once ads are actually serving.
4. **Fix `AMZ_PROFILE_ID`** to `26765323558215` so future automated runs don't have to auto-detect the profile.
5. Re-check in the next 2-day run; once impressions return, we'll have real performance to optimise.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first report of this type, so it establishes the baseline.
There is nothing to compare against yet.

For reference, the baseline set here is:

| Metric | This report (Sep 29–30) |
|---|---|
| Total spend | $0.00 |
| Total sales | $0.00 |
| ACOS | n/a (no spend) |
| ROAS | n/a (no spend) |
| Impressions | 0 |
| Clicks | 0 |
| Purchases | 0 |

Next 2-day run will compare against these figures and report the change as a number and a percentage.

---

*Data source: Amazon Advertising API (Sponsored Products, reporting v3, 7-day attribution). Figures are final
for the window (48h+ old). Generated automatically by the PPC Analyst routine.*

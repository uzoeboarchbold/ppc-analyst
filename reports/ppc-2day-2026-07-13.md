# PPC 2-Day Report — 9–10 July 2026

**Marketplace:** Amazon US (Sponsored Products) · Account: Uzoebo Archbold E-Commerce
**Window covered:** 2026-07-09 to 2026-07-10 (2 full days, ending 48h before the run to allow Amazon's data to finalise)
**Report generated:** 2026-07-13

---

## ⚠️ Read this first — your Sponsored Products ads are not running

The data pulled cleanly from the Amazon Ads API, and the numbers are real. The
headline is not a numbers story, it's a **status** story:

- **Only 2 of your 54 Sponsored Products campaigns are switched on.** The other
  52 are Paused or Archived.
- **Even the 2 "on" campaigns served 0 impressions** — not just in these 2 days,
  but across the **entire last 30 days**. They are enabled but showing to nobody.
- Result: **£0 / $0 spend, $0 sales, no clicks, no impressions** for the window.

In plain English: your Sponsored Products advertising is effectively switched
off. You are not wasting money — but you are also getting no ad-driven sales.

*(Note: a data-source detail was fixed automatically this run — the
`AMZ_PROFILE_ID` setting held the wrong kind of ID, so the correct US ad
profile was located and used. See "Setup note" at the bottom. This did not
affect the accuracy of the figures.)*

---

## Part A — Data table (per campaign)

Window: 2026-07-09 → 2026-07-10. Only campaigns that are enabled/delivering are
shown by the reporting API; both returned all zeros.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales (ENABLED, $8/day) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales (ENABLED, $8/day) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*n/a = cannot be calculated because there were no impressions/clicks/spend.*

No keyword/target rows and no search-term rows were returned, which is expected
when there are zero impressions — nothing served, so nothing to break down.

---

## Part B — Summary in plain English

**Overall for 9–10 July:** Spend $0.00 · Sales $0.00 · ACOS n/a · ROAS n/a.
There was no advertising activity to measure.

**Best / worst campaign:** Not applicable — neither active campaign delivered any
impressions, so there is no better or worse performer to name.

**Wasted spend / negatives to add:** None — you can't waste spend when nothing is
running. No negative keywords are needed this cycle.

**Search terms to add as exact-match:** None available — with zero impressions
there are no converting search terms to harvest yet.

**Why are the two "on" campaigns getting 0 impressions?** They are enabled with an
$8/day budget each (started 9 June 2026) but have shown to nobody for 30+ days.
The usual causes, in order of likelihood:
1. **Bids too low** to win any auction — the most common reason an enabled
   campaign gets no impressions.
2. **Everything inside is paused** — the ad group, the product ads (ASINs), or
   the keywords/targets may be paused even though the campaign is "enabled".
3. **The product isn't buyable** — out of stock, lost Buy Box, or the listing is
   suppressed/inactive, which stops ads from serving.
4. Campaign not yet approved / in a review state.

### What to do next
1. **Decide if you want to advertise at all right now.** If yes, the two enabled
   campaigns need attention; if no, this report will keep reading "all zeros".
2. **Open "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales"** in Campaign Manager
   and check, top to bottom: ad group state, product-ad (ASIN) state, and
   keyword/target state — make sure none are paused.
3. **Check the bids.** If they're at the floor, raise them toward Amazon's
   suggested bid so the ads can win placements. Confirm the daily budget isn't
   the blocker (it isn't here — spend is $0, so budget is never being reached).
4. **Confirm the advertised ASIN is in stock and holds the Buy Box.** Ads don't
   serve without the Buy Box.
5. Once impressions start flowing, the next 2-day report will finally have real
   performance to analyse (ACOS, ROAS, wasted spend, search-term harvest).

---

## Part C — Comparison to the previous 2-day report

**No comparison available this run.** This is the **first 2-day report** produced
by the automation — there is no earlier 2-day report in the `reports` folder to
compare against. From the next run onward, this section will show the change in
each headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both a
number and a percentage.

For reference, the baseline recorded this run is:

| Metric | This report (9–10 Jul) |
|---|---:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| Orders | 0 |
| ACOS | n/a |
| ROAS | n/a |

---

## Setup note (automatic fixes this run)

- **Profile ID corrected:** the `AMZ_PROFILE_ID` environment variable contained an
  application ID (`amzn1.application…`), not a numeric ads-profile ID. The run
  automatically listed the account's profiles and used the **US** profile
  (`26765323558215`, "Uzoebo Archbold E-Commerce"), which is the primary FBA
  marketplace. CA and MX profiles also exist but were not reported on.
- **Delivery note:** this report was saved to the repo and uploaded to the Google
  Drive "PPC Reports" folder. Automated **email could not be sent** — no email/Gmail
  connector is available in this environment. The owner was alerted via push
  notification instead. (Logged to notes-to-self.md so it can be set up.)

*Data source: Amazon Advertising API v3 reporting (spCampaigns / spTargeting /
spSearchTerm), Sponsored Products, US marketplace.*

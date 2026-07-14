# PPC 2-Day Report — 10–11 July 2026

**Marketplace:** Amazon US (Sponsored Products) · Account: Uzoebo Archbold E-Commerce
**Window covered:** 2026-07-10 to 2026-07-11 (2 full days, ended 48h before the run so Amazon's data is finalised)
**Report generated:** 2026-07-14

---

## ⚠️ Read this first — your Sponsored Products ads are still not running

The data pulled from the Amazon Ads API is real, and the headline is the same
as the last report: this is a **status** problem, not a numbers problem.

- **Only 2 of your 54 Sponsored Products campaigns are switched on.** The other
  52 are Paused (45) or Archived (7).
- **The 2 "on" campaigns served 0 impressions again** in this window — as they
  have every day since they were enabled on 9 June 2026. They are enabled but
  showing to nobody.
- Result for 10–11 July: **$0.00 spend, $0.00 sales, 0 clicks, 0 impressions.**

In plain English: your Sponsored Products advertising is effectively switched
off, and has been for roughly **five weeks**. You are not wasting money — but
you are also getting zero ad-driven sales, and this is now the second 2-day
report in a row reading all zeros.

*(Data-source note: the `AMZ_PROFILE_ID` setting still holds the wrong kind of
ID, so the correct US ad profile was located and used automatically again — see
"Setup note" at the bottom. This did not affect accuracy.)*

---

## Part A — Data table (per campaign)

Window: 2026-07-10 → 2026-07-11. Both enabled campaigns returned zeros; the
paused/archived campaigns cannot serve and are not shown.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales (ENABLED, $8/day) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales (ENABLED, $8/day) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*n/a = cannot be calculated with no impressions/clicks/spend.*

No keyword/target rows and no search-term rows were returned — expected when
nothing served. (The keyword/target report completed and returned 0 rows,
confirming zero delivery for the window.)

---

## Part B — Summary in plain English

**Overall for 10–11 July:** Spend $0.00 · Sales $0.00 · ACOS n/a · ROAS n/a.
There was no advertising activity to measure.

**Best / worst campaign:** Not applicable — neither active campaign delivered
any impressions, so there is nothing to rank.

**Wasted spend / negatives to add:** None — you can't waste spend when nothing
is running. No negative keywords needed this cycle.

**Search terms to add as exact-match:** None available — with zero impressions
there are no converting search terms to harvest yet.

**Why the two "on" campaigns get 0 impressions** (enabled, $8/day each, live
since 9 June but shown to nobody for ~5 weeks). Most likely causes, in order:
1. **Bids too low** to win any auction — the most common reason an enabled
   campaign gets no impressions.
2. **Something inside is paused** — the ad group, the product ads (ASINs), or
   the keywords/targets may be paused even though the campaign is "enabled".
3. **The product isn't buyable** — out of stock, lost Buy Box, or a
   suppressed/inactive listing stops ads from serving.
4. Campaign stuck in a review/approval state.

### What to do next
1. **Decide whether you want to advertise right now.** If yes, the two enabled
   campaigns need hands-on attention; if no, every future report will keep
   reading all zeros.
2. **Open "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales"** in Campaign Manager
   and check top-to-bottom: ad group state → product-ad (ASIN) state →
   keyword/target state. Make sure none are paused.
3. **Check the bids.** If they are at the floor, raise them toward Amazon's
   suggested bid so the ads can win placements. Budget is not the blocker here
   (spend is $0, so the $8/day is never reached).
4. **Confirm the advertised ASIN is in stock and holds the Buy Box** — ads do
   not serve without the Buy Box.
5. Once impressions start flowing, the next report will finally have real
   performance to analyse (ACOS, ROAS, wasted spend, search-term harvest).

---

## Part C — Comparison to the previous 2-day report

Previous report: **9–10 July 2026** (generated 2026-07-13). Both reports cover
periods when the account was dark, so every headline metric is unchanged.

| Metric | Previous (9–10 Jul) | This report (10–11 Jul) | Change (number) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 0 | 0 | 0 | 0% |
| Clicks | 0 | 0 | 0 | 0% |
| Spend | $0.00 | $0.00 | $0.00 | 0% |
| Sales | $0.00 | $0.00 | $0.00 | 0% |
| Orders | 0 | 0 | 0 | 0% |
| ACOS | n/a | n/a | — | — |
| ROAS | n/a | n/a | — | — |

**Verdict: no change — and that is the problem.** This is the second 2-day
report in a row with zero delivery. Nothing has improved or worsened in the
numbers because the ads still are not serving; the account has now been
effectively unadvertised for ~5 weeks. The single action that would change the
next report is getting the two enabled campaigns to actually serve (see "What
to do next").

---

## Setup note (automatic fixes / issues this run)

- **Profile ID corrected (again):** the `AMZ_PROFILE_ID` environment variable
  contains an application ID (`amzn1.application…`), not a numeric ads-profile
  ID. The run listed the account's profiles and used the **US** profile
  (`26765323558215`), the only one with Sponsored Products campaigns. CA and MX
  profiles exist but have no campaigns. **Fix at source:** set `AMZ_PROFILE_ID`
  to `26765323558215` to remove this workaround.
- **Amazon report queue was slow this run:** the campaign-level and search-term
  async reports sat in `PENDING` well beyond normal. The keyword/target report
  for the same window completed and returned 0 rows, and both enabled campaigns
  independently confirm zero delivery, so the all-zeros result is certain
  regardless. Logged to notes-to-self.md.
- **Email not sent:** no email/Gmail connector is available in this
  environment, so the automated email step could not run. The report was saved
  to the repo and uploaded to the Google Drive "PPC Reports" folder, and the
  owner was alerted by push notification instead.

*Data source: Amazon Advertising API v3 reporting (spCampaigns / spTargeting /
spSearchTerm), Sponsored Products, US marketplace (profile 26765323558215).*

# PPC 2-Day Report — 3–4 July 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Amazon.com), Sponsored Products
**Dates covered:** Thursday 3 July 2026 and Friday 4 July 2026 (2 full days)
**Data pulled:** 7 July 2026 (data is ended 48h before run so Amazon figures are finalised)
**Currency:** USD

> **Setup note (plain English):** The `AMZ_PROFILE_ID` provided to this tool was
> not a valid account id (it was an application id), so I looked up the real
> accounts and used the **US** seller account, which is the one that has
> Sponsored Products campaigns. Canada and Mexico have no PPC campaigns. The data
> pulled cleanly from Amazon — nothing failed.
>
> **Delivery note:** This report is saved to the repo and uploaded to the Google
> Drive 'PPC Reports' folder. The automated **email could not be sent** because the
> Gmail connector is currently switched off for this automation — to receive these
> by email, enable the Gmail connector for this chat in connector settings.

---

## Part A — Data Table (one row per campaign)

| Campaign | Impressions | Top-of-search imp. share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales (keyword targeting) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales (product targeting) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

Both campaigns are **ENABLED** with an **$8.00/day** budget each. "n/a" appears
where a rate cannot be calculated because there were no impressions or clicks to
divide by.

---

## Part B — Summary (plain English)

**Headline:** Over these two days the account spent **$0.00** and made **$0.00**
in ad sales, because the two live campaigns received **no impressions at all** —
they were not shown to a single shopper. With no spend there is no ACOS or ROAS
to report.

**Best / worst campaign:** There is no best or worst — both campaigns performed
identically at zero. Neither is winning any ad placements.

**Is this a one-off?** No. I checked the previous two weeks as well
(21 June – 4 July) and both campaigns had **zero impressions the entire time**.
This is an ongoing "not serving" problem, not a slow couple of days.

**Wasted spend / negatives to add:** None — you can only waste money once ads are
actually showing, and right now they are not. No search-term data exists yet, so
there is nothing to add as negative keywords.

**Well-converting search terms to add as exact-match:** None available — with no
clicks or search-term traffic there is nothing to harvest yet.

**Why enabled campaigns show zero impressions — most likely causes (in order):**
1. **Bids are too low** to win any auction, so the ads never appear.
2. **Products aren't buyable** — out of stock, no Buy Box, or lost/suppressed
   listing means ads are automatically paused from serving.
3. **Campaigns are brand-new / just launched** and haven't started serving.
4. A **very narrow target or a start-date/portfolio setting** keeping them dark.

**What to do next (priority order):**
1. **Check the products are in stock and hold the Buy Box.** If a product isn't
   buyable, Amazon won't show its ads no matter the bid. Fix this first.
2. **Raise the bids.** Zero impressions on an enabled campaign almost always means
   the bid is below the auction floor. Try increasing default bids meaningfully
   (e.g. toward Amazon's suggested-bid range) and/or add a Top-of-Search placement
   bid adjustment.
3. **Confirm campaign start dates and that targets/keywords are enabled** (not just
   the campaign). An enabled campaign with paused targets still shows nothing.
4. **Re-check in the next report.** Once impressions appear we can start optimising
   for ACOS/ROAS, harvest converting search terms, and add negatives.

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists** — this is the first 2-day report, so there is
nothing to compare against yet. Headline metrics for the record (all zero this
period): Spend $0.00, Sales $0.00, ACOS n/a, ROAS n/a, Impressions 0, Clicks 0,
Purchases 0. The next 2-day report will compare against these figures.

*Improved or worsened?* Not applicable this run (no baseline). The key watch-item
carried forward: **campaigns enabled but serving zero impressions.**

---
*Generated automatically by the PPC Analyst routine. Data source: Amazon Ads API
(Sponsored Products, US profile 26765323558215).*

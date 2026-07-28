# PPC 2-Day Report — 2026-07-24 to 2026-07-25

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)  
**Window covered:** 2026-07-24 to 2026-07-25 (2 full days, ending 48h before the 2026-07-28 run)  
**Currency:** USD

> **Two operational notes for the account owner (read this):**
> 1. **Email was not sent automatically.** The Gmail connector is not enabled
>    for this scheduled chat, so no email tool was available. This report was
>    saved to the repo and uploaded to Google Drive → *PPC Reports* instead.
>    Please enable the Gmail connector for this chat to restore emailing.
> 2. **The `AMZ_PROFILE_ID` secret is misconfigured** — it holds an LWA
>    application id, not a numeric profile id. I worked around it by looking
>    up your profiles and using the US account (`26765323558215`). Please set
>    `AMZ_PROFILE_ID` to `26765323558215` so future runs are robust.

---

## Part A — Data Table (by campaign)

| Campaign | Impressions | Top-of-Search IS | Clicks | CTR | Purchases | Sales | Total Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP KT \| ST w/ Sales | 758 | 21.00% | 1 | 0.13% | 0 | $0.00 | $3.51 | $3.51 | n/a | 0.00 |
| SP PT \| ST w/ Sales | 17 | 12.00% | 1 | 5.88% | 0 | $0.00 | $0.36 | $0.36 | n/a | 0.00 |
| **TOTAL** | **775** | **—** | **2** | **0.26%** | **0** | **$0.00** | **$3.87** | **$1.93** | **n/a** | **0.00** |

*Only campaigns that served impressions in the window appear above. Of the
account's 54 Sponsored Products campaigns, only these 2 delivered any
impressions in this period.*

## Part B — Plain-English Summary

**Overall, this was a near-idle two days for the ads.** Across the whole
Sponsored Products account we spent **$3.87**, got **775**
impressions and **2 clicks**, and made **0 sales**. Because there
were no ad-attributed sales, ACOS is not applicable and ROAS is 0.00 — every
dollar spent (all $3.87 of it) came back as $0 in tracked sales
over these two days.

**The bigger story is missing volume, not bad efficiency.** An account with
54 campaigns serving only 775 impressions and 2 clicks in 48 hours means the
ads are barely being shown. The most likely causes are that the great
majority of campaigns are paused, or daily budgets/bids are set so low that
almost nothing serves. This is the thing to look at first — efficiency
metrics are meaningless at $3.87 of spend.

- **Best campaign:** *SP PT | ST w/ Sales* — tiny, but its 17 impressions
  produced a 5.88% CTR for just $0.36. Highest engagement rate of the two.
- **Worst / most wasted spend:** *SP KT | ST w/ Sales* — spent $3.51 (91% of
  all spend) for 1 click and 0 sales. Nearly all of it went to the exact
  keyword **"pet odor eliminator"** ($3.51, 204 impressions, 1 click, no
  sale). One clickless window is not proof it is a bad keyword, but it is the
  only real spend in the account and is worth watching.

**Wasted spend / suggested negatives:** Nothing yet rises to a confident
negative-keyword call — 1 click on "pet odor eliminator" is too little data to
condemn it. No search term burned meaningful spend without converting. **No
negatives recommended this window.**

**Well-converting search terms to add as exact:** **None.** Zero search terms
converted in this window (0 purchases across the account), so there is nothing
to harvest into exact-match yet.

### What to do next
1. **Check why delivery is so low.** Confirm how many of the 54 campaigns are
   actually enabled, and whether budgets/bids are throttling impressions. If
   you intend to be advertising, the priority is getting impressions flowing.
2. **Fix the two setup issues** in the notes at the top (enable Gmail for this
   chat; correct the `AMZ_PROFILE_ID` secret).
3. **Re-check in 2 days** once more volume accumulates — with real click and
   sales data the ACOS/ROAS and keyword harvesting advice becomes meaningful.

### Search-term detail (for reference)

| Search term | Campaign | Match | Impr | Clicks | Cost | Sales |
|---|---|---|--:|--:|--:|--:|
| pet odor eliminator | SP KT \| ST w/ Sales | EXACT | 62 | 1 | $3.51 | $0.00 |
| get cat pee out of couch | SP PT \| ST w/ Sales | TARGETING_EXPRESSION | 1 | 1 | $0.36 | $0.00 |

## Part C — Comparison to Previous 2-Day Report

**No comparison available: this is the first 2-day report, so there is no
prior report of this type to compare against.** A baseline is now saved
(`ppc-2day-latest.md`); the next 2-day run will show change vs. these numbers
for each headline metric (spend, sales, ACOS, ROAS, impressions, clicks, CTR).

For the record, the baseline headline figures are:

| Metric | Value |
|---|--:|
| Impressions | 775 |
| Clicks | 2 |
| CTR | 0.26% |
| Total cost | $3.87 |
| CPC | $1.93 |
| Purchases | 0 |
| Sales | $0.00 |
| ACOS | n/a |
| ROAS | 0.00 |

---
*Generated automatically on 2026-07-28. Data source: Amazon Ads API
(Sponsored Products, US profile 26765323558215). Attribution: 7-day.*
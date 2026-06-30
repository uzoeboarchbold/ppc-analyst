# PPC 2-Day Report — 26–27 June 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Window covered:** Friday 26 June – Saturday 27 June 2026 (2 full days)
**Report generated:** 30 June 2026 23:02 UTC (data ends 48h before run, as Amazon data finalises with a ~48h lag)
**Currency:** USD

> ⚠️ **Headline: the account is not advertising.** Over the 2-day window
> there were **zero impressions, zero clicks, zero spend and zero ad
> sales**. Only 2 of the 50 Sponsored Products campaigns are enabled, and
> neither served a single impression. The other 48 campaigns are paused.
> This is not a data error — a wider 14-day check (14–27 June) also shows
> zero activity. See "What to do next".

---

## Part A — Data Table (per campaign)

| Campaign | Status | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | Enabled | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP PT \| ST w/ Sales | Enabled | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*The 48 remaining campaigns are paused and served nothing; they are omitted
from the table. "—" means the metric cannot be calculated because there
were no impressions/clicks/spend.*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall ad sales:** $0.00. **ACOS / ROAS:**
  not applicable — you can't have an advertising cost-of-sale when nothing
  is being spent.
- **Best campaign / worst campaign:** none to pick — no campaign served any
  impressions, so there is no performance to rank.
- **Wasted spend / negatives to add:** none. There was no spend, so nothing
  to trim. (You can't waste money you aren't spending — but you also aren't
  making any ad-driven sales.)
- **Search terms to add as exact-match:** none available. With zero clicks
  there is no search-term data to harvest this period.
- **The real issue:** your two enabled campaigns ("SP KT | ST w/ Sales" and
  "SP PT | ST w/ Sales") are switched on but **not serving**. When an
  enabled campaign shows zero impressions for days, it is almost always one
  of these:
  1. **No / zero daily budget** on the campaign (or the account-level
     budget is exhausted or set to $0).
  2. **Bids too low** to win any placement.
  3. **No enabled keywords/targets** inside the campaign (nothing to bid
     on).
  4. **Product not buyable** — out of stock or you don't hold the Buy Box,
     so ads are suppressed.
  Until one of these is fixed, you are getting **no advertising traffic and
  no ad sales at all**.

### What to do next
1. **Log into Amazon Ads and open the two enabled campaigns.** Check the
   daily budget is above $0 and not capped, and that the account has a
   valid payment method (it does on file).
2. **Confirm each enabled campaign has active keywords/targets** with bids
   high enough to compete (start near Amazon's suggested bid).
3. **Check the product listing is in stock and holding the Buy Box** — ads
   won't show otherwise.
4. **Decide on the 48 paused campaigns.** If the plan is to run PPC, a
   couple of well-structured, properly-budgeted campaigns should be
   enabled. If the pause is intentional (e.g. stock conserved, off-season),
   no action — but then expect these reports to keep reading "$0".
5. If you *intended* to be live and spending, treat this as urgent: every
   day at zero impressions is a day of lost ad-driven sales.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run, so it serves as
the baseline.** Future 2-day reports will compare spend, sales, ACOS and
ROAS against these figures (currently all $0 / not-applicable). There is
nothing to show as an up/down change yet.

For context, the baseline to beat is simply: **get above zero.** The first
report that shows real impressions, clicks and sales will be the first
genuine comparison.

---

## Notes on data collection
- Pulled live from the Amazon Advertising API (v3 reporting) for the US
  profile, Sponsored Products, 26–27 June 2026. Campaign, targeting and
  search-term reports were all requested; targeting and search-term reports
  returned no rows (consistent with zero activity).
- One operational note: the `AMZ_PROFILE_ID` provided to this job is an
  *application* identifier, not the numeric advertising profile the API
  needs, so the run resolved the correct US profile automatically. No
  action needed from you — noted for the record.
- **Delivery:** this environment has no email-sending tool, so a true inbox
  email with a subject line could not be sent automatically. The report is
  saved in the repo and uploaded to the Google Drive folder "PPC Reports",
  and a summary is pushed to your phone/inbox via the routine notification.

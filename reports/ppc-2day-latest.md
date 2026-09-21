# PPC 2-Day Report — 18–19 September 2026

**Report type:** 2-day · **Dates covered:** 2026-09-18 to 2026-09-19 (2 full days)
**Marketplace:** Amazon US (USD) · **Generated:** 2026-09-21 23:19 UTC
**Source:** Amazon Ads API — Sponsored Products

> **Heads-up (please read): your ads delivered NOTHING in this window.**
> All 15 of your enabled Sponsored Products campaigns recorded **zero
> impressions, zero clicks and zero spend** on both 18 and 19 September. The
> data pull worked correctly — this is real, not a reporting error. For
> context, the *entire* last 30 days shows only **$2.60 total spend and $0 in
> sales**, almost all of it on one campaign ("Cat Tunnel Bed") and dated before
> 10 September. In short, the advertising account is effectively dormant. See
> "What to do next" below.
>
> **Config note for the record:** the `AMZ_PROFILE_ID` credential is set to an
> *application* ID rather than a numeric ads profile ID, so it can't be used as-is.
> I worked around it automatically by looking up your profiles and using the US
> account (`26765323558215`), which is where all your campaigns live. Fixing that
> env var to `26765323558215` would make future runs cleaner. (Logged in notes-to-self.md.)

---

## Part A — Data table (by campaign)

All enabled campaigns, 18–19 Sep 2026. Every metric is zero because no ads were
served. "TOS IS" = Top-of-search impression share.

| Campaign | Impr. | TOS IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Isolated … Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Auto … B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTALS** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(32 further campaigns are Paused and 7 Archived; none delivered either.)*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Sales:** $0.00. **ACOS / ROAS:** not applicable —
  there was no spend and no sales to measure.
- **Best campaign / worst campaign:** none stands out, because nothing ran.
  Every enabled campaign performed identically at zero.
- **Wasted spend / negatives to add:** none — you can't waste money you didn't
  spend. No negative keywords are warranted this period.
- **Well-converting search terms to add as exact-match:** none available — with
  no clicks or sales there is no search-term data to harvest.
- **The real story:** 15 campaigns are switched ON but Amazon served none of
  your ads. Over the last 30 days the account spent a total of $2.60 and made
  $0 in sales. Something is stopping your ads from showing.

### Most likely reasons your ads aren't showing
1. **Bids too low** to win any auctions (very common — raise bids/CPC).
2. **Daily budgets at or near $0**, or a campaign/portfolio budget cap hit.
3. **Campaign date ranges** ended, or start dates in the future.
4. **The product listing isn't eligible** — out of stock, lost Buy Box,
   suppressed listing, or missing a required attribute. Ads can't run if the
   product isn't buyable.
5. **Billing / payment method issue** on the Amazon Ads account.

### What to do next
1. Open Amazon Ads → Sponsored Products and check, for 2–3 enabled campaigns:
   **daily budget > $0**, **end date not passed**, and **bid** is reasonable
   (try $0.75–$1.50 to start on a cat/pet-odor niche).
2. In Seller Central, confirm the advertised product (ASIN **B0FXW3GW5F** and
   the Cat Tunnel Bed ASIN) is **in stock, winning the Buy Box, and not
   suppressed**. This is the #1 silent killer of delivery.
3. Check **Ads account billing** — a declined card pauses all delivery.
4. Once ads are actually running again, this report will have real numbers to
   analyse (wasted spend, negatives, winning search terms, etc.).
5. Fix the `AMZ_PROFILE_ID` env var to `26765323558215` so future automated
   runs don't have to guess the account.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run of this report type,**
so there is no prior period to compare against. Headline metrics are recorded
here as the new baseline:

| Metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Purchases | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** No trend yet. Baseline established at zero activity. The priority
isn't optimisation — it's getting the ads to deliver at all (see Part B).

---

*Prepared automatically by the PPC Analyst routine. Data: Amazon Ads API,
Sponsored Products, US marketplace. Window ends 48h before run to allow Amazon's
data to finalise.*

**Delivery status:** Saved to the repo and uploaded to Google Drive ("PPC
Reports" folder). Automatic **email could not be sent** this run — the Gmail
connector is connected to the account but not enabled for this automated
session, so no email tool was available. Please enable the Gmail connector for
this automation (or add SMTP credentials) to receive these by email in future.

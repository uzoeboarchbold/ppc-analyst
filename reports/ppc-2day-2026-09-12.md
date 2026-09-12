# PPC 2-Day Report — 8–9 Sep 2026

**Marketplace:** Amazon US (Sponsored Products), currency USD
**Dates covered:** Monday 8 Sep 2026 – Tuesday 9 Sep 2026 (2 full days)
**Report generated:** 12 Sep 2026 (data ends 48h before run, per Amazon's ~48h reporting lag)
**Account:** Uzoebo Archbold E-Commerce (US profile 26765323558215)

> **Read this first — ads effectively did not run.** Across all 15 Sponsored
> Products campaigns there were **0 impressions, 0 clicks, $0.00 spend and
> $0.00 sales** for 8–9 Sep. This is not a data error — the account is barely
> serving. Over the prior two weeks (27 Aug–9 Sep) the whole US account
> delivered only ~1,020 impressions, 4 clicks and $0.60 of spend, with **zero
> sales**. The most likely cause is a **billing/payment problem**: the US
> advertising profile reports `validPaymentMethod = false`, which stops Amazon
> from serving ads. Fix that first (see "What to do next").

> **Note on profile setup:** the `AMZ_PROFILE_ID` environment variable holds an
> *application* ID, not a numeric Ads profile ID, so it can't be used directly.
> The report was run against the correct US profile looked up from the account.
> No numbers were invented; everything below comes straight from the Amazon Ads
> API.

---

## Part A — Data table (per campaign, 8–9 Sep 2026)

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Cat Root 1-10k SV …B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Home + Eliminator + Brand Root 10-25k SV …Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated …B0FXW3GW5F Cat Deterrent Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated …B0FXW3GW5F Cat Deterrent Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated …B0FXW3GW5F Cat Deterrent Spray Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated …B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated …B0FXW3GW5F Pet Odor Eliminator Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated …B0FXW3GW5F Pet Odor Eliminator Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Litter + Urine Root 10-25k SV …Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25-50k SV …B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25-50k SV …B0FXW3GW5F Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 50k+ SV …B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL (15 campaigns)** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*All 15 campaigns are set to ENABLED, but none received any impressions in the
window, so CTR, CPC, ACOS, ROAS and Top-of-search impression share cannot be
calculated (no data). Keyword/target and search-term breakdowns are omitted
because there was no click or impression activity to report.*

*Canada and Mexico profiles have no active Sponsored Products campaigns.*

---

## Part B — Summary in plain English

**The headline:** your ads spent nothing and sold nothing over these two days,
because they essentially weren't being shown to shoppers.

- **Total spend:** $0.00
- **Total sales (from ads):** $0.00
- **ACOS / ROAS:** not applicable — you can't have an advertising cost-of-sale
  or return when there's no spend and no sales.
- **Best / worst campaign:** not meaningful — every campaign had identical
  zero activity.
- **Wasted spend:** none to flag, because there was no spend. (That's not a
  good thing here — it means the ads aren't running at all.)
- **Search terms to add as exact-match:** none available — with no clicks or
  sales there are no converting search terms to harvest yet.

**Why this is happening (most likely):** The US advertising account shows it
does **not** have a valid payment method on file. Amazon will not serve
Sponsored Products ads without one, which fits what we see — campaigns are
switched on, but almost nothing is being shown (only ~1,020 impressions and 4
clicks in the *entire* 14 days before this window, and zero in the window
itself). A secondary factor may be bids set too low to win any ad auctions,
but the payment issue is the thing to rule out first.

**What to do next (in order):**
1. **Check billing.** In Amazon Ads / Seller Central, confirm a valid credit
   card is on file for the US advertising account and that the account isn't
   paused for payment. This is almost certainly the blocker.
2. **Confirm campaigns are delivering** once billing is fixed — look for
   impressions starting to accrue within a day.
3. **Review bids.** If impressions stay near zero even after billing is sorted,
   raise bids on the main campaigns (especially the Auto and the top Exact
   campaigns) so they can win auctions; the $40/day budget is nowhere near
   being used.
4. **Re-run this report** in 2 days — once ads are serving again we'll have
   real numbers to optimise (wasted spend, converting search terms, ACOS).

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run of this report type,**
so there is no prior period to compare against. The table below will be
populated from the next run onward.

| Metric | This report (8–9 Sep) | Previous report | Change (abs) | Change (%) |
|---|--:|--:|--:|--:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Purchases | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Improved or worsened?** No baseline yet. For context, the account is at a
standstill (no serving), so the priority is getting ads live again rather than
period-over-period optimisation.

---

*Data source: Amazon Advertising API (Sponsored Products, spCampaigns report,
7-day attribution). ACOS and ROAS are computed as cost ÷ sales and sales ÷ cost
respectively. Generated automatically by the PPC Analyst routine.*

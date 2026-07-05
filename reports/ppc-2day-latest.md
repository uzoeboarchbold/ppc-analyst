# PPC 2-Day Report — 1–2 July 2026

**Report type:** 2-day | **Window covered:** 2026-07-01 to 2026-07-02 (2 full days)
**Generated:** 2026-07-05 (data ends 48h before run, as Amazon PPC data finalises ~48h late)
**Marketplace:** Amazon US (Sponsored Products) | **Account:** Uzoebo Archbold E-Commerce

> **Note on delivery:** The report was saved to the repo and uploaded to Google Drive successfully.
> Email to uzoebo.archbold@gmail.com could **not** be sent this run — the Gmail connector is
> installed but was not enabled for this session. To receive these by email, enable the Gmail
> connector for the chat/session. (Logged for future runs.)

---

## Headline: the account is effectively dormant — no ads delivered, no spend, no sales

For 1–2 July, the two live campaigns recorded **zero impressions, zero clicks, zero spend and zero sales**.
This is real data pulled from the Amazon Ads API, not a technical failure. Of the account's 50 campaigns,
**only 2 are switched on** ("SP KT | ST w/ Sales" and "SP PT | ST w/ Sales"); the other 48 are paused or
archived. Even over the wider period since these two went live (9 June–2 July) the whole account has drawn
only ~159 impressions and **0 clicks / $0.00 spend / $0.00 sales**. In short: the ads are essentially not
showing, so nothing is being spent and nothing is being sold through PPC.

---

## Part A — Data table (per campaign, Sponsored Products, US)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*Only ENABLED campaigns are shown; 48 other campaigns are paused/archived and had no activity. "n/a" =
cannot be calculated with zero impressions/clicks/spend.*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not applicable (no spend, no sales).
- **Best campaign / worst campaign:** No meaningful winner or loser — both live campaigns did nothing.
- **Wasted spend / negatives to add:** None. Because nothing was spent, there is no wasted spend and no
  negative keywords to suggest this period.
- **Well-converting search terms to add as exact-match:** None available — there were no clicks or
  purchases, so no search-term data to harvest.
- **What to do next (the real issue this period):** The problem is not *how* the money is being spent — it's
  that **the ads aren't running**. Concretely:
  1. **Confirm this is intentional.** If PPC is meant to be live, the two enabled campaigns are getting
     almost no impressions and no clicks — something is throttling delivery.
  2. **Check bids and budget.** Both live campaigns are $8/day but drew 0 impressions. Bids are very likely
     below the auction floor for their keywords/targets — raise bids to competitive levels so ads can win
     placements.
  3. **Check campaign/ad-group/target status and the product listing.** Verify ad groups are enabled, that
     targets/keywords aren't paused, and that the advertised ASIN is in stock and Buy-Box eligible (a lost
     Buy Box stops SP delivery entirely).
  4. **Consider re-enabling proven campaigns.** 48 campaigns are paused/archived; if the goal is sales,
     decide which historically-performing ones to switch back on.
  5. If the account is *deliberately* paused, no action needed — these zero reports are expected until
     campaigns are turned back on.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first 2-day report, so there is no prior baseline to
compare against. Headline metrics for reference (all zero this period):

| Metric | This report (1–2 Jul) | Previous | Change (abs) | Change (%) |
|---|---:|---:|---:|---:|
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** No trend yet (first report). The next 2-day run will compare against this one. The number to
watch is whether impressions rise above zero — that will tell us the ads have started delivering.

---

*Data source: Amazon Advertising API (Sponsored Products v3 reporting), US profile. All figures pulled live;
zero values reflect genuine account activity, not missing data.*

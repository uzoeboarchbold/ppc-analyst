# PPC 2-Day Report — 20–21 November 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace)
**Product:** Cat Deterrent Spray / Pet Odor Eliminator — ASIN B0FXW3GW5F
**Reporting window:** 20 Nov 2026 – 21 Nov 2026 (2 full days)
**Report generated:** 24 Nov 2026 (data ends 48h before run, per Amazon's reporting lag)
**Ad type:** Sponsored Products

---

## ⚠️ Status note (please read first)

The data pulled cleanly from the Amazon Ads API, but it carries one important
real-world finding and two housekeeping items:

1. **Zero delivery.** All 15 enabled Sponsored Products campaigns recorded **zero
   impressions, zero clicks, zero spend and zero sales** for the window — and, on a
   cross-check, for the whole of November so far. The ads are switched on but are not
   showing to shoppers. This is the headline issue, not a data error (see "What to do next").
2. **Credential fix applied automatically.** The `AMZ_PROFILE_ID` provided to this run
   was invalid (it was not a real Amazon profile ID). I identified the correct US
   seller profile automatically and used it, so the pull still succeeded. No action
   needed from you, but it's worth correcting the stored value.
3. **Email could not be sent.** This environment has no email tool connected, so the
   report was saved to the repo and uploaded to Google Drive but **not emailed**. To get
   these by email in future, an email/Gmail connector needs to be added.

---

## Part A — Data table (by campaign)

Window: 20–21 Nov 2026. All 15 **enabled** campaigns are listed. 32 paused and 7
archived campaigns are excluded. CTR, CPC, ACOS and ROAS are undefined (–) because
there were no clicks or spend.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto B0FXW3GW5F | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Cat Root 1–10k SV · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Home + Eliminator + Brand Root 10–25k SV · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated · Cat Deterrent · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated · Cat Deterrent · Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated · Cat Deterrent Spray · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated · Cat Deterrent Spray · Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated · Pet Odor Eliminator · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated · Pet Odor Eliminator · Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP KT · ST w/ Sales | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Litter + Urine Root 10–25k SV · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 25–50k SV · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 25–50k SV · Phrase | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 50k+ SV · Exact | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Cat Tunnel Bed Pink · Exact Ranking | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| **TOTAL (15 enabled campaigns)** | **0** | **–** | **0** | **–** | **0** | **$0.00** | **$0.00** | **–** | **–** | **–** |

*Keyword/target-level report: 0 rows returned (no targets received any impressions).*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS / ROAS:** not applicable — there was no spend and no sales to measure.
- **Impressions / clicks:** 0 / 0.

**What this means.** Your campaigns are turned on (15 of them), but over these two days
they showed to shoppers **zero times**. No impressions means no clicks, no cost, and no
ad-driven sales. So there is no "best vs worst campaign", no wasted spend to cut, and no
winning search terms to harvest yet — simply because nothing ran.

**Why ads can be enabled but not deliver (most likely causes, in order):**
1. **Bids too low to win auctions.** Daily budgets are small ($1.50–$2.50) and bids may
   be below the market clearing price, so you never enter the auction.
2. **New listing with little ranking/history**, so Amazon has little reason to surface it.
3. **Listing not fully eligible** — out of stock, not in the Buy Box, suppressed, or
   missing a required attribute. A listing that can't win the Buy Box usually can't run
   Sponsored Products.

**Wasted spend / negatives to add:** none — there was no spend.
**Well-converting search terms to add as exact-match:** none available yet — no clicks.

### What to do next (priority order)
1. **Confirm the listing is live and winnable:** ASIN B0FXW3GW5F is active, in stock,
   and holding the Buy Box. This is the single most common reason ads don't deliver.
2. **Raise bids** on the enabled campaigns (start with the Auto campaign and the Exact
   "Cat Deterrent Spray" / "Pet Odor Eliminator" campaigns) to a level that can win
   placements, and lift daily budgets enough that a few clicks won't cap the campaign.
3. **Check campaign portfolio/date settings** aren't pausing delivery (end dates,
   portfolio budget caps, dayparting).
4. Once impressions start, re-run this report — it will then show real CTR, ACOS, ROAS,
   wasted spend and search terms to action.

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists — this is the first run, so it is the baseline.**
There is nothing to compare against yet. From the next run onward this section will show
the change in each headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both
an absolute number and a percentage, with a one-line verdict on whether things improved.

| Metric | This report | Previous | Change |
|---|---:|---:|---|
| Impressions | 0 | — | baseline |
| Clicks | 0 | — | baseline |
| Spend | $0.00 | — | baseline |
| Sales | $0.00 | — | baseline |
| ACOS | n/a | — | baseline |
| ROAS | n/a | — | baseline |

---

*Generated automatically by the PPC Analyst routine. Data source: Amazon Advertising API
(Sponsored Products, US profile 26765323558215).*

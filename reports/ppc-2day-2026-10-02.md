# PPC 2-Day Report — 28–29 September 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (USD), Sponsored Products
**Product:** Cat Deterrent Spray / Pet Odor Eliminator (ASIN B0FXW3GW5F)
**Date window covered:** Monday 28 Sep 2026 – Tuesday 29 Sep 2026 (2 full days, ending 48h before the run to allow for Amazon's reporting lag)
**Report generated:** 2 Oct 2026

---

## ⚠️ Read this first — your ads are not running

Your Sponsored Products ads delivered **nothing** in this window: zero
impressions, zero clicks, zero spend, zero sales. This is **not a data error** —
the Amazon API returned real numbers and they are all zero.

Looking back day by day, your ads effectively went dark around **3 September
2026** and have stayed dark ever since. The last time anything served was
1–2 September (just 287 impressions, 1 click, $0.08 total).

**The most likely cause:** your US Seller account shows **no valid payment
method on file**. When Amazon can't charge for ads, it stops serving them even
though the campaigns are still switched "on." You currently have 54 Sponsored
Products campaigns set up and enabled, but none of them can spend.

**What to do next (this is the priority — nothing else matters until it's fixed):**
1. Log in to Seller Central → **Settings → Account Info → Payment Information**
   (and Amazon Advertising → billing) and add/update a valid card.
2. Once billing is valid, confirm a few key campaigns are Enabled and have
   daily budgets set.
3. Give it 24–48 hours, then this report will start showing real performance
   again.

---

## A note on configuration (for whoever maintains the automation)

The `AMZ_PROFILE_ID` environment variable is set to an invalid value (it holds
an application ID, `amzn1.application.…`, not a numeric advertising profile ID).
I worked around it automatically by selecting the only account with live
campaigns — the **US profile (26765323558215)**. Please correct the variable to
`26765323558215` so future runs don't depend on the workaround.

---

## Part A — Data table (by campaign)

Every one of the 54 campaigns returned zeros for this window, so individual
campaign rows would all be identical zeros. Here is the account total:

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **TOTAL (all 54 campaigns)** | 0 | 0% | 0 | — | 0 | $0.00 | $0.00 | — | — | — |

(CTR, CPC, ACOS and ROAS are undefined when there are no clicks, spend or sales.)

---

## Part B — Plain-English summary

- **Overall spend:** $0.00
- **Overall sales (from ads):** $0.00
- **ACOS / ROAS:** Not applicable — you can't have an advertising cost of sale
  or a return on ad spend when no ads ran.
- **Best campaign / worst campaign:** None to call out — they all performed
  identically (no delivery).
- **Wasted spend / negatives to add:** None — you spent nothing, so nothing was
  wasted. (The flip side: you also captured no new sales from ads.)
- **Well-converting search terms to add as exact-match:** None available — there
  was no search-term activity in this window to learn from.
- **What to do next:** Fix the billing/payment issue described at the top. Until
  ads can serve, there is no performance to optimise.

---

## Part C — Comparison to the previous 2-day report

There is **no previous 2-day report** to compare against — this is the first run
of this report type. Future 2-day reports will show the change in each headline
metric (impressions, clicks, spend, sales, ACOS, ROAS) as both a number and a
percentage versus this report.

For context against the days just before the window: delivery was already
negligible (Sept 1: $0.08 spend; Sept 2–27: $0.00), so the zero in this window
continues an existing outage rather than marking a sudden drop.

---

*Generated automatically by the PPC Analyst routine. Data source: Amazon
Advertising API (Sponsored Products, v3 reporting), US profile 26765323558215.*

# PPC 2-Day Report — 11–12 June 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon US (Sponsored Products)
**Window covered:** 11 Jun 2026 and 12 Jun 2026 (2 full days; data ends 48h before the 15 Jun run, as Amazon finalises figures ~48h late)
**Generated:** 15 Jun 2026

---

## ⚠️ Read this first — two issues found

**1. There was zero ad activity in this window.** Both Sponsored Products
campaigns ran with **no impressions, no clicks, no spend and no sales** on
11–12 June. The most likely cause: the account has **no valid payment method
on file** (the API reports `validPaymentMethod = none` for every marketplace).
Amazon will not serve ads without a working payment method, so the campaigns
were effectively switched off. This needs a human to log in and add/fix the
card. Other possible causes (paused campaigns, zero/exhausted budgets) are
worth checking at the same time.

**2. The configured profile ID was wrong, and I fixed it.** The `AMZ_PROFILE_ID`
setting contained an *application* ID (`amzn1.application.…`) instead of a
numeric Ads *profile* ID. I could not use it as-is. I looked up the account's
real profiles and found three (US, Canada, Mexico — all "Uzoebo Archbold
E-Commerce"). Only the **US** profile has any campaigns, so I used that one.
**Action for you:** set `AMZ_PROFILE_ID` to the correct numeric value so future
runs don't have to guess.

- US profile ID: `26765323558215` (this is the live one — use this)
- Canada profile ID: `2840235221595557` (no campaigns)
- Mexico profile ID: `3892485344323414` (no campaigns)

**3. Email could not be sent automatically.** This environment has no email tool
connected, so the "email to uzoebo.archbold@gmail.com" step could not run. The
report is saved in the repo and uploaded to the Google Drive "PPC Reports"
folder, and a phone notification was sent. To enable email, an email/Gmail
integration needs to be added to the automation.

The numbers below are **real data pulled from the Amazon Ads API** — they are
genuinely zero, not missing.

---

## Part A — Data table (Sponsored Products, US)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP PT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **$0.00** | **n/a** | **n/a** |

*"n/a" = cannot be calculated because there were no impressions/clicks (you
can't divide by zero). Canada and Mexico profiles had no campaigns at all.*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  applicable — nothing was spent and nothing was sold.
- **Best campaign / worst campaign:** not meaningful this period — both
  campaigns delivered nothing.
- **Wasted spend / negatives to add:** none to suggest, because there was no
  spend to waste.
- **Search terms to add as exact-match:** none available — with zero clicks
  there are no converting search terms to harvest.
- **What this means:** your ads were not running. For an active FBA account this
  is the single most important thing to fix, because while ads are off you get
  no Sponsored Products visibility and competitors take that placement.

### What to do next (in priority order)
1. **Log in to Amazon Advertising / Seller Central and check the payment
   method.** The API shows no valid payment method on the account — add or
   update the card. This is the most likely reason ads stopped.
2. **Confirm both campaigns are "Enabled"** (not paused) and have a daily budget
   greater than $0 with a sensible bid.
3. **Check the account isn't suspended or out of funds.**
4. **Fix `AMZ_PROFILE_ID`** in the automation to `26765323558215` (US) so future
   reports don't rely on inference.
5. Once ads are live again, the next 2-day report will show real performance and
   this report becomes the baseline for comparison.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run, so there is nothing
to compare against yet. This report becomes the baseline. From the next run, this
section will show each headline metric (spend, sales, ACOS, ROAS, clicks,
impressions) as a change in both absolute number and percentage.

For reference, the baseline figures recorded here are: Impressions 0, Clicks 0,
Spend $0.00, Sales $0.00, Purchases 0, ACOS n/a, ROAS n/a.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting). Reports
pulled for campaign, targeting and search-term levels — targeting and
search-term reports returned zero rows, consistent with zero impressions.*

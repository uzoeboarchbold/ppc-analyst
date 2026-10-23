# PPC 2-Day Report — 19–20 October 2026

**Report type:** 2-day · **Window covered:** 19 Oct 2026 – 20 Oct 2026 (2 full days)
**Generated:** 23 Oct 2026 (data ends 48h before run, per Amazon's ~48h reporting lag)
**Account:** Uzoebo Archbold E-Commerce · **Ad product:** Sponsored Products
**Marketplaces checked:** US, Canada, Mexico (Amazon Advertising, North America region)

---

## ⚠️ Read this first (plain English)

Two things you need to know before the numbers:

1. **Your ads served nothing in this window — and haven't for at least 30 days.**
   Your US account has **15 switched-on (ENABLED) campaigns** with budgets set
   (about **$23.50/day** in total). Despite that, they got **0 impressions,
   0 clicks, £0/$0 spend and 0 sales** on 19–20 Oct. I checked wider: the same
   15 campaigns also show **zero of everything across the last 30 days**. The
   campaigns are "on" but Amazon is not showing them to anyone. This is the
   headline issue — see "What to do next" below.

2. **A configuration value is wrong, but I worked around it.** The
   `AMZ_PROFILE_ID` setting the report is supposed to use is not a valid Amazon
   profile ID (it's a 50-character non-numeric value; a real profile ID is a
   14–16 digit number). I could not scope the report with it. Instead I used
   your login to pull **every advertising profile your account has** — US,
   Canada and Mexico — so you still get a full picture. **Please fix
   `AMZ_PROFILE_ID`** (your US profile ID is `26765323558215`) so future runs
   target the right marketplace cleanly.

3. **Email could not be sent from this run.** The Gmail connector is linked to
   your account but is **not enabled for this automated session**, so I could
   not email the report. It is saved in the repo and uploaded to Google Drive
   (folder "PPC Reports"). To enable email next time, turn the Gmail connector
   on for this chat/session in your Claude connector settings.

The API itself is healthy — login, token refresh and report generation all
worked. The zeros are real data, not a pull failure. I did not invent any
numbers.

---

## Part A — Data table

All monetary figures in the marketplace's local currency (US = USD). "ToS IS"
= Top-of-search impression share.

### United States (profile 26765323558215)

Every enabled campaign below returned zero across the board for 19–20 Oct 2026.
ToS impression share is not applicable when there are no impressions.

| Campaign (ENABLED) | Daily budget | Impr. | ToS IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Cat Root 1-10k SV … Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated … Cat Deterrent Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated … Cat Deterrent Phrase | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated … Cat Deterrent Spray Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated … Cat Deterrent Spray Phrase | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated … Pet Odor Eliminator Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated … Pet Odor Eliminator Phrase | $2.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP KT \| ST w/ Sales | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Litter + Urine Root 10-25k SV … Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25-50k SV … Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25-50k SV … Phrase | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 50k+ SV … Exact | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | $1.50 | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL (US, 15 enabled)** | **$23.50** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

(The US account also has 32 PAUSED and 7 ARCHIVED campaigns, which cannot
serve and are excluded.)

### Canada (profile 2840235221595557)

No Sponsored Products campaigns exist on this profile — nothing to report.

### Mexico (profile 3892485344323414)

No Sponsored Products campaigns exist on this profile — nothing to report.

### Grand total (all marketplaces)

| | Impr. | Clicks | Purchases | Sales | Cost | ACOS | ROAS |
|---|---|---|---|---|---|---|---|
| **All profiles, 19–20 Oct** | 0 | 0 | 0 | $0.00 | $0.00 | n/a | n/a |

---

## Part B — Summary

**Overall:** Across all three marketplaces there was **no ad spend, no sales,
no clicks and no impressions** on 19–20 October. ACOS and ROAS can't be
calculated because nothing was spent or sold through ads.

**Best / worst campaign:** Not meaningful this period — every enabled campaign
performed identically at zero. Nothing is serving, so nothing is winning or
wasting money yet.

**Wasted spend / negatives to add:** None to flag, because there was no spend.
(The usual "high spend, no sales → add as negative" logic has nothing to act
on.)

**Well-converting search terms to add as exact-match:** None available — with
zero impressions there are no search terms to harvest.

**The real problem:** You have 15 enabled campaigns with live budgets, all
pointed at essentially one product line (ASIN **B0FXW3GW5F**, a pet-odour /
cat-deterrent product, plus one cat-tunnel-bed campaign), and they are getting
**zero impressions over a full month**. "Enabled with a budget" but "zero
impressions for 30 days" almost always means one of these:

1. **The product isn't eligible to advertise** — out of stock, lost the Buy
   Box, or the listing is suppressed/inactive. Ads can't show if the product
   isn't the featured offer. *This is the most likely cause when every
   campaign and match type is at exactly zero.*
2. **Bids are too low to win any auction** — if your keyword bids sit well
   below the going rate, you simply never enter the auction.
3. Budgets so small (£/$1.50/day) that combined with low bids, nothing clears.

### What to do next (in order)

1. **Check the product first.** In Seller Central, confirm ASIN B0FXW3GW5F is
   **in stock, active, and holds the Buy Box**. If it doesn't, no amount of
   bidding will make the ads serve — fix that and ads should start showing
   within a day.
2. **Check the bids.** Open two or three of the enabled campaigns and compare
   your keyword bids to Amazon's suggested bid range. If you're far below,
   raise bids toward the suggested range to get into the auction.
3. **Confirm there's no account/billing hold.** A payment or account-health
   issue can stop all delivery.
4. Once impressions start, re-run this report — it will then surface real
   ACOS/ROAS, wasted spend and search-term opportunities.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run**, so there is no
baseline to compare against. This report will become the baseline for the next
2-day run, which will show the change in impressions, clicks, spend, sales,
ACOS and ROAS as both a number and a percentage.

---

*Data source: Amazon Advertising API (Sponsored Products v3 reporting),
North America region. Profiles pulled live via the account's refresh token.
All figures are as reported by Amazon for the stated window; where the account
had no activity, zeros are shown rather than estimated.*

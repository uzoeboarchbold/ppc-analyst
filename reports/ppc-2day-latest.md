# PPC 2-Day Report — 14–15 Jun 2026

**Marketplace:** Amazon US (Sponsored Products) · Account: Uzoebo Archbold E-Commerce
**Window covered:** Sun 14 Jun 2026 – Mon 15 Jun 2026 (2 full days, account timezone America/Los_Angeles)
**Generated:** 18 Jun 2026 (data ends 48h before run, as required)

## Read this first (plain English)
Your Sponsored Products advertising was **switched off in all but name** during these two days. Only **2 of ~55 campaigns are enabled**, and even those two showed **zero impressions** — meaning your ads were not displayed to a single shopper. As a result:

- **Spend: $0.00**
- **PPC sales: $0.00**
- **Clicks: 0**, **Impressions: 0**

This is not an error in the data — I confirmed it against Amazon. The whole US Sponsored Products account is effectively dormant. The remaining 50+ campaigns are **paused or archived**, and the two "live" campaigns are not winning any ad placements.

**Setup note (fixed automatically):** the `AMZ_PROFILE_ID` environment variable is misconfigured — it contains an application ID (`amzn1.application.…`) instead of a numeric Amazon advertising profile ID. I detected this, looked up the account's real profiles, and used the **US profile (26765323558215, USD)** since this is a US FBA account. Please correct the variable to `26765323558215` so future runs are unambiguous (see notes-to-self.md).

---

## Part A — Data table (per campaign, 14–15 Jun 2026)

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales (ENABLED, $8/day) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales (ENABLED, $8/day) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*Only the 2 enabled campaigns are shown; ~53 other campaigns are paused/archived and served nothing in this window. ToS = Top-of-search. Metrics are "n/a" because there were zero impressions and clicks to calculate ratios from.*

## Part B — Summary

- **Overall:** $0 spent, $0 PPC sales, 0 clicks, 0 impressions. ACOS and ROAS cannot be calculated (no spend, no sales).
- **Best campaign:** none — neither enabled campaign delivered.
- **Worst / wasted spend:** none in dollar terms (nothing was spent), but the real waste is **opportunity**: the account is live in name only and is generating no advertising-driven sales.
- **Negatives to add:** none — there were no clicks or search terms to act on.
- **Exact-match search terms to add:** none available — the search-term report is empty because there were zero clicks.
- **Context (last 7 days, 9–15 Jun):** across the whole account there were only a handful of impressions (e.g. "SP KT | ST w/ Sales" got 78 impressions over the week) and **0 clicks** account-wide. So this is not a one-off bad weekend — advertising has essentially stalled.

### What to do next
1. **Decide if advertising should be on at all.** ~53 campaigns are paused. If that is intentional, no action is needed and you can expect $0 reports. If not, re-enable the campaigns you want running.
2. **Fix the two "live" campaigns.** "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales" are enabled but winning no impressions. The usual causes are (a) **bids too low** to enter the auction, (b) the targeted "search terms with sales" list is too narrow, or (c) the advertised product is **out of stock / not Buy-Box eligible**. Check stock and Buy Box first, then raise bids.
3. **Correct `AMZ_PROFILE_ID`** to the numeric US profile `26765323558215`.
4. Once ads are delivering again, this report will start showing real numbers to optimise.

## Part C — Comparison to previous 2-day report
**No previous 2-day report exists** — this is the first run, so there is nothing to compare against. This report is the **baseline**. Headline metrics to track going forward: Spend $0.00, Sales $0.00, Clicks 0, Impressions 0, ACOS n/a, ROAS n/a. The next 2-day report will show the change versus these figures.

---
*Data source: Amazon Advertising API (Sponsored Products v3 reporting), pulled live. No figures were estimated or invented.*

# PPC 2-Day Report — 15–16 Nov 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon.com (US), Sponsored Products
**Dates covered:** Sunday 15 Nov 2026 and Monday 16 Nov 2026 (2 full days)
**Report generated:** 19 Nov 2026 (data finalised to 48h before run)
**Currency:** USD

---

## ⚠️ Read this first

Two things need your attention before the numbers below make sense:

1. **Your ads are not running.** All 15 Sponsored Products campaigns are switched
   ON (status "Enabled"), but they served **zero impressions, zero clicks and spent
   nothing** — not just on these two days, but every day for at least the last two
   weeks. So every figure in this report is zero. That is not a glitch in the
   report; it is what the account is actually doing.

2. **The most likely cause: no valid payment method on the US account.** Amazon
   stops showing your ads when it can't bill you. The account flag for a valid
   payment method is currently **false**. Fixing your billing/card in Seller
   Central (Amazon Ads → Billing) is almost certainly what will turn the ads back on.

3. **A settings note for whoever set this up:** the `AMZ_PROFILE_ID` configured for
   this automation is actually an app ID, not an advertising account ID. I worked
   around it automatically by finding the correct US account (`26765323558215`), so
   the report still ran — but it's worth correcting the setting so future runs are
   unambiguous. Details are in `notes-to-self.md`.

---

## Part A — Data Table (by campaign)

All metrics are for 15–16 Nov 2026 combined. Every active campaign served no traffic.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated …Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV …Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV …Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

(IS = impression share. Dashes mean the metric can't be calculated with no clicks/spend.)

---

## Part B — Summary in plain English

- **Spend:** $0.00. **Sales (ad-attributed):** $0.00. **ACOS / ROAS:** not
  applicable — you can't have an advertising cost-of-sale or return when nothing
  was spent.
- **Best / worst campaign:** none stand out, because none ran. All 15 are tied at zero.
- **Wasted spend / negatives to add:** none to flag — there was no spend to waste,
  and no search terms came in, so there's nothing to add as a negative yet.
- **Winning search terms to add as exact-match:** none available — with no clicks
  or orders in the window, there's no search-term data to mine. This will become
  useful again once delivery resumes.
- **The one thing that matters:** the campaigns are enabled but blocked from
  running. Nothing in the ad settings (bids, budgets, keywords) will change the
  numbers until the account can serve ads again.

### What to do next
1. **Fix billing first.** Go to Amazon Ads / Seller Central → Billing and make sure
   a valid payment method is on file. This is the single blocker.
2. **Confirm delivery resumes.** Within a day of fixing billing, impressions should
   start appearing. The next 2-day report will confirm it.
3. **Then, and only then,** we can go back to the normal optimisation work —
   trimming wasted spend, harvesting winning search terms into exact-match, and
   pushing budget toward the best ACOS campaigns. None of that is meaningful while
   spend is zero.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first one.
From the next run onward, this section will show the change in spend, sales, ACOS
and ROAS as both a number and a percentage.

For context against recent history: the account has shown **zero activity for the
entire trailing 14 days (3–16 Nov 2026)**, so this is a continuation of an
already-dark account rather than a sudden drop. The trend only changes once billing
is fixed.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting). Figures are
real API values for the stated window, not estimates.*

# PPC 2-Day Report — Oct 31–Nov 1, 2026

**Report type:** 2-day · **Dates covered:** 31 Oct 2026 – 1 Nov 2026 (2 full days)
**Run:** 4 Nov 2026 23:09 UTC · **Account:** Uzoebo Archbold E-Commerce (US marketplace, USD) · **Product:** Sponsored Products

---

## ⚠️ Read this first (plain English)

**The data pulled successfully, and the honest result is: the ads spent nothing and sold nothing in these two days.** All 15 US campaigns are switched ON, but not one of them showed a single ad impression, got a click, or cost a cent on 31 Oct or 1 Nov.

Two things to know:

1. **Why no activity?** The most likely cause is that the US advertising account currently has **no valid payment method on file** (Amazon reports `validPaymentMethod: false` for this account). Amazon will not serve Sponsored Products ads without a working payment method, even when campaigns are "enabled." **This is the #1 thing to fix** — add/repair the payment method in Seller Central → Advertising, and ads should start delivering again.

2. **A settings note (already worked around):** the automated credential `AMZ_PROFILE_ID` was set to the wrong kind of value (an *application* ID, not an *advertising profile* ID). I detected this, looked up the account's real profiles, and automatically used the correct **US** profile (`26765323558215`) so the report could still run. No action needed from you, but someone may want to fix that stored setting so it's correct for the record.

These numbers are **real (genuinely zero)** — nothing has been estimated or invented.

---

## Part A — Data table (by campaign)

Window: 31 Oct – 1 Nov 2026. All figures in USD. "ToS IS" = Top-of-search impression share. A dash (—) means the metric can't be calculated because there were no impressions/clicks.

| # | Campaign | Impr. | ToS IS | Clicks | CTR | Purch. | Sales | Cost | CPC | ACOS | ROAS |
|---|----------|------:|-------:|-------:|----:|-------:|------:|-----:|----:|-----:|-----:|
| 1 | SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 2 | SP Cat Root 1-10k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 3 | SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 4 | SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 5 | SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 6 | SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 7 | SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 8 | SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 9 | SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 10 | SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 11 | SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 12 | SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 13 | SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 14 | SP Odor Root 50k+ SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| 15 | SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| | **TOTAL (15 campaigns, all ENABLED)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*Keyword/target breakdown:* the Sponsored Products targeting report returned **0 rows** for the window (no targets received any impressions). *Search-term report:* **0 rows** (no shopper searches triggered an ad).

*Other marketplaces:* the account also has Canada and Mexico advertising profiles, but neither has any Sponsored Products campaigns, so they are not shown.

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS / ROAS:** not applicable (no spend, no sales)
- **Best campaign / worst campaign:** none stands out — every campaign delivered identically nothing. There is no performance to rank yet.
- **Wasted spend / negatives to add:** none — you can't waste money you didn't spend. No negative-keyword suggestions this period.
- **Well-converting search terms to add as exact-match:** none available — there were no clicks or sales to learn from.

**What this means:** your campaigns are built and turned on (15 of them, nicely structured into Auto, Exact, Phrase, and root/isolated keyword groups around your pet-odor / cat-deterrent product and a cat tunnel bed), but they are **not actually running**. For a two-day window to show exactly zero across every campaign and every target, the ads aren't entering auctions at all — this is an account-level block, not a bidding or keyword problem.

### What to do next
1. **Fix the payment method (priority).** In Seller Central → Advertising → Billing, confirm a valid payment method is on file. Amazon shows this US account as having no valid payment method, which stops all ad delivery. This alone is the most likely reason for zero activity.
2. **Check for a campaign-level or account-level pause/suspension.** Even though campaigns read "enabled," confirm the ad account itself isn't paused, out of budget-cap at the account level, or under review.
3. **Confirm the product is in stock and buyable.** Ads won't serve if the ASIN isn't the Featured Offer (Buy Box) or is out of stock.
4. **Re-check after the fix.** Once ads are serving, the next 2-day report will have real impressions, clicks and sales to analyse, and I can start recommending negatives and exact-match additions.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the **first run** of the 2-day report, so there is no baseline to compare against.

| Metric | Previous (2-day) | This period | Change (#) | Change (%) |
|--------|-----------------:|------------:|-----------:|-----------:|
| Impressions | — | 0 | n/a | n/a |
| Clicks | — | 0 | n/a | n/a |
| Spend | — | $0.00 | n/a | n/a |
| Sales | — | $0.00 | n/a | n/a |
| ACOS | — | n/a | n/a | n/a |
| ROAS | — | n/a | n/a | n/a |

**Verdict:** No change can be computed (first report). This period establishes the baseline: zero delivery, pending the payment-method fix above.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting), 14-day attribution window. Pulled 4 Nov 2026. US advertising profile 26765323558215.*

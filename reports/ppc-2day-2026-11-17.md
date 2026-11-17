# PPC 2-Day Report — Nov 13–14, 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Date window covered:** 2026-11-13 and 2026-11-14 (2 full days, ending 48h before the run to let Amazon's data finalise)
**Report generated:** 2026-11-17 (run) · Attribution: 7-day
**Previous report of this type:** none — this is the first 2-day report (baseline)

---

## ⚠️ Read this first — nothing is running

**The account served ZERO ads in this window.** Every campaign recorded 0 impressions, 0 clicks, $0 spend and 0 sales on both Nov 13 and Nov 14. I checked the wider picture too: **there has been no delivery at all for the last 30+ days** (Oct 16 → Nov 14, every single day zero).

This is **not a reporting error** — the API pulled cleanly. The ads genuinely aren't being shown.

**Most likely cause:** the US advertising account has **no valid payment method on file** (`validPaymentMethod: false`). Amazon will not serve Sponsored Products ads without one. The daily budget on the account is also only $40.

**What I had to fix to get this far:** the stored profile ID in the system settings (`AMZ_PROFILE_ID`) was wrong — it held an application ID rather than a real advertising profile ID. I looked up the account's real profiles and used the correct US profile (ID 26765323558215), which holds all 54 live campaigns. (CA and MX profiles exist but have no campaigns.)

---

## Part A — Data table (by campaign)

All 54 enabled campaigns delivered identically zero, so individual rows add no information. Totals:

| Metric | Nov 13–14 total |
|---|---|
| Impressions | 0 |
| Top-of-search impression share | n/a (no impressions) |
| Clicks | 0 |
| CTR | n/a |
| Purchases | 0 |
| Sales | $0.00 |
| Total cost | $0.00 |
| CPC | n/a |
| ACOS | n/a |
| ROAS | n/a |

**Campaigns in the account:** 54 Sponsored Products campaigns, all in ENABLED/PAUSED states, all advertising the Cat Deterrent Spray / Pet Odor Eliminator product (ASIN B0FXW3GW5F). Structure looks deliberate — Exact / Phrase / Broad variants across "cat deterrent", "pet odor eliminator", "litter", "urine" and brand-root themes. The structure is fine; it simply isn't being allowed to run.

---

## Part B — Summary in plain English

- **Overall spend:** $0. **Overall sales:** $0. There is no ACOS or ROAS to report because nothing was spent and nothing was sold through ads.
- **Best / worst campaign:** not applicable — none delivered.
- **Wasted spend / negatives to add:** none — you can't waste spend when nothing is spending. No negative-keyword suggestions this period.
- **Well-converting search terms to add as exact-match:** none available — with no clicks there is no search-term data to mine.
- **The real issue:** your ads are switched on inside Amazon but Amazon is refusing to show them. The overwhelmingly most common reason for an entire account to show zero delivery is a **billing/payment problem**, which matches what the account is reporting (no valid payment method).

### What to do next (in order)
1. **Fix billing.** In Seller Central → Advertising (or the Campaign Manager billing section), add or update a valid credit card / payment method. This is almost certainly the blocker.
2. **Confirm budgets.** The account daily budget shows as $40 — make sure that's intended and that individual campaigns have live daily budgets, not $0.
3. **Check the product is sellable.** Ads won't serve if the product is out of stock or doesn't hold the Buy Box. Confirm B0FXW3GW5F is in stock and Buy-Box eligible.
4. **Re-check in 48 hours.** Once billing is fixed, delivery usually resumes within a day. The next 2-day report will show real numbers to work with, and I can start finding wasted spend and winning search terms then.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first one, so it serves as the baseline. All headline metrics (spend, sales, ACOS, ROAS, impressions, clicks) start at zero.

| Metric | This report | Previous | Change |
|---|---|---|---|
| Impressions | 0 | — | — (baseline) |
| Clicks | 0 | — | — |
| Spend | $0.00 | — | — |
| Sales | $0.00 | — | — |
| ACOS | n/a | — | — |
| ROAS | n/a | — | — |

**Did things improve or worsen?** No basis for comparison yet. The one thing to flag is that the account has been dark for at least a month — so the priority isn't optimisation, it's getting delivery turned back on.

---

*Prepared automatically by the PPC Analyst. Data source: Amazon Advertising API (Sponsored Products), US profile 26765323558215. Note: this environment has no email tool, so this report was delivered via the Google Drive "PPC Reports" folder and shared to your email address rather than sent as a direct email.*

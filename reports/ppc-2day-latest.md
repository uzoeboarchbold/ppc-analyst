# PPC 2-Day Report — 15–16 Aug 2026

**Marketplace:** Amazon.com (US) · Sponsored Products · Seller "Uzoebo Archbold E-Commerce"
**Date window covered:** 15 Aug 2026 – 16 Aug 2026 (2 full days, ending 48h before the 19 Aug 23:04 UTC run — data is finalised)
**Attribution:** 7-day · **Currency:** USD
**Report generated:** 19 Aug 2026

---

### ⚠️ Two operational notes (read first)

1. **Profile ID had to be auto-corrected.** The `AMZ_PROFILE_ID` environment variable is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`, which is an *application* ID, not an Amazon Ads *profile* ID. The API rejected it ("Invalid scope"). I looked up the account's real profiles and used the **US Sponsored Products profile `26765323558215`** (USD), which is the correct primary marketplace for this business. **Fix for good:** set `AMZ_PROFILE_ID=26765323558215` in the environment so future runs don't rely on this fallback. (If you actually want the Canada or Mexico marketplace instead, the IDs are `2840235221595557` (CA) and `3892485344323414` (MX).)

2. **Email was not sent.** The Gmail connector is installed but **not enabled for this automated session**, so I could not email the report. It has been saved to the repo and uploaded to Google Drive ("PPC Reports"). To enable email next time, turn the Gmail connector on for this chat/automation in your Claude connector settings.

---

## Part A — Campaign data table

| Campaign | Impr. | ToS IS | Clicks | CTR | Purch. | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP PT Pet Odor Eliminator 6K-PZMX-MTDZ B0FXW3GW5F | 28 | 4.0% | 1 | 3.6% | 0 | $0.00 | $2.16 | $2.16 | - | 0.00 |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 28 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | - | - | - |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 11 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | - | - | - |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 7 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | - | - | - |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 3 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | - | - | - |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 2 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | - | - | - |
| SP KT \| ST w/ Sales | 2 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | - | - | - |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | - | 0 | - | 0 | $0.00 | $0.00 | - | - | - |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 0 | - | 0 | - | 0 | $0.00 | $0.00 | - | - | - |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | - | 0 | - | 0 | $0.00 | $0.00 | - | - | - |
| SP PT \| ST w/ Sales | 0 | - | 0 | - | 0 | $0.00 | $0.00 | - | - | - |
| **TOTAL (11 campaigns)** | **81** | **1.4%** | **1** | **1.2%** | **0** | **$0.00** | **$2.16** | **$2.16** | **n/a** | **0.00** |

*ToS IS = Top-of-search impression share. ACOS = ad cost ÷ sales. ROAS = sales ÷ ad cost. "-" means not calculable (no clicks or no sales).*

---

## Part B — Plain-English summary

**The headline: almost nothing happened over these two days, and that itself is the problem.**

- **Spend:** $2.16 total across all 11 campaigns for the two days combined — roughly **$1 a day**, against a daily budget of about $40. The account is barely spending.
- **Sales:** $0. No orders came from ads in this window.
- **ACOS / ROAS:** Not meaningful — with $0 sales there's no return to measure.
- **Traffic:** 81 ad impressions and just **1 click** in two days. Top-of-search visibility is near zero (about 1.4% blended).

**Best campaign:** None truly "won" — but "SP PT Pet Odor Eliminator" was the only campaign to get a click and the only one showing any top-of-search presence (4%). It's the single sign of life.

**Worst / wasted spend:** There is no wasted spend to cut this period — total spend is only $2.16 and no single campaign burned money without return. The one campaign that spent ($2.16 on a product-targeting placement against ASIN `B0FS39DYG7`) got a click but no sale; too little data to judge, so **no negative is recommended yet.**

**Search terms to add as exact-match:** None. There were no converting search terms this period (zero orders), so there is nothing proven to promote to exact yet.

**The real story — visibility, not efficiency.** Getting only 81 impressions and 1 click in two days almost always points to one of: bids set too low to win auctions, campaigns paused/out of budget, or listings not eligible to serve. This is not a "trim the losers" week — it's a "why are the ads barely showing?" week.

### What to do next
1. **Fix the profile ID** in the environment (`AMZ_PROFILE_ID=26765323558215`) so reporting is reliable without a fallback.
2. **Check why impressions are so low.** Confirm campaigns are enabled, in budget, and bids are competitive — 81 impressions/2 days suggests bids or budgets are throttling delivery, or listings aren't serving.
3. **Raise bids on the core "pet odor eliminator" keywords** (the phrase/exact campaigns that got 0 clicks) to buy visibility, then re-check in the next report.
4. **Enable the Gmail connector** for this automation so future reports arrive by email.
5. Hold off on negatives and exact-match additions until there's real click and conversion volume to act on.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run of this report type**, so there is no prior period to compare against. This report becomes the baseline; the next 2-day report will show change vs. these numbers (spend $2.16, sales $0.00, ACOS n/a, ROAS 0.00, clicks 1, impressions 81).

---

*Data source: Amazon Advertising API, Sponsored Products v3 reporting (spCampaigns / spTargeting / spSearchTerm), pulled live on 19 Aug 2026. No numbers are estimated.*

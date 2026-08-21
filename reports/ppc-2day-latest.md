# PPC 2-Day Report — 17–18 Aug 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products)
**Dates covered:** Monday 17 Aug 2026 – Tuesday 18 Aug 2026 (2 full days)
**Report generated:** 21 Aug 2026 (data ends 48h before run, per Amazon's reporting lag)

---

## ⚠️ Notes on this run

- **Data source worked.** Live figures were pulled from the Amazon Ads API (Reporting API v3) for the US Sponsored Products account. Nothing is estimated or invented.
- **Profile ID fix (again).** The `AMZ_PROFILE_ID` environment variable holds an application ID, not a valid advertising profile. The correct US profile (`26765323558215`, USD) was found automatically via the profiles endpoint and used instead. No action needed from you.
- **Email not sent this run.** The Gmail connector is installed but switched **off for this automated chat**, so the report could not be emailed. It has been saved to the repo and uploaded to the Google Drive "PPC Reports" folder. To enable email, turn the Gmail connector on for this session in connector settings.

---

## Part A — Data table (by campaign)

| Campaign | Impressions | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| SP Cat Tunnel Bed Pink Only (Exact Ranking) | 56 | 0% | 2 | 3.57% | 0 | $0.00 | $0.50 | $0.25 | n/a | 0.00 |
| SP PT Pet Odor Eliminator (Product targeting) | 8 | 3% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator (Phrase) | 7 | 14% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root (Exact) | 2 | 0% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP KT — ST w/ Sales | 1 | 0% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP PT — ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **74** | **—** | **2** | **2.70%** | **0** | **$0.00** | **$0.50** | **$0.25** | **n/a** | **0.00** |

*ToS = Top-of-search. "—" means not calculable (no clicks, spend or sales, so CPC/ACOS/ROAS are undefined). ACOS is "n/a" where there was spend but no sales (cost-of-sale can't be divided by zero sales). Impression-share is a per-campaign ratio and is not summed in the totals row.*

---

## Part B — Plain-English summary

**The short version: the account is still very quiet, but it finally bought its first clicks.**

- **Spend:** $0.50 total over the two days. Tiny, but no longer zero — the first paid clicks in this account for a while.
- **Sales from ads:** $0.00. The 2 clicks did not lead to a purchase.
- **ACOS / ROAS:** Not meaningful yet. ACOS can't be calculated (you had spend but no sales), and ROAS is 0.00 (no sales returned on the 50 cents spent).
- **Visibility:** **74 impressions** across the campaigns — roughly the same as last time (72). Only one campaign turned impressions into clicks.

**Best campaign:** "SP Cat Tunnel Bed Pink Only (Exact Ranking)" — the only campaign that got clicks (2 clicks from 56 impressions, a 3.57% click rate) at a reasonable $0.25 per click. It's the one campaign actually doing something.

**Worst campaigns:** Six campaigns served **0 impressions** — they aren't showing at all. This usually points to bids that are too low, keywords with little search volume, or campaigns not fully enabled. The "Pet Odor Eliminator" phrase and product-target campaigns did get shown (7–8 impressions) but won zero clicks.

**Wasted spend:** None worth acting on. The only spend was $0.50 on "cat tunnel bed" — too little data (2 clicks) to call it wasted or to add negatives yet. Watch it: if it keeps taking clicks without sales, revisit.

**Search terms to add as exact-match:** None yet. The only search term with clicks was "cat tunnel bed" (2 clicks, 0 sales) — it hasn't converted, so there's nothing proven to promote to exact-match this period.

### What to do next

1. **Wake up the dead campaigns.** Six campaigns got 0 impressions. Raise their bids modestly and confirm they're enabled with budget, so they start serving.
2. **Give the Cat Tunnel Bed campaign a little room.** It's the only one getting clicks. Keep its bid where it is and let it gather more click/sales data before judging it.
3. **Push the Pet Odor Eliminator keywords.** They're getting impressions (7–8) but no clicks — a small bid bump should start winning clicks so we learn what converts.
4. **Re-check next run.** With clicks now trickling in, the next report should start showing whether any of them convert into sales.

---

## Part C — Comparison to previous 2-day report

Compared against the previous 2-day report (**13–14 Aug 2026**).

| Metric | This report (17–18 Aug) | Previous (13–14 Aug) | Change (#) | Change (%) |
| :-- | :-: | :-: | :-: | :-: |
| Impressions | 74 | 72 | +2 | +2.8% |
| Clicks | 2 | 0 | +2 | new (from 0) |
| Spend | $0.50 | $0.00 | +$0.50 | new (from $0) |
| Sales | $0.00 | $0.00 | $0.00 | 0% |
| ACOS | n/a | — | — | — |
| ROAS | 0.00 | — | — | — |

**Did things improve or worsen?** Slightly improved. Impressions held roughly flat (+2.8%), and for the first time the account actually bought clicks (2) at a sensible $0.25 CPC — a step up from two straight days of zero activity. It's still not converting (no sales), so the win is small: the ads are now engaging shoppers, but not yet selling.

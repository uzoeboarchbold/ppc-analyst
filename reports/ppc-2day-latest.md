# PPC 2-Day Report — 23–24 Jul 2026

**Dates covered:** Thursday 23 July 2026 and Friday 24 July 2026 (2 full days, ending 48 h before the run to allow Amazon's data to finalise).
**Run date:** 27 July 2026 (Mon) · **Account:** Uzoebo Archbold E-Commerce — US marketplace · **Currency:** USD · **Ad type:** Sponsored Products.

> **Setup note (plain English):** The stored `AMZ_PROFILE_ID` credential was the wrong kind of ID (an app ID, not an account/profile ID), so it couldn't be used directly. I looked up the account's real profiles and used the active **US** advertising account (the only one with a real daily budget). Data pulled fine after that. No numbers were invented.

---

## Part A — Data Table (per campaign)

| Campaign | Impressions | Top-of-search imp. share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP KT \| ST w/ Sales | 184 | 0.11% | 1 | 0.54% | 0 | $0.00 | $3.51 | $3.51 | n/a | 0.00 |
| SP PT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | n/a | — |
| **TOTAL** | **184** | **0.11%** | **1** | **0.54%** | **0** | **$0.00** | **$3.51** | **$3.51** | **n/a** | **0.00** |

*ACOS is "n/a" because there were no sales to divide the cost into. ROAS is 0.00 for the same reason.*

---

## Part B — Summary (plain English)

- **Overall:** The account spent **$3.51** and made **$0.00 in sales** over these two days. That means **1 click, no orders**, so ACOS can't be calculated and ROAS is 0.
- **Best campaign:** None performed well — there were no sales. By default the least-bad is **"SP PT | ST w/ Sales"**, only because it spent nothing (it also served no impressions).
- **Worst campaign:** **"SP KT | ST w/ Sales"** — it spent the entire $3.51 on a single click that did not convert.
- **Wasted spend / suggested negatives:** The one click came from the exact-match keyword **"pet odor eliminator"** ($3.51, no sale). It's a single click, so it's too early to call it wasteful — but if the next report shows it keeps taking clicks without orders, add it as a **negative exact** or cut its bid.
- **Search terms to add as exact match:** **None.** No search term produced a sale this period, so there's nothing proven to promote to exact match yet.
- **Biggest issue — almost no delivery:** With a **$40/day budget**, spending only **$3.51 over two days** and getting just **184 impressions** is very low. The ads are barely showing (top-of-search share ~0.11%). This usually means **bids are too low**, **targets are too narrow**, or a campaign is effectively paused/under-delivering.

### What to do next
1. **Raise bids** on "SP KT | ST w/ Sales" (especially the "pet odor eliminator" keyword) so the ads actually show — 184 impressions in two days is far too few to learn anything.
2. **Check "SP PT | ST w/ Sales"** — it served **zero** impressions. Confirm it isn't paused, out of budget, or bidding below the floor; add/adjust product targets.
3. **Widen targeting** or add more relevant keywords/products so there's enough traffic to generate clicks and sales.
4. **Re-check in the next 2-day report** before making cut decisions — one click is not enough data to judge a keyword.

---

## Part C — Comparison to previous 2-day report

**No comparison available — this is the first 2-day report on record.** There is no earlier `ppc-2day-latest.md` to compare against, so headline-metric changes (spend, sales, ACOS, ROAS) can't be shown this time. From the next run onward, this section will show each metric's change as a number and a percentage, plus a one-line verdict on whether things improved or worsened.

| Metric | This report | Previous | Change (#) | Change (%) |
|---|--:|--:|--:|--:|
| Spend | $3.51 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | 0.00 | — | — | — |
| Clicks | 1 | — | — | — |
| Impressions | 184 | — | — | — |

---

*Generated automatically by the PPC Analyst routine. Figures are Sponsored Products, US marketplace, from the Amazon Advertising API (7-day attribution). No figures were estimated or invented.*

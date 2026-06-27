# PPC 2-Day Report — 23–24 June 2026

**Window covered:** Tuesday 23 June 2026 → Wednesday 24 June 2026 (2 full days)
**Report generated:** 27 June 2026 (data is finalised with a ~48-hour lag, so this is the most recent fully-settled 2-day window)
**Account:** Uzoebo Archbold E-Commerce — Amazon US (Sponsored Products), profile 26765323558215, USD
**Marketplaces checked:** US (active), Canada (no campaigns), Mexico (no campaigns)

---

## ⚠️ Read this first

**Your Sponsored Products ads were effectively switched off during this window — there was no spend and no sales.**

- Across all three marketplaces (US, CA, MX), Sponsored Products delivered **0 impressions, 0 clicks, £0 / $0 spend and $0 sales** on 23–24 June.
- The reason: **almost every campaign in the US account is currently PAUSED.** Only two campaigns are switched on — "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales" — and they are barely serving any impressions (over the last 30 days they returned 78 and 0 impressions respectively, with no clicks and no spend).
- This is **not a data error.** The Amazon API connection worked and the numbers were pulled successfully; the account genuinely had no ad activity. The previously-active campaigns (the "Cat Deterrent / Pet Odor Eliminator" set for ASIN B0FXW3GW5F) spent ~$329 over the last 30 days but have since been paused.

**Two small technical notes (handled automatically, no action needed from you):**
1. The `AMZ_PROFILE_ID` setting holds an application ID rather than a numeric advertising-profile ID, so it can't be used directly. The report automatically identified and used the correct active US profile instead. Worth correcting the setting when convenient.
2. There is no email-sending tool connected to this automation, so the report could not be emailed. It has been **saved to the repo, uploaded to Google Drive ('PPC Reports'), and sent to you as a notification + file** instead.

---

## Part A — Data table (per campaign)

Only campaigns that were live (ENABLED) in the window are shown. Both served no traffic.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP PT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **$0.00** | **n/a** | **n/a** |

*All other US campaigns were PAUSED during the window and are excluded (they served nothing). Canada and Mexico have no Sponsored Products campaigns.*

---

## Part B — Plain-English summary

**Overall:** Nothing ran. Spend was $0.00 and sales were $0.00 for 23–24 June, so there is no ACOS or ROAS to report (you can't have a cost-of-sale figure when there was no cost and no sale). The two switched-on campaigns received almost no impressions and zero clicks.

**Best / worst campaign:** Not applicable — no campaign delivered traffic. Both enabled campaigns performed identically: zero everything.

**Wasted spend / suggested negatives:** None — there was no spend to waste, and no search terms to add as negatives.

**Well-converting search terms to add as exact-match:** None available — with zero clicks there are no search terms to harvest this window. (For context, when the now-paused campaigns last ran, converting terms sat around the "pet odor eliminator" / "cat deterrent" themes for ASIN B0FXW3GW5F.)

**What to do next:**
1. **Decide whether advertising should be on at all right now.** If you want sales from ads, the paused campaigns need to be re-enabled — as things stand your ads are dark and you're getting no sponsored traffic.
2. If the pause is deliberate (e.g. out of stock, margin/seasonal reasons), no action is needed — but expect these 2-day reports to keep showing zeros until campaigns are switched back on.
3. The two ENABLED campaigns are serving almost no impressions. If they're meant to be your "always-on" campaigns, check their **bids and budgets** — near-zero impressions usually means bids are too low to win placements, or the targets are too narrow.
4. Fix the `AMZ_PROFILE_ID` setting to the numeric US profile (`26765323558215`) when convenient, so the connection is unambiguous.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first one**, so there is nothing to compare against yet.

| Metric | This report (23–24 Jun) | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Total cost | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Purchases | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

From the next 2-day run onwards this section will show the up/down movement in each headline metric versus this report.

---

*Generated automatically by the PPC Analyst. Data source: Amazon Advertising API (Sponsored Products, Reporting API v3). No figures were estimated or invented; all values above were pulled directly from the API for the stated window.*

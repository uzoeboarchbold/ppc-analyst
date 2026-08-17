# PPC 2-Day Report — 13–14 Aug 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products)
**Dates covered:** Thursday 13 Aug 2026 – Friday 14 Aug 2026 (2 full days)
**Report generated:** 17 Aug 2026 (data ends 48h before run, per Amazon's reporting lag)

---

## ⚠️ Notes on this run

- **Data source worked.** Live figures were pulled from the Amazon Ads API (Reporting API v3) for the US Sponsored Products account. Nothing is estimated or invented.
- **Profile ID fix.** The `AMZ_PROFILE_ID` environment variable held an application ID, not a valid advertising profile. The correct US profile (`26765323558215`, USD) was found automatically via the profiles endpoint and used instead. No action needed from you.
- **Email not sent this run.** The Gmail connector is installed but switched **off for this automated chat**, so the report could not be emailed. It has been saved to the repo and uploaded to the Google Drive "PPC Reports" folder. To enable email next time, turn the Gmail connector on for this session in connector settings.
- **First report of its type.** There is no earlier 2-day report to compare against, so the comparison section (Part C) has no prior numbers yet. From the next run onward it will show the change.

---

## Part A — Data table (by campaign)

| Campaign | Impressions | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Isolated — Pet Odor Eliminator (Phrase) | 7 | 14% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Home+Eliminator+Brand Root (Exact) | 27 | 5% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Home+Eliminator+Brand Root (Phrase) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP PT — Pet Odor Eliminator (Product targeting) | 16 | 1% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP KT — ST w/ Sales | 1 | 0% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP — Cat Tunnel Bed Pink (Exact Ranking) | 21 | 0% | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **72** | **—** | **0** | **0%** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*ToS = Top-of-search. "—" means not calculable (no clicks, spend or sales, so CPC/ACOS/ROAS are undefined). Impression-share is a per-campaign ratio and is not summed in the totals row.*

---

## Part B — Plain-English summary

**The short version: the account was almost completely dormant over these two days.**

- **Spend:** $0.00. No clicks were bought, so nothing was charged.
- **Sales from ads:** $0.00. No purchases.
- **ACOS / ROAS:** Not applicable — you can't have an advertising cost-of-sale or return-on-spend when there was no spend and no sales.
- **Visibility:** Ads did show up — **72 impressions** across 6 campaigns — but not one of those impressions turned into a click. So shoppers saw the ads occasionally but none clicked.

**Best campaign:** None stood out on results because there were no clicks or sales anywhere. On visibility alone, "SP Home+Eliminator+Brand Root (Exact)" led with 27 impressions, followed by the Cat Tunnel Bed campaign with 21.

**Worst campaign:** "SP Home+Eliminator+Brand Root (Phrase)" served **0 impressions** — it isn't getting shown at all, which usually points to a bid that's too low, a tiny budget, or the keywords having very little search volume right now.

**Wasted spend:** None to report — because there was no spend at all. So there are no negative keywords to suggest this period.

**Search terms to add as exact-match:** None available. The search-term report came back empty for this window (no clicks means Amazon has no converting search terms to show), so there's nothing to promote to exact-match yet.

### What's likely going on
Impressions with zero clicks and zero spend across every campaign for two straight days almost always means one of these:
1. **Bids are too low** to win the click auctions (you appear low on the page, rarely in the top-of-search slot — note the top-of-search shares of 0–14%).
2. **Daily budget is very small** (the account's daily budget is set to **$40**, but if per-campaign budgets or bids are throttled, delivery stalls).
3. The products are in **low-demand keywords** right now, so few shoppers are searching.

## What to do next
1. **Check that campaigns are actually enabled and funded** — confirm none are paused and that each has budget left. Two days of exactly $0 across the whole account is unusual and worth a quick manual look in Seller Central.
2. **Raise bids modestly** on the main keywords (e.g. "pet odor eliminator", "cat tunnel bed") to start winning clicks and gather data. Even small clicks will tell us what converts.
3. **Fix the dead campaign** — "SP Home+Eliminator+Brand Root (Phrase)" got 0 impressions. Increase its bid or check its keywords so it starts serving.
4. **Re-check next run.** Once clicks start coming in, the next report will show real CTR, CPC, ACOS and ROAS, and we can start recommending negatives and exact-match winners.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** on file — this is the first one. Nothing to compare yet.

From the next 2-day run onward, this section will show each headline metric (spend, sales, ACOS, ROAS, impressions, clicks) as a change versus the prior report, in both absolute numbers and percentage, with a one-line read on whether things improved or worsened.

| Metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 72 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | — | — | — | — |
| ROAS | — | — | — | — |

*Baseline established. Comparison begins next run.*

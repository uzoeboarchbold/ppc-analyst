# PPC 2-Day Report — 25–26 July 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon US (Sponsored Products)
**Date range covered:** 25 Jul 2026 – 26 Jul 2026 (2 full days)
**Report generated:** 29 Jul 2026 (data ends 48h before run, per Amazon's ~48h reporting lag)
**Attribution:** 7-day. Because the report runs only ~48h after the window closes, the 7-day conversion window has not fully elapsed — any sales/purchases are as-attributed-so-far and may rise slightly. Every run has the same lag, so period-to-period comparisons stay fair.

> **Two setup notes for the account owner (did not block this report):**
> 1. **Email was not sent.** The Gmail connector is installed but switched **off for this automated chat**, so no send-email tool was available. This report was still saved to the repo and uploaded to Google Drive. To turn on emailing, enable the Gmail connector for this automation in claude.ai connector settings.
> 2. The `AMZ_PROFILE_ID` environment variable contains an *application* id, not a numeric Ads profile id. I worked around it by looking up the profiles from the refresh token and using the **US seller profile** (the only one with active campaigns). Worth fixing so the variable is correct.

---

## Part A — Data table (by campaign)

| Campaign | Impressions | Top-of-search imp. share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales (keyword-targeted) | 2,079 | 0.27% | 2 | 0.10% | 0 | $0.00 | $6.72 | $3.36 | n/a | 0.00 |
| SP PT \| ST w/ Sales (product-targeted) | 392 | 0.35% | 3 | 0.77% | 0 | $0.00 | $4.69 | $1.56 | n/a | 0.00 |
| **TOTAL** | **2,471** | **—** | **5** | **0.20%** | **0** | **$0.00** | **$11.41** | **$2.28** | **n/a** | **0.00** |

*ACOS is "n/a" because there were no sales to divide cost against. Rate fields are as returned by the Amazon Ads API. Only 2 of the account's 11 enabled campaigns served any impressions in this window (see summary).*

---

## Part B — Summary (plain English)

**The headline:** In these two days the account spent **$11.41** on ads, got **2,471 impressions and 5 clicks**, and made **zero sales**. So ACOS can't be calculated (no sales) and ROAS is **0.00**. The good news is the amount at risk is tiny; the concern is that the money that was spent brought in nothing.

**Best campaign:** **SP PT (product-targeting)** was the less-bad of the two — cheaper clicks ($1.56 vs $3.36) and a far healthier click-through rate (0.77% vs 0.10%). Still no sale, but it's using budget more efficiently.

**Worst campaign:** **SP KT (keyword-targeting)** spent the most ($6.72) for only 2 clicks out of 2,079 impressions — a 0.10% click-through rate. Lots of people saw the ad and almost nobody clicked, which usually means the keyword and the product aren't a strong match, or the listing image/price isn't compelling in that search.

**Most of the account was dark.** 11 campaigns are enabled but only **2 actually ran** in this window (36 are paused, 7 archived). The other 9 enabled campaigns got zero impressions — normally a sign of bids set too low to win placements, exhausted daily budgets, or very low-traffic targets. This is the biggest thing to look into.

**Wasted spend / suggested negatives:** Every dollar this window technically converted to nothing, but the volumes are too small to act on hard — the worst offenders each had only 1–2 clicks:
- ASIN target `B00CKFL93K` (in SP PT) — $4.33 across 2 clicks, no sale.
- Exact keyword `cat odor eliminator for home` (in SP KT) — $5.08, 1 click, no sale.
- Exact keyword `cat deterrent spray` — $1.64, 1 click, no sale.

I would **not** add negatives yet on 1–2 clicks of data — that's not enough to conclude they never convert. Flag them and revisit once they've accumulated more clicks (rule of thumb: ~10+ clicks with no sale before cutting).

**Well-converting search terms to add as exact-match:** **None this window** — there were no conversions on any search term, so there is nothing proven to promote yet.

**What to do next:**
1. **Find out why only 2 of 11 enabled campaigns served.** Check the other 9 for out-of-budget, too-low bids, or dead targets. Waking up profitable campaigns matters far more than the $11 spent here.
2. **Fix SP KT's relevance.** A 0.10% CTR on 2,079 impressions is the clearest problem. Review whether `cat odor eliminator for home` genuinely matches the product, and check the main image/price/title against competitors.
3. **Let SP PT keep running** — it's spending efficiently; give it more clicks before judging conversion.
4. **Don't over-react to $0 sales on $11 spend** — it's a thin two-day sample. Watch the trend across the next reports rather than cutting now.
5. **Housekeeping:** fix the `AMZ_PROFILE_ID` variable and enable the Gmail connector so future reports can be emailed automatically.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first one, so it sets the baseline.** From the next 2-day run onward, this section will show each headline metric's change as a number and a percentage (up/down) versus the prior report.

**Baseline figures to compare against next time:**

| Metric | This report (25–26 Jul) |
|---|---:|
| Spend | $11.41 |
| Sales | $0.00 |
| Impressions | 2,471 |
| Clicks | 5 |
| Purchases | 0 |
| ACOS | n/a (no sales) |
| ROAS | 0.00 |
| Avg CPC | $2.28 |
| CTR | 0.20% |
| Active campaigns (served impressions) | 2 of 11 enabled |

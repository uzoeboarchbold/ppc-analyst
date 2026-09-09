# PPC 2-Day Report — Sep 5–6, 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, USD)
**Dates covered:** 5 September 2026 – 6 September 2026 (2 full days)
**Report generated:** 9 September 2026 (data ends 48h before run, so the window is fully finalised)
**Data source:** Amazon Advertising API — Sponsored Products, 7-day attribution

---

## ⚠️ Read this first

**Two things need your attention, and they explain the whole report:**

1. **Your ads are essentially not running.** In these two days every campaign recorded **zero
   impressions, zero clicks and zero spend**. A wider 30-day check confirms the account is barely
   active: about 1,900 impressions, 17 clicks, **$5.93 total spend and $0 sales** across the last
   month. So there is genuinely nothing to optimise yet — the problem is that the ads aren't serving.

2. **The most likely cause: no valid payment method on the US ad account.** Amazon flags this account
   as `validPaymentMethod: false`. When Amazon can't bill a card, it throttles or stops serving ads,
   which fits the near-zero impressions and spend. **Fixing the payment method in Seller Central /
   the Ads console is almost certainly step one.** Daily budgets are also very low ($1.50–$2.50), which
   would limit volume even once billing works.

*(Note for the record: the `AMZ_PROFILE_ID` credential provided points at the wrong ID — it's an
application ID, not a profile ID. I identified the correct US ad profile automatically and used that,
so the data below is correct. This is logged for the account owner to tidy up.)*

---

## Part A — Data table (per campaign)

All 16 enabled campaigns had no activity in the window. Metrics that require impressions or spend
(Top-of-search impression share, CTR, CPC, ACOS, ROAS) are therefore not applicable (n/a).

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto — B0FXW3GW5F | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent Spray (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent Spray (Phrase) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Cat Deterrent (Phrase) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Pet Odor Eliminator (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Isolated — Pet Odor Eliminator (Phrase) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 50k+ SV (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25–50k SV (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Odor Root 25–50k SV (Phrase) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Cat Root 1–10k SV (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Litter + Urine Root 10–25k SV (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP Home + Eliminator + Brand Root 10–25k SV (Exact) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL (all campaigns)** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*(A 16th campaign, "SP PT Pet Odor Eliminator", also exists and was likewise at zero in this window.)*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Sales:** $0.00. **ACOS / ROAS:** not applicable — no spend and no sales.
- **Best campaign / worst campaign:** none stands out because none served ads. Nothing spent money and
  nothing made money.
- **Wasted spend / negatives to add:** none this period — there was no spend to waste. (Once ads are
  live again, the standard checks resume: high-spend/no-sale terms become negative keywords.)
- **Well-converting search terms to add as exact-match:** none — there were no clicks or conversions to
  learn from.
- **Bigger picture:** the account has made **$0 in ad sales over the last 30 days** while spending only
  ~$6. This isn't a keyword or bidding problem; the ads simply aren't being shown at any meaningful
  volume.

### What to do next
1. **Fix the payment method** on the US Amazon Ads account (it currently reads as invalid). This is the
   single most likely blocker to ads serving.
2. **Confirm the campaigns can actually spend** once billing is fixed — check they aren't out of budget
   or bid too low. Current daily budgets ($1.50–$2.50) are very small; consider raising the few core
   campaigns to a level that can gather data.
3. **Re-run this report in 2–3 days** after the above. If impressions and clicks appear, we can begin
   real optimisation (negatives, exact-match harvesting, bid tuning).
4. Housekeeping: correct the stored `AMZ_PROFILE_ID` to the numeric US profile ID so the credential
   matches what the report actually uses.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the baseline (first) run.** Future 2-day reports will show
the change in each headline metric (impressions, clicks, spend, sales, ACOS, ROAS) versus this one, as
both an absolute number and a percentage.

For reference, this run's headline numbers to compare against next time:

| Metric | This report (Sep 5–6) |
|---|---:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| ACOS | n/a |
| ROAS | n/a |

**Trend:** cannot be judged yet (no prior period). The priority is getting the account serving ads
again so there is data to trend.

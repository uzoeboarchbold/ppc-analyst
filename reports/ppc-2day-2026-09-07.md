# PPC 2-Day Report — Thu 3 Sep & Fri 4 Sep 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Window covered:** 2026-09-03 (Thu) → 2026-09-04 (Fri), 2 full days
**Report generated:** 2026-09-07 (data ends 48h before run, as required)
**Currency:** USD

---

## ⚠️ Read this first — the ads stopped running

Good news: the Amazon Ads connection is working fine. Bad news: **there was no
advertising activity at all on the two days this report covers.** Every campaign
shows 0 impressions, 0 clicks, 0 spend and 0 sales for Sep 3 and Sep 4.

This is **not** a data error. I double-checked by pulling the last 30 days. The
account was running (very small, but running) and then delivery collapsed:

| Day | Impressions | Spend |
|---|---:|---:|
| Mon 1 Sep | 234 | $0.08 |
| Wed 2 Sep | 53 | $0.00 |
| **Thu 3 Sep** | **0** | **$0.00** |
| **Fri 4 Sep** | **0** | **$0.00** |

**Most likely cause:** the US advertising account has **no valid payment method on
file** (Amazon reports `validPaymentMethod: false` for this profile). When the card
fails, Amazon stops serving your ads — which matches the drop to zero. **Fixing the
payment method in Seller Central → Campaign Manager is almost certainly what's needed
to switch the ads back on.**

*(One config note for whoever maintains this: the `AMZ_PROFILE_ID` secret is set to an
application ID rather than the numeric ad-profile ID. I worked around it automatically
by using the correct US profile `26765323558215`, but it's worth correcting the secret.)*

---

## Part A — Data table (per campaign)

All figures are for Sep 3–4 combined. Every active campaign returned zero for the
window, so CTR / CPC / ACOS / ROAS are not calculable (—).

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto — B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV — Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV — Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV — Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV — Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV — Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV — Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(These are the campaigns Amazon returned rows for. Other campaigns in the account
were likewise not serving. Search-term / keyword report also returned no rows, because
there were no clicks to attribute.)*

---

## Part B — Plain-English summary

- **Total spend:** $0.00. **Total sales:** $0.00. **ACOS / ROAS:** n/a (no spend, no sales).
- **Best campaign / worst campaign:** none — nothing ran, so there's nothing to rank.
- **Wasted spend / negatives to add:** none this period (you can't waste money you didn't
  spend). No new negative-keyword suggestions.
- **Well-converting search terms to add as exact-match:** none available — there were no
  clicks or conversions in the window to learn from.
- **What to do next (in order):**
  1. **Check the payment method** on the US ad account in Seller Central → Campaign
     Manager. Amazon shows no valid payment method, which stops ads from running. This is
     the single most likely reason for the zero delivery.
  2. Confirm the **daily budget** ($40/day is set) hasn't been exhausted or the account
     paused at portfolio level.
  3. Once ads are live again, watch for the first day of impressions returning and I'll
     resume normal performance reporting on the next run.
  4. **Fix the `AMZ_PROFILE_ID` secret** to `26765323558215` so future automated runs
     don't have to auto-detect the profile.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first report of this type, so there is
nothing to compare against yet. From the next run onward this section will show each
headline metric (spend, sales, ACOS, ROAS, impressions, clicks) as a change vs. this
report, in both absolute and percentage terms.

For context (not a formal comparison), the two days *before* this window also trended
toward zero: Sep 1 had 234 impressions and $0.08 spend; Sep 2 had 53 impressions and
$0.00 spend; Sep 3–4 had 0. The direction is clearly **worsening** — delivery has fallen
to nothing — and the likely reason is the payment-method issue noted above.

---

*Prepared automatically by the PPC Analyst routine. Data source: Amazon Advertising API
(Sponsored Products, v3 reporting), US profile 26765323558215.*

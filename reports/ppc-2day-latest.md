# PPC 2-Day Report — Nov 8–9, 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Amazon.com, USD)
**Report window:** 2026-11-08 to 2026-11-09 (2 full days, ending 48h before the run to allow for Amazon's data lag)
**Generated:** 2026-11-12 23:10 UTC
**Ad product:** Sponsored Products

---

## ⚠️ Read this first — your ads are not running

Good news: the data pulled fine, the account is reachable, and everything below is real (no invented numbers).

The problem: **your Sponsored Products ads delivered nothing in this period — zero impressions, zero clicks, zero spend, and zero ad sales.** This is not a one-off. When I checked the previous two weeks (Oct 27 – Nov 9), every single day was also zero. The ads have effectively been switched off.

**Most likely cause:** the US advertising account shows **no valid payment method** (`validPaymentMethod = false`). Amazon stops serving all ads the moment billing fails, which fits what we see — 15 campaigns switched on, but not a single impression.

**What that means for you:** right now your products are not being advertised at all, so you're getting no PPC traffic or PPC-driven sales. Every day this stays broken is a day of lost ad sales.

**Fix (do this first):** In Seller Central → **Advertising → Billing** (or Account Info → Payment Methods), add/update a valid credit card and clear any outstanding ad balance. Delivery usually resumes within a few hours of a valid card being accepted. Once it's running again, these reports will start showing real numbers.

*(Technical note: the configured `AMZ_PROFILE_ID` was set incorrectly — it held an application ID instead of a numeric profile ID. I auto-detected the correct US profile and used it, so reporting still worked. This is logged for future runs and doesn't need any action from you unless you reconfigure credentials.)*

---

## Part A — Data table (per campaign)

All 15 enabled campaigns were eligible to serve but recorded no activity in the window. Top-of-search impression share cannot be calculated when there are no impressions (shown as "n/a").

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV … Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Phrase | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Phrase | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV … Exact | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | n/a | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **n/a** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(32 further campaigns are paused and 7 are archived; none served either. Full campaign names shortened for readability — they share the same ASIN group 6K-PZMX-MTDZ / B0FXW3GW5F.)*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00
- **Overall sales (from ads):** $0.00
- **ACOS / ROAS:** Not applicable — with no spend and no sales there is nothing to measure.
- **Best campaign / worst campaign:** None stood out, because none ran. There is no performance to rank.
- **Wasted spend / negatives to add:** None — you can't waste spend when nothing is spending. (Once ads are live again, this section will flag high-spend, no-sales search terms to add as negatives.)
- **Well-converting search terms to add as exact-match:** None available — there were no clicks or conversions to learn from this period.

**What to do next (in order):**
1. **Fix the payment method** in Seller Central → Advertising → Billing. This is the single blocker — nothing else matters until ads can serve.
2. **Confirm delivery resumed:** a few hours after fixing billing, check that impressions start appearing in the Advertising console.
3. **Re-run this report** once ads have been live for a couple of days so we get real numbers to optimise against.
4. Optionally, review the 15 enabled campaigns' budgets/bids while delivery is paused, so they're ready to perform the moment billing is restored.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run, so there is nothing to compare against.** A baseline is saved as of today; the next 2-day report will compare its headline metrics (spend, sales, ACOS, ROAS, impressions, clicks) against this one.

| Metric | This report | Previous | Change (#) | Change (%) |
|---|--:|--:|--:|--:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** No trend yet (first report). The headline for today is operational, not performance: ads are not serving, almost certainly due to a billing/payment-method issue that needs fixing before any optimisation can happen.

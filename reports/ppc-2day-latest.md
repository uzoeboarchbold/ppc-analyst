# PPC 2-Day Report — 16–17 Oct 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products, USD)
**Dates covered:** 16 Oct 2026 and 17 Oct 2026 (2 full days)
**Run:** 20 Oct 2026 23:10 UTC (data ends ~48h before run, per Amazon's reporting lag)
**Compared against:** previous 2-day report — `ppc-2day-2026-08-16.md` (covers 13–14 Aug 2026)

---

## ⚠️ Read this first

**1. The ads are not running. Zero impressions, zero spend, zero sales over the two days.**
The most likely reason: the US advertising account currently has **no valid payment method**
(`validPaymentMethod = false`). Without a valid card on file, Amazon will not put your ads into
the auction, so they show to nobody. In August there was still a trickle of impressions (72 over
two days); now it is a flat zero — consistent with the payment method having lapsed. **Please add/fix
the payment method on the Amazon Ads account.** Budget is not the problem (the $40/day budget is set;
spend is $0).

**2. `AMZ_PROFILE_ID` is still set to the wrong value.** It contains an *application* ID
(`amzn1.application.…`), not a numeric advertising profile ID. I automatically used the correct US
profile (`26765323558215`) so this report could run, but please update the environment variable to
`26765323558215` so future runs don't have to work around it. (The August reports already flagged this.)

**3. The report could not be emailed.** This automated environment has no email/Gmail tool connected,
only Google Drive and GitHub. The report has been saved to the repo and uploaded to the Google Drive
"PPC Reports" folder, but the "email to uzoebo.archbold@gmail.com" step could not be completed. Connect
an email tool (or a Gmail connector) to enable automatic sending.

The data below was pulled successfully from the Amazon Ads API — the zeros are real, not a data error.

---

## Part A — Data table (per campaign)

All 15 enabled campaigns recorded **no impressions, clicks, spend or sales** in the window, so every
row is zero. CPC, ACOS and ROAS are undefined (—) because there was no spend and no sales.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1–10k SV — Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10–25k SV — Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Phrase | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray Phrase | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator Phrase | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10–25k SV — Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV — Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV — Phrase | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV — Exact | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Tunnel Bed Pink — Exact Ranking (Louise) | 0 | — | 0 | 0% | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **0%** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(32 further campaigns are Paused and 7 Archived; none delivered either.)*

---

## Part B — Summary (plain English)

**The short version: your ads did not run at all over these two days. Nothing was shown, nothing was
spent, nothing was sold.**

- **Spend:** $0.00
- **Sales:** $0.00
- **ACOS / ROAS:** Not applicable — you can't have a cost-of-sale or return on ad spend when there was
  no spend and no sales.
- **Impressions:** 0. Not "a few" — literally none. Your 15 enabled campaigns showed to zero shoppers.
- **Clicks / Purchases:** 0 and 0.

**Best / worst campaign:** There is no best or worst to call out — every campaign delivered exactly
zero. The difference between them is meaningless while nothing is being served.

**Wasted spend (negatives to add):** None — there was no spend to waste, so no wasteful search terms
to add as negatives this period.

**Well-converting search terms to add as exact-match:** None — with no clicks there is no search-term
data, so there is nothing to promote to exact match this period.

**Why this is happening (most likely):** Zero impressions across every enabled campaign almost always
means the ads are not eligible to enter the auction at all. The strongest signal here is that the US
advertising account shows **no valid payment method on file**. Amazon stops serving ads when it can't
bill them. Back in August a payment method was still working (you got a small trickle of impressions);
now it's a complete stop, which fits a card having expired or been removed.

**What to do next (in order):**
1. **Fix the payment method** on the Amazon Ads account (Billing → payment settings). This is almost
   certainly the blocker. Nothing else matters until ads can serve.
2. **Correct `AMZ_PROFILE_ID`** to `26765323558215` so these reports stop having to guess the account.
3. Once ads are serving again, **check bids and eligibility** — in August, top-of-search share was only
   1–14% with zero clicks, which suggested bids under the market clearing price. Revisit bids then.
4. **Re-check in the next report.** If impressions are still zero after the payment method is fixed,
   the next step is to confirm campaign eligibility (listing active, Buy Box held on ASIN B0FXW3GW5F).

---

## Part C — Comparison to previous 2-day report (13–14 Aug 2026)

> Note: the previous report of this type is from mid-August — there appears to be a ~2-month gap with
> no 2-day reports in between, so this is not a like-for-like consecutive comparison.

| Metric | This report (16–17 Oct) | Previous (13–14 Aug) | Change | % change |
|---|---:|---:|---:|---:|
| Impressions | 0 | 72 | −72 | −100% |
| Clicks | 0 | 0 | 0 | — (0→0) |
| Spend | $0.00 | $0.00 | $0.00 | — (0→0) |
| Sales | $0.00 | $0.00 | $0.00 | — (0→0) |
| ACOS | n/a | n/a | — | — |
| ROAS | n/a | n/a | — | — |

**Verdict: worsened on delivery.** Spend and sales are unchanged (both still $0), but impressions have
gone from a tiny trickle (72) to **zero** — the account has gone completely dark. The probable cause is
the US advertising account no longer having a valid payment method. Efficiency metrics (ACOS/ROAS)
remain not applicable because there has been no spend throughout.

# PPC 2-Day Report — Sat 21 Nov & Sun 22 Nov 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (USD)
**Reporting window:** 2026-11-21 (Sat) and 2026-11-22 (Sun), full 2 days
**Generated:** 2026-11-25 (data lagged 48h as required)
**Ad type:** Sponsored Products

---

## ⚠️ Read this first — the ads are not running

There were **no Sponsored Products impressions, clicks, spend or sales** on either
day. This is **not** a data error. I successfully pulled the data from Amazon and
cross-checked a wider 14-day window: all 15 of your "enabled" campaigns show
**zero delivery for the past two weeks**, not just these two days.

The most likely reason: your **US Advertising account has no valid payment method**
on file (`validPaymentMethod: false`). When Amazon can't charge the account, it
stops serving your ads even though the campaigns are switched on. Nothing is wrong
with the campaigns themselves — they're simply blocked from spending.

**One fix solves this:** add/update a valid payment method on the US Amazon Ads
account (Advertising console → Billing). Delivery should resume automatically.

A note on setup I worked around: the stored `AMZ_PROFILE_ID` credential is invalid,
so I resolved your real US profile automatically and used that. No action needed
from you, but see "What to do next" for a permanent fix.

---

## Part A — Data table (per campaign)

All figures are for 21–22 Nov 2026 combined. Every enabled campaign returned zero
activity, so every row is zero.

| Campaign | Impr. | TOS Impr. Share | Clicks | CTR | Purchases | Sales | Total Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Auto | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 enabled campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(32 further campaigns are PAUSED and 7 are ARCHIVED; none delivered either.)*
*"—" = not calculable with zero impressions/clicks/spend.*

---

## Part B — Plain-English summary

- **Total spend:** $0.00
- **Total sales (ad-attributed):** $0.00
- **ACOS / ROAS:** Not applicable — you can't have a cost-of-sales ratio when there
  was no cost and no sales.
- **Best campaign / worst campaign:** None stood out, because none ran.
- **Wasted spend / negatives to add:** None — there was no spend to waste. (Can't
  identify negative keywords without click data.)
- **Search terms to add as exact-match:** None available — no search-term data is
  generated while ads aren't serving.

**The single issue:** your ads aren't being delivered. Everything downstream
(keywords, bids, negatives, ACOS tuning) is on hold until delivery resumes. The
campaigns are built and enabled; they just can't spend.

### What to do next
1. **Fix billing (highest priority).** Go to Amazon Advertising console → Billing
   and add a valid payment method / card for the US account. This is almost
   certainly what's stopping delivery.
2. **Confirm delivery resumes.** Within a day of fixing billing, you should start
   seeing impressions again. The next 2-day report will confirm it.
3. **Permanent credential fix (for me).** The `AMZ_PROFILE_ID` stored for my
   automation is invalid; I'm compensating by resolving the US profile
   (`26765323558215`) each run, but it's worth correcting the stored value so the
   automation is clean.
4. Once ads are live again, I'll resume normal optimisation: flag wasted spend,
   suggest negatives, and surface converting search terms to add as exact-match.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** on file — this is the first one, so it sets
the baseline.

| Metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |

**Verdict:** No trend to report yet. The headline for the baseline is that the
account is not delivering ads — fixing billing is the one thing that will change
these numbers next time.

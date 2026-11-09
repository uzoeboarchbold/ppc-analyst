# PPC 2-Day Report — Nov 5–6, 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace) · Sponsored Products
**Window covered:** 2026-11-05 to 2026-11-06 (2 full days, ending 48h before the run to let Amazon's data finalise)
**Report generated:** 2026-11-09
**Delivery:** Saved to repo + uploaded to Google Drive 'PPC Reports'. Email was **not** sent — the Gmail connector is not enabled for this automated session (see note at the end); you were notified by push instead.

---

## ⚠️ Read this first — your ads did not run

I pulled the data successfully, but every number below is **zero**. This is **not** a reporting error on my side — the Amazon login, the account, and the reports all worked. The reason is on the account:

- Your US Amazon Ads account shows **no valid payment method on file** (`validPaymentMethod: false`).
- Because of that, Amazon is **not serving any of your Sponsored Products ads**, even though **15 campaigns are switched ON**.
- Result: **0 impressions, 0 clicks, 0 spend, and 0 sales from PPC** on Nov 5 and Nov 6. To be sure this wasn't just a quiet two days, I also checked the **whole of Oct 10 – Nov 6, and it was zero the entire time** — so the ads have been dark for at least a month.

**What to do (this is the one thing that matters):** Log in to Amazon and **add or update the payment/billing method** for the US account.
- Amazon Ads console → **Billing & payments** → add a valid card, **or**
- Seller Central → **Settings → Account Info → Charge Methods / Deposit Methods**.

Once billing is valid, your 15 enabled campaigns should start delivering again within a few hours, and future reports will show real numbers.

*(Technical note for whoever set up this automation: the `AMZ_PROFILE_ID` environment variable is set to an application ID — `amzn1.application...` — not a numeric Amazon Ads profile ID. I automatically used the correct US profile `26765323558215`, the only one of your three profiles (US/CA/MX) that has campaigns. Please fix the variable so future runs are unambiguous.)*

---

## Part A — Data Table (by campaign)

All 15 **enabled** campaigns were reported; all delivered zero because ads were not served. "TOS IS" = Top-of-search impression share.

| Campaign | Impr. | TOS IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP Isolated – Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV – Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV – Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV – Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV – Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV – Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV – Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Auto | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(32 further campaigns are PAUSED and 7 are ARCHIVED; they are excluded as expected.)*

---

## Part B — Plain-English Summary

- **Overall spend:** $0.00 · **Sales:** $0.00 · **ACOS:** n/a · **ROAS:** n/a (no ads served).
- **Best / worst campaign:** Not applicable — none of them ran, so there's nothing to rank.
- **Wasted spend / negatives to add:** None to flag — you spent nothing. (The real "waste" is lost sales from ads being off.)
- **Well-converting search terms to add as exact-match:** None available — with no clicks there are no search terms to harvest.
- **What to do next:**
  1. **Fix billing** on the US account (see the box at the top). This is the only blocker.
  2. After ads resume, give it 2–3 days, then this report will show live spend, sales, ACOS and ROAS.
  3. Separately, have whoever manages the setup correct the `AMZ_PROFILE_ID` variable.

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists** — this is the first run of this report type, so there is no baseline to compare against. This run becomes the baseline. Headline metrics this period: Spend $0.00, Sales $0.00, ACOS n/a, ROAS n/a.

| Metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** Baseline run. Things can't be called better or worse yet — but the account is currently losing all potential ad-driven sales because ads aren't being served. Fixing the payment method is urgent.

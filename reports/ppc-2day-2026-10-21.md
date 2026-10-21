# PPC 2-Day Report — 17–18 October 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products)
**Window covered:** Saturday 17 Oct – Sunday 18 Oct 2026 (2 full days)
**Generated:** 21 Oct 2026 (data ends 48h before run, per Amazon's reporting lag)
**Report type:** 2-day | **Compared against:** no prior 2-day report (first run)

---

## ⚠️ Read this first

**The account spent nothing and served no ads during this window — and has served no ads at all so far in October.** This is not a data error. The Amazon Ads API pulled cleanly; the numbers are genuinely zero.

The most likely cause: **the US advertising profile has no valid payment method on file** (`validPaymentMethod: false`). Amazon will not run campaigns without a working payment method, even when the campaigns are switched on. **Fixing the payment method in Seller Central / the Ads console is the single most important action — until that is resolved, no campaign can spend or make sales.**

Two config issues also worth knowing (details at the bottom):
1. The `AMZ_PROFILE_ID` credential is set to an **application ID**, not a profile ID. I used the correct US profile automatically, but this should be corrected so future runs are unambiguous.
2. **Email could not be sent.** The Gmail connector is connected but not enabled for automated use in this session, so I could not email this report. It has been saved to the repo and uploaded to Google Drive. Please enable Gmail in chat, or retrieve the report from Drive.

---

## Part A — Data table (by campaign)

All 15 Sponsored Products campaigns target one product (ASIN **B0FXW3GW5F**, a cat deterrent / pet-odor product). For 17–18 Oct the API returned **no activity rows** — every campaign recorded zero impressions, so every derived metric is zero or not applicable.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*"IS" = impression share. "—" = not applicable when there are no impressions/clicks.*

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Sales:** $0.00. **ACOS / ROAS:** not applicable — you can't have a cost-of-advertising ratio when there was no advertising.
- **Best / worst campaign:** none stands out either way — all 15 campaigns were equally inactive.
- **Wasted spend / negatives:** none to flag. You can only waste spend if ads are running; here nothing ran.
- **Well-converting search terms to add as exact-match:** none available — no clicks or search-term data were generated in this window.
- **What to do next (in order):**
  1. **Fix the payment method on the US Amazon Ads account.** This is almost certainly why nothing is serving. Confirm a valid card/bank is attached and the account is in good standing.
  2. Once ads are live again, re-check within 48h that impressions and spend are flowing on the enabled campaigns.
  3. The campaigns themselves look structured and ready (auto + manual exact/phrase, sensible daily budgets of $1.50–$2.50). No structural change is needed right now — the blocker is billing, not setup.
  4. Correct the `AMZ_PROFILE_ID` credential (see below) so reporting is unambiguous.

---

## Part C — Comparison to previous 2-day report

This is the **first 2-day report**, so there is no prior report to compare against. Headline metrics for the record:

| Metric | This report | Previous | Change |
|---|--:|--:|:--|
| Spend | $0.00 | — | n/a (first run) |
| Sales | $0.00 | — | n/a (first run) |
| ACOS | n/a | — | n/a (first run) |
| ROAS | n/a | — | n/a (first run) |

**Overall:** baseline established. The next 2-day report will compare against these figures. The headline to watch is whether spend and sales move above zero once the payment method is fixed.

---

## Technical notes (for whoever maintains this)

- **Data source:** Amazon Advertising API v3 reporting (`/reporting/reports`), Sponsored Products, US seller profile `26765323558215`. Reports pulled at campaign, targeting, and search-term level — all returned empty for 17–18 Oct.
- **Sanity check:** a wider pull (1–18 Oct) returned all 15 campaigns with **zero** impressions/clicks/cost/sales, confirming the account has not served ads this month. CA and MX profiles have no campaigns and no activity either.
- **Likely root cause:** US profile `validPaymentMethod: false`.
- **`AMZ_PROFILE_ID` misconfigured:** the env var contains `amzn1.application.…` (an application ID), not a numeric profile ID. The correct US profile was selected automatically from the account's profile list.
- **Email not sent:** Gmail connector present but not enabled for automated sending in this environment. Report saved to repo and uploaded to the "PPC Reports" Google Drive folder instead.

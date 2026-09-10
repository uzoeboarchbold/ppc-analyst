# PPC 2-Day Report — 6–7 September 2026

**Marketplace:** Amazon US (Sponsored Products) · Seller: Uzoebo Archbold E-Commerce
**Dates covered:** 2026-09-06 and 2026-09-07 (2 full days, ended 48h before the run to allow for data lag)
**Report generated:** 2026-09-10 (run type: 2-day)
**Currency:** USD

---

## ⚠️ Read this first — ads served nothing in this window

There were **no impressions, no clicks, no spend and no sales on any campaign**
across both days. The API pull worked correctly — the account genuinely had
**zero ad delivery** on 6–7 September.

This is almost certainly because the **US marketplace has no valid payment
method on file** (Amazon flags this account as `validPaymentMethod: false`).
Amazon pauses ad delivery when it cannot bill, so the campaigns are live in
name but not actually showing.

For context, over the **last 28 days (Aug 11 – Sep 7)** the whole US account
delivered only **1,860 impressions, 17 clicks, $5.93 spend and $0.00 sales** —
so this is not a one-off quiet couple of days; the account is effectively
dormant and has produced no ad-attributed sales in a month.

Two setup issues were found and worked around (details at the bottom):
1. The `AMZ_PROFILE_ID` credential is wrong (it holds an application id, not a
   numeric profile id). I selected the correct US profile automatically.
2. Canada and Mexico profiles exist but have no Sponsored Products campaigns.

---

## Part A — Data table (by campaign)

All figures are for 6–7 September 2026 combined. Every campaign returned zero,
so ACOS/ROAS/CTR/CPC are not calculable (no clicks or sales).

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Cat Deterrent Spray Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Cat Deterrent Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Cat Deterrent Phrase | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Pet Odor Eliminator Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 50k+ SV … Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 25-50k SV … Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Odor Root 25-50k SV … Phrase | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP Cat Root 1-10k SV … Exact | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP KT \| ST w/ Sales | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | 0% | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| **TOTAL (15 campaigns)** | **0** | **0%** | **0** | **–** | **0** | **$0.00** | **$0.00** | **–** | **–** | **–** |

*(Campaign names shortened for readability; "6K-PZMX-MTDZ B0FXW3GW5F" is the
Cat Deterrent Spray / Pet Odor Eliminator product.)*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  applicable — you can't have an advertising cost-of-sale when nothing was spent
  and nothing sold.
- **Best campaign / worst campaign:** none stand out — every campaign performed
  identically at zero. There is nothing to optimise inside the campaigns yet
  because none of them are actually running.
- **Wasted spend / negatives to add:** none for this window (you spent nothing).
  Over the last 28 days the only notable spend was ~$3.77 on *Cat Tunnel Bed
  Pink Only* with no sales — worth a look later, but tiny.
- **Well-converting search terms to add as exact-match:** none — there were no
  clicks and no sales, so there is no search-term data to harvest.
- **What to do next (in order):**
  1. **Fix the billing.** In Seller Central / Amazon Ads, add or update a valid
     payment method for the US account. This is the single thing stopping your
     ads from showing. Until it's fixed, every other optimisation is moot.
  2. **Confirm campaigns are enabled** (not paused) once billing is live.
  3. **Re-check budgets** — the account daily budget is set very low ($40); make
     sure individual campaign budgets aren't at $0 or paused.
  4. Once ads are delivering again, this report will start showing real
     impressions, clicks and sales, and I'll begin flagging wasted spend and
     good search terms to promote.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report, so
there is no prior period to compare against. Headline metrics for this window
are all zero (spend $0.00, sales $0.00, ACOS n/a, ROAS n/a). Future 2-day
reports will show the change versus this one as both a number and a percentage.

**Trend note (from a 28-day lookback for context, not a formal comparison):**
the account is not delivering and has generated $0 in ad sales over the past
month. Direction: effectively flat at zero — the priority is getting ads live,
not fine-tuning.

---

## Technical notes (for the operator)

- **Data source:** Amazon Ads API v3 async reporting (Sponsored Products),
  region NA. LWA token refresh and report pulls all succeeded.
- **`AMZ_PROFILE_ID` is invalid** — it contains an *application* id
  (`amzn1.application.…`), not a numeric Ads profile id. I listed profiles via
  `/v2/profiles` and used the correct US profile (`26765323558215`). Please fix
  this env var so future runs are unambiguous.
- **Profiles found:** US (USD, used), CA (CAD) and MX (MXN). CA and MX have no
  Sponsored Products campaigns, so US is the only relevant marketplace.
- **Verification:** campaign, targeting and search-term reports were all pulled;
  targeting and search-term reports returned zero rows, consistent with zero
  delivery. Figures here are real API values, not estimates.

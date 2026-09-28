# PPC 2-Day Report — 24–25 September 2026

**Marketplace:** Amazon US (Sponsored Products) · Account: Uzoebo Archbold E-Commerce
**Dates covered:** Thursday 24 Sep 2026 – Friday 25 Sep 2026 (2 full days)
**Generated:** 28 Sep 2026 (data finalised with the standard ~48-hour lag)
**Report type:** 2-day

---

## ⚠️ Read this first — the ads are not running

For the two days in this report your Sponsored Products ads served **nothing at
all**: 0 impressions, 0 clicks, £0 / $0 spend and $0 sales. This is not a data
error — the pull from Amazon worked and simply came back empty.

Looking wider to be sure, the account has had **zero delivery since about 10–11
September**. The last time any ads showed was earlier than that, and even then
the volume was tiny ($0.35 total spend and 782 impressions across the whole 28
days to 25 Sep, with **no sales**).

**Most likely cause:** the Amazon Ads account shows **no valid payment method**
on file. Amazon stops serving ads when it cannot bill them. Until a working card
is added, every enabled campaign stays live in the dashboard but shows to nobody.

**Two small housekeeping notes (handled automatically, no action needed):**
- The `AMZ_PROFILE_ID` credential is set to an application ID rather than a
  numeric profile ID, so it was ignored and the correct US profile was used
  instead. Worth fixing at source when convenient.
- The report could not be emailed this run because the Gmail connector is
  switched off for this automated session. It has still been saved to the repo
  and uploaded to Google Drive. Turn Gmail on for the session to restore email.

---

## Part A — Data table (24–25 Sep 2026)

There was no delivery, so every campaign reads zero for the window. Rather than
list 15 all-zero rows, here is the account total.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **All campaigns (total)** | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |

- 15 campaigns are ENABLED, 32 are PAUSED, 7 are ARCHIVED (54 total).
- None of the 15 enabled campaigns served an impression in the window.
- CTR, CPC, ACOS and ROAS are shown as "—" because you cannot divide by zero
  clicks / zero spend / zero sales.

---

## Part B — Plain-English summary

- **Spend:** $0.00. **Sales:** $0.00. **ACOS / ROAS:** not applicable (nothing
  spent, nothing sold).
- **Best / worst campaign:** none to pick — no campaign ran, so none did well or
  badly. They are all effectively idle.
- **Wasted spend / negatives to add:** none, because there was no spend. (When
  ads restart, the first job will be to watch for clicks that cost money without
  producing sales and add those as negatives.)
- **Well-converting search terms to add as exact-match:** none available — with
  no clicks or sales in the window there are no search terms to harvest yet.

### What to do next
1. **Add a valid payment method to the Amazon Ads account.** This is almost
   certainly why nothing is serving. Everything else is secondary until ads can
   actually bill and run.
2. **Confirm the enabled campaigns still have a daily budget and live bids**
   once billing is fixed, then let them run 3–4 days to gather data.
3. **Re-run this report after delivery resumes.** Only then will spend, ACOS,
   ROAS, wasted-spend negatives and search-term harvesting become meaningful.
4. Optional housekeeping: fix the `AMZ_PROFILE_ID` credential and enable the
   Gmail connector so future reports email themselves.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report, so
there is nothing to compare against yet. From the next run onward this section
will show the change in each headline metric (impressions, clicks, spend, sales,
ACOS, ROAS) as both a number and a percentage.

For reference, the baseline this report establishes is: **0 impressions,
0 clicks, $0.00 spend, 0 purchases, $0.00 sales** for 24–25 Sep 2026.

---

*Prepared automatically by the PPC Analyst. Figures come directly from the
Amazon Advertising API (Sponsored Products, US profile). No numbers were
estimated or invented; where a metric could not be calculated it is shown as "—".*

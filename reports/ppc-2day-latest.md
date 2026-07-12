# PPC 2-Day Report — 8–9 July 2026

**Marketplace:** Amazon US (Sponsored Products) · Uzoebo Archbold E-Commerce
**Reporting window:** 2026-07-08 to 2026-07-09 (2 full days)
**Generated:** 2026-07-12 (data ends 48h before run, per Amazon's finalisation lag)
**Attribution:** 7-day click attribution. For days this recent the window is not
fully mature, so sales/ACOS shown here can only rise later, not fall.

---

## ⚠️ Read this first — advertising is effectively switched OFF

There was **no ad activity to report** for 8–9 July: **zero impressions, zero
clicks, zero spend, zero sales.** This is not a data error or a pull failure —
it was verified directly against Amazon's campaign records:

- The US account has **54 Sponsored Products campaigns**, but only **2 are
  ENABLED** ("SP KT | ST w/ Sales" and "SP PT | ST w/ Sales", $8/day each).
- **45 campaigns are PAUSED** and **7 are ARCHIVED.**
- The 2 enabled campaigns served **0 impressions** in the window — so even the
  live campaigns are not being shown to shoppers (their targeting is a narrow
  "search terms with sales" list, and/or bids are too low to win placements).

In plain terms: the account is currently not advertising. Nothing is being
wasted on spend, but the business is also getting **no PPC traffic, no
PPC-driven sales, and no new search-term data.** That is the one thing worth
acting on this week.

Two setup issues were found and worked around automatically (details at the
bottom): the `AMZ_PROFILE_ID` environment variable is misconfigured, and there
is no email tool connected, so this report was delivered to the repo and Google
Drive but could not be auto-emailed.

---

## Part A — Data table (by campaign)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP KT \| ST w/ Sales (ENABLED, $8/day) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP PT \| ST w/ Sales (ENABLED, $8/day) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (2 enabled campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*45 further campaigns are PAUSED and 7 ARCHIVED; they cannot serve and are not
shown. No keyword/target or search-term rows were returned because there were no
clicks or impressions to attribute.*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales (PPC):** $0.00. **ACOS / ROAS:** not
  applicable — you can't have an ad cost-of-sale when nothing ran.
- **Best campaign / worst campaign:** not meaningful this period — both live
  campaigns produced identical zero results.
- **Wasted spend / negatives to add:** none — there was no spend to waste and no
  search terms to prune.
- **Well-converting search terms to add as exact-match:** none available — with
  zero clicks there is no new search-term data to harvest.
- **What to do next:**
  1. **Decide if PPC should be on.** If yes, this is the priority — right now the
     brand has no paid presence on Amazon US.
  2. **Give the ads a way to actually serve.** The 2 enabled campaigns target
     only "search terms with sales," which is very narrow. Consider re-enabling
     an **Auto** campaign and a broad/phrase discovery campaign (several already
     exist, just paused: e.g. "SP Auto…", the Root Phrase campaigns) to start
     collecting impressions and search-term data again.
  3. **Check bids and budgets.** $8/day with zero impressions usually means bids
     are below the auction floor for the chosen targets — raise bids on the
     enabled campaigns or widen match types so they can win placements.
  4. **Re-run this report once ads are live** so there is real performance data
     (impressions, ACOS, ROAS, converting search terms) to optimise against.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run of this report type,
so it serves as the baseline.** Every headline metric starts at zero:

| Metric | This report (8–9 Jul) | Previous | Change (#) | Change (%) |
|---|--:|--:|--:|--:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** Baseline established. Future 2-day reports will compare against
these figures; the meaningful comparison begins once campaigns are enabled and
serving.

---

## Notes on data collection (what ran, what was worked around)

- **Data source:** Amazon Advertising API v3 reporting (`spCampaigns` and
  `spSearchTerm`), US profile `26765323558215` (USD), plus the SP campaign
  management API to verify campaign states. Auth via refresh-token succeeded.
- **`AMZ_PROFILE_ID` is misconfigured.** It contains an *application* id
  (`amzn1.application.…`), not a numeric Advertising profile id, so it cannot be
  used as the API scope. The correct US profile id was resolved automatically
  from `/v2/profiles` (the only account with real ad activity). *Fix at source:
  set `AMZ_PROFILE_ID=26765323558215`.*
- **Email not sent.** No email/Gmail tool is connected to this environment, so
  the report could not be auto-emailed to uzoebo.archbold@gmail.com. It has been
  saved to the repo `reports/` folder and uploaded to the Google Drive folder
  "PPC Reports". *To enable auto-email, connect a Gmail/email tool.*
- The zero-activity finding was cross-checked against campaign records and is
  accurate, not a symptom of any of the above.

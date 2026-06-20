# PPC 2-Day Report — 16–17 June 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (USD)
**Window covered:** Tue 16 June 2026 and Wed 17 June 2026 (2 full days)
**Run date:** Sat 20 June 2026 (data lagged 48h, as required)
**Product type:** Sponsored Products

---

## ⚠️ Read this first (plain English)

Two things you need to know:

1. **Your Sponsored Products ads ran NOTHING in this window.** Across both days
   (16–17 June) there were **zero impressions, zero clicks, zero spend and zero
   sales**. This is not a data error — I double-checked with a wider pull. The
   ads effectively went dark before ~10 June: of your 54 campaigns, 45 are
   **paused**, 7 are archived, and only **2 are enabled** — and even those 2 got
   no clicks. If you expected ads to be live, something has switched them off.

2. **Two setup problems are blocking automatic delivery** (both need a quick fix
   from you — see "Housekeeping" at the bottom):
   - The `AMZ_PROFILE_ID` setting holds the wrong value (an *application* ID, not
     an ad-account/profile ID). I worked around it automatically by looking up
     your real US profile, so the report still ran — but please fix the setting.
   - There is **no email tool connected** in this environment, so I could not
     email the report. I have saved it to the repo and uploaded it to your Google
     Drive "PPC Reports" folder instead.

---

## Part A — Data table (16–17 June 2026)

One row per enabled campaign plus the totals row. Every active and paused
campaign returned zero for the window; the two **enabled** campaigns are shown
explicitly, the rest are summarised.

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales (enabled) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales (enabled) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| All other 52 campaigns (paused/archived) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

n/a = cannot be calculated with zero impressions/clicks/spend.

---

## Part B — Summary

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS:** n/a (no spend)  •  **ROAS:** n/a (no sales)
- **Best campaign:** none — nothing ran.
- **Worst campaign / wasted spend:** none — there was no spend to waste in this
  window. (No negative-keyword suggestions are needed because nothing served.)
- **Well-converting search terms to add as exact-match:** none available from
  this window (no search-term data, because no ads served).

**Context from a wider look-back (1–17 June), for your awareness only:**
Earlier in June the account *was* spending: roughly **$140 of spend, ~30 clicks,
2 purchases and ~$26 in sales** across that fuller period — i.e. ACOS was very
high (~540%) and most clicks did not convert. The campaign that did convert was
"SP Odor Root 25–50k SV … Phrase" and the product-targeting campaign
"SP PT Pet Odor Eliminator …" (1 sale each). That spend all happened on/before
~9 June; from ~10 June onward everything reads zero.

**What to do next:**
1. **Decide if the ads should be live.** If the pause was intentional (e.g. you
   turned everything off to stop bleeding money at ~540% ACOS), then this "zero"
   report is expected and no action is needed. If it was *not* intentional,
   re-enable your priority campaigns — your two enabled campaigns aren't getting
   impressions, so check budgets/bids and campaign status in Seller Central.
2. **Before relaunching, fix the high-ACOS problem** that was showing earlier in
   June: tighten to the few converting terms, lower bids on non-converters, and
   add negatives for clicks that never convert.
3. **Fix the two setup issues** in Housekeeping so future reports deliver by
   email automatically and stop relying on the workaround.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first report of this type, so
there is no prior period to compare against. From the next run onward this
section will show each headline metric (spend, sales, ACOS, ROAS, clicks,
impressions) as a change in both absolute number and percentage.

Baseline set by this report (all zero): Impressions 0 · Clicks 0 · Spend $0.00 ·
Sales $0.00 · Purchases 0.

---

## Housekeeping (needs a quick fix from the account owner)

1. **`AMZ_PROFILE_ID` is set to the wrong value.** It currently holds
   `amzn1.application.…` (an application ID). The correct numeric US Ads profile
   is `26765323558215`. Please update the environment variable. (I auto-detected
   and used the right profile this run, so the report still completed.)
2. **No email integration.** This environment has Google Drive connected but no
   email/Gmail tool, so the "email the report" step could not run. Connect an
   email tool to enable automatic emailing, or rely on the Google Drive upload.

*Generated automatically by the PPC Analyst routine. Figures pulled live from the
Amazon Advertising API (Sponsored Products, US profile 26765323558215).*

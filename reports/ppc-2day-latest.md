# PPC 2-Day Report — 16–17 July 2026

**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Window covered:** Wed 16 July & Thu 17 July 2026 (2 full days)
**Data pulled:** 20 July 2026 (data ends 48h before run, per Amazon's reporting lag)
**Report type:** 2-day · **Compared against:** previous 2-day report

---

## ⚠️ Please read first — two things need your attention

1. **Your ads are effectively switched OFF.** Almost every campaign is
   *paused* or *archived*. Only two campaigns are still enabled
   (`SP KT | ST w/ Sales` and `SP PT | ST w/ Sales`), and even those served
   **zero impressions** — not just for these two days, but for the whole of
   the last four weeks. So there was **no spend and no sales** in this
   window. The zero figures below are real (I double-checked against a
   4-week pull), not a data error.

2. **A settings/config fix is needed (not urgent, but do it once).**
   The stored `AMZ_PROFILE_ID` value is the wrong kind of ID (it's an app
   ID, not an advertising-account ID), so I fell back to your live US
   advertising account automatically. Everything below is correct. To stop
   this note appearing, set `AMZ_PROFILE_ID` to `26765323558215`.

3. **Email not sent this run.** The Gmail connector is installed but turned
   off for this automated session, so I couldn't email the report. It has
   been saved to the repo and uploaded to Google Drive. Enable Gmail for
   this session to restore email delivery.

---

## Part A — Data table (per campaign)

Only enabled campaigns are shown. All other campaigns are paused/archived
and served nothing.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*n/a = cannot be calculated because there were no impressions/clicks/spend.*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS / ROAS:** Not applicable — you can't have an advertising cost of
  sale or a return on ad spend when nothing was spent.
- **Best / worst campaign:** No campaign delivered anything, so there is no
  best or worst to name. The two enabled campaigns simply didn't serve ads.
- **Wasted spend / negatives to add:** None — there was no spend to waste,
  and no search terms to add as exact-match or block as negatives, because
  no clicks or impressions happened.

**Why this is happening (most likely):** the two enabled campaigns are on,
but their ad groups, keywords, or products underneath are likely paused,
their bids are too low to win any placement, or the advertised product is
out of stock / not buyable. An enabled campaign with a live budget that
still gets *zero* impressions almost always means the problem is one level
down (ad group / target / listing), not the campaign switch itself.

**What to do next (in order):**
1. Decide whether you *want* PPC running right now. If yes, this is the main
   action — nothing else matters until ads are delivering again.
2. Open the two enabled campaigns and check the layer beneath them: are the
   ad groups enabled, are there active keywords/targets, and are the bids
   competitive (try raising to suggested bid)?
3. Confirm the advertised product (ASIN `B0FXW3GW5F` and the cat-tunnel-bed
   ASINs) is in stock and has the Buy Box — ads won't serve otherwise.
4. Once impressions return, come back to this report cadence to watch ACOS,
   wasted spend and winning search terms — none of which can be assessed
   while spend is $0.
5. One-time: set `AMZ_PROFILE_ID=26765323558215` and enable the Gmail
   connector for this automated session.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report,
so there is nothing to compare against yet. From the next 2-day run onward,
this section will show the change in each headline metric (impressions,
clicks, spend, sales, ACOS, ROAS) as both a number and a percentage, with a
one-line verdict on whether things improved or worsened.

For the record, the baseline these figures set is: **Impressions 0 ·
Clicks 0 · Spend $0.00 · Sales $0.00 · ACOS n/a · ROAS n/a.**

---

*Generated automatically by the PPC Analyst routine. Figures are pulled
live from the Amazon Advertising API (Sponsored Products, US profile
26765323558215). No numbers are estimated or invented; where a metric
couldn't be pulled or calculated it is shown as n/a with the reason.*

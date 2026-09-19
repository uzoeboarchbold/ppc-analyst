# PPC 2-Day Report — Tue 15 Sep to Wed 16 Sep 2026

**Marketplace:** Amazon US (profile 26765323558215, USD) · **Ad product:** Sponsored Products
**Report run:** 2026-09-19 (Sat) · **Data window:** 2026-09-15 → 2026-09-16 (2 full days, ending 48h before run)
**Report type:** 2-day · **Compared against:** previous 2-day report (none yet — this is the first)

---

## ⚠️ Note on this run (please read)

Two things worth knowing:

1. **A settings value is wrong, but the report still ran.** The stored
   `AMZ_PROFILE_ID` actually holds an *application* ID
   (`amzn1.application…`), not a real Amazon Ads profile ID, so it can't be
   used to pull data. I looked up the account's real profiles and used the
   **US** one (the main marketplace). No numbers were invented. *Fix for
   later: set `AMZ_PROFILE_ID` to `26765323558215` for US.* (CA and MX
   profiles also exist if you want them covered too.)

2. **There was no ad activity in these two days.** Every campaign shows
   zero impressions, clicks, spend and sales for 15–16 Sep. This is real
   data, not an error. For context, the whole last 30 days only saw ~1,580
   impressions, 16 clicks, **$3.77** spend and **0 sales** — the account is
   in very early ramp-up and is barely serving yet.

3. **Email could not be sent automatically.** The Gmail connector is
   connected to the account but is not enabled for this automated session,
   so the tool to send email is unavailable here. The report was still saved
   to the repo and uploaded to the Google Drive "PPC Reports" folder. *Fix
   for later: enable the Gmail connector for this session/chat so future
   runs can email the report.*

---

## Part A — Data table (by campaign)

All figures are for 15–16 Sep 2026. Every active Sponsored Products campaign
returned zero for the window.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Cat Root 1-10k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Cat Deterrent Spray Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Eliminator Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Phrase | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP Odor Root 50k+ SV 6K-PZMX-MTDZ B0FXW3GW5F Exact | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | $0.00 | n/a | n/a |
| **TOTAL (15 campaigns)** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **$0.00** | **n/a** | **n/a** |

*"n/a" means the metric can't be calculated because there were no clicks/impressions (e.g. you can't divide by zero for CTR, ACOS or ROAS).*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  applicable — nothing was spent, so there's nothing to measure efficiency on.
- **Best campaign / worst campaign:** none stand out — every campaign was flat
  at zero for these two days, so there's no winner or loser to call out yet.
- **Wasted spend / negatives to add:** none. You can't waste money you didn't
  spend. No negative keywords are needed from this window.
- **Search terms to add as exact-match:** none available. With zero clicks and
  zero conversions in the window there are no converting search terms to harvest.
- **Bigger picture:** the ads are effectively not running. Across the last 30
  days the account has spent only $3.77 and made 0 sales, so the campaigns are
  live-but-dormant rather than actively competing.

### What to do next
1. **Fix the profile setting** so future automated pulls are reliable: set
   `AMZ_PROFILE_ID` to `26765323558215` (US).
2. **Check why the ads aren't serving.** Zero impressions on 15 exact/phrase
   campaigns almost always means one of: (a) bids too low to win the auction,
   (b) daily budgets set very low or exhausted, (c) campaigns paused or inside
   a scheduled off-period, or (d) low listing/keyword relevance. Start by
   raising bids on 2–3 priority campaigns (e.g. the Pet Odor Eliminator and
   Cat Tunnel Bed campaigns, which have drawn the most impressions recently)
   and confirm budgets are set to a meaningful daily amount.
3. **Watch the click that isn't converting.** The Cat Tunnel Bed campaign got
   16 clicks over 30 days but 0 sales — once traffic resumes, check the product
   page (price, images, reviews) so paid clicks can actually convert.
4. **Re-assess after the ads are serving.** Once there is real spend, the next
   reports can start optimising ACOS, negatives and search-term harvesting.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first
one, so it serves as the baseline.

| Metric | This report (15–16 Sep) | Previous | Change (#) | Change (%) |
|---|---|---|---|---|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Orders | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** No trend yet — baseline established. Future 2-day reports will
show the up/down change here.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting), US profile 26765323558215. Metrics use 7-day/14-day attribution as provided by the API. Report generated automatically.*

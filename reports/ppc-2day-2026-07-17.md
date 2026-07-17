# PPC 2-Day Report — 13–14 Jul 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon US (Sponsored Products, USD)
**Dates covered:** 13 Jul 2026 and 14 Jul 2026 (2 full days, ending 48h before the 17 Jul run to allow Amazon's ~48h data lag)
**Generated:** 17 Jul 2026

---

## ⚠️ Headline: the ads are switched off

There was **no advertising activity at all** in this window. Zero impressions,
zero clicks, zero spend, and zero ad-driven sales on both 13 and 14 July.

This is not a data error. To be sure, I also pulled the **last 30 days**
(21 Jun – 14 Jul) and it is **zero across every single day**. The US Sponsored
Products account has been completely dark for at least a month.

**Why:** almost every campaign is **PAUSED**. Only two campaigns are switched
to ENABLED — *"SP KT | ST w/ Sales"* and *"SP PT | ST w/ Sales"* — but even
these served **0 impressions**, so they are enabled in name only (most likely
they have no active keywords/targets, bids that are too low to win any auction,
or nothing to spend against). Net effect: the account is spending nothing and
earning nothing from ads.

*Two delivery notes for this run (see "Notes" at the bottom): the `AMZ_PROFILE_ID`
provided in the environment was not a usable profile ID, so I looked the account
up directly; and there is no email tool wired up in this environment, so this
report was delivered to the repo and Google Drive but could not be emailed.*

---

## Part A — Data table (13–14 Jul 2026)

One row per campaign that the API returned for the window (only the 2 ENABLED
campaigns appear; all other campaigns are paused and returned no data).

| Campaign | Status | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | ENABLED | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales | ENABLED | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | — | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*All other campaigns (approx. 48+, e.g. the "Cat Deterrent Spray" / "Pet Odor
Eliminator" campaigns for ASIN B0FXW3GW5F) are PAUSED and served nothing.*
*Top-of-search impression share, CTR, CPC, ACOS and ROAS are undefined ("n/a")
because there were no impressions, clicks or spend to calculate them from.*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00. **Overall sales (from ads):** $0.00.
- **ACOS / ROAS:** not applicable — you can't have a return on $0 of ad spend.
- **Best campaign / worst campaign:** none to pick — nothing ran.
- **Wasted spend:** none, because there was no spend. (The flip side is also
  true: no ads means no new ad-driven customers or ranking momentum.)
- **Search terms to add as exact-match:** none available — with no clicks there
  are no converting search terms to harvest this period.
- **The one thing that matters:** your Sponsored Products ads have been **off for
  at least 30 days**. If that's deliberate (e.g. out of stock, seasonal pause,
  or a rebuild in progress), no action needed. If it's *not* deliberate, you are
  invisible in paid placements and leaving sales on the table.

### What to do next
1. **Confirm it's intentional.** Decide whether the account should be advertising
   right now. If yes, it currently isn't.
2. **Check the two ENABLED campaigns** ("SP KT | ST w/ Sales" and
   "SP PT | ST w/ Sales"). They're switched on but delivering nothing — check
   that they contain active keywords/targets, that bids are high enough to win
   impressions, and that the daily budget (account default is $40/day) isn't the
   blocker.
3. **Check the product is sellable.** Ads won't serve if the ASIN (B0FXW3GW5F) is
   out of stock, suppressed, or has lost the Buy Box — worth a quick look.
4. **Re-enable a small, controlled set** of your previously-working campaigns
   (or fix the two enabled ones) if you want spend to resume, then let this daily
   report track performance from day one.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report, so
there is nothing to compare against yet. From the next run onward, this section
will show the change in each headline metric (spend, sales, ACOS, ROAS) as both
a number and a percentage.

For context instead, here is the recent trend from the diagnostic pull:

| Metric | 13–14 Jul (this report) | Prior 28 days (21 Jun–12 Jul) | Trend |
|---|---:|---:|---|
| Impressions | 0 | 0 | flat (dark) |
| Clicks | 0 | 0 | flat (dark) |
| Spend | $0.00 | $0.00 | flat (dark) |
| Ad sales | $0.00 | $0.00 | flat (dark) |

**Verdict:** unchanged — the account has been consistently dark, not a sudden
drop this window. Nothing "worsened"; it simply hasn't been running.

---

### Notes (for transparency)
- **Profile lookup:** the `AMZ_PROFILE_ID` supplied in the environment was an
  *application* ID, not a numeric Ads profile ID, so it could not be used as the
  API scope. I listed the account's profiles and used the active **US** profile
  (26765323558215, USD). The CA and MX profiles have no campaigns.
- **Email delivery:** no email-sending tool is available in this environment, so
  this report could **not** be emailed to uzoebo.archbold@gmail.com automatically.
  It has been saved to the repo (`reports/`) and uploaded to the Google Drive
  folder "PPC Reports". Please retrieve it there until an email channel is set up.
- **Attribution:** figures use Amazon's 7-day attribution. With everything at
  zero, attribution windows make no difference here.

# PPC 2-Day Report — 14–15 November 2026

**Report type:** 2-day · **Marketplace:** Amazon US (USD) · **Account:** Uzoebo Archbold E-Commerce (seller)
**Data window:** Saturday 14 Nov 2026 – Sunday 15 Nov 2026 (2 full days)
**Generated:** 18 Nov 2026 (data ends 48h before run, as Amazon figures finalise with a ~48h lag)
**Compared against:** _no previous 2-day report — this is the first run (baseline)._

---

## ⚠️ Please read first — two things to know

1. **Which account this is.** The `AMZ_PROFILE_ID` setting we were given is not a valid Amazon
   advertising profile ID (it is an `amzn1.*` resource string, not the numeric ID the API needs),
   so it could not be used directly. To avoid guessing, I logged in with the token, listed every
   advertising profile on the account, and found three marketplaces: **US, Canada and Mexico.**
   Only the **US** profile has any Sponsored Products campaigns at all — Canada and Mexico have
   none. So this report is the US account. **Action needed:** update `AMZ_PROFILE_ID` to the US
   profile's numeric ID so future runs are unambiguous (see notes-to-self.md).

2. **Your ads served nothing in this window.** All 15 Sponsored Products campaigns recorded
   **zero impressions, zero clicks, zero spend and zero sales** on 14–15 Nov. I double-checked by
   pulling the wider 1–15 Nov window — still zero across the board. This is real data, not a
   reporting error: the campaigns exist but are **not delivering any ads.** The most likely causes
   are bids set too low to win placements, a campaign/portfolio budget or start-date not active,
   the listings being out of the Buy Box / out of stock, or the campaigns still pending review.
   There is no email delivery tool configured in this environment, so this report was saved to the
   repo and uploaded to Google Drive but **not emailed** — see the note at the bottom.

---

## Part A — Data table (per campaign)

All figures are for 14–15 Nov 2026, Sponsored Products, US marketplace, in USD.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1-10k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated … Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10-25k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25-50k SV … Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV … Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (15 campaigns)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

_(Campaign names abbreviated with "…" are all for ASIN B0FXW3GW5F — the cat deterrent spray /
pet odor eliminator product. Top-of-search impression share, CTR, CPC, ACOS and ROAS cannot be
calculated with zero impressions/clicks, shown as "—".)_

There were **no keyword/search-term rows** to report, because with zero impressions no keyword or
target recorded any activity.

---

## Part B — Plain-English summary

- **Overall:** Over the two days, the account spent **$0.00** and made **$0.00** in ad sales.
  Nothing was spent and nothing was sold through Sponsored Products, because the ads did not show
  to any shoppers (zero impressions).
- **Best / worst campaign:** Not applicable — every campaign performed identically at zero. Nothing
  wasted money (good), but nothing worked either (the real problem).
- **Wasted spend / negatives to add:** None to suggest — there was no spend and no search-term data
  to mine, so there is nothing to add as a negative keyword yet.
- **Well-converting search terms to add as exact-match:** None available yet — no search-term data
  exists until the campaigns start getting impressions.
- **The headline issue:** You have a fully built-out campaign structure (15 campaigns: an Auto
  campaign, keyword "root" campaigns by search-volume tier, several single-keyword "Isolated"
  campaigns, and two unrelated campaigns — "KT ST w/ Sales" and a "Cat Tunnel Bed" ranking
  campaign) but **none of them is delivering.** A well-structured account that shows zero
  impressions is almost always a delivery problem, not a performance problem.

### What to do next (in order)

1. **Confirm the products are buyable.** Check that ASIN **B0FXW3GW5F** (and the Cat Tunnel Bed
   ASIN) are in stock and hold the Buy Box. Ads will not serve if the listing isn't winning the
   Buy Box.
2. **Check campaign status and budgets.** In Campaign Manager, confirm each campaign is *Enabled*
   (not paused, not out of its start/end dates) and that daily budgets and any portfolio budget
   caps are active and above $0.
3. **Raise bids.** Zero impressions very often means bids are below the auction floor. Set the Auto
   campaign and the exact-match campaigns to a competitive starting bid (check Amazon's suggested
   bid range for each keyword) and let them gather data.
4. **Fix the profile setting** so these reports always target the US account automatically
   (see the ⚠️ note above and notes-to-self.md).
5. **Re-check in the next report.** Once impressions start, we'll have CTR, CPC, ACOS, ROAS and
   search-term data to actually optimise.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first run of this report
type, so it establishes the **baseline**. All headline metrics (spend, sales, ACOS, ROAS,
impressions, clicks, purchases) start at **0 / $0.00**.

| Metric | This report | Previous | Change | % change |
|---|--:|--:|--:|--:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| Purchases | 0 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** Baseline established. Next 2-day report will show real change once the campaigns begin
serving impressions.

---

_Data source: Amazon Advertising API (Sponsored Products v3 reporting), pulled 18 Nov 2026.
US profile selected automatically after the configured profile ID was found to be invalid.
Figures are final (48h lag respected)._

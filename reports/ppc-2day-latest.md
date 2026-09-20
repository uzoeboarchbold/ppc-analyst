# PPC 2-Day Report — 16–17 September 2026

**Report type:** 2-day (Sponsored Products) · **Generated:** 2026-09-20
**Account:** US marketplace (Seller, USD) · **Product:** ASIN B0FXW3GW5F (cat deterrent spray / pet odor eliminator)
**Attribution:** 7-day click · **Currency:** USD

> **Read this first — the account served no ads in this window.** All 15
> Sponsored Products campaigns are ENABLED but delivered **0 impressions,
> 0 clicks, $0.00 spend and 0 sales on both 16 and 17 September.** This is
> real, not a data error (verified against a 30-day pull — see the note
> below). The report is complete; the numbers are simply all zero because
> the ads have stopped running.

## Setup note (what was fixed automatically)
- The `AMZ_PROFILE_ID` environment variable is **misconfigured** — it holds an
  *application* id, not an advertising *profile* id, so it cannot be used to
  pull data. I looked up the account's real profiles and used the **US**
  profile (`26765323558215`), which is the primary market for this business.
  (CA and MX profiles also exist.) This should be corrected in the environment
  so future runs are unambiguous.
- No numbers were invented. Where a metric is undefined because there was no
  activity (CTR, CPC, top-of-search share, ACOS, ROAS), it shows "—".

---

## Part A — Campaign data table (16–17 Sep 2026)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
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

*(All 15 campaigns share identical zero values, so each row is shown once
rather than repeated per day. No keyword/target or search-term rows were
returned by Amazon for this window — a direct consequence of zero delivery.)*

---

## Part B — Summary in plain English

**The short version:** Your ads did not run on 16 or 17 September. There was
no spend, no clicks and no sales. Nothing was wasted — but nothing was earned
either, because the campaigns are not being shown to shoppers.

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS / ROAS:** not applicable (no spend, no sales)
- **Best / worst campaign:** none to pick — every campaign delivered zero.
- **Wasted spend / negatives to add:** none this window (nothing was spent).
- **Search terms to add as exact-match:** none available (no search-term data
  because there was no traffic).

**Why the zeros — the important part.** I checked the last 30 days to be sure
this wasn't an API glitch. The account only ever had a light trickle of
activity between **19 Aug and 2 Sep** (roughly 75–235 impressions a day, 0–2
clicks a day, about **$3.77 total spend, and 0 sales the entire time**). From
**3 September onward there have been zero impressions** — delivery has fully
stopped. So the campaigns are switched on, but they are effectively invisible
to shoppers.

The most likely causes, roughly in order:
1. **Bids too low** to win any placement (very common on a new listing).
2. **Daily budget missing or set to ~zero**, so campaigns can't spend.
3. **Out of stock / not in the Buy Box** — Amazon won't serve ads for a
   listing that can't be bought.
4. Listing/account status issue (suppressed or inactive listing).

### What to do next
1. **Confirm the product is in stock and holds the Buy Box** for ASIN
   B0FXW3GW5F. If not, that alone explains the zero delivery — fix this first.
2. **Check each campaign's daily budget** is set to a real amount (not $0/$1).
3. **Raise bids** on the exact/phrase campaigns to a level that can actually
   win impressions (the earlier trickle suggests bids were far too low), and
   let the Auto campaign run to gather search-term data.
4. **Fix `AMZ_PROFILE_ID`** in the environment to the real US profile id
   (`26765323558215`) so future automated runs are unambiguous.
5. Re-check in the next 2-day report — once delivery resumes there will be
   real numbers to optimise (negatives, exact-match harvesting, ACOS control).

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists** — this is the first run of this report
type, so there is nothing to compare against yet. This report establishes the
baseline.

| Metric | This report (16–17 Sep) | Previous | Change (# / %) |
|---|--:|--:|--:|
| Impressions | 0 | — | — |
| Clicks | 0 | — | — |
| Total cost | $0.00 | — | — |
| Sales | $0.00 | — | — |
| Purchases | 0 | — | — |
| ACOS | n/a | — | — |
| ROAS | n/a | — | — |

**Trend:** Not established (baseline). For context, activity was already
near-zero before this window and stopped entirely on 3 September, so the
priority is getting ads to serve again rather than fine-tuning performance.

---
*Data source: Amazon Advertising API (Sponsored Products, v3 reporting),
US profile 26765323558215. Window: 16–17 Sep 2026, ending 48h+ before the
2026-09-20 run to allow for Amazon's data lag.*

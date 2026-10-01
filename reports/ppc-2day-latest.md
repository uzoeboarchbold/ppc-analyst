# PPC 2-Day Report — 27–28 September 2026

**Window covered:** Sunday 27 Sep 2026 and Monday 28 Sep 2026 (the two full
days ending ~48h before this run, to allow Amazon's data to finalise).
**Run date:** 1 October 2026 · **Marketplace reported:** Amazon US (Sponsored Products)

---

## ⚠️ Read this first

**Your Sponsored Products ads are effectively switched off, so there is almost
nothing to report for these two days.** Two separate issues are behind that:

1. **No valid payment method on the US ad account.** Amazon reports the US
   advertising profile as having no valid payment method. Because of this your
   15 "enabled" campaigns are barely being shown — across the *entire* month of
   September (1–28) they racked up just **287 impressions, 1 click, 8 cents of
   spend and $0 in sales**. For the 27–28 Sep window specifically, they
   recorded **zero** impressions, clicks, spend and sales.

2. **The saved profile setting is wrong (I worked around it automatically).**
   The `AMZ_PROFILE_ID` credential stored for this routine was set to an
   *application ID*, not an advertising *profile ID*, so the first data pull was
   rejected. I detected this, looked up your real profiles directly, and ran the
   report against the correct US account — so this report is based on real data,
   not guesses. Worth fixing the stored value so future runs don't rely on the
   workaround.

The ad credentials themselves are valid and the connection works. The problem
is account/billing state, not the automation.

**Bottom line:** there was no ad activity to analyse in this window. The single
most valuable action is to **add a valid payment method to the US ad account**
so your campaigns can start serving again.

---

## Part A — Data table (27–28 Sep 2026)

Per-campaign, US Sponsored Products. Every enabled campaign returned zero for
the window, so the table collapses to a single totals line.

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| All US SP campaigns (15 enabled) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*CA and MX ad profiles exist on the account but contain **no campaigns**, so
they are not shown.*

### Context — September month-to-date (1–28 Sep), for reference only
This is **not** the 2-day window; it is shown only to prove the ads really are
dark rather than merely quiet for two days.

| Metric (US SP, 1–28 Sep) | Value |
|---|---|
| Impressions | 287 |
| Clicks | 1 |
| Spend | $0.08 |
| Purchases | 0 |
| Sales | $0.00 |
| ACOS / ROAS | n/a (no sales) |

Campaigns with any impressions at all this month: "SP Isolated … Pet Odor
Eliminator Phrase" (131), "SP Home + Eliminator + Brand Root … Exact" (82),
"SP | Cat Tunnel Bed Pink Only | Exact Ranking" (40, the only click/spend),
"SP Auto …" (16), "SP KT | ST w/ Sales" (11), plus two more in single digits.

---

## Part B — Plain-English summary

- **Overall spend:** $0.00 · **Sales:** $0.00 · **ACOS/ROAS:** not applicable
  (no clicks or sales in the window).
- **Best campaign:** none — nothing converted (or even served meaningfully).
- **Worst campaign:** not meaningful; all campaigns are equally idle.
- **Wasted spend / negatives to add:** none to flag — there was no spend to
  waste. (With ads off, there are no search terms burning money.)
- **Well-converting search terms to add as exact-match:** none available — with
  effectively no clicks and no purchases, there is no search-term data to mine
  this period.
- **What to do next:**
  1. **Add a valid payment method** to the US Amazon Ads account. Nothing else
     matters until ads can serve.
  2. Once ads are live again, re-check within a few days — the campaign
     structure (pet-odor / cat-deterrent / cat-tunnel keyword sets) is already
     built and enabled, so spend should resume automatically.
  3. **Fix the stored `AMZ_PROFILE_ID`** so it holds the numeric US profile ID
     (`26765323558215`) instead of an application ID.
  4. Decide whether the empty **CA** and **MX** ad profiles should have
     campaigns at all; if not, they can be ignored.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this routine, so
there is no prior baseline to compare against. All headline metrics
(impressions, clicks, spend, sales, ACOS, ROAS) are being recorded for the
first time here and are all zero for the window. The next 2-day run will compare
against this report.

| Metric | This report | Previous | Change |
|---|---|---|---|
| Impressions | 0 | — | — (first report) |
| Clicks | 0 | — | — |
| Spend | $0.00 | — | — |
| Sales | $0.00 | — | — |
| ACOS | n/a | — | — |
| ROAS | n/a | — | — |

**Direction:** not assessable yet (no baseline). The headline is unchanged
account health: ads are not serving due to the missing payment method.

---

*Data source: Amazon Advertising API (Sponsored Products, v3 reporting),
US profile 26765323558215. ACOS and ROAS computed from cost and 7-day sales.
Generated automatically.*

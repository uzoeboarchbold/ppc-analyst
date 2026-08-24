# PPC 2-Day Report — 20–21 Aug 2026

**Marketplace:** Amazon US (Sponsored Products) · Seller: Uzoebo Archbold E-Commerce
**Dates covered:** 20 Aug 2026 – 21 Aug 2026 (2 full days, ending 48h before this run to allow Amazon data to finalise)
**Run date:** 24 Aug 2026
**Compared against:** No previous 2-day report exists — this is the first run, so there is nothing to compare against yet. Future runs will compare here.

---

## Note on setup
The `AMZ_PROFILE_ID` environment variable holds an **application ID** (`amzn1.application…`), not a numeric Amazon Ads profile ID. The account has three seller profiles: **US, Canada, Mexico**. I defaulted to the **US** profile (the one with a live daily budget configured) and pulled data successfully. If reports should cover a different marketplace, set `AMZ_PROFILE_ID` to the correct numeric profile ID. (Logged in notes-to-self.md.)

---

## Part A — Data Table (per campaign)

Only 5 of 19 campaigns received any impressions in this window; the rest had zero activity. All active campaigns are shown first; zero-activity campaigns are grouped at the bottom.

| Campaign | Impr. | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 42 | 0.00% | 0 | 0% | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Pet Odor Eliminator Phrase | 15 | 0.18% | 0 | 0% | 0 | $0.00 | $0.00 | – | – | – |
| SP Auto … B0FXW3GW5F | 8 | 1.33% | 0 | 0% | 0 | $0.00 | $0.00 | – | – | – |
| SP Isolated … Cat Deterrent Spray Phrase | 5 | 0.00% | 0 | 0% | 0 | $0.00 | $0.00 | – | – | – |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | 4 | 0.00% | 0 | 0% | 0 | $0.00 | $0.00 | – | – | – |
| 14 other campaigns (12 enabled, 4 paused) | 0 | – | 0 | – | 0 | $0.00 | $0.00 | – | – | – |
| **TOTAL** | **74** | **≈0.3%** | **0** | **0%** | **0** | **$0.00** | **$0.00** | **–** | **–** | **–** |

*CTR, CPC, ACOS and ROAS cannot be calculated where clicks/cost/sales are zero (division by zero) — shown as "–".*

---

## Part B — Summary (plain English)

**The short version: the ads are switched on but barely running. Over these two days they were shown 74 times, got zero clicks, spent $0.00 and made $0.00 in sales.**

- **Spend:** $0.00 — nothing was spent because nobody clicked.
- **Sales:** $0.00 — no orders came from ads.
- **ACOS / ROAS:** Not applicable (no spend and no sales).
- **Best campaign:** None stood out — the "Cat Tunnel Bed Pink Only" exact-match campaign got the most exposure (42 of 74 impressions) but still no clicks.
- **Worst campaigns:** 14 of 19 campaigns got **zero impressions at all**, meaning their bids are almost certainly too low to enter any auctions, or their keywords have no search demand.
- **Wasted spend:** None this window — there was no spend to waste.
- **Well-converting search terms to add as exact-match:** None — with zero clicks and zero sales there are no proven search terms to promote yet.
- **Top-of-search share** is essentially 0% everywhere, confirming the ads are not appearing where shoppers look first.

**What this means:** This isn't a "losing money" problem — it's a "not in the game" problem. The account is effectively dormant. The most likely cause is that **bids are set too low to win impressions/clicks**, possibly combined with a very small daily budget (the US profile daily budget is set to $40). A handful of low-relevance impressions are trickling in, but nothing is converting into clicks.

### What to do next
1. **Raise bids** on the campaigns that already get impressions (Cat Tunnel Bed, Pet Odor Eliminator Phrase, the Auto campaign) so they can actually win clicks — start with a modest increase (e.g. +25–50%) and watch.
2. **Check the daily budget and bidding strategy** — confirm campaigns aren't budget-capped or set to "down only" with a floor bid too low to compete.
3. **Investigate the 14 zero-impression campaigns** — verify keywords are relevant, match types aren't over-restrictive, and bids are above the suggested minimum. Consider pausing dead ones to focus budget.
4. **Give it a few days after raising bids**, then re-check: the goal for the next report is to see clicks > 0 so we can start judging conversion and ACOS.

---

## Part C — Comparison to previous 2-day report

There is **no previous 2-day report** to compare against — this is the first report of this type. Headline metrics for this window, to serve as the baseline for next time:

| Metric | This report | Previous | Change |
|---|---:|---:|---|
| Spend | $0.00 | — | — |
| Sales | $0.00 | — | — |
| Impressions | 74 | — | — |
| Clicks | 0 | — | — |
| ACOS | n/a | — | — |
| ROAS | n/a | — | — |

*Overall:* No comparison possible yet. Baseline established.

---
*Data source: Amazon Advertising API (Sponsored Products, reporting v3), US profile 26765323558215. Generated automatically.*

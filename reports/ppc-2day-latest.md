# PPC 2-Day Report — 26–27 October 2026

**Account:** Uzoebo Archbold E-Co — Amazon US (Sponsored Products, USD)
**Period covered:** Monday 26 Oct 2026 and Tuesday 27 Oct 2026 (2 full days, UTC)
**Report generated:** Friday 30 Oct 2026, 23:11 UTC (data ends 48h before run, as required)
**Compared against:** previous 2-day report — *none exists yet; this is the first/baseline report.*

---

## ⚠️ Please read first — two setup issues and one important finding

**1. The configured account ID was invalid, so I selected the account myself.**
The `AMZ_PROFILE_ID` setting is a 50-character value, but real Amazon Ads profile IDs are 14–16 digits, and it matched none of your actual accounts. Your login has three Amazon Ads profiles — **US, Canada and Mexico**, all under "Uzoebo Archbold E-Co". Only the **US** account has any Sponsored Products campaigns (54 of them); Canada and Mexico have none. I therefore ran this report against the **US** account. **Action needed:** please correct `AMZ_PROFILE_ID` to the US profile ID so future runs are unambiguous.

**2. Only North America is reachable from this environment.**
Amazon's EU and Far-East API endpoints are blocked by this environment's network policy. That's fine for now because all your campaigns are in the US, but it's worth knowing if you ever advertise outside North America.

**3. Your ads delivered nothing in this window — in fact, nothing all month.**
You have **15 enabled** Sponsored Products campaigns, but they recorded **zero impressions, zero clicks and zero spend** on 26–27 Oct. I checked a wider window (1–27 Oct) to be sure: still zero impressions and zero spend across the whole month. The campaigns exist and are switched on, but they are not being shown to shoppers. See "What to do next" below — this is the one thing worth acting on.

*(The numbers below are real figures pulled from the Amazon Ads API. They are all zero because there was genuinely no ad activity — nothing has been invented or estimated.)*

---

## Part A — Data table (by campaign)

All 15 enabled campaigns returned zero delivery for 26–27 Oct 2026. Ratio metrics (CTR, CPC, ACOS, ROAS, Top-of-search share) are undefined with no impressions/clicks and are shown as "—".

| Campaign | Impr. | TOS Impr. Share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| SP Auto — Cat Deterrent/Odor (B0FXW3GW5F) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated — Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1–10k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home+Eliminator+Brand Root 10–25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter+Urine Root 10–25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT — Search Terms w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Tunnel Bed Pink — Exact Ranking | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (all SP)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales from ads:** $0.00.
- **ACOS / ROAS:** not applicable — you can't have an advertising cost of sales or a return on ad spend when nothing was spent.
- **Best / worst campaign:** none stands out either way — every campaign performed identically (no activity).
- **Wasted spend / negatives to add:** none. You can only waste money once ads start spending; right now the opposite problem applies — the ads aren't spending at all.
- **Well-converting search terms to add as exact-match:** none available — with no clicks or orders, there's no search-term data to mine yet.
- **The real issue:** 15 campaigns are switched on but invisible to shoppers. The most likely causes, in order:
  1. **Bids are too low to win any auction.** Your daily budgets are very small (mostly **$1.50/day**), and if bids are set to match, Amazon may never place your ad. This is the most common cause of "enabled but zero impressions".
  2. **The product listing isn't eligible to advertise** — e.g. out of stock, suppressed/inactive listing, lost Buy Box, or a brand-new ASIN still being indexed. Ads can't run if the product can't be bought.
  3. **Campaigns have a future start date or a portfolio/budget cap** preventing delivery.

### What to do next
1. **Check the product first.** Confirm ASIN **B0FXW3GW5F** (Cat Deterrent Spray / Pet Odor Eliminator) is in stock, active, and holds the Buy Box. If not, fix that before touching the ads — nothing else matters until the listing can convert.
2. **Raise bids to realistic levels.** On a $1.50/day budget, try bids around $0.40–$0.75 to start winning impressions, then adjust once data comes in. Low budget is fine for testing, but the *bid* is what wins the auction.
3. **Lean on the Auto campaign** to gather cheap discovery data for a few days, then promote the winning search terms into your exact-match campaigns.
4. **Re-check in 48 hours.** Once impressions start, the next 2-day report will have real CTR/CPC/ACOS/ROAS to act on.

---

## Part C — Comparison to previous report

There is **no previous 2-day report** to compare against — this is the first run, so it serves as the **baseline**. All headline metrics start at zero:

| Metric | This report | Previous | Change |
|---|---|---|---|
| Spend | $0.00 | — | baseline |
| Sales | $0.00 | — | baseline |
| ACOS | n/a | — | baseline |
| ROAS | n/a | — | baseline |
| Impressions | 0 | — | baseline |
| Clicks | 0 | — | baseline |

**Verdict:** Neither better nor worse — there's nothing to compare yet. The priority for the next run is simply to get the ads delivering so there's real performance to measure.

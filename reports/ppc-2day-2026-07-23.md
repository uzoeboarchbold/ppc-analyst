# PPC 2-Day Report — 19–20 July 2026

**Marketplace:** Amazon US (USD) · Seller: Uzoebo Archbold E-Commerce
**Ad product:** Sponsored Products
**Window covered:** 2026-07-19 and 2026-07-20 (2 full days, ending 48h before the run to allow Amazon's ~48h data lag)
**Generated:** 2026-07-23 (automated run)

---

## ⚠️ Read this first — two setup notes

1. **No ad activity in this window.** Across the account there were **0 impressions, 0 clicks, $0.00 spend and $0.00 ad sales** on both days. This is not a data error — the data pulled cleanly. The cause is that the advertising is effectively switched off: of the account's ~55 Sponsored Products campaigns, only **2 are Enabled** and even those two did not serve any impressions on these dates. Everything else is Paused or Archived. See the summary for what this means and what to do.

2. **`AMZ_PROFILE_ID` is misconfigured.** The environment variable holds an application ID (`amzn1.application.…`), not a numeric Advertising profile ID, so it can't be used directly. I looked up the real profiles on the account and used the **US** marketplace (profile `26765323558215`), which is the primary FBA marketplace and the only one with any Sponsored Products campaigns. (CA and MX profiles exist but have no SP campaigns.) Please fix this env var to the numeric US profile ID so future runs are unambiguous.

---

## Part A — Data table (per campaign)

Only the two **Enabled** campaigns are shown; all other campaigns are Paused/Archived and did not serve. All figures are for 19–20 July 2026 combined.

| Campaign | Status | Impressions | ToS Impr. Share | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | Enabled ($8/day) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP PT \| ST w/ Sales | Enabled ($8/day) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*"—" means the metric cannot be calculated because there were no impressions/clicks (e.g. CTR, CPC, ACOS and ROAS all require activity to exist).*

---

## Part B — Summary in plain English

**The short version:** Over these two days the account spent **nothing** on Amazon ads and, as a result, made **no ad-driven sales**. Advertising is essentially paused.

- **Overall spend:** $0.00
- **Overall ad sales:** $0.00
- **ACOS / ROAS:** Not applicable — you can't have a cost-of-sales ratio when there's no spend and no sales.
- **Best / worst campaign:** Not applicable — no campaign delivered any impressions, so there's nothing to rank.
- **Wasted spend / negatives to add:** None to flag — there was no spend to waste. (This is the one silver lining of a dark period.)
- **Well-converting search terms to add as exact-match:** None available — with no clicks or sales there are no search terms to harvest this period.

**Why it looks like this:** Only two campaigns are switched on ("SP KT | ST w/ Sales" and "SP PT | ST w/ Sales", $8/day each, both keyword/product-target "search-term harvesting" campaigns started 9 June 2026). Every other campaign — the auto campaigns, the odor/litter/cat-deterrent keyword campaigns, and the older Cat Tunnel Bed set — is Paused or Archived. On top of that, even the two enabled campaigns produced zero impressions on 19–20 July, which usually points to one of: bids set too low to win any auctions, no eligible/active keywords or targets inside them, the promoted product being out of stock or ineligible (e.g. Buy Box lost), or the campaigns simply having nothing to harvest.

**What to do next (in priority order):**
1. **Decide if the pause is intentional.** If advertising was deliberately switched off (budget, stock, seasonality), no action is needed — but you should know that ads are currently contributing $0 in sales.
2. **If it is not intentional, investigate the two Enabled campaigns.** Check that (a) the promoted ASIN is in stock and holds the Buy Box, (b) there are active keywords/targets inside each campaign, and (c) bids are high enough to be competitive. Zero impressions on an enabled, funded campaign almost always traces back to one of these.
3. **Re-enable your core campaigns** (auto + main keyword campaigns) if you intend to keep advertising, starting with the ones that historically converted, at a controlled daily budget.
4. **Fix `AMZ_PROFILE_ID`** to the numeric US profile ID so this report always targets the right account without guesswork.

---

## Part C — Comparison to the previous 2-day report

**No previous 2-day report exists** — this is the first report of this type, so there is no prior baseline to compare against. Future 2-day reports will show the change in each headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both an absolute number and a percentage versus this report.

For the record, this report's baseline headline numbers are: **Impressions 0 · Clicks 0 · Spend $0.00 · Sales $0.00 · ACOS n/a · ROAS n/a.**

---

*Data source: Amazon Advertising API (Sponsored Products v3 reporting), US profile `26765323558215`. Report pulled cleanly; the zero figures reflect genuine account state, not a failed data pull.*

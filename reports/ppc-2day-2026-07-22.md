# PPC 2-Day Report — 18–19 July 2026

**Account:** Uzoebo Archbold E-Commerce — Amazon US (Sponsored Products)
**Window covered:** Sat 18 Jul 2026 – Sun 19 Jul 2026 (2 full days)
**Report generated:** 22 Jul 2026 (data ends 48h before run, as Amazon PPC data finalises with a ~48h lag)
**Currency:** USD

---

## ⚠️ Read this first — the account served no ads

Across the whole window, Sponsored Products delivered **zero impressions, zero
clicks, zero spend and zero sales**. This is not a data error — the pull ran
cleanly and I cross-checked a full 30-day window (20 Jun – 19 Jul), which is
**also entirely zero**. The account has effectively been dark for at least a
month.

There are only **2 enabled campaigns**, and both are fully and correctly set up:
budgets funded ($8/day each), 16 enabled keywords with sensible bids
($0.82–$2.13), 3 ASIN targets, and enabled product ads. Despite all that,
**nothing is serving**. When everything in an account is switched on with
reasonable bids but impressions stay at exactly zero, the cause is almost never
the ad settings — it is that the **advertised product cannot be shown**. See
"What to do next" below.

*(A minor config note for whoever maintains this automation: the `AMZ_PROFILE_ID`
environment variable holds an application ID, not a numeric Ads profile ID, so I
auto-selected the correct active profile — the US account, 26765323558215. Worth
fixing so future runs don't rely on auto-detection.)*

---

## Part A — Data table (by campaign)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP KT \| ST w/ Sales (keyword targeting) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales (product targeting) | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*The account's other 52 campaigns are paused (45) or archived (7) and did not
serve. "n/a" values are ratios that can't be calculated with zero
impressions/clicks/spend.*

---

## Part B — Plain-English summary

- **Overall spend:** $0.00. **Overall sales (PPC-attributed):** $0.00.
- **ACOS / ROAS:** Not applicable — you can't have an advertising cost of sale
  or return on ad spend when there was no ad spend.
- **Best / worst campaign:** Neither campaign spent or earned anything, so there
  is no winner or loser to call out this period. Both are tied at zero.
- **Wasted spend:** None — because there was no spend at all. (The flip side is
  there were also **no sales** from advertising.)
- **Negatives to add:** None recommended — with zero search-term activity there
  is nothing to negate.
- **Search terms to add as exact-match:** None available — no clicks or
  conversions occurred, so there are no converting search terms to harvest yet.

The single most important fact this period: **your Sponsored Products ads are not
running.** Both live campaigns point at one product, **ASIN B0FXW3GW5F** (a cat
deterrent / pet-odour eliminator). Everything on the advertising side is healthy,
which means the block is on the product/listing side.

### What to do next (in priority order)

1. **Check the product listing for ASIN B0FXW3GW5F today.** The most common
   reasons a fully-enabled campaign shows *zero* impressions are:
   - the product is **out of stock**,
   - you have **lost the Buy Box / Featured Offer** (ads only run when you own it),
   - or the **listing is suppressed/inactive** (e.g. missing image, policy flag,
     pricing error).
   Fixing whichever of these applies will switch delivery back on immediately —
   no ad changes required.
2. **Confirm stock and Buy Box status in Seller Central** for that ASIN. If
   stock is low or zero, restock; if the Buy Box is lost, resolve the pricing or
   account-health issue causing it.
3. **Once it's live again, re-check within 48 hours.** The bids and budgets are
   already sensible, so ads should begin serving as soon as the product is
   eligible. This report will then start producing real performance numbers.
4. **No budget or bid changes are needed right now** — raising bids or budgets
   will do nothing while the product itself can't be advertised.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists — this is the first run, so it sets the
baseline.** From the next 2-day report onward, each headline metric (impressions,
clicks, spend, sales, ACOS, ROAS) will be shown here as a change vs. this report,
in both absolute and percentage terms.

For the record, the baseline figures carried forward are:

| Metric | This report (baseline) |
|---|--:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| ACOS | n/a |
| ROAS | n/a |

**Bottom line:** Neither improved nor worsened versus history (there is none) —
but the account is not spending or selling through PPC, and the priority is to
get the advertised product eligible to serve again.

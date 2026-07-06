# PPC 2-Day Report — 2–3 July 2026

**Report type:** 2-day | **Window covered:** 2026-07-02 to 2026-07-03 (2 full days)
**Generated:** 2026-07-06 (window ends 48h before the run, as Amazon PPC data finalises ~48h late)
**Marketplace:** Amazon US (Sponsored Products) | **Account:** Uzoebo Archbold E-Commerce | **Currency:** USD
**Compared against:** previous 2-day report, ppc-2day-2026-07-05.md (covered 1–2 July 2026)

> **Delivery note:** Saved to the repo and uploaded to Google Drive ('PPC Reports') successfully.
> Email to uzoebo.archbold@gmail.com could **not** be sent — there is no email/Gmail sending tool
> connected to this automation session. The headline is delivered by push notification instead.
> To receive these by email, a Gmail integration needs to be enabled for the routine. (Logged for future runs.)

---

## Headline: the account is still dormant — no ads delivered, no spend, no sales

For 2–3 July the two live campaigns recorded **zero impressions, zero clicks, zero spend and zero sales**.
This is real data pulled cleanly from the Amazon Ads API, not a technical failure. Of the account's **54
campaigns, only 2 are switched on** ("SP KT | ST w/ Sales" and "SP PT | ST w/ Sales"); the other 52 are
paused (45) or archived (7). I confirmed against a wider 14-day window (20 June – 3 July): still **0
impressions, $0 cost, $0 sales** account-wide. The ads have effectively been dark since ~9 June.

This is the same picture as the last several 2-day reports — nothing has changed.

---

## Part A — Data table (per campaign, Sponsored Products, US)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SP KT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| SP PT \| ST w/ Sales | 0 | n/a | 0 | n/a | 0 | $0.00 | $0.00 | n/a | n/a | n/a |
| **TOTAL** | **0** | **n/a** | **0** | **n/a** | **0** | **$0.00** | **$0.00** | **n/a** | **n/a** | **n/a** |

*Only the two ENABLED campaigns are shown; the other 52 are paused/archived and served nothing.
"n/a" = cannot be calculated with zero impressions/clicks/spend. Keyword/target and search-term reports both
returned zero rows, consistent with zero impressions. Canada and Mexico profiles have no campaigns.*

---

## Part B — Summary in plain English

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not applicable (no spend, no sales).
- **Best campaign / worst campaign:** No meaningful winner or loser — both live campaigns did nothing.
- **Wasted spend / negatives to add:** None. Nothing was spent, so there is no wasted spend and no negative
  keywords to suggest this period.
- **Well-converting search terms to add as exact-match:** None available — with no clicks or purchases there
  is no search-term data to harvest.

### What's actually going on

The problem is not *how* the money is being spent — it is that **the ads are not running**. I looked inside
the two enabled campaigns to rule out an obvious setup error, and the structure is actually healthy:

- Both ad groups are ENABLED.
- "SP KT" has 16+ enabled keywords with sensible bids ($0.82–$2.13, exact and phrase).
- "SP PT" has 3 enabled product (ASIN) targets with bids of $1.15–$2.09.
- Daily budgets are $8 each.

Despite that, they won **zero impressions in the last 14 days**. When the structure is fine but a campaign
serves literally nothing, the most likely cause is that **the advertised product cannot be shown** — i.e. it
is out of stock, has lost the Buy Box / Featured Offer, or the listing is suppressed/inactive. Amazon does
not serve Sponsored Products ads for a product that isn't buyable, so impressions fall to zero regardless of
bids or budget. (Bids being too low is a secondary possibility, but $2+ exact bids would normally win *some*
impressions, which points away from bids and toward product eligibility.)

### What to do next (priority order)

1. **Check stock and Buy Box for the advertised products** (the "SP PT" targets include ASINs B00CKFL93K,
   B08DS1FHQM, B0GN9WTT1Q; the catalogue centres on the cat-deterrent / pet-odour range). No stock or no Buy
   Box = no ads. This is the single most likely reason for two weeks of zeros.
2. **Confirm this dormancy is intentional.** 52 of 54 campaigns are paused/archived. If the goal is sales,
   decide which historically-performing campaigns to re-enable.
3. **If the products are in stock and buyable but still not serving**, raise bids on the two live campaigns to
   competitive levels and confirm there is no account-level billing hold.
4. **Fix the `AMZ_PROFILE_ID` setting** to the numeric US profile `26765323558215` (it currently holds an
   application ID, not a profile ID — see notes below). The routine auto-corrects this each run, but fixing it
   at source removes the guesswork.
5. Once ads are serving again, these reports will show real performance (ACOS, ROAS, wasted spend, exact-match
   winners) to optimise against.

---

## Part C — Comparison to previous 2-day report

Compared against **ppc-2day-2026-07-05.md** (covered 1–2 July 2026), which was also all zeros:

| Metric | Previous (1–2 Jul) | This report (2–3 Jul) | Change (abs) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 0 | 0 | 0 | 0% |
| Clicks | 0 | 0 | 0 | 0% |
| Total cost | $0.00 | $0.00 | $0.00 | 0% |
| Sales | $0.00 | $0.00 | $0.00 | 0% |
| Purchases | 0 | 0 | 0 | 0% |
| ACOS | n/a | n/a | — | — |
| ROAS | n/a | n/a | — | — |

**Improved or worsened?** Neither — the account is flat at zero for the third-plus consecutive 2-day window.
Nothing has changed since the last report; the ads remain dark. The number to watch is whether impressions
rise above zero — that will be the first sign delivery has resumed. Until a human re-enables campaigns and
confirms the advertised products are buyable, every 2-day report will keep reading zero.

---

*Generated automatically by the PPC Analyst routine. Data source: Amazon Advertising API (Sponsored Products
v3 reporting, 7-day attribution), US profile 26765323558215. All figures pulled live; zero values reflect
genuine account activity, not missing data. No numbers were estimated or invented.*

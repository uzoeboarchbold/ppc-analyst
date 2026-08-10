# PPC 2-Day Report — Aug 6–7, 2026 (Sponsored Products, US)

**Report window:** Thursday 6 August 2026 and Friday 7 August 2026 (2 full days).
**Marketplace/profile:** United States (USD), seller "Uzoebo Archbold E-Commerce".
**Generated:** 10 August 2026 (data ends 48h before run, per Amazon's reporting lag).

> **Please read — two automation issues this run:**
> 1. **Wrong profile ID in config.** The `AMZ_PROFILE_ID` environment variable is set to
>    `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`, which is an *application* ID, not an
>    Amazon Ads *profile* ID. Profiles are numeric. The account has three: **US** (26765323558215),
>    **CA** (2840235221595557) and **MX** (3892485344323414). I used the **US** profile because it is
>    the only one with an active daily budget ($40). If you advertise mainly in Canada or Mexico, update
>    `AMZ_PROFILE_ID` to the right numeric ID so future reports point at the right market.
> 2. **Email not sent.** The Gmail connector is authenticated on the account but switched **off for this
>    automated session**, so I could not email the report this run. It is saved in the repo and uploaded to
>    Google Drive. To enable email, turn the Gmail connector on for this scheduled chat.

## Part A — Data table (by campaign)

| Campaign | Impr. | ToS IS | Clicks | CTR | Purch. | Sales | Cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Isolated 6K-PZMX-MTDZ B0FXW3GW5F Pet Odor Elim... | 12 | 1.7% | 1 | 8.3% | 1 | $13.99 | $2.65 | $2.65 | 18.9% | 5.28 |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| L... | 56 | 0.0% | 1 | 1.8% | 0 | $0.00 | $0.07 | $0.07 | — | 0.00 |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZ... | 32 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP PT Pet Odor Eliminator 6K-PZMX-MTDZ B0FXW3GW5F | 20 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Home + Eliminator + Brand Root 10-25k SV 6K-PZ... | 3 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP KT \| ST w/ Sales | 3 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Odor Root 25-50k SV 6K-PZMX-MTDZ B0FXW3GW5F Ph... | 1 | 0.0% | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP Litter + Urine Root 10-25k SV 6K-PZMX-MTDZ B0F... | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| SP PT \| ST w/ Sales | 0 | — | 0 | 0.0% | 0 | $0.00 | $0.00 | $0.00 | — | — |
| **TOTAL** | **127** | **—** | **2** | **1.6%** | **1** | **$13.99** | **$2.72** | **$1.36** | **19.4%** | **5.14** |

*ToS IS = Top-of-search impression share. "—" = not enough data to calculate (no spend, sales or impressions). Attribution: 7-day. Purchases/Sales are attributed within the window.*

## Part B — Plain-English summary

**The headline:** These were two very quiet days. Across all Sponsored Products campaigns the account
spent **$2.72**, got **127 impressions**, **2 clicks**, and made **1 sale worth $13.99**. That works out
to an **ACOS of 19.4%** and a **ROAS of 5.14** — i.e. every $1 of ad spend returned about $5.14 in sales.
On the surface those are healthy efficiency numbers, but the volume is so low that they rest on a single
click that happened to convert. Don't read too much into two days this thin.

**Best campaign:** *SP Isolated … Pet Odor Eliminator Phrase* — the only campaign that sold anything.
1 click, 1 sale, $13.99 revenue on $2.65 spend (ACOS 18.9%, ROAS 5.28). This is the workhorse right now.

**Worst / wasted spend:** There is essentially none to flag. The only other spend was **$0.07** on the
*Cat Tunnel Bed* campaign (1 click, no sale) — too small to act on. No campaign is burning money.

**What's happening under the hood:** Most campaigns are getting impressions but almost no clicks — e.g.
"angry orange pet odor eliminator" (exact) had 26 impressions and 0 clicks, and the Cat Tunnel Bed target
had 56 impressions and 1 click (1.8% CTR). Low clicks at low spend usually means bids are conservative and/or
listings aren't compelling enough at the impression stage. Top-of-search impression share is near 0% almost
everywhere, so the ads are rarely landing in the prime top-of-search slot.

**Search terms worth adding as exact-match:**
- **"febreze air spray pet odor eliminator"** — 1 click → 1 sale, $13.99, ACOS 18.9%. It converted through
  the phrase keyword "pet odor eliminator". Worth adding as its own **exact-match** keyword so you can bid it
  deliberately and protect the winner. (Caveat: this is one conversion — treat it as a promising candidate, not
  a proven one, and watch it over the next few reports.)
- No other search term has enough data yet.

**Negatives to consider:** Nothing yet. No search term has spent enough with zero return to justify a negative.
Revisit once any single term passes ~10 clicks with no sale.

**What to do next:**
1. **Fix the profile-ID config** so reports are guaranteed to track the right market (see note above).
2. **Add "febreze air spray pet odor eliminator" as an exact-match keyword** in a suitable campaign and give
   it a modest, deliberate bid.
3. **Consider small bid increases** on the campaigns getting impressions but no clicks, to test whether more
   presence (especially top-of-search) turns into clicks — the account is spending well under its $40/day budget.
4. **Keep watching** — two days is too short to change strategy on. The weekly view will be more meaningful.

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first report of this type, so there is no prior period to
compare against. Headline metrics to carry forward as the baseline for next time:

| Metric | This period (Aug 6–7) |
|---|--:|
| Impressions | 127 |
| Clicks | 2 |
| CTR | 1.6% |
| Purchases | 1 |
| Sales | $13.99 |
| Total cost | $2.72 |
| CPC | $1.36 |
| ACOS | 19.4% |
| ROAS | 5.14 |

The next 2-day report will show the change in each of these as a number and a percentage.

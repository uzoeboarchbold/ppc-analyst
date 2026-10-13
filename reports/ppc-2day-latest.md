# PPC 2-Day Report — 9–10 Oct 2026

**Report run:** 2026-10-13 (23:20 UTC)
**Window covered:** Thursday 9 Oct 2026 – Friday 10 Oct 2026 (2 full days, ending 48h before run)
**Account:** Uzoebo Archbold E-Commerce — US marketplace (Sponsored Products)
**Currency:** USD

---

## ⚠️ Read this first — no ads are running

The data pull worked correctly, but it shows **zero activity**: no impressions,
no clicks, no spend and no sales — not just for these two days, but for the
**entire last 30 days**.

The cause is almost certainly a **billing problem on the US account**: Amazon
reports the account has **no valid payment method**, and without one Amazon
will not show your ads at all. You currently have **15 campaigns switched ON**
with about **$23.50/day of budget ready to spend**, but none of it can run
until billing is fixed.

**This is the one thing to action from this report:** go to Amazon Seller
Central / Campaign Manager → Billing, and add or update a valid payment method.
Once that is live, the enabled campaigns should start serving within a day or so.

*(Also noted for the tech setup: the `AMZ_PROFILE_ID` credential was pointing at
the wrong ID — an application ID instead of the store's profile number. The run
auto-corrected by looking up the correct US profile (`26765323558215`), so the
report still ran. Worth fixing the stored value so it's clean for next time.)*

---

## Part A — Data table (by campaign)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All enabled campaigns (15) | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

Every one of the 15 live campaigns returned identical figures — zero across all
metrics — so they are collapsed into a single row above. Derived metrics (CTR,
CPC, ACOS, ROAS, Top-of-search impression share) cannot be calculated because
there were no impressions or clicks to divide by.

**Campaign status overall:** 54 campaigns exist — **15 ENABLED, 32 PAUSED, 7 ARCHIVED.**

---

## Part B — Plain-English summary

- **Overall spend:** $0.00
- **Overall sales:** $0.00
- **ACOS / ROAS:** not applicable (no spend, no sales)
- **Best campaign / worst campaign:** none to pick — nothing delivered.
- **Wasted spend / negatives to add:** none — you can't waste spend when nothing
  is spending. (No search-term data was available to mine for negatives either.)
- **Well-converting search terms to add as exact-match:** none available — there
  were no clicks or conversions in the window to learn from.

### What to do next
1. **Fix billing first.** Add a valid payment method to the US account. This is
   the single blocker — everything else is downstream of it. Nothing in your PPC
   can work until this is done.
2. **Then confirm delivery.** Within ~24–48h of fixing billing, check that your
   15 enabled campaigns are getting impressions again. If they still show zero,
   there may be a second issue (e.g. account suspension, out-of-stock listings,
   or bids set too low).
3. **Re-baseline.** Once ads are actually running, the next 2-day report will
   have real numbers to analyse (wasted spend, winning search terms, ACOS, etc.).
   Right now there is simply nothing to optimise.
4. **Housekeeping (optional):** You have 32 paused and 7 archived campaigns. Once
   spend resumes, it's worth reviewing whether the 15 enabled ones are the right
   set to have live, given the tight ~$1.50/day budgets on most of them.

**Enabled campaigns (all currently serving $0):**

| Campaign | Daily budget |
|---|---:|
| SP Isolated … Cat Deterrent Spray Exact | $1.50 |
| SP Isolated … Cat Deterrent Spray Phrase | $1.50 |
| SP Isolated … Pet Odor Eliminator Phrase | $2.50 |
| SP Odor Root 50k+ SV … Exact | $1.50 |
| SP Odor Root 25-50k SV … Phrase | $1.50 |
| SP Isolated … Pet Odor Eliminator Exact | $1.50 |
| SP Isolated … Cat Deterrent Exact | $1.50 |
| SP Home + Eliminator + Brand Root 10-25k SV … Exact | $1.50 |
| SP Cat Root 1-10k SV … Exact | $1.50 |
| SP Isolated … Cat Deterrent Phrase | $1.50 |
| SP Litter + Urine Root 10-25k SV … Exact | $1.50 |
| SP Odor Root 25-50k SV … Exact | $1.50 |
| SP Auto … B0FXW3GW5F | $1.50 |
| SP KT \| ST w/ Sales | $1.50 |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | $1.50 |
| **Total enabled budget/day** | **$23.50** |

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first run of this report type,
so there is nothing to compare against. This report establishes the baseline.

| Metric | This report | Previous | Change (#) | Change (%) |
|---|---:|---:|---:|---:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | — | — | — | — |
| ROAS | — | — | — | — |

**Verdict:** Can't say improved or worsened without a prior report. The headline
reality for this window is simply that no ads ran.

---

*Data source: Amazon Advertising API (Sponsored Products v3 reporting), US profile
26765323558215. Window 2026-10-09 to 2026-10-10. Figures are final (48h lag respected).*

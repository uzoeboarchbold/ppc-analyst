# PPC 2-Day Report — 15–16 Oct 2026

**Account:** Uzoebo Archbold E-Commerce — US (amazon.com), Sponsored Products
**Window covered:** 15 Oct 2026 – 16 Oct 2026 (2 full days, account time)
**Generated:** 19 Oct 2026, 16:15 PDT (data ends 48h before run, as required)
**Currency:** USD

> **Read this first — your ads are not running.** There was **no Sponsored
> Products activity at all** in this window: zero impressions, zero clicks,
> zero spend, zero sales. This is not a reporting error — the data pulled
> cleanly from the Amazon Ads API. Your 54 campaigns are switched ON, but the
> advertising account shows **no valid payment method**, which is the usual
> reason Amazon stops showing enabled ads. Ads have effectively been dark since
> mid-September. **Action: add/fix the payment method on your Amazon Ads
> account and the campaigns should start serving again.** (One setup note: the
> saved `AMZ_PROFILE_ID` was invalid; I identified the correct US account
> automatically and used it — details at the bottom.)

---

## Part A — Data Table (by campaign)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| _All campaigns (54 enabled/paused)_ | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

No individual campaign served a single impression in the window, so there are
no per-campaign rows to break out. CTR, CPC, ACOS and ROAS are undefined when
there are no clicks or spend.

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00
- **Overall sales (from ads):** $0.00
- **ACOS:** n/a (no spend) — **ROAS:** n/a (no spend)
- **Best campaign / worst campaign:** n/a — nothing ran, so nothing can be
  ranked.
- **Wasted spend / negatives to add:** none to suggest — there was no spend to
  waste, because no ads were shown.
- **Well-converting search terms to add as exact-match:** none available — with
  no clicks or sales there is no search-term data to mine this period.

**What's actually going on.** Your campaigns are enabled and have daily budgets
(mostly $1.50), but Amazon is not serving them. The advertising profile reports
no valid payment method, which stops enabled ads from running. A wider check
confirms the pattern: essentially nothing has served since mid-September (just
287 impressions, 1 click and $0.08 of spend across all of early September, and
flat zero since).

**What to do next (in order):**
1. **Fix billing.** Log in to Amazon Advertising → Account settings → Billing,
   and add or update a valid payment method. This is almost certainly why the
   ads are off.
2. **Confirm serving resumes.** Within a day of fixing billing, impressions
   should reappear. The next 2-day report will show whether they did.
3. **Then review budgets/targets.** Once ads run again, most campaigns are on a
   $1.50/day budget — fine for testing, but we'll want to see which ones earn
   their keep before scaling.
4. Until billing is fixed, there is nothing to optimise — no amount of keyword
   or bid tuning matters while the ads can't be shown.

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report exists** — this is the first run, so there is no
baseline to compare against. All headline metrics are shown below as a starting
point for next time.

| Metric | This report (15–16 Oct) | Previous | Change (#) | Change (%) |
|---|--:|--:|--:|--:|
| Impressions | 0 | — | — | — |
| Clicks | 0 | — | — | — |
| Spend | $0.00 | — | — | — |
| Sales | $0.00 | — | — | — |
| ACOS | n/a | — | — | — |
| ROAS | n/a | — | — | — |

**Verdict:** Can't say improved or worsened without a baseline. The important
signal for next time is simply: did impressions come back above zero (billing
fixed) or not.

---

### Notes on data sourcing (for transparency)
- Pulled live from the Amazon Advertising API (Sponsored Products v3 reporting:
  campaign, targeting, and search-term reports) for 15–16 Oct 2026. All three
  returned zero rows, confirming no activity.
- The configured `AMZ_PROFILE_ID` was not a usable profile id (it held an
  `amzn1.application…` value). I looked up the account's real profiles and used
  the active **US** seller profile (`26765323558215`, amazon.com). The CA and MX
  profiles on the same account have no campaigns. Worth correcting the stored
  `AMZ_PROFILE_ID` so future runs don't depend on this fallback.
- **Email delivery:** the Gmail connector is connected but not enabled for this
  automated chat, so the report could not be emailed automatically this run. It
  was saved to the "PPC Reports" Drive folder and committed to the repo. Enable
  Gmail for the chat to restore automatic emailing.

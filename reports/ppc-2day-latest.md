# PPC 2-Day Report — June 18–19, 2026

**Marketplace:** Amazon US (Sponsored Products) · **Currency:** USD
**Report window:** 18 Jun 2026 – 19 Jun 2026 (the 2 full days ending 48h before the 22 Jun run)
**Generated:** 22 Jun 2026

---

## ⚠️ Read this first

**Your Sponsored Products ads served NOTHING in this window.** Across both days
(18 and 19 June) there were zero impressions, zero clicks, zero spend and zero
sales. This is not a data glitch — the figures for early June came back fine.
Your campaigns simply stopped delivering. The last day with any activity was
**8 June**, and delivery has been flat at zero since 10 June.

Most likely causes: daily budgets exhausted, campaigns paused, or a billing /
payment problem on the account. **This needs a manual check in Seller Central /
Campaign Manager.** Until it's fixed, you are getting no advertising sales.

Two technical notes for transparency:
- The `AMZ_PROFILE_ID` credential is set to an *application ID*, not a usable
  profile ID. I worked around it by looking up the account's real profiles and
  using the **US** profile (the primary marketplace). Worth correcting the
  credential so future runs are unambiguous.
- **The email could not be sent** — there is no email tool connected to this
  environment. The report has been committed to the repository and uploaded to
  the Google Drive "PPC Reports" folder instead.

---

## Part A — Data table (per campaign)

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| _(no campaigns served in this window)_ | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL (18–19 Jun)** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

### For context — last active day (8 June 2026)
This is *outside* the report window, shown only so you can see what "normal"
recently looked like before delivery stopped.

| Date | Impressions | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 8 Jun 2026 | 1,180 | 9 | 0.76% | 0 | $0.00 | $46.36 | $5.15 | ∞ (no sales) | 0.00 |
| 9 Jun 2026 | 159 | 0 | 0.00% | 0 | $0.00 | $0.00 | — | — | — |

---

## Part B — Summary (plain English)

- **Overall spend:** $0.00. **Overall sales:** $0.00. **ACOS / ROAS:** not
  applicable — nothing ran.
- **Best / worst campaign:** none to rank; no campaign delivered.
- **Wasted spend:** none *in the window* (because nothing spent). But note that
  on the last active day (8 June) the account spent **$46.36 for zero sales** —
  100% wasted. If campaigns are switched back on as-is, that waste resumes.
- **Search terms to add as exact-match:** none — there were no converting search
  terms (no clicks converted; no sales at all in the recent active period).
- **What to do next:**
  1. **Check the account today.** Confirm whether campaigns are paused, out of
     budget, or blocked by a billing issue. Re-enable delivery.
  2. **Before re-enabling, fix the money leak.** The 8 June data shows clicks
     with no sales. Review the targeting/keywords and the product listing
     (price, images, reviews) — paying for clicks that never convert is the real
     problem to solve, not just "turn ads back on".
  3. **Fix the `AMZ_PROFILE_ID` credential** so it holds the numeric US profile
     ID (26765323558215), and connect an email tool if emailed reports are wanted.

---

## Part C — Comparison to previous 2-day report

**No previous 2-day report exists** — this is the first one, so there is no prior
baseline to compare against. Headline metrics (spend, sales, ACOS, ROAS) will be
compared here from the next 2-day report onward.

For reference, this report's headline figures are:

| Metric | This report (18–19 Jun) |
|---|--:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| ACOS | n/a |
| ROAS | n/a |

**Verdict:** Can't say "improved" or "worsened" without a baseline, but in
absolute terms this is the worst possible state for an active advertiser —
the ads aren't running at all. Priority is to get delivery restored.

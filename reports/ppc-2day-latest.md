# PPC 2-Day Report — 14–15 October 2026

**Account:** Uzoebo Archbold E-Commerce (US marketplace, Sponsored Products)
**Date window covered:** Wednesday 14 Oct 2026 – Thursday 15 Oct 2026 (2 full days)
**Report generated:** 18 Oct 2026 (data ends 48h before run, as required)

> **⚠️ Read this first — no ads ran in this period.**
> I connected to the Amazon Ads API successfully and pulled the data, but
> **there was no advertising activity at all** on 14–15 October: zero
> impressions, zero clicks, zero spend and zero sales across every campaign.
> To check this wasn't a glitch, I also pulled the **last 30 days** (16 Sep –
> 16 Oct) — every single campaign-day came back with **0 impressions and
> $0.00 spend**. So the ads have not been serving for at least a month.
>
> **Most likely cause:** the US advertising profile shows **no valid payment
> method on file** (`validPaymentMethod: false`). Amazon will not show
> Sponsored Products ads until a working payment method is attached. (It
> could also be out-of-stock or suppressed product listings, but the payment
> flag is the strongest signal.) This can't be fixed through the API — it
> needs sorting in Seller Central. **See "What to do next".**

---

## Part A — Data Table

All 15 currently-enabled campaigns, for 14–15 Oct 2026. Every metric is zero
because nothing served.

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SP Auto 6K-PZMX-MTDZ B0FXW3GW5F | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Spray Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Spray Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Cat Deterrent Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Pet Odor Eliminator Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Isolated – Pet Odor Eliminator Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 50k+ SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV Phrase | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Odor Root 25–50k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Home + Eliminator + Brand Root 10–25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Cat Root 1–10k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP Litter + Urine Root 10–25k SV Exact | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP KT \| ST w/ Sales | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| SP \| Cat Tunnel Bed Pink Only \| Exact Ranking \| Louise | 0 | — | 0 | — | 0 | $0.00 | $0.00 | — | — | — |
| **TOTAL** | **0** | **—** | **0** | **—** | **0** | **$0.00** | **$0.00** | **—** | **—** | **—** |

*(39 further campaigns are Paused or Archived and also had no activity.)*

---

## Part B — Summary (plain English)

- **Overall:** You spent **$0.00** and made **$0.00** in sales from
  Sponsored Products over these two days. ACOS and ROAS can't be calculated
  because there was no spend. This is the same story for the whole past month.
- **Why:** Your ads simply aren't being shown. The strongest clue is that the
  US advertising account has **no valid payment method attached**. Amazon
  pauses ad delivery across the whole account until that's fixed, which would
  explain why all 15 enabled campaigns show nothing.
- **Best / worst campaigns:** Not applicable — with no data, no campaign is
  out-performing or under-performing another. Everything is flat at zero.
- **Wasted spend / negatives to add:** None — you can't waste spend when
  nothing is spending. No negative-keyword suggestions this period.
- **Winning search terms to add as exact-match:** None available — there were
  no clicks or conversions to learn from.
- **The bottom line:** This isn't a performance problem to optimise; it's a
  **delivery problem to unblock**. Nothing in the bids, budgets or keywords is
  the issue — the account just isn't being allowed to run.

### What to do next
1. **Check the US account's payment method in Seller Central** → Advertising /
   Billing. The API reports no valid payment method on file; add or update a
   working card so ads can serve. This is almost certainly the single fix.
2. **Confirm the product is in stock and buyable.** If B0FXW3GW5F (Cat
   Deterrent Spray / Pet Odor Eliminator) or the Cat Tunnel Bed listings are
   out of stock or suppressed, ads won't show even with billing fixed.
3. **Once ads are live again**, let them run 2–3 days, then this report will
   start showing real impressions, spend and sales to optimise against.
4. Nothing to change on campaign structure right now — the 15 enabled
   campaigns and ~$22.50/day of combined budget are ready to go the moment
   delivery is unblocked.

---

## Part C — Comparison to Previous 2-Day Report

**No previous 2-day report was found** — this is the first run of this report,
so there is nothing to compare against yet. From the next run onward this
section will show the change in each headline metric (spend, sales, ACOS,
ROAS) as a number and a percentage, up or down.

For reference, the baseline this run establishes:

| Metric | This report (14–15 Oct) |
|---|--:|
| Impressions | 0 |
| Clicks | 0 |
| Spend | $0.00 |
| Sales | $0.00 |
| Purchases | 0 |
| ACOS | n/a |
| ROAS | n/a |

---

*Data source: Amazon Advertising API (Sponsored Products), US profile
26765323558215. Attribution: 7-day. Prepared automatically by the PPC Analyst.*

> **Delivery note:** Automatic emailing was not possible this run — the Gmail
> connector is not enabled in the automation's chat session. This report is
> saved in the repo (`reports/`) and uploaded to the Google Drive "PPC
> Reports" folder. Enable Gmail for the session to also receive it by email.

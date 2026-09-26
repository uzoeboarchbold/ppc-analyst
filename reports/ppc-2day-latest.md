# PPC 2-Day Report — 22–23 September 2026

**Report type:** 2-day | **Dates covered:** 2026-09-22 to 2026-09-23 (2 full days)
**Generated:** 2026-09-26 (automated run) | **Compares against:** previous 2-day report

---

## ⚠️ Please read first — no numbers this run (data could not be pulled)

This report has **no performance figures** because the automated run could not
reach the advertising data for your account. Nothing is wrong with your ads —
this is a connection/permissions issue on the reporting side. I did not make up
any numbers.

**In plain English:**
- Logging in to Amazon worked fine (the login token is valid).
- Your Amazon Ads **account profile is in a region (Europe or Far East)** that
  this automated environment is **not currently allowed to connect to**. The
  network security policy blocks those two Amazon data addresses, so the request
  is refused before it can even ask for your figures.
- The one region this environment *can* reach (North America) does not contain
  your account, so there is no data to read there.

**What I tried:**
1. Got a fresh Amazon login token — success.
2. Checked the North America Amazon Ads server — it responded, but it only holds
   Canada / Mexico / USA accounts, and yours is not one of them.
3. Tried the Europe and Far-East Amazon Ads servers — both were **blocked (403)**
   by this environment's network policy, so the connection never went through.
4. Stopped there, because the policy explicitly says blocked connections must be
   reported, not worked around.

**How to fix it (one of these — needs a human, ~5 minutes):**
- **Option A (easiest):** if the account really is North American, update the
  `AMZ_PROFILE_ID` setting to the correct North-America profile ID for the
  account. Then the next run will work with no other changes.
- **Option B:** if the account is genuinely in Europe or the Far East, ask
  whoever manages this automation's network policy to **allow outbound access to
  the matching Amazon Ads address** — either `advertising-api-eu.amazon.com`
  (Europe) or `advertising-api-fe.amazon.com` (Far East).

Once either fix is in place, the next scheduled run will pull the real figures
automatically. I have logged the details in `notes-to-self.md` so the fix is
remembered.

---

## Part A — Data table (per campaign + totals)

*No data available for this window — see the note above.*

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| _(unavailable)_ | — | — | — | — | — | — | — | — | — | — |
| **TOTAL** | — | — | — | — | — | — | — | — | — | — |

## Part B — Summary

No summary can be produced for 22–23 September 2026 because the underlying
Sponsored Products data could not be retrieved (connection blocked — see the
note at the top). Overall spend, sales, ACOS, ROAS, best/worst campaigns, wasted
spend, and suggested exact-match search terms will all be filled in on the next
successful run.

**What to do next:** apply Option A or Option B above so the connection can be
made. No changes to your campaigns are recommended from this run, since no
performance data was seen.

## Part C — Comparison to previous 2-day report

No comparison is possible:
- This is the **first 2-day report** in the repository, so there is no prior
  report of this type to compare against, **and**
- This run produced no figures to compare in any case.

Headline-metric change table (spend, sales, ACOS, ROAS — number and %) will
begin from the first two successful runs onward.

---
*Automated PPC analyst run. Data source: Amazon Advertising API (Sponsored
Products). This run: authentication succeeded; data retrieval blocked by network
egress policy for the account's region.*

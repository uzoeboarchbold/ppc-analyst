# PPC 2-Day Report — 21–22 Aug 2026

**Report type:** 2-day · **Dates covered:** Fri 21 Aug 2026 and Sat 22 Aug 2026
(the two full days ending ~48h before the run, allowing for Amazon's data lag)
**Generated:** 2026-08-25 23:04 UTC · **Compared against:** n/a (first 2-day report)

---

## ⚠️ Could not pull the numbers this run — needs a quick fix from you

The report ran on schedule but **could not download any advertising data**, so
there are no figures below. Nothing here is invented. Here is what happened, in
plain English:

- **Logging in worked.** The saved login (client ID, secret and refresh token)
  is valid — the system got a fresh access token with no trouble.
- **Two things then blocked the data pull:**
  1. **The profile ID looks wrong.** The `AMZ_PROFILE_ID` setting holds a value
     that starts with `amzn…`. Amazon expects a **numeric** account/profile ID
     here (roughly a 10-digit number). When we used the current value, Amazon
     replied: *"Invalid Input … profile ID required."*
  2. **The account's region is off-limits to this run.** We can reach Amazon's
     **North America** servers, and they returned **0 advertising profiles** for
     this account — meaning the account isn't a North America one. The
     **Europe** and **Far East** servers, where the account most likely lives,
     are **blocked by this environment's network policy** (the connection is
     refused before it starts). Per the environment's own rules we must not try
     to route around that — it has to be opened up by an admin.

- **What we tried:** refreshed the login token (worked); listed profiles on the
  North America server (0 returned); tried Europe and Far East servers (blocked);
  and sent a test report request with the current profile ID (rejected as
  invalid). No retrying of the blocked region, as required.

### To fix (either or both — takes a few minutes)

1. **Set the correct numeric profile ID.** Replace `AMZ_PROFILE_ID` with the
   numeric profile ID for your Amazon Ads account (you can read it from the
   Amazon Ads console, or by listing profiles in your account's region).
2. **Allow your region.** If your Amazon account is European or Far-East based,
   add the matching Amazon Ads host
   (`advertising-api-eu.amazon.com` or `advertising-api-fe.amazon.com`) to this
   environment's allowed-network list, or run this routine from an environment
   that permits that region.

Once either/both are set, the next scheduled run will pull the data automatically
and this report will fill in normally.

---

## Part A — Data table (by campaign)

_No data available this run — see the note above. Table will populate once the
profile ID / region access is fixed._

| Campaign | Impressions | Top-of-search IS | Clicks | CTR | Purchases | Sales | Total cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — |
| **Total** | — | — | — | — | — | — | — | — | — | — |

## Part B — Plain-English summary

No spend, sales, ACOS or ROAS figures could be retrieved this run because the
data pull was blocked (see the note at the top). Therefore there are no
best/worst campaigns, no wasted-spend candidates, and no search terms to add as
exact-match to report yet.

**What to do next:** fix the profile ID and/or region access as described above.
No account changes are recommended from this run because there is no data to base
them on.

## Part C — Comparison to previous 2-day report

This is the **first** 2-day report, so there is no previous report to compare
against. Once a successful data pull exists, future runs will show the change in
each headline metric (impressions, clicks, spend, sales, ACOS, ROAS) as both a
number and a percentage.

---

_Automated PPC Analyst · Sponsored Products · generated hands-off. Credentials
are read from environment variables and are never printed._

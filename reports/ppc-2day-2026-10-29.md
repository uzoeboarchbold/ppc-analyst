# PPC 2-Day Report — 25–26 Oct 2026

**Report type:** 2-day · **Days covered:** Sunday 25 Oct 2026 and Monday 26 Oct 2026
**Generated:** 2026-10-29 (automated run) · **Status:** ⚠️ Could not pull data this run

---

## ⚠️ Read first — no numbers this run (and why)

This report has **no figures** because I could not reach the advertising data
for your account. I did **not** make any numbers up.

**In plain English:** your login worked fine, but the account's data lives in a
region (Europe / Far East) that this automated environment is currently **not
allowed to connect to**. The connection was blocked by a network rule, not by a
password or token problem.

**What I checked, step by step:**
1. Refreshed the access token with your credentials — ✅ worked.
2. Connected to the North America Amazon Ads server — ✅ worked, it returned 3
   advertising profiles — but **none of them is the profile this report is set
   to use** (`AMZ_PROFILE_ID`). So your account is not a North America account.
3. Tried the Europe server (`advertising-api-eu.amazon.com`) — ❌ **blocked**
   ("Tunnel connection failed: 403 Forbidden").
4. Tried the Far-East server (`advertising-api-fe.amazon.com`) — ❌ **blocked**
   the same way.

A "403" at this stage is a **network-policy block** by the environment itself,
not an Amazon error. I'm not permitted to bypass it, and retrying won't help.

**How to fix it (one-time, needs a person):**
- **Most likely:** allow this environment to reach the Europe/Far-East Amazon
  Ads servers. The environment's network policy is chosen when it's set up —
  see https://code.claude.com/docs/en/claude-code-on-the-web. Once
  `advertising-api-eu.amazon.com` (and/or `-fe`) is allowed, this report will
  run on its own next time.
- **Or, if your account really is North America:** set `AMZ_PROFILE_ID` to one
  of the 3 profiles the North America server returned.

Once either is done, the next scheduled run will produce the full table and
summary automatically — no other changes needed.

---

## Part A — Data table

Not available this run (data could not be pulled — see note above).

| Campaign | Impr. | ToS Impr. share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| *(no data)* | — | — | — | — | — | — | — | — | — | — |
| **TOTAL** | — | — | — | — | — | — | — | — | — | — |

## Part B — Summary

No performance summary this run — the data for your profile could not be
retrieved (network policy blocked the Europe/Far-East Amazon Ads servers where
your account lives). No overall spend/sales/ACOS/ROAS, best/worst campaigns,
wasted-spend negatives, or search terms to add can be reported until the
connection is allowed.

**What to do next:** have someone apply the one-time fix above (allow the
Europe/Far-East Ads servers for this environment, or point `AMZ_PROFILE_ID` at
a North America profile). After that, no further action is needed — the report
will populate automatically on the next run.

## Part C — Comparison to previous 2-day report

No comparison available. This is the **first 2-day report** (no earlier report
of this type exists in the `reports` folder), and this run produced no figures,
so there is nothing to compare yet. Once data flows, each report will show the
change in every headline metric vs. the previous 2-day report, as a number and
a percentage.

---

*Automated PPC report. Data lags ~48h, so this window ends 48h before the run.
Failure details are logged in `notes-to-self.md` for the next run.*

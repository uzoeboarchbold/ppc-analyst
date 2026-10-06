# PPC 2-Day Report — 2–3 Oct 2026 (Fri–Sat)

**Report type:** 2-day · **Dates covered:** 2 Oct 2026 – 3 Oct 2026 (UTC)
**Generated:** 6 Oct 2026 · **Data source:** Amazon Advertising API (Sponsored Products)

---

## ⚠️ Could not pull data this run — one setting needs fixing

**Plain English:** The login worked and your Amazon Ads account was reached
successfully, but the report could not be run because one configuration value
is wrong. The setting `AMZ_PROFILE_ID`, which tells Amazon *which advertising
account* to report on, is currently filled in with the wrong kind of value — it
holds an application ID (begins `amzn1.application…`) instead of the numeric
account/profile ID Amazon expects. Because of that, every data request was
rejected with the error **"Invalid scope."**

No numbers are shown below because I will not make up figures. Here is exactly
what I checked, and the one change that will fix it.

### What I verified (so you know the account is otherwise healthy)
- ✅ **Credentials are valid.** The client ID, client secret and refresh token
  all work — a fresh access token was issued without any problem.
- ✅ **Your account is reachable.** The Amazon Ads account responded and lists
  **three** advertising profiles:
  | Marketplace | Profile ID (numeric) | Type |
  |---|---|---|
  | United States (amazon.com) | `26765323558215` | Seller |
  | Canada (amazon.ca) | `2840235221595557` | Seller |
  | Mexico (amazon.com.mx) | `3892485344323414` | Seller |
- ❌ **The configured profile ID is not one of these.** It is an
  `amzn1.application…` value, which Amazon treats as an invalid profile, so the
  Sponsored Products report cannot run.

### The fix (about 30 seconds)
Set the environment variable **`AMZ_PROFILE_ID`** to a **numeric** profile ID
from the table above. For a US-based FBA business this is almost certainly the
United States profile:

```
AMZ_PROFILE_ID = 26765323558215
```

(Use the Canada or Mexico ID instead if the business you want reported on is
one of those.) Once this is updated, the next scheduled run will pull the data
automatically — no other change is needed.

### What else I tried
- Confirmed the North America API endpoint works; the EU and FE endpoints are
  blocked by this environment's network policy (expected — the account is US/NA,
  so NA is the correct one).
- Attempted the profile list both with and without the scope header to find the
  correct values (the three above).

---

## Part A — Data table
_Not available this run — see the blocker above. Will populate once
`AMZ_PROFILE_ID` is set to a numeric profile._

| Campaign | Impr. | TOS impr. share | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — |

## Part B — Summary
No spend, sales, ACOS or ROAS can be reported for 2–3 Oct 2026 because the data
pull was blocked by the configuration issue above. There are therefore no best/
worst campaigns, no wasted-spend negatives, and no search-term suggestions to
list this run.

**What to do next:** Update `AMZ_PROFILE_ID` to a numeric profile ID (likely
`26765323558215` for the US). The next run will then produce the full table and
recommendations automatically.

## Part C — Comparison to previous 2-day report
No previous 2-day report exists — this is the first run, so there is nothing to
compare against. The next successful run will become the baseline.

---

_Automated PPC report. If figures look off in a future run, check
`notes-to-self.md` in the repo for known issues and fixes._

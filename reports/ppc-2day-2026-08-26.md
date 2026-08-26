# PPC 2-Day Report — 22–23 Aug 2026

**Report type:** 2-day · **Dates covered:** 2026-08-22 to 2026-08-23
(2 full days, ending 48h before the 2026-08-26 23:06 UTC run to allow for
Amazon's ~48-hour data lag)
**Status:** ⚠️ COULD NOT PULL DATA — see note below. No numbers are reported
because none could be retrieved, and this report will never invent figures.

---

## ⚠️ What went wrong (plain English)

The report could not be produced this run because the automation cannot reach
your advertising account.

- **Logging in worked.** The stored client ID, secret and refresh token
  successfully obtained an access token from Amazon. So the credentials
  themselves are valid.
- **The account/profile ID is not usable.** Amazon needs a *numeric*
  advertising "profile ID" (like `1234567890`) to know which seller account to
  report on. The value currently stored (`AMZ_PROFILE_ID`) is instead an
  application-style ID beginning `amzn1.application...`. When sent to Amazon it
  is rejected with *"profile ID required."*
- **No profile to fall back on.** Asking Amazon to list the profiles this login
  can see (US/North America region) returned an **empty list** — this login is
  not currently attached to any advertising account in that region.
- **Other regions are blocked here.** The European and Far-East Amazon
  endpoints are blocked by this environment's network policy (403), so if your
  account is registered in the EU or Japan/Australia region, it can't be
  reached from here at all.

**What I tried:** refreshed the access token (worked), listed profiles in North
America (empty), and attempted a Sponsored Products report with the stored ID
(rejected as not a valid profile). I did not retry the blocked EU/FE endpoints,
as network-policy 403s should not be retried.

## ✅ How to fix it (one of these)

1. **Set the correct profile ID.** Replace `AMZ_PROFILE_ID` with the *numeric*
   advertising profile ID for your seller account. (In the Amazon Ads console
   or via `GET /v2/profiles` on the region where your account lives.)
2. **If your account is EU or FE (Japan/Australia/etc.),** ask for
   `advertising-api-eu.amazon.com` and/or `advertising-api-fe.amazon.com` to be
   added to this environment's allowed-network list.
3. **Confirm advertising access.** Make sure the refresh token was granted
   advertising permissions for a login that actually has access to the ad
   console for this account.

Once any of the above is done, the next scheduled run will pull the data and
produce the full report automatically.

---

## Part A — Data table

*Not available this run — no data could be retrieved (see note above).*

| Campaign | Impr. | Top-of-search IS | Clicks | CTR | Purchases | Sales | Spend | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — |
| **Total** | — | — | — | — | — | — | — | — | — | — |

## Part B — Summary

No spend, sales, ACOS, ROAS, best/worst campaigns, wasted-spend negatives or
search-term suggestions can be reported this run, because no data was
retrieved. **What to do next:** apply one of the fixes above so the connection
to Amazon Ads is restored; the following run will then report normally.

## Part C — Comparison to previous 2-day report

No previous 2-day report exists in the `reports/` folder — this is the first
2-day run — so there is nothing to compare against. Additionally, with no data
retrieved this run, a metric-by-metric comparison is not possible. Both a
baseline and a fresh pull are needed before change figures can be shown.

---

*Automated PPC Analyst · generated 2026-08-26 23:06 UTC · data source: Amazon
Advertising API (Sponsored Products).*

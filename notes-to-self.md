# Notes to Self — PPC Analyst

Running log of lessons so future automated runs work better. Newest first.

## 2026-11-19 (first run — 2-day report)

**AMZ_PROFILE_ID is misconfigured.** The env var contains an LWA *application* ID
(`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric Amazon
Advertising profile ID. The Ads API needs a numeric profile ID in the
`Amazon-Advertising-API-Scope` header, so the configured value cannot be used
directly. Action taken: called `GET /v2/profiles` and picked the correct profile.

**Correct profiles for this account** (seller "Uzoebo Archbold E-Commerce",
entity A1C2I8MOP52E35), all on the NORTH AMERICA endpoint
`https://advertising-api.amazon.com`:
- US — profileId `26765323558215`, USD, dailyBudget $40, validPaymentMethod=**false**. **This is the only account with campaigns (15 SP campaigns). Use this one.**
- CA — profileId `2840235221595557`, CAD, no campaigns.
- MX — profileId `3892485344323414`, MXN, no campaigns.
Future runs: if AMZ_PROFILE_ID is still the LWA app id, use US `26765323558215`.

**Network policy blocks EU/FE Ads endpoints.** `advertising-api-eu.amazon.com`
and `advertising-api-fe.amazon.com` return 403 from the agent proxy. Only the
NA endpoint is reachable. Fine here — this account is NA.

**Account is NOT serving ads.** All 15 US campaigns are status ENABLED but have
had ZERO impressions/clicks/spend/sales every day for the whole trailing 14 days
(checked 2026-11-03 → 2026-11-16). Almost certainly because the US seller
account has `validPaymentMethod=false`, which halts ad delivery. This is the
headline finding, not an API error. Do NOT treat zeros as a data failure — the
API works and the zeros are real. The fix is on the account owner's side
(update the payment/billing method in Seller Central / Amazon Ads).

**Empty targeting/search-term reports are expected while delivery is zero.**
`spTargeting` and `spSearchTerm` v3 reports return 0 rows when there were no
impressions. That is correct behaviour, not a bug.

**Working API flow (v3 reporting):** refresh token -> access token at
`https://api.amazon.com/auth/o2/token`; POST `/reporting/reports` with
Content-Type `application/vnd.createasyncreportrequest.v3+json`, poll
`/reporting/reports/{id}` (~COMPLETED in <1 min for small accounts), download
the GZIP_JSON url. Script kept in scratchpad `pull.py`.

**Date window logic (2-day report):** data lags ~48h. Cover the 2 full days
ending 48h before the run. Run Thu 2026-11-19 -> covered Sun 2026-11-15 &
Mon 2026-11-16.

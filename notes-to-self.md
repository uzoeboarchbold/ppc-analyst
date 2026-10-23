# Notes to Self — PPC Analyst

Running log of lessons so future automated runs are faster and more reliable.

## Environment / setup
- Repo starts nearly empty each session; create `reports/` if missing.
- No `requests` module available. Use Python stdlib `urllib` with an SSL
  context built from `/root/.ccr/ca-bundle.crt` and a ProxyHandler using
  `$HTTPS_PROXY`. Run scripts with `python3 -I`.
- Do NOT print credential values — the auto-mode classifier blocks it
  ("Credential Materialization"). Keep secrets in-process; only print
  booleans/metadata when diagnosing.

## Amazon Ads API (what works)
- Token refresh: `POST https://api.amazon.com/auth/o2/token`
  (grant_type=refresh_token + client_id/secret/refresh_token). WORKS.
- Account region is **NA** → host `https://advertising-api.amazon.com`.
  EU/FE hosts are blocked by the proxy (403 Tunnel) and are not this account.
- `GET /v2/profiles` (no scope header) lists profiles. This account has THREE
  seller profiles: CA `2840235221595557`, MX `3892485344323414`,
  US `26765323558215`.
- Sponsored Products reporting v3: `POST /reporting/reports` with
  Content-Type `application/vnd.createasyncreportrequest.v3+json`, then poll
  `GET /reporting/reports/{id}` until status COMPLETED, then GET the signed
  `url` (GZIP_JSON). reportTypeIds used: `spCampaigns` (groupBy campaign),
  `spTargeting` (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
  `topOfSearchImpressionShare` is a valid spCampaigns column.

## KNOWN CONFIG PROBLEM (2026-10-23)
- **`AMZ_PROFILE_ID` env var is INVALID.** Its value is 50 characters and
  non-numeric. A valid Amazon profile ID is a 14–16 digit integer. Using it
  as the `Amazon-Advertising-API-Scope` header returns HTTP 400
  "profile ID required", so no report can be scoped with it as configured.
- Workaround used: pulled data for ALL THREE profiles the credentials
  return, labelled each marketplace, and flagged the misconfig in the report
  + notified the operator.
- **ACTION for operator:** set `AMZ_PROFILE_ID` to one of the three integer
  IDs above (most likely US `26765323558215`). Until then, future runs must
  keep auto-selecting/looping profiles rather than trusting the env var.

## Date window logic
- Data lags ~48h. 2-day report: cutoff date = today − 48h; cover the TWO full
  days BEFORE that cutoff date (i.e. cutoff−2 and cutoff−1). Example matches:
  Sunday run → cutoff Fri → cover Wed+Thu. 2026-10-23 run → cutoff 2026-10-21
  → cover 2026-10-19 and 2026-10-20.

## Delivery
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `ppc-2day-YYYY-MM-DD.md`.
- Commit+push to branch `claude/great-hopper-ys5pzc`.
- Upload to Google Drive folder 'PPC Reports'; email to uzoebo.archbold@gmail.com.

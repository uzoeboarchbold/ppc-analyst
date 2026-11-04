# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future runs are faster and more reliable. Append; don't delete.

## Account / environment facts
- Seller account: **Uzoebo Archbold E-Commerce** (seller id `A1C2I8MOP52E35`). Product line is pet odor / cat deterrent (ASIN B0FXW3GW5F and a cat tunnel bed).
- Amazon Ads API auth works via LWA refresh token in the **North America** region only:
  - Token URL: `https://api.amazon.com/auth/o2/token`
  - Ads API base: `https://advertising-api.amazon.com`
  - The EU (`advertising-api-eu`) and FE (`advertising-api-fe`) hosts are **blocked by the sandbox proxy (403 tunnel)** — don't bother trying them.
- **`AMZ_PROFILE_ID` env var is MISCONFIGURED.** It contains an *application id*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), **not** a numeric profile id.
  Ignore it. The real NA profiles for this account are:
  - US (primary, USD): **`26765323558215`**  ← use this one for the PPC report
  - CA (CAD): `2840235221595557` (no campaigns)
  - MX (MXN): `3892485344323414` (no campaigns)
  Discover live via `GET /v2/profiles` and pick `countryCode == "US"` / `type == seller`.
  (If the env var ever gets fixed to the numeric US id, great — but don't rely on it.)

## Amazon Ads API v3 reporting gotchas
- Use the async reporting v3 endpoint `POST /reporting/reports`, content type
  `application/vnd.createasyncreportrequest.v3+json`, then poll `GET /reporting/reports/{id}`
  until `COMPLETED`, download the gzipped-JSON `url`.
- **Column names:** there is NO `acosClicks30d` / `roasClicks30d` / `purchases`/`sales` bare.
  Valid attribution-window columns are 7d / 14d (e.g. `purchases14d`, `sales14d`,
  `acosClicks14d`, `roasClicks14d`). Standard choice = **14d window**. (30d exists only for
  `purchases30d`/`sales30d`/`unitsSold*30d`, NOT for acos/roas — those cap at 14d.)
- Report types used: `spCampaigns` (groupBy `campaign`), `spTargeting` (groupBy `targeting`),
  `spSearchTerm` (groupBy `searchTerm`). `topOfSearchImpressionShare` is available on
  spCampaigns and spTargeting, but NOT on spSearchTerm.
- `requests` is not installed in this sandbox — use stdlib `urllib`.

## Date window rule (2-day report)
- Data lags ~48h. Window = the 2 full calendar days ending at the day that is 48h before the run.
  Worked example from the brief: run Sun 00:00 → cover Wed + Thu.
- 2026-11-04 run → window **2026-10-31 to 2026-11-01**.

## History
- **2026-11-04 (first run):** US account had **15 ENABLED campaigns but ZERO delivery**
  (0 impressions/clicks/cost/sales) for Oct 31–Nov 1. Root cause almost certainly
  `validPaymentMethod: false` on the US profile — Amazon does not serve ads without a valid
  payment method. No previous 2-day report existed, so no comparison baseline. Flagged payment
  method to the user as the priority fix. Watch next run to see if spend resumes.

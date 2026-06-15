# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future runs are faster and more reliable.

## Account / API facts (verified 2026-06-15)
- **Region: NA only.** `advertising-api.amazon.com` works. `advertising-api-eu`
  and `advertising-api-fe` are BLOCKED by the network egress allowlist — do not
  bother trying them.
- **AMZ_PROFILE_ID env var is NOT a usable profile ID.** It holds an application
  id (`amzn1.application.…`). The Ads API needs the numeric profile id in the
  `Amazon-Advertising-API-Scope` header. Get it from `GET /v2/profiles`.
  - The active account is the **US seller profile: `26765323558215`** (USD,
    America/Los_Angeles, seller "Uzoebo Archbold E-Commerce"). Use this one.
  - (Other profiles exist: CA `2840235221595557`, MX `3892485344323414` — ignore
    unless asked.)
- Token refresh works fine via `https://api.amazon.com/auth/o2/token` with the 4
  env vars. Access token lasts ~1h; refresh once per long poll.

## Reporting API (v3) gotchas
- Endpoint: `POST /reporting/reports`, header
  `Accept: application/vnd.createasyncreportrequest.v3+json`.
- For `timeUnit: "SUMMARY"` do **NOT** include a `date` column → 400 error
  ("date is not a supported column for this time unit"). Only add `date` if you
  set `timeUnit: "DAILY"`.
- Report types used: `spCampaigns` (groupBy `campaign`), `spTargeting`
  (groupBy `targeting`), `spSearchTerm` (groupBy `searchTerm`).
- Reports are async and SLOW here — frequently 5–10+ min in PENDING before
  COMPLETED. Poll every ~25s with a generous deadline (run the poller as a
  background task; don't let it die at a short timeout).
- Download URL from the COMPLETED response is a plain S3 link → fetch with NO
  auth header, then gzip-decompress.
- ACOS/ROAS are not native columns — compute: ACOS = cost/sales, ROAS = sales/cost.
- `topOfSearchImpressionShare` comes back `null` when there are no impressions.

## Account state (as of 2026-06-15)
- Almost the entire account is PAUSED/ARCHIVED. Only **two** campaigns are
  ENABLED, both launched 2026-06-09, $8/day each:
  - `SP KT | ST w/ Sales`
  - `SP PT | ST w/ Sales`
  - (These target the Cat Deterrent / Pet Odor product, ASIN B0FXW3GW5F.)
- In the 2-day window (Jun 11–12) BOTH enabled campaigns served **zero**
  impressions/clicks/spend/sales. Targeting & search-term reports came back
  empty (consistent with no serving). This is REAL data, not an error — likely
  bids too low / targets too narrow on brand-new campaigns. Flag it, don't
  invent numbers.

## Report bookkeeping
- 2-day window rule: cover the 2 full days ending 48h before run. Run Jun 15 →
  cutoff Jun 13 00:00 → window = **Jun 11 & Jun 12**.
- Save to `reports/`: overwrite `ppc-2day-latest.md` + dated
  `ppc-2day-YYYY-MM-DD.md`. Previous report of THIS type is the comparison base.
- 2026-06-15 was the FIRST 2-day report → no prior baseline to compare against.

## TODO / still unverified
- Google Drive upload: folder 'PPC Reports'. (Drive MCP tools available —
  search_files / create_file. Verify folder exists / create file under it.)
- Email send: needed to email uzoebo.archbold@gmail.com. As of first run I had
  no confirmed email-sending tool wired up — CHECK for a Gmail/email MCP tool
  before claiming the email was sent. If none exists, say so in the report and
  note it here.

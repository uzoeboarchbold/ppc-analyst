# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest at top.

## Account / API facts (confirmed 2026-06-23)
- **AMZ_PROFILE_ID env var is NOT a usable profile ID.** It contains an LWA
  *application* id (`amzn1.application....`), not the numeric advertising
  profileId the API needs. Do NOT pass it as the Scope header — it will fail.
- **Use the numeric US profile: `26765323558215`** (countryCode US, USD,
  seller "Uzoebo Archbold E-Commerce"). This is the only active account.
  - CA profile `2840235221595557` and MX profile `3892485344323414` exist but
    have **0 Sponsored Products campaigns** — ignore them.
- **Region = NA only.** Use host `https://advertising-api.amazon.com`.
  The EU (`-eu`) and FE (`-fe`) hosts are **blocked by the agent proxy
  (403)** — don't waste retries on them; this account is NA anyway.
- Token refresh: POST `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client id/secret. Works fine.
- Reporting = **v3 async**: POST `/reporting/reports` → poll
  GET `/reporting/reports/{id}` until COMPLETED → download gzipped JSON `url`.
  Reports can take 1–3 min to generate; poll with ~15–20s gaps. Empty/no-activity
  windows return a valid file with **0 rows** (not an error).
- Report type ids used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm). Add `"date"` to
  columns if you want DAILY breakdown, else timeUnit=SUMMARY.

## Standing issue to watch
- **Ads stopped serving ~June 10, 2026.** Last real activity was Jun 8–9
  (tiny: ~$46 spend, 9 clicks, 0 orders). From Jun 10 onward: 0 impressions,
  0 spend, 0 sales. The 2 ENABLED campaigns ("SP KT | ST w/ Sales",
  "SP PT | ST w/ Sales", $8/day each) are getting **no impressions** despite
  being enabled — likely out-of-stock ASINs, bids too low to win auctions, or
  account-level pause. Flag this until it changes.

## Date window logic (data lags 48h)
- 2-day report: cover the 2 full days ending 48h before run time.
  Run Tue 2026-06-23 23:02 UTC → 48h back = Sun 06-21 → last 2 full days =
  **2026-06-19 and 2026-06-20**.

## Reports / outputs
- Save to `reports/`: overwrite `ppc-2day-latest.md` + dated `ppc-2day-YYYY-MM-DD.md`.
- Previous report of THIS type: find latest dated `ppc-2day-*.md` (excluding
  today's) to compare. First run = no prior, so no comparison.
- Also upload to Google Drive folder "PPC Reports" and email to
  uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

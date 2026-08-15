# Notes to Self — PPC Analyst runs

Lessons learned, applied on every run. Keep this current.

## Account / credentials
- `AMZ_PROFILE_ID` env var is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an **application-style ID, NOT a valid numeric Amazon Ads profile ID**.
  It cannot be used as the `Amazon-Advertising-API-Scope` header — the API needs a numeric profileId.
- Real profiles on this account (from `GET /v2/profiles`, NA region):
  - **US seller `26765323558215`  ← use this (the operating FBA marketplace)**
  - CA seller `2840235221595557`
  - MX seller `3892485344323414`
- So: ignore `AMZ_PROFILE_ID`, use US `26765323558215`. Flag this in the report until the env var is fixed.

## API / endpoints
- Region: **NA** endpoint works: `https://advertising-api.amazon.com`.
  EU/FE endpoints (`advertising-api-eu`/`-fe`) are blocked by the outbound proxy (403 tunnel). Don't bother; account is NA.
- Token: `POST https://api.amazon.com/auth/o2/token` with grant_type=refresh_token. Works.
- Reporting v3: `POST /reporting/reports`, header `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  Poll `GET /reporting/reports/{id}` until status `COMPLETED`, then download the `url` (GZIP JSON).

## spCampaigns report columns
- `acosClicks7d` and `roasClicks7d` are **NOT valid** columns for spCampaigns → 400 error.
  **Compute ACOS = cost / sales7d, ROAS = sales7d / cost yourself.** (roasClicks14d exists but we standardise on 7d.)
- Valid/used columns: campaignName, campaignId, impressions, topOfSearchImpressionShare, clicks, cost,
  purchases7d, sales7d, clickThroughRate, costPerClick.
- `topOfSearchImpressionShare` IS available on spCampaigns (a fraction, e.g. 0.13 = 13%). null when 0 impressions.

## Data characteristics (as of 2026-08-15 run)
- Account is essentially dormant / freshly launched: tiny impression volume (tens/day), **0 clicks, $0 spend, $0 sales**.
- spSearchTerm report returns 0 rows when there are no clicks (no attributed search terms). Expected, not a bug.
- Product line: pet odor eliminator (ASIN B0FXW3GW5F) + a cat tunnel bed. 8 SP campaigns, most getting near-zero traffic.

## Delivery (Step 4)
- **Google Drive upload works** via `mcp__Google-Drive__create_file` (use `contentMimeType: text/markdown`,
  `disableConversionToGoogleType: true`). Folder "PPC Reports" id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
- **Email does NOT work in this scheduled/headless run.** The Gmail connector is installed but
  `enabledInChat: false` (interactive-OAuth connectors aren't loaded in cron runs). No `mcp__*gmail*` send tool
  is available. Report is delivered via repo commit + Drive instead; the owner must enable the Gmail connector
  for scheduled sessions if automated email is required, OR wire up an SMTP/API-key mailer via env vars.

## Reports
- Save to `reports/`: overwrite `ppc-2day-latest.md` + dated copy `ppc-2day-YYYY-MM-DD.md`.
- Previous-report comparison: find the most recent prior `ppc-2day-*.md` (excluding latest). First run = none yet.

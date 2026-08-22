# Notes to Self — PPC Analyst

Living memory for the automated PPC reporting runs. Read this first each run.

## Account / API facts (confirmed 2026-08-22)
- **AMZ_PROFILE_ID is misconfigured.** The env var holds an *application ID*
  (`amzn1.application....`), NOT a numeric Ads API profile scope. Do NOT pass it
  as `Amazon-Advertising-API-Scope`. Instead resolve the real profile each run:
  `GET https://advertising-api.amazon.com/v2/profiles`.
- **Correct profile = US seller `26765323558215`** (USD). It's the only profile
  with real advertising activity (daily budget $40, 54 SP campaigns). The CA
  (`2840235221595557`) and MX (`3892485344323414`) profiles show placeholder
  max budgets and no campaigns — ignore them unless told otherwise.
- **Region = NA** endpoint `advertising-api.amazon.com`. EU/FE endpoints are
  blocked by the agent proxy (403 CONNECT tunnel) and not relevant anyway.
- Auth: refresh-token exchange at `https://api.amazon.com/auth/o2/token` works
  fine. Access token lasts 3600s.

## API mechanics that work
- **v2 `/v2/sp/campaigns` is DEAD** (404 "Method Not Found"). Use v3:
  `POST /sp/campaigns/list` with header
  `Content-Type: application/vnd.spCampaign.v3+json`.
- **Reporting = v3 async.** `POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  Report types used: `spCampaigns` (groupBy `campaign`, has
  `topOfSearchImpressionShare`), `spTargeting` (groupBy `targeting`),
  `spSearchTerm` (groupBy `searchTerm`). Poll `GET /reporting/reports/{id}`;
  status goes PENDING → PROCESSING → COMPLETED (~40–60s). Download the `url`
  (GZIP_JSON), gunzip, parse.
- Reports only return rows for entities with data in the window; zero-impression
  campaigns are omitted. Derive CTR/CPC/ACOS/ROAS yourself (not returned).
  purchases/sales use the `purchases7d` / `sales7d` columns.

## Date window (data lags ~48h)
- 2-day report: the 2 most recent *fully finalized* calendar days, i.e. days
  entirely ≥48h old. If the run is not at midnight, the day whose end is <48h
  ago is NOT yet safe — exclude it. E.g. run Sat 2026-08-22 23:04 UTC →
  covered Aug 18 + Aug 19 (Aug 20 only ~47h finalized, excluded).

## Business context
- Niche: cat products (cat deterrent / odor eliminator spray B0FXW3GW5F; cat
  tunnel/cave beds). Most campaigns are PAUSED/ARCHIVED with $1.50 daily budgets;
  only a handful ENABLED. Traffic is very low, so short-window reports will often
  show tiny numbers (single-digit clicks, frequently zero sales). This is normal
  for this account, not a data error.

## Delivery
- Google Drive upload works (folder "PPC Reports", id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`).
  Markdown uploaded via `create_file` converts to a Google Doc — fine for viewing.
- **Email step is BLOCKED.** The Gmail connector exists but is `enabledInChat:false`
  for this automated session, so no email can be sent. Needs the user to enable
  the Gmail connector for this chat/automation. Until then, deliver via Drive/repo
  only and flag it at the top of the report + notify the user.

## Run log
- 2026-08-22: First 2-day report (baseline, no prior report to compare).
  Window Aug 18–19. Total spend $1.17, 106 impr, 4 clicks, 0 sales.
  Saved to repo + Drive OK. Email NOT sent (Gmail connector disabled in chat).

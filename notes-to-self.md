# Notes to Self — PPC Analyst

Lessons learned across runs. Read this first, apply, and append new lessons.

## Account / API setup
- **Marketplace:** Active advertising is on the **US** seller profile only.
  - US profile ID: `26765323558215` (USD, daily budget ~$40). CA and MX profiles exist but have **zero campaigns** — ignore them.
- **`AMZ_PROFILE_ID` env var is WRONG:** it contains an application ID
  (`amzn1.application....`), not a numeric Ads profile ID. Do NOT pass it as the
  `Amazon-Advertising-API-Scope` header. Hardcode / resolve to `26765323558215`.
  (If it gets fixed to the numeric ID later, prefer the env var again.)
- **Region:** North America — `https://advertising-api.amazon.com`. EU/FE endpoints
  are blocked by the proxy (403) and are not needed.
- **Auth:** refresh-token flow at `https://api.amazon.com/auth/o2/token` works fine.
- **Do not name a local python module `token.py`** — it shadows the stdlib `token`
  module and breaks `requests`/`urllib3` imports. Use `amztoken.py`.

## Reporting API (v3)
- Use `POST /reporting/reports` with `Content-Type:
  application/vnd.createasyncreportrequest.v3+json`.
- Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`.
  Targeting report: `reportTypeId=spTargeting`, `groupBy=["targeting"]`.
- Reports complete in well under a minute for this small account; poll the report
  URL, download, `gzip.decompress`, `json.loads`.
- ACOS/ROAS/CTR/CPC are not all returned directly — compute them from
  impressions/clicks/cost/purchases7d/sales7d. Guard divide-by-zero.
- Escape `|` characters in campaign names before putting them in markdown tables
  (several campaigns contain literal pipes).

## Date window
- Data lags ~48h. For the 2-day report, cover the 2 full finalised days ending 48h
  before the run. Run on 31 Aug 2026 23:04 UTC → covered **27–28 Aug 2026**.

## Account state (as of 27–28 Aug 2026)
- Extremely low delivery: ~238 impressions / 1 click / $0.25 spend / 0 sales over 2
  days. Top-of-search impression share near 0% everywhere. Root cause is almost
  certainly **bids too low** (budget is not the limiter — $0.25 spent vs $40/day).
  Watch whether bids get raised and delivery improves.

## Delivery / send
- Save to `reports/ppc-2day-latest.md` (overwrite) + dated copy
  `reports/ppc-2day-[run-date].md`. Commit to branch `claude/great-hopper-vbzi2l`.
- Upload same report to Google Drive folder **"PPC Reports"** (folder id
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Use `create_file` with `textContent`,
  `contentMimeType: text/markdown`, `disableConversionToGoogleType: true`.
- **EMAIL STEP BLOCKED (2026-08-31 run):** The Gmail connector is installed but
  `enabledInChat: false`, so its send tools are NOT loaded in the scheduled session
  and the report email could NOT be sent. ACTION FOR THE OWNER: enable the Gmail
  connector for this chat/automation in connector settings so future runs can email
  uzoebo.archbold@gmail.com with subject `PPC 2-Day Report — [dates]`. Until then,
  the report is still available in the repo and in the Drive "PPC Reports" folder.

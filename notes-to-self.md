# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future automated runs go smoothly. Newest at top.

## 2026-08-07 (first run, 2-day report)

**Account / profile**
- The business is one Amazon seller account ("Uzoebo Archbold E-Commerce",
  seller id A1C2I8MOP52E35) with THREE ad profiles: US (`26765323558215`, USD,
  daily budget $40), CA (`2840235221595557`, CAD), MX (`3892485344323414`, MXN).
- **`AMZ_PROFILE_ID` env var is MISCONFIGURED.** It holds an LWA *application id*
  (`amzn1.application.…`), NOT a numeric advertising profile id. It cannot be
  used as the API scope. Until it is fixed, hardcode/self-select the profile.
- The US profile is the active advertising account (only one with a real daily
  budget: $40; CA/MX are left at the default 999999999 = uncapped/unused).
  → Default to US profile `26765323558215` unless data says otherwise.
  ACTION FOR OWNER: set `AMZ_PROFILE_ID=26765323558215` (or per-marketplace).

**API / endpoints**
- LWA token exchange: `POST https://api.amazon.com/auth/o2/token` (works fine).
- Regional Ads hosts: NA `advertising-api.amazon.com` works. EU and FE hosts
  (`-eu`, `-fe`) are BLOCKED by the org egress proxy (403 on CONNECT). Do not
  retry them — the account is NA-region anyway.
- Reporting v3: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`; async —
  poll `GET /reporting/reports/{id}` until COMPLETED, then download the
  presigned URL (GZIP_JSON). Presigned S3 download worked through the proxy.
- **Column gotcha:** the keyword text column is `keyword`, NOT `keywordText`
  (400 error otherwise). Report type ids: `spCampaigns`, `spTargeting`,
  `spSearchTerm`. Attribution window used: 7-day (`purchases7d`, `sales7d`).

**Data note for this window (Aug 3–4)**
- Near-zero delivery: 52 impressions, 0 clicks, $0 spend, $0 sales across 7
  campaigns. Campaigns are enabled but barely serving. If this persists, it's a
  bid/delivery problem worth flagging to the owner, not a reporting bug.

**Delivery channels**
- Google Drive: folder "PPC Reports" exists (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`).
  Upload works via `create_file` with `parentId` + `text_content`
  (contentMimeType `text/markdown`, disableConversion=true to keep it as .md).
- **Email step could NOT run.** The Gmail connector is installed but
  `enabledInChat: false` for this automated session, so no email tool is
  loaded. Report was saved to repo + Drive instead. ACTION FOR OWNER: enable
  the Gmail connector for this scheduled session so future runs can email.

**Reports folder**
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `ppc-2day-[YYYY-MM-DD].md`.
- Previous-report comparison: this is the FIRST 2-day report, so no baseline
  existed. Next run compares against ppc-2day-2026-08-07.

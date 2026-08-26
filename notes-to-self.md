# PPC Analyst — Notes to Self

Running log of lessons so future automated runs work better. Newest first.

## 2026-08-26 — BLOCKER: no usable Amazon Ads profile (2-day run)
- **Auth works.** Refresh-token → access-token exchange against
  `https://api.amazon.com/auth/o2/token` succeeds with the current
  `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`.
- **`AMZ_PROFILE_ID` is wrong.** Its value is
  `amzn1.application.dd42b8099dc749e2af846cb301ada5c5` — that is an
  **application/client identifier**, not an advertising profile. A real
  Sponsored Products profile ID is a **numeric integer** (e.g. `1234567890`).
  Passing it as the `Amazon-Advertising-API-Scope` header returns
  `HTTP 400 "profile ID required"`.
- **No profiles to fall back on.** `GET /v2/profiles` on the NA endpoint
  (`advertising-api.amazon.com`) returns an empty list `[]` for this account.
- **EU/FE endpoints are blocked by egress policy.**
  `advertising-api-eu.amazon.com` and `advertising-api-fe.amazon.com` return
  `403 Forbidden` at the agent proxy (org network policy), so if the real
  profiles live in EU/FE they cannot be reached from this environment.
- **What the operator must do (one of):**
  1. Set `AMZ_PROFILE_ID` to the correct **numeric** advertising profile ID
     for the seller account (find it via `GET /v2/profiles` on the region
     where the account is registered).
  2. If the account is EU/FE, get `advertising-api-eu.amazon.com` /
     `advertising-api-fe.amazon.com` added to this environment's network
     allow-list.
  3. Confirm the refresh token was granted with advertising scopes
     (`advertising::campaign_management`) for a Login-with-Amazon account
     that actually has access to the ad console profiles.
- **How future runs should behave:** re-run the profile-discovery step first;
  if `AMZ_PROFILE_ID` still starts with `amzn1.` or `/v2/profiles` is empty,
  stop, write a failure report, do NOT fabricate metrics, and notify.

## Delivery capabilities in this environment (2026-08-26)
- **Google Drive: works.** `PPC Reports` folder id =
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with the Drive MCP
  `create_file` (set `disableConversionToGoogleType: true` to keep it as
  markdown, not convert to a Google Doc).
- **Email: NOT available.** No Gmail/SMTP/email MCP tool is connected in this
  session — only Google-Drive and github MCP servers plus inter-agent
  SendMessage. The "email to uzoebo.archbold@gmail.com" step of the task
  CANNOT be completed until an email connector is added. Operator action:
  connect a Gmail/email connector, or change the task to Drive-only delivery.
  Until then, runs push a notification and rely on the Drive copy + committed
  report instead of email.

## Report bookkeeping
- Report files live in `reports/`.
  - 2-day: `ppc-2day-latest.md` + dated `ppc-2day-YYYY-MM-DD.md`.
- Date window rule (48h data lag): cover the 2 full calendar days that end
  on/before (now − 48h). For the 2026-08-26 23:06 UTC run that is
  **2026-08-22 → 2026-08-23**.
- Compare each report against the previous report OF THE SAME TYPE. First run
  of a type has no prior report to compare against — say so.

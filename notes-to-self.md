# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Read this first, every run.

## How the reports work
- Report types: 2-day, and likely others (weekly/monthly) saved in `reports/`.
- File naming: `ppc-<type>-latest.md` (overwrite each run) + dated copy `ppc-<type>-[YYYY-MM-DD].md`.
- Compare each run against the **previous report of the same type**.
- Date window: data lags ~48h. For the 2-day report, cover the 2 full calendar
  days ending 48h before the run. Worked example for run 2026-06-29 ~23:00 UTC:
  48h cutoff = 2026-06-27, so window = **2026-06-25 and 2026-06-26**.

## Delivery channels
- Google Drive: the `create_file` tool works; "PPC Reports" folder id =
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with contentMimeType `text/markdown`
  and `disableConversionToGoogleType: true` to keep it as a .md file.
- **No email/Gmail/SMTP tool exists in this environment** (searched 2026-06-29).
  The task asks to email the report; the only way to reach the owner is the
  PushNotification tool, whose email body lands in the owner's inbox. Use that
  as the email substitute AND for blocker alerts. If a real mail tool appears
  later, prefer it for the formal email.

## Amazon Ads API
- Get access token: POST https://api.amazon.com/auth/o2/token with
  grant_type=refresh_token + AMZ_REFRESH_TOKEN / AMZ_CLIENT_ID / AMZ_CLIENT_SECRET.
  This works — token issues fine.
- Regional endpoints: NA = advertising-api.amazon.com (reachable),
  EU = advertising-api-eu.amazon.com, FE = advertising-api-fe.amazon.com.
- **EU and FE are blocked by the egress proxy (403 CONNECT / policy denial).**
  Do NOT retry these — they are org-policy denials. Only NA is allowed outbound.
- SP performance: use the v3 reporting API (POST /reporting/reports, then poll
  GET /reporting/reports/{id}, then download the GZIP_JSON). Scope header is
  `Amazon-Advertising-API-API-Scope` = the **numeric profile ID**.

## KNOWN BLOCKER (first hit 2026-06-29) — must be fixed by the account owner
- `AMZ_PROFILE_ID` is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`.
  That is an **LWA application ID**, NOT an Amazon Ads profile ID. A real
  profile ID is a long **numeric** string (e.g. `1234567890123456`).
- The API confirms it: `GET /v2/profiles` with this scope returns
  `400 Invalid scope: amzn1.application...`; a report request returns
  `400 profile ID required`.
- `GET /v2/profiles` (NA, no scope) returns `[]` — i.e. there are NO profiles
  on the NA region for these credentials, so I cannot auto-discover the correct
  numeric ID. The real account may live in EU/FE (which are proxy-blocked).
- ACTION NEEDED FROM OWNER: set `AMZ_PROFILE_ID` to the correct numeric Ads
  profile ID. If the seller account is EU or FE, also get the egress policy to
  allow the matching advertising-api-eu/fe endpoint. Until then, no real data
  can be pulled and reports will be blocked (do not fabricate numbers).
- Each run: still attempt the pull (in case it's been fixed). Try
  `GET /v2/profiles` on NA first; if it returns a numeric profile, use it.

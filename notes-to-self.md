# Notes to self — PPC Analyst routine

Running log of lessons so each run is faster and cleaner. Newest lessons at top.

## Environment / credentials
- **AMZ_PROFILE_ID is WRONG in env.** It holds an *application* ID
  (`amzn1.application.…`), NOT a numeric Ads profile ID. Do not pass it as the
  `Amazon-Advertising-API-Scope`. Instead: call `GET /v2/profiles` and select
  the active US seller profile **`26765323558215`** (USD, real $40/day budget).
  The CA (`2840235221595557`) and MX (`3892485344323414`) profiles have
  placeholder budgets (~1e9) and are not used.
- Token refresh works fine: `POST https://api.amazon.com/auth/o2/token` with
  `grant_type=refresh_token` + AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN. Access token
  lasts 3600s. Re-mint it before each batch of calls.
- Region endpoint: **NA** = `https://advertising-api.amazon.com`. EU/FE not used.

## Reporting API (v3)
- Endpoint: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Reports are async: status goes PENDING → PROCESSING → COMPLETED. **Can take
  ~4–5 minutes** for this account. Poll ~every 20s; download the gzipped JSON
  from the returned `url` and gunzip.
- Working configs used:
  - Campaigns: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`, columns incl.
    `topOfSearchImpressionShare` (valid here), `purchases30d`, `sales30d`,
    `acosClicks14d`, `roasClicks14d`.
  - Targeting: `reportTypeId=spTargeting`, `groupBy=["targeting"]`.
  - Search terms: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`.
- **Metric scale gotcha:** `clickThroughRate` and `topOfSearchImpressionShare`
  are returned as **percentage-points**, i.e. a value of `100` = 100%, `0.21` =
  0.21%. Do NOT multiply by 100 again. (Confirmed: 1 click / 1 impression → CTR
  field = 100.) ACOS field is also already a percent (78.72 = 78.72%). ROAS is a
  plain ratio. `acos = cost/sales`, `roas = sales/cost` reconcile exactly with
  the cost & sales columns.

## Delivery (Drive + email)
- Google Drive: folder **'PPC Reports'** id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload with `create_file`, `parentId` = that id. Previous reports are stored
  there as Google Docs (auto-converted from markdown). Use
  `disableConversionToGoogleType:true` + `contentMimeType:text/markdown` if you
  want to keep it as a raw .md.
- **No email/Gmail tool is connected to this automated session** — cannot send
  the email. Save to repo + Drive and deliver the headline via PushNotification
  instead. State this plainly at the top of the report. (Recurring every run;
  needs a Gmail integration enabled for the automation to fix.)

## Repo
- The repo can come up as a fresh clone (only the initial commit) with no
  `reports/` folder and no prior report locally — the report history lives in
  Drive. Recreate `reports/` and this notes file when missing. Work on branch
  `claude/great-hopper-uxjel3`.

## Comparison chain (2-day reports)
- Compare against the previous **2-day** report. Recent chain (run date → window):
  22 Jun→20-21 Jun (0s), 23 Jun→19-20 Jun (0s), 24 Jun→... , 27 Jun→23-24 Jun (0s),
  10 Jul→6-7 Jul (0s), 16 Jul→12-13 Jul (0s), 20 Jul→16-17 Jul (0s),
  22 Jul→18-19 Jul (0s), 24 Jul→20-21 Jul (0s), 25 Jul→22-23 Jul (0s),
  27 Jul→23-24 Jul (184 imp / 1 click / $3.51 / $0 sales), **30 Jul→26-27 Jul**.
- Account was effectively dark (0 impressions) from ~9-10 Jun through mid-Jul.
  Delivery restarted around 23 Jul (184 imp) and **scaled up on 26-27 Jul**
  (2,790 imp, 6 clicks, first sale $14.99). Watch whether this holds.
- Two enabled campaigns only: `SP KT | ST w/ Sales` (keyword targeting) and
  `SP PT | ST w/ Sales` (product targeting). ~52 others paused/archived. Core
  product is the cat-deterrent / pet-odour eliminator (ASIN B0FXW3GW5F).

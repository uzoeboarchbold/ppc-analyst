# Notes to Self — PPC Analyst

Lessons learned by automated runs. Read this first every run.

## Credentials / API access
- Auth works: POST https://api.amazon.com/auth/o2/token with refresh_token grant
  using AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN. Access token ~727 chars.
- **IMPORTANT — AMZ_PROFILE_ID env var is misconfigured.** It contains an
  *application* id (`amzn1.application....`), NOT a numeric advertising profile id.
  Do NOT use it directly as the API scope.
- Correct approach: call GET /v2/profiles and pick the profile. The account
  ("Uzoebo Archbold E-Commerce", seller A1C2I8MOP52E35) has 3 profiles:
    - US  26765323558215  (USD, marketplace ATVPDKIKX0DER, dailyBudget $40) <- USE THIS
    - CA  2840235221595557 (CAD, no real budget)
    - MX  3892485344323414 (MXN, no real budget)
  Use the **US** profile `26765323558215` as Amazon-Advertising-API-Scope.
- Region = North America: base URL https://advertising-api.amazon.com
  (EU/FE hosts are blocked by the outbound proxy anyway; profile lives in NA).

## Reporting (v3, async)
- Flow: POST /reporting/reports (create) -> GET /reporting/reports/{id} (poll
  until status COMPLETED) -> download the signed `url` (GZIP_JSON, gunzip -> JSON array).
- Content-Type / Accept: application/vnd.createasyncreportrequest.v3+json
- Report configs used: reportTypeId spCampaigns (groupBy campaign),
  spTargeting (groupBy targeting), spSearchTerm (groupBy searchTerm),
  timeUnit SUMMARY, format GZIP_JSON.
- Reports usually COMPLETE within ~30-60s.
- topOfSearchImpressionShare comes back null when there were no impressions.

## Account facts
- Only 2 campaigns are ENABLED: "SP KT | ST w/ Sales" (id 51177386692133, $8/day)
  and "SP PT | ST w/ Sales" (id 258847863221155, $8/day). Everything else
  (dozens of Cat Tunnel Bed / Cat Deterrent / Odor campaigns) is PAUSED or ARCHIVED.
- Campaign management list: POST /sp/campaigns/list (Content-Type vnd.spCampaign.v3+json).

## Report history / comparison
- Previous report of each type lives in reports/ (e.g. reports/ppc-2day-latest.md).
- 2026-07-09 run (window Jul 5-6): FIRST 2-day report, so no prior report to
  compare against -> treated as baseline.

## Delivery channels
- Google Drive upload works: folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Use mcp__Google-Drive__create_file with contentMimeType text/markdown and
  disableConversionToGoogleType=true (else it converts to a Google Doc).
- **EMAIL NOT AVAILABLE:** there is no Gmail/email/SMTP MCP tool in this
  environment (only agent SendMessage + Drive). The "email it to
  uzoebo.archbold@gmail.com" step cannot be done from here. Report is delivered
  via the repo commit + Google Drive instead. If email is required, an email
  connector (e.g. Gmail MCP) needs to be added to the session.

## Observations to watch
- 2026-07-05/06: both ENABLED campaigns delivered ZERO impressions/clicks/spend/sales.
  Ads effectively dark. If this persists, flag it — likely bids too low, targets
  paused inside the campaigns, or listing not buyable/in stock.

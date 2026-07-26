# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons at top.

## Environment / API access
- **`AMZ_PROFILE_ID` env var is WRONG type.** It holds an *application id*
  (`amzn1.application.…`), NOT a numeric Advertising profile id. Do not send it
  as `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles` (no scope
  header) and pick the profile. This account has 3 profiles:
    - US (seller): **26765323558215**  ← USD, active $40 daily budget = the live one. USE THIS.
    - CA: 2840235221595557
    - MX: 3892485344323414
  Hard-code/derive the US profile `26765323558215` until the env var is fixed.
- **Region = NA only.** `https://advertising-api.amazon.com`. The EU/FE hosts are
  blocked by the agent proxy (403 tunnel) — don't waste retries on them.
- LWA token refresh works: POST `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id/secret. Token lasts 3600s.
- Reporting API v3: POST `/reporting/reports` with Accept/Content-Type
  `application/vnd.createasyncreportrequest.v3+json`. Poll
  `/reporting/reports/{id}`; download from the S3 `url` (presigned, NO auth
  headers) and gunzip. Reports usually COMPLETE in ~30–60s.
  - Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`.
  - Keyword/target report: reportTypeId `spTargeting`, groupBy `["targeting"]`.
  - Column names: cost, costPerClick, clickThroughRate, purchases14d, sales14d,
    acosClicks14d, roasClicks14d, topOfSearchImpressionShare, impressions, clicks.
  - ACOS/ROAS: report has `acosClicks14d`/`roasClicks14d` but they're null when
    there are no clicks. Safer to compute ACOS = cost/sales, ROAS = sales/cost.
  - Poll with `time.sleep()` inside Python (the shell `sleep` command is blocked
    in this env).

## Account status observations
- **2026-07-26 run (covering 22–23 Jul): account fully DORMANT.** Zero
  impressions/clicks/spend/sales for the window AND for the trailing 30 days.
  Only 2 campaigns ENABLED (`SP KT | ST w/ Sales`, `SP PT | ST w/ Sales`, both
  $8/day, live since 2026-06-09) but they serve nothing — targeting report empty,
  so they likely have no eligible/active targets or bids are non-competitive.
  Everything else is PAUSED/ARCHIVED. This is not an API error; it's the real
  state. If future runs still show zeros, the story is "ads switched off," and
  the useful action is to alert the owner, not to keep re-pulling.

## Delivery channels
- **Email step FAILED 2026-07-26.** The Gmail connector exists but is
  `enabledInChat: false` (toggled off for the automated session), so no email
  tool is loaded and the report cannot be emailed hands-off. Google Drive upload
  DOES work. Fix: the account owner must enable the Gmail connector for this
  scheduled session's chat/connector settings. Until then, delivery = repo commit
  + Drive upload + push notification only. Don't retry email; it can't be loaded
  mid-session once it's disabled.

## Report bookkeeping
- Report types & their prior-report files live in `reports/`. This 2-day run is
  the FIRST of its type (no previous ppc-2day report existed) — no comparison
  baseline. Next 2-day run should compare against `ppc-2day-2026-07-26.md`.
- Google Drive: upload to folder named "PPC Reports". Email goes to
  uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

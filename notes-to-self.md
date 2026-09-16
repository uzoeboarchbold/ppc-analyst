# Notes to Self — PPC Analyst routine

Lessons learned so future runs are faster and more reliable. Newest at top.

## Credentials & account (CRITICAL)
- Auth works: POST https://api.amazon.com/auth/o2/token with grant_type=refresh_token
  + AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN → returns a 1 h access_token.
- **`AMZ_PROFILE_ID` env var is WRONG.** It is set to `amzn1.application.dd42...`,
  which is an *application* id, NOT an advertising profile id. Do not use it as the
  API Scope — it will fail.
- **Correct profile = `26765323558215`** (US, USD, seller "Uzoebo Archbold E-Commerce").
  Get profiles from `GET /v2/profiles` on the NA host. The account has 3 profiles:
  US 26765323558215 (the only one with campaigns), CA 2840235221595557 (empty),
  MX 3892485344323414 (empty). Always scope to the US one.
- **Region = NA only.** Use host `https://advertising-api.amazon.com`. The EU and FE
  hosts are blocked by the outbound proxy (CONNECT tunnel 403) and the account has no
  EU/FE profiles anyway.

## API mechanics
- **v2 reporting/campaign endpoints are dead** (`/v2/sp/campaigns` → 404 Method Not Found).
  Use the **v3 async reporting API**: POST `/reporting/reports`
  (Content-Type `application/vnd.createasyncreportrequest.v3+json`), then poll
  `GET /reporting/reports/{id}` until status COMPLETED, then download the `url`
  (GZIP JSON). Reports usually complete within ~20–60 s.
- To list campaigns quickly: POST `/sp/campaigns/list` with
  Content-Type/Accept `application/vnd.spCampaign.v3+json`, body `{"maxResults":100}`.
- **Column gotcha:** `acosClicks7d` and `roasClicks7d` are INVALID for the `spCampaigns`
  report and cause a 400. Do NOT request ACOS/ROAS columns — instead pull `cost`,
  `sales7d`, `purchases7d` and compute ACOS = cost/sales, ROAS = sales/cost yourself.
- Working campaign columns: campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, topOfSearchImpressionShare, clickThroughRate, costPerClick.
- `topOfSearchImpressionShare` only comes back with groupBy=["campaign"].
- Search-term / targeting reports return **empty** when there was no traffic in the
  window — that's expected, not a bug.

## Business state (as of 16 Sep 2026)
- **US profile has `validPaymentMethod: false`.** Ads stopped delivering entirely after
  **2 Sep 2026** — zero impressions every day since, even though all 15 campaigns are
  still ENABLED. Almost certainly a billing/payment failure. If a report window shows
  all zeros, check whether this is still the case before assuming a data problem.
- Budgets are tiny (~$1.50/day per campaign). Even when live (Aug), 30 days gave only
  1,743 impr / 17 clicks / $5.93 spend / $0 sales. Volume is very low.

## Reports
- Report type/date logic: 2-day report covers the 2 full days ending 48 h before the run.
  Run 16 Sep → covered 12–13 Sep.
- Save both `reports/ppc-2day-latest.md` (overwrite) and `reports/ppc-2day-YYYY-MM-DD.md`
  (dated by run date). Previous 2-day report is the one to compare against next time.
- First 2-day report was 2026-09-16 (baseline, all zeros due to the blackout above).

## Delivery (Drive + email)
- Google Drive: upload the report into the folder named "PPC Reports"
  (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). WORKS. Uploaded as a .md file
  with `disableConversionToGoogleType: true` to keep it as markdown.
- **Email is BLOCKED in the automated session.** The Gmail connector is installed
  and connected at org level BUT `enabledInChat: false`, so its tools are not loaded
  and no email can be sent from the routine. There is no SMTP fallback in the
  environment. To fix: the user must enable the Gmail connector for this
  chat/automation in connector settings. Until then, report reaches the user via
  the repo, Google Drive, and the run's push notification only.
- 2026-09-16 run: report saved to repo + uploaded to Drive OK; email NOT sent
  (reason above).

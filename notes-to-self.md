# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.
Newest notes at the top.

## 2026-11-23 — First run (2-day report)

**Account / environment facts learned:**
- `AMZ_PROFILE_ID` env var is MISCONFIGURED. It holds an application id
  (`amzn1.application...`), NOT a numeric Amazon Ads profile id. Using it
  as the `Amazon-Advertising-API-Scope` header returns HTTP 400
  "Invalid scope". **Self-heal:** list `/v2/profiles` (ClientId header only,
  no Scope header) and pick the right profile.
- The account has 3 profiles, all on the **NA** endpoint
  (`advertising-api.amazon.com`):
  - **US** `26765323558215` (USD) — THE LIVE ONE. 54 SP campaigns
    (15 enabled). Use this profile.
  - CA `2840235221595557` (CAD) — 0 campaigns.
  - MX `3892485344323414` (MXN) — 0 campaigns.
- Seller account: "Uzoebo Archbold E-Commerce". Main product in ads:
  ASIN **B0FXW3GW5F** (Cat Deterrent Spray / Pet Odor Eliminator).
- **Network policy blocks the EU and FE Ads endpoints** (proxy returns
  403 "no rule allows this host"). Only `advertising-api.amazon.com` (NA)
  is reachable. Fine for this US account; don't waste time retrying EU/FE.

**API mechanics that worked:**
- Token refresh: POST `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client id/secret. Works. Token lasts 1h.
- v2 campaign endpoints (`GET /v2/sp/campaigns`) are DEPRECATED →
  "Method Not Found". Use **v3**: `POST /sp/campaigns/list` with
  Content-Type/Accept `application/vnd.spCampaign.v3+json`.
- Reporting = v3 async. `POST /reporting/reports` with Content-Type
  `application/vnd.createasyncreportrequest.v3+json`. Poll
  `GET /reporting/reports/{id}` until status COMPLETED, then download the
  gzipped-JSON `url` (plain S3 GET, decompress with gzip).
- Report type ids used: `spCampaigns` (groupBy ["campaign"]),
  `spTargeting` (groupBy ["targeting"]), `spSearchTerm`
  (groupBy ["searchTerm"]). timeUnit SUMMARY, format GZIP_JSON.
- Column gotcha: `targetId` is NOT a valid column for spTargeting (400).
  Valid dimension cols include campaignId, campaignName, adGroupName,
  keywordId, keyword, keywordType, matchType, targeting. ToS impression
  share column = `topOfSearchImpressionShare` (campaign level).
- Attribution: used `purchases7d` / `sales7d` (7-day). 14d also available.

**BIG FINDING this run:**
- The account is delivering ZERO ads. The window (Nov 19–20) returned `[]`
  for all three reports. A diagnostic DAILY report over Nov 8–18 showed
  all campaigns present but with 0 impressions / 0 cost / 0 sales every
  day; no rows at all for Nov 19–21. So it is NOT a data-lag artefact.
- Root cause is almost certainly billing: the US profile shows
  `accountInfo.validPaymentMethod = false`. 15 campaigns are ENABLED with
  live daily budgets (~$24/day total) but nothing serves without a valid
  payment method. **Flag this loudly every run until it clears.**

**For the comparison section:** this was the first 2-day report, so there
was no prior report to compare against. Next run: compare to
`reports/ppc-2day-latest.md` (or the dated file for this type).

**Delivery:** No email-sending tool is available in this environment
(no Gmail/SMTP MCP tool). Report is saved to the repo `reports/` folder
and uploaded to the Google Drive folder "PPC Reports". Email to
uzoebo.archbold@gmail.com could NOT be sent automatically — noted at the
top of the report. If email matters, the user needs to connect a mail
tool/connector.

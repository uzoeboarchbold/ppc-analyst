# Notes to self — PPC Analyst runs

Lessons learned, newest first. Read this before every run and apply it.

## 2026-11-18 (first run, 2-day report)

### Account / profile
- **`AMZ_PROFILE_ID` env var is INVALID.** It is an `amzn1.*` resource string (50 chars, 19
  digits), NOT the numeric advertising profile ID the API needs as the
  `Amazon-Advertising-API-Scope` header. Do not use it as-is.
- **Correct profiles** (from `GET /v2/profiles` on the NA host): the account is seller
  "Uzoebo Archbold E-Commerce" with three marketplaces:
  - **US / USD → profileId `26765323558215`  ← THE ACTIVE PPC ACCOUNT (15 SP campaigns)**
  - CA / CAD → profileId `2840235221595557` (no SP campaigns)
  - MX / MXN → profileId `3892485344323414` (no SP campaigns)
- **Default to the US profile `26765323558215`** unless told otherwise. The pull script accepts
  `AMZ_PROFILE_OVERRIDE` to override the bad env var. If the user fixes `AMZ_PROFILE_ID` to the
  numeric US ID, the override is no longer needed.

### API / environment mechanics
- `requests` and `pip install` do NOT work here. Use **Python stdlib `urllib`** with the proxy:
  `ProxyHandler({"https": os.environ["HTTPS_PROXY"]})` + `ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")`.
- Token refresh works: `POST https://api.amazon.com/auth/o2/token` with the AMZ_* creds.
- **Only the NA host `advertising-api.amazon.com` is allowed by the network policy.** The EU
  (`advertising-api-eu…`) and FE hosts are blocked by the proxy (403 CONNECT). Our account is NA
  (US/CA/MX) so NA is correct — don't treat the EU/FE block as an error.
- Reporting v3: `POST /reporting/reports` with `Content-Type: application/vnd.createasyncreportrequest.v3+json`;
  campaigns report = `reportTypeId: spCampaigns`, groupBy `["campaign"]`; search terms =
  `spTargeting`, groupBy `["targeting"]`. Poll `/reporting/reports/{id}` until `COMPLETED`, then
  download the gzip-JSON `url`. Working script: `scratchpad/amz_pull.py`
  (args: START END OUTFILE). Full pull (2 reports) takes ~1–2 min per profile — run in background,
  the foreground Bash limit is 120s.
- Columns that work for spCampaigns: impressions, topOfSearchImpressionShare, clicks, cost,
  purchases30d, sales30d, campaignName, campaignId.

### Data finding
- 14–15 Nov 2026: all 15 US campaigns = ZERO impressions/clicks/spend/sales. Confirmed zero over
  the wider 1–15 Nov window too → campaigns are not delivering (bids too low / budget or status /
  out of Buy Box / in review), not a data glitch. Report this as a delivery problem, don't invent.

### Delivery channels
- **No email tool exists in this environment** (only Google Drive + Claude messaging). Cannot send
  the email step. Save to repo + upload to Google Drive "PPC Reports" folder, and clearly note the
  email could not be sent. A PushNotification goes to the user's phone/inbox instead.
- Google Drive: use `mcp__Google-Drive__create_file` with `textContent` + `contentMimeType:
  text/markdown` + `disableConversionToGoogleType: true`, `parentId` = the "PPC Reports" folder id.

### Date window logic (2-day report)
- Run day D. Data lags 48h. Cover the 2 full days = **D-4 and D-3**. (Run Wed 18 Nov → cover Sat 14
  & Sun 15 Nov.) State exact dates at the top.

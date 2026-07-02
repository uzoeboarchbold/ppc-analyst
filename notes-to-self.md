# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest lessons at top.

## Environment / API setup (learned 2026-07-02, first run)
- **Region:** Account lives on the **NA** endpoint `https://advertising-api.amazon.com`.
  EU/FE endpoints are blocked by the outbound proxy (403 CONNECT) and aren't needed.
- **Token refresh:** `POST https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id + client_secret. Access token lasts 3600s.
- **IMPORTANT — Profile ID:** The env var `AMZ_PROFILE_ID` is set to an
  *application id* (`amzn1.application...`), NOT a numeric advertising profile id.
  It cannot be used as `Amazon-Advertising-API-Scope`. Get real profiles from
  `GET /v2/profiles`. Three exist:
    - **US (USD) = 26765323558215**  ← primary marketplace, USE THIS
    - CA (CAD) = 2840235221595557
    - MX (MXN) = 3892485344323414
  Business name: "Uzoebo Archbold E-Commerce". Reporting uses the US profile.
- **Reporting API v3** (`POST /reporting/reports`, async):
    - Content-Type header: `application/vnd.createasyncreportrequest.v3+json`
    - reportTypeIds used: `spCampaigns` (groupBy `campaign`), `spTargeting`
      (groupBy `targeting`), `spSearchTerm` (groupBy `searchTerm`).
    - **ACOS/ROAS columns:** only `acosClicks14d` / `roasClicks14d` are valid.
      There is NO `acosClicks30d`/`roasClicks30d` — 400 error if you use them.
      Sales/purchases: `sales30d` / `purchases30d` are fine.
    - `topOfSearchImpressionShare` is valid on campaign + targeting reports.
    - Poll GET /reporting/reports/{id} until status COMPLETED, then download the
      gzip JSON from the `url` field.

## Data / account behaviour
- This is a **very low-volume account**: ~$77 total spend over the 30 days to
  2026-06-30 with only 1 attributed sale ($12.99). A quiet 2-day window with
  little or zero activity is normal — do NOT treat zeros as an error.
- **2026-07-02 run:** the ENTIRE trailing week (Jun 24–30) had ZERO spend/clicks/
  impressions/sales. Ads have effectively gone dark since ~late June. All the
  month's activity was earlier (Jun 2–~23). When you see all-zero, sanity-check
  with a wider window + a DAILY breakdown before concluding (I did — confirmed real).
- If the 2-day report returns few/zero rows, that's the API only returning
  campaigns with records; pull a 30-day report to see the full campaign list.

## Report housekeeping
- Reports live in `reports/`. Overwrite `ppc-2day-latest.md`, also save dated
  `ppc-2day-YYYY-MM-DD.md`. Compare each run to the previous 2-day report.
- Date window rule: 2 full days ending 48h before run (data lags ~48h).
- Deliverables per run: commit reports to git (branch claude/great-hopper-rhmti7),
  upload to Google Drive folder "PPC Reports", email to uzoebo.archbold@gmail.com.

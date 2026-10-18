# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / environment facts
- **Region:** North America. Use host `https://advertising-api.amazon.com`.
  The EU/FE hosts are blocked by the outbound proxy (403 CONNECT) and are
  not needed anyway.
- **OAuth:** refresh-token grant against `https://api.amazon.com/auth/o2/token`
  works with `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`.
  Access token lasts 3600s.
- **`AMZ_PROFILE_ID` is NOT a usable profile id.** It is set to an
  *application* id (`amzn1.application.…`), which the Ads API rejects as a
  scope. Real profile ids are numeric. Resolve the real profile via
  `GET /v2/profiles` each run.
- **Profiles on this account** (all seller, name "Uzoebo Archbold E-Commerce"):
  - `26765323558215` — **US** (USD). THE ONLY PROFILE WITH CAMPAIGNS. Use this.
    Note: `validPaymentMethod: false` on this profile.
  - `2840235221595557` — CA (CAD). No campaigns.
  - `3892485344323414` — MX (MXN). No campaigns.

## Reporting API (v3) gotchas
- Endpoint: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Date range per report must be **<= 31 days**.
- Allowed attribution columns are `purchases7d`, `sales7d`, `acosClicks14d`,
  `roasClicks14d` — there is **no `acosClicks7d`/`roasClicks7d`**. Compute
  ACOS = cost/sales7d and ROAS = sales7d/cost yourself from the 7d figures.
- `topOfSearchImpressionShare` is a valid column at campaign/targeting level.
- Report returns rows **only for entities with activity**; a totally empty
  `[]` means zero impressions/spend in the window, not an error.
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
- Poll: PENDING -> PROCESSING -> COMPLETED, usually ~1-2 min. Download the
  `url` (GZIP_JSON) and gunzip.

## 2026-10-18 run (2-day report, window 2026-10-14..15)
- **No ad delivery.** Campaign/search-term/targeting reports for the window
  were all empty. A 30-day check (Sep 16–Oct 16) returned 330 campaign-day
  rows with **zero impressions and zero cost on every one**. So nothing has
  served for at least a month.
- 54 campaigns exist (15 ENABLED, 32 PAUSED, 7 ARCHIVED), combined enabled
  daily budget ~$22.50, products B0FXW3GW5F (Cat Deterrent Spray / Pet Odor
  Eliminator) and Cat Tunnel Beds.
- **Most likely cause:** US profile `validPaymentMethod: false` — Amazon will
  not serve Sponsored Products without a valid payment method. Could also be
  out-of-stock / suppressed listings or not-buyable offers. Flag to owner;
  can't be fixed via the API.
- No previous 2-day report existed, so no comparison was possible this run.

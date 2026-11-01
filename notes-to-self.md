# Notes to self — PPC Analyst routine

Lessons learned, newest first. Read this before every run and apply it.

## 2026-11-01 (first run, 2-day report)

**Credentials / config**
- Token refresh works: `POST https://api.amazon.com/auth/o2/token` with
  `grant_type=refresh_token` + refresh_token/client_id/client_secret → returns `access_token`.
- **`AMZ_PROFILE_ID` is MALFORMED** — it's a 50-char alphanumeric string, not a numeric
  Amazon profile ID, and matches none of the account's profiles. Do NOT trust it as-is.
- The account has 3 profiles (seller "Uzoebo Archbold E-Commerce"):
  - **US `26765323558215`** ← the ONLY one with Sponsored Products campaigns. USE THIS.
  - CA `2840235221595557` — 0 campaigns. MX `3892485344323414` — 0 campaigns.
- Until the env var is fixed, hard-select the US profile `26765323558215`.
- Flag the malformed env var in the report so the human fixes it.

**Environment / network**
- Only the **NA** host is reachable: `https://advertising-api.amazon.com`.
  EU (`-eu`) and FE (`-fe`) hosts are blocked by the proxy (403 Tunnel). US profile is on NA, so fine.
- Measure env-var VALUE lengths with Python/`printenv`, NOT bash `${#v}` inside a
  `for v in NAME...` loop — that measures the variable NAME length and misled me at first.

**Amazon Ads Reporting API (v3)**
- Flow: `POST /reporting/reports` (Content-Type `application/vnd.createasyncreportrequest.v3+json`)
  → poll `GET /reporting/reports/{id}` until `status==COMPLETED` → download `url` → gunzip → JSON array.
- Report typically ready in ~40–90s. Poll every ~15–20s.
- **Invalid columns:** `acosClicks7d`, `roasClicks7d` do NOT exist. Only 14d variants
  (`acosClicks14d`, `roasClicks14d`). Simplest: omit them and COMPUTE
  ACOS = cost / sales7d * 100, ROAS = sales7d / cost.
- Valid spCampaigns columns I used: campaignName, campaignId, campaignStatus, impressions,
  clicks, cost, costPerClick, clickThroughRate, purchases7d, sales7d, topOfSearchImpressionShare.
- Search-term report type id: `spSearchTerm`, groupBy `["searchTerm"]`.
- **Quirk:** for a window with all-zero metrics, a short window returns `[]` while a longer
  window (e.g. full month) returns zero-filled rows. Empty `[]` ≠ error.

**Business finding (important — recurring until fixed)**
- As of this run, the US account has **ZERO ad delivery**: 0 impressions / clicks / spend / sales
  for the 2-day window AND for all of October. 15 campaigns ENABLED (since 2026-05-18,
  budgets $1.50–$2.50/day), 32 paused, 7 archived.
- Likely cause: bids too low to win auctions, and/or the product (ASIN B0FXW3GW5F + Cat Tunnel Bed)
  not holding the Buy Box / out of stock, and/or billing issue. Check Buy Box FIRST next run.
- If still zero next run, keep surfacing it — this is the headline, not a background note.

**Delivery channels**
- Report saved to `reports/ppc-2day-latest.md` + dated copy, committed to branch
  `claude/great-hopper-23w9sg`.
- Google Drive: upload to folder "PPC Reports" (see run log for status).
- Email to uzoebo.archbold@gmail.com — CHECK whether an email/Gmail tool is actually available
  in this session; if not, note it and rely on the push notification + Drive + repo.

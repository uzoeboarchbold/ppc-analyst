# PPC Analyst — Notes to Self

Running log of lessons so each run is smoother than the last. Newest first.

## 2026-09-03 (first run — 2-day report)

**Account / profile**
- The env var `AMZ_PROFILE_ID` is set to an *application* id
  (`amzn1.application....`), which is NOT a valid Amazon Ads profile id.
  Do not use it directly. Numeric profile ids come from `GET /v2/profiles`.
- Region is **NA** (`https://advertising-api.amazon.com`). EU/FE endpoints
  are blocked by the outbound proxy (403), so don't bother trying them.
- Three profiles exist under seller "Uzoebo Archbold E-Commerce": CA
  (2840235221595557), MX (3892485344323414), US (26765323558215).
  **Only the US profile has Sponsored Products activity** (50+ campaigns).
  CA and MX have 0 SP campaigns. **Always use US profile 26765323558215.**

**Auth**
- Token exchange at `https://api.amazon.com/auth/o2/token` with refresh
  token works fine. Access token lasts ~1h.

**Reporting API (v3, async)**
- Endpoint: `POST /reporting/reports`, then poll `GET /reporting/reports/{id}`,
  then download the gzipped JSON from the returned `url`.
- Content-Type header must be `application/vnd.createasyncreportrequest.v3+json`.
- Column gotchas (differ by reportTypeId):
  - `spCampaigns`: `acosClicks7d` / `roasClicks7d` are INVALID. Only
    `roasClicks14d` exists. **Compute ACOS/ROAS myself** from cost & sales7d.
  - `spTargeting`: `targetingType` is INVALID (use `keywordType` + `matchType`).
  - `spSearchTerm`: `acosClicks7d` / `roasClicks7d` ARE valid here.
  - `topOfSearchImpressionShare`, `costPerClick`, `clickThroughRate` are all
    valid on `spCampaigns`.
  - Safest approach: pull raw impressions/clicks/cost/purchases7d/sales7d and
    compute CTR, CPC, ACOS, ROAS in code for consistency across report types.
- Reports take ~1–3 min to move PENDING → PROCESSING → COMPLETED.

**Email delivery — BLOCKED**
- The Gmail connector is **connected but not enabled in this chat**
  (`enabledInChat: false`), so no Gmail send/draft tool is loaded and the
  report **cannot be emailed automatically**. Google Drive IS enabled.
  Fix for future: enable the Gmail connector for this session's chat, or wire
  up an SMTP/API email path. Until then, deliver via Drive + repo only and
  flag the missed email at the top of the report.

**Date window logic (data lags 48h)**
- End window 48h before run; cover the 2 full days before that point.
  Run 2026-09-03 23:04 UTC → 48h ago = 2026-09-01 → window = 2026-08-30
  and 2026-08-31.

**Data note**
- Account is very low-volume right now. This 2-day window: $0.25 spend,
  331 impressions, 1 click, 0 orders. Most campaigns had 0 impressions.
  Don't mistake near-zero data for an API failure — verify with a raw pull
  before assuming something broke.

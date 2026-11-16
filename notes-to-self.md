# Notes to Self — PPC Analyst runs

Lessons learned across runs. Read this first every run and apply it.

## Account / environment facts
- **Correct US profile ID: `26765323558215`** (USD, seller, marketplace ATVPDKIKX0DER). This is where ALL 54 campaigns live. Use it.
- The `AMZ_PROFILE_ID` env var is **misconfigured** — it holds an application-ID value (`amzn1.application…`), NOT a profile ID. Do not pass it to the Ads API as the scope; it will fail. Instead resolve the profile from `GET /v2/profiles` and pick the US (USD) one, or hardcode `26765323558215`. Flagged to owner to fix the env var.
- CA profile `2840235221595557` and MX profile `3892485344323414` exist but have **0 campaigns** — ignore them.
- Main advertised product: ASIN **B0FXW3GW5F** (cat deterrent / pet-odour spray). Portfolio label seen in names: `6K-PZMX-MTDZ`.

## API mechanics that work
- LWA token: `POST https://api.amazon.com/auth/o2/token` with grant_type=refresh_token + client_id/secret. Returns 1h token.
- Region host: **NA = `https://advertising-api.amazon.com`** (EU/FE hosts are blocked by the proxy and not needed).
- Reports API v3: `POST /reporting/reports` (async) → poll `GET /reporting/reports/{id}` until status COMPLETED → download the `url` (gzip JSON, via proxy, no auth header).
- Report config that works: `adProduct:SPONSORED_PRODUCTS`, `timeUnit:SUMMARY`, `format:GZIP_JSON`, content-type `application/vnd.createasyncreportrequest.v3+json`.
  - Campaign table: reportTypeId `spCampaigns`, groupBy `["campaign"]`. `topOfSearchImpressionShare` IS available here.
  - Keyword/target: reportTypeId `spTargeting`, groupBy `["targeting"]`.
  - Search terms: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
- Reports usually complete within ~30–60s. Poll every 15s.
- Python: `requests` is NOT installed — use `urllib`. Pass `cafile="/root/.ccr/ca-bundle.crt"` to the ssl context; proxy is honoured via env automatically. Run with `python3 -I`.

## Date window logic (2-day report)
- Data lags ~48h. Exclude the 48h-ago day, cover the 2 full calendar days BEFORE it.
- e.g. run Mon 16 Nov → 48h ago = Sat 14 Nov → cover **12–13 Nov**. (Matches the spec example: run Sun → cover Wed+Thu.)

## Attribution
- Using **14-day** click attribution (purchases14d/sales14d/acosClicks14d/roasClicks14d) — Amazon SP default. Keep this consistent across runs for valid comparisons.

## Run history / state of the account
- **2026-11-16 (first 2-day run):** ZERO delivery for 12–13 Nov AND across the whole 30 days (15 Oct–13 Nov). 15 campaigns ENABLED with budgets but served 0 impressions. Root cause suspected: US ad account `validPaymentMethod: false` → Amazon suspended delivery. Reported to owner: fix billing, check ASIN B0FXW3GW5F listing/stock/Buy Box, check account health. No previous report to compare against — this run is the baseline.
- **Watch for:** once `validPaymentMethod` flips to true and impressions appear, resume normal optimisation (negatives, exact-match harvesting, bid tuning).

## Report output checklist
- Overwrite `reports/ppc-2day-latest.md` + save dated `reports/ppc-2day-[run-date].md`, commit to branch `claude/great-hopper-ak5f1a`.
- Upload same file to Google Drive folder "PPC Reports" (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Use `create_file` with `base64Content: sha256:<hash>:<abs path>` and `disableConversionToGoogleType:true`. WORKS.
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
  - **BLOCKED (2026-11-16):** The Gmail connector is connected at org level but `enabledInChat:false` for this session — no Gmail send tool is loaded, and ToolSearch finds none. **Email could NOT be sent automatically.** Owner must enable the Gmail connector's tools for Claude Code sessions (claude.ai → Connectors → Gmail → allow in chat/Code) for future runs to email. Until then, the report reaches the owner via push notification + Google Drive + repo commit.
- Notify owner (push) when there's something that needs them — e.g. the delivery blackout, or the email-send being blocked.

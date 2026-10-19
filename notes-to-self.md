# Notes to Self — PPC Analyst

Running log of lessons so future automated runs work better. Newest first.

## 2026-10-19 (first run — 2-day report)

**Account / profile**
- `AMZ_PROFILE_ID` env var is MISCONFIGURED. It holds an *application* id
  (`amzn1.application.…`), which is NOT a valid Amazon Ads profile id. The
  reporting API needs a numeric profile id in the `Amazon-Advertising-API-Scope`
  header, so the env value cannot be used directly.
- Resolved by calling `GET /v2/profiles` (NA endpoint) and picking the right one.
  The account `A1C2I8MOP52E35` ("Uzoebo Archbold E-Commerce") has 3 profiles:
  - **US  26765323558215  (USD, amazon.com)** ← the active one. 54 SP campaigns.
    Daily budget set to $40; `validPaymentMethod: false`.
  - CA  2840235221595557 (CAD) — 0 campaigns, dormant.
  - MX  3892485344323414 (MXN) — 0 campaigns, dormant.
  - **Future runs: use profile `26765323558215`.** If profiles change, re-run the
    `/v2/profiles` lookup and pick the US seller profile with campaigns.

**Region / network**
- Use the NA endpoint `https://advertising-api.amazon.com`. The EU and FE
  endpoints are BLOCKED by the egress proxy (403 tunnel) — don't rely on them.
- Token refresh works at `https://api.amazon.com/auth/o2/token`.
- All HTTPS must trust the proxy CA at `/root/.ccr/ca-bundle.crt`.

**Reporting API (v3)**
- POST `/reporting/reports` with `Content-Type:
  application/vnd.createasyncreportrequest.v3+json`; reportTypeIds used:
  `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm). Poll `GET /reporting/reports/{id}` until
  COMPLETED, then download the presigned `url` (GZIP_JSON, no auth header on S3).
- `topOfSearchImpressionShare` is available on `spCampaigns`, not on targeting.
- Reports generate in ~1–3 min; poll loop with ~20s sleep is fine.

**DATA FINDING — ads not serving**
- The US account has NO Sponsored Products activity. Diagnostics:
  - Oct 15–16 (this window): 0 rows, 0 impressions.
  - Oct 10–16: 0 rows. Sep 17–Oct 16: campaigns present but 0 impressions.
  - Sep 1–30: only 287 impressions, 1 click, $0.08 spend, 0 sales (all early Sep).
- Campaigns are ENABLED but `validPaymentMethod: false` on the profile. Most
  likely Amazon has stopped serving the ads because there is no valid payment
  method on the advertising account. **This is the headline issue to flag every
  run until it changes.** When impressions reappear, the payment method was
  probably fixed.
- Do NOT invent numbers. A zero report is a valid report here.

**Report plumbing**
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-YYYY-MM-DD.md`
  (run date). Commit to branch `claude/great-hopper-n51ohh`.
- Previous-report comparison: none existed on first run. Next run, compare
  against `ppc-2day-latest.md` before overwriting (read it first).
- Google Drive folder "PPC Reports" + email to uzoebo.archbold@gmail.com.

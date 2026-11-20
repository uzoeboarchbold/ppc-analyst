# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more accurate. Newest at top.

## Account / API facts (confirmed 2026-11-20)
- **Active account = US seller profile `26765323558215`** (marketplace ATVPDKIKX0DER, USD).
  The CA (`2840235221595557`) and MX (`3892485344323414`) profiles exist but have **0 campaigns** — ignore them.
- **`AMZ_PROFILE_ID` env var is NOT usable** — it holds an application id
  (`amzn1.application...`), not a numeric Advertising profile id. Always resolve the real
  profile by calling `GET https://advertising-api.amazon.com/v2/profiles` and picking the US
  seller profile (or whichever has campaigns).
- Region/endpoint: **North America** → `https://advertising-api.amazon.com`. LWA token refresh
  at `https://api.amazon.com/auth/o2/token` works with the env credentials.
- Product under advertisement: ASIN **B0FXW3GW5F** (cat odor eliminator / deterrent spray),
  internal SKU tag `6K-PZMX-MTDZ`.

## Reporting API (v3 `/reporting/reports`)
- `acosClicks7d` and `roasClicks7d` are **invalid columns** — the API rejects them.
  Pull `cost`, `sales7d`, `purchases7d` and **compute ACOS = cost/sales, ROAS = sales/cost**
  yourself. (`roasClicks14d` exists if 14d attribution is ever wanted.)
- Working campaign report: `reportTypeId: spCampaigns`, `groupBy: ["campaign"]`,
  columns incl. `impressions, clicks, cost, purchases7d, sales7d, clickThroughRate,
  costPerClick, topOfSearchImpressionShare, campaignStatus`.
- Search-term report: `reportTypeId: spSearchTerm`, `groupBy: ["searchTerm"]`.
- Attribution convention chosen for these reports: **7-day** (`purchases7d`, `sales7d`).
  Keep it consistent run-to-run so comparisons are apples-to-apples.
- Submitting an identical report request returns HTTP 400 with
  `detail: "The Request is a duplicate of : <reportId>"` — reuse that reportId instead of
  treating it as an error.
- Don't append `curl -w "HTTP:%{code}"` to a body you then pipe to `json.load` — it breaks parsing.

## Date window (2-day report)
- Data lags ~48h. Window = the 2 full finalised days ending 48h before run.
- Run 2026-11-20 23:09 UTC → window = **Mon 2026-11-16 and Tue 2026-11-17**.

## ⚠️ KEY STANDING ISSUE — zero ad delivery
- As of 2026-11-20 the **US profile has `validPaymentMethod: false`** and a $40 daily budget.
  Result: all 15 ENABLED campaigns served **0 impressions / 0 clicks / 0 spend / 0 sales**
  for the window AND for the trailing 30 days. This is **real, not a data error** — do NOT
  invent numbers. Root cause = no valid payment method on the US Ads account, so Amazon will
  not serve the ads.
- Campaign structure exists (54 campaigns: 15 ENABLED, 32 PAUSED, 7 ARCHIVED) — account was
  recently built out. Only 15 campaigns existed during the 11-16/11-17 window.
- **Each run: check whether `validPaymentMethod` has flipped to true and whether impressions
  have started.** The moment real spend appears, the report content changes from "fix billing"
  to normal performance analysis.

## ⚠️ EMAIL DELIVERY BLOCKED (2026-11-20)
- The **Gmail connector is connected at the org level but `enabledInChat: false`** — its tools
  are NOT loaded in automated sessions, so the report cannot be emailed from here. Google Drive
  and GitHub work fine. No SMTP/email fallback is available in this environment.
- **To fix:** the user needs to enable the Gmail connector's tools for Claude Code sessions
  (claude.ai connector settings), or add an email-capable tool. Until then, reports land in the
  repo and the Drive "PPC Reports" folder, and the run notifies by push notification instead.
- Each run: still attempt to load Gmail tools (ToolSearch "gmail send"); if available, email it.

## Delivery checklist each run
1. reports/ppc-2day-latest.md (overwrite) + reports/ppc-2day-YYYY-MM-DD.md (dated), commit to
   branch `claude/great-hopper-bewmbe`.
2. Upload same file to Google Drive folder **"PPC Reports"**.
3. Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — <dates>`.
4. Compare against previous ppc-2day-* report; first run = baseline (no prior).

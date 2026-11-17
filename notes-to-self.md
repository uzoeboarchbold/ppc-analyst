# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more accurate. Append, don't rewrite history.

## Account / environment facts
- **Correct advertising profile = US, profileId `26765323558215`** (marketplace ATVPDKIKX0DER, currency USD, seller "Uzoebo Archbold E-Commerce").
- The env var `AMZ_PROFILE_ID` is **WRONG / unusable**: it holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5` (an application-client-id format, not a numeric profile id). **Do NOT pass it as `Amazon-Advertising-API-Scope`.** Hard-code / resolve the real profile id instead by calling `/v2/profiles` and picking the US seller profile. If someone fixes the env var later, re-verify.
- Profiles on this account: CA `2840235221595557` (0 SP campaigns), MX `3892485344323414` (0 SP campaigns), US `26765323558215` (54 SP campaigns). US is the only active one.
- Product under advertising: Cat Deterrent Spray / Pet Odor Eliminator, ASIN `B0FXW3GW5F`, SKU `6K-PZMX-MTDZ`.
- **Region/proxy**: only the NA endpoint `https://advertising-api.amazon.com` works. The EU (`-eu`) and FE (`-fe`) endpoints are blocked by the outbound proxy (403 Forbidden). All three profiles are NA-region anyway, so this is fine.

## Amazon Ads API gotchas (v3 reporting)
- Auth: refresh-token grant at `https://api.amazon.com/auth/o2/token` works. Access token lasts ~1h.
- Reporting is async: POST `/reporting/reports` -> poll GET `/reporting/reports/{id}` until `status==COMPLETED` -> download the gzipped JSON `url`. Content-Type/Accept = `application/vnd.createasyncreportrequest.v3+json`.
- **Column names**: `acosClicks7d` and `roasClicks7d` DO NOT EXIST. Only `acosClicks14d` / `roasClicks14d` are valid. For a 7-day attribution view, request `cost` + `sales7d` + `purchases7d` and compute ACOS = cost/sales, ROAS = sales/cost yourself.
- Report types used: `spCampaigns` (groupBy `campaign`), `spTargeting` (groupBy `targeting`), `spSearchTerm` (groupBy `searchTerm`). `topOfSearchImpressionShare` is available on `spCampaigns`.
- Targeting & search-term reports return **0 rows when there were no impressions** — that's expected, not a bug.

## Attribution window convention (keep consistent across runs!)
- Headline Sales / Purchases / ACOS / ROAS use **14-day attribution** to match the established report series (the Nov 12–13 report and earlier ones all use "14-day click, Amazon SP default"). Request `cost` + `sales14d` + `purchases14d` and compute ACOS/ROAS, OR use the `acosClicks14d`/`roasClicks14d` columns. (Note: `acosClicks7d`/`roasClicks7d` do NOT exist; `sales7d`/`purchases7d` do, if you ever need a 7d view — but the SERIES standard is 14d, so report 14d.)

## Report history / where to find the previous report (IMPORTANT)
- The repo `reports/` folder can be EMPTY on a fresh clone (the container is ephemeral). **The real archive of past reports is the Google Drive "PPC Reports" folder** (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Always check Drive for the previous report of this type before concluding "no previous report / baseline."
- Known prior 2-day reports in Drive: Nov 12–13 (gen Nov 16), Nov 10–11 (gen Nov 14), Oct 13–14, Aug 13–14, June 13–14. All found zero delivery. The immediately-previous 2-day report to compare against = the most recent one before this run.
- There are also monthly/weekly reports in that folder from the same series (don't confuse types — compare 2-day vs 2-day only).

## Date window convention
- 2-day report: data lags 48h. Window = the 2 full calendar days ending at the 48h-before-now cutoff. E.g. run 2026-11-17 23:09 UTC -> cutoff 2026-11-15 23:09 -> window = Nov 13 & Nov 14.
- Dated report copy uses the **run date** (`ppc-2day-[run YYYY-MM-DD].md`), not the window date, so each run is a distinct file.

## Delivery / sending
- **No email/Gmail tool exists in this environment.** Only the Google-Drive and github MCP servers are available. Cannot send a true email.
  - Substitute: upload the report to the Google Drive "PPC Reports" folder and `share_file` it to uzoebo.archbold@gmail.com with role `reader` — Drive sends a share-notification email with a link. Note this substitution in the report/handoff.
  - If a Gmail/email connector becomes available later, switch to real email.
- Google Drive folder "PPC Reports": create it if it doesn't exist; reuse its folder id afterwards.

## Standing finding (as of 2026-11-17 run)
- **The account has ZERO ad delivery.** All 54 US campaigns are ENABLED but delivered 0 impressions / 0 clicks / 0 spend / 0 sales every day for at least the last 30 days (checked Oct 16 – Nov 14).
- Most likely cause: the US advertising profile has **`validPaymentMethod: false`** — Amazon won't serve ads without a valid payment method on file. (Daily budget is also only $40.)
- Action for the business owner: add/fix a valid payment method in Seller Central → Advertising, confirm campaigns have budgets and the product is in stock & buy-box eligible. Until delivery resumes, every PPC report will be empty.
- If a future run suddenly shows data, delivery resumed — compare against the last non-empty report, and update this note.

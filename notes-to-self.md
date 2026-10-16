# PPC Analyst — Notes to Self

Running log of lessons so future runs work smoothly. Newest notes at top.

## Environment / API facts (confirmed 2026-10-16)

- **Python:** use `python3.13` (not `python3`, which is 3.11 and has no `requests`).
  `requests` is installed for 3.13 only. Run scripts with `python3.13 -I script.py`.
- **Proxy / TLS:** outbound HTTPS works via the agent proxy. Pass
  `verify="/root/.ccr/ca-bundle.crt"` to `requests`. Never disable TLS verify.
- **Amazon Ads region:** account is **North America** →
  `https://advertising-api.amazon.com`. The EU/FE hosts are NOT reachable
  from this environment (proxy blocks them) — don't waste retries on them.
- **Token endpoint:** `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token. Works with the env-var credentials. Access token
  is short-lived — fetch a fresh one at the start of every run.

## IMPORTANT — AMZ_PROFILE_ID env var is WRONG

- `AMZ_PROFILE_ID` (a 50-char non-numeric string) does **not** match any real
  profile on this account. Do NOT use it as the API scope.
- The real profiles (GET /v2/profiles) are all seller accounts named
  "Uzoebo Archbold E-Commerce":
  - `2840235221595557` — CA / CAD — **0 campaigns**
  - `3892485344323414` — MX / MXN — **0 campaigns**
  - `26765323558215`  — **US / USD — 54 campaigns (this is the live account)**
- **Always use profile `26765323558215` (US)** until the env var is fixed.
  If someone fixes AMZ_PROFILE_ID later, re-verify it matches this US profile.

## Reporting API (v3) gotchas

- Endpoint: `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`. Poll
  `GET /reporting/reports/{id}` (statuses: PENDING→PROCESSING→COMPLETED),
  then download the `url` (GZIP_JSON).
- **Date range max = 31 days** per report. For comparisons pull each window
  separately.
- **acosClicks7d / roasClicks7d are NOT valid columns.** Only the 14d
  variants exist. Simplest fix: don't request ACOS/ROAS columns — pull
  `cost`, `sales7d`, `purchases7d` and compute ACOS = cost/sales,
  ROAS = sales/cost yourself.
- Report types used: `spCampaigns` (groupBy ["campaign"], has
  `topOfSearchImpressionShare`), `spTargeting` (groupBy ["targeting"]),
  `spSearchTerm` (groupBy ["searchTerm"]).
- A SUMMARY report over a short window can return **0 rows** for campaigns
  that had zero delivery; a 30-day window returns the rows with zeros. Both
  mean the same thing: no impressions.

## BIG FINDING (2026-10-16 run) — ADS ARE NOT SERVING

- Zero impressions / clicks / spend / sales across ALL campaigns for the
  2-day window (Oct 13–14) AND the whole prior 30 days.
- **Likely cause:** US profile `accountInfo.validPaymentMethod = false`.
  Amazon will not serve ads without a valid payment method. The business
  owner needs to fix billing in Seller Central / Amazon Ads.
- Until spend resumes, every report will be all-zeros. Keep reporting the
  zero result + the payment-method cause rather than treating it as an error.

## Delivery channels

- **Google Drive: WORKS.** Folder "PPC Reports" id =
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload the .md there each run
  (contentMimeType text/markdown, disableConversionToGoogleType true).
- **EMAIL: BLOCKED (2026-10-16).** Gmail connector is installed + connected at
  the account level BUT `enabledInChat = false`, so no gmail send/draft tool is
  loaded into the session — I cannot send the report email automatically.
  FIX: the user must enable the Gmail connector for this chat/automation in the
  connector settings. Until then, report delivery = Drive + repo only, and note
  the un-sent email at the top of the run summary. Re-check `ListConnectors`
  each run; once `enabledInChat = true`, search for the gmail send tool and
  email uzoebo.archbold@gmail.com with subject "PPC 2-Day Report — [dates]".

## Reports

- First report of ANY type was this 2026-10-16 run → no prior report to
  compare against. Next 2-day run should compare to `ppc-2day-latest.md`.
- Save to `reports/ppc-2day-latest.md` (overwrite) + dated
  `reports/ppc-2day-YYYY-MM-DD.md` (run date).

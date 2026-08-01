# Notes to Self — PPC Analyst

Lessons carried between runs. Read this first, every run.

## Environment / credentials
- **`AMZ_PROFILE_ID` is WRONG.** It contains an LWA *application* ID
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric Ads
  profile ID. Do **not** pass it as `Amazon-Advertising-API-Scope`.
- The account has 3 seller profiles under seller "Uzoebo Archbold E-Commerce"
  (seller id A1C2I8MOP52E35):
  - **US = `26765323558215`** (USD, marketplace ATVPDKIKX0DER, daily budget $40) ← USE THIS
  - CA = `2840235221595557` (CAD)
  - MX = `3892485344323414` (MXN)
- All are in the **NA** region → host `https://advertising-api.amazon.com`.
- The proxy blocks the EU/FE ad hosts (403) — that's expected, we're NA-only.
- LWA token: POST `https://api.amazon.com/auth/o2/token` with the 4 env vars,
  grant_type=refresh_token. Works fine; token lasts ~1h.

## Gotchas
- Do NOT name a Python file `token.py` — it shadows the stdlib `token` module
  and breaks `requests`. Use e.g. `get_token.py`.
- Campaign names contain `|` characters — escape them (`\|`) in markdown tables
  or the table columns break.
- Reporting API v3 is async: POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), poll GET
  `/reporting/reports/{id}` until COMPLETED, download the gzip-JSON `url`.
- `topOfSearchImpressionShare` comes back `null` for campaigns with ~no
  eligible impressions; render as "—".
- ACOS/ROAS undefined when sales=0; render "—" / n/a, never divide by zero.

## Report bookkeeping
- 2-day reports live in `reports/`: overwrite `ppc-2day-latest.md` and save a
  dated `ppc-2day-[YYYY-MM-DD].md`. Compare each run to the previous
  `ppc-2day-*.md` dated file.
- Date window: 2 full days ending 48h before run. Run 2026-08-01 covered
  2026-07-28 & 2026-07-29.
- Metrics use 7-day attribution (purchases7d / sales7d).

## Delivery
- Save to Google Drive folder "PPC Reports" (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`)
  and email uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
- **EMAIL BLOCKED (2026-08-01):** The Gmail connector is installed but
  `enabledInChat: false`, so no Gmail send tool is loaded — the report could NOT
  be emailed automatically. ACTION NEEDED: user must enable the Gmail connector
  for this chat/automation in connector settings. Until then, delivery is
  Drive + repo only. Re-check each run.
- **Drive has no delete/update tool** — only create/copy. Don't upload a
  placeholder then re-upload; build the full content first and upload once, or
  you'll leave duplicates you can't clean up (happened on the 2026-08-01 run —
  one stray 11-byte placeholder left behind).

## History
- 2026-08-01 (first run, baseline): Jul 28–29. Almost dormant account —
  spend $2.19, 1 click, 0 sales, 140 impressions across 11 campaigns. Only the
  "…Brand Root … Exact" campaign spent (competitor term "angry orange pet odor
  eliminator"). 10/11 campaigns spent $0 — likely bids too low / low volume.

# Notes to Self — PPC Analyst Routine

Running log of lessons so future runs are faster and more reliable.
Newest lessons at the top of each section.

## Account / API facts (confirmed 2026-07-24)
- **Region: NA.** Endpoint host `https://advertising-api.amazon.com`.
  Auth/token host `https://api.amazon.com/auth/o2/token`. EU/FE hosts are
  blocked by the network proxy anyway.
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** It contains an application
  ARN (`amzn1.application...`), NOT a numeric profile ID. Do NOT pass it as
  the Advertising scope — it will fail. Instead, call `/v2/profiles` and pick
  the profile yourself.
- **Use profile `26765323558215` (US / USD).** It is the only profile with
  active SP campaigns (50+) and a real daily budget ($40). The CA
  (`2840235221595557`) and MX (`3892485344323414`) profiles have ZERO
  campaigns and placeholder budgets — ignore them.
- Seller: "Uzoebo Archbold E-Commerce". Main product in the account is a
  Cat Deterrent Spray / Pet Odor Eliminator (ASIN B0FXW3GW5F).
- Currency for the report is **USD**.

## Reporting API (v3 async)
- Create: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Reports take a few MINUTES to move PENDING -> COMPLETED. Poll every ~15s;
  don't give up early. Run the poll loop in the BACKGROUND (foreground
  `sleep` is blocked in this env, and a 2-min foreground poll times out).
- Report types used: `spCampaigns` (groupBy campaign; has
  `topOfSearchImpressionShare`), `spTargeting` (groupBy targeting), and
  `spSearchTerm` (groupBy searchTerm) for the exact-match candidates.
- Compute CTR, CPC, ACOS, ROAS yourself from raw impressions/clicks/cost/
  sales/purchases — cleaner than relying on every column existing.
- Use `purchases7d` / `sales7d` as the conversion columns (7-day attribution).

## Date window (data lags 48h)
- 2-day report: take the 2 full calendar days ending on/before (now - 48h),
  in the account/UTC frame. State exact dates at the top.

## Delivery channels
- **Google Drive:** folder "PPC Reports" exists, id
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload the .md there each run.
- **Email:** there is NO Gmail/email MCP tool in this environment. The
  scheduled-routine PushNotification is the email channel — its
  <routine_summary> full text becomes the email body to
  uzoebo.archbold@gmail.com. Put the report summary there.
- **Git:** save to `reports/ppc-2day-latest.md` + dated copy, commit & push
  to branch `claude/great-hopper-c8qu4x`.

## Comparison — WHERE THE HISTORY LIVES
- The **git repo starts fresh** each run in this environment (only the
  initial commit is present). The DURABLE history of past 2-day reports
  lives in the **Google Drive "PPC Reports" folder**, NOT in git. So to find
  the previous report of this type, LIST THE DRIVE FOLDER
  (`parentId = '1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo'`) and pick the most recent
  "PPC 2-Day Report …" by date — do not assume "no prior report exists".
- 2-day reports run every ~2 days. As of 2026-07-24 the previous one was
  **18–19 Jul 2026** (created 2026-07-22).

## KEY ONGOING FINDING — account has been DARK since ~9–10 June 2026
- Every 2-day report for 6+ weeks (from mid-June through 21 Jul) shows
  **$0 spend, $0 sales, 0 clicks, 0 impressions**. This is real, not a data
  error (cross-checked against 30-day pulls each time).
- Only 2 campaigns are ENABLED — "SP KT | ST w/ Sales" (keyword targeting)
  and "SP PT | ST w/ Sales" (product targeting), ~$8/day each — and BOTH
  serve zero impressions. The other ~52 campaigns are PAUSED or ARCHIVED.
- Root cause is delivery-side, not settings: most likely the advertised
  product (ASIN B0FXW3GW5F) is out of stock / has lost the Buy Box / listing
  suppressed, OR bids are too low to win any auction. validPaymentMethod is
  now TRUE (an earlier June report suspected payment; that's resolved).
- The spCampaigns report only returns the ENABLED campaigns (both zero);
  spTargeting and spSearchTerm return 0 rows — all consistent with zero
  delivery.
- Because this is a persistent, already-well-documented outage, the
  notification should say "still dark, no change" rather than raise a fresh
  alarm each run.

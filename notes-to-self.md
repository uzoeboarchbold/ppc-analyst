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

## Comparison
- Compare against the PREVIOUS 2-day report file in `reports/`
  (`ppc-2day-*.md`, excluding latest and today's). First run (2026-07-24)
  had no prior report, so no comparison was possible.

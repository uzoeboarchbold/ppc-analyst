#!/usr/bin/env python3
"""Pull Amazon Sponsored Products performance via the Ads API (v3 reporting).

Hands-off helper for the PPC Analyst routine. Requests SUMMARY reports for a
date window, polls until ready, downloads GZIP_JSON, and writes raw JSON to an
output directory.

Usage:
  python3 -I scripts/pull_ppc.py <start YYYY-MM-DD> <end YYYY-MM-DD> <out_dir> [profile_id]

Credentials come from env: AMZ_CLIENT_ID, AMZ_CLIENT_SECRET, AMZ_REFRESH_TOKEN.
NOTE: AMZ_PROFILE_ID in this account is an *application* id, not a numeric
profile id, so the US profile is hard-coded as the default below. Override by
passing a profile id as the 4th argument.
"""
import os, sys, json, gzip, time, ssl, urllib.request, urllib.parse

DEFAULT_PROFILE = "26765323558215"  # US / USD (the only account with campaigns)
HOST = "advertising-api.amazon.com"  # NA region
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else None


def _req(url, data=None, headers=None, method=None):
    return urllib.request.Request(url, data=data, headers=headers or {}, method=method)


def _open(req, tries=5):
    last = None
    for i in range(tries):
        try:
            return urllib.request.urlopen(req, timeout=60, context=CTX)
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode()[:500]
            except Exception:
                pass
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(2 ** (i + 1))
                last = e
                continue
            raise RuntimeError(f"HTTP {e.code}: {body}") from e
        except Exception as e:
            if i < tries - 1:
                time.sleep(2 ** (i + 1))
                last = e
                continue
            raise
    if last:
        raise last


def get_token():
    cid, csec, rt = os.environ["AMZ_CLIENT_ID"], os.environ["AMZ_CLIENT_SECRET"], os.environ["AMZ_REFRESH_TOKEN"]
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token", "refresh_token": rt,
        "client_id": cid, "client_secret": csec,
    }).encode()
    req = _req("https://api.amazon.com/auth/o2/token", data=data,
               headers={"Content-Type": "application/x-www-form-urlencoded"})
    return json.load(_open(req))["access_token"]


def request_report(tok, cid, pid, name, report_type_id, group_by, columns, start, end):
    body = json.dumps({
        "name": name,
        "startDate": start,
        "endDate": end,
        "configuration": {
            "adProduct": "SPONSORED_PRODUCTS",
            "groupBy": group_by,
            "columns": columns,
            "reportTypeId": report_type_id,
            "timeUnit": "SUMMARY",
            "format": "GZIP_JSON",
        },
    }).encode()
    req = _req(f"https://{HOST}/reporting/reports", data=body, method="POST", headers={
        "Authorization": f"Bearer {tok}",
        "Amazon-Advertising-API-ClientId": cid,
        "Amazon-Advertising-API-Scope": pid,
        "Content-Type": "application/vnd.createasyncreportrequest.v3+json",
        "Accept": "application/vnd.createasyncreportrequest.v3+json",
    })
    return json.load(_open(req))["reportId"]


def poll_report(tok, cid, pid, report_id, timeout=900):
    deadline = time.time() + timeout
    url = None
    while time.time() < deadline:
        req = _req(f"https://{HOST}/reporting/reports/{report_id}", headers={
            "Authorization": f"Bearer {tok}",
            "Amazon-Advertising-API-ClientId": cid,
            "Amazon-Advertising-API-Scope": pid,
        })
        j = json.load(_open(req))
        status = j.get("status")
        if status in ("COMPLETED", "SUCCESS"):
            url = j.get("url")
            return url
        if status in ("FAILURE", "CANCELLED"):
            raise RuntimeError(f"Report {report_id} failed: {j.get('statusDetails')}")
        time.sleep(20)
    raise RuntimeError(f"Report {report_id} timed out after {timeout}s")


def download(url):
    # Presigned S3 URL (no auth headers)
    req = _req(url)
    raw = _open(req).read()
    try:
        raw = gzip.decompress(raw)
    except Exception:
        pass
    return json.loads(raw.decode())


def main():
    start, end, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    pid = sys.argv[4] if len(sys.argv) > 4 else DEFAULT_PROFILE
    os.makedirs(out_dir, exist_ok=True)
    cid = os.environ["AMZ_CLIENT_ID"]
    tok = get_token()

    reports = {
        "campaigns": dict(
            report_type_id="spCampaigns", group_by=["campaign"],
            columns=["campaignName", "campaignId", "campaignStatus", "impressions",
                     "topOfSearchImpressionShare", "clicks", "clickThroughRate", "cost",
                     "costPerClick", "purchases14d", "sales14d", "acosClicks14d",
                     "roasClicks14d", "purchases7d", "sales7d"],
        ),
        "targeting": dict(
            report_type_id="spTargeting", group_by=["targeting"],
            columns=["campaignName", "adGroupName", "keyword", "keywordType", "matchType",
                     "targeting", "impressions", "clicks", "clickThroughRate", "cost",
                     "costPerClick", "purchases14d", "sales14d", "acosClicks14d", "roasClicks14d"],
        ),
        "searchterm": dict(
            report_type_id="spSearchTerm", group_by=["searchTerm"],
            columns=["campaignName", "adGroupName", "keyword", "matchType", "searchTerm",
                     "impressions", "clicks", "clickThroughRate", "cost", "costPerClick",
                     "purchases14d", "sales14d", "acosClicks14d", "roasClicks14d"],
        ),
    }

    ids = {}
    for key, cfg in reports.items():
        ids[key] = request_report(tok, cid, pid, f"ppc2day-{key}-{start}", start=start, end=end, **cfg)
        print(f"requested {key}: {ids[key]}", flush=True)

    out = {}
    for key, rid in ids.items():
        url = poll_report(tok, cid, pid, rid)
        data = download(url)
        path = os.path.join(out_dir, f"{key}.json")
        with open(path, "w") as f:
            json.dump(data, f)
        out[key] = len(data) if isinstance(data, list) else "?"
        print(f"downloaded {key}: {out[key]} rows -> {path}", flush=True)


if __name__ == "__main__":
    main()

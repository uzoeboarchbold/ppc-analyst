#!/usr/bin/env python3
import os, sys, json, time, gzip, io, urllib.request, urllib.parse, urllib.error

CID = os.environ["AMZ_CLIENT_ID"]
CSEC = os.environ["AMZ_CLIENT_SECRET"]
RT = os.environ["AMZ_REFRESH_TOKEN"]
PROFILE = "26765323558215"  # US seller profile (env AMZ_PROFILE_ID is an app id, not usable)
BASE = "https://advertising-api.amazon.com"
START = "2026-06-13"
END = "2026-06-14"

def get_token():
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token", "refresh_token": RT,
        "client_id": CID, "client_secret": CSEC,
    }).encode()
    req = urllib.request.Request("https://api.amazon.com/auth/o2/token", data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    return json.load(urllib.request.urlopen(req))["access_token"]

AT = get_token()

def hdr(ct=None):
    h = {"Amazon-Advertising-API-ClientId": CID,
         "Amazon-Advertising-API-Scope": PROFILE,
         "Authorization": "Bearer " + AT}
    if ct: h["Content-Type"] = ct; h["Accept"] = ct
    return h

def api(method, path, body=None, ct=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=hdr(ct), method=method)
    try:
        r = urllib.request.urlopen(req)
        return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()

def create_report(rtid, group_by, columns):
    body = {
        "name": f"{rtid} {START}",
        "startDate": START, "endDate": END,
        "configuration": {
            "adProduct": "SPONSORED_PRODUCTS",
            "groupBy": group_by,
            "columns": columns,
            "reportTypeId": rtid,
            "timeUnit": "SUMMARY",
            "format": "GZIP_JSON",
        },
    }
    ct = "application/vnd.createasyncreportrequest.v3+json"
    st, resp = api("POST", "/reporting/reports", body, ct)
    if st not in (200, 202):
        print(f"CREATE FAIL {rtid}: {st} {resp}", file=sys.stderr)
        return None
    return resp["reportId"]

def poll(rid):
    for _ in range(60):
        st, resp = api("GET", f"/reporting/reports/{rid}")
        if st != 200:
            print(f"POLL FAIL {rid}: {st} {resp}", file=sys.stderr); return None
        status = resp.get("status")
        if status == "COMPLETED":
            return resp.get("url")
        if status in ("FAILURE", "CANCELLED"):
            print(f"REPORT {rid} {status}: {resp}", file=sys.stderr); return None
        time.sleep(20)
    print(f"REPORT {rid} timed out", file=sys.stderr); return None

def download(url):
    raw = urllib.request.urlopen(url).read()
    try:
        return json.loads(gzip.GzipFile(fileobj=io.BytesIO(raw)).read())
    except OSError:
        return json.loads(raw)

CAMP_COLS = ["campaignName","campaignId","impressions","topOfSearchImpressionShare",
    "clicks","clickThroughRate","cost","costPerClick","purchases30d","sales30d"]
TGT_COLS = ["campaignName","keyword","keywordType","targeting","matchType","impressions",
    "clicks","clickThroughRate","cost","costPerClick","purchases30d","sales30d"]
ST_COLS = ["campaignName","keyword","searchTerm","matchType","impressions","clicks",
    "cost","purchases30d","sales30d"]

jobs = {
    "campaigns": ("spCampaigns", ["campaign"], CAMP_COLS),
    "targeting": ("spTargeting", ["targeting"], TGT_COLS),
    "searchterm": ("spSearchTerm", ["searchTerm"], ST_COLS),
}

rids = {}
for k, (rtid, gb, cols) in jobs.items():
    rid = create_report(rtid, gb, cols)
    print(f"{k}: reportId={rid}", file=sys.stderr)
    if rid: rids[k] = rid

out = {}
for k, rid in rids.items():
    url = poll(rid)
    if url:
        out[k] = download(url)
        print(f"{k}: {len(out[k])} rows", file=sys.stderr)

with open("ppc_raw.json", "w") as f:
    json.dump(out, f, indent=2)
print("SAVED ppc_raw.json", file=sys.stderr)

#!/usr/bin/env python3
"""Fetch pinned primary backend files outside the returned checkpoint."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import json
import tarfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parents[1] / "tmp/c9_computation_backend"
OUT = ROOT / "agents/continuation9_computation_method"
WORK.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
PIN = "cfe53e0454fdd167adfab00c69e602341b105e40"
API = "https://api.github.com/repos/philip-engel/philip-engel.github.io/contents/threefold-explorer/api/engine?ref=" + PIN


def fetch(url):
    with urlopen(Request(url, headers={"User-Agent": "S6 publication marked-cochain verification"}), timeout=45) as response:
        return response.read()


def keep(item):
    path = WORK / item["name"]
    cached = ROOT.parents[1] / "tmp/c9_sources" / ("explorer_" + item["name"])
    data = path.read_bytes() if path.exists() else cached.read_bytes() if cached.exists() else fetch(item["download_url"])
    assert len(data) == item["size"]
    blob = f"blob {len(data)}\0".encode() + data
    assert hashlib.sha1(blob).hexdigest() == item["sha"]
    path.write_bytes(data)
    return {"name": item["name"], "url": item["download_url"], "bytes": len(data),
            "git_blob_sha1": item["sha"], "sha256": hashlib.sha256(data).hexdigest()}


items = json.loads(fetch(API))
assert all(item["type"] == "file" for item in items)
with ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(keep, items))
archive = WORK / "local_model_database.tar.gz"
with tarfile.open(archive) as tar:
    for member in tar.getmembers():
        assert not member.issym() and not member.islnk()
        assert not Path(member.name).is_absolute() and ".." not in Path(member.name).parts
    tar.extractall(WORK, filter="data")
metadata = {"repository_commit": PIN, "directory_url": API,
            "scope": "Pinned executable algebraic backend and exact local cochain data; retrieval alone supplies no computation or geometric-identification credit.",
            "sources": records}
(OUT / "S6_SERIES_PUBLISH_c9_backend_sources.json").write_text(json.dumps(metadata, indent=2) + "\n", newline="\n")
for record in records:
    print(record["name"], record["bytes"], record["sha256"])
print("Fetched", len(records), "verified source/data files; extracted database outside checkpoint:", WORK)

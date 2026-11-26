#!/usr/bin/env python3
"""Open primary sources used by the later Paper II unit; store metadata only."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import csv
import hashlib
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents" / "continuation3_provenance" / "later_part"
TEMP = ROOT.parents[1] / "tmp" / "c3_provenance_primary"
OUT.mkdir(parents=True, exist_ok=True)
sources = [
 ("BierstoneMilman_v2", "https://arxiv.org/pdf/alg-geom/9508005v2", "pdf"),
 ("Douady1966", "https://www.numdam.org/item/10.5802/aif.226.pdf", "pdf"),
 ("Buchdahl1999", "https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf", "pdf"),
 ("ArtebaniDolgachev2009", "https://ems.press/content/serial-article-files/44190?nt=1", "pdf"),
] + [("DLMF_"+s.replace(".","_"), "https://dlmf.nist.gov/"+s, "html") for s in ("20.2","20.4","20.5","20.7","20.13","23.3","23.6","23.17")]

def download(row):
 key,url,suffix=row
 result=dict(key=key,url=url,date_utc=datetime.now(timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=40) as response:
   data=response.read();result["http_status"]=response.status
  target=TEMP/(key+"."+suffix);target.write_bytes(data)
  result.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),temp_file=str(target),status="retrieved; exact locus reading recorded separately")
  if suffix=="pdf":subprocess.run(["pdftotext","-layout",str(target),str(target.with_suffix(".txt"))],check=True,capture_output=True)
 except Exception as e:
  result.update(status=type(e).__name__+": "+str(e))
 return result

with ThreadPoolExecutor(max_workers=4) as pool:
 rows=list(pool.map(download,sources))
fields=["key","url","date_utc","http_status","bytes","sha256","temp_file","status"]
with (OUT/"S6_SERIES_PUBLISH_later_source_downloads.tsv").open("w",newline="") as h:
 w=csv.DictWriter(h,fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)
for r in rows:print(r["key"],r.get("http_status"),r.get("sha256"),r["status"])

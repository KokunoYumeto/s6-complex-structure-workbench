#!/usr/bin/env python3
"""Retrieve cited editions for reading; keep published material outside checkpoints."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT.parents[1] / "tmp" / "c3_provenance_primary"
OUT = ROOT / "agents" / "continuation3_provenance"
TEMP.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = [
    ("CDP2020", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/algebraic_dimension_of_compact_complex_threefolds_with_vanishing_second_betti_number.pdf"),
    ("CDP98", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/79BEA1EB6CF23BB9AEBCF4677C82B108/S0010437X98000360a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf"),
    ("AC26", "https://alpo.ge/s6.pdf"),
    ("Engel_v1", "https://arxiv.org/pdf/2609.38442v1"),
    ("DGKX_v1", "https://arxiv.org/pdf/2610.00250v1"),
    ("DGKX_v2", "https://arxiv.org/pdf/2610.00250v2"),
    ("LR_v2", "https://arxiv.org/pdf/2609.33826v2"),
    ("Two_v1", "https://arxiv.org/pdf/2609.33785v1"),
    ("Comb_v1", "https://arxiv.org/pdf/2610.10451v1"),
    ("Log_v1", "https://arxiv.org/pdf/2610.39102v1"),
    ("HKP_v1", "https://arxiv.org/pdf/math/9812076v1"),
    ("Kamenova", "https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf"),
    ("LRS_v1", "https://arxiv.org/pdf/1912.09719v1"),
    ("Yang_v1", "https://arxiv.org/pdf/2609.29666v1"),
    ("Horikawa1974", "https://www.jstage.jst.go.jp/article/jmath1948/26/4/26_4_647/_pdf/-char/en"),
]
IMAGES = [(f"Steenbrink1976_p{page}", f"https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0031:{page+6:08d}/full/1600,/0/default.jpg") for page in [231,233,234,235,236,237,238,239]]
image_mode = "--images" in sys.argv

def retrieve(item):
    key, url = item
    row = dict(key=key, url=url, date_utc=datetime.now(timezone.utc).isoformat())
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=40) as reply:
            data = reply.read()
            row.update(http_status=reply.status, final_url=reply.url)
        expected = b"\xff\xd8" if image_mode else b"%PDF"
        assert data.startswith(expected), "Response has wrong file type"
        path = TEMP / (key + (".jpg" if image_mode else ".pdf"))
        path.write_bytes(data)
        if not image_mode:
            subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True, capture_output=True)
        row.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), temp_file=str(path), status="retrieved; page reading recorded separately")
    except Exception as exc:
        row["status"] = type(exc).__name__ + ": " + str(exc)
    return row

with ThreadPoolExecutor(max_workers=5) as pool:
    rows = list(pool.map(retrieve, IMAGES if image_mode else SOURCES))
fields = ["key", "url", "date_utc", "http_status", "final_url", "bytes", "sha256", "temp_file", "status"]
with (OUT / ("S6_SERIES_PUBLISH_c3_provenance_image_downloads.tsv" if image_mode else "S6_SERIES_PUBLISH_c3_provenance_source_downloads.tsv")).open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
for row in rows:
    print(row["key"], row.get("bytes", ""), row.get("sha256", ""), row["status"])

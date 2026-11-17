"""Fetch already opened primary sources for the source-loop link audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import urllib.request

root = Path(__file__).resolve().parents[2]
target = root / "records/external_source_cache/source_loop_immersions"
target.mkdir(parents=True, exist_ok=True)
sources = [
    ("nemethi_pinter_2015.pdf", "https://ems.press/content/serial-article-files/43391"),
    ("sakai_2015.pdf", "https://arxiv.org/pdf/1405.1947"),
    ("takase_2005.pdf", "https://arxiv.org/pdf/math/0506356"),
    ("gauniyal_turchin.html", "https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/goussarovpolyakviro-type-formulas-for-4k1dimensional-knots-and-links-in-mathbbr6k/FDBF3CFC3531902C45DE9C1D0F8D9A28"),
]
results = []
for name, url in sources:
    item = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    try:
        data = urllib.request.urlopen(url, timeout=15).read()
        (target / name).write_bytes(data)
        item.update(status="saved", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        item.update(status="failed", error=str(exc))
    results.append(item)
    print(json.dumps(item), flush=True)
(root / "records/source_loop_immersion_downloads.json").write_text(json.dumps(results, indent=2)+"\n")

"""Fetch the precise primary inputs used in the four initial analytic checks."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).parent / "literature"
SOURCES = {
    "Gauduchon1985": "https://numdam.org/item/AST_1985__126__129_0.pdf",
    "AgboolaHoward2006": "https://web.math.ucsb.edu/~agboola/papers/bisi_aif_2006.pdf",
    "Waldschmidt1979_translation": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SigmaNoteCanada1979-eng.pdf",
    "HuberWuestholz_v8": "https://arxiv.org/pdf/1805.10104v8",
    "STW_v2": "https://arxiv.org/pdf/1503.04491v2",
    "Shin_v6": "https://arxiv.org/pdf/1009.2253v6",
}

def fetch(item):
    key, url = item
    path = ROOT / f"S6_SERIES_PUBLISH_I_{key}.pdf"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as response:
        data = response.read()
        status, resolved = response.status, response.url
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Not a PDF: {key}")
    path.write_bytes(data)
    return dict(key=key, url=url, resolved_url=resolved, status=status,
                path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                retrieved_at_utc=datetime.now(timezone.utc).isoformat())

if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as executor:
        receipts = list(executor.map(fetch, SOURCES.items()))
    out = ROOT / "S6_SERIES_PUBLISH_I_primary_retrieval_receipt.json"
    out.write_text(json.dumps(receipts, indent=2) + "\n")
    print(json.dumps(receipts, indent=2))

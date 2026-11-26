"""Reopen primary URLs, retaining metadata only and no downloaded source copy."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ("Paper II records page", "https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md"),
    ("AC26", "https://alpo.ge/s6.pdf"),
    ("Viaclovsky2026Combs", "https://arxiv.org/pdf/2610.10451v1"),
    ("Viaclovsky2026Log", "https://arxiv.org/pdf/2610.39102v1"),
    ("LiuRollenske2026", "https://arxiv.org/pdf/2609.33826v2"),
    ("DGKXv1", "https://arxiv.org/pdf/2610.00250v1"),
]


def get(item):
    source, url = item
    row = dict(source=source, url=url, date_utc=datetime.now(timezone.utc).isoformat(),
               status="", final_url="", size="", sha256="", anchor_check="")
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            row.update(status=str(response.status), final_url=response.url,
                       size=str(len(data)), sha256=hashlib.sha256(data).hexdigest())
            if source == "Paper II records page":
                row["anchor_check"] = str(b"paper-ii" in data)
    except Exception as error:
        row["status"] = type(error).__name__ + ": " + str(error)
    return row


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=6) as executor:
        rows = list(executor.map(get, TARGETS))
    target = ROOT / "S6_SERIES_PUBLISH_c4_source_access.tsv"
    with target.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row["source"], row["status"], row["size"], row["sha256"], row["anchor_check"])

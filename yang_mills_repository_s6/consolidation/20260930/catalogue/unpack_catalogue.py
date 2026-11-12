from __future__ import annotations

import gzip
import hashlib
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "CORPUS_CATALOGUE_V2_PUBLIC.sqlite.gz"
OUTPUT = ROOT / "CORPUS_CATALOGUE_V2_PUBLIC.sqlite"
EXPECTED_SHA256 = "c10a285a1e0420a1795b22df7c6981a2a26214deb0a23561a54a1d52c891b893"

with gzip.open(SOURCE, "rb") as incoming, OUTPUT.open("wb") as outgoing:
    shutil.copyfileobj(incoming, outgoing, 1024 * 1024)

actual = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
if actual != EXPECTED_SHA256:
    OUTPUT.unlink(missing_ok=True)
    raise SystemExit(f"SHA-256 mismatch: {actual}")
print(f"verified {OUTPUT.name}: {actual}")

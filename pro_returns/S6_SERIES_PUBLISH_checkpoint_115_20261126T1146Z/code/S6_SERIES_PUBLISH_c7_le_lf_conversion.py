#!/usr/bin/env python3
"""Preserve exact CRLF table bytes reversibly; convert current table to LF.

The executed v001 source and streams are never modified. The corrected
v002 writer is saved but not executed by this conversion program.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import base64
import csv
import io

ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / "agents/continuation7_iii_mixed_torsion/S6_SERIES_PUBLISH_III_02LE_fresh_patterns_v001.tsv"
SOURCE = ROOT / "code/S6_SERIES_PUBLISH_c7_le_mixed_v001.py"
CORRECTED = ROOT / "code/S6_SERIES_PUBLISH_c7_le_mixed_v002.py"
assert not CORRECTED.exists()
old = TABLE.read_bytes()
assert old.count(b"\r\n") == 13 and old.count(b"\r") == 13
new = old.replace(b"\r\n", b"\n")
assert new.replace(b"\n", b"\r\n") == old
assert list(csv.reader(io.StringIO(old.decode()), delimiter="\t")) == list(csv.reader(io.StringIO(new.decode()), delimiter="\t"))
print("Conversion UTC", datetime.now(timezone.utc).isoformat())
print("Original executed table SHA256", sha256(old).hexdigest())
print("Original executed table byte count", len(old))
print("Original executed table exact base64", base64.b64encode(old).decode())
print("Corrected LF table SHA256", sha256(new).hexdigest())
print("Corrected LF table byte count", len(new))
source = SOURCE.read_text()
assert source.count('csv.DictWriter(f, fields, delimiter="\\t", extrasaction="ignore")') == 1
corrected = source.replace('csv.DictWriter(f, fields, delimiter="\\t", extrasaction="ignore")',
                           'csv.DictWriter(f, fields, delimiter="\\t", extrasaction="ignore", lineterminator="\\n")')
corrected = corrected.replace("version 001", "version 002").replace("_v001", "_v002")
assert corrected != source and "lineterminator=" in corrected
CORRECTED.write_text(corrected)
TABLE.write_bytes(new)
print("Executed v001 source retained SHA256", sha256(SOURCE.read_bytes()).hexdigest())
print("Corrected v002 source, NOT RUN, SHA256", sha256(CORRECTED.read_bytes()).hexdigest())
print("PASS: exact original bytes retained reversibly in this output; all table fields unchanged; current table is LF")

"""Admit the reviewed existing KD transitive check, without adding a required row."""
from pathlib import Path
import csv
import io
import hashlib

ROOT = Path(__file__).resolve().parents[1]
EVENT_ID = "publish:c5:III:02KD:completed-preserved-targeted-check"
packet = ROOT / "agents/continuation5_iii_02kd"
source_hash = hashlib.sha256((ROOT / "S6_SERIES_PUBLISH_III.tex").read_bytes()).hexdigest()
assert source_hash == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
comparison = (packet / "S6_SERIES_PUBLISH_III_02KD_comparison.md").read_text()
assert source_hash in comparison
assert (packet / "S6_SERIES_PUBLISH_III_02KD_proof_new.tex").is_file()
path = ROOT / "CHECK_EVENTS.tsv"
before = path.read_bytes()
reader = csv.DictReader(io.StringIO(before.decode()), delimiter="\t")
fields, existing = reader.fieldnames, list(reader)
assert EVENT_ID not in {r["event_id"] for r in existing}
with (packet / "S6_SERIES_PUBLISH_III_02KD_CHECK_EVENTS.tsv").open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    assert reader.fieldnames == fields
    rows = list(reader)
assert len(rows) == 1 and rows[0]["event_id"] == EVENT_ID
assert rows[0]["statement_id"] == "maps:src:D.1.4"
assert rows[0]["type"] == "targeted proof check"
rows[0]["outcome"] = rows[0]["outcome"].replace(
    "publication-unit criteria remain open; root admission required.",
    "publication-unit criteria remain open. Root read the complete preserved "
    "fresh derivation, full comparison and entire receiving proof and admitted "
    "this existing transitive check in continuation five."
)
append = io.StringIO(newline="")
csv.DictWriter(append, fields, delimiter="\t", lineterminator="\n").writerows(rows)
assert path.read_bytes() == before and before.endswith(b"\n")
path.write_bytes(before + append.getvalue().encode())
print("Admitted", EVENT_ID)
print("No required identity or unit row created or closed; prior event bytes retained.")

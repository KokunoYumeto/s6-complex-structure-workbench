"""Bind LQ's fibre-position convention to the live marked-data table."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted/canonical_star_logs.tex"
text = path.read_text()
old = r"The selected fibre labels are their positions, starting at one, in the ordered fibre lists of \ref{maps:src:D.2.19}."
new = r"The selected fibre labels are their positions, starting at one, in the component-data table in the proof of \ref{maps:src:D.2.23}."
assert text.count(old) == 1
path.write_text(text.replace(old, new), newline="\n")
log = lane / "S6_SERIES_PUBLISH_LQ_publication_defects.tsv"
with log.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
for kind in ("D06", "D20"):
    rows.append(dict(zip(fields, ["III-C8-LQ-PUB-029-"+kind, kind, "maps:src:D.2.49",
        "LQ proof, selected-position sentence", "pending page concordance",
        "weighted/canonical_star_logs.tex", "pending final build", old, new,
        "Bounded live-source reading found the actual ordered component table in KY's proof, D.2.23; KT, D.2.19, points to it. Correct the new locator while keeping all fibre labels unchanged. Root's global data-table relocation remains a later integration step.",
        "source locator corrected and read; root admission/global integration pending"])))
with log.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("POSITION_LOCATOR", "KY proof D.2.23; same ordered mathematical fibre labels")
print("TOTAL_SEQUENTIAL_EDITS29; SINGLE_TYPE_DEFECT_ROWS", len(rows))

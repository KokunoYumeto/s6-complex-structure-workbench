"""Apply the exact minor LQ publication readback edits."""
import csv
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted/canonical_star_logs.tex"
original = path.read_text()
text = original
changes = [
    (r"$k=2h$ with $h>0$", r"$k=2h$ with $h\in\mathbb Z_{>0}$", "D20;D26", "State h as a positive integer in the already proved even-root specialization; k=2h is used precisely with even k."),
    (r"$k=2h$, $j$ even and $N=2ke\pm1$.", r"$k=2h$ with $h\in\mathbb Z_{>0}$, $j$ even and $N=2ke\pm1$.", "D20;D26", "Use the same explicit positive-integer h in the specialization proof."),
    (r"At the exceptional $46/II$ position", r"At the exceptional $\mathrm{OS46/II}$ position", "D04;D20", "Use the catalogue profile name consistently with the table and the same actual vanishing words."),
    ("At $f=0$ the new chosen-centre class is", "At $f=0$ the chosen-centre class for $j$ is", "D08;D20", "Identify the translated conductor class by its parameter and the exact adjoining shear formula."),
]
log = lane / "S6_SERIES_PUBLISH_LQ_publication_defects.tsv"
with log.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    records = list(reader)
for number, (old, new, kinds, reason) in enumerate(changes, 25):
    assert text.count(old) == 1, old
    line = text.count("\n", 0, text.index(old)) + 1
    text = text.replace(old, new)
    for kind in kinds.split(";"):
        records.append(dict(zip(fields, [f"III-C8-LQ-PUB-{number:03}-{kind}", kind,
            "maps:src:D.2.49", f"canonical_star_logs.tex readback line {line}",
            "pending page concordance", "weighted/canonical_star_logs.tex",
            "pending final build", old, new, reason,
            "whole publication readback and exact correction completed; root admission and global gates pending"])))
units.check_permanent_identifiers(original, text)
with log.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(records)
path.write_text(text, newline="\n")
print("READBACK_EDITS", len(changes), "TOTAL_SEQUENTIAL_EDITS", 28, "SINGLE_TYPE_DEFECT_ROWS", len(records))
print("LINES", len(text.splitlines()), "IDENTIFIERS_PRESERVED; SHARED_WRITES0")

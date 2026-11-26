"""Apply the exact LN saturation-notation readback correction and record it."""
import csv
from datetime import datetime, timezone
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/whole_fibre_initial_pairs.tex"
before = path.read_text()
old = r"$\operatorname{sat} L=(L\otimes\mathbb Q)\cap\Lambda^2\Lambda$."
new = r"""For a sublattice $L$ of a lattice $W$, write
$\operatorname{sat}L=(L\otimes\mathbb Q)\cap W$; the ambient lattice
is $\Lambda^2\Lambda$ for $F_i$ and $\Lambda$ for the degree-one kernels."""
assert before.count(old) == 1
after = before.replace(old, new)
units.check_permanent_identifiers(before, after)
assert "\r" not in after
log = root / "agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_LN_publication_defects.tsv"
with log.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
rows.append(dict(zip(fields, ["III-C8-LN-PUB-063", "D20", "maps:src:D.2.46",
    "LN theorem, saturation notation after R_i", "pending page concordance",
    "weighted/whole_fibre_initial_pairs.tex", "pending final build", old, new,
    "Whole readback found that the new shorthand named only the degree-two ambient lattice although GI5 also uses saturation in Lambda. Specify both ambient lattices; the original kernels and their inverse maps are unchanged.",
    "source edit and exact readback completed; root admission and page concordance pending"])))
with log.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
path.write_text(after, newline="\n")
print("UTC", datetime.now(timezone.utc).isoformat())
print("READBACK_CORRECTION", "saturation ambient Lambda^2 Lambda or Lambda, respectively")
print("LINES", len(after.splitlines()), "EDIT_ROWS", len(rows), "IDENTIFIERS_PRESERVED")
print("SHARED_WRITES", 0, "AUTOMATIC_CRITERION_CREDIT", 0)

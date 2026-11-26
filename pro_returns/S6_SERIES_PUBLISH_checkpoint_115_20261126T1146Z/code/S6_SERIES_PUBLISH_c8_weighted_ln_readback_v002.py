"""Correct the sentence join in LN's explicit ambient-lattice notation."""
import csv
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/whole_fibre_initial_pairs.tex"
before = path.read_text()
old = "$\\Lambda^2\\Lambda$. Here $R_i=\\Lambda^2A_i-I$ and\nFor a sublattice"
new = "$\\Lambda^2\\Lambda$. Here $R_i=\\Lambda^2A_i-I$.\nFor a sublattice"
assert before.count(old) == 1
after = before.replace(old, new)
units.check_permanent_identifiers(before, after)
log = root / "agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_LN_publication_defects.tsv"
with log.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
rows.append(dict(zip(fields, ["III-C8-LN-PUB-064", "D23", "maps:src:D.2.46",
    "LN theorem, R_i sentence join", "pending page concordance",
    "weighted/whole_fibre_initial_pairs.tex", "pending final build", old, new,
    "Replace the conjunction before the newly separate saturation sentence by a full stop.",
    "exact sentence readback completed; root admission and page concordance pending"])))
with log.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
path.write_text(after, newline="\n")
print("SENTENCE_JOIN_CORRECTED; mathematical formula unchanged")
print("LINES", len(after.splitlines()), "EDIT_ROWS", len(rows), "IDENTIFIERS_PRESERVED")

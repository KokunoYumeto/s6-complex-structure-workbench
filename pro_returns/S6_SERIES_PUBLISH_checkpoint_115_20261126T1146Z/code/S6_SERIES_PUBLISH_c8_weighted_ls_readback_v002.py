"""Make the already proved additional-pair table's local condition explicit."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted/vertical_corrections.tex"
original = path.read_text()
old = "The positive height-one pairs for which neither section is narrow\nat every fibre are"
new = "The positive height-one pairs having a fibre where both section\nclasses are nonzero are"
assert original.count(old) == 1
candidate = original.replace(old, new)
units.check_permanent_identifiers(original, candidate)
table = lane / "S6_SERIES_PUBLISH_LS_publication_defects.tsv"
with table.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
number = max(int(row["change_id"].split("-")[-2]) for row in rows) + 1
for kind in ["D20", "D26"]:
    rows.append(dict(zip(fields, [f"III-C8-LS-PUB-{number:03}-{kind}", kind, "maps:src:D.2.50",
        "vertical_corrections.tex, additional height-one table introduction", "pending page concordance",
        "weighted/vertical_corrections.tex", "pending final build", old, new,
        "Specify failure of the local OR condition: a fibre has both section classes nonzero. The broader phrase neither globally narrow could also describe complementary nonzero classes at different fibres; it was not the table's proved domain. This repairs only the publication wording, not an admitted theorem.",
        "exact readback edit; root admission and global integration pending"])))
path.write_text(candidate, newline="\n")
with table.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("SEQUENTIAL_EDITS", number, "DEFECT_ROWS", len(rows), "IDENTITIES_PRESERVED; SHARED_WRITES0")

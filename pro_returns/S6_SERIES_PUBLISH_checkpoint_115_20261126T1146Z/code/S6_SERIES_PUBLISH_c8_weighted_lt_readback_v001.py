"""Exact LT readback edits; preserve all mathematical identity multiplicities."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted/invariant_chern_caps.tex"
original = path.read_text()
text = original
table = lane / "S6_SERIES_PUBLISH_LT_publication_defects.tsv"
with table.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
number = max(int(row["change_id"].split("-")[-2]) for row in rows)


def replace(old, new, kinds, reason, count=1):
    global text, number
    assert text.count(old) == count, (old, count, text.count(old))
    for _ in range(count):
        at = text.index(old)
        number += 1
        for kind in kinds.split(";"):
            rows.append(dict(zip(fields, [f"III-C8-LT-PUB-{number:03}-{kind}", kind, "maps:src:D.2.51",
                f"invariant_chern_caps.tex, readback at line {text.count(chr(10),0,at)+1}", "pending page concordance",
                "weighted/invariant_chern_caps.tex", "pending final build", old, new, reason,
                "whole publication source read; root admission and global integration pending"])))
        text = text[:at] + new + text[at+len(old):]


replace("When $c=0$, these groups are instead", "When $c=0$, $\\pi_1(U)=\\mathbb Z^2$ and the homology groups are", "D20;D22", "Make the zero-degree fundamental group, already proved by the exact attaching-loop presentation, explicit beside its homology table.")
replace("The displayed homotopy inverses identify the cap, with its marked cell maps,\nwith the mapping torus of the circle bundle over \\eqref{maps:eq:IC_local_1}.", "The displayed maps give a homotopy equivalence from the cap to\nthe mapping torus of the circle bundle over \\eqref{maps:eq:IC_local_1},\nwith the stated marked cell maps and both inverse homotopies.", "D08;D20", "Name the exact proved equivalence and its inverse homotopies rather than using identify with two successive with-phrases.")
for old, new, count in [("Kz", r"\mathcal K z", 8), ("KA_0", r"\mathcal K A_0", 3), ("K(", r"\mathcal K(", 5), ("Kx", r"\mathcal K x", 2)]:
    replace(old, new, "D20", "Rename the partial-sum linear map K to mathcal K by the identity on its defining coefficients and domain ker R, with the inverse identity. The geometric reduced fibre K keeps its name. Every quotient and boundary-preimage formula changes by that exact notation transport.", count=count)
units.check_permanent_identifiers(original, text)
path.write_text(text, newline="\n")
with table.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("LT_LINES", len(original.splitlines()), "->", len(text.splitlines()), "SEQUENTIAL_EDITS", number, "DEFECT_ROWS", len(rows))
print("OLD_IDENTIFIERS_PRESERVED; SHARED_WRITES0; ADDITIONAL_CHECK_CREDIT0")

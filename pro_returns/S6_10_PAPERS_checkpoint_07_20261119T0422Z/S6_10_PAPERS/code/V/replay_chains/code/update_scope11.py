"""Update the exact remaining D2 scope after the independently audited D44-46.

Earlier paragraphs and register rows are retained as dated research records.
This is not an hourly decision or a checkpoint creation.
"""
from pathlib import Path
import csv
import datetime
import json
import re

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "records/fourfolds_results.csv").open(newline="") as stream:
    owned = list(csv.DictReader(stream))
assert {"D.2.44", "D.2.45"} <= {r["id"] for r in owned}

path = ROOT / "sections/manifolds.tex"
text = path.read_text()
start = text.index(r"\paragraph{Remaining task D.2.4")
end = text.index(r"\paragraph{Theorem D.2.5", start)
archive = ROOT / "records/D2_4_superseded_at11.tex"
if not archive.exists():
    archive.write_text(text[start:end])
replacement = r'''\paragraph{Remaining task D.2.4 (Open: the full filling and smooth classification).}
The natural section-line sphere question is complete on all $21$
profiles, with $59$ marked sphere patterns on $50$ initial rows
(D.2.24--28). D.2.29--33 compute every allowed finite affine
logarithm and every original/log additive and original/Mumford
multiplicative choice on the natural initial catalogue: $495$
integral presentations on $172$ initial rows. D.2.37, D.2.40 and
D.2.41 include every positive translation iterate, retaining shared
even factors, arbitrary free finite and regular logarithms and the
ordinary clutch. D.2.43 supplies the full nonsaturated general-cusp
boundary kernel. D.2.46 now removes the scalar-iterate restriction:
all positive section pairs satisfying the fibrewise narrowness
condition and every effective whole-fibre weight distribution on
multiplicative or regular fibres have a complete integral algorithm,
with the original star caps. The exceptional OS49/II Klein-four
vertical subgroup is retained in the actual fundamental group.

The entire specified minimal simply connected smooth sector is now
classified: all $162$ patterns, all their allowed finite logarithmic
orders and affine twists, and every simply connected ordinary clutch,
within the stated primitive-Mumford scope and without additional
regular logarithms. D.2.44--45 resolve the last $18$ patterns.
Residual orders $4,8,20$ give respectively
$Z_{4,1}$, $Z_{8,0}$ and $Z_{4,1}\#Z_{5,1}$.
Their full refined classes are $2,0,14$ in the fixed cyclic
coordinates, and their fundamental-class invariants are zero.
The actual relative spin calculation uses the rational linking of
the literal critical cycle. The preferred finite-$II$ core
three-manifold is a full torsion generator even when the ordinary
regular three-torus is not. No division of an even cyclic residue
or unproved general change-of-three-frame formula is used.

The full D.2 request remains open for logarithmic Mumford star caps,
component-supported initial data and extra vertical corrections,
and the complete smooth invariants of the remaining weighted and
additional-regular-log outputs. For example, D.2.46 constructs the
simply connected OS45/default member with $P=2G$, $Q=8G$, weight
$2$ at $I_8$, all other weights zero, all Mumford caps and ordinary
clutch $e=1$. It has
\[
 H_2=\mathbb Z^{15}\oplus\mathbb Z/8,\qquad
 H_3=\mathbb Z/8,\qquad \chi=32.
\]
Its full mixed fundamental-class and refined tangent invariants
are not yet computed. The integral homology alone does not
identify its smooth type. The active attacks compute actual
component-divisor intersections and torsion framings for weighted
cusps, and full normalization/conductor boundary maps for arbitrary
star logarithms. Earlier failed half-weight, ordinary-characteristic
and nongenerating-three-torus shortcuts are retained with their
corrections in the dated research records.

'''
path.write_text(text[:start] + replacement + text[end:])

path = ROOT / "records/manifolds_results.csv"
with path.open(newline="") as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
row = next(r for r in rows if r["id"] == "D.2.4")
saved = ROOT / "records/scope_rows_superseded_at11.json"
if not saved.exists():
    saved.write_text(json.dumps({"source": path.name, "row": dict(row)}, indent=2) + "\n")
row.update(
    statement="The full D2 classification remains open after all162 minimal simply connected smooth patterns and the arbitrary compatible whole-fibre initial-pair integral algorithm have been completed.",
    status="Open",
    depends_on="D.2.24-46",
    notes="INCOMPLETE: remaining logarithmic star caps, component-supported/extra vertical data, and full weighted/additional-log smooth invariants. Concrete remaining weighted instance: OS45 P2G,Q8G,weight2 atI8,allMumford,e1; pi1=1,H2=Z^15+Z/8,H3=Z/8. All18 former residual4/8/20 patterns are now classified byD44-45.",
)
with path.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

path = ROOT / "S6_04_MAPS_MANIFOLDS_report.md"
text = path.read_text()
newrow = "| D.2 | D.2.1–D.2.46 | Undecided in the full classification. All 162 specified minimal simply connected patterns now have complete smooth identifications, including all allowed finite orders and affine twists in that sector. Exact integral algorithms cover all compatible positive initial section pairs and effective whole-fibre weights on the 21 profiles, with original star caps. Logarithmic star caps, component-supported/extra vertical data, and the remaining weighted/additional-log smooth invariants remain open |"
text = re.sub(r"^\| D\.2 \|.*$", lambda _: newrow, text, flags=re.M)
path.write_text(text)
print(json.dumps({"updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  "minimal_patterns_classified": 162,
                  "remaining_prompt_items": ["D.2"],
                  "current_remaining_example": "OS45 P2G,Q8G,weight2 atI8,allMumford,e1"}, indent=2))

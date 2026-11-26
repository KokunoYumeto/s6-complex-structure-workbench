#!/usr/bin/env python3
"""Exact relocation of published comparison scopes into Programs; no source writes."""
import csv
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / "agents/continuation9_global_sweep"
SOURCE = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text(encoding="utf-8")
ROWS = [
    ("primitive-finite-bounds",
     "& Primitive fixed finite caps in the bounds of the cited calculation remark: $150059$ affine-power tests and $305/99/55$ comparison totals.",
     r"& All $68$ primitive-fixed positions, $1\leq k\leq6$ and every $(n,r)\bmod m$: $150059$ affine-power tests; $305$ full-matrix comparisons, including $99$ torsion-cap and $55$ zero-Euler cases.",
     "Restores in the Programs entry the exact finite scope formerly printed in Q123. The 68 positions, k range, all residue pairs and four counts are copied from the original remark; no new calculation is claimed."),
    ("general-finite-bounds",
     "& The stated finite-lattice range and five-clutch inputs: $34/38675/175/35/725$ totals.",
     r"& The $34$ additional lattice bases, $1\leq k\leq6$ and every residue pair: $38675$ affine-power tests; $175$ full normal/graph matrices, including $35$ torsion-cap cases; $725$ one-site Smith forms at five integer clutch values.",
     "The original Q125 specifies the 34 bases, k range, all residue pairs, 38675 tests, 175 matrices, 35 torsion instances and 725 one-site Smith forms at five clutch values. These exact meanings now remain in the Programs table rather than an unexplained slash-separated tally referring to the rewritten remark."),
    ("multiplicative-comparison-scope",
     "& The $120$ local multiplicative normal forms, with the type subtotals and $213/18/172$ comparison scope of the cited remark.",
     "& The $120$ local multiplicative normal forms, with the type subtotals in the cited remark; $213$ Smith comparisons, including $18$ torsion-cap and $172$ zero-Euler cases.",
     "The mathematical type subtotals remain in Q132. Its former program-comparison counts are retained here with their original meanings instead of a backward reference to removed test-run narration."),
    ("odd-weighted-local-bounds",
     "& The $2334$ exterior and $586$ shared-factor cases, $12249$ saturated kernels, $4265$ basis maps, $2334$ cusp-disc maps, $1386$ lattices, $33264$ finite actions/proper powers and $126/1152$ denominator/orbit cases.",
     r"& Allowed odd-common-factor weights among $1,\allowbreak2,\allowbreak3,\allowbreak5,\allowbreak7,\allowbreak9,\allowbreak15,\allowbreak21,\allowbreak25,\allowbreak35,\allowbreak45,\allowbreak105,\allowbreak315,\allowbreak1001$: $2334$ exterior and $586$ shared-factor cases, $12249$ saturated kernels, $4265$ basis maps, $2334$ cusp-disc maps, $1386$ lattices, $33264$ finite actions/proper powers and $126/1152$ denominator/orbit cases.",
     "The exact weight list from original Q139 is attached to the local/exterior program whose WEIGHTS tuple is that same list. All existing table counts remain unchanged. This records the finite comparison domain and grants no new verification credit."),
    ("odd-weighted-global-bounds",
     "& The $495/459$ patterns, $4950$ family matrices, $1376$ extra-regular matrices, $24$ reversible Smith equivalences and $112$ fibre-torsion comparisons.",
     "& The $495/459$ patterns and $6326$ complete global matrices: $4950$ on the two Euler values and $1376$ with two additional full-vector regular logarithms; $24$ reversible Smith equivalences and $112$ fibre-torsion comparisons.",
     "Original Q139 splits its 6326 complete global matrices into 4950 on the two Euler values and 1376 with two added full-vector regular logarithms. These exact scopes are retained in the associated global Programs entry; 4950+1376=6326. The existing 24 equivalences and 112 comparisons remain unchanged."),
]

now = datetime.now(timezone.utc).isoformat()
proposals, defects = [], []
candidate = SOURCE
for i, (name, old, new, reason) in enumerate(ROWS, 1):
    assert SOURCE.count(old) == 1 and candidate.count(old) == 1, name
    pos = SOURCE.index(old)
    assert pos > SOURCE.index(r"\section{Programs}"), name
    cid = f"CLAUDE-III-P14-PROGRAMS-{i:03d}"
    proposals.append(dict(change_id=cid, name=name, finding="P14", statement_id="programs",
                          unit_id="programs", formal_owner=None,
                          source_line=SOURCE.count("\n", 0, pos)+1,
                          old=old, new=new, interpretation=reason))
    candidate = candidate.replace(old, new, 1)
    defects.append(dict(change_id=cid, type="D09", statement_id="programs",
        old_location="Paper III Programs table; " + name, old_page="current regrouped source",
        new_location="same program row", new_page="pending rendered table review",
        old_text=old, new_text=new, reason=reason,
        review_status="Exact program-row scope relocation read " + now + "; proposed; no formal-result event or independent-check credit."))
    print(cid, name)
restored = candidate
for p in reversed(proposals):
    assert restored.count(p["new"]) == 1
    restored = restored.replace(p["new"], p["old"], 1)
assert restored == SOURCE
OWN.mkdir(parents=True, exist_ok=True)
(OWN / "S6_SERIES_PUBLISH_c9_program_scope_proposals.json").write_text(json.dumps(proposals, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
fields = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
with (OWN / "S6_SERIES_PUBLISH_c9_program_scope_defects.tsv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader(); writer.writerows(defects)
print("Prepared five exact Programs rows; no formal-result events; exact reverse comparison passes.")

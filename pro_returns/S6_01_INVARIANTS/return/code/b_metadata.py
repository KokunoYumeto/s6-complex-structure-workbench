#!/usr/bin/env python3
"""Create the statement ledger for the independently written Part B."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = [
    ("B1.0", "The marked lattice, theta-line-bundle and contracting-scale dictionary, including reversed meridians and the reference-scale ambiguity.", "B.1", "F4", "A2.3", "The compatible scale is u=exp(-2 pi i c); an independently chosen reference multiplies it by an unspecified nonzero constant."),
    ("B1.1", "The relative O and logarithmic-cotangent direct images and their cup maps are unchanged by admissible translation twists and multiplicities (3k,4l).", "B.1;B.2;B.3", "F1;F26", "A1.0;A1.1;A1.2", "Comparison is equality of invariant extensions on the common smooth family; finite nonreduced layers and the cusp are retained."),
    ("B1.2", "All admissible one-component-cusp logarithmic transforms have the six cotangent direct images and Hodge diamond of Part A.", "B.1;B.2;B.3", "F1;F26", "B1.1;A1.3;A2.1;A2.4", "Includes all (3,4) twists with |p|=1 and finite-fundamental-group members themselves."),
    ("B2.1", "For coprime multiplicities (3k,4l), K=f*O(-1) O((k-1)S1+(3l-1)S2), h0q=(1,1,0,0), hp0=0 for p>0, and (h11,h12)=(2,1).", "B.2", "F1;F26", "B1.1;B1.2", "The invariant relative determinant has exponents 2k and l; its evaluation vanishes to orders k-1 and 3l-1."),
    ("B2.2", "The full anticanonical ring is the degree-d Veronese of C[x,y], deg(x,y)=(4l,3k), d=4l+3k-kl; the floor formula and all requested small pairs are computed.", "B.2;B.3", "F17;F26", "B2.1", "If d<0 only degree zero survives; d=0 is impossible under coprimality. Exact monomial and floor computations agree."),
    ("B3.1", "The cyclic universal cover of degree n has connected fibres, n cusp normalization components, and unchanged O and logarithmic-relative cohomology bundles.", "B.3", "F26", "B1.1;A1.2", "The cusp dual complex is an actual connected index-n covering of the original torus, proved by etale pullback of strata."),
    ("B3.2", "On the degree-n universal cover R1 Omega1 and R2 Omega2 acquire C_(p0)^(n-1); h11=h22=n+1 and h12=h21=1.", "B.3", "F1;F26", "B3.1;A1.3", "Derived duality, including Ext1 of the residue skyscraper, is used rather than dualizing torsion naively."),
    ("B3.3", "The cover has K=O(-2S2), anticanonical ring C[U,V] with weights (1,2), Betti numbers (1,0,n-1,0,n-1,0,1), and Frolicher degeneration at E2.", "B.3", "F17;F26", "B2.2;B3.1;B3.2;C1.1", "Rational topology is independently proved by explicit Mayer-Vietoris matrices and cusp attachment cycles. Each nontrivial deck character contributes one Dolbeault class in each of bidegrees (1,1),(2,2).")
]
rows = [dict(id=i, statement=s, status="Proved", where_proved=f"fragments/part_B.tex, Statement {i}", depends_on=deps,
             item_of_the_prompt=item, findings_of_the_survey_settled=survey, notes=note)
        for i,s,item,survey,deps,note in data]
(ROOT / "outputs/part_B_statements.json").write_text(json.dumps(rows, indent=2)+"\n", encoding="utf-8")
print(f"Recorded {len(rows)} Part B statements.")

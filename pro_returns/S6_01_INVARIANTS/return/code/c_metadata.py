#!/usr/bin/env python3
"""Write the numbered Part C result ledger and provenance notes."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[
('C1.1','The Frolicher sequence has E1 != E2 = Einfinity and ranks (1,h;h,1).','Proved','A: one-parameter Hodge table; sphere topology','C.1','F7','Does not determine h.'),
('C1.2','Complete algebraic bases for all d1 maps, with geometric g,q,gq,q^2 choice for X.','Proved','C1.1;A1.3;A3.1;A3.2','C.1;A.3','F7','Part A supplies h=1 and the actual Leray extension of eta.'),
('C2.1','BC and A dimensions computed from kernels/images via dots, arrows, squares, as functions of h.','Proved','C1.1;Stelzig2021 Theorem 3','C.2','F7','Independent of McHugh formulas. Exact matrix and counting computations agree for h=0,...,5.'),
('C2.2','Specialized McHugh and Angella formulas agree with the direct double-complex calculation.','Proved','C2.1;McHugh2018;Angella2018','C.2','F7','No misprint was found in the particular formulas used, not an audit of every formula.'),
('C3.1','Picard Chern-class map z -> zA + conjugate(z)B; Green-operator global G.','Proved','C1.1;C2.1;sphere topology;fibration','C.3','F7','Map is real linear, injective, onto real BC11. Operator formula does not give local coefficients.'),
('C3.2','With AC clockwise collars exp(12 g_gamma)=f*O(-p); standard p=-1 gives the positive factor12.','Proved','C3.1;AC26 Proposition7.27 boundary lift data;local specialization','C.3','F7','Curvature and Stokes fix the sign. Local integral extension lattice is lcm(3,4) Z gamma.'),
('C3.3','Positive-degree Bott-Chern ideal has square zero for every h.','Proved','C1.1;C2.1;C3.1;Serre duality','C.3','F7','No distinguished global Q or h=1 is required.'),
('C3.4','Delta=(0,2,2+2h,4h,2+2h,2,0); degreewise comparison and weaker d-exact lemma distinguished.','Proved','C2.1','C.3','F7','For h>=1 full comparisons hold only in degrees0,6; BC injectivity also holds in degree1.'),
('C3.5','No balanced, strongly Gauduchon, Kahler, locally conformally Kahler, or Hermitian-symplectic metric.','Proved','sphere topology;fibration','C.3','F7','Exact positive pullback paired against closed positive four-form.'),
('C3.6','Gauduchon metric exists with Chern-Ricci form pi f*omega_FS in any fixed Gauduchon A22 class; no Chern-Ricci-flat metric.','Known','canonical bundle formula;C3.1;Gauduchon1985 Theorem2;STW2017 Theorem1.3','C.3','F7','Reduction from K^2=f*O(-1) included, normalization of Ricci fixed.'),
('C3.7','No SKT or astheno-Kahler metric on X.','Proved','C2.1;A3.1;A3.2;explicit period rows','C.3','F7','The hypotheses are discharged by Part A. Fibre integral eta^2=-12 and torus averaging give contradiction.'),
('C3.8','Operator formulas for global G and Q; finite local coefficient atlas not evaluated.','Open','C3.1;C3.2;C3.7;A3.2','C.3','F7','The cohomology restriction map is settled. Uncomputed: coefficient functions of the Green/harmonic representatives for a specified global metric; no numerical elliptic solve was run.')]
records=[]
for id,statement,status,depends,item,findings,notes in rows:
    records.append(dict(id=id,statement=statement,status=status,
        where_proved='fragments/part_C.tex, Statement '+id,
        depends_on=depends,item_of_the_prompt=item,
        findings_of_the_survey_settled=findings,notes=notes))
(root/'outputs/part_C_statements.json').write_text(json.dumps(records,indent=2)+'\n')
print('Wrote',len(records),'numbered Part C records.')


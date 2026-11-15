"""Synchronize Part E statement metadata; the proof files remain authoritative."""
from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
path=root/'records/E_results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f)
    fields=reader.fieldnames
    rows=list(reader)
byid={r['id']:r for r in rows}
byid['E2']['notes']='Graph proof includes full nonreduced fibres. E17 also proves the pencil-specific exceptional higher-image vanishing in the printed resolution argument.'
byid['E7']['notes']='Answers comb section 10(1) fibration retention. E9,E11,E13-E15 compute all specified Kuranishi germs; E16 computes the rank divisors.'
byid['E8']['notes']='Square formula uses wp(P)=0; determinant is -g2^2/(36 pi^2 g3). E16 treats other families and E18 refutes the universal square identity.'
byid['E11']['depends_on']='E7; E9 root comparison; E19 for b2=0 of affine twists'
byid['E11']['notes']='h(T)=(1,1,1,0). The original affine-twist cohomology follows directly from acyclic root lines; higher-multiplicity sphere members use chi(T)=1.'
byid['E13']['notes']='Exact residue determinant b(e2-e1)/((e1+mu)(e2+mu)); source and target identifications checked at all special fibres.'
new=[
 ('E16','Exact Kodaira-Spencer rank divisors in every specified family','Proved','sections/part_E_rank.tex','E8; E13-E15','E.4(iv); Lead 9','F19','Comb divisor y^2 P_sigma(x^4,y^3), with degree(P_sigma)=4m and explicit Gauss-Manin Wronskian.'),
 ('E17','CDP98 Proposition 1.1 requires an embedded-component correction; the pencil-specific CDP20 higher-image step is valid','Refuted','sections/part_E17_audit.tex','E2','E.2; E.3','','Square-zero P1 example; all twisting cohomology computed. Exact stable-section replacement and pulled-back Euler proof of the pencil divisor comparison.'),
 ('E18','Universal square theta identity for arbitrary elliptic sections and linearizations is false','Refuted','sections/part_E18_theta_counterexample.tex','E8; E5','E.4(iv); Lead 9','F19','Explicit local proper torus family with mu=1/2 has nonzero determinant while the square vanishes. Full fibre and direct-image cohomology computed; two numerical methods at 70 digits.'),
 ('E19','All original admissible affine twists have explicit integral homology and rational homology of S6','Proved','sections/part_E19_topology.tex','Exact marking; primary logarithmic-filling gluing calculation','E.1; E.3; E.4 applications; Lead 7','','pi1=Z/|p|; integral H1,H2,H3,H4=Z/|p|; H5=0. Exact gluing determinant -p and Smith form diag(1,1,1,|p|).')
]
for vals in new:
    byid[vals[0]]=dict(zip(fields,vals))
rows=[byid[k] for k in sorted(byid,key=lambda x:int(x[1:]))]
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('Part E statement rows:',len(rows))
print(', '.join(r['id'] for r in rows))

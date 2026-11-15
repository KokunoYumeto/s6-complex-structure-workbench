"""Record the audited cusp-product example and current source/visual checks."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
p=root/'records/root_results.csv'
with p.open(newline='') as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
new={
 'id':'C.2.UN.8',
 'statement':'A compact projective torus fibration has six simply connected irreducible rational-normalized fibres of Euler number six; their integral cohomology and ambient rational Betti numbers are computed',
 'status':'Proved',
 'where_proved':'sections/part_C2_cusp_product.tex',
 'depends_on':'Explicit graph blowups; quotient cofibration; adjunction; Picard restriction; Rossi2017 Proposition 4 and Remark 5',
 'item_of_the_prompt':'C.2',
 'findings_of_the_survey_settled (F-numbers)':'F16',
 'notes':'Known Namikawa cuspidal self-product, compared explicitly with Rossi; complete independent coordinate and cohomology derivation. Refutes extension of the nonzero local-character premise beyond CDP hypotheses. Root and two independent audits accepted.'}
rows=[r for r in rows if r['id']!=new['id']]+[new]
with p.open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=fields); wr.writeheader(); wr.writerows(rows)
qa=root/'records/visual_qa.md'
with qa.open('a') as f:
    f.write('''
## 17:57 UTC build and subsequent inspection

The build recorded in `build/root_build_1803.out` compiled 157 statements into 224 pages. All four stages exited zero, with zero TeX errors, unresolved references, overfull boxes and missing glyphs. The renderer saved distributed and newly targeted page images. The root visually inspected pages 86, 107, 110, 112 and 142 in this version. The mixed-Hodge comparisons, global Euler statement and new unrestricted-fillings passages fit their margins without clipping or overlap. Mathematical additions UN5–10 require another build and inspection before checkpoint 06.
''')
record=root/'records/root_research_1822.md'
record.write_text('''# Root research and proof audit, 15 November 2026, 18:22 UTC

## Unrestricted normal supports, UN5

Read D's full proof. A normal hypersurface surface support has isolated singularities, whose morsification produces an actual embedded negative-square vanishing sphere in a nearby level. Inclusion into the actual torus preserves its square but kills its homotopy class. Normal supports are therefore smooth. The normalized cyclic base change is finite étale over the smooth tube, has connected torus central fibre by the Stein-factor comparison, and its free cyclic quotient gives exactly tori and bielliptic supports. The affine action, multiplicity restrictions and compact realizations are explicit. Accepted.

## Properly elliptic components and the source error, UN6

Read E's full construction and A's independent audit. The local free quotient `(z,[w]) -> (zeta z,[zeta w])`, with `x=z^m`, gives a smooth total space and the actual full fibre P_m + mQ_m. The plurigenus calculation, integral H1, noncontractibility and base-change comparison are explicit. Accepted. Read Fujimoto's 1988 primary scan definitions on pages 91–92, Theorem 2.8 on page 96 and Example 3.4 on page 99. The printed theorem's connected-root-cover claim fails for the displayed weighted Hopf map `[a,b,c] -> [a^m:b:c]`: its target line has square 1 and simply connected complement, while its inverse image is multiple of order m. The normalization of the proposed root cover is the disjoint union of the graphs xi=zeta s_E. The definitions impose neither a multisection nor a Kähler hypothesis. The exact counterexample is recorded in UN6; Example 3.4 already contains the occurrence of properly elliptic components. No priority is claimed.

## Cuspidal product, UN8

Completed the explicit projective example and ran `root_cusp_product.py`. E and D independently checked the charts, exceptional chain, quotient cofibration, canonical extension, fundamental group, divisor restriction kernels, Mordell–Weil ranks and intersection matrix. Both accepted. E requested the exact sextic base-change comparison for the generic Néron–Severi upper bound; added it. Removed the infinity-coefficient typo and split the first display before compilation. Read Rossi, arXiv:1211.6329v3, Proposition 4 and Remark 5: the compact construction and ambient Hodge numbers are known and match the proof here. Added the verified reference and explicit comparison. Fibre integral groups are (Z,0,Z^4,0,Z); ambient rational Betti numbers are (1,0,21,8,21,0,1). A small tube has trivial fundamental group, so the nonzero local character used under CDP assumptions cannot be extended to all irreducible torus degenerations.

## Generic-node transport, UN9–10

Read D's full proof, including the exact quadratic perturbation, rank-one Morse coordinate and boundary transport. E independently accepted that argument. The pinch spherical class has square -4, not -2, by the original A5.15 formula. It is represented by a continuous S2 map; embeddedness is not used. D corrected CR4 and its metadata accordingly. The original isolated Morse class used in UN5 remains an embedded square -2 sphere. These are the exact numerical and representability corrections.

## New main-question progress

A and D isolated the strict-transform term in A'Campo's trace formula: for an irreducible full fibre mS, every exceptional multiplicity in an embedded resolution is at least 2m, so L(T^m)=m e(S_reg). On torus cohomology L(T^m)=det(I-T_1^m). The nearby-cycle SNC calculation makes monodromy quasi-unipotent without an ambient Kähler assumption, and conjugate root-of-unity eigenpairs make this determinant nonnegative. E independently checked this chain. A is writing UN7 and the consequences for rational normalizations and contracted irrational sections; these consequences will be recorded as proved only after their exact conductor and local-character arguments are written and audited. This directly advances the remaining unrestricted zero-Euler classification.
''')
print('Recorded UN8 catalog row, verified-source comparisons and prior visual inspection.')

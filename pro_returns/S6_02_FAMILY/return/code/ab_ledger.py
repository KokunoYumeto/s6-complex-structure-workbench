"""Write the A/B statement ledger from explicit audited entries."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
entries=[
('A.1.1','Canonical bundle O(-2S2), all direct images, graded anticanonical ring, intrinsic fibration and special fibre distinctions','Proved','','A.1','F17','Includes all integer k and all affine/cusp translations.'),
('A.1.2','Normalized finite base changes and explicit product covers of degrees 9 and 8','Proved','','A.1','F22','Free affine action; exact cover/normalization maps; saturated lattices.'),
('A.2.1','Rational centralizer, exact deck lift, norm quotient groups and necessary even shift','Proved','A.1.1;A.1.2','A.2','F2;F22','Exact integer computations and independent HNF checks in ab_exact.py.'),
('A.3.1','Every even shift extends globally with coherent group law and proper punctured-w-disc family','Proved','A.2.1','A.3','F2','Finite and cusp maps, all strata, all collars, V and H1(V)=0 proved.'),
('A.4.1','Exact Albanese curves and j-functions; generic Albanese-only classification necessity','Proved','A.1.2;C.1 interval certificate','A.4','F2;F22','Countable exceptional set explicitly defined by pairs of modular equations; nonreal modulus difference certified by cd_special_intervals.py.'),
('A.4.2','Nonzero Kodaira-Spencer class at every admissible parameter with explicit torus representative','Proved','A.1.1;A.3.1','A.4','F12','First-order canonical-pencil transfer includes nonreduced critical schemes.'),
('A.4.3','Precise transfer and scope of Viaclovsky and Yang methods','Proved','A.1.1;A.2.1;A.3.1;A.4.2','A.4','F2;F12','Read VL26 Proposition4.7 and Y26 Lemmas6.6-6.9/Proposition6.15; explicit matrix substitutions and z->z^2 comparison.'),
('A.5.1','Complete fixed-data classification Xc~Xcprime iff cprime-c in 2Z','Proved','A.1.1;A.2.1;A.3.1;A.4.2','A.5','F2','All actual construction hypotheses specified; local miniversality is proved separately in A.5.2.'),
('A.5.2','Tangent cohomology (1,1,1,0); smooth reduced Kuranishi disc and miniversality at every parameter','Proved','A.1.2;A.3.1;A.4.2;A.5.1','A.5','F8;F12','Independent root-curve, cusp-product, direct-image and normal-quotient derivation; exact checks in ab_deformation.py. DGKX26v1 Section6 audited, with historical omission from v2 stated.'),
('B.1.1','Typed line-bundle quotient with inverse-generator sign; pointed elliptic surface and MW=Z[mu]','Proved','A.3.1','B.1','F4;F5','Independent full logarithm cocycle derivation and rational-section extension; no use of wp-zero identification.'),
('B.1.2','Sharp parameter disc for all ordinary and normalized finite root tori','Proved','B.1.1;B.1.4','B.1','F4;F21','Boundary for ordinary fibres alone is explicitly distinguished; exact full compact-family condition.'),
('B.1.3','Original period section equals one signed visible x=0 section, hence wp_tau(mu)=0','Proved','B.1.1','B.1','F5','Full resolution/height projection, lower bound1/6, exact Cartan check; independent of Part C numerical zero construction.'),
('B.1.4','Global geometric linearization and exact lambda0=1 for period-reference normalization','Proved','B.1.1;B.1.3;C.1 cusp branch','B.1','F4;F5','Read E26 Lemma2.1 and Corollary2.2 with concrete reduction; all special-fibre orders retained.'),
('B.2.1','All (3,4) affine and cusp data classified by (|p|,exp(-pi i(c+k2)))','Proved','A.1.1;A.2.1;A.3.1','B.2','F3','Includes negative linear part, arbitrary cusp sections and unmarked maps; cusp necessity via generic-point toric valuation.'),
('B.2.2','Exactly two sphere classes at fixed u and their transposition under a positive u circuit','Proved','B.1.4;B.2.1','B.2','F3;F4','Explicit Engel integral map and local complex-period map; generator orientations fix shift signs.'),
('B.2.3','Global fixed-sphere-data descent over original u-disc in E26 Remark8.1 is false; corrected double-cover family','Refuted','A.2.1;A.3.1;A.4.1;B.2.1','B.2','F3;F4','Two independent obstructions: finite norm parity and non-even Albanese Laurent expansion. Proper local-u and global-w replacements proved.'),
('B.3.1','Coprime higher sphere multiplicities classified by explicit congruences; fixed-data step2klZ and2kl classes at fixed u','Proved','A.2.1;A.3.1;B.2.1','B.3','F26','All primitive translation vectors in Viaclovsky stipulated sphere family; exact repeated norm and CRT proofs.'),
('B.4.1','Full holomorphic automorphism group Aut(Xc)=C*','Proved','A.1.1;A.2.1;A.3.1;B.2.1','B.4','F29','Integral cocycle quotient is zero; exact determinant and HNF checks; extension of corrected lifts supplied.'),
('B.4.2','Conjugate Xc is X_(1-barc); real locus w=-barw and split full group C* semidirect C2','Proved','A.5.1;B.2.1;B.4.1','B.4','F29','Uses b0part=0; all affine reflection laws and cusp matrices exact; square killed after canonical normalization, action z->1/barz.')]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','findings_of_the_survey_settled (F-numbers)','notes']
with (root/'sections/AB_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(fields)
 for id,statement,status,deps,item,findings,notes in entries:
  w.writerow([id,statement,status,'sections/AB.tex; Statement '+id,deps,item,findings,notes])
print('A/B numbered statements:',len(entries))
print('Status counts:',{k:sum(e[2]==k for e in entries) for k in ['Proved','Refuted','Open']})
print('Prompt items:',','.join(sorted({e[4] for e in entries})))

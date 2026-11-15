"""Write the Part-D statement registry and final small annotations."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
rows=[
('D.1.1','j(Alb S2(w))=J(iw/216), with no meromorphic continuation through any point of |w|=216.','Proved','R1;R3;R7','D.1; Lead 8','R1;R3;R7;Lead8','Earlier-return natural-boundary proof rederived; normalization checked.'),
('D.1.2','A proper flat extension with an intrinsic double anticanonical surface divisor gives a smooth proper surface family and holomorphic Albanese invariant on an open base locus with at most countable complement.','Proved','Grauert1960 coherence and proper image;Buchdahl1999 Theorem11','D.1; Lead 8','R1;Lead8','Canonical base change proved over a smooth curve using the torsion in R1π_*L; does not use corrected Grauert §7 Satz2.'),
('D.1.3','No reduced proper flat complex-space extension through any boundary point exists, even under fibrewise biholomorphism alone.','Proved','D.1.1;D.1.2','D.1; Lead 8','R1;R3;R7;Lead8','Covers both versions requested.'),
('D.2.1','In h=mu-(1-tau)/2, the final period is (6h,a-3ih²+O(h⁴)), tau=i-(3pi i/2)h²+O(h⁴), and D=-3|h|²+O(|h|⁴).','Proved','R3 local theta coefficients','D.2;D.3;D.4; Lead 9','R1;R3;R9;Lead9','Exact symbolic coefficient arithmetic checked.'),
('D.2.2','Lead9 first-order characterization of total-space nonseparation is false: the vector n²(gamma+3u−3w)−6n w+3n delta at h=1/n tends to (0,-3i) when a=0.','Refuted','D.2.1','D.2; Lead 9','R9;Lead9','Actual analytic error O(n^-2), not merely a model counterexample.'),
('D.2.3','The fixed-boundary root-family Hausdorff reflection has central circle R/(Z/2+aZ) for rational a and a point for irrational a; exact nonseparation is specified.','Proved','D.2.1;D.3.1;Cornulier2011 Theorem3.1','D.2; Lead 9','R3;R9;Lead9','Distinguishes central-fibre Hausdorffization from total-family Hausdorffization.'),
('D.2.4','Order-four quotient retains circle or point central fibre, admits no compatible complex-space structure over the base, and moving-line leaf closures are determined.','Proved','D.2.3;R1','D.2; Lead 9','R1;R3;R9;Lead9','Includes properness and irrational intrinsic-leaf topology caveat.'),
('D.3.1','Every Chabauty limit is the annihilator of a graph of a homomorphism on a primitive subgroup K of the explicit lattice L_a; every pair (K,ell) occurs.','Proved','D.2.1;Cornulier2011 Theorem3.1','D.3','R3;R9','Ranks 0–3 for rational a and 0–2 for irrational a. Exact necessary-and-sufficient sequence criterion.'),
('D.3.2','Admissible paths can yield different limiting torus dimensions, so no path-independent local group limit exists.','Proved','D.3.1','D.3','R3;R9','Ordinary base points retain their nonsingular complex limits.'),
('D.4.1','For height H*+epsilon with epsilon small positive, the degeneracy set is one analytic Jordan curve with |t−1|=(pi⁴E4(i)/4)epsilon²(1+O(epsilon)).','Proved','D.2.1;R3 global maximum;E.4 certificate','D.4','R3','Local-in-height result explicitly stated; not asserted globally.'),
('D.4.2','For every supercritical height the exact modular-norm level equation, regular-manifold complement, compactness, and connected negative-sign region are determined.','Proved','R3;R9;minimum principle','D.4','R1;R3;R9','Does not classify every critical level or positive-sign component.'),
('D.4.3','At every rank-three point the period-group closure is A(Z4+V_k), giving Hausdorff quotient R×T^r with r=rank(Z4 intersect k-perp).','Proved','R9 linear algebra;elementary closed-subgroup duality','D.4','R9','Integral rationality and non-Hausdorff cases both included.'),
('D.4.4','On ordinary modulus charts, ∂tau D=i Z(3 Z wpprime−2g2)/(4pi² wpprime); critical points lie in the two explicitly stated factor-zero sets.','Proved','theta heat equation;Ramanujan identities;wp differential equation','D.4','R3','Exact derivation; independent 80-digit finite-difference check is supporting evidence only.'),
('D.4.5','At the equianharmonic point N=3^(1/4) exactly, so the t=0 crossing height is (3/2pi)log48.','Proved','Jacobi product;zero-mean Green distribution;degree-three endomorphism;R3 normalization','D.4','R3','Complete analytic multiplication proof; exact lattice and logarithm arithmetic in d_push_equianharmonic.py.'),
('D.4.6','Complete global supercritical level-set topology and all singular levels.','Open','D.4.1–D.4.5','D.4','R3','The equianharmonic crossing is now exact; global critical-factor analysis and complete level topology remain open.')]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','R_items_and_Leads_used','notes']
with (root/'sections/D_push_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for ident,statement,status,depends,item,rl,notes in rows:
  w.writerow(dict(id=ident,statement=statement,status=status,where_proved='sections/D_push.tex '+ident,depends_on=depends,item_of_the_prompt=item,R_items_and_Leads_used=rl,notes=notes))
print('Wrote',len(rows),'Part-D rows.')

# Independent D.2.50 audit

Status: **passed**. The full source `code/root_vertical_corrections_proof.tex` and revised executable `code/root_vertical_corrections.py` were independently read. No root-owned file was changed.

## Local integral geometry

The matrices retain both edges of I2/III, the actual multiplicity vectors of the starred fibres, and the marked component permutations from D.2.22. For every matrix J, its radical is the primitive whole-fibre vector and its rank is one less than the number of components. The finite permutation preserves J and this vector. The multidegree c=e_p-e_0 is literal section intersection, with both section components of multiplicity one. Pullback reverses the permutation, but its fixed subspace and full integral solution set are unchanged.

For I_n the quotient of degree-zero vectors by the cycle Laplacian has order n, detected by sum(i c_i). Translation by q has gcd(n,q) orbits, so the invariant multidegrees represent precisely (n/gcd(n,q))Z/n. This proves the condition n divides p*q. The finite starred and exceptional types are exhaustively checked, with explicit integer obstructions on all negative cases.

The ambiguity lemma is exact integrally: if J(sigma-I)z=0, then (sigma-I)z=h m with h integral because m is primitive. The finite norm annihilates the left side and equals the positive permutation order times h m on the right. Thus h=0. The complete ambiguity consists of actual invariant component orbit sums, not merely their rational span.

## Global line bundle and degree

A generic trivialization of J_D supplies a rational section whose divisor is vertical. Vanishing of all component degrees forces its local coefficient vector into the integral radical Zm. Hence J_D is genuinely pulled back from the base; no Picard-torsion or numerical-to-linear inference is omitted. Restriction to the zero section makes base pullback injective.

Choose h so that hQ is narrow everywhere. Translation by hQ fixes the literal correction divisor. The h-fold telescope therefore reduces to the already proved narrow-translation height formula, and gives h*degree(J_D)=h*ab/d0. This establishes the necessity of d0 dividing ab and the exact degree. The local Smith solutions construct a global correction for every permitted residue pair, proving sufficiency.

The punctured monodromy comparison also passes: the canonical trivialization of O(D) off the singular fibres telescopes in the h-fold contracting generator. Its long period is gamma_h=h gamma. Therefore S=diag(1,1,1,h) gives A_h=S^{-1} A S; the narrow case with weights h*w forces exactly D.GI2 for A. This asserts no cover of a filled cap.

## Independent execution

`code/fourfolds_vertical_correction_audit.py` writes only its own audit records. Exit0; output `records/fourfolds_vertical_correction_audit.out`. It checks all227 local pairs, including Smith unimodularity and literal solutions, all5696 profile residues, all82 actual elliptic monodromy/section cocycle orders against the recorded component groups, and all16 additional height-one section pairs. The actual generator residues are units and their component-group orders have lcm d0 in every profile. These finite periodic data prove the statement for every integer a,b.

## Additional simply connected initial data

A separate retained executable, `code/fourfolds_corrected_Mumford_examples.py`, uses only multiplicative Mumford caps and the proved punctured comparison. All16 cases pass: OS45/default with (a,b)=(2,4) or(4,2), one simple zero at any of the four I1 sites, and ordinary clutch e=+1 or-1. The exact unsaturated normal closure kills the entire vertical lattice; the remaining gamma generator is killed primitively, so the full fundamental group is trivial. H2=H3=Z4 in the first case and Z2 in the second, with no free middle groups and Euler2. The complete marked matrices are retained in `records/fourfolds_corrected_Mumford_examples.json`. No claim is made that new initial tuples necessarily yield new diffeomorphism types. The original corrected caps remain outside this calculation.

# P3F.34 source and arithmetic audit

## Result and precise source scope

The displayed homology formula agrees with its integral transfer matrix. The source theorem D.2.11 explicitly assumes gcd(n,3k)=1, both in `sections/manifolds.tex` at lines 2156–2186 and in the hypothesis column of the attached MAPS results CSV. Its short description says “general admissible n”; reading that phrase as every free cap drops a hypothesis that is present elsewhere in the same row. P3F.34 supplies the unrestricted free-cap extension. At gcd(n,3k)=1, g=gcd(3k,n,3d)=1, and the formulas literally coincide. The cap (m,n,d)=(9,3,1) has gcd(n,3k)=3 and g=3. The proposed wording records these exact inclusions and the exceptional term without assigning a false refutation to the scoped theorem.

## Exact arithmetic

The normal circle evaluates as (-n,-3d,3k) on the integral one-classes. Its primitive kernel is the rank-two lattice L. The dual transfer has columns (3d,-n,0) and (3k,0,n). The three two-by-two minors are 3kn,3dn,-n². Therefore its determinantal divisors are g and |n|g, giving Smith factors g,|n|. The kernel L is saturated in Z³: if av lies in the kernel for a nonzero integer a, then the integral normal evaluates to zero on v. Consequently computing torsion in the ambient lattice gives exactly the torsion in this rank-two kernel quotient, with only the extra ambient free direction removed.

In the free sector gcd(k,n,d)=1 and (3 does not divide n or 3 divides k), every prime other than three is excluded from g. A factor 3² in g would divide k,n,d after taking the displayed 3d and 3k entries, so g is 1 or 3. For n=0 the criterion forces 3|k and gcd(k,d)=1, whence g=3. The transfer then has image 3Z in the primitive kernel basis e_psi,(0,k,d); its cokernel is Z⊕Z/3. The additional free kernel in the pair sequence gives H2=Z²⊕Z/3. Duality and χ=2 give the printed remaining groups.

The fresh program `code/independent_V_III_checks.py` imports no earlier computational code. It checks every affine power for 7,650 triples (4,756 free, including 1,304 noncoprime free triples and 52 n=0 free triples), compares the criterion and determinantal divisors, and evaluates 427 direct SymPy Smith forms. It also independently checks the V common-root divisors and realification/Hodge-index substitutions. All 25,759 assertions passed. The program preserves the geometric boundary basis and pair sequence as inputs; its finite enumeration supports the general determinant argument and does not replace those geometric inputs.

## Literature comparison

AC26 original Theorems 7.17 and 7.22, printed pp.57 and 60, have the explicit (3,4) cap presentation with p=12l0−4l1−3l2 and gcd(p,12)=1. The receiving D.2.11 instead gives its exact relation to Xiufan Yang's Type C system: U=M_IV, V=U^-1 M_II U and

S = [[0,0,-1,0],[0,-1,1,1],[0,0,0,1],[-1,0,3,0]], det(S)=−1,

with U^(-t)S=ST1 and V^(-t)S=ST2 (`manifolds.tex` lines 2230–2281). The good-root section coordinate is (tau+1)/3, the point-line Picard coordinate is mu_C, and the translation coordinate is 3mu_C. This is an integral Hurwitz reorder and conjugacy of the actual open systems. The unchanged type-II filling is retained as an additional geometric choice.

Yang's attached `Compact_Complex_Threefolds_REPAIRED_v4_5.tex` Theorem 7.13 (source around lines 4070–4150; first-pass aux p.49) calculates the particular original Type B/C global families. The surrounding proof uses actual cusp sweep maps, unit-coefficient elimination, and two relations rx1=a_kappa x2 and (6−m1)x2=0. His general finite-cap presentation in Theorem 7.2 and prime-subgroup freeness criterion at source lines 4194–4210 are related known inputs. P3F.34 retains the same integral-saturation discipline and supplies the explicit changing normal circle and transfer for the component-supported OS49 exterior. The additional gcd factor has not been located in the opened core papers or the recorded searches.

Wang's attached `order_two_rational_homology_sphere_new.tex`, Theorem 1.1 (`intro:main`, lines 99–113), is a positively identified related construction: the genuine line O(P−O), lifted −6P translation, one cubic logarithmic cap, and three multiplicative completions produce simply connected H2=H3=Z/2. Its introduction explains the integral specialization and transgression coefficients (1,2,2,1). This is credited as related integral-torsion methodology; no equivalence of its marked completion with the present OS49 cap is asserted.

The attached E26 and both DGKX editions were compared at their finite-root and periodic-torus completion constructions. Search engine 1 queries on 2026-11-19 were `"OS49" "homology" "affine"`, `"IV" "II" "I_2" "complex threefold" "homology"`, and `"free affine" "cap" "3k" "homology"`. They returned Wang's related construction and broad unrelated results; no exact target formula was identified. This is a bounded search conclusion. It establishes neither worldwide absence nor absence of other mathematical relationships.

## Check type

The complete printed P3F.34 proof was read for its actual normal-circle map, integral q=eta h/3 boundary class, exterior restriction argument, pair sequence and source scope. The above determinant calculation and fresh executable are independent arithmetic checks performed after that reading, so they are not recorded as a before-reading independent re-proof of the complete theorem. The boundary restriction is fixed using the proved n=1 sphere fillings for every k,d; its projected cross-product W satisfies |kW1−dW2+W3|=1 for all k>0 and d, hence W1=W2=0 and W3=±1. This removes the possible unproved integral splitting in the computation. The remaining geometric inputs are P3F.26, P3F.29 and P3F.33, with their prior checks retained.

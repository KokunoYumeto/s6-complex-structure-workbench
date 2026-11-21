# Independent derivation: cdp:st:D.1.4 (tag01G2)

The target proof has not been opened. Inputs read are its packet and the exact supplemental S6_09 E4 statement. The latter supplies local freeness of E=R^1f_*O_Y and H^0(F_c,O_{F_c})=C for each full fibre. The following is the independent derivation of the claimed maps and rank.

Properness, connected fibres and normality of the smooth total space identify f_*O_Y with O_C by Stein factorization. In the Leray spectral sequence H^p(C,R^qf_*O_Y)⇒H^{p+q}(Y,O_Y), coherent cohomology on the curve vanishes for p≥2. The total-degree-one filtration is therefore the short exact sequence

0→H^1(C,O_C) --f^*→ H^1(Y,O_Y) --e→ H^0(C,E)→0.

Here e is the edge map obtained by restricting a cohomology class to the inverse images of base open sets. Further restriction to a fibre c evaluates this section in E⊗C(c), then applies the natural cohomological base-change homomorphism. Naturality of restriction of a Čech cocycle proves equality of that composite with H^1(Y,O_Y)→H^1(F_c,O_{F_c}). At a smooth fibre covered by the statement's base-change hypothesis the last map is an isomorphism, giving exactly its displayed three-factor expression.

For C=P^1 the asserted splitting E=direct-sum O(a_j) can be used summand by summand. A global section of O(a) is a homogeneous polynomial of degree a when a≥0; evaluation at any point is onto its one-dimensional fibre, because a linear form nonvanishing at that point raised to power a evaluates nontrivially. For a<0 there is no nonzero global section: a putative section would have an effective zero divisor of negative degree. Consequently the evaluation rank of E is exactly the number of nonnegative a_j, at every point of the base. Surjectivity of e identifies this with the rank of the restriction wherever base change is an isomorphism. In rank two the rank is two precisely when both degrees are nonnegative. These statements prove the exact equivalence claimed for CDP20's last splitting step.

There is no enumeration over a stored list of degrees: this is a proof for every integer a and every finite direct sum. The only maps and equalities used are the Leray edge, sheaf evaluation, base change, and the explicit evaluation of homogeneous polynomials.

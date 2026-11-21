# Independent recovery derivation: cdp:st:A.5.20, tag 01BB

Checker identity: ii_check_a_recovery_blind. The target proof and B's reconstruction/proposed block remain unopened. Read the original statement/input packet and supplement, then root's exact A.5.3 statement-only input `S6_SERIES_PUBLISH_II_01BB_resolution_conductor_inputs.tex`, SHA256 dc327be8fa7560c681198fed9fca6e88468ddbb830008c4975753e9e6220a4b0. A.5.3 supplies the canonical effective divisor on the minimal resolution, its nonexceptional conductor multiplicities, and the identity omega_Z(D)=h*omega_S. The target's initially given resolution pi is not assumed minimal. The following argument transports its actual maps to the minimal resolution explicitly.

The original data are f:Y to C0, the full fibre mS, eta:T to S, pi:Z to T, the irrational ruling p:Z to B, a noncontracted section C of p, and the resolution conductor 2C+V with V vertical. Every pi-exceptional curve is vertical. A section identifies C with B, so C is smooth with positive genus.

## The horizontal curve map and its normal direction

The map C to D=eta pi(C), with D reduced, is a proper nonconstant map of compact curves and hence finite. At a general point of D the surface germ is a product with the ordinary cusp x²-y³=0. Its normalization is (t,z) to (t³,t²,z), with exactly one branch over the singular curve and generic degree one there. Because the noncontracted horizontal conductor has multiplicity two and has only the component C, the generic degree of C to D is one. Thus this map is the normalization of D; its normal source is C and its geometric genus is positive.

Apply the supplied A.5.14 to the identical Y,S,D: the smooth general two-torus has trivial canonical line and b2(Y)=0 gives H2(Y,Q)=0. That input gives D smooth elliptic and the same cusp type at every point. The finite birational map C to the smooth curve D is an isomorphism, so C and B are elliptic as well. Apply the supplied C2d to the same now smooth D. Its explicit cusp normalization shows that T is smooth on a neighbourhood of its unique inverse-image curve C_T, that C_T to D is an isomorphism, and that deg N_(C_T/T)=0. My independent C2d derivation was frozen before any C2d proof was opened; no target proof has been used for this receiving application.

## Transport of the ruling and conductor to the minimal resolution

Let mu:Z' to T be the minimal resolution. A resolution of a normal surface dominates the minimal resolution by a sequence of point blowups; write pi=mu sigma with sigma:Z to Z'. Every curve contracted by sigma is pi-exceptional and hence p-vertical. Therefore p is constant on each sigma fibre and descends to a holomorphic map p':Z' to B. One direct construction takes the proper image of the graph (sigma,p) in Z' times B. Its projection to Z' is proper with a single point in each fibre, hence finite and bimeromorphic; normality of Z' identifies it with Z'. This gives p' with p=p' sigma. The section C maps to a section C' of p', because its parametrization by B composes with p' to the identity. In particular C' is smooth and sigma maps C isomorphically to C'.

The minimal resolution mu is an isomorphism over the smooth locus of T, including a neighbourhood of C_T. Thus C' is its inverse image and

    (C')² = deg N_(C_T/T) = 0.

Every mu-exceptional curve is also p'-vertical: its strict transform in Z is pi-exceptional, on which p is constant. The canonical effective divisor D' from A.5.3 has the same nonexceptional conductor as the given resolution, with the same scheme multiplicities. Its horizontal part is therefore exactly 2C'. Its remaining nonexceptional curves and its exceptional curves are vertical. Hence

    D'=2C'+V',  V' effective and vertical,
    K_(Z')+2C'+V' numerically equivalent to zero.

This effectiveness comes from the exact A.5.3 input on the minimal resolution; it is not an unstated assumption about the initially written V. The change of resolution is the explicit sigma above, and the conductor is transported by its nonexceptional components and their identical valuations.

## Removal of vertical components and blowups

Since Z' is an irrational ruled surface, contract its vertical (-1)-curves to a geometrically ruled surface rho:Z' to Z0 over B. The contractions are vertical because a rational curve maps constantly to the positive-genus curve B. Let C0=rho(C'); it remains a section. At each point blowup on the successive strict transform of that smooth section its square drops by one; at a point away from it the square is unchanged. Therefore

    C0²=(C')²+n=n>=0,

where n is the number of those section centres, counted through the sequence. Push the canonical/conductor equality to Z0. The canonical divisors and strict section push forward to K_Z0 and C0, and V0=rho_*V' is an effective vertical divisor, a nonnegative sum of full P1 fibres. Thus K_Z0+2C0+V0 is numerically trivial.

Adjunction on the elliptic section gives K_Z0.C0=-C0². Intersecting the preceding equality with C0 yields

    0=C0²+V0.C0=n+deg(V0).

Both summands are nonnegative, so n=0 and V0=0. No blowup centre in rho lies on the section, and every component of V' is rho-exceptional. Consequently C'=rho*C0, while the canonical divisor formula is K_Z'=rho*K_Z0+E_rho, where E_rho is effective and has positive coefficient on every exceptional prime divisor. The numerical equality becomes

    E_rho+V' numerically equivalent to zero.

The intersection form on the divisors exceptional for a sequence of point blowups is negative definite. This follows directly by induction: the total transform of each successive exceptional curve gives an orthogonal basis with square -1. A nonzero linear combination has square minus the sum of its squared coefficients. Hence a numerically trivial exceptional divisor is zero. Since E_rho and V' are effective, rho has no exceptional curves and V'=0. Thus Z' itself is the smooth minimal P1-bundle Z0 over the elliptic curve B, and its canonical conductor is exactly twice the section C'.

## The normalization has no exceptional resolution curve

Any irreducible vertical curve in this P1-bundle is a full fibre and has self-intersection zero. Such a curve cannot be exceptional for mu. Here is the exact analytic intersection argument, to avoid imposing algebraicity on T. For the exceptional fibre over a normal point, choose a nonzero holomorphic function g vanishing at that point. Its pulled-back divisor is G+sum m_i E_i, where m_i>0 and G is the strict transform of its zero curve. Pairing this principal divisor with each E_j gives sum m_i(E_i.E_j)=-G.E_j<=0. Some inequality is strict because the lifted zero curve meets the exceptional fibre by properness; the exceptional fibre is connected since a proper bimeromorphic map to a normal surface has connected fibres. Off-diagonal intersections are nonnegative. For the weighted symmetric matrix A_ij=m_i m_j(E_i.E_j), the identity

    x^T A x = sum_i (sum_j A_ij)x_i² - sum_(i<j) A_ij(x_i-x_j)²

is nonpositive and can vanish only when every x_i is zero: a strict row first forces one coordinate zero, and connectedness propagates it. Thus the exceptional intersection matrix is negative definite. This is the local-function form of Mumford's proof in §1, p.6, which I opened at the Numdam primary source `https://www.numdam.org/article/PMIHES_1961__9__5_0.pdf` (retrievals turn785225548view0–1). The use here is justified by the displayed local pullback divisor and matrix identity; no identification of the analytic germ with an unspecified algebraic germ is made.

In particular a vertical fibre with square zero cannot occur in the exceptional set. Therefore mu has no exceptional curves. It is a finite bimeromorphic map to the normal surface T and hence an isomorphism. This proves that T is smooth and minimal ruled over the same elliptic B. The original pi may include additional resolution blowups; no assertion that this original map is the identity is required or made.

## Euler number and the full conductor

On the smooth normalization T the conductor divisor is exactly 2C_T. There is no remaining vertical conductor by the preceding calculation. The canonical finite-duality description makes its conductor ideal an invertible ideal on T, so its support is precisely C_T. Equivalently the explicit cusp normalization near D and the canonical conductor identity show that eta is an isomorphism away from C_T. Over C_T it is the isomorphism C_T to D already established. Thus the finite proper map eta is bijective and is a homeomorphism of compact Hausdorff spaces. One may also apply Euler additivity to the same two strata:

    e(S)=e(T)-e(C_T)+e(D).

A P1-bundle over an elliptic curve has Euler number 2 times 0=0, and the two curves have Euler number zero. Hence e(S)=0. This proves every target conclusion, with initially singular T and nonminimal given resolution fully allowed through the explicit factorization above.

The fresh program `S6_SERIES_PUBLISH_II_A_recovery_blind_01BB_cells.py` computes the Euler numbers from sphere/circle tensor cell complexes and verifies the weighted-matrix quadratic identity coefficientwise. Its universal algebraic justification is given above. Input and computation hashes are appended before the freeze; the target proof remains unopened.

## Exact prefreeze bindings

Binding written 2026-11-21T20:19:04.100641+00:00, before target release.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01BB_statement_inputs.tex — SHA256 76dabaf2ec25aba4b5b97a7e1e126abcb79cc69df39db76355009e53178bd7f6.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_01BB_cited_input_supplement.tex — SHA256 06eec9f9f3ffdb84c35f413ecd8e31e608386acd20de5ad75d05c4c0632469c1.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_01BB_resolution_conductor_inputs.tex — SHA256 dc327be8fa7560c681198fed9fca6e88468ddbb830008c4975753e9e6220a4b0.
- code/S6_SERIES_PUBLISH_II_A_recovery_blind_01BB_cells.py — SHA256 4395e92c74bc3a2c7e753425b2141f7ad49553435f517d50c56cf14841f37f8d.
- code/S6_SERIES_PUBLISH_II_A_recovery_blind_01BB_cells.out — SHA256 6c94f26ba7a6499071683886b14fcea64e3f5fcdd11e6840a131311250684dae.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_blind_01BB_run.json — SHA256 da6df45516c5e05ccfad77ed3e61d7cd65f1392e31dafe248ffa0775701d10dc.

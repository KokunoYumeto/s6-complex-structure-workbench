# 02WU / night:P4.22: independent prerelease derivation

The target printed proof, outline and prior target programs remain unopened. This derivation uses its exact statement, safe cited inputs, the already independently checked A.5.14 and P4.20 conclusions, and the opened original Beauville monograph. The companion target 02YF is also still closed. The proof below does not rely on that target's asserted fundamental-group conclusion, but constructs the needed maps here.

## 1. Full conductor and the ruled minimal model

Let f:Y→B be the standing proper connected-fibre map from a smooth compact complex threefold with b1(Y)=b2(Y)=0 to a smooth compact curve, with smooth general fibre a complex two-torus. Let mS be the specified full fibre, with S irreducible, singular and reduced. Its normalization ν:T→S is smooth and birationally ruled over an elliptic curve E. Let D be the full divisorial conductor on T, R=D_red and C=Sing(S)_red.

The exact A.5.3 statement applies with the minimal resolution of the smooth normal space T equal to its identity: ω_T(D)=ν*ω_S. P4.12 makes the latter line torsion. Thus K_T+D is numerically zero. The normalization identifies T minus R with S_reg, and maps R finitely and surjectively to C. Every irreducible curve component of R has a nonconstant image because ν is finite.

Let q:T→T0 be the contraction to the minimal ruled model over E. Beauville III.10, p.40, proves that T0=P_E(V), a projective-line bundle. The proof extends the rational ruling to a morphism by resolving its base points; every exceptional rational curve has constant map to the positive-genus base, so the last base-point blowup can be removed. This is the exact map yielding the bundle structure. The local point-blowup and factorization maps are II.3, pp.17–18, II.7, pp.20–21 and II.11–12, pp.23–24. They apply to the compact analytic surface through the same local constructions; all numerical formulas below are transported through these maps.

Write r for the number of point blowups. Proposition III.18, pp.46–47, gives the basis h=c1(O_P(V)(1)), F a fibre, with h²=deg V, h·F=1, F²=0. Adjunction on F and a section gives K_T0=−2h+(deg V+2g(E)−2)F numerically. Since g(E)=1, K_T0²=0; the sphere bundle has e(T0)=2e(E)=0. Every point blowup has K_new=q*K_old+E_exc and E_exc²=−1, while Euler number increases by one. Therefore

e(T)=r,   K_T²=−r.

Put D0=q_*D. At each point blowup the numerical relation K+D=0 implies D_new=q*D_old−E_exc. Indeed the difference is an exceptional multiple, and its intersection with E_exc determines that coefficient. Thus the exceptional coefficient is μ−1, with μ the old conductor multiplicity at the centre. Effectivity forces every centre onto the conductor. This exact formula works for the possibly nontrivial torsion line K+D because its exceptional coefficient and degree are zero.

## 2. All horizontal possibilities on the elliptic ruled model

The intersection D0·F=2 leaves three possible horizontal divisors, plus vertical fibres V=Σa_jF_j:

1. two distinct coefficient-one sections H1+H2;
2. one coefficient-one irreducible bisection H;
3. one coefficient-two section 2H.

Each section maps with degree one to the smooth base E and is a smooth elliptic curve. In the first case adjunction gives 0=(K+H1)·H1=−H1·H2−Σa_j. Thus the sections are disjoint and V=0.

In the second case adjunction gives p_a(H)=1−Σa_j. The normalization of H maps with degree two to E, so Riemann–Hurwitz gives geometric genus at least one. Hence Σa_j=0, p_a(H)=1 and H is smooth elliptic; its degree-two map to E is unramified.

The third case is D0=2H+V. Its reduced support is the smooth elliptic section with rational ruling fibres attached at distinct points, each by one transverse intersection. Adjunction gives H²=−Σa_j. In particular R0 is connected and its inclusion into T0 induces the same fundamental-group map as the section H→T0. Since the bundle projection T0→E has simply connected fibre and is inverse to the section on π1, that inclusion is an isomorphism.

## 3. The differential identity in its exact finite-rank-drop scope

Here is the numerical step used below, proved directly without opening P4.15. For a smooth normalization T whose map to Y has rank two except at finitely many points, the differential gives an injective sheaf map T_T→ν*T_Y. The rank-one cokernel M is locally free away from the finite degeneracy scheme. It has depth at least one at the remaining smooth surface points by the length-one locally free resolution, so it has no zero-dimensional torsion; it has no divisorial torsion because rank is two generically on each divisor. Hence it is torsion-free.

Put L=M**=det(ν*T_Y)⊗det(T_T)^−1. Locally the map from the rank-three bundle to L is its signed maximal-minor row. The Hilbert–Burch exact sequence identifies its image with I_Z L, where I_Z is the maximal-minor ideal and Z has length ℓ. Therefore M=I_Z L. Since H²(Y;Q)=H⁴(Y;Q)=0, the first two Chern classes of ν*T_Y vanish. We have c1(L)=K_T and c2(I_Z L)=ℓ. Multiplicativity gives

0=c2(ν*T_Y)=e(T)−K_T²+ℓ,
so e(T)=K_T²−ℓ.

For the elliptic-ruled r-fold blowup this is r=−r−ℓ. Since r,ℓ≥0, it forces r=ℓ=0. In particular every such finite-rank-drop case is minimal and actually immersive everywhere. The exact line quotient, ideal and Chern product are constructed here rather than inferred from any unresolved sentence about a conductor's geometry.

## 4. The reduced cases are minimal and have Euler number zero

For either of the first two cases in Section 2, the conductor D0 is a disjoint union of smooth reduced elliptic curves. Every allowable blowup centre has μ=1 and adds no exceptional conductor; its strict transform remains smooth and reduced. Thus D itself remains reduced, with disjoint smooth elliptic support.

At a generic point of each component of C, take a transverse reduced plane curve with normalization B=⊕C{t_i}, conductor exponents c_i and delta invariant δ. The Gorenstein conductor duality gives Σc_i=2δ. It follows by applying Hom_A(−,A) to 0→A→B→B/A→0: Hom_A(B,A) is the conductor, B is maximal Cohen–Macaulay, and Ext1(B/A,A) is its length-δ local dual. Here every c_i=1, so the branch count k satisfies k=2δ, while δ≥k−1 from the residue constants. Hence k=2,δ=1, giving two smooth transverse branches.

Thus S is generically ordinary double outside a finite set. The independently checked P4.20 applies to the same ν:T→S and proves normal crossings everywhere. Its normalization sheets are coordinate-plane embeddings, so ν is immersive. Section 3 then gives r=0. The disjoint smooth conductor excludes ordinary triple points: each triple point would have an intersecting pair of conductor curves on each normalization sheet. Therefore C is smooth and D→C is a finite unramified degree-two map locally on each image component. Its components have genus one by Riemann–Hurwitz. Euler additivity gives

e(S)=e(T)−e(R)+e(C)=0.

This proves that the reduced cases contribute only minimal zero-Euler normalizations; it does not impose a normal-crossing hypothesis on other fibres.

## 5. Transport of the double-section conductor

Consider D0=2H+V. At a point of multiplicity μ≥2 the new exceptional P1 is in the conductor with coefficient μ−1. The restricted blowdown R_new→R_old collapses precisely this P1 and is a homeomorphism elsewhere. Compactness identifies R_old with that quotient. A compatible triangulation and van Kampen show that collapsing this connected simply connected subcomplex preserves π1. At a μ=1 point the reduced conductor is smooth and its strict transform maps isomorphically to it.

The initial reduced support has a nodal tree of rational fibres attached to H. A blowup at a smooth point either adds a rational leaf (μ≥2) or leaves this graph unchanged (μ=1). A blowup at a node inserts a rational vertex and subdivides its edge. Thus R remains the strict elliptic section with rational trees attached. The commuting square between the inclusion R→T and its blowdown R0→T0, together with the π1 isomorphisms for both blowdown maps, proves

π1(R)→π1(T) is an isomorphism.

The normalization pushout is the quotient T∪_R C. Triangulate the pair (T,R) and the finite curve map R→C; the inclusion is a cofibration and the mapping-cylinder pushout gives van Kampen. Because R is connected and its π1→π1(T) map is an isomorphism, the induced homomorphism from π1(C) is an isomorphism

π1(C) ≅ π1(S).

This argument allows rational components above distinct ruling fibres to have the same image in C. It depends only on the finite map R→C and not on a one-to-one correspondence of curve components.

## 6. The Euler number of the image curve

All rational components of R map to rationally normalized components of C. The elliptic section H maps to at most one additional component; Riemann–Hurwitz gives its normalization genus zero or one. The finite point-identification model of C gives a free product of the normalization surface groups and a free graph group F_b. P4R.1 makes this actual π1(C)=π1(S) virtually abelian.

If every normalized component is rational, this group is F_b and b≤1. Indeed every finite-index subgroup of F_b has rank 1+d(b−1), and a free group of rank at least two is nonabelian. For c components the exact incidence-cell formula is e(C)=c+1−b≥1.

If one component has elliptic normalization, the group is Z²*F_b. A positive b gives a surjection to F2 by retaining one generator from Z² and one from F_b. Quotients of virtually abelian groups are virtually abelian, whereas F2 is not by the same finite-index rank formula. Hence b=0 and e(C)=c−1≥0. Thus e(C)≥0 in every case, and its only zero case has one irreducible component with elliptic normalization and graph rank zero. Possible unibranch singularities do not change this topological calculation.

Together with P4.13 and T minus R≅S_reg,

e(S)=e(S_reg)+e(C)≥0.

If e(S)=0, then e(C)=0. A rational component of R cannot map nonconstantly to the elliptic normalization of this irreducible C, since its map from P1 factors through normalization and contradicts Riemann–Hurwitz. Therefore R has no rational component. This forces V=0 and no point blowups: a first blowup centred on the coefficient-two section has μ=2 and creates a rational conductor component, whose strict transform persists through every further blowup. Consequently T=T0 is minimal. This proves strict positivity whenever T is nonminimal.

## 7. Every minimal double-section case has Euler number zero

It remains to prove the converse direction of equality. Let T=T0 in the double-section case. If V has v distinct fibres, then e(R)=v because each rational fibre contributes 2−1 to the elliptic section. Since e(T)=0, P4.13 gives 0≤e(S_reg)=−v. Hence V=0 and D=2H, with H a smooth elliptic section.

Let k be the generic degree of H→C. The plane-curve conductor has k branches, each with exponent two. Thus 2k=2δ, or δ=k. The branch delta formula is δ=Σδ_i+Σ_(i<j) I_ij. Since I_ij≥1, it gives k(k−1)/2≤k and hence k≤3.

For k=1, δ=1 makes the transverse curve an ordinary cusp. The finite map H→C has generic degree one, so H is precisely the normalization of C; its genus is one. The independently checked A.5.14 applies to this conductor-image component in the same mS⊂Y, first giving its lci embedding and then the constant cusp-type conclusion via A.5.5. Therefore C is smooth elliptic and the finite birational map H→C is an isomorphism. Additivity yields e(S)=0.

For k=2, δ=2 forces both branches smooth: a singular branch has intrinsic δ at least one and meets another branch with intersection multiplicity at least two, already giving total δ≥3. The two smooth branches have intersection multiplicity two, so their normalization maps are immersive generically. For k=3, δ=3 forces all three branches smooth with all pairwise intersection multiplicities one; these maps are likewise immersive generically. Outside H the normalization is an isomorphism to S_reg. Thus for k=2 or 3 the rank-drop scheme of dν is supported on finitely many points. Section 3, with e(T)=K_T²=0, gives ℓ=0 and immersion everywhere.

At any point of C, every local normalization sheet now embeds as a smooth surface germ. On such a sheet the reduced conductor is the one smooth curve germ H. Any two distinct sheet germs meet in a curve contained in C, so every pairwise intersection on that sheet has the same reduced image germ. Pairwise equality propagates across the sheet germs and makes C smooth at the image point. There are at least two sheets at a singular image point; a single embedded sheet would make that point smooth on S. The restriction ν|H has injective derivative because ν is immersive, so H→C is finite and unramified. Riemann–Hurwitz gives genus(C)=1, and again e(S)=e(T)−e(H)+e(C)=0.

This completes both directions: e(S)≥0, and e(S)=0 exactly when T is minimal. No geometric conclusion is borrowed from the grammatically unresolved final sentence of P4.15.

## 8. Independent computation and its scope

The new shared program S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells.py was written while both target proofs were closed. It represents the weighted double section and vertical fibres by their actual incidence tree, performs the three local blowup operations with the coefficient μ−1, and contracts rational terminal vertices explicitly. It calculates the surface and conductor Euler numbers from those cells, multiplies the weighted total Chern polynomials, and records every possible virtually abelian image-curve Euler case used above.

For the transverse rings it provides explicit conductor-clearing polynomials. On the tacnode branches (x,y)=(t,0),(t,t²), the polynomials x^n−yx^(n−2) and yx^(n−2) give (t^n,0),(0,t^n) for n≥2. On the three lines (0,t),(t,0),(t,t), the polynomials y^(n−1)(y−x), x^(n−1)(x−y), xyx^(n−2) give the three separate order-n branch vectors. The constant and linear image constraints give delta two and three respectively. Each finite polynomial identity is checked by n+1 exact values with proved degree bound n. The all-order formulas are the displayed factorizations, not an inference from finitely many jet orders. For the cusp, every exponent ≥2 is 2a+3b, with the explicit parity formula; only exponent one is missing.

The first program output exposed a mutable-list snapshot error in the displayed weights of earlier stages. The original program, output and run receipt were preserved, the list copied at each stage, and the corrected program rerun before either freeze. A final field clarification records separate tacnode and triple conductor orders. The final run exited zero at 2026-11-21T21:43:47.234651+00:00. Every final output section and all 64 stage records were printed and read before this derivation was frozen. This is a finite exact implementation certificate accompanying the complete general arguments above.

## Exact input and computation bindings

The binding appendix is added by a separate hash-only step before freeze. No target proof has been opened at the time of writing this complete derivation.

Binding recorded 2026-11-21T21:46:28.398687+00:00.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WU_statement_inputs.tex — SHA256 c98174aaca798480d8d2948f87a2311562cc4765dd47b870e9a318705acebf58.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02WU_cited_input_supplement.tex — SHA256 78ea0a6700747ee8c1c8d032866f907a2b35f564a2b614cfee67d87ae038a197.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_WM_WS_safe_scope_01.json — SHA256 8070638508547ad0e9b1b5748f4562bd65c387c4161d55c8bc9f30b2c2fbc7c4.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_01BB_resolution_conductor_inputs.tex — SHA256 dc327be8fa7560c681198fed9fca6e88468ddbb830008c4975753e9e6220a4b0.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_Beauville_1978.pdf — SHA256 a2bdff071df610a8e39200a16ad7675149c1ddf601157b3e3e56cbf285994e4e.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_Beauville_1978_opened_scope_01.json — SHA256 0d2ea94f1a73cee925d69c09fa90003cee229c1d35871e79024ded0e59a2b245.
- agents/ii_checks_A/recovery_20261121T195642Z/group07_WT/S6_SERIES_PUBLISH_II_A_02WT_reading_precision.json — SHA256 5346326bee017ed8dfe21a3022202abf3f40943a81ffa54ac4d704566bb758a7.
- code/S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells.py — SHA256 33f8dad777fef0cc6129aa1f77136f4e4f7beed0068081a336a4041e34697a34.
- code/S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells.out — SHA256 56524f9f0c9ef4a320dc80d866cbf0753896f469bb681a87c7f08c4b38d38030.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells_run.json — SHA256 71299a19d52cc2382473390e4a39c863533589db7e73d4ec5e2d4a617f416063.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_WU_YF_first_attempt_correction.json — SHA256 66d380562fab0ecbba4856912cdbd17c7e4ac87187da5032b817cbadc6c13dd9.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WU_conductor_inputs.tex — SHA256 08e18c9021af072dadba89901d0881d0731dc5f24e95fda9201455acc5a931fe.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WU_conductor_inputs.json — SHA256 e4ba251f5365914fecbc3640db4e96c26505660603dc4bec07e511af5dcfa58f.
- agents/ii_checks_A/recovery_20261121T195642Z/clean_group01/S6_SERIES_PUBLISH_II_01B4_full_proposed.tex — SHA256 691f278b1de3a70f319800c05d415beb3276d21ce3866855fb9df1d1c279ae9c.
- agents/ii_checks_A/recovery_20261121T195642Z/group06_WS/S6_SERIES_PUBLISH_II_02WS_full_proposed.tex — SHA256 76f3f413533e05b5e975bc10aee247fbb97ebed68b126d64345bceb02047ba56.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02YF_cited_input_supplement.tex — SHA256 92c5c5e5b94ee6086601638af4cba782fac7b3298907c4fcbc27ac533fd2b7a8.

# Recovery prefreeze copy: 02WO

Original surviving derivation: agents/ii_checks_A/derivations/S6_SERIES_PUBLISH_II_A_02WO_derivation.md; SHA256 03a3f8bdc61d8f8950e7e57e8086684f93e30a21446b97c8a7e64654c569b63b. Current copy prepared 2026-11-21T20:35:24.651723+00:00.

# Independent derivation: 02WO / night:P4.17

The target proof and prior programs are unopened. Inputs are the exact statement and the P4.16 statement supplied with it. I derive the full affine fundamental group and integral intersection lattice, then the local exclusion, rather than assuming the calculation from that cited special case.

## 1. An explicit affine open cover and integral homology

Fix a≥2,n≥1 and let `M={x^a-z y^n=1}`. It is smooth: when y≠0 its z derivative is nonzero, and when y=0 the equation gives x^a=1 and its x derivative is nonzero. Let ζ_1,...,ζ_a be the distinct roots of 1, in circular order. The fibre y=0 consists of the disjoint affine lines L_i={x=ζ_i,y=0}. Let U_i be M with the other a-1 lines removed.

Each U_i is biholomorphic to C² with coordinates (y,u_i), by

    x=ζ_i+y^n u_i,
    z=sum from k=1 to a of binom(a,k) ζ_i^(a-k) y^(n(k-1)) u_i^k.

The inverse is `u_i=(x-ζ_i)/y^n` where y≠0. Near L_i it is the holomorphic function `z/P_i(x)`, where `P_i(x)=(x^a-1)/(x-ζ_i)` is a unit near x=ζ_i. These formulas agree by the defining equation, so this is a global inverse on U_i. Any two or more U_i intersect in the same open set V={y≠0}, which is C*×C in coordinates (y,x). The transition is `u_j=u_i+(ζ_i-ζ_j)y^-n`.

Starting with U_1 and adding U_2,...,U_a, each union is an open union along the connected V. Van Kampen makes every such union simply connected, since each U_i is simply connected and the map from π1(V) into either simply connected piece is zero. Thus π1(M)=0.

For homology, H1(V)=Z and all Hq(V) for q≥2 vanish. The Mayer–Vietoris sequence at the k-th addition gives

    0→H2(U_1∪...∪U_(k-1))→H2(U_1∪...∪U_k)→Z→0.

The first union has H2=0, so H2(M) is free of rank a-1. The same sequences give Hq(M)=0 for q≥3. The explicit spheres below map to the successive positive or negative generators of these Z quotients, fixing an integral basis rather than merely a full-rank sublattice.

## 2. Matching spheres in the degree-one surface

Write Q={x^a-vz=1}, and put P(x)=x^a-1. Choose the consecutive polygonal edges γ_i from ζ_i to ζ_(i+1), for 1≤i<a. Their interiors are disjoint and avoid all roots. Above each edge take

    x∈γ_i,   |v|=|z|=sqrt(|P(x)|),   v z=P(x).

This is a circle over the interior of the interval, collapsing at each endpoint, hence a sphere K_i. At an endpoint, in the surface coordinates (v,z), it is a smooth graph `z=c conjugate(v)+higher terms` with nonzero c, so the sphere is smoothly embedded. The parameterization `v=r(s)e^(iθ)`, `z=r(s)e^(i(arg P(γ_i(s))-θ))` shows directly that the two fibre terms of the standard Kähler form cancel; the base coordinate depends only on s. Thus K_i is Lagrangian. The complex structure identifies its normal bundle with its tangent bundle with the opposite Euler orientation, so K_i²=-2.

Nonconsecutive edges give disjoint spheres. Consecutive spheres meet only at their common root. Their graph tangent planes have distinct phase coefficients and intersect transversely. Choose the orientation of K_1, then orient each consecutive sphere so that the local intersection is +1. Thus the intersection matrix of `(K_1,...,K_(a-1))` has diagonal -2, adjacent entries +1 and other entries0. This is the negative of the A_(a-1) Cartan form, with this explicit basis and orientation convention.

## 3. Pullback by the exact finite map and the lattice basis

There is a finite proper holomorphic map

    p_n:M→Q,        (x,y,z)↦(x,v=y^n,z),

of degree n, branched along the disjoint lines {v=0,x=ζ_i}. The inverse image Σ_i of K_i is a smooth sphere. Over the open edge the phase of y gives one circle, and at either endpoint the local equation is a graph `z=c conjugate(y)^n+higher terms`; the graph is smooth with real parameter y. The map Σ_i→K_i is a cyclic degree-n cover branched at its two endpoints. Its normal map is an isomorphism onto the pullback normal bundle: at a branch endpoint the z direction gives an isomorphism on the normal quotients; elsewhere p_n is a local diffeomorphism. Thus the preimage sphere represents the pullback of the compactly supported Poincaré dual of K_i.

More explicitly, let α_i∈H_c²(Q;Z) be the dual of K_i. The dual of Σ_i is p_n*α_i. For all i,j the proper-degree integration formula gives

    Σ_i·Σ_j = integral_M p_n*(α_i cup α_j)
             = n integral_Q α_i cup α_j
             = n(K_i·K_j).

This computes the same actual compact cycles, including the adjacent intersections at branch points. Their Gram form is therefore `A_(a-1)(-n)`, with diagonal -2n and adjacent entries n.

To prove these classes are an integral basis, use the open cover from §1. The sphere Σ_i lies in U_i∪U_(i+1). Cutting it along an interior matching circle gives its Mayer–Vietoris boundary in H1(V). The coordinate y traverses that circle once, so this boundary is a generator of H1(V)=Z. At the successive union of U_1,...,U_k, the class Σ_(k-1) therefore maps to a generator of the new Z quotient. Induction proves that all Σ_i form an integral basis of H2(M). This rules out a hidden finite index in the asserted lattice.

The determinant of the negative Cartan form is `(-1)^(a-1) a`. Indeed the determinant of its positive form in rank r obeys D_r=2D_(r-1)-D_(r-2), D_0=1,D_1=2, hence D_r=r+1. Scaling by n gives `(-1)^(a-1) a n^(a-1)`, which is nonzero. Each basis sphere already has the nonzero square -2n.

## 4. Exclusion in every common multiplicity

The polynomial `g=x^a-zy^n` has positive weights `(n+1,a,a)` and degree D=a(n+1). A local fibre equation with common multiplicity m is `F=u g^m`. A holomorphic root `lambda=u^(1/(mD))` gives the local biholomorphism `phi(x_j)=lambda(x)^(w_j)x_j`; its derivative is invertible and `(g∘phi)^m=F`. Thus the unit is absorbed by this exact coordinate map.

Weighted scaling by a small positive ε sends g=1 to g=ε^D and shrinks every chosen compact sphere and normal neighbourhood into the coordinate ball. Composition with phi^-1 puts that sphere in the actual nearby torus fibre F=ε^(mD), preserving its square -2n. The universal cover C² of a complex two-torus makes its π2 zero. The embedded spherical class becomes zero in global H2, whereas extension of its compactly supported dual preserves the nonzero intersection number. This contradiction excludes the germ for every a,n,m. This argument is the same actual map used for the a=2 special case, now with the complete integral lattice proved.

## 5. The named cyclic and singular-normalization cases

For a=n=3 the central germ is `x³-zy³=0`. Its normalization is the explicit finite birational map `(y,t)↦(yt,y,t³)`: t is integral because t³=z and belongs to the original meromorphic field as x/y. The conductor curve y=0 maps by t↦t³, realizing the stated order-three cyclic ramification.

The assertion includes genuinely singular normalizations. For example a=4,n=2 gives `x⁴-zy²=0`. Adjoin u=x²/y, which satisfies u²=z. The normalization is the finite birational map

    {v²=u w}→{x⁴=zy²},       (u,v,w)↦(x=v,y=w,z=u²).

Its source is normal by the S2 property of a hypersurface and regularity in codimension1; its only singular point is the origin. It is therefore the normalization and is singular there. This proves the stated coverage through an explicit finite morphism.


## Current recovery computation and primary inputs

This is a new prefreeze recovery copy. The surviving earlier derivation remains unchanged at its original path. Its historical 19:48 program and receipt were lost in the execution reset; no claim is made that those bytes were restored. The new program below was independently written from these statement equations and these already-derived maps before any target proof or historical target routine was opened. The current run and its output replace the unavailable historical computational evidence.

The fresh program uses sparse arithmetic in Z[zeta,y,u]/(zeta^a-1) for the affine charts; signed matching enumeration of every deleted-row incidence minor and Cauchy–Binet for the lattice determinant; exact deck permutations with the invariant i+j modulo gcd(b,c); first-order dual algebra and degree-bounded interpolation for the normalization differential; and sparse Laurent substitution and the finite normalization-module generators {1,t} for the conductor. Its finite a,n,b,c and monomial ranges are exactly printed in the output. The universal geometric and ring arguments above establish the all-parameter statements.

Opened primary topology inputs are Hatcher's author-hosted Algebraic Topology chapters: https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf, Theorem 1.20 p.43 (van Kampen), Proposition 1.33 p.61 (covering lift); ATch2.pdf, §2.2 pp.149–150 (Mayer–Vietoris, including the chain maps (x,-x) and x+y); ATch3.pdf, cap naturality p.241 and Theorem 3.35 p.245 (compactly supported duality, including proper pullback and extension for open embeddings). These exact passages were reopened and read before this freeze at 20:32–20:34 UTC, with retrievals turn662095772view0–3 and turn241308864view0. Earlier full proof readings of compact-support duality in the continuing work are not used to claim any new target-proof exposure. The maps in the present argument are specified above and below.

For the proper finite maps p, compact support is preserved by inverse image. Their degree is counted at a regular value, where all local degrees are +1 by the complex orientations. Cup naturality and this degree give integral_M p*(alpha cup alpha)=degree(p) integral_Q alpha cup alpha. For the open embedding into the torus, choose one compact neighbourhood containing the two-cycles. Excision identifies H*(U,U−K) with H*(T,T−K); its map to absolute cohomology transports the same Thom class and cup evaluation. This proves the asserted intersection preservation through the actual embedding. Finally every S² map into the torus lifts to its universal cover C² by the covering criterion and contracts there, so its homology class is zero.

The normal Euler number of a Lagrangian sphere is -2 with the stated orientations: the complex structure gives the bundle isomorphism from the tangent bundle to the normal bundle, and the ordered complex frame differs from tangent-then-normal order by one transposition. A height-gradient tangent field on S² has exactly the north and south zeros, both with local index +1, so the tangent Euler number is 2 and the normal Euler number is -2.

## Exact current prefreeze bindings

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WO_statement_inputs.tex — SHA256 7d6bd4adbcf77d00e05955a085329acf2f13e922436d269cddeef9473b31b939.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02WO_cited_input_supplement.tex — SHA256 2a1fce74ed378f48da4d016f41e6dd7e957147fa8afb777357931bad4a35c876.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.py — SHA256 724084534248c4e1e776808c61610ac3f054d639f4011370cc97c0d2a75cbbec.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.out — SHA256 1e8c2f2930dd9d0cd8c74803b051a4f2a3219eebdd64363160ae7254142bbe65.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_group05_program_run.json — SHA256 d48366e97805080d6aae9d6ca0f2c26d5153989f8b0b33218ef1afa95a504b3f.

# Recovery prefreeze copy: 02WP

Original surviving derivation: agents/ii_checks_A/derivations/S6_SERIES_PUBLISH_II_A_02WP_derivation.md; SHA256 7417f2c165db897e5b1fa075d5ef8df57b24958e3393f84b8a9a8845c96a8a70. Current copy prepared 2026-11-21T20:35:24.651723+00:00.

# Independent derivation: 02WP / night:P4.18

The statement and its cited-input statements P4.15/P4.16 have been read; all target proofs remain unopened. The construction below proves the all-parameter spherical obstruction directly and does not assume a rank condition on the normalization.

## 1. A finite map of the actual affine nearby fibres

For a≥2 and b,c≥1 write

    M={x^a-y^b z^c=1},       Q={x^a-u v=1}.

Both surfaces are smooth. On M, a zero y or z forces x^a=1 and a nonzero x derivative; when both are nonzero, a y or z derivative is nonzero. There is a finite proper holomorphic map of degree bc

    p:M→Q,           (x,y,z)↦(x,u=y^b,v=z^c).

Its generic fibres have exactly bc points, all orientation preserving under the complex orientations. Finiteness follows algebraically from the monic equations for y and z and also directly from properness of the power maps.

Choose two consecutive roots of x^a=1 and a simple path between them containing no other root. As derived explicitly in the parallel independent P4.17 calculation, the locus over that path with |u|=|v| and uv=x^a-1 is a compact smoothly embedded Lagrangian sphere K in Q. Direct cancellation of the Kähler form on its circle-over-interval parameterization proves the Lagrangian assertion, and the complex-structure normal-bundle map gives K²=-2.

## 2. The pullback class is spherical, including all branch singularities

Over the interior of the path, the inverse image of K is described by the angle equation `bθ+cψ=arg(x^a-1)` on a two-torus. It has d=gcd(b,c) circles. The deck group Z/b⊕Z/c acts, and continuation around the circle is addition by (1,-1). That permutation has exactly d orbits, each of length bc/d. At each endpoint both y and z vanish, so every circle collapses to a point. The closure of each cylinder is the continuous image of S², with its orientation pulled back from K off the endpoints. It can have an isolated nonsmooth parametrization at the endpoint, which does not affect its fundamental two-cycle.

Let α∈H_c²(Q;Z) be the Poincaré dual of K. The class dual to p*α is the sum of these d oriented spherical fundamental classes. Here is a local justification at the only two possible nonsmooth points. Near an endpoint Q has coordinates (u,v), since the x derivative is nonzero. The inverse image of a sufficiently small coordinate polydisc is the polydisc `|y|<ε^(1/b), |z|<ε^(1/c)` in the smooth source coordinates (y,z), and is contractible. Away from these two polydiscs, the inverse-image cylinders represent the ordinary pullback Thom class. Perturb the two target caps to be transverse to p while keeping their boundary circles fixed. The resulting pullback caps define the Gysin cycle; their difference from the original collapsed cylinder caps is a closed two-cycle in those contractible polydiscs and is zero in homology. Thus the asserted class identification is exact, including at the isolated parametrization singularities.

A sum of finitely many spherical classes in a connected space is spherical: choose their common endpoint as base point and compose the pinch map from S² to a wedge of d spheres with the d displayed maps. Write β for this spherical class in H2(M;Z). Properness and the degree of p give

    β² = integral_M p*α cup p*α
       = bc integral_Q α cup α
       = -2bc.

The equality is the change-of-degree formula for the compactly supported top-degree class α cup α. The value is nonzero for every b,c≥1. This suffices for the statement; no claim about a complete intersection basis for M is needed.

## 3. Transport into the actual torus fibre

The polynomial g=x^a-y^bz^c is weighted homogeneous of positive weights `(b+c,a,a)` and degree D=a(b+c). A germ with common multiplicity m has equation `F=u g^m`. Choose `lambda=u^(1/(mD))` locally and use the biholomorphism `phi(x_j)=lambda(x)^(w_j)x_j`. Its derivative is diagonal with nonzero entries at the origin, and `(g∘phi)^m=F` exactly.

Weighted scaling takes the compact representative of β and a compact neighbourhood of it from g=1 into an arbitrarily small coordinate ball in g=ε^D. Composition with phi^-1 places it inside the actual fibre F=ε^(mD). Compactly supported Poincaré duality and extension by zero preserve its square -2bc under this open embedding. On the other hand the composite spherical map into the nearby complex two-torus is nullhomotopic because that torus has universal cover C². Its global H2 class is zero, forcing square0. This contradiction proves every asserted exclusion, for every common multiplicity.

## 4. The displayed example and its differential

For `x²-z³y⁴=0`, the map

    nu:C²_(y,t)→S,         (y,t)↦(x=y²t³,y,z=t²)

is finite and birational. The element t satisfies the monic equation t²=z and belongs to the meromorphic field as x/(y²z). Its source is smooth and normal, hence this finite map is the normalization. The two derivative columns in the ambient coordinates (x,y,z) are `(2yt³,1,0)` and `(3y²t²,0,2t)`. The three maximal minors are

    -3y²t²,       4yt⁴,       2t.

Their ideal in the smooth normalization ring is exactly (t), since2 is a unit. Thus the rank drops along the whole divisor t=0, with rank1 there and rank2 elsewhere. This proves the normalization and divisorial rank-drop clauses through their actual map, while the preceding finite-map spherical argument still excludes the germ.


## Current recovery computation and primary inputs

This is a new prefreeze recovery copy. The surviving earlier derivation remains unchanged at its original path. Its historical 19:48 program and receipt were lost in the execution reset; no claim is made that those bytes were restored. The new program below was independently written from these statement equations and these already-derived maps before any target proof or historical target routine was opened. The current run and its output replace the unavailable historical computational evidence.

The fresh program uses sparse arithmetic in Z[zeta,y,u]/(zeta^a-1) for the affine charts; signed matching enumeration of every deleted-row incidence minor and Cauchy–Binet for the lattice determinant; exact deck permutations with the invariant i+j modulo gcd(b,c); first-order dual algebra and degree-bounded interpolation for the normalization differential; and sparse Laurent substitution and the finite normalization-module generators {1,t} for the conductor. Its finite a,n,b,c and monomial ranges are exactly printed in the output. The universal geometric and ring arguments above establish the all-parameter statements.

Opened primary topology inputs are Hatcher's author-hosted Algebraic Topology chapters: https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf, Theorem 1.20 p.43 (van Kampen), Proposition 1.33 p.61 (covering lift); ATch2.pdf, §2.2 pp.149–150 (Mayer–Vietoris, including the chain maps (x,-x) and x+y); ATch3.pdf, cap naturality p.241 and Theorem 3.35 p.245 (compactly supported duality, including proper pullback and extension for open embeddings). These exact passages were reopened and read before this freeze at 20:32–20:34 UTC, with retrievals turn662095772view0–3 and turn241308864view0. Earlier full proof readings of compact-support duality in the continuing work are not used to claim any new target-proof exposure. The maps in the present argument are specified above and below.

For the proper finite maps p, compact support is preserved by inverse image. Their degree is counted at a regular value, where all local degrees are +1 by the complex orientations. Cup naturality and this degree give integral_M p*(alpha cup alpha)=degree(p) integral_Q alpha cup alpha. For the open embedding into the torus, choose one compact neighbourhood containing the two-cycles. Excision identifies H*(U,U−K) with H*(T,T−K); its map to absolute cohomology transports the same Thom class and cup evaluation. This proves the asserted intersection preservation through the actual embedding. Finally every S² map into the torus lifts to its universal cover C² by the covering criterion and contracts there, so its homology class is zero.

The normal Euler number of a Lagrangian sphere is -2 with the stated orientations: the complex structure gives the bundle isomorphism from the tangent bundle to the normal bundle, and the ordered complex frame differs from tangent-then-normal order by one transposition. A height-gradient tangent field on S² has exactly the north and south zeros, both with local index +1, so the tangent Euler number is 2 and the normal Euler number is -2.

## Explicit local cap transport at the two ramification points

The sum of spherical images and the pullback dual class can be compared without treating the singular parametrizations as smooth embeddings. In target coordinates (u,v) at an endpoint, the matching cap is a smooth graph v=phi(u,bar u), where phi(0)=0 and its first derivative is c times complex conjugation with c nonzero. On the source p(y,z)=(y^b,z^c), the pulled-back cap has equation z^c=phi(y^b,bar y^b).

Choose a smooth bump chi in the u-disc, equal to one near zero and zero near the boundary of the cap. Replace the target graph by v=phi(u,bar u)+epsilon chi(u), with a sufficiently small nonzero complex epsilon. This is an isotopy fixed at the cap boundary. Near y=0 the perturbed equation has z nonzero, so its z derivative is nonzero. At a solution with z=0, y is nonzero; near the centre the derivative of phi(y^b,bar y^b) is an invertible real-linear map in y, and in the fixed transition annulus its lower derivative bound persists for sufficiently small epsilon. Thus the perturbed pullback is smooth and is transverse to p. Its boundary is exactly the unchanged preimage of the target boundary circle. Both the perturbed cap and the original collapsed cylinder caps lie in the same contractible source polydisc. Their difference is therefore a closed two-cycle bounding there. This gives the precise homology identification PD(p*alpha)=sum of the d spherical classes.

The deck element (1,-1) has order equal to the least positive integer divisible by both b and c, namely bc/gcd(b,c). Its action on the bc-point fibre therefore has gcd(b,c) orbits. The invariant i+j modulo gcd(b,c) labels them bijectively. Each orbit gives one circle over the interior and collapses at both endpoints; orient it by its positive covering degree. Every sphere has the same endpoint, so the pinch map S²→a wedge of d spheres realizes their sum as one spherical class.

## Exact current prefreeze bindings

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WP_statement_inputs.tex — SHA256 5bdba275265deb34d3c26a527247dbd91ffac885598f3740b96f70542368f1d5.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02WP_cited_input_supplement.tex — SHA256 5042a0fc5536d2156eedddaec316fd35bc16d1bec2bf84c33214f4825e31892c.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.py — SHA256 724084534248c4e1e776808c61610ac3f054d639f4011370cc97c0d2a75cbbec.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.out — SHA256 1e8c2f2930dd9d0cd8c74803b051a4f2a3219eebdd64363160ae7254142bbe65.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_group05_program_run.json — SHA256 d48366e97805080d6aae9d6ca0f2c26d5153989f8b0b33218ef1afa95a504b3f.

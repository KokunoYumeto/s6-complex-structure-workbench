# Recovery prefreeze copy: 02WQ

Original surviving derivation: agents/ii_checks_A/derivations/S6_SERIES_PUBLISH_II_A_02WQ_derivation.md; SHA256 83b17aad108939823e714998cfc12904fd42e22ff3272f748a1137a822c25a06. Current copy prepared 2026-11-21T20:35:24.651723+00:00.

# Independent derivation: 02WQ / night:P4.19

The statement and the cited P4.16/P4.18 statements have been read. The target proof and all prior computational routines remain unopened. The normalization, conductor and affine-fibre isomorphism are computed directly below.

## 1. The finite normalization morphism

Let `F=y(x²-zy²)` and let S be its reduced zero germ. It has a planar component A={y=0} and an umbrella component B={x²=zy²}. The normalization is the disjoint union of two smooth planes, with maps

    nu_A:(x,z)↦(x,0,z),
    nu_B:(y,t)↦(yt,y,t²).

The second map is finite because t²=z, and birational because t=x/y in the meromorphic field of B. The smooth source is therefore the normalization. The derivative of F is `(2xy, x²-3zy², -y³)`, so the reduced singular locus is the single smooth curve C={x=y=0}, with coordinate z.

## 2. Both conductor multiplicities

The ring of the umbrella component inside its normalization is `R_B=C{y,yt,t²}⊂C{y,t}`. A monomial y^i t^j belongs to R_B exactly when j is even or i≥1. This also describes convergent power series: separate their even and odd powers of t; every odd part must be divisible by y. Its conductor in C{y,t} is therefore the ideal (y). Indeed multiplying by t tests the only missing generator, and an element belongs to the conductor precisely when both it and its t multiple have no odd coefficient free of y.

For the union, its local ring is the fibre product of the two component rings along their scheme-theoretic intersection. On the plane the other equation restricts to x², so that intersection has ring C{x,z}/(x²). On B the plane equation is y, giving the same intersection ring after y=0. Thus an element supported only on the planar normalization component is a conductor element exactly when its planar function belongs to x² C{x,z}; arbitrary multiplication within that smooth component preserves this ideal.

An element supported only on the umbrella normalization component must multiply every function of C{y,t} into the ideal y R_B. The condition is `h C{y,t}⊂yR_B`. It forces h to be divisible by y; after dividing by y it is the previously computed umbrella conductor condition. Hence h belongs exactly to y² C{y,t}. Conversely every such h has the required product property. The conductor on the full normalization is therefore

    x² C{x,z}  ⊕  y² C{y,t}.

Its divisor has multiplicity2 on each reduced conductor component. The reduced planar conductor maps to C by the identity on z. The reduced umbrella conductor maps by `t↦z=t²`, a finite degree-two map ramified at t=0. These are the exact normalization morphisms proving the stated ramification and multiplicities.

## 3. The actual affine nearby fibre and its topology

On F=1, y is nonzero. Solving the equation gives

    z=(y x²-1)/y³.

Thus the map

    C*×C→{F=1},      (y,x)↦(x,y,(y x²-1)/y³)

is a holomorphic isomorphism with inverse the coordinate projection (x,y,z)↦(y,x). Substitution verifies both compositions and F=1 exactly. The product C*×C deformation retracts onto S¹, by contracting the C coordinate and radially projecting the nonzero C coordinate. Consequently π2 and H2 of this affine nearby fibre are zero. Every spherical class has square0.

The finite conductor map t↦t² and this explicit fibre isomorphism hold for the same germ F. They establish that the stated conductor ramification, by itself, does not supply the nonzero spherical intersection class used in P4.16–P4.18. The assertion has been proved for this exact hypersurface germ and its affine nearby fibre; no additional compact threefold construction is asserted or used.


## Current recovery computation and primary inputs

This is a new prefreeze recovery copy. The surviving earlier derivation remains unchanged at its original path. Its historical 19:48 program and receipt were lost in the execution reset; no claim is made that those bytes were restored. The new program below was independently written from these statement equations and these already-derived maps before any target proof or historical target routine was opened. The current run and its output replace the unavailable historical computational evidence.

The fresh program uses sparse arithmetic in Z[zeta,y,u]/(zeta^a-1) for the affine charts; signed matching enumeration of every deleted-row incidence minor and Cauchy–Binet for the lattice determinant; exact deck permutations with the invariant i+j modulo gcd(b,c); first-order dual algebra and degree-bounded interpolation for the normalization differential; and sparse Laurent substitution and the finite normalization-module generators {1,t} for the conductor. Its finite a,n,b,c and monomial ranges are exactly printed in the output. The universal geometric and ring arguments above establish the all-parameter statements.

Opened primary topology inputs are Hatcher's author-hosted Algebraic Topology chapters: https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf, Theorem 1.20 p.43 (van Kampen), Proposition 1.33 p.61 (covering lift); ATch2.pdf, §2.2 pp.149–150 (Mayer–Vietoris, including the chain maps (x,-x) and x+y); ATch3.pdf, cap naturality p.241 and Theorem 3.35 p.245 (compactly supported duality, including proper pullback and extension for open embeddings). These exact passages were reopened and read before this freeze at 20:32–20:34 UTC, with retrievals turn662095772view0–3 and turn241308864view0. Earlier full proof readings of compact-support duality in the continuing work are not used to claim any new target-proof exposure. The maps in the present argument are specified above and below.

For the proper finite maps p, compact support is preserved by inverse image. Their degree is counted at a regular value, where all local degrees are +1 by the complex orientations. Cup naturality and this degree give integral_M p*(alpha cup alpha)=degree(p) integral_Q alpha cup alpha. For the open embedding into the torus, choose one compact neighbourhood containing the two-cycles. Excision identifies H*(U,U−K) with H*(T,T−K); its map to absolute cohomology transports the same Thom class and cup evaluation. This proves the asserted intersection preservation through the actual embedding. Finally every S² map into the torus lifts to its universal cover C² by the covering criterion and contracts there, so its homology class is zero.

The normal Euler number of a Lagrangian sphere is -2 with the stated orientations: the complex structure gives the bundle isomorphism from the tangent bundle to the normal bundle, and the ordered complex frame differs from tangent-then-normal order by one transposition. A height-gradient tangent field on S² has exactly the north and south zeros, both with local index +1, so the tangent Euler number is 2 and the normal Euler number is -2.

## Finite-module and convergence detail for the conductor computation

The normalized umbrella ring C{y,t} is generated as a module over C{y,yt,t²} by 1 and t: each convergent series splits into its even powers f(y,t²) and t times its even powers g(y,t²). Hence h times the whole normalization lies in yR_B exactly when both h and ht lie in yR_B. The parity condition in the derivation then gives precisely y²C{y,t}, including all convergent series, rather than only polynomial monomials. On the planar branch the intersection quotient is C{x,z}/(x²), so the supported conductor ideal is exactly its kernel (x²). These finite generating maps are the ones used in the fresh program.

## Exact current prefreeze bindings

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WQ_statement_inputs.tex — SHA256 01a9125268ecd476284708a1a2be9a9af414335f40bbad16d2e3a34bdfe00b76.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02WQ_cited_input_supplement.tex — SHA256 67e7a6422566721328c93ebc490336a7b93f2dd93040e6fc3e24d8e8bcddc63c.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.py — SHA256 724084534248c4e1e776808c61610ac3f054d639f4011370cc97c0d2a75cbbec.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.out — SHA256 1e8c2f2930dd9d0cd8c74803b051a4f2a3219eebdd64363160ae7254142bbe65.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_group05_program_run.json — SHA256 d48366e97805080d6aae9d6ca0f2c26d5153989f8b0b33218ef1afa95a504b3f.

# Recovery prefreeze copy: 02WN

Original surviving derivation: agents/ii_checks_A/derivations/S6_SERIES_PUBLISH_II_A_02WN_derivation.md; SHA256 fa3e1003439af46ec6d176bde97ec764aedb712447cdd508f7fa7adddc06e5d1. Current copy prepared 2026-11-21T20:35:24.651723+00:00.

# Independent derivation: 02WN / night:P4.16

The target proof and prior programs remain unopened. The exact statement packet and empty cited-input supplement have been read. The following construction is independent of the printed proof. It proves every positive common multiplicity, using only the actual local-to-nearby-fibre maps.

## The compact spherical class

Let M_n be the smooth affine surface `x²-zy^n=1`. Smoothness follows because y=0 forces x=±1, where the x derivative is nonzero; at y≠0 the z derivative is nonzero. There is a finite holomorphic map of degree n

    p_n:M_n→Q,       (x,y,z)↦(x,v=y^n,z),
    Q={x²-vz=1}.

On Q take the real sphere K defined by x real in [-1,1], z=-conjugate(v), and |v|²=1-x². It is a smoothly embedded S². It is Lagrangian for the restriction of the standard Kähler form of C³: the x coordinate has only one real direction and the v,z contributions cancel. The complex structure sends its tangent bundle to its normal bundle. Comparing `(e1,e2,Je1,Je2)` with the complex orientation `(e1,Je1,e2,Je2)` changes the sign once, so the oriented normal Euler number is minus the tangent Euler number, namely -2. Thus K²=-2.

The inverse image Σ_n=p_n^-1(K) is given by x real, `z=-conjugate(y)^n`, and `|y|^(2n)=1-x²`. It is a smooth sphere: away from its two endpoints it is a circle over an interval; near each endpoint, x is the smooth real function `±sqrt(1-|y|^(2n))` and z is the displayed smooth function of y. The restriction Σ_n→K has degree n, ramified only at the two endpoints. The induced map of normal bundles is an isomorphism to the pullback normal bundle, including at those endpoints: in the source coordinates (y,z), the tangent plane of Σ_n is the y plane when n>1, while the z direction maps isomorphically to the normal quotient of the graph `z=-conjugate(v)` in Q. Therefore

    Σ_n² = n K² = -2n.

Equivalently this is the proper-degree formula for the pullback of the compactly supported Poincaré dual of K. In particular the class of this explicitly mapped sphere has nonzero self-intersection for every n≥1.

## The local embedding, including the unit and the common multiplicity

Set g=x²-zy^n. It is weighted homogeneous for positive integer weights `(n+1,2,2)` and weighted degree D=2(n+1). A local defining function for a fibre whose reduced germ is the stated one and whose common multiplicity is m has the form `F=u g^m`, with u a holomorphic unit. On a sufficiently small simply connected neighbourhood choose the holomorphic root `lambda=u^(1/(mD))`. The map

    phi(x,y,z)=(lambda(x,y,z)^(n+1)x,
                 lambda(x,y,z)^2 y,
                 lambda(x,y,z)^2 z)

has invertible derivative at the origin, since its linear part is diagonal with nonzero entries. It is a local biholomorphism and weighted homogeneity gives `(g∘phi)^m=u g^m=F`. This is the exact coordinate morphism absorbing the unit.

For a positive real ε, the weighted scaling `(x,y,z)↦(ε^(n+1)x,ε²y,ε²z)` sends g=1 to g=ε^D and shrinks the entire compact Σ_n, together with a compact normal neighbourhood, into any prescribed coordinate ball. Composing with phi^-1 embeds it in the actual fibre F=ε^(mD). All maps are holomorphic local isomorphisms on those neighbourhoods and preserve the intersection number -2n.

That actual nearby fibre is a complex two-torus. Its universal cover is C², so π2 is zero. The composite map S²→Σ_n→the nearby torus is nullhomotopic; its integral homology class is therefore zero. The self-intersection of a compact cycle is preserved by this open embedding: extension by zero of its compactly supported Poincaré dual equals the dual of its pushed-forward class. Its square in the torus must consequently be both -2n and zero, a contradiction.

This proves the exclusion for every n and m. The case n=2 is the Whitney umbrella. The proof uses only this local map into a smooth torus fibre; no Betti number of a compact total space enters.


## Current recovery computation and primary inputs

This is a new prefreeze recovery copy. The surviving earlier derivation remains unchanged at its original path. Its historical 19:48 program and receipt were lost in the execution reset; no claim is made that those bytes were restored. The new program below was independently written from these statement equations and these already-derived maps before any target proof or historical target routine was opened. The current run and its output replace the unavailable historical computational evidence.

The fresh program uses sparse arithmetic in Z[zeta,y,u]/(zeta^a-1) for the affine charts; signed matching enumeration of every deleted-row incidence minor and Cauchy–Binet for the lattice determinant; exact deck permutations with the invariant i+j modulo gcd(b,c); first-order dual algebra and degree-bounded interpolation for the normalization differential; and sparse Laurent substitution and the finite normalization-module generators {1,t} for the conductor. Its finite a,n,b,c and monomial ranges are exactly printed in the output. The universal geometric and ring arguments above establish the all-parameter statements.

Opened primary topology inputs are Hatcher's author-hosted Algebraic Topology chapters: https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf, Theorem 1.20 p.43 (van Kampen), Proposition 1.33 p.61 (covering lift); ATch2.pdf, §2.2 pp.149–150 (Mayer–Vietoris, including the chain maps (x,-x) and x+y); ATch3.pdf, cap naturality p.241 and Theorem 3.35 p.245 (compactly supported duality, including proper pullback and extension for open embeddings). These exact passages were reopened and read before this freeze at 20:32–20:34 UTC, with retrievals turn662095772view0–3 and turn241308864view0. Earlier full proof readings of compact-support duality in the continuing work are not used to claim any new target-proof exposure. The maps in the present argument are specified above and below.

For the proper finite maps p, compact support is preserved by inverse image. Their degree is counted at a regular value, where all local degrees are +1 by the complex orientations. Cup naturality and this degree give integral_M p*(alpha cup alpha)=degree(p) integral_Q alpha cup alpha. For the open embedding into the torus, choose one compact neighbourhood containing the two-cycles. Excision identifies H*(U,U−K) with H*(T,T−K); its map to absolute cohomology transports the same Thom class and cup evaluation. This proves the asserted intersection preservation through the actual embedding. Finally every S² map into the torus lifts to its universal cover C² by the covering criterion and contracts there, so its homology class is zero.

The normal Euler number of a Lagrangian sphere is -2 with the stated orientations: the complex structure gives the bundle isomorphism from the tangent bundle to the normal bundle, and the ordered complex frame differs from tangent-then-normal order by one transposition. A height-gradient tangent field on S² has exactly the north and south zeros, both with local index +1, so the tangent Euler number is 2 and the normal Euler number is -2.

## Exact current prefreeze bindings

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WN_statement_inputs.tex — SHA256 62df57e9596519aba35e9ff80017b94aa0844a100d530866813d270a18b70dae.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02WN_cited_input_supplement.tex — SHA256 b4ab069de37e61d98d9a9f799451283b8696dcb82686c9c21868851d9bd1391e.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.py — SHA256 724084534248c4e1e776808c61610ac3f054d639f4011370cc97c0d2a75cbbec.
- code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.out — SHA256 1e8c2f2930dd9d0cd8c74803b051a4f2a3219eebdd64363160ae7254142bbe65.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_group05_program_run.json — SHA256 d48366e97805080d6aae9d6ca0f2c26d5153989f8b0b33218ef1afa95a504b3f.

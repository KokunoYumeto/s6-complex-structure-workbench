# 01FD / cdp:st:C.3.7 — prereading derivation

Checker: i_provenance_recovery. Written on 21 November 2026 before release or reading of this target proof. The target statement and its empty cited-input supplement were read. The other three pending target proofs (01FE, 01FF, 01GL), E_checks.py, and C's target reconstructions remain closed.

## Domain and declared inputs

The domain proved here is a **smooth connected compact complex threefold** Y with b1(Y)=b2(Y)=0. The original statement says only “compact complex threefold” under a convention allowing analytic spaces. This derivation does not verify that broader singular domain, and does not assert a singular counterexample. The source proposal must specify smoothness and check incoming uses.

The map f:Y→C is a proper surjective holomorphic map to a nonsingular compact connected curve, with connected fibres, and its smooth general fibre F is bielliptic. A nonconstant map to the normalization of a possibly singular curve has the same smooth generic fibres; the statement should name the nonsingular base used in the proof.

Inputs read before freezing: D.1.7 (the real coefficient injection for compact connected complex fibres) in the 01FF safe packet; the exact E4 degree-one cohomological flatness statement in its safe supplement and its previously checked Viaclovsky primary transport; Kawai 1969, Proposition 2, pp.605–608, including its complete proof of the relative Albanese construction; Buchdahl 1999, the theorem stated on p.288 and Theorem 11 on p.297, that an even-b1 compact complex surface is Kähler; Saito 1990, Theorem (0.6), p.128, and decompositions (0.7)–(0.8), which apply to a proper map from a smooth Kähler manifold. Kawai's following corollary, claiming the relative Albanese surface is algebraic from the asserted multiple fibres, is **not an input**. Its conclusion is not used below.

The primary surface facts used are that a bielliptic surface is Kähler, has pg=0 and q=1, and its Albanese morphism a_F:F→Alb(F) has connected elliptic fibres and induces an isomorphism on H¹ with real coefficients. For the latter isomorphism, the Albanese map induces an isomorphism on holomorphic one-forms; Hodge decomposition for the Kähler surface and the elliptic curve, together with the conjugate map, gives the real H¹ isomorphism. This fixes the precise cohomological arrow.

## 1. A nonzero invariant class supplied by Y

Connected fibres give f_*R_Y=R_C. The degree-one Leray edge injection H¹(C,R)→H¹(Y,R) shows that C has genus zero, so C≅P¹. The five-term exact sequence then reads

    0 → H¹(Y,R) → H⁰(C,R¹f_*R_Y)
      → H²(C,R) → H²(Y,R).

Both outside groups vanish by the stated Betti hypotheses. Thus the displayed middle arrow is an isomorphism onto R. Choose a nonzero section α of R¹f_*R_Y.

Let U⊂C be the complement of the critical values, further reduced by finitely many values when needed for the relative Albanese construction. The section α has nonzero restriction to U. Here is a proof that does not assume a local invariant-cycle theorem for Y. The coefficient map induces a sheaf morphism

    R¹f_*R_Y → R¹f_*O_Y.

At a point c, compose its stalk map with coherent base change to H¹(Y_c,O_{Y_c}). Proper topological base change identifies the source stalk with H¹(Y_c,R), and the composite is exactly the real coefficient map of D.1.7. It is injective. Hence the sheaf morphism is injective. E4 makes R¹f_*O_Y locally free. If α vanished on U, its image would be a holomorphic section of this vector bundle supported at finitely many points, hence zero, and injectivity would give α=0. This contradiction proves α|U≠0. In particular α gives a nonzero monodromy-invariant class on a regular fibre.

## 2. The actual relative Albanese diagram

Apply Kawai's Proposition 2 only to the bielliptic fibres, where its pg=0, q=1 hypotheses hold. It yields a compact complex surface V over C and a meromorphic map Y⇢V over C whose restriction over a possibly smaller U is the fibrewise Albanese map onto its elliptic image. Resolve V and the graph to obtain

    Z --g--> V'
    |μ       |h
    Y --f--> C,

with μ a modification of smooth compact threefolds, V' a smooth compact surface, and h∘g=f∘μ. The modifications may be chosen to be isomorphisms over U. The map g is proper and surjective. Its general fibre is the connected elliptic fibre of the Albanese map; its Stein factorization has finite birational second map to the normal surface V', so that second map is an isomorphism. Thus all g-fibres are connected.

Pullback gives the injection H¹(V',R)→H¹(Z,R) by the first Leray edge map for g. A modification between smooth compact complex manifolds preserves H¹; equivalently one can resolve its graph into blowups along smooth centres, for which the blowup cohomology formula has no new degree-one summand. Consequently

    H¹(V',R) ↪ H¹(Z,R) ≅ H¹(Y,R)=0.

Therefore b1(V')=0, and Buchdahl's theorem supplies a Kähler metric on V'. No projectivity of V' is asserted or needed.

On U the actual Albanese pullback gives an isomorphism of local systems

    g_U^*: R¹h_{U*}R → R¹f_{U*}R.

Its inverse transports α|U to a nonzero invariant section α' of R¹h_{U*}R. This is an inverse to a specified cohomological map, not an identification of unrelated families.

## 3. Kähler invariant cycles give the contradiction

Apply Saito (0.6) to h:V'→C. Its smooth Kähler source satisfies the theorem's hypothesis with π=id_{V'}. On the smooth base curve, for j:U→C and L=R¹h_{U*}R, the full-support middle intersection-complex summand is IC_C(L)=j_*L[1]. The direct image Rh_*R_{V'}[2] therefore has this summand, whose restriction to U is L[1]; after shifting by −2 it is j_*L[−1]. Taking degree-one global hypercohomology shows that restriction

    H¹(V',R) → H⁰(C,j_*L)=H⁰(U,L)

is surjective onto the invariant sections. More explicitly, choose the decomposition summand with its restriction identified with the L-summand of the smooth direct image; its inclusion induces a lift of every element of H⁰(U,L). The resulting class restricts to that element on a regular fibre. This is the degree-one global invariant-cycle map.

But H¹(V',R)=0 and α' is a nonzero element of its asserted image. The contradiction excludes the bielliptic general fibre in the smooth domain stated above.

## Check scope

This is a newly written derivation from the named inputs before target release. It uses no Kawai corollary, no claim of a horizontal divisor coming from nonexistent multiple Albanese fibres, and no restriction-surjectivity theorem from CDP98/CDP20. It has no numerical or symbolic program component. The entire target proof is still unopened at writing. Later comparison must preserve the stated smoothness qualification and bind the exact maps and primary locators.

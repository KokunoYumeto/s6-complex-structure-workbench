# 01FF / cdp:st:C.3.9 — prereading derivation

Checker: i_provenance_recovery. Written on 21 November 2026 before release or reading of the target proof. Safe statement, D.1.7, D.1.9 and E4 supplements were read. FD/FE/GL target proofs, E_checks.py and C's reconstructions remain closed. The primary CDP98 Proposition 3.6 and the referring CDP20 Corollary 5.3 were read as source context, and their blanket restriction/effectivity argument is not admitted as an input.

## Domain and surface inputs

The domain certified here is a smooth connected compact complex threefold Y with b1(Y)=b2(Y)=0, a(Y)=1, and holomorphic algebraic reduction f:Y→P¹ with connected fibres. The original statement's broad “compact complex threefold” wording requires a smoothness repair for the manifold input E4. No singular case is asserted to be false.

The surface-classification inputs are stated precisely: a secondary Kodaira surface F has b1(F)=1, b2(F)=0, h¹(F,O_F)=1; its canonical bundle has finite order n∈{2,3,4,6}; its canonical cyclic cover is a primary Kodaira surface, whose Albanese is an elliptic curve and whose Albanese morphism is its principal elliptic fibration. The finite canonical deck group acts on this Albanese curve with quotient P¹, giving the unique algebraic reduction π_F:F→P¹. The primary non-Kähler elliptic descriptions in Brînzănescu–Moraru, arXiv:math/0309031v1, §2, p.3, confirm that the elliptic fibration is a quasi-bundle and its divisor classes are given by fibres, including the relation O(mE)=π_F^*O(p) at a multiple fibre. The canonical-cover construction itself is Spec_F(⊕_{j=0}^{n−1}K_F^j) with multiplication using a trivialization of K_F^n.

Prokhorov–Shramov, arXiv:1909.12013v4, the paragraph preceding Lemma 2.4 on p.4 and Corollary 5.2 on p.11, were also read before freezing. They give the primary/secondary algebraic reductions and the exact canonical algebra for the finite primary cover. Only those surface inputs are used; no automorphism-group conclusion is needed.

We take U to be the connected complement of finitely many values where the fibres are smooth secondary Kodaira surfaces. This is the general secondary Kodaira case in the statement. The local construction below also shows explicitly how the intrinsic fibre line class varies holomorphically; it does not posit a meromorphic quotient of all of Y.

## 1. A global real section and the exact Picard coordinate

Leray with real coefficients and f_*R=R gives

    H⁰(P¹,R¹f_*R) ≅ H²(P¹,R) ≅ R,

because H¹(Y,R)=H²(Y,R)=0. Choose α≠0. The coefficient sheaf map R¹f_*R→R¹f_*O is injective: at every stalk, composing with coherent base change is the injective coefficient map H¹(Y_t,R)→H¹(Y_t,O) of D.1.7, using topological proper base change for its source. E4 makes R¹f_*O locally free. Thus α cannot be supported at the omitted values: its holomorphic image would vanish identically. Consequently α|U is a nonzero flat real section.

Over U, H¹(F_t,R) has real dimension one. The nonzero section α trivializes this real local system and its monodromy is the identity (an integral automorphism of a rank-one lattice is ±1, and only +1 fixes α). Choose the primitive integral section e and constant c≠0 with α=c e. Divide the holomorphic image of α by c. Leray for O and H¹(P¹,O)=H²(P¹,O)=0 lifts that global section uniquely to β∈H¹(Y,O_Y).

On each regular fibre, β_t is exactly the coefficient image of e_t. That image is nonzero by D.1.7, and since h¹(O)=1 it is a complex basis. The exponential sequence gives the following specified isomorphism of complex Lie groups:

    C/Z → Pic⁰(F_t),   z mod Z ↦ exp(2πi z β_t).

Under w=exp(2πi z), this is an isomorphism C*→Pic⁰(F_t). It is holomorphic in t, and it is globally single-valued on U because the integral section e is globally fixed. This exact map is the only Picard coordinate used below. In particular |w|=1 means z is real modulo Z; the resulting bundle is the unitary flat bundle with character γ↦exp(2πi z⟨e_t,γ⟩).

## 2. Holomorphic variation of the intrinsic effective line bundle

For each t let A_t=π_{F_t}^*O_{P¹}(1). This is intrinsic: changing the coordinate on the target P¹ preserves the class O(1). To justify holomorphic variation locally, work over a simply connected sufficiently small disc D⊂U. The order n of K_{F_t} is locally fixed. Grauert and fibrewise triviality give a line f_*K_{Y/D}^n whose evaluation is everywhere an isomorphism; trivialize that line on D. The algebra

    ⊕_{j=0}^{n−1} K_{Y/D}^j

with this multiplication gives a finite étale family of the canonical primary Kodaira covers over D. On that family the relative holomorphic one-forms have dimension one. Integrating a local nonzero form from a local section, modulo its two Albanese periods, constructs the relative Albanese curve and the fibrewise Albanese map. The periods depend holomorphically on the parameter and generate the rank-two lattice of the Albanese curve. For a primary Kodaira surface they are the periods on its elliptic base; the central fibre cycles of its principal elliptic bundle are annihilated, so the lattice is the same fixed rank-two quotient of the marked homology throughout D. Changing the section translates the Albanese map and does not change its connected fibres.

The finite deck group acts on this relative Albanese by the maps induced from its action on the canonical cover. Its quotient is a smooth family of genus-zero curves over D, because each quotient is P¹. Locally trivializing that family gives π_D:Y_D→P¹×D. The class π_D^*O(1) restricts to A_t. Two local constructions differ on the genus-zero target by a PGL₂ transformation, which preserves O(1) on every fibre. Hence their classes agree in the relative Picard group, giving a single holomorphic section t↦A_t over U. This is a local relative construction; no extension of an elliptic quotient through a singular fibre is being assumed.

Since b2(F_t)=0, H²(F_t,Z) is a finite group. Its exponent k is fixed under the smooth topological local trivializations on connected U. Therefore c1(A_t^k)=0 and A_t^k lies in Pic⁰(F_t) for the same positive integer k on U. Let q(t)∈C* be its coordinate under the exact isomorphism in Step1. The previous paragraph makes q:U→C* holomorphic and single-valued.

## 3. The character avoids the unit circle and is constant

The bundle A_t^k is effective and has a section with a nonempty zero divisor: pull back a nonzero section of O_{P¹}(k). A unitary flat line bundle on a connected compact complex manifold has no such section. Indeed, in local unitary flat frames the squared norm of a holomorphic section is a globally defined continuous function, locally a sum of |holomorphic function|² (here one square), hence plurisubharmonic. The maximum principle on the compact manifold makes the norm constant; a nonzero section has constant positive norm and cannot vanish. Consequently |q(t)|≠1 for all t∈U.

The connectedness of U makes the sign of log|q(t)| constant. Replace q by q^{-1} for the bounded-function argument when necessary; this is the specified group inversion on C*, and the original effective bundle remains A_t^k. One of q and q^{-1} is a holomorphic map U→{0<|w|<1}. It extends over every omitted point by the removable-singularity theorem. The extension to P¹ is constant, so q itself is a nonzero constant q0. No extension of the underlying fibre divisors across the omitted fibres has been used.

Choose z0∈C with exp(2πi z0)=q0 and form the global line bundle

    L=exp(2πi z0 β) ∈ Pic⁰(Y).

By Step1 its restriction to every F_t, t∈U, is exactly A_t^k. Therefore h⁰(F_t,L|F_t)=k+1≥2, since π_{F_t*}O_{F_t}=O_{P¹}.

## 4. The field contradiction

The coherent sheaf f_*L has generic rank k+1≥2. For d sufficiently large, f_*L⊗O_{P¹}(d) is generated by global sections. Choose two whose restrictions to a general F_t are linearly independent. Their ratio is a meromorphic function on Y nonconstant on F_t. It is transcendental over f^*M(P¹): an algebraic relation would restrict at a regular parameter to a nonzero polynomial with finitely many roots, forcing the ratio to be constant on the connected fibre. Thus a(Y)≥2, contradicting the algebraic-reduction assumption a(Y)=1.

This excludes secondary Kodaira general fibres in the explicit smooth domain. Every use of torsion above is killed by the actual finite exponent k; no torsion-freeness of H¹ or H² of the fibre is assumed.

## Check scope

This argument constructs the global line bundle from a constant relative character. It does not infer effectivity on a general fibre from effectivity of a separately chosen bundle on one fibre, and it does not use the CDP restriction-surjectivity assertion. Its topology, coefficient map, exponential map, local canonical cover and relative Albanese quotient are specified above. No computation program or target proof was read or used. Subsequent whole-proof comparison must retain the smoothness qualification and check the exact local-cover construction and receiving uses.

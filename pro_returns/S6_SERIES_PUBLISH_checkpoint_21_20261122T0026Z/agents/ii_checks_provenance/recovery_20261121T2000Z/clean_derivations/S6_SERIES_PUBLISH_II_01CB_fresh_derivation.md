# Fresh prereading derivation: 01CB / cdp:st:C.2.NC.4

Checker: i_provenance. This derivation is written before releasing or reading this target's printed proof. The exact statement and cited-input packet and its supplemental header have been read. The previous completed C.NC.2/C.NC.3 checks and Paper I work are declared related exposure. No target proof, historical target check, or target program is used below. Both 01CB and 01CC are to be frozen before either target is released.

## 1. Domain, notation, and exact inputs

Let g:Y→C be the proper connected-fibre map of C.NC.3: Y is a connected smooth compact complex threefold, H²(Y,Q)=0, C is a smooth compact curve, and a smooth general fibre has Euler characteristic zero. For a fibre with reduced normal-crossings support S, write its scheme divisor as Σm_i S_i, and ν:⊔T_i→S for the normalization. Let D_i be the conductor divisor on T_i. Let C_α be each connected normalized double curve and τ the number of triple points.

The exact C.NC.2 input gives

    e(C_α)=deg R_α,  Σe(C_α)=3τ,  Σχ(O_Ti)=τ/2,
    e(S)=Σe(T_i)−Σe(C_α)+τ.

The normalization adjunction isomorphism for this Cartier normal-crossings divisor is

    K_Ti ⊗ O_Ti(D_i) ≅ ν_i^*((K_Y⊗O_Y(S))|S_i).

To specify this map locally, take S=(x_1⋯x_r=0) and a local generator Ω of K_Y. The residue of Ω/(x_1⋯x_r) on the branch x_i=0 is a generator of K_Ti(D_i), with a simple pole on each x_j=0, j≠i. Changing Ω or a defining equation changes both sides by the same unit, so these branchwise maps glue. Consequently c₁(K_Ti)+[D_i]=0 in rational cohomology: every line bundle pulled back from Y has rational Chern class zero.

The surface input used here is obtained from Ornea–Verbitsky–Vuletescu, arXiv:1810.05768v3, version 2.8 dated 28 April 2020: Theorem 2.5 (pp.7–9), Theorem 4.2 (p.17), the local description and Remark 4.4 (p.21), and Theorem 5.1 (p.27, proof through p.29). The explicit rationality input is Hassett, Rational surfaces over nonclosed fields, Theorem 2.26, printed p.178 (PDF p.185), applied after the projective/minimal-model transport below. The four particular page images p.17,21,27 and p.178 were actually viewed in full; the stated larger text scopes were read. Their files, hashes, editions and retrieval receipts are bound separately.

## 2. A compact non-Kähler surface has χ(O)=0, with the maps used here

Pass from a compact smooth surface T to its minimal model T_min by contractions of exceptional rational curves. For each blow-up π, π_*O=O and R¹π_*O=0: on its exceptional P¹ the successive formal-neighbourhood quotients are O_P¹(n), n≥0, whose H¹ vanishes. The Leray comparison therefore preserves all H^q(O), and in particular χ(O). Kählerness is preserved under blow-ups and contractions of exceptional curves, so the minimal model of a non-Kähler T is non-Kähler.

Theorem 5.1 says that T_min is of class VII or admits an isotrivial elliptic fibration (these alternatives can overlap). In class VII, b₁=1 and κ=−∞. Theorem 2.5 gives h¹(O)=1 and κ=−∞ gives h⁰(K)=0. Thus χ(O)=1−1+0=0.

In the elliptic case, Theorem 4.2 and Remark 4.4 supply the local maps

    (E×Δ_s)/⟨(z,s)↦(z+e,ζ_m s)⟩ → Δ_t,  t=s^m,

where e is an m-torsion point of exact order m. The action on the total product is free; every reduced fibre is a smooth elliptic curve. The Euler stratification over the finitely many multiple fibres gives e(T_min)=0. On the orbifold base with these multiplicities, the relative tangent line has transition derivative equal to the derivative of an automorphism of E. Such derivatives have finite image, hence their rational first Chern class is zero. The horizontal tangent quotient is the pullback of the orbifold tangent line of the curve. In rational cohomology this proves c₁(T_min) is pulled back from the curve, so c₁(T_min)²=0. This is a comparison of the tangent sequence on the displayed finite root charts; it does not replace the multiple-fibre map by a submersion on the coarse base. The surface Riemann–Roch identity 12χ(O)=c₁²+c₂ now gives χ(O_Tmin)=0. The blow-up transport gives χ(O_T)=0 in either case.

## 3. Reducible support: every normalization component is non-Kähler

Suppose S is connected and reducible. The finite graph of global irreducible components is connected, so for every S_i there is a distinct S_j meeting it. Because Y is smooth, S_j is Cartier. Its canonical section restricts and pulls back to a nonzero section of ν_i^*O_Y(S_j) on T_i, with nonempty effective divisor E_ij. It is nonzero because S_i is not contained in S_j. It vanishes at their intersection, whose divisor branches are present in the normal-crossings charts.

The class [E_ij]=ν_i^*c₁(O_Y(S_j)) is zero in H²(T_i,Q). A Kähler form ω on T_i would give

    0 = ∫_Ti [E_ij]∧ω = ∫_Eij ω > 0.

The last strict inequality holds because E_ij is a nonempty effective complex curve. Thus T_i is non-Kähler. Section 2 gives χ(O_Ti)=0 for every i. The coherent Euler input now implies τ=0. Since deg R_α=0, every C_α has Euler characteristic zero and is a smooth elliptic curve.

With no triple points, every conductor branch on T_i is smooth and distinct conductor branches are disjoint. A connected conductor double cover over C_α is étale, so it too is elliptic. Thus D_i is a disjoint union of smooth elliptic curves, including the case in which its two local sheets are permuted around the underlying double curve.

## 4. The individual surface Euler numbers, including self-gluing and sheet exchange

The argument requires individual e(T_i)=0, not just their sum. Since K_Ti+[D_i]=0 rationally, K_Ti²=D_i². We prove D_i²=0 by the actual normal-line maps.

First take a double curve joining distinct global components S_i and S_j. The pullback divisor E_ij of section 3 is a disjoint union of its conductor curves on T_i (all multiplicities are one for the reduced normal-crossings equation). For each such connected curve B, the restriction O_Ti(E_ij)|B is N_{B/Ti}, because its other curves are disjoint from B. Its degree is zero, as O_Ti(E_ij)=ν_i^*O_Y(S_j) has rational Chern class zero. Hence B²=0.

Now take a double curve C coming from two branches of the same global irreducible component S_i. Let p:B→C be the degree-two étale conductor cover and ι its sheet involution. It may have two connected components. Locally S_i has equation xy=0, with B's first sheet lying in x=0 and its normal coordinate in that sheet equal to y; the second has equation y=0 and normal coordinate x. The identity of conormal generators

    [xy] ↦ [x]⊗[y]

along C glues under coordinate changes. Dualizing and pulling back to B gives the exact line isomorphism

    p^*(O_Y(S_i)|C) ≅ N_{B/T_i} ⊗ ι^*N_{B/T_i}.

Here N is understood separately on the two components if B is disconnected. When B=B₁⊔B₂, restricting this map to either sheet gives deg N_B1+deg N_B2=0. These two degrees together are exactly the contribution of this double curve to D_i². When B is connected, taking degrees gives 2 deg N_B=0, so again the contribution is zero. The left side has degree zero because it is pulled back from an ambient line bundle with rational Chern class zero. This also explicitly handles branch permutation; it does not assume globally separated branches.

All conductor components are covered by these two cases and are disjoint. Therefore D_i²=0 for each i. The holomorphic Euler calculation and Noether's identity give

    e(T_i)=12χ(O_Ti)−K_Ti²=0.

Finally the topological input of section 1 gives e(S)=0−0+0=0. None of these steps divides by a fibre multiplicity or compares unequal multiplicities as equal: the divisors used are the actual reduced global components S_i and S_j in the smooth ambient Y. Thus the result includes arbitrary positive m_i.

## 5. The remaining irreducible singular support and the value τ=2

Let S now be irreducible and singular, with normalization T. The same adjunction gives K_T+[D]=0 rationally, and D is nonempty. The C.NC.2 identity gives χ(O_T)=τ/2≥0.

If τ>0, T cannot be non-Kähler by section 2. Choose a Kähler form ω. Since D is nonempty and effective,

    c₁(K_T)·[ω]=−[D]·[ω]<0.

For every m>0, a nonzero section of mK_T would have an effective zero divisor (possibly empty), whose intersection with ω is nonnegative, contradicting this strict negative intersection. Thus every positive plurigenus vanishes; in particular p_g=P₂=0. Therefore

    0<χ(O_T)=1−h¹(O_T)≤1,

so h¹(O_T)=0, χ(O_T)=1 and τ=2.

To justify rationality with the precise algebraic input, Kähler Hodge decomposition and p_g=0 identify all of H²(T,R) with its real (1,1) part. The Kähler cone is open, so it contains a rational class. Multiplying to an integral class and applying the exponential/Lefschetz (1,1) map gives a positive line bundle; the Kodaira embedding theorem makes T projective. Contract exceptional curves to a smooth projective minimal model T_min. The blow-up maps preserve q and all plurigenera (canonical forms pull back with their exceptional vanishing orders), so q(T_min)=P₂(T_min)=0. Hassett Theorem 2.26, printed p.178, gives that T_min is rational; the contraction map and its inverse birational blow-ups make T rational.

Conversely a rational normalization has χ(O_T)=1, so the same C.NC.2 identity gives τ=2. In the reducible case τ=0 by section 3. This proves exactly the target's alternatives, without an assertion about a wider singular or nonsmooth ambient domain.

## 6. Conclusion and computation scope

Every conclusion of 01CB has been obtained with its original smooth-Y hypotheses: reducible connected support has τ=e=0, each normalized conductor is a disjoint union of smooth elliptic curves, and every T_i has e=0; every singular NC support with a triple point is irreducible with rational normalization and exactly two triple points. The local normal-line identifications and the projective/minimal-model transport above are part of this derivation. There is no target-program execution in this prereading record and no new independent numerical event is asserted. After release, any positively identified inherited computation will be compared with an actually new method as required.

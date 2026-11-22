# Fresh prereading derivation: 01CC / cdp:st:C.2.NC.5

Checker: i_provenance. Written before releasing or reading the target proof. The exact statement/cited-input packet, supplemental header, and safe A.1.1/A.3 kernel inputs have been read. The fresh 01CB derivation is written separately and both derivations are frozen before either target proof is opened. Prior completed C.NC.2/C.NC.3, A.2.2 and related Paper I checks are declared input exposure. No historical target proof/check is used.

## 1. Exact domain and fibre Euler numbers

Let g:Y→C have the smooth compact connected threefold domain of C.NC.3, H²(Y,Q)=0, connected fibres and smooth general fibre F with e(F)=0. Every reduced fibre support has normal crossings. A finite set Δ contains all critical values; outside Δ the map is a proper smooth submersion and hence a differentiable locally trivial bundle.

For each irreducible reduced support S_c, the scheme fibre is mS_c for one positive integer m, so the exact uniform-multiple input C.NC.3 gives e(S_c)=τ(S_c). For every reducible support, C.NC.4, independently derived in the companion 01CB record, gives e(S_c)=τ(S_c)=0, with no equal-multiplicity assumption. Smooth supports are connected and irreducible, so they are included in the uniform-multiple calculation and have τ=e=0.

The companion derivation proves that τ>0 means an irreducible singular support with rational normalization, and then τ=2. The converse also follows from C.NC.2: for an irreducible support with rational normalization T, χ(O_T)=1 forces τ=2. Thus a smooth rational support cannot occur: the same coherent identity would give 1=0. A reducible support cannot have rational normalization components in this setting, because each T_i was proved non-Kähler. Accordingly the number r in the statement is precisely the number of irreducible supports with τ=2.

## 2. Global Euler number and Betti numbers

The topological support of a scheme fibre equals that of its reduction. Additivity of Euler characteristic over the finite stratification C=(C\Δ)⊔Δ and multiplicativity for the differentiable bundle over C\Δ give

    e(Y)=e(C\Δ)e(F)+Σ_{c∈Δ} e((Y_c)_red)=Σ_{c∈Δ}τ((Y_c)_red)=2r.

Here Euler characteristic with compact supports can be used on C\Δ; the compact space Y has the same ordinary Euler number. There is no contribution from values outside Δ, since their fibres are smooth and τ=0. The top Chern class of the complex tangent bundle of the smooth compact Y is the Euler class of its oriented real tangent bundle, so ∫_Y c₃(TY)=e(Y). This is the meaning of the numerical c₃(Y) in the statement.

It follows that e(Y)=0 exactly when every nonnegative τ(S_c) is zero. If additionally b₁(Y)=0, rational Poincaré duality in the closed oriented real six-manifold Y gives b₅=b₁=0, b₄=b₂=0 and b₆=b₀=1. Hence

    2r=e(Y)=2−b₃(Y),  so b₃(Y)=2−2r≥0.

Since r is a nonnegative integer, r is 0 or 1. These are the claimed values; no existence statement for both possibilities is added.

## 3. Ambient line bundles pull back to the trivial bundle on the rational normalization

In the positive case choose one of the irreducible supports S with τ=2, and write η:T→S for its rational normalization. The surface T is smooth. For every A∈Pic(Y), the actual map i∘η:T→Y induces

    c₁((i∘η)^*A)=(i∘η)^*c₁(A)=0 in H²(T,Q).

A smooth rational surface has H¹(T,O_T)=H²(T,O_T)=0 and torsion-free H²(T,Z). One way to see the latter and its functorial transport is to take its projective minimal rational model (P² or a Hirzebruch surface), whose H² is free, and apply the integral blow-up decomposition H²(Bl_p T,Z)=π^*H²(T,Z)⊕Z[E]. The exponential sequence consequently gives an isomorphism c₁:Pic(T)→H²(T,Z). A rationally zero class in this free group is zero. Thus (i∘η)^*A is holomorphically trivial. This conclusion uses both the explicit pullback and the Picard/Chern isomorphism; numerical equivalence alone is not substituted for a line-bundle isomorphism.

Apply this first to A=K_Y^{-1}⊗L. Serre duality on T gives

    H²(T,K_T⊗η^*((K_Y^{-1}⊗L)|S))
       ≅ H⁰(T,η^*((K_Y⊗L^{-1})|S))^* ≅ C.

The last isomorphism uses a trivialization of that line bundle and connectedness of T. The assertion is an isomorphism of one-dimensional vector spaces, not a choice of canonical trivialization for every L.

## 4. The exact normalized-conormal map gives the ambient cotangent group

Write N*=O_Y(−S)|S for the conormal line of the reduced Cartier divisor S, V=Ω_Y¹|S, Q=Ω_S¹/Tor(Ω_S¹), and K=ker(V→Q). These are the exact inputs supplied by A.1.1 and the normalization map A.3; S is reduced even when the scheme fibre is mS.

For a normal-crossings equation F=x_1⋯x_r, the supplied A.1.2 isomorphism is

    η_*η^*N* → K,
    (a_i)_i ↦ Σ_i a_i (∏_{j≠i}x_j) dx_i,

with [F] trivializing N*. This gives the actual comparison of the direct-image line and the ambient conormal kernel; its change-of-equation compatibility is the one in the canonical A.3 map.

Let A=(K_Y⊗L^{-1})|S. The projection formula for the finite η and the line-bundle pullback of section 3 give

    K⊗A ≅ η_*η^*(N*⊗A),
    η^*(N*⊗A)=η^*((O_Y(−S)⊗K_Y⊗L^{-1})|S) ≅ O_T.

Therefore H⁰(S,K⊗A)=H⁰(T,O_T)=C.

For completeness, the differential pullback Ω_S¹→η_*Ω_T¹ has kernel exactly the torsion. Its kernel is zero on the dense regular locus of each component, hence is torsion; conversely a local non-zero-divisor on the reduced S remains a non-zero-divisor on every normalization branch, so it acts injectively on the locally free Ω_T¹ and the pullback kills every torsion section. Thus it induces the injective sheaf map

    Q → η_*Ω_T¹.

Tensoring this map with A and taking H⁰ gives an injection

    H⁰(S,Q⊗A) → H⁰(T,Ω_T¹⊗η^*A)=H⁰(T,Ω_T¹)=0,

where the last equality is the vanishing of holomorphic one-forms on the rational surface. The exact sequence 0→K→V→Q→0 then induces the isomorphism

    H⁰(S,V⊗A) ≅ H⁰(S,K⊗A) ≅ C.

This is the second group of C.NC.11 for every L∈Pic(Y). No restriction-surjectivity property from Pic(Y) to Pic(S) is asserted or needed. Nor is the normalization group identified with the ambient group without the displayed K and Q maps.

## 5. Multiplicity, CDP domain, and conclusion

The full scheme fibre may have multiplicity m. All cotangent/conormal maps just used are attached to the reduced S and its normalization; the ambient line O_Y(−S) is available independently of m. Nothing in the argument forces m=1. The original concluding sentence denying such a force is a scope observation, not an extra hypothesis in this derivation.

For a holomorphic algebraic reduction under the CDP setup, the smooth-domain form of C.3.1 supplies the smooth compact Y and the general-fibre Euler number zero. C.3.5 supplies precisely the Euler stratification identity for these fibrations. The old safe statement snapshot of C.3.1 has the broad words 'compact complex threefold'; the currently completed source explicitly says smooth, and this derivation uses that actual smooth domain. It makes no verification claim for a singular ambient Y and asks for no duplicate edit to the already corrected C.3.1. The earlier full necessary-list exclusions are not needed to recompute e(F)=0: that value is the exact cited input.

All conclusions of 01CC have now been derived with the given hypotheses and exact maps. No target proof or target computation was opened before writing this record; no additional independent numerical/computation event is asserted.

# Fresh derivation of 01GD / cdp:st:D.2.6

Checker: restore_build, GPT-6 Astra (OpenAI), ChatGPT Pro mode.

The target statement packet and its empty reference supplement have been read. The separately authorized dependency 01GA/cdp:st:D.2.3 has now been independently derived, frozen, released and completely compared; its analytic logarithmic de Rham machinery and full proof are permitted inputs for this subsequent check. I have also opened the original Steenbrink scan and the version-bound Bierstone–Milman primary resolution statement. No GD target proof, old target check, or target proof argument has been opened. Root has disclosed only that the target contains a legacy D.18–D.19 reference pair, for later locator transport; no sentence containing that pair has been supplied.

## 1. Exact objects and a proper normal-crossing model

The given h:U→Δ is proper, U is a smooth complex threefold, and h is smooth over Δ* with connected two-torus fibres. The integral H¹ monodromy is identity. Fix its integral marking and put V=H¹(U_t,C), a fixed four-dimensional complexification of a real marked space. The period plane W_t consists of classes of holomorphic one-forms, so the target is to extend W_t holomorphically with W_0⊕bar(W_0)=V and then extend its relative Albanese group family.

Only one connected component U⁰ of U meets h^{-1}(Δ*). Indeed, the proper submersion over the connected punctured disc is a locally trivial differentiable bundle with connected fibres, hence its total space is connected. Components of the smooth manifold U are open and closed. The restriction h⁰:U⁰→Δ is proper and surjective, and the inclusion U⁰→U is a biholomorphism on every fibre with t≠0. Any other connected component is contained in h^{-1}(0) and has no effect on the given punctured family or its periods. This specifies the exact map used to choose the dominating component.

Its reduced central divisor D=(h⁰{}^{-1}(0))_red is compact. Apply Bierstone–Milman, arXiv:alg-geom/9508005v2, 16 August 1995, §0.2(2), printed p.3, Theorem 1.6 and following paragraph, printed p.5, with Remarks 1.7, pp.5–6. The actual primary pages were viewed and hash-bound before this derivation. Theorem 1.6 applies to the compact embedded analytic space D inside U⁰. It gives a finite composite of ambient blowups with smooth centres

π:Ũ→U⁰

such that Ũ is smooth and the final strict transform of D together with the exceptional divisor has normal crossings. Each centre lies in the successive strict transform of D or its intersection with the existing exceptional divisor; in particular every centre lies over D. Thus π is a biholomorphism over U⁰\D. The blowups are proper, so ĥ=h⁰∘π is proper, and its central divisor has the form Σm_iD_i with normal-crossing reduced support. Its multiplicities are the actual positive vanishing orders of h⁰∘π; no reduction of those multiplicities is made.

For t≠0 the exact fibre map π_t:Ũ_t→U_t is a biholomorphism. Pullback by π_t identifies the holomorphic forms and integral cohomology, preserves cup product, and intertwines monodromy. We will construct the period extension using ĥ and then transport it back through these fibre maps. This uses the preprint page numbers just specified; no equality with a journal-page locator is assumed.

## 2. A holomorphic marked vector of top-form periods

Write θ=dĥ/ĥ and L^•=Ω^•_Ũ(log D)/(θ∧Ω^{•−1}_Ũ(log D)). The already checked analytic input supplies the following exact objects.

First, L¹ is locally free of rank two and L² is an invertible sheaf: in a normal-crossing coordinate chart ĥ=product x_i^{m_i}, θ=Σm_i dx_i/x_i spans a direct summand of the absolute logarithmic cotangent bundle. Proper coherence and torsion-freeness make M=ĥ_*L² free of rank one on a sufficiently small disc, since h⁰ of a smooth torus canonical bundle is one. Choose a generator α. It restricts to a nonzero translation-invariant top form on every punctured fibre, so its zero divisor is Σa_iD_i with a_i≥0. At least one a_i<m_i, since otherwise the actual holomorphic section α/ĥ would contradict primitivity of the generator M.

Second, Steenbrink §2.1, Theorem 2.18, §2.19, Proposition 2.20 and Theorem 2.21 give the locally free logarithmic de Rham bundle H²=R²ĥ_*L^•, its connection, full central-fibre base change, residue spectrum in [0,1), and exp(−2πiR)=T₂. These analytic assertions and their exact morphisms were read and checked in the GA derivation. The natural cup map Λ²H¹(U_t,Z)→H²(U_t,Z) is an isomorphism for a real four-torus, using lattice-dual invariant forms and the coordinate two-tori. It commutes with parallel transport. Thus the given identity integral H¹ monodromy implies T₂=I.

Consequently R=0: all its eigenvalues vanish, and exp(−2πiR)−I=R q(R) with q(0)≠0 makes a nilpotent R with identity exponential zero. In a holomorphic frame the connection matrix A(t)dt/t has A(0)=0 and is holomorphic at zero. A holomorphic horizontal frame exists on a smaller disc.

The inclusion of L² in degree two maps α to a holomorphic section of H². Use the fixed cup-product isomorphism q:Λ²V→H²(U_t,C) to express this section as a holomorphic vector

v(t)∈Λ²V

in the horizontal marking. For t≠0 it is a nonzero generator of Λ²W_t. The isomorphism q is constant in the marking because it is the natural cohomological cup map. This is the precise transport from top-form periods to Plücker coordinates.

## 3. The limiting norm is strictly positive

Let Q be the fixed top-degree cup pairing on H², with the orientation induced by a smooth torus fibre. Put

N(t)=Q(q(v(t)),overline(q(v(t)))).

This is a real-analytic real-valued function of (Re t,Im t) on the whole small disc. For t≠0 de Rham comparison identifies it with ∫_{Ũ_t}α_t∧bar(α_t), which is positive. Its local density is a positive constant times |f|² in complex surface coordinates. It follows by continuity that N(0)≥0.

In fact N(0)>0. Suppose N(0)=0. Since N is nonnegative in a neighbourhood of zero and differentiable there, its real first derivatives at zero vanish: each directional derivative is both a right and a left derivative at a local minimum. The real-analytic Taylor expansion then gives N(t)=O(|t|²).

Choose a component with a_i<m_i and a generic point of that component away from the other branches. There are coordinates with ĥ=x^{m_i} and

α=x^{a_i}u(x,z_1,z_2) dz_1∧dz_2,

where u is a holomorphic unit. The coordinate change that absorbs a unit in ĥ is x↦x exp(log(u_0)/m_i), with its nonzero derivative, as explicitly verified in GA; here u_0 denotes the unit in ĥ, independently of the coefficient u of α. Fix a small (z_1,z_2)-polydisc and take one sheet x=ζ t^{1/m_i}. A positive constant c bounds the coefficient and local volume from below, so

N(t)≥c|t|^{2a_i/m_i}.

Since 2a_i/m_i<2, this contradicts the preceding O(|t|²) bound. Therefore N(0)>0. This argument needs neither an assumption on geometric genera of central components nor an invariant Kähler class. The norm identity, the primitive local order and the full logarithmic extension are the exact facts used.

## 4. Explicit extension from the Plücker vector to the period plane

For t≠0 the vector v(t) is decomposable and satisfies v(t)∧v(t)=0. The latter identity is holomorphic, hence holds at zero. The strict positivity just established implies v(0)≠0 and v(0)∧bar(v(0))≠0, because the cup pairing q is induced by wedge product in Λ^•V.

Here is the actual local inverse of the Plücker description. Choose a basis e_1,…,e_4 of V for which the coefficient p_12(0) of e_1∧e_2 in v(0) is nonzero. Write v=Σ_{i<j}p_ij e_i∧e_j. The relation is

p_12p_34−p_13p_24+p_14p_23=0.

On a small disc p_12 stays nonzero. Define the holomorphic vectors

w_1=e_1−(p_23/p_12)e_3−(p_24/p_12)e_4,

w_2=e_2+(p_13/p_12)e_3+(p_14/p_12)e_4.

Direct expansion gives p_12 w_1∧w_2=v: the first five coefficients are immediate, and the coefficient of e_3∧e_4 is (p_13p_24−p_14p_23)/p_12=p_34. Thus W(t)=span(w_1,w_2) is a holomorphic two-plane and equals the original W_t for t≠0. Equivalently, W(t) is the kernel of V→Λ³V, x↦x∧v(t); the displayed basis gives the exact inverse map in this Plücker chart.

At zero, v(0)∧bar(v(0))≠0 says that w_1,w_2,bar(w_1),bar(w_2) form a basis of V. Hence W(0)⊕bar(W(0))=V. Transversality is open, and it already holds away from zero, so the extended map lands in the stated domain T₂. Glue this germ to the given map on Δ* along their identical overlap. This produces the extension on the original disc, not just on the temporarily smaller disc used for the local calculation.

## 5. The actual extended Albanese quotient

Let Λ=H_1(U_t,Z). Its marking is dual to the given integral H¹ marking by the universal coefficient pairing. It is a constant rank-four lattice. Let W⊂V⊗O_Δ be the extended holomorphic rank-two subbundle and let E=W^* be its holomorphic dual bundle. Define, for each γ∈Λ, a holomorphic section ι(γ) of E by

ι_t(γ)(ω)=⟨ω,γ⟩,  ω∈W(t).

This specifies the period-lattice embedding; it is not an unspecified quotient identification. Its real-linear extension Λ_R→E_t is injective: a real cycle functional that vanishes on W(t) also vanishes on bar(W(t)); transversality then makes it zero on V. Both real dimensions are four, so the map is a real-linear isomorphism. Therefore ι_t(Λ) is a full lattice in E_t for every t, including zero.

The action γ:(t,z)↦(t,z+ι_t(γ)) is holomorphic, free and properly discontinuous on E. For the last assertion, on a compact subset of the base the least singular value of the real-linear isomorphism ι_t is uniformly positive. A translation that meets two fixed compact subsets must therefore have bounded lattice coordinates, leaving only finitely many possible γ. The quotient

A=E/ι(Λ)

is consequently a complex manifold, with a smooth holomorphic projection A→Δ. Addition, zero and inverse on E descend to holomorphic group operations. Each fibre is a compact complex two-torus.

The projection is proper. For any compact K⊂Δ, choose a fixed integral basis γ_1,…,γ_4 of Λ. The continuous map

K×[0,1]^4→E|_K,  (t,s)↦Σ s_jι_t(γ_j)

has compact image whose image in A is all of A|_K. The Hausdorff quotient therefore has compact inverse image of every compact K. This proves the required properness directly.

Over Δ*, the period map identifies W_t with H⁰(U_t,Ω¹_{U_t}) by the actual de Rham class map. Holomorphic forms on a torus are translation invariant and closed, and their classes are linearly independent by integration over the marked cycles; the map is a fibrewise isomorphism and hence a holomorphic bundle isomorphism. The Albanese group of a complex torus is H⁰(Ω¹)^*/H_1(Z) under this evaluation pairing. Consequently the above evaluation map identifies A|_{Δ*} with the given relative Albanese group family, fibrewise and holomorphically. This proves exactly the asserted group-family extension.

No extension of a morphism U→A is constructed or needed. The maps used are the dominating-component inclusion, the resolution biholomorphisms π_t, the natural cup isomorphism q, the explicit Plücker chart, and the evaluation-lattice quotient. All of them have been given explicitly or derived from the cited primary resolution theorem at its exact analytic scope.

## 6. Freeze boundary and evidence scope

The new derivation is complete before opening the GD target argument. Its primary inputs are the checked GA logarithmic construction and the newly read version-bound embedded-resolution theorem. The norm positivity argument and the Plücker/evaluation maps were worked out here from those inputs. No polarized period-extension theorem, target proof text, or old target computational routine was used. A separate freeze must precede target release; only the subsequent complete comparison can support a proposed check event.


## Exact input bindings

Manifest: agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GD_input_bindings.json

SHA-256: 695ef5b90c7bb2a3f23e300065ea4994fdf93846a1272446d0ffd619f40b85fe

The manifest binds the original statement packet, its supplement, the completed GA comparison and actual primary readings, and the newly viewed version-bound resolution pages. It was saved while the GD target proof was still closed.

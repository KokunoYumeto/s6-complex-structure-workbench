# S6_4_MAPS: the maps from the complex S^6 to S^3, S^2 and S^4 given by its torus fibration, and their homotopy classes

Development prompt, 12 November 2026. File prefix for your deliverables: `S6_4_MAPS`.

## What is to be settled

X is the compact complex threefold of [AC26] and [E26], diffeomorphic to S^6, with f: X → P¹ whose regular fibres are 2-tori with H₁ = Λ = Z⁴. [E26] Remark 8.3 describes the fibrewise quotient by the 3-torus of the monodromy-invariant rank-three sublattice: "the quotient map is a map S^6 → S^3", with a Seifert picture (a multiple circle of multiplicity 3 over 0 and 4 over 1). It gives no homotopy class, and it says that over the fibre at ∞ the quotient "extends continuously to the composition of the moment mapping with a further quotient to a circle".

Where the matter stands (survey F9, F10, F23, F24):

1. The workbench constructs the circle quotient exactly and proves that the literal quotient does not extend continuously over the cusp fibre W (`workbench/cusp_globalization_replacement.tex`, Theorem `cusp-spec-globalization-obstruction`, parts (i), (iv), (v); proof l. 293-349, 443-502, 551-657; 3 September 2026, before [E26]). AI-produced; two readers of the survey re-derived the non-extension. So Remark 8.3 holds up to homotopy and not as worded.
2. The workbench proves that a cusp collapse map H: X → S⁴ is the non-zero element η₄η₅ of π₆(S⁴) = Z/2 (`workbench/higher_rung_24d_continuation.tex`, Theorem `h24:ret:main`, l. 4378-5107), proves a map q̂₃: X → S³ null-homotopic, and leaves open two classes, one of them equivalent to the class of Engel's map (`workbench/cusp_sphere_route_strengthening.tex`, l. 661-676; `workbench/cusp_cone_sphere_routes.tex`).
3. Sketches by a reader of the survey, checked by no one: the class of Engel's map e: S^6 → S^3 is the element of order two of π₆(S³) = Z/12, and f: S^6 → S² is null-homotopic (`notes/C1_notes.md`, C1-1, C1-2, C1-5).
4. Not done anywhere: an explicit handle decomposition of X adapted to f (the course proves X ≅ S^6 only through the h-cobordism theorem and Θ₆ = 0: `course/integral-homology-and-sphere-recognition.md`); the same maps for the other torus-fibred complex structures on S^6 (Viaclovsky arXiv:2609.33785, 2610.39102; Liu-Rollenske arXiv:2609.33826).

This prompt asks for the theorems: the maps constructed, their homotopy classes computed by two independent methods, and the cell structure made explicit.

## What the outcome must be

1. **Deliverables:** the files listed under "What to deliver" below; `S6_4_MAPS_results.csv` has one row for every item (A.1, A.2, …).
2. **What counts as done for an item:** (a) a theorem with a complete proof (for a homotopy class: the class named in a stated presentation of the group, with the framed-bordism or obstruction-theoretic computation written out and every convention fixed; for a diffeomorphism type: the classifying invariants computed and the classification theorem cited by number and applied; for a construction: the charts, the gluing, compactness and smoothness proved); or (b) a refutation with the located error and the correct statement proved; or (c) partly settled: what is proved, what was computed by program, and the exact undecided instance.
3. **Not acceptable:** "it should be η³"; a heuristic count of Betti numbers offered as a homology computation; "immediate corollary" without the construction; a list of numerical coincidences; a search reported without its code and its bounds; a plan; an item dropped without a row.
4. **Finished** only when every item meets the bar of 2; anything short of it is reported as unfinished, item by item.
5. If the execution environment fails, follow the last section of this prompt.

## Leads (unverified; prove or refute each)

From the survey and the readers' notes `notes/C1_notes.md` (with the script `notes/scripts/C1_check_invariants.py`) and `notes/A1_notes.md` (A1-1, A1-8).

- **Lead 1 (the Seifert picture).** Hom(Λ, Z)^Δ = Zε_γ; χ_γ([z, Π(z)x]) = ([z], ε_γ(x) mod Z) is a fibrewise group epimorphism f⁻¹(B°) → B° × R/Z with kernel the T³-family of L = Z⟨û, ŵ, δ̂⟩. At p_j the filling generator shifts the character by κ_j/m_j (κ₁ = 1, κ₂ = −1), so χ_γ descends to a T³-bundle over a Seifert solid torus with a central circle of multiplicity m_j. The glued 3-manifold M over B minus the cusp disc is the exterior of the torus knot T(3,4) in S³ (π₁(M) = ⟨x, y | x³ = y⁻⁴⟩); filling along the slope of the cusp gives Q with Q ≅ S³ exactly when |p| = 1. The character has no continuous extension to W: at a triple point it behaves like −log|z₂|/log|t|, and the points x_T(a) with a = (−1/4, 1/4) and a′ = (−1/2, 1/4) converge to the same triple point with values 3/4 and 1/2. There is a continuous map e: X → Q that is the literal quotient away from a neighbourhood of W.
- **Lead 2 (the class of e).** A regular fibre of e is a coset of the L-torus in a regular fibre F of f. Let d ∈ [F, SO] = KO⁻¹(T⁴) be the difference between the framing of TX|_F by translation-invariant fields and a lifted base frame, and the stable framing of S^6. d is invariant under the monodromy group; its image in H¹(F; Z/2) lies in H¹(F; Z/2)^Δ = {0, ε_γ mod 2}, which restricts to 0 on L; 2d lies in H³(F; Z)^Δ = Zδ̂ (by duality), which evaluates to 0 on [L]; so d|_L = 0, the fibre is the Lie-framed T³, whose framed-bordism class is η³ = 12ν ∈ π₃^S = Z/24, and [e] is the element of order two of π₆(S³) = Z/12 (the composite η₃η₄η₅). In particular e is essential.
- **Lead 3 (f is null-homotopic).** f = h ∘ e with h: S³ → S² the Seifert map (z₁, z₂) ↦ [z₁⁴ : z₂³], which is the Hopf map composed with a map of degree 12; a self-map of degree k of S³ acts on π₆(S³) by k and 12π₆(S³) = 0, so [f] = 0 in π₆(S²) = Z/12. Without e: f = [s₁³ : s₂⁴] for sections s_j of the topologically trivial bundles O(S_j).
- **Lead 4 (the vanishing torus).** In the local model t = w₀w₁w₂ the fibre 2-torus {|w_j| = ρ_j, arg t fixed} with its fibration framing is Lie-framed (Arf invariant 1) and represents η² ∈ π₂^S; hence the collapse map H: X → S⁴ of the workbench is η₄η₅ ≠ 0.

## Parts

Every Part asks for mathematics: a theorem with its proof, or a computation checked by program. Where a class or a construction resists, prove the strongest partial statement, compute, and state the obstruction exactly. Carry each Part to where it stops.

**A. The circle quotient and Engel's map.**
A.1. Prove or refute Lead 1 statement by statement, with the monodromy matrices and twist vectors of [AC26] Appendix A.1 (T l. 134-161 for the Setup on page 2) and with Engel's covector ε of his Lemma 3.8; identify M and Q; prove the non-extension at each of the three double curves and two triple points of W (the workbench says the character does extend along one of the three double curves, the fixed curve of Aut⁰ = C^*).
A.2. Construct a continuous (better: smooth) map e: X → Q ≅ S³ that agrees with the literal quotient outside a neighbourhood of W, prove that its homotopy class does not depend on the choices, and state exactly what [E26] Remark 8.3 should say. Do the same for general p, where Q is a lens space or a Seifert manifold: identify it.

**B. The homotopy classes.**
B.1. Compute [e] ∈ π₆(S³) = Z/12: prove or refute Lead 2. Write the Pontryagin-Thom argument completely (the regular value, the framed fibre, the comparison of framings with every convention fixed), and confirm the answer by a second, independent computation (for instance the e-invariant of the framed T³; or a framed bordism through the two Seifert solid tori and the cusp; or obstruction theory on a cell structure of X adapted to f).
B.2. Compute [f] ∈ π₆(S²) = Z/12: prove or refute Lead 3.
B.3. Prove or refute Lead 4, and deduce the classes of the workbench's maps: H: X → S⁴ (`h24:ret:main`), q̂₃: X → S³ (claimed null by an explicit framed nullbordism, `workbench/cusp_sphere_route_strengthening.tex`), q̂_γ: X → S² (recorded open; `notes/C1_notes.md`, C1-5, claims it is null), and q₁: X → C ≃ S² ∨ S³ (recorded open; by C1-1 it is determined by [e]).
B.4. The same maps exist for the other torus-fibred complex structures on S^6: Viaclovsky's two-parameter family (one multiple fibre of multiplicity 4, three reduced degenerate fibres), the family of Liu and Rollenske, and X_{3k,4l}. For each, determine the invariant sublattice, the quotient 3-manifold and the class of the resulting map S^6 → S³ in π₆(S³), as far as the papers give the data. Decide whether [e] is an invariant that distinguishes any of these fibrations.
B.5. An explicit handle decomposition. Build a handle decomposition (or a Morse function, or a CW structure) of X adapted to f, from the three special fibres and the T⁴-bundle over the pair of pants, with the attaching data explicit enough to recompute π₁ and H_* and to see the framed fibres of B.1; carry it as far as an explicit proof that X is a homotopy sphere, and say what would be needed for an explicit diffeomorphism with S^6.

**C. The local Kummer cover of the cusp.**
C.1. Prove or refute (`workbench/cusp_toric_cover_completion.tex`): after the base change t = v^N the source action with C_N(v) = C(v^N)/N makes the toric power map P_N(ξ₁, ξ₂, v) = (ξ₁^N, ξ₂^N, v^N) equivariant; it induces a finite flat map of degree N³ onto the completed cusp neighbourhood N₀ and a quasi-étale map of degree N², not flat, onto the normalization of the base change, whose non-flat locus is exactly the union of the double and triple strata. Decide whether these local covers extend to branched covers of X, and compute what they would be.

---


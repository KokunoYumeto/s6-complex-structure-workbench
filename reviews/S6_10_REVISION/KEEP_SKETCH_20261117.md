# What the S6 papers keep under the plan: a sketch (17 Nov 2026)

> **Erratum, 18 Nov 2026** (from the intake of S6_10_PAPERS checkpoint 06 by Claude Opus 5.5 at effort max, `s6_pro_prompts_20261112_work/intake/S6_10_INTAKE_20261118.md` section 5 item 8): the fan formula KL(S−1)(S−3)/8 below (the night run's P3K.31, P3K.33; lines 'The class on every fan' and the table) is false: S6_10 Paper IV §1.8 shows that on the original shorter T² loop the physical class is 26 where the polynomial gives 0. The fixed-edge flop rule −5A is replaced by 7A (Paper IV §1.9), and OS45 has physical reference class 3. The text below is kept as it was written.


By Claude (Fable 5.2 at effort high), agent ab096cc5de62cf843, 17 November 2026, about 13:00 UTC, for the user's
question "What would we keep approximately?". No sub-agents. Plan read: `LAYOUT_DESIGN_20261117.md`, version 3.
Worked from my intake (`reviews/S6_09_INTAKE_20261117/`: `INTAKE_S6_09.md`, `gazette_candidates.tsv`) and the
S6_09 inventory, by script (`scripts/s11_keep.py`, output `out/s11_keep.txt`). I read no further paper text.
Everything here is approximate: counts are by script on the inventory's kind and source columns and on section
page ranges from the `.aux` files; the split of sections into "kept" and "compendium only" is my judgement.

## 1. The series: five papers, not three

| Paper | For whom | Main statement | S6_09 material |
|---|---|---|---|
| **I. The (3,4,∞) family: periods, moduli and the two ends of the disc** | complex geometers | the family is classified with all its discrete data; its moduli is the disc 0 < \|w\| < 216; no limit exists at either end | Paper I without its appendices of re-derivations |
| **II. Torus-fibred threefolds with b₁ = b₂ = 0 and the argument of Campana, Demailly and Peternell** | the same, and readers of CDP | where the CDP argument fails, the exact criterion that replaces it, c₃ ∈ {0, 2} | Paper II; the unrestricted case as a marked second part (choice 2) |
| **III. Maps and manifolds from the construction** | homotopy theorists, 6-manifold topologists | [e] = 6ν′, f is null; the covers; the catalogue over the other elliptic surfaces; the conifold family | Paper III, sections 2-5 and 9, without sections 6-8 and the classical appendices |
| **IV. Smooth monodromy of holomorphic families of complex six-spheres** | differential topologists | class 0 in Θ₇ for the reference family; the class on every fan; a family whose class generates Θ₇ | Paper III section 8, the Θ₇ part of section 2, and Part 3 of the night run |
| **V. A complex structure on 3HP² # (−HP²)** | 8-manifold topologists, complex geometers | a compact complex fourfold fibred in 3-tori, three-connected, with Euler number 6, and its one-parameter family | Paper III section 7 and Part 1 of the night run |

**Recommendation on Paper III:** split it, and give Θ₇ its own paper. Reasons:
- Without the classical appendices Paper III is four unrelated subjects (maps, other manifolds, Θ₇, the fourfold),
  each with its own readers and its own main theorem. None of the four is used by another.
- The Θ₇ result is the one a differential topologist would cite, and after the night run it is no longer "the class
  is 0": it is "the class depends on the fan, and one family generates Θ₇". That needs its own opening.
- The night run adds about 290 pages of proofs to Θ₇ alone (its Part 3 notes, 1.1 MB of TeX at the papers' density
  of about 3.9 KB per page). Inside Paper III they would bury everything else.
- "Short" holds for the opening of Paper IV (about 10 pages), not for its body.
- The fourfold is the same case on a smaller scale: one theorem, self-contained apart from a pointer to Paper I.

Papers II-V each rest on Paper I for the family and its notation; Paper I's opening carries the rung 0 of the series.

## 2. Per paper

Rung 0 = the result and the mechanism, as a draft. Ids are the gazette's (run and statement number; the printed
number is in `gazette_candidates.tsv`). "Known" results are stated and cited, without proof.

### Paper I

**Main results kept (23), with draft rung 0.**
1. FAM B.2.1, with FAM A.2.1, A.3.1. *All discrete data.* The members X(c; w₁, w₂, σ) are classified by (|p|, e^{−πi(c+k₂)}). A biholomorphism covers the identity of P¹ and is affine on fibres with lattice map in the centralizer QI + Q(δ̂⊗γ) of the monodromy, so it can only shift c by an integer n; it extends over the order-four fibre exactly when n·δ̂ dies in Λ^{A₂}/N₂Λ = Z/4 ⊕ Z/2, that is for even n (corrected by k₂); even shifts exist because H¹(P¹, V) = 0 for the rank-two bundle of fibrewise translations.
2. FAM B.2.2, B.2.3. *Two classes at fixed u; Engel's Remark 8.1.* Engel's parameter is u = w², and X_c, X_{c+1} are not biholomorphic by (1); so the family with fixed sphere data lives over the w-disc and does not descend to the u-disc.
3. PUSH E.1.2, with FAM B.3.1. *Viaclovsky's X_{3k,4l}.* The same argument with norms kN₁ and lN₂ gives the identification subgroup 2klZ and 2kl classes at fixed u.
4. FAM B.4.2 and MAPS A.3.2. *Real structures.* The reflection of the base lifts to the periods with an explicit integral matrix, and the reflected twist data return to the standard ones only after an odd shift: the conjugate of X_c is X_{1−c̄}, antiholomorphic involutions exist exactly for w ∈ iR, in two classes, and each non-empty fixed locus is a 3-sphere fibred over a real arc of the base.
5. FAM C.1.1. *The missing period.* β^part = (6i/π) Log(ϑ₁(μ,τ)/(2√3·η(τ))), because ϑ₁/η transforms under the two generators of Δ(3,4,∞) by exactly the period laws of [AC26] and the cusp normalization fixes the constant; μ is the zero of ℘_τ.
6. FAM C.2.3, with ARI C.8.1-C.8.5 and PUSH E.4.1. *The radius.* max D_part = −(3/π) log 6, only at t = 1, so the family is 0 < |w| < 216. D_part is (6/π) log of the Siegel-function norm N of the section P, and N ≤ √2 at every zero of ℘ by three normalized duplication steps of the division identity (4); two interval certificates confirm it.
7. ARI C.4.2, C.4.4. *The division identity.* N(Q)^{m²} = N(mQ)·|Δ|^{(m²−1)/12}/|ψ_m(Q)| (the quasi-parallelogram law of the local height), so on the locus where P has order n, N¹² = |Δ|/|ψ_m(P)|^{12/(m²−1)}: algebraic values at all torsion points.
8. ARI C.2.1. *The Albanese curves of the multiple fibres* have nomes q₂ = iw/216 and q₁ = −w²/48³ = (27/64)q₂², by evaluating (5) at the two fixed points; the family is the punctured unit disc in q₂.
9. ARI C.6.3, C.8.15. *The eleven rational CM fibres* with their height identities; the norm has no critical point on the t-plane besides its maximum.
10. FAM F.1.1. *The monodromy group* is the kernel of an explicit character to Z/12 on the integral stabilizer of δ̂ (index 12): the kernel of ⟨A₁, A₂⟩ → SL₂(Z) is the normal closure of [A₁, A₂²], a Heisenberg lattice cut out by the same character.
11. FAM F.2.2, F.3.1. *Klingler's question.* The group does not act properly on Sp₄(R)/U(1,1): rational points of the null locus ψ(δ̂, Jδ̂) = 0 have infinite unipotent stabilizers and are dense in it. Off that locus the parabolic acts with compact stabilizers, ψ(δ̂, Jδ̂) = −6/D there, and the period map embeds the t-line properly.
12. FAM D.1.4, D.1.6. *The fibres.* NS(F_t) is the integer kernel of one period equation, with E² = −2 Pf(E); abelian fibres and elliptic quotients are read off the sign of the Pfaffian.
13. INV A3.1, with A2.2. *The Hodge table:* h^{1,1} = 2, h^{1,2} = 1. Leray for f reduces every h^{p,q} to cotangent direct images on P¹, and the one undetermined rank is decided by the scalar μ_s(z₂) = i·4√π/(3^{3/4}Γ(1/4)²) ≠ 0.
14. INV C1.1, C2.1, C3.3. *Frölicher, Bott-Chern, Aeppli.* With the Betti numbers of S⁶ the Hodge table forces the ranks of d₁: E₁ ≠ E₂ = E_∞; the Bott-Chern algebra is C ⊕ N with N² = 0.
15. INV A4.2. *Correction to [AC26] Remarks 9.21 and 1.3:* Ω¹_{X/B} has torsion exactly on S₁ ∪ S₂; along the cusp it is torsion-free and not locally free (local computation at t = xyz).
16. INV D4.5, with D4.1. *Twisted tangent cohomology* for every L ∈ Pic(X) = C: on the root curve P(3,4) the direct images of T_X ⊗ M_n are sums of O(d(n)), and for non-integral twists everything is supported at the finitely many fibres on which L is trivial.
17. PUSH A.3.2, with A.1.2, A.2.2. *Engel's Conjecture 8.2 is false as worded.* The pinched space Q has virtual Euler number 24 − 24 = 0, and a flat smoothing keeps the virtual Euler number, while X(u) has Euler number 2; the limits that do exist are two semistable fillings (a flop apart) and a nodal one, from the two-parameter Mumford fan.
18. PUSH B.4.19. *A partial filling.* After w = r⁶ the sphere family fills over (P¹ × Δ) minus the point (∞, 0), with a twelve-cycle in the central divisor.
19. PUSH B.4.33, extended by the night run P2.2, P2.7, P2.9. *No filling at w = 0,* for every admissible twist and every coprime (3k,4l), after any finite cover. A filling would give an origin of the torus torsor with zero radial class (the lattice modulo δ̂ has no invariant vector); the cusp fixes an origin whose radial class is −pn·γ̂ ≠ 0.
20. PUSH D.1.3. *No extension across |w| = 216.* j(Alb S₂) = J(iw/216) has the circle as natural boundary, and in any flat proper extension the Albanese curve of the anticanonical divisor would continue across it.
21. PUSH D.2.3, D.3.1, D.4.8. *The boundary object:* the Hausdorff reflection of the collapsed fibre, its Chabauty limits, and the level curves beyond the boundary.
22. FAM A.5.1, A.5.2, B.4.1 and PUSH E.2.1. *Stated as known* (DGKX v1), with our proof of the 2Z statement as a credited appendix; new is (1,1,1,0) for every coprime (3k,4l).
23. Open, in a last part: INV C3.8 (a literal coefficient atlas); ARI C.7 (transcendence of N at non-torsion points).

**Supporting results** (script, from the papers' `\Uses` lines): the 27 gazette rows of Paper I use 41 further
statements directly; the closure under "uses" is 98 statements, 95 of them ours. 199 of our 312 rows are not reached.
Ranges written "A--B" in a `\Uses` line count only their end points, so the closure is a lower bound.

**Known, to cite:** [AC26] (the construction, π₁ and H_*, K_X, Aut⁰, a = 1, the structure-sheaf direct images,
Lemma 9.2, Theorem 10.5 for the contradiction with CDP20 Cor. 2.3); Engel (the construction, Lemma 2.1, Cor. 2.2,
Prop. 2.4, 2.7, Remarks 8.1, 8.4, Conjecture 8.2); DGKX v1 (Theorem 1.4, Theorem 6.12, Prop. 6.16, Prop. 7.8, C.2);
Viaclovsky 2610.39102 (Theorem 1.1, Prop. 2.3, 4.7, the Questions); Yang; Oguiso-Shioda and Shioda (the
Mordell-Weil lattice and heights); Eichler-Zagier and Duke-Imamoglu; Kubert-Lang (Siegel functions); Tate and
Silverman (local heights); Gross-Zagier and Kolyvagin; DeMarco-Mavraki; Angella and McHugh; Buchdahl; Grauert;
Kuranishi; Illusie-Kato-Nakayama. 15 inventory rows are of kind "cited or re-derived".

**Moved out:** the four classical chapters of the appendix (chain constructions, CW models, path fibrations: 12 rows,
22 pp.); the working edition's re-derivation of [AC26]'s construction and topology (5 appendix sections, 53 rows,
65 pp.: known, so cited); second proofs and re-derivations (about 35 pp.); the routes that failed on the way to
B.4.33 and the first run's local analysis of the puncture (about 36 rows, 66 pp.: history); the concordance, program
and verification appendices (114 pp., to the records and the JSON).

**Pages:** 530 now. Kept from S6_09: about 255 (core sections 2-11: 72; arithmetic, sections 12-16: 67; circle
quotient and real forms: 9; the ends, sections 20-23 without the failed routes: 83; credited re-derivations: 15;
open points and records: 10). Added: an opening of about 20 pages (rungs 0-1), 8 pages from the night run.
**About 285 pages**, of which a reader of the opening reads 20.

### Paper II

**Main results kept (15).**
1. CDP A.1.1. *The omitted term.* For a reduced divisor S the kernel K of Ω¹_X|_S → Ω̃¹_S contains N* with quotient the torsion of Ω¹_S; under the two vanishings of CDP20 p. 692 the ambient sections are ker(δ_A: H⁰(Tors ⊗ A) → H¹(N* ⊗ A)), which need not vanish.
2. CDP B1. *A counterexample without S⁶:* (nodal cubic) × P¹ in a smooth family; both endpoint groups vanish for λ ≠ 1 and the ambient group is C for every λ, carried by the torsion along node × P¹.
3. CDP A.4.9. *CDP20 Prop. 7.3 is true,* with a new proof (unitary-flat differentials on every reduced fibre support); one implication of its printed proof is false.
4. CDP D.1.2. *The component count with monodromy:* r = 2g + s − 1 + t′ − b₁, because H₁ of the complement is the base's H₁ plus the coinvariants of H₁(F); this replaces CDP98 Lemma 3.2.
5. CDP C.3.1. *The general fibre* is a 2-torus or a Hopf surface with a = 0: c₁ = c₂ = 0 and χ(O) = 0 leave the Kodaira-Enriques list, and the corrected count excludes bielliptic, Kodaira, Inoue and elliptic Hopf fibres.
6. CDP C.2.G.1, in the form the night run re-proves (P4.58). *The sign.* For a torus fibration with b₁ = b₂ = 0 and irreducible or normal-crossings fibres: B = P¹, c₃ = Σ e(fibre supports) ∈ {0, 2}, b₃ = 2 − c₃. A support has Euler number 2 if its normalization is rational and 0 otherwise (the number of triple points in the normal-crossings case). So the CDP inequality c₃ ≤ 0 is reversed, and S⁶ sits at c₃ = 2.
7. CDP C4f, with C4a, C4b. *What replaces CDP20 Theorem 2.2.* H²(Y, T_Y ⊗ L) maps onto H²(S̃, K_{S̃} ⊗ η*(K_Y^{−1} ⊗ L)) for the normalization S̃ of a non-normal fibre support; generic vanishing holds exactly when Pic(Y) → Pic(S̃) is non-zero for each such support, and fails for every L when one of these maps is zero, as on X (Pic(X) → Pic(dP₆) is zero).
8. CDP C5b. *X itself:* h^q(T_X ⊗ M_n) in closed form; the map to H²(dP₆, K) = C has rank one exactly for n ∈ {−6, −3, −2} or n ≥ 0.
9. CDP D.2.5, D.2.7. *Trivial monodromy* forces c₃ ≤ 0, and equality occurs: an explicit threefold with H₁ = H₂ = 0, a = 1, fibres E × E, built from the line bundle O(R) on a blown-up surface, whose three singular fibres are a Kodaira and a Hopf surface meeting in an elliptic curve.
10. CDP E6, E7. *Stability.* If the Kodaira-Spencer tensor of a torus fibration over P¹ has rank two at one regular value, every small deformation keeps the fibration; so a = 1 on a neighbourhood of every known family on S⁶.
11. CDP E13-E15. *The other families:* (1,2,2,0) for the two-parameter and the Liu-Rollenske family, (2m+1, 8m+1, 6m+1, 0) for the combs, all with smooth Kuranishi germs, by the root-curve computation of Paper I.
12. PUSH E.2.23, E.2.24. *The (3k,4l) families are separated:* a disc of structures whose punctured part lies in one family has its centre in it (the pencil, the root charts and the cusp propagate by the identity theorem), so each family is open and closed in the space of complex structures on S⁶.
13. CDP E12, E17, E18; INV E2.4. *Corrections* of CDP98 Lemma 1.5, of the divisor-twisting lemma, and of the bound h⁰(T) ≤ 2 of Huckleberry-Kebekus-Peternell.
14. Night run P3K.36. *Correction:* the Liu-Rollenske family with fixed data closes up over u = w², not over the u-disc (the Albanese curve of its multiple fibre changes by q ↦ −q).
15. Open: INV E2.3 (the comb kernel splitting).

**Supporting results:** 44 direct uses; closure 116 statements (109 ours); 191 of our 300 rows not reached, 114 of
them in the unrestricted Euler-sign block (C.2.UN and its relatives).

**Known, to cite:** CDP98 and CDP20 (Theorems 2.1, 2.2, Prop. 7.3, Lemma 4.2); Lehn-Rollenske-Schinko; [AC26]
Section 10 (Lemma 10.3, Theorem 10.5, Lemma 10.7); Viaclovsky's two-parameter and comb papers; Liu-Rollenske; Wang;
the classification of surfaces of class VII and Kodaira's list; Gauduchon; Kuranishi in Meersseman's form; the
inverse-Jacobian results cited as GS2014. 12 rows are "cited or re-derived" (appendix A, 14 pp.), among them E3
(a ∈ {0, 1} on S⁶), which is CDP's and stays a citation.

**Moved out:** sections 7-12 (pp. 95-453, 358 pp., about 112 rows): the classification of all degenerations behind
the unrestricted sign theorem, which has one derivation (choice 2); the 14 pages of re-derivations; 47 pages of
apparatus.

**Pages:** 659 now. Kept: about 230 (sections 2-5: 48; section 6, which C4f uses: 44; sections 13-17: 93; the
appendix of local proofs: 41; open point: 3). Added: an opening of about 12 pages and the night run's proof of the
sign theorem for irreducible and normal-crossings fibres (its Part 4, 423 KB, about 105 pp.; it replaces the
normal-crossings section 9). **About 345 pages.** With the unrestricted part kept as a second part: about 700.

### Paper III

**Main results kept (10).**
1. MAPS A.2.2 and Paper I's circle quotient. *Engel's map S⁶ → S³* exists after a repair at the cusp; agreement with the literal quotient away from the cusp fixes no homotopy class.
2. MAPS B.1.2. *[e] = 6ν′ = η₃η₄η₅,* the element of order two of π₆(S³) = Z/12: by Pontryagin-Thom the class is that of a regular fibre, a Lie-framed 3-torus.
3. MAPS B.2.1. *f: X → P¹ is null-homotopic:* it factors through e and a map S³ → S² of Hopf degree 12, which kills π₆(S³).
4. MAPS B.3.1. *The cusp collapse map X → S⁴* is η₄η₅ ≠ 0: the vanishing 2-torus at a triple point is Lie-framed.
5. MAPS B.5.1. *A CW structure adapted to f,* with cell counts (5,20,45,56,42,17,3).
6. MAPS C.1.3. *The Kummer covers of the cusp* extend to no smooth branched cover of X.
7. MAPS D.1.1-D.1.11. *The universal covers* of the members with π₁ = Z/d: Euler number 2d, b₂ ≥ d − 1, their cohomology ring and diffeomorphism type; not connected sums of S³ × S³.
8. MAPS D.2.28, D.2.44-D.2.48, with the night run's P3F.34. *The other rational elliptic surfaces:* the sphere question on all 21 Mordell-Weil rank-one profiles, and the diffeomorphism classification of the minimal simply connected outputs.
9. MAPS D.3.1-D.3.3. *The conifold transition* of Engel's Remark 8.5: the moving-zero family, whose other side is S³ × S³ with a = 1.
10. MAPS E.2.1. *The fibre product with Engel's surface:* a fourfold with K = Π*L^{−5}, a = 2, not in class C, signature 2. Open: MAPS D.2.4.

**Supporting results** (for the old Paper III as a whole): 62 direct uses; closure 173 (161 ours); 92 of our 253 rows
not reached.

**Known, to cite:** Engel (Remarks 8.3, 8.5); Oguiso-Shioda; Wall, Jupp and Zhubr; Toda and the tables of
Isaksen-Wang-Xu for the stems used; Milnor, Kervaire-Milnor; Mumford 1972; Calabi-Eckmann and CDP98 Example 2.3;
Fujiki. 15 rows "cited or re-derived" for the old Paper III.

**Moved out:** appendices C to AI (pp. 477-891, 253 rows, 415 pp.): Thom and Euler classes, Chern classes, duality,
Pontryagin-Thom, Morse functions, handle cancellation and slides, the Whitney trick, the Adams spectral sequence
computation of the stable 6-stem, the framing obstruction, sphere twists and Θ₆ = 0, almost complex structures and
the octonions. All of it is the course CG-S6 and classical; cited. Also 100 pages of apparatus.

**Pages:** 1,004 now. Kept in Paper III: about 300 (maps without Θ₇: about 12; Kummer 4; other manifolds 166; fibre
product 52; cusp carriers 68, see choice 3). With an opening of 10 pages: **about 310 pages**, 240 if the carriers go
to the compendium.

### Paper IV (Θ₇)

**Main results kept (6).**
1. PUSH C.3.24. *The reference family has class 0.* For the semifree circle action the class is an integer of the fixed-curve knot, (p_rel − 12 s_δ)/24, computed on the page surface (an elliptic surface over the genus-3 curve b³ = a⁴ + 1 with twelve nodal fibres): p_rel = −24, s_δ = −2. It vanishes because the section P never meets the zero section.
2. PUSH C.3.27 and MAPS B.6.24, as independent second and third proofs (a spin^c coboundary; the free-circle quotient after a conifold surgery), and the same value for every coprime (3k,4l).
3. Night run P3K.31, P3K.33, P3F.35. *The class on every fan:* KL(S−1)(S−3)/8 mod 28, S = a² − ab + b² for δ = av + bw: each flop of the periodic fan changes the stable framing by a fixed rule. The original periods on the fan with δ = v + 3w give class 3.
4. Night run P3K.23. *The fixed-edge flop* multiplies the index by −5 mod 28.
5. Night run P3K.10, P3F.21, P3K.22. *Non-trivial monodromy.* The Remark 8.5 family on OS45 (M = O(8G − O), Q = G) has index −3: class 25, a generator, so its finite covers realize all of Θ₇ and their mapping tori are not S¹ × S⁶. OS47 has 24.
6. Night run P3K.30, P3F.53 and the rows around them. *The table:* index χ − H/2 for every one- and two-cap page, over 16 profiles and 30 branches. The contents go in a table, as the plan says.

**Known, to cite:** Cerf, Smale, Kervaire-Milnor, Eells-Kuiper; Haefliger, Montgomery-Yang, Wall, Davis; Jin (the
Torelli group of S² × S³); Oguiso-Shioda.

**Pages:** from S6_09: section 8 (43 pp.) and the Θ₇ part of section 2 (about 38 pp.). From the night run: about 290
pp. of proofs. With an opening of 10 pages: **about 380 pages**, the largest of the five. The opening and the table
are what makes it "short".

### Paper V (the fourfold)

**Main results kept (5).**
1. MAPS F.2.5, F.2.6. *The manifold.* Rank-six monodromy (orders 5 and 4, one unipotent cusp of index one) with free affine lifts glues to a closed 8-manifold that is three-connected with χ = 6 and middle form 3⟨1⟩ ⊕ ⟨−1⟩: the lower blocks of the two matrices are exterior squares of companion matrices, which makes every torsion differential computable.
2. MAPS F.3.5, F.3.6. *The periods.* The system is the primitive exterior square of the genus-two pencil y² = x⁵ + λ³x + λ⁴ extended by a trivial line; P = p(ℓ ∧ H_dR), ℓ = ⟨dx/y⟩, is a rank-three bundle, the extension splits over it because H¹(P*) = 0 on the root curve, and a real shift c of the splitting makes it transverse to its conjugate.
3. MAPS F.3.7, F.4.1. *The theorem:* a compact complex fourfold fibred in 3-tori over P¹, diffeomorphic to 3HP² # (−HP²).
4. Night run P1A.1-P1A.6, P1.13, P1.17, P1.18. *The family:* K_M = h*L^{−6}, the Hodge table, h^q(T) = (1,1,1,2,0), a = 1, Aut = C × Z/2, members classified by the parameter on an exact half-plane, no real structures, no extension at either end.
5. MAPS F.2.39 and F.3.4, F.3.11. *The search:* the effective classification of rank-six data, and the exclusion of the polarized abelian-surface source.

**Known, to cite:** Wall's classification of 3-connected 8-manifolds and the 2026 reference for the homotopy-sphere
ambiguity; Mandal; Mumford and the Kuhn degeneration; the lattice algorithm cited as BHJ22; Achinger-Ogus.

**Pages:** section 7 of Paper III (75 pp.) and the night run's Part 1 (about 30 pp.), with an opening of 6 pages:
**about 110 pages**.

### Totals

| | S6_09 | Kept from S6_09 | New (night run, openings) | After |
|---|---|---|---|---|
| I | 530 | 255 | 30 | 285 |
| II | 659 | 230 | 115 | 345 |
| III (maps, manifolds) | 1,004 | 300 | 10 | 310 |
| IV (Θ₇) | (in III) | 80 | 300 | 380 |
| V (fourfold) | (in III) | 75 | 35 | 110 |
| Total | 2,193 | about 940 | about 490 | about 1,430 |

About 1,250 pages of S6_09 leave the papers (section 3). What a reader reads first is the five openings, about 60
pages in all. Method: page ranges of the sections from the `.aux` files, each section classed by the kinds of its
inventory rows; the night run's proofs by the size of its notes at 3.9 KB of TeX per page (the papers' own ratio);
openings at about 0.7 page per main result.

## 3. In the compendium only

| Kind | Rows | Pages | Papers cite it as |
|---|---|---|---|
| Classical and course material | 265 | 437 (I 22, III 415) | the literature, with locators |
| Known results re-derived: [AC26]'s construction and topology (working edition), the "cited or re-derived" rows | about 95 (53 + 42) | about 105 (I 80, II 14, III 11) | [AC26], Engel, DGKX v1, CDP; our 2Z proof stays in Paper I |
| The unrestricted Euler-sign classification (C.2.UN and relatives) | about 112 | 358 | choice 2 |
| Routes that failed and superseded local analyses (PUSH B.3, most of B.4.1-B.4.29, FAM E) | about 36 | about 66 | a sentence in the provenance |
| Second proofs beyond one per main result | about 15 | about 35 | named in the check record |
| Concordances, program lists, verification and provenance tables | none | 261 (I 114, II 47, III 100) | the records part (about 8 pp. per paper) and the JSON |

The classification by row is the inventory's own kind column, with one correction of mine: 53 rows of Paper I's
appendix count as "ours" there and are re-derivations of [AC26]. With it: ours about 812 rows, known about 95,
classical 265, open and record rows 12. The plan's first pass had 852, 67 and 265.

## 4. The night run (checkpoint 12, 17 Nov 11:49 UTC; 225 rows, still INCOMPLETE)

| Night-run rows | Go to | State |
|---|---|---|
| P3F.3-P3F.24, P3K.5-P3K.11 (class 0 on the reference fan, two more computations) | Paper IV, check record of result 1 | proved in the run |
| P3K.23, P3K.31, P3K.33, P3F.35 (all fans, the flop) | Paper IV, results 3-4 | proved in the run |
| P3K.10, P3F.21, P3K.22 (OS45, OS47, ten primitive-source families) | Paper IV, result 5 | proved in the run |
| P3K.24-P3K.38, P3F.36-P3F.53 (the table, OS49, weighted loops, minimal covers) | Paper IV, result 6 | proved in the run |
| P3F.54-P3F.56, P3K.40-P3K.45 (the E7 source loops, the half-source reflection) | Paper IV, result 6 | **waits for the final**: the report says the other fan transports and the remaining source-moduli loops are under proof |
| P3K.36 (Liu-Rollenske) | Paper II, result 14 | proved in the run; to be read before printing |
| P3F.34 (non-coprime OS49 caps) | Paper III, result 8 | proved in the run |
| P2.1-P2.9 (the corner for all twists; the coefficient −pn) | Paper I, result 19 | proved in the run |
| P2.10, P2.11; P5.1-P5.7 | Paper I, check records of results 17 and 22 (blind derivations) | proved in the run |
| P1.1-P1.19, P1A, P1B | Paper V | proved in the run; P1.18 has a numerical certificate |
| P4.1-P4.5 | Paper II, check record of result 9 | proved in the run |
| P4.6-P4.58, P4R | Paper II, the proof of result 6 | proved in the run |

None of these proofs has a reader other than the run. D.2.5 in its unrestricted form was not confirmed by the run.

## 5. Open choices for S6_10, with my default

1. **Three papers or five.** Default: five (section 1). If three are kept, Paper III still needs the Θ₇ and fourfold
   parts as separately readable parts with their own openings.
2. **The unrestricted sign theorem** (II Prop. 13.1 as printed; 358 pp.; one derivation; not confirmed by the blind
   run). Default: Paper II proves the theorem for irreducible and normal-crossings fibres, states the unrestricted
   theorem in its part for results with one derivation, and that part's proof is the compendium's sections 7-12,
   cited by tag. This is the one place where a new result's proof would sit outside a paper; the alternative that
   keeps the rule is a second part of Paper II of about 360 pages. The user's rule decides.
3. **Results of ours that no main result uses** (about 480 rows by the closure count, a lower bound; among them the
   cusp carriers, 68 pp.). Default: they stay in the papers, in the body after the chapters that the main results
   use, with their proofs as they are and no rungs 0-2 written for them. Only routes that failed and second proofs
   go to the compendium.
4. **Our re-derivations of known results.** Default: keep two in Paper I as credited appendices (the 2Z proof of the
   working edition, about 8 pp.; (1,1,1,0), about 8 pp.), because results 1, 3 and 16 rest on them and DGKX v1 is
   unrefereed and withdrawn from v2. Everything else is cited.
5. **How Paper IV states its results.** Default: results 3-6 go in the part for results with one derivation unless
   the writing run or a second reader re-derives P3K.33 and P3K.10; result 1 is checked (four derivations, two runs).
6. **The arithmetic of Paper I** (sections 12-16, 67 pp.: heights, CM fibres, transcendence). Default: it stays in
   Paper I, since results 6-9 are how the radius is proved; the conditional transcendence material (21 pp.) moves
   to the open part.
7. **Timing.** Default: freeze the S6_10 prompt after the night run's final, since Paper IV's result 6 is still
   growing.

## 6. The night run in the five papers (checkpoint 12, 17 Nov 2026 11:49 UTC)

Added 17 November 2026, about 13:30 UTC, by the same agent (Claude Fable 5.2 at effort high). Built by
`reviews/S6_09_INTAKE_20261117/scripts/s12_night_fold.py` from the run's results table (225 rows: 220 proved, 3 known,
2 refuted; report still INCOMPLETE). Placement is by statement id, the kind is from the run's own comparison columns,
and I set seven kinds by hand (P1.5, P2.2, P3F.2, P3F.34, P3K.36, P4.58, P5.x). I read the row text of about 40 rows
this morning and no proof to the end; the one-line contents below are the first 150 characters of each statement,
cut by script. "Proved" is the run's status: no row has a reader other than the run.

### 6.1 Counts

| Paper | Kind | Rows |
|---|---|---|
| I | background | 1 |
| I | confirmation of an S6_09 statement | 7 |
| I | new result | 4 |
| I | re-derivation | 6 |
| II | confirmation in restricted scope | 1 |
| II | confirmation of an S6_09 statement | 41 |
| II | correction of a printed construction of others | 1 |
| II | new result | 36 |
| III | correction | 2 |
| III | new result | 6 |
| IV | background | 1 |
| IV | confirmation of an S6_09 statement | 16 |
| IV | new result | 76 |
| V | background | 2 |
| V | confirmation of an S6_09 statement | 11 |
| V | correction of the night prompt | 1 |
| V | new result | 13 |

Every row of checkpoint 12 is new to the papers in one of these senses, so the table in 6.5 lists all 225. The six
rows marked "new at 12" are those that checkpoint 11 did not have.

### 6.2 Corrections, and how the text changes

No row of the night run contradicts a statement printed in S6_09. Five rows change what the papers must say.

| Row | S6_09 statement touched | Change to the text |
|---|---|---|
| P3K.31, P3K.33 (the class on every fan) | III Thm 7.28, Cor. 7.32, Thm 2.30, Thm 2.33, Prop. 7.35 and the abstract of Paper III: "the monodromy is zero in Theta_7" | Not wrong: they are proved for the reference fan, where S = 1. In Paper IV each of them gets the words "for the reference cusp fan of [AC26]" in its statement, and the all-fan theorem follows them. The abstract says: class 0 on the reference fan; KL(S-1)(S-3)/8 on the fan with delta = av + bw, S = a^2 - ab + b^2. |
| P3F.34 (non-coprime OS49 caps) | III Thm 4.20 (MAPS D.2.11), printed with the hypothesis gcd(n, 3k) = 1 | The printed theorem stands. The run's "disagrees" is with the one-line summary it was given ("general admissible n"). Paper III adds P3F.34 after it: for a free cap with n != 0, H_1 = H_4 = Z/abs(n) and H_2 = H_3 = Z/abs(n) + Z/g, g = gcd(3k, n, 3d); example (9,3,1). Remove any sentence that states the group formula without the coprimality hypothesis (to be searched in the D.2 summaries and the open-problem text). |
| P4.58 (the equality case of the sign theorem) | II Prop. 13.1 (CDP C.2.G.1): "an irreducible singular support has smooth minimal elliptic ruled normalization, or has normalization resolution of class VII" | In Paper II the theorem is stated for irreducible and normal-crossings supports with "or has smooth minimal Hopf normalization" (class VII with b_2 > 0 is excluded), and with "the Euler number of a normal-crossings support is its number of triple points". The unrestricted statement goes to the part for results with one derivation (choice 2 of section 5). |
| P3K.36 (Liu-Rollenske) | II Prop. 15.9 (CDP E14) and any sentence that speaks of the Liu-Rollenske family over the punctured u-disc | Prop. 15.9 (tangent cohomology of one member) stands. A new statement of kind "Correction", worded neutrally, with its locator in their paper: the family with fixed logarithmic vector e_4/4 closes up over u = w^2 and not over the u-disc, because e_4 is the logarithm of the scalar multiplier. Paper II refers to Paper I's result 2 (Engel's Remark 8.1) as the same phenomenon. To be read by a second reader before printing. |
| P2.2, P2.7, P2.9 (the corner for all twists) | I Thm 21.58 (PUSH B.4.33), stated for the sphere family | The theorem's statement widens: "for every admissible (3,4) twist and every coprime (3k,4l) family". Its mechanism sentence gets the coefficient: the radial class of the comparison of origins is -p n gamma-hat. The open point "whether the same holds for |p| > 1" leaves Paper I. |

Three rows correct our night prompt and nothing in the papers: P1.5 (the rank-three bundle is p(l wedge H_dR) with
the rank-four de Rham bundle; Paper III's proof already has it), P2.2 (the sign of the radial class), P3F.2 (the
plus sign of the reducible-fibre term in Shioda's height formula). They go to the record of prompts.

Not confirmed by the run, and to be labelled as such where printed: CDP D.2.5 in its unrestricted form (II Prop.
14.4; "unresolved in its unrestricted wording" at P4.5, P4.9, P4.13) and the sign theorem for fibres that are neither
irreducible nor normal crossings.

### 6.3 What each opening gains (draft rung 0)

- **Paper I.** Result 19 becomes: *No filling at w = 0, for every twist.* For every admissible (3,4) twist with
  integer p and every coprime (3k,4l) family, the punctured family has no proper Hausdorff analytic filling after any
  finite cover: a filling pins the origin of the torus torsor with zero radial class, the cusp pins it with radial
  class -pn gamma-hat, and p != 0. For p = 0 (the untwisted family) the class vanishes and the filling exists
  (P2.10). No new main result; results 17 and 22 gain a blind second derivation in their check records.
- **Paper II.** Result 6 is restated as in 6.2 and now has a self-contained proof (P4.6-P4.58, P4R). New result 14:
  *the Liu-Rollenske family lives over the w-disc, u = w^2:* one turn of u changes the Albanese curve of its multiple
  fibre from q to -q. Result 9 (D.2.7) gains a second derivation.
- **Paper III.** No new main result. Result 8 gains the non-coprime OS49 homology (P3F.34) and the OS49 topology at
  all orders (P3F.26-P3F.33).
- **Paper IV.** Four of its six main results are the night run's:
  - *The class on every fan.* With the periods and twists fixed, the cusp can be filled along any one-vertex
    periodic fan T(v, w); the member is again a complex structure on S^6, and the class of the w-loop is
    KL(S-1)(S-3)/8 mod 28, S = a^2 - ab + b^2 for delta = av + bw: each periodic flop changes the stable framing
    of the common exterior by a fixed rule (index A goes to A + (l/8)(S-1) - (k/8)(S^2-1)). For K = L = 1 exactly
    sixteen classes occur; the fan with delta = v + 3w gives 3.
  - *The fixed-edge flop* multiplies the index by -5 mod 28; after it the circle action has two isolated fixed
    points.
  - *A generator of Theta_7.* For the rational elliptic surface OS45 with M = O(8G - O), Q = G and one ordinary
    logarithmic gluing, the family over the punctured disc has index chi - H/2 = -3 on its page surface: class 25,
    a generator. Its finite covers realize every class, and for a non-zero class the mapping torus is not
    diffeomorphic to S^1 x S^6. OS47 with M = O(7G - O), Q = 2G has class 24.
  - *The table.* For every one- and two-cap page, k = -3H and l = -24 chi, so the index is chi - H/2; listed for
    16 source profiles and 30 branches, with the OS49 loops (classes 0 on the diagonal fans, every even class over
    all fans and orders).
- **Paper V.** New main result 4: *the family.* Every admissible member has K_M = h^*L^(-6), an explicit Hodge
  table (chi = 6, signature 2), h^q(T) = (1,1,1,2,0) and a smooth miniversal line; a = 1; Aut = C x Z/2; members
  are classified by the parameter on the half-plane Im xi > 1.0945... (an exact Frobenius period constant,
  certified); there are no real structures, and no analytic extension across either end. The mechanism is the one
  of Paper I one rank up: direct images on the root curve of orders 5 and 4. Results 1-3 gain a blind confirmation
  (P1.1-P1.14, P1.19).

### 6.4 Still running or open, and which paper waits

| Item | State at checkpoint 12 | Waits |
|---|---|---|
| The E7 source loops and their transport to other fans (P3F.54-P3F.56, P3K.40-P3K.45) | class 1 on the vertical-edge fan and on the reflected diagonal-flop fan are proved; "the other source-loop fan transports, remaining source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under their stated scope checks" | Paper IV, result 6 (the table). Results 1-5 of Paper IV do not wait. |
| Exhaustion of every construction allowed by Engel's Remark 8.5 | "remains under proof" (item 3.4) | Paper IV: the table is stated as the list of families computed, not as exhaustive, unless the final closes it. |
| CDP D.2.5 unrestricted | unresolved in the run | Paper II: no wait; label as in 6.2. |
| The final package (one paper PDF with all notes input, the results table, the report) | not delivered; the checkpoint's paper inputs only the five main part files | The S6_10 prompt takes the proofs from `notes/*.tex` of the final. Papers I, II, III and V can be prepared from checkpoint 12; Paper IV is frozen last. |

### 6.5 Every row of checkpoint 12

| Id | Content (first 150 characters) | Status | Paper: section | Kind |
|---|---|---|---|---|
| P1.1 | The finite homology monodromies have orders 5,4, respectively, and characteristic polynomials (T-1)^2Phi _5(T) and (T-1)^2(T+1)^2(T^2+1). For N=M_0-I  | Proved | V: the manifold | new result |
| P1.2 | The lower blocks of A,B are precisely the quotient representations of bigwedge^2(C_f^-1),bigwedge^2C_g in the supplied basis Q. The integral quotient  | Proved | V: the manifold | confirmation of an S6_09 statement Compared: MAPS F.3.5. |
| P1.3 | The two finite filling pieces have first integral homology mathbb Z^2 and mathbb Z^2oplusmathbb Z/2. | Proved | V: the manifold | new result |
| P1.4 | The genus-two pencil has one nodal fibre away from 0,infty, at lambda_*=-256/3125. Good reduction at 0,infty requires root orders 8,5. On this root or | Proved | V: the periods | confirmation of an S6_09 statement Compared: MAPS F.3.5. |
| P1.5 | The formula in the prompt with P the image of ell_0wedgemathcal H, and mathcal H the rank-two Hodge bundle, cannot produce a rank-three subbundle. The | Refuted | V: the periods | correction of the night prompt (not of S6_09) |
| P1.6 | There is an orientation-preserving diffeomorphism \[ bigl(3mathbb HP^2mathbin\#(-mathbb HP^2)bigr)mathbin\#Sigma^8 cong 3mathbb HP^2mathbin\#(-mathbb  | Known | V: the theorem and invariants | background (known, cited) |
| P1.7 | The integral H^1 monodromy of the pencil has a companion marking with finite pair (C_f^-1,C_g), and cusp product C_fC_g^-1. Its exterior-square quotie | Proved | V: the periods | confirmation of an S6_09 statement Compared: MAPS F.3.5. |
| P1.8 | With the corrected rank-three bundle P of P1.5, the supplied rank-six system admits a holomorphic lifted family F_c=(sigma+icalpha e)(P) on the punctu | Proved | V: the periods | confirmation of an S6_09 statement Compared: MAPS F.3.6. |
| P1.9 | The periodic Kuhn fan, in the marking S, gives a smooth proper holomorphic filling of the periods Z(q)=sI_3+C(q) for a sufficiently small disk. Its ce | Proved | V: the periods | confirmation of an S6_09 statement Compared: MAPS F.1.1; MAPS F.3.7. |
| P1.10 | For every real parameter c>-h_min the corrected construction gives a compact smooth complex fourfold M_c and a proper holomorphic map to mathbb P^1 wi | Proved | V: the theorem and invariants | confirmation of an S6_09 statement Compared: MAPS F.1.3; MAPS F.2.5; MAPS F.3.7. |
| P1.11 | The index-one central cusp fibre C has torsion-free integral homology with ranks (1,3,9,9,10,3,1). The collapse kappa:T^6to C has primitive image in e | Proved | V: the theorem and invariants | confirmation of an S6_09 statement Compared: MAPS E.1.3; MAPS F.2.5. |
| P1.12 | The fourfold M_c has torsion-free integral homology \[ H_k(M_c;mathbb Z)= mathbb Z,&k=0,8,\\ mathbb Z^4,&k=4,\\ 0,&k=1,2,3,5,6,7. \] In particular it  | Proved | V: the theorem and invariants | confirmation of an S6_09 statement Compared: MAPS F.2.5; MAPS F.2.6. |
| P1.13 | With the complex orientation the fourfold has \[ sigma(M_c)=2,qquad H^4(M_c;mathbb Z)cong I_3,1,qquad w_2(M_c)=0, \] and there is a diagonal integral  | Proved | V: the theorem and invariants | confirmation of an S6_09 statement Compared: MAPS F.1.2; MAPS F.2.5. |
| P1.14 | The constructed fourfold is orientation-preservingly diffeomorphic to 3mathbb HP^2\#(-mathbb HP^2). | Known | V: the theorem and invariants | background (known, cited) |
| P1.15 | The rank-six flat extension, as a complex flat bundle with its invariant line, has the following explicit algebraic connection model. Set omega_k=x^kd | Proved | V: the periods | new result |
| P1.16 | In the canonical splitting sigma_b of P1.15, \[ -1.0342766224163217994942488453783461&<h_b(1),\\ h_b(1)&<-1.0342766224163217994942488453783460. \] In  | Proved | V: the periods | new result |
| P1.17 | For the cusp marking S fixed in P1.1 and the corresponding Kuhn fan, none of the completed fourfolds in this family admits an anti-holomorphic automor | Proved | V: the theorem and invariants | new result |
| P1.18 | In the algebraic splitting sigma_b, the function h_b has its unique global minimum at the finite-root point lambda=infty. The minimum is the exact Fro | Proved | V: the periods | new result |
| P1.19 | There is an independent computation from the full global cellular complex. Its chain ranks in degrees zero through eight are \[ (4,26,87,162,200,156,7 | Proved | V: the theorem and invariants | new result |
| P2.1 | For the prescribed (3,4) construction with integral twists (l_0,l_1,l_2), put \[ b=4l_1+3l_2,qquad p=12l_0-4l_1-3l_2,qquad a=b-12l_0=-p. \] On the log | Proved | I: the ends: no filling at w = 0 | confirmation of an S6_09 statement Compared: PUSH B.4.18. |
| P2.2 | On q=Q^12, actual extending origins have lifts o&=binom-bmu s/2bs^2/24-bCs/12+l_0s/2+v(bs+U),\\ sigma&=-l_0z_gamma+binom6amu vvU+aCv-6av^2+6av. The se | Proved | I: the ends: no filling at w = 0 | new result; corrects a sign in the night prompt |
| P2.3 | There is a proper holomorphic partial filling over (Pp^1timesDelta_r)setminus\(infty,0)\ with smooth total space and reduced normal-crossing parameter | Proved | I: the ends: no filling at w = 0 | confirmation of an S6_09 statement Compared: PUSH B.1.1; PUSH B.1.2; PUSH B.4.18; PUSH B.4.19. |
| P2.4 | For every admissible (3,4) twist, the marked map f:X_ctoPp^1 extends meromorphically over every hypothetical proper Hausdorff analytic filling of a fi | Proved | I: the ends: no filling at w = 0 | confirmation of an S6_09 statement Compared: PUSH B.4.30; PUSH B.4.33; PUSH B.4.31. |
| P2.5 | The global monodromy on Lambda_Q/Qwidehatdelta has no nonzero vector with finite orbit. | Proved | I: the ends: no filling at w = 0 | confirmation of an S6_09 statement Compared: PUSH B.4.30; PUSH B.4.33; PUSH B.4.31. |
| P2.6 | In a smooth resolved proper filling carrying the marked base map, every parameter-central component dominating Pp^1 has zero normal-meridian lattice c | Proved | I: the ends: no filling at w = 0 | confirmation of an S6_09 statement Compared: PUSH B.4.30; PUSH B.4.33; PUSH B.4.31; PUSH B.4.32. |
| P2.7 | For every admissible (3,4) twist, the punctured family has no proper Hausdorff complex-analytic filling at w=0 after any finite parameter cover. This  | Proved | I: the ends: no filling at w = 0 | confirmation of an S6_09 statement Compared: PUSH B.4.30; PUSH B.4.33. |
| P2.8 | For (l_0,l_1,l_2)=(0,2,-1) we have p=-5, a=b=5, component cover y^12=t^8/(t-1)^3, and rotations 8,-3,-5 modulo 12. The descent and origins are H&=5s+U | Proved | I: the ends: no filling at w = 0 | new result |
| P2.9 | Every admissible logarithmic datum in the coprime (3k,4l) family of the supplied Viaclovsky construction has no proper Hausdorff analytic filling at p | Proved | I: the ends: no filling at w = 0 | new result |
| P2.10 | The untwisted family X(u) has a proper flat Hausdorff analytic filling at u=0. Its corner winding is zero. The filling is obtained from two projective | Proved | I: the ends: the untwisted limit | new result |
| P2.11 | The one-component central space specified in Engel's Conjecture 8.2 cannot be the central fibre of a proper flat smoothing with smooth fibres X(u). It | Refuted | I: the ends: the untwisted limit | confirmation of an S6_09 statement Compared: PUSH A.3.1; PUSH A.3.2. |
| P3F.1 | The torsion-free rank-one Mordell--Weil rows are exactly eight, and their Kodaira refinements give exactly twenty-one realized configurations. | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: MAPS D.2.1; MAPS D.2.2. |
| P3F.2 | The section-intersection formula has the positive local-correction term, and the primitive sections in the eight rows have intersection zero with the  | Proved | IV: the reference family: class 0 | background; corrects a sign in the night prompt |
| P3F.3 | The exact Torelli presentation is I(S^2times S^3)=Z aoplusZ b, with (k,ell)(a)=(1,4) and (k,ell)(b)=(8,8). | Proved | IV: the reference family: class 0 | new result |
| P3F.4 | The Hopf lift of every a-power extends over D^4times S^3; its specified sphere gluing is standard. | Proved | IV: the reference family: class 0 | new result |
| P3F.5 | The Haefliger formula applies to an actual Seifert surface. The compact elliptic page has characteristic class K=5F, so the determinant correction mus | Proved | IV: the reference family: class 0 | new result |
| P3F.6 | The two explicit degree-twelve maps of the same genus-three curve give respectively one I_12 fibre and twelve I_1 fibres. Both give chi(mathcal O)=1,  | Proved | IV: the reference family: class 0 | new result (the S6_09 row it was compared with is not decided by it) |
| P3F.7 | The actual circle orbit pair is (S^5,S^2), with fixed normal bundle mathcal O(-1)oplusmathcal O(-1) of weights (-1,+1). The specified conifold replace | Proved | IV: the reference family: class 0 | new result (the S6_09 row it was compared with is not decided by it) |
| P3F.8 | The actual equivariant family return has a typed Hopf-lift image in the Torelli group, and its clutched sphere is the displayed Hopf gluing. | Proved | IV: the reference family: class 0 | new result (the S6_09 row it was compared with is not decided by it) |
| P3F.9 | The resolved cusp orbit has a relative product comparison with a nodal elliptic neighbourhood times the marked gamma circle, retaining the stable oute | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: PUSH C.3.11. |
| P3F.10 | The actual regular-binding page has twelve nodal fibres and boundary T^3. Its circle-line square is s_delta=-2 and its relative Pontryagin pairing is  | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: PUSH C.3.21; MAPS B.6.10. |
| P3F.11 | The integer A=(4k-ell)/24 is independent of the equivariant normal trivialization and is additive. Six parameter loops give exactly six times the inte | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: PUSH C.3.26. |
| P3F.12 | The compact fixed-sheet torsor is smoothly translation-trivial through the specified I_12 model; the transported circle line differs from mathcal O(P- | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: PUSH C.3.21. |
| P3F.13 | The angular origin comparison is thetagamma+6theta(1-theta)delta and its full Q-deck line clutch has winding -12. The earlier complex corner attempt r | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: PUSH C.3.10. |
| P3F.14 | The inherited spin^c index of a fixed-sheet Hopf boundary is precisely chi(S,L_+), independently of the negative-weight normal line. | Proved | IV: the reference family: class 0 | new result |
| P3F.15 | The explicit cyclic action on the twelve labelled node charts extends by units and has the required twelfth-iterate gamma period and circle-line windi | Proved | IV: the reference family: class 0 | new result |
| P3F.16 | The actual labelled comb-smoothing parameter loop has identity smooth monodromy, by a single-valued radial trivialization of the entire glued family. | Proved | IV: the table of families | new result |
| P3F.17 | For coprime multiplicities (3k,4l) the regular-binding page has degree 12kl, Euler characteristic 12kl, signature -8kl, section-line square -2kl and r | Proved | IV: the table of families | confirmation of an S6_09 statement Compared: MAPS B.6.2; MAPS B.6.24. |
| P3F.18 | The two supplied one-logarithmic families have degree-four regular-binding page covers; their precise source and page fibre types are those listed bel | Proved | IV: the table of families | new result |
| P3F.19 | Yang Type B and Type C have explicit nontrivial cyclic quotients of their fundamental groups, excluding homeomorphisms to the six-sphere. | Proved | IV: the table of families | new result |
| P3F.20 | Wang's supplied threefold is simply connected with H_2=H_3=Z/2, as computed by the full integral exterior and clutch complex. | Proved | IV: the table of families | new result |
| P3F.21 | The weighted OS47 data M=mathcal O(7G-O) and Q=2G give an actual holomorphic sphere family over lambda=r^4. Its actual page has s_delta=-14 and p_rm r | Proved | IV: families with non-trivial class | new result |
| P3F.22 | The specified Hopf gluing has Eells--Kuiper invariant mu(lambda(f))=A(f)/28. It is a homomorphism to Theta_7, and lambda(b) is the generator with mu=1 | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: MAPS B.6.20; PUSH C.3.26; PUSH C.3.27. |
| P3F.23 | The positive OS47 r-loop has angular clutch thetagamma+2theta(theta-1)delta, hence one positive gamma turn; its fourth-root cusp deck gauge has windin | Proved | IV: the reference family: class 0 | new result |
| P3F.24 | The forward sphere mapping torus is (S^1times S^6)\#Sigma_Phi; both spin structures have Eells--Kuiper invariant mu(Sigma_Phi). A nonzero value exclud | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: MAPS B.6.25; PUSH C.3.24. |
| P3F.25 | The actual real trace gives A=(12s_delta-p_rm rel)/24=-Rcdot O, with both mapping-torus and bordism boundary reversals included. The original and copr | Proved | IV: families with non-trivial class | confirmation of an S6_09 statement Compared: MAPS B.6.2; MAPS B.6.21; MAPS B.6.24; MAPS B.6.25; PUSH C.3.. |
| P3F.26 | The explicit IV^*+II+I_2 source with M=mathcal O(G-O) and Q=3G has component-supported linearization divisor C_0. Its specified local fillings and ord | Proved | III: the other elliptic surfaces (OS49) | new result |
| P3F.27 | The positive OS49 loop over lambda=r^3 has actual cusp angular cycle K=3u+2gamma and retained line clutch of winding six on the sixth-root cusp cover. | Proved | III: the other elliptic surfaces (OS49) | new result |
| P3F.28 | The actual OS49 linearization gives the exact sequence 0to T^*Mto Mtomathcal O_C_0(-1)to0. Its iterates alternate the two components, and all the tran | Proved | III: the other elliptic surfaces (OS49) | new result |
| P3F.29 | For every OS49 cap order m=3k and invariant vector ell=n(1,-1,0,0)+ddelta with gcd(n,m)=1, the specialization indices are (m,k,k,m) and all four integ | Proved | III: the other elliptic surfaces (OS49) | correction (see 6.2) |
| P3F.30 | The actual quadratic norm morphism has target line N=Motimes T^*M=M^2(-C_0) and scalar lambda^2. It completes to X/mu_2, with transverse A_1 equation  | Proved | IV: the table of families | new result |
| P3F.31 | The explicit positive-diagonal OS49 filling over lambda=r^3 is a sphere family with positive-loop return index zero, oriented homotopy-sphere class ze | Proved | III: the other elliptic surfaces (OS49) | new result |
| P3F.32 | For the positive-diagonal OS49 filling, every cap order m=3k, numerator n=pm1, and integral delta twist gives a sphere family with zero positive-loop  | Proved | III: the other elliptic surfaces (OS49) | new result |
| P3F.33 | The explicit order-3k OS49 affine cap is free exactly when gcd(k,n,d)=1 and either 3nmid n or 3mid k. Every free cap gives fundamental group Z//n/, so | Proved | III: the other elliptic surfaces (OS49) | correction (see 6.2) |
| P3F.34 | For every free affine OS49 cap with nne0, let g=gcd(3k,n,3d)in\1,3\. Then H_1=H_4=Z//n/ and H_2=H_3=Z//n/oplusZ/g. The free cap (m,n,d)=(9,3,1) has H_ | Proved | III: the other elliptic surfaces (OS49) | new result (extends III Thm 4.20; see 6.2) |
| P3F.35 | Every one-vertex unimodular cusp fan is an integral-basis triangulation, and explicit periodic diagonal flops connect it to the vertical-edge fan whil | Proved | IV: the class on every fan | new result |
| P4.1 | Let V=operatornameBl_(0,0)(BtimesDelta), where B=E, let R be the exceptional curve, and put L=OO_V(R). The holomorphic quotient U=L^times/q^Z is a smo | Proved | II: the example with trivial monodromy | confirmation of an S6_09 statement Compared: CDP D.2.7. |
| P4.2 | The three markings and the principal-bundle clutch in the prompt define a smooth compact complex threefold f:YtoPp^1 with connected fibres, exactly th | Proved | II: the example with trivial monodromy | confirmation of an S6_09 statement Compared: CDP D.2.7. |
| P4.3 | Order the local fibre lattice as (a,c,b,d), where (a,c) are the cycles (1,i) in C_i. The regular-fibre inclusions induce the quotient maps \[ H_1(A)=L | Proved | II: the example with trivial monodromy | confirmation of an S6_09 statement Compared: CDP D.2.7. |
| P4.4 | The threefold Y has H_1(Y;Z)=H_2(Y;Z)=0 and pi_1(Y)=1. | Proved | II: the example with trivial monodromy | confirmation of an S6_09 statement Compared: CDP D.2.7. |
| P4.5 | For this example, \[ a(Y)=1,qquad c_3[Y]=0,qquad b_3(Y)=2, \] and the integral homology is free of ranks (1,0,0,2,0,0,1). | Proved | II: the example with trivial monodromy | confirmation of an S6_09 statement Compared: CDP D.2.7; CDP D.2.5. |
| P4.6 | Let X be a compact complex threefold with b_2(X)=0, and let F be a reduced compact normal-crossings divisor. We allow different local branches of one  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.NC.1; CDP C.2.NC.2; CDP C.2.NC.3; CDP C.2.NC.4; CDP . |
| P4.7 | Let f:Xto B be a proper surjective holomorphic map with connected fibres from a compact complex threefold satisfying b_1(X)=b_2(X)=0 to a smooth compa | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.NC.3; CDP C.2.NC.5; CDP C.2.G.1. |
| P4.8 | For a torus fibration in P4.7, an irreducible singular support with rational normalization has Euler number two; every other irreducible support has E | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.NC.3; CDP C.2.NC.4; CDP C.2.NC.5; CDP C.2.G.1. |
| P4.9 | In the requested irreducible and normal-crossing fibre classes, the complete sign, exact Euler values and normalization equality classification hold a | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP D.2.5; CDP C.2.G.1. |
| P4.10 | There is a smooth projective threefold Z with b_1(Z)=0 and a connected torus fibration ZtoPp^1 whose reduced special fibres are irreducible normal-cro | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.11 | There is a smooth compact complex threefold C with b_1(C)=b_2(C)=0, e(C)=0, and a holomorphic submersion CtoPp^1 whose fibres are primary Hopf surface | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.12 | In the torus-fibration setting of Part 4.2, let f^-1(b)=mS have irreducible reduced support. Then \[ omega_S^otimes msimeqOO_S,qquad chi(OO_S)=0,qquad | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.13 | Let a proper holomorphic degeneration of two-dimensional complex tori have smooth total threefold and central fibre mS with irreducible reduced suppor | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP D.2.5; CDP C.2.G.1. |
| P4.14 | The reducible-curve inference in CDP 2020, Proposition 7.3, printed p.~694, omits the two plane cubics \[ Z(Y^2-XZ)=0,qquad XY(X-Y)=0. \] They are red | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.15 | Let mS be an irreducible singular fibre in the setting of 4.2. Suppose its normalization T is smooth and dnu:T_Ttonu^*T_X has rank two away from finit | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.16 | For every integer ngeq1, the reduced hypersurface germ x^2-zy^n=0 cannot occur in a fibre of a proper holomorphic degeneration of complex two-tori wit | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.17 | For all ageq2 and ngeq1, the germ x^a-zy^n=0 is excluded in the setting of P4.16. Its affine nearby fibre has pi_1=0 and compact second-homology inter | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.18 | For ageq2 and b,cgeq1, the reduced germ x^a-y^bz^c=0 cannot occur with a common positive multiplicity in a torus degeneration with smooth total threef | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.19 | The germ y(x^2-zy^2)=0 has ramified conductor, of multiplicity two on each normalization component, but its affine nearby fibre is mathbb C^*timesmath | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.20 | Let mS be an irreducible fibre of a proper holomorphic degeneration of complex two-tori with smooth total threefold. Suppose the normalization of S is | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.21 | In the setting of Part~4.2, an irreducible singular support S with smooth rational normalization T has e(S)>0. | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.22 | In the setting of Part~4.2, an irreducible singular support S whose smooth normalization T is birationally ruled over an elliptic curve has e(S)ge0. E | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.23 | In the setting of Part~4.2, let an irreducible singular support S have smooth normalization T. If its minimal model T_0 belongs to class VII and b_2(T | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P5.1 | The sheaf E is locally free of rank two and is the pullback of the translation Lie bundle V on widehat B. There is an exact sequence labeleq:P5tangent | Proved | I: check record of the classification and deformation results | re-derivation (blind) of an S6_09 statement |
| P5.2 | On the root orbifold, \[ Vsimeqmathcal Oopluswidehat L, qquad R^qh_*mathcal O_Xsimeq bigwedge^q(mathcal Oopluswidehat L)quad(0leq qleq2). \] On B, the | Proved | I: check record of the classification and deformation results | re-derivation (blind) of an S6_09 statement |
| P5.3 | For every admissible c, \[ bigl(h^0(T_X_c),h^1(T_X_c),h^2(T_X_c),h^3(T_X_c)bigr) =(1,1,1,0). \] | Proved | I: check record of the classification and deformation results | re-derivation (blind) of an S6_09 statement |
| P5.4 | The germ of the c-parameter family at each admissible member is a miniversal deformation germ. The Kuranishi germ is a smooth disc. | Proved | I: check record of the classification and deformation results | re-derivation (blind) of an S6_09 statement |
| P5.5 | For every admissible twist of the (3,4) construction, \[ operatornameAut(X_c)=mathbb C/mathbb Zsimeqmathbb C^*. \] The parameter abmodmathbb Z acts by | Proved | I: check record of the classification and deformation results | re-derivation (blind) of an S6_09 statement |
| P5.6 | For fixed admissible twist data, X_csimeq X_c' precisely when c-c'in2mathbb Z. This fixes the integral period of c; the construction still permits an  | Proved | I: check record of the classification and deformation results | re-derivation (blind) of an S6_09 statement |
| P1A.1 | For every admissible member, its vertical translation bundle on widehat B and its first coherent direct image are \[ E_0=F^vee=mathcal Ooplus L^-1oplu | Proved | V: the family in c | new result |
| P1A.2 | The complete Hodge table of every admissible fourfold is the following, with rows indexed by p and columns by q: \[ h^p,q&0&1&2&3&4\\hline 0&1&1&0&0&0 | Proved | V: the family in c | new result |
| P1A.3 | For every admissible fourfold, \[ (h^0(T_M),h^1(T_M),h^2(T_M),h^3(T_M),h^4(T_M)) =(1,1,1,2,0). \] The complex parameter family has a nonzero Kodaira-- | Proved | V: the family in c | new result |
| P1A.4 | The fourfold has algebraic dimension one and \[ Aut^0(M)=mathbb C,qquad Aut(M)=mathbb Ctimesmathbb Z/2. \] In a fixed holomorphic splitting, two membe | Proved | V: the family in c | new result |
| P1A.5 | There is no such analytic extension across any finite boundary point of mathcal H, or across infinity. The same conclusion holds after any finite rami | Proved | V: the family in c | new result |
| P1A.6 | A holomorphic punctured-disc family whose fibres are all members of this fourfold family has an interior parameter limit. After a base change of degre | Proved | V: the family in c | new result |
| P1B.1 | Let N be an endomorphism of Z^6 with N^2=0, rank three, and primitive image. There is a unimodular basis in which \[ I+N= I_3&I_3\\0&I_3 . \] Its cent | Proved | V: the manifold | confirmation of an S6_09 statement Compared: MAPS F.2.1. |
| P1B.2 | A finite-order integral linear action on R^6 admitting a free finite affine torus lift has characteristic polynomial among exactly thirty-eight cyclot | Proved | V: the manifold | confirmation of an S6_09 statement Compared: MAPS F.2.2. |
| P3R.1 | Let W be a compact almost complex eight-manifold whose outward-oriented boundary is the homotopy sphere Sigma. In the presentation Theta_7=Z/28 fixed  | Proved | IV: the reference class: conventions | confirmation of an S6_09 statement Compared: MAPS B.6.9. |
| P3R.2 | The equation 6a=b in Z/28 has no solution for odd b. For b=2r, its solutions are exactly a=5r and a=5r+14 modulo 28. Thus the sixfold class alone leav | Proved | IV: the reference class: conventions | confirmation of an S6_09 statement Compared: MAPS B.6.1; PUSH C.3.4. |
| P4R.1 | For a proper holomorphic degeneration of complex two-tori with smooth total threefold and central fibre mS, where S is irreducible and reduced, the gr | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.2 | In the setting of Part~4.2, every irreducible singular support whose normalization is smooth and whose normalization morphism is bijective has nonnega | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.3 | In the setting of Part~4.2, let an irreducible singular fibre support S have smooth normalization nu:Tto S whose minimal model is ruled over a curve o | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.4 | In the setting of P4R.1, choose a positive small-loop monodromy A on Lambda=H_1(T^4;mathbb Z). For a suitable lambdainLambda, a positive meridian of t | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.5 | In the setting of Part~4.2, an irreducible singular support whose normalization is smooth and has a Hopf surface as its minimal model has nonnegative  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.6 | Let S be an irreducible singular support in Part~4.2, let nu:Nto S be its normalization, and let rho:Tto Nto S use the minimal resolution of N. There  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.7 | In Part~4.2, every irreducible singular support whose normalization has a resolution birationally ruled over a curve of genus at least two has nonnega | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.8 | In Part~4.2, every irreducible singular support whose normalization has a resolution with Hopf minimal model has nonnegative Euler number. The normali | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.9 | In Part~4.2, every irreducible singular support whose normalization has a resolution birationally ruled over an elliptic curve has nonnegative Euler n | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.10 | Let S be an irreducible reduced fibre support in Part~4.2. Suppose that its reduced singular curve C is irreducible and unibranch at every point, that | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.11 | Let S be an irreducible singular support in Part~4.2 whose normalization has ruled resolution, and suppose e(S)=0. In the double-horizontal-divisor ca | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.12 | Let Tto Nto S be the minimal normalization resolution of an irreducible support in Part~4.2 with ruled minimal model of positive base genus. Let r:Tto | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P5.7 | The independently derived values in P5.3--P5.6 agree with the corresponding statements in version~1 of Du--Guo--Kusakabe--Xie, emphOka Geometry and De | Known | I: check record of the classification and deformation results | background (known, cited) |
| P3F.36 | Let the marked rational elliptic source have either profile \(I_1^*+I_3+2I_1\) or \(I_1^*+IV+I_1\), and take the OS50 data \((a,b)=(6,2)\). Put \(M=ma | Proved | IV: the table of families | new result (the S6_09 row it was compared with is not decided by it) |
| P3F.37 | Let S be the minimal regular surface of \[ y^2=x^3+tx+1,qquad G=(0,1),qquad M=mathcal O_S(2G-O),qquad Q=G. \] Choose any one of its three nodal fibres | Proved | IV: the table of families | new result |
| P3F.38 | For the OS50 source \(I_1^*+IV+I_1\), use \(M=mathcal O(aG-O-L_0)\) and the simple whole zero at its \(I_1\) value. The following actual two-cap const | Proved | IV: the table of families | new result (the S6_09 row it was compared with is not decided by it) |
| P3F.39 | For any allowed one-vertex cusp fan, take the star core of P3F.36 or either star/IV core of P3F.38, retaining the other singular source values. Add an | Proved | IV: the table of families | new result |
| P3F.40 | Take any of the ten primitive-translation sources of P3K.22, with its specified line, simple whole zero and ordinary remaining source values. Replace  | Proved | IV: the table of families | new result |
| P3F.41 | For each of the four marked sources and the eight source/root sectors in the proof, let M=mathcal O(aG-O) and Q=bG. For every indicated root order m a | Proved | IV: the table of families | new result |
| P3F.42 | The six source/root sectors in the proof admit the displayed actual line and affine cap maps for every gcd(m,n)=1. Their parameter is lambda=r^m and t | Proved | IV: the table of families | new result |
| P3F.43 | For the type II profiles in rows 45, 47 and 55, with the marked primitive data M=mathcal O(dG-O), Q=G, the root orders m=6l+1 and m=6l construct the a | Proved | IV: the table of families | new result |
| P3F.44 | Every actual affine line lift on one of the constructed additive root sources is carried by the explicit source translation and line maps below to zet | Proved | IV: the table of families | new result |
| P3F.45 | Use any of the ten actual primitive-translation sources of P3K.22, with its marked line, translation G, and selected simple whole I_1 zero. Install fi | Proved | IV: the table of families | new result |
| P3F.46 | Let S be the minimal regular surface of \[ y^2=x^3+tx+t^2,qquad G=(0,t),qquad M=mathcal O_S(aG-O),qquad Q=bG. \] Use its I_1 fibre at t_c=-4/27 as the | Proved | IV: the table of families | new result |
| P3F.47 | On the minimal regular rational elliptic surface \[ y^2=x^3+tx-t,qquad G=(1,1), \] use M=mathcal O(aG-O) and the actual suspension translation -bG, fo | Proved | IV: the table of families | new result |
| P3F.48 | For the actual additive cores constructed in P3F.36, P3F.38, and P3F.41--43, P3F.46--47, add any finite collection of logarithmic caps at smooth or mu | Proved | IV: the table of families | new result |
| P3F.49 | At the quadratic I_1^* root and the good or reduced IV roots of P3F.36 and P3F.38, every extending affine source norm solution with the prescribed can | Proved | IV: the table of families | new result |
| P3K.1 | Let \[ R=mathbf C[u,w,X,v]/(uv-Xw),qquad Z=operatornameSpecR. \] Use the small resolution with charts \[ U_0=(u,w,z),quad X=uz,\ v=wz; qquad U_1=(X,v, | Proved | IV: the reference family: class 0 | new result |
| P3K.2 | Put \(B=mathbf C[u,v]\), \(R'=B[x,y]/(xy-uv)\), and \(J=(x,u)subset R'\). The module \(J\) is flat over \(B\). Its fibre at \((u,v)=(0,0)\) is the nor | Proved | IV: the reference family: class 0 | new result |
| P3K.3 | Let \(B=S^3times S^1\), let \(Ksubset S^3\) be the cusp circle, and set \(T=Ktimes S^1\). Give the trivial real normal two-plane bundle of \(T\) its o | Proved | IV: the reference family: class 0 | new result |
| P3K.4 | The free twelve-label construction of P3F.15, when applied to a reduced \(Q\)-central divisor with no stabilizers at its generic points, has multiplic | Proved | IV: the reference family: class 0 | new result |
| P3K.5 | The integral connecting class from the marked boundary \(T^3\) has square zero and pairs trivially with every extension of the page line. In particula | Proved | IV: the reference family: class 0 | new result |
| P3K.6 | Let one positive gamma turn denote the actual parameter cover whose angular clutch is P3F.13. The orbit family of this cover is the product \(Ytimes S | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: PUSH C.3.10; PUSH C.3.21; MAPS B.6.10. |
| P3K.7 | The real trace gives a spin bordism carrying the Euler line from the actual covered conifold return to a normal sphere bundle. Its index is zero. The  | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: MAPS B.6.2; MAPS B.6.17; MAPS B.6.21; PUSH C.3.15; PUSH C.3.. |
| P3K.8 | The same actual return index vanishes by a second calculation: vertical sphere quantization, an explicit marked cap switch, and acyclicity of the elli | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: MAPS B.6.2; MAPS B.6.21; PUSH C.3.27. |
| P3K.9 | For the rotating framing specified below, the one-gamma-turn return has Jin characteristic numbers \((k,ell)=(-6,-24)\). After removing an extending c | Proved | IV: the reference family: class 0 | confirmation of an S6_09 statement Compared: MAPS B.6.17; MAPS B.6.20. |
| P3K.10 | Let \(S\) be the minimal regular elliptic surface with section \(O\) whose affine equation is \[ y^2=x^3-3f(t)x+2g(t),qquad f=(t^2+1)^2+t,qquad g=(t^2 | Proved | IV: families with non-trivial class | new result |
| P3K.11 | Fix logarithmic orders \(3K,4L\), with \(gcd(3K,4L)=1\), and primitive logarithmic coefficients \(n_0,n_1\), so \(gcd(n_0,3K)=gcd(n_1,4L)=1\). For the | Proved | IV: the reference family: class 0 | new result |
| P3K.12 | In the rank-one Mumford model above a smooth elliptic source fibre, every double curve of the central cycle is elliptic and fixed by the line circle.  | Proved | IV: the table of families | new result |
| P3K.13 | In a retained nonzero-linearization \(I_n\) neighbourhood, the circle quotient is the mapping torus of the actual source translation. If its global or | Proved | IV: the table of families | new result |
| P3K.14 | Let \(S\) be one of the rational elliptic surfaces with \(rm MW(S)=mathbb ZG\). Write the generic Picard point of \(M\) as \(aG\), and the translating | Proved | IV: the table of families | new result |
| P3K.15 | Every smooth sphere member with the standard fixed sphere and normal circle weights \((-1,+1)\) has a semifree line-circle action. For a cyclic affine | Proved | IV: the table of families | new result |
| P3K.16 | For the whole-fibre \(I_1\) cusp construction of P3F.9, together with the actual nonzero-linearization affine caps of P3K.15, the delta orbit has a gl | Proved | IV: the table of families | new result |
| P3K.17 | The negative- and positive-diagonal OS49 families have equal actual return index for every cap order \(m=3k\), \(k>0\), every signed primitive twist \ | Proved | IV: the table of families | new result |
| P3K.18 | In the actual whole-fibre \(I_1\) orbit projection of P3K.16, every sphere member has primitive source-fibre multiplicities at every logarithmic cap.  | Proved | IV: the table of families | new result |
| P3K.19 | For the actual affine root-line caps of P3K.15 in the sphere orbit scope of P3K.16, the root fibre is reduced. A singular root fibre has no nontrivial | Proved | IV: the table of families | new result |
| P3K.20 | For a semistable multiplicative source fibre \(I_N\), a whole-fibre zero of order \(e\) has period determinant \(Ne\) and central Mumford fibre Euler  | Proved | IV: the table of families | new result |
| P3K.21 | In the established sphere orbit and root-line cap scope, a nonzero-linearization \(I_s^*\) source fibre can occur only with \(s=1\), a primitive quadr | Proved | IV: the table of families | new result |
| P3K.22 | For the following ten source profiles, let \(G\) be the marked primitive Mordell--Weil generator, put \(d=1/h(G)\), and choose \(M=mathcal O(dG-O)\),  | Proved | IV: families with non-trivial class | new result |
| P3K.23 | Consider one of the actual sphere families constructed above with a semifree fixed curve \(Fsimeqmathbb P^1\), whose complex normal bundle is \(mathca | Proved | IV: the class on every fan | new result |
| P3K.24 | For the family of P3F.37, put m=4l+3, lge0, and retain its actual parameter lambda=r^m. Its positive r-return satisfies \[ A(Phi)=-(3l+2),qquad mu(Sig | Proved | IV: the table of families | new result |
| P3K.25 | For each of the ten scalar-parameter families of P3K.22, retain its actual period group, cap gluing, physical delta circle, and positive scalar-parame | Proved | IV: the class on every fan | new result |
| P3K.26 | For every one-cap sphere family of P3F.37 and P3F.41--43, with the actual parameter lambda=r^m, the positive single r-loop has the same signed return  | Proved | IV: the table of families | new result |
| P3K.27 | For the ten primitive scalar families of K22, use the actual positive scalar loop, the standard vertical-edge cusp, and the normal product transported | Proved | IV: the table of families | new result |
| P3K.28 | For the actual two-cap sphere families of P3F.38, P3F.46 and P3F.47, retain their signed norms and write \[ D=m_0n_infty+m_infty n_0=varepsilonin\1,-1 | Proved | IV: the table of families | new result |
| P3K.29 | For the actual index-one cusp with its three complex double curves, use positive complex normal meridians \(m_i\) and the relative dual basis \(m_jcdo | Proved | IV: the class on every fan | new result |
| P3K.30 | For every actual page of P3K.26 and P3K.28, let \(M\) be its page-cover degree, \(h(G)=1/d\), and \(aG\) its marked line point. Write \(H=Ma^2/d\) and | Proved | IV: the table of families | new result |
| P3F.50 | Every sphere family obtained from a rational elliptic source with Mordell--Weil group \(mathbb Z\) in the uniformly expanding case of E26 Remark~8.5 h | Proved | IV: the table of families | new result |
| P3F.51 | Every fixed marked rational elliptic source with Mordell--Weil group \(mathbb Z\) in the surviving source profiles is covered by the source, line, cap | Proved | IV: the table of families | new result |
| P3K.31 | For every actual family and positive parameter loop of P3K.27 or P3K.30, retain its physical delta cocharacter and all exterior gluings, and use any a | Proved | IV: the class on every fan | new result |
| P3K.32 | Consider the actual source and root-cap data of P3F.36, P3F.38, P3F.41--43, P3F.46--47, and the primitive-source data of P3K.22. Retain any finite col | Proved | IV: the table of families | new result |
| P3F.52 | Fix one of the whole-fibre sphere source tuples of K20--21 and F36--51, its marked translating point \(Q=bG\), its generic line point \(aG\), a select | Proved | IV: the table of families | new result |
| P3K.33 | Retain the actual K11 construction with logarithmic orders \(3K,4L\), \(gcd(3K,4L)=1\), and either sphere datum \[ 4Ln_0+3Kn_1=varepsilon,qquad vareps | Proved | IV: the class on every fan | new result |
| P3K.34 | Retain the actual component-supported OS49 families of P3F.31--32, with \(lambda=r^3k\), \(k>0\), and cap vector \(n(1,-1,0,0)^t+ddelta\), where \(n=p | Proved | IV: the table of families | new result |
| P3F.53 | The fixed-source canonical scalar sphere families in the literal whole-fibre construction of E26 Remark~8.5, with rational elliptic source and Mordell | Proved | IV: the table of families | new result |
| P3K.35 | Write the actual source line as \(mathcal M=mathcal O(aG-O+D)\), with the prescribed vertical correction when it occurs, and the contracting source tr | Proved | IV: the table of families | new result |
| P3F.54 | For the marked E7 source \[ y^2=x^3+3r x^2+t x+1,qquad G=(0,1), \] the source together with its selected finite nodal zero has the exact parameter \[  | Proved | IV: the table of families | new result |
| P3K.36 | In the supplied Liu--Rollenske construction, retain the exact scalar \(u\) in its line action \(B_u=uB_0\), its good fourth root at the \(III^*\) sour | Proved | II: the other families (Liu-Rollenske) | correction of a printed construction of others (see 6.2) |
| P3K.37 | Keep the exact source, component line, cap and fans of F26/F29/K34: \(M=O(G-O)\), suspension by \(-3G\), source \(I_2\) at \(q=1/t=0\), cap order \(m= | Proved | IV: the table of families | new result |
| P3K.38 | Fix any of the thirty nonempty branches of P3F.53, including its actual source coefficients, vertical line divisor, logarithmic norms, affine cap maps | Proved | IV: the table of families | new result |
| P3F.55 | Let \[ f(s,rho)=(X,Y,R) =(s^2-rho^2,\ s(s^2-rho^2),\ rho): mathbb C^2longrightarrowmathbb C^3. tagCL.1 \] Give both complex spaces their complex orien | Proved | IV: the table of families | new result |
| P3F.56 | Use the exact marked E7 source of P3F.54, \[ y^2=x^3+3r(u)x^2+t x+1,qquad G=(0,1),qquad r(u)=frac1-2u^33u^2,quad t_0(u)=u^2-frac2u. \] Fix either actu | Proved | IV: the table of families | new result |
| P3K.40 (new at 12) | Retain the actual positive selected-cusp source loop of P3F.54 and P3F.56, with fixed sufficiently small scalar, the III-star cap, no logarithmic modi | Proved | IV: the table of families | new result |
| P3K.41 (new at 12) | Fix a marked rational elliptic source in the whole-zero selected \(I_1\) sphere catalogue, its actual source line, translation \(Q=bG\), logarithmic s | Proved | IV: the table of families | new result |
| P3K.42 (new at 12) | Retain the actual positive selected-cusp source loop of P3F.54 and P3F.56, with fixed sufficiently small scalar, the III-star cap, no logarithmic modi | Proved | IV: the table of families | new result |
| P3K.43 (new at 12) | Fix the marked rational elliptic source, actual line, translation \(Q=bG\), whole-zero selected \(I_1\), effective additive caps, and transported peri | Proved | IV: the table of families | new result |
| P3K.44 (new at 12) | Fix the actual OS49 source and component line \(M=mathcal O(G-O)\), suspension by \(-3G\), selected \(I_2\) cusp, good IV-star cap of order \(m=3k\),  | Proved | IV: the table of families | new result |
| P3K.45 (new at 12) | Retain the selected-cusp source family and positive \(rho\)-loop of P3F.54/P3F.56, with fixed scalar, the actual III-star cap, and no logarithmic modi | Proved | IV: the table of families | new result |
| P4.24 | In the setting of Part~4.2, let S be an irreducible singular fibre support with smooth normalization T. If the minimal model of T is a Hopf surface, t | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.25 | Every semi-log-canonical reduced fibre support in Part~4.2 has normal crossings. In particular, let rho:Tto Nto S be a resolution of the normalization | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.26 | In Part~4.2 every irreducible reduced fibre support has nonnegative topological Euler number. For a singular irreducible support, rational resolution  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.27 | Let \(S\) be an irreducible singular reduced fibre support in Part 4.2. Suppose that the minimal resolution \(Tto N\) of its normalization has a Hopf  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.28 | Let p lie on a reduced fibre support of Part~4.2. Suppose its reduced singular locus is a smooth curve near p, and its generic transverse plane-curve  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.29 | Let S be an irreducible singular support in Part~4.2 whose normalization has ruled resolution, and suppose e(S)=0. In the double-horizontal-divisor ca | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.30 | Let C be a compact irreducible reduced curve in the smooth threefold Y of Part~4.2. Suppose its normalization is an elliptic curve E, and every point  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.31 | Let S be an irreducible singular support in Part~4.2 whose normalization has ruled resolution, and suppose e(S)=0. In the double-horizontal-divisor ca | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.32 | An irreducible support in Part~4.2 has Euler number zero exactly in the following cases: it is smooth with a finite unramified torus cover, or it is s | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.33 | Let S be an irreducible singular support in Part~4.2, and let rho:Tto Nto S be its minimal normalization resolution. Then H^2(N,mathcal O_N)=0. If p=d | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.34 | An irreducible singular support with rationally resolved normalization and generic transverse ordinary triple point cannot have Euler number one. For  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.35 | No irreducible support with rationally resolved normalization has Euler number one. Consequently, in a fibration whose supports are all irreducible or | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.36 | Every irreducible singular support in Part~4.2 whose normalization has a Hopf minimal model has smooth minimal Hopf normalization and Euler number zer | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.37 | No irreducible singular support in Part~4.2 has normalization whose minimal resolution has a class-VII minimal model with positive second Betti number | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.38 | An actual irreducible support in Part~4.2 cannot have a singular planar reduced critical curve at a point at which every generic transverse germ is an | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.39 | Let S=(f=0) be a reduced hypersurface germ in a smooth threefold, with one-dimensional reduced critical locus C. Suppose that every generic transverse | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.40 | In the scope of Part~4.2 where every fibre support is irreducible or normal crossing, no irreducible support with positive-genus ruled resolution has  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.41 | At a point of an actual support in Part~4.2, suppose the entire reduced critical curve is the ordinary node C=\z=xy=0\ and both branches have generic  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.42 | In the requested global support classes, a positive-genus ruled-resolution support whose critical curve has generic type A_3 everywhere cannot have tw | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.43 | In the requested full-fibration classes, a support with positive-genus ruled resolution cannot have positive Euler number and generic transverse type  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.44 | In the remaining positive ruled case with generic transverse type A_3 on every conductor component, the horizontal section of the pole divisor is cont | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.45 | In an actual torus degeneration, a point of a planar singular critical curve cannot have generic transverse type D_4 along all its local branches. | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.46 | In the requested full-fibration classes, a support with positive-genus ruled resolution cannot have positive Euler number and generic transverse type  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.47 | Consider an actual torus degeneration at a point where the entire reduced critical curve is the three coordinate axes, with generic transverse type A_ | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.48 | At a planar three-branch critical-curve point with uniform generic transverse type A_3, the local conductor defect is at least ten. At an ordinary non | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.49 | At an ordinary three-axis critical-curve point with uniform generic transverse type A_3 and local defect nine, the normalization has rational singular | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.50 | In the requested full-fibration classes, no support with positive-genus ruled resolution has positive Euler number and generic transverse type A_3 on  | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.51 | Let S be an irreducible reduced support in the torus fibration of Part~4.2 with b_1(S)>0. Every local Milnor fibre of a reduced local equation of S ha | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.52 | In the remaining positive ruled support of Part~4.2, the image of a contracted horizontal pole section has ambient multiplicity exactly three. This re | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.53 | In the remaining positive ruled support, blow up the multiplicity-three image of the contracted horizontal section H, normalize the strict transform S | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4.54 | In the remaining positive ruled support of Part~4.2, the horizontal pole section is not contracted by the normalization resolution. It consequently ma | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.55 | In the remaining positive ruled case, the image A of the horizontal pole section is a smooth rational curve. The map Hto A has degree exactly two. The | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.56 | In the remaining case of P4.55, the other conductor image component B has at least three generic normalization branches. This conclusion imposes no pr | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.57 | The remaining degree-two configuration of P4.55--P4.56 cannot have its image-conductor graph cycle realized at two distinct intersections of its two c | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4.58 | Let f:Yto B be the fibration of Part~4.2, with b_1(Y)=b_2(Y)=0, connected fibres and general fibre a complex two-torus. Suppose every reduced fibre su | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation in restricted scope; sharpens II Prop. 13.1 (see 6.2) Compared: CDP C.2.G.1. |
| P4R.13 | In Part~4.2, let an irreducible singular support S have a normalization with ruled resolution. If its reduced image conductor has a component with ell | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.14 | Let S be an actual reduced support in Part~4.2. At a point where the entire reduced critical locus of its local defining function is one smooth curve, | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.15 | At every critical-curve point of an actual reduced support in Part~4.2 with nonzero ambient Hessian, holomorphic coordinates give the exact product ge | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.16 | In the remaining positive ruled case with uniform transverse type A_3, the three-branch point of the critical curve cannot be the union of a plane tac | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.17 | In the remaining positive ruled case with uniform generic transverse type A_3, every nonordinary three-branch critical-curve point has local conductor | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | new result |
| P4R.18 | In the remaining positive-Euler ruled case of Part~4.2, a noncontracted horizontal pole section maps with degree two or three to a rational normalized | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.19 | Let f be the actual reduced local equation of the remaining positive ruled support, and let C_0 be a smooth local branch of its critical curve with ge | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |
| P4R.20 | In the remaining degree-two horizontal sector after P4.55, suppose that the generic transverse curve along the other image component B has at least th | Proved | II: the sign theorem (irreducible and normal-crossings fibres) | confirmation of an S6_09 statement (restricted scope) Compared: CDP C.2.G.1. |

## 7. Decisions after the sketch (main session, Claude Opus 5.5 at effort max, 17 Nov 2026 ~13:0x UTC)

- **The series:** five papers as sketched (the user agreed), plus the proposal below for a sixth.
- **Point 4 (re-derivations of DGKX v1):** kept in Paper I as two credited appendices (the user: DGKX's refereed version cut those results, so ours go in with credit).
- **Point 2, reframed.** "One derivation" was not a category of the user's rules and is dropped. Under the rule (every proof checked before publication by anyone qualified, the writing run included), the unrestricted sign theorem is *checked only in this writing* (GPT-6 Astra, ChatGPT Pro mode), like any other result whose only check is the writing run's. It is a new result with a complete proof. Its 358 pages are not used by any main result of Paper II (the dependency closure of the main results does not reach the C.2.UN block). PROPOSAL (to the user): it becomes **Paper VI, the sign theorem for every degeneration**, with its own opening and its full proof; Paper II proves the irreducible and normal-crossings case it needs (proved in the writing run and again, blind, in the night run) and cites Paper VI for the general case. Check record of Paper VI: checked only in this writing; a second reader (Claude Fable 5.2) is worth having before publication, not required.
- **Check records generally:** the wording is the user's: [the user's words, omitted] where earlier checks exist (the per-row check ledger, built by script, names them), "checked only in this writing" where the writing run is the only check.

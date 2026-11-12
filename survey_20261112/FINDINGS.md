# S6 workbench survey: ranked findings, their status, and where each goes

Written 12 November 2026 (13:30 UTC) by Claude Fable 5.2, effort high (the user's choice for this survey), from its own
reading and from the notes of fifteen readers (Claude Fable 5.2, effort high; notes in `work\*_notes.md`). This is a
survey to find what is worth checking. Nothing here is a verification. "Read without finding a gap" means a reader
read the proof at medium depth; it does not mean the proof is established.

## What was read

- Primary: the local Codex workspace `C:\Users\user\Documents\math\research\s6_recent_results_main` (LW): the
  canonical S6 snapshot of early September 2026 (the first check of the original manuscript and the 782-page
  workbench), the course CG-S6 (to 11 October 2026; the latest treatment), the consolidation, the five related
  sources and the ledgers.
- Secondary, lightly: the public repository `yang-mills-interacting-workbench` (clone in `repo\`). It holds almost no
  S6 mathematics that is not in LW; its `s6\STATUS_2026-10-05.md` is the corrected public position on
  Campana-Demailly-Peternell.
- Literature read for novelty: [AC26] (the original 108-page manuscript, in transcription), [E26] Engel
  arXiv:2609.38442, CDP20 arXiv:1904.11179v2, CDP98 arXiv:math/9607215, and the later 2026 papers found by search:
  Viaclovsky arXiv:2609.33785, 2610.10451, 2610.39102; Liu-Rollenske arXiv:2609.33826; X. Yang arXiv:2609.29666;
  Z. Wang arXiv:2609.11541; Mandal arXiv:2609.27929. Copies: `C:\Users\user\Documents\s6_pro_prompts_20261112_work\literature\`.
  The scoreboard of 10 November has no S6 row; the S6 literature above should be added to it.

Abbreviations: W = `LW\canonical_S6_snapshot\supporting_materials\workbench\research\`; CG = `LW\courses\CG-S6\src\`;
[N] = the correction note of 1 September 2026, `LW\source_text_blobs\aca0913df424f72b0efc94546498f1f427786191628503ff56208f4153060abb.tex`.
Reader entries are cited as B-1, G1a-13 and so on; the full six-point entries (where, statement, support, what it
adds, assessment, what a full check must establish) are in `work\<reader>_notes.md`, section 2.

## Status marks

- **Settled (literature):** proved in [AC26], [E26] or a later paper with a human author taking responsibility.
- **Proved in the workbench:** a complete written proof exists in LW; AI-produced (GPT-5.6 Sol, later GPT-6 Astra, in
  Codex), reviewed only by other AI sessions; a reader here read it without finding a gap. Not conclusively established.
- **Sketch:** an argument by one of the readers of this survey, written during the survey, checked by no one.
- **Open:** no proof or disproof anywhere I looked.

Prompts: S6_1_CDP, S6_2_INVARIANTS, S6_3_FAMILY, S6_4_MAPS, S6_5_MANIFOLDS, S6_6_ARITHMETIC
(`C:\Users\user\Documents\s6_pro_prompts_20261112\`).

## The first check of the original manuscript, in short (reader A0)

- Timeline: Codex root task started 24 August 2026; ten Pro-mode strips for the transcription of the PDF; two full
  Pro-mode reviews (A, B) and a Codex review (C); corrective rounds 25-27 August; the workbench grew to 5-6 September;
  the course to 11 October. Sub-agents were GPT-5.6 Sol (Ultra) to 4 September and GPT-6 Astra from 5 September. All
  reviewers were AI sessions. Every audit used a GPT transcription of the PDF, not compared here with alpo.ge/s6.pdf.
  The original histories of the sub-agents of 24-31 August are lost (2,039 of them); only the root history remains.
- Result: no error touching a theorem of [AC26] was found. Real slips (A0 table, 21 rows; `W\local_repairs.tex`):
  Remark 7.28 (a loose quantifier), Lemma A.3 (H_k printed for a cohomological sequence), Remark A.6 (Λ for Λ̄), and
  Remarks 1.3 and 9.21, which say Ω¹_{X/B} has torsion along W: it is torsion-free and not locally free there, with
  torsion only at the two multiple fibres (B-4; checked by hand by two readers). One audit finding is itself wrong:
  Proposition 4.7(iv) of [AC26] is valid as printed. Several "Codex results" in the front matter of `main.tex`
  (g₂′(z₂) = −i, the spine lemma, flatness) are already in [AC26].
- Caution on the label VERIFIED: the workbench corrected its own "verified" proofs at least six times.

## Ranked findings

Each entry: statement; where; status and what supports it; what it adds over [AC26], [E26] and the literature;
assessment and gaps; what a full check must establish; where it goes.

### Interest 5

**F1. The complete Hodge diamond of X.** h^{1,1} = h^{2,2} = 2, h^{1,2} = h^{2,1} = 1, with
f_*Ω¹_X = O(−2), R¹f_*Ω¹_X = O ⊕ O(−1)², R²f_*Ω¹_X = O ⊕ O(−1); rows q = 3..0 of h^{p,q}: (0,0,0,1), (0,1,2,1),
(1,2,1,0), (1,0,0,0).
- Where: `W\hodge_frolicher.tex` l. 319-1174 (`prop:log-relative-direct-images`, `prop:log-ks-divisor`,
  `prop:absolute-cotangent-direct-images`, `thm:h12-scalar`, `cor:exact-hodge-diamond`); 27 August 2026. Readers B-1, A0-8.
- Status: proved in the workbench (about 700 lines). The workbench's own item "human replication" is open.
- Adds: [AC26] proves h^{0,q}, h^{p,0} and the relation h^{1,1} = h^{1,2} + 1, and writes "which we do not compute; the
  expected value is h^{1,2} = 1" (Remark 9.21). [E26] omits Dolbeault cohomology. Viaclovsky (2609.33785 §6.2;
  2610.10451 Question 2) leaves the remaining Hodge numbers open for his families. No computation of h^{1,1}, h^{1,2}
  for any complex structure on S^6 was found.
- Assessment: consistent (χ(Ω^p), Serre duality, b_k all check). The value is decided by one scalar: the rank of
  H⁰(κ₁), which rests on μ′(z₂) ≠ 0 at the order-four point, obtained from a degree count and never evaluated.
- A full check must establish: local freeness of the logarithmic sheaves at the three fibres; the invariant bases at
  the multiple fibres; degrees of the direct images; the formula for κ₀, κ₁; the residue computation; an independent
  evaluation of μ′(z₂) (μ is the Eichler-Zagier zero of ℘, F5).
- Goes to: S6_2_INVARIANTS, Parts A, B.

**F2. The exact classification inside the family.** X_c ≅ X_{c′} as abstract complex manifolds if and only if
c′ − c ∈ 2Z; the isomorphism classes of the family form the punctured disc 0 < |w| < e^{−πM}, w = e^{−πic}; every
biholomorphism commutes with f; the obstruction for odd shifts is a class of order two in Λ^{A₂}/N₂Λ = Z/4 ⊕ Z/2 at
the multiplicity-four fibre.
- Where: `W\period_shift_classification.tex` (`pshift:thm:classification`, (PS1)-(PS29); 6 September 2026);
  `CG\periods-and-nontrivial-deformation.md` §§5-8, Theorem 8.1 (11 October). Readers B-7, G1a-1, A1-X1.
- Status: proved in the workbench and again in the course. Two readers re-derived necessity by hand; sufficiency was
  read step by step without finding a gap. No ledger id, no checker beyond lattice arithmetic.
- Adds: [AC26] Remark 6.4 leaves exactly this open. [E26] Remark 8.1 only says the family deforms. Viaclovsky
  2610.39102 proves different multiplicities give different structures and asks (Question 3) whether different
  translation vectors do, for fixed u. X. Yang 2609.29666 (13 September, one week later) proves a statement of the
  same kind, "biholomorphic exactly when the parameters differ by an element of (6/r)Z", for related families that
  are not S^6. So the mechanism now has a printed analogue, and the statement for the S^6 family itself is not in print.
- Assessment: the strongest new theorem in the workspace. Risks: it leans on f = |−2K_X| (F17), on the normalization
  of the base change at the multiple fibres, and on the extension of the even-shift maps over all cusp strata.
- A full check must establish: items (1)-(8) of G1a-1; a comparison with Yang's method.
- Goes to: S6_3_FAMILY, Part A.

### Interest 4

**F3. All discrete choices: every S^6 member of the (3,4) family is one X_w.** For all admissible twist vectors the
isomorphism class depends only on p and on w; for fixed Engel parameter u the threefolds X(u, a₀, a₁) with the same
ψ-values fall into exactly two classes, exchanged by going once around u = 0.
- Where: not in LW. Reader G1a-13(a), with a script for the lattice part; reader B's inference in B-7.
- Status: sketch. It would answer Viaclovsky's Question 3 for multiplicities (3,4).
- A full check must establish: the lattice condition N_j l_j = w_j − (I + nE)w′_j; the analytic gluing as in lesson 9
  §7; the case of linear part −I; the cusp twist l₀ of [AC26]; f = |−2K| for the other twist vectors.
- Goes to: S6_3_FAMILY, Part B.

**F4. The exact dictionary between [AC26] and [E26].** L_μ = O_{E_τ}(P − O); the first period column acts as a lift of
translation by 6P with multiplier e^{2πiβ}; the flat-norm contraction factor of the lifted translation is e^{2πD};
Engel's u = λ₀e^{−2πic} = λ₀w²; the Z-action is properly discontinuous with torus quotients on every fibre exactly for
|u| < |λ₀|e^{−2πM} (a sharp form of [E26] Proposition 2.4); div(φ_per) = F_∞.
- Where: `CG\global-periods-and-line-bundle-quotients.md` §§6-8; `CG\cusp-and-compact-threefold.md` §§9-13
  (Theorem 13.1); lesson 9, Exercise 9.3. Reader G1a-2.
- Status: proved in the course (author self-check only). λ₀ is not evaluated; M is not evaluated.
- Adds: [AC26] Remark 3.12 states the elliptic-surface reading in two lines without proof; [E26] §1.3 gives it
  "roughly". Consequence: Engel's family over the punctured u-disc closes up only on the double cover w² ∝ u.
- Goes to: S6_3_FAMILY, Parts B, C.

**F5. μ is the elliptic logarithm of the Mordell-Weil generator; ℘_τ(μ) = 0; e^{2πiμ(p₀)} = −5 ± 2√6.** Hence μ is the
Eichler-Zagier zero of the Weierstrass function, which has a closed integral formula.
- Where: `CG\cusp-and-compact-threefold.md` §9 (Theorem 9.1, Lemma 9.2), Theorem 11.2, (11.14), (13.9). Reader G1a-3;
  the Eichler-Zagier identification is the reader's.
- Status: the course statements are proved in the course; the identification with Eichler-Zagier is a sketch.
- Adds: proves [AC26] Remark 3.12; gives μ in closed form, hence a way to compute μ′(z₂) (F1), the cusp gluing units
  of W (F21) and the number M (F21).
- Goes to: S6_2_INVARIANTS, Part A; S6_3_FAMILY, Part C.

**F6. The step at CDP20 p. 692, as a general theorem.** For a reduced effective Cartier divisor S in a smooth threefold
and a line bundle A on S: 0 → N* → K_S → T_S → 0 and 0 → K_S → Ω¹_X|_S → Ω̃¹_S → 0; given the two vanishings CDP use,
H⁰(S, Ω¹_X|_S ⊗ A) = ker(δ_A: H⁰(T_S ⊗ A) → H¹(N* ⊗ A)); for normal crossings K_S ≅ η_*η*N*, so the ambient group
vanishes iff H⁰(S̃, η*(N* ⊗ A)) = 0. A proper test family, (nodal cubic) × P¹ over a disc with a twist that extends to
the total space, has both printed vanishings and ambient H⁰ = C. At the cusp fibre W of X the group is exactly C for
every L.
- Where: `W\cdp_program.tex` l. 40-353; [N] Proposition 2.3, Lemma 4.3, Theorem 4.4;
  `CG\non-normal-fibres-and-vanishing.md` §§1-6, §9; `repo\s6\STATUS_2026-10-05.md` §3. Readers B-9, B-10, G1b-1,
  G1b-2, G1b-4, A0-1, H-1, I-4.
- Status: proved in the workbench; four readers recomputed the test family. G1b read CDP20 and CDP98 in the primary
  source: the printed inference is quoted correctly and fails as described. The paper [R] cited by the status note is
  not in LW or the repository.
- Adds: [AC26] Lemma 10.3 and Theorem 10.5 show the failure at W only. The general criterion and a counterexample
  independent of S^6 are not in [AC26], [E26] or any paper found; Liu-Rollenske say the gap "was known only to a few
  experts". Not examined anywhere: non-reduced fibres (CDP20 Remarks 7.2, 7.4), and CDP's own use of "all η*L_t
  trivial" inside the proof of Proposition 7.3.
- Goes to: S6_1_CDP, Parts A, B.

**F7. Frölicher at E₂; Bott-Chern and Aeppli numbers; the Bott-Chern algebra.** E₁ ≠ E₂ = E_∞; h_BC by total degree
(1,0,2,2,2,2,1), h_A (1,2,2,2,2,0,1); H_BC = C·1 ⊕ N with N² = 0, nine explicit generators;
c₁^{BC}(exp(z𝔤)) = zA + z̄B; exp(12𝔤) = f*O(1).
- Where: `W\hodge_frolicher.tex` l. 166, l. 1189; `W\bott_chern_algebra.tex`. Readers B-2, B-3, A0-9.
- Status: proved in the workbench, given F1 and McHugh's formulas (arXiv:1708.03251); agrees with McHugh's table for a
  hypothetical S^6 at h^{1,2} = 1.
- Goes to: S6_2_INVARIANTS, Part C.

**F8. The deformation space of X.** h²(T_X) = h¹(T_X) ≥ 1 (reader B's remark from χ(T_X) = 1, h⁰ = 1, h³ = 0). The value,
unobstructedness, and whether the w-family is the Kuranishi family are open; so are the lengths of
R¹f_*, R²f_*(T_X ⊗ M) and the length r of the stalk of R²f_*(T_X ⊗ L) at the cusp.
- Where: `W\period_parameter_deformation.tex` l. 386-391 (says it is not computed); G1b-4; A0-14; B-17(a).
- Status: open. Viaclovsky 2610.39102 Question 2 asks the same.
- Goes to: S6_2_INVARIANTS, Part D.

**F9. The circle quotient of Engel's Remark 8.3, made exact, and the failure of its literal extension.** The
fibrewise quotient by the invariant 3-torus is a real-analytic map over B minus the cusp, with explicit Seifert solid
tori at the two multiple fibres; the glued 3-manifold is the exterior of the torus knot T(3,4) (the reader's
remark); the literal quotient has no continuous extension over W (two paths to one triple point with values 3/4 and
1/2).
- Where: `W\cusp_globalization_replacement.tex`, Theorem `cusp-spec-globalization-obstruction` (i), (iv), (v);
  3 September 2026, before Engel's paper. Readers C1-1, A1-1.
- Status: proved in the workbench; two readers re-derived the non-extension.
- Adds: [E26] Remark 8.3 says the quotient "extends continuously" over the cusp; that holds only up to homotopy.
- Goes to: S6_4_MAPS, Part A.

**F10. The homotopy class of Engel's map S^6 → S^3.** Claimed: it is the element of order two of π₆(S³) = Z/12 (stable
class η³ = 12ν), because the regular fibre is a Lie-framed 3-torus; and f: S^6 → P¹ is null-homotopic.
- Where: not in LW (the workbench records the equivalent class as open, `W\cusp_sphere_route_strengthening.tex`
  l. 661-676). Reader C1-2, one page, lattice inputs checked by script.
- Status: sketch. Also from C1: [q̂_γ] ∈ π₆(S²), recorded open in LW, is zero by a soft argument (C1-5, sketch).
- Goes to: S6_4_MAPS, Part B.

**F11. A 3-connected rank-three analogue?** The cusp Euler number 3! = 6 is the smallest Euler number Hirzebruch's
congruence allows for an almost complex 8-manifold with c₁c₃ = 0; a 3-connected one has b₄ = 4, σ = 2, Todd genus 0;
3HP² # (−HP²) is almost complex (Mandal, arXiv:2609.27929). Is it a complex manifold fibred in 3-tori over P¹?
- Where: reader E-3 (synthesis; the workbench stops at "not S^8": `W\higher_rung_fourfold_toric_degeneration.tex`,
  `W\higher_rung_s8_constraints.tex`).
- Status: open question.
- Goes to: S6_5_MANIFOLDS, Part C.

**F12. The family deforms: KS(∂_c) ≠ 0 in H¹(X_c, T).** Explicit Beltrami class on the exact domain Im c < −M.
- Where: `W\period_parameter_deformation.tex` (PD1)-(PD18); lesson 9 §§1-4; key-advances reader §2. Readers B-6, G1a-11, H-4.
- Status: proved in the workbench (5-6 September). Settled in the literature by another route since: Viaclovsky
  2610.39102 (29 October) proves the family is not locally isotrivial.
- Goes to: S6_3_FAMILY, Part A (as an input to re-derive).

### Interest 3

**F13. What survives of CDP.** For a compact threefold Y with b₁ = b₂ = 0 and a non-zero effective divisor:
χ(T_Y ⊗ L) = 1 − b₃/2 for every L; if H²(Y, T_Y ⊗ L₀) = 0 for one L₀ then b₃ ≥ 2 (c₃ ≤ 0); if b₃ = 0 then
H²(Y, T_Y ⊗ L) ≠ 0 for every L and R²g_*(T_Y ⊗ L) ≠ 0 for every map g onto a curve.
- Where: `CG\non-normal-fibres-and-vanishing.md` §11.3-11.5; [N] Theorem 5.2, Corollary 5.3; `W\cdp_program.tex`
  l. 1368-1606. Readers G1b-3, B-11, A0-2.
- Status: proved in the workbench. It is the valid core of CDP98's own method; the ledger's "strongest intact
  replacement" is not proved in any sense, and the theorem is conditional on the vanishing whose proof failed.
- Goes to: S6_1_CDP, Part C.

**F14. What replaces CDP20 Theorem 2.2?** No statement with geometric hypotheses is known. Sub-questions (G1b-13):
for torus fibrations c₃ = Σ e(red X_c), so is c₃ ≥ 0 always and which non-normal fibres occur; does the corrected
argument ever prove more than Euler-number additivity (CDP20 Proposition 4.11 makes every singular reduced fibre
non-normal); do threefolds with b₂ = 0, a = 1 and trivial monodromy exist.
- Status: open. Goes to: S6_1_CDP, Parts C, D.

**F15. The coinvariants gap in CDP98 Lemma 3.2 = CDP20 Lemma 4.2.** (K ⋊ Q)^ab = Q^ab ⊕ (K^ab)_Q; corrected count
r = s − 1 + t′; the rank argument is valid exactly when the invariant lattice spans H¹(F, O_F) ((5.33)).
- Where: [AC26] Lemma 10.7, §10.5; `W\cdp_program.tex` l. 1302-1358, 1592-1606. Readers B-12, A0-3.
- Status: settled in [AC26] for X; the exact condition is proved in the workbench. Open: corrected general statements
  of CDP20 Lemma 4.2, Corollary 5.2, Propositions 5.5, 5.6.
- Goes to: S6_1_CDP, Part D.

**F16. The audit of CDP20 Theorem 2.1 and the possible values of a(X) on S^6.** [AC26] Remark 9.9(e) notes that using
CDP20 Theorem 2.1 "is legitimate only insofar as its proof is independent" of the failed steps. Nobody in LW checked
that. Which algebraic dimensions occur for complex structures on S^6 (a = 1 exists; a = 0, a = 2?) is not addressed.
- Status: open (my item). Goes to: S6_1_CDP, Part E.

**F17. The anticanonical ring.** ω_X = O_X(−2S₂); f_*O_X(kS₂) = O_B(⌊k/4⌋p₂); ⊕H⁰(ω_X^{−m}) = C[U,V], degrees 1, 2;
f = |−2K_X|; O(S₁) = L₄, O(S₂) = L₃, ω_X = L₋₆ in the Picard coordinate with L₁₂ = f*O(1).
- Where: `W\analytic_canonical_ring.tex` (CR1)-(CR5); lesson 8. Readers B-8, G1a-10, H-3.
- Status: proved in the workbench; short; refines [AC26] Proposition 9.11. Viaclovsky 2609.33785 uses the
  anticanonical pencil for his family and quotes h⁰(−K) = 1 for this one.
- Goes to: S6_3_FAMILY, Part A (input to re-derive).

**F18. a(X) = 1 in a few lines.** b₂ = 0 makes every effective divisor vertical on a torus fibration, so
M(X) = f*C(t); the argument covers every member of every known family.
- Where: lesson 10 §8. Reader G1b-5. Status: proved in the course. Goes to: S6_1_CDP, Part E.

**F19. The logarithmic Kodaira-Spencer divisor.** div(det κ₀) = p₁ + p₂; det(dZ/dz) vanishes to order 2 at the
order-three point and nowhere else on the smooth base.
- Where: `W\hodge_frolicher.tex` l. 218, l. 525. Reader B-5. Status: proved in the workbench; part of F1.
- Goes to: S6_2_INVARIANTS, Part A.

**F20. Fibres with an elliptic quotient; abelian fibres.** The first-coordinate elliptic quotient exists iff
6μ ∈ Zτ + Z (workbench: a finite set). Reader's sharpening: this is 6P = O, which happens at exactly
t = 64(47 ± 27√3)/11; these two fibres, and the fibres over the dense countable set where P is torsion, are abelian
surfaces.
- Where: `W\cusp_spectral_geometry.tex` l. 959-1176 (S6-CUSP-FIRST-ELLIPTIC-QUOTIENT); reader F-3 with an exact sympy
  script (`work\scratch\F\six_P_meets_O.py`); I-5.
- Status: the workbench part is proved there; the sharpening is a sketch with an exact computation.
- Goes to: S6_3_FAMILY, Part D.

**F21. The admissible range and the cusp fibre in numbers.** The construction exists exactly for Im c < −M,
M = max D_part (existence only; no value); the three gluing multipliers of W are e^{−2πiμ₀}, e^{12πiμ₀},
e^{−2πi(7μ₀+b₀)}; with F5, two of them are units of Z[√6] and W_c = W_{c+1}.
- Where: `W\candidate_geometry.tex` l. 563-596, l. 1029-1064; lesson 4 Theorem 5.1; readers A1-2, A1-4, G1a-5,
  G1a-13(b). The course uses a made-up "M = 7/3" in an exercise.
- Status: the range and multipliers are proved in the workbench; the value of M, the point where D_part is maximal
  and what happens at the boundary |w| = e^{−πM} are open.
- Goes to: S6_3_FAMILY, Part C.

**F22. The finite fillings in explicit form.** Product covers of S₁, S₂ of degrees 9 and 8; the deck-group
presentation; the attachment kernel is exactly ⟨G̃_j^{m_j}t_{−v_j}⟩ ≅ Z; Alb(S₂) has nome ∝ w and Alb(S₁) nome ∝ w²
(the readers' cross-check of F2).
- Where: `W\finite_filling_certificates.tex` FF1-FF46; lessons 1-3. Readers A1-5, A1-6, G1a-7, H-5.
- Status: proved in the workbench; standard. The Albanese cross-check is a sketch.
- Goes to: S6_3_FAMILY, Part A (the cross-check).

**F23. The completed Kummer cover of the cusp.** After t = v^N the modified action C_N(v) = C(v^N)/N makes the toric
power map equivariant: a finite flat map of degree N³ to the completed cusp and a quasi-étale non-flat map of degree
N² to the normal base change, with the double and triple strata as the exact non-flat locus.
- Where: `W\cusp_toric_cover_completion.tex`. Reader A1-8. Status: proved in the workbench; local; standard methods.
- Goes to: S6_4_MAPS, Part C.

**F24. The cusp collapse map H: X → S⁴ is η₄η₅ ≠ 0 in π₆(S⁴) = Z/2.** The vanishing 2-torus at a triple point carries
the Lie framing (Arf invariant 1).
- Where: `W\higher_rung_24d_continuation.tex` l. 4378-5107 (Theorem `h24:ret:main`); evidence
  `retained_angle_20260905`. Readers C1-3, H-15. Status: proved in the workbench; a local fact about a
  normal-crossings triple point.
- Goes to: S6_4_MAPS, Part B.

**F25. The "higher torus wrap" is a fibre product.** The global gluing the workbench records as open
(`W\status.tex` l. 2805; `W\higher_rung_toroidal_elliptic_bridge.tex` (TEB.54)) is closed by X ×_{P¹} S with Engel's
rational elliptic surface S: a simply connected compact complex fourfold Z with χ = 6, b₂ ≥ 2, not Kähler.
- Where: reader E-2. Status: sketch; specialists would call it an immediate corollary.
- Goes to: S6_5_MANIFOLDS, Part B.

**F26. The members with |p| > 1, their universal covers, and Viaclovsky's X_{3k,4l}.** Diffeomorphism types are not
identified anywhere in LW (π₁ = Z/|p|, universal cover simply connected with e = 2|p|).
- Where: [AC26] Theorems 7.17, 7.22; lesson 6 Exercise 2; reader G1a-13(e). Status: open.
- Goes to: S6_5_MANIFOLDS, Part A.

**F27. The limit w → 0 and Engel's Conjecture 8.2.** Not addressed anywhere in LW. Status: open.
- Goes to: S6_3_FAMILY, Part E.

**F28. Klingler's question ([E26] Remark 8.4).** Does the monodromy group act properly discontinuously on
D = Sp₄(R)/U(1,1), or on an open set containing the period image? LW has only the invariant Hermitian forms
(reader I-1: all monodromy-invariant forms H(a,b), signature (2,2); commutant aI + bE). Status: open.
- Goes to: S6_3_FAMILY, Part F.

**F29. Aut(X_c) = C^* exactly.** [AC26] has Aut⁰ = C^*; connectedness is the reader's sketch (G1a-13(f)).
- Goes to: S6_3_FAMILY, Part B.

**F30. Engel's Remark 8.5: other elliptic surfaces, the conifold transition.** Not taken up in LW (the word
"conifold" does not occur in the research folder). Since then: Viaclovsky (III, I₁, I₁, I₁), Liu-Rollenske, Wang
(IV*, I₂, I₁, I₁), Yang. The conifold transition is open. Goes to: S6_5_MANIFOLDS, Part A.

**F31. The Koide count** (side lane; no mathematical link to X, reader D2). R(X) = C₀X + O(X^{1−η}),
C₀ = (9/(2π²))·log(2+√3)·log(3/(2√2)); census R(10⁸) = 3,536,002, recounted independently to 10⁷. Open in LW: the
square-root discrepancy. Reader's reformulation: R(X) counts common perpendiculars between closed geodesics with foot
in a fixed arc, so the exponent 2/3 is within reach by Good / Lekkas-Petridis, and
Σ_{z≤X} ρ(3z−1)ρ(3z+1) = (9/(2π²))log²(2+√3)·X + O(X^{2/3}) would follow.
- Where: `W\koide_*.tex`; D2-8, D2-9. Status: main term proved in the workbench (known theory); the reformulation is a
  sketch checked by program to z = 30,000. Goes to: S6_6_ARITHMETIC, Part A.

**F32. The lattice J** (side lane; no map to X, reader D1). Three Leech neighbours of N(A₅⁴D₄) cycled by an order-3
Weyl element, common sublattice J of determinant 81, a fourth overlattice A₂¹²; reader: J has exactly eight unimodular
overlattices, six Leech and two A₂¹². Open: is J known; its automorphism group; d-neighbours along the Weyl vector and
Coxeter number h/d; the stabilizer of Wilson's cubic in Co₀.
- Where: `W\es_niemeier_residue_fixed_neighbor.tex`; D1-1, D1-13. Status: proved in the workbench and recomputed
  exactly by the reader; novelty not established. Goes to: S6_6_ARITHMETIC, Part B.

### Interest 2 and below (settled or routine; see the readers' notes)

- Re-proofs of [AC26] topology with small gains: sp^q = c^* written out (A0-6, A1-10); the collapse exact sequence
  (A1-11); Mayer-Vietoris and Leray routes compared as maps with absolute signs (A0-7, A1-13, A1-14); exact
  specialization lattices at the multiple fibres (G2-1); π₁ and H_* for general (l₀, l₁, l₂) (already [AC26]);
  a(X) = 1 by repaired meromorphic descent (A1-17).
- Theorem 10.5 without the topology: Pic(X) → Pic(dP₆) is zero, proved three ways (B-13, A0-4); the cusp-local line
  bundle L_Q with degrees (−12, 2, 0, −12, 2, 0) (B-14); Proposition 10.8 reproved (A0-10, B-15).
- Errata of [AC26] (A0-11, A1-18, B-4).
- Ω¹_{X/B} torsion structure; Tors = (f*ω_B ⊗ O(Z))|_Z, Z = 2S₁ + 3S₂ (G1b-8).
- Fibre-degree row (12,0,4,0,−3,0): linking numbers of a generic fibre with loops on W, S₁, S₂ (F-7).
- SU(3) bundles on the regular locus classified by H⁴ = Z⁶ (E-5).
- All invariant Hermitian forms on the fibre lattice (I-1).
- The key-advances reader of 6 September and the 30 September consolidation R1-R8 in the repository (H-7 to H-14):
  elementary quaternionic Gaussian integrals and a six-level tomography design; correct where recomputed; no S6 content.

## The prompts for GPT-6 Astra (effort Pro, ChatGPT Pro mode)

Six prompts, each built for one Pro run. Every open or only-asserted item above that bears on S6 is in one of them;
what is left out is listed in the next section with the reason. Each upload folder holds `PROMPT.md` and one
background zip with a `MANIFEST.tsv`.

| Prompt | What it asks to crack | Findings |
|---|---|---|
| `S6_1_CDP` | The CDP step in full generality (reduced, non-normal, non-reduced fibres), counterexamples that do not use S^6, the strongest true replacement of CDP20 Theorem 2.2, the corrected monodromy lemmas, the audit of CDP20 Theorem 2.1 and which algebraic dimensions occur on S^6 | F6, F13-F16, F18 |
| `S6_2_INVARIANTS` | The Hodge diamond by an independent route with the decisive scalar evaluated; Frölicher, Bott-Chern, Aeppli; h¹ and h² of T_X, the Kuranishi space, completeness of the family; the twisted tangent cohomology; the same for the other members | F1, F5, F7, F8, F19 |
| `S6_3_FAMILY` | The classification c mod 2Z established and extended to all discrete data (Viaclovsky's Question 3); the dictionary with Engel; the numbers M, λ₀, μ(p₀); the boundary; abelian fibres and curves; Engel's Conjecture 8.2; Klingler's question | F2-F5, F12, F17, F20-F22, F27-F29 |
| `S6_4_MAPS` | Engel's map S^6 → S^3 constructed and its class in π₆(S³) computed twice; the classes of f and of the cusp maps; a handle decomposition adapted to f; the Kummer cover | F9, F10, F23, F24 |
| `S6_5_MANIFOLDS` | The members with π₁ = Z/|p| and their covers identified; the table of 6-manifolds from the Oguiso-Shioda list; the conifold transition; the fibre-product fourfold; a 3-connected complex fourfold fibred in 3-tori, constructed or excluded | F11, F25, F26, F30 |
| `S6_6_ARITHMETIC` | An explicit exponent for the sectorial count and its neighbours; the lattice J identified, with its symmetries and overlattices | F31, F32 |

Order by interest: S6_2_INVARIANTS and S6_3_FAMILY first, then S6_1_CDP, S6_4_MAPS, S6_5_MANIFOLDS, S6_6_ARITHMETIC.
They do not depend on one another. S6_2 Part A.2 and S6_3 Part C.1 both evaluate μ; that overlap is deliberate, as a
cross-check.

## Open or only-asserted items left out of the prompts, with the reason

- **The S^12 / S^24 "sphere carrier" programme** (C1-6 to C1-12: smash powers, cone targets, moving 4-spheres, R⁴
  limits, optimality of two and four copies). Self-posed questions with no outside interest; the one piece that is
  about the fibration (F9, F10, F24) is in S6_4_MAPS. The open "conical-target classes" are equivalent to F10.
- **Cusp spectral geometry and the gauge-theory lanes** (reader F: F-1, F-4 to F-6, F-8 to F-14; reader H: H-16 to
  H-19; the root-level Yang-Mills drafts). Every statement depends on a flat fibre metric chosen by the workbench or
  on an auxiliary lattice or matrix model; none is an invariant of the complex structure. The open "exceptional set"
  existence question of the scalar-Gauss files (F-9) is about a rotating ansatz in a matrix model taken from a Pro
  packet. Not pertinent to S6.
- **Quaternionic 4+4+4+1, worldline reduction, Lorentz observation, Gram cones, rank-six and rank-nine lattices,
  octonionic flag** (F-8, F-11 to F-13; E-6 to E-10). Correct elementary computations with no map to X.
- **Erdős-Straus selector material and shell counts** (D1-10 to D1-12). Bookkeeping; proves nothing about the
  conjecture; belongs to the separate Erdős-Straus repository.
- **Cubic value groups Z/4, Z/3, Z/12** (D1-5; key-advances §4). The isometry N ⊗ R → O³ is a choice; other choices
  of the same kind give Z/3 ⊕ Z/6 and Z/3 ⊕ Z/54 (reader's computation), so Z/12 is not an invariant. The underlying
  question (a distinguished embedding) is in S6_6_ARITHMETIC, Part B.
- **The related sources** (Geometric Unity bridge, Nolan Gaussian fibres, the two RH sources, the earlier mass-gap
  comparison; reader I). No statement about X beyond re-derivations; the zeta and Navier-Stokes material is outside
  this topic.
- **Human replication of the Hodge computation** (S6-OPEN-HODGE-REPLICATION) and **external adjudication**
  (S6-OPEN-EXTERNAL-ADJUDICATION): not mathematical tasks for a model. S6_2_INVARIANTS asks for an independent
  derivation, which is the nearest thing.
- **Seven misprints in cited sources** (G2-2: Hill-Taylor, Konstantis-Parton, Goerss, Dugger-Isaksen,
  Isaksen-Wang-Xu, Strickland, Crainic). Errata for other people's papers, unchecked against the sources; not S6
  mathematics. Worth ten minutes each if errata are wanted.
- **The self-contained proof of Θ₆ = 0 by sphere twists and the classical chapters of lessons 7 and 11** (G2-3 to
  G2-7). Expository; the course contains no explicit diffeomorphism X → S^6 and no Morse function adapted to f.
- **"J_X is homotopic to the octonionic almost complex structure"** (G2-8): immediate from π₆(CP³) = 0.
- **A literal global formula for the Bott-Chern representatives G, Q** (B-17(f)): a presentation matter, included as
  an optional last item of S6_2_INVARIANTS, Part C, and not as a target.

## Differences between the local workspace and the repository (reader H)

- The repository's `s6\consolidation\20260930\` is the public derivative of `LW\mathematical_consolidation\`
  (identical mathematics, R1-R8).
- The repository has only the five-page key-advances reader of 6 September; the sources of its five sections are in LW.
- The course CG-S6 (to 11 October) is only in LW.
- `repo\s6\STATUS_2026-10-05.md` is only in the repository. It cites [R] ("The S6 record and the integral monodromy of
  its (3,4,∞) period system", claude-opus-5-5, 28 September 2026) and [N]. [N] is in LW as a TeX draft of 1 September;
  [R] is in neither place (Zenodo record 10.5281/zenodo.23003415).
- The 5 October correction was not applied everywhere in the repository: `WORKBENCH.md`, the root `ATTEMPTS.md`, the
  opening of `s6\ATTEMPTS.md` and consolidation entry MC-006 still say the global S^6 result is unresolved.
- The Yang-Mills continuation `20260930-s6-ns-moment-map-bridge` uses the threefold only through one bit (the class
  η₄η₅) and one number (D); two S6-cusp source files and three Claude `y*.tex` files there have no local copy.

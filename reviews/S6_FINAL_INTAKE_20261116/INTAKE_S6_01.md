# S6_01_INVARIANTS: bounded intake

By the S6 intake agent, Claude Fable 5.2 at effort high, 16 November 2026, 13:58 UTC. No sub-agents. The return is by
GPT-6 Astra (ChatGPT Pro mode), returned 12 November 2026:
`s6_pro_prompts_20261112_work\returns\S6_01_INVARIANTS_unzipped\S6_01_INVARIANTS\`.

Read: the results CSV in full (47 rows). In `fragments\part_A.tex`: the proof of A1.3, and A2.1, A2.2, A2.4, A3.1
with proofs, the opening of A2.3. In `part_C.tex`: C1.1, C3.3 with proofs, C2.1 with the first half of its proof. In
`part_B.tex`: B2.1, B3.2 with proofs, the statement and first half of the proof of B3.3. In `part_E.tex`: E2.2
(statement and first half of the proof), E2.4. Not read: A1.0-A1.2, A3.2, A4, B1, B2.2, B3.1, C1.2, C2.2, C3.1-C3.2,
C3.4-C3.8, all of Part D, E1, E2.1, E2.3, the code, the PDF. One check of my own, by program:
`checks\s601_scalar_check.py` (output beside it). "Proved" is the run's label unless I say what I checked.

## 1. Verdict and counts

47 rows: 41 proved, 2 known, 2 refuted, 2 open. I found no error in what I read, and no conflict with the four
finals. The Hodge table holds up: its decisive scalar is non-zero and I confirmed its value independently to 40 digits.

Rows that are not "Proved":
- **A4.2, Refuted.** "AC26 Remark 9.21 cusp torsion claim for Omega1 is false; support is S1 union S2. Remark 1.3
  must distinguish p = 1 from p = 2." (The survey of 12 November had the same correction, checked by hand by two
  readers.)
- **E2.4, Refuted.** "The universal bound h0(T) <= 2 in HKP Corollary 1.3, repeated in AC26 Remark 9.26, is false for
  the comb members, whose h0(T) = 2m+1 >= 25." The proof says the source derives the bound from the
  Campana-Demailly-Peternell claim that a complex S^6 has no non-constant meromorphic function; with that claim
  false the step fails, and E2.2 supplies the fields. It does not refute the bound for algebraic dimension 0.
- **C3.6, Known.** "Gauduchon metric exists with Chern-Ricci form pi f*omega_FS in any fixed Gauduchon A22 class; no
  Chern-Ricci-flat metric."
- **E2.1, Known.** "For comb members m >= 12, R1O = O(a_m)+O(b_m) with a_m, b_m >= 0 and sum 2m-1, R2O = O(2m-1), and
  h0q = (1, 2m+1, 2m, 0)."
- **C3.8, Open.** "Operator formulas for global G and Q; finite local coefficient atlas not evaluated."
- **E2.3, Open.** "The exact splitting and h0 of K_m and the comb Kuranishi bracket/higher obstruction maps are not
  determined; the smallest unresolved case is a specified smoothed 12-tooth section."

## 2. The main rows

**A3.1, the Hodge table: holds.** For every admissible c the non-zero Hodge numbers are h00 = h01 = 1,
h11 = h22 = 2, h12 = h21 = 1, h32 = h33 = 1.
- How it is obtained: the direct images on P^1 (A1.3): for Omega^1 they are O(-2), O + O(-1)^2, O + O(-1); for
  Omega^2 they are O(-2) + O(-1), O(-2) + O(-1)^2, O. Leray on a curve has no differential. I recomputed the table
  from these six sheaves: it is as stated.
- The one scalar. R^1 f_* Omega^1 is the kernel of kappa_1: O^2 + O(-1)^2 -> O. On global sections kappa_1 kills the
  class of the invariant form eta and takes the value -mu_s(0)/4 at p_2 on the other generator h gamma (A2.4), where
  mu_s(0) is the derivative of mu in the fourth-root coordinate at the order-four point. If it were 0 the table
  would have h12 = 2, h11 = 3.
- Its value (A2.2): mu_s(0) = i C_4, C_4 = 4 sqrt(pi) / (3^(3/4) Gamma(1/4)^2) = 0.23660931408078522468..., from the
  exact identity (A2.1) 6 mu_z^2 - tau_z beta_z = tau_z^2 E_4(tau)^2 / E_6(tau), which at z_2 gives
  6 mu_s(0)^2 = -4/(pi^2 sqrt(E_4(i))). A second proof in the return uses the Abel integral of P on Y^2 = X^3 - 3X.
- My check, independent of both: from the first run's local expansion (mu - (1-tau)/2)^2 = (2i/(3 pi))(tau - i) and
  j''(i), computed numerically, |mu_s(0)| = 0.2366093140807852246877051134504496062943, equal to the claimed value
  in all 40 digits; and j''(i) = -162 Gamma(1/4)^8 / pi^4. So the scalar is the same number as the constant of my
  finding F9 and of S6_05 C.3.1, seen in the root coordinate.
- Consistency checks that pass: chi(Omega^1) = -1 = -c_3/2 (Riemann-Roch on S^6); Serre duality; [AC26]'s relation
  h11 = h12 + 1; the alternating sum of all h^(p,q) is 2.
- Unread and carrying weight: A1.1-A1.2 (local freeness of the logarithmic cotangent sheaves at every stratum and
  their direct images). The workbench (GPT-5.6 Sol in Codex at reasoning effort ultra, 27 August 2026) reached the
  same table by its own computation, so there are two derivations.

**C1.1, Frolicher: holds; the proof is ten lines.** E_1 != E_2 = E_infinity, with d_1 of ranks 1, h, h, 1
(h = h12). Given the zeros h^(p,0) = 0, h02 = h03 = 0, no d_2 or d_3 has a non-zero source and target, and the
vanishing of b_1, ..., b_5 makes the two middle rows exact. I followed every arrow. It is valid for any h.

**C2.1 and C3.3, Bott-Chern: hold as far as I read.** The double complex is a sum of two dots and of arrows (by
Stelzig's structure theorem, which the return cites); I recounted the Bott-Chern and Aeppli tables from the arrows:
totals (1,0,2,2,2,2,1) and (1,2,2,2,2,0,1) at h = 1. C3.3: the positive-degree ideal N has N^2 = 0. The argument
(Leibniz identities; a^2 = d-d-bar of Phi from injectivity of d_1 on H^(1,2); the remaining products land in (3,3)
and integrate to 0) is correct on the page. It uses C3.1 (the Chern class of exp(z g) is zA + z-bar B), which I did
not read.

**B2.1, coprime (3k,4l): holds.** K_X = f^*O(-1) + (k-1) S_1 + (3l-1) S_2. I checked the two orders (3k - 1 - 2k and
4l - 1 - l) and that the fibre degree is (kl - 3k - 4l)/(12kl), which is exactly the pair A = 12kl, D = kl - 3k - 4l
used in PUSH E.2.22. The Hodge numbers (h11, h12) = (2, 1) for these members come from B1.1-B1.2, unread.

**B3.2-B3.3, the degree-n universal covers: hold as far as I read.** The cusp has n normalization components; the
residue sequence gains a skyscraper C^(n-1) at the cusp; so h11 = h22 = n + 1 and h12 = h21 = 1, Betti numbers
(1, 0, n-1, 0, n-1, 0, 1), Frolicher at E_2. The Betti numbers agree with S6_04 D.1 (H_2 = Z^(d-1) + Z/d,
H_4 = Z^(d-1), Euler number 2d), a different run. B3.1 (the comparison of the cover with X) is unread.

**E2.2, the combs: the tangent cohomology agrees with a second run; the Hodge numbers are bounds.**
h(T) = (2m+1, 8m+1, 6m+1, 0), the same as S6_03 E15; K = f-bar^* O(-24m-6); h^(p,0) = 0;
h11 = 4m + 1 + h^0(K_m), h12 = 4m + h^0(K_m), with h^0(K_m) undetermined (E2.3). I read the first half of the
proof (the two extensions by O(24m-1), the canonical bundle, the vanishing of forms).

## 3. Consistency with the four finals

- **Tangent cohomology.** S6_01 D1.3, D2.1, D3.1 ((1,1,1,0), Kodaira-Spencer isomorphism, smooth Kuranishi line) are
  the same statements as the first run's A.5.2, PUSH E.2.1 and S6_03 E9. D4.1 (integral twists; a torsion summand at
  p_1 of length 1 iff 3 does not divide n) is S6_03 C5b; D1.3's coarse direct images O + O(-1), O + 2O(-1), O are
  C5b at n = 0. D4.2 (generic twist (0,0,1,0)) fits S6_03 C4b and C5c. Combs: equal to S6_03 E15.
- **Fibration and K_X.** K_X, the pencil, E1.1 (small deformations keep the pencil, a = 1) agree with the first run
  and with PUSH E.2. B2.2's anticanonical degree d = 4l + 3k - kl is -D of PUSH E.2.22.
- **Periods.** A2.3 (mu is the zero of wp, the section is +-P_*) is the first run's B.1.3; A2.1 gives order 2 of the
  period determinant at z_1 and 0 at z_2, as in the first run's F.3.3.
- **Real forms.** Nothing in S6_01 concerns them. No conflict.
- No conflict found anywhere.

## 4. Credit

- **[AC26].** The construction; K_X; h^(0,q) = (1,1,0,0); h^(p,0) = 0; the relation h11 = h12 + 1 with "the expected
  value is h12 = 1" (Remark 9.21); a(X) = 1; Aut^0 = C^*; the Betti numbers of the members with fundamental group
  Z/|p|.
- **Earlier work on a hypothetical complex S^6**, to be cited where their conditional statements become
  unconditional for X: Gray (h01 > 0), Ugarte (relations among the Hodge numbers and the Frolicher sequence), McHugh
  (arXiv:1708.03251, Bott-Chern and Aeppli numbers as functions of the Hodge numbers), Angella; Stelzig for the
  structure theorem. I name these from the return's citations and from memory of the literature; the references
  must be opened before printing.
- **[E26].** No Dolbeault cohomology (survey of 12 November). Viaclovsky leaves the Hodge numbers of his families
  open (arXiv:2609.33785, Section 6.2; arXiv:2610.10451, Question 2).
- **arXiv:2610.00250v1.** The tangent cohomology and the Kuranishi line (Part D here). Nothing of Parts A, B, C.
- **Ours.** The value h12 = 1 and the full table: first in the workbench (GPT-5.6 Sol in Codex at reasoning effort
  ultra, 27 August 2026), where the scalar was obtained from a degree count and not evaluated; now with the exact
  determinant identity, the closed value of the scalar and two more proofs (GPT-6 Astra, ChatGPT Pro mode, this
  run). Also ours: the Frolicher ranks, the Bott-Chern and Aeppli tables and the square-zero ideal for X, the
  canonical bundle and Hodge numbers for all coprime (3k,4l), the covers, the comb formulas, and the corrections
  A4.2 and E2.4.

## 5. Proposal for the paper

**Place.** A new section 5, "The cohomology of X", before the deformation section (which becomes 6): both rest on
the same direct images on the root curve, and the Hodge table is the answer to a question [AC26] left open.

| Sub-section | Content | Rows | Status |
|---|---|---|---|
| 5.1 | Direct images of O, Omega^1, Omega^2; the determinant identity 6 mu_z^2 - tau_z beta_z = tau_z^2 E_4^2/E_6; the scalar mu_s(0) = 4i sqrt(pi)/(3^(3/4) Gamma(1/4)^2) | A1.0-A1.3, A2.1, A2.2, A2.4 | Theorem (two derivations; scalar checked here) |
| 5.2 | The Hodge table of X_c for every admissible c | A3.1 | Theorem |
| 5.3 | Frolicher: E_1 != E_2 = E_infinity, ranks (1,1,1,1) | C1.1 | Theorem |
| 5.4 | Bott-Chern and Aeppli numbers; N^2 = 0 | C2.1, C3.3 | Theorem for the numbers; N^2 = 0 a theorem once C3.1 has been read, announcement until then |
| 5.5 | The other members: K_X and (h11, h12) = (2,1) for coprime (3k,4l); the covers with h11 = n + 1 | B2.1, B1.2, B3.2, B3.3 | Theorem for K_X and for the covers' numbers (Betti numbers confirmed by S6_04 D.1); the (3k,4l) Hodge numbers an announcement until B1.1-B1.2 are read |
| 5.6 | No balanced, strongly Gauduchon, SKT, astheno-Kahler, lcK or Hermitian-symplectic metric | C3.5, C3.7 | Announcement (unread) |
| remark | The correction of [AC26] Remarks 1.3 and 9.21 (torsion of the relative differentials) | A4.2 | Remark, with [AC26] credited for everything else |

Out of this paper: the combs (E2.1-E2.3) beyond one sentence with the two-run value of h(T); E2.4. E2.4 says a
printed corollary of Huckleberry-Kebekus-Peternell is false for the combs. The mechanism is credible (the bound was
deduced from the CDP statement), but the source has to be read before the sentence is written anywhere, as with
S6_05 A.5.7. It belongs with the CDP note.

One reading still owed before 5.1-5.2 are printed: A1.1-A1.2, about ten pages, by the S6 expert (Claude Fable 5.2
at effort max) or by me in a later bounded round.

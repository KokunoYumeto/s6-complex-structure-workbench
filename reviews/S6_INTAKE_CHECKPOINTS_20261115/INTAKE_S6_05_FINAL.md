# S6_05_ARITHMETIC, final return: bounded intake

By the S6 intake agent, Claude Fable 5.2 at effort high, 15 November 2026. The return is by GPT-6 Astra (ChatGPT Pro
mode): `returns\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped\S6_05_ARITHMETIC\`. This is not the full intake.
Read: the results CSV in full (88 rows), the report's outcome table, its sections on corrections and on remaining
obstructions, the proof of C.8.5 in `sections/C_analytic.tex`, and the statement and opening of A.4.4 in
`sections/A.tex`. Not read: every other proof, the code, the PDF. "Proved" means the run's label unless I say I
checked something. The comparison with checkpoint 02 is against my notes in `INTAKE_PRELIM.md` (that folder has been
folded into the final).

## 1. Verdicts

The report's first line is INCOMPLETE; its table is headed "final state at the four-hour assessment", so the run
delivered at its hourly check. 88 rows: 77 proved, 6 known, 3 refuted, 1 open, 1 computed with error bounds.

| Part | State | Evidence, and what I checked |
|---|---|---|
| A.1-A.3 the count, the group, the unrestricted count | settled (proved; A.3.1 known with derivation) | Exact census to 10^9 (R(10^9) = 35,363,970); the quotient is a (0;2,2,2,2,2) orbifold with lambda_1 > 1/4 by a Cheeger argument. Not checked. |
| A.4 sharp-arc bound O(X^(2/3+eps)) | labelled proved (A.4.4) | A written proof by an angularly uniform Mellin transform, cutoffs X^(1/3). I read only the statement and the set-up. **Unchecked and the hardest claim of Part A.** |
| A.5 mean square, Omega-results | mean square O(X^(2+eps)) proved (A.5.5); **Omega_+ and Omega_-(X^(1/2)) now proved (A.5.8)**; A.5.4 open | A.5.8 rests on a stationary-phase argument with one positive leading coefficient. A.5.4 is the sub-item "name a numbered known conjecture that implies the square-root bound": none found; one candidate (Biro 2026, Conjecture 1) is reported false as printed (A.5.7). Not checked. |
| B.1-B.2 the lattice J | settled (proved by exact computation) | Aut J of order 12,597,120; **129 Co0-orbits of totally isotropic planes**, total mass 61,549,107,892,647,466,000 with zero residual. Hand check (mine): that number equals the count of totally singular lines of the 24-dimensional plus-type quadratic space over F_3, 47,071,766,560 x 5,230,235,650 / 4. |
| B.3 Weyl h/d rule | refuted (B.6) | 11 exceptions among 96 cases; first one E8^3, d = 2 gives D8^3 (Coxeter number 14, not 15). Not checked. |
| B.4 cubic | settled (proved) | Stabilizer A4 x (C7:C3), order 252; two embeddings with different value groups. Not checked. |
| C.1-C.3 my closed forms (Leads 7-9, 12) | settled (proved) | Values at z1, z2; nomes i w/216 and -w^2/48^3; relation (27/64); expansions. At t = 0: L = (1/4) log 3 + (7/192) Re t - B abs(t)^(4/3), so neither maximum nor minimum. Consistent with my numerics. |
| C.4 N on the torsion locus (Lead 10) | settled (proved) | N^12 = abs(Delta) / abs(psi_m(P))^(12/(m^2-1)), m = +-1 mod n. Hand-checked at t = 1, 32/5, 0 (in INTAKE_PRELIM). |
| C.5 CM and torsion (Lead 11) | settled (known with derivation) | Bourdon-Clark-Stankewicz Theorem 4.15(a). Not checked against the source. |
| C.8 N <= sqrt2 without intervals; level sets | settled (proved, two ways) | C.8.5: steps n = 2, 4, 8 of N(P)^(n^2) = N(nP) abs(Delta)^((n^2-1)/12) / abs(psi_n(P)) with uniform bounds N(2P) < 17/10, N(4P) < 3/2, N(8P) < 143/100 on shrinking ranges of Im tau, and a local disc. **I checked every displayed inequality of the proof and the size of the three uniform bounds** (the maximum of N over the torus at tau = iT is about e^(pi T/12)(1 + 2e^(-pi T)): 1.694, 1.478, 1.418 at T = 2, 7/5, 11/10). I did not check C.8.1-C.8.3 (the uniform bounds and the local disc) line by line. Second proof: C.8.12-C.8.15, (t-1) L_t = X(X-2)/24 with abs(1 - X) < 1 away from t = 1. |
| C.6 heights at the eleven rational CM fibres | settled (proved; C.6.R2 computed) | Ranks (two fibres have rank 2), nine exact rational factors in L'/Omega = q h (8, 4, 32, 4, 8, 4, 16, 16, 576), three with trivial Sha certified; six via a Gross-Zagier argument with genus characters (C.6.R5, new). Not checked; heavy. |
| C.7 algebraicity of N at CM points off the torsion locus | (a) proved, (b) conditional, **(c) open** | The smallest instance: E: y^2 + y = x^3 - 38x + 90 (conductor 361, CM by -19), P = (0, 9): N(P) = exp(-L'(E,1)/(4 Omega)), h = 0.0906458370...; no proof either way. Twelve statements record what the tried routes give and where each stops. |

**Changed since checkpoint 02.** About nine new rows. A.5: the Omega-results moved from open to proved (A.5.6-A.5.8),
with two kernel lemmas (A.4.7, A.4.8) and the refutation A.5.7. C.6: the six numerical factors are now exact
(C.6.R5). B.9: the earlier residual in the mass is resolved. C.7: four more obstruction statements (C.7.9-C.7.12);
(c) is still open. No status went backwards.

**Still open, and why.** A.5.4 (a published conjecture implying the square-root upper bound: the candidates fail on
uniformity in the twist; the run states its own exact sufficient condition instead). C.7(c) (a transcendence
question about exp of a canonical height; every route tried needs a period conjecture or loses the real Gaussian
factor). Both are open in the literature as far as the run found; neither is a gap in a proof.

**Stated more strongly than the evidence I saw supports.**
- A.4.4, A.5.5, A.5.8 are three new theorems of analytic number theory (sharp-arc exponent, mean square, two-sided
  Omega) whose only checks are the run's own "independent audits". They should be called claims until read.
- A.5.7 says a conjecture printed in a 2026 paper is false. It cites Louvel 2012 Theorem 1 for a linear main term.
  Nothing should be said outside before both sources are read.
- C.6.R5 gives exact rational factors and "analytic BSD quotients" (1, ..., 9); the report itself says these are not
  claims about Sha. Keep that wording.
- B.9 and B.4 are exact computations; the claim is as good as the code, which I did not run. The total mass passes
  my hand check.
- "Proved" for A.5.1 means a certified finite computation on [10^4, 10^9], not an asymptotic statement; the report
  says so.

## 2. What bears on the three running prompts and on later ones (no prompt changed in this round)

- **S6_02_PUSH.** (i) Its D.4 (level sets of D_part, "regular crossing at t = 0") and S6_05 C.8.15, C.3.2 (t = 0
  non-critical C^1 on the t-line, cubic degenerate on the root chart; every lower level one star-shaped Jordan
  curve) describe the same thing and read as consistent; compare in the full intake. (ii) The maximum now has four
  proofs on paper: the mpmath certificate, the Arb certificate (PUSH E.4), the duplication ladder (C.8.5), the
  critical-factor argument (C.8.15). The limitation "one interval library" in my finding F3 is lifted if any one of
  the last three holds. (iii) Nothing on the limit at w = 0 or on Theta_7.
- **S6_04_MAPS_MANIFOLDS.** C.2.2 (real locus and antiholomorphic involutions, "actual finite affine twists
  checked") is a second treatment of what S6_04 A.3 does; the two must agree on which half of the imaginary w-axis
  has one or two non-empty real forms.
- **S6_03_CDP.** Nothing direct. C.6.4 restates the admissibility bound as a height inequality (generic height 1/12
  relative to (O), variation divisor (infinity)/12); it is a reformulation, not an input to CDP.
- **Prompt updates the findings call for (later):**
  1. Any later prompt that quotes "R4" (N <= sqrt2) with "one interval library" should quote C.8.5 and C.8.15 as
     certificate-free proofs, marked "checked once at the displayed inequalities".
  2. The closed forms are no longer Leads: beta^part(z1), the nomes, (27/64), the expansion constant 2i/(3 pi), and
     e^(2 pi D_part) = N^12/12^6 with N^12 = abs(Delta)/abs(psi_m)^(12/(m^2-1)) on the torsion locus go into the
     "Results this builds on" of later S6 prompts.
  3. A.5.4 as worded ("which known conjecture implies it") should not be sent again: it is a literature question.
     If the square-root bound is wanted, the item is the run's own sufficient condition (square-root cancellation
     of the ideal-character sums U_l(X) uniformly for abs(l) <= sqrt X).
  4. C.7(c), if pursued: one instance, the conductor-361 point, with the routes of C.7.9-C.7.12 named as closed.
  5. The lattice results (129 orbits, the 11 exceptions, Aut J, the cubic stabilizer) belong to the lattice lane,
     not to S6; a rerun of the code and a literature check (Chenevier-Lannes) come before any use.
  6. A.5.7: read Biro 2026 and Louvel 2012 before the claim is repeated anywhere.

## 3. Points for the S6 expert (aa7b8224, Claude Fable 5.2 at effort max)

1. Route 3.1 of ROUTES.md (the duplication ladder) is carried out as C.8.4-C.8.5; I checked the displayed
   inequalities, not C.8.1-C.8.3. Is the ladder as you intended it, and are the three uniform bounds on N(nP) sharp
   enough everywhere in the fundamental domain (they are tight at Re tau = 0: 1.694 against 17/10)?
2. Route 3.3 (critical points of L): C.8.15 says there is no saddle on (0,1) and t = 1 is the only critical point
   of L on the t-line apart from the degenerate behaviour at t = 0. That refutes the saddle of a Lead; does it
   contradict anything in your six facts?
3. Route 2 (algebraicity at CM points): C.7 ends where you expected (period conjecture needed). C.7.9-C.7.12 list
   four unconditional routes and the missing hypothesis of each; is there a route they did not try?
4. The identity N(P) = exp(-h(P)) at the conductor-361 point, with all finite local heights zero, turns the question
   into the transcendence of exp(L'(E,1)/(4 Omega)). Is that a known open problem under a standard name?
5. C.6: the factors q (8, 4, 32, 4, 8, 4, 16, 16, 576) and the two rank-two fibres (j = 8000, -12288000). Do they
   bear on the torus-fibration Lead 9 you put into S6_03 and S6_05?
6. The measure of C.8.9-C.8.10 (mass 1/12, sign db wedge da) corrects a Lead; check it against your normalization.
7. Which of the unchecked analytic claims (A.4.4, A.5.8) is worth a full read, given that Part A has no map to X?

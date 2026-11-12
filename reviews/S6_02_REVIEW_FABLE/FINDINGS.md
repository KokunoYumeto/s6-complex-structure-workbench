# Findings of the review of S6_02_FAMILY (Part II of REVIEW.md)

Saved by the main session from REVIEW.md, Part II, on 12 November 2026: the review agent (Claude Fable 5.2, effort high) could not create a file of this name (a guard refused it).

# Part II. Numbered findings F1-F19

This part is the text meant for `FINDINGS.md`. The session's file guard refused a file of that name written by a
sub-agent ("return findings as text"), so the findings are kept here and are also in the final message of the review.

Every finding is checked by AI only: Astra's written proof, and this one review. "Mine" marks statements that are not
in the return; they are numerical or sketched unless said otherwise. Each entry: the statement; its status; what it
settles and for whom; how new it is.

## Literature

**F1. A paper the survey and the workbench did not know: arXiv:2610.00250.** Du, Guo, Kusakabe, Xie. Version 1
(23 September 2026), "Oka Geometry and Deformations of Torus-Fibred Complex Six-Spheres", states (Theorems 1.3, 1.4
and the introduction): the Kodaira-Spencer map of the period family is an isomorphism, the Kuranishi germ is a
smooth reduced line, h^q(T) = (1,1,1,0), Aut(X_a) = C^*, and X_a is biholomorphic to X_a' exactly when a' - a is in
2Z. Its domain is Im a < -M0 with M0 not evaluated. Version 2 (23 October 2026), "Oka Geometry of Complex
Six-Spheres", has none of this (Sections 6-7 gone). It attributes the construction to Alpoge.
- Status: titles, dates and the v1 statements confirmed from arxiv.org (the HTML through a summarizing tool). The
  proofs of v1 were not read; the reason for the cut is unknown.
- Why it matters: survey findings F2 (classification), F8 (deformation space), F29 (Aut) and the card
  `s6-cdp-framing` list these as not in print. They were in print from 23 September to 23 October 2026 and are still
  on arXiv as v1. The workbench proof of the classification is dated 6 September 2026, seventeen days earlier; whether
  it was public then has to be read from the repository history. Any framing must cite v1 and say what happened to it.

## Settled by the return and confirmed here

**F2. The classification, with numbers.** X_c is biholomorphic to X_c' iff c' - c is in 2Z; the family exists exactly
for Im c < (3/pi) log 6; the isomorphism classes are the punctured disc 0 < |w| < 216, w = e^(-pi i c).
- Status: correct (A.2.1, A.3.1, A.5.1 rechecked by hand and program; C.2.3 below). The 2Z statement is known (F1);
  the radius 216 and the description of the moduli as a disc of that exact radius were found nowhere else.
- Settles [AC26] Remark 6.4 ("left open") and survey F2, F21.

**F3. M = -(3/pi) log 6, attained only at the multiplicity-four fibre.** Equivalent form: at every zero v of wp_tau,
e^(-pi (Im v)^2 / Im tau) |theta1(v,tau)/eta(tau)| <= sqrt2, with equality only on the orbit of tau = i.
- Status: correct. The proof is an analytic cusp bound, an analytic local argument on |tau - i| <= 1.5e-4, and an
  interval certificate of 19,701 boxes. I re-ran the interval proof on all boxes (identical bounds), re-derived the
  local argument by hand, and confirmed the picture with independent floating-point code. Limitation: one interval
  library (mpmath).
- New: the course used a made-up value in an exercise; arXiv:2610.00250v1 leaves M0 unevaluated.
- Mine: D_part = M - (2/pi) |tau - i| + O(|tau - i|^2) near the maximum (numerical, 30 digits for the constant).

**F4. The deformation theory is complete for the (3,4) family.** h^q(X_c, T) = (1,1,1,0); smooth reduced
one-dimensional Kuranishi space; the w-family is miniversal; every small deformation of X_c is some X_c'.
- Status: correct; every direct image and cohomology group recomputed; chi(T_X) = 1 agrees with
  Hirzebruch-Riemann-Roch (c3/2). Known (F1), with a proof here that does not depend on v1.
- Settles survey F8 and Viaclovsky's Question 2 for (3,4). Consequence: every small deformation of X_c has algebraic
  dimension 1 and carries the pencil |-2K|.
- H^2(T_X) = H^2(dP6, K) = C: the obstruction space is carried by the normalization of the non-normal fibre W.

**F5. All discrete data.** Complete invariants (|p|, e^(-pi i (c + k2))), p = 12 l0 - 4 r1 - 3 r2, for all admissible
twist vectors and cusp collars of [AC26]. Every S^6 member of the (3,4) family is exactly one X_w. For fixed u,
Engel's X(u, a0, a1) with |12 psi(a0 + a1)| = 1 are two classes, exchanged by the monodromy around u = 0.
- Status: correct (norm criterion verified on 604,800 data; cusp steps read). The sketch G1a-13(a) of the survey is
  now a theorem. Whether arXiv:2610.00250v1 Section 7.3 covers part of it is unchecked.
- Settles survey F3 and answers Viaclovsky's Question 3 for multiplicities (3,4): yes, exactly one more.
- For X_(3k,4l) (coprime): identification subgroup 2kl Z, 2kl classes at fixed u. Correct with a gap: the dictionary
  to Viaclovsky's coordinates is not written.

**F6. A correction to Engel's Remark 8.1.** The proper holomorphic family with fibre X(u, a0, a1) lives over the
punctured w-disc, w^2 = u. Over the u-disc the fixed-data family does not exist: psi(a0) is in (1/3)Z minus Z, so the
datum moves under the u-monodromy, and X_c, X_(c+1) are not isomorphic. Independent witness: j(Alb S2) is not even in w.
- Status: correct; Engel's sentence and his Construction 3.5 read. It is a one-line slip in a remark, not an error in
  a theorem. The course already says "closes up only on the double cover" (survey F4).

**F7. Automorphisms and real structures.** Aut(X_c) = C^* (known, F1). The conjugate complex manifold of X_c is
X_(1 - cbar). Exactly the members with w in iR have antiholomorphic diffeomorphisms, and antiholomorphic involutions;
their full group is C^* semidirect Z/2.
- Status: correct; the shift by 1 confirmed independently through the Albanese moduli. The real-structure statements
  were found nowhere else. The fixed locus of the involution is a closed 3-manifold in S^6, not yet identified.

**F8. The periods in closed form.** beta^part = (6i/pi) Log(theta1(mu,tau)/(2 sqrt3 eta(tau))); mu is the
Eichler-Zagier zero of wp; e^(2 pi i mu(p0)) = -(5 + 2 sqrt6); mu(z1) = (2 - rho)/3, mu(z2) = (1 - i)/2;
beta^part(z2) = i(3/2 - (3/pi) log 6).
- Status: correct; the transformation laws of [AC26] page 2 checked against the theta laws by hand and numerically.
  Settles survey F5 (the identification) and the "obtain beta" part of C.1.
- Mine (60 digits, proof to be written): beta^part(z1) = -1/2 + i(1/sqrt3 - (3/(2 pi)) log 48); the Albanese curves of
  the multiple fibres have nomes q(Alb S2) = i w/216 and q(Alb S1) = -u/48^3, so q(Alb S1) = (27/64) q(Alb S2)^2;
  admissibility is |q(Alb S2)| < 1 and the moduli of the family is the punctured unit disc in q = q(Alb S2).

**F9. The scalar on which the Hodge diamond rests (survey F1) is non-zero.** Near the order-four point,
(mu - (1 - tau)/2)^2 = (2i/(3 pi)) (tau - i) + O((tau - i)^2), so d mu / d s2 at z2 is non-zero.
- Status: non-vanishing follows from the local argument of C.2.2 (e2'(i) = i d with 10.03 < d < 10.04 certified,
  g2(i) != 0); the constant 2/(3 pi) is mine, numerical (`checks/v5_slope.out`). It is the quantity S6_01 Part A asks
  to evaluate.

**F10. Klingler's question.** Gamma = <A1, A2> has index 12 in the integral stabilizer of delta-hat (kernel of an
explicit character to Z/12), Zariski closure the whole stabilizer. Gamma does not act properly discontinuously on
D = Sp4(R)/U(1,1). It does on O = {psi(delta-hat, J delta-hat) != 0}, the largest such open set, and
psi(delta-hat, J delta-hat) = -6/D, so all admissible periods lie in O_+. The period map embeds the affine t-line
properly in Gamma\O_+.
- Status: correct (matrices and group law by program; the homogeneous-space argument by hand). Settles survey F28 and
  Engel's Remark 8.4 in the form Klingler suggested ("or at least on an analytic open set"). Found nowhere else.

**F11. Fibres and curves.** The Neron-Severi equation for every fibre; abelian iff a class with Pf < 0, elliptic
quotient iff a class with Pf = 0; first-projection quotient exactly at t = 64(47 +- 27 sqrt3)/11; torsion fibres
abelian; all curves vertical, no rational curve outside W, elliptic curves in ordinary fibres.
- Status: correct; mostly standard torus theory applied to Pi. Lead 6's wording was too broad (a special c gives an
  extra elliptic quotient at t = 32/5); the workbench statement stands. The orientation remark on [AC26] Lemma 9.4
  (eta^2 = -12 in the complex orientation) is right and matters for signs only.

**F12. The cusp fibre.** Gluing constants (-a^-1, a^6, -a^-7 u); W_c is isomorphic to W_c' iff c' - c is in Z; the
C^*-fixed double curve is the one of direction e2. Status: correct (the hexagon enumeration by rerun). Settles the
W-part of survey F21: W depends on u only, the threefold on w.

## Not settled

**F13. The boundary |w| = 216 (C.3).** Proved: only the fibre over t = 1 degenerates; its torus cover becomes
C^2 modulo a group of real rank 3, a non-compact Lie group (rational case) or a non-Hausdorff quotient. Not decided:
whether the family has any limit as a complex space.
- Mine (sketch): with F8, j(Alb S2) = j(i w/216) has the whole circle as natural boundary; from this a non-extension
  theorem for the family follows by extending the anticanonical divisor (IMPLICATIONS 3.1). The non-separated
  directions at the collapsed fibre span the complex line C(2,-1).

**F14. The limit w -> 0 for the untwisted family (E.1, Engel's Conjecture 8.2).** Proved: the candidate Q exists as a
compact complex space, T^1 = pi^* O(1), pi_1 = Z, H_* = (Z, Z, Z^8, Z^7, Z^10, 0, Z), chi = 12; its plumbing is flat
and proper away from infinity; at the node over infinity the plumbing is xy = uzv, whose fibres for u != 0 are nodal.
Not decided: whether a filling with central fibre Q exists.
- Mine (sketch): the nearby fibre of the plumbing has Euler number 1, while chi(X(u)) = 2; so the plumbing of Q
  degenerates the nodal contraction of X(u), and the limit of X(u) itself should have normalization a blow-up of
  P_S(O + M) along a curve. This would refute the conjecture as worded and give the corrected statement.

**F15. The limit for the S^6 family and the class in Theta_7 (E.2).** Proved: semistable limits of the two reduced
bielliptic surfaces after w = s^6 (cycles of 4 and 3 ruled surfaces, with their homology). Not done: any
neighbourhood of the multiple fibres in a limit, the central threefold, its topology. The monodromy of the w-family
in pi_0 Diff^+(S^6) = Z/28 is not computed; what the return calls a reduction is the definition of the invariant.

**F16. Why three items came back open.** The sent prompt allowed "(c) partly settled". C.3, E.1 and E.2 stop exactly
where a first construction failed, with no second approach tried.

## About the return

**F17. No error found in 55 statements.** 44 correct, 2 correct with a gap (B.3.1, E.2.2), 6 known, 3 open, 0 wrong.
Label corrections: A.5.1, A.5.2, B.4.1 are Known (F1), E.2.2 is not a reduction, lambda0 = 1 is a normalization,
D.1.3 refutes a wording. Its corrections of the course (component label E_(2,-)) and of Engel's Remark 8.1 are right.

**F18. Every mathematical program reproduces.** Identical outputs except platform digits and one sign convention;
the interval proof re-executed in full.

**F19. Credits to add** when any of this is written up: the workbench and course (classification, 6 September and
11 October 2026), the survey readers' sketches (all-data classification, Aut, Albanese cross-check, abelian fibres),
arXiv:2610.00250v1, Oguiso-Shioda and Shioda (Mordell-Weil), Eichler-Zagier, Kodaira, Mumford, Kervaire-Milnor;
list in section 6 above.

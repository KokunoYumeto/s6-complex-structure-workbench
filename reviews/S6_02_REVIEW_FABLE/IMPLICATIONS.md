# S6_02_FAMILY: implications

Claude Fable 5.2 (Anthropic), effort high, 12 November 2026, 22:45 UTC. Based on `REVIEW.md` in this folder. Statements
marked "mine" are not in the return; where they are sketches they say so, and a sketch is a route to be proved in the
push run, not a result. All checking so far is by AI (GPT-6 Astra's proofs, this review); no human has read any of it.

## 1. What is now settled for the workbench

Survey finding, what the return and the review give, what is left.

| Survey | Now | Left |
|---|---|---|
| F2 classification | Proved again and checked: c mod 2Z; moduli = punctured disc 0 < abs(w) < 216. | Nothing mathematical. Priority: arXiv:2610.00250v1 (section 2). |
| F3 all discrete data | Theorem: invariants (abs(p), e^(-pi i (c+k2))); two classes at fixed u. | Dictionary to Viaclovsky's coordinates for (3k,4l). |
| F4 dictionary with Engel | Proved; u = w^2 with the cusp-normalized reference; Remark 8.1 corrected. | A canonical scale for u does not exist; say so. |
| F5 mu | mu is the Eichler-Zagier zero; beta^part in theta functions; special values. | Proofs of the closed forms at z1 (mine, numerical). |
| F8 deformation space | h(T) = (1,1,1,0), Kuranishi smooth of dimension 1, family miniversal. | Same for X_(3k,4l) and the other families. |
| F12 KS != 0 | Subsumed. | |
| F17 anticanonical ring | Re-proved. | |
| F20 special fibres | Complete: NS equation, loci, the two values of t, torsion fibres; Lead 6 corrected in wording. | |
| F21 M and the boundary | M = -(3/pi) log 6, only at t = 1; W depends on u only. | The boundary object (3.1). |
| F22 fillings, Albanese | Proved; (mine) nomes i w/216 and -u/48^3. | |
| F27 limit w -> 0 | Candidate and local facts only. | Open (3.2, 3.3). |
| F28 Klingler | Answered: not on D; yes on the explicit maximal open set, which contains the period image. | |
| F29 Aut | C^* exactly; plus the real structures. | The real locus as a 3-manifold. |
| survey F1 (Hodge diamond), its scalar | mu'(z2) != 0 follows from C.2.2: (mu - (1-tau)/2)^2 = (2i/(3 pi))(tau - i) + ... | Compare with what S6_01 returned for the same scalar. |

## 2. The CDP correction and the new invariants: what changes

2.1 **Novelty has to be restated.** The classification (2Z), the Kuranishi statement, h^q(T) and Aut = C^* were
stated in arXiv:2610.00250v1 (Du, Guo, Kusakabe, Xie, 23 September 2026) and removed in v2 (23 October 2026). The
workbench proof of the classification is dated 6 September 2026. For the card `s6-cdp-framing` and any note:
"classification of the family" and "Aut" leave the list of things "not in the literature"; they become "stated in
arXiv:2610.00250v1 and withdrawn from v2; proved independently in the workbench (6 September) and again, with the
exact domain, on 12 November". To do before framing: read v1 Sections 6-7 and Appendices B-C in full against A.2-A.5
(does their proof have a gap that explains the cut; do they treat other twist data), and establish from the
repository history when the workbench file became public.

2.2 **What is new beyond [AC26], [E26] and arXiv:2610.00250v1, as far as the return's search and mine go:** the exact
radius (M = -(3/pi) log 6, moduli disc of radius 216); the classification over all discrete data and the two classes
at fixed u (Viaclovsky's Question 3); the double-cover correction to Engel's Remark 8.1; conjugate and real
structures; the theta formula for beta and the closed special values; the monodromy group (index 12) and the answer
to Klingler's question; the Neron-Severi equation and the fibre loci; W_c up to isomorphism; (mine, to be proved)
q(Alb S1) = (27/64) q(Alb S2)^2 and the moduli as the unit disc of q(Alb S2).

2.3 **For the CDP correction itself.** S6_02 does not touch the CDP argument, and it adds two facts that belong in
that story:
- At L = O the groups CDP's theorem is about are now exact: h^q(X, T_X) = (1,1,1,0). H^0 = C is the C^*-action;
  H^2 = C is H^2(dP6, K_dP6), entering through 0 -> T_X(-log W) -> T_X -> nu_* N_nu -> 0 with N_nu = K_dP6. So the
  group that the vanishing statement misses is carried by the normalization of the non-normal fibre: the same place
  where [AC26] Section 10 locates the failure.
- Mine (lead, two lines, to be checked in S6_03): tensor that sequence with any L in Pic(X). nu^* L is trivial
  (Pic(X) -> Pic(dP6) is zero), so the quotient is nu_* K_dP6 again and H^2(X, T_X tensor L) -> H^2(dP6, K) = C is
  onto whenever H^3(X, T_X(-log W) tensor L) = 0, which holds when R^2 f_* of that sheaf is a torsion sheaf (general L).
  That is "H^2(X, T_X tensor L) != 0 for every L" with the reason visible, and it works for any torus fibration with
  a normal-crossings fibre whose normalization has H^2(K) != 0.
- Every small deformation of X_c is an X_c' (F4), so a = 1 on a whole neighbourhood of the family in the space of
  complex structures: the family is not a degenerate corner of something with a = 0.

2.4 **Status words.** Nothing here is established beyond AI checks. For the community the classification with its
numbers and the Klingler answer are the two results easiest to state and to verify by hand; the interval certificate
is the one piece a reader cannot check without a computer.

## 3. The unfinished items: exact targets and routes

### 3.1 C.3, the boundary |w| = 216

What is proved: at Im c = (3/pi) log 6 only the fibre over t = 1 degenerates; the torus cover of the order-four
filling becomes C^2 / Pi Z^4 with Pi of real rank 3; kernel R(1, 3, -3, -x - 3/2), x = Re c.

**Target A (non-existence of a limit in families).** For every w0 with |w0| = 216 and every open U containing w0 there
is no flat proper holomorphic map from a reduced complex space to U whose restriction to U intersect {|w| < 216} is
the family (X_w). Route (mine, sketch):
1. j(Alb S2(w)) = j(q) at q = i w/216 (needs the proof of Re kappa2^part = 3/2, which C.1.1 gives, and
   Im kappa2^part = M). The modular function has the unit circle as natural boundary, so j(Alb S2) continues across no
   point of |w| = 216.
2. Suppose an extension over U exists. The total space is smooth over V = U intersect {|w| < 216}; the images of its
   singular locus and of the critical points of the projection are analytic in U and miss V, hence discrete. Shrink
   to U' where the map is a smooth proper family.
3. pi_* omega^(-1) is coherent and torsion-free, hence invertible, of rank h^0(-K_(X_w)) = 1. A generator sigma
   restricts on X_w, w in V, to the section with divisor 2 S2(w) (base change holds on V since h^0 is constant).
   The component D1 of div(sigma) containing the S2(w) is proper and surjective over U'; off a discrete set its fibres
   are smooth surfaces diffeomorphic to S2 (Ehresmann), so Kahler with one-dimensional Albanese, and j(Alb) is
   holomorphic there. It continues j(Alb S2) across boundary points: contradiction.
Points to make rigorous: step 3 on base change and on the irreducible component; the reduction of a flat proper map
from a reduced space to the smooth case. If it holds, C.3 is settled in the sense "no limit as a complex space in any
family", which is stronger than what the prompt asked.

**Target B (the object that does exist).** Describe the complex-analytic object at a boundary parameter: X minus S2 is
an honest non-compact complex manifold; over t = 1 the root family is (Delta_s x C^2)/Lambda with a non-free,
non-properly-discontinuous action at s = 0. Mine (sketch): from the laws at z2, mu = mu2 + b s + ..., beta = beta2 -
6 b s + ..., b != 0 (finding F9), so the kernel vector acts on the fibre over s by translation by
3 b s (2, -1) + O(s^2): the non-separated directions at the central fibre fill the complex line C(2,-1), which is the
E_i-direction in the coordinates of C.3.2. So the largest Hausdorff quotient collapses the elliptic factor and leaves
C / (Z/2 + Z(x + 3/2)) before the finite quotient: C^* for rational x + 3/2, non-Hausdorff otherwise. Exact targets:
(i) prove this; (ii) decide whether (X_c minus S2) union that curve is a (non-compact) complex space and whether it
is the Hausdorff limit of X_c along Im c -> -M with Re c fixed; (iii) state the foliated description (the linear
foliation of the central torus by C(2,-1), closed leaves iff x + 3/2 rational).

**Target C (beyond the boundary).** For Im c > -M the locus D_c = 0 is a real curve around t = 1 in B; say what the
construction gives over its exterior (a non-compact manifold with a hole) so that "the family exists exactly for
|w| < 216" is complete.

### 3.2 E.1, Engel's Conjecture 8.2 for the untwisted family

What is proved: Q = P_S(O + M) with the sections glued by t_6P is a compact complex space, T^1_Q = pi^* O(1); over
B minus infinity the plumbing ab = u phi is flat, proper, and has Engel's X(u) as fibres; at the node of S_infinity
the plumbing is xy = uzv, whose fibre for u != 0 has an ordinary double point; the blow-up of (x,z) resolves it and
changes the central normalization.

**Target.** One of: (a) a flat proper filling of X(u) over the u-disc with central fibre exactly Q; (b) a proof that
none exists, together with the correct limit: an explicit flat proper filling, its central fibre, the normalization
of that fibre, its Euler number, pi_1 and H_*.

**Route 1 (construction, toric).** Near infinity the family over the (q,u)-bidisc, q the base coordinate at infinity,
is a two-parameter Mumford degeneration: (C^*)^2 modulo the two periods with valuations (in (q,u)) of x1, x2 equal
to ((1,0),(0,0)) and ((0,0),(-1,-1)) up to the signs fixed by B_0. Take the Lambda-bar-periodic fan in
R^2 x R^2_(>=0) with rays (k, l, 1, 0) and rho_l = (0, l, 0, 1) and maximal cones the prisms spanned by
(k,l), (k+1,l), (k,l+1), (k+1,l+1) at height (1,0) and rho_l, rho_(l+1). Each prism is the cone of xy = uzv. Then:
- the unsubdivided fan gives a flat proper family whose fibre at u != 0 is X(u) with the exceptional curve of the
  small resolution contracted, and whose fibre at u = 0 is Q near infinity (to prove; it is the equivariant periodic
  gluing that E.1.5 says is missing);
- a smooth invariant subdivision must cut the bottom square by the A2 diagonal (so that the fibre at u != 0 is
  Engel's Mumford fibre) and the side squares by one of two translation-invariant diagonals; both give a triangulation
  of the prism (orders B < A < rho and rho < B < A); in both the star of rho_l contains two lifts (k,l) and (k,l-1) of
  every ray of the Tate fan, so the central component is the P^1-bundle blown up along a curve over the nodal fibre,
  not the P^1-bundle. Glue with the plumbing of E.1.2 over B minus infinity.
This is my sketch from the fan; every claim in it needs proof (support and flatness of the toric map to C^2, the
identification of the u != 0 fibre with Engel's, properness of the quotient).

**Route 2 (obstruction, Euler numbers).** For any flat proper smoothing of Q the total space is locally xy = g(s,u)
along the double locus S, and chi(nearby fibre) = chi(Q minus S) + integral over S of chi({g(.,u) = 0} near x) =
0 + (contribution of the zero fibre F_b of the leading T^1-section). For b = infinity this is 0 or 1 (C^* contributes
0; the node 1 or 0). But chi(X(u)) = 0 + chi(W) = 2. The plumbing has chi = 1 = chi(X(u) with one P^1 contracted),
which fits Route 1. Gap to close: that the leading T^1-section of any filling of Engel's family vanishes on
F_infinity (true for fillings compatible with the map to P^1 and equal to the plumbing over B minus infinity; for an
arbitrary abstract filling b = 0, 1 are not excluded by the count alone).

**Route 3.** If (a) is still wanted: look for a filling that is not locally a hypersurface smoothing of Q (central
fibre Q with embedded components is excluded by "central fibre exactly Q"); Route 2 says there is none compatible
with the fibration.

Expected outcome: (b). Conjecture 8.2 as worded ("the normalization is P_S(O + M)") is false, and true after
replacing P_S(O + M) by its blow-up along a curve in one section over the fibre at infinity, or after contracting
the exceptional curves of X(u).

### 3.3 E.2, the limit of the S^6 family

What is proved: only the limits of the reduced surfaces S_j(w) after w = s^6.

**Targets.** (i) A flat proper family over the disc of r, w = r^6 (so u = r^12), with smooth total space and reduced
normal-crossings central fibre, restricting to the pulled-back S^6 family for r != 0. (ii) The mu_6-action on it and
the quotient over the w-disc: its central fibre with multiplicities, the singularities of the total space, a
resolution. (iii) Euler number, pi_1, H_* of the central fibres of (i) and (ii); check chi(S^6) = 2 by the
nearby-cycle count. (iv) Decide whether the central fibre is "a logarithmic transform of X(0)" in Engel's sense.

**Route.** Three local models, then gluing by the method of A.3 (translations by sections, H^1 of the sheaf V).
- Over t = 0, 1: on the root disc Delta_(s_j) the torus family degenerates as r -> 0 only through
  e^(-2 pi i beta) = u phi-type scaling with phi a unit, so the plumbing over Delta_(s_j) x Delta_r is the product of
  the smooth elliptic family with the 12-gon Tate model in r (E.2.1 has the charts). The twisted deck generator
  translates by v_j/m_j, whose gamma-part is 1/3 resp. -1/4 of the degenerating period: it shifts the 12-gon by 4
  resp. 3 components and rotates s_j. It has no fixed point, so the quotient is smooth, with central fibre of
  multiplicity m_j along the reduced surfaces of E.2.1. This is the "missing finite-place germ"; it looks like a
  direct extension of E.2.1 from surfaces to the root family.
- Over infinity: the fan of 3.2 Route 1 refined for u = r^12 (rays (0, l, 0, 1/12)-multiples), smooth invariant
  subdivision.
- Descent to w: the group mu_6 acts on the total space over r; compute its fixed loci on the central fibre.

### 3.4 E.2.2, the class of the monodromy in pi_0 Diff^+(S^6) = Theta_7 = Z/28

What is proved: nothing beyond the definition. Phi = F_(2, c0 - 2) composed with parallel transport is the monodromy;
[Phi] corresponds to the homotopy sphere Sigma_Phi.

**Target.** The element of Z/28, with the orientation convention stated; and the same for X_(3k,4l).

**Route 1 (from the filling of 3.3).** The mapping torus of Phi is the restriction of the family to a circle, and it
is (S^1 x S^6) # Sigma_Phi, so mu(Sigma_Phi) is the Eells-Kuiper invariant of that 7-manifold. A resolution W of the
family over the closed w-disc (3.3 (ii)) is a compact complex fourfold with that boundary. If W is spin,
28 mu = (p1^2 - 4 sigma)/32 mod 28 with p1 = c1^2 - 2 c2. If not, use the spin^c form, which is the Todd genus written
without p2: (p1^2 - 4 sigma)/896 - p1 c1^2/192 + c1^4/384 mod 1, with c1 lifted to H^2(W, boundary) (the lift is
unique up to terms that do not change the numbers, since H^2 of the boundary is 0). Mine; the index-theoretic
statement and the spin structure induced on the boundary must be checked before use. All numbers are intersection
numbers on the components of the central fibre. From the semistable model over r alone one gets 6[Phi], that is
[Phi] mod 14.

**Route 2 (structure of Phi).** On torus fibres Phi acts on H_1 by I + 2E or its inverse: it is the twist
x -> rho(-2 theta(x)) x, rho the circle in Aut = C^*, theta the gamma-coordinate, corrected at the special fibres as
in A.3.1. Phi can be chosen S^1-equivariant. The circle action is free off the double curve of direction e2 and has
normal weights (1,-1) there, like the linear action on S^6 in R^3 + C^2. Target: express [Phi] through this twist
(a Gromoll-type or clutching description) and decide whether it is isotopic to the identity. I did not find a
shortcut. The antiholomorphic involution gives no constraint (it reverses both the orientation of S^6 and the loop).

**Route 3.** Show the S^6-bundle over the punctured disc extends smoothly over 0 (then [Phi] = 0), for instance from
a central fibre whose smoothing is a product near every point outside a set over which the bundle is visibly
trivial. Speculative.

### 3.5 Smaller open ends for the push prompt

- B.3.1: write the map from Viaclovsky's data (2.11)-(2.12) to (r_j, s_j, l_0) and re-derive 2kl in his coordinates;
  his Question 1 (are the X_(3k,4l) families in one deformation class) is then: compute h^q(T) for X_(3k,4l) by the
  method of A.5.2 on P(3k,4l) and see whether the Kuranishi space is again the w-disc.
- Prove the closed forms: N(z1) = 3^(1/4) (theta1 at the 3-torsion point of tau = rho),
  q(Alb S1) = (27/64) q(Alb S2)^2, the slope 2/pi (3 e2'(i) = (2/pi) i g2(i)/4).
- A.5.2: replace the citation of the withdrawn v1 lemmas by standard references; state the duality and base-change
  theorems used on the charts of the root curve.
- A second interval library (Arb / python-flint) for the certificate of C.2.3, or a proof of N <= sqrt2 without a
  computer: N^2 is, up to the Gaussian, |theta3(h,tau)|^2/|eta(tau)|^2 at the zero h of wp near the half period; a
  subharmonicity or modular argument might replace 19,701 boxes.
- The real locus: the fixed set of the antiholomorphic involution of X_c, w in iR, as a 3-manifold in S^6.
- The other families (Viaclovsky two-parameter, combs, Liu-Rollenske, Wang, Yang): the method of A.2 needs their
  centralizers and norm groups; A.5 names the first datum to compute for 2609.33785.

## 4. Changes to the unsent prompts

**All three (S6_03, S6_04, S6_05).** Add arXiv:2610.00250 (v1 and v2, both to be attached or named) to the list of
papers after the training data, with the sentence that v1 states the classification, the Kuranishi space and Aut and
v2 does not. Attach the S6_02 return (paper, report, CSV) and this review as material "AI-produced, checked once by AI".

**S6_03_CDP.**
- E.3 ("for X_c: prove that every small deformation carries the pencil |-2K|, or show where this fails"): now a
  consequence of A.5.2. Replace by: verify A.5.2 (it is short), then decide the same for X_(3k,4l), for the |p| > 1
  members and for the other families; and state the theorem "a = 1 on an open set of complex structures on S^6".
- Part C / Lead 4: give h^q(X, T_X) = (1,1,1,0) as a data point, and add the lead of 2.3 (H^2(X, T_X tensor L) maps
  onto H^2(dP6, K) through the normal sequence of the normalization) as something to prove or refute for all L and
  for a general torus fibration with a normal-crossings fibre.
- B.3 (necessary conditions for c3 > 0): add the question whether H^2(E, K_E) != 0 for the normalization E of some
  non-normal fibre is necessary.
- D (monodromy): Gamma is now explicit (index 12 in the vector stabilizer); it can be used in the corrected count of
  Lemma 4.2.

**S6_04_MAPS_MANIFOLDS.**
- Add the item of 3.4 (the class of the w-monodromy in Theta_7 = Z/28): it is a question of the same kind as Leads
  2-4 there, and the handle decomposition of B.5 is a second way to get a coboundary. If the push prompt for S6_02
  keeps it, cross-reference so that the two runs do not both spend their time on it.
- Lead 5 / D.1 (members with |p| > 1): the biholomorphic classification is B.2.1, invariants
  (|p|, e^(-pi i (c+k2))); the prompt should use it and ask only for the diffeomorphism types.
- B.4 (X_(3k,4l)): give B.3.1 (2kl classes) as input with its gap.
- New item: the real forms. For w in iR, X_c has an antiholomorphic involution (B.4.2); identify its fixed locus
  (by Smith theory a mod 2 homology 3-sphere) and its position relative to f (it fibres over the real points of P^1).
- Lead 1 (Seifert picture) can quote Aut = C^* exactly and the fixed double curve (C.4.1) as proved.

**S6_05_ARITHMETIC.** No change to its two problems. Optional addition, if wanted in that lane: the arithmetic of the
period functions at the CM points (N(i)^2 = 2, N(rho)^4 = 3, radii 6^3 and 48^(3/2), the unit 5 + 2 sqrt6, the
relation (27/64)): prove them and say whether D_part at every CM point of the base is (6/pi) log of an algebraic
number.

**S6_01_INVARIANTS (returned, not yet reviewed here).** Its Part D (h^1, h^2 of T_X, Kuranishi) and Part A.2 (the
scalar mu'(z2)) overlap A.5.2 and finding F9; the review of S6_01 should compare the two returns on both points.

## 5. For the push prompt on S6_02

Items to carry: C.3 (Targets A, B, C), E.1 (target (a) or (b), Routes 1-2), E.2 (targets (i)-(iv)), E.2.2 (the
element of Z/28), and the open ends of 3.5. Inputs to state as proved-and-checked-once, with their statements in
full: section 4 of `REVIEW.md`. Leads to state as unverified: every "mine" above. Literature to attach:
arXiv:2610.00250v1 and v2; Oguiso-Shioda; Eells-Kuiper; Kervaire-Milnor; a reference for multi-parameter Mumford
degenerations.

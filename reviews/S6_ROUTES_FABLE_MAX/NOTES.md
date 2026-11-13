# S6_ROUTES_FABLE_MAX: reading notes

Claude Fable 5.2 (Anthropic), effort max, no sub-agents. Started 13 November 2026, 00:43 (machine clock, WEST).
Kept for the later S6 synthesis. Everything marked "hunch" is unverified.

## Read so far (in order)

1. `reviews/S6_02_REVIEW_FABLE/REVIEW.md` (full). Key data for the three questions:
   - Family X_c, Pi_c = [[6 mu, tau, 1, 0], [beta^part + c, mu, 0, 1]]; exists iff Im c < -M, M = max D_part = -(3/pi) log 6, only at t = 1.
   - beta^part = (6i/pi) Log(theta1(mu,tau)/(2 sqrt3 eta(tau))); D_part = (6/pi) log(N/(2 sqrt3)); N = e^{-pi (Im mu)^2/Im tau} |theta1(mu,tau)/eta(tau)|.
   - C.2.3: N <= sqrt2 at every zero of wp_tau, equality exactly on orbit of i. Proof: cusp bound (Im tau >= 2; cusp bound 1.0814 < sqrt2), local argument |tau - i| <= 1.5e-4, 19,701 interval boxes.
   - Local: D_part = M - (2/pi)|tau - i| + O(|tau-i|^2): NOT smooth at i (a cone point: |tau - i| not |tau-i|^2). Reason: mu - (1-tau)/2 ~ sqrt(tau - i).
   - h^q(X_c, T) = (1,1,1,0); every small deformation of X_c is an X_c' (so a = 1 on a neighbourhood).
   - 4.9 closed forms: N(z1) = 3^{1/4}, N(z2) = 2^{1/2}; q(Alb S2) = i w/216, q(Alb S1) = -w^2/48^3.
2. `IMPLICATIONS.md` (full). 3.5: "a proof of N <= sqrt2 without a computer: N^2 is, up to the Gaussian, |theta3(h,tau)|^2/|eta(tau)|^2 at the zero h of wp near the half period; a subharmonicity or modular argument might replace 19,701 boxes."
3. `S6_05_ARITHMETIC/PROMPT.md` (full). Lead 10: N(v,tau) = |g_a(tau)| Siegel function; -log N = archimedean Neron local height lambda_infty(P); R4 says lambda_infty(P_t) >= -(1/2) log 2. Torsion values N^12 = 64 (t=1), 27 (t=0), 10 (t=32/5), 17 +- 10 sqrt3 (order six). Lead 11: CM and torsion only at t = 0, 1. C.5 closes with: "Whether N is algebraic at the CM points of the smooth base ... is a question about the transcendence of a local height; it is not an item of this prompt."
4. `S6_03_CDP/PROMPT.md` (full). E.3 closes with: "Whether a complex structure with a = 0 exists on S^6 outside these families is not an item of this prompt." Lead 7: b2 = 0 + fibration with Kahler general fibre => a = 1. Lead 4: chi(Y, T_Y (x) L) = 1 - b3/2.

(continued below as reading proceeds)

5. Survey FINDINGS.md (full): F19 (det of dZ/dz vanishes to order 2 at the order-three point), F18 (a = 1 from b2 = 0),
   F8, F16 (which a occur on S^6: open), F30 (other elliptic surfaces).
6. CD.tex C.1-C.2 (l. 1-480), D.1.1-D.1.3 (l. 690-862), CD_report.md. Proof structure of C.2.3: cusp bound for T >= 2
   (|Im v| < 0.43, N < 1.082); local Cauchy-Rouche on |tau - i| <= 1.5e-4 with h = v - (1-tau)/2,
   log N = Re H - pi (Im h)^2/T, H = log(theta3(h,tau)/eta), H_(h^2) = -pi/2, G = wp at half period + h, G_x = i d,
   G_(h^2) = -g2(i)/4; 19,701 boxes on [0,1/2] + i[17/20, 2].
7. Engel S6.tex: Section 2 to Def. 2.3 (surface, P, M = O(P-O), Lemma: Hom(t_6P^* M, M) = pi^* O(1), linearization phi
   with a simple zero at infinity); Section 8 (Remarks: family over u, Conjecture 8.2, S^6 -> S^3, Klingler, the general
   construction with any elliptic surface, line bundle and translation).
8. Viaclovsky 2610.10451 Section 10 (text file l. 2073-2110): Question (1) "Does every sufficiently small deformation of
   X_m retain a holomorphic torus fibration over P^1?"; R^1 f_* O = O(a_m) + O(b_m), a_m + b_m = 2m - 1 (Question (4)).

## Derivations made in this session (all unverified; numerics in checks/)

- N = |Siegel function g_a| = exp(-Neron function) = exp(Arakelov-Green g(z,0)); mean of log N over E is 0.
- Klein form k = N/|Delta|^(1/12); wp(z) - wp(w) = -sigma(z+w)sigma(z-w)/(sigma(z)^2 sigma(w)^2) gives
  |wp(z) - wp(w)| = |Delta|^(1/6) N(z+w)N(z-w)/(N(z)^2 N(w)^2); wp' = -sigma(2z)/sigma(z)^4 gives
  N(z)^4 = |Delta|^(1/4) N(2z)/|wp'(z)|. At wp(v) = 0: wp'(v)^2 = -g3, so N(v)^4 = 6 sqrt6 |eta|^6 N(2v)/|E6|^(1/2)
  = 6 sqrt6 N(2v)/|j - 1728|^(1/4) = 3^(3/4) N(2P)/|t-1|^(1/4). Checked (r1, part 1).
- x(2P) = 9 t^2/16 on the Q(t) model. psi_2(P) = t^2(t-1), psi_4, psi_6 as in S6_05 R1.
- Half periods: N(w_i)^4 = |Delta|^(1/3)/|(e_i-e_j)(e_i-e_k)|, product of the three N(w_i) = 2. So R4 reads
  N(v)^2 <= N(w_1)N(w_2)N(w_3). In potential form on the x-line: p(x) = integral log|x - s| dnu(s), nu = Haar pushforward
  proportional to dA/|4x^3 - g2 x - g3|; 2 log N(Q) = (1/6)log|Delta| - p(x(Q)); R4 is
  p(0) >= (1/3)(p(e1)+p(e2)+p(e3)) - (1/3) log 2 (0 is the centroid of the e_i).
- N(v+w_k) = N(v) (|e_k|^2/|(e_k-e_i)(e_k-e_j)|)^(1/4); N(2v) = N(v) N(v+w_1)N(v+w_2)N(v+w_3).
- Landen: N_tau(z) N_tau(z+1/2) = N_(2tau)(2z).
- Lattes: L(t) = (1/12)log|Delta| + (1/2)(potential of the measure of maximal entropy of the Lattes map of E_t at x = 0).
- Complex beta: integral |xi|^(2a-2)|1-xi|^(2b-2) dA = pi Gamma(a)Gamma(b)Gamma(c)/(Gamma(1-a)Gamma(1-b)Gamma(1-c)), a+b+c = 1.
  Lemniscatic: a = 1/4, b = 1/2 + s/2; equianharmonic: a = 1/6. psi(1/2) = -gamma - 2 log 2; psi(1/4)+psi(3/4) = -2gamma - 6 log 2;
  psi(1/3)+psi(2/3) = -2gamma - 3 log 3.
- Heat equation: with F = theta1/eta, d/dtau log F at fixed z = (1/(4 pi i))((F'/F)^2 - wp(z)). On wp = 0:
  d beta/d tau = (6i/pi)(Z v' + Z^2/(4 pi i)). Hence I5 and I6 (checked, r2).
- d^2/dz^2 of N^2 = N^2 (W^2 - wp(z) - (pi^2/3) E2^*(tau)), E2^* = E2 - 3/(pi T); E2^*(i) = 0.
- Period point Omega = [[tau, mu],[mu, beta/6]]; exp(2 pi i beta) theta1(mu,tau)^12/eta(tau)^12 = 12^6: the period curve lies
  in a level set of a Fourier-Jacobi term of index 6; D = 6 det(Im Omega)/Im tau. Gamma\O_+ = punctured unit disc bundle
  over the universal elliptic curve (coordinates tau, mu, xi = exp(-2 pi i beta)).
- Base orbifold is (3,4,infinity): v is two-valued on the tau-plane, branched over the orbit of i (double zero of wp).
  Delta(3,4,infinity) is not in Takeuchi's list of arithmetic triangle groups (from memory).
- Q1 first-order computation: H^1(X, f^*T_B) = H^1(B,T_B) + H^0(B, T_B (x) R^1 f_* O); image of H^1(T_X) lies in
  ker(delta), delta(alpha) = kappa cup alpha in Lambda^2 V (x) Lie; injective iff rank kappa = 2. K3 check: R^2 = 0,
  H^0(O(2) (x) O(-2)) = C, the one non-elliptic direction. For X_c: T_B(-log) (x) R^1 = O(-5) (x) (O + O(-1)) on P(3,4):
  no sections anyway.
- Q2: Lambda_1 = 2 log sigma(u) - u zeta(u) is a third-kind period mod (Q-bar u + log Q-bar^*);
  zeta(u) omega_1 - eta_1 u = omega_1 W - 2 pi i a (Legendre). CM: eta(u) = s_2 u + (pi/A) conj(u), s_2 algebraic.
  N(alpha P) = N(P)^(N alpha) x algebraic; the pairing N(P+Q)/(N(P)N(Q)) at Q = alpha P is N(P)^(Tr alpha) x algebraic
  (trace zero: algebraic for trivial reasons; this is the Ribet-point phenomenon).
- Real segment t > 1: tau = iT, v = 1/2 - i y(T), b = 1/2, P on the bounded real component, 2P on the identity component.

## Not done / to pick up at the synthesis

- No proof written for I1-I6. No paper outside the S6 folders opened; six arXiv ids verified by title only.
- Route 1.1: the passage from first order to all orders (Horikawa), and the logarithmic version at W and at the
  multiple fibres. The rank hypothesis for combs was not checked in Viaclovsky's paper.
- Route 2.2: the table at the eleven rational CM points was not computed (no PARI on this machine: cypari2, gp absent).
- Route 3.1: E_k for k >= 3 not computed; no explicit hand bound for sup_z N beyond the Gaussian-sum bound.
- Did not read S6_02_PUSH or S6_04 prompts, [AC26], S6_01 return, 2610.00250.
- Files: ROUTES.md, NOTES.md, checks/r1_identities.py(.out), checks/r2_derivatives.py(.out), lit/arxiv_ids_verified.txt,
  lit/arxiv_api_ids.xml.

Notes closed 13 November 2026, 01:37 WEST.

## Second step, 13 November 2026, 01:58 WEST: items inserted into the prompts (coordinator's instruction)

- Backups: s6_pro_prompts_20261112_work/S6_03_CDP_PROMPT_before_routes_20261113.md and
  S6_05_ARITHMETIC_PROMPT_before_routes_20261113.md (byte-identical to the prompts before editing).
- S6_03_CDP/PROMPT.md: header note; Lead 9 (stability of the torus fibration) and its line in the Leads preamble; item E.4
  after E.3; the user's "Typesetting check" paragraph before "Checkpoints". Notation there: g: Y -> C.
- S6_05_ARITHMETIC/PROMPT.md: header note; one sentence in problem III; Leads preamble; Lead 7 (two derivations to check);
  new Leads 13 (division formulas), 14 (Mahler measure), 15 (Gaussian sum, potential, gradient), 16 (heights, L-values,
  periods); C.4 (the torsion formula as a step to check); C.5 closing sentence now points to C.7; items in the order
  C.6, C.8, C.7 (C.7 last: (a) leads, (b) conditional theorem with proof, (c) unconditional, decided only by proof);
  material bullet naming s6_routes_checks/ and four arXiv sources; "Typesetting check" before "Checkpoints".
- Lint (push_rule_pro_prompts.py --lint-math): both pass, before and after.
- Formulas added during insertion, beyond ROUTES.md: N(P)^9 = 16 N(3P)|t|^(-2/3); N^12 = 27/|t-1| where 2P = -P and
  64/|t| where 3P = +-P; general m = +-1 mod n form; E_2 = 27^(5/4)/(8|5t-32|); the real-t formula with theta1(x, i/T).
  Tested in checks/r3_inserted_leads.py (ratios 1 to 15 digits; N^12 = 10 at t = 32/5).
- Zip of S6_05 does not yet hold what the prompt now names: s6_routes_checks/ (r1, r2 with outputs) and the TeX sources
  of arXiv:1701.07947, 1909.01253, 2010.15170, 1805.10104 at the paths written in the prompt. S6_03 needs nothing new.
- ROUTES.md itself must not go into a zip: it says which form of C.7 I expect to be reachable.

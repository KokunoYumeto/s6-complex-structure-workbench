# S6: routes for three questions that had no named route

Claude Fable 5.2 (Anthropic), effort max, no sub-agents. 13 November 2026, 00:43-01:40 (machine clock, WEST).

**Status of everything below: my hunch, unverified.** Nothing here is proved. Where a formula was tested numerically the
test is named (`checks/r1_identities.py`, `checks/r2_derivatives.py`, outputs beside them); a numerical test supports a
formula and does not prove it. Derivations were done once, by me, in this session; no second reader. Literature is named
from memory unless marked "id verified" (arXiv identifier and title confirmed through the arXiv API, list in
`lit/arxiv_ids_verified.txt`); no paper outside the S6 folders was opened.

What was read: `REVIEW.md`, `IMPLICATIONS.md` (S6_02 review); the prompts S6_05 and S6_03; the survey `FINDINGS.md`;
`CD.tex` C.1-C.2 and D.1.1-D.1.3 with `CD_report.md`; Engel's TeX, Section 2 (to Definition 2.3) and Section 8;
Viaclovsky arXiv:2610.10451, Section 10 (text file).

Notation as in the S6 prompts: tau the period ratio, j(tau) = 1728 t; v = mu the zero of wp_tau (the elliptic logarithm of
P); N(z,tau) = exp(-pi (Im z)^2/Im tau) |theta1(z,tau)/eta(tau)|; L(t) = log N(P_t); a = Im v/Im tau, b the Betti
coordinates (v = a tau + b); Z = (d/dz) log theta1 at z = v; W = Z + 2 pi i a; R = dv/dtau - a.
On the model Y^2 = X^3 + A X + B, A = -(3/4) t^3 (t-1), B = (1/4) t^4 (t-1)^2, P = (0, t^2(t-1)/2), the discriminant is
Delta_E = -16(4A^3 + 27B^2) = 27 t^8 (t-1)^3.

## 0. Six facts the routes rest on (all mine; each tested numerically; proofs to be written)

**I1 (division formula).** For every n >= 2 and every t on the smooth base with nP_t != O:
N(P)^(n^2) = N(nP) |Delta_E|^((n^2-1)/12) / |psi_n(P)|, psi_n the division polynomial of the model. For n = 2:
**N(P)^4 = 3^(3/4) N(2P) |t-1|^(-1/4)**. It is the duplication formula of the Néron local height
(lambda(2Q) = 4 lambda(Q) - log|2y| + (1/4) log|Delta|), read for N = exp(-lambda). Test: four values of tau, ratio 1 to 15
digits.
- Consequence 1: where P has exact order n, take m = n+1 (so mP = P): **N(P)^12 = |Delta_E| / |psi_(n+1)(P)|^(12/(n^2+2n))**.
  This is the explicit algebraic function asked for in S6_05 C.4. At t = 0 (order 3 on the smooth model, 2P = -P) the n = 2
  formula gives N^3 = 3^(3/4), so N^4 = 3: Lead 7 of S6_05 in one line. At t = 32/5 two duplications give
  N^16 = 40 (5/32)^(1/3) = 10^(4/3), so N^12 = 10.
- Consequence 2: (1/n^2) log(...) of the right side converges to L(t): the torsion values of P equidistribute to the measure
  of I4.

**I2 (N at the zero of wp is an elliptic Mahler measure).** For every lattice, with v a zero of wp and dmu the Haar
probability measure of E: **6 log N(v) = integral over E of log|wp'^2/wp^3| dmu**, equivalently
N(v)^2 = |Delta|^(1/6) / exp(integral of log|wp| dmu), equivalently N(v)^2 = 12 / exp(integral of log ||phi_(0,1)|| dmu) with
phi_(0,1) the weak Jacobi form of weight 0 and index 1 (half the elliptic genus of a K3 surface, whose zeros in z are
the zeros of wp) and || || its Petersson norm. Proof sketch: wp = -sigma(z+v) sigma(z-v)/(sigma(z)^2 sigma(v)^2), log N has
mean zero on E, compare the behaviour at z = 0. Test: grid integral at two values of tau, agreement to 7 digits.
- In the coordinate u = 1/x: with C(u) = (1 - e1 u)(1 - e2 u)(1 - e3 u) = 1 - (g2/4) u^2 - (g3/4) u^3 and the probability
  measure nu proportional to dA(u)/(|u| |C(u)|) on the plane, **N(v)^6 = 4 exp( integral of log|C(u)| dnu )**.
  So R4 (N <= sqrt2) is the statement: **the nu-average of log|C| is at most log 2, with equality exactly when g3 = 0.**
- g3 = 0: with xi = (g2/4) u^2 the average is that of log|1 - xi| for the weight |xi|^(-3/2) |1 - xi|^(-1), a complex beta
  integral; its value is (1/2)(2 psi(1/2) - psi(1/4) - psi(3/4)) = log 2. g2 = 0: weight |xi|^(-5/3) |1 - xi|^(-1), value
  (1/2)(2 psi(1/2) - psi(1/3) - psi(2/3)) = (3/2) log 3 - 2 log 2, so N^6 = 3^(3/2). Both closed forms of the review
  (N(z2)^2 = 2, N(z1)^4 = 3) are digamma identities. Done by hand here; to be written as proofs.

**I3 (Gaussian sum).** For all z, tau, with T = Im tau and Lambda = Z + tau Z:
**N(z)^2 sqrt(2T) |eta(tau)|^2 = sum over m in (1/2)Lambda of eps(m) exp(-2 pi |z - m|^2 / T)**, eps = -1 on Lambda and
+1 on the three other classes. (Poisson summation of |theta1|^2.) Test: three points, ratio 1 to 15 digits.

**I4 (L is a logarithmic potential).** On the t-sphere, in the sense of currents, dd^c L = (1/12) delta_infinity - m_P,
where m_P is the pull-back by P of the Betti form (da wedge db), a positive measure of total mass 1/12 = (1/2) <P,P>.
So L(t) = const + integral of log(1/|t - s|) dm_P(s): **L is the logarithmic potential of the Betti measure of P**, and
R4 says this potential is largest at t = 1. L is superharmonic on the smooth base. Equivalent reading: N^12/12^6 is the
norm of Engel's linearization phi (a section of O(1) vanishing at infinity) in the metric on O(1) whose curvature is
12 m_P. Near t = 1 the density of m_P is of order |t-1|^(-3/2) (integrable); by the mu_3 symmetry L has a second local
maximum at t = 0 (value (1/4) log 3), or a degenerate critical point there.

**I5 (the gradient).** dL/dtau = (W/(8 pi i)) (W + 4 pi i R). Test: finite differences, 12 digits. The critical points of
L are the points with W = 0 (the zero of wp is a critical point of the Green function of its curve: Lin-Wang) or
W = -4 pi i R.

**I6 (the Kodaira-Spencer determinant is a square).** With Omega = [[tau, mu],[mu, beta/6]]:
det(dOmega/dtau) = (W + 2 pi i R)^2/(4 pi^2) = -(dmu/dtau - (i/2 pi) Z)^2. Test: finite differences, 12 digits. It agrees
with survey F19 (the determinant vanishes to order 2 at the order-three point).

---

## 1. A complex structure on S^6 with algebraic dimension 0

What any such structure X must satisfy (short arguments, mine): no non-constant holomorphic map to a curve; h^(3,0) = 0
and h^(0,1) = 1 + h^(0,2) >= 1 (Gray), so Pic(X) = H^1(X, O) is a non-zero vector space containing K_X != 0; c3 = 2, so
every holomorphic vector field has zeros and no construction with a locally free circle action (LVM, moment-angle,
Calabi-Eckmann type) can give S^6; for a holomorphic map onto a surface B with general fibre of genus g, Leray gives
b1(B) = 0 and b2(B) <= 2g.

### Route 1.1. Small deformations of the known families. Checked to first order: closed, with the reason

Reason to try: non-elliptic K3 surfaces are deformations of elliptic ones; Viaclovsky's combs X_m have large Kuranishi
dimension and R^1 f_* O = O(a_m) + O(b_m), a_m + b_m = 2m - 1, so h^(0,1) is large; his Question (1) asks "Does every
sufficiently small deformation of X_m retain a holomorphic torus fibration over P^1?"

What I found: for a torus fibration f: X -> B over a curve, the obstruction to keeping f along theta in H^1(X, T_X) is
f_* theta in H^1(X, f^* T_B) = H^1(B, T_B) + H^0(B, T_B tensor R^1 f_* O). The second summand receives H^0(B, R^1 f_* T_X),
and its image lies in the kernel of the connecting map delta: T_B tensor R^1 f_* O -> R^2 f_* T_(X/B). On a smooth fibre F
delta sends d/dt tensor alpha to kappa(d/dt) cup alpha in H^2(F, T_F) = Lambda^2 H^1(O_F) tensor Lie(F); for a 2-torus this
is injective in alpha exactly when the 2x2 matrix kappa = dOmega/dt has rank 2. Both sheaves are locally free of rank 2,
so a generically injective delta is injective on sections. Hence: **if the Kodaira-Spencer matrix has rank 2 at one point
and B = P^1, then f_* theta = 0 for every theta: every first-order deformation keeps the fibration.** For elliptic
fibrations R^2 = 0 and the obstruction is absent, which is the K3 case; so the test separates the two situations
correctly. For X_c the rank is 2 away from the order-three point (I6, F19), consistent with R1. For every family of
Engel's type I6 shows det kappa is the square of mu_tau - (i/2 pi) Z, which is not identically zero for an algebraic
section (unverified).

So this route does not lead to a = 0: with the first-order statement promoted to all orders, a = 1 holds on a
neighbourhood of every known family, combs included. Why the promotion might fail: Horikawa's theory of deformations
of holomorphic maps needs a statement at the level of obstructions, not only tangent vectors; the special fibres need
the logarithmic version. It is concrete enough for a prompt item, and it would answer the second half of Viaclovsky's
Question (1).

**Prompt item (for S6_03, Part E, after E.3).**
> E.4. Stability of the torus fibration. Let f: X -> B be a proper surjective holomorphic map from a compact complex
> threefold onto a compact Riemann surface with connected fibres, general fibre a complex 2-torus, and Kodaira-Spencer
> matrix kappa = dOmega/dt (the derivative of the period matrix of the fibres) of rank 2 at some point of B. Prove or
> refute: (i) the connecting map T_B tensor R^1 f_* O_X -> R^2 f_* T_(X/B) is injective as a map of sheaves, and for
> B = P^1 every class theta in H^1(X, T_X) has f_* theta = 0 in H^1(X, f^* T_B); (ii) for every deformation of X over a
> germ (S, 0) the map f extends to a holomorphic map to B x S, after shrinking S; (iii) if moreover b_2(X) = 0, every
> sufficiently small deformation of X has algebraic dimension 1. Then apply it: verify the rank hypothesis for X_c, for
> the members with |p| > 1, for X_(3k,4l), for the two-parameter family of arXiv:2609.33785, for the combs X_m of
> arXiv:2610.10451 and for the family of arXiv:2609.33826, and state the answer to Question (1) of arXiv:2610.10451,
> Section 10 ("Does every sufficiently small deformation of X_m retain a holomorphic torus fibration over P^1?").
> Leads (unverified): on a smooth fibre the connecting map is alpha -> kappa cup alpha, injective exactly when kappa has
> rank 2; for families of Engel's type det(dOmega/dtau) = -(dmu/dtau - (i/2 pi)(theta1'/theta1)(mu, tau))^2; for an
> elliptic fibration R^2 = 0 and the statement is false (elliptic K3 surfaces). Done: each of (i)-(iii) proved or
> refuted with the hypotheses that make it true; the hypothesis verified or refuted for each family named, with the
> special fibres (multiple fibres, the fibre W) treated; if (ii) is false, the counterexample deformation and its
> algebraic dimension.

### Route 1.2. Torus fibrations whose period curve is a null curve (Kodaira-Spencer rank 1), then deform

Reason: Route 1.1 leaves exactly this door. If det kappa is identically 0 with kappa != 0, delta has a line of kernels
K inside T_B tensor R^1 f_* O, and sections of K are first-order deformations along which t stops being holomorphic, as
for an elliptic K3 surface. The period domain is an open orbit in the 3-dimensional quadric LG(2,4) with its conformal
structure "det"; the condition is that the period curve is a null curve.
First step: decide whether a null period curve can carry monodromy that gives S^6 (invariants Z, coinvariants Z, the
conditions of [AC26] Theorem 7.17). By I6 a family of Engel's type is null exactly when the section is a leaf of the
holomorphic foliation dz/dtau = (i/2 pi)(theta1'/theta1)(z, tau) on the universal elliptic curve. So the first question
is whether that foliation has an algebraic leaf (a section, or a multisection, of some elliptic surface).
Computation: integrate the leaf through a few torsion points numerically and test for algebraicity of the relation
between wp(z) and j; search the Oguiso-Shioda list for sections on which mu_tau - (i/2 pi) Z vanishes identically.
Why it might fail: the foliation may have no algebraic leaf (I expect none: it is a Painlevé-type transcendental flow);
with rank 1 and constant kernel direction the family splits off a fixed elliptic curve and the total space is not S^6.

### Route 1.3. A construction without a base curve (hyperbolic in place of unipotent gluing)

Reason: every known example is a Mumford-type filling of a quotient with unipotent (parabolic) boundary monodromy; the
analogous surfaces are elliptic. Compact surfaces with a = 0 and a cycle of rational curves (Inoue-Hirzebruch) come from
hyperbolic gluing data. Their threefold analogues exist (Sankaran's analogues of Inoue-Hirzebruch surfaces; toric Kato
manifolds, arXiv:2010.14854, id verified), have a = 0 in many cases, and are not simply connected.
First step: list which infinite periodic fans in R^3 with a group acting cocompactly on the fan give a compact threefold
with pi_1 = 0 and Euler number 2 after quotient and after allowing finite-order (orbifold) elements, as the (3,4)
multiple fibres do for X_c. Computation: Engel's Threefold Explorer style van Kampen and Mayer-Vietoris on such data.
Why it might fail: b_2 of such quotients equals the number of orbits of rays minus relations and is positive in every
example I know; killing it needs a mechanism like the multiple fibres. Not concrete enough for a prompt item.

### Route 1.4. Through the threefold of the Klingler answer

The S6_02 return shows Gamma acts properly on O_+ = {D < 0}. In coordinates (tau, mu, beta), xi = exp(-2 pi i beta):
Gamma\O_+ is the punctured unit disc bundle {0 < ||xi|| < 1} of a line bundle of index 6 over the universal elliptic
curve, with its Néron metric, and X_c is the tautological torus family over one curve in it. I looked for a compact
threefold made from this bundle itself (quotient of the C^*-bundle by xi -> lambda xi): it is a family of primary Kodaira
surfaces over the modular curve and maps onto the elliptic modular surface, so its algebraic dimension is at least 2.
That particular object does not give a = 0. The space Gamma\O_+ is the natural place to look for period curves that
are not tautological sections (Route 1.2 lives here).

**Verdict for question 1.** Best route: 1.2, but its first step is a question whose answer I expect to be negative, and
1.3 is not concrete. The one concrete, decidable statement is the stability theorem of Route 1.1; it says where an
a = 0 structure cannot be. The main question stays without a constructive route that I can name with confidence.

---

## 2. Is N algebraic at CM points where P is not torsion?

By Lead 11 of S6_05, P is torsion at no CM point of the smooth base, so the question is about every CM point other than
t = 0, 1; CM plays no role in the expected answer (transcendental at every algebraic t0 with P_(t0) not torsion).
The eleven rational CM points of the smooth base are t0 = j/1728 for j = 8000, 54000, 287496, 16581375, -3375, -32768,
-884736, -12288000, -884736000, -147197952000, -262537412640768000 (t0 = 125/27, 125/4, 1331/8, 614125/64, -125/64,
-512/27, -512, -64000/9, -512000, -85184000, -151931373056000). For t0 > 1 the point P lies on the bounded real component
and b = 1/2, so 2P is a real point with a = 0 for the lattice Z + (i/T)Z: there
N(P)^4 = 3^(3/4) (t0-1)^(-1/4) theta1(x, i/T)/eta(i/T) with x real, no Gaussian factor.

### Route 2.1. N as an exponential of periods of a 1-motive; transcendence from the period conjecture

Reason: with u the elliptic logarithm of P and Lambda_1 = 2 log sigma(u) - u zeta(u) (an integral of a differential of
the third kind between algebraic points, up to Q-bar u + log Q-bar^*): 2 log N(P) = (1/6) log|Delta| + Re(Lambda_1 + u W),
W = zeta(u) - eta(u) with eta extended real-linearly. So N(P)^2 is, up to an algebraic factor, the canonical norm of an
algebraic point of the extension G_P of E by G_m lying over P, and "N(P) algebraic" says: the fibre of G_P over P contains
an algebraic point of the maximal compact subgroup of G_P(C). It is a quadratic relation between 1-periods and their
complex conjugates. Linear relations are settled (Wüstholz; Huber-Wüstholz, arXiv:1805.10104, id verified); quadratic
ones are not. Grothendieck's period conjecture for the 1-motive [Z -> G_P] predicts that omega, pi, u, zeta(u), Lambda_1
are algebraically independent in the CM case (dimension of the Mumford-Tate group 2 + 2 + 1; Bertolin's formula; the
lift is not deficient in the sense of Jacquinot-Ribet because P = alpha P has no antisymmetric solution alpha), and then
N(P) is transcendental. The "semi-elliptic conjecture" and the sigma-conjecture of Bertolin, Philippon, Saha and Saha
(arXiv:2010.15170, id verified, not opened) are stated for this purpose.
First step: write the real case (t0 > 1 rational CM): N(P)^4 = algebraic x theta1(x, i/T)/eta(i/T), and
2 log(theta-value) = Lambda_1 + u(zeta(u) - (eta_1/omega_1) u), all terms real; derive the transcendence from the
conjecture with the exact list of periods.
Computation: none needed for the conditional theorem; PSLQ on log N(t0) against log 2, log 3, log of the primes of bad
reduction, pi, and the Chowla-Selberg period, at 200 digits, at the eleven points (a negative search is evidence only).
Why it might fail: it is conditional. For non-real t0 the conjugate motive enters and the dimension count needs the
K-span of P and of the image of its conjugate.

### Route 2.2. The global height: N(P_t0) = A(t0) exp(-h(P_t0))

Reason: -log N is the archimedean Néron function in the normalization that sums to the canonical height. For t0 in Q the
curve and the point are defined over Q, so **log N(P_t0) = sum over primes of lambda_p(P_t0) - h(P_t0)**, the sum being
a rational combination of logarithms of primes (bad reduction and denominators). So N(P_t0) is algebraic exactly when
exp(h(P_t0)) is. At t0 = 32/5 (order 4) this reads N = A = 10^(1/12). For a number field take the product over the
archimedean places. For the eleven rational CM curves, if the analytic rank is 1, Gross-Zagier, Kolyvagin and Rubin give
h(P_t0) = r L'(E_t0, 1)/Omega with r rational, so **D_part(t0) = (6/pi)(log(A/(2 sqrt3)) - r L'(E,1)/Omega)**: the period
function of the S^6 family at a rational CM point is an explicit logarithm minus a rational multiple of a central
L-derivative. The inequality R4 becomes h(P_t0) >= sum_p lambda_p(P_t0) - (1/2) log 2 for every rational t0.
First step: at the eleven points compute the minimal model, the local heights, h(P) and the rank (PARI: ellheight,
ellanalyticrank, elllocalred), and compare A exp(-h) with N from theta functions to 50 digits.
Why it might fail as a route to a decision: it converts the question into the transcendence of exp(L'(E,1)/Omega), which
no known method reaches. As an identity it should hold and is new information about D_part.

### Route 2.3. An unconditional proof by the Schneider-Lang method. Checked: the counting does not close

In the CM case theta(z) = sigma(z) exp(-s_2 z^2/2) (s_2 algebraic) satisfies theta(alpha z) = theta(z)^(N alpha) x
algebraic function, so if theta(u) were algebraic, wp and theta would take algebraic values on the rank-2 group O_K u.
Schneider's method for two functions of order 2 needs rank greater than 4; the derivative version needs zeta(u) - s_2 u
algebraic, which is false (Schneider). And the archimedean N contains the non-holomorphic factor exp(-pi |u|^2/(2A)); in
the real case it is the value of theta1(z, tau) itself, whose logarithmic derivative brings in eta_1/omega_1, which is
transcendental. The p-adic analogue is a theorem (Bertrand, 1981: the p-adic height of a non-torsion point of a CM curve
is not zero, by this method, where the growth conditions are milder). I see no way to close the archimedean count.

**Prompt items (for S6_05, Part C, after C.5).**
> C.6. The global formula. For t0 in a number field K, t0 not 0 or 1, prove or refute:
> sum over the embeddings sigma of K in C of log N(P_(sigma t0)) = sum over the finite places v of K of n_v lambda_v(P_t0)
> - [K:Q] h(P_t0), with lambda_v the Néron local heights in the normalization independent of the model and h the canonical
> height relative to (O). Compute both sides to 50 digits at t0 = 32/5, at the two order-six points, and at the eleven
> rational CM points of the smooth base (j = 8000, 54000, 287496, 16581375, -3375, -32768, -884736, -12288000,
> -884736000, -147197952000, -262537412640768000), with the minimal model, the reduction type, the component met by P and
> lambda_p at every bad prime, the rank of E_t0(Q), the index of Z P_t0, and L'(E_t0, 1)/Omega; state D_part(t0) at each
> point in the form (6/pi)(log(A/(2 sqrt3)) - h(P_t0)) with A explicit, and prove the relation of h(P_t0) to L'(E_t0, 1)
> that the theorems of Gross-Zagier, Kolyvagin and Rubin give for these curves, with their hypotheses checked.
> Done: the identity proved or refuted; the table complete; every numerical agreement to 50 digits shown.
>
> C.7. Transcendence. Decide, for every algebraic t0 on the smooth base at which P_t0 is not torsion (the CM points first),
> whether N(t0) is algebraic. Leads (unverified): 2 log N(P) = (1/6) log|Delta| + Re(Lambda_1 + u(zeta(u) - eta(u))),
> Lambda_1 = 2 log sigma(u) - u zeta(u) a period of the 1-motive [Z -> G_P], G_P the extension of E by G_m given by P;
> N(P) is algebraic exactly when the fibre of G_P over P contains an algebraic point of the maximal compact subgroup
> of G_P(C); by C.6, for t0 in Q, exactly when exp(h(P_t0)) is algebraic; for real t0 > 1,
> N(P)^4 = 3^(3/4)(t0-1)^(-1/4) theta1(x, i/T)/eta(i/T) with x real; Grothendieck's period conjecture for [Z -> G_P]
> (dimension of the Mumford-Tate group as computed by Bertolin; arXiv:2010.15170 for the conjecture in the form with
> sigma) would give transcendence; the Schneider-Lang method with wp and sigma(z) exp(-s_2 z^2/2) on O_K u has rank 2
> where rank greater than 4 is needed. Prove each lead or refute it. Done: a proof that N(t0) is transcendental, or an
> algebraic value with its proof, for every such t0; a theorem conditional on a named conjecture is a step on the way
> and is stated as conditional, with the conjecture quoted exactly and the Mumford-Tate group computed.

C.6 is concrete and decidable. C.7 states the question itself; my hunch is that only its conditional form is within
reach, so whether to send it under the push rule is a decision for the main session.

---

## 3. A proof of N <= sqrt2 without the interval certificate

Three reformulations (Section 0): the potential of the Betti measure is largest at t = 1 (I4); the elliptic Mahler
measure of y^2/x^3 is at most 8 (I2); a signed Gaussian sum over the half-lattice, taken at the zero of wp, is at most
2 sqrt(2T)|eta|^2 (I3). In the coordinate eps with g2 = 4, g3 = 4 eps, t = 1/(1 - 27 eps^2/4): Phi(eps) = nu-average of
log|1 - u^2 - eps u^3| is superharmonic on the eps-plane away from eps = +-2/(3 sqrt3) (the cusp, where it is -infinity),
invariant under eps -> -eps and eps -> conj(eps), Phi(0) = log 2, Phi(infinity) = (3/2) log 3 - 2 log 2, and near 0
Phi = log 2 - c|eps| + ... (a cone point: this is the -(2/pi)|tau - i| of the review).

### Route 3.1. The duplication ladder: a finite number of algebraic steps and one local expansion

Reason: by I1, for n = 2^k, (N(P)/sqrt2)^(4^k) = E_k(t) N(2^k P) / |t-1|^(1/4) with E_k an explicit algebraic function
(E_1 = 3^(3/4)/4; E_2 = 27^(5/4) 32/(256 |5t - 32|); the limit of E_k at t = 1 is 2^(1-k) 3^(3/4)/4). Bounding N(2^k P) by
S(tau) = sup over z of N(z, tau) proves N(P) < sqrt2 outside a disc around t = 1 of radius about (27/64) 16^(1-k) (0.42,
0.026, 0.0016, ...), apart from neighbourhoods of the points where 2^k P = O, which the step k-1 covers. Each step
divides the radius by 16. A local expansion at t = 1 with an explicit radius then closes the proof. The return's local
radius (|tau - i| <= 1.5e-4) came from crude Cauchy bounds; with the exact structure
log N = Re log(theta3(h,tau)/eta) - pi (Im h)^2/T, h^2 = -e_2(tau)/Q(h,tau), a radius of order 0.05 in tau looks
reachable by hand, and then k = 2 or 3 is enough.
First step: prove I1 and an explicit bound for S(tau) on the fundamental domain. From I3,
S^2 <= (sum over Lambda of exp(-pi|w|^2/(2T)))/(sqrt(2T)|eta|^2); at tau = i this gives S < 1.554 (true value sqrt2).
A sharper hand bound: by I3 the supremum is over an explicit Gaussian sum.
Computation a model can do: the exact E_k for k <= 4 (division polynomials psi_2, psi_4, psi_8, psi_16 of P), the regions
each step covers, and the radius needed from the local step; a numerical map of where each inequality has slack.
Why it might fail: the regions near 2^k-torsion points and the growth of S toward the cusp need bookkeeping (the cusp
bound of C.2.3, 1.082, already covers Im tau >= 2); the result is a proof free of machine enumeration but with several
pages of explicit estimates, not a one-line argument. Concrete enough for a prompt item.

### Route 3.2. The integral inequality: average of log|1 - u^2 - eps u^3| <= log 2

Reason: I2 turns R4 into one inequality for a family of plane integrals, with the two symmetric cases given by digamma
identities. The integral Z(s, eps) = integral of |u|^(-1)|1 - u^2 - eps u^3|^(s-1) dA is a complex Selberg-type integral;
by the Kawai-Lewellen-Tye factorization it is a finite sum of c_k(s)|f_k(s, eps)|^2 with f_k hypergeometric-type series
in eps, and Phi = d/ds log Z at s = 0. The cone term |eps| comes from a factor with exponent 1/2.
First step: write the factorization at eps = 0 (it gives the beta integral) and the first variation in eps; prove
Phi(eps) < log 2 for small eps with an explicit radius; then monotonicity of Phi along rays from 0, or a majorant.
Computation: series of f_k to high order; numerical Phi on the eps-plane; test of radial monotonicity (it fails on the
imaginary axis beyond the saddle, since Phi rises again to its value at infinity, so the statement to prove is not
global radial monotonicity).
Why it might fail: no sign-definite expression for log 2 - Phi is in sight. Hölder convexity of log Z in s gives
Phi <= (1/s) log Z(s) for s > 0, which is strict at eps = 0 and so cannot give the sharp bound.

### Route 3.3. Critical points of L (Morse count on the sphere)

Reason: L is superharmonic on the smooth base, so its critical points there are maxima or saddles; L -> -infinity only at
t = infinity; t = 0 and t = 1 are cone-type local maxima. On the sphere, maxima minus saddles equals 1. If the only
critical point on the smooth base is one saddle on the segment 0 < t < 1, then L <= max(L(0), L(1)) = (1/2) log 2. By I5
the critical points are the solutions of W = 0 or W = -4 pi i R.
First step: locate all solutions numerically in the half fundamental domain (three boundary arcs carry a Neumann
condition by the symmetry tau -> -conj(tau)); then count them rigorously by a degree argument for the real-analytic map
tau -> W(W + 4 pi i R).
Why it might fail: W and R are not holomorphic in tau, so the count is a topological degree computation, which is again
a computation unless a structural reason is found (Lin-Wang and Chen-Kuo-Lin-Wang count zeros of the Hecke form
Z_(r,s)(tau) for fixed real (r,s); here (r,s) = (a,b) moves with tau).

### Route 3.4. A comparison function

Reason: if M is explicit, M - L is superharmonic on a region and M >= L on its boundary, then M >= L inside (minimum
principle). On the region, dd^c M must be at most -m_P, so one needs a lower bound for the Betti density
(1/T)|v' - a|^2 = |R|^2/T. R satisfies d R/d conj(tau) = conj(R)/(2 i T) and d R/d tau = v'' - R/(2 i T), with
v'' = 144 pi i sqrt6 Delta/E_6^(3/2) (Eichler-Zagier). First step: solve this first-order system for R in closed form
on the imaginary axis. I did not get further.

**Prompt item (for S6_02_PUSH, with the open ends of IMPLICATIONS 3.5; or S6_05 Part C).**
> C.8. R4 without the interval certificate. Prove N(v, tau) <= sqrt2 at every zero v of wp_tau, with equality exactly on
> the modular orbit of i, by an argument in which every inequality is an explicit estimate that a reader can verify
> with pencil-and-paper arithmetic: no interval enumeration, no grid, no box cover. Before that, prove or refute each of
> the following (leads, unverified, tested numerically in `s6_routes/checks/`):
> (a) N(P)^(n^2) = N(nP)|Delta_E|^((n^2-1)/12)/|psi_n(P)| for the model Y^2 = X^3 - (3/4)t^3(t-1)X + (1/4)t^4(t-1)^2,
> Delta_E = 27 t^8 (t-1)^3; in particular N(P)^4 = 3^(3/4) N(2P)|t-1|^(-1/4), and at a point of exact order n,
> N(P)^12 = |Delta_E|/|psi_(n+1)(P)|^(12/(n^2+2n)).
> (b) 6 log N(v) = integral over E of log|wp'^2/wp^3| dmu; N(v)^6 = 4 exp(nu-average of log|1 - (g2/4)u^2 - (g3/4)u^3|),
> nu proportional to dA(u)/(|u||1 - (g2/4)u^2 - (g3/4)u^3|); the values at g3 = 0 and g2 = 0 by complex beta integrals
> (digamma values at 1/2, 1/4, 3/4 and at 1/2, 1/3, 2/3).
> (c) N(z)^2 sqrt(2 Im tau)|eta(tau)|^2 = sum over m in (1/2)(Z + tau Z) of eps(m) exp(-2 pi|z - m|^2/Im tau), eps = -1 on
> the lattice and +1 off it.
> (d) dd^c L = (1/12) delta_infinity - m_P on the t-sphere, m_P the Betti measure of P, of total mass 1/12; L is its
> logarithmic potential; dL/dtau = (W/(8 pi i))(W + 4 pi i R).
> Routes: the duplication ladder (from (a): (N(P)/sqrt2)^(4^k) = E_k(t) N(2^k P)|t-1|^(-1/4), a bound for sup_z N from (c),
> and the local expansion at tau = i with an explicit radius); the integral inequality of (b); the classification of the
> critical points of L from (d). Done: (a)-(d) each proved or refuted; the theorem proved by such an argument, written
> so that the constants of every step are displayed; the certificate of S6_02 C.2.3 is not used anywhere in it.

**Verdict for question 3.** Best route: 3.1 (the ladder). It is concrete enough for a prompt item (drafted). Routes 3.2
and 3.3 are recorded as leads inside the same item. I1-I3 also prove the closed forms that the S6_05 prompt asks for.

---

## 4. By-products for the prompts already written

- S6_05 Lead 7 (N(z1)^4 = 3): one line from I1 with n = 2 at t = 0; also from I2 by a beta integral.
- S6_05 Lead 10 / C.4 (N^12 on the torsion locus): N^12 = |Delta_E|/|psi_(n+1)(P)|^(12/(n^2+2n)) at exact order n.
- S6_05 Lead 9 / C.3: by I4 and the mu_3 symmetry, D_part has a local maximum at t = 0 unless the Betti density vanishes
  there; R = 0 at tau = rho by the symmetry, so the second-order term has to be computed.
- S6_03 E.3 and Viaclovsky's Question (1): the stability statement of Route 1.1.
- The drafted items avoid the phrases the prompt lint bans; they were not run through
  `push_rule_pro_prompts.py` because the lint is for assembled prompts. Run it after insertion.

## 5. Literature named

Id verified (arXiv API, 13 Nov 2026; texts not opened): DeMarco and Mavraki, *Variation of canonical height and
equidistribution*, arXiv:1701.07947 (the function t -> lambda(P_t) and its measure: I4); Corvaja, Demeio, Masser and
Zannier, *On the torsion values for sections of an elliptic scheme*, arXiv:1909.01253 (Betti map; count of torsion
values); DeMarco, Wang and Ye, *Torsion points and the Lattès family*, arXiv:1311.1792; Huber and Wüstholz,
*Transcendence and linear relations of 1-periods*, arXiv:1805.10104; Bertolin, Philippon, Saha and Saha, *Semi-abelian
analogues of Schanuel Conjecture and applications*, arXiv:2010.15170; Istrati, Otiman, Pontecorvo and Ruggiero, *Toric
Kato manifolds*, arXiv:2010.14854.
From memory, not verified: Silverman, *Advanced Topics*, VI.3 and *Variation of the canonical height on elliptic
surfaces* I-III; Everest and ní Fhlathúin, *The elliptic Mahler measure* (1996); Lin and Wang, *Elliptic functions,
Green functions and the mean field equations on tori* (Annals 2010); Chen, Kuo, Lin and Wang, *Green function, Painlevé
VI equation and Eisenstein series of weight one*; Bertolin, *Périodes de 1-motifs et transcendance* (2002) and *Third
kind elliptic integrals and 1-motives*; Jacquinot and Ribet, *Deficient points on extensions of abelian varieties by
G_m* (1987); Bertrand, *Valeurs de fonctions thêta et hauteurs p-adiques* (1981); Waldschmidt, *Nombres transcendants
et groupes algébriques* (Astérisque 69-70) and *Elliptic functions and transcendence* (2008); Horikawa, *On deformations
of holomorphic maps* I-III; Gray, *A property of a hypothetical complex structure on the six sphere* (1997); Sankaran,
*Higher-dimensional analogues of Inoue-Hirzebruch surfaces* (1989); Eichler and Zagier (1982); Dotsenko and Fateev for
complex beta integrals. Every one of these must be opened before a statement is attributed to it.

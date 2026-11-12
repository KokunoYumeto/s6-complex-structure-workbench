# Actual weak-coupling vacuum, observable and spectral maps

8 September 2026. The finite open box and its physical spacing remain fixed
through Sections 1--6. We prove convergence of the actual vacuum and finite
spectral projections of the nonlinear Hamiltonian, and compute an exact
family of limiting observable spectral measures. Section 7 records what a
particular simultaneous low-energy diagonal actually does to those measures.
It does not identify that diagonal with interacting four-dimensional
Yang--Mills theory.

## 1. Original objects and the full-measure Hilbert map

Use the open box with vertices in \(\{-L,\ldots,L\}^3\), \(L\ge2\),
all its positive edges E and faces P, and physical spacing \(a>0\).
Put \(m=2L\), \(r=2m^3+3m^2\). The original operator is
\[
 H_g=\frac{2g^2}{a}\sum_{e\in E}E_e+
       \frac1{2g^2a}\sum_{p\in P}(2-\operatorname{tr}U_p),
 \qquad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,
 \quad T_\alpha=-i\sigma_\alpha/2.                       \tag{1}
\]
In particular \(\kappa=2g^2/a\), \(b=1/(2g^2a)\),
\(\xi=1/(4g^4)\), and the scalar \(2b|P|\) are unchanged.
The physical Hilbert space is the invariant subspace for all vertex gauge
transformations. Let \(\psi_g>0\) be the actual unit ground state and
\(\mathcal E_g\) its actual energy.

Here are the exact coordinate data used below. Root the fixed maximal tree
at \((-L,-L,-L)\), with parent obtained by decreasing the first coordinate
in the order 1,2,3 that exceeds \(-L\). If \(t_v\) is its ordered tree
holonomy, the chord variables are
\[
 Z_c=t_{s(c)}U_ct_{t(c)}^{-1},\qquad c\in\mathcal C.       \tag{2}
\]
The inverse retains the tree links and sets \(U_c=t_s^{-1}Z_ct_t\).
Independent Haar translations in each chord, followed by Fubini, prove
that this coordinate map preserves product Haar measure. Based gauge
averaging eliminates the tree variables exactly. The residual physical
condition on functions of Z is simultaneous conjugation of every Z_c by
one element of SU(2), not independent conjugation of each chord.

The full proof of the quotient form, boundary-sensitive frequencies and
finite-box eigenvalue convergence is in the companion manuscript
*The original finite-box SU(2) Hamiltonian at small positive coupling*.
We retain its exact maps, not merely its spectral conclusion. For real
edge cochains, let \(p_v\) be the additive tree-path integral, and set
\[
 (Tx)_c=p_s(x)+x_c-p_t(x),\quad G=TT^*,\quad C=d_1j,
 \quad B=G^{1/2}C^*CG^{1/2}.                              \tag{3}
\]
Here j inserts chord cochains with zero tree entries; d_1 is the original
oriented face curl with the counting inner products. The identities
\(Tj=I\), \(\ker T=\operatorname{im}d_0=\ker d_1\) and
\(d_1T^*G^{-1}=C\) show that G and B are strictly positive. Choose once
an orthogonal matrix O with
\[
 O^TBO=\operatorname{diag}(\sigma_1^2,\ldots,\sigma_r^2),
 \quad \sigma_\nu>0,
 \qquad z^\alpha=O^TG^{-1/2}x^\alpha.                     \tag{4}
\]
The three Lie-algebra components are denoted by \(\alpha\); they are not
the physical spacing a. O acts on chord indices only.

Except for the Haar-null set where a chord equals \(-I\), every Z has
a unique logarithm
\(Z_c=\exp(y_c^\alpha T_\alpha)\), \(|y_c|<2\pi\).
The exact density and dilated chart are
\[
 \mathcal J(y)=(16\pi^2)^{-r}
    \prod_c\left(\frac{\sin(|y_c|/2)}{|y_c|/2}\right)^2,
 \qquad \Omega_g=\{x:|x_c|<2\pi/g\text{ for all }c\}.
                                                               \tag{5}
\]
For a function F in the based quotient define
\[
 (\mathcal B_gF)(x)=
 \begin{cases}
 g^{3r/2}\mathcal J(gx)^{1/2}F(\exp(gx)),&x\in\Omega_g,\\
 0,&x\notin\Omega_g.
 \end{cases}                                                   \tag{6}
\]
The change of variables in (5) proves this is an isometry into
\(L^2(\mathbb R^{3r},dx)\), onto the closed subspace supported in
\(\Omega_g\). Its adjoint has the reciprocal density and dilation on
that subspace and vanishes on its orthogonal complement. It is not
claimed onto the full Euclidean space for fixed g. Both \(\Omega_g\)
and the density are invariant under simultaneous color rotations, so
(6) intertwines the exact residual physical projections.

The full transformed local form, on compactly supported chart functions,
is
\[
 \frac2a\int A^{ij}(gx)
  \left(\partial_i f-\frac g2(\partial_i\log\mathcal J)(gx)f\right)^*
  \left(\partial_j f-\frac g2(\partial_j\log\mathcal J)(gx)f\right)dx
 +\int\frac{W(gx)}{2g^2a}|f|^2dx,                           \tag{7}
\]
where W is the full sum in (1) expressed by the original chord words,
\(A(0)=G\otimes I_3\), and
\[
 W(y)=\tfrac14\sum_\alpha\|Cy^\alpha\|^2+O_L(|y|^3).
                                                               \tag{8}
\]
All nonconstant coefficients and all word remainders remain in (7).

## 2. Compactness of actual bounded-energy vectors

We first prove the compactness needed for actual eigenvectors. Suppose
\(g_n\downarrow0\), \(\|F_n\|\le K\), and
\(q_{g_n}[F_n]\le K\), with fixed L and a. Write
\(f_n=\mathcal B_{g_n}F_n\). These vectors have a strongly convergent
subsequence in Euclidean L^2.

To prove this, choose a fixed small radius \(\rho>0\) within the
logarithm chart. The positivity of \(C^*C\), (8), and Taylor's integral
remainder give a number \(c>0\) with \(W(y)\ge c|y|^2\) for
\(|y|<\rho\). Flatness of every original face on the contractible open
box implies all chords are I, by the ordered square-interchange argument
for monotone tree paths. Thus W has exactly one zero on the compact chord
manifold. On the complement of this radius-\(\rho\) neighborhood it has
a strictly positive minimum \(c_\rho\).

Both terms of the original form are nonnegative. Its potential part
therefore yields, when \(g_n R<\rho\),
\[
 \int_{|x|>R}|f_n|^2dx
   \le \frac{2aK}{cR^2}+\frac{2aK g_n^2}{c_\rho}.        \tag{9}
\]
Indeed on \(R<|x|<\rho/g_n\) the potential is at least
\(c|x|^2/(2a)\); outside that region it is at least
\(c_\rho/(2g_n^2a)\). These are estimates for the full W, not a
replacement quadratic potential.

On any fixed ball \(|x|\le R\), for sufficiently small g the smooth
principal matrix \(A(gx)\) has a positive lower eigenvalue independent
of g. The logarithmic-density derivative in (7) is bounded there. The
kinetic part of (7), the L^2 bound, and
\(|u|^2\le2|u-v|^2+2|v|^2\) consequently bound
\(\|f_n\|_{H^1(B_R)}\). No derivative estimate is asserted across the
boundary of \(\Omega_g\); every fixed ball is eventually strictly inside.
Rellich compactness on a succession of fixed balls and a diagonal
subsequence give strong local L^2 convergence. The uniform tail estimate
(9), first with R large and then n large, upgrades it to global strong
L^2 convergence. It also preserves inner products for any finite family
of such vectors by polarization. Every constant here may depend on L,a;
none has been assumed uniform in volume.

## 3. Actual vacuum and finite spectral projections

Define
\[
 H_{\rm osc}=\frac1a\left[-2\sum_{\alpha,c,d}G_{cd}
      \partial_{x_c^\alpha}\partial_{x_d^\alpha}
                +\frac18\sum_\alpha\|Cx^\alpha\|^2\right].
                                                               \tag{10}
\]
Its physical subspace consists of the simultaneous-rotation invariants.
The companion finite-box proof gives actual physical eigenvalues
\(\mathcal E_k(g)\to\mu_k\), where the \(\mu_k\) are the sorted
physical eigenvalues of (10), with multiplicity. That proof uses upper
trial spaces and the full-form localization identity; it does not choose
the oscillator vacuum in place of \(\psi_g\).

We now prove the stronger vector conclusion. The comparison trial bound
makes \(q_g[\psi_g]=\mathcal E_g\) bounded at fixed L,a. Section 2
gives compactness of \(\mathcal B_g\psi_g\). For a smooth compactly
supported invariant test function h, pull h back by (6). Its support
stays in the logarithm chart, so it is in the exact original form domain.
The eigenvector identity is
\[
 q_g(\psi_g,\mathcal B_g^*h)
       =\mathcal E_g\langle\mathcal B_g\psi_g,h\rangle.
                                                               \tag{11}
\]
Local H^1 weak compactness from Section 2 and the uniform coefficient
convergence on the support of h let (7) pass to the limit in (11).
Every strongly converging subsequence therefore has a norm-one limit f
satisfying the weak equation \(H_{\rm osc}f=\mu_0f\).
The same energy bounds put f in the oscillator form domain: take increasing
balls in the local lower semicontinuity estimates for derivatives and the
quadratic potential. Compactly supported invariant test functions are a
form core, obtained by invariant smooth radial cutoffs followed by
convolution and rotation averaging. Thus the weak equation identifies
the represented self-adjoint operator, not a different extension.

The oscillator ground eigenspace is one-dimensional. The exact maps (6)
send the positive \(\psi_g\) to nonnegative functions, fixing their phase.
It follows that the entire family converges, not just a subsequence:
\[
 \mathcal B_g\psi_g\longrightarrow\Phi_0
           \quad\hbox{strongly in }L^2(\mathbb R^{3r}).      \tag{12}
\]
Put
\[
 S=G^{-1/2}B^{1/2}G^{-1/2}.
\]
The exact unit Gaussian in chord coordinates is
\[
 \Phi_0(x)=(\det S)^{3/4}(4\pi)^{-3r/4}
       \exp\left(-\frac18\sum_\alpha (x^\alpha)^TSx^\alpha\right).
                                                               \tag{13}
\]
In (4) it is the product
\(\prod_\nu(\sigma_\nu/(4\pi))^{3/4}
e^{-\sigma_\nu|z_\nu|^2/8}\), with the additional constant Jacobian
factor \((\det G)^{-3/4}\) when expressed as an x-wavefunction.
Each real z coordinate has vacuum variance \(2/\sigma_\nu\).
The density factor, this variance, and the ground energy
\(\mu_0=3\sum_\nu\sigma_\nu/(2a)\) are all retained.

Let I be a bounded interval whose endpoints avoid the spectrum of (10),
and let P_g(I) and P_0(I) be the physical spectral projections of H_g
and H_osc. Then, as operators on the common Euclidean physical subspace,
\[
 \|\mathcal B_gP_g(I)\mathcal B_g^*-P_0(I)\|\longrightarrow0.
                                                               \tag{14}
\]
Here and below the adjoint is zero on the complement of \(\Omega_g\).
For proof, eigenvalue convergence gives the same finite rank on both
sides for small g. Choose an orthonormal eigenbasis of the range on the
left. Each vector has bounded absolute energy, so Section 2 gives a
simultaneously strongly convergent subsequence. The argument (11) identifies
the limits as eigenvectors in the indicated oscillator interval. Their
inner products persist. Equality of ranks makes them a basis of that
entire interval. Finite sums of their rank-one projections converge in
operator norm. Every subsequence has the same projection limit, proving
(14) for the original family. Applying the same reasoning to intervals
shifted by the convergent \(\mathcal E_g\) gives (14) for excitation
operators \(H_g-\mathcal E_g\) and \(H_{\rm osc}-\mu_0\).

## 4. Transport of bounded observables and raw spectral measures

Suppose \(B_g\) is multiplication by a bounded physical function on the
original chord manifold, with \(\sup_g\|B_g\|<\infty\), and its
coordinate multiplier \(B_g(\exp(gx))\) converges at each x to a
bounded invariant multiplier B_0(x). This statement defines the class of
maps considered in this section; Section 5 constructs such a map exactly.
Equations (12), the multiplier bound, and dominated convergence against
\(|\Phi_0|^2\) give
\[
 \mathcal B_gB_g\psi_g\to B_0\Phi_0,\qquad
 c_g:=\langle\psi_g,B_g\psi_g\rangle
                  \to c_0:=\langle\Phi_0,B_0\Phi_0\rangle.
                                                               \tag{15}
\]
Consequently the actual vacuum-orthogonal vectors
\[
 v_g=(B_g-c_g)\psi_g
       \quad\hbox{satisfy}\quad
 \mathcal B_gv_g\to v_0=(B_0-c_0)\Phi_0.                  \tag{16}
\]
No unit-vector rescaling or division by a small norm is used here.

Define their raw positive excitation measures by
\[
 \nu_g(J)=\langle v_g,\mathbf1_J(H_g-\mathcal E_g)v_g\rangle,
 \qquad
 \nu_0(J)=\langle v_0,\mathbf1_J(H_{\rm osc}-\mu_0)v_0\rangle.
                                                               \tag{17}
\]
They converge weakly against every bounded continuous function on
\([0,\infty)\), with their total masses retained. To verify the tail
claim needed here, choose an oscillator energy cutoff R not at an
eigenvalue. From (14) and (16), the masses in [0,R] and the total masses
converge. Completeness of the oscillator eigenbasis makes
\(\nu_0((R,\infty))\to0\) as \(R\to\infty\); hence the family
\(\nu_g\) is tight as g tends to zero. On [0,R], isolate the finitely
many eigenvalue clusters and use eigenvalue convergence, (14), and uniform
continuity of the test function. The bounded test-function tail is then
controlled by tightness. This proves the stated convergence without
asserting a moment bound for an unspecified unbounded observable.

In particular for every fixed physical \(t\ge0\),
\[
 \langle v_g,e^{-t(H_g-\mathcal E_g)}v_g\rangle
       \to\langle v_0,e^{-t(H_{\rm osc}-\mu_0)}v_0\rangle.
                                                               \tag{18}
\]
The same finite-projection argument applies to any actual vectors whose
images under (6) converge strongly, including limits of bounded averaged
translation operators. Multiplication is not a necessary hypothesis for
that last vector statement.

## 5. An explicit gauge-invariant field observable with nonzero mass

Choose one spatial mode \(\nu\) in (4), and a real number \(\theta\).
Let \(\chi(y)\) be a smooth simultaneous-rotation-invariant function
equal to one near zero and supported strictly inside the product
logarithm chart. Set on that chart
\[
 B_{g,\theta}(Z)=\exp\left(i\theta\chi(y)
              |(O^TG^{-1/2}(y/g))_\nu|^2\right),          \tag{19}
\]
and set it equal to 1 outside the chart. This is a globally smooth
physical multiplication operator for each g>0. The support property
makes the extensions agree on a full neighborhood of the chart boundary.
It is unitary, and its pointwise multiplier limit is
\(B_{0,\theta}(x)=e^{i\theta|z_\nu|^2}\). Thus (15)--(18)
apply to the actual nonlinear model.

Write \(\sigma=\sigma_\nu\), \(k=3/2\), and
\(\beta=4\theta/\sigma\). Under \(|\Phi_0|^2\), the exact
radial variable \(q=\sigma|z_\nu|^2/4\) has density
\(q^{k-1}e^{-q}/\Gamma(k)\) on \([0,\infty)\).
Integrating the Gaussian with its original variance yields
\[
 c_0=(1-i\beta)^{-3/2},\qquad
 \|v_0\|^2=1-(1+\beta^2)^{-3/2}.                          \tag{20}
\]
The branch of the power is fixed by continuity from \(\beta=0\).
In particular \(\theta\ne0\) gives positive limiting centered mass.
An unchanged bounded continuous physical function B(Z), without the
explicit coordinate map (19), instead has limit B(I) and zero centered
mass by (15). Both statements follow from the same map; neither establishes
that the underlying observables are unrelated.

## 6. Complete spectral coefficients of the explicit observable

For clarity we compute all coefficients, not only a first energy moment.
Use the generalized Laguerre polynomials \(L_n^{k-1}(q)\), fixed by
\[
 \sum_{n=0}^\infty L_n^{k-1}(q)z^n
       =(1-z)^{-k}\exp\left(-\frac{qz}{1-z}\right),\quad |z|<1.
                                                               \tag{21}
\]
Equivalently their coefficients are
\(\sum_{j=0}^n(-1)^j\Gamma(n+k)q^j/
[\Gamma(k+j)(n-j)!j!]\). The Rodrigues expression
\(q^{1-k}e^q(d/dq)^n(e^{-q}q^{n+k-1})/n!\), obtained from
Leibniz's rule, proves by n integrations by parts that their orthogonal
squared norms in the Gamma probability measure are \((k)_n/n!\).
Boundary terms vanish at infinity exponentially and at zero by the powers
appearing before the nth integration. The equation
\(qL_n''+(k-q)L_n'+nL_n=0\) follows directly from their coefficients.
Conjugating the radial oscillator by its ground Gaussian gives
\[
 (H_{\rm osc}-\mu_0)(L(q)\Phi_0)
     =\frac{2\sigma}{a}[-qL''-(k-q)L']\Phi_0.             \tag{22}
\]
Thus \(\sqrt{n!/(k)_n}L_n^{k-1}(q)\Phi_0\) has excitation
energy \(2n\sigma/a\). These vectors are complete in the radial
subspace: if a radial L^2 function is orthogonal to every polynomial,
its Gamma-weighted Laplace transform is analytic on \(\Re t>-1/2\)
by Cauchy--Schwarz and has every derivative zero at t=0. Analyticity and
uniqueness of the Fourier transform of its integrable weighted measure
then make that function zero. Other modes remain in their vacuum factors.

Integrate (21) against \(e^{i\beta q}\) times the Gamma density.
For z near zero the integral is absolutely convergent, and it equals
\((1-i\beta+i\beta z)^{-k}\). Comparing coefficients gives
\[
 \langle \sqrt{n!/(k)_n}L_n^{k-1}\Phi_0,
                   e^{i\theta|z_\nu|^2}\Phi_0\rangle
  =\sqrt{(k)_n/n!}\frac{(-i\beta)^n}{(1-i\beta)^{n+k}}.
                                                               \tag{23}
\]
The vacuum coefficient is precisely (20); centering removes exactly n=0.
Therefore the complete limiting raw measure from the original actual
state is
\[
 \boxed{\nu_0=
   \sum_{n=1}^\infty
    \frac{(3/2)_n}{n!}
    \frac{\beta^{2n}}{(1+\beta^2)^{n+3/2}}
          \delta_{2n\sigma/a}.}                         \tag{24}
\]
Every weight is nonnegative, and the binomial generating series sums
them to \(1-(1+\beta^2)^{-3/2}\), matching the actual norm limit.
The full physical-time correlation is consequently
\[
 \boxed{\lim_{g\downarrow0}
   \langle v_{g,\theta},e^{-t(H_g-\mathcal E_g)}v_{g,\theta}\rangle
 = [1+\beta^2(1-e^{-2\sigma t/a})]^{-3/2}
                   -(1+\beta^2)^{-3/2},\quad t\ge0.}     \tag{25}
\]
This identity describes a proved fixed-box limit of full interacting
matrix elements. It does not assert that the original finite-g measure
equals the right side before taking the limit.

For a lowest mode,
\(\sigma=\sqrt8\sin(\pi/(4L+2))\). Choosing the explicit
\(\theta=\sigma/4\) gives \(\beta=1\), centered mass
\(d=1-2^{-3/2}\) and first positive atom of weight
\(3/(8\sqrt2)\) at energy
\(4\sqrt2\sin(\pi/(4L+2))/a\). Its positive raw mass is a
state calculation, not a claim based only on the eigenvalue location.

## 7. Exact fate of this particular macroscopic low-mode diagonal

There is a useful test of what the gap-closing diagonal in the companion
paper actually retains. Take \(L_j=j^2\), \(a_j=1/(100j)\), j>=2,
choose a lowest mode at each j, and set \(\theta_j=\sigma_j/4\).
Let \(\nu_{g,j}\) be its actual centered raw measure (17),(19).
The proved finite-box weak convergence permits a choice of strictly
positive \(g_j<1/j\) such that
\[
 d_{\rm BL}(\nu_{g_j,j},\nu_{0,j})<1/j,
 \qquad |\|v_{g_j,j}\|^2-d|<1/j.                         \tag{26}
\]
Here \(d_{\rm BL}\) is the supremum over real test functions with
supremum norm and Lipschitz constant at most one. On finite measures on
\([0,\infty)\), weak convergence with tightness and mass convergence
implies (26): restrict tests to a compact interval containing all but a
chosen tail mass; their restrictions form a totally bounded family by
Arzela--Ascoli, so a finite uniform net reduces the assertion to finitely
many continuous test functions. No uniform-in-j semiclassical error was
inserted in this choice.

The comparison measures have j-independent weights in (24) with
\(\beta=1\), and their nth atom has energy
\(2n\sigma_j/a_j\to0\) for every fixed n. Their summable tail
weights are also j-independent. Dominated convergence in this series,
followed by (26), proves
\[
 \nu_{g_j,j}\ \Longrightarrow\ d\,\delta_0,
 \qquad
 \langle v_{g_j,j},e^{-t(H_{g_j,j}-\mathcal E_{g_j,j})}v_{g_j,j}\rangle
       \longrightarrow d\quad(t\ge0).                   \tag{27}
\]
Every finite vector remains exactly vacuum-orthogonal; every finite
Hamiltonian retains g_j>0 and every original plaquette. Nevertheless
(27) is an atom at zero, not positive limiting spectral weight throughout
arbitrarily small intervals away from zero.

More precisely, suppose one tried to represent these limiting vectors
and correlations by a Hilbert vacuum \(\Omega\), a nonnegative
self-adjoint Hamiltonian K with \(K\Omega=0\), and a vector
\(v\perp\Omega\) of squared norm d. Equality
\(\langle v,e^{-tK}v\rangle=d\) for t>0 implies
\(\int(1-e^{-t\omega})d\nu_v(\omega)=0\). Positivity makes
\(\nu_v\) supported at zero, hence Kv=0. Since d>0, that representation
has at least two independent zero-energy vectors. It cannot at the same
time have a unique vacuum. This is an exact consequence for this retained
observable/state limit, not a claim that all spatial limits of (1) behave
this way. Different states and local-observable identifications require
their own maps and spectral calculations.

The result pinpoints a concrete issue: finite gaps can close while a
retained macroscopic mode becomes a stationary zero-energy sector. To
test the desired interacting theory one must transport the actual local
gauge-invariant fields and their nonzero finite-energy spectral weights,
not infer them from that single vanishing gap. The original nonlinear
Hamiltonians, exact chart maps and the failure of uniformity are explicit
in this calculation; no interacting continuum has been replaced by a
claimed free-theory counterexample.

## Primary context

The exact finite-box quotient construction and eigenvalue comparison are
included in the companion source cited in Section 1. The semiclassical
localization method is B. Simon, *Semiclassical analysis of low lying
eigenvalues. I. Non-degenerate minima: asymptotic expansions*, Annales de
l'Institut Henri Poincare A 38 (1983), 295--308, Sections 2,3,6,
https://www.numdam.org/item/AIHPA_1983__38_3_295_0/.
For maximal-tree lattice coordinates see C. W. Bauer, I. D'Andrea,
M. Freytsis and D. M. Grabowska, *A new basis for Hamiltonian SU(2)
simulations*, https://arxiv.org/abs/2307.11829. Their Hamiltonian
coefficients are not substituted for (1).
The target requirement of a nontrivial four-dimensional theory and its
vacuum/spectral axioms is A. Jaffe and E. Witten, *Quantum Yang--Mills
Theory*, Sections 3--4,
https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf.
The oscillator and Gamma identities used here are proved in Sections 3,6;
no novelty is asserted for those classical formulas.

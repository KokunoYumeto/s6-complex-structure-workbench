# The Gamma sector and the exact action of bounded local holonomies

8 September 2026. This note computes the configuration-observable map on
the radial spectral construction. It retains the original finite nonlinear
Hamiltonians and gives an explicit limit in which the Gamma spectral
sector survives while the unrescaled continuous gauge-invariant cylinder
algebra acts by scalars. No assertion about rescaled curvature fields or
all possible continuum constructions follows from that particular map.

## 1. Original states, measures, and an exact phase-density identity

Use the open-box SU(2) Hamiltonian, product Haar space, full vertex gauge
projection, and positive unit vacuum of the included fixed-box proofs:
\[
 H_j=\kappa_j\sum_eE_e+b_j\sum_p(2-\operatorname{tr}U_p),
 \quad \kappa_j=\frac{2g_j^2}{a_j},\quad
 b_j=\frac1{2g_j^2a_j},\quad L_j=j^2,\quad a_j=\frac1{100j}.
\]
The excitation operator is \(A_j=H_j-\mathcal E_j\).
Write \(d\mu_j=|\psi_j|^2dU\) for the actual vacuum configuration measure.
The radial multiplier \(B_j\) of the Gamma note is globally smooth,
gauge invariant and has modulus one. Put
\[
 m_j=\int B_j\,d\mu_j,\qquad
 v_j=(B_j-m_j)\psi_j .
\]
For any bounded configuration multiplier \(F_j\), direct multiplication
on the original Haar space gives
\[
 \begin{split}
 \langle v_j,F_jv_j\rangle
 &=\int F_j\bigl(1-\overline m_j B_j-m_j\overline B_j+|m_j|^2\bigr)d\mu_j,\\
 \left|\langle v_j,F_jv_j\rangle-\mu_j(F_j)\right|
 &\le\|F_j\|_\infty(2|m_j|+|m_j|^2).
 \tag{1}
 \end{split}
\]
There is no division by \(\|v_j\|\) in (1). For the uncentered vector
\(B_j\psi_j\), its configuration measure is exactly \(\mu_j\) at every
regulator, not only asymptotically.

The fixed-box comparison mean is
\(m_{0,j}=(1-i\sqrt j)^{-3/2}\). The positive-coupling selection can impose
\(|m_j-m_{0,j}|<1/j\) together with the Gamma raw-measure estimates,
because these are finitely many convergent quantities at each fixed
box. Thus \(|m_j|\to0\), so (1) identifies the limiting bounded
configuration expectations of the centered state with those of the
vacuum. The statement does not identify their electric or general
noncommuting observable expectations.

## 2. Positive coupling with a retained local flatness estimate

For each integer \(j\ge2\), choose a dyadic \(g_j=2^{-n_j}>0\) small
enough to satisfy all the Gamma note's raw spectral and centering
estimates and \(g_j<j^{-5}\). Let \(n_j\) be the least positive integer
satisfying the finite list. The fixed-box limits prove existence.
Consequently
\[
 g_j^2j^8<j^{-2},\quad
 \kappa_j=200jg_j^2,\quad b_j=50j/g_j^2,\quad
 \xi_j=\frac1{4g_j^4}.
 \tag{2}
\]
Every finite Hamiltonian retains its full electric term, magnetic term,
and scalar Wilson contribution. Along this selected diagonal the raw
spectral measure of \(v_j\) still tends to the Gamma law with shape
\(3/2\) and scale \(c=100\sqrt2\pi\).

Here are the exact spatial maps needed for the local observables. Fix a
coarse positive integer \(k\ge2\). When \(k\) divides \(j\), replace each
coarse edge by its ordered product of \(j/k\) collinear fine links, with
coarse vertex \(n\) placed at fine vertex \((j/k)n\). Physical positions
agree since \(a_j(j/k)n=a_kn\). Denote this continuous map by \(p_{k,j}\).
The small coarse box is contained in the fine box. It intertwines the
vertex gauge actions, with all intermediate endpoint factors cancelling
in their actual order. No reordering of noncommuting links is used.
For a common nested sequence one may restrict to \(j=n!\); then every
fixed \(k\) divides all sufficiently late indices. The Gamma formulas
and their constants are unchanged on this cofinal subsequence.

Section 13 of the included *Spatial continuum* proof establishes
\[
 \int \|I-U_C\|_{\rm HS}^2d\mu_j
 \le 12m^2g_j^2\sqrt{N_jM_j}
 \tag{3}
\]
for an \(m\)-by-\(m\) fine square. Its complete proof retains the ordered
non-Abelian filling, the actual vacuum variational bound and all boundary
counts. In particular \(N_j=6j^2(2j^2+1)^2\) is the number of fine edges,
\(M_j=12j^4(2j^2+1)\) the number of fine faces, and
\[
 \sqrt{N_jM_j}\le18\sqrt5\,j^6.
\]
For clarity the algebraic filling step is not a commuting approximation:
if a disk boundary is \(AqB\) and a newly attached face replaces its
shared segment \(q\) by \(r\), the changed holonomy times the old inverse
is \(A(rq^{-1})A^{-1}\). Iteration gives one conjugated oriented
plaquette per face. Unitary invariance and Cauchy--Schwarz give
\(\|I-U_C\|_{\rm HS}^2\le2m^2\sum_{\text{faces}}(2-\operatorname{tr}U_p)\).
The vacuum bound for the full face sum then gives (3).

Taking \(m=j/k\) gives for every coarse elementary face
\[
 \int\|I-U_p\|_{\rm HS}^2d(p_{k,j})_*\mu_j
 \le\frac{216\sqrt5}{k^2}g_j^2j^8
 \le\frac{216\sqrt5}{k^2j^2}.
 \tag{4}
\]
The finite number of coarse faces permits summation of (4).
The following identifies its full limiting measure, not just individual
plaquette means. On the contractible coarse box, flat link assignments
are exactly
\[
 U_e=q_{s(e)}^{-1}q_{t(e)},\qquad q_o=I,
 \tag{5}
\]
where \(o\) is the coarse root. To prove (5), construct \(q_v\) as the
ordered canonical path from \(o\) to \(v\). Each elementary flatness
identity moves one adjacent coordinate step past another, so all paths
have the same holonomy; hence \(q_sU_e=q_t\). Conversely (5) makes each
face telescope to identity. The inverse map is the canonical path
product. The flat configurations therefore form one compact vertex-gauge
orbit. Independent Haar \(q_v\), \(v\ne o\), give its invariant probability
\(\sigma_k\). It is unique: averaging a continuous function over the
compact gauge group is constant on this transitive orbit, so integration
against any invariant probability gives the same result.

Compactness supplies subsequential limits of the pushed vacuum measures.
Equation (4) puts each limit on the flat orbit; gauge invariance passes to
the limit. Uniqueness of \(\sigma_k\) identifies every subsequential
limit, hence the full sequence. Thus for every continuous gauge-invariant
function \(F\) on the fixed coarse link space, with
\(F_j=F\circ p_{k,j}\),
\[
 \|(F_j-F(I))\psi_j\|^2
 =\int|F-F(I)|^2d(p_{k,j})_*\mu_j\longrightarrow0 .
 \tag{6}
\]
Gauge invariance is essential in (6): a general noninvariant function
need not be constant on the flat orbit.

## 3. Exact semigroup domination on the full nonlinear model

The full finite-volume heat semigroup of \(H_j\) is positivity preserving.
One proof uses its original product-group electric heat kernels and
the positive multiplication operator \(\exp(-tV_j)\), where
\(V_j=b_j\sum_p(2-\operatorname{tr}U_p)\) is bounded and real.
The Trotter product converges strongly and preserves the positive cone.
For complex input, each positive integral kernel satisfies
\(|Kf|\le K|f|\); the same domination passes to the limit in \(L^2\)
and almost everywhere along a subsequence. Multiplication by the scalar
\(\exp(t\mathcal E_j)\) preserves it for \(\exp(-tA_j)\).
Moreover \(\exp(-tA_j)\psi_j=\psi_j\). Therefore for any bounded \(h_j\)
and \(t\ge0\),
\[
 \big|\exp(-tA_j)(h_j\psi_j)\big|
 \le\exp(-tA_j)(|h_j|\psi_j)
 \le\|h_j\|_\infty\psi_j .
 \tag{7}
\]
The physical subspace is invariant, so (7) applies to all the radial
physical states without replacing the Hamiltonian or gauge projection.
Since \(|B_j-m_j|\le2\), (7) yields
\[
 |\exp(-tA_j)v_j|\le2\psi_j .
 \tag{8}
\]
For any fixed finite coefficients \(a_\ell\) and nonnegative times
\(t_\ell\), let \(w_j=\sum_\ell a_\ell\exp(-t_\ell A_j)v_j\).
Equations (6)--(8) prove the explicit estimate
\[
 \|(F_j-F(I))w_j\|
 \le2\left(\sum_\ell|a_\ell|\right)
       \|(F_j-F(I))\psi_j\|\longrightarrow0 .
 \tag{9}
\]
The same result holds when finitely many bounded-phase radial families
are included, since each centered multiplier still has supremum at most
two. No estimate on an unbounded electric operator has been inserted.

## 4. The actual limiting observable representation

The Gamma note proves convergence of every finite time-orbit Gram matrix
to the one on \(L^2(\gamma_c)\), and that these orbit vectors are dense
there. Equation (9) therefore defines the limit of each fixed continuous
gauge-invariant configuration cylinder on this dense space as
\[
 \pi_{\rm cyl}(F)=F(I)\,I_{\mathcal H_\gamma}.
 \tag{10}
\]
This definition respects sums, products, conjugation and the unit, since
evaluation at the identity configuration has those properties. Also
\(\|\pi_{\rm cyl}(F)\|\le\|F\|_\infty\), so it extends by continuity to
the uniform closure of this cylinder algebra. The same scalar acts on
the separately retained vacuum. Formula (9) proves the operator map
on actual approximating vectors, not merely an equality of expectations.

The energy operator on the Gamma sector is nonetheless \(M_\omega\),
with strictly positive measure on every \((0,\varepsilon)\).
These two facts coexist: on this particular selected diagonal, the
unchanged bounded local holonomies cannot generate that nontrivial
spectral sector from the vacuum. Their representation (10) is explicit.
It neither proves that a rescaled curvature or electric algebra has the
same limit nor eliminates another running-coupling path.

The next mathematical map must retain a nonconstant observable beyond
(10). Candidates include the actual plaquette curvature divided by its
specified area and coupling, or gauge-invariant electric fluctuations.
They are unbounded along the regulator sequence, so the bounded factor
estimate (9) does not determine their limit. Their norms, moments,
domains, products and dynamics must be calculated with those factors
present; assigning them the scalar value (10) would be unjustified.

## Proof inputs and literature

The full operator, ground-state and fixed-box convergence proofs are
included as *The original finite-box SU(2) Hamiltonian at small positive
coupling* and *Actual weak-coupling vacuum, observable and spectral maps*.
The nonlinear vacuum estimate used in (3) is proved in Sections 12--13
of the included *Spatial continuum* manuscript. These are integral
mathematical inputs, not assumptions replacing the estimates.

The distinction between raw loop observables and their continuum scaling
is discussed in S. Chatterjee, *Yang--Mills for probabilists*,
Sections 3 and 6--7 ([arXiv:1803.01950](https://arxiv.org/abs/1803.01950)).
The nontrivial local-field target is specified by A. Jaffe and E. Witten,
*Quantum Yang--Mills Theory*, Section 2
([Clay problem text](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)).
Neither source is cited as proving the new operator limit (9)--(10);
that calculation is given above.

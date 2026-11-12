# Exact radial amplitude/time kernel and carrier-window representation

8 September 2026. This note computes the complete complex amplitude/time
kernel of the radial spectral family. It proves the continuous modulation
limit about a nonzero carrier, its exact Hamiltonian, and its relation to
the globally discontinuous amplitude family and the origin zero sector.

## Original objects and conventions

All inner products are conjugate linear in their first argument. Retain

\[
 L_j=j^2,\quad a_j=\frac1{100j},\quad
 \sigma_j=\sqrt8\sin\frac{\pi}{4j^2+2},\quad
 \lambda_j=\frac{2\sigma_j}{a_j}
 =400\sqrt2\,j\sin\frac{\pi}{4j^2+2},\quad j\ge2.
\]

Thus \(j\lambda_j\to c=100\sqrt2\pi\), with physical time t
and every spacing/frequency factor unchanged. Put \(k=3/2\),
\(s_j=\sqrt j\), and \(q=\sigma_j|z|^2/4\). In the exact
oscillator radial Hilbert map, the vacuum is the constant function one in

\[
 \mathcal H_\rho=L^2([0,\infty),\rho),\qquad
 d\rho(q)=\frac{q^{k-1}e^{-q}}{\Gamma(k)}dq.
\]

The normalized Laguerre vectors
\(\ell_n(q)=\sqrt{n!/(k)_n}L_n^{k-1}(q)\) form an orthonormal
basis; the excitation operator is \(\lambda_j N\), where
\(N\ell_n=n\ell_n\). This is the exact radial spectral-coordinate
map of the comparison operator, not replacement of the finite-g operator.
The actual nonlinear Hamiltonian, Haar isometry, physical projection, and
fixed-box transport are those proved in the included companions
*The original finite-box SU(2) Hamiltonian at small positive coupling*
and *Actual weak-coupling vacuum, observable and spectral maps*.

Define uncentered and centered radial vectors

\[
 \phi_j(b)=e^{ib s_jq},\quad
 m_j(b)=\langle1,\phi_j(b)\rangle=(1-ib s_j)^{-k},\quad
 v_j(b)=\phi_j(b)-m_j(b),\qquad b\in\mathbb R.
\]

Their raw centered norm is
\(1-(1+b^2j)^{-k}\). In particular v_j(0)=0 exactly. No division by
this norm is used in the kernel calculation.

## 1. The finite-j kernel, including complex powers and subtraction

The exact coefficients are

\[
 a_n(b)=\langle\ell_n,\phi_j(b)\rangle
 =\sqrt{\frac{(k)_n}{n!}}
       \frac{(-ib s_j)^n}{(1-ib s_j)^{n+k}}.
\]

Let

\[
 P_j(b,d)=(1+ib s_j)(1-id s_j)
          =1+bdj+i(b-d)s_j.
\]

The factors 1+ib s_j and 1-id s_j lie in the open right half-plane.
Their principal arguments add to
\(\arctan(bs_j)-\arctan(ds_j)\in(-\pi,\pi)\).
Consequently their principal logarithms add to the principal logarithm of
P_j, including when bd<0. Therefore

\[
 \overline{a_n(b)}a_n(d)
 =\frac{(k)_n}{n!}\frac{(bdj)^n}{P_j(b,d)^{n+k}},
 \quad
 \overline{m_j(b)}m_j(d)=P_j(b,d)^{-k}.
\]

For t>=0 the binomial-series argument has modulus strictly less than one:

\[
 \left|\frac{bdj\,e^{-t\lambda_j}}{P_j(b,d)}\right|
 \le\frac{|bd|j}{\sqrt{(1+b^2j)(1+d^2j)}}<1.
\]

If b or d is zero the argument is zero and the same formulas apply.
Summing first from n=0 gives the uncentered kernel

\[
 \begin{split}
 F_j(b,d;t)
 &:=\langle\phi_j(b),e^{-t\lambda_jN}\phi_j(d)\rangle\\
 &=\left[1+bdj(1-e^{-t\lambda_j})+i(b-d)\sqrt j\right]^{-k}.
 \tag{1}
 \end{split}
\]

The power in (1) is the principal one. To verify that no phase was lost
when combining the factors, let z run from 0 to e^{-t lambda_j} and put
E(z)=P_j-bdjz. When b=d, both P_j and E(z) are positive real. When b!=d,
E(z) stays in one open half-plane because its nonzero imaginary part is
constant. It never crosses the principal logarithm cut. Also
1-bdjz/P_j lies in the open right half-plane by the strict modulus bound.
At z=0 the logarithmic factorization is exact. Differentiating the two
logarithms along this path gives the same derivative -bdj/E(z), so the
factorization remains exact throughout. This proves the principal-power
identity even for negative bd.

Centering removes precisely the n=0 term. Thus the complete raw kernel is

\[
 \boxed{
 K_j(b,d;t)=
 \left[1+bdj(1-e^{-t\lambda_j})+i(b-d)\sqrt j\right]^{-k}
 -\left[(1+ib\sqrt j)(1-id\sqrt j)\right]^{-k}.
 }
 \tag{2}
\]

Equivalently it is the absolutely convergent series
\(\sum_{n\ge1}\overline{a_n(b)}a_n(d)e^{-t\lambda_jn}\).
Absolute convergence also follows directly from Cauchy--Schwarz and the
unit norms of the uncentered vectors. In particular
\(K_j(d,b;t)=\overline{K_j(b,d;t)}\), as required for a Gram kernel.
When either amplitude is zero, the two terms in (2) coincide and the
centered kernel is zero exactly.

For any finite list (b_l,u_l), u_l>=0, the time-vector Gram matrix is

\[
 \left\langle e^{-u_l\lambda_jN}v_j(b_l),
                e^{-u_m\lambda_jN}v_j(b_m)\right\rangle
 =K_j(b_l,b_m;u_l+u_m).
 \tag{3}
\]

Every such matrix is positive semidefinite, directly from its definition.
No real-part operation has been applied to its off-diagonal entries.

## 2. Fixed global amplitudes and the discontinuous limiting family

For each fixed t>=0,

\[
 j(1-e^{-t\lambda_j})\longrightarrow ct.
 \tag{4}
\]

For b=d!=0, equation (2) consequently gives

\[
 K_j(b,b;t)\longrightarrow(1+cb^2t)^{-k}.
 \tag{5}
\]

The subtracted vacuum mass is (1+b^2j)^{-k}->0. The limit in (5) is
the Laplace transform of Gamma(k,scale cb^2), with raw total mass one.
Its physical scale contains the full b^2 dependence.

For fixed b!=d, the imaginary part of the first denominator in (2) is
(b-d)sqrt(j), while its real part converges to 1+cbdt. Its inverse power
therefore tends to zero. When bd!=0 the second denominator has magnitude
of order j, so its inverse power also tends to zero. When bd=0, the
centered kernel is already zero. Thus

\[
 K_\infty(b,d;t)=
 \begin{cases}
 (1+cb^2t)^{-k},&b=d\ne0,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{6}
\]

For distinct nonzero b,d the leading off-diagonal phase is retained by
the stronger asymptotic

\[
 j^{k/2}K_j(b,d;t)\longrightarrow
 [i(b-d)]^{-k}
 =|b-d|^{-k}
       e^{-i\,\operatorname{sgn}(b-d)k\pi/2}.
 \tag{7}
\]

The vacuum subtraction is of smaller order j^{-k} in this case. Formula
(7) does not apply when one amplitude is zero, because then its two terms
cancel identically. For bd<0 the vacuum term itself has asymptotic phase
\(e^{-i\,\operatorname{sgn}(b-d)k\pi}\); replacing its denominator
by an unsigned real magnitude would give an incorrect finite-j kernel.

The uncentered limit additionally has F_infinity(0,0;t)=1; all its other
entries agree with (6). At equal time it is the Kronecker kernel on the
set of real amplitudes:

\[
 F_\infty(b,d;0)=\mathbf1_{\{b=d\}}.
 \tag{8}
\]

Its amplitude-only cyclic Hilbert space is therefore
\(\ell^2(\mathbb R_{\mathrm{discrete}})\), with unit basis e_b and
vacuum e_0. The finite-j identity
\(B_j(a)B_j(b)=B_j(a+b)\) gives the exact limiting action
\(U(a)e_b=e_{a+b}\). This is a unitary representation of the additive
group of real numbers, but is not continuous in its usual topology:

\[
 \langle e_0,U(a)e_0\rangle=\mathbf1_{\{a=0\}},\qquad
 \|U(a)e_0-e_0\|=\sqrt2\quad(a\ne0).
\]

In particular this amplitude group has no self-adjoint generator P with
U(a)=exp(iaP). Such exponentials are strongly continuous by dominated
convergence in the spectral measure of every vector. The centered family
has the related discontinuity v(0)=0 and norm(v(b))=1 for every b!=0.

The time-cyclic completion has more vectors than this amplitude-only
subspace. An exact representation of all fixed-global-amplitude/time
limits is

\[
 \mathcal H_{\mathrm{global}}=
 \mathbb C\Omega\ \oplus\!
 \bigoplus_{b\in\mathbb R\setminus\{0\}}\mathcal H_\rho,
 \qquad H_b=cb^2Q,\quad Qf(q)=qf(q),
 \tag{9}
\]

with H Omega=0 and phi(b)=1 in its b summand. The operator Q and its
domain are proved in Section 5. Formula (9) gives (6) exactly. Each fibre
is cyclic under its semigroup: if f is orthogonal to all exp(-t cb^2 q),
then the Laplace transform of the finite density f rho is zero for t>=0.
That transform is analytic for positive real part by dominated
differentiation on smaller half-planes. The identity theorem makes it zero
on that half-plane. Its values on s+iR, s>0, are the Fourier transform of
the integrable density e^{-sq}f rho, so Fourier uniqueness makes f=0.

Different nonzero amplitude sectors in (9) are orthogonal, but their
relation is explicit: all have the same q Hilbert space and generators
differing by the physical scalar cb^2. Equivalently the map
f(omega)->f(cb^2q) is a unitary from L2(Gamma(k,scale cb^2)) to H_rho,
intertwining multiplication by omega with cb^2Q. In particular the b and
-b fibres have the same energy operator despite their orthogonality in
this limiting family. Orthogonality does not establish unrelatedness.

## 3. Exact positive-g diagonal transport of the joint kernels

For the actual full nonlinear Hamiltonian at fixed j use the globally
smooth physical multiplier

\[
 B_{g,j}(b;Z)=
 \exp\left(ib\sqrt j\,\chi(y)
 \frac{\sigma_j}{4}
 \left|(O^TG^{-1/2}(y/g))_{\nu_j}\right|^2\right)
 \tag{10}
\]

on the chart and one outside it. The same chi is used for all amplitudes;
it is one near zero and supported inside the chart. All group products
\(B_{g,j}(a)B_{g,j}(b)=B_{g,j}(a+b)\) are exact. The original
nonlinear Hamiltonian, all original plaquettes, the actual positive unit
vacuum psi_gj, and the exact gauge projection are unchanged. Define

\[
 m_{g,j}(b)=\langle\psi_{g,j},B_{g,j}(b)\psi_{g,j}\rangle,
 \quad v_{g,j}(b)=(B_{g,j}(b)-m_{g,j}(b))\psi_{g,j},
 \quad A_{g,j}=H_{g,j}-\mathcal E_{g,j}.
\]

At every fixed j, the companion's bounded-observable theorem transports
each of these vectors strongly to its exact comparison vector. Its
finite spectral projections and tightness argument then give

\[
 \langle v_{g,j}(b),e^{-tA_{g,j}}v_{g,j}(d)\rangle
       \longrightarrow K_j(b,d;t),\qquad t\ge0.
 \tag{11}
\]

Cross terms follow either directly from finite projections or by complex
polarization of strongly transported finite sums of these vectors. This
retains both their real and imaginary parts.

In particular, at stage j one may prescribe any finite list of amplitude
values b_{j,l} and physical times t_{j,r}, and choose 0<g_j<1/j so that
all their coefficient errors and all their pairwise errors in (11) are
less than 1/j. Each j is fixed before applying its convergence theorem;
the finite lists may contain amplitudes of the form b_0+alpha/sqrt(j).
The minimum of finitely many positive small-coupling thresholds is still
positive. This proves the finite-set diagonal statement.

There is also a useful justified strengthening to one diagonal covering
all bounded amplitude/time sets. Here are the details, so no uniformity
in volume is assumed. For each fixed j, write f_g=mathcal B_g psi_g and
extend the transformed multiplier in (10) by any unit-modulus value off
Omega_g. It equals exp(ib sqrt(j) q(x)) on a ball whose radius tends to
infinity as g decreases to zero. Therefore

\[
 \sup_{b\in\mathbb R}
 \|\mathcal B_g B_{g,j}(b)\psi_g-e^{ib\sqrt j q}\Phi_0\|
 \le \|f_g-\Phi_0\|
       +2\|\mathbf1_{\{|x|>R_g\}}\Phi_0\|
 \longrightarrow0,
 \tag{12}
\]

for a suitable R_g->infinity at that fixed j. Inner products with f_g and
Phi_0 imply uniform convergence of m_gj(b) to m_j(b), and hence uniform
strong convergence of centered vectors as well.

For a compact amplitude interval [-M,M], the comparison vectors form a
norm-compact set: continuity in b follows by dominated convergence
against the Gaussian measure. Finite oscillator spectral cutoffs tend
strongly to the identity, so their tail errors are uniform on this compact
set. To see this explicitly, approximate the compact set by a finite
epsilon-net, control every net vector by one cutoff, and use that cutoff
and its complement have norm at most one. Convergence in operator norm of
the transported finite spectral projections, together with (12), gives
the same uniform tail bound for the actual vectors when g is small.

On a fixed finite spectral range, separate its finitely many eigenvalue
clusters. Their projections converge in operator norm, and their actual
excitation energies converge. Uniformly for 0<=t<=T, the difference of
the corresponding exponential scalars is bounded by T times the energy
difference, since all excitation energies are nonnegative. Thus the
finite-range kernel convergence is uniform for |b|,|d|<=M and t in [0,T].
The omitted same-projection tails contribute at most the product of the
two vector tail norms, by the contraction property of the semigroup.
Consequently (11) is uniform on each such compact parameter set.

At stage j choose a positive dyadic g_j<1/j for which this supremum error
on |b|,|d|<=j, 0<=t<=j and the coefficient supremum error are both <1/j.
Such a dyadic exists by the fixed-j result just proved. This yields a
single actual positive-coupling diagonal for every fixed real b,d,t and
for all carrier-window sequences with fixed finite b_0,alpha,delta,t.
It also gives the raw norms by t=0. No estimate uniform in j was asserted
for how small that dyadic must be, and no prescribed renormalized running
coupling is obtained.

## 4. Rescaling around zero: continuous amplitude and zero energy

Set b=alpha/sqrt(j), d=delta/sqrt(j), with alpha,delta fixed. The original
parameter in the multiplier becomes beta=alpha, exactly; q, its original
variance convention, the chart map, and a_j are unchanged. Equation (2)
is now

\[
 \begin{split}
 K_j^{(0)}(\alpha,\delta;t)
 &=[1+\alpha\delta(1-e^{-t\lambda_j})+i(\alpha-\delta)]^{-k}\\
 &\quad-[(1+i\alpha)(1-i\delta)]^{-k}.
 \end{split}
\]

Since lambda_j->0, its limit is the continuous kernel

\[
 K^{(0)}(\alpha,\delta)=
 [1+i(\alpha-\delta)]^{-k}
 -[(1+i\alpha)(1-i\delta)]^{-k},
 \tag{13}
\]

independent of physical time. It is represented exactly on H_rho by

\[
 v^{(0)}(\alpha)=e^{i\alpha q}-(1-i\alpha)^{-k},\qquad
 \Omega=1,
 \quad H^{(0)}=0.
 \tag{14}
\]

The raw norm in (14) is \(1-(1+\alpha^2)^{-k}\), strictly positive
for alpha!=0 and tending to zero continuously as alpha tends to zero.
The complete raw positive spectral measure is
\([1-(1+\alpha^2)^{-k}]\delta_0\). One may verify the energy
collapse directly in the exact Laguerre coordinate map: the coefficients
of exp(i alpha q) no longer depend on j, and
exp(-t lambda_j N) converges strongly to the identity by dominated
convergence of the squared Laguerre coefficients. The first raw
comparison energy moment is lambda_j k alpha^2->0 as an additional
calculation, not as an inference from weak convergence.

The unitary group W(alpha)f=exp(i alpha q)f is strongly continuous on
H_rho, with self-adjoint generator Q on its maximal domain. It provides
a continuous amplitude representation, but every vector in (14) remains
a zero-energy vector. Retaining this entire origin family therefore
enlarges the zero eigenspace beyond the single vacuum.

At finite j the rate of loss of continuity in the unscaled parameter is
also explicit. Differentiation under the Gamma integral gives

\[
 \|\partial_b v_j(b)\|^2
 =j\left[k(k+1)-k^2(1+b^2j)^{-(k+1)}\right].
\]

Indeed the uncentered derivative is i sqrt(j) q phi_j(b), of squared
norm j E(q^2)=jk(k+1), and subtracting its vacuum component removes
\(|m_j'(b)|^2=jk^2(1+b^2j)^{-(k+1)}\). At b=0 this norm squared
is jk. Passing from b to alpha=b sqrt(j) removes precisely that factor
j; it does not alter the already-retained Hamiltonian spacing lambda_j.

## 5. Nonzero carrier windows: continuous modulation and Gamma energy

Fix a nonzero real carrier b_0. Define

\[
 b_j(\alpha)=b_0+\frac{\alpha}{\sqrt j},\qquad
 d_j(\delta)=b_0+\frac{\delta}{\sqrt j}.
\]

The exact multiplier identity is

\[
 B_j(b_j(\alpha))=B_j(b_0)e^{i\alpha q}.
 \tag{15}
\]

At positive g the same identity holds with q replaced by the exact
chart-cutoff radial function in (10), so these states share an actual
finite-regulator multiplier relation.

Now
\((b_j-d_j)\sqrt j=\alpha-\delta\) exactly,
\(b_jd_j\to b_0^2\), and (4) holds. The first denominator in (2)
therefore tends to
\(1+cb_0^2t+i(\alpha-\delta)\). The subtracted vacuum product
tends to zero because both beta parameters b_0 sqrt(j)+alpha and
b_0 sqrt(j)+delta have magnitude tending to infinity. Thus

\[
 \boxed{
 K^{(b_0)}(\alpha,\delta;t)=
 [1+cb_0^2t+i(\alpha-\delta)]^{-k},\qquad b_0\ne0.
 }
 \tag{16}
\]

This is a continuous, nonconstant amplitude/time kernel. In particular
its equal-amplitude raw spectral measure is Gamma(k,scale cb_0^2),
independent of the finite offset alpha. Its off-diagonal entries retain
the full relative modulation phase. Equations (13) and (16) differ at
b_0=0 precisely because the vacuum subtraction then survives.

Put h_0=cb_0^2>0. On H_rho define

\[
 \phi^{(b_0)}(\alpha)(q)=e^{i\alpha q},\qquad
 Qf(q)=qf(q),\quad
 \operatorname{Dom}Q=\left\{f:\int q^2|f(q)|^2d\rho(q)<\infty\right\},
 \qquad H^{(b_0)}=h_0Q.
 \tag{17}
\]

Then the Gamma integral proves exactly

\[
 \begin{split}
 \langle\phi^{(b_0)}(\alpha),
             e^{-tH^{(b_0)}}\phi^{(b_0)}(\delta)\rangle
 &=\int_0^\infty e^{-[h_0t+i(\alpha-\delta)]q}d\rho(q)\\
 &=[1+h_0t+i(\alpha-\delta)]^{-k}.
 \end{split}
 \tag{18}
\]

The real part of the integrating coefficient 1+h_0t is positive,
fixing the same principal branch as in the finite-j formula.

Here are the operator and density details. Multiplication by q on the
maximal domain in (17) is densely defined and symmetric. For nonreal z,
the inverse multiplier (q-z)^{-1} is bounded and maps H_rho into that
domain, since q/(q-z) is bounded. It supplies both nonreal resolvents;
equivalently the adjoint's domain is exactly the same maximal weighted
L2 domain. Thus Q is self-adjoint. The unitary group
W(alpha)=exp(i alpha Q) is multiplication by exp(i alpha q). For every
f in H_rho, dominated convergence with bound 4|f|^2 proves its strong
continuity. On Dom Q the difference quotient tends in norm to iQf,
using |(exp(ihq)-1)/h|<=q. Conversely, existence of a norm derivative
forces the difference quotients to be bounded in L2; Fatou then gives
qf in L2. Hence this is exactly the generator domain, not a smaller
unspecified core. Since h_0>0, H^(b_0) has the same domain.

The span of exp(i alpha q), alpha real, is dense in H_rho. If f is
orthogonal to all these vectors, Cauchy--Schwarz makes the density
f(q)rho(q) integrable on the real line after extending it by zero to
negative q, and its Fourier transform vanishes at every real frequency.
For an explicit uniqueness argument, convolve that L1 density with a
Gaussian of any positive variance. The Gaussian Fourier integral and
Fubini express the convolution as the integral of its vanishing Fourier
transform times the Gaussian Fourier multiplier, so the convolution is
zero. Gaussian convolutions converge to the original L1 density as the
variance decreases to zero; this follows first for continuous compactly
supported functions by uniform continuity and Gaussian tails and then
for general L1 functions by density and contraction. Thus the density,
and therefore f, is zero. This proves the asserted dense span.

Consequently (18) determines the entire carrier-window cyclic Hilbert
space, rather than a proper unidentified subspace. It is the b_0 fibre
already present in (9): the fixed carrier corresponds to alpha=0, and
the window supplies its vectors exp(i alpha q), which lie in that same
time-cyclic fibre. This is the exact map from the globally discontinuous
amplitude labels to their continuous local modulations.

The carrier Hamiltonian can also be checked by an exact differential
conjugation, before taking any limit. On the radial coordinate space,

\[
 Nf=-qf''-(k-q)f',\qquad T_\beta f=e^{i\beta q}f.
\]

For every \(f\in C_c^\infty((0,\infty))\), both f and T_beta f
belong to the radial oscillator operator domain. Product differentiation
with all signs retained gives

\[
 T_\beta^*(\lambda_jN)T_\beta f
 =\lambda_jNf-2i\lambda_j\beta qf'
   +\lambda_j\beta^2qf-i\lambda_j\beta(k-q)f.
 \tag{18a}
\]

For beta=b_0 sqrt(j), the coefficients satisfy
lambda_j beta^2->cb_0^2, lambda_j beta->0, and lambda_j->0. Every
function multiplying them in (18a) is in L2(rho), since f is smooth
with compact support away from zero. Therefore

\[
 T_{b_0\sqrt j}^*(\lambda_jN)T_{b_0\sqrt j}f
       \longrightarrow cb_0^2Qf
       \quad\text{strongly in }\mathcal H_\rho.
 \tag{18b}
\]

The displayed test functions are an operator core for Q: truncate any
f in its maximal domain to [1/R,R], which converges in the norm
\(\int(1+q^2)|f|^2d\rho\), and then approximate each truncated
function by smooth compactly supported functions in a slightly larger
interval, where the weighted density is bounded above and below by
positive constants. This proves a graph limit on a stated core with
the exact phase and physical-time scaling. Equation (18) supplies the
complete semigroup identification; no removal of the differential
terms from the original finite-j operator is asserted in (18a).

The spectral projections of H^(b_0) multiply by indicators of h_0 q.
Its constant vector has the raw probability law Gamma(k,scale h_0),
and its kernel at zero is trivial because rho has no atom at q=0. Its
spectrum is [0,infinity): outside this interval the resolvent multiplier
is bounded, while normalized indicators of arbitrarily short positive
rho-measure intervals about q=E/h_0 are approximate eigenvectors for
every E>=0. In particular the spectrum reaches zero continuously.

A separate vacuum can be retained by adjoining C Omega with energy zero,
orthogonal to this carrier fibre. The kernel on that direct sum
represents the vacuum and all these carrier states; it has a unique zero
eigenvector within those retained sectors. Formula W(alpha) on the
carrier fibre does not by itself prescribe how the actual modulation
acts on Omega. The actual origin-window vectors in Section 4 give that
additional action if they too are retained, and then add the extra zero
sector described there. No arbitrary scalar action on Omega is inferred.

## 6. The complete relation between different windows

For two distinct fixed carriers b_0!=d_0, and finite offsets alpha,delta,
the term (b_j-d_j)sqrt(j) has magnitude tending to infinity. The first
term of (2) therefore vanishes. Each vacuum product also vanishes unless
both carriers are zero, which is excluded in this case; if one carrier
is zero its bounded coefficient multiplies the other vanishing
coefficient. Thus all cross kernels between different carrier windows
tend to zero, including cross kernels between a nonzero carrier window
and the origin window.

All uncentered window kernels together have the exact representation

\[
 \mathcal H_{\mathrm{windows}}
   =\bigoplus_{b_0\in\mathbb R}\mathcal H_\rho,
 \qquad
 \phi(b_0,\alpha)=e^{i\alpha q}\text{ in fibre }b_0,
 \qquad \Omega=\phi(0,0),
 \tag{19}
\]

with H acting as cb_0^2 Q in fibre b_0 and as the zero operator on the
entire origin fibre. Its domain is the set of families f satisfying

\[
 \sum_{b_0\ne0}c^2b_0^4\int q^2|f_{b_0}(q)|^2d\rho(q)<\infty.
\]

This direct sum is self-adjoint by its fibre resolvents, whose norms are
bounded by 1/|Im z| uniformly in b_0 for nonreal z. Every vector has at
most countably many nonzero components: the set of components of norm
at least 1/n is finite for every n. Thus all sums and norm arguments
have their usual Hilbert direct-sum meaning.

The actual common modulation and carrier-shift identities have exact
counterparts on (19):

\[
 (W(\eta)f)_{b_0}(q)=e^{i\eta q}f_{b_0}(q),\qquad
 (U(a)f)_{b_0}(q)=f_{b_0-a}(q).
 \tag{20}
\]

W is strongly continuous by dominated convergence in the sum of the
fibre norms. U is unitary but nonregular, already on Omega. The two
groups commute. On their common dense window vectors they implement
alpha->alpha+eta and b_0->b_0+a respectively, exactly matching the
finite-regulator multiplier identities. Their extension from that dense
span is therefore determined. H has zero kernel equal to the entire
origin fibre, while each nonzero fibre has trivial zero kernel.

The representation (9) embeds isometrically into (19) by retaining just
the constant vector in the origin fibre and every vector in every
nonzero fibre. That subspace is invariant under H and its semigroup.
It need not be invariant under W: W(eta)Omega is a nonconstant origin
vector for eta!=0. This identifies exactly which extra states appear
when the modulation is also applied to the vacuum. Neither construction
identifies a spatial local gauge algebra.

## 7. Configuration density and retained phases

At every finite g,j and every real amplitude, |B_gj(b)|=1 pointwise.
Thus for every bounded multiplication observable F on the original
configuration space,

\[
 \langle B\psi,F B\psi\rangle=\langle\psi,F\psi\rangle.
 \tag{21}
\]

This is an exact identity of uncentered configuration densities, before
any limit. It applies in particular to bounded physical multiplication
observables, with the actual vacuum and Haar measure retained.

For m=<psi,B psi> and v=(B-m)psi, expansion gives

\[
 \begin{split}
 \langle v,Fv\rangle-\langle\psi,F\psi\rangle
 &=-\overline m\langle\psi,FB\psi\rangle
   -m\langle\psi,FB^*\psi\rangle
   +|m|^2\langle\psi,F\psi\rangle,
 \end{split}
\]

and therefore the raw bound

\[
 \left|\langle v,Fv\rangle-\langle\psi,F\psi\rangle\right|
 \le\|F\|(2|m|+|m|^2).
 \tag{22}
\]

It also holds for complex bounded F. For the carrier-window amplitudes,
m_j=(1-i(b_0 sqrt(j)+alpha))^{-k}->0, and the positive-g diagonal in
Section 3 transports this coefficient. Consequently (22) tends to zero
for every uniformly bounded sequence of configuration multipliers F_j.
The retained raw centered norm is 1-|m_j|^2->1. If one additionally
divides by that explicitly retained norm, the corresponding error is
bounded by
\(\|F\|(2|m|+2|m|^2)/(1-|m|^2)\), which also tends to zero.

These equal configuration statistics coexist with the nontrivial Gamma
energy law proved in (16)--(18). Their compatibility already holds at
finite regulators: multiplication by a phase preserves configuration
density, while electric derivatives differentiate that phase. For the
actual Hamiltonian's ground-state quadratic form and a smooth unit
multiplier B=exp(i h), the exact identity is

\[
 q_{H-\mathcal E}[B\psi]
   =\frac{2g^2}{a}\int\psi^2
      \sum_{e,\alpha}|X_{e,\alpha}B|^2dU
   =\frac{2g^2}{a}\int\psi^2
      \sum_{e,\alpha}|X_{e,\alpha}h|^2dU.
 \tag{23}
\]

It follows from the companion's exact ground-state transform, and
|X exp(ih)|^2=|Xh|^2. Subtracting m psi does not change this excitation
form because (H-mathcal E)psi=0. Equation (23) explains, with the
original coefficient 2g^2/a, how a nonconstant smooth phase can alter
energy without altering configuration probabilities. It does not infer
limits of unspecified electric observables or unbounded moments from
the bounded-configuration identity.

## 8. Proven scope

The exact complex Laguerre sum yields a globally nonregular amplitude
family, a continuous origin rescaling whose energies collapse to zero,
and a continuous modulation window about every nonzero global radial
carrier with generator H=cb_0^2Q and a Gamma spectral law. The full
phase, vacuum subtraction, raw mass, physical time, and parameter
dictionary are preserved. The positive-g construction transports all
finite Gram matrices, and the fixed-j compactness argument supplies one
diagonal for the stated parameter families.

The carrier-window modulation is about a selected macroscopic radial
mode. Its exact representation, its inclusion into the global spectral
fibres, and its relation to the origin zero sector have been proved.
They do not specify spatial local fields, their complete gauge-observable
algebra, or the renormalized interacting four-dimensional theory. Failure
of the unscaled global amplitude to be regular does not prove that every
other bridge fails; the continuous nonzero-carrier map above is an
explicit further relation.

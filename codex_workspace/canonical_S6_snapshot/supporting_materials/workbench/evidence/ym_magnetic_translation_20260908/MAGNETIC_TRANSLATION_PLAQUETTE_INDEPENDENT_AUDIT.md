# Independent audit: full-box projected magnetic plaquettes

8 September 2026. This audit preserves the full finite open Wilson box,
the original \(\kappa,b,\xi=b/\kappa\), the scalar \(2bM\), every face,
and the actual normalized positive interacting ground state. It makes
no continuum or uniform-volume claim. The source is
MAGNETIC_TRANSLATION_PLAQUETTE.md in this directory.

## 1. Exact noncommuting vertex integral and all-coupling classification

The four independently oriented physical edges are \(U,V,Z,Y\), with
face word \(UVZ^{-1}Y^{-1}\). For their fixed translations \(a,d,c,b_0\)
in the same order, the translated word is
\[
\operatorname{tr}(a^{-1}Ud^{-1}VZ^{-1}cY^{-1}b_0).
\]
Gauge substitution \(U_e\mapsto g_sU_eg_t^{-1}\) and cyclicity move
all three nonempty vertex insertions into the exact order
\[
\operatorname{tr}\bigl[
(g_0^{-1}b_0a^{-1}g_0)U(g_i^{-1}d^{-1}g_i)
VZ^{-1}(g_j^{-1}cg_j)Y^{-1}\bigr].
\]
The fourth vertex cancels. The first insertion is the product
\(b_0a^{-1}\) before integration, not two independent factors.
For any complex \(2\times2\) matrix \(C\), the Haar twirl commutes
with every irreducible fundamental matrix, so it is scalar; its trace
fixes that scalar to \(\operatorname{tr}C/2\). Consequently
\[
\Pi\mathcal T_hW_p=\alpha_pW_p,\qquad
\alpha_p=\frac18\operatorname{tr}(b_0a^{-1})
\operatorname{tr}(d^{-1})\operatorname{tr}(c).
\]
No commutation of the four translation assignments is used.
Inverse-trace invariance in \(SU(2)\), together with cyclicity for
the first factor, gives \(\alpha_p(h^{-1})=\alpha_p(h)\).
The examples with \(a=b_0\) and with all four assignments equal to
\(i\sigma_3\) correctly disprove the independent-twirl and
background-face-holonomy substitutions, respectively.

The compact elliptic Hamiltonian has a strictly positive smooth ground
state \(\psi\). The original ground-state transform proves simplicity:
\[
\mathfrak q_{H-E}(\psi F,\psi F)
=\kappa\sum_{e,a}\int\psi^2|X_{e,a}F|^2\,dU .
\]
Thus its normalized positive ground state is invariant. All derivatives
and form expressions in the source are legitimate since \(\psi^{-1}\)
is smooth and bounded on the compact configuration manifold.

Let \(F=\Pi\mathcal T_h\psi\), \(c=\langle\psi,\mathcal T_h\psi\rangle\)
and \(\chi=F-c\psi\). If \(\chi=0\), Haar integration of \(F=c\psi\)
gives \(c=1\), because both averaging and translation preserve the
Haar integral and \(\int\psi>0\). Orthogonal-projection norm equality
then gives \(\mathcal T_h\psi=\psi\). Translating and subtracting the
eigen-equation, using commutation with the electric Casimir, gives
\[
b(\mathcal T_h\mathcal V-\mathcal V)\psi=0,\qquad
\mathcal V=\sum_pW_p .
\]
For \(b>0\), positivity permits division by \(\psi\). Projecting and
using \(\langle W_p,W_q\rangle=\delta_{pq}\) forces \(\alpha_p=1\)
for each face. Conversely \(\alpha_p=1\) gives projection norm
equality for each \(\mathcal T_hW_p\), hence
\(\mathcal T_hW_p=W_p\) for every face. Translation then commutes
with the full Hamiltonian and fixes its unique normalized positive
vacuum. Thus all equivalences in source (4.5) hold for every \(b>0\).
At \(b=0\), the vacuum is constant and the separate stated exception
is necessary.

For the unprojected energy, conjugation changes only the potential.
The actual invariant density permits the multiplication function
\(\mathcal T_h^{-1}W_p\) to be Haar-projected, giving exactly
\[
\mathfrak q_{H-E}[\mathcal T_h\psi]
=b\sum_p(1-\alpha_p)\int W_p\psi^2\,dU .
\]
This uses neither independence nor a sign assumption for individual
true-vacuum moments. The aggregate is nonnegative by \(H-E\geq0\).

## 2. True-vacuum perturbation and exact coupling parity

The product free spectrum is a sum of \(j_e(j_e+1)\), with isolated
constant eigenvalue zero and first nonzero eigenvalue \(3/4\). A face
has four distinct fundamental edges, so \(H_0W_p=3W_p\).
The Haar mean of each face vanishes. Distinct elementary faces have
distinct edge supports, and an edge occurring only once kills their
mixed Haar integral. The equal-face integral is 1. Therefore
\[
\langle W_p,W_q\rangle=\delta_{pq},\quad
\|\mathcal V\|_2^2=M,\quad \|\mathcal V\|_\infty=2M .
\]
On the radius-\(3/8\) contour the free resolvent bound is \(8/3\).
The Neumann parameter is \(16M|\xi|/3\), proving the stated
spectral-projection disk \(|\xi|<3/(16M)\). The mean-one
eigenvector normalization is required only locally at zero; the
source correctly supplies the smaller explicit nonvanishing criterion.
The analytic elliptic bootstrap into every fixed Sobolev space is
valid at the fixed finite dimension.

For the actual normalized real vacuum,
\[
\psi_\xi=1+\xi A+\xi^2D+O_L(\xi^3),\qquad
A=\mathcal V/3,\quad \int D=-M/18 .
\]
The last mean follows from unit \(L^2\) norm, not from dropping
the unknown second-order eigenfunction. Consequently
\[
\chi_{\xi,h}=\frac{\xi}{3}\sum_p(\alpha_p-1)W_p+O_L(\xi^2)
\]
in \(H^2\) and every fixed higher Sobolev norm. If
\(\mathcal S_h=\sum_p(1-\alpha_p)\),
\(\mathcal R_h=\sum_p(1-\alpha_p^2)\), and
\(\mathcal D_h=\sum_p(1-\alpha_p)^2\), the order-\(\xi^2\)
overlap and uncentered projection-norm losses are respectively
\(\mathcal S_h/9\) and \(\mathcal R_h/9\). Their difference gives
\(\mathcal D_h=2\mathcal S_h-\mathcal R_h\), as required after
vacuum subtraction.

The central cochain
\[
z_i(n)=(-1)^{\sum_{k<i}n_k}I
\]
has face product \(-I\) in every plane \(i<j\): shifting \(z_j\)
in direction \(i\) changes its sign, while shifting \(z_i\) in
direction \(j\) does not. This holds for every existing boundary
face as well. The unitary involution \(\mathcal Z=\mathcal T_z\)
commutes with all translations and gauge transformations and sends
\(\mathcal V\) to \(-\mathcal V\). Uniqueness gives
\(\psi_{-\xi}=\mathcal Z\psi_\xi\) and \(e(-\xi)=e(\xi)\).
The scalar \(2bM\) is not incorrectly declared even: it cancels in
the excitation operator
\(\kappa(H_0-\xi\mathcal V-e(\xi))\), which is conjugated to the
negative-\(\xi\) version by \(\mathcal Z\).

Thus the squared centered norm, overlap, uncentered squared norm
and excitation form are even real-analytic near zero. The odd
coefficients in the displayed scalar expansions vanish exactly.
The leading vector lies entirely in the free energy-3 eigenspace,
so the source coefficients are
\[
c=1-\xi^2\mathcal S_h/9+O_L(\xi^4),\qquad
\|F\|^2=1-\xi^2\mathcal R_h/9+O_L(\xi^4),
\]
\[
\|\chi\|^2=\xi^2\mathcal D_h/9+O_L(\xi^4),\qquad
\mathfrak q_{H-E}[\chi]
=\kappa\xi^2\mathcal D_h/3+O_L(\kappa\xi^4).
\]
At fixed \(\mathcal D_h>0\), division yields
\(\mathcal Q_{\xi,h}=3\kappa+O_{L,h}(\kappa\xi^2)\).
For bounded remainders \(C_L\), the criterion
\(C_L\xi^2\leq\mathcal D_h/18\) makes the denominator at least
\(\mathcal D_h/18\); subtraction of \(3\kappa\) leaves a numerator
at most \(4C_L\kappa\xi^2\). This verifies the explicit factor 72
in source (5.10).

With the original physical dictionary the leading squared norm is
\(\mathcal D_h/(144g_{\rm YM}^8)\), excitation form
\(\mathcal D_h/(24g_{\rm YM}^6a)\), quotient
\(6g_{\rm YM}^2/a\), and quotient remainder scale
\(1/(8g_{\rm YM}^6a)\). All substitutions check.

One wording correction was reported immediately: before (5.7),
“the norm of \(\chi\)” must read “the squared norm of \(\chi\)” in
the real-analytic assertion. The unsquared norm is
\(|\xi|\sqrt{\mathcal D_h}/3+O(|\xi|^3)\) when \(\mathcal D_h>0\);
it is even but not analytic at zero. The displayed one-sided
\(\xi\downarrow0\) norm expansion is correct.

## 3. Native angular coefficient and complete face counts

For \(h_1(n)=e^{-\theta n_2H_c}\), \(H_c=i\sigma_3=-2T_3\),
the exact vertex formula gives
\[
\alpha_{12}(m)=\cos(m\theta)\cos((m+1)\theta),\quad
\alpha_{13}(m)=\cos^2(m\theta),\quad \alpha_{23}=1 .
\]
The 12 multiplicity at each \(m=-L,\ldots,L-1\) is \(2L(2L+1)\);
the 13 multiplicity at each \(m=-L,\ldots,L\) is \(4L^2\).
Hence the full first norm coefficient is exactly
\[
\mathcal D_L(\theta)=
2L(2L+1)\sum_{m=-L}^{L-1}
[1-\cos(m\theta)\cos((m+1)\theta)]^2
+4L^2\sum_{m=-L}^{L}\sin^4(m\theta).
\]
The 23 faces have not been removed from the interacting vacuum;
only their first coefficient is zero.

Product-to-sum gives
\(\cos(m\theta)\cos((m+1)\theta)
=\{\cos\theta+\cos((2m+1)\theta)\}/2\).
Squaring the resulting expression and using
\(\cos^2x=(1+\cos2x)/2\) proves the 12 Fourier formula (6.8);
\(\sin^4x=(3-4\cos2x+\cos4x)/8\) proves the 13 formula.
The finite sums, not ratios with zero denominators, define every
resonance. Summing finite geometric series gives the printed ratios
where their denominators are nonzero, and continuity covers the rest.

The two terms \(m=0,-1\) give
\(4L(2L+1)(1-\cos\theta)^2\leq\mathcal D_L(\theta)\).
Bounding the 12 summands by 4 and the 13 summands by 1 gives
\(\mathcal D_L\leq20L^2(2L+1)=5M/3\).
Thus \(\mathcal D_L=0\) exactly for \(\theta\in2\pi\mathbb Z\).
The all-\(b>0\) classification proves the same exact zero set for
the physical centered vector, not merely its perturbative coefficient.
At \(\pi\) and \(\pi/2\), direct parity counting gives respectively
\[
16L^2(2L+1),\qquad
4L^2(3L+1+(L\bmod2)).
\]
These values and all Fourier factors check.

## 4. Full small-angle polynomial and global signed error

For \(r_m=m^2+m+\tfrac12\), direct polynomial summation gives
\[
\sum_{m=-L}^{L-1}r_m^2=\frac{L(4L^4+1)}{10},\qquad
\sum_{m=-L}^{L}m^4=
\frac{L(L+1)(2L+1)(3L^2+3L-1)}{15}.
\]
Both identities follow at \(L=1\) and by endpoint increments; for the
first the increment is \(2(L^2+L+\tfrac12)^2\), for the second
\(2(L+1)^4\). Multiplication by the exact face counts therefore gives
\[
\begin{split}
\mathcal A_L
&=\frac{L^2(2L+1)}{15}
(24L^4+24L^3+8L^2-4L+3)\\
&=\frac{16}{5}L^7+\frac{24}{5}L^6
+\frac83L^5+\frac2{15}L^3+\frac15L^2 .
\end{split}
\]
The analogous unsquared sums
\(\sum_{-L}^{L-1}r_m=L(2L^2+1)/3\) and
\(\sum_{-L}^{L}m^2=L(L+1)(2L+1)/3\) give exactly
\[
\mathcal B_L=\frac{2L^2(2L+1)(4L^2+2L+1)}3 .
\]
These are the coefficients of \(\theta^4\) in \(\mathcal D_L\)
and \(\theta^2\) in \(\mathcal S_L\), respectively.

The error estimate is valid for every real angle, not only a formal
Taylor series. The inequality
\[
0\leq t^2/2-(1-\cos t)\leq t^4/24
\]
follows from \(|\sin(t/2)|\leq|t|/2\) and the fourth-order Taylor
remainder bound. For
\(u=1-\cos x\cos y\) and \(q=(x^2+y^2)/2\), averaging this inequality
at \(x+y\) and \(x-y\) gives
\[
0\leq u\leq q,\qquad
0\leq q-u\leq
\frac{x^4+6x^2y^2+y^4}{24}\leq q^2/3 .
\]
The last inequality is exactly \((x^2-y^2)^2\geq0\).
Consequently \(0\leq q^2-u^2\leq2q^3/3\).
For \(u=\sin^2x\) and \(q=x^2\), application at \(2x\) gives the
same two inequalities. Inserting the respective face arguments proves
\[
0\leq\mathcal A_L\theta^4-\mathcal D_L(\theta)
\leq\mathcal E_L|\theta|^6,\qquad
\mathcal E_L=\frac23\left[
2L(2L+1)\sum_{m=-L}^{L-1}r_m^3+
4L^2\sum_{m=-L}^{L}m^6\right].
\]

The exact cubic moment is
\[
\boxed{\sum_{m=-L}^{L-1}r_m^3
=\frac27L^7-\frac15L^5+\frac16L^3-\frac1{420}L.}
\]
It equals \(1/4\) at \(L=1\) and has increment
\(2(L^2+L+\tfrac12)^3\), proving the formula by induction.
The original printed version with \(-L^5/10-43L/420\) was reported:
it gives \(69/2\) at \(L=2\) instead of the correct \(63/2\).
The corrected formula above was subsequently observed in the source.
This was a local displayed-moment typo; the source's final error
polynomial was already correct.

The sixth moment is
\[
\sum_{m=-L}^{L}m^6
=\frac{L(L+1)(2L+1)(3L^4+6L^3-3L+1)}{21},
\]
proved by value 2 at \(L=1\) and increment \(2(L+1)^6\).
Substitution yields exactly
\[
\mathcal E_L=\frac{L^2(2L+1)}{315}
(240L^6+360L^5+156L^4-120L^3-10L^2+40L-1).
\]
An independent symbolic summation returned this same polynomial.
The simpler bound follows without a signed-coefficient estimate:
\(r_m\leq L^2\) on the first range, and \(m^6\leq L^6\) on the
second. Thus
\[
\mathcal E_L\leq\frac{16}{3}L^8(2L+1)\leq16L^9
\quad(L\geq1).
\]
It follows that the claimed explicit remainder, with its sign, is
\[
0\leq\mathcal A_L\theta^4-\mathcal D_L(\theta)
\leq16L^9|\theta|^6 .
\]

## 5. Original cusp coefficient, limits and physical constants

The retained-cusp source fixes \(T_j=j^2\), real cover \(M_j=j\),
\(a_j=1/(100j)\) and \(2L_j=2j^2\). Thus the spatial side of the
open box is \(2L_ja_j=j/50\). The original retained geometry supplies
\(D_j^{\rm geom}=j^4(1+O(j^{-2}))\); this is the same determinant
and nonwrapping physical patch used by the coordinate/gauge proof
in the projection audit, not a new face count or coordinate scaling.
With \(C=2\pi/10^4\),
\[
\theta_j=\frac{2\pi a_j^2}{D_j^{\rm geom}}
=Cj^{-6}(1+O(j^{-2})),\qquad
|\theta_j|(L_j+1)=O(j^{-4}).
\]
The full polynomial above gives
\(\mathcal A_{j^2}=(16/5)j^{14}(1+O(j^{-2}))\).
The signed remainder gives the explicit estimate
\[
0\leq j^{10}
(\mathcal A_{j^2}\theta_j^4-\mathcal D_{j^2}(\theta_j))
\leq16j^{28}|\theta_j|^6=O(j^{-8}).
\]
The leading product has
\[
j^{10}\mathcal A_{j^2}\theta_j^4
=\frac{16}{5}C^4(1+O(j^{-2})).
\]
Squeezing proves the coefficient limit
\[
\lim_{j\to\infty}j^{10}\mathcal D_{j^2}(\theta_j)
=\frac{16}{5}\left(\frac{2\pi}{10^4}\right)^4.
\]
At each finite box the already-proved true-vacuum limit is
\(\lim_{\xi\downarrow0}\|\chi_{\xi,\theta_j}\|^2/\xi^2
=\mathcal D_{j^2}(\theta_j)/9\).
This gives the sequential coefficient \(16C^4/45\) exactly, with
the quantum limit inside the geometric limit as printed.

The number of faces is \(12j^4(2j^2+1)\), so the guaranteed
spectral-projection disk becomes exactly
\[
|\xi|<\frac1{64j^4(2j^2+1)}\sim\frac1{128j^6}.
\]
In the original physical variables at fixed \(g_{\rm YM}>0\),
\[
\kappa_j=200g_{\rm YM}^2j,\quad
b_j=50j/g_{\rm YM}^2,\quad
\xi_j=1/(4g_{\rm YM}^4),\quad
3\kappa_j=600g_{\rm YM}^2j .
\]
The fixed ratio eventually lies outside that sufficient local disk;
this does not assert failure of analyticity beyond the guaranteed
disk. Along this sequence the source correctly makes only the
explicit coefficient and sequential-limit claims. It neither uses
box-dependent remainders as uniform nor infers a fixed-coupling
growing-box quantum quotient from the formal leading coefficient.

## 6. Independent execution coverage

The entire companion source, including the appended Sections 7--10,
was read. The complete checker was read and replayed after its
sixth-order extension. It passed four exact 256-term full vertex
twirls, including noncommuting rational assignments, shared-source
cancellation and the false background-holonomy rule. It also passed
the exact complete-box sums, Fourier forms and exceptional-angle
values, both leading polynomials, and every face of the central
coupling-parity cochain for \(L=2,\ldots,7\), followed by the sixth
moment/error polynomial and diagonal spectral-radius checks.

Independently, symbolic summation verified both \(\mathcal A_L\)
and \(\mathcal E_L\) as polynomial identities. Substitution \(L=r+2\)
made every coefficient of \(16L^9-\mathcal E_L\) strictly positive,
providing a second exact check of the printed error constant.
The source's elementary bound proves the stronger all-\(L\geq1\)
statement directly. None of these checks samples an interacting
vacuum or replaces the analytic/operator proofs.

## 7. Delivery record

Audited companion SHA-256 after its cubic-moment correction:
8de2aec54478e807268afa9e87bc3e75ac602209cd39062d8eb6111432271fb8.

Final companion SHA-256 after the analyticity sentence correction:
e3aaac7862dc9ce2c0112e8773f896f6dd46efa2b6ca6660bebcfd9ae744544b.
Reverting only that sentence in memory reconstructs the previous hash
exactly, proving that no other unreviewed delta entered the final source.

The complete extended checker read and successfully replayed has SHA-256:
66e4109e78f51b2af02e7df3638be5ec82d9c7cf1d75572148d58553b195239e.

Final status: PASS. All mathematical coefficients, maps, domain arguments
and limits pass the bounded independent audit. Both reported corrections
were applied by the source owners and verified: the cubic-moment typo in
(7.10), and the squared-norm wording before (5.7). No mathematical issue
remains open in this bounded audit. This audit did not edit the proof
source, canonical material or remote publication.

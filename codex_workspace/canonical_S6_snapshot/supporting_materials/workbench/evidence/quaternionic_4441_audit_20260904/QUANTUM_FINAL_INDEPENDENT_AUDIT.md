# Independent final mathematical audit: homogeneous quantum confinement

Date: 4 September 2026. This is an independent audit of the assembled source, not approval inferred from an earlier report. No canonical source, remote state, TeX build, or Lean state was changed.

## Verdict and exact audited objects

No substantive mathematical gap or coefficient error was found in the theorem actually stated: for the specified thirty-eight-dimensional homogeneous mechanics, with

\[
\mathcal V_3>0,\quad g^2>0,\quad\hbar>0,\quad\Gamma>0,
\qquad m^2\geq0,\quad\kappa\in\mathbb R,
\]

the defined Friedrichs Hamiltonian has compact resolvent, has a simple strictly positive ground state invariant under spatially constant \(SU(3)\), and its restriction to the constant-group invariant Hilbert space has a strictly positive first excitation gap. No numerical value of that gap, no parameter-uniform gap, and no continuum mass-gap theorem follows or is claimed.

Read completely:

- `output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/homogeneous_quantum_confinement.tex`, 1,231 lines in the audited snapshot, SHA256 `1ed27ebfcb8e4c67d00a64cb998fc6ce5e20e5c0387150cb9a8ca26a9868cb0f`.
- `output/s6_consolidated_canonical_2026-08-26/s6_homogeneous_quantum_confinement.tex`, SHA256 `60e2a87fb4738c4a72812dc1b7f9b9b2a9c6e51bd7ba483fa728bd71a176c75e`.

The standalone root is under the canonical output directory, not directly under the workspace root. It inputs the audited chapter and its abstract preserves the theorem's finite-model scope. Line references below refer to the chapter snapshot identified by its hash.

The earlier `QUANTUM_INDEPENDENT_REVIEW.md` and `QUANTUM_HAMILTONIAN_REVIEW.md` were consulted only after the independent derivations below. The former's integration concerns are resolved in the assembled source: all parameter hypotheses, the full potential, the full closed form and its core, and the coercive resolvent shift are now explicitly present.

## 1. Original metric, momenta, coefficients, and Gauss signs

The original configuration space is

\[
\mathcal Q=\mathfrak{su}(3)^3\oplus\operatorname{Herm}_3(\mathbb C)_0
\oplus\mathbb C^3,
\qquad\dim_{\mathbb R}\mathcal Q=24+8+6=38.
\]

With \(b=x+iy\), the kinetic Lagrangian is

\[
\frac{\mathcal V_3}{g^2}\sum_i\|E_i\|^2
+\frac{\mathcal V_3}{2}\operatorname{tr}X^2
+\mathcal V_3(v^*v).
\]

Using the exact canonical one-form stated in the source gives

\[
\Pi_i=\frac{2\mathcal V_3}{g^2}E_i,\qquad
\Pi_\Phi=\mathcal V_3X,\qquad \pi_b=\mathcal V_3v.
\]

The last identity follows because both the differential of \(v^*v\) and the canonical complex pairing contain \(2\operatorname{Re}\). In real triplet coordinates, \(p_x=2\operatorname{Re}\pi_b\), \(p_y=2\operatorname{Im}\pi_b\). Consequently \(\pi_b=(p_x+ip_y)/2\), and quantization gives

\[
\widehat\pi_b=-\frac{i\hbar}{2}(\partial_x+i\partial_y),\qquad
\widehat\pi_b^*\widehat\pi_b=-\frac{\hbar^2}{4}
(\partial_x^2+\partial_y^2).
\]

The three kinetic coefficients in lines 173–175 are therefore exactly

\[
\frac{\hbar^2g^2}{4\mathcal V_3},\qquad
\frac{\hbar^2}{2\mathcal V_3},\qquad
\frac{\hbar^2}{4\mathcal V_3}.
\]

The mass determinant is checked block by block:

\[
\sqrt{\det M}
=\left(\frac{2\mathcal V_3}{g^2}\right)^{12}
 \mathcal V_3^4(2\mathcal V_3)^3
=\frac{2^{15}\mathcal V_3^{19}}{(g^2)^{12}}=C_M.
\]

For the Gauss map, cyclicity and anti-Hermiticity yield the exact pairings

\[
\begin{aligned}
-\operatorname{tr}(\Pi_i[\xi,A_i])
 &=-\operatorname{tr}([A_i,\Pi_i]\xi),\\
\operatorname{tr}(\Pi_\Phi[\xi,\Phi])
 &=\operatorname{tr}([\Phi,\Pi_\Phi]\xi),\\
2\operatorname{Re}(\pi_b^*\xi b)
 &=\operatorname{tr}((b\pi_b^*-\pi_b b^*)\xi).
\end{aligned}
\]

Thus the source's matrix expression

\[
\mathcal G=\sum_i[A_i,\Pi_i]-[\Phi,\Pi_\Phi]
 -(b\pi_b^*-\pi_b b^*)_{\mathrm{tf}}
\]

is precisely the element paired against \(\xi\) by \(-\operatorname{tr}\). The trace-free projection is necessary on the triplet term and harmless on the already trace-free commutators. Substitution of the momenta reproduces the stated \(\mathcal V_3\)-weighted homogeneous Gauss equation. Since ordinary velocity equals covariant velocity minus \(K_{A_0}\), the Legendre transform has \(H_{A_0}=H_0-\mathcal M_{A_0}\), with the displayed minus sign.

For a linear left action, the first-order differential fields satisfy
\([K_\xi\cdot\nabla,K_\eta\cdot\nabla]=-K_{[\xi,\eta]}\cdot\nabla\).
Multiplying by \((-i\hbar)^2\) gives the source's quantum sign

\[
[\widehat{\mathcal M}_\xi,\widehat{\mathcal M}_\eta]
=i\hbar\widehat{\mathcal M}_{[\xi,\eta]}.
\]

Differentiating \(\psi(R_{e^{-t\xi}}q)\) gives \(-K_\xi\cdot\nabla\psi\), which is also the derivative of \(e^{-it\widehat{\mathcal M}_\xi/\hbar}\psi\). The classical bracket \(\{p\cdot K_\xi,p\cdot K_\eta\}=p\cdot K_{[\xi,\eta]}\) is consistent with both signs.

## 2. Sharp scalar estimate and the exact negative constant

Let the eigenvalues of the original traceless Hermitian \(\Phi\) be \(\lambda_1,\lambda_2,\lambda_3\), and transform \(b\) by the same unitary. This preserves the original \(s\) and \(N\), where

\[
s=\operatorname{tr}\Phi^2+2b^*b,\qquad
N=\det\Phi-b^*\Phi b.
\]

For \(u=\sum_i|b_i|^2>0\), \(N\) is the convex combination with weights \(|b_i|^2/u\) of \(\lambda_1\lambda_2\lambda_3-u\lambda_i\). For the complementary indices \(j,k\), put \(d_i=\lambda_j-\lambda_k\). The trace-zero identity gives

\[
\lambda_j\lambda_k=\frac{\lambda_i^2-d_i^2}{4},\qquad
s=\frac{3\lambda_i^2+d_i^2}{2}+2u.
\]

It follows, with no term removed, that

\[
\lambda_1\lambda_2\lambda_3-u\lambda_i
=\lambda_i^3-\frac{s\lambda_i}{2},\qquad
|\lambda_i|\leq\sqrt{2s/3}.
\]

When \(u=0\), the same expression is \(N\) for each \(i\). When \(s=0\), both original fields vanish. For \(s>0\), all possible extrema of \(x^3-sx/2\) on the indicated closed interval occur at \(x=\pm\sqrt{s/6}\) or \(x=\pm\sqrt{2s/3}\). Direct substitution gives absolute value \(s^{3/2}/(3\sqrt6)\) at all four points. The triangle inequality for the convex combination proves

\[
|N|\leq\frac{s^{3/2}}{3\sqrt6}.
\]

For \(\Phi=\operatorname{diag}(2r,-r,-r)\), \(b=0\), \(r\ne0\), one has \(s=6r^2\), \(N=2r^3\), so equality holds. The coefficient is genuinely sharp on the full original state space.

Set \(\alpha=|\kappa|/(3\sqrt6)\) and \(t=\sqrt s\). The exact remainder after retaining \(\Gamma s^2/8\) is bounded below by \(\Gamma t^4/8-\alpha t^3\). Its derivative is \(t^2(\Gamma t/2-3\alpha)\). For \(\alpha>0\), its global minimum on \([0,\infty)\) is at \(t=6\alpha/\Gamma\), with value

\[
-\frac{54\alpha^4}{\Gamma^3}
=-\frac{\kappa^4}{54\Gamma^3}.
\]

For \(\alpha=0\), the remainder is nonnegative. Since \(m^2s/2\geq0\), the claimed bound

\[
V\geq\frac{\Gamma s^2}{8}-C_\kappa,
\qquad C_\kappa=\frac{\kappa^4}{54\Gamma^3}
\]

holds for both signs of \(\kappa\), including \(\kappa=0\). Multiplication by the retained volume gives \(C=\mathcal V_3C_\kappa\), not \(C_\kappa\), for the Hamiltonian shift.

## 3. Root frequencies, root walls, and exact directed allocation

In the original \(-\operatorname{tr}\) metric, the source's orthonormal pair \(U_{pq},V_{pq}\) is rotated by \(\operatorname{ad}_X\) with frequency \(\theta_p-\theta_q\), where \(X=i\operatorname{diag}(\theta_1,\theta_2,\theta_3)\). Thus the three root pairs each have two real frequencies, and the two Cartan coordinates have frequency zero:

\[
\mathcal S(X)=\operatorname{tr}_{\mathbb R\mathfrak{su}(3)}
\sqrt{-\operatorname{ad}_X^2}
=2\sum_{p<q}|\theta_p-\theta_q|.
\]

For ordered eigenvalues define \(r=\theta_2-\theta_1\geq0\), \(s=\theta_3-\theta_2\geq0\), only within this root calculation. The inverse expressions retained in the source give

\[
\|X\|^2=\frac23(r^2+rs+s^2),\qquad \mathcal S(X)=4(r+s).
\]

Hence

\[
\mathcal S(X)^2-24\|X\|^2=16rs,\qquad
32\|X\|^2-\mathcal S(X)^2=\frac{16}{3}(r-s)^2.
\]

Both sharp constants and all equality cases in the lemma follow. At a nonzero repeated-eigenvalue wall, four real positive frequencies remain; no positive frequency is invented for a commuting coordinate.

For one real coordinate the square-completion identity is

\[
\|\sqrt\alpha f'+\sqrt\beta\,\omega y f\|_2^2
=\alpha\|f'\|_2^2+\beta\omega^2\|yf\|_2^2
-\sqrt{\alpha\beta}\,\omega\|f\|_2^2.
\]

Applying it in the eight real eigendirections yields the slice bound \(-\alpha\Delta_Y+\beta\|[X,Y]\|^2\geq\sqrt{\alpha\beta}\mathcal S(X)\). This operation is at fixed \(X\); no derivatives of an \(X\)-dependent diagonalizing frame enter.

In (MQ.9), for each directed pair \((i,j)\), \(i\ne j\), the coefficients are exactly

\[
\alpha=\frac{(1-\vartheta)a_g}{2},\qquad
\beta=\frac{b_g}{2}.
\]

Each derivative \(\nabla_{A_j}\) occurs twice, giving total \((1-\vartheta)a_g\). Each unordered potential occurs twice, giving total \(b_g\). Each fixed \(i\) has two partners, so its two oscillator lower bounds sum to \(\sqrt{(1-\vartheta)a_gb_g}\mathcal S(A_i)\). Therefore the exact resulting position coefficient is

\[
2\sqrt{6(1-\vartheta)a_gb_g}.
\]

There is no factor-of-two overcount. Under the exact canonical coefficient map

\[
a_g=\frac{\hbar^2g^2}{4\mathcal V_3},\quad
b_g=\frac{\mathcal V_3}{g^2},\quad a_gb_g=\frac{\hbar^2}{4},
\]

this coefficient becomes \(\hbar\sqrt{6(1-\vartheta)}\), as in the full form bound.

## 4. Additional absolute-energy estimate

The elementary one-dimensional estimate (MQ.14) is valid. For a compactly supported smooth \(f\) of unit \(L^2\) norm, write \(t=\|f'\|_2^2\), \(M=\int|x||f|^2>0\). Integrating \((|f|^2)'\) from the two ends of the real line and using Cauchy–Schwarz gives \(\|f\|_\infty^2\leq\sqrt t\). Since at least half the mass lies in \([-2M,2M]\),

\[
\frac12\leq4M\sqrt t,\qquad tM^2\geq\frac1{64}.
\]

Thus \(\alpha t+\gamma M\geq\alpha/(64M^2)+\gamma M\). The latter has minimum at \(M^3=\alpha/(32\gamma)\), giving \(3(\alpha\gamma^2)^{1/3}/2^{8/3}\). Homogeneity in the test function removes the unit-norm restriction, and form-core closure extends the estimate.

Using \(\|A_i\|\geq8^{-1/2}\sum_\nu|x_{i\nu}|\), the twenty-four one-dimensional factors have \(\alpha=a_g/2\), \(\gamma=\sqrt{3a_gb_g/2}\). Their total is exactly

\[
24\frac3{2^{8/3}}\left(\frac{3a_g^2b_g}{4}\right)^{1/3}
=9(3/2)^{1/3}a_g^{2/3}b_g^{1/3}
=9\left(\frac{3\hbar^4g^2}{32\mathcal V_3}\right)^{1/3}.
\]

This is an absolute-energy lower bound for the pure matrix Hamiltonian with its original energy origin. The source explicitly does not equate it with an excitation-gap bound. Adding the original scalar sector need not preserve positivity of the energy origin because its proved lower bound includes \(-\mathcal V_3C_\kappa\).

## 5. Closed form, full compactness, and retained coordinates

The full multiplication potential is the exact \(W=\mathcal V_3U\) in the source. Since \([A_i,\Phi]^*=[A_i,\Phi]\), its adjoint-gradient term has nonnegative squared trace. The triplet term is a squared norm. The scalar bound consequently implies that \(W+C\) is a continuous nonnegative polynomial.

The domain

\[
\mathscr D=H^1(\mathcal Q,d\mu_M)\cap
L^2(\mathcal Q,(W+C)d\mu_M)
\]

is complete in the shifted form norm: a Cauchy sequence converges in \(H^1\) and after multiplication by \(\sqrt{W+C}\), and an almost-everywhere convergent subsequence identifies the two limits. Cutoffs remove tails with derivative error bounded by a constant times \(R^{-2}\|u\|^2\); local mollification then converges because the potential is bounded on each fixed enlarged compact support. This proves the asserted compact-smooth form core. The Riesz construction with \(\mathfrak h+(C+1)\|\cdot\|^2\) is coercive. Testing against the form core and then using its density gives exactly the stated distributional operator domain. The source does not substitute a stronger unproved condition requiring \(Wu\) and \(\Delta u\) separately in \(L^2\).

For \(0<\eta<1\), the full lower bound retains positive derivatives in all coordinates and retains the positive weight

\[
W_\eta=\hbar\sqrt{6(1-\eta)}\sum_i\|A_i\|
+\frac{\mathcal V_3\Gamma}{8}s^2.
\]

In the stated product metric let \(r^2=\sum_i\|A_i\|^2+s\). For \(r\geq R\), either \(\sum_i\|A_i\|^2\geq R^2/2\), or \(s\geq R^2/2\). The resulting uniform tail weight is exactly

\[
w_R=\min\left\{\hbar\sqrt{3(1-\eta)}R,
\frac{\mathcal V_3\Gamma R^4}{32}\right\}\longrightarrow\infty.
\]

For \(\widetilde q=\mathfrak h+C\|\cdot\|^2\), the derivative coefficient in product-metric orthonormal coordinates is

\[
c_0=\min\left\{\frac{\eta\hbar^2g^2}{4\mathcal V_3},
\frac{\hbar^2}{2\mathcal V_3}\right\}>0.
\]

The second term is correct because the triplet factor \(2\,db^*db\) is in this metric; it is not the unweighted \((x,y)\) coordinate gradient. Thus

\[
\int_{r\geq R}|\psi|^2\,d\mu_M\leq\frac{\widetilde q[\psi]}{w_R},
\qquad\int|\nabla\psi|^2\,d\mu_M\leq\frac{\widetilde q[\psi]}{c_0}.
\]

The dimension-independent small-cube estimate is also correct. Writing \(P_j\) for averaging in coordinate \(j\), the summands \(P_1\cdots P_{j-1}(I-P_j)\psi\) are pairwise orthogonal. The one-dimensional variance estimate bounds their squared norms by \(h^2\|\partial_j\psi\|^2\), and averaging in previous coordinates contracts this derivative norm. Summing proves the claimed cube estimate with constant \(h^2\), not an omitted dimension factor.

The finite-rank approximation by means on cubes in \([-R,R]^{38}\), zero outside, therefore has squared error at most

\[
\widetilde q[\psi]\left(\frac{h^2}{c_0}+\frac1{w_R}\right).
\]

The cube complement is indeed contained in \(\{r\geq R\}\), in the metric-orthonormal coordinates being used. Bounded form-domain sets are uniformly approximated by bounded subsets of finite-dimensional spaces. They are consequently totally bounded in \(L^2\). This proves compact form-domain inclusion; composing it with the bounded Riesz map proves compactness of \((H+C+1)^{-1}\). Every commuting gauge direction and every scalar coordinate remains in this argument.

## 6. Gauss domains and the physical reducing space

The linear orthogonal action preserves both the mass measure and the kinetic coefficients, as well as every original term of \(W\). Its fields have zero divergence. The unitary-generator domain is exactly

\[
\{\psi\in\mathscr H:K_\xi\cdot\nabla\psi\in\mathscr H
\text{ distributionally}\}.
\]

For the nontrivial direction, if the distributional derivative belongs to \(L^2\), integrating along the complete linear flow gives the source's Bochner identity, whose difference quotient converges by strong continuity. Radial cutoffs and radial convolution commute with the orthogonal flow and approximate both the function and its derivative. Thus compact smooth functions are a graph core, proving the essential self-adjointness asserted in lines 337–348.

The intersection of the eight closed kernels is precisely the invariant space: a vector in every kernel is invariant under every one-parameter subgroup, hence under connected \(SU(3)\); the converse follows by differentiating the constant orbit. Haar averaging divided by its retained mass is a self-adjoint idempotent with this range. Invariance of the closed form makes its Riesz resolvent commute with the group and with the averaging projection. The projection therefore reduces \(H\), so

\[
D(H_{\mathrm{phys}})=D(H)\cap\mathscr H_{\mathrm{phys}}
\]

is the correct self-adjoint restricted domain. Jensen's inequality for the positive shifted form proves averaging is form-bounded, giving the invariant compact-smooth core. Nonzero radial functions in pairwise disjoint annuli prove the physical space is infinite-dimensional. These are genuine nonzero \(L^2\) states; no singular quotient measure or orbit boundary condition is assumed.

## 7. Heat kernel, positivity, simplicity, and the actual gap

The free kernel for \(-\nabla\cdot D\nabla\) in thirty-eight real coordinates is exactly

\[
p_\tau(q,r)=(4\pi\tau)^{-19}(\det D)^{-1/2}
\exp\left[-\frac{(q-r)^{\mathsf T}D^{-1}(q-r)}{4\tau}\right].
\]

The bridge covariance is supplied by \(\sqrt{2D}(B_s-(s/\tau)B_\tau)\), not \(\sqrt D\). Relative to the original measure \(C_M\,dq\), the potential kernel is consequently \(p_\tau/C_M\) times the bridge expectation. This division is required and is present. The source correctly retains physical Euclidean time \(\hbar\tau\).

The bounded truncations \(W_n=\min(W+C,n)\) suffice for the Duhamel construction, with ordered terms bounded by \((n\tau)^j/j!\). The resolvent passage is valid. To spell out the norm step in lines 991–1004, the resolvent equations give uniform \(H^1\) bounds. For each fixed \(k\), weak lower semicontinuity of the \(W_k\) form and \(n\geq k\) bound the limit's \(k\)-form. Taking the supremum over \(k\) puts the limit in \(\mathscr D\). On any compact support, \(W_n=W+C\) for sufficiently large \(n\), so compact tests identify the unique limiting resolvent solution \(u\). The energy identities then give

\[
\lambda\limsup_n\|u_n\|^2
\leq\operatorname{Re}\langle f,u\rangle-\mathfrak h_\infty[u]
=\lambda\|u\|^2.
\]

Weak lower semicontinuity gives the reverse inequality, proving strong \(L^2\) convergence. Strong semigroup convergence follows from the spectral calculus for these uniformly semibounded operators. Each continuous bridge path has bounded image, on which the polynomial potential is bounded. Dominated convergence of the bridge exponentials is justified by \(W\geq-C\). Restoring the shift contributes exactly \(e^{C\tau}\).

I also directly read Theorem 1.1 and its definitions in the local primary TeX `literature_primary/Simon_Feynman_Kac_1999_20260904/Simon_1999_math-ph_9907022v1.tex`, lines 69–107. It states the continuous bounded-below Brownian-bridge formula for \(-\tfrac12\Delta+V\); the source's \(\sqrt{2D}\) covariance and \(p_\tau\) are the correct retained-coefficient version. The main spectral proof is not relying on Simon's more general unbounded-semigroup theorem or on an unstated positivity hypothesis.

The pathwise exponential is strictly positive and bounded above by \(e^{C\tau}\), so \(K_\tau(q,r)>0\). The Gaussian upper bound supplies a valid \(L^2\) kernel action. Integration against any nonzero nonnegative \(L^2\) function proves positivity improvement. Restriction to the reducing invariant space preserves that conclusion for its positive cone.

The equality of spectral infima does not assume an eigenfunction. The orbit norm

\[
F(q)=\left(\mathcal V_\mu^{-1}
\int_{SU(3)}|f(R_{g^{-1}}q)|^2\,d\mu(g)\right)^{1/2}
\]

has \(\|F\|=\|f\|\). Differentiating the regularized Hilbert-space norm locally and applying Cauchy–Schwarz bounds its kinetic form by the orbit average of the original kinetic form. Invariance of \(W\) gives equality of the potential terms, first for the nonnegative weight \(W+C\), then after subtracting \(C\|f\|^2\). Form approximation yields \(F\in\mathscr D\) with \(\mathfrak h[F]\leq\mathfrak h[f]\). The variational principle proves equality of the full and physical infima.

If the bottom is an eigenvalue, the modulus of a real bottom eigenfunction has no larger kinetic form and has identical potential form and norm. The spectral lower bound forces it also to be a bottom eigenfunction. Positivity improvement makes this modulus strictly positive. A sign-changing bottom eigenfunction would satisfy the strict inequality

\[
|e^{-\tau H}u|<e^{-\tau H}|u|
\]

almost everywhere, because both its nonzero positive and negative parts are mapped to strictly positive functions. The eigenfunction identities contradict that inequality. Orthogonalization against a positive eigenfunction would produce such a sign-changing vector if the real bottom eigenspace had dimension above one. Reality of \(H\) then gives complex dimension one. Every group translate of the positive normalized eigenfunction is positive, normalized, and in this same line, so the proportionality factor must be one. The ground state is invariant, not merely a possibly nontrivial one-dimensional group representation.

Compactness now supplies the existence that the positivity theorem deliberately did not assume: the positive injective compact operator \((H+C+1)^{-1}\) has a positive maximal eigenvalue. The affine inverse relation supplies a bottom eigenvalue of \(H\). Its physical restriction is also compact and injective on an infinite-dimensional Hilbert space, so it has infinitely many positive eigenvalues tending to zero. The resulting physical energies have finite multiplicity, diverge to \(+\infty\), and start with the simple common ground energy. Hence

\[
E_0=E_0^{\mathrm{phys}}<E_1^{\mathrm{phys}},\qquad
E_1^{\mathrm{phys}}-E_0>0.
\]

This deduction proves precisely a strict spectral separation at each fixed allowed parameter tuple. It supplies no numerical estimate for the separation and makes no assertion that the ground energy itself must be positive.

## 8. Classical and Fourier claims: limited scope retained

The homogeneous action pullback and constant momentum-density map retain the factor \(\mathcal V_3\). Since the full Euler–Lagrange residuals of homogeneous fields are spatially constant, their vanishing against all homogeneous time-dependent variations forces their vanishing against arbitrary spacetime tests. This establishes the stated classical solution map, including the Gauss residual. The periodic diagonal gauge example maps zero connection to a nonzero homogeneous flat connection and cannot be reproduced by constant conjugation. The same gauge function sends the stated off-diagonal scalar to a nonconstant scalar, proving the precise orbit-space limitation without calling that loop topologically large in \(SU(3)\).

For the displayed two-coordinate Fourier truncation, direct integration gives

\[
\frac{\Gamma\mathcal V_3}{4}
\left(q^4+3q^2y^2+\frac38y^4\right),\qquad
\frac{\mathcal V_3}{2}\dot q^2+\frac{\mathcal V_3}{4}\dot y^2.
\]

Thus both the mixed coefficient and the unequal Fourier-mode masses are correct. A reducing product subspace with fixed nonzero \(\Omega\in L^2(dy)\) would preserve the operator domain. Applying its projection to compact smooth tensor products puts every \(f(q)\Omega(y)\), \(f\in C_c^\infty\), in the domain. Subtracting the separated \(q\)-term and integrating against two compact \(q\)-tests whose \(q^2\) averages differ isolates \(H_y\Omega\) and \(y^2\Omega\) as \(L^2\) functions. The orthogonal projection in the source is therefore legitimate. Its coefficient identity for arbitrary \(q\) forces \((y^2\Omega)_\perp=0\). A multiplication eigenfunction of \(y^2\) would be supported on a measure-zero level set, so no such nonzero \(L^2\) vector exists.

This proves the stated product-sector obstruction for the displayed interacting truncation. It is not a theorem ruling out every possible embedding, every discarded-mode ansatz, or every relation to a full quantum field theory. The source's closing scope paragraph correctly avoids those broader conclusions. The finite homogeneous spectral theorem does not depend on this ancillary obstruction.

## Audit limits and handoff

This report certifies only the mathematical statements and constants checked above in the identified source snapshot. It does not certify TeX rendering, bibliography-wide provenance, remote synchronization, the separate global \(S^6\) construction, or a continuum construction. The Simon 1983 matrix-discreteness attribution and the contextual Lüscher/Tong references were not separately re-audited against their complete primary texts in this bounded pass; none is used as a substitute for the explicit operator, compactness, or Gauss proofs inspected here.

No canonical correction is required for the stated finite-model compactness, physical-ground, or strict-gap theorem on the evidence of this audit.

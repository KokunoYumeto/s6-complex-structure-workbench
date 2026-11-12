# Full operator-word limit of the radial carrier algebra

8 September 2026. This proof extends the complete amplitude/time kernels
to products of the actual bounded operators, including real-time
evolution. It identifies the resulting operator algebra and its centre.
The original spatial lattice, gauge projection, physical time and
coupling coefficients are retained. This is the algebra of the specified
global radial observables; it is not an identification with the continuum
local Yang--Mills algebra.

## 1. Actual finite operators and their previously proved kernels

Keep \(j\ge2\), \(L_j=j^2\), \(a_j=1/(100j)\), and
\[
 H_j=\frac{2g_j^2}{a_j}\sum_eE_e+
 \frac1{2g_j^2a_j}\sum_p(2-\operatorname{tr}U_p),\qquad
 A_j=H_j-\mathcal E_j\ge0 .
 \tag{1}
\]
Every edge and contained face of the original open box occurs in (1).
The space is the full vertex-gauge-invariant product-Haar space.
The actual positive unit vacuum is \(\psi_j\), and
\(A_j\psi_j=0\). Its uniqueness is proved in the included finite-box
companion. In particular the entire kernel at each regulator is
\(\mathbb C\psi_j\).

The globally smooth physical chart function and multipliers are
\[
 Q_j=g_j^{-2}\chi(y)\frac{\sigma_j}{4}
       |(O^{\mathsf T}G^{-1/2}y)_{\nu_j}|^2,\quad
 B_j(\beta)=e^{i\beta Q_j},\quad
 \sigma_j=\sqrt8\sin\frac{\pi}{4j^2+2}.
 \tag{2}
\]
The cutoff extends the phase by zero outside the logarithm chart, hence
the exponential by one. The same real cutoff is used for every
amplitude. The original quotient kinetic tensor is \(G=TT^*\);
\(O\) diagonalizes \(G^{1/2}C^*CG^{1/2}\). Every \(B_j(\beta)\)
is unitary and exactly physical. Its product law is
\(B_j(\beta)B_j(\gamma)=B_j(\beta+\gamma)\).

Put \(k=3/2\), \(c=100\sqrt2\pi\) and
\[
 d\rho(q)=\frac{q^{k-1}e^{-q}}{\Gamma(k)}\,dq,\qquad q>0.
 \tag{3}
\]
The included amplitude/time proof constructs one positive dyadic
coupling sequence on which all compact-parameter finite-box kernel
tests converge. For the uncentered vectors
\[
 \phi_j(b,\alpha)=B_j(b\sqrt j+\alpha)\psi_j,
 \qquad b,\alpha\in\mathbb R,
 \tag{4}
\]
its exact limit is
\[
 \lim_j\langle\phi_j(b,\alpha),e^{-tA_j}\phi_j(d,\delta)\rangle
 =\mathbf1_{\{b=d\}}
  [1+cb^2t+i(\alpha-\delta)]^{-k},\qquad t\ge0 .
 \tag{5}
\]
This includes \(b=d=0\); it does not discard the origin modulations.
The original finite comparison denominator is
\[
 1+(b\sqrt j+\alpha)(d\sqrt j+\delta)
       (1-e^{-t\lambda_j})
       +i\{(b-d)\sqrt j+\alpha-\delta\},
 \quad
 \lambda_j=400\sqrt2j\sin\frac{\pi}{4j^2+2}.
 \tag{6}
\]
Its inverse \(k\)-th power, with the branch proved in that companion,
gives (5), because \(j\lambda_j\to c\).
The actual positive-\(g\) estimates, including compact-uniform
spectral cutoffs, are part of that proof; (6) is not substituted for an
actual finite-coupling kernel.

## 2. Common dense vectors and the exact limiting operators

Let
\[
 \mathcal H=\bigoplus_{b\in\mathbb R}L^2(\rho),\qquad
 \phi(b,\alpha)_d(q)=\mathbf1_{\{d=b\}}e^{i\alpha q}.
 \tag{7}
\]
Its vacuum vector is \(\Omega=\phi(0,0)\).
The finite span \(\mathcal D\) of these vectors is dense: finite
label support is dense in a Hilbert direct sum, and exponentials are
total in \(L^2(\rho)\). For the latter assertion, orthogonality gives a
finite density with vanishing Fourier transform. Convolution with
Gaussians, followed by their \(L^1\) approximation to the identity,
forces that density to vanish. This establishes density without
assuming a spatial interpretation for either label.

Define \(J_j:\mathcal D\to\mathcal H_j\) by
\(J_j\phi(b,\alpha)=\phi_j(b,\alpha)\), extended linearly.
This definition is unambiguous. For each fixed \(b\), finitely many
distinct exponentials are linearly independent on \(q>0\): a vanishing
finite exponential sum is analytic and all its derivatives at any
point vanish; the resulting Vandermonde matrix has nonzero determinant.
Different \(b\) fibres are independent by the direct sum.
Equation (5) at zero time proves
\[
 \langle J_jv,J_jw\rangle\longrightarrow\langle v,w\rangle
 \qquad(v,w\in\mathcal D).
 \tag{8}
\]
No unit-norm adjustment is made to \(J_jv\).

The limit Hamiltonian is maximal multiplication
\[
 (Hf)_b(q)=cb^2qf_b(q),\quad
 \operatorname{Dom}H=
 \left\{f:\sum_b c^2b^4\int q^2|f_b|^2d\rho<\infty\right\}.
 \tag{9}
\]
Its nonreal resolvents are multiplication by \((cb^2q-z)^{-1}\),
bounded uniformly by \(1/|\operatorname{Im}z|\). The adjoint has
the same maximal domain, so \(H\) is self-adjoint and nonnegative.
Every vector has at most countably many nonzero fibres, since for
every positive integer \(n\) only finitely many have squared norm
at least \(1/n\). Thus sums and dominated-convergence arguments
below apply to each vector even though the full label set is uncountable.

Define the bounded operators
\[
 \begin{split}
 (U(a)f)_b(q)&=f_{b-a}(q),&
 U_j(a)&=B_j(a\sqrt j),\\
 (V(\eta)f)_b(q)&=e^{i\eta q}f_b(q),&
 V_j(\eta)&=B_j(\eta),\\
 S(t)&=e^{-tH},&
 S_j(t)&=e^{-tA_j}\quad(t\ge0).
 \end{split}
 \tag{10}
\]
The two multiplier correspondences hold exactly on the representing
vectors:
\[
 U_j(a)J_jv=J_jU(a)v,\qquad
 V_j(\eta)J_jv=J_jV(\eta)v,\qquad v\in\mathcal D.
 \tag{11}
\]
All \(U,V\) and their actual versions are unitary; all \(S,S_j\)
are contractions. Also \(U\) and \(V\) commute, as do their finite
versions. This does not assert commutation with \(S\).

## 3. Strong convergence across the different Hilbert spaces

Here is the precise notion used for products. Say \(\xi_j\to\xi\)
strongly in the \(J\) sense if for every \(\varepsilon>0\) there is
\(v\in\mathcal D\) with
\[
 \|\xi-v\|<\varepsilon,\qquad
 \limsup_j\|\xi_j-J_jv\|<\varepsilon .
 \tag{12}
\]
Allowing a fixed larger multiple of \(\varepsilon\) gives the same
definition by replacing \(\varepsilon\). This convergence implies
convergence of norms and of pairwise scalar products, by (8) and
approximation with the same finite vectors.

A useful sufficient test is
\[
 \|\xi_j\|\to\|\xi\|,\qquad
 \langle J_jv,\xi_j\rangle\to\langle v,\xi\rangle
 \quad\hbox{for every }v\in\mathcal D.
 \tag{13}
\]
Indeed expansion of the squared difference gives
\(\|\xi_j-J_jv\|^2\to\|\xi-v\|^2\); density then proves (12).

For \(w\in\mathcal D\), (5) and finite linearity give
\[
 \langle J_jv,S_j(t)J_jw\rangle\to\langle v,S(t)w\rangle .
 \tag{14}
\]
The norm is supplied by the same kernel at twice the time:
\[
 \|S_j(t)J_jw\|^2
 =\langle J_jw,S_j(2t)J_jw\rangle
 \longrightarrow
 \langle w,S(2t)w\rangle=\|S(t)w\|^2 .
 \tag{15}
\]
Equations (13)--(15) prove strong \(J\)-convergence of
\(S_j(t)J_jw\) to \(S(t)w\). This output-norm step is essential;
scalar two-point convergence alone would not justify products.

More generally suppose \(\|T_j\|,\|T\|\le C\) and
\(T_jJ_jv\to Tv\) strongly in this sense for all \(v\in\mathcal D\).
If \(\xi_j\to\xi\), then \(T_j\xi_j\to T\xi\).
To prove it, choose \(v\) as in (12). The difference from
\(T_jJ_jv\) has limsup norm at most \(C\varepsilon\);
the latter sequence converges strongly to \(Tv\), and
\(\|T\xi-Tv\|\le C\varepsilon\). Approximate \(Tv\) by a member
of \(\mathcal D\) in the definition, then let \(\varepsilon\downarrow0\).
This is an actual bounded-operator continuity argument, not an
assumption that arbitrary regulator products converge.

Apply this lemma to (11), (14)--(15). Induction proves for any fixed
finite word \(T_j^{(m)}\cdots T_j^{(1)}\) in the operators (10)
and any \(w\in\mathcal D\),
\[
 T_j^{(m)}\cdots T_j^{(1)}J_jw
 \longrightarrow
 T^{(m)}\cdots T^{(1)}w
 \quad\hbox{strongly in the }J\hbox{ sense}.
 \tag{16}
\]
All coefficients, amplitudes and nonnegative times in the word are
retained. Pairwise inner products of any two such words therefore
converge as well, including words applied to \(\Omega\).

## 4. The same sequence also retains real time

For \(w\in\mathcal D\), let \(\mu_j^w\) be its actual raw spectral
measure for \(A_j\) on \(J_jw\), and let \(\mu^w\) be the spectral
measure for \(H\) on \(w\). Their masses converge by (8), and their
Laplace transforms converge by (14).

These facts imply tightness; it is not inferred from a moment bound.
For \(t,R>0\),
\[
 \mu_j^w([R,\infty))
 \le
 \frac{\mu_j^w([0,\infty))-\int e^{-t\omega}d\mu_j^w}
      {1-e^{-tR}} .
 \tag{17}
\]
The limiting numerator tends to zero as \(t\downarrow0\), since
\(S(t)w\to w\) by spectral dominated convergence. Choose such a
small fixed \(t\), then \(R\) large so the denominator is at least
\(1/2\). This controls the tail uniformly for all sufficiently large
\(j\). The finitely many omitted measures have their own vanishing
tails, proving tightness of the sequence.

Every weak subsequential limit has the stated Laplace transform.
Uniqueness can be seen by the change \(x=e^{-\omega}\): equality
at integer times gives equality of all polynomial moments on
\([0,1]\), after assigning zero mass at the added point zero.
Polynomial density determines the measure. Thus
\(\mu_j^w\Rightarrow\mu^w\) on \([0,\infty)\).
Complex polarization supplies the same conclusion for the mixed
measures of any \(v,w\in\mathcal D\).

In particular the bounded continuous tests \(e^{-is\omega}\)
give convergence of all real-time matrix elements, for every fixed
\(s\in\mathbb R\). The actual and limiting real-time groups are
unitary, so their output norms also converge. Criterion (13) proves
\[
 e^{-isA_j}J_jw\longrightarrow e^{-isH}w .
 \tag{18}
\]
The bounded-product argument now proves (16) for finite words also
containing real-time evolution. Neither (17) nor (18) asserts
convergence of unbounded energy moments or uniformity in time
intervals whose lengths diverge with the regulator.

## 5. Domains, shifts, and the retained energy relation

Let \(P\) be multiplication by the label \(b\), with domain
\(\sum_b b^2\|f_b\|^2<\infty\), and let \(Q\) be multiplication by
\(q\), with domain \(\sum_b\int q^2|f_b|^2d\rho<\infty\).
Their spectral projections commute. Formula (9) is the maximal
joint functional-calculus operator \(cQP^2\); it is not restricted
by first demanding both \(P^2f\) and \(Qf\) separately.
For example the entire origin fibre belongs to \(\operatorname{Dom}H\)
even if its vector is not in \(\operatorname{Dom}Q\).

The shifts preserve \(\operatorname{Dom}P\) and
\(\operatorname{Dom}Q\), and direct index substitution proves
\[
 U(a)^*PU(a)=P+aI,\qquad U(a)^*QU(a)=Q .
 \tag{19}
\]
For the energy they give the exact identity
\[
 U(a)^*HU(a)=cQ(P+aI)^2
 \tag{20}
\]
on the shifted maximal domain
\[
 \left\{f:\sum_b c^2(b+a)^4\int q^2|f_b|^2d\rho<\infty\right\}.
\]
A shift need not preserve \(\operatorname{Dom}H\): it can take an
arbitrary origin-fibre vector to a nonzero fibre, where a \(q^2\)
moment is required. On finite-label smooth compactly supported
functions of \(q>0\), all products and polynomial differences
implicit in (19)--(20) are well defined with their displayed signs.

The variable \(Q\) is central for the bounded generators: its bounded
spectral functions commute with \(U,V\) and both time evolutions.
This centrality is a statement about the calculated radial algebra,
not about the centre of all Yang--Mills observables.

## 6. The complete centre of the generated von Neumann algebra

Let \(\mathcal M\) be the von Neumann algebra generated by all the
bounded operators (10). Since \(q>0\) almost everywhere, spectral
dominated convergence in each countable-support vector proves
\[
 E_0=\operatorname*{s-lim}_{t\to\infty}S(t),
 \tag{21}
\]
where \(E_0\) is the projection onto the whole origin fibre.
Consequently \(E_b=U(b)E_0U(-b)\) belongs to \(\mathcal M\)
for every \(b\). The operator
\[
 E_bU(b-d)E_d
 \tag{22}
\]
identifies fibre \(d\) with fibre \(b\) by the identity on \(L^2(\rho)\)
and vanishes elsewhere. Thus all label matrix units occur with their
full infinite-dimensional \(q\) fibre.

Suppose \(T\) commutes with \(\mathcal M\). Commutation with every
\(E_b\) makes it fibre diagonal, \(T=\bigoplus_b T_b\).
Commutation with (22) forces \(T_b=T_d\) under the displayed
fibre identity. Write this common operator as \(T_*\).
Commutation with every \(V(\eta)\) forces \(T_*\) to commute with
all bounded spectral functions of \(Q\).
For completeness the latter functions are generated by the
exponentials: the spectral theorem, or uniqueness of their finite
Fourier measures applied to matrix elements, shows that an operator
commuting with every \(e^{i\eta Q}\) commutes with its spectral
projections. On the scalar space \(L^2(\rho)\), an operator commuting
with all multiplication projections is itself a multiplier.
Indeed \(h=T_*1\) satisfies \(T_*\mathbf1_E=h\mathbf1_E\).
The norm bound on every indicator gives \(|h|\le\|T_*\|\) almost
everywhere, and density of simple functions proves \(T_*=M_h\).

Conversely any common multiplier \(I\otimes M_h\),
\(h\in L^\infty(\rho)\), commutes with every generator. It also
belongs to \(\mathcal M\) as a bounded spectral function of \(Q\).
We have proved
\[
 \mathcal M'=\{I\otimes M_h:h\in L^\infty(\rho)\}
 \subset\mathcal M,\qquad
 Z(\mathcal M)=\mathcal M'
 \cong L^\infty(\rho).
 \tag{23}
\]
Here tensor notation is the exact unitary direct-sum map proved in
the polymer-representation companion; it does not require a
countability assumption on all possible labels.

Thus the Gamma coordinate survives as the complete centre of this
radial algebra. The proof supplies a relation to known nonregular
polymer kinematics rather than declaring that kinematics new.
The novel claim of scope here is the particular operator-word map
from the specified nonlinear regulators, with its retained
spectral measure and physical scale.

## 7. Infinite-time closure does not commute with the regulator limit

Equation (16) concerns fixed finite words. It does not imply
convergence of every operator in the von Neumann closure from
a naively corresponding regulator operator. There is an exact
example already in these sources.

Fix \(\alpha\ne0\) and form the actual centered origin vector
\[
 z_j=(B_j(\alpha)-\langle\psi_j,B_j(\alpha)\psi_j\rangle)\psi_j .
 \tag{24}
\]
It tends strongly in the \(J\) sense to
\[
 z=\phi(0,\alpha)-(1-i\alpha)^{-k}\Omega,\qquad
 \|z\|^2=1-(1+\alpha^2)^{-k}>0 .
\]
At each regulator, the infinite-time limit of \(S_j(t)\) is the
rank-one vacuum projection. It kills \(z_j\) exactly. In the
limiting representation \(z\) lies in the origin fibre, so
\(S(t)z=z\) for every \(t\), and \(E_0z=z\).
Consequently
\[
 \lim_j\lim_{t\to\infty}\|S_j(t)z_j\|^2=0,\qquad
 \lim_{t\to\infty}\lim_j\|S_j(t)z_j\|^2
       =1-(1+\alpha^2)^{-k}.
 \tag{25}
\]
Both orders are explicitly calculated; they cannot be interchanged.
This is also why the centre argument in (21)--(23), which concerns
the completed limiting algebra, must not be advertised as convergence
of the individual finite-volume vacuum projections.

## 8. Relation to local observables and the research target

The bounded spatial cylinder conclusion extends to all the operator
words already proved, including real-time conjugates. Here is the
additional argument. Use the common positive-coupling refinement
containing both the kernel tests and the vacuum flatness tests, and
the divisible coarse/fine sequence in the configuration companion.
For any fixed bounded continuous gauge-invariant coarse cylinder
\(F\), write \(F_j\) for its actual pullback. That companion proves
\[
 \|(F_j-F(I))\psi_j\|\longrightarrow0,\qquad
 \|F_j\|\le\|F\|_\infty.
 \tag{26}
\]
For \(v=\sum_{\ell=1}^n z_\ell\phi(b_\ell,\alpha_\ell)\in\mathcal D\),
the actual unit-modulus phases give the pointwise bound
\[
 |J_jv|\le\left(\sum_{\ell=1}^n|z_\ell|\right)\psi_j.
\]
Thus, without an amplitude or time bound on these fixed parameters,
\[
 \|(F_j-F(I))J_jv\|
 \le\left(\sum_{\ell=1}^n|z_\ell|\right)
          \|(F_j-F(I))\psi_j\|\longrightarrow0.
 \tag{27}
\]
The bounded-operator lemma of Section 3 applies with limiting operator
\(F(I)I\). It follows that all fixed finite mixed words containing
these cylinders, carrier shifts, modulations, and both time evolutions
converge strongly in the \(J\) sense. In particular, for every fixed
real \(s\) and \(v\in\mathcal D\),
\[
 e^{isA_j}F_j e^{-isA_j}J_jv
       \longrightarrow F(I)v.
 \tag{28}
\]
This proves the stated temporal action on the existing spatial
cylinders; it is not necessary to assume it as an additional limit.
Finite collections of coarse cylinders can be placed on a common
divisible grid by the least common multiple of their subdivision
indices. The factorial cofinal sequence in the companion then treats
every fixed such cylinder. No assertion for a continuously moving
regulator-dependent spatial support is hidden in this argument.

The configuration companion proves that on a compatible smaller
positive-coupling diagonal, unchanged bounded continuous local
gauge-invariant holonomies act by \(F(I)I\) on the radial time
orbits. The spatial companion separately proves that the actual
phase double-commutator observable \(jR_g\) tends to \(cQ\) on
weighted carrier time vectors, after explicitly adding weighted
tests to its dyadic selection. This realizes a nonconstant electric
observable in the centre (23), with full tail estimates; it does
not make that global selected-mode observable spatially local.

There remains no proved map from the full spatial local interacting
Yang--Mills algebra onto this radial algebra preserving the required
vacuum, field relations and spacetime dynamics. The positive
spectrum down to zero in the nonzero carrier fibres therefore
does not establish a counterexample for that target theory.
What is established is the complete bounded-word representation,
its real-time extension, its exact energy domains, its centre,
and its additional zero-energy fibre. Those results specify
concrete structures any proposed extension must calculate rather
than hide in a change of coordinates.

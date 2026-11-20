# Paper I mathematical audit, 19 November 2026

Checker: **GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited reasoning effort**. This is a further run in the same model family. No entry below is a different-family check. The pre-proof derivations were saved in `preproof_derivations.md` before the corresponding printed proofs were inspected. The new program `code/exact_paper_i.py` was written independently using only Python's standard library, exact rational coefficients and integer matrices; none of the older programs was read or replayed for this certificate.

## Result and exact extent

The two assigned high-risk lemmas pass the independent derivations and exact checks described below. The local origin and meridian computations used in `night:P2.2`, `night:P2.7` and `night:P2.9` agree with the fixed signs. The geometric no-filling proofs were read in full and checked step by step against their actual analytic hypotheses; that work is recorded as **targeted proof checking**, not as an independent re-proof of every analytic construction or every inherited determinant calculation. No counterexample or mathematical fault was found in the checked argument.

One definite repair is supplied for `inv:D4.5`: replace its reference to the open atlas question `inv:C3.8` by the established Green representative and Picard normalization `inv:C3.1`–`inv:C3.2`, and say **\(\bar\partial\)-closed** instead of the unqualified word “closed.” The operator used in its proof needs precisely \(\bar\partial G_\gamma=0\). This change removes an inaccurate dependency without changing the theorem.

The literal atlas-coefficient problem `inv:C3.8` and the local-norm period gate `ari:C.7.4` remain open. The partial derivations below improve the audit trail; they do not discharge either gate. No new conditional theorem is proposed.

The computation output records **16 passing checks**. The higher-family arithmetic sweep contains **42,892 admissible residue pairs with \(1\leq k,l\leq20\)**. This finite sweep supplements the written proof of the universal coprimality assertion; its bound is not silently removed.

## 1. The three actual Weierstrass models

### 1.1 Arithmetic and geometric equations

Write \(C=t^3(t-1)\), \(D=t^4(t-1)^2\), with \(t\neq0,1\). The two smooth pointed cubics in `I:weierstrass-comparison` are

\[
E_{\rm ar}: y^2=x^3-\tfrac34Cx+\tfrac14D,
\qquad E_{\rm geom}:Y^2=X^3-3CX+2D.
\]

The exact pointed isomorphism and inverse are

\[
\Phi(x,y)=(2x,-2\sqrt2\,y),\qquad
\Phi^{-1}(X,Y)=(X/2,-Y/(2\sqrt2)).
\]

Substitution proves the equation identity, and both maps extend over the unique point at infinity. The chosen section \((0,t^2(t-1)/2)\) maps to \((0,-\sqrt2t^2(t-1))\). With the invariant differentials \(\omega_{\rm ar}=dx/(2y)\) and \(\omega_{\rm geom}=dX/(2Y)\),

\[
\Phi^*\omega_{\rm geom}=-\omega_{\rm ar}/\sqrt2.
\]

Consequently the corresponding lattice map is \(z\mapsto\lambda z\), where \(\lambda=-1/\sqrt2\), and \(\Lambda_{\rm geom}=\lambda\Lambda_{\rm ar}\). Transporting both the period basis and the elliptic logarithm leaves \(\tau\) and \(z/\omega_1\) unchanged. Every term in

\[
\mathcal N(P)=\left|\frac{\theta_1(z/\omega_1,\tau)}{\eta_D(\tau)}\right|
\exp\left(-\pi\frac{\operatorname{Im}(z/\omega_1)^2}{\operatorname{Im}\tau}\right)
\]

therefore agrees under this exact identification. The proof does not compare untransported logarithm coordinates.

The discriminants are

\[
\Delta_{\rm ar}=27(C^3-D^2)=27t^8(t-1)^3,
\qquad \Delta_{\rm geom}=1728(C^3-D^2)=64\Delta_{\rm ar}.
\]

Putting \(a=-\sqrt2\), the Weierstrass coordinate change is \((x,y)\mapsto(a^2x,a^3y)\). The scaling of the division polynomial is \(a^{m^2-1}\), while that of the discriminant is \(a^{12}\). Their absolute factors cancel in the displayed division-norm formula. These statements were derived before reading the printed proof, then compared to it. The fresh program certifies the polynomial and discriminant identities.

### 1.2 The attached AC26 original, Remark 3.12, page 19

The original PDF was opened, its page 19 rendered and visually inspected. It gives the further cubic

\[
E_0:y_0^2=4x_0^3-3Cx_0-D,
\qquad P_0=(0,i\,t^2(t-1)).
\]

The minus sign on \(D\) was checked in the original image. The exact transport is

\[
E_0\longrightarrow E_{\rm ar},\quad
(x_0,y_0)\longmapsto(-x_0,y_0/(2i)),
\]

with inverse \((x,y)\mapsto(-x,2iy)\). Its composite to the geometric model is

\[
(x_0,y_0)\longmapsto(-2x_0,i\sqrt2\,y_0).
\]

It carries the displayed marked section to the section in the lemma. For \(\omega_0=dx_0/y_0\), the arithmetic pullback is \(-i\omega_0\), so the corresponding lattice transport is also explicit. The proposed TeX addition supplies this third model and its inverse; it makes the comparison to the authoritative original inspectable. It is an explanatory addition, not a refutation of the existing two-model lemma.

## 2. The monodromy fundamental set

The coordinates in `I:monodromy-fundamental-set` use

\[
g(B,x,t)=
\begin{pmatrix}1&0&0\\6x&B&0\\t&-x^tJ B&1\end{pmatrix},
\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Here the block sizes are \(1,2,1\). Multiplication is

\[
g(B,x,t)g(C,y,u)=g(BC,x+By,t+u-6x^tJBy).
\]

With \(Q(x)=x_1+x_2+x_1x_2\), the integral group is the kernel of

\[
t+6Q(x)-\alpha(B)\pmod {12},
\quad \alpha(S)=9,\quad\alpha(T)=1,\quad\alpha(-I)=6.
\]

Over \(\mathbf F_2\), \(Q\) vanishes just at the zero vector, hence is invariant under \(\mathrm{SL}_2(\mathbf F_2)\), and its polarization is \(x^tJy\). Those identities prove the character law. The exact code additionally exhausts all 96 relevant \(\mathbf F_2\) instances. The relations \(S^4=1\), \(S^2=(ST)^3\) map to zero in \(\mathbf Z/12\), as verified directly.

Use \(B=n(\operatorname{Re}\tau)a(\operatorname{Im}\tau)k(\theta)\). The proposed region is the classical modular region in \(\tau\), \(0\leq\theta<\pi\), \(0\leq x_1,x_2<1\), and \(0\leq t<12\), with its stated paired faces. A modular reduction by \(A\in\mathrm{SL}_2(\mathbf Z)\) is performed with the **actual lift** \(g(A,0,\widetilde\alpha(A))\in\Gamma\), acting by

\[
(B,x,t)\longmapsto(AB,Ax,t+\widetilde\alpha(A)).
\]

After this operation, an integral Heisenberg translation reduces \(x\) modulo \(\mathbf Z^2\), and the center reduces \(t\) modulo 12. This order of operations proves coverage. Interior uniqueness follows successively from modular uniqueness, the half-angle interval, the half-open \(x\)-square and the central interval. The paired modular boundaries and elliptic stabilizer strata use the displayed lifts; they have Haar measure zero. Thus the result is a fundamental set with its specified identifications, not a claim that the rectangular coordinates are unique at all boundary points.

The two positive faces act as

\[
U:(x_1,x_2,t)\mapsto(x_1+1,x_2,t-6-6x_2),
\quad
V:(x_1,x_2,t)\mapsto(x_1,x_2+1,t-6+6x_1).
\]

Their commutator is \([U,V]=Z^{-1}\) for \(Z:g\mapsto t+12\). The fresh matrix computation reproduces the commutator and the \(S,T,-I\) lift actions. The displayed figure uses these same signs. The local letter \(e\) and earlier letter \(d\) both denote \(\widehat\delta\); the identity map on the lattice identifies their stabilizers. No change of primitive vector or normalization occurs.

## 3. The two extending origins and the corner class

This part distinguishes the newly derived algebra from the extension arguments checked after reading. Let \(N=12\), or \(N=12kl\) in the higher case. Set

\[
s=\frac{\log q}{2\pi i},\quad v=\frac{\log r}{2\pi i},
\quad \gamma=(6\mu,C-s-Nv),\quad\delta=(0,1),
\quad a=b-Nl_0=-p.
\]

The cusp period lift is

\[
z_\gamma=(6s\mu,-s(s+1)/2+s(C-Nv)).
\]

Using the actual origins in `night:P2.2` and `night:P2.9` gives

\[
o=\binom{-6b\mu s/N}{bs^2/(2N)-bCs/N+l_0s/2+v(bs+U)},
\]

\[
\sigma=-l_0z_\gamma+
\binom{6a\mu v}{vU+aCv-Nav^2/2+Nav/2}.
\]

Their subtraction is exactly

\[
F=\sigma-o=a\binom{6\mu(s+Nv)/N}
{C(s+Nv)/N-(s+Nv)^2/(2N)+Nv/2}.
\]

The fresh polynomial code clears the common denominator \(N\) and checks this identity with the relation \(a=b-Nl_0\) substituted. It also checks, coefficient by coefficient,

\[
F(s+Nm,v)-F(s,v)=am\gamma-\tfrac N2am^2\delta,
\]

\[
F(s,v+n)-F(s,v)=an\gamma-\tfrac N2an(n-1)\delta.
\]

Thus the radial class in \(\Lambda/\mathbf Z\widehat\delta\) is \(-pn\widehat\gamma\). The quotient is free and \(p\neq0\), so the positive-sign alternative differs by the nonzero element \(2pn\widehat\gamma\). For the original \((l_0,l_1,l_2)=(0,1,-1)\), \(p=-1\), and the class is consequently \(+n\widehat\gamma\). The sign is fixed by the stated coordinates, rather than selected by a verbal convention.

For \(N=12\), the four descent identities in the printed proof were also expanded by hand. They are

\[
\Delta_{s,12}o=-b\gamma+6(b+l_0)\delta,\quad
\Delta_{v,1}o=H\delta,
\]
\[
\Delta_{s,12}\sigma=-12l_0\gamma+78l_0\delta,\quad
\Delta_{v,1}\sigma=H\delta+a\gamma.
\]

The subsequent extension uses the actual rank-one node charts \(X_iY_i=r\): a holomorphic unit multiplies \(X_i\) and \(Y_i\) inversely. The zero relative to \(o\) extends in the partial filling, and \(\sigma+l_0z_\gamma\) lies in the smooth toric open orbit at the cusp. This is the geometric scope checked in the printed proofs of `night:P2.2` and `night:P2.3`. The fresh algebra alone does not certify the quotient's analytic properness.

## 4. Scope of the no-filling verification

### 4.1 Recovering the marked base from an arbitrary proposed filling

The argument in `night:P2.4` begins with the reduced dominating component, resolves it while preserving the smooth punctured family, and uses the relative line bundle \(L=\omega_{Z/\Delta}^{-2}\). The identity \(K_{X_c}^{-2}=f^*\mathcal O(1)\) gives two sections on every noncentral fibre. Proper coherence makes \(p_*L\) coherent. Multiplication by the parameter is injective, so it is a free rank-two module over the disc's discrete valuation ring. Constant-dimension base change is used on the punctured disc, where the map is a submersion and \(L\) is flat. Evaluation gives the meromorphic pencil.

After resolving its graph, proper image of the critical locus yields the three labelled critical-value curves. Their normalizations are meromorphic sections of \(\mathbf P^1\) over the disc; their limiting values may coincide. The unique projective transformation sending the three distinct sections over the meromorphic germ field to \(0,1,\infty\) has meromorphic coefficients. This proves the needed marked-map extension with finite principal parts. It does not rely on extending an arbitrary punctured-disc map by an unproved graph-closure assertion.

The exact external statements were reopened: Bierstone–Milman Theorem 1.6, its analytic-neighborhood paragraph and condition (1); Grauert's proper direct-image coherence, proper image theorem and constant-cohomology base-change theorem. A smooth point of the original space lies outside the exceptional set, so the centers allowed after the strict transform becomes smooth do not alter the original smooth punctured family. The check concerns the applicability of these statements; it is not an independent proof of resolution or Grauert's theorem.

### 4.2 The horizontal normal-meridian class

The quotient group in `night:P2.6` is explicitly

\[
\big((\Lambda/\mathbf Z\widehat\delta)\rtimes\pi_1(B^\circ)\big)
\times\mathbf Z_R.
\]

The source proof tracks the parameter descent and each finite/collar cross-cocycle into \(\mathbf Z\delta\), so the splitting is taken in precisely this quotient. A positive normal meridian of a component dominating the base has class \((\lambda,e)\). Basing changes by fibre loops act by \(I-T_R^e\), which vanishes in the quotient.

Stein factorization of the proper map from the smooth compact divisor to the base, followed by removal of finitely many branch and critical values, produces a finite-index base subgroup represented by paths on that divisor. Loops can be moved away from the other divisors. Its monodromy orbit on \(\lambda\) is finite. In coordinates \((g,u,w)\), the three unipotent-kernel equations are

\[
u=0,\qquad 6g+w=0,\qquad-w=0.
\]

Their determinant has absolute value 6, so the rational common kernel is zero; the integral quotient lattice is free. The fresh exact matrix certificate verifies this determinant and kernel calculation.

### 4.3 Connectedness and the commuting ratio

The bidisc model after finite covers and principalization has connected fibres: its Stein finite factor is generically degree one, and a finite birational map to the normal bidisc is an isomorphism. The axis ideal becomes monomial by Bierstone–Milman Theorem 1.10; its two factors therefore have nonnegative monomial orders in a normal-crossing chart. The open torus family is unchanged.

In the actual origin splitting, the commuting lifts are

\[
Q_o=T_{-mb\widehat\gamma}Q,\quad R_o=R,
\quad A_Q=I-NmE_{32}+NmE_{41},\quad A_R=I+NnE_{41}.
\]

Their nilpotent products vanish. The \(\widehat\delta\) coordinate of the commutator of two local normal meridians gives

\[
(m\alpha_i+n\beta_i)\kappa_j
=(m\alpha_j+n\beta_j)\kappa_i.
\]

Each denominator is positive. A horizontal central component has ratio zero by the preceding argument. The strict cusp component has ratio \(a\), from the exact origin difference. Both meet the compact connected corner fibre. The finite closed cover by their intersections with the axis components has connected incidence graph, which propagates the ratio. Thus the contradiction is \(a=0\) against the actual admissibility arithmetic.

For \(m_1=3k\), \(m_2=4l\), \(N=m_1m_2\),

\[
a\equiv m_2l_1\pmod {m_1},\qquad
a\equiv m_1l_2\pmod {m_2}.
\]

Coprimality of \(m_1,m_2\) and primitivity of both \(l_j\) prove \(\gcd(a,N)=1\). This is the universal proof; the 42,892-case exact sweep is a bounded supplementary check.

### 4.4 Higher multiplicities and the remaining scope limit

The higher proof recovers the base from

\[
K_X^{-N}=f^*\mathcal O(d),\qquad d=4l+3k-kl\neq0.
\]

The displayed nonvanishing follows directly: \(d=0\) gives \(k\mid4l\); coprimality forces \(k=1\), which makes \(d=3l+3>0\). Choosing the positive-degree canonical or anticanonical power produces the rational normal curve over the field of meromorphic parameter germs. Its three labelled critical points give three rational points. The unique cross-ratio parameter descends to that field by uniqueness, yielding the marked map.

The original Viaclovsky root construction and finite quotient statements were opened and compared. In this run the determinant-order transport \(2,1\mapsto2k,l\) was checked against the displayed root pullbacks and the paper's formula; a new complete derivation of every tangent-chart determinant in the higher family was **not** completed. Accordingly `night:P2.9` receives a targeted-proof-check event with this precise scope, not a blanket independent re-proof. The polynomial origin transport and universal coprimality argument are separately certified.

## 5. Comparison with the attached literature

| Source and locator opened | Exact relationship used | Scope of the comparison |
|---|---|---|
| AC26 original PDF, Remark 3.12, p. 19 | The cubic map in §1.2 carries its pointed equation to the arithmetic and geometric equations; invariant differentials and lattices are transported explicitly. | Original PDF sign checked visually; no conclusion is taken from a conflicting transcription. |
| E26, Definition 2.3, p. 5, and the cubic on p. 3 | Exponentiating the second lattice coordinate gives \([\xi,\eta]\mapsto[\xi,e^{2\pi i\eta}]\); the remaining period acts by \((\xi,W)\mapsto(\xi+6\mu,e^{2\pi i\beta_c}W)\). Engel's generator is its inverse, with translation \(-6P\). | This is an explicit isomorphism of quotient presentations. It does not identify a logarithm with its exponential without the lattice quotient. |
| E26, Remark 8.1 and **Conjecture 8.2**, p. 22; the paragraph following it | E26 proposes the one-component central geometry and discusses logarithmic transforms. Paper I's `night:P2.10` constructs the two-bundle plumbing; `night:P2.11` checks the one-component proposal by its virtual Euler characteristic. | Conjecture 8.2 remains labelled a conjecture in the comparison. This audit does not describe E26 as proving that filling. The no-filling obstruction is checked on the actual logarithmically twisted datum and its integer \(a\). |
| E26, Remark 8.4, pp. 23–24 | The question concerning the maximal proper-action domain is compared with the exact \(q_d\neq0\) statement. | The remark was read; a global claim that no related work exists is not made. |
| DGKX attached v1/v2; v1 Theorems 1.3–1.4, p. 3, Theorem 6.12, pp. 81–82, and Theorem 6.16, p. 85 | The family parameter is related by \(a=c+\delta\), \(\delta=\beta_{\rm part}-\beta_0\), because both particular solutions differ by a constant. Then \(\Omega_a=\Pi_c\), \(a'-a=c'-c\), and the domains translate by \(\operatorname{Im}\delta\). | The dedicated credited insertion is owned by `audit_corrections/P5_7_insertion.tex`. Its affine transport was checked here. Do not replace it by \(a=c\) unless the particular solutions have actually been chosen equal. |
| Viaclovsky, Theorem 1.1, p. 1; Proposition 2.3, pp. 5–6 | The higher \((3k,4l)\) family and free finite root actions supply the precise admissible construction used by `night:P2.9`. | The attached construction and public primary PDF were opened. This supplies neither a proof of the new corner argument nor a claim that the higher family itself originates in this audit. |

Searches of primary-source indexes for the specific corner-filling, maximal-domain and local-norm claims did not locate an additional matching theorem during this run. That is a bounded search outcome, not an exhaustive novelty theorem. The search log records both useful retrievals and inaccessible version-specific DGKX URLs.

## 6. The atlas question and the precise dependency repair

### 6.1 What is proved in `inv:C3.8`

The settled harmonic normalization uses a nonzero functional on \(H^{1,1}_{\bar\partial}(X)\). For an orthonormal harmonic basis \(e_1,e_2\), put

\[
\ell(e)=-\frac1{12}\int_F i_F^*e\wedge\eta,
\qquad
Q=\frac{\sum_j\overline{\ell(e_j)}e_j}
{\sum_j|\ell(e_j)|^2}.
\]

The restriction map has image \(\mathbf C\eta\), kernel \(\mathbf C d_1g\), and \(\int_F\eta^2=-12\). Hence \(\ell\neq0\), the denominator is positive, and the Riesz-vector formula is basis independent with \(\ell(Q)=1\). This finite-dimensional calculation was derived before reading the proof.

The compendium's fibre calculation was also reopened. For \(y=\operatorname{Im}\tau\), \(m=\operatorname{Im}\mu\), \(r=\operatorname{Im}\beta\), \(\Delta=r-6m^2/y\), the explicit relative fibre representative is

\[
Q_F=\frac1{2iy\Delta}\big(r\,d\zeta_1\wedge d\bar\zeta_1
-6m\,d\zeta_1\wedge d\bar\zeta_2
-6m\,d\zeta_2\wedge d\bar\zeta_1
+6y\,d\zeta_2\wedge d\bar\zeta_2\big).
\]

Its square has coefficient \(3/(y\Delta)\) in the ordered complex volume form and its integral is \(-12\). Finite-root invariant bases and cusp logarithmic classes yield the relative class; the Leray argument supplies a global cohomology lift modulo \(d_1g\). They do not evaluate the literal smooth coefficient functions on all overlapping charts. The attempted route through a Čech correction would require explicit cochains cancelling the cusp logarithmic poles. Those cochains were not obtained in this run. The open row therefore stays open.

### 6.2 Repair of `inv:D4.5`

The family of operators there is integrable because

\[
(\bar\partial-2\pi izG_\gamma)^2=-2\pi iz\,\bar\partial G_\gamma=0.
\]

The established Green construction in `inv:C3.1` gives \(G_0=\alpha^{0,1}\) with \(\bar\partial G_0=0\), and `inv:C3.2` supplies the primitive normalization \(G_\gamma=G_0/12\). This suffices for the holomorphic family on \(X\times\mathbf C\) and for proper coherent base change. The open problem of evaluating all atlas coefficient functions is not needed.

The unqualified word “closed” should not be retained here. Indeed, a genuinely \(d\)-closed global \((0,1)\)-form on this \(S^6\) would be \(du\), since \(H^1_{\rm dR}(S^6)=0\). Its \((1,0)\)-part gives \(\partial u=0\), while its \((0,1)\)-part is \(\bar\partial u\); hence its Dolbeault class is zero. The chosen Picard generator has nonzero Dolbeault class. The exact required property is therefore \(\bar\partial\)-closedness. The supplied replacement changes the wording and dependency, not the cohomology formula.

## 7. The local-norm period gate

The complete existing `ari:C.7.1`–`ari:C.7.4` argument was read. The algebraic point \(P\) defines the extension \(G_P\) and its logarithm through

\[
f_u(z)=\frac{\sigma(z+u)}{\sigma(z)\sigma(u)}e^{-\zeta(u)z},
\quad \exp_{G_P}(z,v)=(\exp_Ez,e^v f_u(z)).
\]

The periods are \((0,2\pi i)\) and \((\omega_j,\zeta(u)\omega_j-\eta_ju)\). For a lift \(R=(P,r)\), the maximal-compact character equation gives the exact relation

\[
\chi(R)=\log|r|-\log|\wp'(u)|-2\log\mathcal N(P)
+\tfrac16\log|\Delta_E|.
\]

Thus the alleged algebraicity of the local norm is translated to an algebraic point in the specified compact fibre by the actual multiplicative scalar

\[
r=|\wp'(u)|\,|\Delta_E|^{-1/6}\mathcal N(P)^2.
\]

The printed relative-period argument includes the full periods of \(G_P\) and its conjugate, including \(\zeta(u)\omega_j-\eta_ju\). Legendre inversion therefore places \(u\), \(\zeta(u)\) and their conjugates in the stated base field; it is not permissible to discard these third-kind periods when counting transcendence degree.

The attached Bertolin–Philippon–Saha–Saha primary source was reopened at Construction 3.4, Lemma 3.5, Conjecture 4.7, Proposition 4.12 and Remark 4.13. Its relative inequality is explicitly a conjecture. The diagonal case \(P=Q\) in Remark 4.13 identifies the two period fields through isogeny and leaves the central dimension in the lower bound. This is the external gate used in the existing argument. No unconditional substitute was found.

One additional primary source was opened: Jones–Schmidt, *A Manin–Mumford theorem for the maximal compact subgroup of a universal vectorial extension of a product of elliptic curves*, Theorem 1.1 and §2. Its statement concerns universal **vectorial** extensions and contains a strong algebraic-point restriction. The specific proposed transfer by pushout along \(\mathbf G_a\to\mathbf G_m\) cannot produce the extension \(G_P\): an algebraic morphism \(\mathbf A^1\to\mathbf G_m\) is an invertible polynomial, hence constant; a group morphism is therefore the constant identity. Its pushout extension is split, whereas the extension class of \(G_P\) is the nonzero point \(P\in E^\vee\). This proves the limitation of that exact pushout route. It makes no assertion excluding other mathematical relations or methods.

The search and this explicit comparison do not reduce the open gate. The atlas and period rows retain their previous status, and no check event is recorded as a proof of either requested open conclusion.

## 8. Files and integration

- `preproof_derivations.md`: the pre-proof working derivations and their explicit limits.
- `code/exact_paper_i.py` and `code/exact_paper_i.out.json`: independently written exact computations and complete result metadata.
- `patches.json`: exact replacements and insertion anchors; these are not applied to the shared paper by this agent.
- `paper_i_comparison_addition.tex`: the original-AC cubic paragraph, ready for insertion inside the Weierstrass proof.
- `events.tsv`: label-specific actual events with precise scope and no inflated checking provenance.
- `sources_and_searches.md`: opened primary locators, source-access limitations and bounded literature-search record.
- `frontmatter_I.tex` and `main_index_I.json`: the requested seven-main-theorem frontmatter and outline/target index; it reorganizes established body statements and does not upgrade any unchecked body statement's verification status.

The temporary AC text extraction and original-page rendering are inspection files only. They should be excluded from deliverable and checkpoint archives because the authoritative original is already in the attached source bundle.

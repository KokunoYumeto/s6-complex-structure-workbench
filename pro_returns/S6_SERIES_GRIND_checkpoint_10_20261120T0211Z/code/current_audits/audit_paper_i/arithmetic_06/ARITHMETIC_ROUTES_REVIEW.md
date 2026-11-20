# Exact additional routes for the diagonal arithmetic period

**The unconditional assertion at `ari:C.7.4` remains open.** This continuation closes two specific attempted transports and verifies the concrete CM input by fresh exact code. It does not assert a new conditional theorem, an unconditional norm-transcendence result, or an exhaustive obstruction to every possible method.

Author: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family.
Phase: `S6_SERIES_GRIND`, 2026-11-19.

## 1. Actual input and exposure

The target is the real point

\[
 E:y^2+y=x^3-38x+90,
 \qquad Q=(4,-2)=2(0,9),
 \qquad \beta^2=-19.
\]

The algebraic differential is \(dx/(2y+1)\). With the positive real period \(\omega_1\), the actual logarithm satisfies \(0<u<\omega_1/2\), \(\wp(u)=4\), and \(\wp'(u)=-3\). The extension is the original \(G_Q\), using the exponential

\[
 (z,v)\longmapsto
 \left(\exp_E z,e^v
 \frac{\sigma(z+u)}{\sigma(z)\sigma(u)}e^{-\zeta(u)z}\right).
\]

The actual positive compact lift has fibre coordinate
\(r=3\,19^{-1/2}N(Q)^2\) and logarithm \((u,v)\) with

\[
 v=\frac{u\kappa_1}{\omega_1},\qquad
 \kappa_j=\zeta(u)\omega_j-\eta_j u.
\]

These are the previously checked identities C7.1--2 and C7.9. They are retained without a gauge change. The proposed contradiction from algebraicity would make \([\mathbb Z\to G_Q]\), \(1\mapsto R_N\), a 1-motive over \(\overline{\mathbb Q}\). The following calculations test that proposed use of established period results; they do not assume the desired algebraicity as a new standing hypothesis.

The exposure boundary is recorded in `prereading_new_routes.md`. Before these new calculations, the agent had read C7.1--4, the current C7.6--12 statements, the full C7.9--10 arguments, and the final C7.12 arguments. Thus these are additional routes, not a blind reproof of those statements. The new exterior-square and general finite-CM-list derivations were written before this continuation opened the detailed Huber--Wuestholz source proofs. The symbolic programs were written after that source comparison and are recorded as fresh after-reading implementations.

## 2. Exact exterior-square calculation

Set \(t=2\pi i\), \(z=\zeta(u)\), and use the Legendre convention
\(\eta_1\omega_2-\eta_2\omega_1=t\). The period matrix in the ordered torus, elliptic, and lattice bases is

\[
 P=\begin{pmatrix}
 t&\kappa_1&\kappa_2&v\\
 0&\omega_1&\omega_2&u\\
 0&\eta_1&\eta_2&z\\
 0&0&0&1
 \end{pmatrix}.
\]

This is the actual elliptic 1-motive matrix of Huber--Wuestholz, section 11.1, author-preprint p.93, with the third-kind exponential signs fixed by C7.1. Their matrix is written in precisely the same torus-first order. The second-kind normalization is the one used in the attached Bertolin et al. generalized logarithm. An algebraic change of the second-kind differential changes that row by algebraic row operations and does not alter the first-two-row minor below.

Index the exterior basis by \(01,02,03,12,13,23\). Let \(C=\bigwedge^2P\), namely the matrix of all 2-by-2 minors. The compactness determinant is exactly

\[
 C_{01,13}=\kappa_1u-\omega_1v.
\]

This turns the product expression into an individual period entry of the exterior object. The full matrix and both basis orders are saved in `arithmetic_routes_exact.output.json`; no unnamed normalization is used.

The Betti weights of \(P\) are \((-2,-1,-1,0)\). Consequently the exterior weights, in the displayed order, are

\[
 (-3,-3,-2,-2,-1,-1).
\]

The actual Betti input \(e_1\wedge e_3\) maps to the nonzero vector \((1,0)\) in \(\operatorname{Gr}_{-1}^W\). It therefore does not belong to \(W_{-2}\). The actual de Rham row \(01\) is nonzero on \(W_{-3}\); it does not descend to the quotient by \(W_{-3}\). These are direct statements about the input and functional of this particular period.

Deligne's original Construction 10.1.3, pp.53--56, gives the allowed Hodge types of a 1-motive and its weight filtration. After twisting \(W_{-2}(\bigwedge^2M)\) by the inverse Tate object, the weights are \(-1,0\). The quotient \((\bigwedge^2M)/W_{-3}\), without that twist, has weights \(-2,-1\). Both are the natural places in this exterior construction to seek the required linear 1-period. The actual constant basis changes identify their period matrices and show exactly what happens to the central variable.

### 2.1 The lower-weight subobject

The first four rows and columns of \(C\), divided by \(t\), are

\[
 S=\begin{pmatrix}
 \omega_1&\omega_2&u&-u\\
 \eta_1&\eta_2&z&-z\\
 0&0&1&0\\
 0&0&0&-1
 \end{pmatrix}.
\]

The identities used here are literal Legendre inversions:

\[
 \kappa_1\omega_2-\kappa_2\omega_1=-tu,
 \qquad
 \kappa_1\eta_2-\kappa_2\eta_1=-tz.
\]

Multiply on the left and right by

\[
 L_S=\operatorname{diag}\!\left(I_2,
 \begin{pmatrix}1&1\\0&1\end{pmatrix}\right),\qquad
 R_S=\operatorname{diag}\!\left(I_2,
 \begin{pmatrix}1&-1\\0&-1\end{pmatrix}\right).
\]

Both matrices are integral and unimodular, and

\[
 L_SS R_S=
 \begin{pmatrix}
 \omega_1&\omega_2&u&0\\
 \eta_1&\eta_2&z&0\\
 0&0&1&0\\
 0&0&0&1
 \end{pmatrix}.
\]

This is the period matrix of the point motive \([\mathbb Z\to E]\), \(1\mapsto Q\), plus a trivial lattice summand. On the lattice, the split generator is the difference of the two copies of \(Q\). Every displayed entry is independent of \(v\).

### 2.2 The quotient by the lowest weight

In rows and columns \(03,12,13,23\), the quotient matrix is

\[
 T=\begin{pmatrix}
 t&0&\kappa_1&\kappa_2\\
 0&-t&\kappa_1&\kappa_2\\
 0&0&\omega_1&\omega_2\\
 0&0&\eta_1&\eta_2
 \end{pmatrix}.
\]

Let

\[
 L_T=\operatorname{diag}\!\left(
 \begin{pmatrix}1&-1\\0&1\end{pmatrix},I_2\right),\qquad
 R_T=\operatorname{diag}\!\left(
 \begin{pmatrix}1&1\\0&-1\end{pmatrix},I_2\right).
\]

Then
\[
 L_TTR_T=\operatorname{diag}(t,P_G),\qquad
 P_G=\begin{pmatrix}
 t&\kappa_1&\kappa_2\\
 0&\omega_1&\omega_2\\
 0&\eta_1&\eta_2
 \end{pmatrix}.
\]

The resulting periods are those of a Tate summand and the original group motive. Again the variable \(v\) is absent.

Huber--Wuestholz's Theorem 9.10, author-preprint p.79, describes algebraic-coefficient linear relations of 1-periods, using Theorem 9.7 on pp.77--78. The entire proofs were read. Applying that theorem to the displayed subobject or quotient accesses their central-free matrices. It does not evaluate the omitted minor. This is the exact failure of the proposed exterior-square/truncation application; it leaves open other constructions and period relations.

### 2.3 The diagonal polarization does not remove the entry

The saved symbolic calculation gives

\[
 P^tJ_{\mathrm{dR}}P=tJ_B,
\]

where the only positive upper-triangular entries are
\((J_B)_{03}=(J_B)_{12}=1\), and
\((J_{\mathrm{dR}})_{03}=1\), \((J_{\mathrm{dR}})_{12}=-1\).
The equality holds identically in \(v\), after the stated Legendre and diagonal identities. The primitive exterior bases are

\[
 (01,02,03-12,13,23)_B,
 \qquad
 (01,02,03+12,13,23)_{\mathrm{dR}}.
\]

They give a five-by-five comparison matrix. The tested minor remains one of its entries, and its derivative with respect to \(v\) is nonzero. More precisely the derivative of that five-by-five matrix has rank two. A central change \(v\mapsto v+ts\) changes the compact minor by \(-ts\omega_1\). Thus the actual diagonal polarization identity retains the central degree of freedom.

### 2.4 Precise Cartier-dual transport and the source wording

Define

\[
 L_D=\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix},
 \qquad
 R_D=\begin{pmatrix}0&0&1\\0&1&0\\-1&0&0\end{pmatrix}.
\]

The exact duality formula is

\[
 L_D\bigl(tP_G^{-t}\bigr)R_D
 =\begin{pmatrix}\omega_1&\omega_2&u\\
 \eta_1&\eta_2&z\\0&0&1\end{pmatrix}.
\]

This verifies the field comparison by an actual inverse-transpose Tate duality and two unimodular basis changes. In Bertolin et al., Remark 4.13, p.20, the received text describes the group motive and the point motive as isogenous. Their weight-graded dimension tuples, in weights \((0,-1,-2)\), are respectively \((0,2,1)\) and \((1,2,0)\). An isogeny induces an isomorphism of these weight-graded realizations, so that literal wording cannot hold. The field equality needed in C7.4 follows from the displayed duality or direct Legendre inversion. The current paper uses the latter and needs no mathematical repair on this point. This note corrects the looser phrase “through isogeny” in the agent's earlier audit narrative.

## 3. Every finite list of CM extension classes

Let \(\alpha_1,\ldots,\alpha_r\) lie in the CM order and let
\(H_\alpha\) be the extension of \(E\) by \(\mathbb G_m^r\) with ordered extension classes \(\alpha_jQ\). This includes all finite torus enlargements obtained by adjoining further CM multiples of the fixed point.

For the character \(m=(m_1,\ldots,m_r)\), the pushout extension has class
\(\sum_jm_j\alpha_jQ\). If the sum of the CM coefficients is nonzero, clearing denominators gives a nonzero elliptic endomorphism, hence an isogeny. Its kernel is finite, while \(Q\) is nontorsion. Consequently

\[
 \operatorname{Hom}(H_\alpha,\mathbb G_m)
 =\ker\left(\mathbb Z^r\longrightarrow K,
                   m\longmapsto\sum_jm_j\alpha_j\right).
\]

The restriction map to the torus is injective because a character trivial on that torus factors through the proper connected curve \(E\), and hence is constant. This also proves uniqueness of all extension homomorphisms once their torus and base maps have been fixed.

The kernel is saturated: its quotient is the additive subgroup of \(K\) generated by the \(\alpha_j\), which has no torsion. Choosing its integral basis and completing the kernel basis therefore gives a unimodular torus-coordinate change. The resulting extension is literally

\[
 H_\alpha\simeq H_{(\lambda_1,\ldots,\lambda_s)}
                   \times\mathbb G_m^{r-s},\qquad s\le2.
\]

This is a specialization of Huber--Wuestholz, Proposition 4.14 and its proof, author-preprint pp.34--35, and the following split-factor remark. The comparison is through their explicit character-to-extension-class map; no new structural theorem is claimed.

For the five classes \(1,\beta,(1+\beta)/2,2-\beta,(3+\beta)/2\), the coefficient matrix in \((1,\beta)\) is

\[
 A=\begin{pmatrix}1&0\\0&1\\1/2&1/2\\2&-1\\3/2&1/2\end{pmatrix}.
\]

The exact unimodular change is

\[
 U=\begin{pmatrix}
 1&0&0&0&0\\0&0&1&0&0\\1&1&-2&0&0\\
 -3&0&2&1&0\\-1&0&-1&0&1
 \end{pmatrix},\qquad
 UA=\begin{pmatrix}1&0\\1/2&1/2\\0&0\\0&0\\0&0\end{pmatrix}.
\]

The full integral inverse is saved. Write \(\alpha=(1+\beta)/2\), and set
\(\mathcal G=G_Q\times_EG_{\beta Q}\),
\(\mathcal H=G_Q\times_EG_{\alpha Q}\). The map

\[
 F:\mathcal G\longrightarrow\mathcal H,
 \quad F_E=[2],\quad F_T(t_1,t_2)=(t_1^2,t_1t_2)
\]

exists by the exact extension equality
\((2Q,(1+\beta)Q)=[2]^*(Q,\alpha Q)\). It is an isogeny of degree \(4\cdot2=8\). The reverse map

\[
 G:\mathcal H\longrightarrow\mathcal G,
 \quad G_E=\mathrm{id},\quad G_T(s_1,s_2)=(s_1,s_1^{-1}s_2^2)
\]

has degree two, because \(-Q+2\alpha Q=\beta Q\). Both composites are multiplication by two, verified on base and torus and therefore on the whole extension by uniqueness. More generally, an integer clearing the denominators of the two-by-two coefficient matrix supplies the corresponding comparison isogeny.

Every character on any such enlarged extension, composed with an algebraic map from \(\mathcal G\), is a character of \(\mathcal G\). The latter group has no nonzero character because \(Q,\beta Q\) are independent over \(\mathbb Q\) modulo torsion. Thus adding finitely many CM multiples and split factors gives no character evaluating the Gaussian on that original nonsplit source. This conclusion is confined to that class of group maps. It makes no claim about unrelated extension points or other analytic or arithmetic arguments.

## 4. The exact Ribet projection exclusion

Bertrand--Schmidt, section 1.2, pp.3--4, defines the Ribet subgroup by division of the canonical antisymmetric lifts. For this full CM order its projection lies in the division hull of \(\beta Q\). Hence a Ribet point in the fibre of \(G_Q\) over \(Q\) would require integers \(n>0,m\) with

\[
 (n-m\beta)Q=O.
\]

Its endomorphism norm is \(n^2+19m^2>0\); its kernel is finite. Therefore that fibre contains no point of the Ribet subgroup. This is an unconditional exclusion of this precise source mechanism. The source's Theorems 1--4, pp.2--3, concern algebraic curves with infinitely many Ribet specializations. They do not classify all algebraic points in the single maximal compact fibre under consideration.

Bertrand's 2017 slide 8 writes the same real determinant equation. Its explicit height exclusion is formulated as a conjecture; slide 15 relates it to a period conjecture. Those pages provide precise antecedent and normalization information, without supplying an unconditional resolution of the present point.

## 5. Fresh exact input certificate

`cm_witness_exact.py` independently implements, using SymPy 1.14.0, the literal polynomials printed in C7.10. All **39 checks pass**. They include the degree-19 curve identity, coprimality and separability, the invariant differential pullback, the complete \(1+\beta\) kernel factorization and degree count, the Laurent coefficient giving \(s_2=-2\), and the values

\[
 a=-\frac{21\beta}{703},\qquad
 r_2=-\frac{165}{74}+\frac{1839\beta}{1406},\qquad
 r_2\overline{r_2}=\frac{974799}{26011}.
\]

The exact reduction enumerations give \(\#E(\mathbb F_5)=7\) and \(\#E(\mathbb F_{11})=17\). Both primes are of good reduction. For any prime \(\ell\ne p\), the formal multiplication series \([\ell](T)=\ell T+O(T^2)\) has no nonzero \(\ell\)-primary torsion in the reduction kernel, since its leading coefficient is a local unit. Thus rational \(\ell\)-primary torsion injects into the reduction group. For \(\ell=5\), use the order 17 group; for \(\ell=11\), use the order 7 group; for any other \(\ell\), use both coprime orders. This proves \(E(\mathbb Q)_{\mathrm{tors}}=0\), and in particular the stated \(Q\) is nontorsion.

The program does not recover or execute `C7_cm_explicit.gp`, and it makes no replay claim for that file's historical 110-digit output. Its scope is the exact polynomial and rational arithmetic just listed. The universal constructions and all source hypotheses remain in the printed proof and this report.

## 6. Current disposition and reproducibility

`arithmetic_routes_exact.py` has **70 passing exact checks**, with the complete period, compound, primitive, duality, CM coefficient and torus-map matrices saved. `cm_witness_exact.py` has **39 passing exact checks**, with every polynomial and every finite-field point saved. Run both using the primary Python runtime and SymPy 1.14.0; they use no unavailable original script. Outputs record program SHA-256 values. The evidence is same-family, with the precise after-reading implementation scope stated above.

The remaining assertion is still the unconditional exclusion of the compact determinant for an algebraic lift in the positive diagonal central direction. The two additional routes do not supply that exclusion. The row remains open and no norm-transcendence progress is counted from these route closures. The new result of this continuation is a complete, exact account of these maps and their limits, plus independent execution of the concrete CM input checks.


## 7. Current analytic branch corroboration

A separate fresh program `cm_analytic_balls.py`, using python-flint 0.9.0 at 160 decimal working digits, now gives ten passing interval checks. It records the full balls, not rounded-point comparisons. Both displayed decimal strings are reproduced, and the absolute errors in the sigma expression for the exact Ribet coordinate and the zeta expression for the exact correction constant are less than 10^{-110}. This is a new execution; the absent historical PARI script was not run.

The exact real-period change used for this evaluation is as follows. The checked degree-19 map gives multiplication by beta, and the checked kernel of 1+beta contains all of E[2]. Hence 1+beta factors through [2], giving the endomorphism alpha=(1+beta)/2 and the full order of discriminant -19. The reduced positive binary forms of this discriminant have a<=sqrt(19/3)<3. At a=1 the only reduced class is (1,1,5); at a=2 no admissible odd b gives an integral c=(b^2+19)/8. Thus the CM ideal class is principal. Write tau_0=(1+i sqrt(19))/2. Its Eisenstein invariants are positive real (their real q-series at q=-exp(-pi sqrt(19)) have leading term 1 and tails of absolute value less than 1). The required invariants 152,-361 therefore select an imaginary homothety of Z+tau_0 Z, with positive real scale after that rotation. The unimodular change from (1,tau_0) to (1-2tau_0,1-tau_0), followed by multiplication by i, gives the positive real first period and ratio tau=(1+i/sqrt(19))/2. The program uses omega_1=(g_2(tau)/152)^(1/4)>0, then the inverse-wp branch whose original real logarithm satisfies 0<u<omega_1/2 and wp'(u)=-3. The ball checks independently verify both inequalities, the derivative sign and g_3=-361 to the stated error tolerance.

The numerical evaluation corroborates the analytic branch of the already exact algebraic identities. It supplies no algebraicity or transcendence test for the positive diagonal norm. The guarded proposal `C7_10_current_program_patch.json` preserves the old displayed values and algebraic claims while replacing the historical executable assertion by the two current programs and their exact scopes.

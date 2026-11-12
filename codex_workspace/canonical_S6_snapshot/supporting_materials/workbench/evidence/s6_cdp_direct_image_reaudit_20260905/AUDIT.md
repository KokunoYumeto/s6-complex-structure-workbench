# Independent CDP singular-fibre/direct-image audit

Date: 2026-09-05. This is a bounded mathematical audit, not a release task, a full independent proof of the candidate, or a replacement theorem about complex structures on the sphere. Only this directory was edited. Historical AI verdicts and status labels were not treated as evidence.

Source abbreviations below:

- C = output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/cdp_program.tex.
- G, A, I, P = respectively candidate_geometry.tex, exact_algebra.tex, integral_leray.tex, analytic_picard_completion.tex in that same research directory.
- 20 = literature_primary/CDP20_arXiv_1904.11179_source.tex.
- 20pub = literature_primary/CDP20_corrigendum.txt.
- 98 = literature_primary/CDP98_arXiv_math9607215_source.tex.

Input hashes fix the line locators in INPUT_HASHES.md. The staged replacement_passages.tex contains complete replacements for the two kinds of faulty expressions identified below; canonical files were not changed.

## 1. Outcome

The conductor-to-higher-direct-image implication itself is valid with the full fibre and the exact dual twist retained:
\[
\eta^*((L^\vee\otimes\omega_X)|_W)\simeq\mathcal O_{\widetilde W}
\ \Longrightarrow\
H^0(W,\Omega_X^1|_W\otimes(L^\vee\otimes\omega_X)|_W)\ne0
\]
\[
\Longrightarrow\ H^2(W,(T_X\otimes L)|_W)\ne0
\Longrightarrow\
(R^2f_*(T_X\otimes L))_{p_0}\ne0.
\]
This is a proved map calculation within the explicitly specified proper smooth-total-space normal-crossings setting. Neither nonnormality of W nor possible torsion of the higher-direct-image sheaf invalidates it. It is not a proof that every claimed global input to the S6 candidate holds.

Two written proof passages require correction:

1. C:410–415 matches the outer terms of two five-term sequences and claims a unique middle duality isomorphism. Matching outer terms does not construct that map or prove its uniqueness. The separate absolute-duality proof at C:452–489 supplies the needed analytic Gorenstein duality. The staged replacement constructs the pairing from that duality, retaining the canonical factor and the shift.
2. C:900–907 and I:804–812 treat multiplication by the complex scalar \(\alpha=\log s/(2\pi i)\) as multiplication by a real scalar in the flat real marking. The actual real translation is
\[
a(s)=\operatorname{Re}\alpha(s)\,v+\operatorname{Im}\alpha(s)\,J_s v,
\qquad J_s=\Pi(s)^{-1}i\Pi(s).
\]
The stated literal differential-form formula is not correct as written. The required mixed cohomology class and the based endpoint relation remain exactly the stated ones. Section 6 and the staged TeX prove this from the actual period covariance, not by guessing a real part.

The nodal-cubic test in C:278–352 correctly refutes the formal implication between three sheaf-cohomology groups. The source expressly does not construct its twist on a compact CDP20 threefold, and the family does not satisfy the CDP20 global hypotheses. Therefore this test is not a theorem-level counterexample.

The candidate's all-twist nonvanishing does not require a line bundle that is non-torsion on every fibre. It even includes the trivial twist. The CDP20 assertion that a general global bundle is non-torsion on every fibre is a separate global assertion with a restriction-surjectivity dependency. Neither finite fibre tests nor a non-torsion bundle on one nonnormal fibre proves that assertion. Section 7 gives its exact dependency and the limits of this audit.

## 2. Version and theorem-number audit

The 2020 article is itself the corrigendum to the 1998 paper: 20:255–268 and 20pub:36–50 say that its purpose is to address the incorrect general Lemma 1.5 of CDP98. The file CDP20_corrigendum.txt is the published 2020 article, pp. 679–696, DOI 10.1112/S0010437X19007802; it is not a later correction to the 2020 theorem.

The [1904.11179 arXiv record](https://arxiv.org/abs/1904.11179) gives v2, 20 May 2019, and the 2020 journal reference. The [math/9607215 arXiv record](https://arxiv.org/abs/math/9607215) gives v1, 8 July 1996. Both records were inspected directly in this audit. Local source provenance records retrieval through unversioned arXiv endpoints on 2026-08-29. The local older arXiv source does not have the final journal numbering.

The exact CDP20 claim is Theorem 2.2, 20:302–311 and 20pub:80–88: a compact complex manifold X of complex dimension three, with \(H^1(X,\mathbb Z)=H^2(X,\mathbb Z)=0\), algebraic dimension \(a(X)=1\), and holomorphic algebraic reduction \(f:X\to C\), has \(c_3(X)\le0\), together with the stated twisted-cohomology conclusions. Corollary 2.3 is the algebraic-dimension-zero claim for a compact complex threefold homeomorphic to S6. Proposition 2.4, 20:331–337, supplies the reduction to vanishing of one \(R^2f_*(T_X\otimes\mathcal L)\).

The singular-fibre inference is 20:980–986, published on p. 692 (20pub:754–765): pass from the conormal sequence for \(S=\operatorname{red}X_c\) to a vanishing statement for \(\widetilde\Omega_S^1=\Omega_S^1/\mathrm{torsion}\). This is the location of the missing lifting term.

| Subject | Local older arXiv numbering | Published older numbering cited by CDP20 |
|---|---|---|
| Surjectivity \(H^1(X,\mathcal O_X)\to H^1(F,\mathcal O_F)\) | Theorem 5.1, 98:623–625 | Theorem 3.1, 20:751–752, 20pub:533–534 |
| Split extension and its asserted abelianization | Lemma 5.2, 98:638–665 | Lemma 3.2, 20:535–537, 20pub:307–310 |
| Local freeness of all higher direct images | Lemma 1.5, 98:292–320 | Lemma 1.5, identified as incorrect at 20:257–259 |

The local older source's Theorem 3.1 at 98:478 is a different result. Searching only the number would trace the wrong proof.

There is also a fixed-twist issue in the CDP20 explanatory prose: 20:339–342 displays the fibrewise dual H0 without the canonical factor. The correct fixed-bundle expression is \((L^\vee\otimes\omega_X)|_{X_c}\). For an existential or general-line-bundle assertion, the bijection \(L\mapsto L^\vee\otimes\omega_X\) permits renaming the variable. It does not justify omitting that factor for a fixed unchanged L. C:1153–1156 retains it.

## 3. Exact cotangent filtration and conductor lift

Let S be a reduced effective Cartier divisor in a smooth complex threefold X. Let \(N^*=\mathcal I_S/\mathcal I_S^2\), let
\[
\mathscr T=\ker(\Omega_S^1\to j_*\Omega_{S_{\rm reg}}^1),\qquad
\widetilde\Omega_S^1=\Omega_S^1/\mathscr T,
\]
and let \(\rho:\Omega_X^1|_S\to\Omega_S^1\) be the natural surjection.

The conormal map is injective here. Locally S is \(g=0\) with g reduced in a regular analytic local ring. If \(h\,dg|_S=0\), then h vanishes at the generic smooth point of every irreducible component, where dg is nonzero. The reduced local ring has zero intersection of its minimal primes, so h=0. Thus the conormal sequence is short exact.

Define \(\mathscr K=\rho^{-1}(\mathscr T)\). Taking inverse image and quotient gives exactly
\[
0\to N^*\to\mathscr K\to\mathscr T\to0,\qquad
0\to\mathscr K\to\Omega_X^1|_S\to\widetilde\Omega_S^1\to0.
\]
For a line bundle A on S, tensoring is exact. Under the two vanishings of \(H^0(N^*\otimes A)\) and \(H^0(\widetilde\Omega_S^1\otimes A)\), the global-section sequences identify
\[
H^0(S,\Omega_X^1|_S\otimes A)
\cong
\ker\!\left[
H^0(S,\mathscr T\otimes A)
\xrightarrow{\delta_A}H^1(S,N^*\otimes A)
\right].
\]
This is a canonical identification, not merely a dimension comparison. For a torsion section t, choose local ambient lifts. Their differences are conormal sections and form the Čech cocycle defining \(\delta_A(t)\). The cocycle vanishes precisely when conormal corrections make the local lifts glue. This proves C:52–110. Cotangent torsion alone is not sufficient to contradict ambient vanishing; a nonzero global torsion section must lift.

For the candidate local models \(t=ux,\ uxy,\ uxyz\), let \(\eta:\widetilde S\to S\) be normalization and D the reduced double locus, with inverse-image conductor \(\widetilde D\). The conductor square is
\[
0\to\mathcal O_S
\xrightarrow{h\mapsto(\eta^*h,h|_D)}
\eta_*\mathcal O_{\widetilde S}\oplus\mathcal O_D
\xrightarrow{(\widetilde h,k)\mapsto\widetilde h|_{\widetilde D}-\eta^*k}
\eta_*\mathcal O_{\widetilde D}\to0.
\]
In the double model the conductor ideal is (x,y), and compatible functions are glued by \(h_1(y,z)+h_2(x,z)-h_1(0,z)\). In the triple model the conductor ideal is (xy,xz,yz), and the inclusion-exclusion formula C:197–200 gives a lift from three branch functions agreeing on all pairwise axes. Restriction from each smooth branch to its conductor is surjective. These local calculations prove exactness, including at triple points.

If \(\eta^*A\) has a nowhere-zero section e, tensor this square by \(\Omega_X^1|_S\otimes A\). The pair
\[
\bigl(\eta^*(dt|_S)\otimes e,0\bigr)
\]
is compatible: \(d(xy)=y\,dx+x\,dy\) and \(d(xyz)=yz\,dx+xz\,dy+xy\,dz\) have coefficients in the respective conductor ideals. A unit factor adds \(g\,du\), which vanishes on g=0. Thus there is a unique descended section \(s_e\). At a generic smooth point it is a nonzero ambient conormal covector, so \(s_e\ne0\). Its intrinsic image vanishes away from D and is torsion. If that image were zero, exactness would give \(s_e=dt\otimes\sigma\) for a global section of A; pulling back gives \(\eta^*\sigma=e\), hence \(\sigma\) is nowhere zero and A is trivial.

For connected compact S, a nontrivial A with trivial normalization pullback has H0 zero. Pull back any section and divide by e. The result is constant on every compact normalization component. At intersections of components the value of a section cannot be both zero and nonzero. Connectedness therefore forces either all constants zero or all nonzero; the latter case trivializes A. This verifies C:209–274.

The nodal-cubic test C:285–343 uses
\[
\mathcal C=\{([x:y:z],t):y^2z=x^2(x+z)+tz^3\},\qquad
X=\mathcal C\times\mathbb P^1,\qquad S=C_0\times\mathbb P^1.
\]
The t derivative is \(-z^3\ne0\) on z≠0. On z=0 the equation gives x=0, y≠0, and the z derivative is \(y^2\ne0\); hence the total space is smooth. The normalization of S is \(\mathbb P^1\times\mathbb P^1\). Gluing at the two preimages of the node by \(\lambda=2\) produces a bundle whose nth power has multiplier \(2^n\ne1\). Its H0 is zero and its normalization pullback is trivial. The torsion-free differential quotient injects into the normalization differential sheaf, whose H0 vanishes. The section just constructed still gives nonzero ambient H0. This is the exact formal counterexample, with the limits expressly stated at C:345–352.

## 4. Duality and the quotient-of-stalk map

Keep \(E=T_X\otimes L\), \(E^\vee=\Omega_X^1\otimes L^\vee\). A Cartier surface W has the length-one resolution
\[
0\to\mathcal O_X(-W)\to\mathcal O_X\to i_*\mathcal O_W\to0.
\]
Applying sheaf Hom into \(\omega_X\), multiplication by its nonzerodivisor is injective and the cokernel is
\[
\mathcal E xt_X^1(i_*\mathcal O_W,\omega_X)
=i_*\bigl((\omega_X\otimes\mathcal O_X(W))|_W\bigr).
\]
All other sheaf Ext groups vanish. Thus W is Cohen–Macaulay and Gorenstein, with invertible dualizing sheaf
\[
\omega_W=(\omega_X\otimes\mathcal O_X(W))|_W.
\]
Neither normality nor reducedness is needed for this calculation.

For the full fibre \(W=f^{-1}(p_0)\), \(\mathcal O_X(W)|_W\) is the pullback of the one-dimensional vector space \(\mathcal O_B(p_0)|_{p_0}\). Choosing a nonzero vector trivializes that factor and identifies \(\omega_W\) with \(\omega_X|_W\). The identification includes this scalar choice.

The analytic dualizing complex is \(\omega_W[2]\). The compact analytic duality theorem used at C:452–489 therefore gives the actual pairing
\[
H^2(W,E|_W)^\vee
\cong \operatorname{Ext}^{-2}_W(E|_W,\omega_W[2])
=\operatorname{Hom}_W(E|_W,\omega_W)
=H^0(W,\Omega_X^1|_W\otimes A_L).
\]
The source cites Ramis–Ruget Theorem 2 and Proposition 2 for analytic duality and the complete-intersection dualizing complex. The displayed local Ext calculation checks its specialization to this nonnormal hypersurface; this audit does not rederive the general analytic duality theorem from functional analysis. Locally free first argument removes positive sheaf Ext terms, compactness identifies compactly supported with ordinary cohomology, and finite-dimensionality makes the pairing algebraically perfect.

The five-term argument C:410–415 does not itself construct this map. Even for \(0\to\mathbb C\to\mathbb C^2\to\mathbb C\to0\), the distinct maps \((a,b)\mapsto(a+\lambda b,b)\) induce the identity on both ends. Thus matching ends neither constructs a distinguished middle arrow nor proves its uniqueness. The separate absolute analytic-duality proof supplies what is needed. Replacement 1 uses that argument for the full theorem.

For flatness, \(R=\mathcal O_{B,p_0}\) is a DVR. The map into a smooth local domain \(\mathcal O_{X,x}\) is injective: if a nonzero one-variable germ vanished after composition with f on an open set, the isolated zeros of that germ would make f locally constant, hence constant on connected X. Thus the target is torsion-free over R and is R-flat. Locally free E is f-flat. The uniformizer cuts out the full Cartier fibre. Compact X gives properness. This verifies C:494–525 without a fibre smoothness assumption.

Let \(K^\bullet\) be the bounded finite-free complex supplied locally by analytic coherent cohomology and base change. It computes the direct image and its derived fibre; f-flatness identifies the latter with ordinary restriction to W. For the uniformizer t, the exact sequence of complexes
\[
0\to K^\bullet\xrightarrow{t}K^\bullet\to K^\bullet/tK^\bullet\to0
\]
gives
\[
0\to H^q(K^\bullet)/tH^q(K^\bullet)
\to H^q(K^\bullet/tK^\bullet)
\to H^{q+1}(K^\bullet)[t]\to0,
\]
with \(M[t]=\ker(t:M\to M)=\operatorname{Tor}_1^R(M,R/(t))\). This proves the map direction and obstruction term in C:584–591.

Coherent cohomology of a compact analytic surface vanishes above degree two. If a highest nonzero higher-direct-image sheaf in degree q>2 existed locally, take a point in its support. Nakayama makes its stalk reduction nonzero, while the displayed exact sequence identifies that reduction with nonzero degree-q fibre cohomology, a contradiction. Boundedness permits choosing a highest degree. Thus \(R^qf_*E=0\) for q>2. In degree two the last Tor term vanishes, giving exactly
\[
\beta^2_{p_0}:(R^2f_*E)_{p_0}/\mathfrak m_{p_0}(R^2f_*E)_{p_0}
\xrightarrow{\sim}H^2(W,E|_W).
\]
No constancy of h2 and no local freeness of \(R^2f_*E\) appears. A nonzero vector in the right-hand space does not give a canonical lifted vector in the stalk; it proves the stalk's quotient and hence the stalk are nonzero. Conversely a zero quotient implies a zero coherent stalk by Nakayama. Applying this at every point gives the all-full-fibre criterion for vanishing of the direct-image sheaf.

CDP98 Lemma 1.5 claims all higher direct images are locally free (98:292–295), and its part (b) uses a relative-duality identification at 98:300–308 to infer degree-two local freeness from degree-zero local freeness. That stronger claim cannot generally discard derived terms. Its top-degree base-change formula at 98:315–316 is a different statement, and agrees with the proof above. The corrigendum's admission that Lemma 1.5 is incorrect does not by itself invalidate top-degree base change.

## 5. The candidate-specific dependency actually used

The shortest route C:1076–1108 is for \(L\in\operatorname{Pic}^0(X)\). G:691–873 supplies its cusp model, normalization, and canonical form; G:1323–1366 places it as an open subset of the globally glued compact X. The Picard identity component has \(c_1(L)=0\), so naturality gives \(c_1(\eta^*L|_W)=0\). Since \(\mathrm{dP}_6\) is the blow-up of \(\mathbb P^2\) at three noncollinear points, \(H^1(\mathrm{dP}_6,\mathcal O)=0\), and the exponential sequence makes \(c_1:\operatorname{Pic}(\mathrm{dP}_6)\to H^2(\mathrm{dP}_6,\mathbb Z)\) injective. Its pullback bundle is therefore trivial. The canonical trivialization gives the same result for \(A_L\).

The candidate constants are exactly G:576–582:
\[
B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
Z=sB_0+C(t),\quad
C(t)=\begin{pmatrix}6\mu(t)&h(t)\\b(t)-h(t)&\mu(t)\end{pmatrix}.
\]
The action is \(\Psi_\lambda(x,t)=(e^{2\pi iC(t)\lambda}t^{B_0\lambda}x,t)\). Each unimodular toric chart has t=\(z_0z_1z_2\). The invariant form
\[
\Omega=\frac{dx_1\wedge dx_2\wedge dt}{x_1x_2}
\]
equals \(\pm dz_0\wedge dz_1\wedge dz_2\) in that chart. Under \(\Psi_\lambda\) each \(dx_i/x_i\) acquires only a multiple of dt, which disappears after wedging with dt. This verifies the intrinsic canonical trivialization at G:757–775 with the original coordinates and signs.

The extension to all line bundles is the separate assertion
\[
r=\eta^*i^*:\operatorname{Pic}(X)\to\operatorname{Pic}(\mathrm{dP}_6)=0.
\]
It is not a consequence of conductor descent. The actual corollary C:1207–1230 cites the direct-boundary argument C:1006–1071, whose relevant chain is:

| Input | Actual source |
|---|---|
| \((\bigwedge^2V)^G=\mathbb Zq\), \(q=uw+6\gamma\delta\), \(V_G=\mathbb Z[\delta]\) | A:165–225 and original matrices A:14–22 |
| Finite fillings, \(m_1=3,m_2=4\), original \(v_1,v_2\), marked radial map | G:1118–1320; A:305–381 |
| Pair-of-pants defect and \(\bar d_1+\bar d_2+\bar d_0=0\) | C:722–828 |
| Finite norm identity | C:831–916, corrected real expression in Section 6 |
| Zero-section cusp sweep bounds the displayed solid torus | C:935–981 |
| Chern-class specialization naturality | C:983–1003 |
| Injectivity of degree-two cusp specialization | I:23–399 |

The exact algebra is
\[
\iota_{v_1}q=2(2u+w+3\delta)=2\eta_1,\qquad
\iota_{v_2}q=-3(u+w+2\delta)=-3\eta_2.
\]
Here \(v_1=(1,2,-4,0)^t\), \(v_2=(-1,-3,3,0)^t\). Directly,
\(\iota_{v_1}(uw)=2w+4u\), \(\iota_{v_1}(6\gamma\delta)=6\delta\);
\(\iota_{v_2}(uw)=-3w-3u\), \(\iota_{v_2}(6\gamma\delta)=-6\delta\).
The relations \([\eta_1]=3[\delta]\), \([\eta_2]=2[\delta]\) then give, for E=kq,
\[
\bar d_1=2k[\delta],\qquad \bar d_2=-\tfrac32k[\delta].
\]
The cusp sweep in coordinates \(t=ux_1x_2\) is the boundary of
\(\{|u|=\rho,x_1=1,|x_2|\le1\}\), with parametrization
\[
(\theta,\phi)\mapsto(\rho e^{i(\theta-\phi)},1,e^{i\phi}).
\]
Thus \(t=\rho e^{i\theta}\) and the \(\phi\)-circle is the original horizontal \(\widehat\delta\)-translation. An extending Chern class evaluates to zero on this boundary. The vertical reference form vanishes on the zero-section sweep. With the base-first sign convention retained at C:761–763, this gives \(\bar d_0=0\), and hence \(k[\delta]/2=0\) in \(V_G\otimes\mathbb R\). Therefore k=0.

The source's integral route first uses its order-four specialization parity to write k=2n, then obtains \(4n[\delta]-3n[\delta]=0\), giving the same conclusion. The real norm and balance calculation above does not need that additional parity computation. Finally
\(\operatorname{sp}^2(c_1(L|_W))=c_1(L|_F)=0\), the injectivity from I:23–399 forces \(c_1(L|_W)=0\), and injectivity of c1 on \(\mathrm{dP}_6\) gives r(L)=0.

The alternative P:986–1042 replaces cusp specialization by its toric support-function lemma P:629–984. It retains the same monodromy-invariant class, norm identities, and boundary balance. This audit traced that dependency and its boundary-factor comparison, but did not independently verify every coefficient of the alternative support-function calculation. The actual corollary above cites the direct-boundary route. Its all-Pic input is substantive and is not merely the older list of assumptions H1–H4.

## 6. Proof of the real-marking correction

The complete replacement paragraphs are staged separately. The derivation uses no altered overlap map.

The real marking is \(\Xi(s,x+\Lambda)=[s,\Pi(s)x]\), and the holomorphic overlap is translation by \(\alpha(s)\Pi(s)v_j\). Define \(J_s=\Pi(s)^{-1}i\Pi(s)\). Applying \(\Pi(s)\) to
\[
a_j(s)=\operatorname{Re}\alpha\,v_j+\operatorname{Im}\alpha\,J_s v_j
\]
returns exactly the holomorphic translation. A different logarithm branch changes this real lift by an integral multiple of v_j, so the torus map is unchanged. For real \(s=r\ne1\), \(\alpha=-i\log r/(2\pi)\); the real lift is \(-(\log r)/(2\pi)J_s v_j\), demonstrating why the printed \(\alpha v_j\) is not a real vector.

The proved covariance identity G:1124–1127 is
\[
R_{g_j}(s)\Pi(s)=\Pi(g_js)A_j.
\]
Since R is complex linear,
\[
J_{g_js}A_j
=\Pi(g_js)^{-1}i R_{g_j}(s)\Pi(s)
=\Pi(g_js)^{-1}R_{g_j}(s)i\Pi(s)
=A_jJ_s.
\]
The printed A matrices send the original vectors to themselves:
\[
A_1v_1=(1,6-4,-6-2+4,-2+2)^t=(1,2,-4,0)^t,
\]
\[
A_2v_2=(-1,-3,6-3,-3+3)^t=(-1,-3,3,0)^t.
\]
These computations retain \(v_1=\varepsilon,v_2=-\varepsilon'\) and \(\gamma(v_1)=1,\gamma(v_2)=-1\).

For a constant real alternating form \(\Omega_E=\frac12\sum E_{ab}dx^a\wedge dx^b\), direct substitution gives
\[
h_j^*\Omega_E-\Omega_E
=\sum E_{ab}da_j^a\wedge dx^b
+\tfrac12\sum E_{ab}da_j^a\wedge da_j^b.
\]
The last term is horizontal. On the full clockwise covering circle \(s_j(\theta)=re^{-2\pi i\theta}\), a continuous logarithm has \(\alpha(1)=\alpha(0)-1\). The period marking extends over the full disc, so \(J_{s_j(1)}=J_{s_j(0)}\). Thus \(a_j(1)-a_j(0)=-v_j\).

On the sweep of the marked fibre circle \(x(u)=u\lambda\), with orientation \(d\theta\wedge du\), the horizontal term is zero and the mixed term has integral
\[
\int_0^1 E(a'_j(\theta),\lambda)d\theta
=E(-v_j,\lambda)=-(\iota_{v_j}E)(\lambda).
\]
All marked fibre circles detect the full mixed cohomology component. The pulled-back defect has mixed class \(N_{T_j}d_j\); translation does not change a fibre-zero mixed class, since a representative \(d\theta\wedge\beta\) changes only by a horizontal two-form. The full class extends across the covering disc, where its mixed class is zero. Therefore
\[
N_{T_j}d_j-\iota_{v_j}E=0
\]
with the original clockwise sign. This proves the required cohomological identity even though the printed equality of real forms was not literal.

For the based meridian, the branch continued by g_j satisfies \(\alpha(g_js)=\alpha(s)-1/m_j\). Covariance and \(A_jv_j=v_j\) give
\[
a_j(g_js)=A_ja_j(s)-v_j/m_j.
\]
The inverse image of the zero section is \(-a_j(s)\). The affine generator sends it exactly to
\[
A_j(-a_j(s))+v_j/m_j=-a_j(g_js).
\]
This is the actual endpoint identity claimed at I:804–815. Changing the branch adds an integral multiple of v_j, whose translation commutes with the affine generator because v_j is A_j-invariant. The fixed zero-section whiskers therefore introduce no translated conjugate. After m_j clockwise continuations \(-a_j\) has increased by v_j, so \(\widehat\rho_j^{m_j}=t_{v_j}\) exactly. Thus the norm and based fundamental-group arguments are repaired without modifying any translation, orientation, or coefficient.

## 7. Non-torsion on every fibre and the surviving comparison limit

Trivial normalization pullback does not imply non-torsion. The candidate W has a normalization resolution whose global degree-zero row is
\[
\mathbb Z\longrightarrow\mathbb Z^3\longrightarrow\mathbb Z^2
\quad\text{or}\quad
\mathbb C\longrightarrow\mathbb C^3\longrightarrow\mathbb C^2.
\]
The first differential is zero; the second sends \((n_1,n_2,n_3)\) to \((s,s)\), \(s=n_1-n_2+n_3\). Its strata are \(\mathrm{dP}_6\), three \(\mathbb P^1\)'s, and two points. Positive coherent cohomology on the strata vanishes, and degree-one constant-sheaf cohomology also has no positive-degree stratum contribution. Thus
\[
H^1(W,\mathbb Z)=\mathbb Z^2,\qquad
H^1(W,\mathcal O_W)=\mathbb C^2,
\]
with the usual lattice inclusion induced by constants. The exponential sequence gives
\[
\operatorname{Pic}^0(W)\cong\mathbb C^2/\mathbb Z^2
\cong(\mathbb C^*)^2.
\]
In these coordinates a bundle is torsion exactly when both coordinates are roots of unity, since precisely then one common positive tensor power is trivial. Every such degree-zero bundle pulls back trivially to the rational normalization.

In particular the local canonical trivialization makes \(A_{\mathcal O_X}\) trivial, of order one. Its conductor section is the ordinary conormal dt and is nonzero as an ambient differential. The candidate's all-twist nonvanishing therefore cannot mean that every twist used there is non-torsion.

CDP20 Proposition 5.6, 20:790–799 and 20pub:570–581, concerns a general global line bundle non-torsion on every fibre. It uses Proposition 5.5:
\[
R^1f_*\mathcal O_X\simeq\mathcal O_C(b_1)\oplus\mathcal O_C(b_2),
\qquad b_1,b_2\ge0.
\]
That proposition uses generic restriction-surjectivity from Corollary 5.2, whose proof imports the older restriction theorem with the claim that its proof now works because local freeness has been restored. In the local older arXiv source it is Theorem 5.1; its proof 98:711–740 expressly uses the rank formula from Lemma 5.2 at 98:714 and 98:734.

The formal split-extension inference in that lemma is false in general. For \(\Gamma=N\rtimes H\), the homomorphism
\[
(n,h)\longmapsto([n],[h]):
\Gamma\to(N_{\rm ab})_H\oplus H_{\rm ab}
\]
is well-defined because H acts trivially in the coinvariant quotient. Every homomorphism from \(\Gamma\) to an abelian group kills \([N,N]\), \([H,H]\), and \(h(n)n^{-1}\), and therefore factors uniquely through this map. This proves
\[
\Gamma_{\rm ab}\cong(N_{\rm ab})_H\oplus H_{\rm ab}.
\]
With \(N=H=\mathbb Z\) and H acting on N by \(-1\), this is \(\mathbb Z/2\oplus\mathbb Z\), not \(\mathbb Z^2\). Hence splitting alone does not prove 98:652–656, repeated at 20:535–537. This does not prove that the same failure occurs for all threefolds satisfying CDP20's additional hypotheses. It does identify the exact unproved implication in the cited formal argument.

For the candidate the printed action is explicitly nontrivial: \(T_1u=-u-w\ne u\), and A:217–225 gives the coinvariant rank one. Thus the candidate matrices cannot establish that the omitted action is trivial in the older global restriction theorem.

At one fixed fibre c, torsion in a restriction is detected by the forbidden set
\[
\bigcup_{n\ge1}\ \bigcup_{\lambda\in H^1(X_c,\mathbb Z)}
\{v\in H^1(X,\mathcal O_X): n\,r_c(v)=\lambda_{\mathcal O}\}.
\]
If the complex restriction map r_c has rank two, each nonempty set has codimension two. Across a one-dimensional smooth base stratum these form local analytic incidence sets of dimension at most the dimension of the global parameter space minus one. Countably many lattice choices and coordinate charts give images of measure zero; finitely many singular fibres add countably many proper affine subspaces if the same surjectivity holds there. This is the reason that proved rank-two restriction-surjectivity can yield a global bundle outside every torsion locus. It is an all-parameter incidence argument, not a finite test. Merely knowing one bundle is nontrivial does not show it is non-torsion; all tensor powers must be excluded.

This audit does not independently prove the imported restriction-surjectivity theorem for every CDP20 threefold, or compute the candidate's global restriction map well enough to exhibit one line bundle non-torsion on every fibre. It therefore does not use Proposition 5.6 as a verified candidate-specific input. The candidate's conductor-to-direct-image argument does not need that input: its normalization-pullback condition and its all-Pic restriction calculation have a different exact role, described above.

## 8. Integration disposition

The exact downstream map survives the audit. The real-marking error has a proof-bearing correction preserving the finite norm and the based endpoint relation. The duality theorem survives through the separately supplied absolute analytic duality, with a staged proof replacing the unconstructed middle-arrow argument.

The source contains a substantive candidate-specific all-Pic proof, so its actual dependency chain must be examined rather than dismissed as a list of conditional hypotheses. At the same time, this bounded verification of the local maps does not certify the full global construction, all topology, or a theorem-level counterexample to CDP20. The formal CDP proof defects do not alone prove its theorem false. No canonical edits or external writes were performed.

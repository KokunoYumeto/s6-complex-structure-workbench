---
title: "Scope-Limited Mathematical Referee Report"
subtitle: "Canonical modular S6 manuscript: accessible source pages 56-66 and global assembler"
author: "Independent mathematical audit"
date: "24 August 2026"
lang: en-US
geometry: margin=1in
fontsize: 10pt
toc: true
toc-depth: 3
numbersections: true
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - |
    \usepackage{booktabs,longtable,array,amsmath,amssymb,mathtools,microtype}
  - |
    \usepackage{xcolor}
  - |
    \definecolor{fatalred}{RGB}{145,20,35}
  - |
    \definecolor{darkblue}{RGB}{25,55,95}
  - |
    \usepackage{fancyhdr}
  - |
    \pagestyle{fancy}\fancyhf{}\lhead{Mathematical referee report}\rhead{S6 manuscript}\cfoot{\thepage}
  - |
    \setlength{\emergencystretch}{3em}
---

# Editorial determination

**Recommendation: reject in the supplied form; the principal theorem is not mathematically certifiable.**

This determination rests on two independent grounds.

First, the supplied material is not the asserted 108-page manuscript. The file `s6_canonical_modular_main_108_pages.tex` is a 155-line assembly file containing ten `\input{parts/packet_XX_body.tex}` commands. None of those ten referenced files is present at the referenced location, and a clean compilation stops immediately at the missing `parts/packet_01_body.tex`. The only authoritative mathematical body available for review is packet 06, source pages 56-66, supplied separately. Those pages contain the end of Lemma 7.16, Theorems 7.17 and 7.22, the beginning of the integral Leray computation, the recognition argument in Section 8, the statement of Theorem 9.1, and Lemmas 9.2-9.4. The construction of the purported compact complex threefold, most local models, Appendices A-B, the remainder of Section 9, the bibliography, and the specifically announced Remark 9.9 are absent. Accordingly, this report rigorously audits the mathematics actually supplied and does not silently infer the missing arguments.

Second, the accessible global claims are mutually incompatible with a published theorem. The manuscript claims that the constructed compact complex threefold is homeomorphic, indeed diffeomorphic, to $S^6$, hence has $H^1(X;\mathbb Z)=H^2(X;\mathbb Z)=0$ and $\langle c_3(T_X),[X]\rangle=2$ (Corollary 7.29, Theorem 8.1, and Corollary 8.5). It also claims that $a(X)=1$ and that the holomorphic map $f:X\to\mathbb P^1$ is the algebraic reduction (Theorem 9.1(i)). Campana, Demailly, and Peternell (2020, Theorem 2.2) prove that a compact complex threefold with $H^1(X;\mathbb Z)=H^2(X;\mathbb Z)=0$, algebraic dimension one, and holomorphic algebraic reduction satisfies $c_3(X)\le 0$. Their Corollary 2.3 states directly that a compact complex threefold homeomorphic to $S^6$ has algebraic dimension zero. Thus the manuscript's assertions force both

\[
\langle c_3(T_X),[X]\rangle=2
\qquad\text{and}\qquad
\langle c_3(T_X),[X]\rangle\le 0,
\]

and simultaneously $a(X)=1$ and $a(X)=0$. This is a theorem-level contradiction, not a concern based merely on the historical status of the complex-$S^6$ problem. The manuscript explicitly mentions Campana-Demailly-Peternell and directs the reader to Remark 9.9, but that remark lies in the missing material. Unless the complete manuscript identifies a precise failed hypothesis or supplies a valid refutation of the published theorem, the main result cannot be accepted.

The terminal algebra in the supplied pages is, in contrast, often careful and reproducible. An exact-arithmetic verification script included with this report runs 22 checks and confirms the displayed Smith-normal-form computation in Theorem 7.17, the exterior-power monodromy and Wang ranks in Lemma 7.18, the rank and saturation calculation for $\alpha_2$ in Remark 7.20, the period-function identities in Lemmas 9.2-9.3, and the intersection and Gram-matrix calculation in Lemma 9.4. These positive findings do not validate the missing geometric inputs, and they do not remove the Campana-Demailly-Peternell contradiction.

# Scope, evidence, and review standard

## Materials actually available

The review used the following source material:

1. `s6_canonical_modular_main_108_pages.tex`, SHA-256 `cb0e87362cd83ed5d4720a50e532574678347dd3f570fb87c6bcdb9836b6bd48`. This is an assembler, not a self-contained manuscript.
2. Packet 06, containing the authoritative reconstruction of source pages 56-66 and its page images.
3. The final lines of source page 55 and first lines of source page 67, explicitly marked **context only**. Those lines were used solely to identify the boundaries of incomplete proofs; they were not treated as a substitute for the absent packet bodies.
4. Published mathematical literature needed to test the manuscript's global compatibility, principally Campana et al. (2020), together with standard references for the topological recognition step.

The assembler requests:

\[
\texttt{packet\_01\_body.tex},\ldots,\texttt{packet\_10\_body.tex},
\]

but none is present under `parts/`. Packet 06 exists only in a separate archive and therefore does not make the assembler compilable without manual restructuring. The compilation failure and source inventory are included in `evidence/` in the review bundle.

## Classification used in this report

Each claim is classified as follows.

**Verified** means the proof can be checked from the supplied statements and exact arithmetic without importing a material omitted fact. **Conditionally verified** means the terminal deduction is correct if explicitly identified upstream geometric or analytic inputs are granted. **Unverifiable** means an essential statement, map, lattice, local model, or theorem lies in an absent packet. **Contradicted** means the supplied claim is incompatible with another supplied claim and a directly applicable published theorem.

This distinction is essential. In a construction problem, a correct Smith normal form does not establish that the relation matrix is the matrix induced by the actual gluing. Likewise, a correct Leray differential computation does not establish that the stated sheaves or specialization lattices are correct. The review therefore separates algebraic calculation from geometric identification at every stage.

## Methods

The audit comprised:

- a clean-build and source-completeness test;
- a line-by-line logical review of packet 06;
- exact integer-lattice calculations, including Smith normal forms and determinantal divisors;
- symbolic exterior-algebra checks for the period and Hermitian-form computations;
- a dependency analysis identifying every imported theorem used by the accessible conclusions; and
- a literature consistency check focused on the claimed topology, Chern number, and algebraic reduction.

The accompanying script `computational_checks/verify_packet06.py` uses exact SymPy arithmetic and records machine-readable results in `results.json`. It contains no floating-point tests.

# Claimed proof architecture and point of failure

The accessible pages reveal the following proof architecture.

1. Earlier sections purportedly construct a compact complex threefold $X$ equipped with a holomorphic map $f:X\to B=\mathbb P^1$, with smooth complex two-torus fibres over $B^\circ$ and three special fibres.
2. Section 7 computes $\pi_1(X)$ by van Kampen and computes integral homology twice, first by Mayer-Vietoris and then by the Leray spectral sequence.
3. For the parameter choice $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$, these computations give $\pi_1(X)=1$ and $H_*(X;\mathbb Z)\cong H_*(S^6;\mathbb Z)$.
4. Section 8 applies Hurewicz, Whitehead, Smale, the $h$-cobordism theorem, and $\Theta_6=0$ to conclude $X\cong_{\mathrm{diff}}S^6$.
5. Section 9 analyzes the smooth fibres using period functions and asserts that very general fibres have algebraic dimension zero, while the global map $f$ is the algebraic reduction and $a(X)=1$.

The terminal topological recognition in step 4 is standard if steps 1-3 are correct. The fibrewise exterior algebra at the beginning of step 5 is also internally coherent. The global package nevertheless fails because steps 4 and 5 instantiate the hypotheses and violate the conclusion of Campana et al. (2020). Consequently, at least one of the following must fail:

- $X$ is a smooth compact complex threefold;
- the integral topology is that of $S^6$;
- $f$ is a holomorphic algebraic reduction;
- $a(X)=1$;
- the published Campana-Demailly-Peternell theorem applies as stated.

The supplied material does not identify which assertion is rejected. A rigorous manuscript must do so explicitly.

# Decisive literature contradiction

## Manuscript assertions

The relevant supplied claims are unambiguous.

- Corollary 7.29 states $\pi_1(X)=1$, $H_*(X;\mathbb Z)\cong H_*(S^6;\mathbb Z)$, and $e(X)=\langle c_3(T_X),[X]\rangle=2$.
- Theorem 8.1 states that $X$ is diffeomorphic to $S^6$.
- Corollary 8.5 repeats $\langle c_3(T_X),[X]\rangle=2$.
- Theorem 9.1(i) states $a(X)=1$, $\mathcal M(X)=f^*\mathcal M(B)$, and that $f$ is the algebraic reduction.

From the homology-sphere claim one obtains $H^1(X;\mathbb Z)=H^2(X;\mathbb Z)=0$. The map $f$ is asserted to be holomorphic throughout the construction and specifically to be the algebraic reduction in Theorem 9.1(i).

## Campana-Demailly-Peternell theorem

Campana et al. (2020, Theorem 2.2) address compact complex threefolds with vanishing first and second integral cohomology, algebraic dimension one, and holomorphic algebraic reduction. Their conclusion is $c_3(X)\le 0$. Their Corollary 2.3 specializes this to a compact complex threefold homeomorphic to the six-sphere and concludes $a(X)=0$.

The hypothesis matching is direct:

| Published hypothesis | Manuscript assertion |
|---|---|
| $X$ is a compact complex threefold | Theorem 6.2, invoked in Theorem 8.1 |
| $H^1(X;\mathbb Z)=H^2(X;\mathbb Z)=0$ | Corollary 7.29 and Theorem 8.1 |
| $a(X)=1$ | Theorem 9.1(i) |
| the algebraic reduction is holomorphic | Theorem 9.1(i), with $f:X\to\mathbb P^1$ holomorphic |
| conclusion $c_3(X)\le0$ | contradicts Corollaries 7.29 and 8.5, which give $c_3(X)=2$ |

No subtle comparison of conventions is involved: the top Chern number of a complex threefold is the Euler characteristic of its underlying oriented real tangent bundle, exactly as the manuscript itself states. A space homeomorphic to $S^6$ has Euler characteristic two.

## Why the manuscript's sentence about non-use of CDP20 is insufficient

Packet line 512 says that the proof of Theorem 9.1(i) uses period descriptions and facts about complex tori and that neither Section 7 nor CDP20 “enters,” referring to missing Remark 9.9. This does not resolve the contradiction. A proof may be independent of an earlier theorem and still contradict its conclusion. The relevant question is not whether CDP20 is cited in the derivation; it is whether the hypotheses of CDP20 hold.

A satisfactory response must take one of two forms:

1. **Inapplicability:** state an exact hypothesis of Campana et al. (2020, Theorem 2.2) that fails for the constructed $X$, and prove that failure without contradicting Theorem 9.1(i) or the topology; or
2. **Refutation:** identify a specific invalid step in the published proof and replace it with a complete argument showing that the theorem is false in this setting.

General remarks about singular fibres, nonreduced fibres, non-Kaehler geometry, or the proof being “elementary” do not suffice unless tied to an explicit hypothesis or line in the published proof. The omitted Remark 9.9 is therefore indispensable.

## Editorial consequence

This is a fatal issue. Even a complete and correct verification of all local gluing and homology calculations would not make the manuscript publishable while the contradiction remains. The correct editorial posture is rejection, not ordinary major revision, unless the missing text contains a rigorous resolution of the published obstruction. Because that text was not supplied, no such resolution can be credited.

# Detailed audit of packet 06

## Lemma 7.16: sign propagation

**Location:** source pages 55-57; packet lines 6-55 contain the continuation and conclusion.

The lemma controls the signs in the relations $\widehat\rho_j^{m_j}=t_{\varepsilon_jv_j}$ and is outcome-determinative: equal signs produce the manuscript's $|p|=1$ example, whereas opposite relative signs exchange the $1$ and $7$ cases.

### Step S1: elliptic-generator rotation senses

The argument uses the $(3,4,\infty)$ triangle group $\Delta\cong\mathbb Z/3*\mathbb Z/4$ with generators $x,y$ and cusp generator $z=(xy)^{-1}$. In a one-cusp Fuchsian group, every parabolic element is conjugate into the cusp stabilizer, so a proposed mixed assignment can be rejected by checking that the resulting reduced word is not conjugate to a nonzero power of $xy$ or its inverse. The manuscript's cyclically reduced-word test is correct at the formal free-product level: the words $y^3x$ and $yx^2$ have syllable length two and are not cyclic permutations of $xy$ or $y^3x^2$; powers with absolute exponent greater than one have larger cyclically reduced length.

The derivative computation at $z_1$ is also correct. From

\[
R_1(\tau)=1-\frac1\tau,\qquad \rho=e^{i\pi/3},
\]

one gets $R_1'(\rho)=\rho^{-2}=e^{-2\pi i/3}$. At $z_2$, an order-two zero of $\tau-i$ determines only $(g_2'(z_2))^2=-1$, so the coupling through the parabolic product is indeed needed to choose the sign.

This part is **conditionally sound**, but it depends on absent propositions establishing the triangle-group model, the uniqueness of the cusp, the precise definition of $g_0,g_1,g_2$, and the local orders of the period function.

### Steps S2-S4: deck transformation, regluing, and meridian relation

Given the displayed formula

\[
\widetilde g_j^{\log}(z,\zeta)
 =\left(g_jz,R_{g_j}(z)\zeta+\Pi(g_jz)v_j/m_j\right),
\]

the computation $(\widetilde g_j^{\log})^{m_j}=t_{v_j}$ is correct when $v_j$ is $A_j$-invariant. The invariance calculation for the reglued zero section

\[
\varsigma_j=-\frac{\log s_j}{2\pi i}\Pi(z)v_j
\]

is algebraically consistent with $\log s_j\circ g_j=\log s_j-2\pi i/m_j$. The resulting drift by $-v_j$ for a counterclockwise $s_j$-loop and the inversion to a clockwise meridian yield $\widehat\rho_j^{m_j}=t_{+v_j}$.

The logic is correct **if** the printed coordinate conventions and identifications with the local filling are correct. Those identifications lie in missing Sections 5-7. A complete review would require a single coordinate diagram tracing:

\[
\text{base meridian}\longrightarrow
\text{lift in the logarithmic cover}\longrightarrow
\text{deck generator}\longrightarrow
\pi_1(N_j\setminus m_jS_j)\longrightarrow\pi_1(N_j).
\]

Without that diagram, the sign lemma remains a verified internal consistency check rather than an independently established gluing theorem.

## Theorem 7.17: fundamental group

**Location:** source page 57; packet lines 58-79.

Once the van Kampen presentation is granted, the group calculation is correct. Eliminating $y$ from $xy=c^{\ell_0}$ gives $y=x^{-1}c^{\ell_0}$; because $c$ is central, the group is generated by commuting $x,c$. The two remaining relations have matrix

\[
R=\begin{pmatrix}
3&-\ell_1\\
4&\ell_2-4\ell_0
\end{pmatrix},
\qquad
\det R=-(12\ell_0-4\ell_1-3\ell_2)=-p.
\]

The first Smith invariant is one because the entries include $3$ and $4$. Hence, for $p\ne0$,

\[
\operatorname{coker}R\cong\mathbb Z/|p|\mathbb Z.
\]

The admissibility arithmetic is correct. Modulo three, $p\equiv-\ell_1$, so $3\nmid p$ when $3\nmid\ell_1$. Modulo two, $p\equiv-\ell_2$, so $p$ is odd when $\ell_2$ is odd. Thus $\gcd(p,12)=1$ and $p\ne0$.

Exact Smith-normal-form checks give:

\[
(\ell_0,\ell_1,\ell_2)=(0,1,-1):\quad
R=\begin{pmatrix}3&-1\\4&-1\end{pmatrix},\quad
\operatorname{SNF}(R)=\operatorname{diag}(1,1),
\]

and

\[
(0,1,1):\quad
R=\begin{pmatrix}3&-1\\4&1\end{pmatrix},\quad
\operatorname{SNF}(R)=\operatorname{diag}(1,7).
\]

**Verdict:** the terminal algebra is verified. The theorem remains conditional on the absent van Kampen attaching maps and the assertion that the normal closure of $\Lambda_{\rm tor}$ is exactly $\ker\gamma$.

## Lemma 7.18: Mayer-Vietoris and monodromy

**Location:** source pages 57-58; packet lines 87-125.

The short exact sequence follows formally from Mayer-Vietoris for $X=N_0'\cup X^\circ$ once $H_k(M)\to H_k(N_0')$ is surjective. If

\[
K_k=\ker\bigl(H_k(M)\to H_k(N_0')\bigr),
\]

then elimination of the $N_0'$ component gives

\[
0\to H_k(X^\circ)/j_*K_k\to H_k(X)
\to\ker(j_*|_{K_{k-1}})\to0.
\]

The exterior-power computation from the displayed monodromy is independently verified. In the ordered basis $(\widehat\gamma,\widehat u,\widehat w,\widehat\delta)$,

\[
M_0=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&1&1&0\\
-1&0&0&1
\end{pmatrix}.
\]

For the ordered bivector basis

\[
(\widehat\gamma\wedge\widehat u,
 \widehat\gamma\wedge\widehat w,
 \widehat\gamma\wedge\widehat\delta,
 \widehat u\wedge\widehat w,
 \widehat u\wedge\widehat\delta,
 \widehat w\wedge\widehat\delta),
\]

exact lattice reduction confirms

\[
\operatorname{im}(\wedge^2M_0-I)
 =\left\langle
 \widehat w\wedge\widehat\delta,
 \widehat\gamma\wedge\widehat w+\widehat u\wedge\widehat\delta
 \right\rangle,
\]

with a saturated rank-two image. Exterior powers in degrees zero through four have no cokernel torsion, and the Wang sequence gives ranks

\[
\operatorname{rk}H_k(M)=(1,3,6,6,3,1),
\]

exactly as stated.

The identification of $K_1$ and $K_2$ is not independently verifiable. It uses the topology of the toric central model, the collapse map of Proposition 7.12, and explicit solid tori in a local chart. The bounding-chain argument is plausible as written, but the quotient map into $N_0'$ and the literal identification of the boundary torus depend on missing Section 4 data.

**Verdict:** the Mayer-Vietoris algebra and monodromy calculations are verified; the geometric kernel generators are conditional.

## Lemma 7.19 and Remark 7.20: the two-fibre Mayer-Vietoris map

**Location:** source pages 58-59; packet lines 137-203.

### Degree one

The relation matrix

\[
\begin{pmatrix}
-\ell_1&3&0\\
-\ell_2&0&4
\end{pmatrix}
\]

has $2\times2$ minors $3\ell_2,-4\ell_1,12$. Under admissibility their greatest common divisor is one. The functional

\[
\Phi_1=(12,4\ell_1,3\ell_2)
\]

annihilates both relations and is primitive because

\[
\gcd(12,4\ell_1,3\ell_2)=1.
\]

These statements were exhaustively verified over all admissible residue classes modulo 12. The formula

\[
\Phi_1(j_*[\widetilde a_0])
 =12\ell_0-4\ell_1-3\ell_2=p
\]

then follows from the displayed meridian expression, conditional on that expression being geometrically correct.

### Degree two

The dual-lattice argument in part (c) is formally sound. For maps of finite-rank free abelian groups, the cokernel of the homology map fits into an exact sequence with $\operatorname{Ext}(\operatorname{coker}\psi,\mathbb Z)$ and $\operatorname{Hom}(\ker\psi,\mathbb Z)$. The manuscript proves the first term vanishes by asserting that $L_1+L_2$ is saturated; the displayed three generators indeed form a saturated rank-three lattice because one maximal minor is one.

The concrete matrix in Remark 7.20 is

\[
\alpha_2=
\begin{pmatrix}
2&1&3&0&0&0\\
-4&-2&0&1&0&0\\
-2&-2&-4&0&0&0\\
3&3&0&-1&0&0
\end{pmatrix}.
\]

Exact calculation gives rank three. The greatest common divisor of all $3\times3$ minors is one, so the image is saturated in its rational span and the cokernel is torsion-free of rank one. Moreover

\[
\alpha_2^{\mathsf T}(4,2,3,2)^{\mathsf T}=0,
\]

and the primitive left kernel is generated by $(4,2,3,2)$.

**Verdict:** the displayed integral linear algebra is verified. The formulas for $L_1,L_2$, $\pi_{j*}$, and the bases of $H_2(S_j)$ depend on absent Lemma 7.13 and Appendix A.

## Lemma 7.21: sweeping by a free circle action

**Location:** source page 59; packet lines 206-235.

The abstract identity is correct. For a free $S^1$-action $a:S^1\times Z\to Z$ and quotient $p:Z\to Z/S^1$, the map

\[
(\theta,z)\longmapsto(\theta z,z)
\]

identifies the product circle bundle over $Z$ with the pullback of $p$ along itself. Naturality of fibre integration gives

\[
[S^1]\backslash a^*\mathcal A=p^*p_!\mathcal A,
\]

and therefore

\[
\langle\mathcal A,\operatorname{sw}(y)\rangle
 =\langle p^*p_!\mathcal A,y\rangle.
\]

The freeness test on the local quotient is also logically correct from the displayed equation. Applying the $A_j$-invariant form $\gamma$ yields $k\ell_j/m_j\in\mathbb Z$; $\gcd(\ell_j,m_j)=1$ forces $k=0$, and primitivity of $\widehat\delta$ then forces the circle parameter to vanish.

On a torus, integration along the subcircle generated by $\widehat\delta$ is contraction with $\widehat\delta$ on invariant forms, up to the single global orientation sign already acknowledged.

**Verdict:** locally sound. The extension of this translation action across all pieces of $X^\circ$ depends on missing transition maps, but no internal defect is present in the stated principal-bundle argument.

## Theorem 7.22: integral homology

**Location:** source page 60; packet lines 242-286.

The degree-one conclusion follows from Theorem 7.17. In degree two, the manuscript obtains an extension

\[
0\to\operatorname{coker}\alpha_2\to H_2(X^\circ)
 \xrightarrow{\partial}\ker\alpha_1\to0,
\]

with both outer groups infinite cyclic. If $j_*\xi_{\widehat w}$ maps to a generator of $\ker\alpha_1$ while $j_*\xi_{\widehat\delta}$ lies in the kernel, then quotienting by the two classes reduces $H_2(X)$ to

\[
\operatorname{coker}\alpha_2/
\mathbb Zj_*\xi_{\widehat\delta}.
\]

This elementary extension argument is correct even if the chosen lift of the generator has a nonzero kernel component.

The sweeping identity then yields

\[
\Phi(j_*\xi_{\widehat\delta})
 =\langle\iota\mathcal A,j_*[\widetilde a_0]\rangle.
\]

The contraction is correct:

\[
\iota_{\widehat\delta}(2q)
 =\iota_{\widehat\delta}\bigl(2u\wedge w+12\gamma\wedge\delta\bigr)
 =\pm12\gamma.
\]

Since the generator of $H^1(X^\circ)$ restricts to $12\gamma$, the claimed order $|p|$ follows, provided the restriction map is injective and the geometric boundary formulas are correct.

The deductions in degrees three through five are correct for a closed oriented six-manifold. With finite $H_1$ and $H_2$, universal coefficients and Poincare duality give

\[
H_5=0,\qquad H_4\cong\operatorname{Ext}(H_1,\mathbb Z)
 \cong\mathbb Z/|p|\mathbb Z.
\]

If $e(X)=2$, then $b_3=0$, and

\[
H_3\cong H^3\cong\operatorname{Ext}(H_2,\mathbb Z)
 \cong\mathbb Z/|p|\mathbb Z.
\]

The vulnerable inputs are geometric: the boundary map on the swept tori, the Euler-characteristic calculation $e(X)=e(W)=2$, and the topology of $W$. They lie in absent propositions.

**Verdict:** the homological deduction is conditionally correct; the maps that supply its integer $p$ are not independently reviewable.

## Lemma 7.25: local-system Poincare duality

**Location:** source page 61; packet lines 307-327.

For an oriented punctured surface $B^\circ$ and a local system $\mathcal L$ with stalk $M$, the exact sequence

\[
0\to j_!\mathcal L\to j_*\mathcal L
 \to\bigoplus_{p\in\Sigma}M^{G_p}\to0
\]

has a skyscraper quotient with no positive-degree cohomology. Therefore

\[
H^2(B,j_*\mathcal L)
 \cong H_c^2(B^\circ,\mathcal L)
 \cong H_0(B^\circ,\mathcal L)
 \cong M_G.
\]

This is standard Poincare duality with local coefficients on an oriented surface (Bredon, 1997; Hatcher, 2002). The compatibility with cup products follows from cap-product naturality and the projection formula. The formula $x\smile[y]=[x\otimes y]$ is well-defined because $x$ is invariant.

The manuscript should nevertheless state its left/right module and orientation-local-system conventions. The only ambiguity is a global sign in the chosen generator of $H^2(B;\mathbb Z)$, which the later proposition already absorbs.

**Verdict:** verified, with a minor convention clarification.

## Proposition 7.26: sheaves and the Leray $E_2$ page

**Location:** source pages 61-62; packet lines 330-377.

The formal use of

\[
0\to R^qf_*\mathbb Z\to j_*\mathcal L^q\to Q^q\to0
\]

is correct. If the stated invariant lattices, coinvariant lattices, and skyscraper quotients are accepted, the displayed $H^0$, $H^1$, and $H^2$ groups follow from the long exact sequence and Lemma 7.25.

The essential content, however, is precisely the omitted content. The proposition imports:

- Theorem B.1 for specialization at $p_0$;
- Proposition 7.14 for the multiple fibres at $p_1,p_2$;
- the monodromy matrices $T_0,T_1,T_2$;
- the degree-three cokernel generator under a divisibility hypothesis; and
- several assertions of saturation and torsion-freeness.

None can be reconstructed from packet 06 alone. The displayed computations of two parabolic cohomology groups are plausible, but they also use matrices defined elsewhere.

**Verdict:** not independently verifiable. This is a critical gap because the entire second cohomology computation depends on these integral stalk lattices.

## Proposition 7.27: Leray transgressions

**Location:** source pages 62-63; packet lines 380-431.

The first differential is interpreted as an obstruction to globally lifting $12\gamma$. Given the stated local lift values and meridian identity, the discrepancy sum is

\[
12\ell_0-4\ell_1-3\ell_2=p,
\]

up to the global orientation sign. The Mayer-Vietoris description of $H^2(B;\mathbb Z)$ as the quotient of three boundary values by the sum-zero sublattice is standard.

The multiplicative arithmetic is correct. Normalize

\[
d_2(12\gamma)=p\omega,
\quad d_2(2q)=p'\omega\bar\delta,
\quad d_2(2\gamma uw)=p''\omega[\gamma\delta].
\]

Since

\[
(12\gamma)(2q)=12(2\gamma uw)
\]

and $[q]=12[\gamma\delta]$ in the coinvariants, the Leibniz rule gives

\[
12p''=24p-12p',\qquad p''=2p-p'.
\]

The vanishing of $(2q)(2\gamma uw)$, together with the two nonzero pairings, gives $|p'|=|p''|$. If $p''=-p'$, the preceding equation forces $p=0$, contrary to Theorem 7.17. Therefore $p'=p''=p$ with a common sign. This part is internally correct.

The conclusion

\[
H^1(X;\mathbb Z)=0,
\qquad H^2(X;\mathbb Z)\cong H^3(X;\mathbb Z)
 \cong\mathbb Z/|p|\mathbb Z
\]

then follows because the base has cohomological dimension two and the listed $E_2$ terms leave no extension ambiguity in the relevant total degrees.

**Verdict:** the spectral-sequence algebra is verified conditional on Proposition 7.26 and the local transgression normalization. Those inputs are absent and outcome-determinative.

## Remark 7.28: a genuine quantifier defect

**Location:** source page 63; packet line 434.

The remark states, after noting that $\ell_0$ is free, that

\[
|p|=1
\quad\Longleftrightarrow\quad
(\ell_1\bmod3,\ell_2\bmod4)\in\{(1,3),(2,1)\}.
\]

Read as a statement about a fixed triple $(\ell_0,\ell_1,\ell_2)$, this is false. For example,

\[
(\ell_0,\ell_1,\ell_2)=(100,1,-1)
\]

has residue pair $(1,3)$ but

\[
p=12(100)-4(1)-3(-1)=1199,
\]

so $|p|\ne1$.

The intended statement is correct after adding an existential quantifier:

> For fixed admissible $\ell_1,\ell_2$, there exists $\ell_0\in\mathbb Z$ such that $|p|=1$ if and only if $(\ell_1\bmod3,\ell_2\bmod4)$ is $(1,3)$ or $(2,1)$.

Indeed, $p=\pm1$ is equivalent to

\[
12\ell_0=4\ell_1+3\ell_2\pm1,
\]

and solvability is exactly the displayed residue condition. The computational appendix exhaustively verifies all residue classes.

**Verdict:** confirmed minor mathematical defect; repair is local.

## Corollary 7.29: homology sphere and Chern number

**Location:** source page 63; packet lines 437-442.

For $p=-1$, the prior calculations give trivial $\pi_1$, $H^1$, $H^2$, and $H^3$. The universal-coefficient argument for $H_2=0$ is valid because homology is finitely generated: $\operatorname{Hom}(H_2,\mathbb Z)=0$ makes $H_2$ finite, and $\operatorname{Ext}(H_2,\mathbb Z)=0$ then kills its torsion. Poincare duality gives $H_4=H_5=0$. The rank and torsion of $H_3$ vanish by the same duality and universal-coefficient reasoning. Thus the conclusion that $X$ is an integral homology six-sphere is correct if the preceding computations and the closed-manifold hypothesis are correct.

For a compact complex threefold, the top Chern class of $T_X$ equals the Euler class of the underlying oriented real tangent bundle, so

\[
\langle c_3(T_X),[X]\rangle=e(X)=2.
\]

The notation should consistently distinguish the class $c_3(T_X)\in H^6(X;\mathbb Z)$ from its numerical evaluation.

**Verdict:** conditionally correct. It is one half of the fatal Campana-Demailly-Peternell contradiction.

## Section 8: recognition as the standard smooth six-sphere

**Location:** source pages 63-64; packet lines 444-474.

Lemma 8.2 is standard. If a simply connected closed $n$-manifold has reduced homology that of $S^n$, the Hurewicz theorem applied successively gives $\pi_i=0$ for $i<n$ and $\pi_n\cong\mathbb Z$. A map $S^n\to M$ representing a generator is a homology equivalence, and the homology Whitehead theorem makes it a homotopy equivalence because both spaces have CW homotopy type (Hatcher, 2002).

For $n=6$, a smooth homotopy sphere is homeomorphic to $S^6$ by the high-dimensional generalized Poincare theorem. Smooth oriented homotopy six-spheres form $\Theta_6$, and $\Theta_6=0$ (Kervaire & Milnor, 1963). Therefore any smooth homotopy six-sphere is diffeomorphic to the standard $S^6$. The orientation adjustment by a reflection is correct.

The citation path in the manuscript is somewhat longer than necessary but mathematically standard (Milnor, 1965; Smale, 1961). The decisive hypothesis is that the object produced in Section 6 is genuinely a closed smooth manifold and that Section 7 correctly computes its topology.

**Verdict:** the recognition theorem is conditionally correct. It cannot repair an error in the construction or homology computation; it only propagates those inputs.

## Theorem 9.1: complex-analytic invariants

**Location:** source pages 64-65; packet lines 485-509.

Only the theorem statement and the beginning of the proof of part (i) are supplied. Parts (ii)-(vi), involving higher direct images, the canonical bundle, Chern numbers, automorphisms, and Hodge numbers, are not reviewable from packet 06. Some stated consequences are formally compatible with the claimed topology: for example, $c_1$ and $c_2$ vanish in integral cohomology if $H^2=H^4=0$, and Serre duality on a complex threefold gives $h^{1,2}=h^{2,1}$ without requiring Kaehler Hodge symmetry. But no proof is present.

Part (i) is the contradicted assertion discussed above. Even before applying Campana et al. (2020), the supplied source does not contain the descent argument establishing $\mathcal M(X)=f^*\mathcal M(\mathbb P^1)$ or the treatment of singular and multiple fibres. The page-67 text supplied in the packet is explicitly context only and cannot substitute for the missing proof.

**Verdict:** part (i) is contradicted when combined with the manuscript's topology; parts (ii)-(vi) are unverified.

## Lemma 9.2: Neron-Severi criterion

**Location:** source pages 65-66; packet lines 540-588.

The Hodge-type criterion is correct for a real class on a complex two-torus. Because $H^{2,0}$ is generated by $\sigma_1\wedge\sigma_2$, a real two-form $E$ is of type $(1,1)$ if and only if

\[
E\wedge\sigma_1\wedge\sigma_2=0.
\]

From

\[
\sigma_1=6\mu\gamma+\tau u+w,
\qquad
\sigma_2=\beta\gamma+\mu u+\delta,
\]

exact exterior algebra gives

\[
\begin{aligned}
\sigma_1\wedge\sigma_2={}&
(6\mu^2-\tau\beta)\gamma\wedge u
-\beta\gamma\wedge w
+6\mu\gamma\wedge\delta\\
&-\mu u\wedge w
+\tau u\wedge\delta
+w\wedge\delta.
\end{aligned}
\]

Pairing with a general integral bivector yields exactly

\[
P_E=E_{\gamma u}-E_{\gamma w}\tau-E_{\gamma\delta}\mu
+6E_{uw}\mu+E_{u\delta}\beta
+E_{w\delta}(6\mu^2-\tau\beta).
\]

The computational check reproduces every coefficient and sign.

The result remains conditional on the absent Theorem 3.4, which must ensure that $\Pi(z)\Lambda$ is a full lattice and that $F^1\oplus\overline{F^1}=V\otimes\mathbb C$. The identification of integral $(1,1)$ classes with the Neron-Severi group is standard for complex tori (Birkenhake & Lange, 2004).

**Verdict:** exterior-algebra computation verified; torus-period input absent.

## Lemma 9.3: independence of period functions

**Location:** source page 66; packet lines 591-628.

All displayed substitutions have been checked symbolically. Under $g_0$,

\[
(6\mu^2-\tau\beta)\circ g_0
=(6\mu^2-\tau\beta)+(\beta-\tau+1).
\]

Subtracting a hypothetical linear relation from its transform gives

\[
-b+d+e(\beta-\tau+1)=0.
\]

If $e\ne0$, $\beta-\tau$ would be constant, but $g_0$ translates it by two. Hence $e=0$ and $d=b$.

Applying $g_2$ to the reduced relation and multiplying by $-\tau$ gives equation (9.2):

\[
6b\mu^2+c(\tau-1)\mu+b(\tau^2+3\tau+1)-c\tau=0.
\]

The next $g_0$ difference equals the manuscript's displayed expression up to the harmless overall sign determined by which equation is subtracted from which. It forces $b=0$. If $c\ne0$, then $\mu=\tau/(\tau-1)$, and applying $g_0$ gives the incompatible identity

\[
\frac{\tau}{\tau-1}=\frac{\tau-1}{\tau-2}
\quad\Longrightarrow\quad 0=1.
\]

Thus all coefficients vanish. Substitution into $P_E$ then gives $P_E\equiv0$ exactly for $E\in\mathbb Z\eta$.

**Verdict:** verified from the stated transformation laws. Whether those laws hold on the claimed connected period domain is an absent upstream issue.

## Lemma 9.4: the class $\eta$

**Location:** source page 66, completed by the context at the start of page 67.

The $(1,1)$ condition follows immediately from Lemma 9.2 for

\[
\eta=u\wedge w+6\gamma\wedge\delta.
\]

The self-intersection is correct:

\[
\eta^2
=2(u\wedge w)(6\gamma\wedge\delta)
=12\,\gamma\wedge u\wedge w\wedge\delta.
\]

As an alternating form on the lattice, the inverse bivector has

\[
\eta^\vee(u,w)=-1,
\qquad
\eta^\vee(\gamma,\delta)=-\frac16.
\]

With

\[
G_\eta=\bigl(i\eta^\vee(\sigma_a,\overline{\sigma_b})\bigr),
\]

exact calculation gives

\[
G_\eta=
\begin{pmatrix}
2\operatorname{Im}\tau&2\operatorname{Im}\mu\\
2\operatorname{Im}\mu&\frac13\operatorname{Im}\beta
\end{pmatrix}.
\]

Its determinant is

\[
\det G_\eta
=\frac23\operatorname{Im}\tau\operatorname{Im}\beta
-4(\operatorname{Im}\mu)^2
=\frac23\operatorname{Im}\tau
\left(\operatorname{Im}\beta-
\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}\right).
\]

Thus $\operatorname{Im}\tau>0$ and $D<0$ imply $\det G_\eta<0$, so the real symmetric $2\times2$ matrix has signature $(1,1)$. The relation $H_\eta=2G_\eta^{-1}$ preserves signature. The factor and signs have been independently checked.

The manuscript's exact equality $\eta^2=12$ uses the declared orientation $\operatorname{vol}=\gamma\wedge u\wedge w\wedge\delta$. The earlier statement that orientation is immaterial should be narrowed to the nonvanishing arguments or the chosen volume orientation should be identified with the complex orientation.

**Verdict:** exact linear algebra verified; domain inequalities and the Appell-Humbert global input remain conditional.

# Dependency audit of the global theorem

The supplied pages repeatedly rely on results not present in the source tree. The following omissions are not editorial inconveniences; they are logically central.

## Construction and smoothness

Theorem 8.1 begins, “By Theorem 6.2, $X$ is a compact complex manifold of dimension 3.” Theorem 6.2 is absent. A construction purporting to solve the complex-$S^6$ problem must establish, in local coordinates:

- that all quotient actions are free where required;
- that the local analytic spaces are smooth, including at central and multiple fibres;
- that transition maps are holomorphic and satisfy cocycle identities;
- that regluing produces a Hausdorff space;
- that the map to the base extends holomorphically and properly;
- that the resulting space is compact; and
- that the underlying differentiable structure is the one used in the topological calculations.

None of these can be inferred from packet 06.

## Fundamental-group attaching maps

Theorem 7.17 is only as reliable as the identifications

\[
\widehat\rho_j^{m_j}=t_{v_j},
\qquad
\widehat\rho_1\widehat\rho_2=t_\mu,
\qquad
\Lambda_{\rm tor}=1.
\]

The sign lemma addresses one sensitive point, but the complete van Kampen diagram, basepoint paths, conjugations, and local inclusions are absent. Because the distinction between $|p|=1$ and $|p|=7$ is a sign-level distinction, these maps require independent coordinate verification.

## Homology of the central fibre and collapse

The first homology computation relies on $H_*(W)$, a collapse map, toric bounding chains, and Euler characteristic $e(W)=2$. The second claims independence from part of that route but relies instead on Appendix B's specialization theorem. Both sets of inputs are absent. Two calculations are not genuinely independent if their shared local models or orientation normalizations contain the same error; a complete manuscript should identify the exact shared and independent dependencies.

## Integral specialization lattices

The Leray computation is sensitive to integral index, not merely rational rank. The groups $\mathbb Z/2$, $\mathbb Z/3$, and $\mathbb Z/4$ in Proposition 7.26 determine the global sections and transgressions. Every image must therefore be checked as an integral sublattice, with saturation proved. The supplied terminal calculations do this carefully when matrices are displayed, but the crucial stalk matrices are omitted.

## Period domain and algebraic reduction

The Neron-Severi calculation assumes a full lattice, a one-dimensional connected parameter domain, specific automorphy laws, and the inequality $D<0$. The global algebraic-reduction conclusion additionally needs a proof that meromorphic functions constant on very general fibres descend through singular and multiple fibres. The relevant lemmas and Remark 9.9 are absent.

# Additional mathematical and expository issues

## Nonstandard quotient notation

The manuscript writes $\mathbb Z/p$ while $p$ may be negative. It should use $\mathbb Z/|p|\mathbb Z$ or $\mathbb Z/p\mathbb Z$ with an explicit convention that the ideals $(p)$ and $(-p)$ coincide. This is minor but important in the examples $p=-1$ and $p=-7$.

## Class versus Chern number

Statements such as “$c_3(X)=2$” should be replaced by

\[
\langle c_3(T_X),[X]\rangle=2.
\]

The class lies in $H^6(X;\mathbb Z)$, whereas the integer is its evaluation. The distinction is especially important when applying external Chern-number inequalities.

## Hurewicz induction

Lemma 8.2 is correct, but “applied inductively in degrees $2,\ldots,n$” should be expanded by one sentence: after vanishing of $\pi_i$ for $i<k$, the Hurewicz theorem identifies $\pi_k$ with $H_k$, which vanishes for $k<n$. This avoids the appearance that Hurewicz applies in every degree without a connectivity hypothesis.

## Local coefficient signs

Lemma 7.25 and Proposition 7.27 absorb a global sign into the generator $\omega$. This is legitimate. The manuscript should say once whether local systems are left or right $\mathbb Z[\pi_1]$-modules and how cap product is normalized. Doing so would make the common-sign assertion fully transparent.

## Independence claims

The manuscript repeatedly states that one route does not use another proposition. Such dependency claims should be presented as a directed dependency graph. In a result of this magnitude, the key question is not only whether Section 7.7 cites Section 7.2, but whether both use the same local model, monodromy convention, or orientation normalization. The included `claim_dependency_matrix.csv` begins this audit for the accessible slice.

# Computational verification record

The included exact-arithmetic script executes 22 checks, all of which pass. The checks cover:

1. $\det R=-p$ in Theorem 7.17.
2. Smith normal forms for the $p=-1$ and $p=-7$ examples.
3. Exhaustive admissibility verification of $\gcd(p,12)=1$ over residue classes.
4. The relation-lattice minors and primitive functional in Lemma 7.19(a).
5. Unimodularity of $M_0$.
6. Exterior-power kernel and cokernel ranks and the Wang ranks.
7. The exact image lattice of $\wedge^2M_0-I$.
8. Rank, saturation, and left kernel of the matrix $\alpha_2$.
9. A counterexample to the literal fixed-triple reading of Remark 7.28.
10. Exhaustive verification of the corrected existential residue statement.
11. The expansion of $\sigma_1\wedge\sigma_2$.
12. The formula for $P_E$.
13. The $g_0$ and $g_2$ transformation identities in Lemma 9.3.
14. Equations derived in the linear-independence proof.
15. $\eta^2=12$.
16. The inverse alternating form and Gram matrix.
17. The determinant factorization and signature implication.
18. The formal incompatibility between $c_3=2$ and the externally forced inequality $c_3\le0$.

The script records exact matrices, determinantal divisors, and symbolic expressions in `computational_checks/results.json`. The test does **not** claim to verify omitted geometry, published theorems, or any theorem whose defining matrices are absent.

# Required actions before any renewed review

A renewed review would require all of the following.

1. **Complete source.** Supply a compilable source tree containing all packet bodies, appendices, bibliography, and figures, or an authoritative complete PDF. The current assembler is insufficient.
2. **Direct CDP reconciliation.** Include a theorem-level discussion of Campana et al. (2020, Theorem 2.2 and Corollary 2.3). State every hypothesis, identify the alleged point of nonapplication or error, and prove the claim. Remark 9.9 is mandatory.
3. **Construction audit.** Give a local-coordinate proof of smoothness, Hausdorffness, compactness, and integrability for $X$, with all finite-group and toric quotient actions checked.
4. **Sign audit.** Provide a global convention table and a diagram connecting triangle-group generators, base meridians, logarithmic deck transformations, local filling generators, and van Kampen relations.
5. **Integral topology audit.** Supply the complete matrices for every homology and cohomology map, not just ranks. Prove saturation wherever torsion conclusions depend on it.
6. **Independent Leray audit.** Provide explicit specialization maps at all three special fibres and a chain-level or hypercohomological normalization of $d_2$.
7. **Algebraic-reduction proof.** Supply the complete argument that every meromorphic function descends to $\mathbb P^1$, including extension across singular and multiple fibres.
8. **Corrections.** Repair Remark 7.28, quotient notation, orientation language, and class-versus-number notation.
9. **Reproducibility.** Add a dependency graph, clean-build instructions, and machine-checkable scripts for the integral matrices. The supplied packet reconstruction is useful, but the mathematical source must be complete.

# Final assessment

The accessible pages exhibit substantial technical work and several carefully executed lattice calculations. The fundamental-group Smith normal form, the displayed Mayer-Vietoris matrices, the multiplicative Leray arithmetic, and the fibrewise period identities survive independent exact verification. These are meaningful positive findings.

They do not establish the claimed complex structure on the standard six-sphere. The global construction and most geometric inputs are missing, and the supplied conclusions produce a direct contradiction with Campana et al. (2020). Because the contradiction strikes the central theorem rather than a peripheral lemma, the proper recommendation is **rejection in the present form**. A complete resubmission would have to resolve the Campana-Demailly-Peternell obstruction explicitly before the remaining 97 pages could be meaningfully assessed.

# References

Anonymous. (2026). *Canonical independent LaTeX reconstruction of the 108-page authority PDF* [Incomplete unpublished manuscript supplied for review].

Birkenhake, C., & Lange, H. (2004). *Complex abelian varieties* (2nd ed.). Springer. https://doi.org/10.1007/978-3-662-06307-1

Bredon, G. E. (1997). *Sheaf theory* (2nd ed.). Springer. https://doi.org/10.1007/978-1-4612-0647-7

Campana, F., Demailly, J.-P., & Peternell, T. (2020). The algebraic dimension of compact complex threefolds with vanishing second Betti number. *Compositio Mathematica, 156*(4), 679-696. https://doi.org/10.1112/S0010437X19007802

Hatcher, A. (2002). *Algebraic topology*. Cambridge University Press.

Hirzebruch, F. (1966). *Topological methods in algebraic geometry* (3rd ed.). Springer.

Kervaire, M. A., & Milnor, J. W. (1963). Groups of homotopy spheres: I. *Annals of Mathematics, 77*(3), 504-537. https://doi.org/10.2307/1970128

Milnor, J. (1965). *Lectures on the h-cobordism theorem*. Princeton University Press.

Smale, S. (1961). Generalized Poincare's conjecture in dimensions greater than four. *Annals of Mathematics, 74*(2), 391-406. https://doi.org/10.2307/1970239

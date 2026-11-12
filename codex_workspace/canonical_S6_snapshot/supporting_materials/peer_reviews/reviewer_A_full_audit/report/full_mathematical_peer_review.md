---
title: "Full Mathematical Peer Review of the 108-Page S6 Manuscript"
subtitle: "The (3,4,infinity) modular family of 2-tori completed at three special points"
author: "Independent technical review"
date: "24 August 2026"
geometry: margin=0.78in
fontsize: 10pt
papersize: letter
colorlinks: true
linkcolor: blue
urlcolor: blue
toc: true
toc-depth: 3
numbersections: true
header-includes:
  - |
    ```{=latex}
    \usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array,microtype}
    \usepackage[most]{tcolorbox}
    \newcommand{\Z}{\mathbb Z}
    \newcommand{\C}{\mathbb C}
    \newcommand{\Pone}{\mathbb P^1}
    \newcommand{\cO}{\mathcal O}
    \newcommand{\Pic}{\operatorname{Pic}}
    \newcommand{\NS}{\operatorname{NS}}
    \newcommand{\rk}{\operatorname{rk}}
    \newcommand{\im}{\operatorname{im}}
    \newcommand{\coker}{\operatorname{coker}}
    \newcommand{\Aut}{\operatorname{Aut}}
    \newcommand{\Spec}{\operatorname{Spec}}
    \newcommand{\dP}{\mathrm{dP}}
    \newtcolorbox{assessmentbox}{colback=gray!4,colframe=black!55,boxrule=.5pt,arc=1pt,left=7pt,right=7pt,top=6pt,bottom=6pt}
    ```
---

# Referee determination

**Recommendation:** Major revision and resubmission after independent specialist replication. The manuscript should not be accepted as an established solution in its present form, but this review did **not** identify a fatal mathematical contradiction in the complete 108-page text.

**Central audit conclusion:** The full manuscript materially changes the assessment possible from pages 56--66 alone. Section 10 gives a technically substantive proposed explanation of why the printed arguments of Campana, Demailly, and Peternell (1998, 2020) do not apply to the constructed nonnormal fibre. The conductor-supported ambient cotangent section and the monodromy-coinvariant correction are coherent on close inspection. Thus the earlier packet-only conclusion that the manuscript was immediately refuted by CDP20 is withdrawn and superseded by this report.

**Confidence boundary:** Exact matrix, lattice, Smith-normal-form, exterior-power, period, and intersection computations were independently reproduced. The main unresolved audit risk is geometric rather than arithmetic: the global collapse and integral specialization at the cusp, the analytic base-change/duality arguments at nonnormal or nonreduced fibres, and the manuscript's challenge to published literature require independent checking by specialists. No finite referee audit can convert an extraordinary new construction into a theorem merely by failing to locate an error.

The manuscript claims a compact complex threefold $X$ and a holomorphic map

$$
f:X\longrightarrow \Pone
$$

whose general fibres are complex two-tori, whose three special fibres consist of a reduced irreducible nonnormal normal-crossing surface $W$ and two multiple fibres $3S_1$ and $4S_2$, and for a particular choice of logarithmic twisting data satisfies

$$
\pi_1(X)=1,\qquad H^*(X;\Z)\cong H^*(S^6;\Z),\qquad X\cong_{\mathrm{diff}}S^6.
$$

It further claims

$$
a(X)=1,\qquad K_X\cong f^*\cO_{\Pone}(-1)\otimes\cO_X(2S_2),
$$

$$
R^1f_*\cO_X\cong\cO\oplus\cO(-1),\qquad R^2f_*\cO_X\cong\cO(-1),
$$

and $c_3(X)=2$. These conclusions would resolve the classical Hopf problem in the affirmative and, at the same time, contradict the printed conclusions of Campana et al. (2020, Theorem 2.2 and Corollary 2.3). That combination makes the burden of proof exceptionally high.

My disposition is therefore deliberately two-level:

1. **Internal mathematical audit:** I found the proof architecture coherent and found no theorem-breaking inconsistency. The exact computations tested independently are correct.
2. **Publication-level validation:** The manuscript is not yet ready to be treated as a settled proof. Several pivotal, nonstandard geometric arguments require expansion and independent specialist replication, especially because Section 10 would invalidate published theorem statements for the proposed example.

# Scope, source status, and review method

## Source completeness and provenance

The reviewed archive, `s6_canonical_108_pages_audited.zip`, is complete as a reconstruction package. It contains ten modular source parts, a modular assembler, a monolithic source, a 108-page compiled PDF, an authority reassembly, build scripts, checksum manifests, page-by-page visual audits, and reconstruction provenance. The archive's own verification script passes. The modular and monolithic sources compile to byte-identical PDFs in the audited environment.

This establishes fidelity to the supplied authority PDF, not authorship of the TeX source and not mathematical correctness. The archive expressly states that it is an independent reconstruction rather than the author's original TeX. For any formal submission, an author-controlled source or an explicit author sign-off on the reconstructed canonical PDF is necessary.

The earlier review package was based on an incomplete 155-line assembler plus packet 06. Its conclusion that the main theorem was directly contradicted by CDP20 was a correct description of the logical conflict visible in that slice, but an incorrect final assessment of the complete manuscript because Section 10 was unavailable. This report replaces that review in full.

## Review procedures

The audit used four complementary procedures.

First, I read the complete proof dependency chain rather than reviewing isolated claims. In particular, I traced the construction from the monodromy representation through the period family, the three local fillings, the global gluing, both integral topology computations, smooth recognition, analytic invariants, and the literature-conflict analysis.

Second, I independently reproduced exact computations with integer and symbolic arithmetic. The supplied audit package contains `audit/exact_checks.py` and a machine-readable result file. Twenty-eight checks pass. These include monodromy orders, contragredient matrices, fixed lattices, the invariant alternating form, Smith normal forms, exterior-power monodromy, Wang ranks, saturation tests, the fundamental-group determinant, the period transformation identities, the Neron-Severi polynomial, and the Hermitian Gram determinant.

Third, I compared the two topology routes. The first route uses an explicit collapse and Mayer--Vietoris. The second uses the integral Leray spectral sequence and Appendix B's nearby-cycle specialization theorem. Agreement between genuinely different calculations is significant evidence, although it is not a substitute for verifying their shared geometric inputs.

Fourth, I reviewed Section 10 as an argument about the exact printed proof mechanisms in Campana et al. (1998, 2020), not merely as an assertion that those papers are wrong. The review distinguishes: (a) the formal contradiction between conclusions; (b) the manuscript's proposed failure mechanism; and (c) whether that proposed mechanism has been independently validated.

## Meaning of audit labels

“Verified computationally” means that the displayed finite calculation has been reproduced exactly. “No contradiction found” means that the proof was read and its logical transitions appear coherent, but it is not a certification. “Major revision request” identifies a pivotal argument whose present exposition is too compressed for an extraordinary theorem, even where no specific counterexample has been found. “Confirmed error” is reserved for a statement or proof sentence for which a definite defect can be exhibited.

# The proof architecture and its dependency graph

The main theorem has the following dependency chain.

1. Sections 2--3 construct a rank-four integral local system over the $(3,4,\infty)$ orbifold and a nonpolarized holomorphic family of complex two-tori with monodromies of orders $3$, $4$, and unipotent type at the cusp.
2. Section 4 constructs a toric filling at the cusp from an infinite $A_2$ fan and a free, properly discontinuous $\Z^2$ action. Its central fibre $W$ is irreducible and nonnormal, with normalization $\dP_6$, three double curves, and two triple points.
3. Section 5 constructs the order-$3$ and order-$4$ logarithmic fillings, with reduced fibres bielliptic surfaces.
4. Section 6 glues the smooth family and three fillings into a compact complex threefold $X\to\Pone$ and records the discrete gluing parameter $\ell_0$.
5. Section 7 computes $\pi_1(X)$ and integral homology. For the chosen twists $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$, the controlling integer
   $$
   p=12\ell_0-4\ell_1-3\ell_2
   $$
   is $-1$. The manuscript gives two integral homology computations.
6. Section 8 uses the simply connected integral homology-sphere conclusion, Hurewicz--Whitehead theory, and $\Theta_6=0$ to identify $X$ diffeomorphically with $S^6$.
7. Section 9 computes algebraic dimension, direct images, the canonical bundle, Chern-number consequences, holomorphic forms, and automorphisms.
8. Section 10 explains why the printed CDP98/CDP20 proof mechanisms are claimed not to cover this $X$.

A fatal defect in Sections 2--6 would invalidate the space. A defect in either topology route could potentially be repaired by the other only if their shared local specialization and gluing data remain valid. A defect in Section 9 would not by itself destroy the complex structure on $S^6$, but it could remove the claimed contradiction with CDP20. A defect in Section 10 would reinstate the literature obstruction unless the published theorem itself were independently corrected.

# Section-by-section mathematical review

## Lattice and monodromy data (Section 2)

The matrices

$$
T_1=\begin{pmatrix}
1&0&-6&2\\0&-1&1&1\\0&-1&0&1\\0&0&0&1
\end{pmatrix},\qquad
T_2=\begin{pmatrix}
1&6&0&-3\\0&0&-1&1\\0&1&0&0\\0&0&0&1
\end{pmatrix}
$$

satisfy

$$
T_1^3=I,\qquad T_2^4=I,\qquad T_0=(T_1T_2)^{-1}=I+N,\qquad N^2=0.
$$

The exact orders are indeed $3$ and $4$. The displayed contragredients $A_j=(T_j^{-1})^t$ and $M_0=(T_0^{-1})^t$ are correct, and $A_1A_2M_0=I$. The invariant and vanishing-cycle lattices are also correct:

$$
\ker(M_0-I)=\im(M_0-I)=\langle\widehat w,\widehat\delta\rangle,
$$

and the induced map

$$
B_0:\overline\Lambda\to\Lambda_{\mathrm{tor}},\qquad
B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

is unimodular. The fixed lattices

$$
\Lambda^{A_1}=\langle\varepsilon,\widehat\delta\rangle,
\qquad
\Lambda^{A_2}=\langle\varepsilon',\widehat\delta\rangle
$$

are primitive rank-two sublattices with the stated generators.

The invariant alternating form $Q_0$ is also consistent. In the ordered basis $(\gamma,u,w,\delta)$, its nonzero entries are $Q_0(\gamma,\delta)=1$ and $Q_0(u,w)=6$. Direct multiplication gives $T_j^tQ_0T_j=Q_0$. The induced form

$$
b_N(x,y)=Q_0(x,Ny)
$$

on $V/\ker N$, in the basis $\bar w,\bar\delta$, is $\operatorname{diag}(6,-1)$. This confirms the manuscript's central nonpolarized feature: the monodromy-compatible alternating form has indefinite limiting form and does not define a polarization. This matters because standard polarized degeneration theorems cannot simply be imported (Clemens, 1977; Mumford, 1972).

The group-theoretic uniformization by the $(3,4,\infty)$ triangle group is standard. The manuscript carefully separates the uniformizing coordinate from the period coordinate at the cusp and derives the translation sign. I found no inconsistency in the presentation $\Delta\cong\Z/3*\Z/4$ or the definition of the representation.

**Disposition:** Exact algebra verified. No correction required, except that a concise table of all actions on $V$, $\Lambda$, and their exterior powers would reduce later sign risk.

## Period family (Section 3)

The period matrix is built from

$$
\sigma_1=6\mu\gamma+\tau u+w,
\qquad
\sigma_2=\beta\gamma+\mu u+\delta,
$$

with $F^1=\langle\sigma_1,\sigma_2\rangle$. The construction proceeds through three nontrivial analytic steps: a modular function $\tau$, a torsor solution $\mu$ for an automorphy sheaf of degree $-1$, and a solution $\beta$ to a further additive cocycle. The final imaginary constant is chosen so that the lattice remains nondegenerate.

The modular transformation laws used later are mutually consistent. The automorphy sheaf calculation in Lemma 3.10, including the degree $-1$ conclusion, is coherent: the chosen modular expression has the required character, and its divisor behavior at the cusp gives $\mathscr L\simeq\cO(-1)$. Because a square-root factor is used, the argument would be clearer if formulated invariantly in terms of the orbifold line bundle and its character, rather than by an implicitly chosen branch. I did not find a contradiction in the present construction.

The nondegeneracy argument is important. It is not enough that $\Pi(z)$ be formally equivariant; its four real columns must span a full lattice in $\C^2$. The manuscript reduces the determinant to an inequality involving

$$
D=\operatorname{Im}\beta-\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}
$$

and uses the free imaginary constant in $\beta$ to force $D<0$ throughout a compact fundamental domain. The proper-discontinuity and compactness input makes this strategy plausible. The same expression later controls the signature of the Hermitian form associated with $\eta$.

The cusp asymptotic decomposition

$$
Z=sB_0+C(t_c)
$$

is the precise bridge to the toric filling. I checked the equivariance and the exponential identity that produces the torus element $c_{\bar\lambda}(t_c)$. No algebraic inconsistency was found.

**Disposition:** No fatal defect found. For publication, the torsor existence and the global nondegeneracy choice should be stated as standalone propositions with explicit cohomology groups and norm estimates. The current proof is credible but densely packed.

## Toric filling at the cusp (Section 4)

The fan consists of cones over the cells of the periodic $A_2$ triangulation at height one. Every maximal cone is unimodular because the edge differences form a $\Z^2$ basis. Local finiteness of the triangulation gives a Hausdorff, second-countable toric complex manifold, and the character $t=\chi^{(0,0,1)}$ has reduced normal-crossing divisor

$$
t^{-1}(0)=\bigcup_{v\in\Z^2}E_v.
$$

The action

$$
\Psi_{\bar\lambda}=\tau_{\bar\lambda}\circ\Phi_{\bar\lambda}
$$

combines integral translation of the fan with a $t$-dependent torus translation. The manuscript does more than assert properness: it introduces a rescaled position map and obtains a quantitative displacement estimate. Since $B_0$ is orthogonal and unimodular, large group elements move compact sets apart uniformly near the cusp. The compact fundamental-set argument then yields properness of the quotient map to the disc.

The action is free. On the central fibre, the fan translation is free on irreducible components; away from the central fibre, the action corresponds to a free lattice translation on the torus cover. The quotient therefore has local models

$$
t=z_0,
\qquad t=z_0z_1,
\qquad t=z_0z_1z_2,
$$

and is smooth. The invariant logarithmic/top form gives the asserted relative canonical trivialization.

The normalization and conductor combinatorics are consistent. A fundamental component is $\dP_6$; opposite sides of its toric hexagon are identified. This yields three rational double curves and two triple points. The orbit stratification

$$
W=(\C^*)^2\sqcup 3\C^*\sqcup\{P,Q\}
$$

gives $e(W)=2$.

I found one definite exposition defect. Proposition 4.7(iv) says the image of the section is closed because it is “proper over $\Delta$.” That is not the correct reason when the base is an open disc. The conclusion is readily repaired: a continuous section of a Hausdorff map has closed graph/image, or one may prove closedness directly in the chosen quotient chart. This does not threaten the construction.

The highest-risk part of Section 4 is not a visible algebraic error but the global topological bookkeeping for an infinite fan and quotient. The manuscript contains the needed ideas, yet a publication version should consolidate them into one theorem: local finiteness, second countability, freeness, proper discontinuity, compact fundamental domain, and compatibility of the toric deformation with the group action.

**Disposition:** No theorem-breaking defect found. One minor proof sentence should be corrected; global quotient topology deserves expansion.

## Finite-order logarithmic fillings (Section 5)

The local family over the linearizing disc carries an affine transformation whose linear part is $A_j$ and whose translation part is $v_j/m_j$. The admissibility conditions ensure that the affine cyclic action is free. The fixed-point criterion is correctly reduced to membership of the translation vector in $(A_j-I)$ of the torus lattice, and the chosen vectors avoid that image.

The quotient produces a smooth threefold with multiple fibre $m_jS_j$. The reductions $S_j$ are bielliptic surfaces. The computed first homology and torsion are compatible with the standard Bagnera--de Franchis classification (Barth et al., 2004). The order-$3$ and order-$4$ cases also generate the precise local specialization indices later used in Section 7.

The logarithmic regluing section is arranged so that the transformed zero section is invariant. The conjugation identity used to compare the punctured family with the quotient is correct. The resulting drift controls $\ell_j=\gamma(v_j)$.

**Disposition:** No fatal error found. The proof would be more auditable with a single diagram showing the cover, affine action, quotient, multiple fibre, reduction, and boundary identification. The classification of the two bielliptic surfaces should be tied explicitly to the standard notation in Barth et al. (2004).

## Global gluing and compactness (Section 6)

The three local models are glued to the smooth family over $B^\circ$. The overlap maps are biholomorphisms by construction. The manuscript addresses Hausdorffness through shrinkable collars and the fact that each local piece maps properly to a disc. Properness of the global map is local on the base for a separated holomorphic map; the resulting total space is compact because the base is compact and the map is proper.

The zero section is used as more than notation: it fixes the lift of boundary meridians and prevents hidden fibre translations in the finite-order gluings. At the cusp, affine regluing changes the discrete parameter $\ell_0$, and the tautological gluing gives $\ell_0=0$.

No incompatibility was found among the boundary identifications. The proof is nevertheless unusually sensitive to the distinction between the smooth fibre lattice, the toric translation lattice, and the quotient of $\Lambda$ by $\Lambda_{\mathrm{tor}}$. A one-page gluing table should identify, for every boundary component, the deck group, meridian, fibre translation, orientation, and induced relation in $\pi_1$.

**Disposition:** Coherent. Major revision only in presentation and auditability, not because of a demonstrated flaw.

## Fundamental group (Section 7.5)

After attaching the cusp filling, the normal closure of $\Lambda_{\mathrm{tor}}$ is $\ker\gamma$. Hence the image of the fibre group is generated by one central element $c$. The two finite fillings impose

$$
x^3=c^{\ell_1},\qquad y^4=c^{\ell_2},
$$

and the cusp relation gives $xy=c^{\ell_0}$. Thus

$$
\pi_1(X)=\langle c,x,y\mid c\text{ central},\ xy=c^{\ell_0},\ x^3=c^{\ell_1},\ y^4=c^{\ell_2}\rangle.
$$

Eliminating $y$ makes the group abelian with relation matrix

$$
R=\begin{pmatrix}
3&-\ell_1\\
4&\ell_2-4\ell_0
\end{pmatrix},
\qquad
\det R=-(12\ell_0-4\ell_1-3\ell_2).
$$

Because the entries include $3$ and $4$, the first Smith invariant is $1$; hence

$$
\pi_1(X)\cong\Z/|p|,
\qquad
p=12\ell_0-4\ell_1-3\ell_2.
$$

The admissibility congruences imply $\gcd(p,12)=1$. For $(0,1,-1)$, $p=-1$ and the group is trivial. For the comparison sign, $p=-7$.

These calculations pass exact Smith-normal-form checks. The manuscript's long sign lemma is not redundant: a relative sign error would interchange the simply connected and $\Z/7$ examples. I found its treatment internally consistent. The final invariant $|p|$ is orientation-independent, but the manuscript should provide a compact convention table because the proof currently requires the reader to track clockwise meridians through several covers.

**Disposition:** Algebra verified. No mathematical correction required.

## First integral homology route: collapse and Mayer--Vietoris (Sections 7.1--7.6)

The first route constructs an equivariant collapse of a nearby torus fibre onto the singular fibre. The central fibre has homology

$$
H_k(W;\Z)=(\Z,\Z^2,\Z^4,\Z^2,\Z),
\qquad k=0,\ldots,4.
$$

The boundary mapping torus has Wang ranks

$$
(1,3,6,6,3,1).
$$

The kernel of its map to $W$ is described by the toric meridian and the two vanishing-cycle tori. Attaching the remainder of the fibration and computing the relevant quotient maps gives, for admissible data,

$$
H_k(X;\Z)\cong\Z/|p|\quad (1\le k\le4),
$$

with $H_0=H_6=\Z$ and the remaining groups determined by duality. For $p=\pm1$, the middle homology vanishes.

The exterior-power monodromy and all displayed lattice ranks are correct. In particular, for

$$
M_0=\begin{pmatrix}
1&0&0&0\\0&1&0&0\\0&1&1&0\\-1&0&0&1
\end{pmatrix},
$$

the Wang ranks are exactly $(1,3,6,6,3,1)$. The image of $\bigwedge^2M_0-I$ is the saturated rank-two lattice generated by the stated vectors. The matrix called $\alpha_2$ has rank $3$, gcd of its nonzero $3\times3$ minors equal to $1$, and the displayed primitive left-kernel generator.

The unresolved risk is geometric: Proposition 7.2's global collapse is elaborate. The manuscript constructs it using polar coordinates, a honeycomb subdivision, and lifted deformation retractions. It appears designed to address continuity across double and triple strata and equivariance under the toric lattice. I did not locate a discontinuity or an equivariance failure. Nevertheless, this is one of the places where an independent topology specialist should reconstruct the map rather than merely inspect the prose. A cell-level chain model or an explicit diagram would substantially improve verifiability.

**Disposition:** All finite algebra checks pass. The collapse theorem remains a major specialist-verification item.

## Second integral homology route: Leray spectral sequence (Section 7.7)

The second route is structurally independent. Let $j:B^\circ\hookrightarrow B$ and let $\mathcal L^q$ be the local system with fibre $\bigwedge^qV$. The manuscript identifies $R^qf_*\Z$ as a subsheaf of $j_*\mathcal L^q$, with local quotient skyscrapers determined by specialization at the three special fibres.

At the finite fibres the pullback lattices have the claimed indices. In degree one, the indices are $3$ and $4$. At the order-$4$ fibre there is an additional index $2$ in degrees two and three. The degree-two conclusion follows from the invariant-lattice Gram determinant and evenness of the bielliptic intersection form. The degree-three index follows by pairing with the degree-one image. These calculations are correct at the lattice level.

At the cusp, Theorem B.1 asserts that specialization is injective and its image is the full $T_0$-invariant lattice in every degree. Consequently the global sections are

$$
H^0(B,R^1)=12\Z\gamma,
\quad
H^0(B,R^2)=\Z\cdot2q,
\quad
H^0(B,R^3)=\Z\cdot2\gamma uw,
\quad
H^0(B,R^4)=12\Z\operatorname{vol}.
$$

The coinvariant groups in degree two are torsion-free, with $[uw]=6[\gamma\delta]$. The parabolic cohomology groups $H^1(B,R^1)$ and $H^1(B,R^2)$ vanish by the displayed intersection calculations.

Multiplicativity reduces all nonzero $d_2$ maps to the same integer, up to sign. The geometric extension class is $p=12\ell_0-4\ell_1-3\ell_2$. Hence, for $p=\pm1$, the spectral sequence yields the cohomology of $S^6$.

I independently checked the arithmetic underlying the multiplicative argument. The difficult input is not the final differential calculation but the integral identification of the cusp specialization lattice. That input is reviewed separately below.

**Disposition:** Internally consistent and strongly corroborative. Conditional on Appendix B, the second route is persuasive.

## Recognition as the smooth six-sphere (Section 8)

Once $X$ is simply connected and has the integral homology of $S^6$, the Hurewicz theorem and Whitehead's theorem make it a homotopy $6$-sphere. Smooth homotopy $6$-spheres are classified by $\Theta_6$, and $\Theta_6=0$ (Kervaire & Milnor, 1963). Thus the diffeomorphism conclusion follows.

This step is standard and correct, conditional on Section 7. The manuscript could make explicit that the smooth structure is oriented by the complex orientation, although in dimension six there is no exotic sphere ambiguity.

**Disposition:** Valid conditional deduction.

## Algebraic dimension (Section 9.1)

The Neron--Severi calculation begins with the condition

$$
E\wedge\sigma_1\wedge\sigma_2=0.
$$

For a general integral two-form $E$, the manuscript obtains a polynomial $P_E$ in $1,\tau,\mu,\beta$, and $6\mu^2-\tau\beta$. The symbolic expansion is correct. Lemma 9.3 proves these five holomorphic functions are linearly independent by applying the $g_0$ and $g_2$ transformation laws. I reproduced the successive-difference identities.

It follows that the very general fibre has

$$
\NS(F_b)=\Z\eta,
\qquad
\eta=u\wedge w+6\gamma\wedge\delta.
$$

The square is

$$
\eta^2=12.
$$

The associated Hermitian Gram matrix is

$$
G_\eta=
\begin{pmatrix}
2\operatorname{Im}\tau&2\operatorname{Im}\mu\\
2\operatorname{Im}\mu&\frac13\operatorname{Im}\beta
\end{pmatrix},
$$

with determinant

$$
\det G_\eta=
\frac23\operatorname{Im}\tau
\left(
\operatorname{Im}\beta-
\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}
\right)<0.
$$

Thus $\eta$ has signature $(1,1)$ and no nonzero multiple is semipositive. The manuscript concludes that the very general torus has algebraic dimension zero. This is consistent with the standard theory of divisors on complex tori: effective divisors induce semipositive Hermitian forms, while algebraic dimension one for a two-torus is governed by a nonzero isotropic semipositive class (Birkenhake & Lange, 2004; Lange & Birkenhake, 1999). Because the proof compresses this classification step, it should state the exact proposition being used.

A meromorphic function on $X$ restricts to a constant on very general fibres. The manuscript then proves that constancy on uncountably many fibres forces descent to the base. Hence

$$
\mathcal M(X)=f^*\mathcal M(\Pone),
\qquad a(X)=1,
$$

and $f$ is the algebraic reduction.

**Disposition:** No contradiction found; exact period algebra verified. Add an explicit torus-classification citation or proof.

## Canonical bundle and direct images (Sections 9.2--9.4)

The relative two-form $e=d\zeta_1\wedge d\zeta_2$ transforms by $\det R_g$. Its behavior at the finite orbifold points gives fractional vanishing orders $2/3$ and $1/4$, and it is regular and nonvanishing at the cusp. The resulting direct image is

$$
f_*\omega_{X/B}\cong\cO_{\Pone}(1).
$$

The multiple-fibre correction yields

$$
K_X\cong f^*\cO(-1)\otimes\cO(2S_2).
$$

The character arithmetic is coherent. The non-torsion conclusion follows because the stated bundle has a nontrivial multiple-fibre component and its appropriate power is a nontrivial pullback.

For the structure-sheaf direct images, the manuscript obtains

$$
f_*\cO_X=\cO,
\qquad
R^1f_*\cO_X\cong\cO\oplus\cO(-1),
\qquad
R^2f_*\cO_X\cong\cO(-1).
$$

The fibre cohomology at $W$ is computed by the normalization/conductor sequence. The finite multiple fibres are handled by equivariant local models and descending induction through the nilpotent thickening. Relative duality identifies the top direct image. The eigenweights determine the splitting of $R^1$.

I found no algebraic inconsistency, and the resulting global Hodge numbers agree with the Leray calculation. The main concern is the precision of the analytic foundations. In a theorem of this importance, references to Grauert, base change, and relative duality should be attached to exact statements and hypotheses. The reader should not have to infer that the scheme-theoretic multiple fibres are covered, that the relevant sheaves are flat, and that duality applies to the Gorenstein nonnormal surface $W$.

**Disposition:** Plausible and internally consistent. Major revision requested for exact analytic theorem statements.

## Holomorphic forms, automorphisms, and Chern data (Sections 9.5--9.7)

The vanishing of global holomorphic $p$-forms is derived by writing invariant forms on the universal cover and using the period derivatives and local growth at the cusp and orbifold points. The weight-zero and weight-one lemmas eliminate the remaining coefficients. The argument is technically detailed and consistent with the computed $h^{0,q}$.

The identity component of the automorphism group must preserve the algebraic reduction and hence acts fibrewise. Translation vector fields correspond to the invariant lattice line $\Lambda^\Delta=\Z\widehat\delta$, giving a one-dimensional vertical field. Its flow is $\C^*$ rather than an elliptic translation group because of the degeneration. The toric fixed set is one rational double curve with normal weights $(+1,-1)$. This is compatible with $e(X^{\C^*})=e(X)=2$.

Because $H^2(X;\Z)=H^4(X;\Z)=0$, $c_1$ and $c_2$ vanish integrally. The top Chern number equals the Euler characteristic,

$$
\langle c_3(T_X),[X]\rangle=e(X)=2.
$$

The Riemann--Roch arithmetic giving $\chi(\cO_X)=0$, $\chi(\Omega_X^1)=-1$, and $\chi(T_X)=1$ is consistent.

**Disposition:** No contradiction found. These conclusions remain conditional on the topology and direct-image calculations.

# Appendix B: integral specialization at the nonnormal cusp

Appendix B is one of the two most important parts of the manuscript. It is intended to remove reliance on the geometric collapse for the statement

$$
\im\bigl(H^q(W;\Z)\to H^q(F;\Z)\bigr)
=H^q(F;\Z)^{T_0}
$$

and to establish injectivity and saturation integrally.

## Nearby-cycle sheaves

The local normal-crossing models give Milnor fibres of homotopy type point, $S^1$, and $T^2$. Therefore

$$
\mathcal H^0\psi=\Z_W,
\qquad
\mathcal H^1\psi=\mathcal V,
\qquad
\mathcal H^2\psi=\Z_P\oplus\Z_Q.
$$

The global orientation convention along the three double curves determines the restriction maps at the two triple points. In both cases the image consists of triples satisfying

$$
n_1-n_2+n_3=0.
$$

Thus the exact sequence

$$
0\to\mathcal V\to\bigoplus_{k=1}^3\iota_{k*}\Z_{\bar C_k}
\xrightarrow{\delta_1}\Z_P\oplus\Z_Q\to0
$$

is correct provided the branch labels and orientations are those fixed in the normalization. The manuscript performs the sign check explicitly at both triple points.

## The $E_2$ page

The normalization/conductor resolution gives

$$
H^\bullet(W;\Z)=(\Z,\Z^2,\Z^4,\Z^2,\Z),
$$

all free. The calculation of $H^\bullet(W;\mathcal V)$ gives

$$
(\Z^2,\Z,\Z^3,0),
$$

and the top nearby-cycle row contributes $\Z^2$ in bidegree $(0,2)$. The total rank on the $E_2$ page is $18$, while the smooth torus fibre has total Betti number $16$. Hence exactly one rank must be killed.

The degree-by-degree rank bookkeeping forces all differentials touching the bottom row to vanish except for the one needed in total degree three. This part is internally consistent. Since all groups are free, rank information does not by itself prove saturation; the appendix addresses that separately.

## Saturation and the degree-three Gysin argument

The key additional input is a compactly supported cycle transported along a torus orbit. The manuscript constructs a local trivialization near that orbit, uses the Gysin map to identify a primitive degree-three class, and shows that specialization has rank two and saturated image in degree three. Poincare duality and multiplicativity then propagate the saturation and invariant-lattice identification to all degrees.

I did not locate a rank mismatch, sign inconsistency, or circular dependency. Appendix B explicitly states which parts still rely on the geometric collapse: the identification of particular generators and normalizations, not the injectivity and invariant-image theorem used by the Leray route.

The revision problem is exposition and independent reproducibility. The argument should state the nearby-cycle functor, the specialization morphism, the edge map, and the compact-support/Gysin construction in a standard derived-category framework, with precise integral references such as Deligne's SGA 7 formalism or a modern equivalent (Deligne, 1973; Dimca, 2004; Kashiwara & Schapira, 1990). The present argument is plausible, but it is too consequential to leave any ambiguity about conventions or functoriality.

**Disposition:** No fatal defect found; highest-priority specialist verification item.

# Section 10 and the conflict with CDP98/CDP20

## The formal contradiction

If the manuscript's main conclusions hold, then $X$ satisfies

$$
H^1(X;\Z)=H^2(X;\Z)=0,
\qquad a(X)=1,
$$

and has a holomorphic algebraic reduction $f:X\to\Pone$. Campana et al. (2020, Theorem 2.2) print, under those hypotheses, $c_3(X)\le0$, and their Corollary 2.3 prints $a(X)=0$ for a compact complex threefold homeomorphic to $S^6$. The manuscript instead has $c_3(X)=2$ and $a(X)=1$. Both sets of conclusions cannot simultaneously be correct.

The complete manuscript does not evade this issue. It isolates two exact proof mechanisms and argues that one is irreparably false at the nonnormal fibre $W$, while the other is a monodromy error that can be repaired for this example.

## The nonnormal-fibre cotangent mechanism

Let $S$ be a reduced normal-crossing fibre in a smooth threefold $\mathcal X\to\Delta$, with normalization $\eta:\widetilde S\to S$ and conductor $D$. Locally the defining function is $g=ux$, $uxy$, or $uxyz$. The differential $dg|_S$ is nonzero away from the conductor but restricts to zero on the conductor.

For a line bundle $A$ on $S$ whose pullback to $\widetilde S$ is trivial, choose a nowhere-zero pullback section $e$. The normalization/conductor Mayer--Vietoris sequence lets the pair

$$
\bigl(\eta^*(dg|_S)\otimes e,0\bigr)
$$

descend to a nonzero section

$$
s\in H^0(S,\Omega^1_{\mathcal X}|_S\otimes A).
$$

Its image in $\Omega_S^1\otimes A$ is supported on the conductor and is torsion. Therefore its image in the torsion-free quotient

$$
\widetilde\Omega_S^1=\Omega_S^1/\mathcal T(\Omega_S^1)
$$

is zero. If $A$ is nontrivial, $s$ does not arise from the conormal line. This produces exactly the type of ambient cotangent section that is invisible to a vanishing statement for $\widetilde\Omega_S^1\otimes A$.

This is the strongest part of the manuscript's rebuttal. The local formulas are elementary and the descent through the conductor sequence is explicit. The mechanism shows that the implication

$$
H^0(S,\widetilde\Omega_S^1\otimes A)=0
\quad\Longrightarrow\quad
H^0(S,\Omega^1_X|_S\otimes A)=0
$$

is not valid for nonnormal $S$ merely from vanishing of the conormal contribution. For normal $S$, extension across codimension two can restore the argument; for the nonnormal surface $W$, the conductor supports the obstruction.

For the constructed $W$, every line bundle from $X$ pulls back trivially to the normalization $\dP_6$ because $c_1=0$ and $\Pic(\dP_6)\hookrightarrow H^2(\dP_6;\Z)$. Serre--Grothendieck duality then gives

$$
H^2\bigl(W,(T_X\otimes L)|_W\bigr)^*
\cong
H^0\bigl(W,\Omega_X^1|_W\otimes(L^*\otimes\omega_X)|_W\bigr)
\ne0.
$$

Top-degree cohomology and base change imply $R^2f_*(T_X\otimes L)\ne0$. The manuscript therefore claims that the hypothesis used by Campana et al. (2020, Proposition 2.4) holds for no $L$ on this $X$.

I found no local algebra error in this mechanism. The remaining burden is to state the exact analytic duality and top-degree base-change theorems with all hypotheses. Because this argument would invalidate a published theorem's application, it must be independently refereed by experts in nonnormal complex spaces and analytic duality.

## The monodromy-coinvariant correction

The second issue concerns a split group extension

$$
1\to K\to G\to Q\to1.
$$

The correct abelianization is

$$
G^{\mathrm{ab}}\cong Q^{\mathrm{ab}}\oplus(K^{\mathrm{ab}})_Q,
$$

where the second summand consists of coinvariants under conjugation. It is not generally $Q^{\mathrm{ab}}\oplus K^{\mathrm{ab}}$ unless the action is trivial. This is standard group homology.

For the manuscript's torus fibration, the unipotent monodromy acts nontrivially on $H_1(F;\Z)$. The coinvariant rank is one, not four. Consequently, formulas in the printed CDP98/CDP20 route that use $b_1(F)$ rather than the coinvariant rank do not apply to this example. This also explains how

$$
H^1(X,\cO_X)\cong\C
$$

can coexist with

$$
H^1(F,\cO_F)\cong\C^2
$$

without surjectivity of restriction.

The manuscript then proves by a separate countability argument that a line bundle non-torsion on every fibre nevertheless exists. Thus the monodromy problem breaks the printed route to that input but can be repaired for this example. By contrast, the nonnormal cotangent reduction remains unavailable.

The group-theoretic correction is correct. Its application to the exact sequence in CDP98 should still be checked against the precise local topological model and notation in the original paper, but the mathematical principle is not in doubt.

## Referee assessment of the literature dispute

The earlier packet-only report treated CDP20 as an external theorem that immediately refuted the manuscript. That treatment is no longer defensible after reading Section 10. The manuscript supplies a concrete countermechanism, not a generic assertion of exception.

The appropriate present conclusion is narrower:

- The manuscript and the printed CDP20 conclusions are formally incompatible.
- Section 10 gives a coherent explanation of why the printed proof does not cover the proposed nonnormal fibre.
- This review found no internal defect in that explanation.
- The explanation has not, by virtue of this review, been externally adjudicated. Acceptance would effectively publish a counterexample to CDP20 and should involve independent referees familiar with the original proof.

# Confirmed errors and corrections

## Remark 7.28: quantifier error

The manuscript's residue characterization is false as a biconditional for a fixed triple. The triple

$$
(\ell_0,\ell_1,\ell_2)=(100,1,-1)
$$

has the listed residue pair, but

$$
p=12(100)-4(1)-3(-1)=1199\ne\pm1.
$$

The correct statement is:

> For fixed admissible $\ell_1,\ell_2$, there exists $\ell_0\in\Z$ such that $|12\ell_0-4\ell_1-3\ell_2|=1$ if and only if the residue pair is one of the two listed pairs.

Alternatively, the remark should retain the equation involving $\ell_0$ and not reduce it to residues alone. This error is not used in the chosen example and does not affect the main theorem.

## Proposition 4.7(iv): closed-image justification

The statement that the section image is closed because it is “proper over the disc” is not the correct proof. Replace it with the closed-graph argument for a section into a Hausdorff total space or an explicit quotient-chart proof. The conclusion remains valid.

# Major revision requirements

The following revisions are necessary before the manuscript could reasonably be accepted.

## 1. Isolate and expand the two topology engines

Proposition 7.2 and Appendix B should each be independently readable. The collapse proof needs a complete equivariance and continuity theorem, preferably with a cell-level model. Appendix B needs a formal nearby-cycle and specialization setup, precise integral references, and a fully diagrammed saturation argument. The manuscript should state exactly which conclusions are independent and which share inputs.

## 2. Make analytic base change and duality citation-complete

Proposition 9.13 and Theorem 10.5 rely on the most delicate analytic tools in the paper. For every use, state the morphism, sheaf, flatness hypothesis, fibre dimension, and exact conclusion. In particular, clarify top-degree base change at every scheme-theoretic fibre, duality on the Gorenstein nonnormal surface $W$, and the treatment of nilpotent multiple fibres.

## 3. Separate the CDP critique into a specialist-verifiable note

Section 10 should be presented with exact quotations, theorem numbers, and a commutative diagram showing the failed reduction. The local conductor construction should be stated as a general proposition independent of the example. The authors should seek independent comments from the authors of CDP20 or equivalent experts. This is not a demand for deference to the literature; it is a demand proportionate to overturning a published theorem.

## 4. Add a complete convention and gluing table

The signs, meridian orientations, deck generators, and translations should be summarized in one table. The manuscript's sign lemma is careful, but the information is dispersed. This is a preventable source of catastrophic error.

## 5. Strengthen provenance for a formal submission

Because the reviewed source is a reconstruction, a journal submission must be tied to an author-approved version. The reconstruction audit can remain supplementary evidence, but it cannot substitute for authorial verification that every formula and correction reflects the intended manuscript.

## 6. Correct the two confirmed local defects

Remark 7.28 and the proof sentence in Proposition 4.7(iv) should be corrected explicitly in a revision ledger.

# Computational audit

The accompanying script performs twenty-eight exact checks, all passing. It uses integer matrices, Smith normal forms, determinantal divisors, exterior powers, and symbolic polynomial identities. The checks include:

- $T_1^3=T_2^4=I$, exact orders, $T_1T_2T_0=I$, and $N^2=0$;
- the displayed contragredient matrices and their product relation;
- the fixed lattices, the unimodular map $B_0$, and invariance/signature of $Q_0$;
- the determinant and Smith normal form in Theorem 7.17;
- all admissible congruence classes proving $\gcd(p,12)=1$;
- the relation-lattice primitivity in Lemma 7.19;
- exterior-power monodromy, Wang ranks $(1,3,6,6,3,1)$, and the saturated image in degree two;
- the rank, saturation, and primitive left kernel of the displayed $\alpha_2$ matrix;
- a concrete counterexample to the literal wording of Remark 7.28 and verification of the corrected existential version;
- the expansion of $\sigma_1\wedge\sigma_2$ and the formula for $P_E$;
- the $g_0$ and $g_2$ transformation identities in Lemma 9.3;
- $\eta^2=12$, the Gram matrix $G_\eta$, and its determinant factorization;
- explicit bookkeeping of the formal CDP20 conflict and the fact that Section 10, not arithmetic, is where applicability is disputed.

These checks validate formulas, not geometric existence. In particular, a correct Smith normal form does not prove that the relation matrix is the correct topological attaching matrix; that depends on the gluing and sign arguments. The report maintains that distinction throughout.

# Final recommendation

I recommend **major revision and resubmission**, with the following editorial interpretation.

The manuscript should not be rejected merely by citing CDP20. The complete text gives a concrete and technically credible challenge to the proof step relevant to a nonnormal fibre. The earlier packet-only rejection rationale is superseded.

The manuscript also should not be accepted solely because no flaw was found in one extended review. It claims the first complex structure on $S^6$, uses a novel nonpolarized torus degeneration, depends on delicate integral specialization, and would falsify printed conclusions in the literature. The appropriate standard is independent replication of the cusp topology and the Section 10 analytic mechanism.

Subject to that replication, the proof architecture is serious. It is not a collection of unsupported claims: the construction is explicit, the finite algebra is unusually detailed, two topology computations agree, and the literature conflict is confronted directly. The confirmed errors are local and repairable. The unresolved issues are high-risk proof-verification issues, not demonstrated contradictions.

A revised manuscript should be sent to at least three specialist readers covering: (1) toric and semi-abelian degenerations with nonpolarized monodromy; (2) integral nearby cycles and topology of normal-crossing degenerations; and (3) compact complex threefolds, analytic duality, and the CDP98/CDP20 arguments. Acceptance should depend on affirmative reports from those domains.

# References

Agricola, I., Bazzoni, G., Goertsches, O., Konstantis, P., & Rollenske, S. (2018). On the history of the Hopf problem. *Differential Geometry and its Applications, 57*, 1--9.

Ash, A., Mumford, D., Rapoport, M., & Tai, Y.-S. (2010). *Smooth compactifications of locally symmetric varieties* (2nd ed.). Cambridge University Press.

Banica, C., & Stanasila, O. (1976). *Algebraic methods in the global theory of complex spaces*. Wiley.

Barth, W., Hulek, K., Peters, C., & Van de Ven, A. (2004). *Compact complex surfaces* (2nd ed.). Springer.

Birkenhake, C., & Lange, H. (2004). *Complex abelian varieties* (2nd ed.). Springer.

Bredon, G. E. (1997). *Sheaf theory* (2nd ed.). Springer.

Campana, F., Demailly, J.-P., & Peternell, T. (1998). The algebraic dimension of compact complex threefolds with vanishing second Betti number. *Compositio Mathematica, 112*, 77--91.

Campana, F., Demailly, J.-P., & Peternell, T. (2020). Corrigendum: The algebraic dimension of compact complex threefolds with vanishing second Betti number. *Compositio Mathematica, 156*, 679--696.

Clemens, C. H. (1977). Degeneration of Kahler manifolds. *Duke Mathematical Journal, 44*, 215--290.

Deligne, P. (1973). Le formalisme des cycles evanescents. In P. Deligne & N. Katz (Eds.), *Groupes de monodromie en geometrie algebrique (SGA 7 II)* (Lecture Notes in Mathematics 340, pp. 82--115). Springer.

Dimca, A. (2004). *Sheaves in topology*. Springer.

Fulton, W. (1993). *Introduction to toric varieties*. Princeton University Press.

Hatcher, A. (2002). *Algebraic topology*. Cambridge University Press.

Kashiwara, M., & Schapira, P. (1990). *Sheaves on manifolds*. Springer.

Kervaire, M. A., & Milnor, J. W. (1963). Groups of homotopy spheres I. *Annals of Mathematics, 77*, 504--537.

Lange, H., & Birkenhake, C. (1999). *Complex tori*. Birkhauser.

Mumford, D. (1972). An analytic construction of degenerating abelian varieties over complete rings. *Compositio Mathematica, 24*, 239--272.

Ramis, J.-P., & Ruget, G. (1970). Complexe dualisant et theoremes de dualite en geometrie analytique complexe. *Publications Mathematiques de l'IHES, 38*, 77--91.

Ramis, J.-P., Ruget, G., & Verdier, J.-L. (1971). Dualite relative en geometrie analytique complexe. *Inventiones Mathematicae, 13*, 261--283.

Smale, S. (1961). Generalized Poincare's conjecture in dimensions greater than four. *Annals of Mathematics, 74*, 391--406.

# Appendix A: audit disposition by central claim

| Central claim | Audit disposition | Principal dependency | Required follow-up |
|---|---|---|---|
| Smooth compact complex threefold $X$ exists | No fatal defect found | Sections 2--6 | Independent review of infinite toric quotient and gluing |
| $\pi_1(X)=1$ | Exact algebra verified, conditional on attaching relations | Section 7.5 | Orientation/gluing table |
| $H^*(X;\Z)=H^*(S^6;\Z)$ | Two routes agree; not fully certified | Sections 7.2--7.7, Appendix B | Replicate collapse and nearby-cycle specialization |
| $X\cong_{\mathrm{diff}}S^6$ | Standard conditional consequence | Section 8 | None beyond topology verification |
| $a(X)=1$ | Coherent; period algebra verified | Section 9.1 | Expand torus algebraic-dimension criterion |
| Direct images and $K_X$ | Plausible | Sections 9.2--9.4 | Exact base-change/duality statements |
| $c_3(X)=2$ | Conditional on topology | Sections 7--9 | No separate arithmetic issue |
| CDP20 does not apply | Substantive rebuttal; not externally adjudicated | Section 10 | Specialist independent review and literature response |

# Appendix B: supersession notice

This report supersedes the prior packet-06 review. That earlier review correctly identified the formal incompatibility between the claims visible on pages 56--66 and the printed CDP20 conclusions, but it did not have the complete manuscript. In particular, it lacked Section 10, Appendix B, and the complete construction. Its recommendation of rejection on the ground of an unrebutted CDP20 contradiction is withdrawn. The exact packet-06 arithmetic findings remain useful and have been incorporated into the present full-manuscript checks.

# Appendix C: reproducibility

The review bundle contains:

- `report/full_mathematical_peer_review.pdf`, the primary report;
- `report/full_mathematical_peer_review.md` and `.tex`, editable sources;
- `audit/issue_ledger.csv` and `.json`;
- `audit/theorem_dependency_matrix.csv`;
- `audit/exact_checks.py`, `exact_checks_results.json`, and execution logs;
- `evidence/archive_verify_stdout.txt` and reconstruction-audit extracts;
- `evidence/source_page_line_map.csv` and `.md`;
- `MANIFEST.sha256` and a review receipt.

To rerun the arithmetic audit from the bundle root:

```bash
python audit/exact_checks.py
```

To rebuild the report, use Pandoc with XeLaTeX or compile the included generated LaTeX source. The PDF was rendered at 200 dpi and preflighted before packaging.

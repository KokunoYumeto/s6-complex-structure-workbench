---
title: "Independent Mathematical Proof Audit - Revised Integrated Edition"
subtitle: "Corrective addendum, results map, and preserved original audit"
author: "Independent reconstruction audit"
date: "25 August 2026"
geometry: margin=0.82in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
toc: true
toc-depth: 3
header-includes:
  - \usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array}
  - \usepackage[T1]{fontenc}
  - \newcommand{\Z}{\mathbb Z}
  - \newcommand{\C}{\mathbb C}
  - \newcommand{\Pone}{\mathbb P^1}
  - \newcommand{\M}{\mathcal M}
  - \newcommand{\spmap}{\operatorname{sp}}
---

# Editorial record

This revised edition preserves the original proof audit verbatim after a dated corrective addendum. The original report was a good-faith assessment of the proof path then reconstructed; the new material identifies the exact morphism-level conflation that made its topology verdict too negative, audits the independent nearby-cycle/Leray route, and updates the status without deleting the historical record.

\newpage

# Correction notice

This addendum changes the mathematical assessment issued in the earlier report titled *Independent Mathematical Proof Audit*.

The earlier report gave the disposition

> **MAJOR REVISION - MAIN THEOREM NOT CERTIFIED.**

That disposition was supported by four asserted unresolved obligations: the cusp-collapse map, the integral specialization map, the based van Kampen inclusions, and the identification of the displayed Mayer-Vietoris/Leray maps with the geometry. After integrating the reconstructed full source and auditing the arguments that were previously underweighted, that statement is too broad.

The exact correction is:

> **The cusp-collapse route remains incompletely certified, but it is not required for the manuscript's second topology proof. Appendix B constructs the intrinsic nearby-cycle specialization map, Section 7.7 uses that map in the Leray spectral sequence, and Section 7.5 supplies the based van Kampen computation. I found no load-bearing defect in that non-collapse route. The previous topology-based rejection is therefore withdrawn.**

The current assessment is a **provisional positive mathematical review with focused verification requests**, rather than a rejection or a claim of completed journal certification.

# Evidence integrated

The integration used three classes of evidence.

1. The canonical 108-page source and matching PDF.
2. The prior exact-arithmetic harness and theorem/risk ledgers.
3. A supplied progress record from a second validation/reconstruction effort. That record reports a direct proof of $a(X)=1$, a separate nearby-cycle/Leray topology argument, 28/28 and 38/38 exact-check passes, two corrected transcription defects in the new proof layer, and a policy of withholding the word "verified" from compressed geometric steps.

The actual workbench files named in the progress record were not supplied here. I therefore did not treat their existence or their reported compilation as evidence by itself. Instead, I located and audited the corresponding arguments in the canonical source: Section 9.1 for algebraic dimension, Appendix B for nearby cycles, Sections 7.5 and 7.7 for topology, and Section 10 for the non-normal fibre mechanism.

# The precise mathematical mistake in the earlier audit

The earlier report effectively required an integral identification

$$
\spmap^q=c^*:H^q(W;\Z)\longrightarrow H^q(F;\Z)
$$

before accepting the homology computation. That requirement belongs to the collapse/Mayer-Vietoris route. It is not a premise of the Leray route.

The canonical source defines the intrinsic map

$$
\spmap^q:
(R^qf_*\Z)_{p_0}=H^q(W;\Z)
\longrightarrow
(j_*j^*R^qf_*\Z)_{p_0}=H^q(F;\Z)^{T_0}.
$$

Appendix B proves directly, using nearby cycles, that this is an integral isomorphism onto the invariant lattice. The proof does not use the homotopy equivalence $N'_0\simeq W$, the collapse map $c$, or the first Mayer-Vietoris computation. The source then states explicitly that identifying $\spmap^q$ with $c^*$, and fixing certain degree-two generators, remains part of the collapse route.

Thus the two statements are related by the following exact dependency:

$$
\text{collapse construction}
\Longrightarrow
\spmap^q=c^*,
$$

while

$$
\text{Appendix B}
\Longrightarrow
\spmap^q:H^q(W;\Z)\xrightarrow{\sim}H^q(F;\Z)^{T_0}
$$

without the collapse construction. Section 7.7 uses the second arrow, not the first implication.

This discharges the earlier objection R2 as an objection to the main $S^6$ theorem. It does not certify the explicit collapse description.

# Re-audit of Appendix B

## Local nearby-cycle sheaves

For the three local models

$$
t=z_0,\qquad t=z_0z_1,\qquad t=z_0z_1z_2,
$$

the Milnor fibres are homotopy equivalent to

$$
\mathrm{pt},\qquad S^1,\qquad T^2.
$$

Consequently

$$
\mathcal H^0\psi=\Z_W,
\qquad
\mathcal H^1\psi=\mathcal V,
\qquad
\mathcal H^2\psi=\Z_P\oplus\Z_Q,
\qquad
\mathcal H^{\ge3}\psi=0.
$$

At each triple point, the three restriction values of a class in $\mathcal V$ satisfy

$$
n_1-n_2+n_3=0.
$$

The source computes the same sign relation at both triple points from the ordered branches. I checked the branch-pair calculation and found it consistent.

## Cohomology of $W$ and $\mathcal V$

The normalization/conductor resolution gives

$$
H^q(W;\Z)\cong \Z^{1,2,4,2,1}
$$

in degrees $0,\ldots,4$. The exact sequence for $\mathcal V$ gives the free cohomology ranks used in the spectral sequence. No torsion is introduced in these computations.

## Spectral-sequence ranks

The hypercohomology spectral sequence

$$
E_2^{a,b}=H^a(W;\mathcal H^b\psi)
\Longrightarrow H^{a+b}(F;\Z)
$$

has only three nonzero rows. The rank equations force all differentials touching the zero row to vanish except for one remaining degree-three possibility.

The degree-three question is resolved by a compact-support specialization lemma and a Gysin map along a $T_f$-orbit $K\cong T^2$ in the smooth locus of $W$. The corresponding orbit $K_t\subset F_t$ is a translate of the linear subtorus defined by the saturated lattice $\Lambda_{\mathrm{tor}}\subset\Lambda$. Its Gysin image is therefore a saturated rank-two direct summand of $H^3(F_t;\Z)$. This forces $\spmap^3$ to be injective of rank two with saturated image.

The exact finite check independently reproduces:

$$
\operatorname{rk}(\bigwedge^qV)^{T_0}=(1,2,4,2,1)
$$

and shows that each image $(\bigwedge^qT_0-I)\bigwedge^qV$ is saturated. Equal rank plus saturation then identifies the specialization image with the invariant lattice.

**Audit result:** Appendix B is no longer classified as a missing integral map. Its proof has been reconstructed through the local sheaves, rank equations, degree-three Gysin argument, and saturation step. The standard nearby-cycle formalism cited at the start remains an external theorem input, not an omitted manuscript argument.

# Re-audit of the Leray topology computation

Let $R^q=R^qf_*\Z$ and $\mathcal L^q=j^*R^q$. Appendix B gives equality of $R^q$ with $j_*\mathcal L^q$ at $p_0$. The finite fibres give the remaining local index data. Section 7.7 obtains

$$
H^0(B,R^1)=12\Z\gamma,
\quad
H^0(B,R^2)=2\Z q,
\quad
H^0(B,R^3)=2\Z\gamma uw,
$$

and the relevant parabolic cohomology groups vanish.

Proposition 7.27 does not infer the first transgression from the desired answer. It constructs local lifts and evaluates their discrepancies on the three based meridians. The result is

$$
d_2^{0,1}(12\gamma)=\pm
(12\ell_0-4\ell_1-3\ell_2)\omega.
$$

The same computation is repeated in a Mayer-Vietoris model of the base, where the quotient of the three annulus-meridian values by the sum-zero sublattice maps $(n_0,n_1,n_2)$ to $\pm(n_0+n_1+n_2)\omega$. This supplies an internal check of the obstruction formula without using the first topology computation of $X$.

Multiplicativity gives

$$
d_2^{0,2}(2q)=\pm p\,\omega\bar\delta,
\qquad
 d_2^{0,3}(2\gamma uw)=\pm p\,\omega[\gamma\delta]
$$

with the same sign, where

$$
p=12\ell_0-4\ell_1-3\ell_2.
$$

The exact algebra supporting the common sign is:

$$
p''=2p-p',
\qquad
|p'|=|p''|.
$$

The opposite-sign branch gives $p=0$, while the actual data has $p=-1$. Hence $p'=p''=p$.

For

$$
(\ell_0,\ell_1,\ell_2)=(0,1,-1),
\qquad p=-1,
$$

all three transgressions are multiplication by a unit. The spectral sequence therefore gives

$$
H^1(X;\Z)=H^2(X;\Z)=H^3(X;\Z)=0.
$$

**Audit result:** the old R4 classification conflated the first Mayer-Vietoris route with the separate Leray route. The Leray differential is geometrically derived in the source and survives the present audit.

# Re-audit of van Kampen

The manuscript uses explicit deck transformations

$$
(x,z)\longmapsto(A_jx+v_j/m_j,\zeta z)
$$

on the local covers. Raising the deck generator to the $m_j$-th power gives the fibre translation $t_{v_j}$. The invariant zero-section removes an additional undetected translation at the finite fibres.

At the cusp, the tautological section is the disc through $(1,1)$. Its boundary is the toric meridian, so the cusp drift is

$$
\mu=0,
\qquad \ell_0=0.
$$

The sign lemma then compares all possible sign-entry points at the order-three and order-four fibres and proves that the relative signs agree. Reversing the global meridian convention changes all three $\ell_i$ simultaneously and replaces $p$ by $-p$, leaving $|p|$ unchanged.

After killing the toric lattice, the presentation reduces to

$$
x^3=c^{\ell_1},
\qquad
y^4=c^{\ell_2},
\qquad
xy=c^{\ell_0}.
$$

Its abelian relation matrix has determinant $-p$; for the actual data its Smith form is $\operatorname{diag}(1,1,1)$. The nonabelian elimination in Theorem 7.17 yields the same cyclic group of order $|p|$, hence

$$
\pi_1(X)=1.
$$

**Audit result:** the earlier R3 entry should not remain "critical unresolved." The source gives based loops, deck actions, primitive meridians, drift, and relative sign control. No contrary morphism was found.

# Topological recognition

The audited non-collapse route now supplies

$$
\pi_1(X)=1,
\qquad
H^1(X;\Z)=H^2(X;\Z)=H^3(X;\Z)=0.
$$

Universal coefficients and Poincare duality give

$$
H_k(X;\Z)=0\quad(0<k<6),
\qquad
H_0(X;\Z)=H_6(X;\Z)=\Z.
$$

The recognition argument then proceeds through Hurewicz, Whitehead, the high-dimensional Poincare theorem, and the fact that the smooth homotopy-sphere group in dimension six is trivial. No defect was found in that final step.

# Independent algebraic-dimension result

Section 9.1 proves $a(X)=1$ without Section 7 and without CDP.

The exact period calculation shows that an integral bivector $E$ is of type $(1,1)$ precisely when a five-term period expression $P_E$ vanishes. The transformation laws under $g_0$ and $g_2$ prove the linear independence of

$$
1,\quad\tau,\quad\mu,\quad\beta,\quad6\mu^2-\tau\beta.
$$

Therefore

$$
P_E\equiv0
\Longleftrightarrow
E\in\Z\eta,
\qquad
\eta=u\wedge w+6\gamma\wedge\delta.
$$

The class $\eta$ has square $12$ and signature $(1,1)$. Away from a countable set, the Neron-Severi group is exactly $\Z\eta$, which excludes both an abelian-surface polarization and an elliptic quotient fibre class. The very general torus fibre therefore has algebraic dimension zero.

For any meromorphic $g$ on $X$, its restrictions are constant on uncountably many such fibres. The vanishing locus of $dg\wedge f^*dt$ must equal the regular fibration locus; the resulting function on the base extends meromorphically across the omitted points. Hence

$$
\mathcal M(X)=f^*\mathcal M(\mathbb P^1)=f^*\C(t),
\qquad
a(X)=1.
$$

**Audit result:** Lemmas 9.2-9.6, Proposition 9.7, and Corollary 9.8 should be upgraded from downstream/dependency classifications to independently verified arguments, subject only to the already constructed family in Sections 3-6.

# Section 10 and the CDP comparison

The local calculation at a reduced non-normal normal-crossings fibre is sound. For $g=xy$ or $g=xyz$, the ambient differential $dg|_S$ vanishes on the conductor locus but is nonzero on the smooth locus. A trivialization of a line bundle on the normalization glues

$$
\eta^*(dg|_S)\otimes e
$$

with zero conductor value to a nonzero global ambient one-form. Its intrinsic image is conductor-supported torsion and vanishes in the torsion-free differential sheaf. For a nontrivial line bundle it does not arise from the conormal term.

The duality and top-degree base-change steps used to turn this section into nonzero $R^2f_*(T_X\otimes L)$ are correctly stated for the local setting used. The global application invokes the earlier topology/Picard conclusions to show that the relevant line bundle becomes trivial on the normalization of $W$.

This establishes a precise local mechanism and an explicit dependency chain. It does not follow merely from a discrepancy in a printed proof that an unrelated theorem is false; the manuscript instead couples the local defect to its constructed $X$ and derives a direct nonvanishing statement.

# Revised risk ledger

| ID | Claim | Revised status | Effect on main theorem |
|---|---|---|---|
| C1 | Global cusp-collapse continuity/equivariance | Open for the collapse description | Not used by the nearby-cycle/Leray recognition route |
| C2 | Equality $c^*=\spmap$ and degree-two collapse normalizations | Open for first route and later collapse-dependent statements | Not used to prove $\pi_1$ or the homology sphere by the second route |
| B1 | Nearby-cycle specialization is the invariant lattice | Reconstructed and verified at manuscript level | Supplies the central-fibre stalk input for Leray |
| V1 | Based van Kampen inclusions, signs, drift, primitive meridians | Reconstructed and verified at manuscript level | Gives $\pi_1(X)=1$ for $p=-1$ |
| L1 | Leray transgression calculation | Reconstructed and verified at manuscript level | Gives $H^1=H^2=H^3=0$ for $p=-1$ |
| MV1 | First collapse/Mayer-Vietoris chain map | Still requires an independent full audit | Redundant for recognition, relevant to the first route and explicit collapse claims |
| G1 | Analytic construction and global gluing in Sections 3-6 | Reviewed with no identified defect; not formally mechanized | Remains the principal construction-level review scope |
| A1 | Direct algebraic-dimension argument | Independently verified | Establishes $a(X)=1$ without Section 7 or CDP |
| D1 | Local conductor-supported ambient differential | Verified locally | Supports the Section 10 mechanism; global application uses earlier results |

# Revised peer-review recommendation

The original rejection should not be retained unchanged. It was driven by the assertion that unresolved collapse and matrix-identification questions blocked every proof of the topology. The full source supplies a separate proof, and that proof survives the present reconstruction.

The appropriate recommendation is:

> **Reconsidered, provisionally favorable, with focused revision and external verification requests.** The manuscript should make the two topology routes impossible to conflate, move the nearby-cycle/Leray dependency graph to the front of Section 7, preserve the distinction between $\spmap$ and $c^*$, and expand the few standard-formalism transitions most likely to concern referees. The explicit cusp-collapse argument should remain separately labeled until its full stratum-by-stratum proof is audited.

No mathematical disproof was found. More importantly, the former stated reason for withholding the main theorem no longer survives the integrated audit.

# What this addendum does not claim

This update does not claim access to the unprovided live Overleaf workbench. It does not certify the reported pre-correction drafts. It does not replace external checking of SGA-style nearby-cycle formalism, analytic Serre duality, cohomology and base change, or smooth homotopy-sphere classification. It records which exact arguments in the canonical source were reconstructed and which earlier objections have therefore been retired or narrowed.


\newpage

# Cold-entry mathematical results map

# Purpose and current status

The manuscript constructs a compact complex threefold

$$
f:X\longrightarrow \Pone
$$

whose generic fibre is a complex two-torus, whose central fibre is a reduced non-normal normal-crossings surface $W$, and whose other two singular fibres have multiplicities $3$ and $4$. The intended topological conclusion is that the underlying smooth six-manifold is diffeomorphic to $S^6$.

A first proof audit accepted the exact lattice calculations but stopped at the integral topology. The reconstructed full source changes that assessment. The source contains a second topology computation which does not use the disputed cusp-collapse map. I have traced this second route line by line through Appendix B, Section 7.7, the based van Kampen computation, and the final recognition argument. No load-bearing error was found in that route.

The present status is therefore:

* the earlier objection that the $S^6$ theorem necessarily depends on the cusp-collapse map is withdrawn;
* the nearby-cycle/Leray topology route survives the present reconstruction audit;
* the direct period argument proving $a(X)=1$ and $\M(X)=f^*\C(t)$ survives independently of the topology computation and independently of the CDP discussion;
* the explicit collapse description of $W$ and the first Mayer-Vietoris route still require their own full geometric audit;
* the local analytic mechanism identified in Section 10 at a non-normal normal-crossings fibre is mathematically sound, while its global application uses the topology and Picard results proved earlier in the manuscript.

This is a positive corrective assessment, not a claim that every cited theorem and every analytic gluing statement has received a journal-length external verification.

# The construction in one diagram

The monodromy representation on the rank-four lattice $V$ is generated by matrices $T_1,T_2$ of exact orders $3,4$, with

$$
T_0=(T_1T_2)^{-1}=I+N,\qquad N^2=0,\qquad \operatorname{rank}N=2.
$$

The dual lattice $\Lambda=V^\vee$ carries the contragredient monodromies

$$
A_j=(T_j^{-1})^{\mathsf t},\qquad M_0=(T_0^{-1})^{\mathsf t},\qquad A_1A_2M_0=I.
$$

The logarithmic fillings use twist vectors

$$
v_1=\varepsilon,
\qquad
v_2=-\varepsilon',
\qquad
(\ell_0,\ell_1,\ell_2)=(0,1,-1).
$$

The arithmetic parameter governing both the fundamental group and the Leray transgressions is

$$
p=12\ell_0-4\ell_1-3\ell_2=-1.
$$

Thus the decisive maps in the second topology route are multiplication by a unit.

# The precise correction: $\operatorname{sp}^q$ is not being replaced by $c^*$

Two maps with the same source and target appear in the manuscript:

$$
\operatorname{sp}^q:H^q(W;\Z)\longrightarrow H^q(F;\Z)^{T_0}
$$

is the nearby-cycle specialization map, while

$$
c^*:H^q(W;\Z)\longrightarrow H^q(F;\Z)
$$

comes from the explicit cusp-collapse map $c:F\to W$ of Section 7.2. When the collapse construction is used, the manuscript identifies these maps. The Leray proof does not require that identification. It uses only the stalk morphism

$$
(R^qf_*\Z)_{p_0}=H^q(W;\Z)
\longrightarrow
(j_*\mathcal L^q)_{p_0}=H^q(F;\Z)^{T_0},
$$

which is exactly $\operatorname{sp}^q$. Appendix B proves that this map is an isomorphism. Consequently the cusp-collapse continuity problem is not a premise of the second topology route.

# Nearby cycles at the central fibre

The local models are

$$
t=z_0,
\qquad
t=z_0z_1,
\qquad
t=z_0z_1z_2.
$$

Their Milnor fibres have homotopy types

$$
\mathrm{pt},\qquad S^1,\qquad T^2.
$$

For the nearby-cycle complex $\psi$, Appendix B obtains

$$
\mathcal H^0\psi=\Z_W,
\qquad
\mathcal H^1\psi=\mathcal V,
\qquad
\mathcal H^2\psi=\Z_P\oplus\Z_Q,
\qquad
\mathcal H^{\ge 3}\psi=0.
$$

The sheaf $\mathcal V$ is controlled by the three double curves. At both triple points the restriction values satisfy the same integral relation

$$
n_1-n_2+n_3=0.
$$

The resulting hypercohomology spectral sequence has rows of ranks

$$
(1,2,4,2,1),
\qquad
(2,1,3),
\qquad
(2).
$$

Rank bookkeeping against $H^*(F;\Z)\cong\bigwedge^*\Z^4$, followed by the degree-three Gysin argument along a saturated two-dimensional subtorus, proves that each

$$
\operatorname{sp}^q:H^q(W;\Z)\xrightarrow{\sim}H^q(F;\Z)^{T_0}
$$

is an integral isomorphism. The exact Smith calculations independently confirm the invariant ranks

$$
(1,2,4,2,1)
$$

and the saturation of the relevant monodromy images.

# Leray transgressions

The local finite-fibre calculations give

$$
H^0(B,R^1f_*\Z)=12\Z\gamma,
\qquad
H^0(B,R^2f_*\Z)=2\Z q,
\qquad
H^0(B,R^3f_*\Z)=2\Z\gamma uw.
$$

The obstruction calculation in Proposition 7.27 evaluates local lifts on the three meridians and gives

$$
d_2^{0,1}(12\gamma)=\pm p\omega.
$$

Multiplicativity and the pairings in the coefficient systems give, with the same sign,

$$
d_2^{0,2}(2q)=\pm p\,\omega\bar\delta,
\qquad
 d_2^{0,3}(2\gamma uw)=\pm p\,\omega[\gamma\delta].
$$

For the actual twists, $p=-1$. These three maps are therefore isomorphisms onto their rank-one targets, and the Leray calculation yields

$$
H^1(X;\Z)=H^2(X;\Z)=H^3(X;\Z)=0.
$$

Universal coefficients and Poincare duality then give the integral homology of a six-sphere.

# Fundamental group

The based overlap calculation gives generators $x,y,c$ with relations

$$
x^3=c^{\ell_1},
\qquad
y^4=c^{\ell_2},
\qquad
xy=c^{\ell_0}.
$$

The corresponding relation matrix is

$$
\begin{pmatrix}
3&0&-\ell_1\\
0&4&-\ell_2\\
1&1&-\ell_0
\end{pmatrix},
$$

whose determinant is $-p$. For $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$, its Smith form is $\operatorname{diag}(1,1,1)$. The nonabelian elimination in Theorem 7.17 gives the same cyclic group of order $|p|$, hence

$$
\pi_1(X)=1.
$$

The source explicitly tracks the clockwise meridians, the deck transformations, the zero-section drifts, the common sign at the order-three and order-four fibres, and the vanishing cusp drift $\mu=0$. This is substantially more than a matrix consistency check.

# Recognition

The topology chain now supplies

$$
\pi_1(X)=1,
\qquad
H_*(X;\Z)\cong H_*(S^6;\Z).
$$

Hurewicz and Whitehead identify $X$ as a homotopy six-sphere. The smooth homotopy-sphere classification in dimension six has trivial group $\Theta_6$, so the underlying smooth manifold is diffeomorphic to $S^6$.

# Algebraic dimension

For a smooth fibre $F_b$, an integral class $E\in\bigwedge^2V$ is of type $(1,1)$ precisely when

$$
P_E=E_{\gamma u}-E_{\gamma w}\tau-E_{\gamma\delta}\mu
+6E_{uw}\mu+E_{u\delta}\beta
+E_{w\delta}(6\mu^2-\tau\beta)
$$

vanishes at the period point. The five functions

$$
1,\quad \tau,\quad \mu,\quad \beta,\quad 6\mu^2-\tau\beta
$$

are linearly independent under the exact $g_0,g_2$ transformation laws. Therefore

$$
P_E\equiv0
\quad\Longleftrightarrow\quad
E\in\Z\eta,
\qquad
\eta=u\wedge w+6\gamma\wedge\delta.
$$

The class satisfies

$$
\eta^2=12
$$

and has Hermitian signature $(1,1)$. Outside a countable exceptional set, $\operatorname{NS}(F_b)=\Z\eta$. Such a torus cannot have algebraic dimension two, because it has no positive definite Neron-Severi class, and cannot have algebraic dimension one, because a fibre class of a torus quotient has square zero whereas every nonzero multiple of $\eta$ has nonzero square. Hence the very general fibre has algebraic dimension zero.

A meromorphic function on $X$ restricts constantly to uncountably many such fibres. The analytic set

$$
\{dg\wedge f^*dt=0\}
$$

must then be all of the regular fibration locus, so the function descends to the base and extends meromorphically across the finitely many omitted points. Therefore

$$
\M(X)=f^*\M(\Pone)=f^*\C(t),
\qquad
a(X)=1,
$$

and $f$ is the algebraic reduction. This proof does not invoke Section 7 or the CDP argument.

# Section 10: the non-normal fibre mechanism

For a reduced normal-crossings fibre $S$, the ambient differential $dg|_S$ is nonzero away from the double locus and vanishes on that locus. If a line bundle $A$ becomes trivial on the normalization, the pair

$$
\bigl(\eta^*(dg|_S)\otimes e,0\bigr)
$$

glues to a nonzero section of $\Omega^1_{\mathcal X}|_S\otimes A$. Its intrinsic image is torsion supported on the conductor and disappears in the torsion-free quotient of $\Omega_S^1$, but for nontrivial $A$ it does not come from the conormal line. This verifies the local obstruction highlighted by Lemma 10.3.

Serre-Grothendieck duality and top-degree cohomology/base change convert the section into nonvanishing of $R^2f_*(T_X\otimes L)$ at $W$. The global application uses the earlier topology and Picard statements to trivialize the pullback of $A$ to the normalization. Thus the local analytic defect and its global deployment have explicit, separately visible dependencies.

# Remaining work

The explicit cusp-collapse map and its identification with $c^*$ remain important for the first topology route, for the detailed description of the collapse of a smooth fibre onto $W$, and for some degree-two normalizations used later. They are not premises of the nearby-cycle/Leray recognition route.

The remaining high-value peer-review work is now narrower:

1. verify the cited nearby-cycle formalism and the Gysin-with-support compatibility against the cited sources;
2. continue line-by-line review of the period family, proper discontinuity, compact toric quotient, and global Hausdorff gluing in Sections 3-6;
3. complete or refute the explicit cusp-collapse construction for the claims that actually depend on it;
4. cross-check every external literature quotation in Section 10 against the printed sources.

The exact finite checks included with this report pass 17/17, in addition to the earlier 38/38 core algebra checks.


\newpage

# Original audit preserved as issued

# Independent Mathematical Proof Audit

## Manuscript audited

**Claim:** a compact complex threefold constructed as a torus fibration over $\mathbb P^1$ is diffeomorphic to $S^6$, yielding an integrable complex structure on the six-sphere.

**Source audited:** `s6_canonical_full_108_pages.tex` and the matching 108-page canonical PDF.

**Audit standard:** every indispensable implication must either be checked exactly, reduced to a cited standard theorem with its hypotheses verified, or marked unresolved. Numerical agreement, internal consistency, and absence of an obvious contradiction are not treated as proof.

## Disposition

> **MAJOR REVISION - MAIN THEOREM NOT CERTIFIED.**

I found **no explicit arithmetic contradiction** and **no concrete local analytic error** in the construction through the gluing of the three local fillings. The exact finite algebra in Sections 2, 5, 7, and Appendix A is reproducible and passes independent computer-algebra checks.

The proof nevertheless does not yet meet a certification standard because the global topology depends on geometric maps whose asserted integral effect has not been independently established in the supplied argument at chain level. In particular, the proof of the $S^6$ identification requires all of the following to be correct simultaneously:

1. the cusp filling has the asserted homotopy/collapse model;
2. the specialization map $H_q(F;\mathbb Z)\to H_q(W;\mathbb Z)$ is the stated quotient, integrally and with the stated orientations;
3. the overlap inclusions used by van Kampen impose exactly the displayed twist relations;
4. the Mayer--Vietoris or Leray differentials are represented by the displayed integral matrices in the claimed geometric bases.

The downstream Smith-normal-form calculations are correct **after those identifications are granted**. They do not themselves prove the identifications.

## 1. Claim chain and audit result

| Manuscript stage | Pages | Audit result | Reason |
|---|---:|---|---|
| Lattice and monodromy data | 8-13 | **Exact pass** | Integer matrices, invariant lattices, coinvariants, exterior powers, and alternating form checked exactly. |
| Period family | 14-23 | **Reviewed; no error found** | Transformation laws, torsor construction, cusp asymptotics, determinant identity, and equivariance are internally coherent. This is not a formal verification of the analytic existence arguments. |
| Toric cusp filling | 24-31 | **Reviewed; no local error found** | Fan smoothness, free proper action estimate, compact quotient, central fibre, and overlap map are coherent. The later topological collapse is a separate issue. |
| Logarithmic fillings | 31-35 | **Exact/local pass** | Finite-order action, fixed-point criterion, freeness for the chosen twists, and local quotient structure check out. |
| Global complex gluing | 36-39 | **Reviewed; no error found** | The quotient atlas, Hausdorff argument, properness, and connectedness are coherent once the local models are accepted. |
| Fundamental group and homology | 40-62 | **Not certified** | Algebraic reductions pass conditionally, but the geometric overlap and specialization maps require an independent integral chain-level proof. |
| Recognition as $S^6$ | 63-66 | **Conditional pass** | Standard once simple connectivity and integral homology-sphere status are established. |
| Complex-analytic invariants | 64-94 | **Conditional/consistency pass** | No topological, Hodge, or Riemann--Roch contradiction found; all conclusions remain conditional on existence and topology of $X$. |
| Appendices | 95-108 | **Supporting exact checks; topology still conditional** | Matrix and cell computations are useful evidence, but the crucial identification of their algebraic maps with the actual geometric maps remains the unresolved point. |

## 2. Exact calculations that pass

### 2.1 Monodromy matrices

Using the matrices printed in Section 2, exact integer arithmetic verifies:

$$
\det T_1=\det T_2=1,\qquad T_1^3=I,\qquad T_2^4=I,\qquad T_2^2\ne I.
$$

With $T_0=(T_1T_2)^{-1}=I+N$,

$$
N^2=0,\qquad \operatorname{rank}N=2.
$$

For the contragredient matrices

$$
A_j=(T_j^{-1})^{\mathsf t},\qquad M_0=(T_0^{-1})^{\mathsf t},
$$

one obtains exactly

$$
A_1A_2M_0=I.
$$

The Smith normal forms of $A_1-I$, $A_2-I$, and $M_0-I$ have nonzero diagonal entries $(1,1)$. The combined coinvariant block has nonzero Smith entries $(1,1,1)$, giving a free rank-one coinvariant group.

### 2.2 Distinguished lattices and twists

The computations verify

$$
\ker(M_0-I)=\operatorname{im}(M_0-I)=\langle\widehat w,\widehat\delta\rangle,
$$

$$
\Lambda^{A_1}=\langle\varepsilon,\widehat\delta\rangle,
\qquad
\Lambda^{A_2}=\langle\varepsilon',\widehat\delta\rangle,
$$

where

$$
\varepsilon=\widehat\gamma+2\widehat u-4\widehat w,
\qquad
\varepsilon'=\widehat\gamma+3\widehat u-3\widehat w.
$$

For the manuscript's choices

$$
v_1=\varepsilon,\qquad v_2=-\varepsilon',
$$

one has

$$
(\ell_0,\ell_1,\ell_2)=(0,1,-1).
$$

The freeness criteria in Proposition 5.6 are therefore satisfied:

$$
3\nmid\gamma(v_1),\qquad \gamma(v_2)\text{ is odd}.
$$

### 2.3 Invariant alternating form

Solving the integral invariance equations

$$
T_j^{\mathsf t}QT_j=Q\quad(j=1,2)
$$

for alternating $Q$ gives a rank-one lattice generated by the form

$$
Q_0(\gamma,\delta)=1,\qquad Q_0(u,w)=6,
$$

with all other independent pairings zero. This agrees with Lemma 2.8. The induced form $Q_0(x,Ny)$ on $V/\ker N$ has matrix $\operatorname{diag}(6,-1)$.

### 2.4 Conditional fundamental-group arithmetic

The exact group and lattice algebra gives the manuscript's order formula

$$
|p|=|12\ell_0-4\ell_1-3\ell_2|.
$$

For $(0,1,-1)$,

$$
p=-1,
$$

so the resulting cyclic group is trivial. The base-orbifold elimination is also exact: once the cusp meridian and the two elliptic meridians are related as claimed by the overlap inclusions, the relations of orders $3$ and $4$ force the remaining generator to be trivial because $\gcd(3,4)=1$.

This is a **conditional certificate**: it verifies the algebra after the geometric maps are supplied; it does not prove that the actual inclusions of the overlaps induce precisely those relations.

### 2.5 Downstream consistency checks

The displayed integral matrices in the topology computation have the claimed ranks and Smith normal forms. Under the manuscript's asserted geometric identifications they produce

$$
H_k(X;\mathbb Z)=
\begin{cases}
\mathbb Z,&k=0,6,\\
0,&0<k<6.
\end{cases}
$$

The complex-analytic invariants are also numerically consistent with a complex structure on a homology six-sphere:

- $H^2(X;\mathbb Z)=H^4(X;\mathbb Z)=0$ gives $c_1=c_2=0$;
- $\int_Xc_3=e(X)=2$;
- Hirzebruch--Riemann--Roch gives $\chi(\mathcal O_X)=c_1c_2/24=0$, matching the stated $h^{0,q}$;
- the same calculation gives $\chi(T_X)=\tfrac12\int_Xc_3=1$, matching the manuscript's stated value.

These checks rule out several easy inconsistencies. They do not establish existence.

## 3. Critical unresolved proof obligations

### 3.1 Cusp-neighbourhood homotopy model

**Relevant manuscript material:** Proposition 7.2 and Lemmas 7.5--7.10, pages 40-50; toric construction, pages 24-31.

The proof uses a sequence of straightening, polar decomposition, positive-part retraction, phase spreading, and fixed-fibre collapse maps. For certification, one must prove that the composite:

1. is continuous across every toric stratum, including double and triple loci;
2. is equivariant for the full $\bar\Lambda$-action;
3. descends to the quotient $N_0$;
4. yields the claimed map of pairs and the claimed specialization map on integral homology.

The manuscript provides geometric formulas and local arguments, but the audit did not obtain a complete independent chain homotopy or cellular model verifying all four properties simultaneously. This is indispensable because later calculations use the exact induced map, not merely its rational rank.

### 3.2 Integral specialization map

**Relevant manuscript material:** Proposition 7.12, pages 50-52; Appendix B, pages 100-108.

The claimed formula is

$$
\ker\bigl(c_*:H_q(F;\mathbb Z)\to H_q(W;\mathbb Z)\bigr)
=(\bigwedge^qM_0-I)\bigwedge^q\Lambda,
$$

with $c_*$ surjective.

An integral proof must control:

- saturation of every image;
- torsion, not only ranks over $\mathbb Q$;
- identification of the nearby-cycle edge map with the geometric collapse map;
- orientations and signs in degree three;
- compatibility with the bases later used in Mayer--Vietoris.

Appendix B supplies a sophisticated nearby-cycle calculation and rank arguments. The remaining certification burden is the exact integral identification of those spectral-sequence maps with the geometric maps used in Section 7. Until that identification is independently reproduced, the homology-sphere conclusion is conditional.

### 3.3 van Kampen inclusion maps

**Relevant manuscript material:** Theorem 7.17 and its preparatory lemmas, pages 52-57; zero-section drift, pages 38-40.

The final group simplification is correct once the inclusion maps from the three boundary mapping tori are granted. What still requires independent proof is that the actual inclusions encode exactly:

- the monodromy relations $A_1,A_2,M_0$;
- the logarithmic drifts $-v_1,-v_2$;
- the cusp gluing class $\ell_0$;
- the manuscript's meridian-orientation convention.

A sign error changes $p=12\ell_0-4\ell_1-3\ell_2$, and a primitive-versus-multiple error changes the group itself. The executable certificate therefore labels the result conditional rather than treating the correct final simplification as evidence for the geometric inputs.

### 3.4 Mayer--Vietoris and Leray boundary maps

**Relevant manuscript material:** Sections 7.6-7.7, pages 57-62; Appendices A-B, pages 95-108.

The manuscript presents two routes to the homology calculation. They are valuable cross-checks, but they are not fully independent at the point that matters: both use the same monodromy and specialization geometry. The finite matrices pass exact verification. Certification still requires a complete geometric derivation of those matrices in the actual integral bases of the overlaps, including transfer indices, orientations, and primitivity.

A satisfactory revision would include either:

- an explicit finite CW model for $X$ with all cellular boundary matrices printed and derived from the attaching maps; or
- a fully functorial nearby-cycle/Mayer--Vietoris proof that identifies every edge and boundary map integrally, with a separate chain-level check of the van Kampen maps.

## 4. Steps that are valid once topology is established

### 4.1 Recognition of the smooth manifold

If $X$ is a closed smooth simply connected integral homology six-sphere, the recognition argument in Section 8 is standard: Hurewicz and Whitehead make it a homotopy sphere, and the vanishing of the group of smooth homotopy six-spheres identifies it diffeomorphically with the standard $S^6$. I found no issue in this conditional step.

### 4.2 Complex-analytic calculations

The Neron--Severi, algebraic-dimension, direct-image, canonical-bundle, holomorphic-form, vector-field, and fixed-locus calculations are internally consistent with the earlier construction. I found no numerical contradiction. They cannot rescue an unproved topology step, and the discussion of a conflict with previously published work is not evidence that the construction is correct; the construction must stand on its own.

## 5. Theorem-level audit classification

The accompanying CSV ledger assigns each theorem-like statement one of the following statuses:

- **VERIFIED-EXACT:** independently checked by exact algebra or a complete elementary argument;
- **REVIEWED-NO-ERROR-FOUND:** read for hypotheses and logical coherence, with no concrete defect found, but not formalized;
- **CONDITIONAL-PASS:** correct after an earlier unresolved statement is granted;
- **CRITICAL-UNRESOLVED:** indispensable to the main theorem and not independently certified;
- **SECONDARY:** not needed for the existence or $S^6$ identification.

The ledger deliberately does not convert “no error found” into “proved.”

## 6. Evidence and reproducibility

The evidence bundle contains:

1. the canonical TeX and PDF reviewed;
2. this report in Markdown and PDF;
3. an audit-annotated copy of all 108 manuscript pages;
4. a PDF of the critical evidence pages;
5. page-range source and text extracts;
6. theorem and proof-risk ledgers;
7. exact matrix, lattice, exterior-power, chain-matrix, Hodge, and topology checks;
8. a portable `reproduce_core_checks.py` script;
9. checksums and a clean verification script.

The exact checks are deterministic. Running `run_all_checks.sh` in the evidence bundle verifies the static checksums and reruns the core algebraic audit.

## 7. Final peer-review recommendation

The manuscript contains a detailed and mathematically serious construction. The exact algebra and local models survive substantial checking, so rejection on the basis of an elementary matrix or parity error is not supported by this audit.

The claimed complex structure on $S^6$, however, is **not established to a rigorous certification standard by the supplied evidence**. The paper should receive **major revision** centered on a self-contained, independently checkable integral topology package for Section 7 and Appendix B. Until that package is supplied and verified, the proper status of the main theorem is **unconfirmed**, not proved and not disproved.


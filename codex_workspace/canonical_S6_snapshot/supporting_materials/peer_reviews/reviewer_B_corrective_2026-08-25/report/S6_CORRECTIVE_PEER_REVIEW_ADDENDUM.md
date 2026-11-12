---
title: "Corrective Addendum to the Independent Mathematical Proof Audit"
subtitle: "S6 complex-threefold manuscript - integrated validation update"
author: "Independent reconstruction audit"
date: "25 August 2026"
geometry: margin=0.85in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - \usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array}
  - \usepackage[T1]{fontenc}
  - \newcommand{\Z}{\mathbb Z}
  - \newcommand{\C}{\mathbb C}
  - \newcommand{\spmap}{\operatorname{sp}}
---

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

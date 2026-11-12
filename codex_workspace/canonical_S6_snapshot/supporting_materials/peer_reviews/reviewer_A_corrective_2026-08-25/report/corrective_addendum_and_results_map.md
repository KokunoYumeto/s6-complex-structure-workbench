---
title: "Corrective Addendum and Mathematical Results Map"
subtitle: "Supplement to the full mathematical peer review of the 108-page S6 manuscript"
author: "Independent technical review"
date: "25 August 2026"
geometry: margin=0.78in
fontsize: 10pt
papersize: letter
colorlinks: true
linkcolor: blue
urlcolor: blue
toc: false
toc-depth: 3
numbersections: true
header-includes:
  - |
    ```{=latex}
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
    ```
---


# Corrective addendum dated 25 August 2026

This edition integrates the mathematical claims contained in the user-supplied Codex progress log, but it does not treat that log as evidence by itself. The log reports two strengthened proof lines: a direct period-theoretic proof that

$$
a(X)=1,
\qquad
\mathcal M(X)=f^*\mathbb C(t),
$$

and an integral nearby-cycle/Leray computation that proves the homology-sphere conclusion without the global cusp-collapse theorem. It also reports corrections to a modular-frame factor, a Neron--Severi simplification, Lemma A.3's variance, and the distinction between $\Lambda$ and $\bar\Lambda$. Only the progress log, not the separate Codex workbench files or its claimed 38-check harness, was supplied. Every point promoted in this report was therefore re-located and re-checked in the audited 108-page manuscript itself.

The result is a genuine but limited correction to the review of 24 August 2026.

1. The direct algebraic-dimension argument in Section 9.1 is stronger than the earlier review stated. Its period calculation, very-general Neron--Severi computation, exclusion of algebraic dimensions one and two for the fibres, and meromorphic descent form a complete argument conditional only on the construction of the period family and standard structure theory for complex tori. It is independent of Section 7 and of Campana--Demailly--Peternell.
2. The second topology route in Section 7.7 and Appendix B is not merely corroborative. It is a logically sufficient topology engine for the recognition of $X$ as $S^6$, provided the based fundamental-group relations, the finite-fibre specialization lattices, the integral cusp specialization theorem, and the geometric identification of the Leray transgressions are correct. Proposition 7.2's global collapse is therefore not theorem-critical for the sphere-recognition chain, although it remains necessary for the manuscript's first topology route and for its explicit collapse-map and generator claims.
3. Lemma A.3 contains a confirmed variance error. The displayed Mayer--Vietoris sequence and every map subsequently computed are cohomological, although the proof writes $H_k$. Replacing $H_k$ by $H^k$ throughout that calculation and applying universal coefficients at the end repairs the lemma without changing its stated groups.
4. The corrected source already contains the modular factor $\mathsf e=F^{-1}e$ needed on source page 71, and the current algebra in Lemma 9.3 is correct. Those are repairs present in the audited text, not defects of the current version.
5. The current cusp notation correctly uses $\bar\Lambda=\Lambda/\Lambda_{\mathrm{tor}}$ as the deck group. The Codex log does not identify the earlier erroneous occurrence, so no additional current-source error is asserted on that point.

The recommendation remains **major revision and independent specialist replication**. The reason is no longer a suspicion that the global collapse is the sole route to the homology calculation, nor an unresolved algebraic-dimension argument. The remaining burden is concentrated in the actual geometric realization of the displayed local and global maps, integral nearby-cycle functoriality and orientation data, the based van Kampen and transgression comparisons, and the analytic duality/base-change/literature-comparison chain in Section 10.

## Mathematical results so far: a cold-entry guide

### The construction being claimed

The manuscript starts with a rank-four integral lattice $\Lambda$ and monodromies of orbifold orders $3$ and $4$, together with a unipotent cusp monodromy. Period functions $\tau,\mu,\beta$ define a holomorphic family of two-dimensional complex tori over the thrice-punctured projective line. Three local fillings are then attached: a toric, reduced, irreducible, nonnormal normal-crossing fibre $W$ at the cusp, and multiple fibres $3S_1$ and $4S_2$ whose reductions are bielliptic surfaces. The gluing parameters enter the topology only through

$$
p=12\ell_0-4\ell_1-3\ell_2.
$$

For the actual data $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$, one has $p=-1$.

### The topology chain now isolated

The based van Kampen calculation produces

$$
\pi_1(X)=\langle c,x,y\mid c\ \text{central},\ xy=c^{\ell_0},\ x^3=c^{\ell_1},\ y^4=c^{\ell_2}\rangle
\cong \mathbb Z/|p|,
$$

conditional on the geometric identification of the three meridians and their drift terms. Thus the actual value $p=-1$ gives $\pi_1(X)=1$.

The independent Leray route uses the exact cusp-specialization statement

$$
H^q(W;\mathbb Z)\xrightarrow{\ \operatorname{sp}^q\ }
H^q(F;\mathbb Z)^{T_0}
$$

as an isomorphism for $0\le q\le4$, together with the finite-fibre specialization indices. It obtains

$$
H^0(B,R^1f_*\mathbb Z)=12\mathbb Z\gamma,
\quad
H^0(B,R^2f_*\mathbb Z)=\mathbb Z\cdot2q,
\quad
H^0(B,R^3f_*\mathbb Z)=\mathbb Z\cdot2\gamma uw.
$$

The three relevant transgressions are

$$
\begin{aligned}
d_2^{0,1}(12\gamma)&=\pm p\,\omega,\\
d_2^{0,2}(2q)&=\pm p\,\omega\bar\delta,\\
d_2^{0,3}(2\gamma uw)&=\pm p\,\omega[\gamma\delta],
\end{aligned}
$$

with one common sign. Multiplicativity gives the same integer in all three formulas. When $p=-1$, these maps are units. The spectral sequence then yields $H^1(X)=H^2(X)=H^3(X)=0$; universal coefficients and Poincare duality give the integral homology of $S^6$. Together with $\pi_1(X)=1$ and $\Theta_6=0$, this implies $X\cong_{\mathrm{diff}}S^6$.

This route does not use the global collapse theorem. Its theorem-critical unresolved inputs are instead: the based meridian relations, the integral specialization theorem at $W$, the finite-fibre lattices, and the geometric realization of the first transgression and its multiplicative comparison.

### The direct algebraic-dimension chain

For an integral class

$$
E=E_{\gamma u}\gamma u+E_{\gamma w}\gamma w+E_{\gamma\delta}\gamma\delta
  +E_{uw}uw+E_{u\delta}u\delta+E_{w\delta}w\delta,
$$

Section 9.1 proves

$$
E\in\operatorname{NS}(F_b)
\quad\Longleftrightarrow\quad
P_E(z)=0,
$$

where

$$
P_E=E_{\gamma u}-E_{\gamma w}\tau-E_{\gamma\delta}\mu
 +6E_{uw}\mu+E_{u\delta}\beta+E_{w\delta}(6\mu^2-\tau\beta).
$$

The transformation laws under the two orbifold generators prove that

$$
1,\ \tau,\ \mu,\ \beta,\ 6\mu^2-\tau\beta
$$

are linearly independent. Hence the very general fibre has

$$
\operatorname{NS}(F_b)=\mathbb Z\eta,
\qquad
\eta=uw+6\gamma\delta.
$$

Moreover

$$
\eta^2=12,
\qquad
G_\eta=
\begin{pmatrix}
2\operatorname{Im}\tau&2\operatorname{Im}\mu\\
2\operatorname{Im}\mu&\frac13\operatorname{Im}\beta
\end{pmatrix},
$$

and

$$
\det G_\eta=\frac{2}{3}\operatorname{Im}\tau
\left(\operatorname{Im}\beta-\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}\right)<0.
$$

Thus every nonzero multiple of $\eta$ is nondegenerate and indefinite, while its square is nonzero. A two-torus of algebraic dimension two would have an ample positive class; one of algebraic dimension one would have a nonzero fibre class of square zero. Neither can occur when $\operatorname{NS}=\mathbb Z\eta$. Therefore the very general fibre has algebraic dimension zero.

A separate descent lemma shows that a meromorphic function on $X$ which is constant on uncountably many smooth fibres comes from the base. Since very general fibres have algebraic dimension zero,

$$
\mathcal M(X)=f^*\mathcal M(\mathbb P^1)=f^*\mathbb C(t),
\qquad
a(X)=1,
$$

and $f$ is the algebraic reduction. This proof is independent of the topology and of the CDP dispute.

### What Section 10 has and has not established

The local conductor calculation produces a nonzero ambient cotangent section on a reduced nonnormal normal-crossing fibre even when the torsion-free intrinsic cotangent sheaf has no section. For a line bundle $A$ trivial after normalization, the pair

$$
\bigl(\eta^*(df|_W)\otimes e,0\bigr)
$$

descends through the normalization/conductor sequence to

$$
s\in H^0(W,\Omega_X^1|_W\otimes A),
$$

whose intrinsic image is conductor-supported torsion. This local mechanism is mathematically real and was independently reconstructed.

Its application to the global contradiction requires the exact analytic chain

$$
H^2(W,E)^\vee
\simeq \operatorname{Hom}_W(E,\omega_W)
\simeq H^0(W,E^\vee\otimes\omega_W),
\qquad E=(T_X\otimes L)|_W,
$$

followed by the top-degree base-change map

$$
(R^2f_*(T_X\otimes L))_0\otimes k(0)
\longrightarrow H^2(W,(T_X\otimes L)|_W).
$$

The manuscript states the relevant Gorenstein duality and top-degree base-change hypotheses, and no internal contradiction was found. Nevertheless, three assertions must remain distinct:

1. the local computation may expose a gap in a printed proof at a nonnormal fibre;
2. that does not by itself prove the published theorem false in all stated generality;
3. the theorem is contradicted by this example only after the construction and every hypothesis on $X$ have independently been certified.

## Revised status ledger

| Status | Claim | Present assessment |
|---|---|---|
| **VERIFIED exact algebra** | monodromy, Smith forms, invariant/coinvariant lattices, period transformations, $P_E$, $\eta^2$, Gram determinant, Appendix B rank matrices | Reproduced in two local harnesses: 28 legacy checks and 14 supplemental checks, all passing. |
| **CONDITIONALLY VALIDATED** | direct proof of $a(X)=1$ and $\mathcal M(X)=f^*\mathbb C(t)$ | The complete argument is present and survives line-by-line review, conditional on the period-family construction and standard complex-torus structure theory. |
| **CONDITIONALLY VALIDATED** | Leray route from specialization and transgression data to $H_*(X)=H_*(S^6)$ | Formal sheaf, spectral-sequence, rank, saturation, and multiplicativity logic survives review. Geometric bridge inputs remain open to specialist replication. |
| **OPEN** | existence and exact gluing of the global compact complex threefold | No fatal defect found, but the infinite toric quotient, finite logarithmic fillings, and Hausdorff/proper gluing remain construction-level obligations. |
| **OPEN** | Section 10 as a counterexample to the printed CDP conclusions | Local conductor mechanism is strong; global duality/base change and exact comparison with the published proof require specialist adjudication. |
| **REFUTED local wording** | Remark 7.28 as a fixed-triple biconditional | False; must be existential in $\ell_0$. |
| **REFUTED proof sentence** | Proposition 4.7(iv)'s properness justification | Closedness needs the closed-graph/section argument. |
| **REFUTED notation/variance** | Lemma A.3's displayed Mayer--Vietoris sequence as homology | It is cohomology. The stated groups survive after correction and UCT. |



# Disposition

This addendum is incorporated verbatim into the primary revised report. The full section-by-section audit, issue ledger, proof-obligation analysis, and references follow there.

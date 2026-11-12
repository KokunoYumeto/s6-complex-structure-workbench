---
title: "S6 Candidate-Specific Validation Update"
date: "26 August 2026"
---

**Scope:** properness, flatness, duality, the conductor-supported differential, and top-degree cohomology/base change in Sections 9-10 of the current 108-page candidate.  
**Disposition of this slice:** **verified from the stated candidate inputs.**  
**Disposition of the whole candidate:** **not certified by this update.**

## Result

The new workbench observation is correct and materially narrows the search for a candidate-specific counterexample.

1. Once the constructed object is a compact connected complex threefold and the displayed map \(f:X\to\mathbf P^1\) is a nonconstant holomorphic map, properness and flatness follow.
2. Every holomorphic vector bundle on \(X\), in particular \(E=T_X\otimes L\), is flat over \(\mathbf P^1\).
3. For every \(b\in\mathbf P^1\), including the nonreduced multiple fibres, the canonical top-degree base-change morphism
   \[
   \beta_b^2:(R^2f_*E)_b\otimes_{\mathcal O_{\mathbf P^1,b}}k(b)
       \longrightarrow H^2(X_b,E|_{X_b})
   \]
   is an isomorphism, with \(X_b\) the scheme-theoretic fibre.
4. The duality and local conductor argument at the reduced normal-crossings fibre \(W\) is sound. It gives
   \[
   H^2\bigl(W,(T_X\otimes L)|_W\bigr)\ne0
   \]
   for every \(L\in\operatorname{Pic}(X)\), after using the manuscript's topological input \(H^2(X,\mathbf Z)=0\) and the asserted normalization \(\widetilde W\simeq\mathrm{dP}_6\).
5. The base-change isomorphism transfers this nonvanishing to
   \[
   R^2f_*(T_X\otimes L)\ne0.
   \]

No counterexample occurs in the properness-flatness-duality-base-change layer. A counterexample to the actual candidate must enter earlier: in the construction of the compact Hausdorff threefold, the toric description and normalization of \(W\), or the integral topology used to obtain \(H^2(X,\mathbf Z)=0\).

## Status discipline

The supplied workbench record reports exact-check harnesses but also records two proof-layer transcription corrections and expressly keeps compressed toric and nearby-cycle steps open until they survive line-by-line reconstruction. This update preserves that discipline.

The statuses used here are:

- **verified:** a complete argument is given in this report;
- **verified-exact:** a finite algebraic identity also has a machine-reproducible certificate;
- **verified-from-input:** the deduction is complete after the named candidate inputs are supplied;
- **open candidate-specific:** the claim concerns the actual construction and is not replaced by rank or matrix agreement.

## Properness, surjectivity, and flatness

Let \(X\) be a compact connected complex manifold of dimension three and let \(f:X\to B=\mathbf P^1\) be a nonconstant holomorphic map.

### 3.1 Properness and surjectivity

A continuous map from a compact space to a Hausdorff space is proper. Thus \(f\) is proper.

A nonconstant holomorphic map from a connected complex manifold to a Riemann surface is open. Its image is also compact, hence closed in \(\mathbf P^1\). The nonempty image is both open and closed, so \(f(X)=\mathbf P^1\).

### 3.2 Flatness of \(f\)

Fix \(x\in X\), set \(b=f(x)\), and write
\[
A=\mathcal O_{B,b},\qquad R=\mathcal O_{X,x}.
\]
The ring \(A\) is a discrete valuation ring. The ring \(R\) is a regular local integral domain because \(X\) is a complex manifold.

Let \(t\in A\) be a local parameter. Its pullback \(f^*t\in R\) is nonzero. If its germ were zero, \(f\) would map a neighbourhood of \(x\) into the point \(b\); a holomorphic map locally constant on a nonempty open subset of connected \(X\) is globally constant, contrary to the hypothesis.

Since \(R\) is a domain, \(f^*t\) is a non-zero-divisor. Every nonzero element of the DVR \(A\) is a unit times a power of \(t\), so no nonzero element of \(A\) annihilates a nonzero element of \(R\). Thus \(R\) is torsion-free over \(A\), and torsion-free modules over a DVR are flat. Hence \(f\) is flat at every point.

This proof includes a multiple fibre locally written \(t=s^m\): the scheme-theoretic fibre is nonreduced, but \(s^m\) remains a non-zero-divisor.

### 3.3 Flatness of vector bundles

For a holomorphic vector bundle \(E\), one has locally \(E_x\simeq R^{\oplus r}\). Since \(R\) is flat over \(A\), \(E_x\) is flat over \(A\). Therefore every vector bundle on \(X\), including \(T_X\otimes L\), is \(f\)-flat.

The morphism proved flat is exactly
\[
\mathcal O_{B,b}\longrightarrow\mathcal O_{X,x};
\]
the proof identifies the image of a uniformizer as a non-zero-divisor. It does not assert that \(f\) is smooth.

## Top-degree cohomology and base change

Every scheme-theoretic fibre \(X_b\) has pure complex dimension two: locally it is cut out in the regular three-dimensional local ring \(R\) by the non-zero-divisor \(f^*t\).

Work on a sufficiently small Stein neighbourhood \(U\subset B\) of \(b\). The analytic cohomology-and-base-change theorem represents \(Rf_*E|_U\) by a bounded complex \(K^\bullet\) of finite free \(\mathcal O_U\)-modules, and \(f\)-flatness identifies its derived fibre with ordinary coherent cohomology of the scheme-theoretic fibre:
\[
K^\bullet\otimes^{\mathbf L}_{\mathcal O_U}k(b)
 \simeq R\Gamma(X_b,E|_{X_b}).
\]

For a bounded complex of finite free modules over \(A=\mathcal O_{B,b}\), the universal-coefficient exact sequence is
\[
0\longrightarrow H^q(K)\otimes_A k(b)
 \longrightarrow H^q(K\otimes_A k(b))
 \longrightarrow \operatorname{Tor}_1^A(H^{q+1}(K),k(b))
 \longrightarrow0.
\tag{4.1}
\]

### 4.1 Vanishing of the next direct image

Suppose \(H^q(K)\ne0\) for some \(q>2\), and choose the largest such \(q\). At a point in its support, Nakayama gives \(H^q(K)\otimes k(b)\ne0\). The maximality of \(q\) makes the Tor term in (4.1) zero, so the fibre has nonzero \(H^q\). A coherent sheaf on the compact two-dimensional complex space \(X_b\) has no cohomology above degree two. This contradiction gives
\[
R^qf_*E=0\qquad(q>2).
\]

### 4.2 The degree-two isomorphism

For \(q=2\), the obstruction in (4.1) is
\[
\operatorname{Tor}_1^A(R^3f_*E,k(b))=0.
\]
Therefore
\[
(R^2f_*E)_b\otimes_A k(b)
 \xrightarrow{\ \sim\ }
H^2(X_b,E|_{X_b})
\]
for every \(b\). No constancy of \(h^2\), local freeness of \(R^2f_*E\), reducedness of the fibre, or smoothness of \(f\) is used.

This identifies the exact reason top degree works: the only possible defect is the Tor term from the next direct image, and that next direct image vanishes.

## Duality on the central fibre

Now use the candidate-specific fibre \(W=f^{-1}(p_0)\), asserted to be a reduced effective Cartier divisor of multiplicity one in the smooth threefold \(X\).

A Cartier divisor in a smooth space is a local complete intersection, hence Cohen-Macaulay and Gorenstein. Adjunction gives
\[
\omega_W\simeq(\omega_X\otimes\mathcal O_X(W))|_W.
\]
Since \(W=f^*(p_0)\) as a Cartier divisor,
\[
\mathcal O_X(W)\simeq f^*\mathcal O_B(p_0).
\]
Its restriction to \(W\) is the pullback of the one-dimensional vector space \(\mathcal O_B(p_0)|_{p_0}\) along the constant map \(W\to p_0\), so it is a trivial line bundle. Hence
\[
\omega_W\simeq\omega_X|_W.
\]

For
\[
G=(T_X\otimes L)|_W,
\qquad A=(L^*\otimes\omega_X)|_W,
\]
Serre-Grothendieck duality on the compact Cohen-Macaulay surface gives the exact isomorphism
\[
H^2(W,G)^\vee
 \simeq H^0(W,G^\vee\otimes\omega_W)
 \simeq H^0(W,\Omega_X^1|_W\otimes A).
\tag{5.1}
\]
Thus it remains to construct one nonzero section on the right.

## The conductor-supported differential

Let \(\eta:\widetilde W\to W\) be the normalization, \(D\subset W\) the reduced double locus, and \(\widetilde D=\eta^{-1}(D)\). The candidate supplies the local models
\[
t=x,\qquad t=xy,\qquad t=xyz.
\]

### 6.1 Conormal injection

Since \(W\) is Cartier, the conormal sequence is exact:
\[
0\longrightarrow\mathcal O_W\cdot dt
 \longrightarrow\Omega_X^1|_W
 \longrightarrow\Omega_W^1
 \longrightarrow0.
\tag{6.1}
\]
The included finite checks certify injectivity directly in the singular models:
\[
((xy):x)\cap((xy):y)=(y)\cap(x)=(xy),
\]
and
\[
((xyz):yz)\cap((xyz):xz)\cap((xyz):xy)
=(x)\cap(y)\cap(z)=(xyz).
\]

### 6.2 Vanishing on the conductor and nonvanishing off it

In the double model,
\[
d(xy)=y\,dx+x\,dy,
\]
whose coefficients lie in the conductor ideal \((x,y)\). In the triple model,
\[
d(xyz)=yz\,dx+xz\,dy+xy\,dz,
\]
whose coefficients lie in \((xy,xz,yz)\). Therefore \(\eta^*(dt)|_{\widetilde D}=0\).

Away from \(D\), the model is \(t=ux\) with \(u\) a unit, so \(dt|_W=u\,dx\ne0\).

### 6.3 Normalization-conductor descent

The normalization-conductor sequence is
\[
0\longrightarrow\mathcal O_W
 \longrightarrow\eta_*\mathcal O_{\widetilde W}\oplus\mathcal O_D
 \longrightarrow\eta_*\mathcal O_{\widetilde D}
 \longrightarrow0.
\tag{6.2}
\]
The double and triple inclusion-exclusion reconstructions are reproduced in the exact-check script.

Assume \(\eta^*A\simeq\mathcal O_{\widetilde W}\), and choose a nowhere-zero trivializing section \(e\). Tensoring (6.2) with \(E=\Omega_X^1|_W\otimes A\), the pair
\[
(\eta^*(dt)\otimes e,0)
\]
agrees on \(\widetilde D\) and descends uniquely to
\[
s\in H^0(W,\Omega_X^1|_W\otimes A).
\]
It is nonzero because its pullback is nonzero off \(\widetilde D\). Its image in \(\Omega_W^1\otimes A\) vanishes on the dense smooth locus and is conductor-supported torsion. This is the exact nonnormal-fibre mechanism.

## Triviality on the normalization

The manuscript uses
\[
H^2(X,\mathbf Z)=0.
\]
Therefore \(c_1(M)=0\) for every line bundle \(M\) on \(X\). With the candidate-specific identification \(\widetilde W\simeq\mathrm{dP}_6\), one has \(H^1(\widetilde W,\mathcal O)=0\). The exponential sequence makes
\[
c_1:\operatorname{Pic}(\widetilde W)\hookrightarrow H^2(\widetilde W,\mathbf Z)
\]
injective. Naturality gives
\[
\eta^*(M|_W)\simeq\mathcal O_{\widetilde W}
\]
for every \(M\in\operatorname{Pic}(X)\), in particular for \(M=L^*\otimes\omega_X\). Thus the descent construction applies to the line bundle \(A\) in (5.1).

Combining duality and descent gives
\[
H^2\bigl(W,(T_X\otimes L)|_W\bigr)\ne0.
\tag{7.1}
\]
Combining (7.1) with top-degree base change gives
\[
R^2f_*(T_X\otimes L)\ne0.
\tag{7.2}
\]

## Exact dependency boundary

The verified arrows begin at three named inputs:

\[
\begin{array}{c}
\text{CAND-X: compact connected smooth }X\text{ and nonconstant }f:X\to\mathbf P^1\\
\Downarrow\\
\text{properness, flatness, and vector-bundle }f\text{-flatness}\\
\Downarrow\\
\beta_b^2\text{ is an isomorphism for every scheme-theoretic fibre},
\end{array}
\]

and

\[
\begin{array}{c}
\text{CAND-W: reduced Cartier SNC fibre, }\widetilde W\simeq\mathrm{dP}_6\\
\text{TOP-H2: }H^2(X,\mathbf Z)=0\\
\Downarrow\\
\eta^*((L^*\otimes\omega_X)|_W)\simeq\mathcal O_{\widetilde W}\\
\Downarrow\\
\text{conductor-supported section}\\
\Downarrow\\
H^2(W,(T_X\otimes L)|_W)\ne0\\
\Downarrow\\
R^2f_*(T_X\otimes L)\ne0.
\end{array}
\]

The arrows after the three inputs have been checked. The inputs are not established by these arrows, and Section 10 must not be used circularly as evidence for TOP-H2.

## Preliminary audit of the candidate construction

A targeted rereading of Theorem 4.5 and Theorem 6.2 found no immediate defect in the following chain:

- \(B_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\) is integral, orthogonal, and unimodular;
- fixed-point exclusion uses an explicit norm inequality and a bounded holomorphic correction;
- proper discontinuity reduces chart intersections to a bounded lattice-translation problem;
- the quotient is a covering and Hausdorff by finite-translate separation;
- a finite union of compact toric polydiscs supplies a compact fundamental set over each smaller closed disc;
- the local fibre equations descend through a local biholomorphism as \(x\), \(xy\), and \(xyz\);
- the global gluing uses pairwise disjoint punctured base discs, so nonsingleton equivalence classes have exactly two representatives and the transitions are the displayed biholomorphisms.

This is a positive audit finding, not a complete certification of Sections 3-6. Every analytic input defining the period functions and the two finite-point fillings still needs the same line-by-line treatment.

## Candidate-specific test program

### CAND-X: existence of the global threefold

**Target:** the quotient and gluing produce a second-countable compact Hausdorff smooth complex threefold and a global holomorphic map.

**Decisive falsifiers:** a nonfree point; infinitely many deck translates meeting a fixed compact set; a nonsingle-valued overlap; a branch change altering the glued complex structure; a non-Hausdorff pair; or failure of local properness at a special point.

### CAND-W: exact central fibre

**Target:** the quotient fibre is reduced SNC, has the stated three double curves and two triple points, and has normalization \(\mathrm{dP}_6\) with the printed conductor identifications.

**Decisive falsifiers:** a ray of nonunit height; a nonprimitive quotient identification; an extra orbit of vertices, edges, or triangles; hidden isotropy inside a branch; a wrong pairing of boundary curves; or a quotient chart not biholomorphic to \(x\), \(xy\), or \(xyz\).

### TOP-H2: integral topology

**Target:** an integral calculation of \(H^2(X,\mathbf Z)\) in which each matrix is proved to be the matrix of the actual geometric morphism in the stated bases.

**Decisive falsifiers:** a sign or nonprimitive meridian in based van Kampen; a different drift; a nonsaturated image; a transgression not equal to the displayed integer \(p\); or a mismatch between a printed matrix and the geometric map.

### ANA-REF: publication-level references

**Target:** bind the finite-complex theorem, analytic Serre-Grothendieck duality, and the nonnormal conductor formalism to exact cited statements with every hypothesis matched.

This is a source-binding task, not a newly found mathematical gap in the reconstructed arrows.

## Conclusion

The properness-flatness-duality-top-base-change chain is valid. The chain starts only after the candidate's global construction, central-fibre description, and integral \(H^2\)-vanishing have been supplied.

Base change is therefore no longer a plausible candidate-specific weak point. The highest-value unresolved work is the construction and integral topology, especially the exact geometric identification of the nearby-cycle/Leray and based van Kampen maps.

## Package contents

The evidence package contains this report, a claim-by-claim ledger, a candidate-specific test-program ledger, exact symbolic checks for the \(xy\) and \(xyz\) models, source excerpts for the relevant manuscript sections, the supplied current-progress transcript, and a fail-closed verification script.

The exact script certifies only the finite identities it names. It does not certify the global candidate inputs.

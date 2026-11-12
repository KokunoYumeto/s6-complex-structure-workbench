# Proper-flat surface base change without a smooth total space {#general-surface-base-change}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

This chapter proves the general surface theorem underlying the degree-two fibre map in [lesson 10](../CG-S6-10.html#duality-and-base-change). The total space need not be smooth or compact. The fibres retain their full analytic structure, including nilpotents. The existing [compact-smooth graph argument](proper-base-change-over-a-curve.md#graph-resolution) remains a separate, useful proof for the course's original threefold.

## 1. The statement and the exact map {#general-surface-theorem}

Let \(f:X\to B\) be a proper flat holomorphic map of complex analytic spaces, where \(B\) is a Riemann surface. Assume every full fibre has pure complex dimension two. Let \(E\) be a holomorphic vector bundle on \(X\). For \(b\in B\), write

\[
A=\mathcal O_{B,b},\qquad k(b)=A/\mathfrak m_b,\qquad
X_b=X\mathbin{\times}_B\{b\},\qquad E_b=E|_{X_b}.
\tag{1.1}
\]

**Theorem 1.1.** The higher direct images satisfy

\[
R^q f_*E=0\quad(q>2),\qquad
\beta_b^2:(R^2f_*E)_b\otimes_A k(b)
\xrightarrow{\ \sim\ }H^2(X_b,E_b).
\tag{1.2}
\]

Here \(\beta_b^2\) is the canonical restriction map, not an isomorphism selected by comparing dimensions. There is no assumption that the fibres are reduced, that \(h^2(X_b,E_b)\) is constant, or that \(R^2f_*E\) is locally free.

Two analytic inputs are needed. First, a bounded complex of finite free holomorphic modules must actually represent the derived direct image. Second, coherent cohomology on each compact full fibre must vanish above its dimension. Neither input follows merely from the other. Sections 2 and 3 give their exact proof routes; Sections 4 and 5 identify the fibre map and finish the deduction.

## 2. The relative finite complex {#general-relative-complex}

Fix \(b\). After shrinking to a disc \(U\) about \(b\), there is a bounded finite free complex \(P^\bullet\) on \(U\) and an identification

\[
P^\bullet\simeq Rf_*E|_U
\tag{2.1}
\]

given by actual comparison maps. The construction does not assume a smooth total space:

1. [FC-4](general-analytic-fc.md#FC-4) uses properness to cover the inverse image of a smaller closed base disc by finitely many nested analytic charts. Their finite intersections are represented as full closed analytic graphs in products of ambient Stein domains. The coefficient modules keep their original ideals.
2. [FC-3](general-analytic-fc.md#FC-3) proves the finite acyclic-cover comparison, including the augmented Čech differential, its total-complex signs and the comparison with an injective resolution.
3. [FC-0–FC-2](general-analytic-fc.md#FC-0) attach finite free terms, using nuclear perturbation after shrinking. The selected radii all remain above a fixed final radius. Thus the argument constructs a complex on one common neighbourhood; it does not take an uncontrolled infinite intersection of neighbourhoods.
4. [FC-5](general-analytic-fc.md#FC-5) proves that restriction to every Stein subopen preserves the actual comparison maps. The resulting sheaf-complex zigzag identifies the complex with \(Rf_*E\). Its coherent kernels, images and cokernels establish coherence of every \(R^qf_*E\).
5. [FC-6](general-analytic-fc.md#FC-6) bounds the complex at its lower end. If \(L^\bullet\) is the bounded-above representative and \(I=\operatorname{im}(d_L^{-1})\), then \(I\) is locally finite free on the smooth base curve. Replace the negative tail by \(I\hookrightarrow L^0\), with \(I\) in degree \(-1\). The map from \(L^\bullet\) to this bounded complex is a quasi-isomorphism.

The last step uses finite freeness of an image **submodule** of a free module over the discrete valuation ring \(A\). It does not assert that its quotient or any cohomology module is free. The finite-matrix proof and the passage from a stalk basis to a neighbourhood are included in FC-6.

The complete chain behind the construction is

\[
\text{nuclear sections}
\longrightarrow\text{transverse restriction}
\longrightarrow\text{relative perturbation}
\longrightarrow\text{finite complex}.
\tag{2.2}
\]

Its individual proofs are [NS-0–NS-6](general-analytic-ns.md#NS-0), [BT-0–BT-6](general-analytic-bt.md#BT-0), [RP-0–RP-5](general-analytic-rp.md#RP-0), and [FC-0–FC-6](general-analytic-fc.md#FC-0). In particular, the comparison cone uses

\[
C(h)^k=L^k\oplus E^{k-1},\qquad
D(\ell,e)=(d_L\ell,\,h\ell-d_Ee).
\tag{2.3}
\]

Those signs are retained in the finite-term attachments. This shifted comparison complex is distinct from the unshifted cone used for the fibre quotient in Section 4.

## 3. The compact coherent dimension bound {#general-dimension-bound}

The companion [QG-6](general-analytic-qg.md#QG-6) proves the following statement at full analytic structure:

\[
Z\text{ compact},\quad \dim Z\le n,\quad F\text{ coherent}
\quad\Longrightarrow\quad H^k(Z,F)=0\quad(k>n).
\tag{3.1}
\]

Its prerequisite chain is explicit. [QN-0–QN-5](general-analytic-qn.md#QN-0) supply the compatible Levi directions and strongly \(q\)-complete neighbourhoods. [WL-0–WL-6](general-analytic-wl.md#WL-0) establish weighted solvability, graph domains and approximation; the full Hermitian curvature identity required there is proved in [BK-0–BK-5](general-analytic-bk.md#BK-0), without a Kähler assumption. [CL-0–CL-5](general-analytic-cl.md#CL-0) pass to coherent coefficients. [QG-0–QG-5](general-analytic-qg.md#QG-0) then prove the gluing and exhaustion argument.

For (3.1), QG-6 constructs a strongly \((n+1)\)-convex exhaustion on the compact support by induction on its analytic strata. The reduced support is used to construct smooth functions only. The coherent sheaf and its full, possibly nonradical defining ideal are retained when applying the vanishing theorem. Reduction of a space's support is not used to replace its structure sheaf.

Properness makes \(X_b\) compact, and \(E_b\) is locally free over its full structure sheaf. Therefore (3.1) gives

\[
H^q(X_b,E_b)=0\qquad(q>2).
\tag{3.2}
\]

This fibrewise statement alone is not yet the direct-image vanishing in (1.2).

## 4. Why the comparison is the canonical full-fibre map {#general-canonical-fibre}

Choose a coordinate \(z\) on \(U\) with zero set \(\{b\}\), put \(V=f^{-1}(U)\), and write \(i:X_b\hookrightarrow V\) and \(j:\{b\}\hookrightarrow U\). Flatness and local freeness give the exact sequence

\[
0\longrightarrow E\xrightarrow{\ f^*z\ }E
\longrightarrow i_*E_b\longrightarrow0.
\tag{4.1}
\]

The quotient is by \((f^*z)\), not by its radical. Thus (4.1) includes all nilpotents in the fibre.

Take an injective resolution \(J^\bullet\) of \(E\) as an \(\mathcal O_V\)-module and set \(K^\bullet=f_*J^\bullet\). The cone of multiplication by \(f^*z\) has terms and differential

\[
\operatorname{Cone}(z:J\to J)^q=J^q\oplus J^{q+1},\qquad
d(a,c)=(d_Ja+zc,-d_Jc).
\tag{4.2}
\]

By (4.1), it resolves \(i_*E_b\). Its terms are finite sums of flabby sheaves, hence acyclic for \(f_*\). Applying \(f_*\) gives exactly \(\operatorname{Cone}(z:K\to K)\).

On the base, let

\[
T^\bullet=[\mathcal O_U\xrightarrow{\ z\ }\mathcal O_U]
\tag{4.3}
\]

in degrees \(-1,0\). This bounded free resolution of \(j_*k(b)\) is K-flat. In degree \(q\), the differential on \(K\otimes T\), with components \((a,c)\in K^q\oplus K^{q+1}\), is

\[
d(a,c)=(d_Ka+(-1)^{q+1}zc,\ d_Kc).
\tag{4.4}
\]

The map \((a,c)\mapsto(a,(-1)^{q+1}c)\) identifies (4.4) with (4.2). A flabby resolution on \(X_b\) stays flabby under its closed pushforward, so the latter direct image is \(j_*R\Gamma(X_b,E_b)\). Taking the stalk at \(b\) gives

\[
P_b^\bullet\otimes_A^{\mathbf L}k(b)
\simeq (Rf_*E)_b\otimes_A^{\mathbf L}k(b)
\simeq R\Gamma(X_b,E_b).
\tag{4.5}
\]

Every comparison comes from the restriction in (4.1). Consequently the induced map from ordinary cohomology modulo \(z\) is \(\beta_b^q\). If \(z\) is replaced by \(uz\) for a unit \(u\), multiplication by \(u\) in degree \(-1\) and the identity in degree zero define an augmentation-preserving chain map \(T_{uz}\to T_z\). Hence the resulting map does not depend on the chosen coordinate. [FC-7](general-analytic-fc.md#FC-7) gives the resolution and flat-tensor justifications used throughout this comparison.

## 5. The torsion term and the top-degree deduction {#general-top-degree}

Write \(M^q=(R^qf_*E)_b\). Since \(P_b^\bullet\) is termwise free, multiplication by \(z\) gives a short exact sequence of complexes. Its cohomology sequence and (4.5) yield

\[
0\longrightarrow M^q/zM^q
\xrightarrow{\ \beta_b^q\ }H^q(X_b,E_b)
\longrightarrow M^{q+1}[z]\longrightarrow0,
\qquad M[z]=\ker(z:M\to M).
\tag{5.1}
\]

The final term is not discarded in arbitrary degrees. The two-term resolution (4.3) identifies it with \(\operatorname{Tor}_1^A(M^{q+1},k(b))\).

For \(q>2\), (3.2) and (5.1) imply \(M^q=zM^q\). This is a finite \(A\)-module by the coherence proved in FC-5. Choose generators \(m_1,\ldots,m_r\) and write \(m_i=z\sum_j a_{ij}m_j\). The adjugate of \(I-z(a_{ij})\) shows that its determinant annihilates every generator. That determinant has residue \(1\), so it is a unit. Thus \(M^q=0\).

This holds at every base point, proving \(R^qf_*E=0\) for \(q>2\). In degree two, the last term of (5.1) is therefore zero. Its first arrow is exactly the canonical isomorphism in (1.2). This proves Theorem 1.1.

For comparison, the finite free complex

\[
A\xrightarrow{\ z\ }A
\tag{5.2}
\]

in degrees \(1,2\) has \(H^2=A/(z)\). Its degree-two fibre map is an isomorphism even though that cohomology module is not free and its fibre dimension jumps. This is an algebraic example explaining why the theorem does not assert local freeness; it is not an asserted geometric realization by a family of surfaces.

## 6. Prerequisite guide and proof boundaries {#general-prerequisites}

The nine companions linked above include all sixty arguments in the analytic construction. They use the following earlier programme results, rather than treating a bibliography entry as a proof:

- [Coherent sheaves and Oka's theorem](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/coherent-sheaves-and-okas-theorem.md): kernels, images, cokernels and finite local resolutions.
- [Cartan coherence and complex spaces](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/cartans-coherence-theorem-and-complex-spaces.md): full closed analytic structures and coherent closed pushforward.
- [Analytic germs and local parametrization](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/analytic-germs-local-parametrization-and-the-nullstellensatz.md): finite local components and dimension drop in the stratification.
- [Fréchet sections and Schwartz's theorem](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/frechet-spaces-of-sections-and-schwartzs-theorem.md): open mapping, section topologies and the compact-map finiteness argument.
- [Cartan A and B](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/theorems-a-and-b-on-stein-manifolds.md): coherent acyclicity and section generation on ambient Stein domains.
- [Finiteness on compact complex spaces](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/finiteness-on-compact-complex-spaces.md), Lemma 1.1: the full closed-embedding model of intersections. The finite-cover cohomology comparison is additionally proved in FC-3.
- [Plurisubharmonic functions and Stein manifolds](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/plurisubharmonic-functions-and-stein-manifolds.md) and [Stein domains](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/stein-domains-in-complex-space.md): ambient domains and products.
- [The Dolbeault complex](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/the-dolbeault-complex.md) and [the Hilbert-space argument for weighted solutions](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/complex-analytic-spaces-and-coherent-sheaves/src/hormanders-l2-estimates-on-pseudoconvex-domains.md): the indicated inputs of WL-1–WL-6.
- [Fourier and Sobolev prerequisite bridges](https://github.com/KokunoYumeto/open-math-courses/blob/da4341471768cc41daf24b8bb03236cb773b8e1b/docs/courses/elliptic-operators-and-boundary-problems/src/prerequisite-bridges.md), Sections 1–2: the Fourier inversion, Plancherel and integer Sobolev calculations used in WL-2. WL-2 supplies its own first-order local regularity argument; the separate higher-order regularity candidate is not imported with an unproved initial regularity assumption.

These are cross-course prerequisites. A download containing only CG-S6 does not thereby contain their full texts. The exact source identities and result locators belong to the accompanying dependency record.

The mathematical route follows Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012: Chapters VI–VII for the Hermitian identity and weighted estimates, and Chapter IX for q-convexity, nuclear sections and direct images. Each companion gives its narrower source locations. The new exposition does not change the source's terms or claim novelty for the classical results.

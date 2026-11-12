# Integral projective splitting for lesson 11 {#projective-provider}

This CC0 provider is written by GPT-6 Astra (OpenAI), at Ultra, October 2026, from the complete chain arguments of [the Thom/Euler provider](thom-euler-for-lesson11.md) and Sections 1–6 of *The Gysin sequence and projective splitting*, written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026, under CC0. The [unaltered latter source](../sources/gysin-sequence-and-projective-splitting.source.txt) is included. We give the full complex, compact-base argument used in lesson 11, including a finite-dimensional proof of the line tensor rule. No infinite-dimensional classification theorem is used. This is author self-review.

## 1. The exact Gysin maps {#gysin-maps}

Let \(V\to B\) be an oriented real rank-\(r\) bundle, \(r>0\), over a Hausdorff base. Write \(E\) for its total space, \(E_0\) for the complement of its zero section, and \(\pi\) for its projection. The exact cohomology sequence of the pair and the Thom isomorphism of the preceding provider give

\[
\cdots\longrightarrow H^{j-r}(B;G)
\xrightarrow{\,a\mapsto a\smile e(V)\,}H^j(B;G)
\xrightarrow{\pi_0^*}H^j(E_0;G)
\xrightarrow{\pi_!}H^{j-r+1}(B;G)
\xrightarrow{\,\smile e(V)\,}H^{j+1}(B;G)\longrightarrow\cdots .
\tag{1.1}
\]

Here \(G\) is any abelian group and the integral Euler class acts on these coefficient groups. Explicitly, if \(u_V\) is the positive Thom class, set \(\Phi(a)=\pi^*a\smile u_V\) and \(\pi_!=\Phi^{-1}\delta\), where \(\delta\) is the pair connecting map. The forgetful map sends \(u_V\) to \(\pi^*e(V)\); consequently it sends \(\Phi(a)\) to \(\pi^*(a\smile e(V))\). Fibre contraction identifies the cohomology of \(E\) with that of \(B\). These substitutions in the exact pair sequence prove (1.1), including the displayed maps and every degree. Negative-degree groups vanish. A metric retracts \(E_0\) onto \(S(V)\) by \(v\mapsto((1-t)+t/\|v\|)v\).

For later sign comparisons the convention also gives

\[
\pi_!(\pi_0^*b\smile y)=(-1)^{\deg b}b\smile\pi_!(y).
\tag{1.2}
\]

Indeed extend a cocycle for \(y\) to a cochain on \(E\). The coboundary of its product with the closed cochain \(\pi^*b\) is \((-1)^{\deg b}\pi^*b\) times its coboundary. Apply \(\Phi^{-1}\). This retains the sign determined by the chosen connecting map.

## 2. Finite projective spaces and their full integral groups {#finite-projective-space}

Define \(\mathbb{CP}^n\) as the set of complex lines in \(\mathbb C^{n+1}\), with its topology of rank-one orthogonal projections. It is a closed bounded set of matrices satisfying \(P^*=P\), \(P^2=P\), \(\operatorname{tr}P=1\), hence compact Hausdorff. Near a fixed line, projection to that line is invertible on any sufficiently close line; its graph is a continuous complex coordinate. These graph charts also trivialize the tautological line \(Q\).

There is one cell in each real dimension \(0,2,\ldots,2n\). More explicitly the attaching map of the closed unit ball in \(\mathbb C^q\) is

\[
z\longmapsto[z:\sqrt{1-\|z\|^2}].
\tag{2.1}
\]

Its boundary maps to \(\mathbb{CP}^{q-1}\). The interior maps bijectively to its complementary affine chart with coordinate \(z/\sqrt{1-\|z\|^2}\). Thus the attachment quotient is homeomorphic to \(\mathbb{CP}^q\): the resulting continuous bijection is from a compact space to a Hausdorff space, and images of closed sets are compact and closed.

Here is the singular-group calculation behind this cell argument. In a finite disk attachment, the preceding skeleton together with the outer collars \(\|z\|>1/2\) is an open neighbourhood that retracts to that skeleton by radial motion in each collar. The homotopy is continuous on the attachment quotient because its quotient map is a closed surjection of compact Hausdorff spaces, and its product with the interval is still closed and quotient. The triple exact sequence permits replacing the skeleton by this neighbourhood in relative homology. Excision then removes the skeleton and leaves the disjoint disk-interior/collar pairs. Each pair has the groups of \((D^d,S^{d-1})\): the sphere and pair calculation in the Thom/Euler provider gives one copy of \(\mathbb Z\) in degree \(d\), and zero otherwise. The same argument gives the relative cohomology with any coefficients. Induction over the finite attachments proves vanishing above the dimension. Because all cells here are even-dimensional, the intervening odd homology groups vanish. At each even attachment, the exact sequence therefore adds a free copy of \(\mathbb Z\) in precisely that degree and preserves lower groups. Hence \(H_{2i}(\mathbb{CP}^n;\mathbb Z)=\mathbb Z\) for \(0\le i\le n\), and all other homology groups vanish.

The unit sphere of \(Q\) is \(S^{2n+1}\), via \(v\mapsto([v],v)\), with inverse forgetting the line. A complex line has its real orientation \((v,iv)\); multiplication by a nonzero complex scalar has positive real determinant. Put \(x=-e(Q_{\mathbb R})\). For \(1\le j\le2n\), the positive sphere groups appearing beside the multiplication maps in (1.1) vanish. In degree one its degree-zero connecting map lands in a negative-degree group and is zero. It follows successively that the odd base cohomology groups vanish and multiplication by \(e(Q_{\mathbb R})\) is an isomorphism between successive even groups through degree \(2n\). Starting at \(H^0=\mathbb Z\), and using the dimension bound above, this proves

\[
H^*(\mathbb{CP}^n;\mathbb Z)=\mathbb Z[x]/(x^{n+1}).
\tag{2.2}
\]

The sign is fixed as follows. A Hermitian metric, linear in the first variable, gives the anti-complex-linear map \(w\mapsto\langle -,w\rangle\) from a line to its dual. Its real determinant is negative, so \(e(Q^*_{\mathbb R})=-e(Q_{\mathbb R})=x\). On \(\mathbb{CP}^1\), the functional \((z_0,z_1)\mapsto z_1\) is a section of \(Q^*\) with one zero at \([1:0]\). In the frame \((1,\zeta)\) its value is \(\zeta\), with positive local index. The sphere zero formula gives \(\langle x,[\mathbb{CP}^1]\rangle=1\), in the complex orientation. The stereographic map \([1:\zeta]\mapsto(2\Re\zeta,2\Im\zeta,1-|\zeta|^2)/(1+|\zeta|^2)\) preserves that orientation: at \(\zeta=0\), its two coordinate derivatives followed by the outward normal have positive determinant. This is the sign used in lesson 11.

## 3. The integral projective-bundle map {#projective-module}

For a complex rank-\(n\) bundle \(V\) over a Hausdorff base, let \(p:P(V)\to B\) be its bundle of lines. The chart construction gives a locally trivial Hausdorff bundle with fibre \(\mathbb{CP}^{n-1}\) and a tautological line \(S\subset p^*V\). Set \(z=-e(S_{\mathbb R})\). For every abelian group \(G\), the map

\[
\bigoplus_{i=0}^{n-1}H^{m-2i}(B;G)\longrightarrow H^m(P(V);G),\qquad
(b_i)\longmapsto\sum_{i=0}^{n-1}p^*b_i\smile z^i
\tag{3.1}
\]

is an isomorphism. In particular \(p^*\) is injective, including on integral torsion.

To prove this without a cohomological limit assumption, choose integral cocycles \(c_i\) for \(z^i\), with \(c_0=1\). The unshifted right cap operation of the Thom/Euler provider gives the chain map

\[
T:C_m(P(V);\mathbb Z)\longrightarrow\bigoplus_{i=0}^{n-1}C_{m-2i}(B;\mathbb Z),
\qquad T_i=p_*R_{c_i}.
\tag{3.2}
\]

Its cap identity proves commutation with the differentials; replacing a cocycle by a coboundary changes this map by the cap homotopy proved there. On a trivializing open set, \(z^i\) is the pullback of the fibre class in (2.2). The fibre singular complex is chain homotopy equivalent to \(\bigoplus_{i=0}^{n-1}\mathbb Z[2i]\): split its free boundary groups off the chain groups, split the free homology off its cycles, and contract each remaining boundary/preimage pair. Its projection to \(\mathbb Z[2i]\) can be chosen to be the cocycle dual to \(x^i\). The Alexander–Whitney and shuffle equivalence supplied in the Thom/Euler provider then identifies the product complex with the right side of (3.2). The projection is precisely \(p_*R_{c_i}\), since it evaluates on the last \(2i\)-face and retains the first face projected to the base. Thus (3.2) is a homology isomorphism on each such open set.

The maps preserve projected support. Apply them to the small-chain Mayer–Vietoris sequences for two base open sets and their inverse images. Their connecting maps commute because these are maps of exact chain sequences. The five lemma makes \(T\) an isomorphism over a union whenever it is one on the two sets and their intersection. Induction over a finite trivializing cover works: the intersection with the last chart has a cover by fewer trivializing sets. In particular this proves the assertion on every compact restricted base. Every cycle upstairs, downstairs, or witnessing a boundary has compact projected support; finite unions of such compact sets are compact. Therefore the global homology map is an isomorphism as well. This is a direct argument about finite chains, with no inverse limit of cohomology groups.

Apply the natural universal coefficient exact sequences, proved in the Thom/Euler provider, to the map of free complexes (3.2). Its Hom and Ext maps are isomorphisms because its homology maps are. Exactness therefore makes the dual cohomology map an isomorphism for every \(G\). Evaluation of a cochain on \(p_*R_{c_i}\) is exactly \(p^*b_i\smile c_i\); there are finitely many summands, so dualization retains their direct sum. This proves exactly (3.1). Associativity of cup product proves its compatibility with the base module structure.

## 4. Actual flag bundles over compact bases {#integral-flag-map}

Now let \(B\) be compact Hausdorff. The finite embedding and orthogonal-projection construction in lesson 11, Section 10.1, supplies a Hermitian metric on every bundle in use. Over \(P(V)\), take the orthogonal complement \(Q_1\) of its tautological line, so \(p_1^*V=S_1\oplus Q_1\). Projectivize \(Q_1\), take the next tautological line and its complement, and repeat until rank one. Orthogonal projection matrices depend continuously on the base and have constant rank; a fixed maximal independent set of columns remains independent nearby, so these images and kernels are actual local bundles. This constructs

\[
f:\operatorname{Flag}(V)\longrightarrow B,\qquad f^*V=L_1\oplus\cdots\oplus L_n.
\tag{4.1}
\]

Each projection in the tower has injective cohomology pullback by (3.1), so the composite does too, with integral or any other constant coefficients. Its total spaces are compact Hausdorff. For compactness, given an open cover upstairs, trivialize near a base point and cover its compact projective fibre by finitely many product neighbourhoods in that cover. Intersect their base neighbourhoods. These products cover all the fibres over this smaller neighbourhood. Finitely many such base neighbourhoods cover the compact base, yielding a finite subcover upstairs. The Hausdorff assertion follows by separating distinct base points downstairs or points over the same base point in a chart. Thus a second bundle can be split by a second flag tower over the first; the resulting common pullback is still injective and the space is still compact. Ranks zero and one require no tower.

## 5. Line tensor products, with a finite classifying map {#line-tensor-rule}

Define \(c_1(L)=e(L_{\mathbb R})\) for a complex line. Conjugation reverses its real orientation, so \(c_1(\bar L)=-c_1(L)\); the metric dual map above gives \(c_1(L^*)=-c_1(L)\).

For lines \(L,M\) on a compact Hausdorff base, choose finite embeddings \(L\hookrightarrow B\times\mathbb C^N\), \(M\hookrightarrow B\times\mathbb C^K\). Their image projections give continuous maps \(g:B\to\mathbb{CP}^{N-1}\), \(h:B\to\mathbb{CP}^{K-1}\). The embedding itself identifies \(L\) with \(g^*Q_N\) and \(M\) with \(h^*Q_K\), complex linearly on every fibre. Adding a trivial coordinate if necessary makes \(N,K\ge2\).

The product chain equivalence and free even homology of Section 2 give \(H_1(\mathbb{CP}^{N-1}\times\mathbb{CP}^{K-1};\mathbb Z)=0\) and \(H_2=\mathbb Z\oplus\mathbb Z\), with generators the projective lines in the two axes. The universal coefficient sequence therefore shows that a degree-two integral class is determined by restriction to these two axes. Let \(Q_1,Q_2\) be the two pulled-back tautological lines. On the first axis \(Q_2\) is a fixed one-dimensional vector space, so \(Q_1\otimes Q_2\) is isomorphic to \(Q_1\); on the second it is isomorphic to \(Q_2\). These isomorphisms preserve complex orientations. Euler naturality and this degree-two detection prove

\[
c_1(Q_1\otimes Q_2)=c_1(Q_1)+c_1(Q_2).
\]

Pull back by \((g,h)\) and retain the actual bundle identifications. We obtain

\[
c_1(L\otimes M)=c_1(L)+c_1(M),\qquad
c_1(\operatorname{Hom}_{\mathbb C}(L,M))=c_1(M)-c_1(L).
\tag{5.1}
\]

This applies on every compact flag space constructed above. The [Chern-class provider](integral-chern-classes-for-lesson11.md) now uses those exact maps.

## Human references and scope

John Milnor and James Stasheff, *Characteristic Classes* (1974), Section 12, is the human reference for Gysin sequences. Allen Hatcher, *Algebraic Topology* (2002), Section 4.D, Theorem 4D.1, is the human reference for Leray–Hirsch. Their protected text and figures are not reproduced. The preceding proofs preserve the integral maps, coefficient groups and signs from the cited CC0 source. The finite line classification in Section 5 establishes the entire tensor rule needed here without claiming a theorem about arbitrary infinite classifying spaces.

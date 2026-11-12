# Integral Chern classes and characters for lesson 11 {#chern-provider}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026, under CC0. These arguments use the complete [Thom/Euler](thom-euler-for-lesson11.md) and [projective splitting](projective-splitting-for-lesson11.md) providers included here. They reconstruct the compact-base portion of Sections 1–2 and 4 of *Chern classes and the integral universal ring*, written by GPT-6.1 Sol (OpenAI), at Ultra, under CC0; its [unaltered source](../sources/chern-classes-and-the-integral-universal-ring.source.txt) is retained. Author self-review is recorded separately from independent review.

## 1. Define the classes by the exact projective relation {#integral-definition}

Let \(V\to B\) be a complex bundle of rank \(r>0\) over a compact Hausdorff space. On \(p:P(V)\to B\), write \(S\) for the tautological line and \(z=-c_1(S)\). The integral projective module isomorphism of the previous provider says that \(1,z,\ldots,z^{r-1}\) are a free module basis over \(H^*(B;\mathbb Z)\). There are therefore unique classes \(c_i(V)\in H^{2i}(B;\mathbb Z)\) such that

\[
z^r+p^*c_1(V)z^{r-1}+\cdots+p^*c_r(V)=0.
\tag{1.1}
\]

Existence follows by expressing \(-z^r\) in that basis, uniqueness from its linear independence, and the degrees from the graded isomorphism. Set \(c_0(V)=1\), \(c_i(V)=0\) for \(i>r\), and \(c(0)=1\). For a line, \(P(V)=B\) and \(S=V\), so (1.1) is exactly the previously defined \(c_1(V)=e(V_{\mathbb R})\). Pullback of the projective relation under a bundle pullback between compact bases is the relation for the pulled-back bundle. Its uniqueness proves naturality.

Pull \(V\) to its actual flag bundle, where it splits into lines \(L_j\), and put \(t_j=c_1(L_j)\). On the projectivization of this split bundle, \(\operatorname{Hom}_{\mathbb C}(S,p^*V)\) has the nowhere-zero section given by the tautological inclusion. The Thom/Euler provider proves that its Euler class is zero. Its line summands are \(S^*\otimes p^*L_j\), so the line tensor and Euler product rules give

\[
0=\prod_{j=1}^r(z+p^*t_j).
\tag{1.2}
\]

All summands have even real dimension; their ordered complex orientations introduce no permutation signs. Expansion and uniqueness in (1.1) now prove

\[
f^*c_i(V)=e_i(t_1,\ldots,t_r),\qquad
f^*c_r(V)=\prod_jt_j=f^*e(V_{\mathbb R}),
\tag{1.3}
\]

where \(e_i\) is the sum of all products of \(i\) distinct variables. Since integral flag pullback is injective, including on torsion, the second equality descends to

\[
c_r(V)=e(V_{\mathbb R})
\tag{1.4}
\]

in the orientation determined by the actual complex structure. In particular no rational differential form has been used to define or identify this integral class.

## 2. Sum, conjugation, and the comparison with the Euler construction {#chern-rules}

Pass to a common compact flag space for \(V\) and \(W\). Their roots there are \(t_i\) and \(u_j\). The elementary symmetric polynomial of the combined list is the product of their total elementary symmetric polynomials. Injective pullback therefore proves

\[
c(V\oplus W)=c(V)c(W),\qquad c(\mathbb C^k)=1.
\tag{2.1}
\]

The latter follows because a trivial line has a nowhere-zero section and Euler class zero. Thus the classes are stable. On the same flag space \(\bar V\) splits into \(\bar L_i\), whose first classes are \(-t_i\) by the orientation calculation. Each elementary symmetric polynomial of degree \(i\) acquires the sign \((-1)^i\), giving

\[
c_i(\bar V)=(-1)^i c_i(V).
\tag{2.2}
\]

A Hermitian metric linear in the first variable gives the complex-linear isomorphism \(\bar V\to V^*\), \(\bar v\mapsto\langle -,v\rangle\). Indeed multiplying \(\bar v\) by \(\lambda\) replaces \(v\) by \(\bar\lambda v\), so it multiplies the functional by \(\lambda\). This proves the same rule for the dual.

For an exact comparison with the source's Euler/Gysin definition, restrict to the compact sphere bundle \(\pi:S(V)\to B\). On it the unit vector is a global nonzero section of \(\pi^*V\); its orthogonal complement \(Q\) has rank \(r-1\), and \(\pi^*V=\mathbb C\oplus Q\). The rank-\(2r\) real Gysin sequence in the previous provider gives an isomorphism

\[
\pi^*:H^{2i}(B;\mathbb Z)\xrightarrow{\cong}H^{2i}(S(V);\mathbb Z),\qquad i<r,
\tag{2.3}
\]

because the two groups adjoining it have degrees \(2i-2r\) and \(2i-2r+1\), both negative. The source definition sets the top class equal to the Euler class and uniquely specifies every lower class by \(\pi^*c_i(V)=c_i(Q)\), inductively in rank. Our classes have the same top value by (1.4) and the same lower pullbacks by (2.1) and naturality. Starting with rank one, (2.3) therefore proves equality of all these classes with that definition. The source's deleted total space retracts radially onto \(S(V)\); its tautological quotient restricts to precisely \(Q\). The retraction and pullback maps give the exact comparison, so no noncompact-base classification result is hidden in this argument.

More generally, any natural classes satisfying the line normalization and Whitney formula agree with these on compact bases: pull them to the flag space, apply the Whitney formula to its actual line sum, then use injectivity. This proves uniqueness with every integral contribution retained.

## 3. Define and prove the Chern-character operations {#character-operations}

Write \(s_j(t)=\sum_a t_a^j\). These are integral polynomials in the elementary symmetric polynomials. To see this constructively, take the formal logarithmic derivative of the finite polynomial

\[
c_t=\prod_a(1+t_at)=\sum_{i=0}^r c_i t^i.
\]

In the formal power series ring, its constant coefficient one makes it invertible. Expanding each factor's geometric series gives

\[
\frac{d c_t}{dt}=c_t\sum_{j\ge1}(-1)^{j-1}s_jt^{j-1}.
\tag{3.1}
\]

Comparing the coefficient of \(t^{j-1}\) gives a recursion determining \(s_j\) as an integral polynomial in \(c_1,\ldots,c_j\), with every term present. Define, degree by degree in rational cohomology,

\[
\operatorname{ch}(V)=r+\sum_{j\ge1}\frac{s_j(c_1(V),\ldots,c_j(V))}{j!}.
\tag{3.2}
\]

For an arbitrary base the meaning is the sequence of its homogeneous terms; on a finite-dimensional base only finitely many can be nonzero. On a flag space this is \(\sum_a e^{t_a}\), with the exponential also interpreted degree by degree. The direct sum joins the root lists. The tensor product splits into lines \(L_i\otimes M_j\), whose first classes are \(t_i+u_j\) by the proved line rule. The binomial identity in each finite homogeneous degree proves \(e^{t+u}=e^te^u\). Rational flag pullback is injective by the same projective module theorem, so

\[
\operatorname{ch}(V\oplus W)=\operatorname{ch}(V)+\operatorname{ch}(W),\qquad
\operatorname{ch}(V\otimes W)=\operatorname{ch}(V)\operatorname{ch}(W).
\tag{3.3}
\]

Additivity extends the character to the Grothendieck group by \([V]-[W]\mapsto\operatorname{ch}(V)-\operatorname{ch}(W)\). If two presentations become isomorphic after adding the same bundle, (3.3) makes these differences equal, which proves that the extension is well-defined. The tensor identity makes it a ring map; the trivial rank-one bundle maps to one. This is exactly the integral-class character used on products of two-spheres in lesson 11, Section 10.3. It retains the rank, factorial, and conjugate contributions required in Sections 10.4–10.5.

## Human reference and receiving maps

John Milnor and James Stasheff, *Characteristic Classes* (1974), Sections 13–14, especially Theorem 14.5, Lemma 14.9, Theorem 14.10 and the Whitney formula, is the human reference. Its protected wording is not reproduced. The included CC0 source records its own reading history; the present author inspected its integral construction, projective comparison and conjugation proofs. The exact receiving maps are (1.4) for the sphere Euler number, (2.2) for the complexified real stable trivialization, and (3.3) for the product basis in the Bott-integrality calculation. This provider does not claim a separate computation of the entire universal Grassmannian ring.

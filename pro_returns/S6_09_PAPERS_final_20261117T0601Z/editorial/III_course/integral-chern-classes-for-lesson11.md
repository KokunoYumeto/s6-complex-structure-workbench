\section{Integral Chern classes}\label{courseIII:integral-chern-classes-for-lesson11:section}
The following complete arguments are retained as re-derivations of their classical prerequisites. Source-specific calculations and their hypotheses are stated explicitly.

\subsection{Define the classes by the exact projective relation}
\label{courseIII:integral-chern-classes-for-lesson11:integral-definition}\label{courseIII:integral-chern-classes-for-lesson11:section-1}\label{courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-1}

Let \(V\to B\) be a complex bundle of rank \(r>0\) over a compact Hausdorff space. On \(p:P(V)\to B\), write \(S\) for the tautological line and \(z=-c_1(S)\). The integral projective module isomorphism of the previous provider says that \(1,z,\ldots,z^{r-1}\) are a free module basis over \(H^*(B;\mathbb Z)\). There are therefore unique classes \(c_i(V)\in H^{2i}(B;\mathbb Z)\) such that



```{=latex}
\begin{equation}
z^r+p^*c_1(V)z^{r-1}+\cdots+p^*c_r(V)=0.
\label{courseIII:integral-chern-classes-for-lesson11:eq:1.1}
\end{equation}
```



Existence follows by expressing \(-z^r\) in that basis, uniqueness from its linear independence, and the degrees from the graded isomorphism. Set \(c_0(V)=1\), \(c_i(V)=0\) for \(i>r\), and \(c(0)=1\). For a line, \(P(V)=B\) and \(S=V\), so \eqref{courseIII:integral-chern-classes-for-lesson11:eq:1.1} is exactly the previously defined \(c_1(V)=e(V_{\mathbb R})\). Pullback of the projective relation under a bundle pullback between compact bases is the relation for the pulled-back bundle. Its uniqueness proves naturality.

Pull \(V\) to its actual flag bundle, where it splits into lines \(L_j\), and put \(t_j=c_1(L_j)\). On the projectivization of this split bundle, \(\operatorname{Hom}_{\mathbb C}(S,p^*V)\) has the nowhere-zero section given by the tautological inclusion. The Thom/Euler provider proves that its Euler class is zero. Its line summands are \(S^*\otimes p^*L_j\), so the line tensor and Euler product rules give



```{=latex}
\begin{equation}
0=\prod_{j=1}^r(z+p^*t_j).
\label{courseIII:integral-chern-classes-for-lesson11:eq:1.2}
\end{equation}
```



All summands have even real dimension; their ordered complex orientations introduce no permutation signs. Expansion and uniqueness in \eqref{courseIII:integral-chern-classes-for-lesson11:eq:1.1} now prove



```{=latex}
\begin{equation}
f^*c_i(V)=e_i(t_1,\ldots,t_r),\qquad
f^*c_r(V)=\prod_jt_j=f^*e(V_{\mathbb R}),
\label{courseIII:integral-chern-classes-for-lesson11:eq:1.3}
\end{equation}
```



where \(e_i\) is the sum of all products of \(i\) distinct variables. Since integral flag pullback is injective, including on torsion, the second equality descends to



```{=latex}
\begin{equation}
c_r(V)=e(V_{\mathbb R})
\label{courseIII:integral-chern-classes-for-lesson11:eq:1.4}
\end{equation}
```



in the orientation determined by the actual complex structure. In particular no rational differential form has been used to define or identify this integral class.

\subsection{Sum, conjugation, and the comparison with the Euler construction}
\label{courseIII:integral-chern-classes-for-lesson11:chern-rules}\label{courseIII:integral-chern-classes-for-lesson11:section-2}\label{courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-2}

Pass to a common compact flag space for \(V\) and \(W\). Their roots there are \(t_i\) and \(u_j\). The elementary symmetric polynomial of the combined list is the product of their total elementary symmetric polynomials. Injective pullback therefore proves



```{=latex}
\begin{equation}
c(V\oplus W)=c(V)c(W),\qquad c(\mathbb C^k)=1.
\label{courseIII:integral-chern-classes-for-lesson11:eq:2.1}
\end{equation}
```



The latter follows because a trivial line has a nowhere-zero section and Euler class zero. Thus the classes are stable. On the same flag space \(\bar V\) splits into \(\bar L_i\), whose first classes are \(-t_i\) by the orientation calculation. Each elementary symmetric polynomial of degree \(i\) acquires the sign \((-1)^i\), giving



```{=latex}
\begin{equation}
c_i(\bar V)=(-1)^i c_i(V).
\label{courseIII:integral-chern-classes-for-lesson11:eq:2.2}
\end{equation}
```



A Hermitian metric linear in the first variable gives the complex-linear isomorphism \(\bar V\to V^*\), \(\bar v\mapsto\langle -,v\rangle\). Indeed multiplying \(\bar v\) by \(\lambda\) replaces \(v\) by \(\bar\lambda v\), so it multiplies the functional by \(\lambda\). This proves the same rule for the dual.

For an exact comparison with the source's Euler/Gysin definition, restrict to the compact sphere bundle \(\pi:S(V)\to B\). On it the unit vector is a global nonzero section of \(\pi^*V\); its orthogonal complement \(Q\) has rank \(r-1\), and \(\pi^*V=\mathbb C\oplus Q\). The rank-\(2r\) real Gysin sequence in the previous provider gives an isomorphism



```{=latex}
\begin{equation}
\pi^*:H^{2i}(B;\mathbb Z)\xrightarrow{\cong}H^{2i}(S(V);\mathbb Z),\qquad i<r,
\label{courseIII:integral-chern-classes-for-lesson11:eq:2.3}
\end{equation}
```



because the two groups adjoining it have degrees \(2i-2r\) and \(2i-2r+1\), both negative. The source definition sets the top class equal to the Euler class and uniquely specifies every lower class by \(\pi^*c_i(V)=c_i(Q)\), inductively in rank. Our classes have the same top value by \eqref{courseIII:integral-chern-classes-for-lesson11:eq:1.4} and the same lower pullbacks by \eqref{courseIII:integral-chern-classes-for-lesson11:eq:2.1} and naturality. Starting with rank one, \eqref{courseIII:integral-chern-classes-for-lesson11:eq:2.3} therefore proves equality of all these classes with that definition. The source's deleted total space retracts radially onto \(S(V)\); its tautological quotient restricts to precisely \(Q\). The retraction and pullback maps give the exact comparison, so no noncompact-base classification result is hidden in this argument.

More generally, any natural classes satisfying the line normalization and Whitney formula agree with these on compact bases: pull them to the flag space, apply the Whitney formula to its actual line sum, then use injectivity. This proves uniqueness with every integral contribution retained.

\subsection{Define and prove the Chern-character operations}
\label{courseIII:integral-chern-classes-for-lesson11:character-operations}\label{courseIII:integral-chern-classes-for-lesson11:section-3}\label{courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-3}

Write \(s_j(t)=\sum_a t_a^j\). These are integral polynomials in the elementary symmetric polynomials. To see this constructively, take the formal logarithmic derivative of the finite polynomial



```{=latex}
\[
c_t=\prod_a(1+t_at)=\sum_{i=0}^r c_i t^i.
\]
```



In the formal power series ring, its constant coefficient one makes it invertible. Expanding each factor's geometric series gives



```{=latex}
\begin{equation}
\frac{d c_t}{dt}=c_t\sum_{j\ge1}(-1)^{j-1}s_jt^{j-1}.
\label{courseIII:integral-chern-classes-for-lesson11:eq:3.1}
\end{equation}
```



Comparing the coefficient of \(t^{j-1}\) gives a recursion determining \(s_j\) as an integral polynomial in \(c_1,\ldots,c_j\), with every term present. Define, degree by degree in rational cohomology,



```{=latex}
\begin{equation}
\operatorname{ch}(V)=r+\sum_{j\ge1}\frac{s_j(c_1(V),\ldots,c_j(V))}{j!}.
\label{courseIII:integral-chern-classes-for-lesson11:eq:3.2}
\end{equation}
```



For an arbitrary base the meaning is the sequence of its homogeneous terms; on a finite-dimensional base only finitely many can be nonzero. On a flag space this is \(\sum_a e^{t_a}\), with the exponential also interpreted degree by degree. The direct sum joins the root lists. The tensor product splits into lines \(L_i\otimes M_j\), whose first classes are \(t_i+u_j\) by the proved line rule. The binomial identity in each finite homogeneous degree proves \(e^{t+u}=e^te^u\). Rational flag pullback is injective by the same projective module theorem, so



```{=latex}
\begin{equation}
\operatorname{ch}(V\oplus W)=\operatorname{ch}(V)+\operatorname{ch}(W),\qquad
\operatorname{ch}(V\otimes W)=\operatorname{ch}(V)\operatorname{ch}(W).
\label{courseIII:integral-chern-classes-for-lesson11:eq:3.3}
\end{equation}
```



Additivity extends the character to the Grothendieck group by \([V]-[W]\mapsto\operatorname{ch}(V)-\operatorname{ch}(W)\). If two presentations become isomorphic after adding the same bundle, \eqref{courseIII:integral-chern-classes-for-lesson11:eq:3.3} makes these differences equal, which proves that the extension is well-defined. The tensor identity makes it a ring map; the trivial rank-one bundle maps to one. This is exactly the integral-class character used on products of two-spheres in lesson 11, Section 10.3. It retains the rank, factorial, and conjugate contributions required in Sections 10.4–10.5.


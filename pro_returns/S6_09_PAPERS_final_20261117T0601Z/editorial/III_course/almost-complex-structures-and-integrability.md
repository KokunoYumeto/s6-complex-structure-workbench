\section{Almost complex structures, octonions, and integrability}\label{courseIII:almost-complex-structures-and-integrability:section}
The following complete arguments are retained as re-derivations of their classical prerequisites. Source-specific calculations and their hypotheses are stated explicitly.



The construction in this course gives complex coordinate charts on a compact six-dimensional manifold. The standard octonion construction gives an endomorphism of the tangent bundle of the round six-sphere. To compare these objects, we need the exact map from coordinate charts to a tangent-bundle endomorphism and the exact obstruction to reversing that map. We develop those maps first. We then calculate the obstruction for the octonion field, including its relation to the associator and all constants in its norm.

The multiplication formulas below are compared directly with [John Baez, *The Octonions*, Section 2.2](https://arxiv.org/abs/math/0105155v4). The sphere background is treated by [Panagiotis Konstantis and Maurizio Parton, *Almost complex structures on spheres*](https://arxiv.org/abs/1707.03883v1). The later coordinate construction follows the factorization of Malgrange as developed in [C. Denson Hill and Michael Taylor, *Integrability of Rough Almost Complex Structures*, Sections 2–4](https://arxiv.org/abs/0710.2310v2). We keep their matrix conventions when comparing formulas and identify the sign correction needed in their equation 3.14.

\subsection{From charts to a tensor, and from a tensor to a differential equation}
\label{courseIII:almost-complex-structures-and-integrability:charts-and-tensors}\label{courseIII:almost-complex-structures-and-integrability:section-1}

Let \(M\) be a smooth real manifold of dimension \(2n\). An **almost complex structure** is a smooth real bundle endomorphism



```{=latex}
\begin{equation}
J:TM\longrightarrow TM,\qquad J^2=-\operatorname{id}_{TM}.
\label{courseIII:almost-complex-structures-and-integrability:eq:1.1}
\end{equation}
```



It makes each real tangent space a complex vector space by
\((a+ib)v=av+bJv\). The coefficients \(a,b\) are real, and the relation \(J^2=-1\) verifies multiplication by two complex scalars. Conversely multiplication by \(i\) in a complex vector-bundle structure on \(TM\) satisfies \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.1}. These two operations are inverse.

If \(z:U\to\mathbb C^n\) is a complex coordinate chart, let \(I\) denote multiplication by \(i\) on the real tangent spaces of \(\mathbb C^n\), and set



```{=latex}
\begin{equation}
J|_U=(Dz)^{-1}I(Dz).
\label{courseIII:almost-complex-structures-and-integrability:eq:1.2}
\end{equation}
```



For overlapping holomorphic charts \(z,w\), their transition derivative satisfies \(D(w\circ z^{-1})I=I D(w\circ z^{-1})\), so \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.2} agrees on the overlap. A complex atlas therefore defines an almost complex structure. A structure obtained in this way is called **integrable**.

The inverse problem asks for a local map \(F:U\to\mathbb C^n\), with invertible real differential, satisfying



```{=latex}
\begin{equation}
dF\circ J=i\,dF.
\label{courseIII:almost-complex-structures-and-integrability:eq:1.3}
\end{equation}
```



Such maps are precisely the required complex coordinate charts: the real inverse-function theorem makes them charts, and the chain rule makes their transition maps satisfy the ordinary Cauchy–Riemann equations. For completeness, a \(C^1\) map between open subsets of \(\mathbb C^n\) whose differential is complex-linear is holomorphic. On a closed polydisc in its domain, each component is holomorphic in one variable with the others fixed, by the one-variable Cauchy–Riemann theorem. Apply the one-variable Cauchy integral formula in each variable successively. The resulting product Cauchy integral has a convergent multivariable power series on every smaller polydisc, and equals the original component. Thus the transitions are holomorphic in the atlas sense.

Complexify the real tangent bundle and extend \(J\) complex-linearly. Define



```{=latex}
\begin{equation}
\begin{gathered}
T^{1,0}_JM=\ker(J-i),\qquad T^{0,1}_JM=\ker(J+i),\\
\pi^{1,0}=\tfrac12(1-iJ),\qquad
\pi^{0,1}=\tfrac12(1+iJ).
\end{gathered}
\label{courseIII:almost-complex-structures-and-integrability:eq:1.4}
\end{equation}
```



Multiplication of these operators gives \((\pi^{1,0})^2=\pi^{1,0}\), \((\pi^{0,1})^2=\pi^{0,1}\), \(\pi^{1,0}\pi^{0,1}=0\), and \(\pi^{1,0}+\pi^{0,1}=1\). Complex conjugation interchanges their images. In particular both eigenbundles have complex rank \(n\).

The **Nijenhuis tensor** used throughout this lesson is



```{=latex}
\begin{equation}
N_J(X,Y)=[JX,JY]-[X,Y]-J[JX,Y]-J[X,JY].
\label{courseIII:almost-complex-structures-and-integrability:eq:1.5}
\end{equation}
```



Its sign is the negative of the convention in Hill–Taylor equation 1.2. Write \(N_{\mathrm{HT}}=-N_J\) when comparing those sources. Their zero conditions agree because multiplication by \(-1\) is an invertible bundle map.

We verify that \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5} is a tensor rather than an operator depending on the chosen extensions of tangent vectors. Inserting \(fX\) for \(X\), the four extra derivative terms, in their displayed order, are



```{=latex}
\begin{equation}
-(JYf)JX,\quad (Yf)X,\quad -(Yf)X,\quad (JYf)JX.
\label{courseIII:almost-complex-structures-and-integrability:eq:1.6}
\end{equation}
```



They sum to zero. Thus \(N_J(fX,Y)=fN_J(X,Y)\). Skewness in \(X,Y\) gives linearity in the second argument as well. Substituting \(JX\) or \(JY\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5} and using \(J^2=-1\) also gives



```{=latex}
\begin{equation}
N_J(JX,Y)=N_J(X,JY)=-J N_J(X,Y).
\label{courseIII:almost-complex-structures-and-integrability:eq:1.7}
\end{equation}
```



These identities include the exact real-to-complex type information. For sections \(Z,W\) of \(T^{0,1}_JM\), complex bilinearity and \(JZ=-iZ\) give



```{=latex}
\begin{equation}
N_J(Z,W)=-2[Z,W]+2iJ[Z,W]
=-4\pi^{1,0}[Z,W].
\label{courseIII:almost-complex-structures-and-integrability:eq:1.8}
\end{equation}
```



For two sections of \(T^{1,0}_JM\) the corresponding formula is \(-4\pi^{0,1}[Z,W]\). For one section of each type all four terms in \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5} cancel. Consequently



```{=latex}
\begin{equation}
N_J=0\quad\Longleftrightarrow\quad
[\Gamma(T^{0,1}_JM),\Gamma(T^{0,1}_JM)]
\subseteq\Gamma(T^{0,1}_JM).
\label{courseIII:almost-complex-structures-and-integrability:eq:1.9}
\end{equation}
```



The right side is **involutivity**. In complex coordinates the fields \(\partial/\partial\bar z_j\) span this bundle and commute; the bracket formula for their smooth linear combinations proves involutivity. Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.8}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:1.9} prove that every integrable \(J\) has \(N_J=0\).

There is a useful scalar version of the same obstruction. Let \(\bar\partial_J f\) be the \((0,1)\) part of \(df\), and on forms define \(\bar\partial_J\) to be the \((p,q+1)\) component of the exterior derivative of a \((p,q)\) form. For \(Z,W\) of type \((0,1)\), the definition of exterior derivative gives



```{=latex}
\begin{equation}
\begin{aligned}
(\bar\partial_J^2f)(Z,W)
&=Z(Wf)-W(Zf)-(\bar\partial_Jf)([Z,W])\\
&=df\bigl(\pi^{1,0}[Z,W]\bigr)
=-\tfrac14df\bigl(N_J(Z,W)\bigr).
\end{aligned}
\label{courseIII:almost-complex-structures-and-integrability:eq:1.10}
\end{equation}
```



Thus the obstruction is both a bundle map and the failure of this first-order operator to square to zero on functions. All factors in their comparison are explicit.

\subsection{Two octonion formulas and the exact map between them}
\label{courseIII:almost-complex-structures-and-integrability:octonion-comparison}\label{courseIII:almost-complex-structures-and-integrability:section-2}

We first construct the needed algebraic identities. This also fixes every multiplication sign used later. Represent the quaternions by



```{=latex}
\begin{equation}
Q(\alpha,\beta)=
\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix},
\qquad \alpha,\beta\in\mathbb C.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.1}
\end{equation}
```



Matrix multiplication gives



```{=latex}
\begin{equation}
Q(\alpha,\beta)Q(\gamma,\delta)
=Q(\alpha\gamma-\beta\bar\delta,
\alpha\delta+\beta\bar\gamma).
\label{courseIII:almost-complex-structures-and-integrability:eq:2.2}
\end{equation}
```



Conjugation \(q\mapsto\bar q\) is matrix adjoint; the norm squared is the determinant \(|\alpha|^2+|\beta|^2\). Hence \(|ab|=|a||b|\), \(\overline{ab}=\bar b\bar a\), and \(a\bar a=|a|^2\). The real part \(\operatorname{Re}a=\frac12\operatorname{tr}a\) is unchanged by cyclic permutation of a product. Set



```{=latex}
\begin{equation}
i=Q(i,0),\quad j=Q(0,1),\quad k=Q(0,i).
\label{courseIII:almost-complex-structures-and-integrability:eq:2.3}
\end{equation}
```



Direct multiplication gives \(ij=k,jk=i,ki=j\), their reversed products with minus signs, and \(i^2=j^2=k^2=-1\). The quaternion product is associative because it is matrix multiplication.

On \(\mathbb H\oplus\mathbb H\), the product used for our labelled sphere is



```{=latex}
\begin{equation}
(a,b)\cdot(c,d)=(ac-\bar d b,\;da+b\bar c),
\quad \overline{(a,b)}=(\bar a,-b),
\quad |(a,b)|^2=|a|^2+|b|^2.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.4}
\end{equation}
```



Baez's Cayley–Dickson formula in Section 2.2 is



```{=latex}
\begin{equation}
(a,b)\star(c,d)=(ac-d\bar b,\;\bar a d+cb),
\quad (a,b)^*=(\bar a,-b).
\label{courseIII:almost-complex-structures-and-integrability:eq:2.5}
\end{equation}
```



Neither formula is being substituted silently for the other. Define



```{=latex}
\begin{equation}
\Phi:(\mathbb H\oplus\mathbb H,\cdot)
\longrightarrow(\mathbb H\oplus\mathbb H,\star),
\qquad \Phi(a,b)=(a,\bar b).
\label{courseIII:almost-complex-structures-and-integrability:eq:2.6}
\end{equation}
```



It is real-linear, norm preserving, fixes \((1,0)\), and has inverse itself. Most importantly,



```{=latex}
\begin{equation}
\begin{aligned}
\Phi(a,b)\star\Phi(c,d)
&=(ac-\bar d b,\;\bar a\bar d+c\bar b)\\
&=\bigl(ac-\bar d b,\;\overline{da+b\bar c}\bigr)\\
&=\Phi\bigl((a,b)\cdot(c,d)\bigr).
\end{aligned}
\label{courseIII:almost-complex-structures-and-integrability:eq:2.7}
\end{equation}
```



Also \(\Phi(\overline{(a,b)})=(\bar a,-\bar b)=\Phi(a,b)^*\). Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.6}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:2.7} prove a unital isometric real algebra isomorphism, including conjugation. They transport associators and cross products with no discarded term.

Hereafter write \(xy\) for \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.4}, and call this algebra \(\mathbb O\). Its identity is \(1=(1,0)\). Expanding the norm gives



```{=latex}
\begin{equation}
\begin{aligned}
|ac-\bar d b|^2
&=|a|^2|c|^2+|d|^2|b|^2-2\operatorname{Re}(ac\bar b d),\\
|da+b\bar c|^2
&=|d|^2|a|^2+|b|^2|c|^2+2\operatorname{Re}(dac\bar b).
\end{aligned}
\label{courseIII:almost-complex-structures-and-integrability:eq:2.8}
\end{equation}
```



The displayed cross terms cancel by the cyclic trace identity in the associative quaternion algebra. Therefore



```{=latex}
\begin{equation}
|xy|^2=|x|^2|y|^2.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.9}
\end{equation}
```



This calculation does not assume associativity of the octonions.

Let \(L_x\) be the real linear map \(y\mapsto xy\), and let \(L_x^*\) be its adjoint for the Euclidean inner product associated with \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.4}. Polarizing \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.9} in \(y\) gives \(L_x^*L_x=|x|^2I\). Expanding \(|(1+tx)y|^2=|1+tx|^2|y|^2\) in real \(t\), and then polarizing in \(y\), gives



```{=latex}
\begin{equation}
L_x+L_x^*=2\operatorname{Re}(x)I.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.10}
\end{equation}
```



For \(x\) in the seven-dimensional imaginary space \(\operatorname{Im}\mathbb O=1^\perp\), it follows that



```{=latex}
\begin{equation}
L_x^*=-L_x,\qquad L_x^2=-|x|^2I.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.11}
\end{equation}
```



Applying the last identity to \(1\), and polarizing, gives \(x^2=-|x|^2\) and \(xy+yx=-2\langle x,y\rangle\) for imaginary \(x,y\). Also \(\operatorname{Re}(xy)=\langle L_xy,1\rangle=-\langle y,x\rangle\). Define their cross product by



```{=latex}
\begin{equation}
xy=-\langle x,y\rangle+x\times y.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.12}
\end{equation}
```



It is imaginary, bilinear and skew. The identity
\(\langle L_xy,L_x1\rangle=|x|^2\langle y,1\rangle=0\)
proves perpendicularity to \(x\), and skewness then proves perpendicularity to \(y\). Separating real and imaginary parts of \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.9} gives



```{=latex}
\begin{equation}
|x\times y|^2=|x|^2|y|^2-\langle x,y\rangle^2.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.13}
\end{equation}
```



Applying \(L_x^2\) to \(y\) and using \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.12} twice gives the full repeated-product identity



```{=latex}
\begin{equation}
x\times(x\times y)=-|x|^2y+\langle x,y\rangle x.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.14}
\end{equation}
```



Finally \(L_x^*=-L_x\) gives
\(\langle x\times y,z\rangle=-\langle x\times z,y\rangle\).
Together with skewness in \(x,y\), this says that



```{=latex}
\begin{equation}
\varphi(x,y,z)=\langle x\times y,z\rangle
\label{courseIII:almost-complex-structures-and-integrability:eq:2.15}
\end{equation}
```



is an alternating trilinear form. Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.13}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:2.15} are proved consequences of the original product; none requires suppressing its nonassociativity.

Use the ordered orthonormal basis



```{=latex}
\begin{equation}
\begin{gathered}
e_1=(i,0),\ e_2=(j,0),\ e_3=(k,0),\ e_4=(0,1),\\
e_5=(0,i),\ e_6=(0,j),\ e_7=(0,k).
\end{gathered}
\label{courseIII:almost-complex-structures-and-integrability:eq:2.16}
\end{equation}
```



The complete imaginary multiplication table is specified by the oriented triples



```{=latex}
\begin{equation}
123,\quad145,\quad176,\quad246,\quad257,\quad347,\quad365.
\label{courseIII:almost-complex-structures-and-integrability:eq:2.17}
\end{equation}
```



In a triple \(abc\), the products \(e_ae_b=e_c,e_be_c=e_a,e_ce_a=e_b\) have positive sign; reversed products are negative, and \(e_a^2=-1\). Each unordered pair of distinct indices occurs in exactly one triple, so this specifies all products. Substituting \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.3} in \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.4} verifies the seven displayed triples and hence, by skewness, the entire table.

\subsection{The round six-sphere and its complete Nijenhuis tensor}
\label{courseIII:almost-complex-structures-and-integrability:round-sphere-obstruction}\label{courseIII:almost-complex-structures-and-integrability:section-3}

Let



```{=latex}
\begin{equation}
S^6=\{p\in\operatorname{Im}\mathbb O:|p|=1\},
\qquad T_pS^6=p^\perp,
\qquad J_pU=p\times U.
\label{courseIII:almost-complex-structures-and-integrability:eq:3.1}
\end{equation}
```



Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.14} gives \(J_p^2U=-U\) on \(p^\perp\), with the coefficient \(|p|^2=1\) retained from the defining sphere. Perpendicularity makes \(J_pU\) tangent, and \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.13} gives \(|J_pU|=|U|\). Thus \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1} is a smooth orthogonal almost complex structure for the round metric.

Write \(D\) for ambient differentiation and \(\nabla\) for tangential projection. Differentiating \(\langle V,p\rangle=0\) in a tangent direction \(U\) gives



```{=latex}
\begin{equation}
D_UV=\nabla_UV-\langle U,V\rangle p.
\label{courseIII:almost-complex-structures-and-integrability:eq:3.2}
\end{equation}
```



This connection preserves the induced metric and has zero torsion, directly by projection of the ambient derivative. It is the round Levi-Civita connection. Differentiating \(JV=p\times V\), using \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.2}, and projecting tangentially yields



```{=latex}
\begin{equation}
A(U,V):=(\nabla_UJ)V
=U\times V-\langle U\times V,p\rangle p.
\label{courseIII:almost-complex-structures-and-integrability:eq:3.3}
\end{equation}
```



The normal contribution to \(p\times D_UV\) is zero because \(p\times p=0\). Hence \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.3} includes the entire derivative. It is skew in \(U,V\). Differentiating \(J^2=-1\) gives \(A(U,JV)=-JA(U,V)\); using skewness gives the other identity



```{=latex}
\begin{equation}
A(JU,V)=A(U,JV)=-JA(U,V).
\label{courseIII:almost-complex-structures-and-integrability:eq:3.4}
\end{equation}
```



For a torsion-free connection, substitute \([X,Y]=\nabla_XY-\nabla_YX\) into \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5}. Terms containing derivatives of \(X,Y\) cancel, leaving



```{=latex}
\begin{equation}
N_J(U,V)=A(JU,V)-A(JV,U)+JA(V,U)-JA(U,V).
\label{courseIII:almost-complex-structures-and-integrability:eq:3.5}
\end{equation}
```



Skewness and \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.4} turn each of the four terms into \(-JA(U,V)\). We have therefore proved



```{=latex}
\begin{equation}
N_J(U,V)=-4JA(U,V)=-4p\times(U\times V).
\label{courseIII:almost-complex-structures-and-integrability:eq:3.6}
\end{equation}
```



No normal term was dropped in the last equality: it is annihilated exactly by \(p\times p=0\). Alternation of \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.15} identifies the coefficient of that normal term as
\(\langle U\times V,p\rangle=\langle JU,V\rangle\). The norm of the orthogonal projection in \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.3} is therefore



```{=latex}
\begin{equation}
|N_J(U,V)|^2
=16\bigl(|U|^2|V|^2-\langle U,V\rangle^2
-\langle JU,V\rangle^2\bigr).
\label{courseIII:almost-complex-structures-and-integrability:eq:3.7}
\end{equation}
```



At any \(p\), choose a unit \(U\in T_pS^6\), and a unit \(V\) perpendicular to \(U,JU\) in that six-dimensional tangent space. Then \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.7} gives \(|N_J(U,V)|=4\). Thus \(N_J\) is nonzero at every point, and \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.9} proves that the particular field \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1} is not integrable.

The associated real two-form is \(\omega(U,V)=\langle JU,V\rangle\). The exterior derivative of a two-form for a torsion-free connection is the cyclic sum of its covariant derivative. Using \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.3} and pairing with a tangent \(W\), the normal term disappears by \(\langle p,W\rangle=0\), and all three cyclic terms agree by alternation. Hence



```{=latex}
\begin{equation}
d\omega(U,V,W)=3\langle U\times V,W\rangle.
\label{courseIII:almost-complex-structures-and-integrability:eq:3.8}
\end{equation}
```



For our labels, at \(p=e_7\),



```{=latex}
\begin{equation}
Je_1=-e_6,\quad Je_2=e_5,\quad Je_3=e_4,
\quad N_J(e_1,e_2)=-4e_4,
\quad d\omega(e_1,e_2,e_3)=3.
\label{courseIII:almost-complex-structures-and-integrability:eq:3.9}
\end{equation}
```



Every equality follows from \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.17}, so \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.9} fixes both the tensor convention and the orientation-sensitive multiplication signs.

There is also an orientation sign to retain. At \(e_7\), the complex-oriented real basis \((e_1,Je_1,e_2,Je_2,e_3,Je_3)\) is \((e_1,-e_6,e_2,e_5,e_3,e_4)\). Its permutation of \((e_1,\ldots,e_6)\) has six inversions and one additional minus sign, hence determinant \(-1\). The latter basis is positively oriented for the outward orientation of \(S^6\subset\mathbb R^7\), because \((e_7,e_1,\ldots,e_6)\) has positive determinant. Thus this labelled octonion field induces the negative of the outward orientation. The sign is constant on the connected sphere. It will appear explicitly in its top Chern number below.

\subsection{The associator, the exact kernel, and the complex obstruction map}
\label{courseIII:almost-complex-structures-and-integrability:associator-and-kernel}\label{courseIII:almost-complex-structures-and-integrability:section-4}

The **associator** records the precise defect of associativity:



```{=latex}
\begin{equation}
[x,y,z]_{\mathbb O}=(xy)z-x(yz).
\label{courseIII:almost-complex-structures-and-integrability:eq:4.1}
\end{equation}
```



For \(p,U,V\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1}, set \(\alpha=\langle JU,V\rangle\). Expand both original products in \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.1}, using only \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.12}:



```{=latex}
\begin{equation}
\begin{aligned}
(pU)V&=-\alpha+(JU)\times V,\\
p(UV)&=-\langle U,V\rangle p-\alpha+p\times(U\times V).
\end{aligned}
\label{courseIII:almost-complex-structures-and-integrability:eq:4.2}
\end{equation}
```



Both scalar terms \(-\alpha\) are displayed and cancel. Alternation and \(J^2=-1\) give
\(\langle(JU)\times V,p\rangle=\langle J(JU),V\rangle=-\langle U,V\rangle\).
Consequently the remaining first two terms are exactly
\((JU)\times V+\langle U,V\rangle p=A(JU,V)\). Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.4} now gives



```{=latex}
\begin{equation}
[p,U,V]_{\mathbb O}=-2JA(U,V),
\qquad \boxed{N_J(U,V)=2[p,U,V]_{\mathbb O}}.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.3}
\end{equation}
```



For the Hill–Taylor tensor convention the coefficient is \(-2\). The algebra isomorphism \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.6} transports \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.3} to Baez's product, because applying a homomorphism to the two terms of \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.1} gives their corresponding two terms in the target algebra. This is the exact relation between the algebraic defect and the geometric tensor.

We next describe the object cut out by the obstruction, rather than only asserting that it is nonzero. For a fixed nonzero tangent \(U\), define the real linear map



```{=latex}
\begin{equation}
\mathcal N_U:T_pS^6\longrightarrow T_pS^6,
\qquad \mathcal N_U(V)=N_J(U,V),
\qquad W_U=\{U,JU\}^{\perp}\subset T_pS^6.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.4}
\end{equation}
```



Since \(U\) and \(JU\) are perpendicular and have the same norm, the full orthogonal decomposition is



```{=latex}
\begin{equation}
V=\frac{\langle U,V\rangle}{|U|^2}U
+\frac{\langle JU,V\rangle}{|U|^2}JU+V_\perp,
\qquad V_\perp\in W_U.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.5}
\end{equation}
```



Substitution in \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.7} gives



```{=latex}
\begin{equation}
|\mathcal N_U(V)|^2=16|U|^2|V_\perp|^2,
\qquad \ker\mathcal N_U=\operatorname{span}_{\mathbb R}\{U,JU\}.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.6}
\end{equation}
```



Thus a real two-plane generated by independent \(U,V\) has zero octonionic associator with \(p\) exactly when it is the complex line generated by \(U\). The two conditions are equivalent by \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.3}, not merely formally similar.

\label{courseIII:almost-complex-structures-and-integrability:octonion-circle-figure-style-min-width:900px-max-width:none-width:900px}
Illustration description: A specified circle of unit tangent vectors at the original basis point e7. The curves plot the exact norm formulas for the Nijenhuis tensor and the octonion associator; they represent this stated slice, not a picture of the whole sphere. Their zero set is the complex line in \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.6}. Proof: \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.6}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:3.7}, \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.3}, and \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.6}. Human source for the original octonion algebra: Baez, Section 2.2; the full calculations are given here.

Let \(A_U(V)=A(U,V)\). The identity \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.14}, with skewness, gives
\(U\times JU=U\times(p\times U)=|U|^2p\).
If \(V\in W_U\), then \(\langle U\times V,p\rangle=\langle JU,V\rangle=0\), and
\(\langle U\times V,JU\rangle=-\langle U\times JU,V\rangle=0\).
Therefore \(A_U(V)=U\times V\) lies in \(W_U\). Applying \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.14} again gives



```{=latex}
\begin{equation}
A_U^2|_{W_U}=-|U|^2I,
\qquad A_UJ=-JA_U,
\qquad \mathcal N_U^2|_{W_U}=-16|U|^2I.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.7}
\end{equation}
```



The middle identity is \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.4}, and the last follows by multiplying \(\mathcal N_U=-4JA_U\) twice. Hence the image of \(\mathcal N_U\) is exactly \(W_U\), its rank is four, and its inverse on \(W_U\) is



```{=latex}
\begin{equation}
(\mathcal N_U|_{W_U})^{-1}
=-\frac{1}{16|U|^2}\mathcal N_U|_{W_U}.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.8}
\end{equation}
```



Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.8} constructs the connecting map from every vector in the image back to an argument of the tensor. It also shows that the four nonzero real singular values are \(4|U|\).

The complex form of the obstruction is even more precise. Extend \(N_J\) complex-bilinearly. Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.8} defines a complex bundle map



```{=latex}
\begin{equation}
\mathscr N:\Lambda^2_{\mathbb C}T^{0,1}_JS^6
\longrightarrow T^{1,0}_JS^6.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.9}
\end{equation}
```



We prove that it is an isomorphism at every point. Choose unit vectors \(u_1,u_2\) with \(u_2\perp u_1,Ju_1\), and set \(u_3=A(u_1,u_2)=u_1\times u_2\). Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.13}, \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.3}, and \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.7} show that \(u_3\) is unit and perpendicular to \(u_1,Ju_1\). It is also perpendicular to \(u_2,Ju_2\): perpendicularity to \(u_2\) is a cross-product identity, and
\(\langle u_1\times u_2,Ju_2\rangle=\langle u_1,u_2\times Ju_2\rangle=\langle u_1,p\rangle=0\).
Metric compatibility with \(J\) then shows that
\(u_1,Ju_1,u_2,Ju_2,u_3,Ju_3\) is an orthonormal real basis.

The repeated-product identity gives



```{=latex}
\begin{equation}
A(u_1,u_2)=u_3,\qquad
A(u_2,u_3)=u_1,\qquad
A(u_3,u_1)=u_2.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.10}
\end{equation}
```



For example \(u_2\times(u_1\times u_2)=u_1\) follows from \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.14} after reversing the inner product, and the result is tangent, so its normal projection is zero. Define complex bases



```{=latex}
\begin{equation}
Z_a=\tfrac12(u_a-iJu_a),\qquad
\bar Z_a=\tfrac12(u_a+iJu_a),\quad a=1,2,3.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.11}
\end{equation}
```



Using \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.7}, expansion of these four terms gives
\(N_J(\bar Z_a,\bar Z_b)=\frac12\{N_J(u_a,u_b)-iJN_J(u_a,u_b)\}\).
Together with \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.6} and \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.10}, this yields



```{=latex}
\begin{equation}
\mathscr N(\bar Z_2\wedge\bar Z_3)=-4iZ_1,
\quad \mathscr N(\bar Z_3\wedge\bar Z_1)=-4iZ_2,
\quad \mathscr N(\bar Z_1\wedge\bar Z_2)=-4iZ_3.
\label{courseIII:almost-complex-structures-and-integrability:eq:4.12}
\end{equation}
```



In the displayed ordered bases its determinant is \((-4i)^3=64i\), and its inverse sends \(Z_c\) to \((i/4)\bar Z_a\wedge\bar Z_b\) for the corresponding cyclic pair. This proves the isomorphism claim. By \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.8}, the projected bracket map is exactly \(-\mathscr N/4\). By \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.10}, the scalar failure of \(\bar\partial_J^2=0\) is its dual evaluation. Thus the algebra, tangent tensor, projected bracket and scalar differential operator are linked by proved maps.

\subsection{What changes under a diffeomorphism or a complex atlas}
\label{courseIII:almost-complex-structures-and-integrability:transport-of-structures}\label{courseIII:almost-complex-structures-and-integrability:section-5}

Let \(\phi:M\to M'\) be a smooth diffeomorphism, and let \(J'\) be an almost complex structure on \(M'\). Its pullback is



```{=latex}
\begin{equation}
J^\phi_p=(D\phi_p)^{-1}J'_{\phi(p)}D\phi_p.
\label{courseIII:almost-complex-structures-and-integrability:eq:5.1}
\end{equation}
```



It is smooth and squares to \(-1\). For vector fields the differential carries brackets to brackets:
\(\phi_*[X,Y]=[\phi_*X,\phi_*Y]\).
To verify this identity, apply both sides to a smooth function \(f\) on \(M'\): each equals \(X(Y(f\circ\phi))-Y(X(f\circ\phi))\), transported by \(\phi^{-1}\). Substituting this identity in all four terms of \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5} gives



```{=latex}
\begin{equation}
D\phi_p\,N_{J^\phi}(U,V)
=N_{J'}(D\phi_pU,D\phi_pV).
\label{courseIII:almost-complex-structures-and-integrability:eq:5.2}
\end{equation}
```



If \(J'\) comes from complex charts \(z_\alpha\), then \(z_\alpha\circ\phi\) are complex charts inducing \eqref{courseIII:almost-complex-structures-and-integrability:eq:5.1}. Conversely an atlas for \(J^\phi\) transports through \(\phi^{-1}\). Thus integrability is preserved exactly under \eqref{courseIII:almost-complex-structures-and-integrability:eq:5.1}.

Apply \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.2} directly to the holomorphic quotient and gluing charts constructed in lessons 1–5. Their holomorphic transition maps give a tensor \(J_X\) on the actual manifold \(X\), and \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.8} gives \(N_{J_X}=0\). This statement uses the charts already proved to exist. It is independent of the separate smooth-recognition argument in lesson 7.

The local constructions also show why the octonionic calculation cannot obstruct all conceivable complex structures on the same underlying smooth manifold. Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.7} proves a statement about the specific field \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1}. Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:5.2} proves that no diffeomorphism can carry that field to a field arising from holomorphic charts, because an invertible differential cannot carry a nonzero tensor to zero. The exact obstruction distinguishes these fields while preserving the possibility of other fields on the same tangent bundle.

There is a second constraint supplied by compactness. On any compact oriented \(2n\)-manifold, a closed two-form \(\omega\) satisfying \(\omega(v,Jv)>0\) for an almost complex structure has \(\int_M\omega^n>0\) in the associated orientation. In a complex basis, a positive compatible form has positive determinant; more generally taming gives the same orientation through the path to its positive \((1,1)\) part, since the value on \((v,Jv)\) remains positive along that path. If \(H^2(M;\mathbb R)=0\), then \(\omega=d\alpha\), and closedness gives



```{=latex}
\begin{equation}
\omega^n=d(\alpha\wedge\omega^{n-1}),\qquad
\int_M\omega^n=0
\label{courseIII:almost-complex-structures-and-integrability:eq:5.3}
\end{equation}
```



by Stokes' theorem. For the application to a Hermitian metric we only need the compatible case: at a unitary real basis \(v_1,Jv_1,\ldots,v_n,Jv_n\), one has \(\omega^n(v_1,Jv_1,\ldots,v_n,Jv_n)=n!\). In particular a complex structure on a compact six-manifold with the integral cohomology calculated in lesson 7 cannot have a Kähler metric. This is a direct map from the exactness of a two-form to a contradiction with its volume integral; it does not identify the round form \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.8} with another metric's form.

\subsection{The full coordinate equation and its change of variables}
\label{courseIII:almost-complex-structures-and-integrability:coordinate-equation}\label{courseIII:almost-complex-structures-and-integrability:section-6}

We now prove the smooth coordinate-existence theorem. Fix a point \(p\) of a smooth \(2n\)-manifold with a smooth almost complex structure \(J\). Begin with real coordinates \(y\), with \(y(p)=y_p\). Choose a real basis \(v_1,J_pv_1,\ldots,v_n,J_pv_n\) of the tangent space. Such a basis is obtained by successively choosing a vector outside the previously chosen \(J_p\)-invariant span; the relation \(J_p^2=-1\) ensures that each step adds two independent vectors. Let \(C\) be the invertible real matrix carrying this basis to the standard ordered real basis of \(\mathbb C^n\), and put



```{=latex}
\begin{equation}
z=C(y-y_p),\qquad J_z=CJ_yC^{-1}.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.1}
\end{equation}
```



This is an exact coordinate comparison; it retains the original field \(J_y\) by its displayed inverse. At \(z=0\), \(J_z=I\). The projection of \(T^{0,1}_J\) onto the span of the coordinate fields \(\partial_{\bar z_j}\) is therefore invertible near zero, by continuity of its determinant. Hence that eigenbundle has a unique frame



```{=latex}
\begin{equation}
L_j=\partial_{\bar z_j}-\sum_{k=1}^n A_{jk}(z)\partial_{z_k},
\qquad A(0)=0.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.2}
\end{equation}
```



The functions \(A_{jk}\) are smooth, since they are obtained by inverting that finite matrix of smooth coefficients. A row vector \(F=(F_1,\ldots,F_n)\) satisfies \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.3} precisely when all \(L_jF_\ell\) vanish, or



```{=latex}
\begin{equation}
\partial_{\bar z}F=A\partial_zF.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.3}
\end{equation}
```



Here \(\partial_{\bar z}F\) and \(\partial_zF\) are matrices with derivative index in the row and function index in the column. This order matters in all subsequent products.

Compute the bracket directly. It has no \(\partial_{\bar z}\) component, and its coefficient row in the \(\partial_z\) directions is



```{=latex}
\begin{equation}
-\partial_{\bar z_j}A_k+\partial_{\bar z_k}A_j
+A_j\partial_z A_k-A_k\partial_z A_j.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.4}
\end{equation}
```



Because no nonzero combination of the \(L_j\) has zero \(\partial_{\bar z}\) component, involutivity is equivalent here to the literal commutation relations \([L_j,L_k]=0\). By \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.9} it is equivalent to



```{=latex}
\begin{equation}
\partial_{\bar z_k}A_j+A_j\partial_z A_k
=\partial_{\bar z_j}A_k+A_k\partial_z A_j.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.5}
\end{equation}
```



Let \(H\) be a real local diffeomorphism close to the identity, write \(\zeta=H(z)\), and seek \(F=G\circ H\). Suppose \(\partial_{\bar\zeta}G=B\partial_\zeta G\). The chain rule, in the row convention of \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.3}, gives



```{=latex}
\begin{equation}
\partial_{\bar z}H+(\partial_{\bar z}\bar H)(B\circ H)
=A\{\partial_z H+(\partial_z\bar H)(B\circ H)\}.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.6}
\end{equation}
```



Thus the exact transformed coefficient matrix is



```{=latex}
\begin{equation}
E:=B\circ H
=-(\partial_{\bar z}\bar H-A\partial_z\bar H)^{-1}
(\partial_{\bar z}H-A\partial_zH).
\label{courseIII:almost-complex-structures-and-integrability:eq:6.7}
\end{equation}
```



The inverse exists near \((H,A)=(\operatorname{id},0)\), where its matrix is \(I\). In particular \(H=\operatorname{id}\) gives \(B=A\). The transformed field is \(DH\,J\,(DH)^{-1}\), as follows by applying the chain rule to vectors annihilating the coordinate functions. Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:5.2} therefore proves that \(B\) satisfies \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.5} with \(\zeta\) in place of \(z\) whenever \(A\) satisfies it. We will choose \(H\) so that it also satisfies



```{=latex}
\begin{equation}
\sum_{j=1}^n\partial_{\zeta_j}B_j=0.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.8}
\end{equation}
```



This extra equation makes the coefficient field analytic. Sections 7–9 prove that assertion and the existence of the required \(H\), instead of assuming them as additional hypotheses about the original \(J\).

**Source sign correction.** Keep the definitions \(E\) and \(\Psi=\sum_j(\partial_{\zeta_j}B_j)\circ H\) exactly as in Hill–Taylor equations 3.9 and3.12. At \(A=0\), insert \(H(z)=z+\epsilon h(z)\) into \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.7}. Its two matrix factors give



```{=latex}
\begin{equation}
E=-\epsilon\partial_{\bar z}h+O(\epsilon^2),
\qquad
D_H\Psi(\operatorname{id},0)h
=-\sum_j\partial_{z_j}\partial_{\bar z_j}h
=-\tfrac14\Delta h.
\label{courseIII:almost-complex-structures-and-integrability:eq:6.9}
\end{equation}
```



The first variation of \((DH)^{-1}\) multiplies \(DE=0\) at the base point, so it contributes nothing. The sign in their displayed equation 3.14 is positive; with their preceding definitions it must be negative. If \(\mathcal G\) solves \(\Delta v=f\) with zero boundary values, the right inverse under their point condition \(h(0)=0\) is correspondingly \(-4(\mathcal Gf-\mathcal Gf(0))\), rather than their positive expression. Invertibility is preserved. Below we give a periodic construction whose inverse is an explicit Fourier multiplier and has the sign in \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.9}.

\subsection{Constructing the divergence-free coordinates}
\label{courseIII:almost-complex-structures-and-integrability:periodic-gauge}\label{courseIII:almost-complex-structures-and-integrability:section-7}

We give the analytic estimates needed for this step, including the function spaces and the treatment of constants. Let \(m=2n\), and let \(\mathbb T^m=\mathbb R^m/(2\pi\mathbb Z)^m\). For an integer \(s\), its Sobolev norm is



```{=latex}
\begin{equation}
\|u\|_{H^s}^2
=(2\pi)^m\sum_{k\in\mathbb Z^m}(1+|k|^2)^s|\widehat u(k)|^2,
\qquad
\widehat u(k)=(2\pi)^{-m}\int_{[-\pi,\pi]^m}e^{-ik\cdot x}u(x)\,dx.
\label{courseIII:almost-complex-structures-and-integrability:eq:7.1}
\end{equation}
```



For vector or matrix functions, sum the squared norms of the entries. We treat complex entries as pairs of real entries. Fix an integer \(s>m/2+3\).

Here are the estimates we use. If \(r>m/2\), Cauchy–Schwarz gives



```{=latex}
\begin{equation}
\sum_k|\widehat u(k)|
\leq\left(\sum_k(1+|k|^2)^{-r}\right)^{1/2}
\left(\sum_k(1+|k|^2)^r|\widehat u(k)|^2\right)^{1/2}.
\label{courseIII:almost-complex-structures-and-integrability:eq:7.2}
\end{equation}
```



The first sum is finite by comparison on successive lattice shells with \(\sum_{q\geq1}q^{m-1-2r}\). This proves \(H^r\subset C^0\); applying it to derivatives proves \(H^{r+j}\subset C^j\). The convolution formula for Fourier coefficients, the inequality




```{=latex}
\[
(1+|k+\ell|^2)^{r/2}\leq C_r\{(1+|k|^2)^{r/2}+(1+|\ell|^2)^{r/2}\}
\]
```



,
and the elementary convolution bound \(\|a*b\|_{\ell^2}\leq\|a\|_{\ell^1}\|b\|_{\ell^2}\) give



```{=latex}
\begin{equation}
\|uv\|_{H^r}\leq C_r\|u\|_{H^r}\|v\|_{H^r}.
\label{courseIII:almost-complex-structures-and-integrability:eq:7.3}
\end{equation}
```



The convolution bound follows from the triangle inequality in \(\ell^2\) applied to the sum of translated copies of \(b\), weighted by \(a\). The same proof with
\(|k|^a|\ell|^b\leq C_r\{(1+|k|^2)^{r/2}+(1+|\ell|^2)^{r/2}\}\)
shows that products of derivatives of total order at most \(r\) are in \(L^2\), with the same type of bound. On \(\mathbb R^m\) the identical argument uses integrals and Young's convolution inequality, whose proof is the same translated-norm argument.

These estimates also hold on concentric balls with radii in a fixed compact interval of positive radii, with uniform constants. One explicit extension construction suffices to see this. Flatten a boundary patch, and for its half-space normal coordinate \(t\geq0\) extend to \(t<0\) by
\(Eu(x',-t)=\sum_{\ell=1}^{r+1}c_\ell u(x',\ell t)\),
where \(\sum_\ell c_\ell(-\ell)^j=1\) for \(0\leq j\leq r\). The Vandermonde matrix is invertible. Derivatives through order \(r\) match at the boundary, and changes of variable bound the Sobolev norm of each reflected term. A finite set of boundary charts and a smooth partition of unity give an extension on a ball. Dilations between the stated range of radii keep all constants bounded. Applying the Euclidean Fourier estimates to these extensions proves the assertions for balls.

Choose a smooth real function \(\chi\) supported in \(\{|x|<2\}\subset(-\pi,\pi)^m\), equal to one on \(\{|x|\leq1\}\). For sufficiently small positive \(\epsilon\), define the periodic matrix



```{=latex}
\begin{equation}
\widetilde A_\epsilon(x)=\chi(x)A(\epsilon x).
\label{courseIII:almost-complex-structures-and-integrability:eq:7.4}
\end{equation}
```



The original coefficient matrix is defined on the support because \(\epsilon\) is small. Every derivative through order \(s+1\) tends uniformly to zero as \(\epsilon\to0\): the zeroth order uses \(A(0)=0\), and a positive derivative of \(A(\epsilon x)\) contains the factor \(\epsilon^{|\alpha|}\). Leibniz's rule retains the derivatives of \(\chi\), multiplied by these same vanishing factors or by \(A(\epsilon x)\). Thus
\(\|\widetilde A_\epsilon\|_{H^{s+1}}\to0\).
On the unit ball it is the exact pullback under \(z=\epsilon x\); outside that ball no involutivity assertion is needed.

Let \(h\in H^{s+2}(\mathbb T^m;\mathbb C^n)\) have zero mean and be small, and let the lift of \(H\) be



```{=latex}
\begin{equation}
H(x)=x+h(x).
\label{courseIII:almost-complex-structures-and-integrability:eq:7.5}
\end{equation}
```



The real Jacobian is \(DH=I+Dh\). Arrange \(\|Dh\|_\infty<1/2\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.2}. For any \(y\in\mathbb R^m\), the map \(x\mapsto y-h(x)\) is a contraction of the complete space \(\mathbb R^m\); its successive iterates have differences bounded by a geometric series and hence converge to its unique fixed point. Thus \(H\) is bijective on \(\mathbb R^m\). Its periodic lift property descends to a diffeomorphism of \(\mathbb T^m\). Its Jacobian determinant \(j_H\) is positive: all \(I+tDh\), \(0\leq t\leq1\), are invertible by the Neumann series, so their determinants cannot change the positive sign at \(t=0\).

Use \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.7}, with \(\widetilde A_\epsilon\) in place of \(A\), to define the periodic function \(E\). Put \(B=E\circ H^{-1}\). The pullback of the left side of \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.8}, multiplied by its real Jacobian, is



```{=latex}
\begin{equation}
\mathcal F(h,\widetilde A_epsilon)
=j_H\sum_j\bigl(\partial_{\zeta_j}B_j\bigr)\circ H.
\label{courseIII:almost-complex-structures-and-integrability:eq:7.6}
\end{equation}
```



Formula \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.6} is evaluated on the fixed \(x\)-torus as follows: differentiate \(E_j(x)\), and contract its real differential with \((DH)^{-1}\) applied to the constant complex vector \(\partial_{\zeta_j}\). Hence it involves only \(\widetilde A_epsilon,D\widetilde A_epsilon,Dh,D^2h\), matrix inversion, and multiplication. There is no loss from differentiating a parameter-dependent composition. Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.2}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:7.3} and the locally convergent matrix Neumann series prove that



```{=latex}
\begin{equation}
\mathcal F:H^{s+2}_0\times H^{s+1}
\longrightarrow H^s_0
\label{courseIII:almost-complex-structures-and-integrability:eq:7.7}
\end{equation}
```



is continuously differentiable near \((0,0)\); the subscript means zero mean. Its output has zero mean because change of variables in the integral of \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.6} gives the integral of a periodic derivative in \(\zeta\), which is zero. The regularities already proved make this ordinary change of variables legitimate. All inverses in the formula exist in a neighborhood of the base point by \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.3}.

At the base point, \(E=0\), so the derivative of the Jacobian factor contributes zero. Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.9} gives the exact derivative



```{=latex}
\begin{equation}
L:=D_h\mathcal F(0,0)=-\tfrac14\Delta:
H^{s+2}_0\longrightarrow H^s_0.
\label{courseIII:almost-complex-structures-and-integrability:eq:7.8}
\end{equation}
```



It is a bounded bijection. Its inverse is the Fourier multiplier



```{=latex}
\begin{equation}
\widehat{L^{-1}f}(0)=0,
\qquad
\widehat{L^{-1}f}(k)=\frac{4}{|k|^2}\widehat f(k)
\quad(k\ne0).
\label{courseIII:almost-complex-structures-and-integrability:eq:7.9}
\end{equation}
```



The norm bound follows from 



```{=latex}
\[
(1+|k|^2)^2/|k|^4\leq4
\]
```



 for nonzero integer \(k\). Thus the constant Fourier mode is treated exactly, and the sign agrees with \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.9}.

For clarity, the needed implicit-function argument is the following contraction. Define
\(T_A(h)=h-L^{-1}\mathcal F(h,A)\).
Its derivative in \(h\) is zero at \((0,0)\), so continuity makes its Lipschitz constant at most \(1/2\) on a sufficiently small closed ball in \(H^{s+2}_0\), for all sufficiently small \(A\). Since \(T_0(0)=0\), shrinking the allowed norm of \(A\) makes \(\|T_A(0)\|\) at most half the radius of that ball. The map then preserves the ball. Successive iterates converge by a geometric-series bound in the complete Sobolev space to a unique fixed point. At that point \(\mathcal F(h,A)=0\). Apply this to \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.4}.

We have constructed \(H\) and \(B\) satisfying \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.7}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:6.8}, with \(B\) as small in \(C^0\) as desired. The function \(B\) belongs locally to \(H^{s+1}\). To verify the last assertion, the weak chain rule for \(E\circ H^{-1}\) is obtained first for smooth approximations and then by passage in Sobolev norm: the first derivative uses \(DE\,(DH)^{-1}\), change of variables bounds its \(L^2\) norm, and each successive derivative is a finite product of derivatives of \(E\) and \(H\), with factors of \((DH)^{-1}\). The product estimates following \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.3} bound these terms through order \(s+1\). Smooth periodic approximations preserve the uniform lower Jacobian bound, so the limit has those weak derivatives. This proves the claimed regularity without assuming that the newly constructed coordinates are already smooth.

On the image of the unit ball, involutivity is preserved by the diffeomorphism, as proved after \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.7}. Thus there \(B\) satisfies both \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.5} and \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.8}. The next section proves the stronger regularity forced by those equations.

\subsection{Why the gauged coefficient matrix is analytic}
\label{courseIII:almost-complex-structures-and-integrability:analytic-estimates}\label{courseIII:almost-complex-structures-and-integrability:section-8}

This section supplies the elliptic step used in the coordinate construction. All estimates are local in the real dimension \(m=2n\). For a column field \(b=(b_1,\ldots,b_n)\), define the constant-coefficient first-order operator



```{=latex}
\begin{equation}
\mathcal Lb=
\left((\partial_{\bar\zeta_j}b_k-\partial_{\bar\zeta_k}b_j)_{j<k},
\ \sum_j\partial_{\zeta_j}b_j\right).
\label{courseIII:almost-complex-structures-and-integrability:eq:8.1}
\end{equation}
```



For a real covector \(\xi=(\xi_x,\xi_y)\), the symbol of \(\partial_{\bar\zeta_j}\) is \(a_j=(i\xi_{x_j}-\xi_{y_j})/2\), and that of \(\partial_{\zeta_j}\) is \(-\bar a_j\). Expanding the squared norms of the wedge and inner product gives



```{=latex}
\begin{equation}
\sum_{j<k}|a_jb_k-a_kb_j|^2
+\left|\sum_j\bar a_jb_j\right|^2
=|a|^2|b|^2=\tfrac14|\xi|^2|b|^2.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.2}
\end{equation}
```



Indeed the diagonal terms on the left collect \(|a_j|^2|b_k|^2\) for every ordered pair, while the mixed terms cancel. Parseval's identity therefore proves, for compactly supported smooth fields,



```{=latex}
\begin{equation}
\|Db\|_{L^2}=2\|\mathcal Lb\|_{L^2}.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.3}
\end{equation}
```



Apply \(\mathcal L\) to every column of \(B\). Its full system is



```{=latex}
\begin{equation}
\mathcal LB=\mathcal Q(B,DB),
\qquad
\mathcal Q(B,DV)_{jk}=B_j\partial_\zeta V_k-B_k\partial_\zeta V_j
\quad(j<k),
\label{courseIII:almost-complex-structures-and-integrability:eq:8.4}
\end{equation}
```



with zero divergence component. This is exactly \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.5}, with its terms rearranged, together with \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.8}. The finite sums in the row products give, for the Euclidean norms of all entries,
\(|\mathcal Q(B,DV)|\leq2n|B||DV|\).
Take the smallness in \cref{courseIII:almost-complex-structures-and-integrability:section-7} so that



```{=latex}
\begin{equation}
\sup|B|<\frac1{8n}.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.5}
\end{equation}
```



The factor \(2\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.3} then permits absorption of the highest derivative in
\(\mathcal P_BV=\mathcal LV-\mathcal Q(B,DV)\).

\subsubsection{Smoothness, including weak derivatives}
\label{courseIII:almost-complex-structures-and-integrability:section-8.1}

First consider a compactly supported \(V\in L^2\) for which \(\mathcal P_BV\in L^2\) distributionally, with \(B\) continuously differentiable and satisfying \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.5}. We prove \(V\in H^1\). Convolve with a smooth compactly supported approximate identity \(\rho_\delta\). The commutator of a term \(B\partial_a\) with convolution is the sum of an integral with kernel
\((B(x)-B(x-y))\partial_a\rho_\delta(y)\)
and an integral with a factor \(\partial_aB(x-y)\rho_\delta(y)\), with signs determined by integration by parts. Their absolute values suffice for this estimate. The mean-value inequality bounds the first difference by \(\|DB\|_\infty|y|\). Since



```{=latex}
\begin{equation}
\int|y||D\rho_\delta(y)|\,dy
=\int|y||D\rho(y)|\,dy,
\label{courseIII:almost-complex-structures-and-integrability:eq:8.6}
\end{equation}
```



Young's inequality bounds both commutators uniformly on \(L^2\). Thus \(\mathcal P_B(\rho_\delta*V)\) is bounded in \(L^2\). Applying \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.3} and absorbing the term \(\mathcal Q(B,D(\rho_\delta*V))\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.5} bounds the derivatives uniformly in \(L^2\). Weak compactness gives a weakly convergent subsequence of these derivatives; testing against compactly supported smooth functions identifies its limit as the distributional derivative of \(V\). This proves \(H^1\) regularity. For a local assertion, first multiply by a smooth cutoff; the extra term is a bounded coefficient times \(V\), hence remains in \(L^2\). The convolution is performed inside a slightly larger region, so no boundary extension of the equation is required.

Suppose now \(B\in H^r_{\mathrm{loc}}\), with integer \(r>m/2+2\), and \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.4} holds. This applies to the matrix obtained in Section 7. Differentiate the equation distributionally by a multi-index \(\alpha\) of length \(r\). The terms with no derivative on the first factor are moved to the left. The result is



```{=latex}
\begin{equation}
\mathcal P_B(D^\alpha B)
=\sum_{0<\beta\leq\alpha}\binom{\alpha}{\beta}
\mathcal Q(D^\beta B,D(D^{\alpha-\beta}B)).
\label{courseIII:almost-complex-structures-and-integrability:eq:8.7}
\end{equation}
```



Every term on the right is in \(L^2\). To see this, put one derivative on each copy of \(B\); the remaining derivative orders sum to \(r-1\). The derivative-product estimate following \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.3}, applied to \(DB\in H^{r-1}\), gives the bound because \(r-1>m/2\). The differentiated identity follows by approximation of \(B\) in \(H^r\), using those same bounds to pass the products to distributions. Its left side has \(D^\alpha B\in L^2\), and \(B\) is \(C^1\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.2}. The preceding convolution argument therefore proves \(D^\alpha B\in H^1_{\mathrm{loc}}\). Hence \(B\in H^{r+1}_{\mathrm{loc}}\). Iteration proves \(B\in C^\infty\).

\subsubsection{An interior estimate with only one inverse distance}
\label{courseIII:almost-complex-structures-and-integrability:section-8.2}

We need the dependence on the shrinking radius, not merely smoothness. Fix a closed ball \(\overline{B_R}\) inside the region just considered, and an integer \(q>m/2\). For \(R/2\leq r<r+\delta<R\), choose a smooth cutoff equal to one on \(B_r\), supported in \(B_{r+\delta}\), with \(|D\chi|\leq c/\delta\). Applying \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.3} and absorption to \(\chi D^\alpha V\), separately for every \(|\alpha|\leq q\), gives



```{=latex}
\begin{equation}
\|DV\|_{H^q(B_r)}
\leq C\left\{
\|\mathcal P_BV\|_{H^q(B_{r+\delta})}
+(\delta^{-1}+K)\|V\|_{H^q(B_{r+\delta})}
\right\}.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.8}
\end{equation}
```



Here \(C,K\) are finite constants independent of \(r,\delta,V\). One can take \(K\) to be a fixed multiple of \(1+\max_{1\leq j\leq q}\|D^jB\|_{L^\infty(B_R)}\). To check the estimate, commute \(D^\alpha\) past \(\mathcal P_B\). Each commutator has at least one derivative on \(B\), hence at most \(|\alpha|\) derivatives on \(V\), and is bounded by this \(K\) times \(\|V\|_{H^q}\). The commutator with \(\chi\) uses only \(D\chi\), because \(\mathcal P_B\) is first order. Applying the estimate separately to \(D^\alpha V\), rather than differentiating the cutoff \(q\) times, is what leaves precisely \(\delta^{-1}\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.8}. The coefficient of the highest derivative is absorbed by \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.5} before summing these inequalities.

\subsubsection{Factorial bounds}
\label{courseIII:almost-complex-structures-and-integrability:section-8.3}

Set



```{=latex}
\begin{equation}
F_k(r)=\max_{|\alpha|=k}\|D^\alpha B\|_{H^q(B_r)}.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.9}
\end{equation}
```



Use \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.8} for \(V=D^\alpha B\), \(|\alpha|=k\), and use \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.7} with that multi-index. The ball version of \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.3} bounds every product in \(H^q\), uniformly for these radii. The identity
\(\sum_{|\beta|=j,\beta\leq\alpha}\binom\alpha\beta=\binom kj\)
is the coefficient of \(t^j\) in \(\prod_a(1+t)^{\alpha_a}\). Thus, enlarging the fixed constant \(C\),



```{=latex}
\begin{equation}
F_{k+1}(r)\leq C\left\{
(\delta^{-1}+K)F_k(r+\delta)
+\sum_{j=1}^k\binom kjF_j(r+\delta)F_{k-j+1}(r+\delta)
\right\}.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.10}
\end{equation}
```



Choose \(M\geq\max(1,4R F_1(R))\). We prove by induction, for a sufficiently large fixed \(a\geq1\), that



```{=latex}
\begin{equation}
F_k(r)\leq
\frac{M a^{k-1}k!}{(k+1)^2(R-r)^k}
\qquad(k\geq1, R/2\leq r<R).
\label{courseIII:almost-complex-structures-and-integrability:eq:8.11}
\end{equation}
```



The case \(k=1\) follows from the choice of \(M\). For the induction step put \(d=R-r\), \(\delta=d/(k+1)\), so that \(d'=R-r-\delta=dk/(k+1)\). Then
\((d/d')^{k+1}=(1+1/k)^{k+1}\leq4\).
In the product term of \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.10}, write \(\ell=k-j+1\). The factorials satisfy \(\binom kj j!\ell!=k!\ell\), and



```{=latex}
\begin{equation}
\sum_{j=1}^k\frac{k-j+1}{(j+1)^2(k-j+2)^2}
\leq \frac{8(k+1)}{(k+2)^2}.
\label{courseIII:almost-complex-structures-and-integrability:eq:8.12}
\end{equation}
```



Here is a bound with all its indices. Put \(a_1=j+1\), \(b_1=k-j+2\), so \(a_1+b_1=k+3\), and replace \((b_1-1)/b_1^2\) by \(1/b_1\). In the terms \(a_1\leq(k+3)/2\), use \(1/b_1\leq2/(k+3)\) and \(\sum_{a_1\geq2}a_1^{-2}<1\). In the other terms use \(a_1^{-2}\leq4/(k+3)^2\), \(1/b_1\leq1/2\), and at most \(k\) terms. The total is at most \(4/(k+3)\), which is at most the right side of \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.12}, since \((k+2)^2\leq2(k+1)(k+3)\).

The products in \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.10}, divided by the proposed bound for \(F_{k+1}(r)\), are therefore at most \(32CM/a\). Its linear term has ratio at most \(9C(1+KR)/a\), using \((k+2)^2/(k+1)^2\leq9/4\). Choosing, for example,



```{=latex}
\begin{equation}
a\geq128C(1+KR+M)
\label{courseIII:almost-complex-structures-and-integrability:eq:8.13}
\end{equation}
```



makes their sum at most one and completes the induction. The factor \((k+1)^{-2}\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.11} is retained because it controls the full convolution of derivatives in the nonlinear equation.

At \(r=3R/4\), the Sobolev embedding \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.2} and \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.11} give a constant \(C_0\) with
\(\sup_{B_{3R/4}}|D^\alpha B|\leq C_0(4a/R)^{|\alpha|}|\alpha|!\).
Taylor's formula along a segment with increment \(h\), expanded by the multinomial theorem, bounds its remainder of order \(k\) by
\(C_0\{(4a/R)\sum_j|h_j|\}^{k+1}\), provided the segment stays in that ball. This tends to zero for sufficiently small \(h\). Thus the Taylor series equals \(B\) near each point. We have proved real analyticity from the actual equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.4}, including the existence and convergence of the required derivatives.

\subsection{Analytic commuting flows produce the coordinates}
\label{courseIII:almost-complex-structures-and-integrability:analytic-flows}\label{courseIII:almost-complex-structures-and-integrability:section-9}

We finish the coordinate-existence proof without invoking an unproved analytic Frobenius theorem. Translate the point \(H(0)\) to the origin in the \(\zeta\)-coordinates, recording this translation in the final map. A real-analytic matrix \(B(\zeta,\bar\zeta)\) extends to a holomorphic matrix \(\mathcal B(z,w)\) in independent variables \((z,w)\in\mathbb C^n\times\mathbb C^n\). Indeed substitute \(x=(z+w)/2\), \(y=(z-w)/(2i)\) into its convergent real power series. The real diagonal \((z,w)=(\zeta,\bar\zeta)\) recovers the original matrix exactly.

Consider the holomorphic vector fields



```{=latex}
\begin{equation}
\mathcal L_j=\partial_{w_j}-\sum_k\mathcal B_{jk}(z,w)\partial_{z_k}.
\label{courseIII:almost-complex-structures-and-integrability:eq:9.1}
\end{equation}
```



Their brackets vanish. Their bracket formula is \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.4}, and is zero on the real diagonal by \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.5}. To verify that it is then identically zero holomorphically, make the invertible linear substitution between \((z,w)\) and \((x,y)\) just given. A holomorphic power series in \((x,y)\) that vanishes for real \((x,y)\) in an open set has every Taylor coefficient zero, by differentiating its restriction in those real coordinates. Apply this to each bracket coefficient.

Each \(\mathcal L_j\) has a local holomorphic flow \(\Phi_j^t\). One direct proof is Picard iteration on a smaller closed polydisc: on a larger polydisc the holomorphic coefficients and their first derivatives are bounded, say by \(M_0,M_1\). Choose \(|t|M_0\) smaller than the margin to the larger boundary and \(|t|M_1<1/2\). The map
\(u(t)\mapsto u(0)+\int_0^t\mathcal L_j(u(s))\,ds\)
preserves the closed sup-norm ball of curves and is a contraction there. Integrating along the straight complex segment and iterating gives holomorphic functions of the initial value and \(t\); uniform convergence on the smaller polydisc preserves holomorphicity by the Cauchy integral formula. The limit solves the differential equation and is unique. Negative time gives the local inverse by uniqueness.

The flows commute. To check this, the chain rule for the flow equation gives the exact inverse-pushforward formula \(\frac{d}{dt}(\Phi_j^{-t})_*\mathcal L_k=(\Phi_j^{-t})_*[\mathcal L_j,\mathcal L_k]=0\). Its value is therefore the original \(\mathcal L_k\). It follows that \(\Phi_j^t\) sends integral curves of \(\mathcal L_k\) to integral curves with the same parameter; uniqueness of their initial-value problems gives \(\Phi_j^t\Phi_k^u=\Phi_k^u\Phi_j^t\) wherever both sides are defined.

Start on the transverse complex plane \(w=0\) and define



```{=latex}
\begin{equation}
\Theta(a,t)=\Phi_1^{t_1}\circ\cdots\circ\Phi_n^{t_n}(a,0).
\label{courseIII:almost-complex-structures-and-integrability:eq:9.2}
\end{equation}
```



The \(w\)-coordinate is exactly \(t\), since \(\mathcal L_jw_k=\delta_{jk}\). The derivative in \(a\) of the \(z\)-coordinate is the identity at \((0,0)\). Thus \(D\Theta(0,0)\) is a block triangular matrix with identity diagonal blocks, and is invertible. The holomorphic inverse-function theorem here follows from the same contraction argument: after subtracting the value and multiplying by the inverse derivative, write \(\Theta(v)=v+R(v)\) with \(DR(0)=0\), and solve \(v=y-R(v)\) on a small closed ball. Its convergent iterations are holomorphic in \(y\), so the inverse is holomorphic. Let \(\mathcal G(z,w)\) be the first \(n\) components of this inverse, the initial value \(a\).

Commutativity of the flows makes \(\mathcal G\) constant on each \(\mathcal L_j\)-flow. Therefore



```{=latex}
\begin{equation}
\partial_{w_j}\mathcal G
=\mathcal B_j\partial_z\mathcal G.
\label{courseIII:almost-complex-structures-and-integrability:eq:9.3}
\end{equation}
```



Restrict to \((z,w)=(\zeta,\bar\zeta)\). The resulting real-analytic map \(G(\zeta)=\mathcal G(\zeta,\bar\zeta)\) satisfies
\(\partial_{\bar\zeta}G=B\partial_\zeta G\).
At the chosen center its differential, with output regarded as a column, is



```{=latex}
\begin{equation}
dG(v)=v+B(0)^{\mathsf T}\bar v.
\label{courseIII:almost-complex-structures-and-integrability:eq:9.4}
\end{equation}
```



This follows either from the inverse triangular matrix in \eqref{courseIII:almost-complex-structures-and-integrability:eq:9.2} or directly from \eqref{courseIII:almost-complex-structures-and-integrability:eq:9.3} and \(\partial_z\mathcal G(0)=I\). The real perturbation in \eqref{courseIII:almost-complex-structures-and-integrability:eq:9.4} has norm at most \(|B(0)|<1\), so it is invertible. Thus \(G\) is a real local diffeomorphism.

Return to the untranslated gauged coordinate by using \(G(\zeta-H(0))\), where \(G\) is constructed for the translated coefficient \(B(\zeta+H(0))\). The complete coordinate map on the original \(y\)-domain is



```{=latex}
\begin{equation}
F_y(y)=\epsilon\,
G\left(H\left(\frac{C(y-y_p)}{\epsilon}\right)-H(0)\right).
\label{courseIII:almost-complex-structures-and-integrability:eq:9.5}
\end{equation}
```



Restrict to a neighborhood where \(|C(y-y_p)|<\epsilon\) and all the flow and inverse maps above are defined. Then the cutoff in \eqref{courseIII:almost-complex-structures-and-integrability:eq:7.4} equals one. Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.6}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:6.7} prove exactly that \(dF_y\circ J_y=i,dF_y\). Its real derivative is invertible by the invertibility of \(C\), the positive scale \(\epsilon\), \(DH\), and \(DG\). Every coordinate change, translation and scale used in the construction occurs explicitly in \eqref{courseIII:almost-complex-structures-and-integrability:eq:9.5}.

The map is initially of finite Sobolev regularity, sufficient for a \(C^1\) chart. It is in fact smooth. In the \(z\)-coordinates its components satisfy the linear first-order system
\((\partial_{\bar z}-A\partial_z)f=0\), with smooth \(A\) as small as desired on a smaller ball. The symbol of \(\partial_{\bar z}\) has norm \(|\xi|/2\); Parseval gives the same first-order estimate as \eqref{courseIII:almost-complex-structures-and-integrability:eq:8.3}. The cutoff, absorption and convolution argument of \cref{courseIII:almost-complex-structures-and-integrability:section-8.1} applies to this system. After differentiating it, the commutators contain derivatives of the smooth coefficient \(A\) and at most the already known number of derivatives of \(f\). It follows successively that \(f\in H^{r+1}_{\mathrm{loc}}\) whenever \(f\in H^r_{\mathrm{loc}}\). Sobolev embedding gives smoothness.

We have proved the smooth Newlander–Nirenberg theorem in the form needed here:

**Theorem 9.1.** A smooth almost complex structure is induced by a complex coordinate atlas if and only if its tensor \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5} vanishes.

Necessity was proved in Section 1. For sufficiency, the original zero tensor gives \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.5}; Sections 7–8 construct the actual divergence-free analytic coefficient field, and the commuting flows give \eqref{courseIII:almost-complex-structures-and-integrability:eq:9.5}. On overlaps the chain rule and the Cauchy integral argument after \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.3} make the transitions holomorphic. No analytic regularity hypothesis was imposed on the original smooth field.

\label{courseIII:almost-complex-structures-and-integrability:integrability-map-figure-style-min-width:900px-max-width:none-width:900px}
Illustration description: The exact local maps in the coordinate proof. The cutoff equals one on the receiving domain, and the original scale, real coordinate matrix, and translation all reappear in the final formula \eqref{courseIII:almost-complex-structures-and-integrability:eq:9.5}. The coefficient in the translated analytic chart is B-hat(w)=B(w+H (0)). The torus is the auxiliary periodic domain used in Section 7. Proof: Sections 6–9. Human source for the factorization method: Hill–Taylor, Sections 2–4; this lesson supplies the periodic construction, corrected sign, and convergence estimates.

\subsection{The sphere restriction, with a proof of the needed Bott generation}
\label{courseIII:almost-complex-structures-and-integrability:sphere-classification}\label{courseIII:almost-complex-structures-and-integrability:section-10}

We prove that the positive-dimensional spheres admitting almost complex structures are exactly \(S^2\) and \(S^6\). The characteristic-class argument is the one discussed by Konstantis–Parton, Sections 3–6. We supply the needed generation step in complex K-theory by polynomial clutching, so its required integrality does not rest on an unproved appeal to Bott periodicity. The same finite linearization is developed in the CC0 supporting course *K-theory for operator algebras*, lesson *Bott periodicity*, \cref{courseIII:almost-complex-structures-and-integrability:section-5}; its full Toeplitz proof gives periodicity for a larger class of coefficient algebras than we need here.

\subsubsection{Bundles, clutching, and based loops}
\label{courseIII:almost-complex-structures-and-integrability:section-10.1}

All bases in Sections 10.1–10.3 are compact Hausdorff spaces. For such a space \(Y\), \(K^0(Y)\) is the group completion of the direct-sum monoid of finite-rank complex vector bundles. Thus its elements are differences \([E]-[F]\), with the relation that adding the same bundle to both terms does not change the difference. Tensor product makes this a ring.

We use two elementary bundle facts, with their proofs. Every bundle \(E\) over compact \(Y\) embeds in a trivial bundle: choose finitely many trivializations and a partition of unity \(\rho_i\) subordinate to them, and send \(v\in E_y\) to the list \((\sqrt{\rho_i(y)}v_i)_i\) of its local coordinates, with zero entries off the corresponding supports. At least one \(\rho_i(y)\) is positive, so the map is injective on each fibre. Its image is a subbundle, and the orthogonal complement gives \(E\oplus E^\perp\simeq\mathbf1^N\). The orthogonal projection onto the image is continuous, as is seen in a local frame by the formula \(T(T^*T)^{-1}T^*\).

Second, bundles pulled back by homotopic maps from a compact space are isomorphic. Embed the bundle over the product with the homotopy interval in a trivial bundle as just described, and let \(p(y,t)\) be its range projection. Uniform continuity gives a finite partition of the interval on which consecutive projections differ in norm by less than one, uniformly in \(y\). For projections \(p,q\) with \(\|p-q\|<1\), the map \(q:\operatorname{im}p\to\operatorname{im}q\) is injective, since \(\|qv\|\geq(1-\|p-q\|)\|v\|\). Reversing \(p,q\) gives equal ranks, so it is an isomorphism; its inverse is continuous in local finite matrices. Composing these finite isomorphisms proves the assertion. This proof applies equally with a compact disk included in the base.

Apply these facts to a bundle on \(S^2\times Y\). Its restrictions to the closed hemispheres are pullbacks of bundles on \(Y\), by contraction of the disks. Their restrictions at one equatorial point identify those two bundles, say with \(E_0\). Adding the pullback of a complement of \(E_0\) makes both hemisphere bundles trivial. The stabilized bundle is then obtained from a clutching map



```{=latex}
\begin{equation}
g:Y\times\mathbb T\longrightarrow GL_r(\mathbb C).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.1}
\end{equation}
```



Changing one hemisphere frame by \(g(y,1)^{-1}\) makes \(g(y,1)=I_r\). Homotopies of such based loops give isomorphic stable bundles: glue throughout the homotopy and apply the preceding interval result. Block sum of loops gives direct sum of bundles. Pointwise product gives the same stable sum, by the explicit based homotopy



```{=latex}
\begin{equation}
\begin{pmatrix}g&0\\0&I\end{pmatrix}
R_\theta
\begin{pmatrix}I&0\\0&h\end{pmatrix}R_\theta^{-1},
\quad
R_\theta=
\begin{pmatrix}\cos\theta I&-\sin\theta I\\
\sin\theta I&\cos\theta I\end{pmatrix},
\quad0\leq\theta\leq\frac\pi2.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.2}
\end{equation}
```



The endpoints are \(\operatorname{diag}(g,h)\) and \(\operatorname{diag}(gh,I)\). All loop values at \(1\) remain the identity.

\subsubsection{The finite polynomial reduction}
\label{courseIII:almost-complex-structures-and-integrability:section-10.2}

Regard \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.1} as a based loop in matrices over the Banach algebra \(D=C(Y)\). It is uniformly approximated by Laurent polynomial loops. Indeed convolution in the circle coordinate with the Fejér kernel
\((N+1)^{-1}|\sum_{j=0}^N e^{ij\theta}|^2\)
converges uniformly for continuous Banach-valued functions: the kernel has integral one, is nonnegative, and outside any fixed arc its bound is \(((N+1)\sin^2(\theta/2))^{-1}\). Uniform continuity controls the near arc and this bound controls its complement. The inverse of \(g\) has bounded norm by compactness. Therefore a sufficiently close Laurent approximation is joined to \(g\) by invertible straight interpolations, by the Neumann series. Replacing every interpolant \(H(z)\) by \(H(z)H(1)^{-1}\) makes the entire homotopy based.

Let \(g_0\) be the resulting based Laurent polynomial loop. Choose an integer \(a\geq0\) so that \(f(z)=z^ag_0(z)\) is a polynomial, say \(f(z)=\sum_{j=0}^d a_jz^j\), with \(f(1)=I_r\). The notation \(a_j\) denotes matrix coefficients, whereas \(a\) is the chosen Laurent exponent. Form the block matrix



```{=latex}
\begin{equation}
\mu(f)(z)=
\begin{pmatrix}
a_0&a_1&\cdots&a_d\\
-zI&I&\cdots&0\\
0&-zI&\ddots&\vdots\\
\vdots&\ddots&\ddots&I
\end{pmatrix}.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.3}
\end{equation}
```



This matrix is linear in \(z\). Its precise rows are: the top row is \((a_0,\ldots,a_d)\), and row \(j\), \(1\leq j\leq d\), has entries \(-zI\) in column \(j-1\), \(I\) in column \(j\), and zero elsewhere.

Eliminate the columns successively from \(j=d\) down to \(1\). When the last nonzero top-row coefficient is \(A_j=a_j+a_{j+1}z+\cdots+a_dz^{d-j}\), left multiplication by \(I-E_{0j}(A_j)\) clears it and replaces the preceding coefficient by \(a_{j-1}+A_jz\). Right multiplication by \(I+E_{j,j-1}(zI)\) then clears the subdiagonal \(-zI\) without disturbing that top row. The result after all steps is \(\operatorname{diag}(f,I_{dr})\). Every elementary factor is connected to the identity through invertibles by multiplying its off-diagonal block by a real parameter in \([0,1]\); its inverse changes that block's sign. This proves both invertibility of \(\mu(f)\) on the circle and a homotopy to the displayed diagonal matrix. Basing the entire homotopy by right multiplication with its value at \(1\) inverted gives a based linear loop



```{=latex}
\begin{equation}
\ell(z)=\mu(f)(z)\mu(f)(1)^{-1}=I+(z-1)b
\label{courseIII:almost-complex-structures-and-integrability:eq:10.4}
\end{equation}
```



with the same stable class as \(f\). This includes \(d=0\), where the based polynomial is already the identity.

The spectrum of \(b\in M_{(d+1)r}(C(Y))\) misses the line \(\operatorname{Re}\lambda=1/2\). For \(z\ne1\),
\(I+(z-1)b=(1-z)((1-z)^{-1}I-b)\),
and the numbers \((1-z)^{-1}\), \(z\in\mathbb T\setminus\{1\}\), run exactly along that line. Let \(e\) be the Riesz idempotent for the spectral part to its right:



```{=latex}
\begin{equation}
e=\frac1{2\pi i}\int_\Gamma(\lambda I-b)^{-1}\,d\lambda,
\label{courseIII:almost-complex-structures-and-integrability:eq:10.5}
\end{equation}
```



where \(\Gamma\) is a positively oriented contour enclosing that part and no other spectrum. Such a contour can be chosen uniformly on \(Y\): the matrices are bounded, and the compact spectrum of the algebra element has positive distance from the separating line. The resolvent identity proves continuity of the integral, its commutation with \(b\), and its idempotence. For the last statement, multiply the two contour integrals on nested separating contours and use




```{=latex}
\[
(\lambda-b)^{-1}(\mu-b)^{-1}=((\lambda-b)^{-1}-(\mu-b)^{-1})/(\mu-\lambda)
\]
```



,
then apply the scalar Cauchy formula. It also shows that \(e\) acts as identity on the enclosed spectral summand and zero on its complement.

The path \(b_t=(1-t)b+te\) keeps its right spectral part strictly to the right of the line and its left part strictly to the left: on those two invariant summands its spectra are respectively \((1-t)\lambda+t\) and \((1-t)\lambda\). Thus \(I+(z-1)b_t\) stays invertible. Its endpoint is \(I-e+ze\).

The image of \(e(y)\) is a vector bundle \(E_e\): its rank is locally constant, and a nonzero minor supplies local frames. Let \(p_e\) be its orthogonal range projection. In the orthogonal splitting \(E_e\oplus E_e^\perp\), the idempotent has matrix \(\begin{pmatrix}I&T\\0&0\end{pmatrix}\). Replacing \(T\) by \((1-t)T\) is a continuous idempotent homotopy from \(e\) to \(p_e\), and \(I-e_t+ze_t\) is invertible with inverse \(I-e_t+z^{-1}e_t\). Hence the endpoint loop multiplies by \(z\) on the actual bundle \(E_e\) and by one on its complement.

\subsubsection{Integral Chern characters on a product of two-spheres}
\label{courseIII:almost-complex-structures-and-integrability:section-10.3}

Let \(Q\) be the line over \(S^2=\mathbb{CP}^1\) with finite-chart frame \((1,\zeta)\) and infinity-chart frame \((1/\zeta,1)\). The finite frame equals \(\zeta\) times the infinity frame. Thus the coefficient transfer from the finite to the infinity chart is exactly the loop \(z\) used above. Put \(b=[Q]-[\mathbf1]\), keeping the subtracted rank-one class.

The preceding reduction and \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.2} show that for every compact \(Y\), the group \(K^0(S^2\times Y)\) is generated by



```{=latex}
\begin{equation}
\operatorname{pr}_Y^*K^0(Y)
\quad\text{and}\quad
\operatorname{pr}_{S^2}^*b\ \operatorname{pr}_Y^*K^0(Y).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.6}
\end{equation}
```



To retain the ranks and the Laurent contribution explicitly, a stabilized clutching loop \(g_0\) of size \(r\) has



```{=latex}
\begin{equation}
[T_{g_0}]-r[\mathbf1]
=b\left([E_e]-ar[\mathbf1]\right).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.7}
\end{equation}
```



Indeed the endpoint \(I-p_e+zp_e\) clutches \((Q\otimes E_e)\oplus E_e^\perp\), whose difference from the trivial bundle is \(b[E_e]\). The original loop is obtained from \(f=z^ag_0\) by subtracting the \(a\) positive scalar loops on all \(r\) coordinates, by \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.2}. Finally undo the original complement added to trivialize the hemisphere restrictions; its class lies in the first summand of \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.6}. This proves the full generation assertion needed here.

We fix the integral Chern sign first. The coordinate functional \((z_0,z_1)\mapsto z_1\), restricted to the tautological line, is a section of \(Q^*\). It has one zero, at \([1:0]\). In the finite frame \((1,\zeta)\), its coefficient is \(\zeta\), whose real derivative has positive determinant. The Euler class of a complex line equals its first Chern class; the local zero formula therefore gives \(c_1(Q^*)=u\) and \(c_1(Q)=-u\). The local zero formula follows by pulling the positive fibre Thom class back under the section, using excision to split the relative group into its isolated-zero disks, and evaluating each local degree on the oriented disk. Homotopy of the section to the zero section identifies the resulting absolute class with the Euler class. This also proves the zero-count formula used in Section 10.5.

The curvature calculation provides the exact differential-form comparison in these coordinates. Use the unit section \(s=(1,\zeta)/\sqrt{1+|\zeta|^2}\). The projected unitary connection has connection and curvature forms



```{=latex}
\begin{equation}
\mathcal A=s^*ds=
\frac{\bar\zeta\,d\zeta-\zeta\,d\bar\zeta}{2(1+|\zeta|^2)},
\qquad
\mathcal F=d\mathcal A=
\frac{d\bar\zeta\wedge d\zeta}{(1+|\zeta|^2)^2}.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.8}
\end{equation}
```



With the convention \(c_1=(i/2\pi)\mathcal F\), its integral in the complex orientation is



```{=latex}
\begin{equation}
\frac{i}{2\pi}\int_{\mathbb C}\mathcal F
=-\frac1\pi\int_{\mathbb R^2}\frac{dx\,dy}{(1+x^2+y^2)^2}
=-2\int_0^\infty\frac{r\,dr}{(1+r^2)^2}=-1.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.9}
\end{equation}
```



Thus \(c_1(Q)=-u\), where \(u\) is the positive integral generator. The clutching loop direction is positive while this tautological line's Chern number is negative; both signs are retained. Since \(u^2=0\),



```{=latex}
\begin{equation}
\operatorname{ch}(Q)=1-u,
\qquad \operatorname{ch}(b)=-u.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.10}
\end{equation}
```



The Chern character is defined degree by degree as rank plus the Newton power sum in the Chern roots divided by \(j!\) in degree \(2j\). Its sum and tensor rules follow from the integral splitting principle: pull back to a common flag bundle, where both bundles split into lines and pullback on cohomology is injective. If their line roots are \(t_i\) and \(u_j\), the characters are \(\sum_i e^{t_i}\) and \(\sum_j e^{u_j}\); the direct sum joins these lists, while the tensor product has roots \(t_i+u_j\). The finite homogeneous coefficients of \(e^{t+u}=e^te^u\), followed by injectivity of pullback, prove additivity and multiplicativity on the original base. These are the integral Chern classes, with the complex orientation on the underlying real bundle. The curvature expression \(\operatorname{tr}\exp(i\mathcal F/2\pi)\) has the same operations: direct sums are block diagonal, and the two tensor curvature endomorphisms commute. The factorial and rank in both expressions are retained.

For \(P_n=(S^2)^n\), let \(b_i\) and \(u_i\) be the pullbacks from the \(i\)-th factor. Induction using \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.6} proves that its K-group is generated by \(b_I=\prod_{i\in I}b_i\), for all subsets \(I\subseteq\{1,\ldots,n\}\), including \(b_\varnothing=1\). Its integral cohomology has basis \(u_I=\prod_{i\in I}u_i\), with \(u_i^2=0\). This follows from the product cell structure: each factor has one zero-cell and one two-cell, all cellular boundary maps vanish, and products of the oriented two-cells identify the cup products and their evaluations on the corresponding factor submanifolds. Formula \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.10} gives



```{=latex}
\begin{equation}
\operatorname{ch}(b_I)=(-1)^{|I|}u_I.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.11}
\end{equation}
```



These images are an integral basis, so the generators \(b_I\) are also independent. In particular the entire Chern character of every complex vector bundle on \(P_n\) has integral coefficients in this basis. This is the precise Bott integrality consequence required for the sphere argument, now with its generation and independence proved.

\subsubsection{The degree-one map and the factorial}
\label{courseIII:almost-complex-structures-and-integrability:section-10.4}

Collapse the union of subspaces of \(P_n\) in which at least one factor is its infinity point. The quotient is the smash product \(S^2\wedge\cdots\wedge S^2\), the one-point compactification of \(\mathbb R^{2n}\), hence a \(2n\)-sphere. Identify it with the outward-oriented unit sphere by



```{=latex}
\begin{equation}
x\longmapsto\frac{(2x,\,1-|x|^2)}{1+|x|^2},
\qquad \infty\longmapsto(0,\ldots,0,-1).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.12}
\end{equation}
```



At \(x=0\), the derivative in the \(2n\) tangent directions is twice the identity, and the outward normal is the last positive coordinate. Moving that normal to the front has sign \((-1)^{2n}=1\); thus the map has positive local degree. The resulting collapse map \(f:P_n\to S^{2n}\) has degree one and



```{=latex}
\begin{equation}
f^*u=u_1\cdots u_n
\quad\text{for the positive generator }u\in H^{2n}(S^{2n};\mathbb Z).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.13}
\end{equation}
```



It is an isomorphism on cohomology in degrees zero and \(2n\). It is not an isomorphism on the full cohomology when \(n>1\): the product has the additional classes \(u_I\) in intermediate degrees. This corrects the broader wording in Konstantis–Parton \cref{courseIII:almost-complex-structures-and-integrability:section-6} without altering the map used in their top-degree argument.

Let \(E\) be a complex vector bundle of rank \(r\) on \(S^{2n}\). All Chern classes below degree \(2n\) vanish, and classes above it are zero by dimension. Newton's identity gives



```{=latex}
\begin{equation}
\operatorname{ch}(E)=r+
\frac{(-1)^{n-1}}{(n-1)!}c_n(E).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.14}
\end{equation}
```



To check its coefficient, write the Chern polynomial as \(\prod_j(1+x_jt)=1+c_n t^n\) through degree \(n\). Its logarithmic derivative has coefficient \(nc_n\) at \(t^{n-1}\), whereas the product expression gives \((-1)^{n-1}\sum_jx_j^n\). Division by \(n!\) in the exponential defining the Chern character gives \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.14}, including its rank and sign. This symmetric-polynomial identity is valid in cohomology without choosing actual line summands on the sphere.

By naturality, \(f^*\operatorname{ch}(E)=\operatorname{ch}(f^*E)\). Equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.11}, \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.13}, and \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.14} imply



```{=latex}
\begin{equation}
\frac{\langle c_n(E),[S^{2n}]\rangle}{(n-1)!}\in\mathbb Z.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.15}
\end{equation}
```



We used only the top-degree coefficient of the exact pullback, while retaining the other cohomology classes of \(P_n\).

\subsubsection{Apply the calculation to the tangent bundle}
\label{courseIII:almost-complex-structures-and-integrability:section-10.5}

An almost complex structure on \(S^{2n}\) makes its real tangent bundle into a complex rank-\(n\) bundle \(E\). Its top Chern class is the Euler class in the orientation induced by \(J\): both are the signed zero obstruction of a section of the same oriented real bundle; a complex frame gives the same local orientation used for the top Chern obstruction. Write \(\sigma=1\) or \(-1\) for the sign of this orientation relative to the outward sphere orientation. Its outward-oriented tangent Euler number is exactly two, as the following section computes without a general Euler-characteristic theorem. Fix a unit \(a\in\mathbb R^{2n+1}\) and use the tangent field \(s_a(p)=a-\langle a,p\rangle p\). Its only zeros are \(p=a\) and \(p=-a\). Differentiation on the tangent space at either zero is \(-\langle a,p\rangle I\), so the two derivatives are \(-I\) and \(+I\) in real dimension \(2n\), both with determinant sign \(+1\). The zero-count proof in \cref{courseIII:almost-complex-structures-and-integrability:section-10.3} gives Euler number two. Reversing the fibre orientation multiplies its class by \(\sigma\). It follows that



```{=latex}
\begin{equation}
c_n(E)=2\sigma u.
\label{courseIII:almost-complex-structures-and-integrability:eq:10.16}
\end{equation}
```



Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.15} gives \((n-1)!\mid2\). Thus \(n\leq3\).

We must still exclude \(n=2\), and the following argument excludes every even \(n\). The full real stable trivialization is



```{=latex}
\begin{equation}
TS^{2n}\oplus\mathbf1_{\mathbb R}
\longrightarrow S^{2n}\times\mathbb R^{2n+1},
\qquad (p;v,a)\longmapsto(p;v+ap).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.17}
\end{equation}
```



Its inverse sends \((p;w)\) to \((p;w-\langle w,p\rangle p,\langle w,p\rangle)\). Complexifying it gives
\((E\oplus\bar E)\oplus\mathbf1_{\mathbb C}\simeq\mathbf1_{\mathbb C}^{2n+1}\).
The exact map behind \(E_{\mathbb R}\otimes\mathbb C\simeq E\oplus\bar E\) sends \(v\otimes z\) to \((zv,z\bar v)\), with scalar multiplication in the conjugate bundle in the second component. In underlying real notation its inverse on \((w,\bar v)\) is
\(\frac12(w+v)\otimes1+\frac12J(v-w)\otimes i\).
This proves the complexification comparison, including its conjugate summand; it does not assert that \(E\) itself is stably trivial as a complex bundle.

Conjugation gives \(c_j(\bar E)=(-1)^jc_j(E)\), since it negates each line Chern root; the equality also follows from conjugating the unitary curvature in the elementary symmetric Chern polynomial. Taking total Chern classes of the complexified stable trivialization, and using the dimension of the sphere, yields



```{=latex}
\begin{equation}
1=c(E)c(\bar E)
=1+(1+(-1)^n)c_n(E).
\label{courseIII:almost-complex-structures-and-integrability:eq:10.18}
\end{equation}
```



The term \((-1)^nc_n(E)^2\) is in degree \(4n\), which is zero on the \(2n\)-sphere; this is its exact reason for vanishing. If \(n\) is even, \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.18} says \(2c_n(E)=0\), contradicting \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.16} in the free group \(H^{2n}(S^{2n};\mathbb Z)\). Hence only \(n=1,3\) remain.

Both are realized. The complex atlas of \(\mathbb{CP}^1\), identified with \(S^2\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.12} in dimension two, provides \(n=1\). Formula \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1} provides \(n=3\); its failure of integrability does not affect the almost-complex assertion. With our original octonion labels, the orientation calculation after \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.9} gives \(\sigma=-1\), so its top Chern class is \(-2u\) in the outward orientation, and its top Chern character is \(-u\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.14}. An odd-dimensional real tangent space cannot carry \(J^2=-1\), because it would be a complex vector space and thus have even real dimension. This proves the claimed classification of positive-dimensional spheres. The zero-sphere consists of two complex zero-dimensional points and is outside that stated range.

\subsection{Six complete exercises}
\label{courseIII:almost-complex-structures-and-integrability:integrability-exercises}\label{courseIII:almost-complex-structures-and-integrability:section-11}

\subsubsection{Exercise 1. Keep the algebra and orientation comparisons together}
\label{courseIII:almost-complex-structures-and-integrability:exercise-1}

Prove that the map \(\Phi\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.6} preserves cross products and associators, and compute its determinant on the imaginary seven-space.

**Solution.** It preserves the real unit, the inner product, and multiplication by \eqref{courseIII:almost-complex-structures-and-integrability:eq:2.6}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:2.7}. Applying it to \(xy=-\langle x,y\rangle+x\times y\) therefore gives \(\Phi(x\times y)=\Phi(x)\times_\star\Phi(y)\). Applying it separately to the two bracketed products in \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.1} gives \(\Phi([x,y,z]_{\mathbb O})=[\Phi x,\Phi y,\Phi z]_\star\). In the basis \((1,e_1,\ldots,e_7)\), it fixes the first quaternion and the real coordinate of the second quaternion, and negates its three imaginary coordinates. Its full determinant is \((-1)^3=-1\). Since the real unit is fixed, the determinant on its perpendicular imaginary space is also \(-1\). Thus the induced sphere map reverses the specified ambient outward orientations while intertwining the two corresponding almost complex fields. Their complex orientations are transported by the intertwining differential, as follows directly from the ordered bases \((v_1,Jv_1,\ldots,v_3,Jv_3)\). There is no conflict between these two orientation statements: the ambient and complex orientations have each been specified separately and compared by explicit determinants.

\subsubsection{Exercise 2. Describe every fixed-vector obstruction map, including its zero case}
\label{courseIII:almost-complex-structures-and-integrability:exercise-2}

For \(\mathcal N_U\) in \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.4}, determine its kernel and image, solve \(\mathcal N_UV=W\) when it is solvable, and include \(U=0\).

**Solution.** If \(U\ne0\), equations \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.6}–\eqref{courseIII:almost-complex-structures-and-integrability:eq:4.8} give kernel \(\operatorname{span}_{\mathbb R}(U,JU)\), image \(W_U\), and the particular solution



```{=latex}
\begin{equation}
V_0=-\frac{\mathcal N_UW}{16|U|^2}\quad(W\in W_U).
\label{courseIII:almost-complex-structures-and-integrability:eq:11.1}
\end{equation}
```



Indeed applying \(\mathcal N_U\) gives \(W\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.7}. All solutions are \(V_0+aU+bJU\), \(a,b\in\mathbb R\), because their differences are exactly the kernel. A vector with nonzero component in \(\operatorname{span}(U,JU)\) is not in the image. If \(U=0\), bilinearity gives \(\mathcal N_0=0\), its kernel is the entire tangent space, its image is zero, and the equation has every \(V\) as a solution for \(W=0\) and no solution otherwise. No division in \eqref{courseIII:almost-complex-structures-and-integrability:eq:11.1} is applied to this zero case.

\subsubsection{Exercise 3. Determine all scalar holomorphic functions for the octonion field}
\label{courseIII:almost-complex-structures-and-integrability:exercise-3}

Let \(U\subset S^6\) be a connected open subset, and let \(f:U\to\mathbb C\) be a \(C^2\) function satisfying \(df\circ J=i\,df\) for the field \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1}. Prove that \(f\) is constant.

**Solution.** The equation says \(\bar\partial_Jf=0\). Hence \(\bar\partial_J^2f=0\). By \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.10}, \(df\) annihilates the image of \(\mathscr N\). Equation \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.12} says that image is the entire \(T^{1,0}_J\), while the original equation says that \(df\) annihilates \(T^{0,1}_J\). Their direct sum is the complexified tangent bundle, so \(df=0\). The function is locally constant, and connectedness makes it constant on \(U\). In the adapted frame the precise equations are



```{=latex}
\begin{equation}
(\bar\partial_J^2f)(\bar Z_2,\bar Z_3)=iZ_1f,
\quad
(\bar\partial_J^2f)(\bar Z_3,\bar Z_1)=iZ_2f,
\quad
(\bar\partial_J^2f)(\bar Z_1,\bar Z_2)=iZ_3f.
\label{courseIII:almost-complex-structures-and-integrability:eq:11.2}
\end{equation}
```



This is stronger than the assertion that this field supplies no holomorphic coordinate system. More generally the same proof applies to any almost complex structure for which the image of the complex tensor map in \eqref{courseIII:almost-complex-structures-and-integrability:eq:4.9} spans \(T^{1,0}\) at every point of the open set. It proves that exact consequence; it does not assert the same condition for a different field on the sphere.

\subsubsection{Exercise 4. Test the coordinate-change sign without discarding nonlinear terms}
\label{courseIII:almost-complex-structures-and-integrability:exercise-4}

In complex dimension one, take \(A=0\), real \(\epsilon\), and \(H(z)=z+\epsilon z\bar z\). Compute \(E=B\circ H\), the real Jacobian, and \(\Psi=(\partial_\zeta B)\circ H\) wherever the displayed inverses exist.

**Solution.** Here \(\bar H=\bar z+\epsilon z\bar z\), so \eqref{courseIII:almost-complex-structures-and-integrability:eq:6.7} gives



```{=latex}
\begin{equation}
E=-\frac{\epsilon z}{1+\epsilon z},
\qquad
j_H=(1+\epsilon\bar z)(1+\epsilon z)-\epsilon^2z\bar z
=1+\epsilon(z+\bar z).
\label{courseIII:almost-complex-structures-and-integrability:eq:11.3}
\end{equation}
```



The cancelled quadratic terms are displayed in the determinant. The inverse real Jacobian gives
\((\partial_\zeta H^{-1})\circ H=(1+\epsilon z)/j_H\).
The expression \(E\) is holomorphic in \(z\), so its \(\bar z\)-derivative is zero. Therefore



```{=latex}
\begin{equation}
\Psi=-\frac{\epsilon}
{(1+\epsilon z)\{1+\epsilon(z+\bar z)\}}.
\label{courseIII:almost-complex-structures-and-integrability:eq:11.4}
\end{equation}
```



For example, on \(|\epsilon z|<1/4\) both denominators are nonzero and the real Jacobian is positive. The first variation is \(-1\), in agreement with \(-\frac14\Delta(z\bar z)=-1\). This local test is not the periodic coordinate choice in \cref{courseIII:almost-complex-structures-and-integrability:section-7}; it verifies the sign using the original nonlinear formula on its stated domain.

\subsubsection{Exercise 5. See the intermediate cohomology which the collapse does not remove}
\label{courseIII:almost-complex-structures-and-integrability:exercise-5}

On \(S^2\times S^2\), expand the full K-class and Chern character of \(Q_1\otimes Q_2\), and compare with a pullback from \(S^4\) under \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.12}.

**Solution.** Since \([Q_i]=1+b_i\),



```{=latex}
\begin{equation}
[Q_1\otimes Q_2]=1+b_1+b_2+b_1b_2,
\qquad
\operatorname{ch}(Q_1\otimes Q_2)
=1-u_1-u_2+u_1u_2.
\label{courseIII:almost-complex-structures-and-integrability:eq:11.5}
\end{equation}
```



The two degree-two terms are nonzero: they pair as \(-1\) with the respective factor spheres. A bundle of rank \(r\) on \(S^4\) has Chern character \(r-c_2\) by \eqref{courseIII:almost-complex-structures-and-integrability:eq:10.14}, so its pullback has the form \(r-mu_1u_2\) for an integer \(m\); it has no degree-two component. Thus the line in \eqref{courseIII:almost-complex-structures-and-integrability:eq:11.5} is not such a pullback. The map \(f^*\) identifies the top generators exactly but does not make the product's intermediate classes disappear. This is the concrete distinction needed in the sphere proof.

\subsubsection{Exercise 6. Conjugate the actual almost complex field}
\label{courseIII:almost-complex-structures-and-integrability:exercise-6}

Compute \(N_{-J}\), the complex orientation, and the top Chern class for the negative of the field \eqref{courseIII:almost-complex-structures-and-integrability:eq:3.1}, preserving the outward orientation of the labelled sphere.

**Solution.** Substitute \(-J\) in all four terms of \eqref{courseIII:almost-complex-structures-and-integrability:eq:1.5}. The first term has two minus signs in its bracket, and each of the last two terms has one minus sign from the outer endomorphism and one from the inner vector. Consequently



```{=latex}
\begin{equation}
N_{-J}=N_J.
\label{courseIII:almost-complex-structures-and-integrability:eq:11.6}
\end{equation}
```



The ordered real complex basis changes from \((v_1,Jv_1,v_2,Jv_2,v_3,Jv_3)\) to \((v_1,-Jv_1,v_2,-Jv_2,v_3,-Jv_3)\), so its orientation changes by \((-1)^3=-1\). Since the original field has sign \(-1\) relative to the outward orientation, the conjugate has sign \(+1\). Its complex tangent bundle is the conjugate bundle of the original one, so \(c_3\) changes from \(-2u\) to \(+2u\), and \(\operatorname{ch}_3=c_3/2\) changes from \(-u\) to \(+u\). The nonzero tensor in \eqref{courseIII:almost-complex-structures-and-integrability:eq:11.6} remains, so this conjugate field is also not integrable. The calculation changes an orientation and a Chern sign without changing the zero condition of the actual tensor.



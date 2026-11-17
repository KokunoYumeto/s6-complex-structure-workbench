\section{The exact characteristic-two coordinate calculation}\label{courseIII:the-exact-characteristic-two-coordinate-calculation:section}
The following complete arguments are retained as re-derivations of their classical prerequisites. Source-specific calculations and their hypotheses are stated explicitly.



This is a fully written algebraic prerequisite for assessing the real-oriented route in Kiran Luecke, arXiv:2109.00048v2, original author TeX 158–187. It does not construct the required bordism spectrum or import that source's orientation and cooperation calculations. No topological cooperation classification or novelty is claimed here.

\subsection{Every symmetric homogeneous additive two-cocycle}
\label{courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-cocycles}\label{courseIII:the-exact-characteristic-two-coordinate-calculation:section-1}\label{courseIII:formal-char2:1}

Let \(R\) be a commutative \(\mathbb F_2\)-algebra, and let \(N\geq2\). Suppose


```{=latex}
\begin{equation}
C(x,y)=\sum_{i=1}^{N-1}c_i x^{N-i}y^i\in R[x,y]
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.1}
\end{equation}
```


is symmetric and satisfies the full polynomial identity


```{=latex}
\begin{equation}
C(x,y)+C(x+y,z)=C(y,z)+C(x,y+z).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2}
\end{equation}
```


All coefficients belong to the original ring; no division by a possibly nonunit will be used. Differentiating \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2} with respect to \(z\) and setting \(z=0\) gives


```{=latex}
\begin{equation}
\frac{\partial C}{\partial y}(x,y)
   =c_1\bigl((x+y)^{N-1}-y^{N-1}\bigr).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.3}
\end{equation}
```


If \(N\) is odd, the full polynomial
\(c_1((x+y)^N-x^N-y^N)\) has the derivative \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.3}, since the image of the integer \(N\) in \(R\) is \(1\). Subtract it from \(C\). The difference has zero derivative with respect to \(y\); by symmetry it also has zero derivative with respect to \(x\). In characteristic two, these two assertions mean that each nonzero monomial has even exponent in both variables: a monomial with an odd exponent has derivative coefficient \(1\), and distinct monomials do not acquire the same derivative exponent. Such a monomial cannot have the odd total degree \(N\). Hence in this case


```{=latex}
\begin{equation}
C(x,y)=c_1\bigl((x+y)^N-x^N-y^N\bigr).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.4}
\end{equation}
```



Suppose \(N>2\) is even. The coefficient of \(x^{N-2}y\) on the left of \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.3} is \(2c_2=0\). Its coefficient on the right is \((N-1)c_1=c_1\). Thus \(c_1=0\), and both derivatives of \(C\) are zero. Consequently there is a unique homogeneous polynomial \(D\) of degree \(N/2\) with


```{=latex}
\begin{equation}
C(x,y)=D(x^2,y^2).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.5}
\end{equation}
```


It is symmetric, has no axis terms, and satisfies \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2}: substitute \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.5} in that identity, use \((x+y)^2=x^2+y^2\), and use injectivity of the substitution homomorphism \(R[X,Y,Z]\to R[x,y,z]\), \((X,Y,Z)\mapsto(x^2,y^2,z^2)\). Injectivity follows from the distinct monomial exponents, even when \(R\) has zero divisors. At \(N=2\), every polynomial in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.1} has the form \(cxy\), and direct substitution verifies \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2}.

Write \(N=2^r q\), with \(q\) odd. Repeated use of \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.5}, ending with \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.4} when \(q>1\), proves the complete classification


```{=latex}
\begin{equation}
C(x,y)=
 \begin{cases}
 c\bigl((x+y)^N-x^N-y^N\bigr),&q>1,\\
 c\,x^{N/2}y^{N/2},&q=1.
 \end{cases}
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6}
\end{equation}
```


In the first case the coefficient is unique: the coefficient of \(x^{N-2^r}y^{2^r}\) in the displayed polynomial is the image of \(q\), hence is \(1\). This follows directly by raising the expansion of \((x+y)^q\) to the power \(2^r\). In the second case it is the displayed monomial coefficient. Conversely every polynomial in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} satisfies \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2}, either by cancellation of all four full binomial expansions or, for the second case, by the additivity of the power \(x\mapsto x^{N/2}\). Thus \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} proves both necessity and sufficiency over every indicated ring.

\subsection{Constructing the full coordinate and its inverse}
\label{courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-linearization}\label{courseIII:the-exact-characteristic-two-coordinate-calculation:section-2}\label{courseIII:formal-char2:2}

Let \(F(x,y)\in R[[x,y]]\) be a commutative one-dimensional formal group law with its original identities \(F(x,0)=x\), \(F(0,y)=y\), and suppose its actual two-series is


```{=latex}
\begin{equation}
[2]_F(x)=F(x,x)=0.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.1}
\end{equation}
```


We construct a strict coordinate \(l(x)=x+\sum_{j\geq2}l_jx^j\), including every coefficient, with


```{=latex}
\begin{equation}
l(F(x,y))=l(x)+l(y).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.2}
\end{equation}
```


The assertion is about the full formal series, not an equality through a tested degree.

Proceed by integer degree \(N=2,3,\ldots\). Suppose a previously constructed invertible coordinate \(L_{N-1}\) gives the full formal law


```{=latex}
\begin{equation}
F_N(x,y)=L_{N-1}\bigl(F(L_{N-1}^{-1}(x),L_{N-1}^{-1}(y))\bigr)
 =x+y+\sum_{i,j\geq1,\ i+j\geq N}a^{(N)}_{ij}x^iy^j.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.3}
\end{equation}
```


For the initial step use \(L_1(x)=x\). Every coefficient in the infinite remainder in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.3} is retained by this definition. Let
\(C_N(x,y)=\sum_{i+j=N}a^{(N)}_{ij}x^iy^j\).
Comparing the total-degree-\(N\) coefficients in the two full associativity expressions for \(F_N\) gives \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2} for \(C_N\). Substituting a nonlinear term of degree at least \(N\) into a monomial of degree \(N\) changes that monomial only in degrees at least \(2N-1>N\); this proves that no further degree-\(N\) terms were lost in that comparison. Commutativity gives symmetry, so \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} applies.

The coordinate change in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.3} preserves the full equation \(F_N(x,x)=0\), because it is \(L_{N-1}(F(L_{N-1}^{-1}(x),L_{N-1}^{-1}(x)))\). If \(N\) is a power of two, \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} gives \(C_N=cx^{N/2}y^{N/2}\). Its value at \((x,x)\) is \(cx^N\). All the other terms in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.3} have larger total degree and hence give powers of \(x\) larger than \(N\). Equation \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.1} therefore forces \(c=0\). At this stage put \(h_N(x)=x\).

If \(N\) is not a power of two, use the unique coefficient \(c\) in the first line of \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} and put


```{=latex}
\begin{equation}
h_N(x)=x+cx^N.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.4}
\end{equation}
```


This has a complete formal inverse. Explicitly, for \(g(x)=x+\sum_{j\geq2}b_jx^j\), set recursively


```{=latex}
\begin{equation}
b_j=-c\,[x^j]\left(x+\sum_{2\leq i<j}b_ix^i\right)^N\qquad(j\geq2).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.5}
\end{equation}
```


Only the already fixed coefficients enter \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.5}, since \(N\geq2\). It gives \(h_N(g(x))=x\) coefficient by coefficient. The same recursive solution exists for a left inverse, and composing the two identities shows that it is this very \(g\); thus both inverse identities hold. The minus sign in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.5} is retained, with its image in \(R\) equal to plus.

Now set


```{=latex}
\begin{equation}
L_N=h_N\circ L_{N-1},\qquad
 F_{N+1}(x,y)=h_N\bigl(F_N(h_N^{-1}(x),h_N^{-1}(y))\bigr).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.6}
\end{equation}
```


The total-degree-\(N\) term in the second formula is


```{=latex}
\begin{equation}
C_N(x,y)+c\bigl((x+y)^N-x^N-y^N\bigr)=0,
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.7}
\end{equation}
```


using \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} and the original coefficient equality \(2c=0\). In the power-of-two case both contributions were zero already. All terms of smaller degree are unchanged, and the higher coefficients are exactly those of the full composition in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.6}. Thus the induction hypothesis \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.3} holds at the next step without replacing any higher coefficient by zero.

For every fixed degree \(d\), the coefficients of \(L_N\) through degree \(d\) are unchanged once \(N>d\). Define \(l_d\) to be their stabilized values and let \(l\) be the resulting full formal series. The same stabilization holds for the complete inverses, so they give \(l^{-1}\) and both inverse identities. Any fixed coefficient in a composite of formal series depends on finitely many input coefficients. Passing to those stabilized coefficients in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.6} proves \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.2} in every degree, and therefore as an identity in \(R[[x,y]]\). The construction uses only coefficient extraction, addition and multiplication in \(R\); applying a ring homomorphism to all its steps gives the same construction over the target ring.

\subsection{Every strict automorphism of the additive law}
\label{courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-additive-series}\label{courseIII:the-exact-characteristic-two-coordinate-calculation:section-3}\label{courseIII:formal-char2:3}

For a series \(f(x)=x+\sum_{N\geq2}a_Nx^N\), the identity \(f(x+y)=f(x)+f(y)\) is equivalent, degree by degree, to
\(a_N((x+y)^N-x^N-y^N)=0\).
If \(N\) is not a power of two, the coefficient identified after \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6} is \(1\), so it forces \(a_N=0\), even over a ring with zero divisors. If \(N=2^i\), all mixed binomial coefficients are zero in characteristic two, so \(a_N\) is unrestricted. Thus every such strict automorphism, with its unique full inverse, has exactly the form


```{=latex}
\begin{equation}
f(x)=\sum_{i\geq0}a_i x^{2^i},\qquad a_0=1.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.1}
\end{equation}
```


For \(g(x)=\sum_{j\geq0}b_jx^{2^j}\), retain the chosen composition order. The complete coefficient formula is


```{=latex}
\begin{equation}
(g\circ f)(x)
   =\sum_{n\geq0}\left(\sum_{i+j=n}a_j^{2^i}b_i\right)x^{2^n}.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.2}
\end{equation}
```


For each fixed \(n\), this sum is finite and includes both endpoints \(a_n\) and \(b_n\). No assumption on nilpotence is needed. It follows directly that the functor of these coefficient sequences is represented by the polynomial algebra \(\mathbb F_2[\xi_1,\xi_2,\ldots]\), with \(\xi_0=1\), coproduct recording this precise order given by


```{=latex}
\begin{equation}
\Delta\xi_n=\sum_{i=0}^{n}\xi_{n-i}^{2^i}\otimes\xi_i,
 \qquad\epsilon(\xi_n)=0\quad(n\geq1).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3}
\end{equation}
```


Associativity of full series composition proves coassociativity of \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3}, and the identity series proves both counit equations. If the variable \(x\) has cohomological degree \(1\), the coefficient \(a_i\) has cohomological degree \(1-2^i\); the corresponding homological coefficient generator in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3} has degree \(2^i-1\). The complete grading change is this reversal, not an omitted factor. Formula \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3} agrees algebraically with the precise Milnor coproduct already used by the course. Identifying its representing functor with the actual spectrum's cooperation functor still requires the geometric orientation and bordism arguments; it is not a consequence of this algebraic calculation alone.

\subsection{The full inverse operation and two worked exercises}
\label{courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-inverse-exercises}\label{courseIII:the-exact-characteristic-two-coordinate-calculation:section-4}\label{courseIII:formal-char2:4}

Write the inverse of \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.1} as \(g(x)=\sum_{i\geq0}b_ix^{2^i}\), with \(b_0=1\). It is additive because applying \(f\) to \(g(x+y)\) and to \(g(x)+g(y)\) gives the same series, and substitution by the inverse of \(f\) is injective. Equation \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.2}, with \(g\circ f=x\), gives the complete recursive formula


```{=latex}
\begin{equation}
b_n=-a_n-\sum_{i=1}^{n-1}a_{n-i}^{2^i}b_i\qquad(n\geq1).
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.1}
\end{equation}
```


Every term involves previously determined coefficients. Both minus signs retain their original roles; their images in the coefficient ring equal plus. Conversely this recursion gives a left inverse and therefore the unique two-sided inverse already constructed. It represents the antipode of \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3}. In particular,


```{=latex}
\begin{equation}
b_1=a_1,\quad b_2=a_2+a_1^3,\quad
 b_3=a_3+a_1a_2^2+a_1^4a_2+a_1^7.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.2}
\end{equation}
```


Both antipode identities hold because both full series composites are the identity. This proves the group structure, including inversion, over every original coefficient ring.

\subsubsection{Exercise 4.1. A complete original law over a ring with zero divisors}
\label{courseIII:the-exact-characteristic-two-coordinate-calculation:exercise-4.1}\label{courseIII:formal-char2:4.1}

Let \(R=\mathbb F_2[u]/(u^3)\), and retain the exact coordinate \(h(x)=x+ux^3\). Find its full inverse and the complete law \(F(x,y)=h^{-1}(h(x)+h(y))\). Verify the two-series and the comparison without discarding higher contributions.

**Solution.** The polynomial


```{=latex}
\begin{equation}
g(x)=x+ux^3+u^2x^5
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.3}
\end{equation}
```


is its full inverse. Indeed


```{=latex}
\[
g+ug^3=x+ux^3+u^2x^5+ux^3+3u^2x^5=x.
\]
```


The coefficient \(3\) maps to \(1\); every further summand has a factor \(u^3\) and is exactly zero in the specified original ring. In the other order,


```{=latex}
\[
h+uh^3+u^2h^5=x+ux^3+ux^3+3u^2x^5+u^2x^5=x,
\]
```


by the same coefficient identities. Put \(s=x+y\) and \(t=x^3+y^3\) only for this displayed expansion. The entire composite is


```{=latex}
\begin{equation}
\begin{aligned}
 F(x,y)&=s+ut+u(s+ut)^3+u^2(s+ut)^5\\
 &=x+y+u(x^2y+xy^2)\\
 &\quad+u^2(x^4y+x^3y^2+x^2y^3+xy^4).
\end{aligned}
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.4}
\end{equation}
```


The first line retains all original factors. Terms with coefficient divisible by \(u^3\) vanish in \(R\); the remaining second-order contribution is
\(u^2(s^2t+s^5)\), which expands to exactly the four terms displayed. Thus \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.4} is the full formal law, not a finite approximation. Its associativity, identity and commutativity follow by applying the invertible \(h\) to both sides of those identities. Substitution \(y=x\) gives \(2x+2ux^3+4u^2x^5=0\), with all integer multiplicities retained before passage to \(R\). Finally \(h(F)=h(x)+h(y)\) follows from the proved inverse identity. At stage \(N=3\), \cref{courseIII:the-exact-characteristic-two-coordinate-calculation:section-2} selects this exact \(h\); its full composition eliminates the fifth-degree terms together with the third-degree ones. They were contributions of the original law, and were not deleted before the calculation.

\subsubsection{Exercise 4.2. Which order does the coproduct record?}
\label{courseIII:the-exact-characteristic-two-coordinate-calculation:exercise-4.2}\label{courseIII:formal-char2:4.2}

In the same ring, set \(f(x)=x+ux^2\) and \(g(x)=x+x^2\). Compute both full composites and compare them with the two endpoint terms and the middle term of \(\Delta\xi_2\).

**Solution.** Direct expansion gives


```{=latex}
\begin{equation}
\begin{aligned}
 (g\circ f)(x)&=x+(u+1)x^2+u^2x^4,\\
 (f\circ g)(x)&=x+(1+u)x^2+ux^4.
\end{aligned}
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.5}
\end{equation}
```


Their difference is \((u^2+u)x^4\neq0\) because \(1,u,u^2\) are an \(\mathbb F_2\)-basis of the original quotient ring. Formula \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3} gives


```{=latex}
\begin{equation}
\Delta\xi_2=\xi_2\otimes1+\xi_1^2\otimes\xi_1+1\otimes\xi_2.
 \label{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.6}
\end{equation}
```


Evaluating the first tensor factor on \(f\) and the second on \(g\) yields \(0+u^2\cdot1+0=u^2\), exactly the coefficient of \(x^4\) in \(g\circ f\). Reversing the evaluations yields \(u\). Both endpoint terms occur in \eqref{courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.6}, even though these particular two series give them value zero.

Illustration description: The full original nilpotent coordinate and the actual three-factor cooperation map.

The upper panel is the complete polynomial identity of formal-coordinate Exercise 4.1. The lower panel records the actual maps and factor order of projective-cooperation Sections 3–5. Both coproduct endpoints and the original integer two are retained. Reproducible source: `draw_projective_coordinate.py`.


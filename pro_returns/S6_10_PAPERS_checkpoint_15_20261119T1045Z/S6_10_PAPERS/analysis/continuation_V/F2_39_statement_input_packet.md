# maps:src:F.2.39: clean target and named input statements

Current statements only. All checker metadata and every target/input proof are stripped. No producing code or post-reading conclusions are included.

## Target

```tex
\begin{theorem}[the full effective classification and all marked gluings]\label{maps:src:F.2.39}



The linear classification and all-twist topological computation
asked for in F.2 have the following complete effective answer.
For $k=2$ and $k=3$, every admissible ordered integral tuple
has the canonical representative of \ref{maps:src:F.2.37}, with an explicit
simultaneous unimodular conjugator.  Equality of these
representatives is necessary and sufficient for simultaneous
integral conjugacy.  There is no fixed global height cutoff;
the finite stopping bound for an input of height $H$ is
$(2H+1)^{36(k+1)}$ candidates before the proved rejection
filters.  The separate involution normal form has exactly
56 classes and is computed completely in \ref{maps:src:F.2.38}.

For every choice of actual free affine orders and integer
numerators, integral clutch vector, and specified primitive
Kuhn cusp marking, \ref{maps:src:F.2.31} and \ref{maps:src:F.2.35} compute the full
fundamental group and every integral homology group of the
gluing.  This is the fully marked correction to \ref{maps:src:F.2.3};
peripheral matrices are not substituted for a choice of
filling.  The algorithms have no cutoff on affine orders,
twist entries or lattice indices.  The complete list of data
with $\pi_1=1$ and $H_2=H_3=0$ is the constructive
parametrization of \ref{maps:src:F.2.30}, with its exact lattice enumeration
and necessary-and-sufficient finite tests.  Each retained
filling has the homology and oriented smooth type stated
there.

\end{theorem}
```

## Named input maps:src:F.2.37

```tex
\begin{theorem}[a complete canonical-representative algorithm]\label{maps:src:F.2.37}



Every marked linear tuple in F.2, for either $k=2$ or $k=3$,
has a computable canonical integral representative and a
returned simultaneous unimodular conjugator. Two inputs have
the same representative if and only if they are simultaneously
$\mathrm{GL}_6(\mathbb Z)$ conjugate. The algorithm uses a proved
finite bound depending on the input. No fixed global entry bound
can represent every class.

This is an effective classification, not a claim that its
infinite output has been printed in a finite table. The
ordered involution sector has the separate complete finite
normal form \ref{maps:src:F.2.38}, and all of its $56$ classes have been
computed. The general bounded fallback is potentially very
expensive; its finiteness is a theorem, not a runtime estimate.

\end{theorem}
```

## Named input maps:src:F.2.38

```tex
\begin{theorem}[the complete ordered involution stratum]\label{maps:src:F.2.38}



There are exactly 56 simultaneous $\mathrm{GL}_6(\mathbb Z)$
conjugacy classes of ordered tuples $(M_1,M_2,M_0)$ satisfying
the primitive maximal-cusp conditions of F.2 with both finite
linear orders equal to two.  An explicit integral normalizer
returns a canonical representative and a checked unimodular
conjugating matrix for every such input, without any bound on
its entries.  Every representative has free affine lifts of
actual order four at both finite points.  None can give a
simply connected filling, for any choices of free affine
orders or twists.

\end{theorem}
```

## Named input maps:src:F.2.31

```tex
\begin{theorem}[complete fundamental-group data for every input]\label{maps:src:F.2.31}



Let $k=2$ or $3$, and let an integral rank-six tuple satisfy the
finite-order and primitive maximal-cusp conditions of F.2.  No
irreducibility, determinant-one, or prospective-survivor hypothesis is
imposed.  Specify each actual finite affine action as
\[
 \tau_i(x)=M_ix+v_i/m_i,\qquad v_i\in\Lambda=\mathbb Z^6,
 \quad \tau_i^{m_i}=1\text{ on }\Lambda_{\mathbb R}/\Lambda,
 \tag{F.G1}\label{maps:eq:F.G1}
\]
and require its cyclic action to be free.  The numerator need not be
fixed by $M_i$.  Define its actual integral power vector and the cusp
lattice by
\[
 w_i=\frac1{m_i}\sum_{j=0}^{m_i-1}M_i^jv_i\in\Lambda^{M_i},
 \qquad U=\operatorname{im}\bigl((M_1\cdots M_k)^{-1}-I\bigr).
 \tag{F.G2}\label{maps:eq:F.G2}
\]
Use left conjugation transport for the peripheral generators $s_i$,
and record the integral translation clutching by $\kappa\in\Lambda$
in $s_1\cdots s_kx^\kappa=1$.  Then the full fundamental group is
\[
 \left\langle x^\lambda,s_1,\ldots,s_k\ \left|\
 \begin{array}{l}
 x^\lambda x^\mu=x^{\lambda+\mu},\quad x^u=1\ (u\in U),\\
 s_ix^\lambda s_i^{-1}=x^{M_i\lambda},\quad
 s_i^{m_i}=x^{w_i},\quad s_1\cdots s_kx^\kappa=1
 \end{array}\right.\right\rangle .                         \tag{F.G3}\label{maps:eq:F.G3}
\]
Only a basis of $\Lambda$ and of $U$ is needed in this finite
presentation.  The program below also determines exactly which
quotient of the apparent fibre subgroup injects.

Put
\[
 L=\sum_{g\in\langle M_1,\ldots,M_k\rangle}gU,
 \qquad A=\Lambda/L.                                      \tag{F.G4}\label{maps:eq:F.G4}
\]
This is an integral sum, without saturation.  For two points, put
$d=\gcd(m_1,m_2)$, $M=M_1$, and
$S_j(M)=I+M+\cdots+M^{j-1}$.  Choose integers $a,b$ with
$am_1+bm_2=d$, and set, in $A$,
\[
 \begin{split}
 w'_2&=-w_2-S_{m_2}(M)\kappa,\\
 e&=(m_2/d)w_1-(m_1/d)w'_2,\qquad
 z=aw_1+bw'_2,\qquad \overline A=A/\langle e\rangle .
 \end{split}                                             \tag{F.G5}\label{maps:eq:F.G5}
\]
There is an exact sequence and a complete marked extension description
\[
 1\longrightarrow\overline A\longrightarrow\pi_1
   \longrightarrow C_d\longrightarrow1,
 \qquad txt^{-1}=M(x),\quad t^d=z.                         \tag{F.G6}\label{maps:eq:F.G6}
\]
Thus its order is $d|\overline A|$ if $\overline A$ is finite;
otherwise it is infinite.  In particular $d=1$ gives precisely
the abelian group $\overline A$.

For three genuine points, so $m_i\ge2$, let
\[
 \Gamma=\langle q_1,q_2,q_3\mid q_i^{m_i}=1,
                         \ q_1q_2q_3=1\rangle,
 \qquad \epsilon=\sum_i1/m_i-1.                           \tag{F.G7}\label{maps:eq:F.G7}
\]
The action $q_i\mapsto M_i$ is well defined on $A$.
If $\epsilon\le0$, the exact sequence is
\[
                    1\longrightarrow A\longrightarrow\pi_1
                         \longrightarrow\Gamma\longrightarrow1. 
 \tag{F.G8}\label{maps:eq:F.G8}
\]
If $\epsilon>0$, $\Gamma$ is the finite spherical triangle group.
Using its action on $A$, form the exact transfer vector
\[
 e=\sum_{g\in\Gamma}g\kappa+
       \sum_{i=1}^3\ \sum_{g\in\Gamma/\langle q_i\rangle}g w_i.
 \tag{F.G9}\label{maps:eq:F.G9}
\]
The second sums use left coset representatives and are independent
of their choice.  In this case the exact sequence has kernel
$A/\langle e\rangle$, with the same lifted relations \eqref{maps:eq:F.G3}.
Consequently \eqref{maps:eq:F.G3}, \eqref{maps:eq:F.G6}, \eqref{maps:eq:F.G8}, and \eqref{maps:eq:F.G9} give every requested
fundamental group by finite operations, including the precise
injected abelian kernel and all extension data.  These statements
do not claim a conjugacy classification of the original tuples.

For every input, the full first integral homology is the Smith
cokernel of the integer matrix
\[
 \begin{pmatrix}
 M_1-I&\cdots&M_k-I&-w_1&\cdots&-w_k&\kappa\\
 0&\cdots&0&&\operatorname{diag}(m_1,\ldots,m_k)&&\boldsymbol1
 \end{pmatrix}.                                           \tag{F.G10}\label{maps:eq:F.G10}
\]
Here the bottom left zero block has $k$ rows.  The code records
the full matrix, not only its invariant factors.

\end{theorem}
```

## Named input maps:src:F.2.35

```tex
\begin{theorem}[complete integral homology of a marked gluing]\label{maps:src:F.2.35}



For every fully marked F.2 datum there is a terminating exact
integer algorithm computing every integral homology group of
the resulting eight-manifold, including every torsion invariant
factor.  The input consists of the finite homology matrices
$M_1,\ldots,M_k$, free affine numerators $v_i/m_i$ of their
actual orders, the integral clutch vector $\kappa$, and the
chosen primitive cusp marking
\[
 M_0=(M_1\cdots M_k)^{-1},\qquad
 M_0P=P\begin{pmatrix}I_3&I_3\\0&I_3\end{pmatrix},
 \qquad P\in\mathrm{GL}(6,\mathbb Z).                       \tag{F.GC1}\label{maps:eq:F.GC1}
\]
Here $k=2$ or $3$ and the genuine orders are at least two;
order-one sites are first eliminated as in \ref{maps:src:F.2.31}.
If a marking is not supplied, the algorithm makes and records
one by Smith reduction.  It does not identify that choice
with an unspecified prescribed marking.
The complete chain prefix through degree nine has at most
4003 generators in any degree.  No spectral-sequence
extension, saturation convention, orientation assumption or
unbounded search enters the homology calculation.

\end{theorem}
```

## Named input maps:src:F.2.3

```tex
\begin{proposition}[Counterexample: determination by peripheral data alone]\label{maps:src:F.2.3}



Monodromy matrices and affine twist vectors alone do not
determine the homology of a compact glued manifold.  A cusp
filling, or an equivalent relative topological specification,
is additional data.

\end{proposition}
```

## Named input maps:src:F.2.30

```tex
\begin{corollary}[constructive classification of all survivors]\label{maps:src:F.2.30}



For the marked Kuhn cap and affine translation clutchings
used throughout F.2, the following is a complete constructive
classification of the data with
$\pi_1=1$ and $H_2=H_3=0$, up to integral conjugacy of their
linear tuples and oriented diffeomorphism of their fillings.

There are no data with three genuine finite fillings.
With two fillings their actual affine orders are five and
four.  Order the order-five point first.
The complete, unbounded parameter set is the rational
projective normal form of \ref{maps:src:F.2.20} together with its
exceptional rational affine line.
For each parameter, run the terminating order,
conductor, stable-lattice, and primitive-extension algorithm
of \ref{maps:src:F.2.22}.  Discard precisely the integral classes failing
\eqref{maps:eq:F.HC1} or one of \eqref{maps:eq:F.HC3}.
The classes retained by this procedure are exactly all
surviving integral linear tuples.
For each retained class all simply connected affine
twists are exactly the choices satisfying \eqref{maps:eq:F.T12};
their fillings are all oriented diffeomorphic to its
normalized filling.
If ordered labels with the order-four point first are
desired, interchange the finite labels and recompute
$M_0=(M_1M_2)^{-1}$.

Every retained datum has
\[
 \pi_1=1,\qquad
 H_j=\begin{cases}
  \mathbb Z,&j=0,8,\\
  \mathbb Z^4,&j=4,\\
  0,&\text{otherwise},
 \end{cases}
 \tag{F.HC13}\label{maps:eq:F.HC13}
\]
and its oriented smooth manifold is
$3\mathbb{HP}^2\#(-\mathbb{HP}^2)$.
It has bounded-cusp holomorphic periods in the literal
sense of F.3, by \ref{maps:src:F.3.11}.
The classification here concerns the survivor subproblem.
It does not classify the nonsurviving tuples or compute
their full integral homology, as also requested in F.2.

\end{corollary}
```

## Named input maps:src:F.2.1

```tex
\begin{proposition}[the cusp normal form]\label{maps:src:F.2.1}



Under the integral index-one condition in F.2, the cusp matrix is
conjugate in $\operatorname{GL}_6(\mathbb Z)$ to
\[
 U=\begin{pmatrix}I_3&I_3\\0&I_3\end{pmatrix}.
\]
Its integral centralizer consists exactly of
$\left(\begin{smallmatrix}P&Q\\0&P\end{smallmatrix}\right)$
with $P\in\operatorname{GL}_3(\mathbb Z)$ and
$Q\in\operatorname{Mat}_{3\times3}(\mathbb Z)$.

\end{proposition}
```

## Named input maps:src:F.2.2

```tex
\begin{proposition}[a complete finite-order filter]\label{maps:src:F.2.2}



The linear order of a finite matrix in $\operatorname{GL}_6(\mathbb Z)$
which admits a free affine lift belongs to
\[
 \{1,2,3,4,5,6,8,10,12\}.
 \tag{F.3}\label{maps:eq:F.3}
\]
There are 38 possible degree-six cyclotomic characteristic
polynomials with an eigenvalue one, and 19 of them commute
with some real complex structure.  These are necessary types,
not 38 or 19 conjugacy classes of admissible tuples.

\end{proposition}
```

## Named input maps:src:F.2.36

```tex
\begin{theorem}[simultaneous integral conjugacy for every input]\label{maps:src:F.2.36}



There is an unconditional exact algorithm which decides simultaneous
$\mathrm{GL}_6(\mathbb Z)$ conjugacy of any two marked matrix tuples of
F.2 and returns a conjugating matrix when one exists. The algorithm
does not impose a bound on their entries, on the affine multiplicities,
or on the integral conjugator. More generally it applies to any integral
tuple containing a matrix $1+N$ with $N^2=0$ and $\operatorname{rank}N=3$;
the primitive-image assumption is unnecessary for this statement.

\end{theorem}
```

## Named input maps:src:F.2.33

```tex
\begin{theorem}[arbitrary finite affine caps]\label{maps:src:F.2.33}



Let $g(x)=Mx+v/m$ be a free cyclic affine action of actual order
$m\geq2$ on $T^r$, with $M\in\mathrm{GL}(r,\mathbb Z)$ and
$v\in\mathbb Z^r$.  For every specified degree bound $d$, there is
an explicit terminating integer algorithm producing chains and
boundary maps through degree $d+1$ for the pair
\[
 B=(D^2\times T^r)/\langle(s,x)\mapsto
 (e^{2\pi i/m}s,g(x))\rangle,
 \qquad Y=\partial B.                                      \tag{F.CA1}\label{maps:eq:F.CA1}
\]
The cap complex has at most $2^r$ generators in each degree and
the boundary complex at most $2^{r+1}$.  These are complexes of
finite rank in each degree; only their indicated finite prefixes
are required to compute $H_j(B)$, $H_j(Y)$ and $H_j(B,Y)$ for
$j\leq d$.  Their maps retain the affine translations and all
integral higher coherence terms.  In particular, the construction
does not replace an equivariant torus chain complex by its
homology without recording the correction terms.

\end{theorem}
```

## Named input maps:src:F.2.7

```tex
\begin{theorem}[the orbifold quotient]\label{maps:src:F.2.7}



For the specified torus fillings in F.2, with affine
multiplicities $m_1,\ldots,m_k$, the fundamental group of the
total space has a canonical surjection onto
\[
 \langle x_1,\ldots,x_k\mid
       x_i^{m_i}=1,\ x_1\cdots x_k=1\rangle.
 \tag{F.27}\label{maps:eq:F.27}
\]
Consequently a simply connected example with $k=2$ requires
$\gcd(m_1,m_2)=1$.  There is no simply connected example with
$k=3$ and $m_1,m_2,m_3\geq2$.  An affine multiplicity-one
point is an ordinary smooth point and reduces to the problem
with one fewer multiple fibre.

\end{theorem}
```

## Named input maps:src:F.2.16

```tex
\begin{theorem}[an unbounded integral family]\label{maps:src:F.2.16}



There are infinitely many simultaneous rational conjugacy classes
of integral rank-six tuples of the linear type $(5,4)$ in F.2,
with primitive maximal square-zero cusp.  An explicit infinite
subfamily has free affine lifts of orders five and four.
Apart from the parameter zero, the rank-five irreducible quotient
in the family is not self-dual.  Thus no finite bound on rational
conjugacy classes is valid for the unrestricted input tuples.
This does not assert infinitely many three-connected survivors.

\end{theorem}
```

## Exact convention data

The ordered tuple is (M1,...,Mk,M0), k=2 or3, with Mi integral six-by-six matrices of finite order for i>=1 and M0=(M1...Mk)^(-1). The maximal primitive cusp is N=M0-I with N^2=0, rankN=3 and primitive image. Integral conjugacy is simultaneous by one P in GL6(Z), preserving the order of the finite labels. Define the height of an integer tuple as the maximum absolute value of all its entries; any finite tie-breaking order may be specified explicitly and must be retained by the actual returned conjugator. The affine inputs and power vectors are exactly F.G1–F.G2 in the statement above, the clutch word is s1...sk x^kappa=1, and the cusp marking is the actual P in F.GC1. The prescribed filling is the index-one periodic Kuhn cap, not unspecified peripheral data.

The additional named displayed input F.CN3 is the exact identity
tr(M1 M2^3)=-v^4+v^3-v^2+2
for the explicit unrestricted integral family of F2.16. That family has just been independently checked in the continuation; its complete parameter definition follows in a separate definition-only attachment. The reference to F2.30 supplies its entire stated survivor classification as an input, including each of its named finite tests; no expanded target proof is included here.

The exact family-definition attachment is `analysis/continuation_V/F2_16_statement_parameter_packet.md`, SHA256 c2f08560ed7990f84b8ef27de67f1b4a994f50494b9867d206a0b915fbba4873. It contains only the parameter definitions and statements, not its target proof.

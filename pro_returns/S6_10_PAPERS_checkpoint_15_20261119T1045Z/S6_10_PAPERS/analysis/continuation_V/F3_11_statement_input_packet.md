# maps:src:F.3.11: clean target and named input statements

Current statements only. All checker metadata and every target/input proof are stripped. No producing code or post-reading conclusions are included.

## Target

```tex
\begin{theorem}[the bounded-cusp period decision]\label{maps:src:F.3.11}



Let
$B^*=\mathbb P^1\setminus\{p_0,p_1,\ldots,p_k\}$,
where $k\ge1$, and let
$\rho:\pi_1(B^*)\to GL^+(6,\mathbb R)$ be a representation.
Assume that the monodromy $M_0$ at $p_0$ satisfies
$(M_0-I)^2=0$ and $\operatorname{rank}(M_0-I)=3$.
Then there is a holomorphic period family with this monodromy
and nondegenerate real transversality everywhere on $B^*$,
equivalently a nondegenerate imaginary part in each local
normalized period chart.
In a marking with $M_0=\left(\begin{smallmatrix}I&I\\0&I\end{smallmatrix}\right)$
its cusp period is
\[
 Z(t)=\frac{\log t}{2\pi i}I_3+C(t),
 \qquad C(t)\text{ holomorphic at }t=0.
 \tag{F.O6}\label{maps:eq:F.O6}
\]
Any prescribed finite jet of $C$ at zero may be imposed.
For an integral primitive cusp the marking can be integral.
Consequently every topological survivor of F.2 admits the
period family requested literally in F.3.  No good-reduction
condition at the other, still punctured, points is included
in this assertion.

\end{theorem}
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

## Named input maps:src:F.3.8

```tex
\begin{theorem}[the unpolarized period domain has LSAP]\label{maps:src:F.3.8}



Let $D_3$ be the component of
\[
 \{F\in\operatorname{Gr}(3,\mathbb C^6):F\cap\overline F=0\}
\]
containing the standard complex structure, so that
$D_3\cong GL^+(6,\mathbb R)/GL(3,\mathbb C)$.
At every point, $D_3$
is dominated by a spanning tube of nine complex lines.  In particular,
it has the local spray approximation property (LSAP) and is Oka--1.
These assertions concern the unpolarized domain.

\end{theorem}
```

## Named input maps:src:F.3.10

```tex
\begin{lemma}[retaining isolated extension points]\label{maps:src:F.3.10}



Let $R$ be an open Riemann surface, $V\to R$ a holomorphic vector
bundle, and $\mathscr U\subset\operatorname{Gr}_r(V)$ an open
subset whose projection onto $R$ is surjective.  Let $S\subset R$
be finite.  Suppose that over $R\setminus S$ this projection is
a holomorphic fibre bundle with an LSAP fibre.  Let $K\subset R$
be a compact Runge set containing $S$ in its interior.
Every continuous section of $\mathscr U$ which is holomorphic
near $K$ can be deformed through sections to a holomorphic
section, with arbitrary uniform approximation on $K$ and
interpolation of any given finite jets at finitely many points
of its interior.  No fibre-bundle or Serre-fibration assertion
is required at the points of $S$.

\end{lemma}
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

## Named input maps:src:F.2.15

```tex
\begin{proposition}[automatic local complex compatibility]\label{maps:src:F.2.15}



Every simply connected datum of F.2 with two finite affine
fillings automatically has finite linear actions commuting
with real complex structures.  This assertion concerns the
individual finite actions and does not produce simultaneous
global periods.

\end{proposition}
```

## Exact period and cusp-chart definitions

For a real oriented rank-six local system Lambda_R on B*, write V=Lambda_R tensor C. The transverse periods are three-planes F in C6 satisfying F direct-sum conjugate(F)=C6; the representation acts by its actual real linear maps. F3.8 defines D3 to be the component containing the standard complex structure, and F3.9 explicitly asks for its associated D3 bundle. F3.11 itself does not state a preassigned component or name D3. For a chosen real cusp normalizer P, the actual coordinate map is F=P F_standard, so the cusp construction is transported from D3 to P D3. This packet imposes no extra requirement that P have positive determinant. A period family here is a holomorphic transverse section in the component specified by that actual cusp marking. In a split cusp marking N=M0-I=[[0,I3],[0,0]], a graph is represented by columns (Z;I3). The monodromy operation is Z->Z+I3. The correction coordinate C is defined by Z=(log t/(2pi i))I3+C; it is single-valued on the punctured disc. The labelled F.O7 condition is exactly det(y(t)I3+Im C)>0 with y(t)=-log|t|/(2pi). This specifies the positive transverse component in this graph chart. At t=0 the requested C extends holomorphically and has a prescribed finite matrix jet.

The open Riemann surface retaining this cusp point is R=P1 minus{p1,...,pk}. The removed other points carry no extension/good-reduction condition. Their representation data remain the actual original rho. The primary LSAP input already opened by root is Alarcon–Forstneric, Oka-1 manifolds v5, Definition7.7 p22 and Proposition7.13(d) p24, with the exact section/interpolation scope used in root's F3.8 review. F3.10 is included above as its complete existing in-paper statement, without its proof.

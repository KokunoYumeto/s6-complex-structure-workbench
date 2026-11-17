# P4.36: all Hopf normalizations are smooth minimal

Status: Proved; independently audited.

```tex
\subsection{Eliminating all positive-Euler Hopf resolutions}

\begin{statement}{P4.36}{Proved}
Every irreducible singular support in Part~4.2 whose
normalization has a Hopf minimal model has smooth minimal
Hopf normalization and Euler number zero. The assertion
does not assume initially that the normalization is smooth
or that its Euler number vanishes.
\end{statement}
\begin{proof}
Let $T\to N\to S\subset Y$ be the minimal normalization
resolution, and let $\pi:T\to T_0$ contract its $k$ blowups
to a minimal Hopf surface. We first take a finite unramified
primary Hopf cover $T'_0\to T_0$ and pull back the actual
sequence of point blowups. This gives a finite unramified
map $T'\to T$ and a blowup morphism $T'\to T'_0$.
Compose with $T\to Y$. All Chern calculations below take
place on this explicit smooth cover; no cover of the
singular normalization $N$ is asserted. To avoid a second
set of symbols we write $T,T_0,k,\rho$ for these covered
objects until the last paragraph.

The primary Hopf normal form and proof of P4.24 give a
nowhere-zero holomorphic foliation on $T_0$ tangent to
every compact curve. Its saturated pullback to $T$ is a
line subbundle away from finitely many simple saddle
zeros. It is tangent to every strict conductor component
and every created exceptional curve. The actual conductor
centres lie on these invariant curves. Every blowup centre
is either a regular point of this foliation or one of its
saddles. Let $\varepsilon=0$ in the first case and
$\varepsilon=1$ in the second. The same explicit two-chart
calculation as in P4.24 gives
\[
 c_1(L)=-K_T+V,\qquad
 V'=\mu^*V+\varepsilon E,
 \qquad K_T^2=-k,\qquad K_TV-V^2=0.
\]
Topologically trivial line-bundle factors from $T_0$ do
not change these integral intersection calculations.

Put $B=\rho^*TY$. Its first and second rational Chern
classes vanish: $b_2(Y)=0$ gives $c_1(TY)=0$ rationally,
and Poincar\'e duality gives $H^4(Y;\mathbb Q)=0$ and
hence $c_2(TY)=0$. The derivative $L\to B$ can now have
a divisorial zero, since $\rho$ contracts exceptional
curves. Denote that effective integral divisor by $Z$.
Dividing by it gives the saturated line injection in
codimension one
\[
 L'=L(Z)\longrightarrow B,
 \qquad c_1(L')=-K_T+V+Z.
\]
The quotient $Q=B/L'$ is torsionfree of rank two.
Write $z_0\ge0$ for the length of $Q^{**}/Q$.
The double dual is locally free on the smooth surface,
and the Chern sequence gives
\[
 c_2(Q^{**})=(-K_T+V+Z)^2-z_0.
\]

Let $E_B\subset B$ be the saturated rank-two image
of $d\rho:TT\to B$. Its determinant is
$\det E_B=\omega_T^{-1}(R)$, where the effective
integral divisor $R$ is the divisorial zero of the
determinant map. Since $E_B$ is saturated in $B$,
the divided foliation line $L'$ is contained in it.
The image of $E_B/L'$ in $Q^{**}$ is saturated in
codimension one. Its rank-one double dual
$J=(E_B/L')^{**}$ is a line bundle. The map into
$Q^{**}$ extends across the finitely many omitted
points by Hartogs, since both sheaves are locally
free there. Its saturation is therefore a line bundle
of first Chern class $R-V-Z$; the rank-one quotient
is an ideal sheaf of a zero-dimensional scheme
times a line bundle of first Chern class $K_T-R$.
Let its length be $z_1\ge0$. Thus
\[
 (-K_T+V+Z)^2-z_0
       =(R-V-Z)(K_T-R)+z_1.
\]
Using $K_T^2=-k$ and $K_TV-V^2=0$, this is precisely
\[
 \mathcal B(R,Z)
 :=R^2-K_TR-VR-ZR-K_TZ+2VZ+Z^2
 =k+z_0+z_1.                                      \tag{P4.36.1}
\]

We now evaluate the left side through the actual
point blowups, retaining all integral coefficients.
Push $R$ and $Z$ down along the chosen sequence.
At one reversed blowup write
\[
 R'=\mu^*R+cE,\quad Z'=\mu^*Z+dE,
 \quad K'=\mu^*K+E,\quad V'=\mu^*V+\varepsilon E.
\]
The integers $c,d$ are not assumed positive.
Since $E^2=-1$ and a pulled-back divisor has zero
intersection with $E$, direct expansion gives
\[
 \mathcal B(R',Z')-\mathcal B(R,Z)
 =-c^2+(1+\varepsilon)c+cd+(1-2\varepsilon)d-d^2.
\]
Set $a=c-1$ and $b=d-(1-\varepsilon)$. For each
$\varepsilon\in\{0,1\}$ this is exactly
\[
 1-(a^2+b^2-ab)\le1.                            \tag{P4.36.2}
\]
The quadratic form is
$\frac12(a^2+b^2+(a-b)^2)$; it is nonnegative
and is zero exactly when $a=b=0$.
All divisor intersections on the initial Hopf
surface are zero because $b_2(T_0)=0$.
Summing (P4.36.2) therefore gives
$\mathcal B(R,Z)\le k$.
Equation (P4.36.1) forces equality, $z_0=z_1=0$,
and at every single blowup
\[
 c=1,\qquad d=1-\varepsilon.                    \tag{P4.36.3}
\]

Every created exceptional curve has positive
coefficient in $Z$. At a regular centre, (P4.36.3)
adds one to its nonnegative pulled-back coefficient.
At a saddle centre it adds zero, but at least one
previously created exceptional curve passes through
that saddle. The original Hopf foliation has no
zero; the two-chart blowup calculation places each
new saddle on the new exceptional curve. Induction
therefore gives a positive pulled-back coefficient
at every later saddle blowup as well.

The foliation is tangent to each exceptional curve.
If its image under $\rho$ were a curve, the derivative
along its tangent line would be nonzero at a generic
point: a nonconstant holomorphic map of smooth
normalized curves in characteristic zero is
generically immersive. Positive divisorial order
of $d\rho|_L$ contradicts that fact. Thus every
created exceptional curve is contracted by $\rho$,
and hence by the normalization resolution, since
the normalization map is finite.

Return to the original, possibly secondary Hopf
surface. Every exceptional curve downstairs has
an exceptional lift in the finite unramified cover;
the preceding argument makes its image a point.
Thus all exceptional curves of the original
$\pi:T\to T_0$ would be contracted by the minimal
resolution $T\to N$. If $k>0$, the exceptional curve
of its last blowup is a smooth rational curve of
self-intersection $-1$, which a minimal resolution
cannot contract. Hence $k=0$.
There is no further exceptional contraction from
a minimal Hopf surface: every compact curve has
self-intersection zero by $b_2=0$, whereas a
nonempty exceptional configuration has negative
definite intersection matrix, as proved in P4R.6.
Therefore $T=N=T_0$ is a smooth minimal Hopf
surface. P4.24 gives $e(S)=0$ and its complete
elliptic-conductor description.
\end{proof}
```

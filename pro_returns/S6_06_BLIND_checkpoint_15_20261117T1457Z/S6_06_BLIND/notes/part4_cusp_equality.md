# P4.28–P4.29: cuspidal local rigidity and ruled equality

Status: Proved; independent root audit accepted 2026-11-17 03:00 UTC. The complete proof source below is included in part4.tex. Exact algebra was executed in code/part4/cusp_normal_forms.py.

```tex
\subsection{Cuspidal transverse type and the ruled equality case}

\begin{statement}{P4.28}{Proved}
Let $p$ lie on a reduced fibre support of Part~4.2.
Suppose its reduced singular locus is a smooth curve
near $p$, and its generic transverse plane-curve germ
is the cusp $a^2+b^3=0$. Then the actual germ at $p$
is analytically isomorphic to
$\{a^2+b^3=0\}\times(\mathbb C,0)$.
In particular its normalization is smooth.
\end{statement}
\begin{proof}
We extend the boundary argument of P4.20 in the
precise form used here. Suppose a deformation retains
the smooth critical curve near a fixed transverse
boundary sphere and retains transverse type $A_2$.
Near a boundary point, the holomorphic Morse lemma
in the nondegenerate transverse variable followed
by extraction of a cube root of a unit gives
coordinates with defining function $a^2+b^3$.
The third coordinate parametrizes the critical
curve. Its transversality to the boundary lets
one real third-coordinate variable be solved
from the boundary equation; the complex
coordinates $a,b$ remain free. Thus the
restriction to the boundary is submersive
at every nonzero level. Compactness and
the smooth part of the boundary give the
same uniform nonzero-level submersion as
in P4.20. Its finite-critical-value and
proper Ehresmann transport proof applies
unchanged. A compact spherical class of
nonzero square in a deformed nearby
fibre would therefore lie in an actual
nearby torus fibre, which is impossible.
All deformations below retain this
boundary transverse type.

Choose holomorphic coordinates $(x,y,z)$
so the smooth critical curve is $x=y=0$.
The transverse Hessian along it is a
symmetric rank-one matrix over the
discrete valuation ring $\mathbb C\{z\}$.
It is not the zero matrix generically.
It can be diagonalized holomorphically
to $h(z)x^2$. Here is the elementary
ring calculation. The determinant is
zero. Choose a diagonal entry of
minimal order; one exists since the
square of the off-diagonal entry is
the product of the two diagonal entries.
The ratio of the off-diagonal entry
to the chosen entry is holomorphic.
Completing its square gives the desired
invertible coordinate change. The
coefficient $h$ is not identically zero.

First suppose that the Hessian has
rank one at $p$. The Morse lemma with
parameters $(y,z)$ writes the reduced
equation as
\[
 g=X^2+y^3h_1(y,z).
\]
Indeed after removing the $X$ direction,
the remaining function and its first
two $y$ derivatives vanish on the
critical curve; the third derivative
is not identically zero there. If
$h_1(0,0)\ne0$, extracting its cube
root in the $y$ coordinate proves the
asserted product form.

Otherwise $h_1(0,z)$ has a zero of
finite positive order. Use
$g_\eta=X^2+y^3(h_1+\eta)$.
For arbitrarily small generic $\eta$,
the function $h_1(0,z)+\eta$ has a
simple zero $z_\eta$ near zero.
This follows directly from one-variable
Weierstrass preparation, avoiding the
finite critical values of $h_1(0,z)$.
At $(0,0,z_\eta)$ the function
$Z=h_1(y,z)+\eta$ is a coordinate,
since its $z$ derivative is nonzero.
The actual germ is
$X^2+y^3Z$, which is excluded by
P4.16: its nearby fibre has a
spherical class of square $-6$.
On a fixed sufficiently small boundary,
$h_1(0,z)$ is nonzero at the critical
curve, and this persists for small
$\eta$. The deformed transverse type
is therefore still $A_2$ there.
The preceding boundary transport gives
the contradiction.

It remains to exclude Hessian rank
zero at $p$, so $h(0)=0$. In the
diagonalizing coordinates add
$\varepsilon y^3$ to $g$. The
critical curve and its transverse
Hessian do not change. The cubic
coefficient in the transverse kernel
remains nonzero near the original
compact boundary for small
$\varepsilon$, so this deformation
has the boundary property just proved.
Choose $\varepsilon$ so that the
coefficient of $y^3$ at the origin
is nonzero.

On a smaller neighbourhood, Weierstrass
preparation in $y$ gives a unit times
\[
 P=y^3+a(x,z)y^2+b(x,z)y+c(x,z).
\]
Restriction to $x=0$ is a unit times
$y^3$, so all three coefficients
vanish at $x=0$. The critical-curve
equation $g_x(0,0,z)=0$ first gives
$c_x(0,z)=0$. In the identity
$g=U P$ the mixed derivative on
the critical curve is then
$g_{xy}=U b_x$, since the terms
containing $c,c_x,b$ vanish there.
The zero $xy$ Hessian entry therefore
gives $b_x(0,z)=0$. Thus
$x^2\mid b$, $x^2\mid c$, and
$x\mid a$.
The Tschirnhaus change $y=Y-a/3$
therefore gives exactly
\[
 P=Y^3+x^2H(x,Y,z).
\]
The coefficient $H(0,0,z)$ is a unit
multiple of the original Hessian
coefficient $h(z)$. It is not
identically zero but vanishes at
zero. Perturb it to $H+\eta$.
At a simple root of
$H(0,0,z)+\eta$, the coordinates
$(x,Y,Z=H+\eta)$ give
$Y^3+x^2Z$. P4.18 excludes this
binomial germ by its compact
spherical class of nonzero square.

There are two nested transport
neighbourhoods in this argument.
First fix the original ball for
$g\to g+\varepsilon y^3$.
Then choose a smaller ball in the
Weierstrass coordinate neighbourhood,
where $g+\varepsilon y^3$ has only
the original critical curve and its
boundary has transverse type $A_2$.
The second perturbation transports
its spherical class into a nearby
fibre on this smaller ball. Inclusion
puts it in a fibre on the original
ball; the first boundary transport
puts it in a fibre of $g$.
This does not require extending the
second perturbation outside its
coordinate neighbourhood.
Units in the reduced equations are
retained during the perturbations.
At a binomial special point a unit
can be absorbed by the positive
weighted coordinate scaling of
P4.16--P4.18.

We have ruled out both a zero
Hessian and a vanishing cubic
coefficient. The product form
follows. Its normalization is
the finite map
\[
 (u,z)\longmapsto (a=u^3,b=-u^2,z),
\]
whose source is smooth, whose
inverse rational parameter off
$b=0$ is $u=-a/b$, and whose
restriction to the conductor is
the identity on the $z$ coordinate.
\end{proof}

\begin{statement}{P4.29}{Proved}
Let $S$ be an irreducible singular support
in Part~4.2 whose normalization has ruled
resolution, and suppose $e(S)=0$.
In the double-horizontal-divisor case,
when the generic transverse type is
cuspidal $A_2$, the normalization is
a smooth minimal elliptic ruled surface.
The image conductor is a smooth elliptic
curve and every point along it has the
product cusp germ of P4.28.
\end{statement}
\begin{proof}
Use the notation of P4R.7 and P4R.9.
The actual resolved pole support is
a section $H$ with rational trees,
and its inclusion in the ruled
resolution $T$ induces an isomorphism
on fundamental groups. Thus
$\pi_1(S)=\pi_1(C)$, where
$C=\operatorname{Sing}(S)_{\rm red}$.
The virtually abelian curve-group
calculation gives $e(C)\ge0$, and
P4.13 gives $e(S_{\rm reg})\ge0$.
Equality makes both numbers zero.
The same connected-curve calculation
shows that $C$ has exactly one
normalized component, of genus one,
and has no point-identification
cycles.

All rational components of the
resolved pole support are contracted
to points: a nonconstant proper map
from a rational curve to the
elliptic normalization of $C$ is
impossible. Hence the strict
conductor consists only of $H$.
The generic cusp has one
normalization branch, so
$H\to C$ has generic degree one
and is the normalization of $C$.
In particular $H$ and the ruling
base both have genus one.

Every exceptional curve of
$T\to N$ is now rational and
vertical for the ruling, since
$H$ is not contracted. The ruling
$r:T\to H$ descends to a holomorphic
map $\bar r:N\to H$. For an explicit
descent, the image of
$(\rho_N,r):T\to N\times H$
projects properly and bijectively
to $N$, because $r$ is constant
on each exceptional fibre. Its
normalized graph projects finitely
and birationally to the normal
space $N$, hence is isomorphic
to $N$.

The normalization singularities
are rational. Indeed a sequence
of point blowups of a
$\mathbb P^1$-bundle has
$R^1r_*\mathcal O_T=0$.
For a blowup this follows from
the two affine charts, or from
the exact sequence of the
exceptional $\mathbb P^1$ with
$H^1(\mathcal O_{\mathbb P^1})=0$;
the assertion for the whole
sequence follows by Leray.
Since $\rho_{N*}\mathcal O_T
=\mathcal O_N$, the low-degree
Leray sequence for
$r=\bar r\circ\rho_N$ gives
\[
 \bar r_*R^1\rho_{N*}\mathcal O_T=0.
\]
Here $R^2\bar r_*\mathcal O_N=0$
because $\bar r$ has one-dimensional
fibres. The sheaf
$R^1\rho_{N*}\mathcal O_T$ is
supported at finitely many
normalization singular points,
and direct image of a nonzero
such sheaf to $H$ is nonzero.
Thus it vanishes. In particular
$\chi(\mathcal O_N)
=\chi(\mathcal O_T)=0$.

We next check the scheme structure
of the conductor, to prove that
its image curve is smooth.
Write $I$ for the conductor ideal
on $S$ and on $N$, and let
$C_{\rm sch}\subset S$ and
$D_{\rm sch}\subset N$ be its
two zero schemes. Locally
$\mathcal O_S$ is Gorenstein
of dimension two and
$\nu_*\mathcal O_N$ is a
maximal Cohen--Macaulay module.
Finite duality identifies
its dual module with $I$,
which is again maximal
Cohen--Macaulay. The depth
lemma in
$0\to I\to\mathcal O_S
\to\mathcal O_{C_{\rm sch}}\to0$
therefore gives depth one
for the conductor curve.
At a generic cusp its local
length in the transverse
direction is one. A
one-dimensional Cohen--Macaulay
scheme which is generically
reduced is reduced: any
nilpotent ideal would have
zero-dimensional support,
contradicting the absence of
embedded associated points.
Consequently $C_{\rm sch}=C$.

Put $L=\nu^*\omega_S$, a
torsion line bundle by P4.12.
Finite duality on $N$ gives
\[
 I=\omega_N\otimes L^{-1}.
\]
Serre duality on the compact
Cohen--Macaulay surface $N$
gives $\chi(I)=\chi(L)$.
The rational-singularity
comparison just proved and
the projection formula give
$\chi(L)=\chi(\rho_N^*L)$.
Riemann--Roch on the smooth
surface $T$, with the rational
Chern class of this torsion
line bundle equal to zero,
gives $\chi(\rho_N^*L)
=\chi(\mathcal O_T)=0$.
Therefore
$\chi(\mathcal O_{D_{\rm sch}})
=\chi(\mathcal O_N)-\chi(I)=0$.

The exact conductor square is
\[
 0\longrightarrow\mathcal O_S
 \longrightarrow
 \nu_*\mathcal O_N\oplus\mathcal O_C
 \longrightarrow\nu_*\mathcal O_{D_{\rm sch}}
 \longrightarrow0.
\]
Taking Euler characteristics and
using $\chi(\mathcal O_S)=0$
from P4.12 yields
$\chi(\mathcal O_C)=0$.
Its normalization is the
smooth elliptic curve $H$,
so the normalization sequence
gives $\chi(\mathcal O_C)
 =-\sum_p\delta(C,p)$.
All delta invariants vanish;
thus $C$ is smooth.

Every point of $C$ now satisfies
P4.28, so $S$ has the product
cusp germ there and $N$ is
smooth along the conductor.
It was already smooth away
from the conductor. P4.22
therefore applies and makes
this elliptic ruled
normalization minimal.
\end{proof}
```

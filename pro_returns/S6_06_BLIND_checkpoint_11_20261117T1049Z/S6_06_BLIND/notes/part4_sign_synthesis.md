# P4.26: numerical sign for every irreducible support

Status: Proved. The rational and intermediate-class-VII pushout arguments extend to the minimal normalization resolution because P4R.6 identifies the complete inverse image of the singular locus. P4.25 closes the reduced-conductor alternatives. Together with P4R.7–9 this proves the numerical sign for all irreducible supports. The global sum is stated for fibrations whose supports are all irreducible or NC; no sign for reducible non-NC supports is silently assumed.

```latex
\subsection{Numerical sign for arbitrary irreducible supports}

\begin{statement}{P4.26}{Proved}
In Part~4.2 every irreducible reduced fibre support
has nonnegative topological Euler number. For a
singular irreducible support, rational resolution
of the normalization gives strictly positive
Euler number; so does a resolution whose minimal
model is of class VII with positive second
Betti number. These assertions permit singular
normalization.

Every normal-crossing support has the
nonnegative even Euler number of P4.6.
Consequently, for a fibration all of whose
reduced supports are irreducible or have
normal crossings,
\[
 B=\mathbb P^1,\qquad c_3(Y)\in\{0,2\},
 \qquad b_3(Y)=2-c_3(Y).
\]
This last conclusion does not assume a
classification of the equality cases for
irreducible nonnormal supports.
\end{statement}
\begin{proof}
For an irreducible singular support use the
minimal resolution of its normalization
$\rho:T\to N\to S$, and put
$A=\rho^{-1}(\operatorname{Sing}S)_{\rm red}$,
$C=\operatorname{Sing}(S)_{\rm red}$.
P4R.6 gives an effective integral divisor
$D$ with support $A$ and $K_T+D$ torsion.
The resolution $T$ has Kodaira dimension
$-\infty$, by P4.12. We explain the two
remaining transfers from smooth
normalization to this resolution.

Suppose first that $T$ is rational.
Push $D$ to a minimal rational surface.
The complete anticanonical-support calculation
in P4.21 has the following exact alternatives.
The reduced support is connected; either
its fundamental group is trivial and all
its normalized components are rational,
or the divisor itself is reduced with
normal crossings. On $\mathbb P^2$ these
are the plane cubic configurations
enumerated there. On a ruled minimal
surface they are the degree-two horizontal
configurations there. Those arguments use
only the effective integral divisor and
$K+D\equiv0$, so apply to the present
resolved divisor.

We check their preservation through the
actual blowup morphisms. A blowup at
conductor multiplicity $\mu$ gives
exceptional coefficient $\mu-1$.
For $\mu=1$, the centre is a smooth
point of the reduced support and its
strict transform is isomorphic to that
support. For $\mu\ge2$, the whole
exceptional $\mathbb P^1$ belongs to
the new support. Its contraction is
the blowup map on supports. Collapsing
this connected simply connected
subcomplex does not change the
fundamental group, by van Kampen.
The reduced normal-crossing case stays
reduced normal crossing: a smooth
point gives coefficient zero and a
double point gives coefficient one.
Thus the same alternatives hold for
the actual divisor $D$ on $T$.

In the reduced normal-crossing alternative,
P4.25 makes $S$ normal crossing. Its
normalization is smooth, so this minimal
normalization resolution is the
normalization itself. The rational case
of P4.6--P4.8 gives $e(S)=2$.
In the other alternative $\pi_1(A)=1$
and $\pi_1(T)=1$. The proper-map pushout
$T\cup_A C\to S$ is a homeomorphism:
it is a continuous compact-to-Hausdorff
bijection, since $\rho$ is an isomorphism
off $A$ and $A$ is the full inverse
image of $C$. Compatible triangulation
makes $A\to T$ a cofibration.
Van Kampen therefore gives
$\pi_1(S)\simeq\pi_1(C)$.
Every normalized component of $C$ is
rational: a nonconstant map from a
normalized component of $A$ onto it
is a finite map from $\mathbb P^1$.
Contracted components of $A$ contribute
no exception to this statement.
The curve $C$ is connected, and its
fundamental group is a free group
$F_b$ on the cycles of its
point-identification graph. P4R.1
implies $b\le1$. If $c\ge1$ is the
number of its components, then
\[
 e(C)=c+1-b\ge1.
\]
P4.13 gives $e(S_{\rm reg})\ge0$,
so $e(S)>0$.

Now suppose that the minimal model
$T_0$ is of class VII with
$b_2(T_0)>0$. The divisor pushed to
$T_0$ satisfies the hypotheses of
Dloussky's numerically anticanonical
theorem exactly as in P4.23.
The verified sources and their
normalization-independent hypotheses
are specified there. The
Inoue--Hirzebruch and parabolic Inoue
alternatives give a reduced
normal-crossing divisor, preserved
under the blowups just checked.
P4.25 then makes $S$ normal crossing
and $T=N$ smooth. The immersive
normalization Chern formula would
give $e(T)=K_T^2$, whereas
$e(T)=b_2(T)>0$ and
$K_T^2=-b_2(T)$. These alternatives
cannot occur.

In the intermediate alternative
$A$ is a connected rational cycle
with attached rational trees, and
\[
 \pi_1(A)=\mathbb Z,\qquad
 \pi_1(T)=\mathbb Z.
\]
Both statements survive the actual
blowups; they concern the resolution
and do not require $N$ to be smooth.
Every normalized component of $C$
is again rational and $C$ is connected.
With $\pi_1(C)=F_b$, the pushout
presentation is exactly
\[
 \pi_1(S)=
 \langle t,c_1,\ldots,c_b
 \mid t^k=w(c_1,\ldots,c_b)\rangle
\]
for the actual two conductor-group
homomorphisms. A component contracted
to a point merely induces the zero
homomorphism on its group. The
amalgam and free-product normal-form
argument in P4.23, which allowed
arbitrary $k$ and $w$, gives $b\le1$
from virtual abelianness.
Thus $e(C)=c+1-b\ge1$, and
$e(S)>0$ follows again from P4.13.

This exhausts these two resolution
classes. Ruled resolutions of positive
base genus are covered by P4R.7
and P4R.9, and Hopf minimal models
by P4R.8. The class-VII minimal
model with $b_2=0$ is Hopf or Inoue,
by the verified classification in
P4.8. An Inoue model has no curves,
so it cannot carry the nonempty
effective divisor pushed down from
$D$. Therefore it does not occur
here. All irreducible singular
supports have now been covered.

A normal irreducible support is
smooth by P4.12. The cyclic
base-change comparison and torus
deformation theorem in P4.8 show
that it has a finite unramified
torus cover, hence Euler number
zero. This proves the full
irreducible assertion.

For the final global statement,
$B=\mathbb P^1$ follows from
$b_1(Y)=0$ and connected fibres,
as proved in P4.7. Euler
additivity over the finitely many
exceptional base values gives
\[
 e(Y)=\sum_{b\in B}
 e\bigl((f^{-1}(b))_{\rm red}\bigr),
\]
because a smooth torus has Euler
number zero and the complement
is a proper smooth fibre bundle.
Every summand is nonnegative
under the stated support
hypothesis. Poincar\'e duality
and $b_1=b_2=0$ give
$e(Y)=2-b_3(Y)$; the nondegenerate
skew-symmetric cup-product
pairing on $H^3(Y;\mathbb Q)$
makes $b_3(Y)$ even. Thus
$0\le e(Y)\le2$ and $e(Y)$ is
even, which proves the asserted
values and their Chern-number
interpretation.
\end{proof}
```

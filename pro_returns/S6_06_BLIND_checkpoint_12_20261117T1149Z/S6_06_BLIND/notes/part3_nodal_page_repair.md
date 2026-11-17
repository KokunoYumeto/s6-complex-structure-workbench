# A local real page repair with its actual circle line

Working exact local result, 17 November 2026. The global pullback
to the doubled four-cycle and its parameter-sheet multiplicity
remain to be identified. No new global return class is assigned.

## 1. A smooth replacement level in the opposite resolution

Use the new chart \((s,u,v)\) of (NS.3), with
\[
 q=suv,\qquad
 \delta(s,u,v)=(\delta^{-1}s,u,\delta v).
\]
The opposite chart is
\((S,U,V)=(s^{-1},su,sv)\).
Put \(R=|s|\), \(h=1+R^2\), and fix a small
\(\epsilon>0\). Define
\[
 {\cal R}_\epsilon^2
       =\frac{h^2|v|^2+\epsilon R^2}
                    {h^2|u|^2+\epsilon}.             \tag{PR.1}
\]
In the opposite chart this is the same function:
\[
 {\cal R}_\epsilon^2
       =\frac{(1+|S|^2)^2|V|^2+\epsilon}
                    {(1+|S|^2)^2|U|^2+\epsilon|S|^2}.
\]
It vanishes exactly on the first fixed disc and tends to infinity
exactly on the second fixed disc. On their complement it is a
positive smooth function. It is a submersion there. Indeed its
derivative with respect to \(|v|^2\) is positive; its derivative
with respect to \(|u|^2\) is negative when its numerator is
nonzero. A possible critical point therefore has \(u=v=0\),
where (PR.1) is \(R^2\), with nonzero radial derivative for
\(0<R<\infty\). The two endpoint charts give the same conclusion.

Away from the exceptional curve this function tends, as
\(\epsilon\to0\), to \(|v/u|\), the old line radius \(|t|\).
Choose a torus-invariant cutoff equal to one on a small normal
tube and zero on its outer collar. In the collar, the finite
levels under consideration have \(u,v\ne0\), and the old radius
has a uniformly nonzero differential. A sufficiently small
cutoff perturbation remains a submersion there. Its level can
be identified with the old level by integrating the torus-invariant
normal vector field which differentiates that one-parameter
family of levels. Thus the new and old pages have exactly the
same marked outer boundary.

For a fixed \(0<\rho<\infty\), the new quotient page is
\({\cal R}_\epsilon=\rho\) divided by the physical delta circle.
The action is free on this level because the level avoids the
fixed discs. Its orbit space under the residual two-torus is
connected: putting \(A=|u|^2,B=|v|^2\), its equation is
\[
 B=\rho^2 A+\frac{\epsilon(\rho^2-R^2)}{(1+R^2)^2}.
\]
For each \(R\), the allowed values of \(A\) form one interval,
starting at zero for \(R\leq\rho\) and at the value which makes
\(B=0\) for \(R\geq\rho\). This lower boundary stays inside
the small tube for small \(\epsilon\). Truncating by the
transported outer collar gives one connected region, and all
torus orbits are connected. The replacement page is therefore
connected. Its outer boundary is the old \(S^3\), whose old
filling was the source four-ball.

## 2. The three fixed points and their orientations

Let the residual torus generators \(\lambda_1,\lambda_2\)
rotate \(u,v\), respectively, while fixing \(s\). Write their
degree-two characters as \(u_1,u_2\). The old invariant source
coordinates are \(x=u\), \(y=sv\); the old line coordinate is
\(t=v/u\). The old source four-ball has one torus fixed point
with tangent weights \(u_1,u_2\).

The new page has exactly three residual torus fixed points:
\[
 \begin{array}{c|c|c}
 \text{point}&\text{chart coordinates}
             &\text{principal delta-fibre weight}\\ \hline
 A&s=u=0,\ |v|=\rho\sqrt\epsilon&u_2\\
 B&u=v=0,\ |s|=\rho&0\\
 C&S=V=0,\ |U|=\sqrt\epsilon/\rho&-u_1 .
 \end{array}                                        \tag{PR.2}
\]
At all three points the local source tangent weights are
\(u_1,u_2\). Their orientations relative to those complex
coordinates are \(+,-,+\), respectively.

Here is the orientation calculation. Orient the orbit by
physical-circle-first from the complex threefold. The original
source page is then oriented by minus the orbit orientation
divided by \(d\log|t|\); increasing the suspension coordinate
decreases the line radius. At \(A\), the circle vector is the
positive \(v\)-phase vector, and
\(d\log{\cal R}_\epsilon\) points in the positive \(v\)-radial
direction. This gives the positive orientation in
\((x,y)=(u,sv)\). At \(B\), the circle vector is the negative
\(s\)-phase vector and the radius differential is the positive
\(s\)-radial direction; the page orientation is the negative
orientation in \((u,sv)\). At \(C\), the circle vector is the
negative \(U\)-phase vector and
\({\cal R}_\epsilon=\sqrt\epsilon/|U|\); the two negatives give
the positive orientation in \((SU,V)\). These computations use
the same common outer collar as the old source orientation.

## 3. The actual circle line and the relative characteristic numbers

The principal circle rotations at the three new fixed points
are listed in (PR.2). At the old fixed point the principal
rotation is \(u_2-u_1\), because \(t=v/u\).
For the convention \(x=[d\eta]\), with \(\eta(\delta)=1\),
the equivariant Euler-line restriction is minus this principal
rotation: the equivariant curvature is \(d\eta-\iota_\xi\eta\).
Thus its restrictions are
\[
       -u_2,\quad 0,\quad u_1
       \quad\text{and, on the old page,}\quad u_1-u_2.
                                                        \tag{PR.3}
\]
The line is the actual principal-circle line on the common
outer collar, so it glues over the closed oriented difference
\[
                  Z=P_{\rm new}\cup(-P_{\rm old}).
\]
The residual torus action also glues after the equivariant collar
isotopy above.

For clarity, the localization used here follows directly from
the oriented equivariant Thom maps. After inverting nonzero
torus characters, the complement of the finitely many fixed
points has zero equivariant cohomology: each of its finitely
many orbit-type strata has a proper stabilizer and is killed
by a character vanishing on that stabilizer. Excision and the
Thom map identify a class with its restrictions divided by the
oriented tangent Euler classes. Applying pushforward to these
Thom classes gives the sum of these fractions. This supplies
the needed formula for the compact glued manifold, including
its signs.

At \(A,B,C\) and the reversed old point the tangent Euler
classes are respectively
\[
                 u_1u_2,\quad -u_1u_2,\quad
                 u_1u_2,\quad -u_1u_2 .
\]
The first Pontryagin restriction at every point is
\(u_1^2+u_2^2\). Equations (PR.2)--(PR.3) therefore give
\[
 \begin{aligned}
 \langle p_1(TZ),[Z]\rangle&=0,\\
 \langle x^2,[Z]\rangle
  &=\frac{u_2^2+u_1^2-(u_1-u_2)^2}{u_1u_2}=2 .
 \end{aligned}                                      \tag{PR.4}
\]
Adding any common background equivariant line class to all
four restrictions leaves the second result unchanged: both
its quadratic and its linear cross terms cancel. Hence this
is the relative characteristic calculation for the actual
line, independent of its exterior frame.

The local graph-index combination is consequently
\[
                 \frac{12\langle x^2,[Z]\rangle
                            -\langle p_1(TZ),[Z]\rangle}{24}=1.
                                                        \tag{PR.5}
\]
This is a local page-replacement result. Its use in the global
return calculation still requires the actual angular trace and
the pullback to the doubled four-cycle, retaining its signed
gamma-sheet multiplicity. In particular the initial relative
coordinates remain
\[
       m=-k+6A=-\ell/4,\qquad n=-6A.
\]
No count of global sheets, or identification of a different
edge's \(4n\) cycle, is supplied merely by (PR.5).

The repair function, opposite-chart identity, line weights and
relative characteristic arithmetic are checked exactly in
code/part3_fourfold/nodal_page_repair.py and its JSON output.

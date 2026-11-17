# The actual nodal branch map for a nonfixed-edge flop

Working exact comparison, 17 November 2026. The chart maps below
identify the elementary branch modification and the image of a
source norm-shell page. They retain the subsequent page surgery
and its integral line comparison as unfinished.

## 1. Both small resolutions with the source and circle retained

Use the old small-resolution chart
\[
 (t,a,b),\qquad q=t a b .
\]
The old exceptional curve is \(a=b=0\), with coordinate \(t\).
Its opposite chart is
\[
 t_\infty=t^{-1},\qquad a_\infty=t a,\qquad
 b_\infty=t b,\qquad q=t_\infty a_\infty b_\infty .
\]
The physical circle acts by
\[
          (t,a,b)\longmapsto(\delta t,a,\delta^{-1}b).
                                                        \tag{NS.1}
\]
On \(t\in\mathbb C^*\), the actual source-line chart is
\[
 x=a,\qquad y=t b,\qquad V=t,\qquad q=xy .           \tag{NS.2}
\]
Thus \(V\) is the delta line coordinate and \(x,y\) are invariant
source coordinates. This map is invertible there:
\(t=V,\ a=x,\ b=y/V\).

The contraction to the common conifold is
\[
 (X,Y,Z,W)=(a,tb,b,ta),\qquad XY=ZW=q .
\]
In the opposite small resolution take
\[
 s'=b/a,\qquad u'=a,\qquad v'=ta .
\]
Its map to the conifold and its source base function are
\[
 (X,Y,Z,W)=(u',s'v',s'u',v'),\qquad
 q=s'u'v'.                                          \tag{NS.3}
\]
The circle acts by
\[
 (s',u',v')\longmapsto(\delta^{-1}s',u',\delta v').
\]
The new line chart \(v'\ne0\) has invariant source coordinates
\[
 x'=u',\qquad y'=s'v',\qquad V'=v'.
\]
Substituting (NS.2) proves the exact map on its common open set:
\[
                 x'=x,\qquad y'=y,\qquad V'=xV.
                                                        \tag{NS.4}
\]
The inverse local flop uses the inverse branch factor. Interchanging
the two source branches gives the analogous \(V'=yV\) formula.
These are actual small-resolution charts, with the fixed and free
circle strata retained.

## 2. The two branches and the global invertible extension

On the smooth source surface \(xy=q\), the local divisor of \(x\)
has order one on the branch \(x=0\), and order zero on the branch
\(y=0\). The local divisor of \(q\) has order one on each branch.
Consequently multiplying (NS.4) by a meromorphic base factor
\(q^j\) changes the two orders to
\[
                            (j+1,j).
\]
Their difference is always one.

This gives a precise obstruction to interpreting the selected
toric line chart as an invertible modification by a whole fibre
on the original nodal source. Its central \(I_1\) curve is one
irreducible divisor. A meromorphic isomorphism between two
invertible source line bundles, which is an isomorphism on every
nearby smooth fibre, has divisor supported on that irreducible
central curve. Its coefficients on the two analytic branches at
the node are therefore equal. The orders just calculated are
unequal. Thus (NS.4), with the selected toric frames, is not such
a whole-fibre meromorphic modification.

This does not prevent the generic Picard points from agreeing.
On a Tate fibre, replacing a line multiplier \(\alpha\) by
\(\alpha/q\) gives the exact generic line isomorphism \(V\mapsto
V/Z\). An invertible canonical extension of that generic Picard
point can be chosen by transporting the original line bundle.
Its local frame is then the original regular frame. It is the
additional requirement that this frame be the selected new toric
line coordinate which produces the unequal branch orders above.
The coordinate change required to pass between those frames is
exactly (NS.4), not an unspecified change of rigidification.

For an explicit Tate-chain version, write \(Z=q^j x_j\) in the
node chart \(x_jy_j=q\). Under \(V'=V/Z\), the factor is
\[
                        q^{-j}x_j^{-1}.
\]
Removing the whole-fibre factor \(q^{-j}\) leaves \(x_j^{-1}\),
whose two branch orders are \((-1,0)\). In the adjacent chart the
source transition is \(x_{j+1}=y_j^{-1}\). This records both
branches and the exact residual unit/pole at their overlap.

## 3. The common blowup and the old norm-shell page

In the source blowup chart \(y=xz\), the common blowup of the
old line chart along its nodal line fibre has coordinates
\((x,z,t)\), with \(t\in\mathbb C^*\). Its maps to the old
source-line chart and to the new resolution are respectively
\[
 (x,z,t)\longmapsto(x,y=xz,V=t),
\]
\[
 (x,z,t)\longmapsto
       (s'=z/t,\ u'=x,\ v'=tx).                    \tag{NS.5}
\]
Substitution verifies \(q=x^2z=s'u'v'\) and the common conifold
coordinates. The other blowup chart gives the reciprocal formula,
so the exceptional curve is the full \(\mathbb P^1_z\).

Choose the original source Hermitian norm shell on this regular
line chart. On its exceptional curve the norm fixes
\(|t|=\rho>0\), after retaining its bounded metric factor.
Equation (NS.5) sends that curve into the new exceptional curve
\(u'=v'=0\), with coordinate \(s'=z/t\). In the orbit by (NS.1),
the image is the interval parametrized by
\[
                           |s'|=|z|/\rho .
\]
The two endpoints \(z=0,\infty\) map to the two endpoints of the
new exceptional curve, on the surviving fixed locus. The
angular coordinate of \(z\) is removed by the delta orbit.
Hence the pushed-forward source blowup is not an embedded
replacement page: its exceptional sphere has a one-dimensional
orbit image. This failure is established by (NS.5), rather than
inferred from a numerical characteristic comparison.

An actual new page must replace this collapsed piece and specify
the Euler-line gluing on its new boundary. The local charts
determine the branch factor and the interval endpoints, but
they do not yet determine the integral normal-product change
between the exteriors of the three cusp curves. That is the
remaining map in the cross-edge return calculation.

All polynomial chart identities and branch-order differences are
checked in code/part3_fourfold/nodal_shear_page.py and its JSON
certificate.

# The exact local characteristic comparison at the two-torsion strata

We use the actual four fixed-surface patches and four isolated points
constructed in part3_e6_selected_infinity_mu2_fixed_working.md. The
calculation below compares each resolved patch with its original
orbifold patch through their literal common boundary. It does not
assign the global source-surface terms or the return.

## The fixed-surface and normal-line boundary maps

At a node use the actual coordinates \((\chi,\zeta,\ell,u)\) of
the preceding note. The involution is
\((\chi,\zeta,\ell,u)\mapsto(-\chi,-\zeta,-\ell,u)\).
The physical weights are \((0,0,w,-w)\). Its original fixed
surface is \(F_0=\mathbb C^2_{\chi,\zeta}/\{\pm1\}\).
The resolved fixed surface has charts \((\rho,z)\) and
\((\rho',z')\), glued by
\[
 \rho'=\rho z^2,\qquad z'=z^{-1}.
\]
Its exact morphism to \(F_0\) sends these charts to the invariant
coordinates \((x,y,t)=(\chi^2,\chi\zeta,\zeta^2)\):
\[
 (x,y,t)=(\rho,\rho z,\rho z^2),\qquad
 (x,y,t)=(\rho' z'^2,\rho'z',\rho'),\qquad xt=y^2.
\tag{MR2a}
\]
The zero section \(C\) is contracted to the origin. The restriction
away from \(C\) is a biholomorphism. Indeed a point with \(x\ne0\)
has the unique inverse \(\rho=x,z=y/x\), and a point with \(t\ne0\)
has the other inverse. These opens cover the complement of the origin.

Take the original orbifold ball
\(|\chi|^2+|\zeta|^2\le r^2\). Its inverse image has the
literal boundary
\[
 |\rho|(1+|z|^2)=r^2,
\tag{MR2b}
\]
and the corresponding expression on the second chart. Thus MR2a
identifies the two boundary three-manifolds with their complex outward
orientations. The resolved domain is the disc bundle of
\(\mathcal O_C(-2)\); the common boundary is the circle bundle
with clutch exponent \(-2\), identified by MR2a with
\(S^3/\{\pm1\}\).

Let \(L\) be the odd physical normal line on the resolved fixed
surface, with coordinate \(a=\ell/\chi\) on the first chart.
Its second coordinate is \(a'=\ell/\zeta=a/z\), so
\(L|_C=\mathcal O_C(1)\). The whole boundary line morphism to
the original odd-character orbifold line is
\[
 a\longmapsto\ell=\chi a,
\tag{MR2c}
\]
with the analogous \(\zeta a'\) expression on the second chart.
Changing the local square root \(\chi\) changes \(\ell\) by
its actual odd stabilizer action. Hence MR2c is a well-defined
holomorphic line-bundle isomorphism on the common punctured surface.
The other physical normal line has the unchanged coordinate \(u\).
The order-two boundary character of \(L\) is retained.

For the positive-weight line minus the negative-weight line, write
\(D=c_1(L_+)-c_1(L_-)\). The actual weights give
\(D\cdot C=w\). The integral intersection matrix of the resolved
disc bundle, in the complex zero-section basis, is the one-by-one
matrix \([-2]\). More explicitly, the map
\(H_2(N;\mathbb Z)\to H_2(N,\partial N;\mathbb Z)\)
sends the zero section to \(-2\) times the oriented fibre-disc
generator, whose intersection with the zero section is one. The
boundary cellular complex has differentials \(d_2=[2]\),
\(d_3=d_1=0\), so the restriction of \(D\) has class
\(w\bmod2\) in \(H^2(\partial N;\mathbb Z)=\mathbb Z/2\).
It is the nontrivial class, as also given by MR2c.

The original odd-character orbifold line has its flat sign connection
on the ball. Match connections through MR2c on the common boundary.
The rational relative lift of \(D\) is obtained from the displayed
integral map by solving \(-2q=w\), which gives \(q=-w/2\).
Consequently the exact relative square difference is
\[
 \Delta(D^2)=q w=-\frac12.
\tag{MR2d}
\]
This computation retains both the integral matrix and its nontrivial
boundary torsion; it selects no integer from a residue.

## The tangent comparison with the same boundary frame

The original form \(d\chi\wedge d\zeta\) is invariant under the
involution. Under MR2a it becomes
\(\tfrac12 d\rho\wedge dz\) on the first chart and
\(-\tfrac12 d\rho'\wedge dz'\) on the second. Thus it extends
to a nowhere-zero canonical frame on the entire resolved domain.
The two determinant frames agree under the actual boundary map. The
relative difference of their first-Chern squares is therefore zero.

The second-Chern difference can be counted with a specific common
boundary vector field. Fix a real number \(0<e<1\) and use
\[
 (1+e)\chi\frac{\partial}{\partial\chi}
 +(1-e)\zeta\frac{\partial}{\partial\zeta}.
\tag{MR2e}
\]
It is invariant and outward pointing on the boundary of the ball.
Its only orbifold zero has complex local index one and stabilizer
order two, and therefore orbifold index \(1/2\). On the first
resolved chart the same vector field is
\[
 2(1+e)\rho\frac{\partial}{\partial\rho}
       -2e z\frac{\partial}{\partial z},
\]
and on the second it is
\[
 2(1-e)\rho'\frac{\partial}{\partial\rho'}
       +2e z'\frac{\partial}{\partial z'}.
\]
There is one nondegenerate zero in each chart, at the two distinct
ends of \(C\). Each has real oriented index \(+1\), because
the real determinant of an invertible complex derivative is the
positive squared modulus of its complex determinant. The two fields
are literally the same field on MR2b. Thus their relative top-Chern
difference is \(2-1/2=3/2\). The identity
\(p_1=c_1^2-2c_2\), obtained by writing the two complex Chern roots,
now gives
\[
 \Delta p_1(TF)=-3.
\tag{MR2f}
\]
This also supplies the sign of the local tangent contribution with
the stated complex boundary orientation.

## The surface correction and the isolated point

For the actual normal weights \(+1,-1\), expansion of the SZ.57
fixed-surface integrand gives exactly
\[
 R_u(F)=\frac1{24}\int_F\bigl(p_1(TF)-3D^2\bigr).
\tag{MR2g}
\]
Here the positive-hyperplane variable and the normal roots are the
ones retained in that formula. To check the expansion directly, the
numerator is
\(2u^3-2(a-b)u^2-(p_1(TF)+a^2+b^2)u\), and the denominator is
\(24(u+a)(-u+b)\). The coefficient of \(u^{-1}\) is
\((p_1(TF)-3(a-b)^2)/24\), proving MR2g without a change of
generator. The version with the two actual line weights interchanged
has the same expression because \(D\) changes sign.

Substituting MR2d and MR2f yields the exact surface correction
\[
 \Delta R_u(F)=\frac{-3-3(-1/2)}{24}=-\frac1{16}.
\]
The isolated point in the same resolved node chart has weights
\((2w,-w,-w,-w)\), and the preceding independently audited
calculation gives \(R_u=1/16\). Their sum is zero. Thus replacing
the original orbifold node by its actual smooth quotient resolution
changes this complete local weighted characteristic contribution by
exactly zero. All four node comparisons use these same displayed
boundary maps, so their total change is zero as well.

The full chord, line and period arrows remain part of this comparison.
On the \(\chi\)-pivot chart the source map is
\(z_{\rm new}=A_bz+B_bau\), with line coordinates
\(a_{\rm new}=\mathcal C^s a\),
\(u_{\rm new}=\mathcal C^{-s}u\). Substituting
\(\ell=\chi a\) gives exactly
\(\zeta_{\rm new}=A_b\zeta+B_b\ell u\) and the original
line arrow. The \(\gamma^{-1}B\) phases in MF2g commute with
this same identity. On the fixed surface the quadratic term vanishes,
and the linear normal factors are precisely the complete retained
units; no factor is replaced by its central value. The original
marked-volume coefficient also pulls back by these very maps.
Connections on the two sides can therefore be matched through these
specific bundle isomorphisms on the collar, and their transgression
terms cancel there. The zero local correction is preserved under the
actual generator and boundary-orientation transport used in the global
ledger. The global orbifold fixed-surface integrals and reference caps
still require their own complete calculation.

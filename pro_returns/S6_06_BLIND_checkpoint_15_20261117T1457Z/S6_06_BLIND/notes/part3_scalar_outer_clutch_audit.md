# Exact scalar outer-normal clutch and the earlier simultaneous-product premise

Independent audit by fourfold, 17 November 2026. This note keeps the
primitive positive scalar loop and the actual forward arrow of K10/K22.
It records the precise map missing from the earlier K25/K29 argument.
It does not alter an archived proof or infer a global return solely from
a normal determinant.

## SOC.1. Literal periods and the closed scalar charts

The physical line coordinate is \(V\). The actual cusp periods are
\[
 h:(Z,V,q)\longmapsto(\kappa qZ,\alpha V,q),\qquad
 B:(Z,V,q)\longmapsto(gZ,q\eta V,q),\qquad
 \eta=\lambda\beta.
\]
Here \(\kappa,\alpha,g,\beta\) are independent of the scalar parameter.
For the primitive K22 cap-to-ordinary convention the forward arrow is
\(R_{\rm ord}(Z,V)=(Z,q^{-1}V)\). Reindexing by the actual period
\(B\) leaves \(E_\lambda(Z,V)=(gZ,\eta V)\). On a cut scalar
interval the maps
\[
 C_\tau(Z,V)=(A_\tau Z,D_\tau V),\qquad
 A_\tau=e^{-\chi\log g},\quad D_\tau=e^{-\chi\log\eta}
\]
have \(C_{\rm end}E_\lambda=1\) on full collars. The same actual
logarithms and cutoff as SCN.1 retain every spatial and parameter
derivative. They commute with the full periods and the physical delta
circle, preserve \(q\), and act on the two vertex charts by
\[
 (a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u,v,w)\mapsto(ADu,D^{-1}v,A^{-1}w).
\]
Substitution in all three curve transition rows leaves their complete
coefficients unchanged. Thus in these genuinely closed charts the
primitive scalar unit windings remain
\[
 \operatorname{wind}(\kappa,\alpha,g,\eta)=(0,0,0,1).
 \tag{SOC.1}
\]
For a positive degree-\(M\) pullback they are \((0,0,0,M)\).
The pullback atlas is explicit. On its \(j\)-th cut sheet, write
\(u=j+\tau\), \(0\le j<M\), and put
\[
 C^{(M)}_{j+\tau}=C^{(1)}_\tau E_{\lambda(\tau)}^{-j}.
\]
At the next seam both collar expressions equal
\(E_\lambda^{-(j+1)}\), with all derivatives. The last cancels the
forward arrow \(q^{-M}\) after the actual reindexing \(B^M\).
This is the pullback of the original family, not a separately chosen
normal product. For negative \(M\), reverse the parameter of the
positive \(|M|\)-fold pullback; all the displayed windings acquire
the same sign. No change from an endpoint-to-initial closing map to a
forward map is implicit in this calculation.

## SOC.2. The outer fixed-normal map is not the inner common cap gauge

At the second vertex the actual native fixed-curve product uses
\[
 z_0=\kappa w,\qquad N_{0,-}=\alpha v,\qquad
 N_{0,+}=(\kappa\alpha)^{-1}u.
 \tag{SOC.2}
\]
These are exactly the \(C_0\) row of GF.11. On that same physical
fixed branch, the native \(C_1\) star has coordinates
\[
 z_1=g w,\qquad N_{1,-}=\eta v,\qquad
 N_{1,+}=(g\eta)^{-1}u.
 \tag{SOC.3}
\]
Indeed its native star is
\((\eta v,g w,(g\eta)^{-1}u)\); the middle coordinate is the
zero-weight tangent to this fixed branch, while the first and last
have physical weights \(-1,+1\). Therefore the literal map is
\[
 z_1=(g/\kappa)z_0,\qquad
 \begin{pmatrix}N_{1,-}\\N_{1,+}\end{pmatrix}
 =\begin{pmatrix}
 \eta/\alpha&0\\0&\kappa\alpha/(g\eta)
 \end{pmatrix}
 \begin{pmatrix}N_{0,-}\\N_{0,+}\end{pmatrix}.
 \tag{SOC.4}
\]
All factors here are the original functions. Relative to their fixed
reference values, the scalar phase part of the normal matrix is
\(\operatorname{diag}(\lambda/\lambda_*,\lambda_*/\lambda)\).
The canonical positive-weight complex normal structure conjugates
the negative first line. Its determinant transition is consequently
\[
 \det_+\Gamma
 =\frac{\kappa}{g}\frac{\alpha}{\overline\alpha}
                     \frac{\overline\eta}{\eta}.
 \tag{SOC.5}
\]
For the fixed-source scalar loop its winding is exactly \(-2\), or
\(-2M\) on the degree-\(M\) pullback. At the other outer vertex the
two products use the same first-vertex coordinates: the fixed branch
has tangent \(b\), negative normal \(a\), and positive normal \(c\).
The corresponding comparison is the identity. Thus the two outer
branch determinant comparisons have windings \(0\) and \(-2M\).

This is distinct data on explicitly different overlaps from the equal
inner charged-cap gauges in K25. Those inner gauges can be removed by
their one common cap frame change; that operation has not provided a
frame change on the two outer fixed branches matching (SOC.4). A
nonvanishing determinant homotopy on the fixed annulus, preserving the
specified endpoint products, would have the same parameter winding at
both ends. Equations (SOC.4)--(SOC.5) prove that such a homotopy does
not exist for \(M\ne0\).

In particular the K25 sentence which makes the determinant class of
the additional fixed-locus sphere boundary a pullback from its
three-dimensional parameter-free base has not carried this outer
clutch. Its asserted \(b^2=0\) does not follow from the inner common
gauge calculation. The needed correction is the actual line obtained
by adjoining (SOC.4) to the already written charged-cap maps, with
their oriented base cycle retained.

## SOC.3. Direct obstruction to K29's stated marked equivariant product

The full proof of PO.5--PO.11 applies to the closed charts in SOC.1;
its argument uses the actual three rows and arbitrary smooth
equivariant normal derivatives, not a diagonal-normal assumption.
Here is its scalar specialization in full.

At the first vertex write the tangent derivative factors on the
labelled \(C_2,C_1\) axes as \(A,C\), and at the second as \(U,V\).
Their parameter windings are integers \(a_*,c_*,u_*,v_*\).
For a pointed nonfixed curve whose actual coordinate transition is
\(z_-=\xi^{-1}/z_+\), an orientation-preserving equivariant product
has \(F(z_+)/z_+\) rotation-invariant. Its winding is constant along
the orbit cylinder. Comparing its two endpoint derivative limits
gives \(\operatorname{wind}P+\operatorname{wind}Q
=\operatorname{wind}\xi\). The actual \(C_2,C_1\) transitions
therefore force
\[
 a_*+u_*=0,\qquad c_*+v_*=M.
 \tag{SOC.6}
\]

On \(C_0\), the canonical positive-weight normal coordinates at the
first and second vertices are \((\overline a,c)\) and
\((\overline v,u)\). The actual normal transition is
\[
 \begin{pmatrix}\overline v\\u\end{pmatrix}
 =\begin{pmatrix}
 \overline\alpha^{-1}\overline b&0\\0&\kappa\alpha b
 \end{pmatrix}
 \begin{pmatrix}\overline a\\c\end{pmatrix},
\]
with determinant \(\kappa(\alpha/\overline\alpha)|b|^2\).
In the fixed reference product this determinant has constant phase.
An arbitrary equivariant normal derivative is an invertible complex
two-by-two map in this structure. Its determinant winding is constant
as its source point contracts to either vertex. Consequently the
single bundle-map square gives
\[
 (-v_*+u_*)+\operatorname{wind}\kappa
   +2\operatorname{wind}\alpha-(-a_*+c_*)=0.
 \tag{SOC.7}
\]
Substituting (SOC.6) and the literal scalar windings reduces the
left-hand side to \(-M\). For the positive primitive loop it is
\(-1\), a contradiction. Thus the actual labelled three-curve
plumbing admits no periodic smooth delta-equivariant product carrying
the labelled curves, vertices and complex curve orientations to
constant copies. A product connection with identity return on the
entire marked neighbourhood would supply precisely that forbidden
product.

This locates the failure of the premise asserted at K29 Section3.
The subsequent use of that premise to put the original scalar
variation in the form \(\operatorname{diag}(v,0,0)\), and to make
both nonfixed relative right integers zero, is unsupported by that
construction. The independently established cellular groups,
reciprocal-section basis maps, variation symmetry, and frame-change
formula remain their separate exact statements. The scalar fixed-star
product and its individual pair are also separate maps and are not
contradicted by the marked three-curve obstruction.

## SOC.4. Retained correction target

The explicit native scalar \(C_1\) calculation in SCN retains the
same forward arrow, period reindexing and actual native star as
(SOC.1)--(SOC.4). Its single free pair is \((1,-1)\), obtained from
an actual relative square. The comparison still requiring the full
oriented map is the closed additional fixed-normal base in the K25
master bordism, carrying the one nonzero outer determinant clutch
(SOC.5). No global characteristic number is assigned in this audit
from the determinant winding alone.

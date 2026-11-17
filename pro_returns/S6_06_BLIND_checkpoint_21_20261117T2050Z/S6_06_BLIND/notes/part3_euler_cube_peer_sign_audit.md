# Independent sign audit at the physical Hopf meridian

17 November 2026. This records exact local arrows needed by P3K.66.
The collar and connection computations below are verified. The identification
with the meridian-one convention of F56/K42 is being audited separately;
no known characteristic value is used to choose an orientation.

## PS.1. The two oriented quotient spheres

At the first Cox-chart origin write
\[
 q_H=c_0+j\overline{c_1}.
\]
In the original complex coordinate order \((c_0,c_1)\), this is the
orientation-preserving real map to \((1,i,j,k)\). The physical circle is
\(q_H\mapsto q_He^{-i\theta}\). At \(q_H=1\) its tangent is \(-i\).
For \(z=q_H i q_H^{-1}\), the two horizontal derivatives are
\(j\mapsto-2k\) and \(k\mapsto2j\). Thus, with the outward orientation
on the unit sphere in \(\operatorname{Im}\mathbb H\),
\[
 [S^3_H]=-[S^1_\delta][S^2_z].
\]
The right-complex coordinates are \((c_0,d)\), \(d=\overline{c_1}\).
Their real complex basis \((1,i,j,ji)=(1,i,j,-k)\) reverses quaternion
orientation. In the projective chart \(d/c_0=x+iy\), the Hopf derivative
is \((\partial_x,\partial_y)\mapsto(-2k,-2j)\). Consequently
\[
 [\mathbf P^1_{\mathrm{right}}]=-[S^2_z].
\]

Let \(\alpha\) denote the Maurer/contact form normalized to value one
on the positive right phase. Its pullback to the unit section
\((1+j(x+iy))/\sqrt{1+x^2+y^2}\) is
\((x\,dy-y\,dx)/(1+x^2+y^2)\). Hence its curvature has integral one
on the right-complex projective orientation, and minus one on \(S^2_z\).
The physical principal connection is \(A=-\alpha\). The nonzero-vector
line with the physical positive scalar representation has
\[
 c_1(\mathcal L_\delta)=-dA,\qquad
 \int_{S^2_z}dA=1,\qquad
 \int_{S^2_z}c_1(\mathcal L_\delta)=-1,
 \qquad
 \int_{\mathbf P^1_{\mathrm{right}}}c_1(\mathcal L_\delta)=1.
\]
Here the Chern sign follows directly from a local unitary connection
\(\nabla=d+2\pi iA\): \(c_1=(i/2\pi)F_\nabla=-dA\).

The radial factor must also be retained. Since
\(\Omega_{\mathbb C^2}=dr\wedge\Omega_{S^3_H}\), moving the circle
factor to the front gives
\[
 \Omega_{\mathbb C^2}=d\delta\wedge dr\wedge\Omega_{S^2_z}.
\]
Therefore the outward circle-first normal quotient meridian, for the
complex orientation on the fixed curve, is \(S^2_z\). The right-complex
projective sphere is its opposite. The names “positive meridian” and
“physical line” cannot identify these two orientations without the
actual accompanying normal/base orientation arrow.

## PS.2. The full Cartier-to-Cox coefficient arrow

F56 constructs its positive-weight spinor as
\[
 E=\mathcal O(D_+)\oplus\mathcal O(-D_-),
 \qquad (p,q)=(\overline{c_0},c_1).
\]
K42 uses \(x=s-\rho\), \(y=s+\rho\), \(Z=x/y\), with the actual
Cartier vector frames \((1/x,y)\). Its coefficient map to the
dual-tautological/tautological frames is \(\operatorname{diag}(1/y,y)\).
After positive Hermitian normalization, writing \(Y=y/|y|\), this is
\[
 (\overline{c_0},c_1)
       =\operatorname{diag}(\overline Y,Y)(a,b).
\]
It follows literally that
\[
 (c_0,\overline{c_1})
       =\operatorname{diag}(Y,\overline Y)(\overline a,\overline b).
\]
Left multiplication by the first normalized quaternion gives
\[
 q_H^{\mathrm{right\ coefficients}}
   =g(x,y)\overline{(a,b)},\qquad
 g(x,y)=\frac1{\sqrt{|x|^2+|y|^2}}
     \begin{pmatrix}y&-\overline x\\x&\overline y\end{pmatrix}.
\]
Thus the same full-unit matrix \(g\) appearing in K42 is retained,
but its coefficient arrow is anti-linear. The currently written K42
arrow \(gS(a,b)\), with \(S\) the linear summand swap, differs by the
constant anti-linear swap \(S\circ\text{conjugation}\).

For adjoint coordinates
\(\gamma=|a|^2-|b|^2\) and \(\ell=\overline a b\), the linear swap
has action \((\gamma,\ell)\mapsto(-\gamma,\overline\ell)\), of real
determinant \(+1\). The anti-linear swap has action
\((\gamma,\ell)\mapsto(-\gamma,\ell)\), of determinant \(-1\).
The latter reverses the projective meridian. This is also forced by
the circle action: \(g\overline{e^{i\theta}(a,b)}
=e^{-i\theta}g\overline{(a,b)}\), whereas the linear swap retains
the positive scalar. A dual/Hermitian interpretation must include
this arrow; the displayed Cartier frames are vector frames.

## PS.2a. The literal F9 source-normal and physical-line map

P3F.9 removes the remaining ambiguity in the local height convention.
Its first small-resolution chart is \((x,v,z)\), with
\(u=xz\), \(y=vz\), physical weights \(0,-1,+1\), and increasing
quotient height \(b=(|z|^2-|v|^2)/2\). The fixed curve is
\(v=z=0\). Thus its ordered Cox normal is \((c_0,c_1)=(v,z)\), its
source complex normal is \(y=vz\), and its positive-weight spinor is
\((\overline v,z)\). The physical circle acts by a common positive
scalar on that spinor. The positive projective complex orientation of
this spinor equals the actual circle-first normal meridian orientation.
Indeed, in coordinates \((b,\operatorname{Re}y,\operatorname{Im}y)\)
the outward projective sphere has the opposite of the raw orientation,
and F9/F56's physical normal orientation is exactly that opposite raw
orientation. To check the sign at one point, take \(v=1,z=0\). Then
\(b<0\), the projective coordinate is \(z/\overline v\), and
\(y=|v|^2(z/\overline v)\) has the same complex orientation. The
outward sphere orientation in the raw ordered three-plane at its
negative \(b\)-axis is minus this complex orientation. This proves the
stated opposite sign. Equivalently this is the explicit quaternion computation
in PS.1.

The physical principal circle over this projective sphere is the unit
circle in the tautological line. Therefore its nonzero-vector line is
\(\mathcal O(-1)\), and its Chern class has integral \(-1\) on the
actual outward meridian. The meridian-one Thom line is its dual
\(\mathcal O(1)\). The duality arrow is explicit: for the invariant
Hermitian metric it sends a nonzero vector \(v\) to the functional
\(w\mapsto\langle v,w\rangle/\langle v,v\rangle\), with the inner
product linear in its second argument. It conjugates the physical
circle character and retains the base point. On a regular source page
this gives the literal line map to \(M^{-1}\), since the original
nonzero-vector line there is \(M\).

Thus the source-page comparison and the meridian-one comparison are
related by an actual Hermitian dual map. With the latter convention the
page restriction is \(-c_1(M)\), and the real principal curvature
represents \(+dA\). The assertion in EC.1 that the same convention has
both meridian value one and page restriction \(+c_1(M)\) omits that
dual arrow.

## PS.3. The independent collar sign

In the boundary orientation
\(\Omega_B=d\alpha\wedge du\wedge dv\wedge d\gamma\wedge d\theta\),
retain the exact forms from EC.4:
\[
 \beta=-n\{du+(\alpha-6\theta)dv\},\quad
 F=d\alpha\wedge d\gamma+n\,d\alpha\wedge dv,
 \quad d\beta=-n\,d\alpha\wedge dv+6n\,d\theta\wedge dv.
\]
They obey \(F^2=(d\beta)^2=0\) and
\(\beta Fd\beta=6n^2\Omega_B\). Hence
\[
 3\int_0^1\beta(F+s\,d\beta)^2ds=18n^2\Omega_B.
\]
The actual outward collar has its cutoff decreasing from one to zero,
so its contribution in the declared source-first auxiliary orientation
is \(-18n^2\). This computation does not identify that orientation
with any unstated Hopf-meridian convention.

## PS.4. A global anti-linear cap map

The missing arrow extends over the actual two cap products. This can
be seen without choosing a reflection separately in each chart. For
every \(SU(2)\) transition matrix write
\[
 g=\begin{pmatrix}a&-\overline b\\b&\overline a\end{pmatrix},
 \qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Then \(\overline g=JgJ^{-1}\). Complex conjugation is the canonical
anti-linear bundle map \(C:E\longrightarrow\overline E\), and \(J\)
is a complex-linear bundle isomorphism from \(E\) to \(\overline E\).
Their quotient is the globally defined quaternionic anti-linear map
\[
 Q=J^{-1}C:E\longrightarrow E,
 \qquad Q(a,b)=(\overline b,-\overline a).
\]
It commutes with every \(SU(2)\) transition, has \(Q^2=-1\), preserves
the real four-dimensional orientation, and satisfies
\(Q(e^{i\theta}v)=e^{-i\theta}Q(v)\).

For a unit vector \(v\), the vectors \(v,Qv\) are an orthonormal
basis. Their rank-one Hermitian projections sum to the identity.
Consequently the projectivization of \(Q\) acts by minus the identity
on the traceless Hermitian three-plane. This is the actual fibrewise
antipodal map of \(S(\operatorname{ad}E)\); its normal three-dimensional
determinant and its sphere degree are both \(-1\). It extends to the
normal three-disc by \(w\mapsto-w\).

In the inner cap \(D^4\), use the actual Cartier frame; in the outer
cap \(D^3\times S^1\), use the actual Cox frame. The same formula for
\(Q\) is used in both. Since it commutes with the transition on the
overlap, these extensions glue through \(W\), retaining the complete
matrix \(g(x,y)\) and its parameter dependence. The orientation-
preserving factor \(J\) gives the corresponding map to the conjugate
spinor. The literal two cap maps on their sphere boundaries are thus
identity on the cap base times this projective map, with the specified
clutch conjugation. No homotopy removing the degree of \(g\) is used.

The determinant trivialization from the Cartier ratio is retained.
Any extending scalar unit used in the original coefficient maps is
sent to its conjugate by \(C\); the inverse circle character is retained
at the same time. Its normal adjoint action is unchanged. Thus this
construction also carries the actual scalar boundary gauges, rather
than discarding a winding. The associated complex line is dualized by
the exact anti-equivariance of \(Q\).

## PS.5. The oriented cap pair under that exact map

Let \(B\) be the closed normal sphere bundle obtained from the original
two cap products, and let \(B'\) be the conjugated cap model just
constructed, with its conjugate projective orientation. The above
map \(\Psi:B\longrightarrow B'\) is fibrewise degree \(-1\) over the
unchanged oriented four-dimensional base. Its associated-line map is
the Hermitian dual map, so
\[
 \deg\Psi=-1,\qquad \Psi^*x'=-x,
 \qquad \Psi^*p_1(TB')=p_1(TB).
\]
The last equality is naturality under the displayed diffeomorphism;
it does not depend on orienting the normal bundle. Direct integration
therefore gives
\[
 \int_{B'}(x')^3=\int_Bx^3,
 \qquad
 \int_{B'}p_1(TB')x'=\int_Bp_1(TB)x.
\]
The two minus signs in each equality are respectively the degree of
\(\Psi\) and the dual-line factor. Moreover \(\overline g=JgJ^{-1}\)
shows that the relative second Chern number of the spinor remains
\(-1\) and its adjoint Pontryagin number remains \(4\), with the
base orientation of SP.15 unchanged.

These are direct statements about the exact conjugated cap models.
Their application to the physical mapping-torus class still requires
the actual normal/meridian and associated-circle dictionary in PS.1:
the underlying nonzero-vector line of the physical circle has value
\(-1\) on the outward circle-first meridian for the complex fixed-base
orientation. This sign cannot be supplied by a declaration that the
same line has meridian value one. Root and checks retain the global
Jin and period arrow as the remaining separate comparison.

For the meridian-one Thom line specifically, PS.2a supplies the missing
dual map on both caps. A retained scalar boundary gauge is inverted
pointwise; its extending gauge on the outer \(D^3\times S^1\) is
inverted by the same formula, and the inner \(S^3\) has no additional
gauge class. The normal clutch remains the conjugate of the same
\(g(x,y)\), so its relative Pontryagin number remains \(4\). On the
normal sphere bundle with that line and its physical outward meridian,
\(\pi_*x=1\), \(4x^2=\pi^*p_1(\nu)\), and the resulting pair is
\((1,4)\). On the inner surgery cap the same meridian-one line is
exactly SP.5's oriented normal Euler class. Its previously constructed
Seifert four-cycle therefore retains pair \((5,-4)\). These two
computations give \((6,0)\) after the stated physical-to-Jin parameter
reversal for this meridian-one line. This conclusion uses the explicit
duality and normal arrows, not the prior value of that pair. Identifying
this convention with the run's physical Hopf-lift convention is the
remaining global F22 comparison being checked by root and checks.

## PS.6. The physical product-factor dictionary submitted for audit

The exact exterior of the fixed curve is
\(E=D^3_y\times S^3_{q_H}\), with its complex orientation. Here the
orientation of the \(h\)-sphere bounding \(D^3_y\) is opposite the
complex orientation of the fixed curve. Therefore the actual complex
six-sphere is
\[
 X=-\partial(D^3_y\times D^4_{q_H}).
\]
This is an identity of the two oriented product pieces: on the exterior
the boundary sign of \(D^3_y\times D^4_{q_H}\) is negative, while on
the fixed tube the displayed outer minus agrees with the complex
fixed-curve orientation.

The physical Hopf circle and quotient \(S^2_z\) give the circle-first
orientation \(S^3_u=-S^3_{q_H}\). Consequently the same actual
six-sphere is \(\partial(D^4_u\times D^3_y)\), including both pieces.
The associated physical nonzero-vector line is \(M\), with Chern
number \(-1\) on this \(S^2_z\). To use F22's convention that its
generator is positive, orient the factor \(S^2_z\) oppositely and
orient the doubled \(S^3_y\) oppositely as well. The orientation of
the six-dimensional quotient product is unchanged. Its circle-first
Hopf \(S^3_u\) also reverses. Thus both four-ball factors in
\[
 (D^4_u\times S^3_y)\cup_{\widetilde f}
                      (S^3_u\times D^4_y)
\]
reverse orientation, and their eight-dimensional product orientation
is unchanged. The underlying maps and circle action are the same;
this is the full factor-orientation relabelling, rather than a choice
of a sign from a previously calculated invariant.

Under this physical-line dictionary, the class entering the characteristic
integrals is \(x_{\rm phys}=c_1(M)=-x_{\rm Thom}\), where
\(x_{\rm Thom}\) is SP.5's outward-meridian-one class. The six-dimensional
mapping-torus orientation is unchanged. Thus the actual oriented odd
pair changes by minus:
\[
 (k,\ell)_{\rm phys}=-(k,\ell)_{\rm Thom}.
\]
This is separate from PS.5's *conjugated cap-model* comparison, which
reverses both the normal projective orientation and the line. The
physical quotient orientation in the present paragraph is fixed by
the original complex threefold and the physical circle.

The displayed F22 product-factor identification is submitted to root
and checks for independent audit. No active source-loop statement or
numerical result is changed before that audit. In particular EC.1
currently combines the physical-line curvature convention with the
meridian-one K42 initial pair; these are the two classes distinguished
by the explicit maps above.

## PS.7. Precise status of the affected arguments

* The original local Cox charts, source and Cartier divisors, the
  relative Chern clutch matrix \(g\), its degree and \(c_2=-1\), and
  \(p_1(\operatorname{ad}E)=4\) remain established.
* The literal positive-spinor-to-Cox arrow is anti-linear. The written
  SP.9/10 linear coefficient arrow must be replaced by PS.2/4, with
  the dual circle character retained.
* The two cap extensions and their meridian-one oriented pair
  \((6,0)\) are preserved by the exact normal/dual arrows in PS.5.
  This does not identify that line with the physical page line \(M\).
* The normal-sphere correction has index zero with either line sign;
  this zero input is unaffected.
* K6's literal source-page restriction of the nonzero-vector line is
  \(M\). The meridian-one Thom line restricts to \(M^{-1}\). Any
  K6/K7/F56 statement using both of these as the same oriented line
  must retain the Hermitian dual arrow instead.
* F22's abstract transfer construction remains its specified complex-line
  construction. Its use for this physical return needs the complete
  factor dictionary of PS.6; the isolated word “Euler” does not supply
  that dictionary.
* EC's exterior-form/collar computation is established in its declared
  auxiliary orientation. Its combination with the K42 initial pair is
  not yet promoted by this audit.

The pre-correction K42/F56 proof, code, output and QA are preserved
verbatim in `records/k42_pre_antilinear_arrow/`, with SHA256 manifest.
No active K42/F56 file was changed in this audit.

The exact certificate is
`code/part3_fourfold/euler_cube_peer_sign.py` and its JSON/output files.
The unresolved global junction is precisely the anti-linear/dual
Cartier-to-Cox and meridian convention in PS.2, not the exterior-form
calculation in PS.3.

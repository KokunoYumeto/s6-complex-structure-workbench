# Infinity collision: relative circle-quotient excision

This is the complete working proof following IF.1--12 and IF.8a in
notes/part3_source_infinity_fourfold_working.md. It retains the actual
source, Cartier line, cap and physical circle maps. The original global
source-coordinate/root endpoint dictionary remains explicit in IF.1--6.
No eight-dimensional signature or unproved spin extension is substituted
for the circle-quotient comparison.

Root has passed the complete map, normal-line, orientation, finite-chart
Stokes and transfer audit, including the final self-contained IE.7
calculation. The combined result is reserved for K57 after checkpoint14;
no numbered manuscript export has yet been made. The earlier audit-draft
status is retained here as its history rather than a remaining scope gap.

## IE.1. Two actual collision fillings and their boundary families

Choose a small closed source-base disc \(U\) around \(t=0\), disjoint
from the selected value and the cap. Its boundary annulus contains no
singular source fibre for any small \(\epsilon\). Fix a nonzero
reference \(\epsilon_*\). Let \(S_\epsilon\) be the actual minimal
source over \(U\), with its marked small resolution at \(\epsilon=0\),
and retain \(M_a=\mathcal O(aG-O)\), \(a=1,2\).

The first filling \(W_{\rm c}(N)\) is the regularized collision family
IF.8--10, with \(\lambda=\epsilon^N\lambda_0\). After its
determinant-one regularization the total fourfold is smooth; the
function \(\epsilon\) may have a singular central fibre. Its actual
source/line periods are (IF.15), its physical circle is \(\delta\),
and its protected boundary is the primitive source-line/parameter
chain.

The reference filling \(W_{\rm r}(N)\) uses the fixed source
\(S_{\epsilon_*}\), its fixed actual line \(M_a\), and the same scalar
\(\lambda=\epsilon^N\lambda_0\). No selected zero lies in \(U\).
Its actual suspension lift \(B_0\) is therefore invertible over
\(U\), including both ordinary I1 fibres. Use the full chain
\[
 X_j=V\epsilon^{-j},\qquad
 Y_j=\epsilon^{j+1}/V,\qquad X_jY_j=\epsilon ,
 \quad j\in\mathbb Z.                                  \tag{IE.1}
\]
The suspension carries chart \(j\) to \(j+N\), with \(B_0\) on
its source and line frames. A nonzero iterate changes the chain
index; a segment of \(N\) node/middle charts is a compact
fundamental cover over the compact source patch. Thus
\(W_{\rm r}(N)\) is a smooth fourfold with exactly \(N\) fixed
source surfaces in its central chain, of normal weights \(+1,-1\).

On the boundary annulus the varying source, Cartier line,
translation and line lift all extend over the full
\(\epsilon\)-disc. They are the full source/line maps, not just
their limiting Picard points. The changed-origin coordinate
of IF.10 has pure parameter deck, and its source-base
continuation on this annulus is zero because \(q_*\) is a unit
on \(U\).

Here is the actual smooth boundary transport. Introduce
\(s\in[0,1]\), use source parameter
\(\epsilon_s=(1-s)\epsilon+s\epsilon_*\), and keep the
degeneration coordinate \(\epsilon\) and scalar
\(\epsilon^N\lambda_0\) fixed. The boundary source fibres
stay smooth. Continue their actual line and suspension
using the source/Cartier expressions. On each chain chart
the equation is always \(XY=\epsilon\). There are local
lifts of \(\partial_s\) keeping \(\epsilon\) and the
source-base boundary coordinate fixed: take the
source-family chart lift and its actual line frame,
with zero \(X,Y\) derivatives. Under a unit frame change,
carry its derivative into the two opposite normal
coordinates. These give lifts on the actual quotient
charts.

Use a finite partition of unity on the compact quotient
collar to combine the lifts, then average over the physical
circle. The resulting field still has \(ds=1\),
\(d\epsilon=0\), and fixed source-base boundary coordinate.
Its compact fundamental cover makes the flow complete for
\(0\le s\le1\). Its time-one map is an actual equivariant
boundary diffeomorphism
\[
        \Psi:\partial_U W_{\rm c}(N)
                   \longrightarrow\partial_U W_{\rm r}(N).   \tag{IE.2}
\]
It retains the full source/line units and \(j\)-label
transport. The flow is in the chain atlas, not a
translation logarithm across the interior collision.

Glue the two fillings along (IE.2), reversing the reference
orientation and rounding the common corners. The result
\(W_{\rm rel}(N)\) is a compact oriented smooth
eight-dimensional delta-manifold. Its outer boundary is
the closed relative mapping-torus piece. Its fixed set
consists of the compact interior/H components of
\(W_{\rm c}\), and \(N\) closed doubles of its E patches
with the oppositely oriented reference patches. Their
normal bundles are glued by the actual derivative of
\(\Psi\).

## IE.2. Exterior transport and selected-cusp cancellation

The same source deformation extends on the complement
of \(U\), including the actual cap root. Its division
section, finite character, norm lift and full annular
integral cochain are those of IF.3 and IF.10. On the
selected I1 collar the actual normalization is (IF.2);
the Tate, Picard and Hom units (IF.3)--(IF.5) have
extending logarithms and zero source-parameter winding.
Its Cox products continue through \(\epsilon_s\), with
the same scalar parameter and physical circle.

On the outer circle the completed threefolds are smooth
and proper. Lift \(\partial_s\) as above, prescribing
(IE.2) on a collar of \(\partial U\). Extend the lift
using a partition of unity and circle averaging.
Near the selected fixed sphere prescribe the literal
Cox-coordinate unit map. Its normal derivative extends
through \(s\) and the source-parameter disc, so it
transports the actual Hopf Euler line and normal
framing. The resulting exterior diffeomorphism agrees
with (IE.2).

The two selected fixed-sphere traces and their normal
products are thereby identified, including the positive
physical orbit. Remove the product tubes and perform
the same conifold replacement on both sides. The
identification extends over \(D^3\times S^2\), with
its transported meridian and Hopf Euler line. The
remaining exterior is a product bordism. Therefore
the difference of the two completed Jin six-manifolds
is the relative collision boundary of \(W_{\rm rel}\),
with the parameter-convention sign in IE.5.
This cancels actual selected scalar traces; it does
not supply a holomorphic full selected corner.

## IE.3. The E doubles and actual Cartier class

The marked source small resolution in the unit
Weierstrass coordinates of IF.5 is
\[
 A=Dz,\quad C=Bz,\quad X=Bz,\quad
 Y=(B+Dz)/2,\quad v_0=(B-Dz)/2 .
\]
Here \(A=Y-v_0\), \(B=Y+v_0\), \(C=X\), and
\(D=T_0+X^2+(1-2v_0)X\). The complementary chart is
\[
 D=Aw,\quad B=Cw,\quad w=z^{-1},\quad
 v_0=(Cw-A)/2.
\]
Thus \(dv_0/dB=1/2\) in the first chart and
\(dv_0/dA=-1/2\) in the second. These are actual
submersion charts on both sides of the exceptional
curve. Choose the source-base boundary outside the
two moving critical values. Its restriction is then
a proper submersion as well; the boundary transports
used below are transports of this resolved family.
At \(v_0=0\) the I2 has components \(C_0,C_1\);
the marked section meets \(C_1\), and \(O\) meets
\(C_0\). The actual degree-two section closure has
Cartier equation
\[
                  1-Bz^3-(1-2v_0)z^2=0 .
\]
To see this directly, the tangent slope at
\(G=(0,v_0)\) is \(T_0/(2v_0)\), so the actual
double has \(Y+v_0=-T_0X/(2v_0)\). In the first
resolution chart this gives \(T_0=-2v_0/z\).
Substitute \(2v_0=B-Dz\), \(X=Bz\) and
\(D=T_0+X^2+(1-2v_0)X\); canceling on the dense
ordinary chart gives the displayed Cartier equation,
which defines its closure. At \(v_0=0\), one has
\(B=Dz\) and
\(T_0=D(1-z^2-Dz^4)\). The two central components
are therefore \(C_1=\{D=0\}\) and
\(C_0=\{1-z^2-Dz^4=0\}\), with the latter exactly
the displayed double-section closure.
It restricts to \(C_0\) with multiplicity one and
does not contain \(C_1\). Consequently
\[
 c_1(M_1)[C_1]=1,\qquad c_1(M_2)[C_1]=2.               \tag{IE.3}
\]
The second equality retains the actual vertical
Cartier specialization \(2G-O=C_0\).

The local source patch retracts onto its I2
plumbing: use the radial collapse of \(xy=t\)
to the axes in the two node charts and the
component normal-disc retractions elsewhere.
Its integral two-cycle lattice has primitive
basis \(F=C_0+C_1,C_1\), with pairing
\[
                  \begin{pmatrix}0&0\\0&-2\end{pmatrix}.       \tag{IE.4}
\]
The normalized component two-cells give integral
\(C_0,C_1\), and the zero-section relative disc
meets \(F\) once. The smooth source resolution
is a submersion over \(v_0\), also with boundary,
so this marking transports to \(S_{\epsilon_*}\).

On the reference chain (IE.1) the positive normal
line is literally \(M_a\), and the negative one
is \(M_a^{-1}\). Conjugating the negative-weight
line gives determinant
\[
                          b_{\rm r}=2c_1(M_a).          \tag{IE.5}
\]
Indeed the actual fibre-linear change \(V\mapsto gV\)
on \(M_a^\times\) induces
\((X_j,Y_j)\mapsto(gX_j,g^{-1}Y_j)\) in the chain.
After conjugating the negative-weight coordinate,
the determinant transition is
\(g/\overline g=g^2/|g|^2\). A Hermitian metric
identifies the conjugate of \(M_a^{-1}\) with
\(M_a\) by this explicit positive real factor.
The boundary flow \(\Psi\) of IE.1 preserves the
physical circle, so its normal derivative becomes
a complex linear map after this conjugation. Its
full determinant is transported, including any
off-diagonal entries; no diagonal derivative is
assumed.
It evaluates to zero on \(F\) and \(2a\) on \(C_1\).
Its boundary class is zero integrally: in the
central Tate marking \(QP^2=1\), so \(Z^aV^2\)
is a nonvanishing boundary frame. Transport that
actual frame through the smooth source/Cartier
family. Equivalently the boundary component class
has order two and (IE.5) kills it. A relative lift
is \(-aC_1\), up to the null fibre and a boundary
connecting class. Thus
\[
                              b_{\rm r}^2=-2a^2.        \tag{IE.6}
\]

Here is the chart map identifying the collision E
patch with that same minimal I2 patch. The E face
between the primitive rays
\((0,j,1,0)\), \((0,j+1,1,0)\) has quotient lattice
\((Z,s)\), star rays \((0,1),(1,1)\), and primitive
source period \((Z,s)\mapsto(Z+2s,s)\). On the central
source write \(Q=t^2u_Q(t)\) and use the actual
square root with transported leading coefficient,
\(\widetilde q=t\sqrt{u_Q(t)}\). The two-node chart
chain is
\[
 \xi_\ell=Z\widetilde q^{-\ell},\qquad
 \eta_\ell=\widetilde q^{\ell+1}/Z,\qquad
 \xi_\ell\eta_\ell=\widetilde q,
 \quad \ell\pmod2.                                  \tag{IE.5a}
\]
Its literal overlaps are
\(\xi_{\ell+1}=\eta_\ell^{-1}\),
\(\eta_{\ell+1}=\xi_\ell\eta_\ell^2\).
These are the E-star characters with the retained
Tate units; the primitive stabilizer shifts
\(\ell\) by two. In particular the map has no
additional base ramification or exceptional curve.

For completeness, compose this map with the actual
Tate uniformization into the unit source
\(Y_0^2=X_0^3+X_0^2+T_0X_0\). In its marked Tate
coordinate the convergent functions are
\[
 X_T=\sum_{\nu\in\mathbb Z}
       \frac{Q^\nu Z}{(1-Q^\nu Z)^2}
       -2\sum_{\nu\ge1}\frac{\nu Q^\nu}{1-Q^\nu},
 \qquad
 Y_T=\sum_{\nu\in\mathbb Z}
       \frac{(Q^\nu Z)^2}{(1-Q^\nu Z)^3}
       +\sum_{\nu\ge1}\frac{\nu Q^\nu}{1-Q^\nu}.
\]
The retained minimal Weierstrass coordinate change
has leading terms
\(X_0=4X_T-T_0/2+O(T_0^2,T_0X_T)\) and
\(Y_0=8Y_T+4X_T+O(T_0Y_T,T_0X_T)\), while
\(T_0=16\widetilde q+O(\widetilde q^2)\).
On the chart \(Z=\xi\),
\(\widetilde q=\xi\eta\), this gives
\[
 T_0=16\xi\eta+O(\xi^2),\quad
 X_0=4\xi(1-\eta)^2+O(\xi^2),\quad
 Y_0=4\xi(1-\eta^2)+O(\xi^2).                       \tag{IE.5b}
\]
For every negative summation index, rewrite the
summand in \(Q^k/Z\); its exponents are nonnegative
in this node chart. The resulting series converge
normally on a smaller chart, so these are actual
holomorphic maps, including the axes.

The map to the two small-resolution charts is
\[
 z=X_0/Y_0,\quad D=T_0+X_0+X_0^2,\quad B=Y_0,
 \qquad
 w=Y_0/X_0,\quad C=X_0,\quad A=Y_0.                 \tag{IE.5c}
\]
The source equation gives \(A=Dz,C=Bz\) exactly.
At the marked two-torsion point \(\eta=1\), the
double zero of \(X_0\) and simple zero of \(Y_0\)
make the first quotient extend. On \(C_1\),
\[
 z=\frac{1-\eta}{1+\eta},\qquad
 D=4\xi(1+\eta)^2+O(\xi^2).
\]
The Jacobian of \((\xi,\eta)\mapsto(D,z)\) on
\(\xi=0\) is \(-8\). At \(\eta=-1\), use
\((C,w)\): its Jacobian has magnitude eight there.
The second node is covered by the literal chain
overlap in (IE.5a). This proves the biholomorphism
on the whole component, its two nodes, and the
marked section, with the source orientation and
boundary marking retained.

The actual normal determinant is marked by
\[
                         Z^aV^2/\xi_E^{\,2j+1}.
\]
After extracting its weight-two normal factor,
this character is a meromorphic section of
\(N_+\otimes N_-^{-1}\). It is invariant under the
source period, since \(QP^2=1\), and is nonzero
away from the two central components. Its
dual-character order is zero on each component.
The actual node charts above therefore make the
section invertible also at their intersections.
The Hermitian identification of this line with
the positive-weight spinor determinant is the
same one used in (IE.5). This proves zero
integral first Chern class, rather than merely
a rational vanishing of its degree. One can also
read the integral obstruction from the plumbing
retraction: \(H_1=\mathbb Z\), \(H_2=\mathbb Z^2\)
with primitive basis \(C_0,C_1\), so
\(\operatorname{Ext}(H_1,\mathbb Z)=0\); vanishing
on both components determines the zero class
in \(H^2\). Hence in this boundary marking
\[
                               b_{\rm c}^2=0.           \tag{IE.7}
\]
Replacing \(\xi_E=\epsilon/t\) by \(\epsilon\)
adds the explicit boundary gauge \(t^{2j+1}\).
It may be odd and is retained. A boundary
gauge changes the glued class by the
Mayer--Vietoris image of \(H^1(\partial S;\mathbb Z)\).
Its square and its product with the glued
determinant class vanish. Indeed represent
the connecting class as \(d\chi\wedge\alpha\)
in the collar; its square repeats \(d\chi\),
and its product integrates the zero boundary
restriction of the other class. Thus the
actual derivative of (IE.2) has exactly the
square difference (IE.7) minus (IE.6).

The source patches are oriented diffeomorphic
with boundary. Their closed double has
signature zero and hence tangent Pontryagin
integral zero. This uses only the ordinary
four-dimensional fixed-surface signature
identity. With weights \(+1,-1\), its
normal-link contribution is
\[
 \frac1{24}\int_{S_{\rm c}\cup(-S_{\rm r})}
            \{p_1(TS)-3b^2\}=-\frac{a^2}{4}.           \tag{IE.8}
\]
There are exactly \(N\) E doubles: the actual
scalar period shifts the primitive chain by
\(N\), and the collision-boundary source
loop fixes these labels.

## IE.4. Finite stabilizers and the actual Stokes identity

Remove invariant normal tubes of every fixed
component from \(W_{\rm rel}\). The physical
circle is locally free on the complement.
Its quotient is a compact oriented
seven-dimensional orbifold \(Z\), carrying
the actual orbifold Euler line with class \(x\).

A slice with stabilizer \(\mu_d\) gives a
finite chart \(\widetilde U/\mu_d\). Average
metrics, partitions of unity and connections
over \(\mu_d\) and over the physical circle.
Normalize the connection by
\(\alpha(\delta)=1\). Its curvature represents
the same physical \(x\) on every chart. The
actual tangent splitting is
\[
 TW_{\rm rel}|_{\rm locally\ free}
                    \cong\pi^*TZ\oplus\mathbb R_\delta .      \tag{IE.9}
\]
Choose its connection to match the actual
boundary tangent connections after a collar
interpolation. The basic Chern--Weil form
\[
                      \Omega=\frac{4x^3-p_1(TZ)x}{24}         \tag{IE.10}
\]
is closed. Integrate each finite chart as
\(d^{-1}\int_{\widetilde U}\). Ordinary Stokes
on the finite covers and their averaged
partition of unity cancels every interior
face with exactly these multiplicities.
The finite-isotropy strata are not boundary
faces. Consequently
\(\int_{\partial Z}\Omega=0\).

On a fixed normal link, (IE.9) restricts
to the fixed tangent and weighted normal
bundles. Its equivariant Thom denominator
is \(\prod_i(x_i+w_i u)\). The finite
chart integral, equivalently the weighted
projective power map, gives
\(1/\prod_iw_i\), with every negative
normal conjugation's orientation sign.
Thus its actual contribution is (IE.16), proved below.
The compact interior/H values and (IE.8)
are exactly the terms in this Stokes
identity, including finite stabilizers.
No spin structure on this comparison
bordism or eight-dimensional signature
formula is used.

## IE.5. Outer boundary and Jin conventions

Orient \(W_{\rm c}\) complexly and the
reference piece oppositely. Define
\(\delta\wedge\operatorname{or}(Z)
=\operatorname{or}(W_{\rm rel})\).
Near the outer parameter boundary,
\[
 \operatorname{or}(W)
 =\delta\wedge\operatorname{or}(Y)
                  \wedge d\rho\wedge d\theta .
\]
Since \(\dim Y=5\), its quotient boundary
orientation is
\[
                         -\operatorname{or}(Y)\wedge d\theta.       \tag{IE.11}
\]
At an inner fixed-normal boundary the
minus sign from removing the normal disc
and the minus sign from quotienting an
oriented boundary by the odd-dimensional
orbit cancel. Its orientation is the
positive complex-normal link convention
of (IE.16). Therefore Stokes gives
\[
                 A_{\rm physical,difference}
                          =\sum_F\mathcal R(F).          \tag{IE.12}
\]

Jin identifies \((z,0)\sim(f(z),1)\).
The positive physical family with return
\(f\) has the inverse parameter marking.
The map to the Jin six-manifold reverses
that circle and preserves the physical
Euler line. Hence
\[
                  A_{\rm Jin,difference}
                           =-\sum_F\mathcal R(F).         \tag{IE.13}
\]
The common conifold replacement in IE.2
uses the same transported positive
meridian, so adds no line or orientation
change.

## IE.6. Scalar-order independence and exact local values

The selected-cusp fan in this argument is the initial
vertical-edge fan or its literal reflected fan under
\((Z,V)\mapsto(Z^{-1},P^aV)\). In either marking the
physical delta circle has the already specified
\((-1,+1)\) fixed-curve model, and the selected-unit
transport in IE.2 closes that same fan. The admitted
source/cap sectors are \((a,b)=(1,2)\), \(m=4p\),
and \((a,b)=(2,1)\), \(m=4p-1\), with \(p\ge1\),
their actual \(n=\pm1\) norm markings, and the
retained integral \(d\delta\) twist. No comparison
with a further flopped fan is used here.

Over \(U\) the ordinary suspension, with
no linearization zero, is an actual family
over the product of a source annulus and
a small scalar annulus:
\[
                   B_\lambda=2(-1)^{b+1}\lambda q_*U_a^b.
\]
There is no finite cap in this local
family, so every integer scalar winding
is a closed local loop. Its source-base
boundary family extends over the source
disc, with the actual periods and Cartier
frames. Choose IE.1's transport on this
entire product.

A pair of pants mapping into this
product realizes the based-loop identity
\[
 (\epsilon\text{ turn},N\text{ scalar turns})
   =(\epsilon\text{ turn},0)+(0,N\text{ scalar turns}).    \tag{IE.14}
\]
Pull back the actual local family and
quotient its free physical circle.
This is a seven-dimensional bordism
of the mapping-torus pieces. Glue the
source-base boundary collars by the
full-product transport. The fixed-source
scalar-loop boundary is exactly the
reference piece of IE.1 and cancels.
Thus the closed relative collision
boundaries \(Q_{\rm rel}(N)\) and
\(Q_{\rm rel}(0)\) are bordant with
their actual Euler line. Their
characteristic difference is independent
of \(N\). This is a literal parameter
product and collar construction; no
division of a covered sphere class occurs.

For any admitted cap, its exterior
source/root/line family extends over
the source disc. IE.2 cancels it with
the constant exterior. Hence this
same local relative boundary represents
the fixed-scalar source loop for that
completed family. It suffices to use
the two fully executed orders \(N=8\)
for \((a,b)=(1,2)\), and \(N=6\) for
\((a,b)=(2,1)\):
\[
 \begin{array}{c|rrr}
 (a,b,N)&\text{interior/H}&N\text{ E doubles}&\text{total}\\ \hline
 (1,2,8)&2&-2&0\\
 (2,1,6)&5&-6&-1 .
 \end{array}                                           \tag{IE.15}
\]
Independent executions at \(N=4,12\)
in the first case and \(N=3,9\) in
the second give the same relative
sums. They check the arithmetic;
the independence proof is (IE.14).

By (IE.13), the fixed-scalar marked infinity
Jin differences are respectively \(0\) and \(+1\).
Apply P3F.22's proved Jin-to-\(\Theta_7\) transfer
to the two actual completed boundary mapping
tori: on each, IE.2 has made the specified conifold
replacement, transported the same positive meridian,
and retained the actual Euler line of its free circle
bundle. To select their actual return maps, prescribe
the product connection on the common selected tube
in IE.2's closed Cox product, extend it to a connection
on the actual parameter family, and average over
the physical delta circle. The prescribed product
connection remains unchanged under that averaging.
After the conifold replacement its return is a
diffeomorphism \(f\) of \(Y=S^2\times S^3\), equal
to the identity on the prescribed tube. The actual
Euler line extends around the family, so \(f\)
preserves its primitive class \(x\in H^2(Y;\mathbb Z)\).
The return preserves orientation; the perfect
pairing \(H^2\otimes H^3\to H^5\) then shows that
it preserves \(H^3\) as well. Thus \(f\in I(Y)\).

On the complement of that tube, P3F.22's Hopf lift
is literally the physical return lift supplied by
this delta-equivariant connection and its preserved
Euler line. On the tube it is the same identity
extension in the proved conifold/Hopf collar
construction. Consequently its \(\lambda(f)\) is
the actual clutched sphere of this parameter return.
This identifies the return map and its lift before
using the characteristic polynomial. Their
characteristic integers are
\(\int(4x^3-p_1x)/24\) in the Jin convention.
The transfer sends their difference to that integer
modulo 28. The pair-of-pants map (IE.14) identifies
the difference of these actual returns with the
fixed-scalar positive epsilon source loop. Thus
its oriented sphere class is \(0\) for \((a,b)=(1,2)\)
and \(1\) for \((a,b)=(2,1)\), in each of the two
specified vertical-edge fan markings. This conclusion
does not assign either source-zero fan return.

The old
\(v\)/new \(\epsilon\) scalar path,
\(D^{-4}\) root endpoint and
half-loop fan map remain the explicit
dictionary of IF.1--6. Their winding
corrections are not absorbed into
(IE.15).

## IE.7. Complete normal-link calculation for the two executed fans

This section supplies the local formulas used in IE.4 and
the exact finite sums in (IE.15), independently of the
uncompleted source-zero attachment. Let a compact fixed
component \(F\) have complex normal roots \(x_i\) and
nonzero physical delta weights \(w_i\). Retain its complex
orientation and the original complex normal-sphere
orientation. Its actual normal-link quotient contribution is
\[
 \mathcal R(F)=[u^{-1}]\int_F
 \frac{4u^3-u\{p_1(TF)+\sum_i(x_i+w_i u)^2\}}
      {24\prod_i(x_i+w_i u)}.                         \tag{IE.16}
\]
The coefficient is the Laurent coefficient at infinity.
On the normal sphere, adding its radial real line gives
the pullback of \(TF\oplus\nu_F\); quotienting the
physical orbit removes its oriented real line. Thus the
stable quotient Pontryagin class is the displayed
equivariant class. The equivariant Thom class restricts
to \(\prod_i(x_i+w_i u)\). The localized pushforward
therefore gives (IE.16), with the Euler and integration
identities of Atiyah--Bott (1984), printed pages 8--9,
Theorem (3.5), equations (3.7)--(3.8).

The fibre normalization can be verified directly. For
positive weights, the weighted projective power map
\([z_i]\mapsto[z_i^{w_i}]\) has generic degree
\(\prod_iw_i\) and pulls its rational hyperplane class
back to the ordinary hyperplane class. Consequently
\(\int u^{r-1}=1/\prod_iw_i\). The relation
\(\prod_i(x_i+w_i u)=0\) gives all higher pushforwards
recursively. Conjugating a negative-weight line changes
\((x_i,w_i)\) to \((-x_i,-w_i)\) and reverses the
original normal orientation. This is precisely the
denominator sign in (IE.16); every finite stabilizer
factor remains.

For a point and a curve the respective formulas are
\[
 \frac{4-\sum_iw_i^2}{24\prod_iw_i},\qquad
 -\frac1{24\prod_iw_i}\int_F\sum_i
 \left\{\frac{4-\sum_jw_j^2}{w_i}+2w_i\right\}x_i.
                                                               \tag{IE.17}
\]
For a surface, put
\[
 P=w_1w_2,\quad c=4-w_1^2-w_2^2,\quad
 A=\frac{x_1}{w_1}+\frac{x_2}{w_2},\quad
 B=\frac{x_1^2}{w_1^2}+\frac{x_1x_2}{w_1w_2}
                         +\frac{x_2^2}{w_2^2}.
\]
Its contribution is
\[
 \int_F\frac{cB+2(w_1x_1+w_2x_2)A
                 -p_1(TF)-x_1^2-x_2^2}{24P}.             \tag{IE.18}
\]
Weights \((1,-1)\) give
\((p_1(TF)-3(x_1-x_2)^2)/24\), the formula used
in (IE.8), in the same original normal orientation.

For each exported regular cone let \(C\) be the
ordered matrix of its four primitive rays in the
original \((Z,V,\text{base}_0,\text{base}_1)\)
lattice. The coordinate characters are the rows of
\(C^{-1}\), and their actual physical weights are
\[
                    C^{-1}(0,1,0,0)^{\mathsf T}.        \tag{IE.19}
\]
The vanishing of the nonzero-weight coordinates
specifies every local fixed stratum. The recorded
face permutations and literal period matrices glue
these strata, so no component is counted twice or
omitted. There is no fixed stratum in the open
protected A or B face: their span is respectively
\(\langle(1,0,0,0),(0,0,1,0)\rangle\) or
\(\langle(1,-a,0,0),(0,0,1,0)\rangle\), neither
of which contains the physical delta vector.
Their remaining boundary strata belong to the
already recorded H/interior cones. The protected
E face does contain delta; its fixed surfaces are
exactly the N chain components treated in IE.3.
Thus the interior, H and E contributions exhaust
the fixed set of the relative comparison.
On an interior fixed component, unwrap
each chart by its recorded period \(n\). An
auxiliary cocharacter \(e\) then has tangent and
normal weights
\[
                            C^{-1}T_n e.                 \tag{IE.20}
\]
This is the dual of the actual map
\(C_{\rm unwrapped}=T_{-n}C\). Applying the same
pushforward to the fixed component divides (IE.17)
or (IE.18), evaluated at its auxiliary roots, by
the product of its tangent weights. The two
independently executed choices are
\((1,4,16,64)\) and \((1,5,25,125)\); the code
verifies agreement separately on every component.

On the exceptional base H use \(w=q_B/q_A\) and
normal coordinate \(q_A\). The exact periods have
normal-order matrix
\[
 H_\infty=\begin{pmatrix}2&b\\-a&N-2\end{pmatrix},
\]
and remaining nonconstant factors
\[
 h:(Z,V)\mapsto(wZ,w^{-a}V),\qquad
 g:(Z,V)\mapsto(w^bZ,w^{-2}(1-w)^N V).                 \tag{IE.21}
\]
All other factors are the retained nonzero source,
Cartier and suspension units of IF.5. The three
marked base points are \(w=0,1,\infty\), on the
B,E,A faces respectively. For each regular rank-three
H face, drop its zero first base coordinate and
form the unimodular matrix \(B_H\). Its orbit
closure has the actual base coordinate \(w\), so
is \(\mathbb P^1\). If
\((p_j,q_j,s_j)\) is row \(j\) of \(B_H^{-1}\),
its generic normal coordinate is
\(\eta_j=Z^{p_j}V^{q_j}q_A^{s_j}\).

For an occurrence at period \(n=(n_1,n_2)\), let
\((p,q,r,s)\) be its corresponding full chart row.
The exact recorded checks are
\((p,q)=(p_j,q_j)\) and
\(s+(p,q)H_\infty n=s_j\). Set
\[
 e_w=p(n_1+bn_2)+q(-an_1-2n_2),\qquad e_1=Nn_2q.
\]
The three actual coefficient orders of the generic
normal vector, in its holomorphic local frames, are
\[
 \begin{array}{c|cc|c}
  \text{sector}&x&y&\text{order at its marked point}\\ \hline
  B&w&q_A&e_w+r\\
  E&(1-w)/u_\epsilon&q_A&e_1+r\\
  A&w^{-1}&wq_A&-e_w+r-s-e_1.
 \end{array}                                             \tag{IE.22}
\]
Their sum is the actual normal-line degree. In
particular the \((1-w)^N\) term, the higher ray
heights, and every recorded period remain in the
degree computation.

The two auxiliary fibre circles \((1,2,0,0)\) and
\((1,3,0,0)\) commute with (IE.21) and the full
periods. On each compact H fixed surface, their
fixed sets consist of these rank-three curves and
the isolated chart fixed points. A sector-interior
three-face has base rank two and only the physical
one-dimensional fibre kernel, so supplies no
additional auxiliary fixed curve. If an auxiliary
fixed curve has normal weight \(\eta\), normal
degree \(d_t\), and ambient normal weights/degrees
\((\beta_i,d_i)\), substitute
\[
 x_i=\beta_i u+d_i h,\qquad
 p_1(TF)=\eta^2u^2+2\eta d_t hu,\qquad h^2=0
\]
into (IE.18). Writing the numerator polynomial
there as \(R_0u^2+R_hhu\), its exact localized
contribution is
\[
                         R_h/\eta-R_0d_t/\eta^2.         \tag{IE.23}
\]
This divides by the actual Euler class
\(\eta u+d_t h\). Isolated fixed points use the
two nonzero tangent weights. Both auxiliary circles
agree component by component. Independent outputs
also compute \(c_1(TF)^2,c_2(TF)\), and verify the
integrality of \((c_1^2-2c_2)/3\) and
\((c_1^2+c_2)/12\) on every H surface.

The complete finite outputs are
\[
 \begin{array}{c|rr|rr|r}
 (a,b,N)&\#\text{ interior}&\sum_{\rm int}\mathcal R
 &\#H&\sum_H\mathcal R&\text{combined}\\ \hline
 (1,2,8)&2153&9333/16&125&-9301/16&2\\
 (2,1,6)&2147&739&111&-734&5.
 \end{array}                                             \tag{IE.24}
\]
There are 194 and 152 full-fibre auxiliary fixed
curves on H, respectively. Every primitive ray,
ordered determinant-one cone, period, face
permutation, normal degree and rational summand
is retained in the corresponding
\(\texttt{source\_infinity\_regular\_fan}\),
\(\texttt{fixed\_charts}\),
\(\texttt{interior\_residues}\), and
\(\texttt{h\_residues}\) JSON/certificate files
under \(\texttt{code/part3\_fourfold/}\).
Their scope is the actual infinity matrices and
period maps just displayed. Combining (IE.24)
with the E doubles proved in IE.3 gives (IE.15).

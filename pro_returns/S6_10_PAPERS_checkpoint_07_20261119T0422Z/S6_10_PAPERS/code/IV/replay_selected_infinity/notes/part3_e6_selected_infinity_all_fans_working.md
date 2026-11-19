# The marked selected-infinity return on every selected lattice fan

Working proof, 18 November 2026.  This proof retains the original E6
family, the point line M6, suspension exponent one, and the reduced
quadratic cap with \((m,n)=(2,1)\), its chosen finite character and full
integral reference cochain used in K101.  The scalar is the same fixed
nonzero original scalar satisfying the strict contraction estimate of
IA.1.  The parameter is the complete positive epsilon loop, where
epsilon=1/w.  All fan changes below occur at the selected cusp.  The
initial physical Jin pair (-4,8) and actual return class -1 are those
proved by the complete source, finite-cap, normal, moving-cap and
outer-transfer maps of K101.  The native pair (2,-6) uses the actual
MC2/OT Cox product and the K68 characteristic-to-free-coordinate map,
as specified again after IF.20 below.

For an integer unimodular matrix P let T(P) denote its two-triangle
periodic selected fan.  We construct the actual family at every such
fan, its full relative products, and a terminating integer return
algorithm.  The last section evaluates this algorithm and proves that
its image in Z/28 is exactly the fourteen odd residues.  Every
reference to a scalar, cap or source period below is to its full map.

## Statement

For the actual marked family
\[
 y_o^2=x_o^3+r x_o^2+t_o x_o+t_o^2,\qquad G=(0,t_o),\qquad
 r=\frac{\epsilon^2(3\epsilon^2-2)}{(1-3\epsilon^2)^2},
\]
with \((M_a,b,m,n)=(M_6,1,2,1)\), the fixed original scalar,
finite character and reference of K101, the positive full epsilon
return is constructed on every lattice-basis selected fan \(T(P)\),
\(P\in GL_2(\mathbb Z)\).  The complete integer algorithm in
IF.4--5 computes its actual class.  If \(S_6(P)\) denotes the
integer path sum of K71 on the same canonical basis, its value is
\[
 A_\infty(T(P))=
 \left[\frac23\bigl(S_6(P)+1\bigr)-x^2-xy-y^2\right]_{28},
 \qquad (x,y)^t=P^{-1}(0,1)^t.
\]
The full affine morphism of the two prism/reset systems is IF.41--45.
Its integral construction proves that the displayed fraction is an
even integer.  The exact image is all fourteen odd residues in
\(\mathbb Z/28\), with the explicit actual fan words in IF.6.
On the vertical fan
\(T_j=\left(\begin{smallmatrix}1&0\\j&1\end{smallmatrix}\right)\)
the physical Jin characteristic pair and native free pair are
\[
 (k_M,\ell_M)=(-4-12j(j-1),8),\qquad
 (\mu,\nu)=(2,-6-12j(j-1)),
\]
and its actual class is \([-1-2j(j-1)]_{28}\).  The original
height, every coefficient unit, both endpoint directions and the
full cap word are retained by the written maps.

## IF.1. Original height and the complete period coefficients

The original source is
\(y_o^2=x_o^3+r x_o^2+t_o x_o+t_o^2\), with
\(G=(0,t_o)\) and
\(r=\epsilon^2(3\epsilon^2-2)/(1-3\epsilon^2)^2\).
Keep the literal original and native source coordinates of EI and OT:
\[
 d=1-3\epsilon^2,\qquad
 x_o=\epsilon^2d^{-2}x_e,\quad
 y_o=\epsilon^3d^{-3}y_e,\quad
 t_o=\epsilon^4d^{-3}t_e,
 \qquad q_o=\epsilon^4d^{-3}q_e.
 \tag{IF.1}
\]
The native equation and selected value are
\[
 y_e^2=x_e^3+(3\epsilon^2-2)x_e^2+d t_e x_e+\epsilon^2t_e^2,
 \quad G=(0,\epsilon t_e),\quad t_{c,e}=1-\epsilon^2.
 \tag{IF.2}
\]
The source isomorphism in IF.1 preserves the actual marked point and
the canonical point section.  Consequently the Tate point coordinate
and its point-line coefficient agree under that arrow.  In the original
height q=q_o the exact two periods have the form
\[
 H:(Z,V,q)\longmapsto(\kappa qZ,\alpha V,q),\qquad
 B:(Z,V,q)\longmapsto(gZ,q\eta V,q),
 \tag{IF.3}
\]
where
\[
 \kappa=\epsilon^{-4}d^3\kappa_e,\qquad
 \alpha=P_G^6,\qquad g=P_G^{-1},\qquad
 \eta=\lambda d^3\beta_e.
 \tag{IF.4}
\]
Here Q=\kappa_e q_e is the full Tate parameter, and \(\beta_e\) is
the full point-frame suspension coefficient divided by q_e after the
native \(\epsilon^4\) scalar is retained.  The source, Miller and
point-frame calculation of EI and OT gives extending nonzero
\(\kappa_e,P_G,\beta_e\), with respective values
\(-1/64,-1,64\) at the selected central node.  At q_e=0 the first
coefficient is exactly \(-(1-\epsilon^2)^2/64\).  All its higher
terms remain in IF.4.  Thus, on the chosen epsilon annulus and a
uniformly small original q disc, the windings of
\((\kappa,\alpha,g,\eta)\) are
\[
                         (-4,0,0,0).
 \tag{IF.5}
\]
The functions \(\epsilon^4\kappa,\alpha,g,\eta\) have fixed based
periodic logarithms there.  Their q derivatives are retained.  The
q-disc radius is chosen on the compact parameter circle using IF.1;
no extension on a fixed original q-disc through epsilon zero is used.

The line interpretation in IF.4 is the module map, not a meromorphic
coefficient evaluated at a coinciding point section.  In the
complementary graph its two coefficients are explicitly
\[
 \mathcal B^{\rm raw}=\sigma^{-6}\bar B,\qquad
 \mathcal B^{\rm pt}(p)=\mathcal B^{\rm raw}(p)
                          \frac{r_{T_bp}}{r_p},\qquad
 \psi=\frac{f_{P_G^6}}{r_p},\qquad
 \beta=\mathcal B^{\rm pt}\frac{\psi(T_bp)}{\psi(p)}.
 \tag{IF.6}
\]
The actual Cartier maps in EI identify the second coefficient and its
inverse as extending units through both O/T section charts.  The last
formula is exactly the selected point-theta square of OT.9a.  It gives
IF.4 after the complete original-height substitution; it retains every
horizontal section factor.

On the exterior and finite cap retain the K96 sector maps with
\[
 \Phi_\beta=A^kB^{j_{\alpha\beta}}\Phi_\alpha,\qquad A^m=B^n.
 \tag{IF.7}
\]
In the complementary graph a quarter turn has the actual word
\(AB^{j_\gamma}\), and its four iterates give
\(A^4B^{\sum j_\gamma}\).  The source and line coordinates in
IF.1--6 commute with this full square.  Every fan map below is the
identity in these original exterior/cap coordinates after its displayed
inverse character map.  Thus IF.7 and its endpoint-to-initial inverse
are part of every family and return constructed here.

## IF.2. All vertical fans: the actual relative line and tangent maps

For \(T_j=\left(\begin{smallmatrix}1&0\\j&1\end{smallmatrix}\right)\)
the literal character and period maps are
\[
 Z_j=Z,\quad V_j=Z^{-j}V,\quad H_j=HB^j,\quad B_j=B,
\]
\[
 Q_j=\kappa qg^j,\qquad
 \alpha_j=\alpha\eta^j\kappa^{-j}g^{-j^2},\qquad
 \eta_j=\eta g^{-j}.
 \tag{IF.8}
\]
The source comparison uses \(Q_s=Q\exp(sj\log g)\).  In a
nodal source chart xy=Q_s its exact horizontal field is
\(\partial_s+j\log g\,y\partial_y\), with the full analytic
unit in its coefficient.  On the protected outside collar it is the
marked-period field obtained by differentiating IF.8.  Join these
fields by a vertical partition of unity, fixed on the two protected
collars, and average over the physical circle.  The full Cartier arrow
is multiplication by \(Z^j\): in the two source charts it carries
the generators \(x^{-j-1}y^j,x^{-j}y^{j+1}\) to \(1/x,y\).
The same arrow carries the positive normal spinor, its actual Cox
Hopf map and the product cap.  Outside the selected piece it is the
identity in IF.1 and IF.7.  This is the K63/EG.40 construction applied
to the complete coefficients IF.4; its defining vector field and both
Cartier generators have just been specified.

Use full real period coefficients, with \(z=\log Z/(2\pi i)\),
\(\ell=\log V/(2\pi i)\):
\[
 (z,\ell)=u(1,0)+b(\tau,\mu)+d_\delta(0,1)
                         +\gamma(G_0,\beta_0),
 \tag{IF.9}
\]
where \(\tau=\log(\kappa q)/(2\pi i)\),
\(\mu=\log\alpha/(2\pi i)\),
\(G_0=\log g/(2\pi i)\), and
\(\beta_0=\log(\eta q)/(2\pi i)\).  The imaginary period
matrix is invertible by the same strict contraction determinant used
in IA.1 and OT.  The real parts then determine u and d_delta; in
particular \(d_\delta=\operatorname{Re}\ell-\operatorname{Re}\mu\,b
-\operatorname{Re}\beta_0\,\gamma\).  Differentiating this
identity retains every unit and its derivative.

Write \(\alpha_q=\arg q/(2\pi)\),
\(\theta=\arg\epsilon/(2\pi)\).  The actual q and epsilon
decks, and the full shear of these coefficient coordinates, are
\[
 (u,d_\delta)\mapsto(u-b,d_\delta-\gamma),\qquad
 (u,d_\delta)\mapsto(u+4b,d_\delta),
\]
\[
 u_j=u,\quad b_j=b,\quad\gamma_j=\gamma-jb,\quad
 d_{\delta,j}=d_\delta-ju.
 \tag{IF.10}
\]
The actual real connections therefore satisfy
\[
 A_0=dd_\delta+\alpha_q\,d\gamma,\qquad
 A_j=dd_{\delta,j}+\alpha_q\,d\gamma_j+4j\theta\,db,
\]
\[
 \beta_j=A_j-A_0=-j\{du+(\alpha_q-4\theta)db\}.
 \tag{IF.11}
\]
The expression is invariant under both full deck changes.  It is an
identity of connections in IF.9, so it does not discard any analytic
unit phase.

Here is the relative bundle map needed for the curvature calculation.
On the completed selected quotient piece let the source graph map b
be changed by a supported real logarithm to be constant near the fixed
tube.  On the theta cut define the line \(\mathcal T\) by the
coefficient arrow \(e^{2\pi i b}\).  Its curvature is
\(\Xi=d\theta\wedge db\), and \(\Xi^2=0\).  The full coefficient
square IF.10 gives
\[
                  U_j\simeq U_0\otimes\mathcal T^{4j},
                  \qquad U=M^*.
 \tag{IF.12}
\]
We verify its prescribed outer arrow, including its integral gauge.
The boundary first homology is freely generated by
\(\alpha_q,\theta,b,\gamma\): the q commutator kills u
primitively, and the epsilon commutator is 4u.  The completed piece
has the three extending generators \(\theta,b,\gamma\); the
Thom/Mayer--Vietoris computation in the K63 relative piece is carried
by the source, normal and Hopf maps above.  Thus only the q-angle
coefficient of a boundary ratio remains to be tested.  Choose the
actual source section \(Z_*=i\), gamma zero, in a sufficiently
small common selected disc.  It stays away from the retained point
divisors (near one and minus one) and both node branches.  The source
field is chosen zero on this section, and its full map is
\[
 (q/Z_*,Z_*,1)\longmapsto
                  (qZ_*^{j-1},Z_*,Z_*^{-j}).
 \tag{IF.13}
\]
Both sides are genuine free toric charts with height equal to the
three-coordinate product.  The inverse uses the opposite nonzero
powers of Z_*.  The line arrow and inverse extend across the whole
disc; hence the q-angle winding is zero.

For clarity the remaining extension is an actual Cech construction.
Take the full transition functions of
\(U_jU_0^{-1}\mathcal T^{-4j}\), subtract the integral
one-cochain whose coboundary is their integral logarithm two-cocycle,
and write the resulting real one-cocycle as
\(r_{il}=a_l-a_i\), with
\(a_i=\sum_k\rho_k r_{ki}\).  Multiplication of its frames by
\(e^{-2\pi i a_i}\) supplies an absolute isomorphism.  Remove the
three extending boundary characters \(\theta,b,\gamma\) from its
ratio with the specified outer arrow.  By IF.13 the remaining ratio
has a single real logarithm; extend that logarithm with a collar
cutoff.  The resulting map is exactly IF.12 on the boundary.  Its
inverse has the prescribed opposite direction.  The only residual
inner-cap gauge is a theta character, which extends over its actual
\(D^3\times S^2\times S^1\) product.  The full cap word IF.7 is
therefore unchanged.

The tangent comparison is also relative.  Write q' for the actual
implicit solution \(Q(q',\epsilon)=Q(q,\epsilon)g(q,\epsilon)^j\).
Its derivative in q is nonzero after shrinking the selected disc;
it has \(q'=q a_j\) with \(a_j(0,\epsilon)=g(0,\epsilon)^j\).
Set \(c=g(q',\epsilon)/g(q,\epsilon)\) and use its unique
logarithm zero on q=0.  In the untwisted suspension the actual map is
\((Z,\gamma_j)\mapsto(c^{\gamma_j}Z,\gamma_j)\), with
\(c^{\gamma_j+1}g(q)=g(q')c^{\gamma_j}\).  It extends the two
node charts by opposite unit factors.  If
\(\delta G=\log c/(2\pi i)\), its full source block is
\[
 \begin{pmatrix}\omega'\\d\gamma'\\db'\end{pmatrix}
 =\begin{pmatrix}1&\operatorname{Re}\delta G&-j\operatorname{Re}\delta G\\
                 0&1&-j\\0&0&1\end{pmatrix}
   \begin{pmatrix}\omega\\d\gamma\\db\end{pmatrix}.
 \tag{IF.14a}
\]
All base derivatives of these entries remain in the off-diagonal
base/source block.  The base
block is the actual two-dimensional q change and has its retained
theta dependence.  The full derivative is block triangular.
Connections with these same triangular blocks have curvature-square
trace equal to the sum on the diagonal blocks.  The strictly
triangular source block contributes zero.  On its comparison collar
the base block depends on \(\alpha_q,\theta\) and one collar
variable, so its curvature-square vanishes by dimension.  This proves
zero transgression on the whole comparison collar, not only equality
of two endpoint frames.

The remaining relative \(p_1\Xi\) pairing uses a literal level
cobordism.  Take \(U_1\Subset U_2\Subset U_3\) around the fixed
tube, all connection/surgery changes in U1, and a real lift
\(\widetilde b\) of the original graph map on U3.  For a cutoff
\(\chi=1\) on U2, supported in U3, set
\[
 b_s=b\exp\bigl(2\pi i s\chi(c-\widetilde b)\bigr).
 \tag{IF.14}
\]
A common regular value different from \(e^{2\pi i c}\) gives a
relative level cobordism, fixed on the outer boundary.  Its terminal
level misses U1 and is the same cycle before and after surgery.  The
original level is the source three-level times the gamma circle; its
source-pulled p1 integral is zero.  Stokes with the just proved zero
outer transgression gives zero on the terminal level.  This proves
the required relative pairing while retaining the actual level
cobordism.  In particular \(\ell_M\) is independent of j.

For the Euler cube, IF.12 gives an interior contribution affine in j.
The exact outside pullback and connection difference are
\[
 A_{{\rm ext},j}=dd_{\delta,j}+\alpha_q\,d\gamma_j
                         +j(du+\alpha_q\,db),\qquad
 d\beta_j=-j\,d\alpha_q\wedge db+4j\,d\theta\wedge db.
 \tag{IF.15}
\]
With \(\Omega_B=d\alpha_q\wedge du\wedge db\wedge d\gamma
\wedge d\theta\), direct exterior multiplication gives
\[
 3\int_0^1\beta_j(F_{{\rm ext},j}+s\,d\beta_j)^2ds
                         =12j^2\Omega_B.
 \tag{IF.16}
\]
The actual outward interpolation runs from s=1 to s=0, so its
contribution is -12j^2.  As in OT, the physical dual and the actual
Jin interval reversal give the same sign for this curvature in the
physical Jin pair.  Thus
\[
        k_{M,j}=k_{M,0}+Lj-12j^2,\qquad \ell_{M,j}=8
 \tag{IF.17}
\]
for one constant L fixed by the actual endpoint comparison next.

## IF.3. The full reflected endpoint and the vertical integer seed

The original family and its canonical point section depend on
\(\zeta=\epsilon^2\).  The map from epsilon to minus epsilon is
the identity in original source coordinates; in IF.2 it is
\((x_e,y_e,t_e)\mapsto(x_e,-y_e,t_e)\).  On the selected
normalization this sends its source coordinate to its negative.
With the retained node order, Q is unchanged and
\(Z\mapsto Z^{-1}, P_G\mapsto P_G^{-1}\).  The full theta
identity, including all infinite product factors, is
\[
 f_{P_G^{-a}}(Z^{-1})=P_G^a f_{P_G^a}(Z),\qquad a=6.
 \tag{IF.18}
\]
The canonical original point-section coefficient is unchanged.
Consequently the actual point-theta line map is
\((Z,V)\mapsto(Z^{-1},P_G^aV)\).  Composing the target source
period, whose line coefficient is \(P_G^{-a}\), gives exactly
\[
                         (Z,V,q)\longmapsto(Q/Z,V,q).
 \tag{IF.19}
\]
This uses the full Q=\kappa q and its invertible analytic factor;
the original height q is unchanged by IF.1 under the sign change.
Its valuation map is
\((x,y,h)\mapsto(-x+h,y,h)\), including the height-one
translation.  Substitution in the two triangles gives
\(T_j\mapsto T_{1-j}\).

To see that IF.19 is a full family arrow, perform the source, Cartier,
root and Cauchy construction of the actual reference cochain first
on the zeta disc in original coordinates, with the fixed original
reference at zeta_*.  Pull it back by epsilon squared.  The original
root family and every Miller unit are holomorphic there on their
retained cap domain.  Thus the full IF.7 cochain, its integers and
finite character are literally even.  Source inversion and the target
H period above carry this chosen reference; no new annular period is
inserted.  The map on the epsilon circle is the orientation-preserving
half rotation.  It preserves the actual physical circle, its line,
the complete normal/Cox arrow and the same identity extension on the
selected tube.  It therefore identifies the physical Jin pairs at
j=0 and j=1.  IF.17 and the proved K101 pair give L=12.  We obtain
\[
 \begin{split}
 (k_{M,j},\ell_{M,j})&=(-4-12j(j-1),8),\\
 (\mu_j,\nu_j)&=(2,-6-12j(j-1)),\\
 A_j&=-1-2j(j-1).
 \end{split}
 \tag{IF.20}
\]
Here the native product is fixed by the actual MC2 positive Cox frame
\[
 v=G_0e,\qquad G_0=\begin{pmatrix}1&-Z\\ \bar Z&1\end{pmatrix},\qquad
 v_{\rm cap}=G_0\operatorname{diag}(e^{-8\pi i\theta},1)G_0^{-1}v_F,
 \tag{IF.20a}
\]
with the period-one theta of IF.10 and with its full original common
phase and reciprocal positive factors carried by the extending maps
of MC2.  The original ball map of OT holds this Cox quaternion fixed
and uses the written physical Hopf lift on the selected tube.  Thus
the literal K68 piece-exchange and inverse-clutch map applies to this
native product; its free-coordinate identities are
\(k_M=\mu+\nu\) and \(\ell_M=4\mu\).  In particular
\(\mu=\ell_M/4\), \(\nu=k_M-\ell_M/4\) give (2,-6)
at j=0 and the displayed pairs at every j under IF.8--14.  These are
the actual native coordinates, obtained before reducing any class
modulo 28.

## IF.4. Full ordinary products and the doubled circle prisms

Let P be any determinant-one basis.  Its inverse gives the new
character rows and P gives the new period columns.  The complete
coefficient matrix is
\[
 A_{is}=(\kappa^{P_{1s}}g^{P_{2s}})^{(P^{-1})_{i1}}
        (\alpha^{P_{1s}}\eta^{P_{2s}})^{(P^{-1})_{i2}}.
 \tag{IF.21}
\]
The q exponents are \(P^{-1}P=I\).  The full source and line
coefficients remain analytic on the protected q-disc times the
parameter annulus, with the periodic logarithms from IF.4.  Retain
them in the three exact adjacent Cox rows, from the first chart
(a,b,c) with q=abc:
\[
 (A_{11}A_{21}bc,A_{21}^{-1}ab,A_{11}^{-1}b^{-1}),\quad
 (A_{12}A_{22}bc,A_{22}^{-1}c^{-1},A_{12}^{-1}ac),\quad
 (a^{-1},ab,ac).
 \tag{IF.22}
\]
The native coordinates are respectively (b,a,c), (c,a,b), (a,b,c).
Their second charts are
\[
 (A_{11}w,A_{21}v,(A_{11}A_{21})^{-1}u),\quad
 (A_{22}v,A_{12}w,(A_{12}A_{22})^{-1}u),\quad(u,v,w).
 \tag{IF.23}
\]
In each case \(z'=1/z,\ n'=zn\), and the height remains the
literal product.  The ordinary second vertex is
\((u,A_{22}v,A_{11}w)\); its three normal matrices are
\[
 D_0=\operatorname{diag}(A_{22}/A_{21},A_{11}A_{21}),\quad
 D_1=\operatorname{diag}(A_{11}/A_{12},A_{12}A_{22}),\quad
 D_2=\operatorname{diag}(A_{22},A_{11}).
 \tag{IF.24}
\]
All determinants equal \(A_{11}A_{22}\) and have winding -4.

Use the actual double pullback of the parameter loop, including its
two complete closing arrows.  Define
\[
 W=\begin{pmatrix}-4&0\\0&0\end{pmatrix},\quad t=-4,\quad
 B_P=2P^{-1}WP,\quad
 \ell=(B_{22}-B_{21},B_{11}-B_{12},B_{22}).
 \tag{IF.25}
\]
After separating each full periodic logarithm, the normal factors on
this pullback are \(H_tq_HH_{\ell_i-t}\).  An explicit based
quaternion extension of an integer phase is
\[
 p_r(s,\theta)=\sin\chi(s)e^{2\pi i r\theta}+j\cos\chi(s),\qquad
 H_r(s,\theta)=p_r(s,\theta)p_r(s,0)^{-1},
 \tag{IF.26}
\]
Here \(\chi\) is a smooth radial function equal to zero near the
centre and to \(\pi/2\) near the boundary.  Thus the expression is
smooth on the full disc, is identity near the centre, has the stated
phase at the boundary, and is periodic at both parameter endpoints.
In fact \(p_r(s,0)=\sin\chi(s)+j\cos\chi(s)\); hence
\(H_r=1\) near the centre and
\(H_r=e^{2\pi i r\theta}\) near the boundary.  Also
\(H_r(s,0)=H_r(s,1)=1\) at every radial value.
The zero-winding unit
logs are extended by the same protected cutoff.  With the native
Hopf factor U the full ordinary comparison is
\((UH_tU^{-1})q_HH_{\ell_i-t}\).  Its left degree is
\(2t=-8\) and its right degree is zero; its inverse cylinder has
left degree +8.  The exact tube equation is
\(zD_{i,*}K_i=zD_i\).  It identifies both vertex products.  Restore
the complete higher normal jets by the actual normal rescaling
\(F_s(z,n)=(z,s^{-1}F(z,sn))\), with its derivative value at zero,
and integrate its cutoff velocity on the annulus between the two
protected radii.  Whenever q is changed in this rescaling use its
actual inverse q-coordinate from the retained source map; this keeps
the original equation q=zn0n1 and every full coefficient of IF.22.
This is the full normal-product construction of GF/ZA in the written
coordinates, rather than only its linearization.

Put \((x,y)^t=P^{-1}(0,1)^t\) and
\[
 w=(x,y,-x-y),\qquad d=(-x-2y,-2x-y,x-y).
 \tag{IF.27}
\]
The actual circle action on the native spinor is
\(q_H\mapsto e^{-iw_i\phi/2}q_H e^{id_i\phi/2}\).
The integers d_i and w_i have the same parity, so the two endpoint
signs agree with the base/normal Spin endpoints.  Composing this
action with IF.26 gives the complete trace degrees
\[
 I_i=t w_i+d_i(\ell_i-t),\qquad
 J_i=t w_i-d_i(\ell_i-t).
 \tag{IF.28}
\]
For the symmetric ordinary variation matrix V and its three stable
normal entries delta the full prism equations are
\[
 V(w_i e_i-w_0e_0)=I_i e_i-I_0e_0,\qquad
 w_i\delta_i-w_0\delta_0=J_i-J_0,\quad i=1,2.
 \tag{IF.29}
\]
They are the actual circle/derivative prisms obtained from IF.22--28.

At T_j these data are particularly explicit:
\[
 B_j=\begin{pmatrix}-8&0\\8j&0\end{pmatrix},\quad
 I=(16j-8,0,0),\quad J=(8-16j,-8,8),
 \tag{IF.30}
\]
\[
 V=\begin{pmatrix}
 24j(j-1)&8-16j&16j-8\\
 8-16j&0&0\\16j-8&0&0
 \end{pmatrix},\quad
 \delta=(-24-24j(j-1),16j-16,-16j).
 \tag{IF.31}
\]
Indeed the fixed entries are
\(V_{00}=2t-2\mu_j-2\nu_j\),
\(\delta_0=2t-2\mu_j+2\nu_j\) by the actual ordinary cylinder,
and the remaining entries follow from IF.29.  The single native
right integers at C1 and C2 are respectively
\(4(j-1)\) and \(-4j\).  Their identification uses the actual
double pullback: \((\delta_i-V_{ii})/2\) is the doubled free
degree and \((\delta_i-V_{ii})/4\) is its original free degree.
No element of Z/28 is divided.

## IF.5. The directed fan changes, unique target and termination

For columns v,w, the triangles of T(P) are
\(\{n,n+v,n+w\}\) and
\(\{n+v,n+w,n+v+w\}\).  Swapping columns, and right
multiplication by
\[
 R=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\quad
 R^2,\quad -I,\quad -R,\quad -R^2
 \tag{IF.32}
\]
give the same full fan, by the literal triangle translations of
AF.1.  The identity on the absolute dense torus identifies every
matched affine cone semigroup with its inverse, commutes with all
full periods IF.3, and is the identity on IF.7.  It preserves the
physical circle and the original height.

There is a unique representative either T_j or
\(C=\left(\begin{smallmatrix}p&-r\\q&s\end{smallmatrix}\right)\)
with p,r>0 and ps+rq=1.  The six actual unimodular triangles of the
star place the physical vector either on its primitive ray or in the
interior of one ordered cone; these two placements give exactly
these representatives.  For the second form apply the literal
Euclidean parents
\[
 Q_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 Q_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix}:\quad
 C\mapsto CQ_0^{-1}\ (r\ge p),\quad
 C\mapsto CQ_1^{-1}\ (p>r).
 \tag{IF.33}
\]
The positive pair becomes (p,r-p) or (p-r,r), so its sum decreases.
Since gcd(p,r)=1, equality gives p=r=1, and the next parent is T_j.
Reverse the finite word.  Each forward target has physical weights
(r,p,-r-p), all nonzero.

Every word step is a complete family map.  Q0 uses characters
(ZV,V), periods (H,H^-1B), and first triple (a/c,bc,c); Q1 uses
characters (Z,ZV), periods (HB^-1,B), and first triple (a/b,b,bc).
The two other-ruling native charts are
\[
 (n_0/n_1,zn_1,n_1),\qquad(n_1/n_0,zn_0,n_0),
 \tag{IF.34}
\]
with common rank-one matrix
\(\left(\begin{smallmatrix}n_0&n_1\\zn_0&zn_1\end{smallmatrix}\right)\)
and the same q.  At Q1 interchange the two normal coordinates by
the exact unitary path
\[
 S_s=\tfrac12\begin{pmatrix}
 1+e^{\pi i s}&1-e^{\pi i s}\\1-e^{\pi i s}&1+e^{\pi i s}
 \end{pmatrix},\quad0\le s\le1.
 \tag{IF.35}
\]
It commutes with the scalar normal transition zI and preserves the
oriented real normal four-plane.  The full torus multiplier (A,D)
has the Cox lift
\[
 (a_0,a_1,c_0,c_1)\longmapsto
                  (a_0,Aa_1,(AD)^{-1}c_0,Dc_1).
 \tag{IF.36}
\]
It preserves q and both resolutions.  Applied to every coefficient
and every closing map, this lift gives the full multiplier substitution
\[
 A'_{is}=\prod_{h,k}A_{hk}^{(Q^{-1})_{ih}Q_{ks}}.
 \tag{IF.37}
\]
The inverse is the substitution for Q^-1.  All higher q terms and
annular units are carried by these identities.  Transport the link
metric by the Cox arrow and its positive radial normalization; use
IF.26 and its protected full normal rescaling to restore the complete
jets.  All period translates commute with the construction.  On the
common exterior the inverse character map returns to the same
original source and Cartier coefficients, hence to IF.7 including
each integer and finite character.  Two compact ruling charts replace
the chosen tube in the compact original exterior.  Their common
blowup and projective ruling maps are the actual F35/AF.2 maps; their
integral blowup/Gysin maps preserve the sphere cohomology and the
primitive period relations preserve the trivial fundamental group.
Thus each step constructs the actual compact sphere family and its
physical return at the specified new fan.

Select the old edge i=0 or1 and write c=Vii,e=delta_i.  The actual
common-link map is
\((h,q_H)\mapsto(q_H^{-1}h q_H,q_H)\).  With IF.35 and the
native complex reset its free-coordinate action is
\[
 (\mu,\rho,S)\longmapsto(\mu+2\rho,-\rho,S+\rho),\qquad
                         \rho=(e-c)/4.
 \tag{IF.38}
\]
K68 fixes the central generator as the physical +1 class, using the
same inverse-clutch/piece exchange as OT.  Adding the identical
ordinary comparison on both sides of IF.38 gives the selected target
entries
\[
                V'_{22}=c,\qquad\delta'_2=2c-e,\qquad
                S'=S+(e-c)/4.
 \tag{IF.39}
\]
Compute the target I,J,w by IF.25--28.  The full target equations are
IF.29 and IF.39.  Since all target weights are nonzero their unique
symmetric solution is
\[
 C=w_2^2c-w_2I_2,\qquad E=w_2(2c-e)-J_2,
\]
\[
 V'_{rs}=\frac{I_r}{w_r}\delta_{rs}+\frac{C}{w_rw_s},\qquad
 \delta'_r=\frac{J_r+E}{w_r}.
 \tag{IF.40}
\]
For uniqueness a symmetric difference annihilates the plane spanned
by \(w_i e_i-w_0e_0\); it is a scalar multiple of
\((1/w_r)(1/w_s)\).  The stable difference has one analogous
constant.  The two specified target entries fix both.  Existence is
the actual family and products constructed in IF.34--37.  Hence this
rational solution equals their integral invariants; rho in IF.38 is
the actual integer free degree.  Start with IF.31 and S=A_j, perform
IF.39--40 along the unique finite word, and reduce S modulo 28 only
at the end.  This proves the return algorithm for every stated fan.

## IF.6. An exact affine morphism of prism data and the image

Let S6(P),V6(P),delta6(P) be the integer path sum and ordinary data
of the proved K71 algorithm in its own single-loop convention.  The
following comparison is an explicit affine map of the two complete
prism systems and their directed resets.  It evaluates the algorithm
just constructed.

K71 has trace inputs equal to three quarters of IF.25--28.  On every
vertical seed, IF.31 and AF.3 give
\[
 V_\infty=\tfrac43V_6,\qquad
 \delta_\infty-\tfrac43\delta_6=(-8,0,0),\qquad
 S_\infty-\tfrac23S_6=-\tfrac13.
 \tag{IF.41}
\]
For a nonvertical canonical basis set
\[
 w=(x,y,-x-y),\quad D=w_0w_1w_2,\quad
                    N=x^2+xy+y^2.
 \tag{IF.42}
\]
The first forward edge is Q0 from a vertical seed.  Its target
weights are (1,1,-2).  IF.39 sends the derivative difference in
IF.41 to the homogeneous prism solution with constant E=-16=8D.
Thereafter the affine morphism is exactly
\[
 V_\infty=\tfrac43V_6,\qquad
 \delta_{\infty,i}-\tfrac43\delta_{6,i}=\frac{8D}{w_i}.
 \tag{IF.43}
\]
Indeed the selected target stable difference is the negative of
the old selected difference, and
\[
                   \frac{D'}{w'_2}=-\frac{D}{w_i}
 \tag{IF.44}
\]
for both Q0 and Q1.  This proves IF.43 on each target by the full
uniqueness argument IF.40, not only on its selected entry.  The
return increment of the difference
\(S_\infty-\tfrac23S_6\) is \(2D/w_i\).  The exact target
weights are (x+y,y,-x-2y) at Q0 and (x,x+y,-2x-y) at Q1, so direct
substitution gives
\[
                         N'-N=-2D/w_i.
 \tag{IF.45}
\]
The first-step difference changes from -1/3 to -7/3, while N changes
from 1 to 3.  Induction with IF.45 therefore gives the complete integer
evaluation
\[
 \boxed{\displaystyle
 S_\infty(P)=\frac23\bigl(S_6(P)+1\bigr)
                   -\bigl(x^2+xy+y^2\bigr),\qquad
 (x,y)^t=P^{-1}(0,1)^t.}
 \tag{IF.46}
\]
For a vertical basis this is IF.20.  Under all identical-fan arrows
IF.32 the norm N is unchanged: they permute the three entries of w
up to a common sign, and \(N=(w_0^2+w_1^2+w_2^2)/2\).
The actual integer algorithms use the same canonical representative,
so IF.46 applies to every unimodular input, including determinant -1.

The construction above proves S_infinity is an integer.  IF.46 then
implies 3 divides S6+1, since 2 and 3 are coprime.  Its first term is
therefore even.  The pair (x,y) is primitive; modulo 2 the three
possible nonzero pairs all have N=1.  Hence every selected-infinity
return is odd modulo 28.  This is an upper-image proof for all inputs.

Here are actual canonical bases, finite words from T0, and full
integer path sums exhibiting every permitted residue.  A word lists
the successive Q0/Q1 arrows of IF.34--39.

| Residue | Basis rows | Word | Integer path sum |
|---|---|---|---:|
| 1 | (6,-7); (-5,6) | 0111110 | -17639 |
| 3 | (3,-1); (-2,1) | 011 | -165 |
| 5 | (9,-5); (-7,4) | 011101 | -21415 |
| 7 | (5,-4); (-1,1) | 00001 | -385 |
| 9 | (1,-2); (0,1) | 00 | -19 |
| 11 | (4,-1); (-3,1) | 0111 | -465 |
| 13 | (2,-1); (-1,1) | 01 | -43 |
| 15 | (3,-5); (-1,2) | 0010 | -601 |
| 17 | (7,-3); (-2,1) | 00011 | -991 |
| 19 | (1,-3); (0,1) | 000 | -37 |
| 21 | (1,-1); (0,1) | 0 | -7 |
| 23 | (1,-4); (0,1) | 0000 | -61 |
| 25 | (7,-10); (-2,3) | 000110 | -6667 |
| 27 | (1,-7); (0,1) | 0000000 | -169 |

Each determinant is one.  The certificate saves every full V and
delta along these paths.  Thus the exact image is
\(\{1,3,5,\ldots,27\}\), using actual maps and integer degrees.

## IF.7. Independent exact equation checks and scope

The program
`code/part3_fourfold/e6_selected_infinity_all_fans.py` uses Fraction
arithmetic and fresh rational row reduction of the ten literal
equations for the six symmetric variation entries and three stable
derivative entries.  It checks rank nine, consistency, every original
equation, integrality, the selected inverse and actual right degree.
It does not call the closed solution IF.40 in these solves.

The exact run checks 6,504 unimodular inputs with entry bound 18,
representing 814 fans, and solves 1,840 distinct complete systems.  An
independent three-edge traversal checks 210 states through depth 7;
the four transitions requiring another fixed vertical seed are left
to the separately proved IF.20 seed.  It checks all signed vertical
indices from -40 through 40, the full coefficient-map inverses, both
symbolic identities IF.44--45, the complete affine relation IF.43
and all fourteen displayed witnesses.  The current run passes 283,285 exact
assertions.  The finite counts audit the equations; the full geometric
construction, Euclidean termination and parity proof give the stated
unrestricted result.

The fixed original scalar, the full positive epsilon loop, the stated
M6 and quadratic-cap family, its finite character/reference and the
original selected height have been kept throughout.  The proof
constructs these returns on every selected lattice-basis fan.  All
claimed integers are calculated from their actual normal products
and characteristic maps before the final reduction modulo 28.

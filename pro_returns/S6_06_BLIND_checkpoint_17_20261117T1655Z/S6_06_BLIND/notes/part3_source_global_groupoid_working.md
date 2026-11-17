# The actual global rho family and its loop groupoid

Proved as P3K.58 after the root and independent infinity-dictionary
audits. RG.1--6 retain two source-zero fan objects and the
full infinity dictionary. RG.7 applies the independently audited
infinity excision to compute their paired sum. No individual
source-zero class is assigned. The earlier version with unevaluated
infinity term is preserved in
records/attempts/source_global_groupoid_before_infinity_corollary/.

Fix one of the two E7 one-cap data:
\[
 (a,b,m)=(1,2,4p)\quad\hbox{or}\quad(2,1,4p-1),
 \qquad n=\pm1,\quad N=km,\quad k>0.
\]
The marked scalar is \(\lambda(v)=v^N\lambda_0\). Put
\[
 v=\rho^2-1,\qquad
 E_v:\ Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
 \quad T_0=v^2-2v.
\]

## RG.1. A bounded parameter surface and its actual charts

Take a large finite \(R>2\), and remove small disjoint discs around
\(\rho=-1,0,1\) from the disc \(|\rho|\le R\). Denote this compact
four-holed surface by \(B_R\). Its two points over \(v=1/8\) are
filled using the actual family of K53. We choose \(\lambda_0\) in
the common contracting range on this compact parameter surface.
This does not presume that the same fixed scalar remains
contracting throughout a punctured neighbourhood of infinity.

All source equations and the canonical Cartier divisors are the
ones displayed above. The discriminant of their cubic in \(X\),
viewed as a polynomial in \(T\), has parameter discriminant
\[
 16v^2(v+1)^6(1-8v)^3.
\]
Thus on this bounded parameter surface the only excluded source
degenerations are the two source-zero lifts and the selected
collision. The unselected type-II point is precisely the disc
already constructed in K53.

Choose a single cap-overlap annulus sufficiently far out in the
\(T\)-plane to avoid all finite critical values for the compact
range of \(v\). The III-star root equations are
\[
 y'^2=x'^3+(1-2v)z^{2p}x'^2+
 \begin{cases}x',&m=4p,\\zx',&m=4p-1,\end{cases}
 +v^2z^{6p},\qquad G'=(0,vz^{3p}).
\]
Their central models, finite kernel branch and root-line
corrections are the ones in K49 and K53. They are uniform for
bounded \(v\) after shrinking the root disc. The norm-ratio has
the actual nonzero central value \(-2\) or \(+2\), respectively.
Consequently its logarithm and chosen root extend on the root
disc times the bounded \(v\)-disc with that reference value.
The same finite averaging preserves the literal root equation
\(A_0^m=B_0^n\) and every finite character. No cube root of \(v\)
is used to define these global cap charts.

The full reference annular map \(F_0\) of K49 is continued on
this fixed cap annulus. Its regular elliptic source, root,
Cartier and norm maps are holomorphic for every \(v\) in that
bounded disc, including zero. The parameter-disc exponential
lifting and the fixed-contour Cauchy splitting of RCZ.5 therefore
apply on the entire bounded disc, with the same full reference
map. One may choose the fixed cap annulus this large at the
initial reference; transport to it is through the literal source
and cap charts, carrying every integral annular period. The
construction retains the entire reference \(d\delta\) and the
reduced doubled period. Its restriction near \(v=0\) is the
marked continuation used in K49.

The selected cusp has the exact normalization
\[
 X=s^2-1,\qquad Y=s(s^2-\rho^2),\qquad
 Z=\frac{s-\rho}{s+\rho}.
\]
The marked point \(G\) is \(s=-1\), so
\[
 P_G=\frac{1+\rho}{1-\rho}.
\]
It is a nonzero finite function on \(B_R\). The unique small
Tate period and the physical height \(q_1=T-T_0\) satisfy
\[
 \left.\frac{Q}{q_1}\right|_{q_1=0}
       =-\frac{v}{64(v+1)^3}
       =-\frac{\rho^2-1}{64\rho^6}.                 \tag{RG.1}
\]
The actual unit \(Q/q_1\), not just its leading coefficient, is
retained in the charts. The chosen fourth root of the nodal
\(c_4\) is \(2\rho\). Hence the Tate source coordinate is fixed
over the rho surface; there is no unrecorded branch interchange.
The lift of \(G\) is fixed by its displayed finite nodal limit.
Any alternative continuation differing by \(Q^j\) would have
limit zero or infinity for \(j\ne0\), so that integral ambiguity
does not occur. The theta/Cartier line map then fixes the line
coordinate as well.

A chosen periodic cusp fan \(\mathcal T\) therefore gives actual
toric charts over this entire bounded parameter surface.
Nonzero unit windings in (RG.1) and \(P_G\) remain in their
transition maps; no logarithm is used to discard them.
The uniform norm shells, finite caps and compact-base gluing
give a smooth proper sphere family over \(B_R\), with the
prescribed physical circle. The cap and selected-cusp charts
just specified identify the actual endpoint groupoid below.

## RG.2. The full scalar cut and its forward endpoint arrows

Choose \(t=\log v/(2\pi i)\) on parameter cuts and
\[
 s_\infty=\frac{\log q_\infty}{2\pi i},\qquad
 h=1-T_0(v)q_\infty,\qquad q_1=q_\infty^{-1}h.
\]
The actual ordinary-to-cap cochain is
\[
 F_t=F_0+nk\,t\,s_\infty\delta.
\]
For an integer change \(t\mapsto t+w\), its forward arrows are
\[
 R^{\rm ord}_w=q_1^{nkw},\qquad
 R^{\rm cap}_w=h^{nkw}.                              \tag{RG.2}
\]
Multiplication here denotes the actual line maps. Their square is
\[
 F_{t+w}\circ R^{\rm ord}_w
        =R^{\rm cap}_w\circ F_t,                     \tag{RG.3}
\]
because the additional factor in \(F\) is \(q_\infty^{nkw}\).
This retains the direction: \(R_w\) is the map from the initial
lifted fibre to the terminal lifted fibre. The physical forward
return uses its inverse as the closing arrow.

These are maps of every retained local model. On the cap, \(h\)
is an invariant nonzero unit, so its multiplication commutes
with the root, source, line and norm maps. At the selected cusp,
\(q_1^{nkw}\) is its integral line-height translation. Reindexing
by the corresponding suspension period leaves a bounded toric
multiplier, with its full source and line factors. Thus it
extends through the periodic fan as the actual integral
reindexing. Its inverse extends too. The finite characters and
the total cyclic lattice cocycle stay in \(A_0^m=B_0^n\).

The scalar-root parameter itself is single valued:
\[
 r=v^k r_0,\qquad r_0^m=\lambda_0,\qquad
 A=r^nA_0,\quad B=r^mB_0.
\]
The cut in (RG.2) is consequently the retained annular gluing
cut, not a newly inserted root character. The arrows obey
\(R_{w+w'}=R_{w'}R_w\) literally. For the positive local rho
loops the integers are
\[
 \begin{array}{c|rrrr}
 \text{puncture}&-1&0&1&\infty\\ \hline
 \operatorname{wind}v&1&0&1&-2\\
 \operatorname{wind}r&k&0&k&-2k .
 \end{array}                                           \tag{RG.4}
\]
The infinity orientation in this table is the positive
\(\epsilon=1/\rho\) orientation.

### RG.2a. The actual source-zero closing on every cusp chart

Near the lift \(\rho=1\), retain the two-node Tate/Cartier
coordinates of SZ.39--44. With \(q=q_1\), their periods are
\[
 h:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 g_{\rm per}:(Z,V)\mapsto(gZ,\eta qV),
\]
where
\[
 \kappa=q_2u_Q,\quad \alpha=P^a,\quad
 g=P^{-b},\quad
 \eta=2(-1)^{b+1}\lambda_0v^Nc_X^{-2},\quad
 P=q_2^{-1}u_P,\quad c_X=q_2u_X.
                                                        \tag{RG.4a}
\]
All the displayed \(u\)'s are the actual nonzero two-node
units with their extending logarithms. At \(q_1=0\), the
function \(q_2\) has a simple zero in \(v\). A positive \(v\)
loop therefore has the complete period-unit winding matrix
\[
 \begin{pmatrix}
  \operatorname{wind}\kappa&\operatorname{wind}g\\
  \operatorname{wind}\alpha&\operatorname{wind}\eta
 \end{pmatrix}
 =
 \begin{pmatrix}1&b\\-a&N-2\end{pmatrix}.              \tag{RG.4b}
\]
Its trace is \(N-1\). In particular the three raw normal
determinants in the labelled six-chart plumbing have that
winding; for even \(N\) their underlying real normal loops
are nontrivial in \(\pi_1(SO(4))\). The fixed-labelled-vertex
ordinary product used for the selected rho loop is not used
in this source-zero comparison.

The endpoint itself is also retained. Put \(L=nk\). The
forward arrow of (RG.2) at this puncture is
\[
             R_{\rm ord}:(Z,V,q)\mapsto(Z,q^LV,q).
                                                        \tag{RG.4c}
\]
For the two triangle charts
\[
 T^+_{i,j}:\quad q=x_0x_1x_2,\quad Z=q^ix_1,\quad V=q^jx_2,
\qquad
 T^-_{i,j}:\quad q=y_0y_1y_2,\quad
 Z=q^iy_0y_1,\quad V=q^jy_0y_2,
\]
this sends the index \((i,j)\) to \((i,j+L)\), with the
three chart coordinates unchanged. To return to the chosen
index representatives apply the actual period
\(g_{\rm per}^{-L}\). On their dense tori the resulting map is
\[
             (Z,V)\mapsto(g^{-L}Z,\eta^{-L}V).        \tag{RG.4d}
\]
Consequently its literal maps in the named charts are
\[
 \begin{split}
 T^+:\ &(x_0,x_1,x_2)\mapsto
       ((g\eta)^Lx_0,g^{-L}x_1,\eta^{-L}x_2),\\
 T^-:\ &(y_0,y_1,y_2)\mapsto
       ((g\eta)^{-L}y_0,\eta^Ly_1,g^Ly_2).
 \end{split}                                         \tag{RG.4e}
\]
These formulas retain the complete bounded multipliers at the
endpoint, rather than replacing the endpoint by identity in
the six named charts. Every exponent is integral. They glue
by the actual period maps and extend to the toric boundaries.
For another periodic fan the same proof uses its character
matrix: (RG.4c) translates every height-one vertex by
\((0,L)\), and (RG.4d) is the remaining bounded torus map.
The physical return uses the inverse of (RG.4e) after path
transport. The cap endpoint is the unchanged-index map
\[
       (X_j,Y_j)\mapsto(h^LX_j,h^{-L}Y_j)
\]
with its actual finite root action retained. Equations
(RG.3) and (RG.4c--e) give their full common overlap.

The opposite source-zero lift is obtained by the literal
reflection in RG.3; its fan is \(J\mathcal T\), and its
closing is the conjugate of these full maps. No identity
closing, labelled product, or omitted chain reindexing is
assumed in (RG.8).

## RG.3. Reflection as an actual arrow between the two fan objects

At \(-\rho\) the source and cap data depend on the same \(v\).
The selected normalization exchanges its two branches. The
literal Tate and line map is
\[
 \mathcal R_\rho:\ (Z,V)\longmapsto(Q/Z,V),
 \qquad P\longmapsto P^{-1}.                          \tag{RG.5}
\]
It is the identity on the underlying marked source and its
Cartier divisor, expressed in the two actual Tate coordinate
systems. The line arrow follows from the theta identities,
without a suppressed multiplier:
\[
 \frac{\Theta_Q(QP/Z)}{\Theta_Q(Q/Z)}
       =\frac{\Theta_Q(Z/P)}{\Theta_Q(Z)}.
\]
For \(M_a\), apply the same identity to \(P^a\), retaining its
actual Cartier representative. The ordinary source, cap and
\(F_0\) maps are carried identically because they depend on
\(v\). Equation (RG.3) is also intertwined, since \(q_1,h\) are
unchanged and the line coordinate in (RG.5) is unchanged.

The fan map in the original lattice is
\[
 (x_Z,x_V,h)\longmapsto(-x_Z+h,x_V,h).
\]
Its linear two-dimensional part is
\(J=\operatorname{diag}(-1,1)\); the integral height translation
and the nonzero unit \(Q/q_1\) are retained. This gives the
actual arrow
\[
 \mathcal X_{\mathcal T,\rho}\longrightarrow
             \mathcal X_{J\mathcal T,-\rho}.
\]
Its square is the identity on all charts, including the cap.
It preserves the physical circle and the complex orientation.
The parameter map \(\rho\mapsto-\rho\) has positive local
complex degree one at both source-zero lifts.

Let \(Z_{\mathcal T}\) denote the positive return near
\(\rho=1\), with its actual full marked data, and let
\(Z^-_{\mathcal T}\) denote that near \(\rho=-1\). Then the
actual family arrow (RG.5) proves
\[
                  [Z^-_{\mathcal T}]=[Z_{J\mathcal T}]. \tag{RG.6}
\]
This does not identify \(Z_{\mathcal T}\) with
\(Z_{J\mathcal T}\). The two fan objects remain distinct inputs
to the loop relation.

## RG.4. The cut-surface groupoid relation and the selected loop

Choose a rectangular outer boundary containing the three holes,
with disjoint vertical slits from their lower points to its
lower edge. Use its lower-right point as basepoint. Walking the
boundary of the cut-open disc, and then reversing that boundary
word, gives based positive meridians in the order
\[
             \gamma_+\gamma_0\gamma_-\gamma_\infty=1. \tag{RG.7}
\]
Concatenation in this equation means traversal from left to
right. The outer positive infinity meridian is clockwise in
the rho plane. The slit paths give actual transport maps from
the reference fibre to the four local fibres.

Choose a smooth connection for the actual family over the
cut surface, averaged over the physical circle. On a lifted
parameter path, let \(P_\gamma\) be its transport. Its endpoint
in the reference fibre is
\[
             \Phi_\gamma=R_{w(\gamma)}^{-1}P_\gamma,
\]
with (RG.2), and with the slit-path conjugations included.
The total integer in (RG.7) is \(1+0+1-2=0\), so its total
closing arrow is literally \(R_0=1\). A contraction of the
cut-disc boundary gives, by lifting its paths through this
connection, an isotopy of the product of its four actual
physical returns to the identity. Thus, as arrows on the
reference oriented sphere,
\[
       \Phi_\infty\Phi_-\Phi_0\Phi_+\simeq\operatorname{Id}.
                                                               \tag{RG.8}
\]
No fibrewise conjugacy alone is used to deduce this relation.
It comes from the actual family on the cut surface and its
literal endpoint maps.

Near \(\rho=0\), take the analytic cube root \(u^3=v\) with
\(u(0)^3=-1\). In the \(G=(0,1)\) source coordinates put
\[
 \xi=x-u,\qquad \sigma=\rho/u.
\]
The selected curve is exactly
\[
 y^2=\xi^2(\xi+\sigma^2),\qquad
 q=\frac{y^2-\xi^2(\xi+\sigma^2)}{\xi+u}.
\]
These are the actual F56 source coordinates. The parameter
\(\sigma=\rho/u\) has nonzero complex derivative \(u(0)^{-1}\).
The normalized source point has
\(s_{\rm norm}=s/u\), so its Tate coordinate is exactly
\((s-\rho)/(s+\rho)\), with no further reflection. The
Cartier and root maps are the analytic local coordinate maps
of K49/F51; their parameter units have extending logarithms.
The scalar ratio
\(\lambda(v)/\lambda(-1)\) has an extending logarithm on this
disc. Its explicit homotopy through that logarithm, with the
same root/line cochains, identifies the positive local return
with F56's fixed-scalar return. For the initial fan and its
reflected fan, K45/F56 therefore give
\[
                         [\Phi_0]=1.
\]
The two unselected points over \(v=1/8\) have the actual
disc extensions of K53 and give zero returns.

Write \(I_{\mathcal T}\) for the positive infinity return in
this actual bounded-parameter family. Applying the oriented
mapping-class identification with \(\Theta_7\), and using the
actual slit-path conjugations in (RG.8), gives
\[
 [Z_{\mathcal T}]+[Z_{J\mathcal T}]+1+[I_{\mathcal T}]
                  =0\quad\hbox{in }\Theta_7.          \tag{RG.9}
\]
Conjugation disappears here because this oriented group is
abelian; the underlying family arrows were retained before
passing to it. K49 separately identifies each original
positive \(u\)-return with three positive \(v\)-returns.
No value or division is assigned to either source-zero term.
The infinity term is evaluated by the separately proved excision
in RG.7 below.

## RG.5. The infinity scalar path and the independent scalar parameter

The term \(I_{\mathcal T}\) is defined by the actual positive
\(\epsilon=1/\rho\) loop, before any change to the infinity
source coordinates. Its literal scalar is
\[
 \lambda=(\epsilon^{-2}-1)^N\lambda_0,\qquad
 r=\epsilon^{-2k}(1-\epsilon^2)^k r_0.                \tag{RG.10}
\]
The unit \((1-\epsilon^2)^k\) has an extending logarithm;
using that logarithm gives an actual based homotopy to a
root-scalar loop of winding \(-2k\). At a fixed sufficiently
small epsilon circle, all amplitudes are chosen in a common
contracting range.

For clarity, one can use the actual source construction with
independent root-scalar variable \(r\). Its maps are
\[
 B=r^mB_0,\qquad A=r^nA_0,\qquad
 F=F_0+n\frac{\log r}{2\pi i}s_\infty\delta.
\]
The positive \(r\)-loop has the full forward arrows
\(q_1^n\) and \(h^n\). These commute with the retained source
charts and finite groupoid maps, so this is an actual family
over the epsilon annulus times a small \(r\)-annulus. The
parameter square \((\epsilon,r)=(\epsilon_*e^{2\pi is},
r_*e^{2\pi i(ps+qt)})\) gives the usual product-parameter
homotopies with all those endpoint arrows retained.

Denote by \(I_{\mathcal T}(j)\) the actual coupled loop of this
family with one positive epsilon turn and \(r\)-winding \(j\).
Then
\[
 I_{\mathcal T}(j)-I_{\mathcal T}(j')
       =(j-j')A^{\rm scalar}_{\mathcal T}.             \tag{RG.11}
\]
This is a comparison of actual loops in the same constructed
two-parameter family. In particular \(I_{\mathcal T}\) in
(RG.9) is \(I_{\mathcal T}(-2k)\). A different local rescaling
\(\lambda=\epsilon^{N_\infty}\lambda_\infty\), with
\(N_\infty=k_\infty m\), is the distinct loop
\(I_{\mathcal T}(k_\infty)\), with difference
\[
 I_{\mathcal T}(-2k)-I_{\mathcal T}(k_\infty)
       =-(2k+k_\infty)A^{\rm scalar}_{\mathcal T}.
\]
An identification of the latter loop with another infinity
model must carry that model's complete source, root,
Cartier, annular and normal arrows. RG.6 supplies this
annular dictionary; only afterward does RG.7 use the
separately proved infinity excision.

For the initial and reflected vertical-edge fans the actual
fixed-source page calculation K26 and the literal C2 native
comparison K62 give
\[
 A^{\rm scalar}=0\quad(a,b,m)=(1,2,4p),\qquad
 A^{\rm scalar}=1-3p\quad(a,b,m)=(2,1,4p-1).
\]
This scalar input does not identify the two source-zero fan
returns in (RG.9).

## RG.6. Full comparison with the marked infinity source

This paragraph supplies the punctured-family arrow to the infinity
presentation IF.1--6. It uses that presentation's full reference
overlap, defined by transport of the global reference at one
nonzero epsilon. It does not identify a central collision attachment
or infer the characteristic value of its boundary.

The source, section and actual selected height map are
\[
 v=\epsilon^{-2}-1,\quad
 X=\epsilon^{-2}x,\quad Y=\epsilon^{-3}y,\quad
 T=\epsilon^{-4}t,\quad
 g=\epsilon(1-\epsilon^2),\quad
 q_{1,\rm old}=\epsilon^{-4}q_{*,\rm new}.
                                                        \tag{RG.12}
\]
They give exactly
\[
 y^2=x^3+(-2+3\epsilon^2)x^2+tx+
              \epsilon^2(1-\epsilon^2)^2,\quad G=(0,g),
\qquad
 t_*=(1-\epsilon^2)(1-3\epsilon^2).
\]
The selected normalization coordinate changes by
\(s_{\rm new}=\epsilon s_{\rm old}\). Therefore
\[
 Z_{\rm old}=\frac{s_{\rm old}-\rho}{s_{\rm old}+\rho}
            =\frac{s_{\rm new}-1}{s_{\rm new}+1}
            =Z_{\rm new}.
                                                        \tag{RG.13}
\]
The Tate period \(Q\) and marked \(P\) agree literally.
The physical-height units satisfy
\[
 \kappa_{\rm old}=\epsilon^4\kappa_{\rm new},\qquad
 P=-\frac{1+\epsilon}{1-\epsilon},\qquad
 \left.\kappa_{\rm new}\right|_{q_*=0}
                       =-\frac{1-\epsilon^2}{64}.
\]
Every nonconstant unit in these equations is retained. The
integer epsilon power is a toric unit on the punctured parameter
annulus, with its winding; the selected fan is unchanged by
(RG.13).

The Cartier map is the canonical divisor map, not an identification
only of generic Picard classes. The primitive lift satisfies
\[
 I_\epsilon U_{a,\rm old}I_\epsilon^{-1}
                  =\epsilon^{2a}U_{a,\rm new}.
                                                        \tag{RG.14}
\]
Since \(ab=2\), its \(b\)-th power cancels exactly the
\(\epsilon^{-4}\) in the selected height. Thus
\[
 I_\epsilon\bigl(2(-1)^{b+1}\lambda
             q_{1,\rm old}U_{a,\rm old}^{\,b}\bigr)
 I_\epsilon^{-1}
       =2(-1)^{b+1}\lambda q_{*,\rm new}U_{a,\rm new}^{\,b}.
                                                        \tag{RG.15}
\]
The Hom section itself provides a second literal check. With
\[
 F_{21}=\frac{Y+v+TX/(2v)}X,\qquad
 F_{12}=\frac{Y-v-TX/(2v)}X
\]
in the old presentation, substitution gives
\(F_{ab,\rm old}=\epsilon^{-1}F_{ab,\rm new}\) and
\(v=\epsilon^{-3}g\). Hence
\[
       \frac{q_{1,\rm old}}{vF_{ab,\rm old}}
               =\frac{q_{*,\rm new}}{gF_{ab,\rm new}}. \tag{RG.16}
\]
This retains the actual degree-two Cartier correction as well.
In particular the scalar in (RG.10) is unchanged.

On the logarithmic epsilon cover, the cap comparison is
\[
 z_{\rm old}=\epsilon^{4/m}z_{\rm new}.
                                                        \tag{RG.17}
\]
For \(m=4p\), its minimal source coordinates \(X',Y'\) are
unchanged. For \(m=4p-1\), the old-to-new arrow multiplies
them by \(\epsilon^{-2/m},\epsilon^{-3/m}\). It carries the
marked section, source resolution ideals and every Cartier
correction by their actual coordinate maps. Its full positive
epsilon endpoint is
\[
 D_{\rm new}^{-4}:\quad
 (z,X',Y')\mapsto
 (\zeta_m^{-4}z,\zeta_m^{-2}X',\zeta_m^{-3}Y')
                                                        \tag{RG.18}
\]
in the reduced case; the last two factors are one in the good
case. The ordinary and cap source arrows commute with the
specified finite root maps on each parameter chart.

Here is the completion of that endpoint on the affine line
atlas. Write \(A_0=L D\), with \(L\) covering the specified
signed division translation. The central finite commutator
character is one: in the good root the division point is \(O\);
in the reduced root the actual line
\(\mathcal O(2G'-O)\) restricts to the trivial line on the
compact reduced III fibre. Its commuting source maps have
constant line multipliers there. The finite eigenspace
average, retaining its actual conjugating unit, therefore
gives \(DLD^{-1}=L\). In this actual atlas
\[
                         A_0^4D^{-4}=L^4.
                                                        \tag{RG.19}
\]
The latter extends and has identity central source translation
in both branches; after its central scalar is retained it has
the small extending Lie logarithm. For the reduced branch the
annular comparison still contains
\[
                    4\log R-\log(4R)=2(1+i).
                                                        \tag{RG.20}
\]
The signed source part is multiplied by \(n\), and its line
part is the actual Cartier factor of automorphy. This entire
period is included in the total atlas cochain. It is not
replaced by the small logarithm or suppressed in (RG.19).

To specify the annular marking, fix one nonzero
\(\epsilon_*\), transport the full global ordinary-to-cap
map through (RG.12--17), and use that entire map as the
infinity reference \(F_*\). It includes the given integral
\(d\delta\) and all finite characters. The cap-overlap source
and Cartier family is smooth over the full epsilon disc:
its base annulus avoids the unselected collision and the
selected fibre. The actual root division branches, norm
units and their equivariant line lifts extend on the cap.
Their nonzero norm-ratio has the fixed central value \(+2\)
or \(-2\), including at \(\epsilon=0\).

Continue \(F_*\) by the parameter-disc exponential lifting
on every ordinary and finite groupoid overlap, and solve the
remaining vector cochains by the fixed source-base Cauchy
contours of RCZ.3 and RCZ.5. At the reference fibre the full
maps agree, so every integral overlap and cyclic-group
discrepancy is zero there. It is locally constant and hence
zero throughout the parameter disc. The nonzero doubled
period (RG.20) is kept when changing logarithmic parameter
charts; the two compared total cocycles carry the same
term. Before taking a Lie logarithm at the reduced root,
use the actual suspension power to remove its component
translation. Finite averaging is applied to vector
cochains, not to lattice components. The root line
exponentials extend by the actual resolved Cartier maps.
This constructs precisely IF.3's full \(F_0\), with its
reference, rather than choosing an unmarked overlap.

For clarity, the scalar closing defect is explicit. Put
\[
 t_\epsilon=\frac{\log\epsilon}{2\pi i},\qquad
 \ell(\epsilon)=\frac{\log(1-\epsilon^2)}{2\pi i}.
\]
Then \(t_v=-2t_\epsilon+\ell(\epsilon)\).
The old and new ordinary forward arrows for the positive
epsilon loop are \(q_{1,\rm old}^{-2nk}\) and
\(q_{*,\rm new}^{-2nk}\). Their ratio is
\(\epsilon^{8nk}\). The obligatory scalar cochain on the
logarithmic parameter cover is
\[
 c_0(t_\epsilon)=
       \exp\{-2\pi i\,4nk\,t_\epsilon(t_\epsilon-1)\},
 \qquad
 \frac{c_0(t_\epsilon+1)}{c_0(t_\epsilon)}
                              =\epsilon^{-8nk}.
                                                        \tag{RG.21}
\]
The unit \((1-\epsilon^2)^k\), its actual logarithm and
the corresponding cap unit \(h\) remain in the full
ordinary-to-cap square. Equation (RG.21) is a cochain in
that square, not by itself a single-valued global scalar.
The cap correction (RG.19), the source and line maps, and
the remaining vector cochain are carried simultaneously.

The two local family comparisons on angular parameter
charts now differ by an actual global extending
translation. The rational source-section and line
valuation argument of RCZ.4 applies to these marked
punctured E7 sources and identifies this map with a
holomorphic physical scalar. Factor that scalar on the
two-chart epsilon annulus by RCZ.4's literal
Cauchy--Green solution: for its overlap logarithm
\(\ell_c\), set \(b_+=\chi_-\ell_c\),
\(b_-=-\chi_+\ell_c\), solve
\(\bar\partial v=\bar\partial b_\pm\) using
\(1/(\pi(\epsilon-w))\), and use
\(e^{b_\pm-v}\). The two adjusted actual maps then glue
on both overlap components. This retains the scalar
winding, (RG.21), the full finite cocycle and (RG.20).

Thus on the punctured parameter annulus the global
infinity restriction is carried to IF's actual source,
Cartier, cap and \(F_0\) family with the literal scalar
\((\epsilon^{-2}-1)^N\lambda_0\). Its positive return
is \(I_{\mathcal T}(-2k)\) in (RG.11), using the inverse
closing arrows on both sides. This is an annular family
morphism; it asserts neither a central filling nor
any equality between the two source-zero fan returns.

Finally the reflected source descriptions match through
one actual period. IF's half-turn arrow is
\(\mathcal I_\epsilon(Z,V)=(1/Z,P^aV)\).
At the target \(P_{\rm target}=P^{-1}\), so
\[
        h_{\rm target}\circ\mathcal I_\epsilon
                  =(Q/Z,V)=\mathcal R_\rho .
                                                        \tag{RG.22}
\]
This is the exact quotient arrow, with its integral
height reindexing and all its unit factors. It is the
reflection used in (RG.6), rather than an additional
unmarked endpoint identification.

## RG.7. The actual paired source-zero returns

This conclusion has the initial fan \(\mathcal T_0\) and
its reflected fan \(J\mathcal T_0\) as its precise scope.
It retains the one III-star cap, its prescribed finite
character, the full \(F_0\), the norm sign \(n=\pm1\),
and the original scalar
\(\lambda=v^N\lambda_0\) with \(N=km\), \(k>0\).
No additional logarithmic disc is introduced at either
colliding finite site.

The actual infinity collision excision IE.1--6 of
P3K.57 computes the fixed-scalar positive epsilon
return in the marked IF source/cap family:
\[
 \begin{array}{c|c}
 (a,b,m)&I^{\rm fixed}_{\mathcal T}\\ \hline
 (1,2,4p)&0\\
 (2,1,4p-1)&1 .
 \end{array}                                            \tag{RG.23}
\]
The two entries apply to each of the two stated fan
objects, with the actual positive physical orbit and
Jin-to-\(\Theta_7\) transfer of that excision. Its local
Euler-line bordism and cap cancellation establish this
input independently of the groupoid relation.

To pass from (RG.23) to the actual global infinity loop,
use the family with independent root-scalar variable
constructed in RG.5. On a fixed small epsilon circle,
the unit \((1-\epsilon^2)^k\) in (RG.10) has the actual
extending logarithm. Multiplying its argument by
\(s\in[0,1]\) gives a based parameter homotopy that
retains the cap root and the full annular cochain.
The resulting loop has one positive epsilon turn and
exactly \(-2k\) positive \(r\)-turns. In the actual
two-parameter family its based loop is the product of
the fixed-scalar source loop and \(-2k\) scalar loops.
The endpoint squares are (RG.2--3) and (RG.21), with
the finite root and Cartier arrows already matched
by RG.6. Thus the relation is one of the actual
completed family returns, not a substitution into a
characteristic formula:
\[
             I_{\mathcal T}
                  =I^{\rm fixed}_{\mathcal T}
                         -2kA^{\rm scalar}_{\mathcal T}.
                                                        \tag{RG.24}
\]
K26 and the actual C2 characteristic comparison K62 give
\(A^{\rm scalar}=0\) in the good branch
and \(A^{\rm scalar}=1-3p\) in the reduced branch,
for these two actual fan objects. Therefore
\[
 \begin{array}{c|c|c}
 (a,b,m)&I_{\mathcal T}
                 &[Z_{\mathcal T}]+[Z_{J\mathcal T}]\\ \hline
 (1,2,4p)&0&-1\\
 (2,1,4p-1)&1-2k(1-3p)&-2+2k(1-3p)
 \end{array}
 \qquad\text{in }\Theta_7\cong\mathbb Z/28.             \tag{RG.25}
\]
The last column is (RG.9), with its already proved
selected-cusp term \(1\), actual zero unselected
term, and the two separate source-zero fan objects.
It is valid for both retained norm signs. The original
positive \(u\)-returns are separately the cubes of
these positive \(v\)-returns by K49; that is an actual
covering-family statement, not division of a class.

Equation (RG.25) determines only the paired sum.
Neither individual source-zero return, nor an equality
between those two fan returns, is assigned here.
The ordinary-product obstruction and the full
source-zero closing of RG.2a remain part of the
construction.

Root has audited RG.1--6 and independently checked
the two paired formulas. Fourfold has independently
audited RG.1--3, RG.5 and the complete RG.6 dictionary.
The source/cut/closing identities and the paired
arithmetic are executed in
code/part3/source_global_groupoid.py.

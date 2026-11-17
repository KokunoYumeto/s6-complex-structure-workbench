# The exact local integer calculation for bottom-row winding

Proved as P3K.76 after the full root audit, checks relative-calibration audit, and fourfold shorter-C0 audit, 17 November 2026. This note constructs and compares the
completed primitive nodal orbit pieces with full fixed-source periods
\[
 h:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\mapsto(gZ,q\eta V),
\]
whose source units $\kappa,g$ have zero parameter winding and whose
line multipliers have windings $(L,J)$. The full bounded factors and
the actual closed torus seam are retained. It extends the local
calculation SI.1--5; an application to a named family must use that
family's actual primitive period and cap dictionary. This note does
not identify a different period basis by its winding numbers alone.

## BW.1. The actual line tensor, including its outer gauge

Use the closed coordinates of the actual torus seam. A source-independent
bounded rescaling $(A,D)$ acts by the two literal vertex maps (SI.4)
and intertwines every period row. The endpoint equality $C_1E=C_0$
is retained on full collars. In these coordinates write
$\alpha=e^{2\pi iL\theta}\alpha_*$ and
$\eta=e^{2\pi iJ\theta}\eta_*$, with the full zero-winding factors
and their logarithms. The physical-circle quotient retains their
positive norms and the source factors. Its F9 source/graph construction
is therefore the same smooth piece $C$ for every $L,J$; the phase
changes remain on its actual circle line. The normal and cap maps
are exactly (SI.11)--(SI.13), with the physical height unchanged.

Let $b,\gamma:C\to\mathbb R/\mathbb Z$ be the two graph maps with
outer values $v,\gamma$. Each has a real lift on the fixed sphere
and can be made constant on the fixed surgery tube by its supported
real homotopy. The exact theta-cut gauge implementing this change
is its exponential times theta, as in SI.3. They then extend over the
same $D^3\times S^2$ cap. Define two actual lines on $\mathcal C$
by theta-cut coefficient gluings
\[
 T_b:\ w\mapsto e^{2\pi ib}w,\qquad
 T_\gamma:\ w\mapsto e^{2\pi i\gamma}w.
\]
Their real curvatures are
\[
 \Xi=d\theta\wedge db,\quad \Psi=d\theta\wedge d\gamma,
 \qquad \Xi^2=\Psi^2=\Xi\Psi=0.                    \tag{BW.1}
\]
Use the meridian-one line $U=M^*$, with the K68 physical orientation.
The actual period coefficients have theta deck
\[
 (u,d)\longmapsto(u,d-Lv-J\gamma).
                                                        \tag{BW.2}
\]
Hence the full boundary connection on $U$ is
\[
 A_{L,J}=dd+(\alpha_q+J\theta)d\gamma+L\theta\,dv.
                                                        \tag{BW.3}
\]
Differentiating the actual complex period expression (SI.14) retains
all unit phases and their derivatives. Equation (BW.3) is written in
those full coefficient coordinates, not in a constant-factor
approximation to the physical characters.

The exact coefficient theta clutch is the tensor product of those
for $T_b^L$ and $T_\gamma^J$. The meridian and regular $b\times\gamma$
evaluations remain respectively one and zero. The integral Thom,
Mayer--Vietoris and Wang computation of SI.3 leaves precisely these
four evaluations. It therefore gives
\[
 U_{L,J}\simeq U_{0,1}\otimes T_b^L\otimes T_\gamma^{J-1}.
                                                        \tag{BW.4}
\]
Here the symbol $U_{0,1}$ means the actual line obtained from this
piece by the displayed inverse theta-cut tensors. It is defined
before making a comparison to any reference family.

The isomorphism in (BW.4) carries its prescribed outer arrow, rather
than only its absolute Chern class. In the doubly cut coefficient
frames that arrow has the literal connection difference
$L\theta\,dv+(J-1)\theta\,d\gamma$. The only nonextending boundary
winding in $H^1(\mathcal B)/\operatorname{im}H^1(\mathcal C)$ is the
$q$ angle. Choose one theta value and the free section disc
$|Z_*|=1,V=1,\gamma=v=0$ used in (SI.23). On this disc both tensor
lines have their constant frame and the prescribed arrow is the
identity. It has no $q$-angle winding. The integral-logarithm and
partition-of-unity Cech construction of (SI.24), followed by the
extending theta, $b$, gamma gauges and the remaining real boundary
logarithm, makes (BW.4) exactly that outer arrow. Its inner cap gauge
extends over $D^3\times S^2\times S^1$. Thus (BW.4) is a relative
line morphism with its full boundary and cap marking.

## BW.2. The relative local pairing is calibrated by an actual map

We spell out the local reference comparison needed here. All four
zero-winding unit factors are nonzero on a protected $q$ disc. Choose
their actual logarithms. Between two specified sets of these factors
use
\[
 u_s=u_0\exp\bigl(s\log(u_1/u_0)\bigr),\qquad0\le s\le1.
                                                        \tag{BW.5}
\]
The ratios have the displayed holomorphic logarithms on a common
smaller disc. This is an explicit path of the full commuting torus
periods, not just a path of their leading coefficients. Their
$q$-valuation matrix remains the identity. Their logarithmic norms
are uniformly bounded on the compact path, so the same small disc
and the same finite fundamental regions give the toric quotients.
The period translations act freely on the labels of the fixed
unimodular charts; on the regular region the invertible real period
matrix gives the quotient. The resulting compact pieces with
boundary are a smooth family over $s$.
At the calibration endpoint take $\kappa,\alpha_*,g,\eta_*$
to be their fixed-parameter values, hence functions of $q$ only.
The zero-winding logarithms in (BW.5) give the displayed path to
these values; the endpoint normal matrices below are therefore
literally independent of the circle parameter.

The integer closing exponent $e$ is fixed throughout this path.
For the full bounded closing unit $u_s$ the actual bounded endpoint
and cut multiplier obey
\[
 E_s=(g_s^{-e},u_s\eta_s^{-e}),\qquad
 (C_s)_1=(g_s^e,u_s^{-1}\eta_s^e),\qquad
 (C_s)_1E_s=(C_s)_0=1.
                                                        \tag{BW.5a}
\]
Use the same endpoint-flat cut function on every $s$ chart. These
identities then hold on the entire collars with all jets. No
discrete annular exponent, finite root character or exterior cap
datum is varied. Only these compact local pieces and their
prescribed outer arrows occur in the comparison.

For the source parameter $Q_s=q\kappa_s$, the exact node horizontal
field is $\partial_s+(\partial_s\log\kappa_s)y\partial_y$ in
$xy=Q_s$. Prescribe the identity on the real source-period
coefficients on the entire outer collar. Interpolate the two
horizontal fields by a partition in their affine space of vertical
differences, as in (SI.10). For the suspension source factor $g_s$
use its full $\exp(\gamma\log g_s)$ untwisting. Positive line norms
use the F9 proper coordinate, with its two fixed endpoint lifts
$1/2+\varepsilon,1/2-\varepsilon$. Every coordinate comparison is
relative to the specified outer real coefficients. These are actual
flows and hence diffeomorphisms of the compact pieces.

The normalization graph isotopy stays in that same short arc with
distinct endpoint heights. Its velocity extends over the fixed tube.
The full unit normal factors in the two toric charts give its
Cartier/Hopf normal arrow; since the unit logarithms in (BW.5) extend,
their parameter-$s$ homotopies carry the entire normal jets and the
actual physical circle. The boundary sphere velocity extends over
the three-ball, and the adjoint normal arrow extends over the Hopf
sphere cap. This is the exact extension used in (SI.12)--(SI.13).

Over this path the principal circle lines, including their Hopf caps,
form an actual line bundle on the smooth family. Choose an invariant
horizontal lift of the just constructed base field. On the outside
collar prescribe the lift which fixes the full real coefficient $d$.
Near the cap use the carried Cartier/Hopf lift. On their overlap the
difference is vertical, so an invariant partition of unity glues
these lifts. Its flow gives an actual line-bundle isomorphism. It
is the prescribed real-period isomorphism on the whole boundary;
there the connections $dd+\alpha_qd\gamma+\theta d\gamma$ agree
literally. The $q$-disc gauge above also fixes the integral boundary
normalization. This constructs the relative pair morphism, including
its line and cap, between $U_{0,1}$ and the corresponding local
scalar-winding-one piece with the same integer $e$ and prescribed
outer coefficients. More directly, inverse theta-cut tensors in
(BW.4) replace the local line multipliers by
$\alpha_*$ and $e^{2\pi i\theta}\eta_*$, without changing their
positive norms or source factors. Identity on the circle quotient,
the displayed coefficient tensors, and (BW.5a) are its literal
local arrow. It does not alter or posit a map between unspecified
global exteriors.

Let $F_{0,1}$ be a connection curvature with this fixed boundary
value. The relative pairing
\[
 B_{\rm loc}=\int_{\mathcal C}F_{0,1}^{2}\wedge\Xi
                                                        \tag{BW.6}
\]
is preserved by the constructed morphism. Connections with the same
boundary value give the same number: their curvature difference is
exact with zero boundary primitive, and Stokes applies to the closed
form $\Xi$.

Apply the actual local SCN.9/K62 $C_2$ bordism to this winding-one
piece, with the same $e$ and every factor in (BW.5a). Its first
outer normal arrow is the identity and the second is the base
factor $\kappa^{-1}$ with normal matrix
$\operatorname{diag}(\alpha_*^{-1},\kappa\alpha_*)$.
Both are parameter-independent. The common inner physical-circle
gauge therefore extends over the retained joint cap and these
outer arrows. The resulting line and normal transitions pull back
from the three-dimensional fixed-cobordism factor; hence
$b^2=p_1(\nu)=p_1(T\bar X)=0$ there. The two separate sphere-bundle
identities for $4\int x^3=3b^2+p_1(\nu)$ and
$\int p_1x=p_1(T\bar X)+p_1(\nu)$ give zero individually.
The common exterior collar is an actual product with its equal
connection. It contributes zero to their difference, without
selecting or changing a global exterior. This proves equality of
the two relative integer Euler cubes for the local pieces.
The SI whole-collar calculation at $n=1$ is exactly
$3B_{\rm loc}-3$. Thus
\[
                         B_{\rm loc}=1.               \tag{BW.7}
\]
This is a calibration by one actual integer comparison and the
explicit relative morphism above. It does not select an integer
from a central residue.

By (BW.4) we may choose on the original piece the curvature
$F_{L,J}=F_{0,1}+L\Xi+(J-1)\Psi$, with its exact boundary value.
Since the last two summands both contain $d\theta$, (BW.1) gives
\[
 \int_{\mathcal C}F_{L,J}^{2}\wedge\Xi
       =\int_{\mathcal C}F_{0,1}^{2}\wedge\Xi=1.
                                                        \tag{BW.8}
\]

## BW.3. The full shear and its two characteristic integrals

For the actual shear $V_n=Z^{-n}V$, $h_n=hB^n$, the source parameter
remains $Q_n=\kappa qg^n$, while the line windings are $(L+nJ,J)$.
The exact coefficient map is still $u_n=u,v_n=v,\gamma_n=\gamma-nv,
d_n=d-nu$. Its new connection is
\[
 A_n=dd_n+(\alpha_q+J\theta)d\gamma_n+(L+nJ)\theta\,dv.
\]
Thus the actual piece-minus-exterior form is still
\[
 \beta_n=-n(du+\alpha_qdv),\qquad d\beta_n=-n\,d\alpha_q\wedge dv.
                                                        \tag{BW.9}
\]
The same section-disc/Cech construction makes the interior line map
$U_n\to U_0\otimes T_b^{nJ}$ relative to this exact boundary arrow.
The source and graph maps (SI.10)--(SI.13) use the same full units;
their tangent boundary matrix is $I+n\phi_gE_{12}-nE_{32}$.
Its Maurer form squares to zero, so the entire tangent collar has
$\operatorname{tr}F^2=0$. The actual regular-level argument (SI.27)
gives $\langle p_1,\Xi\rangle=0$. Therefore
\[
                         \ell_{M,n}=\ell_{M,0}.        \tag{BW.10}
\]

Use the piece coefficient gamma$=\gamma_n$ and the positive boundary
orientation $\Omega=d\alpha_q\wedge du\wedge dv\wedge d\gamma\wedge d\theta$.
The retained exterior curvature is now
\[
 F_{{\rm ext},n}=(d\alpha_q+Jd\theta)\wedge(d\gamma+n\,dv)
                                      +L\,d\theta\wedge dv.
                                                        \tag{BW.11}
\]
Its square contributes a linear term; it must not be set to zero.
Exact exterior algebra gives
\[
 3\int_0^1\beta_n\wedge
             (F_{{\rm ext},n}+s\,d\beta_n)^2\,ds
                  =(6Ln+3Jn^2)\Omega.                \tag{BW.12}
\]
The outward collar runs from $s=1$ to $s=0$, so its physical Euler
cube contribution is $-6Ln-3Jn^2$. The exact interior relative line
map and (BW.8) give interior contribution $3nJ$. The K68 physical
line and Jin orientation are the ones in (SI.29). Combining the
two actual pieces therefore gives
\[
 \begin{aligned}
 k_{M,n}&=k_{M,0}-6Ln-3Jn(n-1),\\
 \ell_{M,n}&=\ell_{M,0},\\
 A_{M,n}&=A_{M,0}-Ln-\tfrac J2n(n-1).
 \end{aligned}                                      \tag{BW.13}
\]
Every boundary primitive has been included. In particular the
linear $L$ term comes from the actual $F_{{\rm ext},n}^2$ term and
is fixed as an integer by the relative morphism; no modulo-28
comparison is used to choose it.

The domain of this local calculation is the explicitly constructed
primitive nodal quotient piece and its stated closed seam. Its use
for a named global family retains that family's identification of
this piece, physical line, cap and parameter orientation. The
ordinary and finite-cap source data have not been replaced by
an abstract winding matrix in this proof.

## BW.4. The actual OS49 positive reference is the fan T1

Now retain the actual source and every datum of OR65.1:
\[
 y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12),\qquad
 G=(t^2,t^2),\quad M=\mathcal O(G-O),\quad Q=3G.
                                                        \tag{BW.14}
\]
The suspension is over $-Q$, with its actual target-point
linearization divisor $C_0$ on the $I_2$ source fibre. The
$IV^*$ cap has order $m=3k>0$, norm sign $\nu=\pm1$ and
fixed character $d\in\mathbb Z$. Its exact ordinary-to-cap
arrow is
\[
 \Phi_r(z,s_0)=z+\frac{\log s_0}{2\pi i}\Pi_r(s_0)
                 \{\nu(e_\gamma-e_u)+d\delta\}.
                                                        \tag{BW.15}
\]
The root action is $A_r=r^\nu A_0$. The ordinary closing is
the endpoint-to-initial map $q^{-\nu}$; its forward is $q^\nu$.
On the type-II source neighbourhood retain the original line
complement and contracting suspension. None of these arrows
is replaced by a whole-fibre linearization.

The original source and suspension logarithmic periods are
\[
 u=(2s,s)^t+U(q),\quad
 \gamma=(-3s,-s+mv)^t+C(q),\quad
 s=\frac{\log q}{2\pi i},\quad v=\frac{\log r}{2\pi i}.
\]
The actual integral deck-generator change is
\[
 H=-u-\gamma=(s,-mv)^t-U-C,\qquad
 K=3u+2\gamma=(0,s+2mv)^t+D,\quad D=3U+2C.
                                                        \tag{BW.16}
\]
Its determinant is one; these are actual deck transformations,
including their bounded source and line units. Thus in the
original physical characters the periods are exactly those of
BW.1, with
\[
                   (L,J)=(-m,2m).                    \tag{BW.17}
\]
The bounded forward is $E_r=(g^{-\nu},\eta^{-\nu})$;
the complete seam of BW.5a has $e=\nu,u=1$. Its actual cap
square is (BW.15). Hence both signs use the same positive
parameter orientation in (BW.17).

Write $T_n=T(e_1+ne_2,e_2)$ in this fixed physical lattice.
The infinite negative-diagonal fan is $T_0$. The two triangles
of $T_1$ are
\[
 \{0,e_1+e_2,e_2\},\qquad
 \{e_1+e_2,e_2,e_1+2e_2\}.
\]
The first is a positive-diagonal square triangle; the second
is its other triangle translated by $e_2$. Translation by
$e_2$ is the full actual $K$ deck, with the unit factors in
(BW.16). These equalities hold for every integral translate,
so the two infinite fans and all their localized cone rings
are literally the same. The dense-character identity descends
through the unchanged period action and finite-cap arrows.

The fixed-star charts on $T_n$ use
$Z_n=Z,V_n=Z^{-n}V$ and
\[
 (Z,n_0,n_1)=(Z,q/(ZV_n),V_n),\qquad
 (Z',n'_0,n'_1)=(Z^{-1},Zn_0,Zn_1).
                                                        \tag{BW.18}
\]
For $n=1$ they become exactly
\[
 (Z,A,B)=(Z,q/V,V/Z),\qquad
 (Z',A',B')=(Z^{-1},qZ/V,V),
                                                        \tag{BW.19}
\]
the OC.11 positive-fan normal charts. In particular the
actual global quaternion is precisely
\[
 q_H=(1+jZ)(A+j\overline B)
     =(Z^{-1}+j)(A'+j\overline {B'}).
                                                        \tag{BW.20}
\]
The physical circle is right multiplication by $e^{-i\phi}$.
The decreasing contracting-$K$ height, the constant signed
normal reference change for $\nu=-1$, and the full unit
normal arrows are OC.12--19. Thus this identification retains
the actual Cox cap and its framing, not just the common fan.

The independent positive page is the actual line-complement
subfan with heights $\lceil j/2\rceil$ and component degrees
$(-1,+1)$. Its $m$ norm shells, cap root and regular bands
are OR65.2. The full normal quotient clutch in OC.17--20 has
zero normal Pontryagin integral; OC.21 retains
$M_{\rm rel}^2=-2k$ and $p_{\rm rel}=-24k$. K68's exact
physical/dual line arrow converts its pair to
\[
                      (k_{M,1},\ell_{M,1})=(2m,8m).
                                                        \tag{BW.21}
\]
The constant $d$-character is carried on every root sheet;
its $m$-fold product is one. The relative page line changes
only by its already retained base class, whose square and
pairing with $M$ vanish. The point-angle determinant-one
map in OC.7--10 proves the same signed pair for each $\nu$.

Apply the actual relative calculation (BW.13) in these charts
and subtract its value at $n=1$. With (BW.17) and (BW.21)
this gives the complete physical pair and index
\[
 \boxed{\quad k_{M,n}=2m-6m(n-1)^2,\qquad
 \ell_{M,n}=8m,\qquad A_{M,n}=-m(n-1)^2.\quad}
                                                        \tag{BW.22}
\]
The dual-$U$ pair is the negative of this pair. In particular
the negative fan's integer is now computed by the actual line
and tangent morphisms. Its value was not selected from K65's
residue. The native fixed-star free pair is
\[
               (\mu_n,\rho_n)=(2m,-6m(n-1)^2).       \tag{BW.23}
\]

## BW.5. The actual shorter endpoint and the full vertical seed

Retain the exact endpoint of OR65.6. The rational source-line
lift $U$ satisfies $\rho=B_0^{-1}/U^3$; its orders at the
cusp and finite cap are respectively $1$ and $-1$ modulo
three. The rational root $g_0^3=q^{-\nu}\rho^{-2\nu}$ gives
the endpoint-to-initial map
\[
 C_r=r^{2\nu k}g_0U^{-2\nu}:X_{\zeta_3r}\longrightarrow X_r.
                                                        \tag{BW.24}
\]
On the cap the full Cartier map is the invariant unit times
$L^{-2\nu}$, with $DLD^{-1}=\zeta_3L$ and $L^3=B_0^{-1}$.
Consequently $\Phi_rC_r=C_{\rm cap}\Phi_{\zeta_3r}$ and
$C_{\rm cap}A_{\zeta_3r}C_{\rm cap}^{-1}=A_r$. This retains
the original $d$-character and both values of $\nu$.

After the actual source deck reindexing, the full bounded
closing logarithm and extending origin are
\[
 c(v)=\frac{\nu}{3}(D+2mv\delta)-\frac{2\nu k}{3}\delta,
 \qquad \sigma(v)=\nu vD+\nu m v(v-1)\delta,
\]
\[
 \sigma(v+1/3)-\sigma(v)=c(v),\qquad
 \sum_{j=0}^2c(v+j/3)=\nu D+2\nu mv\delta.           \tag{BW.25}
\]
The forward endpoint is the inverse of this closing. On
$T_n$ apply the literal character map $(z,\ell)\mapsto
(z,\ell-nz)$ to every vector in (BW.25). This is an
integral monomial map and preserves their equalities, all
bounded units and the zero-height endpoint. The sheet product
$P_j=\exp(2\pi i\sum_{h<j}c(v+h/3))$ is the actual product
of the first $j$ closing maps. Its values at $j=0,1,2,3$ are
those of OR65.31, with this same character map applied.

For completeness use the fixed native C0 coordinate order
$(b_1,a,c_1)$ from K73. A cut multiplier $(A,D_n)$, with
$D_n=DA^{-n}$, acts by the factors
\[
 (A,(AD_n)^{-1},D_n),\qquad
 (A^{-1},D_n^{-1},AD_n)
                                                        \tag{BW.26}
\]
on its two normal charts. Its literal Cox lift is
\[
 (a_0,a_1,c_0,c_1)\longmapsto
 (a_0,Aa_1,(AD_n)^{-1}c_0,D_n c_1).                  \tag{BW.27}
\]
It preserves $q$ and the physical circle. The all-sheet
identity in (BW.25) holds on each of these four character
factors. Thus the covered $r$ native product is the literal
triple pullback of the shorter $w=r^3$ native product,
including every collar and the cap square (BW.24).

We also compare that product to the canonical seam used in
BW.4. On a linear interior cut the origin product has
logarithm $\sigma(v+\theta)-\sigma(v)$, whereas the
canonical cut has logarithm
$\nu\theta D+2\nu m\theta(v+\theta)\delta$.
Their difference is the explicit physical-circle factor
\[
                 -\nu m(\theta^2+\theta)\delta.
                                                        \tag{BW.28}
\]
Its exponential has value one at both endpoints. It is
therefore an actual based global physical-circle action,
including its possible winding. It acts identically on the
orbit normal three-plane and extends on the same line and
Hopf cap. Flatten both cuts on the protected collars using
their common actual endpoint relation. The remaining unit
ratios have zero endpoint logarithm and the explicit
exponential interpolation carries their full jets. This
gives the actual relative cap and line comparison between
the two covered products; it does not discard a closed
circle loop. Hence their completed physical-circle lines
and stable tangent bundles are isomorphic with their
specified orientation and outer frame.

The degree-three mapping-torus covering now gives literal
equalities of characteristic integrals, not division in
$\Theta_7$. Writing $j=m/3=k$ on the shorter loop gives
\[
 (k_{M,n}^{w},\ell_{M,n}^{w})
       =(2k-6k(n-1)^2,8k),\qquad
 A_{M,n}^{w}=-k(n-1)^2.                              \tag{BW.29}
\]
The sphere classes are the residues of (BW.22) and (BW.29)
by the actual physical Hopf transfer K68.

Here is also the full seed for further exact fan comparisons.
Write $j=m$ for the $r$ loop and $j=k$ for the actual shorter
$w$ loop. Use the literal doubled ordinary product, carrying
the native fixed-star product just specified. Its native
double pair is $(4j,-12j(n-1)^2)$. The K70/NV actual C0
product change is pure left $-2J=-4j$, so its ordinary
double pair is $(0,-12j(n-1)^2)$. Consequently
\[
 V^{(2)}=\begin{pmatrix}
 12j(n-1)^2&8j(1-n)&8j(n-1)\\
 8j(1-n)&4j&0\\8j(n-1)&0&4j
 \end{pmatrix},\qquad
 \delta^{(2)}=\begin{pmatrix}
 -12j(n-1)^2\\8j(n-1)\\8j(1-n)
 \end{pmatrix}.                                    \tag{BW.30}
\]
The off-diagonal and remaining diagonal entries come from
the full actual trace, not the index. Indeed the doubled
period winding in these characters is
$B=\left(\begin{smallmatrix}0&0\\2j(2n-1)&4j\end{smallmatrix}\right)$,
$t_0=2j$, $w=(0,1,-1)$, $d=(-2,-1,-1)$. The literal
normal and derivative prisms of OR65.16--17 give
$I=(8j(n-1),4j,-4j)$ and $W=(8j(1-n),0,0)$, which
determine every remaining entry of (BW.30).

This result computes every vertical-edge fan with the exact
OS49 source, component line, cap and endpoint just retained.
It does not substitute these numbers into a previously
withdrawn universal scalar-fan expression.

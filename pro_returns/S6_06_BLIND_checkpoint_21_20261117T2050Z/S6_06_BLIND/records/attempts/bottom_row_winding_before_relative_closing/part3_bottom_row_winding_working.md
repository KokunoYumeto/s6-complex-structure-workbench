# The exact local integer calculation for bottom-row winding

Working proof, 17 November 2026. This note constructs and compares the
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
its line and cap, between any $U_{0,1}$ just defined and the local
piece of a fixed canonical SI reference family. It does not alter
or posit a map between their unspecified global exteriors.

Let $F_{0,1}$ be a connection curvature with this fixed boundary
value. The relative pairing
\[
 B_{\rm loc}=\int_{\mathcal C}F_{0,1}^{,2}\wedge\Xi
                                                        \tag{BW.6}
\]
is preserved by the constructed morphism. Connections with the same
boundary value give the same number: their curvature difference is
exact with zero boundary primitive, and Stokes applies to the closed
form $\Xi$.

Take as reference the actual OS45 canonical $J=1$ family of K70/K72.
Its $n=1$ K62 comparison retains both its line and normal bundles and
gives equality of its two integer Euler cubes. The SI whole-collar
calculation at $n=1$ is exactly $3B_{\rm loc}-3$. Thus
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
 \int_{\mathcal C}F_{L,J}^{,2}\wedge\Xi
       =\int_{\mathcal C}F_{0,1}^{,2}\wedge\Xi=1.
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

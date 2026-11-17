# The complete integer seed on the scalar vertical-edge fans

Proved as P3K.72 after full root and checks audits, 17 November 2026. The family here is
one of the actual fixed-source canonical scalar families of K26, K28 or
K32, with its original source, Cartier line, finite caps and full ordinary
closing. Its parameter has scalar winding $J$: in the positive canonical
parameter, $\lambda=r^J$. The ordinary forward closing is the prescribed
$q^e u(q)$, with $u$ a source-independent nonzero unit. All finite-cap
arrows and every integral annular cochain are retained. The initial
physical characteristic pair is the actual K30/K68--69 pair
$(k_{M,0},\ell_{M,0})=(3H,24\chi)$.

The following argument computes the integer pair on each actual fan
$T_n=T(e_1+ne_2,e_2)$. It uses the separately constructed native fixed
star and its Cox cap. It makes no assertion of a simultaneous
delta-equivariant product on the full three-edge plumbing.

## SI.1. The closed scalar seam and the actual orbit pieces

Retain the full cusp periods
\[
 h:(Z,V)\longmapsto(\kappa qZ,\alpha_LV),\qquad
 B:(Z,V)\longmapsto(gZ,q\eta V),\qquad \eta=\lambda\beta.
                                                        \tag{SI.1}
\]
Here $\kappa,\alpha_L,g,\beta$ are the actual units, independent of the
scalar parameter. Their nonzero holomorphic logarithms on the small
protected $q$ disc are fixed once. The scalar radius is fixed on the
parameter circle; $\theta$ has period one. The only parameter winding
in this matrix is $\operatorname{wind}\eta=J$.

Reindex the ordinary forward closing by the actual $B^{-e}$. Its bounded
arrow is exactly
\[
 E:(Z,V)\longmapsto(g^{-e}Z,u\eta^{-e}V).
                                                        \tag{SI.2}
\]
On a cut parameter interval use the full torus multiplier
$C_\theta=(A_\theta,D_\theta)$ of K64, with
\[
 C_0=1,\qquad C_1=(g^e,u^{-1}\eta^e),\qquad C_1E=C_0.
                                                        \tag{SI.3}
\]
The equality holds on the full protected collars, with all derivatives.
The functions are the actual logarithmic cut functions of the bounded
units and of $\eta$; their angular winding is retained. They commute
with both periods and the physical circle. On the two vertex charts
their maps are, literally,
\[
 (a,b,c)\longmapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u,v,w)\longmapsto(ADu,D^{-1}v,A^{-1}w).
                                                        \tag{SI.4}
\]
Both triple products remain $q$. The complete three period rows
intertwine these maps, so they extend across the toric charts and
retain every $q$-normal derivative. The finite-cap closing square is
the original one, carried by the same ordinary arrow. Thus the closed
coordinates used below are coordinates on that actual family.

For the $n$-th fan take
\[
 Z_n=Z,\quad V_n=Z^{-n}V,\quad h_n=hB^n,\quad B_n=B.
\]
Direct substitution gives
\[
 Q_n=\kappa qg^n,\quad
 \alpha_{L,n}=\alpha_L\eta^n\kappa^{-n}g^{-n^2},\quad
 g_n=g,\quad\eta_n=\eta g^{-n}.                       \tag{SI.5}
\]
The source parameter $Q_n$ is independent of $\theta$. The two line
windings are $nJ,J$. In these characters the seam is exactly
$(A,D A^{-n})$, so (SI.3) remains the actual endpoint equality. On a
multiple parameter cover its successive laps are $C_\theta E^{-j}$;
this is the literal pullback, not a new seam choice.

Take the physical-circle quotient. The F9 node maps are the same
actual maps in these vertical characters:
\[
 2b=r-|y|^2/r,\quad 2b'=|x|^2r-r^{-1},\qquad
 \frac{db'}{db}=\frac{|x|^2+r^{-2}}{1+|y|^2r^{-2}}>0.
                                                        \tag{SI.6}
\]
The contracting $B$ coefficient is the negative of the increasing
F9 moment coordinate. Its real-period formula is
\[
 \gamma_n=
 \frac{\log|Q_n|\log|V_n|-\log|\alpha_{L,n}|\log|Z_n|}
 {\log|Q_n|\log|q\eta_n|-\log|\alpha_{L,n}|\log|g|}.
                                                        \tag{SI.7}
\]
The denominator has leading term $(\log|q|)^2$. It is nonzero on a
uniform small disc. The complete norms in (SI.7) are independent of
$\theta$; parameter phases have not been deleted from the circle
bundle. Substitution of $h_n$ leaves $\gamma_n$ unchanged and
substitution of $B$ increases it by one.

The F9 conifold interval has representatives $z=\sqrt r$, $v=u=0$,
$w=1/\sqrt r$. Choose on it
\[
 \gamma_n=\tfrac12-\varepsilon\frac{r-1}{r+1},
 \qquad0<\varepsilon<\tfrac14.                       \tag{SI.8}
\]
Its endpoint lifts are $1/2+\varepsilon,1/2-\varepsilon$ and the
endpoint derivatives in the two F9 charts are both $-4\varepsilon$.
The fixed sphere's second endpoint is the $h_n^{-1}$ translate of the
second conifold endpoint, hence has the same gamma lift by (SI.7).
There is no extra integer between them. Extend the two proper
decreasing coordinate maps, using a convex interpolation equal to
the prescribed real-period map on the outer collar. Its derivatives
remain negative and its lifts commute with addition of one. The
normalization cylinder then has a graph in this same short arc.

Untwist the source part of $B$ by its actual $\exp(\gamma\log g)$
isotopy, and the line norm by its full positive-norm isotopy. This
gives the orbit piece
\[
 W_n=E_n\times S^1_{\gamma_n},
                                                        \tag{SI.9}
\]
where $E_n$ is the nodal source neighbourhood with Tate parameter
$Q_n$. This assertion is relative to the exact outer coordinates
just prescribed. It also holds over the closed parameter: (SI.3)
closes the toric charts, its multipliers commute with all periods,
and the quotient construction uses precisely their unchanged
source and real-norm data. Only the line phase has parameter
winding. That phase is retained in SI.3 below.

## SI.2. The source, fixed tube and marked Cox cap map

Write $L_g=\log g$. Interpolate the actual source parameters by
$Q_s=\kappa q\exp(snL_g)$, $0\le s\le1$. Near the node $xy=Q_s$
the horizontal vector field is
\[
 \partial_s+nL_g y\partial_y.                         \tag{SI.10}
\]
It keeps $q,\theta$ fixed and preserves the node and its two branches.
On the outer regular collar prescribe instead the real marked-period
map $u+\tau_s v\mapsto u+\tau_0v$. Both are horizontal over the same
$\partial_s$; their difference on the overlap is vertical. A partition
equal to one on the protected node and outside collars interpolates
them in this affine space. On the compact source neighbourhood the
resulting boundary-tangent field has a complete flow. It is periodic
in $\theta$ and is precisely the real-coefficient map on the entire
outer collar. No real period expression is used as a smooth node map.

Transport the fixed normalization sphere by this source flow. Its
gamma graph and the graph at $n=0$ lie in the short arc (SI.8), with
the same ordered, distinct endpoint values. Their convex interpolation
remains embedded: the source normalization is injective except at its
two node preimages, and those two heights stay distinct. The velocity
extends from the sphere to a tube and then by a cutoff. This gives an
actual ambient isotopy, fixed on the outside collar and periodic in
the parameter.

The normal map is also retained. In the native fixed star
$(z,n_0,n_1)=(Z,q/(ZV),V)$ the character map is exactly
\[
 (z,n_0,n_1)\longmapsto(z,z^n n_0,z^{-n}n_1),
 \qquad q=zn_0n_1.                                  \tag{SI.11}
\]
Let $D_0,D_\infty$ denote the two marked branch sections of the
normalization. In the positive Hopf spinor convention the corresponding
bundle arrow is the Cartier arrow
\[
 E_n^{\rm spin}=E_0^{\rm spin}\otimes
               \mathcal O(n(D_0-D_\infty))
       \longrightarrow E_0^{\rm spin},\qquad v\longmapsto Z^n v.
                                                        \tag{SI.12}
\]
In its Cartier frames the displayed apparent zeros and poles cancel.
In (SI.11) the negative complex normal is conjugated when passing to
the Hopf spinor; transporting the Hermitian norms leaves the common
phase of $Z^n$, and the remaining real positive factors are the
explicit positive normal rescalings. Thus (SI.12) is the typed
normal-bundle map of (SI.11), with the same physical circle and
physical height. Its adjoint map carries the normal three-plane.
The source flow contributes its actual derivative and the graph
isotopy contributes its positive triangular normal map. These
comparisons extend through their isotopies.

Extend the boundary sphere isotopy over its three-ball by a collar
cutoff of its boundary velocity. On the Hopf sphere factor use the
adjoint arrow of (SI.12). This is the same literal product-cap
construction as SQ.8--9, now with the constant marked nodal source;
it does not replace the Cox normal map by a base tangent derivative.
It supplies a diffeomorphism of completed pieces, including their
actual cap and circle-line marking,
\[
 C_n=(W_n\setminus\operatorname{int}(F_n\times D^3))
                      \cup(D^3\times S^2)\longrightarrow C_0.
                                                        \tag{SI.13}
\]
Its circle line is compared next. The finite caps and the rest of the
quotient exterior are the original ones throughout.

## SI.3. The full integral line and its prescribed boundary arrow

Use the actual complex period coefficients
\[
 (z,\ell)=u(1,0)+v(\tau,\mu)+d(0,1)+\gamma(G,\zeta),
                                                        \tag{SI.14}
\]
where $z=\log Z/(2\pi i)$, $\ell=\log V/(2\pi i)$,
$\tau=\log(\kappa q)/(2\pi i)$, $\mu=\log\alpha_L/(2\pi i)$,
$G=\log g/(2\pi i)$, and $\zeta=\log(q\eta)/(2\pi i)$.
The imaginary parts invert (SI.7); the real parts then determine
$u,d$. Thus differentiating $d=\Re\ell-\Re\mu\,v-\Re\zeta\,\gamma$
retains every unit and its derivative. The coordinates are the closed
ones in (SI.3). With $\alpha=\arg q/(2\pi)$, their integer deck maps are
\[
 q\text{-turn}:(u,d)\mapsto(u-v,d-\gamma),\qquad
 \theta\text{-turn}:(u,d)\mapsto(u,d-J\gamma).
                                                        \tag{SI.15}
\]
The bounded source and line factors in the seam give their actual
periodic logarithms, not further unrecorded integral changes.

Direct substitution of both characters in (SI.14) gives
\[
 u_n=u,\quad v_n=v,\quad\gamma_n=\gamma-nv,\quad d_n=d-nu.
                                                        \tag{SI.16}
\]
The meridian-one line is $U=M^*$, with $M$ the physical line, exactly
as in K68. In these coefficient frames choose the actual boundary
connections
\[
 A_0=dd+(\alpha+J\theta)d\gamma,\qquad
 A_n=dd_n+(\alpha+J\theta)d\gamma_n+nJ\theta\,dv.
                                                        \tag{SI.17}
\]
They are invariant under their full integer deck maps. In particular
the new theta map is $d_n\mapsto d_n-J\gamma_n-nJv$. In physical
coordinates the connection includes all the differentials in
(SI.14); it does not discard the units. Their exact difference is
\[
 \beta_n=A_n-A_0=-n(du+\alpha\,dv).                  \tag{SI.18}
\]
The coframe with the full Tate phase is
$du+(\alpha+\phi_\kappa)dv$; consequently (SI.18) retains the
additional $n\phi_\kappa dv$ when expressed in that coframe.

Let $b:C_0\to\mathbb R/\mathbb Z$ be the source graph map with boundary
value $v$. It extends over the Lefschetz two-handle because the
attaching vanishing circle is the $u$ circle and $v$ is constant on
it. On the fixed sphere its restriction has a real lift. Modify that
lift by a supported real homotopy to make $b$ constant on a smaller
fixed tube; it then extends constantly over the cap. The marked
source and both branch sections return literally in the closed
coordinates, so this construction is periodic. Its precise theta
clutch change is implemented by $\exp(2\pi i nJ\theta h)$, where $h$
is the supported real difference of the two graph maps.

On the completed six-dimensional piece $\mathcal C$ define the line
$\mathcal T$ by its theta-cut coefficient gluing
$w\mapsto e^{2\pi i b}w$. Its connection in those frames is
$d-2\pi i\theta\,db$, so
\[
 c_1(\mathcal T)=\Xi=d\theta\wedge db,\qquad\Xi^2=0.
                                                        \tag{SI.19}
\]
On the normalization graph cut, the actual constant factor
$\alpha_{L,n}/\alpha_L$ has winding $nJ$. The theta-cut description is
$d_n\mapsto d_n-nJb$ relative to the old line, exactly the dual
coefficient gluing of $\mathcal T^{nJ}$. On the doubly cut rectangle
the coordinate change $d_n\mapsto d_n+nJ\theta b$ identifies these
two descriptions. The remaining logarithms are explicitly
\[
 nf_\beta-nf_\kappa-n^2f_g,
 \qquad -nf_g,                                       \tag{SI.20}
\]
with the fixed scalar-radius constant retained. They extend in the
chosen full unit charts.

For the integral check, $H_1(C_0)=\mathbb Z\langle b,\gamma\rangle$ and
$H_2(C_0)=\mathbb Z\langle\text{Hopf meridian},b\times\gamma\rangle$.
The removal Thom sequence adds the normal meridian, since the
regular fibre times gamma misses $F$; the cap identifies that
meridian and kills the primitive fibre class. All groups are free.
The parameter maps fix $b,\gamma$ and the oriented meridian. They
cannot add a meridian to the regular $b\times\gamma$ class: the actual
Euler line has value zero on that real-period torus and one on the
meridian. Wang therefore adds precisely the two classes
$b\times\theta,\gamma\times\theta$. The line difference has value
$nJ$ on the first, zero on the second because $\eta_n/\eta=g^{-n}$
has a logarithm, and zero on both old generators by (SI.12) and the
primitive real-period section. Consequently
\[
 c_1(U_n)-c_1(U_0)=nJ\Xi.                            \tag{SI.21}
\]

We require the particular outer isomorphism, not only this equality.
The actual boundary $\mathcal B$ has
\[
 H_1(\mathcal B)=\mathbb Z\langle\alpha,\theta,v,\gamma\rangle,
 \quad \operatorname{im}H^1(\mathcal C)=
       \mathbb Z\langle d\theta,db,d\gamma\rangle.
                                                        \tag{SI.22}
\]
The $q$ monodromy kills $u$ primitively. There is no source theta
monodromy in this scalar case. The gamma map extends through the cap
by its real lift on the short fixed graph, and the theta family has
the explicit free section supplied by the closed coordinates.
Thus the only boundary winding that does not extend is the
$q$-angle winding.

Choose one parameter value $\theta_*$, gamma zero outside (SI.8),
and a constant Tate section $Z=Z_*$ with $|Z_*|=1$, at a generic
smooth normalization point avoiding the finitely many marked source
sections and the two branches at that parameter. On a small parameter
arc the same point and a uniformly smaller $q$ disc work. The
relations $\log|Z_*|=\log|V|=0$ give $v=\gamma=0$ literally in
(SI.7) and (SI.14). In the actual closed first-vertex charts the
section-disc map is
\[
 (q/Z_*,Z_*,1)\longmapsto
              (qZ_*^{n-1},Z_*,Z_*^{-n}).              \tag{SI.23}
\]
The height is $q$ on both sides. Both nonvanishing coordinates
remain nonzero at $q=0$, so the disc lies in the free locus and
misses the fixed surgery. The line arrow $Z_*^{-n}$ extends on
the full disc, and its inverse is an opposite power of the same
nonzero constant. In the original coordinates all seam factors
are retained in the inverse of (SI.4); they are extending units.
The source horizontal flow can fix this section on that parameter
arc, since its prescribed boundary field fixes $v=0$ and the node
is disjoint; extend this choice periodically by a parameter cutoff.
This disc at $\theta_*$ tests the generator of the sole alpha
obstruction in (SI.22). That integral winding is constant on the
connected boundary, so its zero value proves the assertion for the
whole prescribed boundary line arrow. No simultaneous avoidance of
moving Cartier sections over the full parameter circle is needed.

An explicit Cech construction now supplies
\[
 J_n:U_n\longrightarrow U_0\otimes\mathcal T^{nJ}
                                                        \tag{SI.24}
\]
with exactly the boundary arrow (SI.16)--(SI.18). Form the actual
unit transitions of the ratio line, including (SI.20), on a good
cover of $\mathcal C$. Their logarithms have an integral two-cocycle
which vanishes by (SI.21). Subtract its integral one-cochain. For
the resulting real one-cocycle $r_{ij}$ in frame convention
$e_j=e^{2\pi i r_{ij}}e_i$, set $a_i=\sum_k\rho_k r_{ki}$; then
$a_j-a_i=r_{ij}$. Multiplication by $e^{-2\pi i a_i}$ gives its
global unit frame; invert the corresponding Hom map to obtain
(SI.24). Its boundary ratio with the prescribed map has no alpha
winding by (SI.23). Remove its other integral windings using the
extending functions theta, $b$, gamma in (SI.22), then extend the
remaining real logarithm with a collar cutoff. This makes the
boundary map literally the prescribed one. On the inner cap any
remaining theta gauge extends over $D^3\times S^2\times S^1$.
The resulting map retains every annular integer and finite-cap
character.

## SI.4. Relative Pontryagin pairing with the full tangent collar

On the outer collar use the stable coframe
\[
 du+(\alpha+\phi_\kappa)dv,\quad dv,\quad d\gamma,
 \quad d\alpha,\quad d\theta,\quad dr_q.
\]
The actual piece map (SI.13), prescribed in the real-period coordinates
on this whole collar, has coframe matrix
\[
 G=I+n\phi_g E_{12}-nE_{32},\qquad
 G^{-1}dG=n\,d\phi_g E_{12}.                         \tag{SI.25}
\]
Here $\phi_g=\Im\log g/(2\pi)$ is independent of theta. The line
phase $J\theta$ belongs to (SI.17), not to an unrecorded tangent
block; its positive norm has already entered gamma. The Maurer
form squares to zero. For an interpolation of the actual flat
tangent connections by $\chi(r)G^{-1}dG$,
\[
 F=\chi' dr\wedge\omega+(\chi^2-\chi)\omega^2,
 \qquad\operatorname{tr}F^2=0.                       \tag{SI.26}
\]
Thus the full tangent $p_1$ form can be chosen zero throughout
the gluing collar. This uses the exact matrix, not only flatness
at its ends. The source and graph isotopies are fixed there.

On $C_0$ choose nested fixed tubes so that all surgery and
connection modifications lie inside an inner tube, and choose
the tangent connection outside it pulled from the actual source
$E_0$, with a trivial gamma line. It has the specified flat source
part on the outer collar. At a fixed theta, a regular product level
of $b:E_0\to S^1$ is $N^3\times S^1_\gamma$, and the pulled-back
source $p_1$ four-form restricts to zero on it. Modify $b$ by its
real lift to be constant on a larger tube. A regular value distinct
from that constant gives a level missing the entire surgery and
all connection changes. The regular-value cobordism of this
supported homotopy is relative to the original outside boundary;
the closed $p_1$ form and its zero outer trace show its integral
remains zero. The new level need not be a product. Its two normal
directions in $\mathcal C$ are the framed $b$ and theta directions.
Consequently, with the retained flat boundary connection,
\[
 \langle p_1(T\mathcal C),\Xi\rangle=0.              \tag{SI.27}
\]
Here $p_1$ is relative and $\Xi$ is absolute. Equation (SI.24)
makes the line change exactly $nJ\Xi$ plus the retained boundary
primitive. The former pairs to zero by (SI.27); the exact terms
pair to a boundary integral which vanishes on the whole collar
by (SI.26). The exterior is unchanged. Therefore
\[
 \ell_{U,n}=\ell_{U,0}=-24\chi,
 \qquad\ell_{M,n}=24\chi.                           \tag{SI.28}
\]

## SI.5. The whole collar cube, its orientation and the integer seed

Use the K68 physical/dual dictionary. In the auxiliary positive
orientation
\[
 \Omega_+=dr_q\wedge d\alpha\wedge du\wedge dv
                        \wedge d\gamma_B\wedge d\theta,
\]
the real curvature $F=dA$ is that of $U$. The actual physical
line and the physical-to-Jin parameter reversal give
\[
 k_M=\int_{\Omega_+}F^3,
 \qquad k_U=-\int_{\Omega_+}F^3.                     \tag{SI.29}
\]
These are exactly the K66/K68 line and orientation maps, now
applied to the same physical Cox normal and positive scalar
parameter. No generator is selected from its residue.

On the common completed piece (SI.24) permits the affine
curvature $F_n=F_0+nJ\Xi$. Since $\Xi^2=0$, its cube change is
linear in $n$. The common exterior connection is kept. In the
piece coefficients, write gamma for $\gamma_n$; thus
$\gamma_{\rm ext}=\gamma+nv$, $d_{\rm ext}=d_n+nu$. Its full
boundary connection and curvature pull back to
\[
 A_{{\rm ext},n}=dd_n+(\alpha+J\theta)d\gamma
                         +n\{du+(\alpha+J\theta)dv\},
 \quad F_{{\rm ext},n}=(d\alpha+Jd\theta)
                                      \wedge(d\gamma+n\,dv).
                                                        \tag{SI.30}
\]
The piece-minus-exterior form is exactly
$\beta_n=-n(du+\alpha dv)$, and $d\beta_n=-n d\alpha\wedge dv$.
Both $F_{{\rm ext},n}^2$ and $(d\beta_n)^2$ vanish. Orient the
outward boundary of the piece by
\[
 \Omega_{\mathcal B}=d\alpha\wedge du\wedge dv
                                    \wedge d\gamma\wedge d\theta.
\]
Its marked unit cell has integral one; the actual nilmanifold
monodromy preserves this cell and volume. Direct exterior algebra
gives
\[
 3\int_0^1\beta_n\wedge
            (F_{{\rm ext},n}+s\,d\beta_n)^2\,ds
                       =3J n^2\Omega_{\mathcal B}.     \tag{SI.31}
\]
The connection on an outward gluing collar is
$A_{{\rm ext},n}+\chi(t)\beta_n$ with $\chi(0)=1$, $\chi(1)=0$.
Its actual cube integral therefore runs from $s=1$ to $s=0$,
and is $-3Jn^2$. Combining the interior linear term with this
complete collar yields one fixed real constant $L$ such that
\[
 k_{M,n}=k_{M,0}+Ln-3Jn^2.                           \tag{SI.32}
\]
The relative map (SI.24) and its prescribed outer gauge are what
exclude a further Mayer--Vietoris term here.

The exact $n=1$ comparison is K62's C2 Cox bordism. Its first
outer map is the identity and its second is base $\kappa^{-1}$,
normal $\operatorname{diag}(\alpha_L^{-1},\kappa\alpha_L)$.
They are scalar-parameter-independent. The two inner charged
boundaries carry one and the same physical-delta gauge, so it
extends through these constant outer maps. On the additional
normal-sphere boundary, both its determinant line and its normal
three-plane are pulled from the three-dimensional fixed factor.
Thus $b^2=p_1(\nu)=p_1(T\bar X)=0$. The individual sphere-bundle
identities $4\int x^3=3b^2+p_1(\nu)$ and
$\int p_1x=p_1(T\bar X)+p_1(\nu)$ show that both characteristic
corrections vanish. This is the narrow integer comparison proved
in SCN.9, with every source, cap and closing factor retained.
The C2 target basis $(e_1,e_1+e_2)$ is exactly $T_1$:
its second triangle translated by $-e_1$ is the first $T_1$
triangle, and its first translated by $e_2$ is the second.
These translations are the actual $h^{-1}$ and $B$ periods with
all their units, so the induced quotient/cap arrow is the literal
identity in the absolute charts. Thus $k_{M,1}=k_{M,0}$ in the
same Cox marking used in (SI.13). It follows from (SI.32) that
$L=3J$.

The complete resulting integer pair and index are
\[
 \begin{aligned}
 k_{M,n}&=3H-3J n(n-1),&\ell_{M,n}&=24\chi,\\
 k_{U,n}&=-3H+3J n(n-1),&\ell_{U,n}&=-24\chi,\\
 A_{M,n}&=H/2-\chi-Jn(n-1)/2.
 \end{aligned}                                      \tag{SI.33}
\]
The native fixed-star identities from the actual physical
Hopf transfer are $k_M=m+n_0$, $\ell_M=4m$. Hence
\[
 (m_0^{\rm native},n_0^{\rm native})
       =(6\chi,3H-6\chi-3Jn(n-1)).                   \tag{SI.34}
\]
The polynomial has been obtained from the whole relative line
and tangent calculation. The congruence K64 is an independent
consistency check, not an input determining an integer lift.

For the literal doubled ordinary plumbing product of K64/K70,
the native-to-ordinary comparison is the actual pure-left
$-2J$ endpoint. Thus its fixed entries, ready for the actual
nonzero-weight target reconstruction, are
\[
 V_{00}^{(2)}=2J-6H+6Jn(n-1),\qquad
 \delta_0^{(2)}=2J+6H-24\chi-6Jn(n-1).
                                                        \tag{SI.35}
\]
For completeness, the retained K55/K64 trace maps on this literal
doubled product have
\[
 B=P_n^{-1}\operatorname{diag}(0,2J)P_n
       =\begin{pmatrix}0&0\\2Jn&2J\end{pmatrix},\qquad
 w=(0,1,-1),
\]
\[
 I=(2J(2n-1),2J,-2J),\qquad
 W=(2J(1-2n),0,0).
\]
Their exact integral graph/prism equations consequently give the
complete ordinary seed
\[
 V^{(2)}=
 \begin{pmatrix}
 2J-6H+6Jn(n-1)&2J(1-2n)&2J(2n-1)\\
 2J(1-2n)&2J&0\\
 2J(2n-1)&0&2J
 \end{pmatrix},
\]
\[
 \delta^{(2)}=
 \begin{pmatrix}
 2J+6H-24\chi-6Jn(n-1)\\2J(2n-1)\\2J(1-2n)
 \end{pmatrix}.                                      \tag{SI.36}
\]
No division in $\Theta_7$ occurs in this statement. The exact
scope remains the canonical closing (SI.2), its literal parameter
covers, and the actual physical-vertical-edge fans.

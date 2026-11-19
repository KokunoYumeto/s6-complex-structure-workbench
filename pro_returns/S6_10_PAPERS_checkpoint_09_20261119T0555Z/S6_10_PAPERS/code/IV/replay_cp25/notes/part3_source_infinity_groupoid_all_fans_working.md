# The E7 infinity return on every lattice-basis fan

Proved as P3K.92 after full root and independent map audits. The earlier
candidate with an extra reflection
at infinity is preserved in `part3_source_infinity_all_fans_working.md`.
The maps below determine the corrected label directly.

## Statement

Retain either of the actual E7 one-cap families
\[
 (a,b,m)=(1,2,4p)\quad\hbox{or}\quad(2,1,4p-1),\qquad p\ge1,
\]
with either norm sign \(n=\pm1\), its prescribed finite character and
its full integral ordinary-to-cap reference cochain. Use the physical
circle and orientation of P3K.68. For \(P\in\mathrm{GL}_2(\mathbb Z)\),
let \(\mathcal T(P)\) be the two-triangle periodic fan with triangles
\(\{r,r+v,r+w\}\) and \(\{r+v,r+w,r+v+w\}\), where \(v,w\) are the
columns of \(P\). Put \(J=\operatorname{diag}(-1,1)\).

The marked infinity family is
\[
 y^2=x^3+(-2+3\epsilon^2)x^2+t x+
                  \epsilon^2(1-\epsilon^2)^2,
 \qquad G=(0,\epsilon(1-\epsilon^2)),                 \tag{IFan.1}
\]
with selected height
\[
 q_*=t-(1-\epsilon^2)(1-3\epsilon^2).
\]
The return uses one positive \(\epsilon\)-circle, a fixed sufficiently
small suspension scalar, and the actual source/line/root closing
specified in IFan.4 below. Let its oriented clutched sphere class be
\(I_a(P)\in\Theta_7\cong\mathbb Z/28\).

Let \(Z_a(P)\) be P3K.90's fixed-scalar source-zero class at the same
fan, and let \(C(P)\) be P3K.71's selected-cusp source class. Then
\[
 \boxed{\ I_a(P)=-Z_a(P)-Z_a(JP)-C(P)\pmod {28}.\ } \tag{IFan.2}
\]
This is a complete finite algorithm for every unimodular input, using
the actual algorithms of those two theorems. It is independent of the
cap order \(p\), norm sign, and retained fixed characters within the
stated branches because the two actual input algorithms have that
scope. No characteristic integer or free relative coordinate is
recovered from this equation in \(\Theta_7\).

For every vertical fan \(T_j=\left(\begin{smallmatrix}1&0\\j&1\end{smallmatrix}\right)\),
\[
 I_a(T_j)=1-a\pmod {28}.                            \tag{IFan.3}
\]
In particular these vertical classes are zero in the good branch and
\(-1\) in the reduced branch. On the nonvertical fan \(Q_0^2\), where
\(Q_0=\left(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\right)\),
the formula gives respectively \(10\) and \(7\) modulo28. These are
classes of the actual marked infinity loop.

## IFan.1. A compact parameter family with the complete cap atlas

Start with the sectioned source
\[
 E_v:\quad Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
 \quad q_1=T-(v^2-2v),\quad v=\rho^2-1.              \tag{IFan.4}
\]
Take a large finite \(R>2\) and remove disjoint small discs about
\(\rho=1,0,-1\) from \(|\rho|\le R\). This gives a compact surface
\(B_R\) with four boundary components. The two points above \(v=1/8\)
are filled by P3K.53's actual source/Cartier/root family. Its source
critical point is away from \(G\), its actual Hom map is a unit there,
and its selected-node charts persist. Thus these two discs introduce
no return.

The parameter discriminant is \(16v^2(v+1)^6(1-8v)^3\). On \(B_R\)
there are consequently no other excluded source degenerations. Choose
one cap annulus in the \(T\)-plane outside every finite critical value
for this compact parameter range. Its exact root equations are
\[
 y'^2=x'^3+(1-2v)z^{2p}x'^2+
 \begin{cases}x',&m=4p,\\zx',&m=4p-1,\end{cases}
 +v^2z^{6p},\qquad G'=(0,vz^{3p}).                   \tag{IFan.5}
\]
All resolution and Cartier corrections are the actual ones in P3K.49.
The central norm-ratio is the retained constant \(-2\) or \(+2\), so
its root and its logarithm with that reference extend on the root
disc times the bounded source-parameter disc. Finite averaging acts
on the line cochains while retaining their prescribed characters;
it preserves the literal equation \(A_0^m=B_0^n\).

Here is the full independent scalar family used in the argument:
\[
 B=r^mB_0(v),\qquad A=r^nA_0(v),\qquad A_0^m=B_0^n,
 \qquad
 F=F_0(v)+n\frac{\log r}{2\pi i}s_\infty\delta.      \tag{IFan.6}
\]
The map \(F\) is ordinary-to-cap. The fixed reference \(F_0\) includes
the actual integral annular period, every finite character and the
reduced doubled period. It is continued on the chosen cap annulus by
the parameter-disc exponential lifting and the fixed-contour Cauchy
splitting of P3K.49. The annular source is regular throughout the
bounded parameter disc. Its full source and line maps therefore
continue, rather than only their generic Picard classes.

On the overlap put \(q_1=q_\infty^{-1}h_\infty\),
\(h_\infty=1-(v^2-2v)q_\infty\). A positive scalar-root turn has the
actual forward maps \(R_{\rm ord}=q_1^n\) and
\(R_{\rm cap}=h_\infty^n\) on the physical line. Their exact square is
\[
 F_{\rm end}R_{\rm ord}=R_{\rm cap}F_{\rm start}.     \tag{IFan.7}
\]
The cap unit has its full extending logarithm; it is not replaced by
its central value. The actual parameter return uses the inverse of
the forward closing map after transport. In this theorem we take
\(r=r_0\) constant, \(r_0^m=\lambda_0\). Both scalar forward maps for
a loop in \(B_R\) are then the identity. The nonconstant source and
finite-root maps in \(F_0(v)\) remain in (IFan.6).

Choose \(\lambda_0\) in the common contracting range over compact
\(B_R\). All coefficients and their inverses have finite bounds in
the source/cap atlases. The norm shells and finite root quotients of
P3K.49 give the corresponding uniform proper quotient. This argument
uses a compact parameter surface; it does not claim one scalar works
at all arbitrarily small infinity radii. For two radii, the compact
annulus between them admits a common smaller scalar, and the actual
independent \(r\)-family gives the connecting zero-winding amplitude
path. This identifies the two loop returns by actual family transport.

## IFan.2. Every cone, full coefficient, and physical circle

The selected normalization on (IFan.4) is
\[
 X=s^2-1,\quad Y=s(s^2-\rho^2),\qquad
 Z=\frac{s-\rho}{s+\rho},\qquad
 P_G=\frac{1+\rho}{1-\rho}.                          \tag{IFan.8}
\]
The actual Tate period is \(Q=q_1\kappa\), with
\[
 \kappa(0,\rho)=-\frac{\rho^2-1}{64\rho^6}.
\]
Both \(P_G\) and the full \(\kappa\) are nonzero on the compact
parameter surface after taking a uniform selected disc. The chosen
nodal fourth root is \(2\rho\). The source branch marking is thus
single valued. A different lift of \(G\) by \(Q^j\) would have nodal
limit zero or infinity for \(j\ne0\), contrary to (IFan.8), so the
integer lift is fixed. The rigidified theta/Cartier line map supplies
the actual physical coordinate \(V\), with its degree-two correction
when \(a=2\).

For an absolute cone \(\sigma\) of the periodic fan, its affine
coordinate ring is generated by the characters
\(Z^uV^v q_1^h\) in the dual integral semigroup. Every change of period
basis carries the four full coefficients by
\[
 U'_{is}=\prod_{h,j}U_{hj}^{(P^{-1})_{ih}P_{js}}.     \tag{IFan.9}
\]
The inverse substitution uses \(P^{-1}\). This carries all higher
\(q_1\) terms, every source-parameter unit and the exact closing.
Multiplying an absolute character by a nowhere-zero base unit to an
integer power defines an automorphism on this actual affine chart;
its inverse retains the reciprocal unit. Therefore all these maps
extend across the toric divisors, and they agree on intersecting
cones as the same character maps. No unit logarithm is used to erase
parameter winding.

The resulting family has exactly the P3K.90 periodic chart atlas at
each source-zero boundary and the P3K.71 atlas at the selected-cusp
boundary. A finite set of cone orbits and the uniform norm bounds
give a compact fundamental region. The ordinary exterior and finite
caps are glued by (IFan.6), unchanged outside the selected disc. The
physical action is always \(V\mapsto e^{i\phi}V\). Thus the family is
smooth and proper over \(B_R\), with that actual action. Each fibre
is the completed oriented sphere of P3K.90: its proof constructs every
fan by the actual two-ruling replacements with the common-blowup
integral Gysin and primitive fundamental-group maps. The same full
coefficient maps (IFan.9) make those replacements relative to this
parameter surface.

The branch reflection is an especially explicit cone map:
\[
 \mathcal R_\rho:(Z,V,q_1)\longmapsto(Q/Z,V,q_1),
 \qquad P_G\longmapsto P_G^{-1}.                    \tag{IFan.10}
\]
It is the identity on the underlying marked source and Cartier
divisor, expressed in its two branch coordinates. Its line square
is the literal theta identity
\[
 \frac{\Theta_Q(QP_G/Z)}{\Theta_Q(Q/Z)}
       =\frac{\Theta_Q(Z/P_G)}{\Theta_Q(Z)}.
\]
For the actual \(M_a\), its canonical tensor/Cartier correction is
carried as well. On each character the pullback is exactly
\[
 Z^uV^v q_1^h\longmapsto
          \kappa^u Z^{-u}V^v q_1^{h+u}.             \tag{IFan.11}
\]
This is the integral dual-semigroup map of
\((x,y,h)\mapsto(-x+h,y,h)\), including its height translation. Its
square is the identity. It maps the entire fan \(\mathcal T(P)\) to
\(\mathcal T(JP)\), with the indicated integer translate. The ordinary,
cap and \(F_0\) maps depend on \(v\) and are carried identically.
It preserves the physical circle and complex orientation, including
the actual normal and line maps on every cone. More explicitly, write
the full periods as
\[
 H(Z,V)=(QZ,\alpha V),\qquad
 B(Z,V)=(gZ,q_1\eta V).
\]
The target coefficients are \((Q,\alpha^{-1},g^{-1},\eta)\), so the
literal maps satisfy
\[
 \mathcal R_\rho H=H_{\rm target}^{-1}\mathcal R_\rho,
 \qquad \mathcal R_\rho B=B_{\rm target}\mathcal R_\rho.
\]
These identities retain the entire coefficients, not only their
leading valuations, and prove equivariance with the full period
quotient and its physical line.

## IFan.3. The three finite local returns with their labels

At \(\rho=1\) the parameter \(v=\rho^2-1\) has positive complex
local degree one. The complete source, Cartier, root and \(F_0\)
markings above are those of P3K.90, so the positive return is
\(Z_a(P)\). At \(\rho=-1\) the derivative is \(-2\), again positive
as a real oriented complex local map. Equation (IFan.10), whose
ordinary/cap map is literally the identity, identifies that return
with \(Z_a(JP)\). It makes no identification of these two classes.

Near \(\rho=0\), choose the holomorphic cube root \(u^3=v\) with
\(u(0)^3=-1\), and put
\[
 X=u^2x,\quad Y=u^3y,\quad T=u^4t,\qquad
 \xi=x-u,\quad \sigma=\rho/u.
\]
The exact selected equation and its actual base map are
\[
 y^2=\xi^2(\xi+\sigma^2),\qquad
 q_{\rm old}=\frac{y^2-\xi^2(\xi+\sigma^2)}{\xi+u},
 \qquad q_1=u^4q_{\rm old}.                         \tag{IFan.12}
\]
The normalized source coordinate is \(s/u\), so its marked Tate
coordinate is exactly \((s-\rho)/(s+\rho)\). There is no branch
reflection at this interface. The local parameter \(\sigma\) has
nonzero complex derivative \(u(0)^{-1}\), hence preserves the
positive source loop. The divisor-defined line map scales the
primitive lift by \(u^{2a}\); the full suspension contains the
height \(u^{-4}\), so \(2ab-4=0\) keeps its scalar unchanged.
All cap-root factors of \(u\) have logarithms on this disc and carry
the full finite character. The degree-two Cartier map is conjugated
on its source and target, with both factors retained. These are the
actual local source/line/root maps of P3K.49 and the selected-source
maps of P3K.71. Their coefficient substitutions (IFan.9) extend on
every cone, so the third finite return is exactly \(C(P)\).

The unselected points over \(v=1/8\) have the actual P3K.53 disc
extension. Their source, Cartier and root maps are the identity on
the selected fan overlap; thus this disc extension also carries
every fan in (IFan.9), and its return is zero.

## IFan.4. Infinity: the full rescaling, root endpoint and annular lift

On the outer boundary put \(\epsilon=1/\rho\). The literal source
map is
\[
 X=\epsilon^{-2}x,\quad Y=\epsilon^{-3}y,\quad
 T=\epsilon^{-4}t,\quad v=\epsilon^{-2}-1,
 \qquad q_1=\epsilon^{-4}q_*.                       \tag{IFan.13}
\]
It gives (IFan.1). With \(s_{\rm new}=\epsilon s_{\rm old}\),
\[
 Z_{\rm old}=\frac{s_{\rm old}-\rho}{s_{\rm old}+\rho}
       =\frac{s_{\rm new}-1}{s_{\rm new}+1}
       =Z_{\rm new}.                               \tag{IFan.14}
\]
Consequently \(Q\) and \(P_G\) agree, and the selected fan remains
\(\mathcal T(P)\). The unit relation is
\(\kappa_{\rm old}=\epsilon^4\kappa_{\rm new}\), with
\(P_G=-(1+\epsilon)/(1-\epsilon)\) and
\(\kappa_{\rm new}(0)=-(1-\epsilon^2)/64\).
All integer \(\epsilon\)-powers are retained as actual units on the
parameter annulus. In particular their winding is not discarded.
In the displayed period notation the exact coefficient relations are
\(\kappa_{\rm new}=\epsilon^{-4}\kappa_{\rm old}\),
\(\eta_{\rm new}=\epsilon^{-4}\eta_{\rm old}\), while
\(\alpha\) and \(g\) are unchanged. Therefore both full periods
\((QZ,\alpha V)\) and \((gZ,q\eta V)\) agree in the transported
Tate/Cartier coordinates.

The line map is the canonical divisor map: on a local equation
\(f_D\) it carries the actual section \(f/f_D\) to its pullback in
the target divisor chart. Its coordinate factor is precisely the
ratio of the two pulled-back divisor equations. This definition
carries the degree-two Cartier correction and supplies the line
unit on every source chart. In the rigidified Tate frames its source
point and period are those in (IFan.14). Its primitive lift satisfies
\[
 I U_{a,\rm old} I^{-1}=\epsilon^{2a}U_{a,\rm new}.
\]
Therefore the complete suspension obeys
\[
 I\bigl(2(-1)^{b+1}\lambda q_1U_{a,\rm old}^{\,b}\bigr)I^{-1}
 =2(-1)^{b+1}\lambda q_*U_{a,\rm new}^{\,b}.          \tag{IFan.15}
\]
The actual Hom section checks this without omitting the height:
\(F_{ab,\rm old}=\epsilon^{-1}F_{ab,\rm new}\) and
\(v=\epsilon^{-3}g\), where \(g=\epsilon(1-\epsilon^2)\), give
\[
 \frac{q_1}{vF_{ab,\rm old}}
       =\frac{q_*}{gF_{ab,\rm new}}.                \tag{IFan.16}
\]
Any local Cartier unit is used with its reciprocal in the inverse
map and with its actual integer powers in all cone characters.
The full morphism has no additional fan reflection.

On the parameter logarithm cover the finite-root map is
\[
 z_{\rm old}=\epsilon^{4/m}z_{\rm new}.              \tag{IFan.17}
\]
The good minimal source coordinates are unchanged. In the reduced
root the old-to-new factors are \(\epsilon^{-2/m}\) and
\(\epsilon^{-3/m}\). Thus its positive endpoint is the actual
\(D^{-4}\), including \((\zeta_m^{-4},\zeta_m^{-2},\zeta_m^{-3})\)
on \((z,x',y')\) in the reduced case. The resolution ideals and
Cartier factors are carried by these coordinate maps.

Write \(A_0=L D\) for the actual signed division lift, with \(L\)
covering translation by \(-nR\). The good
central division point is \(O\). In the reduced root the actual line
is trivial on the compact III fibre, and both commuting source maps
have constant line multipliers there. The finite commutator character
is thus one. The prescribed eigenspace averaging retains its
conjugating unit and gives \([D,L]=1\) exactly. Hence
\[
 A_0^4D^{-4}=L^4.                                  \tag{IFan.18}
\]
The full finite action in (IFan.6) is \(A=r_0^n A_0\), so the
actual representative of this endpoint in the quotient is
\[
 A^4D^{-4}=S_{r_0^{4n}}L^4,                         \tag{IFan.18a}
\]
where \(S_c\) is multiplication by \(c\) on the physical line. This
constant scalar is retained. If the comparison along the logarithmic
parameter cut has endpoint \(H_1=D^{-4}H_0\), its endpoint-to-initial
correction is
\[
 G_1=S_{r_0^{-4n}}L^{-4},\qquad
 G_1(A^4D^{-4})=\mathrm{Id}.                        \tag{IFan.18b}
\]
The displayed equality is literal before passing to the quotient;
\(A^4\) is its specified deck map. Fix the same reference logarithm
\(\log r_0\) as in (IFan.6). The scalar part of \(G_1\) is carried
by the explicit based path \(S_{\exp(-4n\theta\log r_0)}\),
\(0\le\theta\le1\), on both ordinary and cap charts. This is a path
from \(1\) to \(r_0^{-4n}\), not a closed loop; these endpoints
implement the prescribed inverse closing. Its square is
\(F S_c=S_c F\) for every \(c\), including the full root/line and
normal maps. On the parameter logarithm cover the corresponding
holomorphic scalar cochain is
\(S_{\exp(-4n t_\epsilon\log r_0)}\), with one-step ratio
\(S_{r_0^{-4n}}\). It is part of the endpoint atlas, not asserted to
be a single-valued scalar on an unglued annulus.

The source translation of \(L^4\) specializes to the identity. Its
own central line scalar is likewise retained before taking the small
extending Lie logarithm. The inverse of that logarithm supplies the
remaining \(L^{-4}\) in (IFan.18b); its ordinary-to-cap comparison
is the full relative cochain described below. In the reduced branch the *annular* cochain still
contains the nonzero marked period
\[
 4\log R-\log(4R)=2\omega_1+2\omega_2,              \tag{IFan.19}
\]
where \(\omega_1,\omega_2\) are the actual transported source period
sections, with central square-lattice values \((1,i)\). Thus its
integral vector is \((2,2)\) and its central value is \(2(1+i)\);
the nearby period functions are retained. Its signed source part is
multiplied by \(-n\), since \(L\) covers \(t_{-nR}\), and the full Cartier factor is
carried at the same time. No logarithm of \(L^4\)
replaces that lattice cochain.

Fix a nonzero \(\epsilon_*\) and transport the entire original
ordinary-to-cap map there through (IFan.13--17). This defines the
reference infinity overlap, including its integral \(d\delta\).
Continue it by the parameter-disc exponential lifting and fixed
source-annulus Cauchy contours. Every integral or finite discrepancy
is locally constant and is zero at the full reference map; the two
atlases carry the same term (IFan.19). Remove an actual suspension
power before taking a Lie logarithm at a reduced component. Average
only the vector cochains over the finite group, and use their actual
Cartier exponentials. This constructs the same full \(F_0\) on both
sides, rather than choosing another annular clutch.

For completeness the scalar cochain of a general coupled reference
is also retained. With \(t_\epsilon=\log\epsilon/(2\pi i)\), the
old and new forward arrows for \(\lambda=v^{km}\lambda_0\) differ
by \(\epsilon^{8nk}\). Their compensating cochain is
\[
 c_0(t_\epsilon)=\exp[-2\pi i\,4nk\,t_\epsilon(t_\epsilon-1)],
 \qquad c_0(t_\epsilon+1)/c_0(t_\epsilon)=\epsilon^{-8nk}.
                                                               \tag{IFan.20}
\]
The full \((1-\epsilon^2)^k\) unit and the cap \(h_\infty\) unit
remain in the same square (IFan.7). In the fixed-scalar theorem
\(k=0\), this displayed correction is exactly one.

Finally the local comparisons on two angular annulus charts differ
by an actual extending translation. The source/line valuation
argument in P3K.49 identifies it with the physical scalar. For its
retained overlap logarithm \(\ell\), take
\(b_+=\chi_-\ell\), \(b_-=-\chi_+\ell\), solve
\(\bar\partial w=\bar\partial b_\pm\) by the fixed Cauchy kernel,
and use \(e^{b_\pm-w}\). The two maps glue on both overlap
components, with the integral winding and finite cocycle retained.
This includes both the scalar cochain in (IFan.18b) and the lattice
cochain in (IFan.19). It gives an actual single-valued annular family morphism, preserves
\(V\)'s physical circle, and intertwines the inverse endpoint
closings. It identifies the infinity return with \(I_a(P)\) of the
statement.

The separate half-turn map is
\(\mathcal I_\epsilon(Z,V)=(1/Z,P_G^aV)\). At its target
\(P_G\) is inverted, so \(h_{\rm target}\mathcal I_\epsilon=(Q/Z,V)\).
This is precisely (IFan.10). It does not modify (IFan.14); confusing
these two arrows would insert an erroneous \(J\) in (IFan.2).

## IFan.5. The actual loop product and the sphere class

Choose the lower-right corner of a rectangle containing the three
holes as basepoint and use disjoint vertical slits to their lower
points. The boundary of the cut surface gives the based positive
meridians, traversed in the displayed word order,
\[
 \gamma_+\gamma_0\gamma_-\gamma_\infty=1.            \tag{IFan.21}
\]
The positive infinity meridian is clockwise in \(\rho\) and positive
in \(\epsilon=1/\rho\). The coordinate maps above all have positive
complex local degree. Thus no boundary parameter is silently reversed.

Use a smooth connection in the actual proper sphere family, averaged
over the physical circle. Retain its slit transports as maps, not
only fibrewise conjugacies. On a lifted path the actual return is
\(R_{\rm end}^{-1}P_\gamma\), using the forward maps in (IFan.7).
For fixed \(r\) their total scalar winding is zero. More generally
the coupled reference has windings \(1,0,1,-2\), whose full forward
maps multiply to \(R_0=1\). The contraction of the cut-disc boundary
lifts to an isotopy
\[
 \Phi_\infty\Phi_-\Phi_0\Phi_+\simeq\mathrm{Id}.    \tag{IFan.22}
\]
This isotopy uses every cap and selected-cone endpoint already
constructed. It is an isotopy of the actual oriented sphere returns.

The oriented clutch identification with \(\Theta_7\) is additive
under composition. Its group is abelian, so the retained slit-path
conjugations have no effect after taking the class. The three finite
terms in IFan.3 and the infinity term in IFan.4 give
\[
 Z_a(P)+C(P)+Z_a(JP)+I_a(P)=0.
\]
This proves (IFan.2). It invokes the actual family morphisms before
passing to the group; it does not divide a covered sphere class.

## IFan.6. Vertical simplification and exact examples

The basis identity
\[
 P_{1-j}=J P_j S,\qquad
 S=\begin{pmatrix}-1&0\\1&1\end{pmatrix}
\]
is an identical-fan arrow. Its two triangles are translates of the
matched original triangles, and the identity on absolute characters
extends on their identical semigroups. This is one of the exact
column-swap/rotation arrows of P3K.71 and P3K.90. Thus the reflected
vertical fan is exactly \(T_{1-j}\), including its height translate.

Put
\[
 P_b(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2},\qquad b=3-a.
\]
P3K.89 gives \(Z_a(T_j)=P_b(j)\), and P3K.66 gives
\(C(T_j)=-1-3j(j-1)\), as actual classes with their full source
and cap arrows. Polynomial expansion gives
\[
 P_b(j)+P_b(1-j)=3j(j-1)+a.
\]
Substitution in the proved groupoid relation yields (IFan.3).
This is a statement in \(\Theta_7\); no individual infinity
characteristic pair is claimed.

For \(P=Q_0^2\), the two actual finite algorithms give
\[
 \begin{array}{c|rrr|r}
 a&Z_a(P)&Z_a(JP)&C(P)&I_a(P)\pmod{28}\\\hline
 1&6&31&-19&10\\
 2&9&59&-19&7
 \end{array}
\]
The middle entries are the algorithms' integer path representatives
before taking residues. They are not asserted to be infinity
characteristic integers. All other inputs are evaluated by the same
finite exact source-zero and selected-cusp algorithms in (IFan.2).

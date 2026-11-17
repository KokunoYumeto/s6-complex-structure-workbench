# OS49 with marked smooth order-one clutches: the integral groupoid and actual comparison

Working proof for independent audit, 17 November 2026. We retain the
exact OS49 source, component Cartier line, suspension, type-II model,
selected toric cusp and good IV-star cap of F26/F29/F33--34. The finite
cap has order \(m=3k\), invariant vector
\(n\ell_0+d\delta\), and the actual free action of F33. Here
\(k>0\), and initially \(n,d\) are the given integers; no coprimality
or norm-sign reduction is imposed. The chosen periodic index-one fan
is fixed, and can be any lattice-basis fan of K77.

Choose finitely many marked disjoint smooth-site discs, avoiding those
three source values. On each, retain the entire actual order-one
translation clutch, its line lift, and every annular unit. Our arrow
convention is ordinary-to-disc:
\[
 \Phi_i(x,z_i)=x+\frac{\log z_i}{2\pi i}\Pi(z_i)\ell_i
                         +u_i(z_i),\qquad \ell_i\in\Lambda.
\tag{OCS.1}
\]
Here \(u_i\) is its actual single-valued Lie part on the overlap,
with its full line component; the formula is read in the compact
torus quotient. All vectors are transported to the specified common
basepoint along the marked cuts. This includes any extra ordinary
framing chart with its actual signed vector. None is set to zero.
Put
\[
 \sigma=\sum_i\psi(\ell_i),\qquad D=n+m\sigma.
\tag{OCS.2}
\]

The calculation below gives the full integral translation-period
groupoid \(H^2=\mathbb Z\oplus\mathbb Z/k\). It then constructs
an actual holomorphic translation-family comparison to the one-cap
datum \((m,D,d)\), with the precise integer change of the finite
lift and its annular cochain recorded. Its finite quotient action
is the same action as the original cap. In particular the sphere
members of these data have exactly \(D=\pm1\). The proof does not
assign a return number before this family comparison is audited.

## OCS.1. The actual extending period sheaf

Order the homology lattice as \((\gamma,u,w,\delta)\), and set
\(\psi=(1,0,0,0)\), \(\ell_0=(1,-1,0,0)^t\). The actual marked
homology matrices, obtained as inverse transposes of F26.3, are
\[
 A=\begin{pmatrix}1&0&0&0\\0&1&-1&0\\3&3&-2&0\\1&1&-1&1\end{pmatrix},
 \quad B=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&-1&1&0\\0&0&0&1\end{pmatrix},
 \quad C=\begin{pmatrix}1&0&0&0\\0&1&0&0\\-3&-2&1&0\\-1&-1&0&1\end{pmatrix}.
\tag{OCS.3}
\]
They satisfy \(ABC=1\), \(A^3=1\), and \(\psi A=\psi B=\psi C=\psi\).
The finite root atlas has the constant lattice \(\Lambda=\mathbb Z^4\)
and cyclic group of order \(m\) acting by \(A\), including its
ineffective subgroup on this linear lattice. That subgroup is not
discarded.

At the retained II disc the extending period stalk is
\(\ker(B-1)=\mathbb Z\gamma\oplus\mathbb Z\delta\). The source
translation direction is the actual additive direction there; its
elliptic periods have no nonzero invariant combination. The suspension
period and the physical period extend by the actual line-complement
quotient. At the selected cusp the full period valuation matrix has
determinant one. Its two logarithmic radial periods therefore have
no nonzero bounded combination; the two angular periods extend as
the logarithms of the actual source and physical torus actions.
The stalk is exactly
\(\ker(C-1)=\mathbb Zw\oplus\mathbb Z\delta\).
These are the explicit kernel calculations of (OCS.3), and match
the unit charts in K44, OC.2. On each nonfinite disc the period sheaf
is the invariant extension \(j_*\Lambda\).

For completeness its higher cohomology on that disc is zero. On a
punctured disc the circle complex is
\(\Lambda\xrightarrow{M-1}\Lambda\). Its degree-one group is
the coinvariant lattice. In the radial extension this is exactly the
local degree-one term removed by passing from the punctured derived
extension to its invariant degree-zero sheaf: the map on that term
is the identity of the same marked circle complex. Equivalently,
using two slit sectors and the centre, the same cancellation gives
only \(\ker(M-1)\) in degree zero. This is an integral cancellation;
no rational averaging occurs. Smooth-site discs give the constant
lattice in degree zero and the same vanishing in higher degrees.

Let \(\mathcal A\) be the sheaf of extending translations of the
actual compactified suspension, on the full root atlas and groupoid.
Let \(\mathcal V\) be its holomorphic Lie sheaf and \(\mathcal H\)
its period sheaf just described. The exact sequence is
\[
 0\longrightarrow\mathcal H\longrightarrow\mathcal V
                  \xrightarrow{\exp}\mathcal A\longrightarrow0.
\tag{OCS.4}
\]
At the cusp this follows from the literal integral reindexing and
bounded unit map in K44, OC.7--8; logarithms of those units give
the local Lie lift on every same fan. At II it is the actual source
and line lift. On the good root it is the usual local exponential
cover of the smooth compact torus family, with its entire finite
group cochain retained. It is not an assertion of surjectivity on
invariant coarse sections.

The coarse terms of \(\mathcal V\) are \(\mathcal O\) and
\(\mathcal O(-1)\), as proved by the actual IV-star substitution
in K44, OC.3. The original source vector is \(z^{2k}\) times the
root vector and \(0\le2k<3k\), so this coarse extension has not
changed. Its vector extension splits by the Laurent calculation
\(H^1(\mathcal O(1))=0\). Thus
\[
                  H^1(\mathcal V)=H^2(\mathcal V)=0.
\tag{OCS.5}
\]
Finite averaging is used only on these complex vector sheaves.
It is not used on \(\mathcal H\); the latter has the torsion
computed next.

## OCS.2. A complete integral root-groupoid complex

Remove the three special discs. On their pair of pants use the
marked fundamental loops with product \(ABC=1\). A one-cochain
is \((p,q)\in\Lambda^2\); its three restrictions are
\[
                    p,\qquad q,\qquad -C(p+Aq).
\tag{OCS.6}
\]
The finite root disc uses the full cyclic resolution, whose
differentials alternate \(A-1\) and
\(N_m=1+A+\cdots+A^{m-1}\). Each of the other discs has only
the invariant degree-zero term described above.

A total degree-two cocycle is
\((\eta,b_A,b_B,b_C)\), with \(\eta\in\Lambda^A\) and
\(b_A,b_B,b_C\in\Lambda\). The complete degree-one relations,
for \(p,q,a,r,s,t\in\Lambda\), are
\[
 \begin{split}
 \eta&=N_m a,\\
 b_A&=p-a-(A-1)r,\\
 b_B&=q-(B-1)s,\\
 b_C&=-C(p+Aq)-(C-1)t.
 \end{split}                                           \tag{OCS.7}
\]
These are the Mayer--Vietoris cone maps of the displayed actual
restrictions. In particular the finite group relation appears as
\(N_m a\), and is not replaced by the order-three norm.

With extra ordinary boundary loops take the actual presentation
\(a b c\mu_1\cdots\mu_r=1\), where each \(\mu_i\) has identity
linear action in its transported frame. If its pair-of-pants
one-cochain is \(p_i\), the third restriction in (OCS.6) is
\(-C(p+Aq+\sum_i p_i)\), and its own restriction is \(p_i\).
Consequently (OCS.8) gains exactly \(\sum_i b_i\). Eliminating
each \(p_i\) is an integral identity block and gives the addition
of the full transported clutch vector used below. This fixes the
cut order and every vector transport in the calculation.

Eliminate \(p,q\) by the unimodular boundary-coordinate change
\[
                 v_*=b_A+A b_B+C^{-1}b_C.
\tag{OCS.8}
\]
Its determinant on the three lattice blocks is \(\det C^{-1}=1\).
The remaining relation in that block is
\[
 v_*=-a-(A-1)r-A(B-1)s-(1-C^{-1})t.                   \tag{OCS.9}
\]
The last three images generate precisely \(\ker\psi\), integrally.
Here is an explicit preimage table, with its three entries ordered
as the arguments of \((A-1),A(B-1),(1-C^{-1})\):
\[
 \begin{array}{c|ccc}
 \text{target}&r&s&t\\\hline
 u&-u&w&0\\
 w&-w&-u-w&0\\
 \delta&2w&2(u+w)&-Cu.
 \end{array}                                           \tag{OCS.10}
\]
Substituting (OCS.3) verifies every column. The row \(\psi\)
kills all three images. Thus the quotient is the primitive lattice
\(\mathbb Z\), without hidden finite index.

The invariant lattice of \(A\) is primitively generated by
\(\ell_0,\delta\), and the exact norm is
\[
 N_3=\begin{pmatrix}3&0&0&0\\-3&0&0&0\\0&0&0&0\\0&0&-1&3\end{pmatrix},
 \qquad N_m=kN_3.
\tag{OCS.11}
\]
Writing \(c\) for the remaining ordinary base generator, the
entire reduced relation matrix in the basis
\((\ell_0,\delta,c)\) is consequently
\[
 \begin{pmatrix}m&0&0&0\\0&0&-k&m\\-1&0&0&0\end{pmatrix}.
\tag{OCS.12}
\]
The first column gives \(c=m\ell_0\); the third gives
\(k\delta=0\), and the fourth is its multiple. Hence
\[
 H^2(\mathcal H)=\mathbb Z\ell_0\oplus(\mathbb Z/k)\delta,
 \qquad
 (\eta=n\ell_0+d\delta,v_*)\longmapsto
                   (n+m\psi(v_*),d\bmod k).
\tag{OCS.13}
\]
This is an integral atlas/groupoid computation. In particular its
\(\mathbb Z/k\) summand has not been lost by taking finite
invariants over \(\mathbb C\).

Adding a smooth disc is the same cone calculation with identity
linear monodromy and no finite group. Its full clutch vector is
transported along the marked cut, and contributes that vector to
\(v_*\). Thus its class in (OCS.13) is
\(m\psi(\ell_i)\ell_0\). The original cap cocycle is exactly
\(n\ell_0+d\delta\), because its lifted cyclic generator has
\(m\)-th power that period.

## OCS.3. The signed meridians and the exact integer cochain

The plus-log arrow (OCS.1) sends the zero section of the filled
disc to the path \(-s\Pi\ell_i\) in the ordinary coordinates.
Its filled positive meridian is therefore
\[
                         \alpha_i-\ell_i.
\tag{OCS.14}
\]
For the finite root the marked filled meridian is
\(m\alpha_A-(n\ell_0+d\delta)\), exactly F34.3. The II and cusp
fillings kill their base meridians and the primitive relation
lattice computed in F26. The surviving fibre quotient is
\(\mathbb Z\gamma\), measured by \(\psi\). The base relation
then gives \(\alpha_A=-\sum_i\psi(\ell_i)\gamma\), and the
finite power relation gives \(D\gamma=0\), with the plus sign
in (OCS.2). These are all generators and relations: each filled
boundary maps surjectively onto its local group, and the two
nonfinite relations reduce the original commuting torus generators
to this one generator. Thus
\[
                         \pi_1(X)=\mathbb Z/|D|,
\tag{OCS.15}
\]
where \(D=0\) means \(\mathbb Z\).

We now give the full integer cochain behind redistribution. Put
\(L=\sum_i\ell_i\) after the marked transports and
\(\sigma=\psi(L)\). The difference from the one-cap reference
\((m,D,d)\) has reduced cocycle
\[
                  (\eta,v_*)=(-m\sigma\ell_0,L).
\tag{OCS.16}
\]
Take the finite-root one-cochain \(a=-\sigma\ell_0\) in (OCS.7).
Its contribution is \((-m\sigma\ell_0,\sigma\ell_0)\).
The remaining vector \(L-\sigma\ell_0\) lies in \(\ker\psi\).
Use its actual \((u,w,\delta)\) coefficients in the negative
of the table (OCS.10) to obtain \(r,s,t\) in (OCS.9).
The eliminated \(p,q\) are recovered by the inverse of (OCS.8).
Thus (OCS.16) is the coboundary of a specified integral total
one-cochain, including every component of every original vector.
The slit-sector identifications in (OCS.6) are the actual parallel
transports along the marked cuts, so this is also a cochain on
the refined analytic atlas. No ordinary vector has been replaced
by its gamma projection without this cochain.

The finite action itself is retained. Its two displayed affine
lifts differ by
\[
 \frac{D-n}{m}\ell_0=\sigma\ell_0,
\tag{OCS.17}
\]
an invariant integral period of the actual smooth root torus.
They induce exactly the same automorphism of that torus and the
same finite quotient. Their lifted norm and annular logarithm
differ by the recorded one-cochain, not by an omitted choice.
The delta coefficient is unchanged: \(N_m(-\sigma\ell_0)\)
has zero delta component. The fixed finite character \(d\)
therefore remains the original one. Since \(D\equiv n\pmod m\),
the free-action criterion of F33 holds for both displayed data.

The same change has a literal source/line-cover expression. Retain
the actual commuting cap and suspension maps and put
\[
 B_r=r^mB_0,\qquad A_{n,d,r}=r^nA_{n,d,0},\qquad
 A_{D,d,r}=B_r^\sigma A_{n,d,r}.
\tag{OCS.17a}
\]
Then \((A_{D,d,r})^m=B_r^D\) and
\(\langle A_{D,d,r},B_r\rangle=\langle A_{n,d,r},B_r\rangle\).
The root coordinate is unchanged. In the root marking the
suspension period is the invariant \(\ell_0\); its full source
and line factors are those of F29, not just its gamma covector.
Thus (OCS.17a) gives exactly the invariant lattice change in
(OCS.17), with central line factor \(B_0^\sigma\) and scalar
factor \(r^{m\sigma}\) retained. Its fixed delta character
commutes with these maps. Identity on this quotient is the
finite-cap map used in (OCS.18).

## OCS.4. Realizing the cochain by actual holomorphic family maps

Compare the given clutched family with that one-cap reference
using the unchanged local ordinary, II, cusp, and root models.
Their local overlap differences are actual sections of
\(\mathcal A\). On simply connected atlas sectors choose the
actual holomorphic Lie lifts, including their source and line
coordinates. Their lattice-valued total two-cocycle is precisely
the one computed in OCS.2--3. Subtract the periods of the explicit
integral one-cochain in (OCS.16). The resulting Lie one-cochain
is closed on all ordinary overlaps and on the full cyclic
root groupoid.

Solve this closed cochain by (OCS.5). This is an actual analytic
operation: split the negative and nonnegative Laurent parts in
the two coarse summands \(\mathcal O\), \(\mathcal O(-1)\),
use the same Laurent splitting for their extension, and average
only the resulting complex vector cochains at the finite root.
On a refinement of the given discs, fixed Cauchy contours give
the identical solution. All source and line units in (OCS.1)
are inputs to these integrals and are retained.

Here is its exact map convention. Write the new overlap as
\(g^{\rm new}_{ij}=t_{\theta_{ij}}g^{\rm ref}_{ij}\), with
linear Lie action \(L_{ij}\). The solved equation is
\(\theta_{ij}=s_i-L_{ij}s_j\). The local maps
\[
 F_i=t_{-s_i},\qquad
                F_i g^{\rm new}_{ij}=g^{\rm ref}_{ij}F_j
\tag{OCS.18}
\]
therefore glue literally. Their inverses are the opposite
translations. On the cusp their exponentials are the full bounded
torus units after the exact period reindexing of K44, OC.8; those
units and their inverses extend on every cone of the same fan.
On the root, (OCS.18) is also the finite-deck square because the
finite group terms were included before averaging. The source
translation lifts to the actual degree-zero root line, and the
generic compact-elliptic commutation argument in K44, OC.1 extends
that equality across the root. At II it uses the original reduced
line-complement quotient. Thus these are actual holomorphic maps
of the filled families and their lines, including their normal
collars, rather than only isomorphisms of cohomology classes.

For a varying scalar all of this is analytic on a small parameter
disc: the period matrix, source/line lifts and given overlap units
are analytic, and the Cauchy contours can be fixed. The integral
cochain in OCS.3 is constant, including its finite group terms.
The canonical parameter can be \(\lambda=r^m\); the original
finite lift, the changed lift, and their parameter-closing arrows
remain part of (OCS.18).

The local parameter comparisons glue over an annulus as follows.
Their ratios are global extending translations. The fixed-scalar
endpoint proof of K44, OC.3 applies here without a restriction on
the free norm \(n\): the root commutator has \(m\)-fold value
\(B^{ma}\), and \(A^m=B^n\) and commutation with \(B\) still
force \(a=0\). Its rational source/line lift is \(fU^j\);
the actual divisor of \(B_0^{-1}/U^3\) still gives \(v_*=j/3\).
Thus \(j=3a\) and \(fU^{3a}=cB_0^{-a}\), which on the quotient
is the actual physical scalar \(c\lambda^a\). The entire global
translation group is consequently the same physical \(\mathbb C^*\),
with every finite kernel included. This also holds on the new
torsor because translations commute and hence have the same
translation sheaf.

The parameter Isom torsor is therefore a holomorphic
\(\mathbb C^*\) torsor. Here is an explicit smooth nonzero section
on a thin annulus. Take local holomorphic comparisons \(F_\alpha\),
with \(F_\alpha=c_{\alpha\beta}F_\beta\), and a smooth partition
of unity \(\rho_\beta\) on their parameter cover. The forms
\[
 \mathfrak a_\alpha=
       \sum_\beta\rho_\beta\,d\log c_{\alpha\beta},
 \qquad
 \mathfrak a_\alpha-\mathfrak a_\gamma
                         =d\log c_{\alpha\gamma}
\tag{OCS.18a}
\]
define a connection on this actual torsor. Angular parallel transport
from one chosen point gives a nonzero comparison \(F^{\rm par}_\theta\),
with holonomy \(c\in\mathbb C^*\). Choose a logarithm of that
one scalar and a smooth lift \(\chi\) satisfying
\(\chi(\theta+1)=\chi(\theta)+1\), constant on the prescribed
parameter collars. Then
\(\exp(-\chi(\theta)\log c)F^{\rm par}_\theta\) is a smooth
periodic section, with all derivatives matched.

Extend it to a thin radial annulus by the explicit connection ODE.
In a local comparison frame its scalar coefficient satisfies
\[
 \partial_\varrho z_\alpha
     =-\mathfrak a_\alpha(\partial_\varrho)z_\alpha,
 \qquad
 z_\alpha(\varrho,\theta)=z_\alpha(\varrho_0,\theta)
    \exp\left(-\int_{\varrho_0}^{\varrho}
           \mathfrak a_\alpha(\partial_s)\,ds\right).
\tag{OCS.18b}
\]
The transformation rule in (OCS.18a) makes these solutions agree
under the original transition scalars. The connection and the
initial circle section are periodic, so the extended section is
periodic as well. It is nowhere zero and consists throughout of
actual family isomorphisms.
In the associated line write its induced antiholomorphic derivative
as \(\bar\partial s=\omega s\). Extend the coefficient of
\(\omega\) smoothly with compact support to a plane neighbourhood
and put
\[
 u(r)=\frac1\pi\int\frac{\omega_{\bar w}(w)}{r-w}\,dA(w).
\tag{OCS.19}
\]
On the smaller annulus \(\bar\partial u=\omega\), so
\(e^{-u}s\) is an actual nonzero holomorphic section. Multiplication
by this scalar acts on all original line, toric and finite-cap
charts. It changes no finite character or annular lattice vector.
This proves a closed holomorphic family isomorphism on the parameter
annulus, with the actual endpoint arrows carried. It does not infer
trivial loop transport from a fibrewise conjugacy.

The physical return can also be checked directly before this last
scalar adjustment. Retain the actual parameter period matrix:
on the positive canonical \(r\)-loop, with \(\lambda=r^m\),
its cut logarithm obeys
\[
             \Pi(v+1)-\Pi(v)=m\delta\psi,
                \qquad v=\log r/(2\pi i).
\tag{OCS.19a}
\]
Thus the change of the full ordinary clutch (OCS.1) is
\(m\psi(\ell_i)\log(z_i)\delta/(2\pi i)\); its source and
fixed delta components are unchanged. Its inverse forward-closing
factor is exactly \(z_i^{-m\psi(\ell_i)}\). The finite cap
contributes \(t^{-n}\) in the original OS49 base coordinate, with
finite cap at \(t=0\) and selected cusp at infinity. With fixed
clutch units the ordinary forward map is consequently
\[
 f_X(t)=t^{-n}\prod_i(t-c_i)^{-m\psi(\ell_i)},
 \qquad f_Y(t)=t^{-D}.                               \tag{OCS.19b}
\]
At each site all the other factors are retained as its extending
cap unit. At the cusp the first map has valuation \(D\), and its
ratio to \(q^D\) is the full extending unit. Its actual toric
period reindexing is the one in K76. Any given additional
parameter-dependent unit is likewise retained in its prescribed
closing arrow. Formula (OCS.19a), rather than a parameter-constant
period convention, is used in the comparison.

Let \(F_t:X_t\to Y_t\) be the constructed interval comparison,
where \(Y\) is the canonical datum \((m,D,d)\) at the same scalar.
Let \(E_X:X_0\to X_1\) and \(E_Y:Y_0\to Y_1\) be the actual
forward endpoints just specified, including their root squares and
all units, and let \(P_Y:Y_0\to Y_1\) be smooth parallel transport.
Both endpoints carry the same marked parameter lattice deck
(OCS.19a); all remaining factors are the actual translation
cochains. Therefore
\[
 C=F_1E_XF_0^{-1}E_Y^{-1}:Y_1\longrightarrow Y_1
\]
is a global extending translation with identity linear lattice
part. The endpoint calculation above identifies it with a physical
scalar, including every finite root kernel. The literal equations
are
\[
 F_1E_XF_0^{-1}=CE_Y,\qquad
 F_0\bigl(E_X^{-1}F_1^{-1}P_YF_0\bigr)F_0^{-1}
                       =E_Y^{-1}C^{-1}P_Y.            \tag{OCS.19c}
\]
The actual scalar isotopy removes \(C\). This is the oriented
physical return conjugacy. In the sphere sector \(D=\pm1\),
\(E_Y\) is precisely the K76 canonical positive \(r\)-endpoint,
so the positive \(r\)-return has class \(S_m(P)\) of K77.

There is also a specified shorter endpoint obtained by transporting
the exact OR65 endpoint through this family map. If
\(C^Y_r:Y_{\zeta_3r}\to Y_r\) is its endpoint-to-initial map, set
\[
                 C^X_r=F_r^{-1}C^Y_rF_{\zeta_3r}.
\tag{OCS.19d}
\]
Every cap square and intermediate-sheet product is conjugated by
these same maps, including its full three-step norm. The induced
shorter family is isomorphic to the K77 shorter family and has
return \(S_k(P)\). This concerns this actual transported endpoint;
it assigns no value to an additional unspecified short-loop
identification.

## OCS.5. Topology and the precise completed scope

The map (OCS.18)--(OCS.19) identifies the given family with the
one-cap family \((m,D,d)\) at the same scalar and on the same fan.
All original annular integers remain in the explicit comparison.
F34 now computes its entire integral homology with \(n\) replaced
by \(D\); its finite torsion factor is unchanged because
\[
              \gcd(m,D,3d)=\gcd(m,n,3d).
\]
Together with (OCS.15), this proves that its sphere members are
exactly \(D=\pm1\). Their comparison target is precisely the
actual K76 datum of that norm sign, with order \(m\), delta
character \(d\), and the original source/Cartier marking.

This concerns finitely many fixed, marked, smooth order-one sites
and their actual translation clutches. The map transports their
full affine and line data. No additional singular-site replacement,
change of source, or arbitrary nontranslation endpoint is included.
The source-zero collision work and its unresolved compact
attachment are separate from this fixed-source calculation.

The complete integer matrices, primitive preimages, 14-by-24
total degree-two map, reduced relations and the explicit
redistribution cochain are executed in
`code/part3/os49_order_one_groupoid.py` and its saved outputs.


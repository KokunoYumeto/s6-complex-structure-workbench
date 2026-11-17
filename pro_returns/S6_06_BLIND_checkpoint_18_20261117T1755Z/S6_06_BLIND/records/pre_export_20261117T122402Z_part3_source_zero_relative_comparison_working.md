# Relative old-u / new-v source-zero comparison

Proved punctured-family comparison after root audit, 17 November 2026. The finite
fan execution is separate. This note retains the original normalized
E7 presentation, the literal new presentation and their cap/annular
arrows. Sections RCZ.5–7 explicitly complete the previously unselected
reference annular marking F0, starting from the entire old map at one
marked parameter. The earlier unresolved version is preserved in
records under `pre_reference_F0_...md`. No numerical source-loop
return is assigned by this comparison.

## RCZ.1. The actual common source, line and suspension

The coordinate arrow is
\[
 I_u:(x,y,t,u)\longmapsto
 (X,Y,T,v)=(u^2x,u^3y,u^4t,u^3).
\]
It carries G and O to their marked counterparts and carries the
canonical Cartier line \(M_a=\mathcal O(aG-O)\), for
\((a,b)=(1,2),(2,1)\), by its actual divisor map. The primitive
translation lift and selected-base coordinate satisfy
\[
 I_uU_{a,\mathrm{old}}I_u^{-1}=u^{2a}U_{a,\mathrm{new}},
 \qquad q_{\mathrm{old}}=u^{-4}q_{\mathrm{new}}.
\]
Since \(ab=2\), these factors cancel in the actual suspension
\(2(-1)^{b+1}\lambda qU_a^b\). The scalar is therefore the same
literal scalar, not a scalar with an omitted u-power.

The cusp Tate period and marked section point agree under I_u.
Its physical-height unit is retained as
\(q_{\mathrm{old}}/q_{\mathrm{new}}=u^{-4}\). On the u-annulus
this is an invertible integer-power toric multiplier. It preserves
the chosen fan and physical delta character. Its parameter winding
is retained; no global logarithm of u is chosen here.

For a cap of order m, the root arrow on the logarithmic u cover is
\[
 z_{\mathrm{old}}=u^{4/m}z_{\mathrm{new}}.
\]
For the good root \(m=4p\), the minimal coordinates satisfy
\(X'_{\mathrm{new}}=x'_{\mathrm{old}}\) and
\(Y'_{\mathrm{new}}=y'_{\mathrm{old}}\). For the reduced root
\(m=4p-1\), they satisfy
\[
 X'_{\mathrm{new}}=u^{-2/m}x'_{\mathrm{old}},\qquad
 Y'_{\mathrm{new}}=u^{-3/m}y'_{\mathrm{old}}.
\]
These maps carry the actual section to
\((0,vz_{\mathrm{new}}^{3p})\), preserve the specified resolution
ideals, and commute with the root deck D. Their full positive
u-loop endpoint is \(D_{\mathrm{new}}^{-4}\). In the reduced
coordinates this is exactly
\[
 (z,X',Y')\longmapsto
 (\zeta_m^{-4}z,\zeta_m^{-2}X',\zeta_m^{-3}Y'),
\]
because \(4p=m+1\). This is the root endpoint; it is not silently
replaced by the identity on the affine cap.

## RCZ.2. The extending fourth translation and its retained period

Let R be the actual division section \(mR=Q\), with the branch
specified in F41 or F37. The signed affine cap is represented by
\(A=L D\), where L covers \(-nR\), and its scalar normalization
is the one giving \(A^m=B^n\). We retain the finite eigenspace
construction used for L.

Its central commutator character is one in both actual branches.
In the good branch R specializes to O, so L on the central compact
elliptic fibre is a scalar line automorphism. Such a scalar commutes
with the actual D lift. In the reduced branch the line is
\(N=\mathcal O(2G'-O)\). The doubling formula puts 2G' at O on
the reduced central fibre. Both meet its smooth locus, so the
restriction of this Cartier line is literally the trivial line;
its component degrees are also zero. In a trivialization of that
line, the central line multipliers of D and L are holomorphic
units on a compact connected reduced curve, hence constants.
Their source maps commute because D fixes R. Their line maps
therefore commute as well. Thus the finite eigencharacter is one.

The actual finite eigenspace lift can consequently be chosen with
\(DLD^{-1}=L\). Its norm normalization is a base-invariant unit
and preserves this equality. This is the exact normalized lift
used in the cap; any initial unit discrepancy is removed by its
finite averaging conjugation, with that conjugation retained on
the annulus. In these charts
\[
                         A^4D^{-4}=L^4.
\]
The map on the right is an actual extending line map. In the good
branch its central source translation is zero. In the reduced
branch R specializes to the nonidentity two-torsion point, so
\(-4nR\) also specializes to zero. Hence L^4 restricts to a
nonzero scalar on the central fibre. On a simply connected
parameter chart divide by that scalar, take its scalar logarithm,
and use the inverse of the exponential near the identity of the
extending translation group. This produces a small extending Lie
logarithm of L^4. It does not identify that logarithm with four
times an annular logarithm of L.

In particular, on the marked good fourth root of the reduced
branch, write its square lattice as \(\mathbb Z+i\mathbb Z\),
with \(R(0)=(1+i)/2\). A logarithm tending to this half-period
satisfies
\[
             4\log R-\log(4R)=2(1+i),
\]
where the second logarithm is the small one. With signed n the
source part is multiplied by n. The full line-period vector is
the actual difference of the two lifted line logarithms; it
includes the Cartier factor of automorphy. It is retained as an
integral annular cochain. No parameter-dependent multiple of
this source period is asserted to extend across the reduced cap.

The exact finite-unit conjugation has a useful elementary form.
In the input-scalar convention, let an actual cap map be
\(A'=\beta A\), where \(\prod_{j=0}^{m-1}\beta(D^jz)=1\)
and its central character has already been matched. Put
\(g=\log\beta\), with central value zero, and
\[
 f(z)=-\frac1m\sum_{j=0}^{m-1}j\,g(D^jz).
\]
Then \(f(Dz)-f(z)=-g(z)\), and multiplication by \(e^f\)
conjugates A' to A. The maps and logarithms depend holomorphically
on the parameter on each chosen parameter chart. The finite
character is matched before this zero-central logarithm is taken.

## RCZ.3. The relative Lie solve and the full groupoid

Over a simply connected small parameter chart in the u-annulus,
the actual extending translation Lie bundle has
\[
 0\longrightarrow\mathcal O\delta\longrightarrow V
       \longrightarrow\mathcal O(-1)\longrightarrow0
\]
on the coarse source base. This is the relative version of CP.1.
Indeed the root substitution sends the source dualizing vector
to \(z^k\) times the root vector, with its exact deck character
\(\zeta_m^k\), and \(0\le k<m\). Its invariant extension is
therefore the original source Lie line. The Weierstrass invariant
differential and I_u supply the actual relative line frames;
their extra u-powers are units on this parameter chart.

The extension splits by the ordinary Cauchy/Laurent solution for
\(\mathcal O(1)\). The same fixed-circle integrals solve every
V-valued base one-cocycle for \(\mathcal O\) and
\(\mathcal O(-1)\). These integrals preserve holomorphic
parameter dependence. Finite averaging applies to these complex
vector cochains. Thus the relative first coherent cohomology of
V over the source base is zero, with an explicit parameter-dependent
solution operator.

The exponential sequence is used on the entire root atlas and
its groupoid,
\[
 0\longrightarrow H\longrightarrow V\longrightarrow A
       \longrightarrow0.
\]
At a reduced root, the actual suspension-power removal of its
component translation is made before taking the identity-component
logarithm, exactly as in CP.3. Lie exponentiation alone is not used
to erase a disconnected component.
Atlas logarithms are not presumed invariant. Their ordinary
overlap discrepancies and all finite cyclic-group discrepancies
form a total integral two-cocycle. Its finite terms retain the
literal equation \(A^m=B^n\), the central line character and
the actual period lift. The doubled period in RCZ.2 is carried
by that total cochain whenever parameter charts are changed.
Only after the two actual total two-cocycles have been compared
is the remaining V-valued one-cocycle solved by the preceding
operator. No assertion about surjectivity of exponentiation on
coarse invariant sections is used.

All resulting local exponentials are the extending source/line
maps of CP.3. At the cusp their two characters become bounded
holomorphic units after the actual integral component reindexing;
at every finite root they are the line lifts on the actual
resolved source, with the stated finite character. These local
maps therefore transport the annular and Cox normal charts as
actual maps.

## RCZ.4. The parameter scalar group and explicit analytic factorization

On the punctured source-parameter annulus every source has the
same marked Mordell--Weil group \(\mathbb ZG\). The endpoint
calculation CP.3–4 applies relative to this annulus. In particular
an actual global extending translation lifts off the selected cusp,
its source part is \(jG\) with j locally constant, and its line
part is a rational base function times the primitive lift U_G^j.
The cap orders and root characters give its exact valuations.
The selected cusp uses its actual integer reindexing. Taking the
degree of that rational divisor gives the same equality
\(j=bk\) as CP.4, and the norm ratio identifies the full map
with a physical scalar. Evaluation at one ordinary marked origin
shows that this scalar is holomorphic in the source parameter.
Conversely every such holomorphic nonzero scalar extends through
all the actual charts. The relative global translation group is
therefore the physical \(\mathcal O^*\), with no omitted finite
kernel.

Here is the explicit parameter factorization used for locally
constructed family comparisons. Cover a slightly larger round
u-annulus by two angular charts U_+,U_-, with simply connected
overlap components. Write the actual scalar transition as c and
choose a holomorphic logarithm \(\ell\) on each overlap
component. Choose a smooth angular partition \(\chi_++\chi_-=1\)
subordinate to these charts, and put
\[
 b_+=\chi_-\ell,\qquad b_-=-\chi_+\ell.
\]
These are extended by zero away from the respective overlap
supports. They satisfy \(b_+-b_-=\ell\), and
\(\bar\partial b_+=\bar\partial b_-\) is a globally defined
smooth (0,1)-form \(\eta=f(u)d\bar u\). Choose a radial cutoff
equal to one on a smaller closed annulus carrying the loop and
compactly supported in the larger annulus. Extend the cut-off
coefficient by zero to the plane and set
\[
 v(u)=\frac1\pi\int_{\mathbb C}
             \frac{\widetilde f(w)}{u-w}\,dA(w).
\]
The distribution identity
\(\bar\partial_u(1/(\pi(u-w)))=\delta_w\) gives
\(\bar\partial v=\eta\) on the smaller annulus. Thus
\[
 h_+=e^{b_+-v},\qquad h_-=e^{b_--v}
\]
are nonvanishing holomorphic functions with \(h_+/h_-=c\).
When the local comparison maps have the actual arrow
\(I_+=cI_-\), the maps \(h_+^{-1}I_+\) and
\(h_-^{-1}I_-\) glue literally. All multipliers are physical
scalars; their action on the line and normal coordinates is the
specified one. This gives the analytic factorization, including
both overlap components and any winding of c.

For the actual scalar rescaling \(\lambda=v^N\lambda_0\),
write \(N=km\), \(v=u^3\), and
\(t=\log u/(2\pi i)\). The old and new ordinary forward decks
are \(q_{\mathrm{old}}^{3kn}\) and
\(q_{\mathrm{new}}^{3kn}\); their ratio is
\(u^{-12kn}\). The literal compensating scalar cochain is
\[
 c_0(t)=\exp\bigl(2\pi i\,6kn\,t(t-1)\bigr),
 \qquad \frac{c_0(t+1)}{c_0(t)}=u^{12kn}.
\]
This is retained in the forward endpoint square. It is not
declared to be a single-valued multiplier by itself, or to extend
over u=0 in the old coordinates. Any remaining scalar transitions
are treated by the factorization just given.

## RCZ.5. Completing the previously unselected annular marking

Section 21 of `part3_source_zero_completion_working.md` left F0
specified as a holomorphic actual reference-scalar overlap, without
choosing its absolute integral annular marking. We now make that
choice. Fix a nonzero u* and put v*=u*^3. Transport the **entire**
old ordinary-to-cap map at u* through the canonical source/Cartier
arrow I_{u*}, including its chosen root cut, signed norm, prescribed
\(d\delta\), and every period in its lifted logarithm. Call this
actual map F*. The new F0 is constructed below to restrict exactly
to F*. This is completion of the previously unselected data; it is
not a proof that an unrecorded different choice had the same integer.
The new analytic norm root uses the transported old value at this
reference point and the same prescribed finite character. Its
nonvanishing norm unit extends on the root polydisc, so this branch
continues analytically there. The finite unit conjugation in RCZ.2
is included before F* is regarded as a map into that new cap.

Choose a fixed cap-overlap annulus C in the T-base sufficiently far
from the colliding finite fibres. All source fibres above C remain
smooth elliptic curves for v in a full sufficiently small disc D,
including v=0. The root source, its actual corrected Cartier line,
its division branch and its normalized A0 extend on this product by
the displayed good/reduced equations and resolved line diagrams.
At a fixed sufficiently small reference scalar, the ordinary and
cap norm quotients are therefore smooth proper families of compact
complex tori over C×D.

There are literal local comparison maps on this whole product.
Cover C by two angular charts C_+,C_-. Choose a root branch z_i(q)
on each. Restriction to that chosen sheet gives a map from the
ordinary pullback line quotient to the cap quotient. It has no
residual quotient: an element \(A^jB^h\) fixing that sheet has
\(j=mk\), and is exactly \(B^{nk+h}\). Thus the fibre on the
chosen sheet is precisely \(N^\times/\langle B\rangle\).
The source/Cartier identification supplies the claimed local map.
On overlap, its map between sheets is the literal indicated power
of A0, including its line character and the relation \(A_0^m=B_0^n\).
This description continues through v=0 on C; no singular source
fibre occurs in this overlap annulus.

The two local comparisons differ by translations in the actual
Jacobian family J over C×D. Its Lie bundle V is holomorphically
trivializable there by the source dualizing vector, physical delta,
and the same additive Cauchy splitting of their extension. One can
also use the literal constant-factor-of-automorphy presentation of
the degree-zero elliptic line on each simply connected angular
chart. Its periods and marked Picard point are holomorphic in
(q,v), including at v=0. These are frames of the actual line
translation group, not an identification with an unrelated torus.

Correct each local comparison on C_i×{v*} to equal F*. The required
translation has a holomorphic logarithm on the simply connected
C_i. Extend its coefficients in the just specified Lie frame
holomorphically in v, and exponentiate. This makes local actual
maps E_i on C_i×D satisfying E_i|_{v*}=F*.

Their overlap translation is the identity at v*. It therefore has
a unique holomorphic Lie logarithm \(\ell_{ij}(q,v)\) whose value
at v* is zero. To construct it, lift along the simply connected
v-disc through the exponential covering of the smooth torus
family, starting at zero; uniqueness gives holomorphic dependence
on q as well. The overlap components are simply connected. Any
ordinary or finite-group discrepancy of these logarithms is an
integral period and is zero at v*. It remains zero throughout D.
The finite root groupoid has not been forgotten: its free-sheet
description above carries every A0 power and its norm to these
ordinary overlap maps. In particular its bar-resolution terms are
carried by those exact maps before the logarithms are chosen.

Thus \(\ell_{ij}\) is a genuine V-valued one-cocycle, vanishing
at v*. Apply the q-variable Cauchy splitting with contours and
partition independent of v. The integrals preserve holomorphic
v-dependence and vanish at v*. Exponentiating the resulting
cochains glues the E_i to an actual holomorphic comparison
\[
             F_0:\mathcal Y|_{C\times D}
                         \longrightarrow\mathcal C|_{C\times D},
                   \qquad F_0|_{v*}=F^*.
\]
This constructs continuation in the actual Hom/source-period
torsor. It does not merely transport an abstract lattice vector.
The integral T-annulus cocycle of this map is locally constant in
v in its transported period lattice. At v* it is exactly that of
F*, so it retains the prescribed dδ and full reduced doubled
period throughout D. Inserting an extra \(q^j\delta\) would
change F*; no such insertion occurs in this construction.
The physical delta part has the literal coordinate check
\(q_{\rm old}^d=u^{-4d}q_{\rm new}^d\). Its q-order is d
on both sides. The remaining u-unit is retained in the physical
scalar comparison; it is not a new annular integer.

## RCZ.6. The chain extension and the common base-direction cocycle

On a cut angular chart, the constructed F0 lifts to an actual
nonzero-line map. Lift the value of the marked origin through the
regular covering \(N^\times\to N^\times/\langle B_0\rangle\).
The cut annulus times D is simply connected, so this gives a
holomorphic source point and a nonzero line vector. The
degree-zero Hom-line argument of CP.3 then gives an invertible
line lift over the source fibre; its multiplier is holomorphic
and nonzero through v=0. It commutes with B0 by the literal
constant-factor-of-automorphy calculation. On two such charts
the maps differ by the actual integral deck power, not by a
newly chosen pointwise identification.
Every such line map also commutes with physical scalar
multiplication. Hence its B0 commutation is the exact commutation
with the rescaled suspension \(v^N\lambda_0B_0\) as well;
no change of the source lift is made at that step.

Consequently these maps act in the finite-cap chain charts by
the actual source map and
\[
 (X_j,Y_j)\longmapsto
           (a(q,v)X_j,a(q,v)^{-1}Y_j),
\]
with a a nonzero holomorphic unit through v=0. Their integral
deck ambiguities are retained as the corresponding chain-index
translations. In particular, for \(N=km\) the root A shifts
the index by kn, B by km, and the actual sheet relation remains
\(A^m=B^n\). The prescribed dδ changes only the retained
single-valued line multiplier on the overlap; q is nonzero
there, so that multiplier also extends through v=0.
Here a(q,v) denotes the multiplier in the chosen rigidified
constant-factor line coordinates of the actual degree-zero
line. The Cartier-to-rigidified coordinate maps are carried
with it; the formula does not identify every original Cartier
chart's multiplier with the same scalar function.

For the rescaled scalar, the exact Section 21 cochain is still
\(F=F_0+nk\,t_v s_\infty\delta\), where
\(t_v=\log v/(2\pi i)\). Its ordinary and cap origins obey
the already checked literal equality
\[
 F+o_{\rm ord}-o_{\rm cap}=F_0.
\]
A positive root-cut continuation multiplies the new line
coordinate by \(v^{nk}\), exactly its chain shift kn, with
the same A0 source and line map. The parameter deck is the
retained pair \(q_1^{nk},h^{nk}\), and
\(F_{t_v+1}R_{\rm ord}=R_{\rm cap}F_{t_v}\) is unchanged.
Thus the new choice of F0 extends in the existing chain atlas
and commutes with its chosen root, Cartier and norm maps. No
fractional power of v is inserted in a single central chart.

The ordinary origin itself is not a single-valued central
coordinate. With the exact convention
\(\eta=\zeta-o_{\rm ord}\) and
\(o_{\rm ord}=nk\,t_v s_1\delta\), positive continuation
of q1 at fixed old coordinate changes
\[
 \eta\longmapsto\eta-nk\,t_v\delta,
 \qquad V_\eta\longmapsto v^{-nk}V_\eta.
\]
Its inverse gluing arrow multiplies by \(v^{nk}\). Positive
q-infinity continuation has \(s_1\mapsto s_1-1\) and hence
the opposite sign, giving the \(v^{nk}\) cap-cut factor above.
These are the actual two arrows. Their compatibility with the
literal h,g collision-fan atlas is a separate remaining assembly
calculation. This note does not use the ordinary origin to
identify central E-chain components in that fan.

Now compare the old u-family with the pullback of this marked
v-family on the u-annulus. At u* the source, line, cap and cusp
maps agree, with the reference annular arrow just constructed.
All their integral base-direction total two-cocycles therefore
agree at that point. Under the actual I_u identification of
period lattices, their difference is a locally constant class:
choose atlas logarithms on a small simply connected parameter
chart and retain each ordinary, finite-group and cusp period
discrepancy. These discrepancies are integral and continuous.
The explicit root maps, line-unit conjugations and toric unit
maps in RCZ.1–2 identify the local models in every such chart.
The zero difference at u* consequently stays zero under their
actual parameter continuation around the connected annulus.
In particular the doubled period is carried as an integral
one-cochain on changing parameter charts, not discarded as an
extending Lie logarithm.

This establishes the base-direction discrete equality required
by RCZ.3 for the newly completed marking. The relative coherent
solution in that section therefore gives actual local family
isomorphisms on each simply connected parameter chart, with all
root/cusp and annular maps retained.

## RCZ.7. The actual global family arrow

The ratio of two such local comparisons is a global extending
translation of the same marked compactified family. RCZ.4
identifies it with a holomorphic physical scalar, including
every finite-kernel endpoint. Apply its explicit two-angular-chart
factorization on a smaller u-annulus carrying the chosen loop.
The corrected local maps glue to a literal holomorphic
delta-equivariant family isomorphism from the old u-family to
the pullback under v=u^3 of the constructed v-family, with F0
marked as in RCZ.5. For the rescaled scalar the quadratic
cochain of RCZ.4 is included in its forward endpoint square;
its one-step ratio is u^{12kn}, the exact compensating ratio.

Every map used here is the actual source/Cartier coordinate
arrow, an extending translation on its stated root or toric
chart, or physical scalar multiplication. Their inverses have
the same extensions. Thus the map carries the normal circle
and the prescribed fan as well as the complex fibres. It is a
family morphism over the annulus. This argument assigns no
numerical return or extension of the old coordinates across
u=0; those remain the separate collision/fixed-stratum tasks.

The construction deliberately fixes the previously unselected
F0 by the full old reference map. It makes no assertion that an
independently chosen different integral annular marking would
be equal to that one.

## RCZ.8. The oriented mapping-torus consequence

Use the actual rescaled new family
\(\lambda=v^N\lambda_0\), with \(N=km\), and its pullback
\(\lambda=u^{3N}\lambda_0\). The isomorphism just constructed
is a map of these actual families, including their closing
arrows. A positive u-circle maps to three positive v-circles.
Pull back a connection from the v-family and transport it by
the isomorphism. The resulting actual parallel transport around
u is the third iterate of that around v, conjugated by the
reference-fibre map. Consequently their oriented mapping tori
satisfy
\[
 M_{\Phi_{\rm old,u}}\cong M_{\Phi_{\rm new,v}^{\,3}},
 \qquad
 [\Phi_{\rm old,u}]=3[\Phi_{\rm new,v}]\quad\text{in }\Theta_7.
\]
Equivalently the left mapping torus is the degree-three
parameter pullback of the actual new mapping torus. The
physical return uses the inverse closing arrow on both sides;
the family isomorphism intertwines those arrows, so this
argument introduces no inverse-loop sign. It retains the
specified scalar rescaling and assigns no value to either
unknown class. No numerical class division is used.

## Audit record

Checks independently passed RCZ.3–4 in their earlier,
remaining-F0 scope, including the relative Lie splitting,
groupoid exponentiation with component removal, scalar valuation
equation and both signs in the Cauchy–Green factorization.
Fourfold independently passed the literal central Cartier and
commutator calculation of RCZ.2. Root's full independent read
passed RCZ.1–7 for the punctured family with F0 newly specified
by the complete old reference overlap. The collision ordinary-
origin deck just recorded is not promoted as an already attached
central-fan map. The precise scope is also saved in
`records/source_zero_relative_comparison_scope.json`.

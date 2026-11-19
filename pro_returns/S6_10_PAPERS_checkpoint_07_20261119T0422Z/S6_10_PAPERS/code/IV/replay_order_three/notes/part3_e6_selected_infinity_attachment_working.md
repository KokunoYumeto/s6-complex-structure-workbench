# E6 selected infinity: the compact-period attachment calculation

Working continuation of EI.6--12 and EIR.7--11. The local source,
point-line, finite-deck and six/nine factor arrows have independent
peer audits. This file records the compactness argument and the exact
remaining global cover data. No characteristic pair or return is assigned.

## IA.1. The selected local period quotient

Use the actual EI.65 periods on the selected bidisc:

\[
h:(Z,V)\mapsto(qZ,P^aV),\qquad
B:(Z,V)\mapsto(P^{-b}Z,\sigma^4q C V),
\quad C=\lambda\beta/\kappa.
\]

The entire functions P, beta and kappa are those of EI.65--66.
Shrink the closed bidisc, and choose the original nonzero lambda
small enough that \(|C|<1\) there. P and C are units; P has
central value minus one. Their logarithms of absolute value are
bounded, with no choice or deletion of their angular arguments.

On \(q\sigma\ne0\), put \(L_q=\log|q|\),
\(L_\sigma=\log|\sigma|\), \(L_P=\log|P|\),
\(L_C=\log|C|\). The real period matrix is exactly

\[
\begin{pmatrix}
L_q&-bL_P\\aL_P&4L_\sigma+L_q+L_C
\end{pmatrix}.
\tag{IA.1}
\]

Its determinant is
\(L_q(4L_\sigma+L_q+L_C)+abL_P^2>0\), with \(ab=6\).
Thus the two actual logarithmic translations form a discrete full
lattice. The remaining two phase circles are compact. An actual
integer period word puts every point into the real parallelogram
whose coefficients in IA.1 lie in \([0,1]^2\). For a uniform
constant K this gives

\[
e^{-K}|q|\le |Z|\le e^K,\qquad
e^{-2K}|\sigma^4q|\le |V|\le e^{2K}.
\tag{IA.2}
\]

These bounds retain the full unit constants. They put the source
coordinates \((x_0,y_0)=(Z,q/Z)\) and the line coordinates
\((U_0,V_0)=(V,\sigma^4q/V)\) in a fixed bounded affine box.

The six-chart morphism EI.69 is proper over that box. Explicitly,
for valuation variables \(s=\operatorname{ord}\sigma\),
\(x=\operatorname{ord}x_0\), \(y=\operatorname{ord}y_0\)
and \(u=\operatorname{ord}U_0\), its six cones are the intervals

\[
(0,s,2s,3s,4s,4s+y,4s+y+x),
\]

where each consecutive pair specifies the corresponding permitted
interval for u. More precisely their endpoints are
\(0,s,2s,3s,4s,4s+y,4s+y+x\); their union is the full interval
\([0,4s+x+y]\). The chart inequalities are exactly
\(\operatorname{ord}U\ge0\), \(\operatorname{ord}V\ge0\),
\(u+\operatorname{ord}V=4s+x+y\). Common endpoints give their
common faces. The explicit primitive cones of EI.70 therefore
subdivide the entire original affine cone, without changing its
support. Equivalently the morphism is the closure of the full
projective graph of the ratios
\([U:\prod_{r\le k}f_r]\), \(1\le k\le5\), with the chart
maps EI.69. These projective factors prove properness directly.

At the two base divisors the same compactification retains the
source and line chain indices. h shifts \((i,j)\) by \((1,0)\)
and B by \((0,1)\), with the complete unit maps EI.71. The
adjacent source and line chart maps are those written in EI.67--72.
Every central chart is a translate of one of the six displayed
charts, including its projective exceptional fibre. Bounded
neighbourhoods in those charts meet only finitely many adjacent
index cells: on the nonzero locus this follows from IA.1--2, and
on the base divisors from the explicit consecutive source/line
chain maps. Thus the period action remains proper through the
boundary strata. A finite number of the bounded chart regions,
with their projective exceptional fibres, gives a compact local
fundamental region. This proves local properness of this selected
period quotient; it does not discard its full unit actions.

## IA.2. The source section graphs and finite actions

The two source graph centres on sigma zero are the actual smooth
source sections O and T. Under the full source translation their
union is preserved, and all their period translates are retained.
Blowing up that union is a proper equivariant morphism. EI.57--64
gives its actual original-source and point-line maps. Its corner
equations pull back the line chain to the written associated
nodes. The nine-factor resolution of EI.71--73 is proper by the
same projective-ratio construction as in IA.1. Its unit overlaps
with the six-chart atlas and its source-reset units are explicit.
These are relative modifications supported at sigma zero and
preserve the whole punctured boundary family.

On the selected H collars the fourth-root graph action permutes
the four branches freely. On the ordinary O/T corners it has the
actual finite normal types recorded in SIT.5; in particular the
second chart at j zero has type \(1/4(1,3,1,3)\). The cover
charts and their period quotient have the displayed smooth
atlases. Their subsequent finite quotient is retained with all
stabilizers. No smooth coarse quotient or determinant-line
extension is inferred from the cover alone.

## IA.3. The global cover and what remains to be joined

The actual source-base graph is the proper closure of
\(t_o q_{\infty,\epsilon}=\epsilon^4d_0^{-3}\) in the product
of the two source-base projective lines and the epsilon disc.
Its fourth-root chart is \(t_o=\sigma^4d_0^{-3}\),
\(q_{\infty,\epsilon}=\Xi^4\), \(\epsilon=\Xi\sigma\),
with the literal finite quotient EI.52. This retains the base
graph multiplicities; it makes no unrecorded base change.

The native finite chart contains the actual I2 resolution EI.15--17.
Its overlap with the complementary chart is exactly EI.74--79,
including the point/tensor coefficients and every integer chain
power. The original finite cap lies on the original domain
\(|q_{\infty,o}|<\delta\), hence on the large-sigma side in
the fourth-root chart. Its actual ordinary-to-cap map transports
the graph quarter turn to \(A B^{j_\gamma}\); all its norm,
scalar, source, character and reference factors are those of
EIR.28 and EI.80. The unmodified original source charts away
from the colliding III fibre form the remaining compact exterior.

The local maps identify the boundary charts in this cover. The
next global step is a single finite chart ledger for the union:
the native I2 patch, the four selected collars, the ordinary
O/T graph corners, their finite quotient strata, the original
exterior, and the original finite cap. That ledger must retain
each finite face once and the full original physical line.
The remaining finite quotient resolution maps and their
determinant characters must be recorded before extracting
characteristic data. No oriented global boundary equation or
numerical return is entered here.

## IA.4. The complete native I2 source graph and its ordinary overlap

This supplies the source graph at the finite native I2 fibre,
including the point where the native affine coordinates x and y
vanish. Keep \(A_0=3\epsilon^2-2\), \(d=1-3\epsilon^2\)
and the entire native coordinate \(t\). In EI.15 put
\(a=x/t\), \(b_0=y/t\). The smooth resolution equation is
\[
 b_0^2=t a^3+A_0a^2+da+\epsilon^2,
 \qquad a(d+A_0a+t a^2)=b_0^2-\epsilon^2.
\tag{IA.3}
\]
The displayed denominator is a unit near the full central T
section, including t zero. The original source morphism has
\(x_o=\epsilon^2d^{-2}ta\),
\(y_o=\epsilon^3d^{-3}tb_0\),
\(t_o=\epsilon^4d^{-3}t\). After the common factor, the
pullback of its resolved-source ideal is
\[
 (a,\epsilon b_0,\epsilon^2)=(b_0,\epsilon)^2.
\tag{IA.4}
\]
Indeed IA.3 expresses a through \(b_0^2-\epsilon^2\)
with its nonzero denominator, and conversely expresses
\(b_0^2\) through a and \(\epsilon^2\). The Rees graph is
therefore the quadratic Veronese of the blowup
\(\operatorname{Bl}_{(b_0,\epsilon)}\), with both charts
retained.

In the first chart write \(b_0=\epsilon z\),
\(a=\epsilon^2 C\). Its equation and its actual original
resolved coordinates are
\[
 z^2=t\epsilon^4C^3+A_0\epsilon^2C^2+dC+1,
 \qquad (x_o/t_o,y_o/t_o)=(dC,z).
\tag{IA.5}
\]
In the second chart \(\epsilon=b_0v\), \(a=b_0^2C\),
\[
 1=t b_0^4C^3+A_0b_0^2C^2+dC+v^2,
 \qquad(t_o/x_o,y_o/x_o)
       =(v^2/(dC),v/(dC)).
\tag{IA.6}
\]
The second formula is used where C is nonzero; the first
chart supplies its projective complement. These maps preserve
the full original equation and all parameters, and agree on
the displayed blowup overlap. They extend through t zero.

At O use \(\eta=-x/y\), \(U=\eta^2x\). The full equation is
\[
 1=U+A_0\eta^2+dt\eta^4/U
                    +\epsilon^2t^2\eta^6/U^2.
\tag{IA.7}
\]
The graph is \(\operatorname{Bl}_{(\eta,\epsilon)}\).
On its corner \(\epsilon=\eta v\), the actual original
coordinates are
\[
 x_o=v^2U/d^2,\quad y_o=-v^3U/d^3,\quad
 t_o=\eta^4v^4t/d^3,
 \quad (t_o/x_o,y_o/x_o)
       =(\eta^4v^2t/(dU),-v/d).
\tag{IA.8}
\]
On the other chart \(\eta=\epsilon p\), the original
O parameter is \(\tau_o=dp\). This includes the full
projective exceptional curve and the actual marked even
multiple \(aG\); no point is supplied by deleting that chart.

The complete source-period arrow also crosses these graphs.
For the actual \(-G\) chord on IA.7 set
\[
 \begin{split}
 k&=-\eta^{-1}+\eta^3vt/U,\\
 C_1&=(d-2v)/U+2\eta^4v^2t/U^2,\\
 c_1&=v+C_1-\eta^4vtC_1/U.
 \end{split}
\tag{IA.9}
\]
The target I2 coordinates are
\(a'=\eta^2C_1\), \(b_0'=\eta c_1\), hence its graph
map is \((\eta,v)\mapsto(\eta c_1,v/c_1)\).
On the central corner \(c_1=1-v\). In the other graph chart
this is the literal additive arrow \(z=p-1\).
The inverse-form chart through the complete T graph is equally
explicit. Put
\[
 D=d+A_0a+t a^2,\quad
 k^{-1}=\kappa=(b_0-\epsilon)/D,\quad
 W=1-\kappa^2(A_0+ta).
\]
Then the target O parameter is
\[
 \eta'=\frac{\kappa W}{W-\epsilon t\kappa^3}.
\tag{IA.10}
\]
On IA.5, \(\eta'/\epsilon\) extends and has central
value \(z-1\). The displayed denominators are units on
the stated coordinate neighbourhoods. Three chronological
copies give the full \(-3G\) arrow; their complete units
are composed in order. Thus both admitted odd b have
central p to p minus b and z to z minus b, with their
entire source maps retained.

The overlap with the complementary graph is especially
simple and fixes its chart labels. On \(\chi\ne0\),
\[
 x_e=\chi^{-2}\bar X,\quad y_e=\chi^{-3}\bar Y,
 \quad t_e=\chi^{-4},\quad\epsilon=\chi\sigma.
\]
Consequently
\[
 \eta_e=\chi\bar\eta,\qquad
 (b_0)_e=y_e/t_e=\chi\bar Y.
\tag{IA.11}
\]
Both native blowup ideals are the corresponding
complementary ideal multiplied by the same nonzero unit
\(\chi\). Their projective ratios, the two complete
source graph charts, and the original resolution maps
therefore agree literally. This reaches the whole native
I2 patch, not just its punctured source torus.

The canonical point section is carried by the same map.
The actual O Cartier ratio satisfies
\[
 \frac{\tau_e-\tau_e(aG)}{\tau_e}
  =\frac{\bar\tau-\bar\tau(aG)}{\bar\tau}.
\tag{IA.12}
\]
Away from its two point divisors the canonical section
is the shared frame. The full normalized point Hom
coefficient is
\(\epsilon^{-6}(q_e/t^3)B_{a,b,e}\), together with
the target/source ratio of these actual point frames.
For \(\epsilon\ne0\) it is the original ordinary
invertible Hom map off the selected fibre. Its only
possible new divisor is \(\epsilon=0\), where the full
Miller computation EI.18 gives \(64q_e\). Thus it has
zero divisor on the smooth native resolved source over
the H-unit domain. The meromorphic coefficient and its
reciprocal extend in each nonzero line frame, including
the I2 fibre; this follows by the local divisor criterion
in those smooth charts. Pullback carries the same unit
through the two source blowups. This argument retains
the complete Miller function and actual source/target
line maps, and does not replace them by their limits.

Finally the native chain \(A_kB_k=\epsilon\),
\(V=\epsilon^kA_k\) has the exact overlap
\[
 X_k=\chi^kA_k,\qquad
 Y_k=\chi^{-k-1}B_k,
 \qquad X_kY_k=\sigma,\quad V=\sigma^kX_k.
\tag{IA.13}
\]
On either graph its factorization pulls back the same
two divisors under IA.11. Every integer power and the
finite fourth-root phases are retained. The ordered
factor interface at the full corner is handled by the
common refinement described next, rather than by
identifying the two factor orders.

The independent symbolic record for IA.3--13 is
`code/part3_fourfold/e6_selected_infinity_native_graph.py`
and its JSON/stdout. It checks the complete source
identities and coordinate directions; the compact
global assembly is still recorded separately below.

## IA.5. The full factor-order interface and finite normal charts

On the q-unit overlap the selected nine-factor atlas
retains the grouped order \((\eta^4,v^4)\), whereas the
four successive ordinary chain nodes retain the
alternating order \((\eta,v)^4\). Their agreement when
one factor is a unit follows from the explicit unit
deletions above. At the full corner use the actual
common fan constructed in
`notes/part3_e6_selected_infinity_toric_audit.md` and
`code/part3/e6_selected_infinity_factor_overlay.json`.
Its 38 smooth three-cones subdivide both factor orders;
the invariant quotient lattice extension has 238 smooth
four-cones. Both parent invariant-monomial maps are
saved for every cone. This gives the actual two
modification arrows, retaining the source and point-line
functions on the whole overlap.

For selected period j the dense coefficient comparison
is \(U_{\rm selected}=q^{-j}\psi(\eta v)^{-4j}V_{\rm phys}\).
The inverse carries the entire \(q^j\psi^{-1}\).
The common refinement lifts precisely these unit powers,
and the full source reset
\((\eta,v)\mapsto(\eta c_b,v/c_b)\) together with
\(V_{\rm phys}\mapsto\mathcal C(\eta v)^4V_{\rm phys}\),
\(\mathcal C=\lambda H\mathcal B\). Thus it retains
the previously specified cap/reference data as well
as the line-chain index.

For the O/T finite quotient the inherited original
marked-family form is, in the specified cover order,
\[
 8\eta^4v^3d^{-2}u_{O/T}\,
 d\chi\wedge d\eta\wedge dv\wedge d\log V_{\rm phys}.
\tag{IA.14}
\]
In quotient characters \((\chi^4,\chi\eta,v,V_{\rm phys})\)
its character is \((-1,5,4,0)\). The full derivative
unit is preserved by
\(u_{\rm source}=u_{\rm target}c_bJ_b\),
\(J_b=1+\eta\partial_\eta\log c_b-v\partial_v\log c_b\).
All orders in the common refinement use this original
form. The separate local volume has character
\((0,1,1,0)\); IA.14 is the exact morphism between the
two frames.

The remaining ordinary finite stabilizers occur in
the pair of non-O/T two-torsion source sections. Their
actual source ideal and quotient blowups are those of
`code/part3_root/e6_selected_infinity_mu2_pair.json`.
Their full source-mixing coefficients and point-line
normal maps remain in that construction. The finite
normal chart list can now be used to extract the
minimal physical fixed faces. Their source/cap boundary
identifications and the doubled fixed-surface classes
are the next entries in the global ledger; no numerical
return is assigned here.

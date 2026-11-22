# 02WM / night:P4.15: exact preproof scope counterexample

The target proof remains closed. This record derives the scope witness from
the completed Paper I construction inputs, before any target release. It does
not replace the original universal final sentence by a silently restricted
one. The exact original sentence is:

> The reduced conductor and singular locus are disjoint unions of smooth
> elliptic curves, and their normalization maps are finite and unramified.

The preceding target sentence says that e(S)=0 in the last two alternatives;
the displayed final sentence does not contain that qualifier. The following
actual member of the standing family satisfies the target rank hypothesis
and belongs to its rational alternative, while its reduced conductor has
the explicitly different Euler number computed below.

## Source and ambient morphism

The sole new construction input is
`S6_SERIES_PUBLISH_II_02WM_construction_scope_inputs.json`, SHA256
`3ce326b9666d3e88a88aeb18f1e9186ad16aa940cb70482075b9a26607aae0d1`.
Its six exact fragments are bound to completed Paper I source SHA256
`179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74`
and its completion gate. I have read all six fragments, including their
complete declared marking, multiplicities and local-chart data. Two local
construction fragments originate inside a cited Paper I proof; they give
only the displayed construction definitions and named strata. They contain
no 02WM proof, and I assign no new independent credit to those Paper I owners.

Take the standard untwisted (3,4) sphere member, with the precisely specified
period matrix and translation vectors in that input, and its proper map
f:X_c→P1_t. Its underlying smooth manifold is S6, so b1(X_c)=b2(X_c)=0.
The general fibre is the constructed complex two-torus. At infinity the full
fibre is the reduced one-component cusp W, hence m=1 and S=W. The local
filling has smooth total space and the displayed proper flat Cartier map.
Thus this is the standing global fibration, not merely an unrelated local
plane-curve model.

## Normalization, conductor maps and differential

Use exactly the declared normalization ν:P→W, where P=dP6, and set
C=Sing(W)_red. The inverse image R=ν^(-1)(C)_red is the hexagonal toric
boundary of P. For e=h,v,d the input gives C_e=P1 and two boundary maps
ρ_e^0,ρ_e^1:C_e→P with

j_e=ν∘ρ_e^0=ν∘ρ_e^1:C_e→W.

The normalization of R is the map

η_R: ⨿_(e∈{h,v,d}, ε∈{0,1}) C_e → R,

whose six restrictions are exactly ρ_e^ε with image restricted to R. Its
images are the six boundary curves, meeting in the six cyclic boundary
nodes. This is the precise map used for the conductor topology; no choice
of which toric exceptional curve is called ρ_h^0 is needed or invented.

At a triple point the family chart is q=z0 z1 z2 in smooth coordinates on
the total threefold. A branch of the normalization of q=0 is the coordinate
plane z_i=0, embedded by the inclusion of the other two coordinates. Its
Jacobian has the two corresponding standard basis columns, and its
corresponding two-by-two maximal minor is 1. The two-factor chart has the
same description with a free third coordinate; the smooth chart is a
smooth embedded surface. Therefore dν has rank two at every point of P,
its maximal-minor ideal is the unit ideal in every normalization chart,
and the finite maximal-minor scheme has length ℓ=0.

The surface P is the blowup of P2 at three noncollinear points. For the
blowdown π:P→P2 and exceptional curves E1,E2,E3, write L=π*O_P2(1).
The actual intersection basis satisfies L²=1, E_i²=−1 and every mixed
pairing zero; K_P=−3L+E1+E2+E3. Hence K_P²=9−3=6. Each point blowup
replaces a point by P1, increasing Euler number by one, so e(P)=3+3=6.
This satisfies the target numerical rational alternative e(P)=6−ℓ/2.

## Exact obstruction to the universal final sentence

Euler additivity for η_R gives

e(R)=Σ_(e,ε)e(C_e)−6=6·2−6=6.

Every disjoint union of smooth elliptic curves has Euler number zero.
An isomorphism of compact analytic curves would induce a homeomorphism of
their underlying topological spaces and an isomorphism on the finite
singular-homology groups, preserving their alternating rank sum. The
computed Euler numbers therefore exclude such an isomorphism for this
specific conductor R. The obstruction uses the actual normalization map
η_R and its six double identifications.

Each j_e is finite and nonconstant onto its conductor-image component;
its normalization is C_e=P1. A nonconstant map from C_e to a smooth elliptic
curve would have degree d≥1 and Riemann–Hurwitz would read
−2=d·0+deg(Ram), with deg(Ram)≥0, which is impossible. These exact j_e maps
therefore also exclude the asserted elliptic normalization of every image
component. The ordinary triple-point charts additionally display the two
image triple points P_+,P_− supplied by the construction input.

Thus the universal conductor sentence fails for an actual member of the
stated rational alternative. The independent argument for the other two
alternatives proves the same sentence there, with ν and its conductor
restrictions unchanged. The proposed source repair must explicitly retain
the qualifier “In either of the last two alternatives” for both e(S)=0
and the conductor conclusion. This is recorded as D25, with the original
sentence and this refutation preserved. The receiving-use audit must
identify which alternative and which morphism each application actually
uses; it may not mark the original statement unchanged.

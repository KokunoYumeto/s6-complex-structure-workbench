# Fresh prereading derivation of VI cdp:st:C.2.VII.1

19 November 2026. Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation.

This derivation uses only the target statement in VI's 018_statement_packet.json and the cited primary-source inputs. I have not opened VI's target proof or 019 review. I have read Dloussky's author v3, arXiv math/0406387, especially Definition2.16 and Definition2.20, Lemma2.22 and its following paragraph, Corollary2.25, Proposition2.27, Proposition2.29 and Theorem2.38; DOT2003's actual primary text pp283–285 and296. I also opened Inoue's original 1974 paper for the no-curves property. The current argument treats every Hopf surface and does not need the narrower general-fibre exclusion C.3.8.

## 1. Reduction to the minimal surface with the exact divisor formula

Write the given torsion line bundle K_Z+D as tau. Its torsion implies its intersection with every curve is zero. Contract one exceptional curve E with E^2=-1, by pi:Z->Z0, and set D0=pi_*D. Let m be the multiplicity of D0 at the contracted point. Write D as its strict transform plus kE. The canonical formula is K_Z=pi^*K_Z0+E. The strict transform of D0 meets E with total multiplicity m, while adjunction gives K_Z.E=-1. Consequently

    0=(K_Z+D).E=-1+m-k,  so  k=m-1,
    D=pi^*D0-E,  and K_Z+D=pi^*(K_Z0+D0).

These are actual divisor and line-bundle equalities. Pullback on Picard groups for a point blow-up is injective: a trivial pullback descends to a trivial line bundle by pi_*O_Z=O_Z0 and projection formula. Thus K_Z0+D0 is torsion. Because D is effective, k>=0 implies m>=1. In particular D0 is nonzero. The same argument works after every contraction, so on the minimal model S there is a nonzero effective D_S with K_S+D_S torsion; every inverse blow-up is centred on the then-current support.

For completeness, this hypothesis forces Kodaira dimension -infinity even under the older b1=1 terminology: after killing the torsion, a nonzero pluricanonical section would give a nonzero section of O(-nD_S). Multiplication by the canonical section of O(nD_S) would be a holomorphic function on the compact connected surface vanishing along D_S. Such a function is zero, a contradiction.

## 2. Minimal supports and the cited known configurations

Suppose first b2(S)>0. A torsion line bundle is flat with finite monodromy, so the equation is the m=1 instance of Dloussky's Definition2.20. The cited NAC/GSS theorem applies. The cited configuration results give the following components of the maximal reduced curve divisor: a rational cycle with rational trees attached in the intermediate case; the rational cycles in the Inoue–Hirzebruch cases; and the disjoint elliptic curve and rational cycle in the parabolic Inoue case. Their singularities are ordinary nodes, including a self-node for a one-component rational cycle. Here the precise convention of Definition2.16 matters: an elliptic curve is a zero-cycle. The trees in DOT pp284–285 are attached to that cycle and introduce no additional circuit. These configurations are supplied known inputs, not newly asserted classification theorems.

The support R_S of D_S is a union of entire connected components of this maximal divisor. Indeed, if an irreducible curve C outside R_S met it, then D_S.C>0 by positivity of local intersection. But D_S.C=-K_S.C<=0 on a minimal class VII surface. This is exactly the morphism used in Lemma2.22: it compares intersection with the actual effective D_S to the canonical intersection. Hence no such C exists. The source's Corollary2.25/Proposition2.27 ensure a cycle in each selected component, and the displayed known maximal configurations give precisely the same conclusion. No assertion that every component of the maximal divisor is selected is needed.

For b2(S)=0, the standard completed minimal classification recalled at DOT pp283–284 gives Hopf or Inoue surfaces. The latter have no curves (Inoue1974, Proposition2(i), Proposition3(i), and the unramified double-cover construction in Section4), so the existing nonzero D_S rules them out. On a Hopf surface every reduced curve component is a smooth elliptic curve and distinct components are disjoint. Here is a direct description of the maps behind that assertion. Pass to a finite unramified primary Hopf cover with universal covering C^2 minus0 and contracting deck generator F. The inverse image of a compact curve is a closed analytic curve there; its closure at0 is analytic by the extension theorem for a curve across a lower-dimensional analytic subset. Near0 it has finitely many analytic branches. A power of F preserves each branch and lifts to an invertible contracting germ of its normalization. In a normalized disk its quotient away from0 is an annulus with its two boundary circles glued by that contraction, hence a smooth genus-one curve. The branches have no mutual intersections or singularities away from0 after shrinking; contraction then proves the same throughout the covering curve. The finite primary-to-secondary map is unramified and locally biholomorphic, so it preserves smoothness and cannot create a transverse intersection of disjoint branches. Its restriction on each curve is finite unramified; Riemann–Hurwitz gives genus one downstairs as well. This treats also Hopf surfaces of algebraic dimension one.

The bound r(S)<=b2(S) is the cited general rational-curve bound in DOT's Introduction p283; for the Hopf case the preceding curve description gives r(S)=0 directly. In the positive-b2 NAC case the known GSS count even gives equality, but only the stated bound is used below.

## 3. Arithmetic genus and Euler number from the normalization maps

For a connected nodal reduced curve C with smooth normalization components C_i of genera g_i, let v be their number and e the number of nodes, counting a self-node as one edge. The normalization sequence is

    0 -> O_C -> direct_sum O_Ci -> direct_sum_nodes C ->0.

At a node its last map is the difference of the values on the two branches. Taking Euler characteristics gives

    p_a(C)=sum(g_i)+e-v+1.

Topologically the normalization identifies two distinct preimages at each node. Every such identification reduces the Euler characteristic by one, including a self-node, so

    e_top(C)=sum_i(2-2g_i)-e.

For a rational cycle with trees, every g_i=0 and the connected dual graph has one circuit, hence e=v. Thus p_a=1 and e_top=v=r(C). For an elliptic component with rational trees, sum(g_i)=1 and the graph is a tree, hence e=v-1. There are r(C)=v-1 rational components; again p_a=1 and e_top=v-1=r(C). A lone elliptic curve is the case v=1,e=0. The minimal supports from Section2 therefore satisfy both formulas componentwise. This computation includes the one-nodal-rational-curve cycle using v=e=1.

## 4. Every allowed blow-up preserves the component description

Now rebuild Z from S along the actual given blow-up sequence. A centre is on the current support by Section1. The support is nodal by Section2 and the induction below, so only these local situations occur.

* At a smooth point of a support component of multiplicity a, the total multiplicity is m=a. If a=1, k=0: the exceptional curve is absent from the new support and the strict-transform support maps isomorphically to the previous support. If a>=2, k=a-1>0: the exceptional P1 is present and meets the strict transform at exactly one point transversely. The dual graph gains one rational leaf and one edge.
* At a node whose two branch multiplicities are a and b, including two branches of the same irreducible component, m=a+b>=2. The exceptional curve appears with coefficient a+b-1. The two strict-transform branches meet it transversely at distinct points. The old dual-graph edge is replaced by a path of two edges with the new rational vertex in between. For a self-node this changes a loop into a two-edge cycle, with the same first graph Betti number.

All displayed local maps are the standard two point-blow-up charts: x=u,y=uv and x=uv,y=v. Substitution into a local defining monomial x^a or x^a y^b gives the multiplicities just used. No exceptional component occurs at a centre away from the support, since that would have k=-1 and violate effectiveness.

A leaf attachment or edge subdivision increases both v and e by one and adds a genus-zero normalization component. The formulas in Section3 therefore preserve p_a=1 and increase both e_top and r by one. In the a=1 smooth-point case the support, e_top and r are unchanged. Connected components are neither merged nor split. Consequently every connected component of R=D_red still has p_a=1 and e_top=r componentwise; summing proves e(R)=r(R).

For all rational curves on the surface, each point blow-up introduces exactly its exceptional P1. Every other irreducible curve is the strict transform of its image; normalization genus is birationally unchanged. Thus after n blow-ups r(Z)=r(S)+n. The blow-up adds one generator of H2 with square-1, so b2(Z)=b2(S)+n. The minimal bound gives r(Z)<=b2(Z).

Finally, in any connected component containing an elliptic curve, the normalization genus sum is at least one. The exact genus formula says that sum plus the first Betti number of the connected dual graph equals one. Thus the genus sum is exactly one and the graph has no circuit. There is exactly one elliptic component; every other component is rational and all remaining edges form trees attached to it. A second elliptic curve would raise the genus sum to at least two. A path joining two distinct points of the first elliptic curve would create a graph circuit. Both contradict the proved genus formula.

This completes all assertions of the target statement before its proof has been opened. A fresh graph/blow-up certificate and comparison will follow; neither will be backdated into this derivation.

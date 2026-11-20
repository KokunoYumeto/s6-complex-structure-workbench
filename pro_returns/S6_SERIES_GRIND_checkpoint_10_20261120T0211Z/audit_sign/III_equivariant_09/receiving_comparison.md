# OS45: complete new collar and framing receiving comparison

## Verdict and exact reading order

**PASS for the new weighted-OS45 collar, Hopf sphere, relative Borel transport, and refined-characteristic decision. The resulting refined class is zero for the fixed D2.53 example.** This review does not assert the general open D2.4 classification.

Both independent documents were frozen before exchange. My isolated Borel/framing derivation was frozen at 00:49:06 UTC with SHA `b8ebe13a13fd8caea0fc942167a7c277becf7eb4486ddfa2b966bd1217b69724`. Corrections' complete derivation was frozen at 00:53:29 UTC with SHA `2f0e2955c56447e6e5f9d81184ab0ce02bae85cc75be00c50d32776154faf47c`. I then read the complete corrections document, including all seven sections. The geometric collar was not among my isolated prereading inputs; its comparison below is explicitly after reading. My independent earlier route proves the Borel class and framing parity from the supplied action/homology/Hopf-sphere data. It does not receive retroactive credit for deriving the actual collar before seeing it.

For source receiving I opened the actual current III passages: complete local Tate calculation D.FI2; triangular-fan statement D47.1 and its ray characters; D.GC1–4 and the angular-area/normal-meridian proof D.GC14 and its continuation; actual tuple D.VC9; D2.53 statement, D.PC3–8 and D.OS5–8; D.OL fixed-locus paragraph; D44.5–8 reference/Bott/Thom calculation; and D.WI9–13 reference-parity and relative-link mechanism. I also read corrections' complete earlier `III_OS45_local_geometry_receiving_08.md`, whose former middle-collar and specialization gates are resolved by the new construction rather than erased. This is not a fresh whole-prereading review of all the already printed D2.53 invariant computation.

Reviewer: GPT-6 Astra, OpenAI, ChatGPT Pro mode; inherited effort not separately exposed. Both reviewers are in the same model family. A new independently authored, after-reading certificate performs 34 exact algebraic checks, with no producing-code import.

## 1. Actual line, units and deck maps

The two actual elliptic monodromies in D.VC9 are T^8 and T; their G cocycles are (3,0) and (0,0). Consequently the same based vanishing cycle e1 is fixed around both ends, and the exponential period and section coordinates q_E,P,Q are single valued on the chosen two-punctured narrow neighborhood. Their logarithms need not be single valued. The section O remains the origin. The actual canonical meromorphic section s of M=O(P-O), together with the displayed theta quotient sigma, defines the exact flat frame e_flat=s/sigma. The original D.FI2 identity sigma(q_E Z)=P sigma(Z) then gives the physical first period multiplier P.

For the actual forward point/line map F(s(Z))=c_F(Z)s(QZ), linearity gives

    F(e_flat(Z)) = [c_F(Z) sigma(QZ)/sigma(Z)] e_flat(QZ).

Thus kappa is the displayed expression, with all scalar factors retained. On a regular elliptic fibre the ratio has zero divisor and trivial automorphy, so it is a nonzero constant on that compact fibre. This proves its independence of Z. It is the coefficient of the existing F, rather than a newly chosen lift. The section's whole-fibre divisor permits the stated limiting valuation. In the backward-linearization convention of D.FI2, 8w-(-6)(24)=16 gives w=-16; the actual forward inverse lift therefore has physical valuation +16. This matches the original gamma column.

Literal tautological duality sends a nonzero physical line vector to the unique dual vector evaluating as one on it. Its coefficient is V=W_flat^{-1}, so both period multipliers are inverted. The actual deck maps are therefore exactly

    (Z,V)->(q_E Z,P^{-1}V),
    (Z,V)->(QZ,kappa^{-1}V).

The nonzero holomorphic units stay in those four functions. The local quotient map Phi uses them through these actual brackets, with no independent endpoint origin or scalar frame. The unshifted graph edge is retained. In particular the lattice identity (0,-6)=9l1-3l2 is checked but is not applied to translate the edge: the accompanying source unit q_E^9 Q^{-3} is never set to one.

## 2. Original graph cone and exact endpoint maps

D.FI2 gives F_i=max(6-i,0), with quasi-period increment -6. The consecutive source-line graph vertices (0,6),(1,5) lie in the D47.1 triangular fan. An adjacent ordered cone has columns (1,0,5),(1,1,5),(1,0,6), determinant one. Its exact character maps are

    q=xyz, Z=y, V=x^5 y^5 z^6.

The extending physical coordinate is q^6/(ZV)=x. Its source-node map is (X,Y,W_ext)=(xz,y,x), with inverse (x,y,z)=(W_ext,Y,X/W_ext) and Jacobian -x. This is used on x nonzero, precisely the selected open double-curve orbit. It retains the nonconstant Jacobian, rather than dropping a winding. The line frame (Z/q^6)e_flat has zero valuation on both adjacent branches. Since neither section P nor O meets this node, the frame and its inverse extend there. For example the theta leading unit of P is still present in this frame; the statement about zero orders does not replace that unit by one.

The short weights calculated by the inverse cone matrix are

    e1=(-1,1,0), delta=(-1,0,1), e1-delta=(0,1,-1).

Thus e1-delta is the actual source vanishing circle at fixed extending line coordinate; delta is inverse physical line rotation. At the first I1, the zero cocycle gives literal source vanishing vector e1 and zero line degree. Both meridian/delta pairs have oriented area e1 wedge delta.

On Q={ad-bc=1}, f=ad, use Phi=[t(f),Z=ab,V=f^6/a]. At the I8 end retain q0=f c0(f), and at the I1 end retain q1=(1-f)c1(f). The actual endpoint charts are

    (x,y,z)=(c0^6/b,ab,c0^{-5}d),
    (X,Y,W)=(-c1 c/a,ab,a/f^6).

Direct substitution gives xyz=q0, the exact Z, and x^5 y^5 z^6=f^6/a. At the second end XY=c1(1-f)=q1 and W=V^{-1}. Both reciprocal source/line maps are therefore maps of the original marked nonzero line. At the first core a=d=0 the Jacobian in domain coordinates(a,b,d) is c0(0)/b. At the second core b=c=0 the Jacobian in(a,b,c) is c1(1). They are nonzero. The exact symbolic certificate retains the derivatives of arbitrary c0,c1; their higher jets vanish from these core determinants for the actual reasons a=d=0 or b=c=0, rather than by assuming constant units.

D.GC explicitly permits holomorphic unit factors in the long periods. The cone characters above refer to the chosen local base character q. A local Tate equation with a unit factor is related to its node coordinates by multiplying the relevant coordinate by that actual invertible unit; that unit remains in c0 or c1 and the global deck functions. No root-period unit is discarded.

## 3. Based middle collar and tangent-bundle homotopy

Take the specified simple arc in its actual peripheral tree, and a sufficiently thin neighborhood containing only the selected I8/I1 sites. The smooth tubular map t(s+iu)=p(s)+iu p'(s) has positive determinant |p'(s)|^2 along the arc. Compactness and shrinking provide an orientation-preserving map on the strip. Near each endpoint it is chosen holomorphic in the actual local coordinate; the already displayed endpoint units apply there.

At a regular level f, the logarithmic fibre map(a,b)->(Z,V) has character matrix

    [[1,1],[-1,0]],

of determinant one. Its vertical differential is a complex-linear isomorphism. In vertical/horizontal splittings, the full real derivative is block upper triangular: the vertical block is this complex isomorphism and the base block is a+b conjugation, with |a|>|b|. The homotopy a+(1-r)b conjugation has determinant |a|^2-(1-r)^2|b|^2>0. Contracting the off-diagonal block gives the exact oriented-bundle comparison to a complex-linear block map. This homotopy is relative to the holomorphic endpoint neighborhoods. It keeps the vertical kernel and delta fixed. Hence it supplies the required framing transport; it does not assume the middle base map is holomorphic.

## 4. Embedded sphere and exact odd homology class

For g(alpha,beta)=(alpha,beta;-bar beta,bar alpha) in SU2, the generic f level has |alpha|^2=f and |beta|^2=1-f. Its two phase variables(A,B) map to the actual short torus phases by

    (A,B)->(A+B,-A),

again determinant one. For every actual regular compact complex-torus fibre, its marked four periods are a real basis. Thus the real span of e1,delta intersects the full period lattice precisely in Z e1 plus Z delta: any purported additional intersection would give a real dependence involving e2 or gamma. This proves injectivity of each short T2 with its actual period functions. Distinct levels of the compact sphere lie over distinct points of the based arc.

At the cusp core the selected finite edge has no nonzero translation stabilizer in L; a nonzero translation cannot preserve both endpoints of a finite edge. Unit multipliers do not change that stratum translation. The scalar weight on its open orbit is primitive, so the endpoint circle is embedded. At the I1 end the scalar orbit is free and primitive in the actual zero-free cap, exactly as in D.OL's fixed-locus discussion. The nonzero endpoint Jacobians above prove immersion. Compactness gives an embedded SU2 and a neighborhood on which Phi is an embedding.

The small left translation L_epsilon commutes with the scalar right action. Its moved entries are the literal formulas in the frozen receiving document. A common zero a=d would force alpha=0 and then a=-epsilon bar beta nonzero; a common zero b=c would force beta=0 and then b=epsilon bar alpha nonzero. The neighborhood is chosen to avoid every other critical curve and the toric endpoints. Hence the displaced N is embedded, free under the same scalar circle, and disjoint from the complete critical cycle. It is isotopic to the compact model.

The connecting-map calculation can be checked directly without relying only on a Smith total. In the actual bivector order let alpha_0=e1 wedge delta and let R=Lambda^2 A0-I for the printed D.PC5 matrix. Then

    R(e1 wedge e2 + e2 wedge delta)=2 alpha_0.

All entries of R are even, because A0=I modulo2, whereas alpha_0 is primitive modulo2. Therefore alpha_0 has exact order two in coker R. The Wang injection carries it to a class of the same order in the actual cusp boundary H2. D.GC2 kills this angular area in the cusp. In the exterior, the selected first I1 vanishing disc times delta kills the same marked class; the based collar carries the two endpoint areas exactly to alpha_0.

Cutting the compact sphere along a level near the cusp gives that actual short torus, with degree-one phase map above. Thus its Mayer–Vietoris boundary is ±alpha_0, not zero. Since H3(X)=Z/8 and every element of the torsion image in boundary H2 has order at most two, a class mapping to this nonzero order-two element must be odd. The displaced N has the same class. This proves precisely the odd generator needed for the refined decision.

## 5. Independent Borel map and the actual reference frame

My frozen proof gives lambda_{S1}(TX)=u^2 integrally, using the torsion-free degree-four kernel rather than just rational localization. It constructs the literal Hopf disk map

    [n,z]->[n,(z,sqrt(1-|z|^2)v(n))]

into(X_{S1},X), with boundary[n,z]->z^{-1}n and derivative map a->d(z^{-1})(a). The induced W/N->CP2 has the written inverse and degree±1. The torsion difference of relative lambda lifts comes from H3(X;Z)=Z/8 and maps to zero in H4(W,N;Z)=Z. Hence a global stable frame differs from the quotient-descending frame by an odd clutch integer. The quotient-descending Hopf frame is odd relative to the bounding tangent frame; arbitrary rank-three normal-frame changes stabilize by twice an integer. The induced global tangent parity is therefore even.

The actual reference rho in D44.5 is the abstract kernel/target frame, retaining its first vector delta. In the SL2 left Lie frame, after removing the delta coefficient, df has row(ac,bd). Its Bott column is(B,-A), A=ac, B=bd. Under the actual right scalar action, A has weight-2 and B has weight+2, while the Lie off-diagonal frame changes by D2. Thus the completed Bott frame is invariant and descends to the actual quotient over S2. This identifies its parity with the descending frame in my independent argument.

The full receiving local computation additionally gives deg A2=4, deg A1=1 and the exact degree-three gauge C=A2 A1^{-1}. Its equivariance D2 C D1^{-1} agrees with the actual derivative convention, so its even global tangent-parity conclusion agrees with the Hopf disk route. These degrees are not confused with the rank-three normal stabilization factor two.

The chosen global second abstract kernel vector may differ from this local one. Both retain the same nowhere-zero delta; their matrix is in C semidirect C*. The target-line change is in C*, and the horizontal-splitting change is contractible. Restricted to S3, every such change is nullhomotopic. Therefore there is no unrecorded integer degree-three shift between the actual global reference and the displayed local descended frame. The real base-map homotopy of section3 preserves this comparison.

## 6. Actual admissibility and refined class

I freshly read the original Zhubr2013 journal issue pages5,6,8,9, including Theorem1 and the complete section5 proof. Its Lemma1 gives the actual SO3->SO5 index-two map; Lemma4 identifies the tangent-plane and three-frame comparison, and section5 identifies the extendible class as the nontrivial class relative to an embedded sphere's tangent frame.

Here lambda=0 gives a stable real tangent trivialization. Removing a point outside N leaves a six-manifold with a five-dimensional CW model. In that range the inclusion SO6->SO is an isomorphism on the homotopy groups needed to classify the bundle, so the stable trivialization gives an actual full tangent frame on X minus that point. Its restriction to N has the already computed even stable tangent parity. An actual tangent parallelization of S3 has odd stable parity relative to its bounding frame. The projection SO6->V6,3 sends their difference to its nonzero mod-two class, by the explicit rank-three index-two map. The resulting three-frame is therefore nontrivial relative to N in Zhubr's exact definition.

N is an odd generator of the only two-primary torsion summand. Zhubr Theorem1 applies to this actual embedded representative and three-frame. The remaining three vectors of the full frame trivialize the complement, so its obstruction o4 is zero. Hence the receiving refined characteristic P_ref is zero. This applies Theorem1 and its proven geometric mechanism, not the separately stated unproved Conjecture1 about arbitrary changes of frame.

The relative-link route in receiving section7 agrees. The unit Bott residues of D44.6 identify the global/reference comparison class with the Thom-intersection class of the full critical nullchain. Their difference extends to H3(X;Z) and evaluates to zero on the torsion N. Thus the total critical intersection is odd, including the local specialization chains. The reference parity is also odd, and the two halves in D.WI13 cancel. No separate uncomputed individual crossing number is assigned, and the old even core coefficients are not used to discard the specialization chains.

## 7. Evidence, exact limits and publication recommendation

The new `collar_exact_certificate.py` and JSON execute **34 exact assertions**: ordered cone/period adapters, reciprocal source-line maps, both full unit-jet endpoint Jacobians, complete marked Wang order-two identity/parity obstruction, middle character/meridian maps, circle weights, and the real base-homotopy determinant. All pass. These checks supplement the actual compactness, geometric embedding and relative characteristic arguments above.

Precise primary-source openings for the independent Borel/framing proof are in `source_comparison.json`: Atiyah–Bott original Theorem3.5 and its proof context, Bott original TheoremII corollary and full stable O period, and Redden arXiv0912.2086v2 Remark2.17p12 and section6.1pp24–25. The last two exact representation factors agree with the independently frozen quaternionic/adjoint calculation. Zhubr's newly read original pages and the receiving manuscript locators are recorded in the companion JSON.

No remaining mathematical gap was found in this new weighted-OS45 argument at the stated exact source/unit/collar/parity scope. Source integration, honest placement of the former open alternative, and final rebuilt-page review remain root's publication tasks. No shared source, canonical row or inventory is modified here. The prior whole-D2.53 reading-order and imported input records retain their existing scope; this review adds a full independently derived Borel/framing subargument and a complete after-reading comparison of the new geometric extension.

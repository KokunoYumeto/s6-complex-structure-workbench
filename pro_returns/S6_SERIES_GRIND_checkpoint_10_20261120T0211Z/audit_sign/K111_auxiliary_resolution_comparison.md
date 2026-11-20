# K111: actual auxiliary-resolution maps and current completion scope

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), 19 November 2026. This is a continuation of the full printed comparison and fresh cone calculations. It does not claim a blind reconstruction of the full original proof or a second model family.

## The literal role of the upper triangulations

I2Z.9, I2O.2 and I2I.2 first construct convex periodic cells in the original valuation lattices and then triangulate their upper faces. Their subsequent chart maps are proper subdivisions to those stated toric cells. The seventy-two triangles are therefore the chosen auxiliary subdivision of a fixed periodic cell model. The underlying source characters, actual point/O modules, full period functions and physical circle are separately specified in I2Z.19–23, I2O.3 and I2I.3.

The original zero upper array is absent from the supplied files. The explicit program `code/K111_zero_upper_flop_witness.py` constructs two seventy-two-triangle arrays obeying the printed hexagon, lattice, source-band and whole boundary conditions. They differ by the square circuit

\[
(-10,-5)+(-9,-4)=(-9,-5)+(-10,-4).
\]

The literal one-to-zero map, with the retained period word, carries the top-edge parameter to
\(\gamma(t)=(-10+2t,-3-3t)\). One diagonal introduces \(t=2/5\); the other does not. Its character map is

\[
X'_0=P^2X_1/Y_1,\qquad Y'_0=P^{-3}p^{-1}/X_1,
\]

with inverse
\(X_1=P^{-3}p^{-1}/Y'_0\),
\(Y_1=P^{-1}p^{-1}/(X'_0Y'_0)\).
The witness has 22 exact checks. It proves that the printed support and band restrictions do not recover the named immutable subdivision. It identifies an explicit circuit and its source character map; no numerical return is assigned by it.

## The newly constructed common fan

The actual common torus is \((X_c,Z_c,P)=(V_{\rm reg}/Z,Z,P)\). Its periods are

\[
L_c=(P^{23}p^{-1}f_0^2X_c,P^3p^3Z_c,P),\qquad
T_c=(P^{11}p^{-1}f_0X_c,P^3p^2Z_c,P).
\]

For the word \((i,j)\), put \(A=23i+11j\), \(B=3i+3j\), \(u=2i+j\). Its valuation shift is \((Ah,Bh,0)\), its full p column is \((-i-j,3i+2j,0)\), and its full \(f_0\) column is \((u,0,0)\).

The three original cells, in this common lattice at height one, are

| Cell | Ordered vertices |
|---|---|
| Infinity fundamental domain \(H\) | \((0,0),(-12,0),(-23,-3),(-11,-3)\) |
| Zero cell | \((0,0),(5,0),(13,-3),(19,-6),(14,-6),(6,-3)\) |
| One cell | \((0,0),(1,-3),(13,-3),(12,0)\) |

Their area is thirty-six. The zero and one entries are images under the literal character maps \((X_c,Z_c)=(1/(X_0Y_0),Y_0)\) and \((X_c,Z_c)=(Y_1,1/X_1)\). Both maps and their inverses retain the original integral lattice.

`code/K111_new_common_auxiliary_fan.py` overlays the translated **convex cells** inside \(H\). The translate bounds come from exact extrema of the two coordinates of the inverse period matrix. Rational clipping yields six polygons of disjoint interiors and total area thirty-six. Every record retains its zero and one owner period word. Period copies of all boundary vertices are inserted before ordered-ear triangulation. The result has eight initial three-cones.

`code/K111_regularize_new_common_fan.py` enumerates each singular cone's entire coefficient quotient. It chooses a primitive nonzero parallelepiped ray and inserts every period copy meeting \(H\) in every incident cone. Every affected determinant strictly decreases. The file retains every parent, child, coefficient column and owner word. Its 959 stellar orbits produce **1,926 regular cones**, of maximum primitive height nineteen. The exact final area is thirty-six. Both full boundary edge sets agree under

\[
(a,b,h)\mapsto(a+11h,b+3h,h),\qquad
(a,b,h)\mapsto(a+12h,b,h).
\]

These are the actual words \(T_c\) and \(L_cT_c^{-1}\), including their full coefficient columns. The regularization and complete parent-containment checks number 100,740; the initial overlay has thirty additional checks. All new rays have positive P height.

Every affine morphism to a convex parent is the explicit semigroup homomorphism

\[
\mathbb C[\sigma^\vee\cap M]\longrightarrow
\mathbb C[\tau^\vee\cap M],\qquad \chi^m\longmapsto\chi^m,
\quad \tau\subset\sigma.
\]

Containment makes every exponent nonnegative; the lattice is unchanged. Equal character sums preserve every binomial relation. Character localization supplies the inverse on the dense original torus. The recorded period word inserts the full p and \(f_0\) factors above. No roots of these units are adjoined.

The support is unchanged. The valuative criterion can be read directly from the same cones: the character valuations of a torus point extending to the parent lie in \(\sigma\); the subdivision covers \(\sigma\), so they lie in a child cone and give a lift after the same finite base change already used to represent the valuation. Intersections of children are their common faces, which give uniqueness on their separated toric gluing. Thus these maps are the proper toric refinements of the stated periodic cell models.

## Exact common resolution on the generic exceptional domain

Let \(\Sigma_{\rm old}\) denote the actual triangulated periodic atlas named in I2F and \(\Sigma_{\rm new}\) the newly constructed atlas. Each refines the same three periodic convex cell models. The fan whose cones are
\(\sigma_{\rm old}\cap\sigma_{\rm new}\) has the literal identity-character maps just displayed to both atlases. Rational half-plane intersections give a finite list modulo the original period lattice. A relative triangulation and the quotient-ray determinant descent give a regular common refinement. This specifies its cones and morphisms mathematically; the missing old array prevents executing that particular combined list here.

The generic comparison retains each full period function because the identity-character map commutes with multiplication by its entire invariant p and \(f_0\) factors. On an affine child chart these factors have exactly the inverse-matrix exponent columns; the opposite period word cancels them pointwise. The cocharacter \((1,0,0)\) is unchanged, so these are equivariant morphisms for the original physical circle.

All added generic rays have positive P height. Localizing at P removes precisely those cones, and the maps become the identity on the original family there. Since \(t=Pu_t\) and \(s=P(p-1)/u_s\), every added divisor maps to the original collision \((s,t)=(0,0)\). Thus the generic common resolution gives an actual relative comparison over the punctured source.

The point/O comparison uses the same pulled-back functions. In common coordinates they are

\[
x_1=pP^3Z_c,\qquad y_1=Z_c^{-1},\qquad
v_2=\frac{\eta P^2X_cZ_c}{f_{P^2}(pP^3Z_c)}.
\]

The graph is the closure of the same rational map \([x_1:P^2]\). Taking its proper transform on the common resolution gives proper maps to both graph closures, with the literal charts
\(x_1=P^2a,\ ay_1=R\) and \(P^2=x_1c,\ y_1=Rc\).
Their point generators \((a-1)^{-1},(c-1)^{-1}\), zero generator \(x_1-1\), and full I2P units \(E,E_O,\eta\) pull back by the same functions. The identities \(C=-cA\) and the reciprocal coefficient arrows remain identities after pullback. This establishes the marked generic graph comparison, including its actual line-module arrow.

## Completed fresh one endpoint

The one endpoint of this new common fan is fully executed in `code/K111_new_one_endpoint.py`. For every common cone with owner \((i,j)\), its native upper rays are

\[
(a,b,h)\longmapsto(-b+Bh,a-Ah,h,0).
\]

The complete source arrow is

\[
X_c=P^A v^{12u}p^{-i-j}c_{12}^uY_1,\qquad
Z_c=P^Bp^{3i+2j}/X_1,
\]

with actual inverse

\[
X_1=P^Bp^{3i+2j}/Z_c,\qquad
Y_1=X_cP^{-A}v^{-12u}p^{i+j}c_{12}^{-u}.
\]

Each lifted cone is joined to \(E_0\). The extracted upper top edge is the minimal interval \((0,1),(1,1)\) in the exact lattice \(U(a,b)=(3a,a+12b,b,0)\). All twelve lower raw parents and their eight regular children are then attached.

The output has 2,022 regular four-cones, 3,056 internal facets and exactly 1,926 generic boundary facets. Its L source/target facets number 24 on each side; its T source/target facets number one on each side. Every other facet is paired internally. The actual L and T character matrices, their inverses and both full unit columns are checked on all twenty-five paired facets. Every vanishing face coordinate maps to its actual target coordinate; negative powers occur only on the stated localizations. The original source rows \(3r-x\) and \(x\) are nonnegative on every cone. The full point coefficient and its reciprocal are retained. There are 15,217 checks.

The whole compact one-corner inventory consists of sixty isolated points, with contribution \((12,88)\). Each of its twelve lower surfaces has the minimal three-chart star and completed pair \((1,-2)\), verified by the cyclic intersection calculation and the exact contraction route. These values are scoped to this constructed endpoint.

The old and new one endpoints both refine the same I2O convex cell support and agree on the entire pure lower fan \(r=0\), with rays \(E_0,\ldots,E_{12}\). Their cone-intersection common resolution retains that subfan; every added ray has \(r>0\). The same semigroup maps are therefore the identity after localizing at P. They retain the full L/T periods, original point graph and physical cocharacter \((0,1,0,0)\). Every exceptional divisor maps to \((s,t)=(0,0)\). This proves the relative one-end marked comparison at the level of its specified toric and point-graph maps.

## Completed zero and infinity endpoints

The zero endpoint is now fully executed in `K111_new_zero_endpoint_v2.json`: 54,121 regular four-cones, 1,926 generic boundary facets, 302 complete period pairs, all actual source-band rows, and exact slice volume 29/2. The 555,873 checks include every quotient star, source-cut star, period completion and full reciprocal unit column. All additional corner rays have positive values of both original base heights. Its entire P-invertible lower fan remains the two original triangles on A,B1,B2,B3.

The infinity endpoint is fully executed in `K111_new_infinity_endpoint.json`: 2,381 regular four-cones, 1,926 generic facets, twenty-five full period pairs and exact slice volume 95/6. Its 21,005 checks retain the source arrow `(Xc,Zc,P,p)=(X,Z,Ru,u^-1)`, the full `f0=u^-12*f_infinity`, all 120 quotient stars and the complete compact corner inventory. The compact corner pair (-1331/9,-583/9) agrees both through direct intersection matrices and two exact auxiliary-character evaluations. Its R-invertible lower fan is exactly the original cone on A0,A1.

## Complete physical-owner compact calculation

`K111_T2_compact_ledger.json` assigns the physical components before evaluating the second circle. It has 1,664 completed generic physical components and 33,847 zero, sixty one and 337 infinity compact corner components: 35,908 compact owners in total. Every generic disc or half-plane star and every compact corner point, curve or complete angular surface star is retained. The other thirteen physical owners are the single zero moving component and twelve labelled one-end lower components. All 67 second-fixed pieces belonging to those owners remain assigned to them and are handled in their actual framed calculations.

For each compact F the proof in `K111_two_torus_physical_specialization.md` keeps the actual physical normal Euler factor, localizes the second circle within F, cancels its poles and evaluates the original physical contribution at the second parameter zero. The 983,447 exact checks cover 1,926 three-end curve clutches and 52,546 compact corner second-fixed pieces, with cancellation and two numerator-preserving substitutions separately for every F. The resulting complete compact pair is (895,139).

The parent agent then independently recomputed all 35,908 owner sums, both substitutions, the 1,926 ordered matrix clutches and 52,546 corner pieces without importing or reading the producing implementation. Its `code/K111_compact_owner_independent.py` receipt has 484,310 checks and the same pair (895,139). This is a separate implementation by the same GPT-6 Astra model family; it is not a second-model claim.

## The actual point-graph scope and the filling morphism

An additional full receiving test found that the already-counted four-cones do **not** all map to the proper graph of (x,P²). The mixed-sign counts for val(x)-2val(P) are 8,723 at zero, 229 at one and 184 at infinity. The counts crossing some chart boundary of the further A1 resolution are 11,051, 440 and 841. These failures are saved, including every affected cone index, in `K111_point_graph_lift_scope.json`. The earlier symbolic boundary comparison did not test these inequalities. Its claim is restricted accordingly. The initial broader proof draft is retained as `K111_new_auxiliary_proof_initial_unresolved_graph.tex` and is superseded by the complete received filling proof.

The construction now uses the regular toric atlas as a filling of the marked exterior in its own right. It does not pull back and resolve a new source graph inside the counted atlas. The toric compact circle action, regular tangent bundle and physical fixed inventory are defined on the full constructed atlas. The graph comparison is used precisely on the unchanged exterior and twelve lower source bodies where its complete chart maps have been checked.

Every face of the entire localized exterior lies in one of the original graph/resolved-node charts. The maps are `a=x/P²`, or `(u,w)=(x,P/x)`, or `(u,w)=(x/P,P²/x)`. The latter two have the actual inverse source equations `(P,x,c,y)=(uw,u,uw²,Ruw²)` and `(uw,u²w,w,Rw)`. All their coordinate rows are nonnegative on their designated original faces. At infinity, the whole localized lower cone uses `(u,w)=(R² u_base Zc,R^-1 Zc^-1)`. These maps retain the original R unit. All twelve one-end lower owners have three charts apiece; every one of those thirty-six charts maps to the resolved graph through these equations. The complete receipt has 20,711 checks.

The identity-character maps identify the full original exterior atlas, with its full period functions. Their point-module map is the identity on the same I2P generators and entire coefficient functions, including P powers and the O factor P^-2. Thus the same analytic exterior and original physical line are glued to the new toric filling. On the compact interior the physical action remains the literal toric cocharacter; a projection of that entire interior to the resolved point graph is not part of this filling construction.

For the second action use the compact group S1×S1. The full theta-ratio coefficient acts on the point charts by `A'=xi*zeta*E/E'*A`, `C'=xi*E/E'*C`, and on the O module by `C'_O=xi*zeta*(x-P²)/(zeta*x-P²)*EO/EO'*C_O`. Invariant small node domains keep E and its reciprocal units. On an invariant O annulus 1/2<|x|<2 and |P²|<1/4, both linear factors are nonzero for |zeta|=1. These maps therefore extend at both original sections, preserve `C=-cA`, and compose by cancellation of the middle entire unit. For zeta=1 they give exactly the original physical scalar multiplication.

## Moving normal bundle and lower doubles

The new zero moving owner has thirty-one full charts, twenty-six of which cross an ambient point-graph wall. Its comparison uses the exact scope of NS.23a: the full outer normal derivative into the held Cox product, together with the actual normal divisor bundles in the interior. A global ambient source-graph lift is not used. The complete native characters give Dminus²=-309, Dminus*Dplus=293 and Dplus²=-305. All thirty compact source rays and their thirty-by-thirty intersection matrix are retained. An independent chronological calculation contracts twenty-nine actual sum-of-neighbor rays to the original P1-times-disc fan, retaining reciprocal localizations and the normal powers.

The cap is the same specified NC map with the new full derivative N. Its exact equations `B=C^-1*N` and `C_hat*B=N` identify the cap-glued bundle; the rounded D3×D2 bordism carries that bundle to the closed replacement. Its classes are x=h+Dminus and y=-h-Dplus. The output `K111_new_moving_cap.json` has 343 checks and yields (c1²,c2,p1)=(-1200,-294,-87), hence the physical moving-minus-own-reference pair (-906,-111). The fixed-source RB reference, including its own cap, remains the unchanged original bundle with those three characteristic numbers zero.

The twelve minimal lower stars use their complete resolved-source maps above and the entire IL source flow, normal arrows, line ODE and inverse cap square. Their actual full product `Hplus*Hminus=P/us`, L factors P^-2 and P², and complete gamma identity are retained. The collision normal pairings are (-2/3,-1/3,-2/3); the original reciprocal cube-framed reference has (-2/3,+2/3,-2/3). The exact boundary torsion equality `I*(-1,-1)=(1,1)` and the unchanged reciprocal source/cap transport give closed pairings (0,-1,0) and tangent p1=0. Each double contributes (1,-2), so the twelve contribute (12,-24).

## Whole exterior, finite reference square and directed comparison

The unchanged exterior preserves P,R,s,t,q=t-tc(s), every original analytic unit and the selected root r0*s^4. The ordinary infinity cap lies there. Its full invariant cube root, finite deck character and integral annular cochain are the same ASI2.26–29 maps. The forward square remains `Phi_(rho+4)*q^4=h_infinity^4*Phi_rho`, with reciprocal arrows and the original selected-zero reindex. The exact root/source rectangle, native right phase fifteen and physical winding thirty also remain unchanged.

On opposite framed collars the tangent and physical-line connections are transported through these exact derivative and module arrows. Reversing the same interpolation reverses its transgression. The complete fixed-face inventory and actual NC/IL cap maps then give the Stokes computation of this filling: (895,139)+(12,-24)+(-906,-111)=(1,4). This combines only parts of the newly constructed filling with the unchanged fixed-source own reference.

The full RFB comparison remains `U_j -> I_j^*U_0 tensor T^(12j)`, with its endpoint-to-initial clutch and outer primitive `-j(du+alpha_q*dv)`. The original Euler collar is -36j²; the actual integer 0-to-1 Cox map fixes the linear coefficient 36, while the nilpotent tangent collar has zero p1 transgression. Thus the whole positive reference change is (72,0). The literal Jin map `[y,t] -> [y,1-t]`, with the same physical-line lift, reverses the parameter orientation. The resulting directed pair is (71,-4), with native pair (-1,72) and physical inverse-clutch value 12.

The complete receiving proof is `K111_new_auxiliary_proof.tex`, sections A–G. The parent accepted the full geometric comparison after the corrections branch's independent receiving report `audit_corrections/K111_auxiliary_boundary_comparison_05.md` (SHA256 `7c70e0fd26792cd94f3b2ea597d9b1fe53f41c7eaeacd8209d6f25b98c016b18`). Its separately attributed 137,749 boundary/normal checks, 2,464 period/cocharacter checks and 18 inherited identities close the exterior, point/O, source, cap and reference maps at their exact scopes. The report and these scopes have now been read in full by this branch. The new auxiliary-filling route proves the stated K111 pair and physical return. The larger F41/F46/K94/K96 chains retain the exact imported scopes in `K111_import_scope_map.md`; a complete new reproof of those larger results is not claimed. The absent original common array, original compact (2723,19124) ledger and original 324-chart lower chain remain in the separate final problem `iv:open:K111:original_auxiliary_arrays`. All their text and tags are preserved once; the new proof uses its own complete atlas, physical components and actual boundary maps. The failed whole-interior graph assertion remains recorded and supplies no input to this route.

## Exact final-atlas linkage

`K111_same_atlas_link.json` passes286,678 checks. Every final endpoint chart occurs exactly once across generic, compact and explicitly capped pieces. Every physical-owner face is compared through its actual native/common character map; every corner weight and all31 moving ordered cones/full T0 alignments agree with the final fan. The SHA256 table links both parent independent input receipts to these unchanged compact and moving outputs. The separate parent moving calculation has378 checks and reproduces the full divisor matrix, chronological blowup coefficients, own-cap roots and pair(-906,-111).

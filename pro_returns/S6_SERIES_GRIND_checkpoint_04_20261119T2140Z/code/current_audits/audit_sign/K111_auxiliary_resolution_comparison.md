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

## Remaining completed-family calculation

The fresh zero endpoint still requires its whole regular four-dimensional extension, both source bands, all three period facet pairings and the finite point/O graphs. Its comparison uses the full matrix I2ZC.3 and inverse

\[
X_0=P^{A+B}p^{2i+j}f_0^u/(X_cZ_c),\qquad
Y_0=P^{-B}p^{-(3i+2j)}Z_c.
\]

The fresh infinity endpoint still requires its lower determinant-eleven joins, full facet completion and fixed-star inventory. Its actual source arrow is
\((X_c,Z_c,P,p)=(X,Z,Ru,u^{-1})\), with inverse \((R,u)=(pP,p^{-1})\) and \(f_0=u^{-12}f_\infty\). The original physical cocharacter and the full volume signs remain those in I2L and CFL.16.

After these executed extensions, the whole compact fixed-star calculation must use their actual generic normal clutch vectors, completed surface intersection matrices and corner stars. The new one-end values are not inserted into the old CFL total. The original unavailable common-edge chain, original numerical CFL ledger and final absolute seed retain their stated open verification scope.

The final comparison of complete quotients must retain the same marked outer circle bundle, both finite-character/reference squares, original parameter arrow and endpoint caps. On any common region where the displayed refinement maps are the identity, their derivative is the identity on the tangent bundle, and their point-module arrow is the identity on the actual physical nonzero-vector line. These are the concrete maps required for the eventual glued quotient bordism. No completed whole-family bordism or absolute return is assigned at the present stage.

# 01GL / cdp:st:E14 — prereading derivation

Checker: i_provenance_recovery. Written on 21 November 2026 with the target E14 proof and E_checks.py still closed. The exact safe statement, its E1/E4/E5/E6/E13 inputs, the root-isolated Liu–Rollenske construction data and the separately bound primary construction statements were read. Previously completed E7 and D.1.9 are declared inputs. The related E13 status messages and primary two-parameter coherent-calculation context are disclosed in the prereading input receipt. No independence from these declared inputs is asserted.

Fix any nonzero sufficiently small scale u₀ in the Liu–Rollenske construction. The derivation below is uniform after restricting u to a disc about u₀ contained in the construction's punctured small-scale range. It proves the stated tangent dimensions, a transverse cusp-splitting deformation, smooth reduced two-dimensional Kuranishi germ, and the fibration/algebraic-dimension assertion.

## 1. Exact coordinate transport of the Liu–Rollenske input

Put k=27/4. In the original primary Weierstrass equation use

    T = k(1−t)/t,   X=x/t²,   Y=y/t³.

Substitution gives

    Y²=X³+TX+T,     P=(−1,i).

The old III* value 0 maps to T=∞, the old cusp value 1 to T=0, and the selected old I₁ value ∞ to c=−27/4. This is an isomorphism of Weierstrass models over the indicated base automorphism, not just an identification of generic equations. Near old t=0, the new infinity coordinates are X∞=X/T²=x/[k(1−t)]² and Y∞=Y/T³=y/[k(1−t)]³; their denominators are units and the new base coordinate is 1/T=t/[k(1−t)]. Near old t=∞, put v=1/t. Then X=v²x and Y=v³y are precisely the old infinity coordinates, and T=k(v−1). These charts prove the global isomorphism. It lifts to the minimal resolutions and preserves both P and O.

Consequently the pullback identifies M=O(P−O), the translations by −2P, and the homomorphism φ with its prescribed zero on the selected I₁ fibre. Choose the transported φ itself, so the scale u is unchanged. A different holomorphic choice φε'=a(ε)φε would give the explicit invertible parameter change (u,ε)↦(a(ε)u,ε).

The proposed transverse elliptic input is

    Sε: Y²=X³+TX+T+ε,
    Pε=(−1,b(ε)),  b(ε)²=ε−1,  b(0)=i.

Its finite discriminant polynomial is

    Dε(T)=4T³+27(T+ε)²,
    disc_T(Dε)=314928 ε³(1−ε).

Thus for small ε≠0 there are three simple finite nodal values. Exactly one is the holomorphic simple root c(ε) continuing c=−27/4. The other two replace the cusp at 0. The selected linearization zero remains c(ε); the other two singular fibres are the rank-one nodal fibres of the open quotient construction.

For comparison with the cited E13 equation, set T=α⁴t, X=α²x, Y=α³y and α⁶=ε on a ramified punctured parameter cover. Then

    y²=x³+tx+μt+1,  μ=α⁻²,  μ³=1/ε.

The corresponding section is x=−μ, y=α⁻³b and its square is 1−μ³. This exact transport puts ε near 0 at large μ. Therefore the small-μ conclusion of E13 is not used to establish the cusp calculation below.

## 2. The actual holomorphic family of threefolds

At infinity use T=r⁻⁴, X=r⁻²x', Y=r⁻³y'. The good-reduction equation and section are

    y'²=x'³+x'+r²+εr⁶,   P'ε=(−r²,b(ε)r³).

The deck map is

    (x',y',r) ↦ (−x',−iy',ir).

It preserves the equation and carries P'ε(r) to P'ε(ir). At r=0 the elliptic curve and its nonzero fixed two-torsion point (0,0) are independent of ε. Under a scaled Weierstrass uniformization with square lattice this point is the half-diagonal class (1+i)/2: its wp value and derivative are zero. Thus the point is the exact same fixed two-torsion datum as in the primary construction.

The minimal elliptic surfaces Sε form a holomorphic family near ε=0. The finite cusp in the fibre causes no singularity of the surface: the derivative of its defining equation with respect to T is −(X+1), nonzero at the cusp. The only Weierstrass resolution is the constant III* configuration at infinity. Its equisingular good-reduction model above gives the same resolution configuration and section component, so it resolves simultaneously over a sufficiently small disc.

The line Hom(t_{2Pε}*Mε,Mε) is the fibre class O(F) throughout this family. Here is a direct persistence argument from the central primary input. At ε=0 its section φ has exactly the selected full fibre as divisor. The central surface is rational, so H¹(O)=H²(O)=0. Upper semicontinuity gives the same vanishings on nearby smooth surfaces, and the exponential sequence identifies Pic(Sε) with H²(Sε,Z). The two line bundles in this assertion have equal Chern classes centrally and vary in the fixed integral lattice of the smooth surface family, hence have equal classes for every small ε. Translation is the Weierstrass addition map with inverse translation by the negative section; the two maps extend to the relatively minimal elliptic models, whose uniqueness over the base preserves this inverse pair. Their ratio line is trivial on every fibre of the surface family. Grauert for this ratio, whose fibre H⁰ is one and H¹ is zero, makes the relative trivialization holomorphic. Choose it to agree with the transported central φ. The section of O(F) vanishing at c(ε) then gives φε holomorphically.

Use Mε× and

    τε(s,m)=(t_{−2Pε}(s), u φε(t_{2Pε}*m)).

Freeness and proper discontinuity hold uniformly for u in a sufficiently small punctured range. A Hermitian norm on the line bundles over the compact surface family bounds the norm of φε uniformly; multiplying by small u makes the action strictly contracting on nonzero line fibres. On compact base subsets away from c(ε), its norm also has a positive lower bound. These two estimates give freeness, proper discontinuity and properness of the compact quotient fibres exactly through this action.

At the selected simple node the integral degeneration data, the selected zero of φε and the toric fan are fixed under this holomorphic deformation. The toric charts have the equations xy=T−c(ε) and xyz=T−c(ε), with invertible holomorphic gluing units. Thus the same gluing gives a holomorphic completion with the dP₆ normalization and opposite-side identifications. This completion is a smooth total-space family; its local derivatives and gluing maps have the displayed normal-crossing equations.

At infinity the good-reduction torus family has the same lattice action and fixed torsion datum. The primitive class a=e₄/4 with ξ(a)=1/4 determines the holomorphic order-four torsion section. Twist the deck map by that section. Its order is four; the central fibre action is free by the primitive ξ-coordinate in the primary construction. The same fixed-torsion model and compactness give freeness after shrinking the parameter disc. The punctured gluing is the explicit translation

    σ_a(r)=(log r)/(2πi) ·4a(r),
    Ψ_a(x,r)=(x+σ_a(r),r),
    Ψ_a ρ = ρ' Ψ_a.

These maps vary holomorphically with ε and u; changing the log branch adds a period. They give the same inverse translation gluing as at ε=0. This constructs a proper holomorphic family Yε,u with smooth total-space fibres and central member exactly the given Y(u). The primary topology statement gives b₁=b₂=0 and integral six-sphere topology centrally; the nearby smooth proper family has the same differentiable type.

## 3. The root base, canonical bundle and coherent direct images

Let B denote the reduced multiplicity-four fibre over infinity, so f*∞=4B. Form the order-four root curve 𝔅 of (P¹,∞), with root divisor D and coarse map q:𝔅→P¹. The map

    p:Y→𝔅

is specified by the line O_Y(B), its canonical section, and the isomorphism O_Y(4B)=f*O_{P¹}(∞). On the root chart the base change of Y is the good-reduction torus family. Thus the map is smooth at the root fibre. Its other singular fibres are the cusp fibre and the selected normal-crossing fibre. Write L=O_𝔅(−D).

The canonical line is

    K_Y = O_Y(−4B) = f*O_{P¹}(−1).

To check the divisor, on M× over finite T use the three-form

    Θ = dX∧dT/(2Y) ∧ dlog z.

A change of line trivialization adds a differential from the surface to dlog z; wedging with its top-degree two-form kills that term. Translation on the elliptic surface preserves its relative invariant differential, so Θ is τε-invariant. At the cusp and ordinary nodes the residue expression dX∧dT/(2Y) extends as a nonvanishing two-form on the smooth elliptic surface. In a toric completion chart xyz=T−c, the equivalent form dlog x∧dlog y∧dT is dx∧dy∧dz; the double chart gives the same nonvanishing conclusion. Hence there are no finite zeros or poles.

At infinity the displayed substitution gives Θ=−4r⁻⁴Θ_good, up to the nonzero line-trivialization unit. The good three-form is invariant under the free order-four action and descends as a nonvanishing local canonical frame. The divisor is exactly −4B. On the root curve,

    K_𝔅=O_𝔅(−5D),   T_𝔅=O_𝔅(5D),
    ω_{Y/𝔅}=p*O_𝔅(D)=p*L⁻¹.

Every fibre of p is a connected Gorenstein Cartier surface. Its dualizing sheaf is trivial, because the displayed relative canonical bundle is pulled back from the base. The degree-one cohomological-flatness input gives H⁰(O)=C. Serre duality therefore gives h²(O)=1. Flatness over the smooth local base charts follows from torsion-freeness over their discrete valuation rings. Euler characteristic is constant in this proper flat family and is zero on a smooth torus fibre, hence h¹(O)=2. These statements hold after the root chart at infinity as well. Grauert gives locally free direct images and base change. Relative duality gives

    p_*O_Y=O_𝔅,   R²p_*O_Y=L.

The cup product identifies det W with L, where W=R¹p_*O_Y. At a smooth torus and the root abelian fibre this is the usual exterior product. At the cusp, the normalization sequence has quotient O_E on the cuspidal elliptic curve E; the product of its additive connecting class with a nonzero elliptic H¹ class maps to the generator of H² through the same connecting map. At the selected toric fibre the normalization complex has one rational surface, three rational double curves and two triple points. Its O-cohomology is the cohomology algebra of the torus formed from two triangles. In an oriented basis the degree-one cup pairing is [[0,1],[-1,0]], so it is again nonzero. Thus the exterior product is an isomorphism on every fibre and hence on the base.

The integral transgression class of the already completed D.1.9 construction gives a nowhere-zero section β of W. At finite values this follows from its nonzero integral full-fibre restrictions and the coefficient injection. At the root fibre its restriction to the reduced bielliptic surface is nonzero for the same coefficient reason; finite étale pullback to the good-reduction abelian surface stays nonzero by trace. Therefore

    0→O_𝔅·β→W→L→0.

For each integer n one has

    q_*O_𝔅(nD)=O_{P¹}(floor(n/4)·∞),   R^j q_*=0 for j>0.

This follows directly by taking the invariant monomials on the order-four chart; the invariant functor is exact in characteristic zero. In particular H¹(𝔅,L⁻¹)=0, and the extension splits:

    W=O_𝔅⊕L.

No identification of the cusp with a product surface is used in this argument.

## 4. The vertical tangent sheaf

Set A=ker(dp:T_Y→p*T_𝔅). This is locally free of rank two. At the cusp use the smooth total-space coordinates

    T=g(x,y)=(y²−x³)/(1+x).

The two partial derivatives generate (y,x²), and their syzygy is free of rank one; together with the line-direction vector field it gives A of rank two. At a double chart xy=T−c the vertical generators are x∂x−y∂y and the remaining torus vector. At a triple chart xyz=T−c the syzygies are freely generated by x∂x−y∂y and x∂x−z∂z. At the root fibre p is a smooth torus fibration.

Scalar multiplication on M× gives a section of A. In the cusp chart it is the nonzero line-direction generator. In each toric chart it is a fixed nonzero vector of the rank-two toric logarithmic frame, so it is nonzero as a section of A even at a point where its image vector in T_Y vanishes. At the root fibre it is a nonzero translation vector. Its quotient in A is therefore a line bundle.

The cokernel of dp is supported in codimension two, since the multiple fibre has been absorbed by the exact root map. Taking determinants gives

    det A=K_Y⁻¹⊗p*T_𝔅⁻¹=p*L,
    0→O_Y→A→p*L→0.

This extension splits. Its class lies in H¹(Y,p*L⁻¹). The Leray map from that group to H⁰(𝔅,L⁻¹⊗W) is injective because H¹(𝔅,L⁻¹)=0. On each regular torus fibre the tangent bundle is trivial and its constant nonzero scalar vector has a constant complement, so the extension class restricts to zero. Its image in the locally free sheaf L⁻¹⊗W vanishes on the regular open set and hence everywhere. Thus

    A=O_Y⊕p*L.

Projection formula, the direct images O,W,L and the root line cohomology now give

    h•(Y,A)=(1,1,0,0).

Put N=p*T_𝔅=p*O_𝔅(5D). The same calculation gives

    h•(Y,N)=(2,4,2,0).

In detail the direct images of A have summands (O,L), (O,L,L,L²), and (L,L²); only the O summand in degrees zero and one contributes. For N the summands are O(5D), O(5D)⊕O(4D), and O(4D), with dimensions two, four and two and no base H¹.

## 5. The critical quotient and its actual restriction maps

Let I=im(dp) and Q=coker(dp). There are two exact sequences

    0→I→N→Q→0,
    0→A→T_Y→I→0.

At the selected toric fibre, Q is O_Dcrit, tensored with the fixed base tangent line. The critical curve Dcrit consists of three rational curves joining the two triple points. Its normalization has three P¹ components, and each ordinary triple point contributes two matching conditions. Consequently (h⁰,h¹)(O_Dcrit)=(1,2). The pullback conductor in dP₆ is the hexagon. Each opposite pair of hexagon edges maps to the same theta-graph edge with opposite orientation. Therefore the induced pullback H¹(O_Dcrit)→H¹(O_hexagon) is zero. The normalization exact sequence of the surface gives

    H¹(O_Fc) → H¹(O_Dcrit)

as an isomorphism. The exact graph cochain maps and their cancellation are checked in the new program.

At the cusp, direct differentiation gives

    g_y=2y/(1+x),
    (1+x)²g_x=−y²−x²(3+2x).

Thus the critical quotient is O/(y,x²). It is a doubled elliptic curve Q₀ with nilpotent coordinate x. The reduced elliptic curve is the quotient of the line over the cusp by z↦q₀z, with 0<|q₀|<1. The restriction of a local line trivialization to the cusp is regular in the cuspidal ring, so its multiplier has no term linear in the normalization variable w. Accordingly Q₀ is locally the quotient

    (C*×Spec C[x]/(x²))/(z,x)↦(q₀(1+cx)z,x).

Its two global functions are 1 and x, and its first cohomology is a free rank-one module over C[x]/(x²). Hence (h⁰,h¹)(O_Q₀)=(2,2).

The restriction H¹(O_F₀)→H¹(O_Q₀) has rank two. This is the essential cusp calculation. Normalize y²=x³ by x=w²,y=w³. Its additive group parameter is ζ=x/y=1/w, the section P has ζ(P)=i, and translation by −2P is

    ζ↦ζ−2i,     w↦w/(1−2iw).

Modulo w³ its difference from w is 2iw²=2ix. The cusp normalization sequence represents the extra H¹ class by the missing linear term w. Restrict that sequence to the critical thickening: the normalized local ring is C[w]/(w³), the subring is C[1,w²], and the quotient is generated by w. The displayed group difference is exactly the connecting cocycle of this generator on the elliptic quotient. Its image in H¹(O_Q₀) is therefore 2ix times the nonzero elliptic cocycle.

The integral class β has nonzero image in H¹ of the normalization ruled surface, hence in H¹(O_E). Indeed the cusp normalization is a topological homeomorphism and the ruled surface projects to E with H¹ isomorphism; the real coefficient map for E is injective. Thus β restricts to a class with nonzero constant term in H¹(O_Q₀). Together with the connecting class whose image is 2ix, it forms a basis. This proves the restriction isomorphism, including the nonzero constant 2i.

It follows that

    h•(Y,Q)=(3,4,0,0).

Choose the splitting W=Oβ⊕L so that its second finite-base frame at the cusp is a connecting class, after subtracting a multiple of β. Let λ≠0 be the constant component of the restriction of β in the elliptic covering cocycle basis. Rescale the second frame so its cusp value is λ times the class represented by w. With the target basis given by the restriction of β and x times that restriction, the second image is exactly 2i times the second basis vector: multiplication by x kills the nilpotent part of the first image. This is a legitimate global splitting change because H⁰(L⁻¹) is one-dimensional and its finite-base frame is constant. At the toric fibre use the images of these two global frames as the basis of H¹(O_Dcrit), which is possible by the preceding isomorphism.

Global sections of T_𝔅 and of T_𝔅⊗L on the finite T-chart are affine linear polynomials. The map H⁰(N)→H⁰(Q) is

    a₀+a₁T ↦ (a₀, 0, a₀+a₁c),
    c=−27/4,

where the middle coordinate is the nilpotent cusp jet. It is injective of rank two. On H¹, write the two polynomial components as a(T),b(T). With the above actual bases the restriction is

    (a,b) ↦ (a(0), 2i b(0), a(c), b(c)).

This is an isomorphism. Its inverse sends (x,y,z,w) to

    a₀=x,  b₀=y/(2i),
    a₁=(z−x)/c,  b₁=(w−y/(2i))/c.

This explicit inverse proves the rank on the whole coefficient space. The new program checks both compositions on its complete Gaussian-rational basis; it does not infer rank from sampled parameter values.

The first exact sequence consequently gives

    h•(Y,I)=(0,1,2,0).

The second gives, since h²(A)=h³(A)=0,

    h•(Y,T_Y)=(1,2,2,0).

All calculations concern the actual central cusp, not a semicontinuity extrapolation from the three-node locus.

## 6. The two Kodaira–Spencer directions

Changing log u differentiates the gluing action by the constant scalar vector. Its cocycle is the nonzero elliptic covering cocycle on the critical elliptic curve. Hence it gives a nonzero class in H¹(O_Y) inside H¹(A). The map H¹(A)→H¹(T_Y) is injective because H⁰(I)=0. Thus the scale direction is nonzero.

For the ε family the local cusp map is

    gε(x,y)=(y²−x³−ε)/(1+x),
    ∂εgε|ε=0 = −1/(1+x) ≡ −1+x mod (y,x²).

A base vector field contributes only a constant in this local Jacobi quotient; its global affine values account for the constant cusp coordinate and the selected-node coordinate. The x coordinate survives in coker(H⁰(N)→H⁰(Q)), which is one-dimensional. The Čech description identifies its connecting class with the image of the ε Kodaira–Spencer class in H¹(I): on overlaps of local total-space trivializations, applying dp to the deformation vector-field cocycle gives the differences of the local derivatives of gε. Thus the nonzero x coordinate is exactly that image.

The scale direction maps to zero in H¹(I), while the ε direction maps to its nonzero generator. Therefore the two constructed directions are linearly independent. They fill the already calculated two-dimensional H¹(T_Y).

## 7. Smoothness and reducedness of the Kuranishi germ

Embed the Kuranishi germ in H¹(T_Y)≅C² with its usual defining analytic ideal. The actual holomorphic (u,ε) family gives a map from a smooth bidisc to that germ. Its composite with the embedding has invertible derivative by the previous calculation. The holomorphic inverse function theorem makes that composite a local biholomorphism of C². Every function in the Kuranishi ideal pulls back to zero on this open bidisc and therefore is the zero germ. The ideal is zero. This proves that the Kuranishi germ is a smooth reduced surface and that the displayed family is locally miniversal. It also excludes a hidden nonreduced obstruction structure; that conclusion follows from the ideal argument, not merely from the dimension of a reduced component.

## 8. Fibration retention and meromorphic functions

The completed current E7 applies to this exact Liu–Rollenske construction and supplies the rank-two hypothesis of E6 on a regular torus fibre. Its earlier independent check and the primary input maps are declared exposure, not an additional GL derivation. E6 therefore retains a proper torus fibration over P¹ for every sufficiently small deformation, including the analytic-germ scope stated there. The central b₂ is zero by the primary topology theorem and remains zero in the smooth proper deformation family. E1 identifies the meromorphic function field with the pullback of M(P¹), since smooth general two-torus fibres are Kähler. Thus every sufficiently small deformation has algebraic dimension one.

## 9. Computation and checking scope

The new program and its exact output were written and run before this target proof is released. They check the Weierstrass coefficient transport, discriminant polynomial, truncated normalization translation, cusp deformation class, conductor graph cochains and cup pairing, root-line cohomology dimensions, and both compositions of the explicit H¹ restriction inverse. The geometric identifications and sheaf maps are proved above; the program does not substitute for them.

The exact files are bound in clean_group12/S6_SERIES_PUBLISH_II_01GL_prereading_inputs.json. The old E14 routine and E_checks.py remain unopened. A different-method comparison with any positively identified old routine must be made after release and must retain this chronology.

No E14 proof or old owner check record was read to produce this derivation. Related E13 method status, the primary Two coherent calculation, prior E7 and the stated construction/topology inputs are expressly disclosed. No additional event is awarded for the source opening, for individual finite computations, or for the future full-proof comparison until its actual scope is recorded.

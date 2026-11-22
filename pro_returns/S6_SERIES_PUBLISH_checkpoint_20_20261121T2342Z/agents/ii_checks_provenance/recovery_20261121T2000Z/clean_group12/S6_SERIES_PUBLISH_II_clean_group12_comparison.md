# 01GL / E14: frozen derivation and complete proof comparison

The own derivation was frozen at 23:30:06 UTC on 21 November 2026, before
release or reading of E14. Its original bytes remain unchanged. The
statement, cited statement inputs, root-isolated construction definitions,
primary construction statements and the declared prior E7/D.1.9 work were
read before the freeze. The related E13 method/status messages and the
primary two-parameter coherent-calculation context are expressly disclosed.
They do not provide the E14 cusp proof. No independence from those declared
inputs is asserted.

After the freeze I released and actually read the entire E14 statement and
all thirteen original proof items, including the initial workflow item.
I then read the complete current owner, which differs only by the already
applied E4 primary-reference transport and a terminal newline. The current
reference is Viaclovsky's Theorem 2.2, pages4–5. No earlier snapshot has been
overwritten. I subsequently read the complete E13 proposed proof and its
comparison, supplied by C, solely to verify the local maps invoked by E14.
That reading is postfreeze input verification and earns no E13 event.

## Result and actual scope

The independently constructed family has exactly the original E14 domain:
every nonzero sufficiently small Liu–Rollenske scale, with a local
two-parameter deformation about that member. The tangent dimensions are
(1,2,2,0); the Kuranishi germ is a smooth reduced surface; the transverse
parameter replaces the cusp by two rank-one nodal fibres; and all small
deformations retain a torus fibration and have algebraic dimension one.
The original statement is retained byte for byte except for its hidden
bibliographic metadata. No smoothness hypothesis is added: these are the
specific smooth manifolds constructed in the primary theorem.

The proof is compared on the actual family. The ramified coordinate change
T=alpha^4 t, X=alpha^2 x, Y=alpha^3 y with alpha^6=epsilon identifies the
punctured elliptic equations with the E13 equation at mu=alpha^-2. Thus
mu^3=1/epsilon. It carries a cusp neighbourhood to large mu, and supplies
no transport to the small-mu theorem's domain. The final proposal uses only
the local connection, period-pairing, normalization and ideal calculations
from the E13 proof, writing their particular maps for this family. The
cusp calculation itself is established in both the frozen derivation and
the printed proof.

## Complete proof comparison

1. **Weierstrass and scale transport.** The displayed affine change has
   k=27/4 and T=k(1-t)/t. The own derivation also supplies both omitted
   charts: at old zero the new infinity coordinates are
   x/[k(1-t)]², y/[k(1-t)]³ and t/[k(1-t)]; at old infinity they
   are v²x,v³y and T=k(v-1). The new proof writes these maps. They
   identify O,P,M=O(P-O), the lifted translation and the selected
   linearization. The scale is preserved by choosing the transported
   linearization. The three exceptional values and the section P=(-1,i)
   agree exactly. The new transverse equation has discriminant
   4T³+27(T+epsilon)² and cubic discriminant
   314928 epsilon³(1-epsilon); the selected simple node remains separate.

2. **The actual family and gluing.** The frozen derivation establishes
   the varying line-homomorphism bundle using the central primary
   identity, the smooth surface family, H¹(O)=H²(O)=0 and the integral
   Chern-class identification. Grauert makes the resulting trivialization
   holomorphic. The proposal writes this argument before using its
   contracting multiplier. The fixed toric fan gives the selected-node
   filling; the infinity equation, torsion class and inverse punctured
   logarithmic gluing give the same root construction. The original
   compact-family argument and Ehresmann conclusion are retained.
   Primary Proposition2.1 and Theorem5.1 are exact numbered locators in
   the already cited arXiv v2 source. They replace source-label prose;
   no page number inferred from a private font-wrapper build is printed.

3. **Root and canonical maps.** The own proof constructs the root
   morphism from O_Y(B), its section and O_Y(4B)=f*O(infinity), with
   f= rho composed with fbar. This is now explicit in the paper.
   The cusp form identity is unchanged. At xyz=T-c the toric
   logarithmic form becomes dx wedge dy wedge dz. At the order-four
   root chart the surface form picks up -4r^-4, and the invariant good
   three-form descends through the free affine quotient. Hence
   K_Y=f*O(-1)=fbar*O(-4), with the exact same divisor convention in
   both arguments. Adjunction, H0=C, duality and flat Euler
   characteristic give (1,2,1) on every full fibre. Grauert's
   locally-free/base-change conclusion is therefore justified on the
   full (T,epsilon) base, including the cusp point.

4. **Vertical Lie and coherent bundles.** The printed connection is
   alpha=(y+b)dx/[2y(x+1)], with the stated +1,-1 residues. For
   omega=dx/(2y) and its dual V, the horizontal lift is
   V-alpha(V)v*d/dv. The root substitution gives
   (y'+br³)dx'/[2y'(x'+r²)] and omega=r omega'. These exact maps
   give E=O+O(-1). The local cusp vector field is regular because
   its connection coefficient is regular there. The proposal makes
   its cusp scope explicit after the root transition.

   The printed comparison G=R1O -> E uses the invariant alternating
   pairing H1(C)/F1 -> (F1)* on smooth fibres. At rank-one points
   its coherent frame consists of the graph-loop and elliptic
   normalization classes; at the rank-two hexagon both are graph loops.
   The good-reduction frame supplies infinity. I read these complete
   local comparisons in C's E13 final proof after the E14 freeze.
   They are applied to the connection just written, without asserting
   a parameter-domain inclusion. G and E are locally free at the sole
   missing point of the two-dimensional base, so both the isomorphism
   and its inverse extend by Hartogs; their composites remain identity.
   This checks an isomorphism rather than only equality of degrees.

   The own derivation has a second route: the all-fibre cup pairing
   identifies det G with O(-1); the integral class beta is nowhere zero
   by D.1.9, normalization and trace on the root cover; and
   H1(O(1))=0 splits 0->O beta->G->O(-1)->0. Its vertical tangent
   extension splits by the Leray restriction map and its zero
   restrictions to regular tori. That route is independent of the
   printed Hartogs step and reaches the same actual bundles.

5. **Logarithmic tangent sequence.** The coordinate change
   x~ = x/(1+x)^(1/3), y~ = y/(1+x)^(1/2) sends the cusp map to
   y~²-x~³. The three printed logarithmic generators are exact:
   their determinant is 6(y~²-x~³), and their map to the base is
   (0,6T,0). They give the stated kernel and O(5-8)=O(-3)
   quotient. Weighted line cohomology yields h(Tlog)=(1,1,0,0).
   The proposal now bounds this temporary renaming to that local
   module computation and explicitly returns to the Weierstrass
   coordinates. The coordinate map carries the Jacobian ideal to
   itself and x~=x modulo x², so the later jet coordinate is unchanged.
   This is an exact quotient-ring transport, not an unstated renaming.

6. **Cusp critical thickening.** The printed critical curve has
   T=-3x², epsilon=x²(3+2x). It is smooth and finite flat of
   degree two over the epsilon disc. The translation fixes x
   on its punctured part, hence throughout; its line multiplier is
   a nonzero holomorphic contraction. The resulting elliptic family
   has H0 and H1 free of rank one over the central dual numbers
   A=C[x]/(x²). The own proof obtains exactly that critical quotient
   from (g_x,g_y)=(x²,y) for g=(y²-x³)/(1+x).

7. **The actual H1 restriction at the cusp.** In the printed method,
   the horizontal lift at a nearby node has line component
   -b/(1+x). The toric line is generated by Vtilde+
   [b/(1+x)]v*d/dv. Quotienting to the elliptic normalization
   gives the row (1,-b/(1+x)). These particular maps are now
   displayed, rather than only referring to E13. The normalization
   exact sequence of the cuspidal fibre, with quotient O_E and
   dimensions (1,2,1), proves surjectivity to H1(O_E).
   Therefore the scalar in that row extends as a unit. On the
   central dual numbers b=i and the row is (1,-i+ix), with
   matrix [[1,-i],[0,i]] and determinant i. This proves full
   rank on the nonreduced critical fibre.

   The own frozen route normalizes the cusp by x=w²,y=w³.
   Its additive group coordinate is zeta=1/w, P has zeta=i,
   and translation by -2P is w -> w/(1-2iw). In C[w]/(w³)
   the connecting cocycle of the missing normalization term w
   is 2i*w²=2i*x. The beta class has a nonzero constant
   elliptic component. Hence the actual restriction is an
   isomorphism with a basis model diag(1,2i). This supplies
   both the cusp nilpotent contribution and its nonvanishing.

   The two displayed linear models are related explicitly. Fix the
   same cyclic target frame e of H1(O_Z) over A, choose p,q in
   H1(O_C) with R(p)=e and R(q)=2i*x*e, and then put
   p'=p, q'=-i*p+q/2. One has R(p')=e and
   R(q')=(-i+ix)e. The source change is [[1,-i],[0,1/2]]
   with inverse [[1,2i],[0,2]]. These formulas construct the
   comparison of the models on the actual restriction map.
   They do not claim that an unspecified original beta frame is
   already the connection frame, and the program alone is not
   used to identify those geometric frames.

8. **Dimensions and Kodaira–Spencer map.** The original logarithmic
   exact sequence and h(J)=(0,1,1), together with the rank-two
   quotient (0,0,1), yield h(T)=(1,2,2,0).
   The frozen proof uses 0->I->N->Q->0 and
   0->A->T->I->0 instead. It computes h(N)=(2,4,2,0),
   h(Q)=(3,4,0,0) and the restriction map
   (a(T),b(T)) -> (a(0),2i b(0),a(c),b(c)).
   Its explicit interpolation inverse verifies the full four
   dimensional map; the conductor cochain comparison supplies
   the selected-node restriction. Thus h(I)=(0,1,2,0).
   Both exact sequences give the same tangent groups.

   The epsilon derivative is exactly -1/(1+x)=-1+x modulo
   the Jacobian ideal. A variation of the base map on a trivial
   ambient deformation contributes only a constant to this
   quotient. The nilpotent x coefficient therefore detects a
   nonzero tangent direction. The scale direction is independently
   nonzero: its elliptic singular-curve modulus varies with u,
   while the intrinsic anticanonical pencil and exceptional fibre
   configuration are preserved by a trivial ambient deformation.
   The own proof also identifies its nonzero class in H1(A)
   and the epsilon class's nonzero image in H1(I). These
   maps prove independence of the two directions.

9. **Kuranishi and all deformations.** The actual bidisc maps into
   the Kuranishi embedding with invertible differential. Presenting
   its ring as C{z1,z2}/I, the inverse function theorem makes
   the substitution before quotienting an isomorphism. Every
   element of I pulls back to zero, so I=0. The proposal
   includes this argument for the complete germ, including its
   reducedness. The completed E7 supplies E6's rank-two
   hypothesis for this exact Liu–Rollenske construction; this
   dependency is now named. E1 then identifies the meromorphic
   function field with the pullback from P1, so a=1.

## Original and new computation methods

Only after the freeze and complete E14 reading did root supply the
exact E14-only slice, original lines97–104 with the necessary original
import and symbol declarations. I read every line and executed that
slice. It returns the collision discriminant
-314928 epsilon³(epsilon-1), the Taylor jet -i+ix, and determinant i.
No other routine of E_checks.py was opened.

The prerelease program uses exact Gaussian-rational truncated algebras
for the normalization translation, exact graph cochains for the
hexagon-to-theta conductor map, direct weighted line cohomology, and
an explicit interpolation inverse whose two composites are checked
on the entire four-element basis. Its cusp computation derives the
connecting cocycle rather than Taylor-expanding the printed connection
row. It verifies the geometric route in the frozen derivation.

For the discriminant alone, the prerelease program's five-term cubic
formula is a direct implementation of a standard discriminant identity.
I do not count that as a sufficient method distinction from the old
symbolic discriminant call. After release I therefore wrote a separate
critical-root norm certificate. For D=4T³+27(T+epsilon)² it verifies

    D - (4/3)T³(T+3)
      = (1/2)D' [T+epsilon-(2/9)T²].

If r1,r2 are the two roots of D', the polynomial identities give
r1+r2=-9/2 and r1*r2=(9/2)epsilon, and hence

    D(r1)D(r2)=729 epsilon³(epsilon-1).

The norm formula Res(D,D')=12³ D(r1)D(r2) and
disc(D)=-Res(D,D')/4 yields the same exact polynomial. The program
uses only sparse rational polynomial multiplication, not a discriminant,
resultant, determinant, root-solver or symbolic factorization command.
It also checks the central factorization and both inverse
compositions of the explicit jet-model basis change. This supplement is
unambiguously postrelease; it adds no second independent event.

The arithmetic program does not itself prove the line-bundle, family,
sheaf or period identifications. Those exact maps are in the frozen
derivation and the complete proof comparison above.

## Publication and accounting

The original statement, its scope, all four labelled equations, all
stable tags and all displayed final values are preserved. The proof
retains the printed logarithmic tangent/critical-curve route. It removes
the initial source-workflow item, iteration labels, empty announcements
and negative proof-status recaps; supplies the numbered primary
citations; and expands the coordinate, line-bundle, root, normalization
and analytic-ideal maps described above. Its first v1 reading exposed
two ambiguities introduced by those expansions: the cusp vector's
local scope and the rank-two normalization frame. Both are corrected
in v2 and explicitly retained in the version history.

The proposed accounting is one targeted proof check and one actual
complete comparative rereading of this owner, after root review and
application. The finite programs and their postrelease supplements,
the input E13 reading, the source update and automated validation
add no further independent event. There is no manuscript-page reading
credit and no canonical mutation by this agent.

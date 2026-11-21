# Independent recovery derivation: cdp:st:C2d, tag 01FJ

Checker identity: ii_check_a_recovery_blind. The target proof, B's proposed text and the old C_jets.py have not been opened. Read only the original statement/input packet and its supplement. The calculation below is derived from the three equations in the statement. The cited A.2.4 statement supplies the definition and one cusp instance of the inverse-Jacobian fractional ideal; all three local computations are derived here explicitly.

## Normal bundles and degrees

Let N=N_(D/Y), E=N* and L=O_Y(S)|D. The exact tangent sequence on the smooth compact curve D has deg(T_Y|D)=0 because b2(Y)=0 and the Chern class comes from Y. Thus deg N=2g(D)-2 and deg E=2-2g(D). Also deg L=0. The leading normal jet of a local equation for S is intrinsically a section of Sym^k(E) tensor L; change of equation multiplies by the line's transition, and normal-coordinate changes act by the symmetric power of the conormal transition.

For either the cusp or tacnode, the quadratic normal jet H has generic rank one. Its determinant vanishes identically, so the saturation of its generic linear factor defines a line subbundle M of E. Put Q=E/M; it is a line bundle because saturation on a smooth curve has locally free quotient. Write m=deg M and q=deg Q. The section H lies in M² tensor L and is nonzero. Hence 2m>=0 and m+q=2-2g. All assertions here concern the same H, N and D; the saturation replaces only the choice of a frame for its intrinsic generic line and does not alter the normal map.

## Cusp

The kernel of H in N is the line Q*. Restrict the third normal jet to that kernel. The change in a third jet under a nonlinear coordinate change is a contraction of H with one kernel vector, which vanishes; the same holds for a unit change of the equation. Thus the restriction is a well-defined holomorphic section b of Q³ tensor L. It is generically nonzero for x²-y³. Therefore 3q>=0. Combining the two inequalities gives

    deg E = (2m)/2 + (3q)/3 >= 0,

so g<=1. When g=1 both m and q are zero. Nonzero sections H and b of degree-zero lines on a compact curve have no zeros. In local coordinates (x,y,z), with D given by x=y=0, the holomorphic Morse splitting in the x direction removes all terms involving x beyond a nondegenerate square. The remaining function starts with a nonzero multiple of y³ at every z. Extracting a holomorphic cube root of its unit changes y biholomorphically and gives the parameter-preserving equation x²-y³=0 everywhere along D. Concretely, the coordinate change has nonzero diagonal linear terms in x,y and leaves z on D unchanged.

Its normalization is (t,z) to (x=t³,y=t²,z), which is finite and birational: t is integral, t²=y, and on the dense set y nonzero it is x/y. The source is smooth and normal, hence is the normalization. The curve t=0 maps isomorphically to D. The leading term y=t² gives an isomorphism Q to (N*_(C/T))² along this curve. Since deg Q=0, the normal line of C in the normalization has degree zero.

## Tacnode

The cubic restriction to Q* vanishes identically because it vanishes generically for x²-y⁴. In a local frame adapted to M and Q, keep the relevant terms of the equation as

    a x² + b x y² + c y⁴,

where terms x³,x²y and terms of higher relevant weight do not affect the fourth-order restriction after eliminating the nondegenerate x direction. On the open set a nonzero, its critical-value fourth coefficient is c-b²/(4a). The vanishing of the cubic restriction makes this fourth coefficient intrinsic: a different transverse complement or a nonlinear coordinate change changes the critical-curve parameter only by its linear map on Q*, and lower-degree restricted coefficients are zero. Multiplying by H clears its only possible denominator and defines a global holomorphic section

    Delta = 4ac-b² of M² tensor Q⁴ tensor L².

One may check holomorphic gluing directly from x replaced by x+lambda y²: b changes to b+2a lambda and c to c+b lambda+a lambda², leaving Delta unchanged. Linear frame and equation changes supply exactly the displayed tensor powers. The identity holds where a is nonzero and hence everywhere by holomorphic extension; the polynomial expression shows there is no pole at a zero of H. The generic tacnode hypothesis says Delta is nonzero.

It follows that 2m+4q>=0, as well as 2m>=0. Therefore

    deg E=m+q=((2m)+(2m+4q))/4 >=0.

Again g<=1. For g=1 both nonnegative summands vanish, so m=q=0 and both a and Delta are nowhere zero in every local line frame. The x-direction holomorphic Morse splitting, followed by extraction of a fourth root of the residual unit, gives x²-y⁴=0 near every point of D, with holomorphic parameter z along D.

The normalization is the disjoint pair of maps (t,z) to (x=t²,y=t,z) and (t,z) to (x=-t²,y=t,z). These local charts glue by permutations of the two branches and biholomorphisms over D. Consequently the inverse-image curve is finite unramified of degree two over D; any connected component has genus one by the covering Euler formula. On each branch y=t gives Q pulled back from D isomorphic to N*_(C/T). Its degree, and hence that of the normal line, is zero. The normalization is smooth in these charts.

## Ordinary triple point

All normal jets of degree below three vanish identically because they vanish generically. The cubic jet lies in Sym³(E) tensor L. A binary cubic with three distinct linear factors has discriminant equal, up to a nonzero constant convention, to the product of the squared wedges of its three linear factors. Thus its discriminant is a holomorphic section of (det E)^6 tensor L⁴. This tensor law follows explicitly because a linear change g sends each wedge to det(g) times that wedge, and a scalar change of the cubic multiplies the discriminant by its fourth power. It is nonzero at a general point, so

    6 deg E >=0.

Hence g<=1. When g=1 its degree is zero, so the discriminant is nowhere zero. The three tangent directions remain distinct along all D. Locally their roots vary holomorphically, yielding three smooth analytic branches. Straighten two branches to x=0 and y=0. The third is y=x u(x,z) with u a holomorphic unit. The map (x,y,z) to (x,y/u(x,z),z) is a biholomorphism preserving the first two branches and sending the third to y=x. This gives xy(x-y)=0 up to a unit and proves the asserted constant transverse analytic type.

The normalization consists locally of the three smooth branch charts, with their curves over D. They glue by the permutation action on the three branches, giving a finite unramified degree-three covering. Its connected components have genus one. To compute their normal degrees, pass to the finite unramified covering which orders the three branches. On that covering the three distinct tangent lines L1,L2,L3 are line subbundles of the pullback of N. Any two sum to N. The projections of L3 to L1 and L2 in N=L1 direct-sum L2 are everywhere nonzero, hence are line-bundle isomorphisms. Thus their degrees are equal; their sum is deg N=0, so all are zero. These lines are exactly the normal tangent lines of the branch curves in the three normalization sheets. Degrees under finite covering multiply by its degree, so each original branch-cover component has normal degree zero as claimed.

## The inverse Jacobian ideals: exact normalization maps

The fractional ideal is J^-1={h in the total quotient sheaf: hJ subset O_S}. Under a biholomorphic coordinate change, the gradient transforms by its invertible Jacobian matrix; multiplying the equation by a unit multiplies its gradient modulo the equation by that unit. Consequently the fractional-ideal calculation transports through the exact local coordinate maps above, and it suffices to calculate in the displayed parameter-preserving normal forms. Coefficients below are holomorphic in the unchanged curve parameter z.

For the cusp, B=C{t,z} and R=C{t²,t³,z}=C{z}+t²B. The Jacobian ideal is (x,y²), whose image is (t³,t⁴). If h belongs to J^-1, then A=t³h is holomorphic and lies in R; also tA=t⁴h lies in R. The coefficient of t in A is zero by the first condition, and the constant coefficient of A is zero by the second. Thus A lies in t²B and h lies in t^-1B. Conversely t^-1B times t³ and t⁴ lies in R, so J^-1=t^-1B. This proves the simple-pole bound and its exact module.

For the tacnode, use the two maps x=±t²,y=t. The image ring is

    R={(f,g) in B direct-sum B: f-g is divisible by t²}.

Indeed every holomorphic function a(y)+x b(y) gives (a+t²b,a-t²b), and conversely a=(f+g)/2 and b=(f-g)/(2t²). The Jacobian generators have images (t²,-t²) and (t³,t³), with harmless nonzero constants. For h=(h1,h2), let A=t²h1 and B_2=t²h2. Membership of h times the first generator in R gives A+B_2 divisible by t²; membership for the second gives A-B_2 divisible by t. At constant order these are A0+B0=0 and A0-B0=0, so A0=B0=0. Hence h1 and h2 each have at most a simple pole. The linear relation also gives opposite residues. Explicitly,

    J^-1=(B direct-sum B)+C{z}(t^-1,-t^-1).

For the triple point use the three branch maps (x,y)=(t,0),(0,t),(t,t). Its image ring consists of triples with a common constant term and whose third linear coefficient is the sum of the first two. Every higher coefficient is independent: for k>=2 the polynomials x^k-x^(k-1)y, y^k-xy^(k-1), and x^(k-1)y realize the three individual order-k branch monomials. Thus the conductor is t²B³. The two Jacobian generators are (0,-t²,t²) and (t²,0,-t²). Put A_i=t²h_i. Their product triples must have equal constant terms; because each has a zero component, all A_i have zero constant term. Therefore every h_i has at most a simple pole. The linear relations are A1,1=-A3,1 and A2,1=-A3,1. Hence

    J^-1=B³+C{z}(t^-1,t^-1,-t^-1).

These inclusions are inclusions of the actual fractional modules in O_T(C_red) on the stated normalization charts, not a comparison only at generic points. The coefficient conditions hold in C{z}, so they control all points of the curve and all possible poles there. The three normalization maps also establish the claimed smoothness near the inverse-image curves.

The fresh prefreeze program independently checks the cleared tacnode invariant, its tensor weights, the binary wedge transformation, the degree inequalities, the finite conductor coefficient conditions and the delta-one ring descriptions. Its output and hashes will be bound below before the derivation freeze. The target proof and old C_jets.py remain unopened.

## Exact prefreeze input and computation bindings

Binding written 2026-11-21T20:16:19.121876+00:00, before target proof release.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01FJ_statement_inputs.tex — SHA256 7d15df03ab3aa6bf777f65f0ec349285d53844c5eef61b4d7dfa76a3636d0d88.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_01FJ_cited_input_supplement.tex — SHA256 2d69b83b453a3a64d00f56c2638224b9c80a5bce79e75f1a2e81efab730e71ee.
- code/S6_SERIES_PUBLISH_II_A_recovery_blind_curve_jets.py — SHA256 5a4352b704ac498f87e0634248255c71ee90027dd1749e63cc115d3acd62e316.
- code/S6_SERIES_PUBLISH_II_A_recovery_blind_curve_jets.out — SHA256 4044a85c9c780c25d9bf27aab9eb2e255ffc981fac02bb8ee7269649696407f5.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_blind_curve_jets_run.json — SHA256 f23651498e08873dd8420a0e3100dc56c4afbcb4a14c4b9acf72669b773ee4d0.

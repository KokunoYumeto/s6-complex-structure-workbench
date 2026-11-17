# Completing the untwisted construction

The local algebra in notes/part2.md and the independent audit in notes/part2_plumbing_audit_checks.md is retained. Here we supply the remaining global atlas and the exact toric comparison.

## Compact analytic plumbing atlas

Choose a smooth Hermitian metric on M over the compact rational elliptic surface S and the induced inverse metric on M^{-1}. On each of Y_i=P_S(O+M), the finite coordinate z_i lies in M and the infinity coordinate w_i=z_i^{-1} lies in M^{-1}. Choose epsilon<1/4. The middle chart is the open annular bundle epsilon/2<|z_i|<2/epsilon, times the parameter disc. There are two neck bundles. The first is over S with coordinates (z_0,w_1), the latter over h(p), satisfying

    z_0 w_1=r phi_p,
    |z_0|<epsilon, |w_1|<epsilon.

The second has coordinates (z_1,w_0) over the same p and satisfies z_1w_0=r, with the same inequalities. We glue the part epsilon/2<|z_0|<epsilon of the first neck to the zero end of middle chart zero, and epsilon/2<|w_1|<epsilon to the infinity end of middle chart one, over h. We glue the second neck to the other two ends by its coordinate projections. In any holomorphic frame of M these are explicit holomorphic maps; changing frame multiplies z and w by inverse transition units, and the first product transforms as Hom(h*M,M), exactly as phi. Thus every map is a holomorphic isomorphism on the indicated open overlap.

The norm of phi is bounded on S. Choose a parameter radius rho with rho max(1,||phi||)<epsilon²/16. The two ends of a neck cannot overlap, since |z|,|w|>epsilon/2 would contradict its product equation. The two ends attached to one middle chart are also disjoint. These bounds eliminate nontrivial chains of overlap identifications within a single neck.

For completeness, a compact fundamental cover over each closed disc |r|<=rho'<rho consists of the closed middle annuli 3epsilon/4<=|z_i|<=4/(3epsilon), and closed neck pieces |z|,|w|<=3epsilon/4. A neck point outside these smaller pieces has one coordinate >3epsilon/4 and is represented in its middle chart. Conversely a point at a boundary of a middle piece is represented in the corresponding smaller neck. On this finite union of compact bundles, the equivalence relation is the union of the diagonals and the closed graphs of the explicit coordinate identifications and their inverses. No further graph can accumulate because each neck has disjoint attaching ends. The equivalence relation is therefore closed. Its quotient is compact and Hausdorff. The open charts above identify that quotient locally with the specified analytic hypersurfaces, so this is also a proof of the Hausdorff property of the analytic gluing. Preimages of compact parameter sets are closed subsets of such compact quotients; the map is proper.

The central space has two globally distinguished components. At the first neck their ideal branches are (z_0,r) and (w_1,r). At the second neck zw=r, both corresponding ideals are Cartier. The ideal sheaf of either chosen global component is therefore coherent and agrees with (z,r) at the singular first neck. Its blowup is globally defined and proper. The chart calculations in part2_plumbing_charts.py give smooth charts except for the product node bw=xy. The small resolution of (b,x) exists on a fixed nodal neighborhood and is an isomorphism away from its singular section; hence it glues to the identity on the rest. The resulting analytic space is smooth. Its central divisor is reduced NC: in the first blowup chart r=za; in the other resolved charts r is one coordinate. These formulas also prove flatness directly by the absence of parameter torsion.

## Exact comparison of the generic cusp fan

Fix r nonzero and put u=r². The global first blowup is an isomorphism on this fibre. At the node of S_infinity, choose Tate coordinates x,y with q=xy. The unresolved compactified threefold chart is

    zw=u xy,

after a harmless multiplication of z or w by a fixed nonzero r-dependent unit. On its dense torus use character coordinates (x,z,q); then y=q/x and w=u q/z. The four affine monomials have exponent vectors

    (1,0,0), (-1,0,1), (0,1,0), (0,-1,1).

The dual cone consists exactly of (a,b,c) with 0<=a<=c and 0<=b<=c. It is the cone over the unit square at height one, with primitive rays (0,0,1),(1,0,1),(0,1,1),(1,1,1). The small resolution of (z,x), which is the restriction of (b,x) because r is a unit, subdivides that cone by a=b. Its two cones are the cones over the two unit-square triangles with main diagonal [(0,0),(1,1)]. Each determinant has absolute value one. The two resolved charts have q equal to the product of three coordinates, exactly the normal-crossing charts of the triangular Mumford fan.

The Tate period shifts a by one, and the linearization period shifts b by one; their nonzero holomorphic unit factors act by units on each affine toric chart. Therefore the translated charts constitute the Z²-periodic triangulation used in E26 Proposition 2.8. This explicitly identifies the generic compactification, including the central t=cusp fibre, with E26's X(u). We choose the nodal branch x so that its ray direction is the Tate-period direction; exchanging x and y gives the other diagonal and is an explicitly different choice of small resolution. The chosen main diagonal is the one fixed above.

The generic quotient over S minus S_infinity is exactly the inverse generator (p,z)->(h(p),z/(u phi_p)), as checked in the independent audit. Thus the toric comparison and the generic quotient identify the whole compact fibre holomorphically, not just its dense open set.

The involution (r,z_0,z_1)->(-r,z_0,-z_1) preserves both neck equations, the global component ideal and the small-resolution ideal. The finite quotient is proper and Hausdorff over u=r². Its local rings are torsion free over C{u}, and hence flat. Off u=0 the involution exchanges the two square roots of u, and the comparison on middle chart zero is the identity. Its fibre is therefore exactly one copy of X(u). This gives a proper flat filling for the original parameter u. It permits a singular and multiple central quotient fibre, which is sufficient for the requested control.

## Why the proposed one-component limit has the wrong virtual Euler number

Let Q be the space in E26 Conjecture 8.2, with normalization Y=P_S(O+M), identifying the two sections by h. Locally Q has equation xy=0, so Q is a compact lci complex space. Its double locus is S and its first-order smoothing line is L=M tensor h*M^{-1}=O_S(F). We compute its intrinsic virtual Euler number by restricting its cotangent complex to the normalization. Along one labelled branch, let a be the normal class of S in that branch and b the normal class of the other branch. A local smooth ambient hypersurface presentation gives

    c(T_Q^vir)|_Y=c(T_Y)(1+B)/(1+B+D),

where D is the branch conductor and B|_D=b, D|_D=a. The difference of its degree-three term from c3(T_Y), localized to S, is

    -c2(S)+c1(S)b-ab-b².

Adding the other branch gives -2c2(S)+c1(S)(a+b)-(a+b)². This expression is symmetric, depends only on a+b=c1(L), and therefore descends through the normalization identification. It follows that

    e_vir(Q)=e(Y)-2e(S)+integral_S[c1(S)c1(L)-c1(L)²].

Here e(Y)=24, e(S)=12, c1(S)=F and F²=0. Hence e_vir(Q)=0.

A proper flat smoothing with central fibre Q is a relative lci morphism near Q. Indeed embed a local total-space germ in a polydisc over the parameter disc. Lift a regular sequence defining Q to its ideal. The lifts generate by Nakayama after reduction modulo the parameter; flatness makes the parameter a nonzero divisor, so the lifted sequence is regular by successive reduction. The quotient by these lifts has the same special fibre and no parameter torsion; Nakayama makes the remaining kernel zero. Thus the relative cotangent complex is perfect of amplitude [-1,0] and restricts to the intrinsic cotangent complex of Q. Its virtual tangent Chern classes specialize to those of Q. The compact fibre cycles of a flat map to a disc are homologous locally over any closed parameter interval (use the local regular-sequence orientation and glue the induced oriented chains), so pairing the degree-three virtual class is constant. On a smooth fibre that pairing is its ordinary topological Euler number. Consequently every such smooth fibre has Euler number zero.

The actual X(u) has Euler number two. Over every finite t-stratum the fibrewise M-scaling circle acts freely and gives Euler number zero. Its cusp fibre is the index-one triangular Mumford surface: all positive-dimensional torus strata have Euler number zero and the two triangle strata are points. Additivity therefore gives e(X(u))=2. This contradicts the value forced by Q. Hence the central space specified in Conjecture 8.2 cannot be the central fibre of a proper flat smoothing of X(u), while the explicit two-component construction above gives the corrected existence statement.

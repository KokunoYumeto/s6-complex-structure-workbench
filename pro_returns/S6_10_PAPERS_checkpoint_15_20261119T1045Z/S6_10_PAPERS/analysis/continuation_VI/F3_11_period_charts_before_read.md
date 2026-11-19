# F3.11: actual normalized lattice-period chart and projection, before target

19 November 2026. Only root's clean statement and definitions have been supplied. Neither receiving paragraph nor F3.11's old proof/producer has been opened. The scope is precisely the local period normalization/transversality assertion and the Grassmann projection differential.

Let e1,...,e6 be the actual fixed real lattice basis of Lambda in V. The quotient pi:V_C to E=V_C/F is complex linear and surjective. Hence the six actual periods pi(e_i) span E over C: the e_i already span V_C. Since dim_C E=3, some ordered triple pi(e_i1),pi(e_i2),pi(e_i3) is a complex basis. Retain these actual indices and order the complementary three as j1,j2,j3. Let P be the integral permutation matrix whose columns are e_i1,e_i2,e_i3,e_j1,e_j2,e_j3 in the original basis. This is an actual GL6(Z) basis change; no new unmarked lattice is substituted.

Choose a local holomorphic coordinate frame for E, and write

    B=(pi(e_i1),pi(e_i2),pi(e_i3)),
    C=(pi(e_j1),pi(e_j2),pi(e_j3)),      Z=B^(-1) C.

The actual coordinate isomorphism on E is multiplication by B^(-1). In these coordinates the quotient map is

    B^(-1) pi P = [I3,Z].

Its kernel consists exactly of (-Z t,t), t in C3. Thus the actual frame for F in the permuted complexified lattice is the column matrix (-Z;I3), with the minus sign as stated. Multiplication by P returns it to the original marking. Its conjugate frame is (-bar Z;I3), since P is real. These are actual coordinate equalities, not equivalences of abstract period conventions.

Write Z=X+iY with real matrices X,Y. The restriction of this quotient map to the real marked vector space sends (x,y) in R3 plus R3 to x+Zy. Under the actual real coordinate map C3 to R3 plus R3 given by real and imaginary parts, its matrix is

    [[I3,X],[0,Y]].

Its real determinant is det Y. Its inverse, when defined, sends (u,v) to (u-X Y^(-1)v,Y^(-1)v). Thus the real quotient map is an isomorphism precisely when det Im Z is nonzero. Its real kernel is F intersect V. The exact equivalence with F plus bar F=V_C follows as well: a nonzero real vector in F lies in F intersect bar F; conversely the complex subspace F intersect bar F is conjugation-stable, so any nonzero vector in it has a nonzero real or imaginary part lying in F intersect V. Therefore F intersect V=0 exactly when F intersect bar F=0. Both complex dimensions are3, so this is precisely their direct-sum transversality.

The graph frames give the same test with its sign retained. Their combined matrix is

    K=[[-Z,-bar Z],[I3,I3]].

Left multiplication by [[I3,Z],[0,I3]] sends K to [[0,Z-bar Z],[I3,I3]]. Swapping its two blocks of rows has determinant (-1)^9=-1 and gives the upper triangular block matrix [[I3,I3],[0,Z-bar Z]]. Hence

    det K=-det(Z-bar Z)=8i det(Im Z).

This independently records the graph/minus-sign convention. The real normalized period matrix [I3,Z] and the complex kernel graph (-Z;I3) have thus been related by the exact quotient and kernel maps.

For local persistence, use the same actual lattice triple and permutation. The projected basis entries depend holomorphically on the local holomorphic plane F and quotient frame. At the chosen point det B is nonzero, so it remains nonzero on a neighbourhood; B^(-1) and Z=B^(-1)C are holomorphic there. The real-valued determinant det Im Z is continuous. Its nonzero value at the chosen transverse plane persists on a smaller open neighbourhood. Both the lattice marking and the quotient coordinate maps remain the same ones throughout that chart. No holomorphicity is claimed for Im Z itself.

For the additional projection assertion, trivialize the rank6 holomorphic bundle V over an actual base neighbourhood W in R. Split its trivial fibre as A plus B with both dimensions3. The Grassmann chart consists of the actual graph planes

    F_(t,C)={(Cv,v):v in B},       C in Hom_C(B,A), t in W.

The inverse chart takes the plane whose projection to B is invertible to its A projection composed with the inverse B projection. These maps are holomorphic and inverse. The bundle projection is exactly (t,C) to t in this chart. Restricting to the specified open U leaves an open subset of W times Mat3(C); about each point this contains a product of a base neighbourhood and a matrix neighbourhood. Its differential is the actual linear projection

    dpr_(t,C):(delta t,delta C) -> delta t,

with right inverse delta t to (delta t,0). Thus the restricted projection has the claimed local holomorphic product/submersion structure. This calculation also gives the same surjective tangent map when the base is expressed in local analytic-space coordinates; no smoothness of an unspecified base presentation is inferred. In the lattice-period chart above, this graph coordinate is C=-Z, exactly as the kernel equality shows.

The accompanying newly authored exact program checks the universal block products/sign, the actual integer permutation and B inverse on a nontrivial marked example, and the projection/right-inverse map. The derivation and computation will be frozen before either receiving paragraph is opened. This is not a whole F3.11 re-proof.

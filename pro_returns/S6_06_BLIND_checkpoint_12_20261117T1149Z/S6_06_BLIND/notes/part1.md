# Current proof status (updated 2026-11-17 01:44 UTC)

The complete current derivations are in `notes/part1.tex`, statements P1.1–P1.19. The working notes below are retained as a chronological record; their earlier provisional entries are superseded by those proofs. Current exact status and permitted stated-value comparisons are in `code/part1/results_mapping.json`. Parent-owned analytic invariants, parameter classification and endpoints are in `notes/part1_analytic.tex` and `notes/part1_endpoints.tex`.

All work owned here is complete. In particular P1.18 proves the unique global minimum of h_b at infinity by a complete certified interval cover, and P1.19 supplies the independent full global cellular calculation with its necessary nonzero cusp Ext term. The latter exports every corrected differential and all Smith change-of-basis matrices; it does not rely on the global duality argument of P1.12.

---

# Part 1: independent derivations (working record)

All calculations use column vectors. The input matrices A and B act on the supplied cohomology lattice, and M1=A^t, M2=B^t act on the homology lattice Λ=Z^6. The exterior basis of Λ²Z⁴ is (01,02,03,12,13,23). The standard rank-three cusp basis is (a1,a2,a3,b1,b2,b3), with N(bj)=aj and N(aj)=0. The chosen marking from that basis into the supplied homology lattice is

```
S = [[ 0,0,0,1,0,0],
     [ 0,1,0,0,0,0],
     [ 0,0,1,0,0,0],
     [-1,0,0,0,1,0],
     [ 1,0,0,0,0,1],
     [-1,0,0,0,0,0]].
```

Every claim below distinguishes the actual matrices from proposed geometric interpretations. The code is exact integer/rational Python/SymPy code; there are no floating-point tests in the assertions recorded here.

## P1.1 (Proved): the finite tuple and its global invariant lattices

The matrices M1 and M2 have exact orders 5 and 4. Their characteristic polynomials are (T−1)²Φ5(T) and (T−1)²(T+1)²(T²+1). For M0=(M1 M2)^−1,

```
N = M0-I = [[ 0,0,0,0,0, 0],
            [ 0,0,0,1,0,-1],
            [ 0,0,0,0,1, 1],
            [-1,0,0,0,0, 0],
            [ 1,0,0,0,0, 0],
            [-1,0,0,0,0, 0]].
```

Thus N²=0, rank N=3, and its nonzero Smith factors are 1,1,1. The displayed matrix S has determinant ±1 and S^−1 M0 S=[[I3,I3],[0,I3]], which is an independent integral certificate of all three assertions.

The common invariant subgroup in Λ is zero. Its coinvariant quotient Λ/((M1−I)Λ+(M2−I)Λ) is Z, and the quotient map is exactly ell(x)=x0. Indeed, the Hermite basis for the relation subgroup is (e1,e2,e3,e4,e5), and stacking the two fixed-vector equations has rank six. On the supplied cohomology lattice the common invariants are Ze0, whereas the coinvariants have Smith factors (1,1,1,1,1,2), hence are Z/2. This distinction is accompanied by the explicit duality pairing and computed maps: ell is a homomorphism Λ→Z, and the cohomology fixed vector e0 represents ell under Λ∨=Hom(Λ,Z).

For i=1,2 one has Mi vi=vi and ell(vi)=1,−1. Therefore the kth power of the affine map xi↦Mi xi+vi/mi is Mi^k xi+kvi/mi. Its mith power is the identity on R^6/Z^6. A fixed point of its kth power would, after applying ell:R^6/Z^6→R/Z, satisfy k ell(vi)/mi=0 in R/Z. The numbers k/5 for 1≤k≤4 and −k/4 for 1≤k≤3 are nonintegral. Every nonidentity group element therefore acts without fixed points. This proves the asserted free actions, including the order-four square.

The complete input, all matrices, powers, nullspaces and Smith outputs are in code/part1/tuple_check.py and tuple_check.out.

## P1.2 (Proved): exterior-square comparison and the integral index

Let E_f=Λ²(Cf^−1), E_g=Λ² Cg, and let Q be the supplied unimodular change of basis. Direct expansion of the two-by-two minors gives

```
Q^-1 E_f Q =
[[1,-1, 0, 1,0,0],
 [0, 1,-1,-1,1,0],
 [0, 1, 0,-1,0,0],
 [0, 2,-1,-1,0,1],
 [0, 2, 0,-1,0,0],
 [0, 1, 1,-1,0,0]],

Q^-1 E_g Q =
[[1,0, 1,0,0,0],
 [0,0,-1,0,1,0],
 [0,0,-1,0,0,1],
 [0,0,-1,0,0,0],
 [0,1,-1,0,0,0],
 [0,0,-1,1,0,0]].
```

The lower five-by-five blocks agree exactly with those of A and B. This proves the claimed identity for the quotient representations over Z.

There is an integral correction to the stronger wording in item 1.4. Put L=Λ²Z⁴, let B6:L×L→Z be the wedge pairing into the oriented generator of Λ⁴Z⁴, and put omega=(1,1,1,1,1,1)^t. Then omega²=2. The primitive lattice P=omega-perpendicular is the kernel of the row (1,−1,1,1,−1,1). The quotient lattice Q0=L/Z omega is the lower-block lattice. The natural inclusion followed by quotient, j:P→Q0, is an injective map of integral representations with cokernel Z/2.

For a full direct certificate, a basis of P and the matrix of j in the quotient basis are

```
Pbasis = [[ 1,-1,-1, 1,-1],
          [ 1, 0, 0, 0, 0],
          [ 0, 1, 0, 0, 0],
          [ 0, 0, 1, 0, 0],
          [ 0, 0, 0, 1, 0],
          [ 0, 0, 0, 0, 1]],

j = [[ 0,1,1,-1,1],
     [-1,2,1,-1,1],
     [-1,1,2,-1,1],
     [-1,1,1, 0,1],
     [-1,1,1,-1,2]].
```

The determinant of j is 2. Exact linear algebra shows that both simultaneous invariant bilinear-form spaces have dimension one. Their primitive integral forms have determinant −2 on P and −16 on Q0; each has coefficients of greatest common divisor one. An integral representation isomorphism would pull one primitive form to plus or minus the other: rational proportionality follows from the one-dimensional invariant-form space, and content one forces the proportionality factor to have absolute value one. A unimodular pullback preserves determinant, which contradicts 2≠16. Consequently these two integral representations are not isomorphic. The map j⊗Q is the requested rational identification; j exhibits its precise integral defect. Since L is unimodular and Z omega is primitive, its pairing identifies Q0 with P∨, and j is the natural inclusion P→P∨. The full rank-six input therefore has quotient the dual primitive lattice in this companion marking. The rational assertion in the prompt agrees; replacing it by an integral identification with P is false.

All pairings, primitive actions, intertwiners and dimensions are recorded in code/part1/primitive_lattice.py and primitive_lattice.out.

## P1.3 (Proved): the abelianization of the two finite caps

For each free affine quotient Ki=T⁶/<tau_i>, the covering R⁶→Ki has deck group generated by commuting x0,...,x5 and one element a_i, with relations a_i x^u a_i^−1=x^(Mi u) and a_i^mi=x^vi. These relations follow directly from the affine lifts on R⁶; conversely they reduce every word to x^u a_i^r, 0≤r<mi, so they give the full deck group. Abelianization has relation matrix with columns ((Mi−I)e_j,0), j=0,...,5, and (−vi,mi). The exact seven-by-seven matrices and Smith decompositions in tuple_check.out yield

H1(K1;Z)=Z²,    H1(K2;Z)=Z²⊕Z/2.

The local disk quotient (T⁶×D²)/<tau_i, z↦exp(2πi/mi)z> deformation retracts equivariantly onto Ki by radial contraction. Thus these are also the first homology groups of the finite filling pieces. Their free actions prove that the disk quotients are smooth; finite group quotient charts are supplied by disjoint translates of a small coordinate ball.

## P1.4 (Proved): singular points and root charts of the genus-two pencil

For f_lambda(x)=x⁵+lambda³x+lambda⁴ its discriminant is lambda^15(3125 lambda+256). At lambda_star=−256/3125 there is one double root x_star=64/625. Indeed f=f'=0 gives x=−5lambda/4; the displayed values satisfy both equations, and f''(x_star)=20 x_star³ is nonzero. The other three finite roots are simple, and the branch point at infinity of the odd-degree hyperelliptic model is smooth. Thus the reduced fibre has one ordinary node and no other singular point; its normalization has genus one. The total family is smooth at the node because partial f/partial lambda at that point is nonzero, as the exact calculation in pencil_charts.py records.

At zero use lambda=u⁸, x=u⁶X, y=u¹⁵Y. The smooth model is

Y²=X⁵+X+u².

Its central fibre is smooth because X⁵+X has distinct roots. The compactification at infinity uses the usual odd-degree hyperelliptic coordinate and is smooth there as well. The two relative holomorphic differentials have frames dX/Y and X dX/Y, and the original forms satisfy dx/y=u^−9 dX/Y and x dx/y=u^−3 X dX/Y.

At infinity use lambda=u^−5, x=u^−4X, y=u^−10Y. The smooth model is

Y²=X⁵+uX+1.

Again its central fibre has simple roots, and dx/y=u⁶ dX/Y, x dx/y=u² X dX/Y. These explicit charts prove good reduction after roots of orders eight and five. The deck maps on central curves are (X,Y)↦(iX,zeta8 Y) at zero and (X,Y)↦(zeta5^−1X,Y) at infinity. On H^{1,0} their eigenvalues are zeta8,zeta8³ and zeta5^−1,zeta5^−2. Complex conjugation supplies the other eigenvalues on H¹, proving characteristic polynomials T⁴+1 and Φ5(T) and proving that the displayed root orders are minimal. The fourth power at zero is the hyperelliptic involution, so it acts as −I on H¹ and as I on Λ²H¹.

On the root orbifold the two differential lines are genuine orbifold line bundles. Their meromorphic generators have orbifold divisors (6/5)[infinity]−(9/8)[zero] and (2/5)[infinity]−(3/8)[zero]. The same local expressions remain frames of the Hodge extension at the nodal point: a differential with nonzero numerator at the node becomes an allowed pair of simple poles of opposite residues on the normalization, and the independent linear combination vanishing at the node is a regular genus-one differential. Hence neither line has a zero or a pole as a section of the extended Hodge bundle there. The relative forms remain independent, so they split the rank-two bundle. Writing T for the second line gives H=T³⊕T and deg(T)=1/40, deg(T³)=3/40.

The above local calculations establish the local conjugacy spectra. Proposition P1.7 below completes the global integral monodromy comparison using the rank-one local transformation and its primitive vanishing cycle; it is not inferred merely from the spectra.

## P1.5 (Proved): literal rank obstruction in the displayed period formula

In the wording of the prompt H is the rank-two Hodge bundle, ell0 is its rank-one subbundle, and P is the image of ell0 wedge H. At every point, the linear map ell0 tensor H→Λ²H has kernel ell0 tensor ell0 and image of dimension one. Projection into W cannot increase the dimension. A splitting sigma:P→V has rank at most one, and adding the linear map i c alpha e:P→V does not change that bound. Therefore the displayed formula cannot produce a rank-three F with that stated meaning of H.

There is a precise comparison that supplies the intended rank-three object. Let H_dR be the rank-four flat cohomology bundle. The map ell0 tensor(H_dR/ell0)→Λ²H_dR is an injective holomorphic map with image ell0 wedge H_dR, of rank three. Its intersection with the invariant line C omega is zero: every nonzero element of ell0 wedge H_dR is decomposable, hence has square zero in Λ⁴H_dR, whereas omega²≠0. Projection to W therefore restricts to an isomorphism onto a rank-three subbundle. This is the repaired P. The comparison does not itself construct a holomorphic lift in the supplied rank-six extension or prove global real transversality.

## P1.6 (Known, with derivation): absorption of the exotic eight-sphere by the named target

Theorem A of Kramer--Stolz, *A diffeomorphism classification of manifolds which are like projective planes*, J. Differential Geometry 77 (2007), 177--188, is open and verified at https://archive.ymsc.tsinghua.edu.cn/pacm_download/21/694-JDG-77-2-A1-kramer.pdf. It states that a smooth simply connected manifold of dimension 2m≠4 with integral homology Z⊕Z⊕Z absorbs every homotopy 2m-sphere by connected sum. Apply it to HP², whose cells in dimensions 0,4,8 verify the homology and connectivity hypotheses. The resulting diffeomorphism HP²#Sigma8→HP² preserves orientation: the signature of the source and target is +1, whereas reversing orientation would change its sign. Form its oriented connected sum with the identity of 2HP²#(−HP²), using coordinate disks. Associativity of oriented connected sum gives an orientation-preserving diffeomorphism

(3HP²#(−HP²))#Sigma8 → 3HP²#(−HP²).

Thus the two alternatives named in 1.6 represent the same oriented diffeomorphism class. This is a proved relation between the two candidates. Identification of the constructed M with that class still needs its characteristic pair; it does not follow from this absorption argument alone.

## Geometric and topological computation under development

The periodic Freudenthal triangulation has 1 vertex, 7 edges, 12 triangles and 6 tetrahedra modulo Z³. For a simplex sigma of dimension p, its toric stratum has complex dimension 3−p. Each of the 6 maximal simplices has normalized volume one, and its cone generators (v0,1),...,(v3,1) form a Z-basis of Z⁴. The corresponding chart is C⁴ and the parameter is the product of its four coordinates. This proves smoothness and reduced normal crossings in each chart. The toric overlaps are the monomial coordinate changes coming from the common faces of these cones. Translation by lambda∈Z³ sends (v,n) to (v+n lambda,n), preserves the fan, and induces z↦t^lambda z on the open torus. No nontrivial translation stabilizes a bounded simplex, so the action is free on every central toric stratum. The quotient central fibre has the 26 stated strata. Euler characteristic with compact supports is additive over the finite stratification, and χ_c((C*)^j)=0 for j>0, so the central Euler number is six. Quotient by an index-d period sublattice multiplies the number of translation classes of every simplex by d and gives Euler number 6d. Properness of the analytic quotient and the explicit global collapse still require their full gluing argument.

The orbit-filtration complex is built from quotient lattices Q_sigma=Z³/span_Z(sigma−sigma). Its term at (p,q) is a direct sum over p-simplices of Λ^q Q_sigma. The differential is the signed sum of the quotient maps over codimension-one face inclusions. Every quotient projection, every right inverse, all 74 codimension-one incidences, and every matrix are in cusp_complex.json. Smith decompositions yield free E2 groups and total Betti vector (1,3,9,9,10,3,1). The canonical quotient maps from a constant Z³ fibre give the exact collapse matrices in cusp_collapse.json; the marked version in cusp_marked_collapse.json is invariant under [[I,I],[0,I]] and has primitive image, with a free cokernel of rank one only in degree four.

The intended geometric model is the moment-map quotient over the dual cell decomposition of T³: over the dual cell to sigma the angular torus is (Z³/span sigma) tensor R/Z. Its orbit filtration gives the preceding integer complex. The fibre identity section splits the base T³. Dimensional support leaves only one possible higher differential, from base degree three/fibre degree zero to base degree one/fibre degree one; the section kills it. This gives a route from the matrix computation to the actual central homology. A full comparison map from the toric quotient, with all self-identifications, remains to be written before promoting the matrix computation to a completed proof.

The global Mayer--Vietoris candidate uses the two finite-cap mapping tori of the five-dimensional kernels of ell. Boundary maps use the exact cyclic norm sums. The cusp fibre map uses the above marked collapse, and its boundary suspension term is set to zero. The resulting chain matrices have sizes

C0=4, C1=26, C2=87, C3=162, C4=200, C5=156, C6=79, C7=23, C8=3.

All consecutive products vanish exactly; Smith homology is free with Betti vector (1,0,0,0,4,0,0,0,1). The complete program and all matrices are global_candidate_complex.py/.json/.out. This is currently a diagnostic chain model. The unresolved geometric step is the proof that the actual cusp-boundary suspension map is represented by zero in the chosen markings. Choosing it to make the asserted answer true would be invalid; the computation is therefore not labelled a proof of the global manifold's homology.

The fundamental-group presentation associated to the zero cusp closing section has generators x in Λ and a1,a2, relations [x,x']=1, a_i x a_i^−1=Mi x, a_i^mi=vi, and a1 a2=1. The cusp also kills im N, already implied by the last relation and the conjugation relations. Since a2=a1^−1, the actions of M1 and M2 are inverses on the fibre quotient. Their orders divide 5 and 4, hence the action is trivial. The fibre quotient is Z via ell, and the presentation becomes the abelian three-generator presentation with relation matrix [[5,0,−1],[0,4,1],[1,1,0]], determinant −1. This proves triviality for that fully marked gluing. Derivation of the zero closing section from the requested cusp marking is the same geometric issue just identified.

No period subbundle, global complex fourfold, Hodge numbers, automorphism groups, tangent cohomology, or c-family limit is asserted from these matrix computations.


## P1.7 (Proved, using verified Levelt theorem): global integral monodromy of the pencil

Put z=lambda/lambda_star and take the base point z=1/2. Choose positively oriented based meridians g_infinity,g_1,g_0 with g_infinity g_1 g_0=1, the convention in Beukers--Heckman, Definition 3.1. Let H_infinity,H_1,H_0 be their actions on H¹(C;Z). The local root charts give characteristic polynomials Phi5 and T⁴+1 for H_infinity and H_0^−1. Their sets of eigenvalues are disjoint. The local nodal equation xy=z−1 gives H_1−I of rank one. To see its integral coefficient, cut the nearby oriented surface along its vanishing simple closed curve delta, insert the annulus xy=z−1, and turn its parameter positively once. A transversal crossing the annulus acquires one copy of delta; all curves disjoint from it remain fixed. This proves the Picard--Lefschetz formula H_1(x)=x+epsilon <x,delta> delta, with epsilon=±1 depending on whether cohomology or homology and the pairing order is used. The normalization has genus one, so delta is nonseparating and has an integral transverse curve of intersection one. In particular delta is primitive.

The hypotheses of Beukers--Heckman, Theorem 3.5 (Levelt), Inventiones Mathematicae 95 (1989), 325--354, pp.331--332, are now verified. The theorem identifies the triple over C with (Cf,Cf^−1 Cg,Cg^−1). Its proof works over Q here: with A=H_infinity and B=H_0^−1, the intersection of ker(B−A), A^−1 ker(B−A), and A^−2 ker(B−A) contains a nonzero rational vector v. Irreducibility follows because a common nonzero proper invariant subspace or its quotient is fixed by the rank-one transformation, forcing an eigenvalue shared by A and B. Thus v,Av,A²v,A³v are independent, and in this rational basis A and B are the two companion matrices. This proves a rational intertwiner, with its field of definition verified.

We now prove that the actual integral lattices agree. In the companion lattice put d=(1,1,1,0)^t and

```
J = [[ 0,-1, 1,-1],
     [ 1, 0,-1, 1],
     [-1, 1, 0,-1],
     [ 1,-1, 1, 0]].
```

The exact identities Cf^t J Cf=J, Cg^t J Cg=J, det J=1 and Cf^−1 Cg=I−d(d^t J) are checked by the code. The orbit d,Cf d,Cf²d,Cf³d has pairing matrix

```
[[0,-1,0,0],
 [1,0,-1,0],
 [0,1,0,-1],
 [0,0,1,0]],
```

of determinant one. Under a rational intertwiner, d maps to a nonzero rational multiple a delta. The invariant alternating forms are one-dimensional, by solving the two linear invariance equations (the coefficient matrix has nullity one). Write the pulled-back integral intersection form as cJ. Comparing the two rank-one transvection formulas gives c/a²=±1. Consequently the four actual integral cycles delta,H_infinity delta,H_infinity²delta,H_infinity³delta have exactly the displayed unimodular pairing matrix, with an overall sign. A full-rank sublattice with determinant-one intersection form has index one in the unimodular H¹ lattice, because its determinant equals the square of that index. The rational intertwiner therefore becomes integral after scaling by a. This proves the integral companion marking.

Finally the reversal matrix R with ones on its antidiagonal is unimodular and satisfies R Cf R^−1=Cf^−1 and R Cg^−1 R^−1=Cg. Thus the two finite monodromies in the convention of the prompt are exactly Cf^−1 and Cg, and the nodal monodromy is Cf Cg^−1=(Cg Cf^−1)^−1. Its primitive exterior-square quotient has the lower blocks of A,B by P1.2. The cohomological cusp product is (BA)^−1, whose transpose is the supplied homological M0. This checks the order of products as well as the local spectra.

The source was opened at https://math.uchicago.edu/~drinfeld/Hypergeometric_motives/Beukers-Heckman.pdf. The preceding rational comparison derives the needed form of the result from its numbered theorem, and the integral upgrade is proved here. Exact model matrices are in companion_markings.py/.out. No unseen source about the present fourfold is used.

## P1.8 (Proved): a global transverse lift after repairing the rank-three definition

Let B_tilde be the root orbifold of P¹_lambda with orders five at infinity and eight at zero; leave lambda_star as an ordinary point. All bundles in this paragraph are holomorphic orbifold bundles. Let H_dR be the canonical logarithmic extension of H¹ of the genus-two pencil at lambda_star, after making the two finite monodromies trivial on their root charts. Its Hodge subbundle is H=T³⊕T by P1.4. The symplectic pairing gives the exact sequence H→H_dR→H∨, with H as kernel: pointwise this is the Lagrangian property of the two-dimensional Hodge subspace, and at the nodal point it follows in the plumbing chart from the nonzero residue pairing. Let ell0=T³. Define P to be the image of ell0 wedge H_dR in W=(Λ²H_dR)/O omega. The injectivity proved in P1.5 gives

0 → T⁴ → P → O⊕T² → 0.

The maps are wedge product, passage to the symplectic quotient, and the projection H_dR/ell0→H∨. Contraction with omega defines alpha:P→O; its kernel K has factors T⁴ and T². This alpha is surjective, including at the nodal point, because the symplectic form is nondegenerate and ell0 is a nonzero line.

Here the orbifold line T has rational divisor (2/5)[infinity]−(3/8)[zero]. For each a=2,4,−2,−4 the invariant direct image of T^a to the coarse P¹ has degree −1, as one sees by taking the floors of the two coefficients. For a=0 its degree is zero. Taking invariants of a finite stabilizer is exact over C: the average of its elements is a projection to invariants. Hence orbifold H^j(T^a) equals H^j(P¹,O(−1)) for these four exponents. These H⁰ and H¹ vanish. This last assertion has the direct two-chart proof by splitting a Laurent series on C* into its nonnegative and negative powers; degree −1 leaves no missing power in the Cech coboundary map. The same argument gives H¹(O)=0 and H⁰(O)=C.

The extension above splits because Ext¹(O,T⁴)=H¹(T⁴)=0 and Ext¹(T²,T⁴)=H¹(T²)=0. Thus P≅T⁴⊕T²⊕O. In particular

H¹(P∨)=0,   H⁰(P∨)=C alpha,   H⁰(P)=C g,

where g is uniquely normalized by alpha(g)=1.

The given integral rank-six representation defines V on the punctured base by flat transition matrices. Its local logarithmic extension at the cusp has frame exp(−sNv) times a flat frame, s=log q/(2πi), Nv=(BA)^−1−I. On the finite root charts it is the trivial extension with the finite deck action. These charts give an exact bundle sequence 0→Oe→V→W→0. Exactness at the cusp follows directly from the compatible nilpotent exponential frames; exactness on the finite charts follows from averaging a splitting of finite representations. The pullback of this extension along P→W splits because H¹(P∨)=0. Fix a holomorphic splitting sigma:P→V. Two such splittings differ by z alpha e for a unique z∈C. This is a proved comparison map between all choices. One may fix the remaining scalar by requiring the e-coordinate of sigma(g) to vanish in the fixed flat frame at z_base=1/2.

On a smooth curve fibre choose a generator u of ell0. Put r=i·projection(u wedge bar(u)) in W_R and A=alpha(r). The polarization gives A>0. To verify the intersection of the two three-planes, use the symplectic decomposition H_dR,C=span(u,bar(u))⊕K0, where K0 is the symplectic orthogonal plane. An equality u wedge v−bar(u) wedge w=t omega has zero Λ²K0 component on the left and a nonzero such component on the right, so t=0. The remaining equality lies in the one-dimensional span of u wedge bar(u). Consequently P∩bar(P)=C r.

Since r is real, sigma(r)−overline(sigma(r)) is a pure imaginary multiple of e. Define the real function h by

sigma(r)−overline(sigma(r)) = 2i A h e.

Both numerator and denominator multiply by |a|² when u is multiplied by a, so h is well defined on the base. It is real analytic on the smooth base, continuous on the two finite root charts, and invariant under their deck groups. For real c set F_c=(sigma+i c alpha e)(P). Its projection to P is an isomorphism. A vector in F_c∩bar(F_c) projects to a multiple of r; comparing its two unique lifts gives 2i A(h+c)e. Therefore F_c∩bar(F_c)=0 exactly at points with h+c≠0. This derives the transversality test, including its scalar and the real line used in it.

We compute the cusp growth from the actual matrices, rather than posit its sign. In the companion marking, put D=Cf Cg^−1−I. Its only nonzero column is D e0=(0,1,1,1)^t. In the rank-six cohomology marking, Nv=(BA)^−1−I has first row (0,0,0,−1,1,−1). For a,b∈C⁴, let pi(a wedge Db) be its lower five coordinates after Q^−1. The exact identity

(Nv)_{0,*}(0,pi(a wedge Db)) = contraction(a wedge Db)=a0 b0

is verified symbolically for arbitrary a,b in cusp_lift_asymptotic.py. Also Nw pi(a wedge Db)=0.

Write the Hodge line in a flat frame as u=exp(sD)a(q), where a is holomorphic at q=0. The nodal differential dx/y has nonzero residue, so a0(0)≠0. Put y=Im(s), k=|a0(q)|². In the logarithmic frame,

exp(−sNw)r = i pi(a wedge bar(a)) + 2y pi(a wedge D bar(a)),

and A=i·contraction(a wedge bar(a))+2yk. The logarithmic splitting sigma is bounded. When we return its lift to a flat frame by exp(sNv), the only term of quadratic order in y in the imaginary e-coordinate is 2ky²e, by the displayed matrix identity. All other terms are O(y), uniformly for Re(s) in a fixed interval of length one. Therefore

h(q)=y+O(1)=−log|q|/(2π)+O(1).

In particular h tends to +infinity at the cusp. On B_tilde minus that point it has a finite attained minimum h_min. The base is connected, and along a path from a minimum point toward the cusp h takes every value in [h_min,infinity). Hence the exact transversality domain for real c, with this splitting, is c>−h_min. It is nonempty. Changing sigma by i b alpha e replaces h by h+b and takes the family F_c to F_{c+b}; this is the precise parameter translation relating splitting choices. The number h_min has not been numerically evaluated here.

The fourfold periods have the asserted bounded cusp form. At q=0, the map Nv:F_log→ker Nv is an isomorphism. Indeed Nw has rank two on P_0, with kernel spanned by pi(a wedge Da); the displayed scalar identity maps its lift to the nonzero vector a0²e. Thus Nv has rank three on the lifted three-plane. In an integral Jordan basis with Nv b_j=a_j, the projection of F_log to V/ker Nv is invertible, so F_log is the graph of a holomorphic matrix C(q). Multiplication by exp(sNv) replaces C(q) by sI3+C(q). The matrix is bounded at zero. This proves the form Z=sI3+C(q), with no assumed positivity or symmetry of C.

At the zero root chart the fourth power of the order-eight deck action is identity on W and V, hence on the whole constructed graph. The graph therefore descends to the order-four chart. At infinity it is compatible with the order-five action. Both finite affine maps are holomorphic for these tori, because their linear parts preserve F and their translation parts act holomorphically on every complex torus.

This proves existence of a global holomorphic transverse rank-three bundle for an entire real half-line of parameters, and it proves its finite-chart and cusp behaviour. It uses the repaired full de Rham bundle in P. It does not furnish the requested thirty-digit evaluations or an evaluated value of h_min.

## P1.9 (Proved): toric local charts, quotient, properness, and Euler number

Fix the integral Jordan marking S stated at the beginning. Let Sigma be the fan in R³×R formed by the cones over every simplex of the Z³-periodic Kuhn triangulation at height one and their faces. For a maximal simplex with ordered vertices v0,...,v3, the matrix whose columns are (vj,1) has determinant ±1. Let u0,...,u3 be the dual integral basis. The associated affine chart has coordinates xj=chi^{uj} and is C⁴. The height character is the sum of the uj, so q=x0 x1 x2 x3. For a common face, invert the coordinates of the omitted rays and use the change of dual bases; this gives an explicit monomial holomorphic overlap map. Its inverse is the inverse unimodular monomial map. These overlaps construct the smooth toric space Z_Sigma with its map q to C. They show directly that the zero fibre is reduced and has normal crossings, including the four-branch points corresponding to tetrahedra.

For a bounded holomorphic matrix C(q), the period lattice acts on the open torus by

(z,q) ↦ (q^lambda exp(2πi C(q)lambda) z,q),   lambda∈Z³.

The monomial part carries the cone over a simplex sigma to that over sigma+lambda. The exponential part is a nowhere-zero torus element holomorphic in q; torus multiplication extends over every toric chart. The formula therefore defines holomorphic maps of the whole toric space over a sufficiently small disc. They compose according to addition in Z³ and preserve q. The action is free at q=0 because no nonzero translation stabilizes a bounded simplex, and a point fixed by a toric automorphism must have its orbit cone stabilized. Off zero, the real-linear period map has imaginary part Im(s)I+Im(C(q)); it is invertible for small |q|, so the action has no nontrivial fixed point there either.

Here is a direct local-finiteness and properness check for this infinite-chart quotient. For q≠0 put u=log|z|/log|q| in R³. Translation changes u by (I+E(q))lambda, where E(q) is uniformly O(1/|log|q||). On a sufficiently small disc the operator norms of E and of (I+E)^−1 are bounded and the latter is uniformly at most two. Thus every orbit has a representative with u in a fixed bounded subset of R³, by reducing (I+E)^−1u modulo Z³. That bounded set meets finitely many maximal simplices. On the chart for a simplex containing u, the valuations of x0,...,x3 are its barycentric coordinates times log|q|, hence |xj|≤1. The representatives are therefore contained in finitely many closed unit polydiscs with q=x0x1x2x3. These compact sets also contain all their limits at q=0, and the toric coordinate description shows that the central quotient has no other points: every central orbit is represented in one of the finitely many stars of lattice vertices meeting the bounded set. Hence the inverse image of a smaller closed base disc is compact in the quotient.

For Hausdorffness and proper discontinuity, take two compact coordinate neighborhoods in the infinite-chart space. Their central strata meet finitely many cones. A translate carrying one central neighborhood to the other must translate these finite sets of bounded simplices to intersecting sets, allowing finitely many lambda. Off a smaller neighborhood of q=0 the usual discrete lattice action is proper. In a sequence approaching zero, the bounded valuation sets above and the uniform inverse bound on I+E force lambda to remain bounded. Thus only finitely many translates of the two compact neighborhoods meet. The quotient is Hausdorff, the free action supplies manifold charts, and the compact inverse-image argument proves properness. Since q is a nonzero divisor on each smooth chart, the map to the one-dimensional disc is flat. Its nonzero fibres are exactly C³/(Z³+Z(q)Z³) by the exponential coordinate map z_j=exp(2πi zeta_j).

A p-simplex gives a stratum (C*)^{3−p}. Modulo the period lattice the stratum counts are (1,7,12,6). Additivity of compactly supported Euler characteristic and χ_c((C*)^j)=0 for j>0 give Euler number six. Replacing Z³ by an index-d sublattice in the deck action creates d translation classes above each old class and gives Euler number 6d. This proves the stated index dependence, with the comparison map the finite covering of toric quotients induced by inclusion of period sublattices.

## P1.10 (Proved): the global holomorphic gluing and its fundamental group

The transverse bundle F_c defines the holomorphic torus family over the nonspecial base by evaluation: a vector lambda∈Λ maps to the functional omega↦<lambda,omega> on F_c. Transversality says that the real-linear evaluation Λ_R→F_c∨ is an isomorphism, so Λ embeds as a discrete full lattice. Quotienting the local holomorphic vector bundle by these holomorphic period sections gives the required three-torus bundle. The period transitions are the given integral monodromies.

On a finite root disc u^mi=t_i, take the pullback torus family and divide by (x,u)↦(Mi x+vi/mi,exp(2πi/mi)u). The affine freeness in P1.1 proves smoothness of the quotient, including u=0. Its special fibre is mi times its reduced free torus quotient. Over the punctured disc, the map to the original family is translation by minus (log u/(2πi)) times the period of vi. Changing log u by 2πi changes the translation by a lattice vector, and changing u by exp(2πi/mi) produces exactly vi/mi. Hence this is a well-defined holomorphic gluing isomorphism. At the cusp use the toric quotient of P1.9 and the period identification furnished by P1.8. Its zero section on the punctured disc, zeta=0, extends to the dense torus of the central component represented by the lattice vertex zero.

The maps glue holomorphically to P¹, and compactness follows from a finite closed cover of the base by compact interiors of the three local proper pieces and the compact torus bundle over the remaining compact surface with boundary. All charts have been specified above; the overlaps on the finite collars are the logarithmic translations just given, and those on the cusp collar are the exponential period map. The total space is therefore a compact smooth complex fourfold for every c>−h_min. It has exactly the two multiple fibres and the stated rank-three toric cusp.

We fix positive based meridians g1,g2,g0 with g1g2g0=1 on the base pair of pants. The torus bundle there has its zero section, so its fundamental group is Λ semidirect the free group on g1,g2. Gluing the finite pieces gives the relations g_i^mi=vi and conjugation by g_i equal to Mi; the logarithmic gluing formula above proves their signs. The cusp zero section contracts g0. Its vanishing cycles kill im N. The latter relations also follow from g1g2=1 and the conjugation actions, but recording them checks the cusp explicitly. The remaining group is computed in the paragraph preceding P1.7: the coprime orders force both actions to be trivial, the fibre coinvariants are Z through ell, and the relation matrix has determinant −1. Therefore the fundamental group of this specified gluing is trivial. Euler additivity gives χ=6, since the two finite fibres are free torus quotients and the smooth fibres have Euler number zero.

# The OS50 quadratic I1* cap: source maps, line lift and integral topology

Working status after Part4 closure. This note records exact source calculations and the remaining marking calculation; no sphere tuple is declared before that marking is complete.

## Actual affine source norm

On the quadratic semistable root the Tate period and generator have representatives

    q_T=z²u(z²),  Z_G=zv(z),  v(z)v(−z)=−u(z²).

For b≡2 mod4 choose the component-zero representative

    Z_Q=v(z)^b/u(z²)^(b/2).

It satisfies Z_Q(−z)=Z_Q(z)^−1 and Z_Q(0)=−1. The canonical deck is inversion on the Tate coordinate combined with z↦−z.

There is a particularly direct actual source solution. The pullback section G is equivariant for this deck, so translation by R=(nb/2)G commutes with it. For every odd n, the integer nb/2 is odd. Thus

    A_source=T_R D,  B_source=T_{bG},
    A_source²=B_source^n,  [A_source,B_source]=1.

Its component action on I2 is j↦−j+1, hence is transitive. This uses an actual integer multiple of the marked section, rather than only a component congruence. In a single Tate representative, the output translation is evaluated at the output root coordinate: A(Z,z)=(Z_R(−z)/Z,−z).

An equivalent local solution, without choosing a global section representative, is A(Z,z)=(R(z)/Z,−z), R=z w(z), where

    w(−z)/w(z)=−Z_Q(z)^n.

The right side has value1 and reciprocal values under z↦−z. Its analytic logarithm is odd; taking minus half of that logarithm constructs w. The convention for the two R representatives is related by inversion/output evaluation and must be retained when writing the boundary marking.

## The degree-zero root line and its torsion character

For even a, the generic root Picard point is represented by

    Z_P=v(z)^a/u(z²)^(a/2),
    Z_P(−z)=Z_P(z)^−1,  Z_P(0)=(-1)^(a/2).

For the surviving a=2,6, this central value is −1. On the Tate cover the degree-zero line has automorphy

    (Z,lambda) ~ (q_T Z,Z_P lambda).

Because Z_P is a nonvanishing holomorphic unit, these transitions extend as unit transitions across the two-component Tate model. They have degree zero on each component. The deck (Z,lambda,z)↦(1/Z,lambda,−z) respects this relation exactly. A translation lift acts by a scalar on lambda in this frame. The actual suspension multiplier is a holomorphic unit times the small scalar parameter, and its equivariance makes that unit even. Taking an analytic square root gives an actual line lift with A²=B^n. The integral choice of its square-root phase is retained in the universal circle cover as a delta exponent.

This root line is compared with the actual corrected source line O(aG−O−L0) on the punctured neighbourhood. An explicit vertical comparison on the resolved quadratic correspondence is still being written; it cannot be replaced by a bare pullback to the minimal root, because the pullback has nonzero degree on the exceptional curves over the four inversion fixed points.

The central source curve I2 has H1=Z eta and H2=Z². Its affine reflection reverses eta and exchanges the two components. The orbit cap is its actual mapping torus. Its fundamental group is the Klein-bottle group

    <h,eta | h eta h^−1=eta^−1>,

and H1=Z h⊕Z/2 eta, H2=Z, H3=Z. The circle line retains a nontrivial torsion Euler class. In the Tate logarithm frame the inversion of the graph period gives the central extension

    h eta h^−1=eta^−1 delta^k,  k=a/2 mod2.

Here k is odd, so the abelianization relation 2eta=k delta is primitive. This parity is fixed by Z_P(0)=−1. The exact integral delta representative depends on the retained collar frame and is not dropped.

## Boundary marking warning and a consistent group model

The suspension boundary generator cannot simply be sent to h². The original source monodromy and the section Q have a nontrivial affine cross relation. Choose elliptic generators u,w and the source meridian alpha so that

    alpha u alpha^−1=u^−1,
    alpha w alpha^−1=w^−1 u^−1,
    alpha gamma alpha^−1=gamma w^b,
    [gamma,u]=[gamma,w]=[u,w]=1.

The last relation represents the actual component class of bG; changing a source origin changes its vector by (M−I) times an integral vector. In this gauge a consistent map to the orbit-cap group is

    u↦1,  w↦eta,  gamma↦h² eta^(−b/2),  alpha↦h^n eta^c.

The integer c can be changed by the choice of a fixed-node path and of h. Its exact marked value is still to be derived from the outer Tate collar. This model explains why sending gamma to h² alone would fail the affine commutator relation. It is not yet being used as a certified complete boundary map.

## The source complement matrix for I1*+I3+2I1, b=2

Remove a small I1* fibre neighbourhood from the rational elliptic source. Its component lattice is primitive, and the complement P has H1=0 and H2 of rank4. The quotient H2(S)/<I1* components> has basis (O,G,C1,C2). In this basis translation by 2G has matrix

    T=[[-1,-2,0,0],
       [ 2, 3,0,0],
       [ 1, 2,-1,1],
       [ 0, 1,-1,0]].

The actual H2(P) action is its inverse transpose U. The executed exact calculation gives

    Smith(T−I)=(1,1,2,0),
    ker(U−I)=Z(1,1,0,0),
    coker(U−I)=Z⊕Z/2.

The primitive source fibre F=(1,1,0,0) represents the nonzero order-two class in that cokernel: its rational preimage is (t+1/2,t,0,0), whereas 2F has an integral preimage. This torsion is essential in the orbit Mayer–Vietoris map. It is not an obstruction by itself: the boundary has a matching order-two class.

The expected boundary four-manifold is the mapping torus of T3 with matrix

    M3=[[-1,-1,0],[0,-1,b],[0,0,1]]

in the ordered fibre basis (u,w,gamma). Its H1 and H2 each have a Z/2 torsion summand for b≡2 mod4. The source fibre maps to twice the component-orbit generator in H2 of the I2 reflection cap. Completing the exact boundary identification and its map to the source complement is the current remaining step.

## Exact resolved-root comparison of the actual line

Let S' be the minimal quadratic semistable root, with fibre I2. The canonical deck D is inversion on the Tate fibre combined with z↦−z. Its four fixed points are smooth points of the two central components. Let beta:Shat→S' blow up these four points. The lifted deck fixes the four exceptional curves, and its quotient pi:Shat→S is the smooth I1* source. Label E0,E1 the exceptional curves above the leaves L0,L1 met by O and P=aG; for a=2 or6, P meets L1. Each E_i has square −1 and pi*L_i=2E_i. The strict transforms of the two root sections are Ohat,Phat. Consequently, as actual Cartier divisors,

    pi*(P−O−L0)=Phat−Ohat−2E0,
    beta*(P'−O')=Phat−Ohat+E1−E0,
    beta*N=pi*M+E0+E1,    N=O(P'−O').

The last identity is the required exact comparison. The divisor E0+E1 is invariant under translation by Q=bG for b≡2 mod4, which swaps these two points and also swaps the other two exceptional curves. Thus the comparison transports the actual suspension Hom-line and its specified lift; no unrecorded vertical correction remains. The sections P' and O' meet the same root component, so N has degree zero on both I2 components. In the Tate frame its actual Picard character is the unit Z_P displayed above, with value −1 at z=0.

For completeness, a deck character in the line lift must be retained. Let F be a line lift of translation by G on N and let D also denote the canonical order-two line lift. The Tate unit transitions produce F directly, and every other such lift differs by a base unit. Write D F D^−1=c(z)F, where c(z)c(−z)=1. After multiplying F by a base unit, an odd logarithm makes c the constant chi=c(0)∈{1,−1}. The actual suspension lift has the form B=beta(z)F^b. Its descent and the even integer b imply beta(−z)=beta(z). For k=nb/2, set

    A=chi^(−k/2) beta(z)^(n/2) F^k D.

Choose the analytic square roots of the even nonvanishing units, retaining their integer phase in the outer collar. Then the equalities AB=BA and A²=B^n hold as actual maps of N^×, including the factor chi^k in (F^kD)². The affine source action exchanges the two central components. For odd n, integers r,s with rn+2s=1 give the actual generator H=A^rB^s; its fibre multiplier is a bounded unit times the square root of the small suspension scalar. It is uniformly contracting after shrinking the parameter disc. A positive iterate cannot fix a nonzero line vector by the norm inequality; negative iterates are expansive. Thus the quotient is free and proper. This is the same explicit norm-shell compactness argument as P3K.15, now with the displayed line comparison.

## Full integral source-boundary chain calculation

The complement P of the I1* tube is simply connected. The elliptic fibration over the complementary disc, with its section, presents its fundamental group as the elliptic lattice modulo the remaining vanishing cycles; this group is abelian. The primitive fibre-component lattice in the unimodular rational-source lattice gives H1(P)=0, hence this presentation is trivial. The long exact sequence gives H2(P)=Z4 and no other positive reduced homology. The source Néron–Severi basis used in the certificate is

    (O,F,C0,C1,L1,R0,R1,A2_1,A2_2,G).

Its Gram determinant is −1. The dual columns with indices (O,G,A2_1,A2_2) give the actual complement lattice, with intersection matrix

    J=[[-12,12,8,4],[12,-12,-8,-4],[8,-8,-6,-3],[4,-4,-3,-2]].

Writing U=T^(−transpose), we have J U=T J. The source boundary complex is C3=Z,C2=Z4,C1=Z4,C0=Z with sole differential d2=J. This description and its equivariance follow directly from the Poincaré–Lefschetz triangle C(boundary P)→C(P)→C(P,boundary P): the latter two complexes split over Z because all their homology is free, and the only nonzero homology map is the displayed intersection pairing. There is no degree-minus-one map between these split complexes that could supply an omitted homotopy term. Translation acts by U on absolute H2 and T on its relative dual. Taking the actual mapping-torus cone therefore gives all boundary and inclusion matrices printed in `code/part3/i1star_boundary.json`.

In the certificate's integral H2 bases, let (epsilon,r,s) denote the boundary generators, with 2epsilon=0, and (tau,g) the exterior generators, with 2tau=0. The inclusion and source-fibre classes are exactly

    i2=[[1,0,−2],[0,0,1]],
    F_boundary=epsilon−2r,   F_exterior=tau.

The actual inversion (p,t)↦(−p,−t) has boundary action

    epsilon↦epsilon,  r↦r,  s↦−s−2epsilon.

On the I2 reflection cap, H2=Z C and the sum of the two central component classes is 2C. The source-boundary inversion just computed is not used to identify the marked cap column: it can change that cap marking by a gamma shear. Instead, the actual fibre identity F_boundary=epsilon−2r and F_cap=2C gives

    epsilon↦0,  r↦−C,  s↦kappa C,

where kappa is the actual integral cap coefficient. In target order (tau,g,C), with the Mayer–Vietoris sign on the cap row, the full map is

    [[1,0,−2],[0,0,1],[0,1,−kappa]].

The first source and target generators both have order two; their map is the identity. The free block has determinant −1 for every integer kappa. Equivalently the actual integral boundary basis change s_new=s+kappa r, of determinant one, makes the cap column zero while preserving its exterior column. Thus the full H2 Mayer–Vietoris map is an isomorphism of finitely generated abelian groups, with all torsion retained. No value of kappa is inferred from the source-boundary inversion.

The first exploratory run used the wrong order in the chain-cone inversion factor −Tminus*T^−1 and failed its chain identity. The corrected factor is −T^−1*Tminus (and likewise −U^−1*Uminus in degree three). The executed code checks both chain identities before exporting any result.

## Final degree-one/three maps to complete

In a source boundary gauge (u,w,alpha,gamma), the affine source relation is alpha gamma alpha^−1=gamma w^b. The cap map must therefore retain gamma↦h² eta^(−b/2), not merely h². Its free first-homology columns (alpha,gamma) are (n,2); the remaining source loop w maps to the nonzero order-two class eta, and u maps to zero. Together with the exterior row (0,1), the free gluing determinant is n. The top source-fibre trace gives the same columns (n,2) in degree three, while the exterior trace row is (0,1). These geometric columns still need the complete marked collar derivation before the one-cap n=±1 sphere assertion is promoted. Extra smooth caps and the I1*+IV source are not yet included in this note's topology calculation.

## One-cap topology: completed calculation awaiting independent audit

For the explicitly constructed affine cap, the remaining first/third-homology calculation does not require choosing the integer c above to be zero. We retain it. On boundary H1 use the generators (epsilon,alpha,gamma), with 2epsilon=0; on cap H1 use (eta,h), with 2eta=0. The exact map is

    epsilon↦eta, alpha↦n h+c eta, gamma↦2h−(b/2)eta.

The elliptic vanishing cycle u maps to zero, and the primitive graph period w maps to eta. The coefficient n is the actual identity A=H^n from P3K.15, while B=H² gives the gamma coefficient2. The affine commutator forces the retained −b/2 graph correction. The exterior sends alpha and epsilon to zero and gamma to its generator. In target order (eta,h,gamma_exterior), the combined map is therefore

    [[1,c,−b/2],[0,n,2],[0,0,1]].

The first rows/columns are interpreted with the displayed order-two relations. Its torsion map is the identity and its free determinant is n, independently of the retained integer c.

In degree three the boundary basis consists of the oriented source boundary N and the trace of its elliptic fibre through gamma. The certificate gives exterior row (0,1). Let Z be the cap H3 generator, represented by the trace of C0+C1 through one h turn. Then N maps to nZ and the gamma trace maps to2Z. To see the indices directly, lift to the double root boundary: the fibre specialization is C0+C1, and the actual norm identities send the two source directions to H^n and H². The graph correction is a path in the two-dimensional central source fibre and contributes no three-homology class. Thus the degree-three gluing matrix is

    [[0,1],[−n,−2]],

of determinant n. In degree four the boundary Z maps to zero and supplies the oriented top class. Together with the complete H2 isomorphism above, Mayer–Vietoris yields

    H0(Y)=H5(Y)=Z, H1(Y)=H3(Y)=Z/|n|,
    H2(Y)=H4(Y)=0.

Van Kampen is equally exact. The source exterior has pi1=Z gamma. Gluing kills u,w and alpha, hence eta=1 and h^n=1; gamma=h². Since n is odd, this gives pi1(Y)=Z/|n|. In particular n=±1 gives a simply connected integral homology five-sphere. The standard fixed sphere at the chosen whole-zero I1 remains the actual cusp-chart sphere, with primitive Hopf Euler meridian. The Gysin and final fixed-tube Mayer–Vietoris calculation of P3K.22 then applies to this actual orbit and line: it gives pi1(X)=0 and H*(X;Z)=H*(S6;Z), hence the smooth sphere by the already cited six-sphere classification. No characteristic return value is inferred from this topology calculation.

This conclusion currently concerns the constructed single quadratic I1* cap on the I1*+I3+2I1 source, with (a,b)=(6,2), norm n=±1 and its retained delta phase. The arbitrary additional smooth-cap tuples and the I1*+IV source still require their joint calculation. The geometric source-boundary cone and the one-cap line comparison should receive the parent's independent audit before this paragraph is exported as a proved statement.

## Actual Hom direction and the exact sign comparison (authoritative convention)

The global Hom section for M=O(P−O+vertical) gives the contracting source map t_(−Q), where Q=bG. The preceding positive-translation model was a homology computation; its identification with the actual map is specified here. We retain Q=bG and F as a lift of t_G, but set

    B=beta(z)F^(−b), k=−nb/2,
    A=chi^(−k/2) beta(z)^(n/2) F^k D.

The same exact calculation gives AB=BA and A²=B^n. Its source maps are B_source=t_(−bG) and A_source=t_(−nbG/2)D. For rn+2s=1, the actual primitive generator H=A^rB^s covers

    h=t_(−bG/2)D.

This is independent of n. The generic line and its resolved-divisor comparison are unchanged. The norm multiplier of H is still the positive one-half power of the small suspension scalar, so the actual map is contracting.

The actual exterior orbit is T_(t_−Q)P. The explicit diffeomorphism

    R:T_(t_−Q)P→T_(t_Q)P,   [p,t]↦[p,−t]

is well defined: the source relation (p,t+1)~(t_−Q p,t) becomes exactly the target relation after this substitution. It fixes every source slice and reverses the suspension circle. In particular gamma_actual↦−gamma_positive, while u,w and the source meridian alpha are unchanged. It reverses the total mapping-torus orientation; each source fibre keeps its complex orientation. No identification of line bundles by this real map is asserted: the actual line lift was constructed directly above.

For a mapping-torus chain cone of a source map f, this reversal is identity on the direct summand and −f^−1 on the suspended summand. The certificate now executes both chain identities. In boundary degrees one, two, three the matrices are

    Phi1=diag(I4,−1), Phi2=diag(I4,−T^−1),
    Phi3=diag(1,−U^−1).

The actual negative-translation matrices are T^−1,U^−1. The actual H2 representatives are Phi2^−1 times the previously printed positive-model representatives. Their exterior columns and the source-fibre identity epsilon−2r are unchanged, because R fixes direct source two-cycles. Thus the full arbitrary-kappa H2 calculation applies to these explicitly transported actual chains.

With this actual convention the affine relation has the opposite Q term:

    alpha gamma alpha^−1=gamma w^(−b).

The cap map is therefore

    u↦1, w↦eta, gamma↦h² eta^(+b/2), alpha↦h^n eta^c.

The actual degree-one matrix has torsion row (1,c,+b/2), with the same free rows (0,n,2),(0,0,1). The degree-three basis uses the positively oriented actual gamma trace, so its matrix remains [[0,1],[−n,−2]]. These are the conventions now exported by the certificate. The intermediate positive-Q matrices remain useful only through the displayed map R and its chain matrices.

The same exact chain construction applies to the I1*+IV+I1 source at (a,b)=(6,2), leaving IV ordinary. Its actual Néron–Severi basis has the identical D5+A2 Gram matrix, and the sections 2G and3G have the identical displayed classes and component permutations. The complement of the I1* tube again fibres over a disc with a section; its fundamental group is a quotient of the elliptic lattice, and the unimodular-lattice sequence gives H1=0. Thus it is simply connected and has the same Poincaré–Lefschetz chain data. This proves the identical one-quadratic-cap topology without identifying the two complex sources.

## Final positive outer-meridian alignment (supersedes earlier free-row signs)

The positive base meridian alpha and positive outward log-norm gamma have the cap images alpha↦−n h and gamma↦2h. This is an exact coordinate calculation: normalize the contraction B to t↦t−1 and write theta=arg(z)/(2pi). Then A acts as(theta,t)↦(theta+1/2,t−n/2). The original outer coordinates are x=2theta,y=t+n theta. A positive alpha changes x by1 at fixed y, so delta t=−n/2; gamma changes y by1, so delta t=1. The positive cap h changes t by1/2. The actual killed meridian is therefore2alpha+n gamma. The bounded norm-unit straightening is the explicit norm-shell coordinate of P3K.15; the remaining source-period terms are the retained graph and collar coefficients.

Because gamma is the positive outward suspension circle, it represents the inverse contracting deck B^−1. The source affine relation in this convention is alpha gamma alpha^−1=gamma w^b, and its actual cap map is

    u↦1, w↦eta, gamma↦h² eta^(−b/2), alpha↦h^(−n) eta^c.

The final degree-one matrix is [[1,c,−b/2],[0,−n,2],[0,0,1]]. The degree-three matrix is [[0,1],[n,−2]], with the Mayer–Vietoris minus sign on the cap row. Both determinants are−n. All homology and sphere conclusions are unchanged. The certificate now prints exactly these signs, and the final export will use only this convention.

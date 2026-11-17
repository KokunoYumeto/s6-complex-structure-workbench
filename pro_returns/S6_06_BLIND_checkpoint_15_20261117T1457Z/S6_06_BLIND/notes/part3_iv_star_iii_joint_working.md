# Joint IV* and III caps on the E6+A1 source

Complete derivation submitted for independent audit; proposed statement P3F.46. All four actual source/line pairs and both local cap maps are retained. The computation assigns sphere membership and integral topology, not a parameter-return class.

## J1. The source, the four pairs, and the exact root charts

We use the minimal regular surface of

    y²=x³+t x+t²,    G=(0,t).

The discriminant is t³(4+27t), giving III at0, I1 at t_c=-4/27, and IV* at infinity. On the open chart x nonzero, put u=(y-t)/x and v=(y+t)/x. The inverse is x=uv-(v-u)/2, t=x(v-u)/2, y=x(u+v)/2. Thus the surface is rational. The marked section has nonidentity components in E6 and A1, G.O=0 and height1/6. The integral Gram determinant below is -1, so these marked classes are an integral source basis; its discriminant and height also give primitive G and no Mordell--Weil torsion.

Put M=O(aG-O), Q=bG. The four pairs and actual root domains are

| (a,b) | IV* root order m_6 | III root order m_2 |
|---|---|---|
| (1,6) | 3l, l>=1, good | 4k, k>=1, good |
| (2,3) | 3l, l>=1, good | 4k+1, k>=0, reduced III |
| (3,2) | 3l+2, l>=0, reduced IV | 4k, k>=1, good |
| (6,1) | 3l+2, l>=0, reduced IV | 4k+1, k>=0, reduced III |

Choose integers n_6,n_2 with gcd(m_i,n_i)=1. They are retained with sign. At a reduced order-one III cap, n_2=0 is permitted. The sole simple whole-fibre zero is the actual I1 at t_c.

The source map h is t_(-bG). If T denotes its pushforward on divisor cycles, the exact section formula gives TM-M=-F. Its pullback is T^(-1), so h^*M-M=F. Hence the forward line map M_p->M_h(p) is a section of h^*M tensor M^(-1)=O(F). The section vanishing simply at t_c gives the specified B_0, and B_lambda=lambda B_0. This fixes the line direction and the negative source translation.

At infinity take q=1/t, x0=q²x, y0=q³y. The exact equation and section are

    y0²=x0³+q³x0+q⁴,    G=(0,q²).

For m_6=3l+2, put q=z^m6, x0=z^(4l+2)X, y0=z^(6l+3)Y. Then

    Y²=X³+z^(l+2)X+z²,    G'=(0,z).

Its A2 resolution has a reduced IV fibre. In X=zX1,Y=zY1 the two nonidentity labels are Y1=+1,-1. With k=2l+1, the deck is

    D(X,Y,z)=(zeta_m^(-2k)X,zeta_m^(-3k)Y,zeta_m z).

Its character on Y1 is zeta_m^(-(3k+1))=zeta_m^(-2m)=1, so all three labels are fixed. For m_6=3l the substitution k=2l gives the good equation

    Y²=X³+z^l X+1,    G'=(0,1),

with central deck (X,Y)->(zeta_3² X,Y). The central marked point G' has exact order3, since its horizontal tangent has triple intersection with Y²=X³+1.

At the III site use q=t. For m_2=4k+1, substitute q=z^m2, x=z^(2k)X, y=z^(3k)Y. We obtain

    Y²=X³+zX+z^(2k+2),    G'=(0,z^(k+1)).

Resolving its A1 point gives the actual reduced III fibre, and the deck fixes its two component labels. For m_2=4k the same coordinate substitution gives

    Y²=X³+X+z^(2k),    G'=(0,z^k),

whose central deck is (X,Y)->(-X,iY). The limit G'=(0,0) is the nonzero fixed two-torsion point. The actual minimal root maps are precisely these substitutions followed by the displayed A1/A2 resolutions or smooth good models.

## J2. Both line comparisons, exact commuting norms, and the joint family

At a reduced root aG' has identity component and N=O(aG'-O) has degree zero on every component. The original M also has degree zero on each component at that site. Pull it first to the resolved fibre product. Its degree is zero on every exceptional curve contracted in relative minimalization, so the blowup Picard decomposition descends it through each actual contraction. The resulting line and N differ by a vertical divisor with zero component degrees. The reduced III or IV intersection matrix has integral kernel the whole-fibre vector. Removing that exact base power identifies the lines and retains the deck character. This carries the specified B_0, not merely its generic Picard point.

For a good IV* root, the minimal cubic deck has tangent weights (2,1) at the three fixed points. The quotient lattice is Z²+Z(2,1)/3; its minimal rays are ((3-j)/3,j/3). The common smooth root refinement has rays

    (1,0),(2,1),(1,1),(1,2),(0,1).

Let beta be this root blowup and pi its toric map to the minimal quotient resolution. The section w=0 on that resolution has Cartier support h(v)=max(v_w-2v_z,0). Thus its exact pullback comparison is

    beta^*(root section)-pi^*(resolved section)
        = sum_v min(v_w,2v_z) E_v,

with exceptional coefficients (2,1,1). Subtract the O-chart contribution from the marked aG'-chart contribution. The resulting equality is

    beta^*N=pi^*M+D_(aG)-D_O.                         (J.1)

The original source map is the invariant Weierstrass substitution above. Its crepant quotient resolution is exactly the IV* source. Since Q'_0=O for b=3,6, translation by Q' is locally w->w unit+z² h(z³). It preserves (w,z),(w,z²),(z,w),(z,w²), hence the common normalized blowup and every correction coefficient in (J.1). This proves equivariance of the actual line comparison. For m_6=3l pull the entire diagram through the extra degree-l root and resolve the fibre product; the divisor equality and its maps pull back exactly.

For a good III root, the minimal fourth deck has two order-four fixed points O,P and one orbit {R1,R2} of stabilizer two. Its tangent weights are (1,1). Blow up all four points by beta and take the quotient pi. The exceptional images D0,D1,D2 have squares -4,-4,-2, and the proper central image C has square -1. The actual fibre is 4C+D0+D1+2D2. Contract C and then the resulting (-1)-curve D2. The two remaining curves have squares -2, intersection two, and the invariant Weierstrass map gives the original III tangency. The marked sections avoid both contracted curves. Therefore the exact divisor identity is

    beta^*N=pi^*alpha^*M+E_(aG)-E_O.                  (J.2)

Here alpha denotes those two contractions. Since b=2,6, Q'_0=O; its translation fixes all blowup centres and preserves the correction. This gives the specified B_0 and its deck commutation on N. For m_2=4k pull the entire correspondence through the additional base change and resolve, retaining (J.2) and all its characters.

The good central line has nonzero torsion Picard class of order3 at IV* and order2 at III. The actual connecting map [v]->[(D-1)v] from fixed elliptic points to Lambda/(D-1)Lambda carries it to the primitive torsion class of the cap circle line. A common deck character is retained; it does not change this torsion order.

Now work at either site, writing m,n,N,D for its data. At a reduced root, multiplication by m is invertible on the additive identity component and the component group. At a good root, use its analytic inverse branch at O. Thus there is a unique marked analytic R with mR=Q'; it is D-invariant by uniqueness. The actual source map t_(-nR)D has mth power t_(-nQ'). It extends on the minimal regular root by resolving the addition graph and comparing the invariant holomorphic two-form; common exceptional support gives the holomorphic translation and its inverse.

Lift t_(-R) to F on N. The chord divisor on a smooth fibre supplies the Hom section; its remaining vertical divisor has zero component degrees, hence is a whole fibre and is removed by that exact base monomial. Finite deck averaging then gives

    D F D^(-1)=chi F,    chi^m=1.

Write the actual descended lift as B_0=beta(q) F^m. The ratio is a base unit because every fibre is compact and connected. Deck commutation forces beta to be invariant. In particular F and D commute with B_0, and

    (F^n D)^m/B_0^n = chi^(n m(m-1)/2) beta(q)^(-n).

Dividing by an invariant analytic mth root of this unit produces A_0 with A_0^m=B_0^n and [A_0,B_0]=1. This retains the character factor for even good-root orders.

Set L=lcm(m_6,m_2), lambda=r^L and A_(i,r)=r^(L n_i/m_i)A_(i,0). Then A_(i,r)^m_i=B_lambda^n_i exactly. Choose u_i,v_i with n_i u_i+m_i v_i=1. The actual primitive generator is

    H_i=A_(i,r)^u_i B_lambda^v_i=r^(L/m_i)H_(i,0),
    H_i^m_i=B_lambda,    H_i^n_i=A_(i,r).             (J.3)

On smaller compact source tubes the norm ratios of H_(i,0) and its inverse are bounded. Thus H_i is strictly contracting for small r, and its norm shell gives a smooth proper cap N_i^times/<H_i>. The delta circle is free there: a unit rotation equal to H_i^j forces j=0 by contraction, then the unit is one.

With outward h_i=H_i^(-1), the single-A cut has

    alpha_i -> -n_i h_i,    gamma -> m_i h_i,
    mu_i=m_i alpha_i+n_i gamma.                      (J.4)

The actual holomorphic annular map is obtained in the constant-period extension (C times C*)/Lambda: remove its integral period two-cocycle on the annulus, whose H2 is zero, then solve the resulting holomorphic Lie-bundle cocycle on the Stein annulus. Choose its gamma component so the positive cut is A_(i,r) itself. The scalar variation from c0 to c, c=log(lambda)/(2pi i), is n_i(c-c0)s_i delta/m_i. This proves the same marking as (J.4), retaining every elliptic and delta phase.

For one positive r-loop, put k_i=L n_i/m_i. The inverse closing near each cap is q_i^k_i, with its extending unit retained. The global multiplier on the ordinary region is

    f(t)=t^k_2 (t-t_c)^(-(k_6+k_2)).                 (J.5)

It has orders k_2 at0, k_6 at infinity, and -(k_6+k_2) at the selected cusp. Its ratios to the two prescribed local multipliers are units. The cap charts themselves close by the identity; their annular transitions give precisely those local multipliers. At the cusp (J.5) is, modulo the specified B_lambda iterates, a bounded source translation and an invertible scalar unit, so it and its inverse extend in the actual nodal Mumford charts. This constructs the joint proper holomorphic family over the punctured r-disc. No return value is inferred from the source roots or from (J.5).

## J3. The complete source and boundary chain maps

Use the integral basis O,F,C0,...,C5,A1,G. The E6 graph has edges (0,1),(1,2),(2,3),(3,4),(2,5), with Cartan matrix A and highest-root marks v=(1,2,3,2,1,2). The source Gram matrix B has O²=G²=-1, OF=GF=1, E6 block -A, A1²=-2, and G.C0=G.A1=1; all other unspecified pairings vanish. Its determinant is -1. Thus the stated classes form the entire integral lattice.

For an integer j, let R_j be the E6 inverse-Cartan column at C0 or C4 when j=1 or2 modulo3, together with one half of A1 when j is odd. Let c_j be the sum of the corresponding diagonal entries4/3 and1/2. The exact section formula is

    phi=G-O-F+R_1,       phi²=-1/6,
    P_j=O+(1+(j²/6-2+c_j)/2)F+j phi-R_j.             (J.6)

It is integral, has square -1, and has the prescribed component intersections. Translation by G sends O to G, G to P_2, cyclically permutes the three affine E6 arms, and swaps A1 with F-A1. These columns define the integral isometry T_+. The actual map is T=T_+^(-b).

Let

    L_6=(F-sum(v_j C_j),C0,...,C5),
    L_2=(F-A1,A1),       L=(L_6,L_2).

Their multiplicity vectors are (1,v) and (1,1), and both products with L_i are F. If P is their actual component permutation, TL=LP.

The source complement V of both fibre tubes is represented by the integral relative complex

    C4=Z, C3=Z², C2=NS(S), C1=Z^9, C0=Z,
    d4=(1,1)^t, d2=L^t B, d3=d1=0.                  (J.7)

For boundary i, its source complex has C3=Z, C2=C1=Z^(r_i), C0=Z, with d2=L_i^t B L_i. Its inclusion is L_i in degree2, the component-coordinate embedding in degree1, and the ith coordinate in degree3. These complexes follow from the actual source/relative pair: the source and the tube retracts have free even homology, so the degree-one derived homotopy group of the two even split complexes is zero. Consequently the displayed maps have no omitted odd homotopy parameter. This also applies to the actual tangencies in reduced III/IV fibres; it does not replace them by an SNC fibre.

The action on (J.7) is T in degree2, P^(-t) in degree1, and identity in degrees0,3,4. On each boundary it is P_i in degree2, P_i^(-t) in degree1, and identity otherwise. The program forms their actual mapping-torus cones

    d_cone,j = [[d_j,T_(j-1)-1],[0,-d_(j-1)]],

then the block-diagonal inclusion of these cones. It exports every chain inclusion, integral Smith representative, projection, and marked alpha,gamma,N3,Fgamma cycle. The resulting exterior W has

    H1(W)=Z², H3(W)=Z², H4(W)=Z,
    H2(W)=Z/b + Z²,                                 (J.8)

where Z/1 is omitted.

The source complement has pi1(V)=Z. Indeed, the remaining I1 kills its primitive vanishing cycle v. If A is the III monodromy, A²=-I and tr(A)=0. The product relation with IV* and that I1 gives abs(<v,Av>)=1: expand tr(A^(-1)T_v^(-1)), whose absolute value is the absolute value of this pairing and equals1 from the inverse IV* trace. Hence v and Av form an integral elliptic basis, and conjugating the vanishing-cycle relation by the retained base loop kills both. The section gives the exact remaining generator, the base annulus loop. Translation acts trivially on that loop. Therefore pi1(W)=Z alpha direct_sum Z gamma. The two boundary base meridians map to alpha,-alpha; both outward gamma loops map to gamma.

## J4. Actual cap specialization and the complete integral MV maps

At a good cap, H1=Z h plus Z/p, H2=Z C, H3=Z(C h), H4=0, with p=3 or2. The generic fibre transports through the actual smooth root to its central elliptic fibre with degree one, so F maps to C. On the elliptic lattice the same transport is the identity. Since n u+m v=1, u is prime to the good deck order. The lattices (D-1)Lambda and (D^u-1)Lambda agree integrally: for order3, D+1=-D² is unimodular; for order4 the relevant odd powers are D or D^(-1). Thus the boundary finite torsion maps isomorphically to the cap finite torsion. The full elliptic fundamental group also maps onto the cap elliptic lattice, not just its finite abelianization.

At a reduced cap, H1=Z h, H2=Z C, H3=Z(sum C_j), H4=0. The primitive H_i cyclically permutes all central components: its component translation is -Q/m_i, independent of n_i by the Bezout identity in (J.3), and is nonzero modulo3 or2. The actual fibre specializes to the sum of the r_i components. It therefore maps to r_i C in H2 and to the primitive invariant sum in the Wang H3 trace.

Use boundary H2 coordinates (eta_i,r_i,s_i) at a good cap, with eta_i of order p_i and F=r_i. At a reduced cap use (r_i,s_i), with F=3r_i at IV* or2r_i at III. In both cases the cap sends r_i to C_i. Write its actual remaining column s_i->kappa_i C_i. No vanishing of either kappa is imposed.

The raw exterior maps, with rows ordered as torsion then two free classes, are:

| (a,b) | IV* H2 inclusion | III H2 inclusion |
|---|---|---|
| (1,6) | [[-2,1,6],[0,0,-1],[0,0,-1]] | [[3,1,3],[0,0,0],[0,0,1]] |
| (2,3) | [[1,2,7],[0,0,0],[0,0,-1]] | [[1,0],[0,-1],[0,2]] |
| (3,2) | [[-1,18],[0,1],[0,3]] | [[-1,-3,-1],[0,0,0],[0,0,1]] |
| (6,1) | [[0,-1],[0,3]] | [[0,-1],[0,2]] |

The torsion row is reduced modulo b. At b=6 use the exact CRT map Z/6->Z/3 plus Z/2, 1->(eta_6,eta_2); its exterior coefficient is -2+3=1. At b=3 its torsion generator already maps to1. At b=2 use minus the incoming III torsion generator. With domain order (eta,r_6,s_6,r_2,s_2), target order (tau,g1,g2,C6,C2), the complete degree-two maps are

    b=6: [[1,1,0,1,3],
          [0,0,-1,0,0],
          [0,0,-1,0,1],
          [0,-1,-kappa_6,0,0],
          [0,0,0,-1,-kappa_2]],

    b=3: [[1,2,1,1,0],
          [0,0,0,0,-1],
          [0,0,-1,0,2],
          [0,-1,-kappa_6,0,0],
          [0,0,0,-1,-kappa_2]],

    b=2: [[1,1,0,1,1],
          [0,0,1,0,0],
          [0,0,3,0,1],
          [0,-1,-kappa_6,0,0],
          [0,0,0,-1,-kappa_2]].                     (J.9)

Their determinants are1,1,-1. The first row and coordinate have order b. For b=1 the full free matrix is

    [[0,-1,0,-1],
     [0,3,0,2],
     [-1,-kappa_6,0,0],
     [0,0,-1,-kappa_2]],                             (J.10)

with determinant -1. Hence D2 is an integral isomorphism in every case and for every actual collar coefficient.

In degree one, each good boundary torsion maps isomorphically to its cap torsion and to zero in W. We retain arbitrary torsion path coefficients c_i,d_i in alpha_i and gamma before eliminating this actual isomorphism; the complete matrices are in the JSON. After that elimination, in the physical order (alpha_6,gamma_6,alpha_2,gamma_2), the free map is

    D1=[[1,0,-1,0],
        [0,1,0,1],
        [n_6,-m_6,0,0],
        [0,0,n_2,-m_2]].                            (J.11)

In degree three use the actual source-boundary class N_i followed by F gamma_i. The cap map is (-n_i,m_i): it is the norm-circle degree from (J.4), followed by specialization to the primitive invariant central fibre. No additional source three-class exists, because the cap source retracts to a two-dimensional central fibre. The source-cone calculation gives exterior N_6=-N_2 and the same Fgamma at both ends. In the exported bases, the IV* marked boundary change is diag(1,-1), the III one is identity; at b=1,2 the exterior target change is [[0,-1],[1,0]], and at b=3,6 it is identity. Thus the exact physical D3 equals the matrix (J.11).

Both determinants are

    det D1=det D3=-(m_2 n_6+m_6 n_2).                (J.12)

In degree four the map is (1,-1):Z²->Z, up to the recorded common target orientation. In degree zero it is [[1,1],[-1,0],[0,-1]], the actual three-piece incidence map. These specify every nonzero gluing degree.

## J5. Fundamental group, all integral homology, and sphere criterion

The full elliptic boundary lattice dies in V by the integral vanishing-cycle argument in J3. In each good cap the same lattice is the full normal elliptic subgroup, so van Kampen kills it. A reduced cap has no remaining elliptic subgroup. The exact residual presentation is

    <h_6,h_2 | h_6^m_6=h_2^m_2, h_6^n_6=h_2^(-n_2)>.

It is cyclic: choose u,v with n_6 u+m_6 v=1 and write
h_6=(h_6^n_6)^u(h_6^m_6)^v=h_2^(-n_2 u+m_2 v).
Its abelian presentation has a primitive relation and determinant

    D=m_2 n_6+m_6 n_2.

Therefore pi1(Y)=Z/|D|, with Z for D=0. The exact MV maps give, for D nonzero,

    H0(Y)=H5(Y)=Z, H1(Y)=H3(Y)=Z/|D|, H2(Y)=H4(Y)=0.

For D=0 the first three Smith factors of (J.11) are one, and its last factor is zero; the same holds for D3. Hence H_j(Y)=Z for every j from0 through5. These statements follow from the complete integral sequence, including D2, D4 and D0.

The orbit is the standard S5 exactly when D=+1 or-1. The actual delta circle is free on both added caps, and its only fixed locus is the selected nodal-fibre sphere, with its primitive O(-1) plus O(-1) Hopf chart. The Gysin and fixed-tube maps already proved in P3K.22 give pi1(X)=pi1(Y) and, for D=+/-1, the integral S6 homology. Theta6=0 gives the standard oriented S6. For D=0 or abs(D)>1, the displayed nontrivial fundamental group excludes a sphere. P3F.35's actual finite flop chain is the identity outside the cusp and transports this sphere criterion to every allowed fan.

Thus, for the prescribed two-cap construction, all four source pairs have precisely the sphere tuples

    m_2 n_6+m_6 n_2=+1 or-1

in their root domains in J1. This equation itself forces coprimality of the two orders and of each local norm pair. No return index is assigned here.

## Certificate

The complete source, chain maps, Smith representatives, marked cycles, full finite-group degree-one maps, all symbolic kappa columns, degree-three orientation changes, and all MV degrees are executed in code/part3/iv_star_iii_joint.py, with saved .json and .out. The four symbolic D2 determinants are units independently of both kappas; the D1/D3 determinant identity is symbolic for all orders. A further1056 exact integral Smith cases include positive, negative and zero D and verify the first three Smith factors. These finite checks supplement the displayed all-order proof.

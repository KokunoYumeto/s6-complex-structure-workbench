# Part 5: blind derivation from the construction

This file was written before opening arXiv:2610.00250, either version, or any other source stating the tangent cohomology or the full automorphism group of the constructed threefold. The construction data below were checked against the original [AC26] PDF, p. 2. The auxiliary general theorems used are Grauert's cohomology and base-change theorem, §7 Satz 5 (1960), with its 1963 corrigendum read, and Douady's existence and minimality results, §VII.8 and §VIII.1 (1974). No conclusion about the tangent cohomology is taken from [AC26].

We fix an admissible value of c and the marked sphere twist data (l0,l1,l2)=(0,1,-1), unless general admissible twist data are explicitly mentioned. All coherent cohomology has coefficients C. The surface D is the reduced singular locus of the cusp fibre W; it consists of three rational curves joining the two triple points. Write

    L=f*O_B(-1) tensor O_X(2 S1+S2),   F=O_X(S1+S2),
    E=ker(df:T_X -> f*T_B),            J=I_D tensor F.

We use the analytic root orbifold Bhat of B=P1 at 0 and 1, of orders 3 and 4. This notation is only a concise description of descent: a coherent sheaf on Bhat is a coherent sheaf on each root disc, equipped with the specified finite cyclic action, and ordinary compatible sheaves elsewhere. The morphism h:X->Bhat is defined by the divisors S1,S2 and their canonical sections, since 3S1=f*(0) and 4S2=f*(1). The coarse map is pi:Bhat->B, and f=pi h. Taking invariants of a finite group over C is exact, by the averaging projector. Consequently cohomology of a coherent sheaf on Bhat is the cohomology of its invariant direct image on B. We denote by Lhat and Fhat the root-orbifold line bundles whose pullbacks are L and F.

## P5.1. Proved: the exact sequence from the local charts

There is an exact sequence of coherent O_X-modules

    0 -> E -> T_X -> J -> 0,                         (5.1)

and E is locally free of rank two. Moreover E=h*V, where V is the orbifold bundle of fibrewise translation vector fields.

Proof. Away from the three special fibres the assertion is the tangent sequence of a holomorphic submersion. On the finite root chart, the map to the coarse base is t=s^m and its differential has image (s^(m-1)) times the pullback tangent line of B. The root-chart-to-X map is étale because the affine cyclic action is free; hence this calculation descends. The vanishing orders are 2 along S1 and 3 along S2.

At a cusp double point we take coordinates x,y,z with q=xy; the image of dq is the ideal (x,y), and a vector field a d/dx+b d/dy+c d/dz belongs to its kernel exactly when ya+xb=0. The convergent power series ring is a domain, and reducing modulo x and y shows a=xA, b=-yA; c is arbitrary. The kernel is free with generators x d/dx-y d/dy and d/dz. At a triple point q=xyz, the equation is yz a+xz b+xy c=0. Reduction modulo x, y, z gives a=xA,b=yB,c=zC; cancellation gives A+B+C=0. Thus the kernel is free with generators (x,-y,0) and (x,0,-z). The image is (xy,xz,yz), which is the reduced ideal of the three coordinate axes. These are precisely the local defining ideals of D. At a smooth point of W the derivative is surjective.

Globally the image of df is

    I_D tensor f*T_B tensor O_X(-2S1-3S2).

Since T_B=O_B(2) and 3S1=f*(0), 4S2=f*(1), this line bundle is F=O_X(S1+S2). This proves (5.1), including its scheme structure along the triple points. On the toric charts the two vertical logarithmic torus fields form exactly the free kernel just calculated. The linear part of every period translation has identity vertical derivative, while a finite base generator acts on vertical fields by the matrix R_g. Thus the local evaluations from the translation Lie bundle glue to an isomorphism h*V->E. The translations in the collar maps have identity vertical derivative and do not alter this comparison. ∎

## P5.2. Proved: the orbifold bundles and all direct images used

The translation bundle and the first coherent direct image on Bhat split as

    V=O_Bhat + Lhat,       R^1 h_*O_X=O_Bhat + Lhat,
    h_*O_X=O_Bhat,         R^2 h_*O_X=Lhat.          (5.2)

The following are the resulting direct images on the coarse base:

| sheaf | R^0 f_* | R^1 f_* | R^2 f_* |
|---|---|---|---|
| O_X | O | O + O(-1) | O(-1) |
| L | O(-1) | O(-1) + O(-1) | O(-1) |
| F | O | O + O | O |
| E | O + O(-1) | O + O(-1)^3 | O(-1)^2 |
| J | O(-1) | O(-1)^2 | O |

Proof of (5.2). In the period coordinates the two finite generators have vertical linear factors

    R1=[[-1/tau, 0],[(1-mu)/tau,1]],
    R2=[[1/tau,0],[-mu/tau,1]].

These follow directly by applying the homology matrices to the last two columns of Pi. Their second coordinate line is fixed. Their other eigenvalues at the roots, with zeta_j=exp(-2pi i/m_j), are zeta_1^2 and zeta_2. At the cusp R0=I and both logarithmic torus fields extend as sections of the abstract bundle E, by P5.1. Thus V is an extension of a line of these root weights (2,1) by O.

We compute its determinant without using a claimed canonical-bundle formula. Let Delta(tau)=q_tau product_{n>=1}(1-q_tau^n)^24 be the modular discriminant. The construction uses the ordinary elliptic modular parameter, so Delta has weight 12, has no zero in the upper half-plane, and has one simple zero at the cusp. The determinant r_g of R_g is the reciprocal modular factor, with a possible sign; its twelfth power has no sign. Hence Delta(tau)^(-1) gives a meromorphic section of (det V)^12 with precisely a simple pole at p0 and no other zero or pole. The root weights of det V are (2,1), so

    det V=pi*O_B(-1) tensor O_Bhat(2 p1/3+p2/4)=Lhat.

For clarity, the equality can be checked solely by root coordinates: the twelfth power of the right hand side is pi*O_B(-12+8+3)=pi*O_B(-1), and the two prescribed root characters agree; their quotient has zero root characters, descends to P1, and has twelfth power trivial, so it is trivial. There is no torsion in Pic(P1).

The invariant line gives 0->O->V->Lhat->0. Its extension group is H^1(Bhat,Lhat^(-1)). For an orbifold line written as pi*O(d) O(a p1/3+b p2/4), its invariant direct image is

    O_B(d+floor(a/3)+floor(b/4)).                   (5.3)

Indeed, on a root disc its invariant meromorphic coefficient has integral powers of t=s^m and pole order at most floor(a/m). This proves the rule also for negative a. For Lhat^(-1)=(1,-2,-1), formula (5.3) gives O(-1), whose H^1 is zero by its elementary Laurent-Cech computation. Therefore V splits.

We next construct R^1 h_*O from the Hodge quotient on the smooth torus fibres. In the quotient of the flat rank-four bundle by the two period rows, gamma and u form a basis; the classes w and delta equal -6mu gamma-tau u and -beta gamma-mu u. In this basis the first cohomology transitions are upper triangular with diagonal (1,r_g): for example T1u=-u-w gives the second column (6mu(g1z),tau(g1z)-1). Their determinant is therefore the same Lhat, and the image of gamma defines a nowhere-zero invariant section. It is nonzero at every root point because comparison of the w and delta coefficients in a linear combination of the two period rows shows that gamma never belongs to their span.

At the cusp, the normalization S=dP6 of W and its three double curves D_i yield the exact coherent normalization complex

    0 -> O_W -> nu_*O_S -> O_D1 + O_D2 + O_D3
      -> C_P + C_Q -> 0.                          (5.4)

The maps are differences between the two branches and the alternating sum at each triple point. Local exactness at xy=0 is the fibre-product identity for its two branches; at xyz=0 it follows by inclusion-exclusion of the three convergent power series rings. Explicitly the restriction differences satisfy g12(0)-g13(0)+g23(0)=0, and this relation suffices to reconstruct three branch functions. All strata in (5.4) have vanishing positive coherent cohomology. Its global complex is

    C --0--> C^3 --[[1,-1,1],[1,-1,1]]--> C^2,

so h^q(W,O_W)=(1,2,1). It is the cellular cochain complex of the two-triangle torus. Its cup product in degrees (1,1) is the exterior product giving its oriented fundamental class, and is nonzero.

The same branch resolution for constant coefficients shows that H^1(W,C)->H^1(W,O_W) is an isomorphism. The toroidal covering and the lattice quotient identify the two generators with gamma and u: a loop in W recording a translation of a normalization component has class in Lambda/Lambda_tor; the pairings with gamma,u are its two coordinates. The two flat cohomology sections therefore give a holomorphic frame through the cusp. One can see the extension by pulling back locally constant Cech cocycles on the toroidal cover; the same cocycles with coefficients in O give holomorphic sections on the full disc. Their central values form the basis just computed.

Flatness of the map to each ordinary or root disc follows because the local ring of the smooth total space is torsion free over the disc DVR. Properness is part of the given compactification construction; all fibres have dimension two. The coherent structure sheaf is flat, and the dimensions (1,2,1) are constant at the cusp and on the root charts. Grauert §7 Satz 5 therefore gives local freeness and base change there. The finite cyclic descent is exact. Thus the extension 0->O->R^1h_*O->Lhat->0 exists across every chart and splits by the same H^1(Lhat^-1)=0 calculation. The relative cup product identifies R^2h_*O with Lhat, since it is nonzero on smooth tori and on W by (5.4). Connectedness of the fibres and the maximum principle give h_*O=O.

For any line M on Bhat, the projection formula and (5.2) give

    R^q f_*(h*M)=pi_*(M tensor wedge^q(O+Lhat)).    (5.5)

This statement can also be checked separately in every root disc by tensoring and then applying the averaging projector; thus it includes the non-reduced scheme fibres of f. Formula (5.3) gives the first four rows of the table.

To obtain the fifth row we must compute the restriction map at D. The conductor square for the normalization S->W gives the exact sequence

    0 -> O_W -> nu_*O_S + O_D -> nu_*O_boundary ->0,   (5.6)

where boundary is the hexagon in S. The boundary has h^1=1, while D has h^1=2: its normalization is three P1s and its two ordinary triple points each impose two independent equality conditions. The resulting incidence matrix is

    [[1,-1,0],[0,1,-1],[1,-1,0],[0,1,-1]].

The induced map H^1(D,O_D)->H^1(boundary,O_boundary) is zero. To verify the sign, orient the three edges of the theta graph from P to Q. Traversing the hexagon gives e1-e2+e3-e1+e2-e3=0. The comparison from the constant branch complexes to the coherent ones is an isomorphism in degree one, so this signed cellular calculation computes the coherent pullback as well. The long exact sequence of (5.6) now shows that

    H^1(W,O_W) -> H^1(D,O_D)

is an isomorphism. This comparison includes both triple points, where two conditions, rather than one, occur.

The canonical section of F is nonzero at W, so F|D=O_D. In the restriction exact sequence 0->J->F->O_D->0, the map f_*F=O->C_p0 is ordinary evaluation and is surjective. The map R^1f_*F=O^2->C_p0^2 is evaluation followed by the preceding isomorphism. Its evaluation is an isomorphism on the fibre because R^1f_*F is the trivial rank-two bundle and Grauert base change applies. Both kernels are therefore O(-p0) in their respective ranks. Finally H^2(D,O_D)=0, and R^2f_*F=O, giving the last row. ∎

## P5.3. Proved: tangent cohomology

For every admissible c,

    (h^0(X_c,T),h^1(X_c,T),h^2(X_c,T),h^3(X_c,T))=(1,1,1,0).

Proof. The Laurent-Cech computation on the two standard charts of P1 gives H^0(O(d)) of dimension max(d+1,0) and H^1(O(d)) of dimension max(-d-1,0). Because the base is a curve, the Leray spectral sequence has only columns 0 and 1 and no nonzero higher differential. The table in P5.2 gives

    H^q(X,E)=(C,C,0,0),
    H^q(X,J)=(0,0,C,0).

The long exact sequence of (5.1) then gives H^0(T)=C, H^1(T)=C, H^2(T)=C and H^3(T)=0, with no undetermined connecting homomorphism: every adjacent group that could modify these four values is zero. The exact integer and rational checks of the bundle table, normalization matrices, and cohomology dimensions are in code/part5/bundle_cohomology.py and its output. The scalar dimensions in that program record the proven sheaf calculation; the proof is (5.1)-(5.6). ∎

## P5.4. Proved: the c-family is miniversal at each admissible member

The germ of the admissible c-parameter family at every c is a miniversal deformation germ; its Kuranishi germ is a smooth one-dimensional disc.

Proof. The explicit period and gluing formulas depend holomorphically on c, and strict admissibility is open, so a small c-disc defines a proper holomorphic family. Consider its first-order deformation in the direction dc=1. A first-order trivialization of the complex manifold would turn the map f into f+epsilon v, where v belongs to H^0(X,f*T_B). Since f_*O_X=O_B, this vector is the pullback of a vector field on B. On a simply connected regular base chart, transport the discrete marking through that first-order trivialization. Its lattice matrix is constant and is the identity at the reference point. A possible translation of the torus does not affect periods. An infinitesimal complex linear coordinate change H must therefore satisfy the exact matrix equation

    partial_c Pi + v(t) partial_t Pi = H(t) Pi.

The last two columns on the left vanish because they are the constant identity columns; hence H(t)=0. The upper entry of the second column then gives v(t) tau'(t)=0. The construction has nonconstant tau and tau' nonzero on the regular base, so v=0 there and therefore globally. The lower entry of the first column now gives 1=0. This contradiction proves that the Kodaira-Spencer map of the c-disc is nonzero. This calculation uses the entire marked period matrix and does not require a separate assertion that one selected elliptic quotient is intrinsic. By P5.3 it is an isomorphism onto H^1(X,T).

We invoke Douady's §VII.8 Théorème principal (1974, p.598), giving a finite-dimensional versal analytic germ, and §VIII.1 Théorème 1 and its corollary (p.600), giving the uniqueness of its tangent map. In the smooth-manifold case the first-order deformation classes are H^1(T), as follows directly by differentiating the holomorphic transition maps: their first-order differences are tangent-valued Cech 1-cocycles, and changes of local trivialization are coboundaries. Thus the tangent dimension of this germ is one. Embed it minimally as the zero space of an ideal I in C{z}. The versal property induces a map from our c-disc whose derivative is invertible. Pullback annihilates I; substitution by a convergent power series with nonzero derivative is an injective ring map C{z}->C{c-c0}, hence I=0. The inverse-function theorem identifies the two smooth germs, proving miniversality. This argument also rules out a non-reduced embedded germ. ∎

## P5.5. Proved: full automorphism group

For the sphere twist data, and in fact every admissible twist of the same (3,4) construction,

    Aut(X_c)=C*=C/Z.

The isomorphism sends a in C/Z to translation by a times the period vector delta-hat.

Proof: preservation of the fibration. Taking determinants in (5.1), whose quotient ideal I_D has codimension-two support, gives K_X^(-1)=L tensor F. Using the fibre-divisor relations,

    L tensor F = f*O(-1) O(3S1+2S2)=O(2S2).

Therefore K_X^(-2)=O(4S2)=f*O(1). Its complete two-dimensional space of sections is the pullback of H^0(P1,O(1)), so its complete linear system is exactly f. Every automorphism preserves this intrinsic linear system and induces an automorphism of B. The fibres of multiplicities 3 and 4 and the cusp fibre are individually distinguished by their scheme structures. The induced Möbius transformation fixes 0,1,infinity, hence is the identity.

Proof: linear parts. An automorphism of a complex torus is a translation followed by a group automorphism. To see the affine statement directly, lift its derivative to the universal vector cover; it is lattice-periodic and therefore descends to a holomorphic matrix-valued function on the compact torus, hence is constant. Integrating gives an affine lift. The integral linear action of a fibre-preserving automorphism is locally constant in the marked family and commutes with A1,A2.

In the ordered homology basis (gamma-hat,u-hat,w-hat,delta-hat), the matrices are

    A1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]],
    A2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]].

Solving PAj=AjP over Q gives P=a I+b E41. This is independently recomputed by code/part5/centralizer.py. Integrality gives a,b in Z, and det P=a^4 forces a=+1 or -1. A holomorphic linear map H on the vector cover satisfies H Pi=Pi P; its last two columns give H=aI, while its first column then gives b=0. Thus the possible linear parts are +I and -I.

The latter cannot occur. Normalize the base change t=s^3 at the first multiple fibre. The automorphism lifts canonically to this normalization and fixes s. At s=0 it would be z->-z+b on the covering torus. Commutation with the affine deck action z->A1 z+v1/3 gives

    (I-A1)b = 2v1/3 modulo Lambda.

Apply the torus character gamma:Lambda_R/Lambda->R/Z. It annihilates I-A1, whereas the right hand side has character 2l1/3. Freeness gives 3 not dividing l1, so this class is nonzero. This excludes -I and accounts for every possible integral linear part.

Proof: translation components. We give the integral calculation, since a dimension count of the connected automorphism group does not account for discrete components. Let j denote the inclusion of the cusp-punctured orbifold into Bhat, and let H=j_*Lambda be the lattice sheaf. Its cusp stalk is ker(M0-I)=Z w-hat+Z delta-hat. Let A be the sheaf of fibrewise translations of the local compactification that extend holomorphically at the cusp. There is an exact sequence of sheaves of abelian groups on Bhat

    0 -> H -> V -> A -> 0,                         (5.7)

where the second arrow exponentiates the translation vector.

Here is the local verification at the only non-smooth place. The toroidal covering Y_epsilon->N0 has component lattice Gamma=Lambda/Lambda_tor. A fibrewise translation automorphism acts identically on the nearby torus lattice and hence on Gamma, so it lifts to the covering. On its punctured open torus the lift is multiplication x->a(q)x. It sends a central component E0 to a component Ev. The index-one condition makes B0:Gamma->Z^2 an isomorphism. Composing with the unique corresponding deck shear makes the lift preserve E0. It then preserves the intersections of E0 with the other central components, so it preserves the torus E0 minus its boundary. In the chart (C*)^2 x Delta_q, evaluating at x=(1,1) shows that each a_i(q) is a holomorphic unit at q=0. It has a logarithm on the disc. Conversely multiplication by two holomorphic units extends on every toric chart and commutes with the deck shears. The kernel of exponentiation consists of period vectors Pi(q)lambda with no logarithmic term, precisely lambda in ker(M0-I). This proves exactness at the cusp. The covering-lift assertion may be checked on the nearby fibre and its meridian: the nearby fibre surjects onto Gamma, and a meridian bounding a disc through a smooth point of W remains bounding after an automorphism; hence the induced homomorphism to Gamma is unchanged. At a finite root chart ordinary local logarithms on the simply connected root disc give exactness, with finite-group equivariance retained rather than suppressed.

We now compute H^1(Bhat,H). Put

    M0=(A1 A2)^(-1)
      =[[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]].

A cocycle on the cusp-punctured orbifold is a pair (x1,x2) in Lambda^2 with N1 x1=0 and N2 x2=0, where

    N1=I+A1+A1^2
      =[[3,0,0,0],[6,0,0,0],[-12,0,0,0],[0,2,1,3]],
    N2=I+A2+A2^2+A2^3
      =[[4,0,0,0],[12,0,0,0],[-12,0,0,0],[0,2,2,4]].

Extension over the cusp says that the cocycle on g0 is zero in coker(M0-I). Since im(M0-I)=Z w-hat+Z delta-hat, the first two coordinates of x1+A1x2 must vanish. The complete integral solution is

    x1=(0,-b,2b-3c,c),   x2=(0,-2a-b,b,a),     a,b,c in Z.

For a lattice element lambda=(g,u,w,d), its principal cocycle ((A1-I)lambda,(A2-I)lambda) has parameter vector

    (a,b,c)^t = [[3,0,1],[-6,1,-1],[-2,1,0]] (g,u,w)^t.

This 3 by 3 matrix has determinant -1. More explicitly,

    g=c-a-b,   u=3c-2a-2b,   w=4a+3b-3c

gives a primitive integral coboundary for every cocycle. Thus H^1(Bhat,H)=0, including torsion. The complete Smith decomposition is in code/part5/parabolic_cohomology.py. The independent cover-complex calculation in code/part5/orbifold_lattice_complex.py verifies the same vanishing, with every differential printed.

By (5.7), every global extending translation therefore has a global logarithm in H^0(Bhat,V)=C. The kernel is H^0(Bhat,H)=Lambda^{A1,A2}=Z delta-hat, also checked by the exact centralizer program. Thus all translations are C/Z. The flow extends in the finite charts by commutation with their affine actions and in the cusp charts by torus multiplication. This proves existence, faithfulness and completeness of the displayed automorphism group. ∎

## P5.6. Proved: the integral c-period and isomorphism criterion

For fixed admissible twist data in the (3,4) construction, X_c and X_c' are biholomorphic exactly when c-c' belongs to 2Z. This statement fixes the period of the parameter; it does not fix an additive normalization of beta_part.

Proof. The argument recovering f from K_X^-2 applies to both manifolds. A biholomorphism fixes the base. Its integral linear map is P=aI+bE41 by the same centralizer computation, and H Pi_c=Pi_c' P gives a=+1 or -1 and b=a(c-c'). The multiple-fibre argument excludes a=-1. Hence c-c'=b is an integer.

We determine which shears S_b=I+bE41 preserve the compactified torsor class. For completeness we compute the relevant second sheaf cohomology integrally. Cover Bhat by a pair of pants P, the two root discs, and an ordinary cusp disc. The group cochains on P are Lambda in degree zero and Lambda^2 in degree one, with differential ((A1-I),(A2-I)). On the finite root discs they are the periodic cyclic resolution

    Lambda --(Aj-I)--> Lambda --Nj--> Lambda --(Aj-I)--> ... .

On the cusp disc only ker(M0-I) in degree zero occurs. The annuli have the two-term complexes Lambda --(Aj-I)--> Lambda. The restriction in degree one from P to its three annuli is

    (x1,x2) -> (x1,x2,-M0(x1+A1x2)).

The total Cech complex has ranks 14,28,20,8 in degrees 0 through 3. Its entire integer matrices d0,d1,d2 and their zero products are printed by code/part5/orbifold_lattice_complex.py. Smith decomposition gives H^0=Z, H^1=0 and H^2=Z+Z/2.

The degree-two presentation admits a short hand computation. After eliminating the annular coordinates, its generators are the invariant lattices Lambda^A1, Lambda^A2 and the global coinvariant Z detected by gamma. Put

    epsilon1=(1,2,-4,0),   epsilon2=(1,3,-3,0).

Each invariant lattice has basis (delta-hat,epsilon_j). Write the five generators as (delta1,epsilon1,delta2,epsilon2,hc). The norm and overlap relations reduce to

    delta1=0,   2delta2=0,   3epsilon1=hc=4epsilon2.       (5.8)

For the constant rank-one sheaf Z the identical calculation has generators z1,z2,hc and relations 3z1=hc=4z2; its primitive generator is z1-z2. The inclusion Z delta-hat->H sends z1 to delta1=0, z2 to delta2, and hc to zero. It therefore sends the primitive degree-two generator to the nonzero element delta2 of order two. The quotient gamma:H->Z sends epsilon1,epsilon2,hc to z1,z2,hc and kills delta1,delta2.

The compactified torsor of the construction is classified by H^1(Bhat,A). Sequence (5.7) identifies this with H^2(Bhat,H), because H^1(Bhat,V)=0 and H^2(Bhat,V)=0. The first vanishing follows from V=O+Lhat and its invariant image O+O(-1); the second follows from coherent cohomology on the coarse curve. This identification is constructive: take local logarithms of the holomorphic translation transitions, form their lattice-valued Cech coboundary, and reverse the process using the vanishing of H^1(V) and H^2(V).

We choose the orientations of the collar cocycle so that its character under gamma is

    (4l1+3l2-12l0)(z1-z2)=-p(z1-z2),
    p=12l0-4l1-3l2.

This follows directly from the cyclic norm of v_j/m_j, which is v_j, and the oppositely oriented cusp collar: the two finite root contributions are l1 z1 and l2 z2, while the cusp is -l0 hc. Thus (5.8) keeps the collar contribution, including its factor 12.

The shear S_b-I is the rank-one map b delta-hat tensor gamma. It changes the characteristic class by -bp delta2. Freeness requires l2 odd, so p is odd. The class is fixed exactly when b is even. For the integral shear, the Jacobian models themselves are identified: Pi_c and Pi_c' differ by the integral basis change S_b; on the cusp the bounded period matrix C changes in the beta entry by the integer c-c', so exp(2pi i C lambda) is unchanged for every integral lambda. The toric fan, its lattice, and its gluing units are therefore literally the same. On each root disc the same lattice basis change identifies the smooth Jacobian family and its linear cyclic action. Equality of characteristic classes now gives a holomorphic isomorphism between torsors for this fixed sheaf A by the constructive description above. The local group sheaf A consists precisely of translations extending across the toroidal cusp. Thus the isomorphism extends on all three charts. Conversely a global isomorphism preserves the class, forcing b even. ∎

## Checkpoint status and comparison restriction

Statements P5.1-P5.6 and all the cited exact computations have been written without opening the comparison paper. A scheduled hourly checkpoint containing this file is required before the first opening of arXiv:2610.00250. Part 5.3 (comparison with both versions) is still pending that checkpoint and subsequent source access. The invariant computations above have not yet been compared to that source.

## General references opened for this derivation

Grauert, H., *Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen*, Publ. Math. IHES 5 (1960), 5-64, §7 Satz5, p.64. Primary PDF opened and relevant statement read: https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf . The 1963 corrigendum, Publ. Math. IHES16, pp.35-36, was also opened: https://www.numdam.org/item/10.1007/BF02684291.pdf . Its §7 correction changes Satz2; we use Satz5 with flatness and constant cohomology.

Douady, A., *Le problème des modules locaux pour les espaces C-analytiques compacts*, Ann. Sci. ENS (4)7 (1974), 569-602. Primary PDF opened: https://numdam.org/item/10.24033/asens.1280.pdf . We use §VII.8 Théorème principal, p.598, and §VIII.1 Théorème1 with its corollary, p.600. The tangent identification required in P5.4 is given by the explicit first-order Cech argument there.

The original Kuranishi 1962 paper was searched for, but its JSTOR PDF and a candidate Annals endpoint were unavailable; it is not used as an opened source. No literature claim of priority is made. The comparison required by the prompt remains deliberately unopened.

# Localized exclusion of extra smooth and multiplicative orders

Proposed P3F.48; complete proof for independent audit. We consider the actual additive cores constructed in P3F.36,38,41,42,43,46,47. They include the one- and two-additive-cap source profiles with b=1,2,3,6. The marked elliptic and delta collar data are retained, and all extra logarithmic sites are removed before applying the source inversion. The result excludes effective order greater than one at every added smooth or multiplicative source site. It does not discard an order-one clutch or assert a parameter-return identity.

## E1. The exact source-exterior input

Let W0 be the original negative-translation orbit source with only its prescribed additive-core tubes removed. It is the actual mapping torus of t_(-bG) on that source complement. Let q=1 or2 be the number of those removed additive tubes. The complete source-cone calculations in the indicated statements give

    H2(W0;Z)=Z/b plus Z^q,
    H3(W0;Z)=Z^q.

Here the trivial Z/1 is omitted. The H3 basis is the actual common generic-fibre trace F gamma, together with q-1 source-boundary classes N_i at the old removed additive tubes. These are precisely the marked degree-three representatives exported in the source-cone certificates. For q=1 it is just F gamma. For q=2 the relation is N_1+N_2=0, and the displayed two generators form an integral basis.

On the source mapping torus the actual map

    I[p,t]=[-p,-t]

is an involution, reverses the five-dimensional orientation, fixes the base, and preserves every chosen tube. Its action on H2(W0) is minus the identity after removing the b-primary torsion. Here is the exact source reason, which also checks this property independently of a Smith basis. The height decomposition writes the rational source lattice using O,F, the root components, and the marked Shioda class phi. Inversion fixes O,F, takes phi to -phi, and permutes each root component by its inverse component label. Every retained multiplicative source fibre has transitive t_(-bG) component action. In its coinvariants its components therefore span only the whole-fibre direction. The removed additive components have already been imposed in the complement intersection map. Translation sends phi to phi plus a nonzero rational multiple of F, so F vanishes in the rational degree-two coinvariant. Its surviving direction is phi, on which inversion is negative. The remaining q-1 directions are traces of the base-annulus H1 classes; source inversion fixes those base classes and time reversal negates their traces. Thus I is -1 on all H2(W0;Q). Since the integral torsion is exactly Z/b, its action on H2(W0;Z_(p)) is literally -1 for every prime p not dividing b. No division by2 is used here: the torsion-free localized group injects into its rationalization.

All these statements concern the actual source maps. In particular the new E6+A1 certificate iv_star_iii_joint.py exports the source inversion, its chain maps, and its full mixed-group H2 action for all four pairs. The earlier I1* certificates retain the corresponding source inversion. The remaining one-core calculations use the same marked section/root decomposition and their displayed full source cones.

## E2. The ordinary comparison with every extra tube

Remove all added ordinary smooth and multiplicative source tubes from W0. Write W for the resulting exterior, U_j for those actual ordinary tubes, and E_j=boundary U_j. We work over R=Z_(p), where p does not divide b. Every H2(U_j;R) and H2(E_j;R) is free. At a multiplicative site this uses the actual primitive Euler pair (N,c), with gcd(N,c)=1, because t_(-bG) is transitive on its source components. The ordinary cap maps on H2 are surjective. Their kernels are the actual smooth rims

    a alpha, b alpha, alpha gamma

or the multiplicative classes R_j,L_j of P3F.40. These are primitive free groups of rank3 or2. Denote their direct sum by K.

The map H3(W;R)->H3(W0;R) is onto by actual representatives. Each old N_i lies in a collar of its old additive boundary, disjoint from every new tube. The common F gamma trace can be taken over a regular source value outside all the new tubes. Thus the full marked H3 basis in E1 lies in W. The Mayer--Vietoris connecting map from H3(W0) to the new boundary H2 is therefore zero.

The next boundary map H2(W0;R)->direct_sum H1(E_j;R) also vanishes. Its image lies in the kernel of the ordinary cap H1 maps, namely the direct sum of primitive meridians R alpha_j. These meridians are I-even. Its source is I-odd by E1. Equivariance therefore makes twice every image zero. The target meridian group is torsion-free, even when p=2, so the image is zero.

The exact ordinary MV sequence now gives

    0 -> direct_sum H2(E_j;R)
      -> H2(W;R) plus direct_sum H2(U_j;R)
      -> H2(W0;R) -> 0.

Using the actual surjections H2(E_j)->H2(U_j) and their kernels, this is exactly

    0 -> K -> H2(W;R) -> H2(W0;R) -> 0.               (E.1)

For completeness, surjectivity of the last map follows by subtracting boundary lifts of the U_j coordinates from any ordinary MV preimage. Its kernel is exactly K because a boundary preimage with all cap coordinates zero belongs to those local ordinary kernels. Injectivity follows from the vanishing H3 connecting map just proved. Thus no rim subgroup or finite-index correction has been omitted.

Let g_-(q) be the Lie lift of the actual source translation -bG(q). With the mapping-torus convention (p,1)~(t_(g_-)p,0), its exact local smooth source trivialization is

    (a,b,t) -> [a+b tau(q)-t g_-(q),t].

The relation at t=1 is literal: t_(g_-)(a+b tau-g_-)=a+b tau. The actual source inversion is (-a,-b,-t), with alpha fixed. Hence every smooth ordinary kernel is I-odd, and its three core two-tori ab,a gamma,b gamma are I-even. On a multiplicative Tate sector, write g_-(q) after continuation as g_-(q)+c_-. The continuation is a->a+Nb-c_- t, and commutes with this same minus identity. Thus the physical c of P3F.40 is c_-, equivalently minus the component integer of +bG. Therefore the exact classes z,B are I-even and R,L are I-odd. These are the actual weighted source markings; no inversion is extended over a replacement cap.

Both K and the quotient in (E.1) are free and I-odd. Choose any R-linear splitting, which exists since the quotient is free. The involution matrix has form [[-1,C],[0,-1]]. Its square is the identity, so 2C=0. The coefficient ring has no2-torsion, and C=0. Thus I is -1 on all the free module H2(W;R). Every I-even new boundary core column maps to zero in W, again because twice its image is zero in a torsion-free module. This proof treats p=2 without an eigenprojection or an inverse of2.

## E3. Eliminating the actual additive-core blocks

The prescribed additive-core degree-two MV map is an integral isomorphism in each constructed core, with all its actual collar coefficients retained. This is P3F.36/38 and the complete blocks of P3F.41--43,46,47. Project the full new target H2(W;R) plus the old cap H2 groups to H2(W0;R) plus those cap groups. On the old boundary summand its map is exactly that previously proved isomorphism, by the actual ordinary inclusions. Thus its image is a graph over the full projected module and meets K trivially. Eliminating precisely that graph leaves K, together with the new replacement-cap targets. This is an exact module quotient, not an extension of the source involution over old caps. It also does not require the old closed orbit itself to be a sphere or its old Seifert determinant to be nonzero.

For a smooth replacement retain its actual primitive meridian

    mu=m alpha+n gamma+lambda_a a+lambda_b b,
    gcd(m,n)=1.

The cap H2 map is the exterior square of the exact quotient by mu. Its kernel is mu wedge H1(E). Since all core columns map to zero in W, the remaining ordinary rim block has the exact presentation

    [[m,0,0,-lambda_a],
     [0,m,0,-lambda_b],
     [0,0,m,n]].                                     (E.2)

At a prime p dividing m, n is a unit in R, and this quotient is exactly (R/mR)^2. The third relation eliminates the vector (-lambda_a,-lambda_b,n) from (R/mR)^3; its last coordinate is a unit. Every elliptic coefficient is retained in this elimination.

For a multiplicative replacement, use the exact P3F.40 boundary basis (z,R,B,L), with z.L=R.B=1 and all self-pairings zero. The exterior z,B columns vanish by E2, while R,L are this site's independent ordinary kernel. With physical c=-c_G and retained Tate period integer j, put A=Nj-cn. The actual cap has rows

    [[m,-A,s,t], [0,0,m,A]].

The cap isotropic-kernel equation is mt=As, and actual component transitivity gives gcd(m,A)=1. Thus s=mk,t=Ak. The actual target basis change T_new=T+kC gives

    [[m,-A,0,0], [0,0,m,A]].                         (E.3)

Eliminating the two exterior R,L rows leaves diag(m,m), hence again (R/mR)^2. This uses precisely the local cap maps of P3F.40, whose local hypotheses are the primitive source Euler pair and transitivity; the global primitive-source assumption of its first application is replaced here by the exact zero core columns in E2.

The site kernels in (E.1) are a direct sum. Therefore the blocks (E.2)--(E.3) occupy independent summands after the old additive blocks are eliminated. A prime divisor of any new order contributes nonzero degree-two MV cokernel. That cokernel injects into H2 of the full closed orbit by the complete MV sequence, so a sphere orbit cannot have such a divisor.

## E4. Why the required localization always applies to a sphere

Keep the actual marked base meridians and the positive gamma generator, and quotient the orbit fundamental group by the normal elliptic generators. The resulting marked Seifert relations include

    m_i alpha_i+n_i gamma=0,
    sum_i alpha_i+b_0 gamma=0

in the abelianization; b_0 is the retained integer base framing. The precise elliptic or delta path terms vanish under this quotient, not by a change of gamma marking. If a prime p divides two effective orders, the corresponding primitive norm relations force gamma=0 modulo p. All other meridians are then determined, while the two indicated meridians have only their one sum relation. Hence this quotient has nonzero H1 over F_p. A sphere therefore has pairwise coprime effective orders. This argument retains b_0, since its term vanishes once gamma=0.

Every prime dividing b divides a required old good/star order in the actual weighted cores. For b=2 there is either the quadratic I1* cap or a good III/III* order divisible by4. For b=3 there is a good IV/IV* order divisible by3. For b=6 both primes occur in the corresponding required old caps: I1* plus good IV, or good IV* plus good III. For b=1 there is no restriction. Thus any prime divisor of a new smooth or multiplicative order is prime to b in a sphere member. It is exactly a prime to which E1--E3 applies, yielding a contradiction.

Consequently every added smooth or multiplicative effective order is one. The initial reduction to effective primitive pairs is the actual finite-kernel quotient map of P3K.19, so this conclusion does not merely discard an ineffective group factor. The proof retains every order-one elliptic, gamma and delta clutch. Finally the actual finite flop chain P3F.35 is the identity off the selected cusp; it preserves the extra sites and transports the exclusion to every allowed fan.

## Certificate and scope

The source inversion and source-cone inputs are retained in the I1* and IV*+III certificates. The new certificate weighted_extra_sites.py exports the exact smooth and multiplicative replacement matrices, their localized eliminations, the involution-extension identity, and the prime/order implication for each weighted core. These algebraic checks supplement the exact ordinary comparison (E.1), which is proved above from actual cycle representatives.

No order-one clutch or parameter-return comparison is concluded by this exclusion. Its result is the precise effective-order restriction needed before the remaining global source/line/gamma cochains.

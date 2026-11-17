# Part 2 main argument: divisor meridians at the corner

This proof draft is independent of all earlier runs. It is under cross-check by the other agents in this run. The lattice and analytic constructions, not a previously asserted non-existence result, are its inputs.

## P2.6. The actual sixfold parameter descent and its collar

Put b=4l1+3l2, a=b-12l0=-p. The full twist vectors may have delta components; they have no effect on the calculations below because the c-variation of Pi(v_j) is -12l_j v delta. Fix s=log(q)/(2pi i), v=log(r)/(2pi i), c=-12v. The period columns are those of P2.1. On the regular t-base define

    H(t)=-(4l1 log(t)+3l2 log(t-1))/(2pi i).

Its changes of branch are integral multiples of the period delta. Thus translation by H(t)delta is a well-defined holomorphic section of the torus group. The parameter deck v->v+1 acts on the regular-family coordinates by

    R:(t,v,zeta)->(t,v+1,zeta+H(t)delta).

This is the descent map for the family built with the prescribed finite gluings: near the first root disc the gluing changes by -4l1 log(t)/(2pi i)delta; the remaining term in H is holomorphic there. Near the second root disc the same assertion holds with -3l2 log(t-1). Adding this bounded holomorphic delta-translation extends the descent over the finite cap. Since c changes by -12, the finite affine action changes by -12l_j/m_j delta, an integral period, so the cap action itself is unchanged. This verifies the descent on both finite charts.

Near the cusp write H=b s+U(q), where U=-3l2 log(1-q)/(2pi i) is holomorphic at q=0. In the cusp chart eta=zeta+l0 z_gamma, the parameter descent is translation by (a s+U)delta. Adding the lattice period a gamma rewrites this as

    (6a mu, U+aC-12a v),

which is holomorphic and bounded in q at zero, for each v. Its exponentials are units in every toric chart. Therefore it extends over the cusp filling. This fixes the collar sign and constructs the actual descended family over r*, without using an isomorphism assertion from an earlier run.

## P2.7. Explicit origins and their differences

On q=Q^12 define the following lifts of sections into C²:

    o=(-b mu s/2,
       b s²/24-b C s/12+l0 s/2+v(b s+U)),

    sigma=-l0 z_gamma+
       (6a mu v, vU+aCv-6av²+6av).

Their deck differences are

    o(s+12,v)-o(s,v)=-b gamma+6(b+l0)delta,
    o(s,v+1)-o(s,v)=H delta,
    sigma(s+12,v)-sigma(s,v)=-12l0 gamma+78l0 delta,
    sigma(s,v+1)-sigma(s,v)=H delta+a gamma.

Every extra term is a lattice period, so these are actual holomorphic sections of the descended torus torsor. In cusp coordinates sigma+l0 z_gamma is the displayed holomorphic function of q and v, and hence sigma extends over q=0 in the smooth open orbit of the cusp component. Subtracting o makes the r-deck pure: the coordinates eta=zeta-o have trivial parameter deck on the vector coordinate. The rank-one toroidal construction below extends eta=0 over r=0. Thus o is an extending origin for that partial filling.

Exact subtraction gives

    sigma-o=a F0,
    F0=(mu(s+12v)/2,
        C(s+12v)/12-(s+12v)²/24+6v).

After q=Q^(12m), r=R^n, its differences are

    Delta_Q F=a m gamma-6a m² delta,
    Delta_R F=a n gamma-6a n(n-1)delta.

In particular the radial coefficient is -pn, with the printed definition p=12l0-4l1-3l2 and F=sigma-o. The proposed +pn has the wrong sign in these conventions. The default p=-1 reproduces the F printed in the prompt.

The calculations are polynomial identities and are independently checked in code/part2_origins_and_group.py. The holomorphic functions mu,C,U are invariant under the integer s shifts used here; no numerical approximation occurs.

## P2.8. The rank-one partial filling

We spell out the local toroidal chart used in P2.7. On a simply connected finite-base chart, first quotient the vector coordinates by the delta period and put W=exp(-2pi i eta2), z=eta1. The remaining periods act by

    (z,W)->(z+1,W),
    (z,W)->(z+tau,exp(-2pi i mu)W),
    (z,W)->(z+6mu,d(t)r^12 W),

where d is a nonzero holomorphic unit on the chosen finite-base chart. The first two transformations define a degree-zero holomorphic line bundle without its zero section over the elliptic curve C/(Z+tau Z); no product assertion is made about this bundle.

Use the infinite chain with node chart indexed by i in Z,

    X_i=W/r^i, Y_i=r^(i+1)/W, X_iY_i=r.

The overlap where Y_i is nonzero is given by X_(i+1)=Y_i^(-1), Y_(i+1)=rY_i. Together with the corresponding inverse overlap these are holomorphic isomorphisms, and give the standard infinite P1 chain at r=0. Units acting on W act inversely on X_i,Y_i and extend; the third period shifts i by twelve, translates z by 6mu, and acts by the unit d. The quotient therefore has a cycle of twelve P1 bundles over the elliptic base at r=0. The node charts are smooth because r=X_iY_i is a coordinate function on the smooth (X_i,Y_i)-plane; the extra elliptic and base coordinates give a smooth fourfold. The central divisor is reduced with normal crossings.

For properness, restrict to a relatively compact finite-base chart and sufficiently small r. The elliptic lattice has a compact fundamental parallelogram uniformly on that chart. The period shifting i by twelve gives twelve node neighborhoods and twelve middle annuli as a compact fundamental region in the chain; the unit d and the line-bundle transition units are bounded above and below on this compact base. The usual inner and outer radius bounds can therefore be chosen uniformly. These regions cover the quotient, and their closures are compact over a closed smaller r-disc. This proves properness. At nonzero r the quotient is exactly the displayed torus, so its chart comparison is explicit.

At the finite root point j, the affine translation v_j/m_j has gamma coefficient l_j/m_j. Its W multiplier contains r^(12l_j/m_j), so it rotates the component cycle by 12l_j/m_j. The shifts are 4l1 and 3l2. The affine generator has order m_j and every nontrivial power moves the twelve-cycle by a nonzero rotation: 3 does not divide l1 and l2 is odd. Thus the action is free also on the central divisor. Quotienting the smooth charts gives smooth total space, a reduced NC r-central divisor, and the original finite multiple fibre in t. The overlap maps are the explicit logarithmic gluing translations; after subtracting their local origins, their remaining factors are holomorphic units and integral chain shifts, so they extend in these charts.

The component cover on the regular t-base is

    y^12=t^(4l1)(t-1)^(3l2).

Its three rotations are 4l1,3l2,-b modulo12; the cusp rotation is also p modulo12. Gluing this finite-base filling to the prescribed q-cusp filling over r* by the translation sigma-o gives a smooth-total, proper partial filling over (P1 x Delta_r) minus (infinity,0). Properness and the Hausdorff property follow locally on this covered base; the two maps agree on the overlap by P2.7.

## P2.9. Extension of the marked algebraic-reduction map over any proper filling

The marked map f of the (3,4) family extends meromorphically over every proper analytic filling of a finite parameter cover.

Proof. Take the reduced irreducible component of the total space that dominates the parameter disc, and resolve it isomorphically over the punctured disc. The result Z is smooth and proper over the disc. The relative canonical line bundle omega_(Z/Delta) restricts on every noncentral fibre to K_X. The direct chart computation P5.5 gives K_X^(-2)=f*O_P1(1), with h0=2. Consequently the coherent sheaf p_*omega^(-2) has rank two and no torsion: multiplication by the parameter is injective on a line bundle on this dominating component, hence also on its pushforward. A torsion-free coherent sheaf on a smooth disc is locally free. Choose its frame. Evaluation gives a meromorphic map Z to P1 agreeing on every noncentral fibre with f followed by a projective linear transformation. Resolving its graph makes F=(p,f') proper over P1 x Delta.

The relative critical locus is the closed analytic rank-drop locus of dF. Its image is analytic by the proper mapping theorem. Off zero its image has exactly three points in each P1, namely the two multiple fibres and the cusp. Thus its nonvertical components are three analytic curves of degree one over the punctured disc. Their multiplicity-three, multiplicity-four and cusp labels remove permutation monodromy. Their normalizations give three meromorphic sections of P1 over the whole disc, even when their limits coincide. The unique Möbius transformation sending them to 0,1,infinity has meromorphic coefficients (the elementary cross-ratio formula). Composing produces the desired meromorphic marked f. Resolve this last graph. Every modification made is an isomorphism over the punctured parameter disc, except harmless modifications within q=0 introduced later to make divisors NC. ∎

## P2.10. A finite-orbit lattice calculation

The representation generated by A1,A2 on Lambda_Q/Qdelta has no nonzero vector with finite orbit. In coordinates (g,u,w), the cusp inverse-transport matrix has nilpotent part N=E32. A finite orbit vector is fixed by a power of every conjugate of the cusp unipotent. Since (I+N)^k=I+kN in characteristic zero, it lies in ker(N), ker(NA1), and ker(NA2). These equations are

    u=0, 6g+w=0, -w=0,

and force g=u=w=0. This is stronger than merely computing common fixed vectors. The computation and its exact zero kernel are in part2_origins_and_group.py.

## P2.11. The normalized meridian of a horizontal central component

Work over the finite regular t-base with the actual parameter family r=R^n. Modulo the normal subgroup generated by delta, its fundamental group is

    (Lambda/Zdelta semidirect pi1(B_regular)) x Z_R.

Indeed the R-deck is a delta-translation H(t), its changes of t-branch are delta periods, and its lattice monodromy differs from the identity only by multiples of delta. The stated quotient follows directly from the universal-cover deck action, without a claim about any unmarked quotient space.

Let D be a smooth central divisor in a resolved proper filling whose image in P1 is dominant. Its oriented small normal meridian projects to m positive parameter turns, m the positive order of R along D. Modulo delta it is represented by (lambda,m). Conjugating by a fibre loop changes lambda by (I-T_R^m) of that loop, which is zero modulo delta. Transporting a meridian along a path in D therefore transports lambda by the base monodromy. The proper map D->P1 factors into a map with connected fibres followed by a finite map of curves. Outside finitely many values it is a smooth fibration after this factorization. Its fundamental group maps onto a finite-index subgroup of the regular-base fundamental group. Hence lambda has finite orbit under the global monodromy. P2.10 gives lambda=0. In particular its gamma coefficient is zero, with no division or torsion ambiguity.

The same argument applies to a component with central multiplicity m>1: the small meridian has R-degree m throughout, and the conjugation calculation still vanishes modulo delta. Extra components lying over isolated t-values are not discarded; they enter the corner calculation next.

## P2.12. The corner commutator and the non-existence proof

The (3,4) family for every admissible twist has no proper Hausdorff complex-analytic filling after a finite parameter cover.

Proof. A supposed filling pulls back to a proper filling with w=R^(6n), for some positive integer n. By P2.9 resolve it to a smooth proper space carrying the marked map to P1 x Delta_R. Near infinity make the further finite base change q=Q^(12m), with m positive, normalize, and resolve both total space and the pullback of the two axes. These are proper analytic operations and leave the smooth torus family over Q* x R* unchanged. The fibre over the corner is connected: the Stein factor of this proper map is finite and is generically a single sheet, since its general torus fibre is connected; the bidisc is normal, so a finite birational factor is the identity.

We compute the fundamental group on the corner complement. Let Q and R denote the positive deck lifts before choosing an origin. In the lattice coordinates its presentation has the commuting lattice Lambda and

    A_Q=I-12m E32+12m E41,
    A_R=I+12n E41,
    [Q,R]=-12mn b delta.

The affine relation follows by subtracting H(s+12m)-H(s)=12mb and taking n parameter turns. The commuting lifts

    Q_o=T_(-mb gamma) Q,       R_o=R

give a semidirect-product presentation Lambda semidirect Z². Central delta adjustments in these lifts do not affect any calculation below. Define kappa(lambda)=gamma(lambda), the first integral lattice coordinate.

For each irreducible component D_i of the total inverse image of the two axes, put alpha_i=ord_(D_i)(Q), beta_i=ord_(D_i)(R). These are nonnegative integers with alpha_i+beta_i>0. Write its positively oriented meridian in the semidirect product as (lambda_i,alpha_i,beta_i), and put kappa_i=gamma(lambda_i). The value kappa_i is independent of the path used to base the meridian, because every commutator changes a lattice vector by an element killed by gamma.

Two such divisors that meet have commuting meridians: in a smooth NC chart the meridians are coordinate circles. Their images in the corner-complement fundamental group commute as well. Computing the delta coordinate of this commutator gives

    (m alpha_i+n beta_i) kappa_j
       =(m alpha_j+n beta_j) kappa_i.             (C)

There are no higher terms: both monodromy nilpotents have square zero and their products vanish. Formula (C) follows equally by multiplication of the displayed integer matrices. Thus the ratio kappa_i/(m alpha_i+n beta_i) is constant along every edge of the divisor intersection graph. Its denominator is strictly positive, including for every extra vertical central component.

A component of the central divisor dominating the t-base exists, since the proper map onto P1 x Delta is surjective. Choose its strict transform. It meets the corner fibre by properness. P2.11 gives kappa_i=0, alpha_i=0, beta_i>0, so its ratio is zero.

The strict cusp divisor also meets the corner fibre. Choose its smooth local branch met by the extending cusp origin sigma. The Q-meridian of that branch, expressed in the original Jacobian coordinates, has gamma coefficient -12m l0 from the collar section -l0 z_gamma. Relative to Q_o its coefficient is

    -12m l0+mb=ma.

Thus its ratio is a, since beta=0 and alpha=1 there. At a further ramification or resolution that retains this branch, both the Q-order and this coefficient acquire the same positive factor, so the ratio remains a.

The corner fibre is a compact connected subset of the union of the axis divisors. A finite closed cover by its intersections with their irreducible components has a connected incidence graph: a disconnected graph would partition that fibre into two disjoint nonempty closed subsets, both open in the fibre. Hence a chain of intersecting axis components joins the chosen horizontal central component to the chosen strict cusp component. Formula (C) forces their ratios to coincide. This gives a=0.

Freeness of the finite actions gives 3 not dividing l1 and l2 odd, so p=12l0-4l1-3l2 is coprime to 12 and is nonzero. Therefore a=-p is nonzero, a contradiction. This proves the claim, allowing singular initial total spaces, nonreduced central spaces, and additional components. ∎

## Verification points still being checked

Before this draft receives a final Proved label, the independent reviews must check the normal-meridian transport through the Stein factor in P2.11, the use of the intrinsic anticanonical pencil in P2.9, and the existence of the connected divisor chain in P2.12. The integer identities are already computed; the corresponding program does not substitute for those geometric checks.

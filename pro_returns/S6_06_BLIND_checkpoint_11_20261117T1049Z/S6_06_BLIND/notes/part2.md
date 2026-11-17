# Part 2: working derivation

## P2.1. Exact period and collar identities

We use the ordered lattice (gamma-hat,u-hat,w-hat,delta-hat), and put q=exp(2 pi i s), r=exp(2 pi i v). Positive q and r loops increase s and v by one. Since w=r^6=exp(-pi i c), c=-12v, modulo a fixed additive normalization. We write tau=s+h(q), beta=C(q)-s-12v, with h,mu,C holomorphic at q=0. The holomorphic period map on the logarithmic cover is

    Pi(s,v)=[ gamma, u, w, delta ],
    gamma=(6mu,C-s-12v), u=(s+h,mu), w=(1,0), delta=(0,1).

Its period-column identities are Pi(s+1,v)=Pi(s,v)Kq and Pi(s,v+1)=Pi(s,v)Kr, where

    Kq=[[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]],
    Kr=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[-12,0,0,1]].

These are period-column comparison maps, not an implicit change of the transport convention. Their induced action on a fixed real torus marking is obtained by applying Pi inverse to the same complex vector; it is Kq inverse and Kr inverse in that convention. The matrices commute. In the holomorphic characters Z=exp(2 pi i zeta1), W=exp(-2 pi i zeta2), adding u multiplies by (q exp(2 pi i h), exp(-2 pi i mu)); adding gamma multiplies by (exp(12 pi i mu), q r^12 exp(-2 pi i C)). This derives the displayed Jacobian character laws directly from AC26's period matrix.

The collar section carrying the primitive gamma-hat class can be represented on the logarithmic cover by

    z_gamma(s,v)=(6s mu, -s(s+1)/2+s(C-12v)).

Indeed z_gamma(s+1,v)-z_gamma(s,v)=gamma(s+1,v). Therefore it descends to a holomorphic section of the torus family over the punctured q-disc, and its connecting lattice class is gamma-hat. Its r-loop difference is -12s delta. Multiplying by l0 records the collar term exactly. These identities are checked symbolically in code/part2_corner.py.

The finite gluing maps have the translation (log s_j)/(2 pi i) Pi v_j, where t_j=s_j^{m_j}. Replacing v by v+1 changes their delta coordinate by -12 l_j log(s_j)/(2 pi i), namely -4l1 log(t)/(2 pi i) and -3l2 log(t-1)/(2 pi i). At the cusp log(t)=-log(q), and log(t-1)=-log(q)+log(1-q), with the latter last term a single-valued holomorphic unit logarithm. The coefficient of s delta after subtracting the collar correction is consequently

    a=4l1+3l2-12l0=-p.

This calculation retains l0. It is a calculation of the gluing cocycle; identifying all choices of extending origins still requires the remaining local construction.

## P2.2. A sign inconsistency in the supplied origin formulas

Define exactly the vector-valued holomorphic function on the logarithmic cover printed in the prompt,

    F(s,v)=(mu(s+12v)/2, C(s+12v)/12-(s+12v)^2/24+6v).

Here C=C(q) and mu=mu(q) are held fixed under integral s shifts. Exact subtraction gives, for every integer m,n,

    F(s+12m,v)-F(s,v)=m gamma-6m^2 delta,
    F(s,v+n)-F(s,v)=n gamma-6n(n-1) delta.

For the specified sphere twists (0,1,-1), p=-1. Thus the printed F has radial class +n gamma-hat modulo delta-hat, whereas the proposed p n gamma-hat has the opposite sign. The classes differ by 2n gamma-hat in the free lattice Lambda/Z delta-hat and are unequal for n nonzero. The two printed assertions cannot both hold with the printed conventions. The collar computation P2.1 produces the coefficient -p, consistent with the printed F at the default twist.

This refutes the literal compatibility of the proposed +p rule with the supplied F. It does not identify F with the difference of the two actual extending origins without constructing those origins. That geometric identification is a separate open obligation.

For the requested example (l0,l1,l2)=(0,2,-1), the exact arithmetic gives p=-5 and a=5. Its finite component shifts would be +8 and -3 in a 12-cycle, with cusp shift -5 modulo 12; the component-cover equation is y^12=t^8/(t-1)^3. This last sentence records the induced gluing permutation, not a completed construction of a proper filling.

## P2.3. Why the stated unrestricted non-existence mechanism still needs a proof

Solving the simultaneous invariant-vector equations on Lambda_Q/Q delta-hat gives zero; the exact rank computation appears in part2_corner.py. This verifies the lattice input. The required geometric statement is stronger: an arbitrary proper analytic filling over r must produce, on a suitable common model, a trace section whose radial defect is a globally invariant lattice class and also has zero defect in the cusp origin. A meromorphic extension of the normalized algebraic-reduction map to that common model, and control of all divisorial radial meridians, are needed to make that implication. They have not been derived from properness alone in this file.

The elementary obstruction to treating graph closure as automatic is the holomorphic map from a punctured disc to P1 given by exp(1/r). Its graph has no meromorphic extension across zero: a meromorphic function on a disc has a Laurent expansion with finite principal part, whereas exp(1/r) has infinitely many negative Laurent coefficients. This example is an exact statement about that graph-closure inference; it is not a filling of the S6 family and does not refute the desired non-existence theorem. The special structure of the S6 family might supply the missing extension, and that is what remains to be proved.

## P2.4. Untwisted plumbing construction, written for independent checking

This subsection is a construction under active verification. It is not yet labelled Proved.

Let S be the smooth rational elliptic surface of E26, M=O_S(P-O), h=t_{6P}, L=M tensor h*M^{-1}=O_S(F_infinity), and phi a section of L with divisor F_infinity. All these are fixed holomorphic objects. Form two copies Y0,Y1 of the P1-bundle P_S(O+M). A coordinate z near the zero section is a vector in M; the inverse coordinate w near infinity is in M^{-1}. Identify zero(Y0) at p with infinity(Y1) at h(p), and zero(Y1) with infinity(Y0) at p. Replace the first intersection by the neck equation zw=r phi(p), in M tensor h*M^{-1}; replace the second by z'w'=r in M tensor M^{-1}.

For a precise analytic gluing, choose Hermitian disk neighborhoods of the four sections with disjoint closures on each Y_i, of radius epsilon. Retain the compact middle portions and attach the two necks on epsilon/2<|z|<epsilon or epsilon/2<|w|<epsilon. Choose |r| so small that both |r phi| and |r| are less than epsilon^2/4 in the corresponding product metrics. The two annular attachments in each neck are then disjoint. The attachment maps are the holomorphic coordinate projections, with h on the first infinity side. Bundle transition functions preserve the equations because phi is a section of exactly the product normal bundle. These give a Hausdorff analytic atlas. A finite cover of compact S and closed middle/neck subsets proves properness over a smaller closed r-disc. The central fibre is the cycle of Y0 and Y1, with the two indicated copies of S as double loci. Torsion freeness over C{r} proves flatness.

Over S minus F_infinity, crossing the two necks in succession identifies z0(p) with r^2 phi_p z0(h(p)). Consequently the general fibre over r is the quotient of M^times by the lift of h^{-1} scaled by u=r^2, on exactly the region where E26 defines its original quotient. This is an explicit comparison map obtained by iterating the two displayed neck identifications.

At a smooth point of F_infinity, phi is a coordinate q and zw=rq. At its unique nodal point choose coordinates x,y on the smooth surface S with phi=xy. The total fourfold has equation zw=rxy. For r nonzero its only singularity is the ordinary double point z=w=x=y=0. Blow up the coherent ideal of the globally distinguished central component, locally (z,r) at this neck. This ideal is globally available because the two central components are distinct; at the other neck it is Cartier. Its two charts are

    r=z a, w=a xy                 (coordinates z,a,x,y),
    z=r b, bw=xy                 (coordinates r,b,w,x,y with one equation).

The first is smooth. The second is the product of a threefold ordinary double point with the r-disc. Take its small resolution by the ideal (b,x). Its charts are

    b=x k, y=k w                 (coordinates r,x,k,w),
    x=b k, w=k y                 (coordinates r,b,k,y).

They are smooth and glue by k inversion. This modification is an isomorphism off the singular section, so it glues to the unchanged complement. It is proper, being locally the projective small resolution. The first chart has r=za and the small-resolution charts have r as a coordinate, so the resulting map is flat with reduced normal-crossings central divisor. The local toric subdivision must still be explicitly matched to the A2 fan prescribed in E26/AC26 to identify the general compactified fibre, rather than only its quotient complement.

There is an involution sending r to -r, acting trivially on Y0's fibre coordinate and by -1 on Y1's. Both neck equations are preserved. It preserves the component-blowup ideal and the small-resolution ideal (b,x), because b changes by a sign. Its quotient is proper over u=r^2. The u-map is flat because u is a nonzero divisor in the invariant local rings, which are torsion free over the one-dimensional regular base. Away from u=0 the action exchanges the two r-values and hence gives precisely one copy of the corresponding fibre. This would supply the original, unramified parameter filling once the preceding fan identification is checked.

## P2.5. Euler obstruction for the proposed single-component central fibre

For Q obtained by identifying the zero and infinity sections of P_S(O+M) via h, its normalization has Euler number 2e(S)=24 and its double locus is S. Its local crossing smoothing line is L=O_S(F_infinity). The virtual top Chern correction along the double locus is

    e_vir(Q)=e(normalization)-2e(S)+integral_S(c1(S)c1(L)-c1(L)^2).

One derivation is obtained by restricting the virtual tangent bundle of a local hypersurface model to its normalization. If a,b are the two branch normal Chern classes, c1(L)=a+b. The two branch corrections sum to -2c2(S)+c1(S)(a+b)-(a+b)^2, by multiplying c(TY)(1+b)/(1+a+b) on each branch. This expression is symmetric and therefore descends from the two labelled normal branches; it defines the same virtual Chern number of the intrinsic perfect cotangent complex.

Here c1(S)=[F_infinity] and F_infinity^2=0, so e_vir(Q)=0. The prescribed smooth untwisted X(u) has Euler number 2: scaling the M^times coordinate gives a free circle action over every finite base fibre, and the index-one A2 toric fibre has two point strata, all other strata having Euler number zero. Thus a proper flat lci smoothing of Q cannot have X(u) as its smooth fibres. The needed reduction from an arbitrary flat smoothing with this lci central fibre to a relative lci morphism is the local lifting of a regular sequence over the disc, to be written explicitly in the paper. The computation corrects the stated central fibre, not the existence of a different central fibre.

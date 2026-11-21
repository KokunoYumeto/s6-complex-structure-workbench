# Paper I: statement-directed global check of main A–C

## Method and exposure

This is a global used-and-rechecked comparison, **not a blind reproof**. I have already read and edited extensive arithmetic/analytic proofs, the real-reflection proof, and the newly checked A2 local models. I have performed the initial four and nine scoped target checks and their disclosed computations; these are existing evidence, not new credit here. I read the current main statements and their cited input statements before writing this record. A setup extractor for F2.1 also printed the full F1.1 and F1.2 proofs; that exposure is explicitly included. The displayed block law and quadratic character calculation below are not assigned fresh independent credit.

The detailed current main-theorem outlines and the current literature-status table have not yet been opened for this comparison. This record fixes the intended claim/input derivations and anticipated wording checks before that detailed review. Exact statement/input snapshots and source hashes are in the two intake JSON files. The target is the current publication text, with the attached proofs and this run's already recorded checks used as evidence.

## Main A: exact chain and normalization

1. **Pointed model and logarithm.** The arithmetic equation has A=−3t³(t−1)/4, B=t⁴(t−1)²/4 and P=(0,t²(t−1)/2). The geometric model is obtained by `(x,y)->(2x,−2sqrt(2)y)`, so its discriminant is 64 times the arithmetic one. The normalized norm is transported by the pointed lattice isomorphism. The finite t=0,1 assertions use the stated smooth root models, not the singular rational equations at those parameters. The cusp-selected zero mu and the condition beta_part+tau→0 fix the logarithm branch in the theta-period formula.

2. **Determinant and domain.** Taking the imaginary part of `(6i/pi)Log(theta1/(2sqrt3 eta))` gives `(6/pi)log|theta1/(2sqrt3 eta)|`. Subtracting `6(Im mu)²/Im tau` gives `D_part=(6/pi)log(N/(2sqrt3))` exactly. The input maximum `N=sqrt2` at t=1 therefore gives `M=−3log6/pi` and `H*=−M`. For the parameter `w=exp(−pi i c)`, `|w|=exp(pi Im c)`; its exact radius is exp(pi H*)=216, and u=w² has radius46656. The “all ordinary and both finite root fibres” clause matters: at the threshold the finite t=1 root lattice degenerates, while above it the range of D_part yields a zero somewhere. Below it all determinants have the fixed negative sign.

3. **Global shape.** The cited critical theorem already supplies the complete coarse statement: t=0 is C1 with `L_t=7/384`; t=1 is the unique maximum; all other coarse points are noncritical; every ray from1 is strictly decreasing to minus infinity. At the ray through t=0 the derivative in the outward radial direction is `−2L_t(0)=−7/192`, consistent with strict decrease. The level through0 has value `(1/4)log3` because its norm is 3^(1/4). Strict radial monotonicity, the endpoint limits and continuity give one radial intersection at every angle and hence nested star-shaped Jordan levels. The body supplies the needed smoothness, including the one C1 point.

4. **Division and torsion.** The normalized division relation has exponent `(m²−1)/12` on the absolute discriminant and denominator `|psi_m|`. A torsion congruence m=±1 mod n makes N(mP)=N(P), giving the displayed twelfth-power formula. Its m>=2 and nonzero-division hypotheses must remain inherited from the general formula. The five values and all F4–F8 polynomials are exactly those in C4.4. In particular `(sqrt2)^12=64`, `(3^(1/4))^12=27`, and the two order-six positive values multiply to11. The smooth central model caveat must stay visible or be supplied by the common main setup.

5. **Heights.** The sum formula is the normalized global canonical-height decomposition with lambda_sigma=−log N and complex embeddings counted separately. For K=Q, exponentiating gives `N=A_t exp(−hhat_O)`. The eleven A_t values agree with the exact finite local-height table: the nontrivial sums are log2/2+log3/2, (2/3)log2+(1/4)log3, (3/4)log2, log2, log2, log3/2, and (5/12)log3; the remaining sums are zero. The explicit model maps have differential scale u_i^(-1), already checked in this run. No theorem about transcendence of these nontorsion norm values follows from this identity; the corresponding questions belong to the final open discussion.

Expected outline ingredients: the pointed model/zero, theta multiplier identity with its cusp constant, division-ladder maximum, derivative factors plus cusp/compact estimates, division values, and normalized height decomposition. The exact maximum uses the retained analytic ladder proof; the archived duplicate interval-cover proof is not a separate necessary input.

## Main B: parameter, discrete data and real forms

1. **Intrinsic base.** The anticanonical-pencil input recovers f and labels the multiplicity-three, multiplicity-four and cusp fibres. Therefore a biholomorphism is over the identity of B. The full affine/collar theorem is the operative all-data input; it must not be inferred merely from equality of a middle torus period.

2. **Standard multiplicities.** For `p=12l0−4r1−3r2`, the primitivity hypotheses give gcd(p,6)=1 and p!=0. The classification theorem gives `p'=a p`, integral n=c'−c, and parity `n=k2−k2' mod2`. Under the exact map to `exp(−pi i(c+k2))`, the parity condition is precisely equality of the multiplicative invariant. The sign a changes p to ±p, so the complete integer invariant is |p|. Full analytic collar data are retained in constructing the comparison; their elimination is the proved global gluing conclusion, not an omission of those data.

3. **Sphere circuit and higher multiplicities.** At a fixed standard datum p'=p forces a=1, and the period subgroup is2Z. At fixed u=exp(−2pi i c), one positive circuit sends c to c−1 and changes w to−w, exchanging the two classes. For m1=3k,m2=4l, gcd(3k,4l)=1 implies gcd(k,2l)=1. Primitivity of r'_j makes the two congruences solve a single residue class modulo2kl; the fixed-data subgroup is2kl Z. The body theorem and its exact Viaclovsky coordinate transport supply the displayed finite-vector and cusp signs, including the condition p=±1. The original u reference must be the same on both sides, as in the common Definition.

4. **Nomes and conjugation.** The finite periods give q2=iw/216 and q1=−w²/48³, so `q1/q2²=216²/48³=27/64`. The real comparison is c' =1−bar(c) modulo2Z; exponentiating gives w'=−bar(w), with no further phase. A self-comparison therefore has Re(c)=1/2 mod Z. The explicit reflection theorem supplies a genuine involution after its translation correction.

5. **Two real classes and their topology.** The action on holomorphic translations is z→1/bar(z). A cocycle a satisfies a/bar(a)=1, hence is real and nonzero, and holomorphic twisted conjugacy multiplies it by a positive number |b|². This gives exactly two classes. For w=−ir, q2 is positive; for w=ir, it is negative. The full fixed-fibre table has two nonempty classes in the former case and one in the latter, with the corresponding S3/semifree and S3/Hopf conclusions supplied by mapsI A3.3. The topological S3 calculation is an exposed cited input here, not a new independent derivation from mod-two homology alone.

Expected outline ingredients: intrinsic pencil, full period/lattice normalizer and local affine/cusp comparisons, arithmetic congruences, higher-multiplicity coordinate transport, parameter circuit, and actual reflection/fixed-set classification. A statement that merely gives the middle quotient would not prove the compact comparison.

## Main C: group, action, period curve and all fibre loci

### Exact coordinate dictionary and group algebra

The main setup has d=delta_hat and the vertical two-vector `Pi_c d=(0,1)`. The monodromy section instead names the lattice vector e=delta_hat. Thus its P_e and q_e are the main statement's P_d and q_d by the identity e=d in the lattice; its e must not be identified with the two-dimensional vertical vector without applying Pi_c.

Preservation of the displayed symplectic matrix and fixation of d force the first row `(1,0,0,0)`, middle block B in SL2, and lower middle row `−x^t J2 B`; integrality forces the middle first column to be6x. Multiplication gives

`g(B,x,t)g(C,y,s)=g(BC,x+By,t+s−6 x^t J2 B y)`.

Modulo2, Q(x)=x1+x2+x1x2 is one on all three nonzero vectors and zero on zero, so it is SL2(F2)-invariant, and its polar form is x^t J2 y. Consequently `t+6Q(x)−alpha(B)` is a character modulo12. The input generation theorem proves its kernel is the **actual** monodromy; mere containment would be insufficient. The character is onto using g(I,0,1), giving index12. A lattice line automorphism sends d to±d, yielding the additional index two and total24.

The fundamental-set input is explicitly for `Gamma\P_d(R)`, the **vector** stabilizer. Its modular lifts have central entries9,1,6. The two Heisenberg left multiplications give exactly the printed shifts `t−6−6x2` and `t−6+6x1`. The angle interval of length pi uses the actual lift of−I and its central shift; paired modular faces need those identifications. The main phrase “in the real parabolic” should be checked against this precise group scope.

### Proper action and the embedded curve

For q_d!=0, the complex line spanned over R by d,Jd is nondegenerate for psi. The stabilizer of J in the vector stabilizer is a compact circle acting on its complementary complex line. At each fixed nonzero q value the action is homogeneous with this compact stabilizer; a continuously chosen section in q supplies a product description and hence properness on both sign regions. The discrete lattice action is therefore properly discontinuous, and finite stabilizers give the stated Hausdorff analytic orbifolds.

At q_d=0, put v=Jd. The plane spanned by d,v is isotropic. Points with rational v are dense: nearby isotropic pairs `(d,v')` are carried to `(d,v)` by nearby real symplectic changes fixing d. For rational v the nonzero rational map

`N(w)=psi(d,w)d+psi(v,w)v`

has N²=0, is symplectic-infinitesimal, and commutes with J. Multiplying N by a denominator gives an integral unipotent fixing d, and a suitable power lies in the finite-index group Gamma. Its powers are distinct and stabilize J. Thus every open set meeting the null locus contains a point with infinite stabilizer. This establishes the maximality mechanism in the main statement; the body proof must supply this density, not only the single example J0.

The global period chart has D_c<0 and q_d=−6/D_c>0, so its sign agrees with the parameter domain. On the quotient the modular j function is well defined and its composition with the period map is1728t. It supplies a holomorphic left inverse, proving injectivity and immersion. The finite root limits remain inside O+ and descend through the actual finite monodromy. Once extended over0,1, the map is proper because inverse images of compact quotient sets are closed and have bounded t coordinate. The left inverse then also gives the complex-space embedding. The cusp escapes because |j| grows, so closure adds precisely the two finite root values.

### Neron–Severi and quotient morphisms

For the rows `sigma1=(6mu,tau,1,0)` and `sigma2=(beta,mu,0,1)`, the coefficient of `E wedge sigma1 wedge sigma2` is exactly

`E12−E13 tau+(6E23−E14)mu+E24 beta+E34(6mu²−tau beta)`.

For real integral E, its vanishing is the (1,1) condition. The real period determinant in the marked ordering is `Im(tau)*D_c<0`, hence the complex orientation gives E²=−2Pf(E). The invariant form has E14=6,E23=1, so Pf=6 and square−12, as stated.

A nonzero real (1,1) form with Pf=0 has one-dimensional Hermitian rank. After changing its sign it is semipositive; its radical is a rational J-invariant real plane. The saturated null lattice is the connected elliptic kernel, and dividing by its complex subtorus gives the associated quotient morphism. Conversely every elliptic quotient pulls back an integral positive degree form to such an isotropic E. Negative Pf means positive square, hence a definite Hermitian form after a sign, giving a polarization. These are exactly the two loci in the input theorem. On a two-torus a nonzero curve class has nonnegative square (intersect with a translate); a fibre with NS=Z eta therefore has no curves, since every nonzero multiple of eta has negative square.

The input theorem distinguishes the locus description from the actual construction of connected kernels: the latter uses the saturated null lattices of the full integral kernel. The main wording “these countable unions classify all quotient maps” should be checked and, if needed, made explicit by this morphism. No claim about unparameterized individual maps should be inferred from a union of loci alone.

Expected outline ingredients: actual character-kernel generation; fundamental-set face maps; compact stabilizers and dense null stabilizers; the global chart and j left inverse; the exact (1,1) kernel, Pfaffian sign, and saturated-kernel quotient construction. Appell–Humbert and polarization criteria are known inputs; the explicit marked equations/loci are the present application.

## Next comparison gate

After freezing this record, read every current outline step for A–C, the corresponding current body proofs, and the literature-status rows. Check hypotheses, all coordinate/sign constants, the exact scope of the global statements, proof dependency ordering and the distinction between known inputs and the stated application. Record only the comparisons actually performed as used-and-rechecked events. Propose guarded front-matter edits for any concrete discrepancy; no main TeX writes.

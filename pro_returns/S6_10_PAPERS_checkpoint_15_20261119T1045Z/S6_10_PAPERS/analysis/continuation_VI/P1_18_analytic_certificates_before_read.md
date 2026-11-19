# P1.18: complete analytic certificate derivations before target exposure

19 November 2026. This document is written from the clean operator/algorithm packet `analysis/continuation_V/P1_18_analytic_certificate_statement_packet.md`, SHA256 17f21a06c362fb787f2daee44d0b5d516417c084193c9ad5245626468cb77501, and the additional midpoint-polynomial assertion supplied without a target. No printed P1.18 numerical paragraph or producing code has been opened. The geometric/global argument remains root's separate scope. All matrix equations below use the right-ODE convention supplied in the packet.

## 0. Exact weighted norm and entrywise ball maps

Let W=diag(w_i), with every w_i positive. The actual coordinate isomorphism is Phi(M)=W^(-1)MW, whose inverse is Q to WQW^(-1). Its ij entry is M_ij w_j/w_i, and Phi(MN)=Phi(M)Phi(N). Thus the specified norm is the maximum absolute row-sum norm of that exact conjugate. Directly,

    sum_j |(MN)_ij| w_j/w_i
    <= sum_k |M_ik| w_k/w_i sum_j |N_kj| w_j/w_k
    <= ||N||_w sum_k |M_ik| w_k/w_i.

Taking the maximum over i proves submultiplicativity. Also ||I||_w=1, the triangle inequality follows row by row, and the individual term in a row gives

    |M_ij| <= ||M||_w w_i/w_j.

For a complex-ball matrix C, let |C|_+ be the nonnegative matrix of certified upper bounds for the absolute values of its entries. Matrix sums/products are enclosed through the actual entry sums. More explicitly, for centres C,D and entrywise radii E,F, multiplication has centre CD and radius bounded by

    |C| F + E |D| + E F,

plus the computed arithmetic rounding radius. This follows by expanding (C+Delta C)(D+Delta D) and bounding each ij sum. There is no change of norm hidden in this rule. In particular left multiplication by a known constant Hc transforms a tail E by the actual matrix product |Hc|_+ E; uncertainty of Hc itself is retained by the same displayed product rule.

## A. Ordinary finite-root Taylor coefficients, Gronwall and Cauchy tails

The two matrices in `root_connection_matrices` are already the gauged right-ODE coefficients. The supplied exact frame convention is

    E_root(t)=E_original(lambda(t)) D_root(t),
    G_root=D_root^(-1)(lambda'(t) Gamma6)D_root+D_root^(-1)D_root'.

This frame identity and the listed root coefficients are permitted statement inputs. The numerical variable change is the actual map t=alpha z at zero, alpha^4=256/3125, and u=alpha z at infinity, alpha^5=3125/256, using the positive real root. Consequently the chain rule gives G_z(z)=alpha G_root(alpha z). No second gauge is applied to the already gauged matrices. The specified diagonal D_root and its inverse retain the frame map when its entries are evaluated. All error products involving that diagonal use the entrywise multiplication rule above.

Write m=4 or5. Multiplying the supplied rational G_root(t) by 1+t^m/alpha^m gives a polynomial of degree at most m-1 with rational matrix coefficients C_j. Hence

    G_z(z)=B(z)/(1+z^m),
    B_j=alpha^(j+1) C_j,       B(z)=sum_(j=0)^(m-1) B_j z^j.

This gives every coefficient by an exact scalar coordinate map. The new code derives C_j from the given rational functions and verifies the polynomial identities rather than fitting numerical values.

Substitute U(z)=sum_(n>=0) U_n z^n with U_0=I into (1+z^m)U'=UB. Equating the coefficient of z^n gives

    (n+1)U_(n+1)
      = sum_(j=0)^min(m-1,n) U_(n-j) B_j
        - (n-m+1)U_(n-m+1),       n>=m,

and the same formula with the last term absent for0<=n<m. The last term is scalar times a matrix and is on the displayed side; the numerator products retain the order U_(n-j) B_j. This is the exact recurrence. It uniquely determines the normalized Taylor series. Local holomorphic existence also follows directly by Picard iteration of U=I+integral UG on any closed disc of radius less than1: the k-fold iterated integral is bounded by (Lr)^k/k!, so the series converges uniformly and differentiates to the equation. Its Taylor coefficients are therefore precisely this recurrence.

Use the packet's weights (1,1/128,1/128,1/32,1/64,1/32), and define

    b=max_i sum_(j,k) |(B_k)_ij| w_j/w_i.

For |z|=t<1 the numerator norm is at most b, since every t^k<=1. The reverse triangle inequality gives |1+z^m|>=1-t^m. Along a radial segment z=t exp(i theta), the integral equation and weighted product estimate imply

    ||U(t exp(i theta))||_w
      <=1+integral_0^t b/(1-s^m) ||U(s exp(i theta))||_w ds.

The allowed scalar Gronwall inequality applies to this actual continuous nonnegative norm. For0<=s<1 one has

    1/(1-s^m) <= 1/[m(1-s)] +(m-1)/m.

To verify the sign exactly, multiply by the positive denominator: the difference from1 in the resulting numerator is

    [sum_(j=1)^(m-1) s^j -(m-1)s^m]/m >=0,

because every s^j>=s^m. Integration therefore gives the stated bound on the entire closed disc |z|<=R<1,

    ||U(z)||_w <= K(R)
       =exp(b[-log(1-R)/m+(m-1)R/m]).

Cauchy's coefficient integral is a matrix integral. Applying the weighted norm to that integral, with its explicit factor R^(-n), gives ||U_n||_w<=K(R)R^(-n). For the polynomial through degree N and every |z|<=r<R, summing the geometric tail proves

    ||U(z)-sum_(n=0)^N U_n z^n||_w
       <= tau_N(r;R)
       :=K(R)(r/R)^(N+1)/(1-r/R).

Its actual ij-entry error is tau_N w_i/w_j. After left multiplication by Hc the ij error is bounded by

    tau_N sum_l |(Hc)_il|_+ w_l/w_j.

The exact coefficient balls, point evaluation rounding and any uncertainty of Hc are retained separately through the earlier multiplication formula. The stated N=3000 and R=0.999 satisfy the argument on every enclosing rectangle whose actual maximum radius r is below R. The commonly used bound r<=0.98 is one such domain; a rectangle is not replaced by its midpoint radius.

## B. A simultaneous entrywise enclosure on a convex rectangle

Let z0 be the rectangle centre, rho its Euclidean half-diagonal, and A a nonnegative entrywise bound for |G(z)| over the whole rectangle. Fix any point z of the rectangle and set delta=z-z0. The entire segment z0+t delta lies in the rectangle. Along it,

    d/dt Y(z0+t delta)=delta Y(z0+t delta) G(z0+t delta).

Iterating this integral equation yields an ordered integral of k right factors G at its k-th term. Taking entrywise absolute values bounds every such product by A^k, each scalar path factor by |delta|, and the simplex volume by1/k!. Thus the series is absolutely dominated by

    |Y(z0)|_+ sum_(k>=0) |delta|^k A^k/k!.

The actual difference omits the k=0 term. Since every entry of A^k is nonnegative and |delta|<=rho,

    |Y(z)-Y(z0)| <= |Y(z0)|_+ [exp(rho A)-I]

entry by entry, simultaneously throughout the rectangle. The actual centre enclosure supplies |Y(z0)|_+, so its coefficient and evaluation radii are retained. Add this difference bound to that centre ball. The proof does not use sampled boundary or interior values. A rigorous matrix-exponential evaluation encloses the displayed nonnegative matrix; its rounding uncertainty is retained in the final entrywise radii.

### The additional midpoint-polynomial route

Let p(z)=sum_(j=0)^N c_j z^j, with coefficient discs c_j in [c_hat_j +/- epsilon_j]. At the exact rectangle centre z0, evaluating the midpoint polynomial gives a ball with arithmetic rounding radius eta. The full p(z0) differs from that midpoint evaluation by at most

    sum_j epsilon_j |z0|^j + eta.

For any point z in the rectangle, integrate p' along the segment from z0 to z. The convexity hypothesis retains the whole segment, and the true maximum modulus r of the enclosing rectangle bounds every segment point. Therefore

    |p(z)-p(z0)|
       <=rho sum_(j=1)^N j (|c_hat_j|+epsilon_j) r^(j-1).

Adding these bounds encloses every p(z), with the full coefficient uncertainty present in the derivative term. This can also be written with any certified |c_j| upper bounds. For an analytic series, add its separately established tail at radius r. The same argument applies entrywise to every matrix polynomial. When z0 or a coefficient midpoint is represented by a ball, its evaluation uncertainty belongs in eta, and the derivative and maximum-radius bounds use the full coordinate enclosure. No centre evaluation silently replaces a rectangular domain.

## C. Cusp Frobenius factor and finite commutator inverse

Put L(q)=I+R log q on the chosen punctured-disc branch, where R^2=0. Then L^(-1)=I-R log q and L^(-1)L'=R/q exactly. Substituting the actual factorization G=H L P into

    G'=G(R/q+A/(1+q))

and multiplying on the left by L^(-1)H^(-1) gives

    P'=ad(P)/q+P A/(1+q),
    ad(Q)=Q R-R Q.

This derivation fixes the sign and the side of the A multiplication. With P=sum_(n>=0)P_n q^n and P_0=I, coefficient comparison gives, for n>=1,

    (n I-ad)P_n
       =sum_(j=0)^(n-1) (-1)^(n-1-j) P_j A.               (C1)

Equivalently, after multiplying the differential equation by q(1+q),

    (n I-ad)P_n=ad(P_(n-1))+P_(n-1) A-(n-1)P_(n-1).     (C2)

Both exact recurrences have been derived before target exposure. An implementation of C1 can update the preceding right-hand sum by S_n=P_(n-1)A-S_(n-1), beginning with S_1=A.

The actual commutator satisfies

    ad^2(Q)=-2 R Q R,       ad^3(Q)=0,

by direct expansion using R^2=0. Thus for every positive integer n,

    (n I-ad)^(-1)=1/n [I+ad/n+ad^2/n^2].

Multiplication by nI-ad on either side cancels every intermediate power, leaving I-ad^3/n^3=I. The recurrence therefore has exactly one solution with P_0=I; no resonance or unspecified inverse is assumed.

Use the new cusp weights (100,1,1,1,1,1), with r0=||R||_w and a0=||A||_w. The same exact weighted similarity proves

    ||ad(Q)||_w<=2r0||Q||_w,
    ||ad^2(Q)||_w<=4r0^2||Q||_w.

(The direct formula supplies an even smaller second bound, but the displayed bound is the one used.) Set C0=1+2r0+4r0^2 and gamma=C0 a0. The finite inverse above has norm at most C0/n, because n>=1. Formula C1 then yields

    ||P_n||_w <= gamma/n sum_(j=0)^(n-1) ||P_j||_w.

Define nonnegative c_0=1 and c_n=gamma/n sum_(j<n)c_j. Induction gives ||P_n||_w<=c_n. Subtracting the equations for consecutive n gives

    c_n=(gamma+n-1)c_(n-1)/n.

The resulting power series has radius at least1 by its coefficient ratio and satisfies (1-s)C'(s)=gamma C(s), C(0)=1. Solving this scalar equation yields C(s)=(1-s)^(-gamma). Hence the matrix series P converges normally on every disc |q|<1, differentiates term by term, and solves the displayed P equation. It has P(0)=I and so is invertible near zero. This proves actual existence and uniqueness of the holomorphic Frobenius factor from its recurrence.

For0<s<1, the bound is

    ||P(q)||_w <=K0(s)=(1-s)^(-C0 a0)  on |q|<=s.

Cauchy's matrix coefficient integral and a geometric sum give, through degree N,

    ||P(q)-sum_(n=0)^N P_n q^n||_w
       <=K0(s)(r/s)^(N+1)/(1-r/s),      |q|<=r<s.

The entrywise factor is again w_i/w_j, now with the cusp weights. In particular the stated N=600,s=0.4,r<=0.25 are in the proven domain. On the inner disc r=0.01 use the actual coefficient absolute sums

    |P_ij(q)-delta_ij|
      <=sum_(n=1)^N |(P_n)_ij|_+ r^n + (w_i/w_j)tail_N(r;s).

This is a uniform analytic factor enclosure. Multiplication by H and I+R log q retains their actual matrix entries and the specified logarithm branch; no uniform bound on log q at zero is inferred from the holomorphic-factor bound.

## D. Collar Taylor continuation, all convolutions and actual transition order

Write t=z-z0 and m=5. The exact polynomial denominator and numerator expansions are

    q_j=binom(5,j)z0^(5-j)  for0<=j<=5, with1 added to q_0,
    Btilde_j=sum_(k=j)^4 binom(k,j) B_k z0^(k-j),   0<=j<=4.

For the transition T(t) with T(0)=I, one has

    (sum_(j=0)^5 q_j t^j) T'(t)
       =T(t) sum_(j=0)^4 Btilde_j t^j.

Equating every coefficient gives the exact finite recurrence

    T_(n+1)=[sum_(j=0)^min(4,n) T_(n-j) Btilde_j
             -sum_(j=1)^min(5,n) q_j(n-j+1)T_(n-j+1)]
              /[(n+1)q_0].

Both convolution sums, their bounds and all scalar factors have been retained. q_0 is nonzero because z0 avoids the five denominator roots. For the roots zeta_j=exp((2j+1)pi i/5) let Rloc=(1/2)min_j|z0-zeta_j|. Each factor is nonzero throughout the closed disc |t|<=Rloc. Since 1+z^5=product_j(z-zeta_j), the reverse triangle inequality proves the exact positive denominator bound

    |1+(z0+t)^5| >=Dlower
       :=product_j(|z0-zeta_j|-Rloc)>0.

The weighted norm of the numerator throughout that disc is at most

    Bmax=max_i sum_(j,k) |(Btilde_k)_ij| w_j/w_i Rloc^k.

Therefore the right connection has norm at most M=Bmax/Dlower. Radial Gronwall from T(0)=I gives ||T(t)||_w<=exp(M Rloc) on the whole disc. The matrix Cauchy integral and geometric sum then prove, for any |delta|<Rloc,

    ||T(delta)-sum_(n=0)^N T_n delta^n||_w
       <=exp(M Rloc)(|delta|/Rloc)^(N+1)/(1-|delta|/Rloc).

This establishes the requested N=160 tail when |delta|/Rloc<0.3. The exact geometric distances, denominator lower bound and numerator upper bound are each enclosed by rigorous scalar balls; computations retain the endpoints needed for a positive Dlower and a ratio below0.3. An interval containing zero for a required denominator cannot certify that step.

The actual solution equation fixes the order of continuation: at the next point,

    Y(z0+delta)=Y(z0) T_z0(delta).

Indeed the right-hand side as a function of delta satisfies the original right ODE and has the correct initial value. Successive steps are consequently products on the right in chronological order, Y_start T_0 T_1 ... . Each transition polynomial is evaluated with coefficient and point balls, then its entrywise tail radius (w_i/w_j)tau is added before multiplication. The entrywise product rule from section0 propagates every previous rounding and tail radius. This supplies an actual composition of enclosures along the collar.

## E. Real implicit derivatives and full-domain Hessian enclosure

The actual fixed row selection in the packet forms a4-by-4 real matrix M from the first four lower-five rows of

    (Im Y_i1, Re Y_i1, Im Y_i2, Re Y_i2),

and b from Re Y_i3. The upper row gives c=(Im Y_01,Re Y_01,Im Y_02,Re Y_02) and d=Re Y_03. The exact system is Mv=b and

    h=k(c v-d),          k=96/(625 pi).

The given full-square determinant enclosure excludes zero. Hence M is invertible at every point of that square and the implicit vector v is defined there by the actual inverse, with the stated fixed minor. An approximate row choice has only selected this matrix; its inverse and determinant must be computed rigorously on the whole enclosure.

For either real coordinate a=x,y, differentiating Mv=b gives

    v_a=M^(-1)(b_a-M_a v).

Differentiating again for a,b in {x,y} gives

    v_ab=M^(-1)(b_ab-M_ab v-M_a v_b-M_b v_a).

These formulas follow from the actual product rule, retain the order of the real matrix factors, and handle repeated derivatives with their two identical cross terms. The height derivatives are therefore

    h_a=k(c_a v+c v_a-d_a),
    h_ab=k(c_ab v+c_a v_b+c_b v_a+c v_ab-d_ab).

Because Y and G are holomorphic and Y'=YG, the chain rule supplies

    Y_x=YG,          Y_y=iYG,
    Y_xx=Y(G^2+G'),  Y_xy=iY(G^2+G'),  Y_yy=-Y(G^2+G').

The equality for Y_xx differentiates the right product and therefore uses G^2+G' in precisely that order. Taking the specified real and imaginary coordinate projections gives every M_a,M_ab,b_a,b_ab,c_a,c_ab,d_a,d_ab. These projections are actual real linear maps, so they take rigorous complex balls to rigorous real interval bounds. Rigorous full-square enclosures of Y,G,G', M^(-1), and all displayed products consequently bound every Hessian entry on the whole square. The interval for k includes the actual positive pi value and its reciprocal. No global minimum or symmetry conclusion is part of this isolated analytic certificate.

## Scope and chronology

All formulas and proofs above were written without a target or producer. The separately authored code will compute the supplied root recurrences to degree3000, the cusp factor to degree600, representative actual collar transitions to degree160, and exact independent cross-checks of the commutator and implicit derivative identities. The full old domain subdivision and any stored positivity margins have not been supplied; those numerical data remain the owner's separately rerun certificate scope. The current proof comparison will identify any extra printed route before credit is assigned. This document and the new program/output will be frozen together before the receiving numerical paragraphs are requested.

## Fresh computation completed before target reading

The separately authored program has now passed713 checks at256-bit rigorous ball precision. It computed both root fundamental series through degree3000, the cusp factor through degree600, and actual160-term collar transitions from0.95 to1.20, with reverse transitions enclosing the identity. A local transition inside the convergence disc overlaps the independently summed global series. The code derives every root numerator from the supplied rational connection and cross-checks its initial coefficients against an independently expanded geometric connection series. It verifies the full36-dimensional commutator operator and its finite inverses, and checks all600 cusp coefficients against the independently derived majorant.

The root tails at r=0.98,R=0.999 are enclosed by approximately8.207e-23 and1.161e-22, respectively; the complete rigorous endpoint intervals are in the output. The cusp exact constants are r0=5103/8000, a0=367/512, C0=62452609/16000000 and gamma=22920107503/8192000000. Its degree600 tail at r=0.25,s=0.4 is below2.348e-122. Every displayed decimal here is a deliberately rounded outward summary of the recorded ball interval.

The exact symbolic implicit-derivative test uses a genuinely varying selected determinant and a nonzero Hessian. It computes the real system and the height independently, differentiates that explicit expression, and compares every first and second formula, including the mixed i and yy minus signs. This checks the actual derivative maps without using the old height certificate or its central square data.

During code development, the Python Fraction/Arb interface required an explicit exact rational-to-ball conversion; the mathematical formula was unchanged. An initial constant-height diagnostic was strengthened to a nonconstant determinant/nonzero-Hessian analytic example before this freeze. All final outputs below refer to the successful final code. The full global leaf subdivision and original positivity margins remain outside this isolated scope and are covered by the owner's independent numerical rerun.

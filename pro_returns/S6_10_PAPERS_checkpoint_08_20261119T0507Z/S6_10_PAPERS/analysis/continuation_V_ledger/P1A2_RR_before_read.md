# P1A.2: Chern-root calculation before reading printed Step9

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation; reviewer /root/ledger.

Only the following mathematical input was supplied by the paper owner:
a compact complex fourfold with c1=c3=0 and the Chern numbers
integral c2^2=2 and integral c4=6, with analytic Hirzebruch--Riemann--Roch
available in the form

    chi_y = integral product_(i=1)^4 [ x_i(1+y exp(-x_i))/(1-exp(-x_i)) ].

No P1A.2 printed proof, check summary, producer code, or other reviewer's
RR calculation has been read. This note derives the entire indicated
RR step from that input; it does not claim the preceding geometric or
cohomological proof steps.

## Formal coefficient computation

Give each formal Chern root x_i degree1; the integral takes the
homogeneous degree4 component. The formal power-series quotient is

    Q_y(x) = a + b x + c x^2 + d x^4 + O(x^5),
    a=1+y, b=(1-y)/2, c=(1+y)/12, d=-(1+y)/720.

This follows by multiplying the right-hand side by 1-exp(-x) and
matching it with x(1+y exp(-x)); in particular the coefficient of x^3
is zero. The degree4 partitions possible in the product of four factors
are 4, 2+2, 2+1+1, and 1+1+1+1. Thus its degree4 part is exactly

    a^3 d sum_i x_i^4
    + a^2 c^2 sum_(i<j) x_i^2 x_j^2
    + a b^2 c sum_i sum_(j<k; j,k distinct from i) x_i^2 x_j x_k
    + b^4 c4.

The second and third sums are unordered in the two equal-degree
positions, so no extra factorial is omitted.

## Exact symmetric identities

Let p_k=sum_i x_i^k and c_j=e_j(x1,x2,x3,x4). Newton's identities give

    p2=c1^2-2c2=-2c2,
    p4=c1 p3-c2 p2+c3 p1-4c4=2c2^2-4c4.

Consequently

    sum_(i<j) x_i^2 x_j^2 = (p2^2-p4)/2 = c2^2+2c4.

For the third sum, multiplying c3 by c1 counts the four all-distinct
monomials x1 x2 x3 x4 and precisely the monomials with exponent pattern
2+1+1. Hence

    sum_i sum_(j<k; j,k distinct from i) x_i^2 x_j x_k
      = c1 c3 -4c4 = -4c4.

Substitution proves the universal degree4 expression on c1=c3=0:

    [product Q_y(x_i)]_4
      = (2a^3d+a^2c^2)c2^2
        +(-4a^3d+2a^2c^2-4ab^2c+b^4)c4
      = (1+y)^4 c2^2/240
        +(-1-124y+474y^2-124y^3-y^4)c4/720.

The c4 coefficient is obtained from

    7(1+y)^4/360 - (1-y^2)^2/12 + (1-y)^4/16.

Expanding its numerator over720 gives respectively
(-1,-124,474,-124,-1) in degrees0 through4, including both endpoint
coefficients. This establishes the universal expression explicitly.

## Substitute the actual Chern numbers

With integral c2^2=2 and integral c4=6, the numerator over720 is

    6(1+4y+6y^2+4y^3+y^4)
    +6(-1-124y+474y^2-124y^3-y^4)
      = -720y+2880y^2-720y^3.

Therefore

    chi_y = -y + 4y^2 - y^3,
    (chi(Omega^0),...,chi(Omega^4)) = (0,-1,4,-1,0).

This is the claimed RR output. No step of this calculation relies on the
Hodge table being proved elsewhere or on reading the target proof.

## Independent computation design before opening Step9

The fresh program will recover the Taylor quotient by formal division of
the two exponential series, without entering the coefficients a,b,c,d.
It will multiply the four series at u,-u,v,-v and solve for the two
coefficients of (u^2+v^2)^2 and u^2 v^2. This tests the formula by a
different symmetric specialization. Its completeness as an identity in
c2,c4 follows because a monic quartic with e1=e3=0 is even, and because
u^2+v^2 and u^2v^2 are algebraically independent elementary symmetric
polynomials in u^2,v^2. The mathematical derivation above already proves
the general restricted identity; the program is a fresh exact check.

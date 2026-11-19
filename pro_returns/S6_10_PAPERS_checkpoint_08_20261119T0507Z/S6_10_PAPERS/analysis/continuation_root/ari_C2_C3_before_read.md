# Prereading derivations of ARI C.2.1–2 and C.3.1–2

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.
The four target statements were read with checker metadata removed. Their
printed proofs have not been opened. Cited input statements A.4.1, A.5.1,
B.4.2, C.2.3, ARI C.1.1–3, and the definitions of rho, N, D and kappa were
read. The local finite-fibre kappa definitions were read as cited inputs.
Here rho=(1+i sqrt(3))/2, as fixed in the source; T0=sqrt(3)/2.

## C.2.1: nomes and natural boundary

The actual Albanese markings give q1=exp(-2*pi*i*kappa1) and
q2=exp(-pi*i*kappa2). The finite-fibre definitions are
kappa1=beta(z1)+2*(2-rho)/3 and kappa2=beta(z2)+3*(1-i)/2.
Substitution of the cited exact beta values gives

    kappa1=c+1/2-(3i/(2pi))*log48,
    kappa2=c+3/2-(3i/pi)*log6.

Exponentiating, with w=exp(-pi*i*c), gives
q1=-w^2/48^3, q2=i*w/216 and q1=(27/64)*q2^2.
The cited exact family-domain theorem gives 0<|w|<216, hence precisely
0<|q2|<1. The first Albanese invariant is the cited modular j-series
J(q1), holomorphic for 0<|q1|<1. Its leading q1^{-1} term gives a pole
of order two at w=0. Its domain in w is |w|<48^(3/2).

For completeness, every root of unity is a nonremovable boundary point
of J(q). At tau=a/c+i*y, a primitive SL2Z change of basis sends the
rational cusp a/c to infinity. Modular invariance and J(q)=q^{-1}+O(1)
give growth exp(2*pi/(c^2*y)) as y decreases to zero. The roots of unity
are dense on |q|=1. Any holomorphic continuation across a boundary
point would continue across an arc containing one of these points,
contradicting that divergence. The inverse images under q1=-w^2/48^3
are dense on |w|=48^(3/2), proving the claimed natural boundary.
Since 216^2=46656<48^3=110592, the entire family boundary lies strictly
inside that analytic continuation disc.

## C.2.2: real structure

The cited B.4.2 supplies the exact antiholomorphic parameter map
c -> 1-conjugate(c), the period-2 equivalences, and the actual split
semidirect product on its fixed classes. Thus the equivalence criterion
is c'-(1-conjugate(c)) in 2Z. A self-equivalence exists precisely for
Re(c) in 1/2+Z. In q2=i exp(-pi*i*c)/216 this is exactly q2 real and
nonzero. The order-two generator in the stated split group gives an
actual involution; the existence of an involution is not inferred from
a self-equivalence without that cited splitting.

## Common differential identities for C.3

Use c0=pi^2 E2/3, g2=4*pi^4 E4/3 and g3=8*pi^6 E6/27. A prime on
these quantities denotes d/dtau. The Ramanujan equations are

    c0' = i/(2pi)*(c0^2-g2/12),
    g2' = (2i*c0/pi)*g2-(3i/pi)*g3,
    g3' = (3i*c0/pi)*g3-i*g2^2/(6pi).

For H=partial_z log(theta1(z,tau)) and wp=Weierstrass(z,tau), the
opened heat/product normalization gives H_z=-wp-c0 and

    wp_tau=(wp^2-c0*wp)/(pi*i)+H*wp_z/(2pi*i)+i*g2/(6pi).

Indeed differentiate H_tau=(-wp_z-2H(wp+c0))/(4pi*i), use
wp_zz=6wp^2-g2/2, and substitute the equation for c0'.
Along the zero branch wp(mu,tau)=0, with p=wp_z(mu,tau), this gives

    mu' = iH/(2pi)-i*g2/(6pi*p),
    p' = 3i*c0*p/(2pi)+i*g2^2/(12pi*p),
    H' = i*p/(4pi)+i*c0*g2/(6pi*p).

The first line is used away from the double half-period root; the
half-period computation below uses the cubic equation directly.

## C.3.1: square point and quartic norm

Let e(tau)=wp((1-tau)/2,tau), G=g2(i), delta=tau-i. At i,
e=0, c0=pi, g3=0. Differentiating 4e^3-g2*e-g3=0 and the displayed
modular system gives

    g2'=2iG, g3'=-iG^2/(6pi),
    e'=iG/(6pi), e''=-G/(2pi).

For h=mu-(1-tau)/2, the local wp expansion is

    wp=e+(3e^2-g2/4)h^2+(3e^3-e*g2/4)h^4+O(h^6).

Solving wp=0 for delta=a*h^2+b*h^4+O(h^6) gives
a=-3*pi*i/2, b=-9*pi^2*i/8. Its inverse is
h^2=(2i/(3pi))*delta+delta^2/(3pi)+O(delta^3), and taking the
chosen holomorphic square root gives the factor 1-i*delta/4.

The half-period theta shift cancels its exponential against the metric
factor, so L=log N=Re F(h,tau)-pi*(Im h)^2/Im tau, where
F=log(theta3(h,tau)/eta(tau)). At (0,i),

    F=.5log2, F_h=0, F_hh=-pi, F_hhhh=G/2,
    F_tau=0, F_hh,tau=-i*pi/2-iG/(8pi),
    F_tau,tau=-G/(24pi^2).

The identity F_tau(0,tau)=i*e(tau)/(4pi) follows directly from
the heat equation and eta'/eta. Substituting delta=a*h^2+O(h^4)
in its holomorphic Taylor expansion gives quartic coefficient
-3*pi^2/8-5G/192. The metric term contributes

    -pi*(Im h)^2
    -3*pi^2/4*|h|^2*Re(h^2)
    +3*pi^2/8*(|h|^4+Re(h^4)).

The Re(h^4) terms in pi^2 cancel. Thus

    L=.5log2-pi|h|^2/2+3pi^2|h|^4/8
       -3pi^2|h|^2 Re(h^2)/4-5G Re(h^4)/192+O(|h|^6).

Both the root equation and this shifted norm are invariant under h -> -h,
so the next possible total degree is six. Inverting h^2 and using
D_part=(6/pi)log(N/(2sqrt3)) yields

    D_part=D_* -2|delta|/pi
       +(|delta|^2+|delta| Im(delta))/pi
       +5G Re(delta^2)/(72pi^3)+O(|delta|^3).

The mixed term includes -|delta|Im(delta)/pi from the quadratic
term's inversion and +2|delta|Im(delta)/pi from the quartic term.
This accounts for its sign without a numerical fit.

## C.3.2: equianharmonic point

At rho, g2=0, g3=-p^2, c0=pi/T0 and H=2pi*i/3 for the specified
third-period point. The latter value follows from the 3-torsion elliptic
symmetry and H_z=-wp-c0, or from the theta translation law at that
point. It is an explicit input to verify against the source before
closing the check. The modular and root systems give

    mu'=-1/3, mu''=3p/(8pi^2),
    mu'''=9i*p/(16pi^2*T0),
    g2'=3i*p^2/pi, g2''=-15*c0*p^2/pi^2,
    g3'=-3i*c0*p^2/pi.

These give exactly the displayed quadratic and cubic coefficients of
mu. Substitution into t=g2^3/(g2^3-27g3^2) gives

    t=i*p^2*delta^3/pi^3*(1+3i*delta/(2T0)+O(delta^2)).

For the norm L=Re log(theta1(mu,tau)/eta)-pi*(Im mu)^2/T,
differentiate the actual metric expression. With r=Im(mu)/T,

    partial_tau partial_bartau L
      =-pi/(2T)*|mu'-r|^2.

Write mu=(2-tau)/3+h, h=A delta^2+O(delta^3), A=3p/(16pi^2).
Then mu'-r=2A delta+O(|delta|^2), and the radial quartic coefficient
of L is -pi|A|^2/(2T0)=-9|p|^2/(512*pi^3*T0).

The harmonic leading coefficient is also fixed exactly. Put
K=H+2pi*i*r. The heat equation gives

    2 partial_tau L=i*K^2/(4pi)-i*K*g2/(6pi*p).

Here K=i*p*delta/(4pi)+O(|delta|^2) and
g2=3i*p^2*delta/pi+O(delta^2). Its quadratic coefficient is
7i*p^2/(64pi^3), giving harmonic term (7/192)Re(t).

The theta norm is invariant under the actual SL2Z basis change:
the exponential multiplier in theta1/eta is canceled by the
transformed Gaussian, and integral translations and mu -> -mu
leave its absolute value unchanged. Hence L descends to the modular
parameter t. In a local root coordinate u with t=u^3, its real-analytic
expansion is invariant under u -> exp(2pi*i/3)u. Up to degree four,
the only remaining mixed monomial is |u|^4; the lower |u|^2 term
vanishes by the computed curvature. Since
|t|^(4/3)=|p|^(8/3)|delta|^4/pi^4+O(|delta|^5),

    L=.25log3+7Re(t)/192
       -9pi|t|^(4/3)/(512*T0*|p|^(2/3))+O(|t|^(5/3)).

The value .25log3 is the cited C.1.2 special-value input. Multiplication
by 6/pi gives every displayed D_part coefficient. Along real t of
opposite signs, its nonzero linear term has opposite signs and dominates
the order-4/3 error, proving that the point is neither a local maximum
nor a local minimum. No conditional theorem or numerical inference is
introduced by this calculation.

## Gates before comparison

The algebraic derivations are complete. Exact source checks remain for
the quoted Ramanujan equations, modular/theta transformations and the
specified H value at rho. Fresh symbolic code will verify each displayed
jet and the mixed-term coefficients. These are recorded gates, not
claims of completed source or computational verification.

## Closure of the third-period H gate, still before the target proof

Use the full-period quasi-period convention eta(1)=c0 and
eta(tau)=c0*tau-2*pi*i. The homothety law for the zeta function on
the invariant square/equianharmonic lattice is zeta(a*z)=a^{-1}zeta(z).
At tau=i it gives eta(i)=-i*c0, hence c0=pi by Legendre. At tau=rho
it gives eta(rho)=rho^{-1}c0=(1-rho)c0, hence
c0*(2rho-1)=2*pi*i and c0=pi/T0.

Now omega=rho-1 has order three and, for mu0=(2-rho)/3,
omega*mu0=mu0+(rho-1). Therefore

    (omega^{-1}-1) zeta(mu0)=c0*(rho-1)-2*pi*i.

Substituting omega^{-1}=-rho and c0*(2rho-1)=2*pi*i gives
zeta(mu0)=c0*(rho+1)/3. Since H=zeta-c0*z,
H(mu0)=c0*(2rho-1)/3=2*pi*i/3, as required. These are explicit
lattice and quasi-period morphisms. The calculation closes the
previous H-value gate before comparison with the printed proof.

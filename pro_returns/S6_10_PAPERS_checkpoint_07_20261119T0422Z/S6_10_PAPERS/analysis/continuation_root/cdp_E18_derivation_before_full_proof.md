# E18: derivation recorded before opening the full receiving proof

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation.

## Scope of independence

The statement of E18 and the statements of E5/E8 were extracted. The existing
checker summary of E18 was visible, and a search displayed several isolated
lines of its proof, including the proposed half-period and the nonzero
determinant. Accordingly this document supports a targeted proof check and a
new computation, not a claim that the whole counterexample was independently
discovered or that every printed step had been unseen. The full receiving
proof has not yet been opened. Its missing source-matching obligation is being
checked against opened primary NIST formulas.

## Derivation from the named theta expression

Write theta(z,tau)=theta_1(pi*z|tau), q=exp(pi*i*tau),
Q=q^2, and h=theta_z/theta. The change of variables in NIST DLMF 20.13.1
gives theta_tau=theta_zz/(4*pi*i). The eta product gives
(log eta)'=pi*i*E2/12. Comparing the Laurent expansion at the lattice
origin in the elliptic difference -h_z-wp gives pi^2*E2/3. Thus
h_z=-wp-pi^2*E2/3. For b=(i/pi)log(theta(mu,tau)/eta(tau))+constant,

    b'=(h_z+h^2)/(4*pi^2)+E2/12+i*mu'*h/pi
      =(h^2-wp)/(4*pi^2)+i*mu'*h/pi.

The determinant of [[1,mu'],[mu',b']] is therefore exactly

    -(mu'-i*h/(2*pi))^2-wp/(4*pi^2).

This identity contains an actual extra elliptic term. The omitted term
vanishes on the original branch wp(mu,tau)=0, as that branch states.

For the constant section mu=1/2 the theta shift is an even theta_2 function,
so h=0. The quotient R=theta_1(1/2,tau)/eta(tau) is

    R=2*q^(1/6)*product_{n>=1}(1+q^(2n))^2.

At tau=i every factor is positive and R>2*exp(-pi/6)>1 (pi<4 and
exp(2/3)<2 suffice for the latter bound, or the sharper elementary bounds).
Choose b=(i/pi)log R+i. Its imaginary part is positive at i and hence in a
small neighborhood. The symmetric period matrix has positive imaginary
part there. The raw four columns (1,0),(0,1),(tau,mu),(6mu,6b) generate a
full rank-four lattice: replacing the last by (mu,b) gives a standard
positive period matrix. The new vector has exact order six modulo the raw
lattice, since its second imaginary coordinate forces its coefficient
to be a multiple of six, after the first imaginary coordinate kills the
tau-column coefficient. Identity on C^2 gives the degree-six finite isogeny.

Differentiating the convergent product gives at mu=1/2

    b'=-1/6-4*sum_{n>=1} n*Q^n/(1+Q^n).

At tau=i this is strictly negative, so already the product, without any
elliptic normalization convention, proves the alleged square-only value
zero is false. DLMF 23.6.2 with omega_1=1/2, together with theta_3^4=
theta_2^4+theta_4^4, identifies the same value as
-(theta_3^4+theta_4^4)/12=-wp(1/2)/(4*pi^2).

The quotient theta(z-1/2)/theta(z) has translations 1 and -1 under z+1
and z+tau, respectively, by the theta quasi-periodicity formulas. Its
divisor is [1/2]-[0]. This specifies the line bundle and linearization used
in the local construction. The cohomology boundary for a rank-two
Kodaira--Spencer tensor maps 1 to that tensor in Lie(F) tensor H^1(O_F),
so has rank one. Its next map is the wedge map eta -> kappa wedge eta and
has rank two; the intervening ranks of the tangent direct images are
2, 3, 1. This is a local statement over the smooth base.

## Newly implemented computation

Use exact rational coefficient arrays and the divisor-sum expansion of
the logarithmic product to compare with the fourth powers of the two
theta series through order 120 in q. This is a finite exact coefficient
check; the analytic identity and its nonzero value are justified above,
not by truncation. A separate symbolic elimination verifies the general
determinant identity without evaluation.

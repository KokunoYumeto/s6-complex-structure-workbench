# E18: complete derivation before reading its printed proof

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation; reviewer /root/ledger.

## Exact input history

The statement in papers/II/revisions/cdp_st_E18.tex was extracted alone.
It asserts that the square-only expression from Lead9 fails for arbitrary
local elliptic sections and linearizations, points to the exact formula
cdp:eq:E-theta-general, and retains the actual original family's square
formula on its stated locus wp(mu,tau)=0. That revision contains no
StatementRecord or local Uses field.

The cited equation and its definitions were then located in the E8
statement. A display-extraction error also exposed the preceding E7 proof
tail and E8's pre-continuation metadata summary, which names the heat,
eta, and logarithmic theta derivative identities. No E18 proof text,
root E18 continuation comparison, or root E18 program has been opened.
Accordingly this is an independent derivation of E18 from its cited E8
input; it makes no independence claim for the proof of E8 itself.

The supplied period convention is

    Omega(tau) = [[tau, mu(tau)], [mu(tau), B(tau)]],
    B=beta/6=(i/pi) log(theta_1(mu,tau)/eta(tau)) + C,

where theta_1 is normalized in its first argument to periods1 andtau,
the logarithm is a local holomorphic branch, and C is constant. Write
h=partial_mu log(theta_1), and use the Weierstrass function for
Lambda_tau=Z+tau Z. All derivatives below follow this normalization.

## 1. Derive the exact formula

For this theta normalization the heat equation is
partial_tau theta_1=(4 pi i)^(-1) partial_mu² theta_1.
The standard eta and theta/Weierstrass identities in the same periods are

    eta'/eta = (pi i/12) E2,
    partial_mu h = -wp(mu,tau) - (pi²/3) E2.

These are named classical inputs, rather than additional new claims
of E18. Their normalization can also be checked directly: termwise
differentiation of the normally convergent theta series proves the
heat equation; logarithmic differentiation of eta's product gives
the E2 series; the difference of -partial_mu h andwp is elliptic
and holomorphic, hence constant, and its Laurent constant ispi²E2/3.

The chain rule gives

    B' = (i/pi) [h mu' + (theta_tau/theta) - eta'/eta]
       = (i/pi) h mu' + (partial_mu h + h²)/(4 pi²) + E2/12
       = (i/pi) h mu' + (h² - wp)/(4 pi²).

The two E2 terms cancel exactly. Since det(Omega')=B'-(mu')²,

    det(Omega') = -(mu' - i h/(2pi))² - wp(mu,tau)/(4pi²).

This is the referenced general equation. The logarithm branch changes
B by a constant and therefore does not alter the derivative. A further
nonconstant change of the specified linearization would add its
derivative; no such change is made or needed for this counterexample.

## 2. A concrete local section with zero square term

Take tau0=i, and on a small simply connected neighbourhood U ofi in
the upper half-plane take the actual elliptic section mu(tau)=1/2.
It is the nonzero two-torsion section represented by the constant
complex number1/2 in C/(Z+tau Z). Thus mu'=0.

The shift identity theta_1(1/2+z,tau)=theta_2(z,tau), with first
argument normalized to period1, and evenness oftheta_2 give
h(1/2,tau)=0. The denominator theta_2(0,tau) is nonzero neari;
this also follows from the positive product at tau=i and continuity.
Consequently the proposed square-only expression is identically zero
onU for this section.

## 3. Prove the omitted term is nonzero, without a numerical estimate

For the square lattice Lambda=Z+iZ, its normally convergent defining
series gives wp(iz;i)=-wp(z;i) after the literal bijection
Lambda→Lambda, omega→i omega. Evenness and lattice periodicity
follow from the same series and its derivative.

Set z0=(1+i)/2. Since iz0=z0-1, periodicity and the displayed
rotation law give wp(z0)=0. Also -z0=z0-(1+i); oddness and
periodicity ofwp' give wp'(z0)=0. Hence z0 is a zero of order
at least two. The elliptic functionwp has exactly one double pole
onC/Lambda, at0, and no other pole. Its zero divisor therefore has
degree two. One can see the equality of zero and pole degrees by
integratingwp'/wp on a fundamental parallelogram, whose opposite
boundary integrals cancel. Thus z0 accounts for the complete zero
divisor. The points1/2 andz0 are distinct moduloLambda, so

    wp(1/2;i) != 0.

The exact determinant at tau=i is therefore

    det(Omega'(i)) = -wp(1/2;i)/(4pi²) != 0,

while its alleged square-only value iszero. This is a genuine local
counterexample, not a comparison of approximate floating-point values.

## 4. Realize the data by an actual local period family

Choose C=i and the logarithm that is real on the positive value
theta_2(0,i)/eta(i). At tau=i let q=exp(-pi). The convergent products
give the exact positive ratio

    theta_2(0,i)/eta(i)
      = 2 q^(1/6) product_{n>=1}(1+q^(2n))².

Its logarithm is greater than log2-pi/6. Therefore

    Im B(i) = 1 + (1/pi) log(theta_2(0,i)/eta(i))
            > 5/6 + (log2)/pi > 0.

Since mu=1/2 is real, ImOmega(i) is the positive diagonal matrix
diag(1,ImB(i)). After shrinkingU, the symmetric holomorphic matrix
Omega has positive definite imaginary part throughoutU. The explicit
quotient C²/(Z²+Omega(tau) Z²) then gives an actual local holomorphic
family of polarized complex two-tori with exactly these periods.
The theta and eta factors remain nonzero there, so the prescribed
linearization and logarithm exist. This verifies the period-family
scope of the counterexample, rather than merely substituting unrelated
formal variables into the determinant identity.

## 5. Preserve the actual original-family assertion

On the original period branch specified in the statement, the cited
equationwp(mu,tau)=0 removes precisely the extra term in the exact
formula. The square formula therefore holds on that stated branch.
The counterexample's section1/2 at tau=i has nonzero wp and hence
does not satisfy that branch equation. The exact inclusion of the
branch into the local period domain is the substitutionwp=0 in the
derived formula; no assertion about all other linearizations is made.

## Scope of the derivation

This proves every assertion of E18 as stated: a local period-family
counterexample to the unqualified square formula, the exact corrected
theta-expression formula, and its restriction to the stated original
wp=0 branch. The proof and the half-period counterexample were written
before opening the printed E18 proof. The next step is an exact
comparison with that proof and its source locator, followed by checks
of the classical normalization references.

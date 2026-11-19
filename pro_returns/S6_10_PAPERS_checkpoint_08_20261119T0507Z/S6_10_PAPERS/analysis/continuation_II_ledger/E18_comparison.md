# E18 receiving comparison, 19 November 2026

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation, reviewer /root/ledger.

## Preserved order and exact scope

`E18_prederivation.md` was saved at 04:43:07 UTC, before the E18 printed
proof or root's E18 comparison/program was opened. Its original SHA-256 is
`e819e389de807b0814d58cfb84173acd52d66692870cfe8802738c2572950114`;
the original file and its receipt are preserved without retrospective edits.

The prederivation completely establishes the stated determinant counterexample
from the cited E8 identity and definitions: the exact chain-rule formula, its
nonzero half-period discrepancy, existence of a positive symmetric-period
family, and the restriction to the original branch wp(mu)=0. The proof uses
the square lattice's actual rotation and its divisor of zeros to establish
nonvanishing, instead of the printed proof's theta-constant evaluation.

Input-history correction: the extractor took the proposition environment but
missed a separate `Uses` macro immediately after it. Contrary to the statement
in the original note, the revision does contain that macro; it names the
general theta equation and E5. The first equation extractor also displayed
the tail of E7 and E8's old checker narrative, including the names of the
heat/eta/logarithmic derivative identities. No E18 proof was exposed there.
This limits the independence claim to E18 using its cited E8 input; it is
not a prereading reproof of E8. The exact earlier note is retained so that
the correction cannot conceal the order of exposure.

The printed proof additionally develops the original elliptic-line quotient,
its index-six isogeny to the symmetric-period family, and all direct images.
Those expansions were not fully written in the prereading note. Their checks
below occurred after reading them and are targeted proof checks. Thus this
receipt does not close a gate requiring prereading rederivation of every
printed expansion merely by calling the E18 statement's alternative proof
complete. No owner-completed whole-row gate is asserted here.

## Comparison of the counterexample

The printed choice is exactly the independently chosen mu=1/2, C=i, tau=i.
Both computations give

    det(Omega') = -(mu' - i h/(2 pi))^2 - wp/(4 pi^2).

The printed nonzero value is -(theta3(0,i)^4+theta4(0,i)^4)/12.
In DLMF notation, e1=pi^2(theta2^4+2 theta4^4)/(12 omega1^2),
with omega1=1/2. Substituting theta3^4=theta2^4+theta4^4 gives the
printed coefficient exactly. Its sign and normalization agree with the
prederived square-lattice argument. The assertion for the original family
follows by the exact substitution wp=0; no assertion that this equation
holds for every elliptic section is made.

The positive-product inequality in printed Step 1 is valid: log 2 > 2/3
by strict midpoint convexity of 1/x integrated from 1 to 2, and pi<4;
therefore log 2 > pi/6. The remaining factors of the theta2/eta product
are greater than one. This strengthens the prereading note's sufficient
bound Im(v)>5/6+log(2)/pi to the printed Im(v)>1.

## Targeted checks of the explicit morphisms and extra cohomology

For the elliptic-line quotient, exponentiation a=exp(2 pi i z2) kills
the second unit period. The other generators act as (z,a)->(z+1,a)
and (z,a)->(z+tau,-a). The ratio theta1(z-P)/theta1(z), P=1/2,
has divisor P-O and multipliers 1 and exp(2 pi i P)=-1. These are
the actual transition functions of the displayed quotient. The last
generator (3,beta) projects to zero in the base elliptic curve and to
the contraction exp(2 pi i beta) in the line, since Im(beta)>0.

For the comparison to the symmetric lattice, the inclusion of the old
lattice in the new one, in their specified ordered bases, is exactly
diag(1,1,1,6). Its cokernel is Z/6. Identity on C^2 descends to the
degree-six isogeny. On the Lie spaces it is identity; on the integral
period local systems it is this inclusion, which becomes an isomorphism
over C. The induced map of holomorphic de Rham bundles respects the Hodge
subbundles and their Gauss-Manin connection, so the induced KS maps
commute with these actual invertible comparisons. This proves the
claimed equality of KS ranks without replacing the original lattice
silently by the enlarged one. The real period determinant is
-6 Im(tau) Im(v) in the recorded row/column order, so the lattice is full.

For cohomology, put V=H^0(T_fibre) and W=H^1(O_fibre), both dimension2.
Translation-invariant forms give H^q(O)=wedge^q W and
H^q(T_relative)=V tensor wedge^q W. With kappa's columns k1,k2,
the boundary W -> V tensor wedge^2 W has columns (-k2,k1),
so its determinant equals det(kappa). At the displayed half-period
kappa=diag(1,-wp/(4 pi^2)); both boundaries consequently have their
claimed ranks on a sufficiently small disc. The long exact direct-image
sequence then gives ranks 2,3,1 for T_total in degrees 0,1,2:
the first is V, the second is coker(C -> V tensor W), and the third
maps isomorphically to wedge^2 W. Higher relative cohomology vanishes.
The bundles and quotient bundles are holomorphic of constant rank and
trivial on this disc. The Stein Leray spectral sequence therefore gives
the displayed spaces of sections for total-space cohomology, rather
than finite dimensions for O(Delta). These are post-reading targeted
checks, not prereading proof claims.

## Primary formula matching

Opened directly from NIST DLMF on 19 November 2026:

- https://dlmf.nist.gov/20.2 : equations20.2.1, 20.2.2 and20.2.12,
  the Fourier series and half-period translation. The change of argument
  is exactly vartheta(z,tau)=theta(pi z|tau).
- https://dlmf.nist.gov/20.13 : equation20.13.1 has coefficient
  -i pi/4 in the DLMF argument. Substitution of pi z produces
  (4 pi i)^(-1) in the period-one argument used in E18.
- https://dlmf.nist.gov/20.4 : equations20.4.3--5 give the theta
  constant products with nome exp(pi i tau).
- https://dlmf.nist.gov/23.17 : equation23.17.8 gives the eta
  product with q^(1/12). Cancellation gives precisely the exponent1/6
  in theta2/eta, as printed.
- https://dlmf.nist.gov/23.6 : equation23.6.2, with omega1=1/2,
  and https://dlmf.nist.gov/23.3 equation23.3.9 identify wp(1/2)
  with e1 at the same periods.
- https://dlmf.nist.gov/20.7 : equation20.7.5 is the theta fourth-power
  identity needed to match the printed numerator.

The elementary eta derivative also follows by differentiating the normally
convergent eta product; the heat identity follows termwise from the theta
series. No new source theorem about the original family's wp=0 equation
is inferred from these formulas.

## New independent computation and disposition

`code/continuation_II_ledger/E18_exact_algebra.py` was written after the
prederivation and printed-proof comparison, without opening the producer
program or root's E18 program. It checks the E2 cancellation, exact square
correction, half-period specialization, Smith form/index-six lattice map,
real lattice determinant, cohomology boundary determinant and line
multiplier. Its output is `E18_exact_algebra.output.json`. These finite
exact computations support the identified algebraic steps; they do not
replace the analytic arguments or certify unexamined proofs.

No change to the mathematical E18 statement is indicated by this check.
The row remains proved on the source's established mathematical basis,
while the strict every-printed-step prereading gate is not asserted closed
by this receipt. Root owns the source and the overall Paper II gate.

# ARI C.2.1--2 and C.3.1--2: continuation comparison

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

## Reading order and mathematical scope

The target statements and their cited input statements were extracted with
StatementRecord metadata removed. The complete file
`ari_C2_C3_before_read.md` was written before opening the four target
proofs. Its final section resolves the equianharmonic logarithmic theta
derivative using the exact CM lattice map and zeta quasi-periods.
The subsequent comparison used the complete printed proofs in
`papers/I/07_arithmetic.tex`.

* C.2.1: all new mathematical steps match. The cited Albanese lattices
  determine the actual positive-imaginary period representatives; their
  exponential maps give both signs and the factor 27/64. The rational-cusp
  modular map and density argument give the larger natural boundary, and
  216 squared divided by 48 cubed equals 27/64. The prior exact-period
  classification is an expressly cited input, not a new result of this row.
* C.2.2: the prereading argument derives the stated conclusion from the
  cited complete B.4.2 equivalence and split automorphism statement. The
  printed proof additionally repeats explicit four-by-four reflection
  intertwiners, affine correcting cocycles and their Laurent gluing.
  Those repeated steps were not independently written before being read
  here. This event is therefore targeted; the strongest every-step gate
  remains open. No mathematical fault is asserted from that protocol gate.
* C.3.1: the implicit cubic calculation, even root coordinate, all theta
  derivatives, real quartic norm and inverse-coordinate expansion match.
  The prereading derivation obtained e'' by the cubic and Ramanujan
  equations, whereas the printed proof also gives the exact modular
  transformation calculation. Both yield -G/(2 pi). In particular the
  positive mixed |delta| Im(delta) coefficient is reproduced exactly.
* C.3.2: the zero-branch vector field, H value at the 3-torsion point,
  third derivative, coarse modular coordinate, harmonic cubic and negative
  radial quartic all match. The actual local stabilizer is
  gamma(tau)=1-1/tau, and the zero section transforms as
  mu(gamma(tau))=(1-mu(tau))/tau. This is now printed explicitly before
  the invariant-monomial argument. The coefficient of Re(t) is 7/192
  for log N and 7/(32 pi) for D_part.

## Fresh computations

`code/continuation_root/ari_C2_C3_fresh.py` was written without reading
the producing computation programs. Its 34 checks pass exactly under
SymPy: the normalized differential vector field, the preserved root
cubic, both half-period derivatives, the forward and inverse jets, the
real quartic polynomial, the mixed term, the equianharmonic derivatives,
the cubic and quartic modular coefficients, and the CM lattice morphism.
It also generates 81 exact Fourier coefficients for each Eisenstein
series independently by divisor sums and checks all three Ramanujan
equations coefficient by coefficient. This supplies an independent
algebraic method for coefficients previously checked by numerical theta
evaluation. The analytic remainder orders are justified in the written
derivation, not inferred from a finite series check.

The initial execution reached the final CM calculation with a symbolic
`0*I` residual whose unsimplified structural equality test failed.
Applying the algebra system's exact simplification before comparing to
zero corrected that checker implementation. No displayed coefficient
was changed. The complete successful output and stdout are retained.

## Opened classical sources and credit

The primary Erban--Van Gorder paper, Research in Number Theory (2021)
7:25, DOI10.1007/s40993-021-00240-6, was opened and its first page
visually read. Equations(1.1)--(1.4) give the E2/E4/E6 normalizations
and Ramanujan system. Paper I now prints the exact conversion
x=exp(2 pi i tau), d/dtau=2 pi i x d/dx and the receiving g2/g3/E
normalizations.

The NIST primary pages were opened for equations20.13.1,
20.7.26 and20.7.30,23.5.2--3 and23.18.4--6. The receiving theta
argument is pi z and its full lattice periods are 1,tau. The square
period value follows from23.5.3 with 2 omega1=1 and the exact cubic
identity g2=-4(e1 e2+e2 e3+e3 e1). The previous short beta-integral
paragraph has been replaced by that exact source-and-normalization
calculation; its original text remains in the unchanged compendium
and the checkpoint06 source. This follows the instruction to cite
classical inputs at their exact opened loci.

Renewed searches against the original AC26 PDF extraction, E26 and both
DGKX versions are preserved with hashes and every query in
`ari_C2_C3_credit_search.json`. The queries were 216, 27 followed by64,
48 with exponent notation, natural boundary, Albanese, antiholomorphic,
equianharmonic,7/192 and lemniscatic. None returned a matching passage.
This is a bounded search result, not an exhaustive absence claim.
The DGKXv1 exact-period theorem was separately reopened at source label
p2:thm:exact-period (Theorem1.4): it gives the 2Z parameter equivalence
and Aut=C*. That positive antecedent remains credited. The calculations
of the additional nomes, continuation radius and two higher local
expansions are the receiving results at this search scope.

## Row gates

C.2.1, C.3.1 and C.3.2 have complete prereading rederivations, fresh
exact computations and opened known-input receipts. C.2.1 also has the
required renewed main-result credit search. C.2.2 retains its additional
explicit-reflection prereading gate and is recorded only as targeted.

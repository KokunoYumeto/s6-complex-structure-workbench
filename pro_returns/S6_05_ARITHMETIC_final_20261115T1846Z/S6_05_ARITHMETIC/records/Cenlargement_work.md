# CM-stable enlargement: exact audit

Date: 15 November 2026. Main statement: C.7.10 in `sections/C_cm_enlargement.tex`.

## What is proved

For E: y^2+y=x^3-38x+90, P=(0,9), Q=2P=(4,-2), beta=i sqrt(19), the fibre product G_Q times_E G_(beta Q) has a CM endomorphism B with B^2=[-19]. Its group of algebraic characters is zero, and its algebra of quasi-endomorphisms is exactly Q(beta). The compatibility uses dual endomorphisms: beta^dagger=-beta; the torus map is (t1,t2) -> (t2^-1,t1^19). These are actual algebraic maps.

The algebraic logarithm-coordinate matrix is

    B = [[beta,0,0],[a,0,-1],[beta*a,19,0]],  a=-21*beta/703.

An explicit algebraic compact lift of Q in the antisymmetric extension is

    r2 = -165/74 + (1839/1406)*beta.

The proof uses the exact CM multiplication rational functions, not the unverified lift conventions of Bertrand's slide criterion. The degree-nine kernel polynomial, its rational map, the norm-twenty kernel polynomial and the exact identity determining the branch are all printed in the manuscript. `code/C7_cm_explicit.gp` verifies the polynomial identities over Q(beta), including the map equation, coprimality, kernel product, divisibility and squarefreeness. It also checks the analytic formulas to 110 digits. The analytic discrepancies are approximately 10^-114, but the exact identities are what prove the statement.

The model has s2=-2. With real elliptic logarithm u and D=zeta(u)-s2*u, the second lift has logarithm v2=-beta*u*D+a*u. If N(P) were algebraic, the first compact lift would have logarithm v1=u*D-pi*u^2/A. Hence the complex-linear minus-beta projector would give

    Pi_minus U = -pi*u^2/(2*A) * (0,1,beta).

Its first torus exponential is exactly the real Gaussian in the norm. This isolates the missing factor in a Lie coordinate, but does not prove its exponential algebraic. Pi_minus is not the differential of an algebraic quasi-endomorphism. Every actual quasi-endomorphism is a0+b0*B with rational a0,b0 and conjugate eigenvalues. Its distance to the spectral values (0,1) is at least 1/2. Thus rational polynomials, compositions, isogeny inverses and their complex operator-norm limits do not realize or approximate the desired projector. There is also no algebraic character to a one-dimensional torus, even after isogeny.

## Code and validation

- `code/C7_cm_kernel.gp`, `.out`: exact factorization of psi_19 at the model, degree-nine CM kernel factor.
- `code/C7_cm_explicit.gp`, `.out`: exact rational-map and witness checks; 110-digit independent analytic check.
- `code/C7_cm_enlargement_check.py`, `.out`: symbolic matrix square, idempotent and Gaussian projection residuals, all exactly zero.
- `code/C7_enlargement_typeset_check.out`, `records/Cenlargement_typeset_check.out`: isolated compilation, four pages, no overfull box.
- `results_Cenlargement.csv`: standard-schema statement registration.

The failed first execution is deliberately preserved as `code/C7_cm_explicit_attempt1.gp` and `.out`. Its error was the PARI syntax `deriv(cmh,2)`, where the second argument denotes a variable rather than the derivative order. The corrected run uses `deriv(deriv(cmh))` and exits with a nonzero code if an exact assertion fails. The failed run's undefined-variable numerical output is not used.

## Consequence for the main question

This exact witness is an algebraic compact point in an antisymmetric extension, not a counterexample to the diagonal norm conjecture. It shows explicitly why a compactness argument must distinguish the two extensions. The Gaussian norm N(P), at this curve of conductor 361 and at the other rational CM curves, remains undecided unconditionally. The remaining implication is not a missing rational coefficient: it is the unsupported inference from algebraicity of exp(U) to algebraicity of exp(Pi_minus U) for a projector that has no algebraic group origin.

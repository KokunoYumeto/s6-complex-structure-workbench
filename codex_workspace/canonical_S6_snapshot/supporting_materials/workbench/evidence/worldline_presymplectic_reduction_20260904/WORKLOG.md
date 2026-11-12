# Task log: worldline presymplectic reduction

## Delegated objective

Independently compute the complete presymplectic/Hamiltonian reduction of

\[
S[x,Z,e]=\int\left(\langle p_\alpha(Z),\dot x\rangle_L-
\frac e2\bigl(\det p_\alpha(Z)-m_0^2c^2\bigr)\right)d\tau
\]

under the time-dependent left `SU(3)` action, treating positive mass, nonzero
rank-one massless momentum, and `Z=0` separately and retaining every original
constant and sign.  Required outputs were a standalone line-indexed TeX proof,
deterministic symbolic checks, and an audit receipt in this directory, without
editing canonical sources.

## Added evidence request

After the primary reduction was complete, compare source lines 875--1654 of
`exact_lorentz_observation_bridge.tex` with the exact reduction, especially its
composite momentum, constrained quotient, threshold, spectra, and worldline
action.  Identify every qualification caused by irregular strata and separate
an algebraic threshold from a dynamically generated interacting gap.

## Chronology and mathematical decisions

- Fixed the convention `Omega=-d Theta` with
  `Theta=<p_alpha(Z),dx>_L`; no coordinate or constant was normalized away.
- Derived the Euler--Lagrange equations before quotienting.
- Proved the exact Gram quotient and its stabilizers at ranks two, one, and
  zero.  Distinguished the rank-one intrinsic tangent kernel from four
  transverse rank-opening directions.
- Computed the massive characteristic quotient and fixed the cotangent sign by
  an exact pullback calculation.
- Derived the irregular massless equations and supplied explicit rank-one and
  zero-vertex counterexamples to equivalence of the full written action with
  the standard massless multiplier action.
- Added a proof that the characteristic real action is free and proper and an
  explicit smooth rank-one Gram section after an adversarial audit identified
  those proof-completion needs.
- Compared the extended packet line by line.  Its positive threshold and free
  multiplication spectra survive, but direct variation of its constrained
  worldline action yields `dot x=0` above threshold and ordinary propagation
  only at threshold.
- Extended the exact checker from 33 to 39 checks for the later packet's
  retained radial derivative, differential ranks, kernel, and second-order
  threshold opening.
- Compiled twice, scanned the log, rendered all pages, and inspected the full
  contact sheet plus the dense concluding pages.

## Final state

- Standalone proof: 987 physical source lines, 14 PDF pages.
- Exact checks: 39/39 PASS.
- Whole-module adversarial falsification: PASS at TeX SHA-256
  `9098F5DC68362E7D03AD8EA892C994C5AB0B7A10F75DE82833F106AD1E268CB7`.
- Canonical sources edited: none.

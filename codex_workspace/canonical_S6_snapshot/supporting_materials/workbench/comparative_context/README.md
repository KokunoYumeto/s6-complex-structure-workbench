# Prior Fable/Jacobian certificate: exact boundary and reusable method

This note records the bounded inspection requested for the separate ES workspace. No files from that external corpus are bundled here, and none of its mathematics is used as a premise in the S6 proof.

## What was actually located

The bounded source search located Jon Poplett's JGPTech/Fun Jacobian package
and an immutable audit copy pinned to commit
`2fe1901840ef3aa28232930e1aec8d8bbb61281a`. The 11 files common to the two
inspected copies were hash-compared and byte-identical. The proof source
`Local_Fidelity_Global_Alias_Pipeline_Proof.tex` has SHA-256
`4C18CC12084D1075FF876C525583414E13C34C23F3B9F247A99D6E018D989F5F`.
An independent exact-arithmetic audit, its JSON receipt, and its checkers were
also inspected. They are not bundled here because they belong to a separate
workstream; the finite certificate needed for comparison is reproduced below.

## Exact result independently replayed

The corpus gives a degree-seven polynomial map
\(F:\mathbb C^3\to\mathbb C^3\) publicly attributed there to Fable. Exact
rational-polynomial arithmetic verifies `det DF = -2`, while the three
distinct rational points

- `(0, 0, -1/4)`
- `(1, -3/2, 13/2)`
- `(-1, 3/2, 13/2)`

all map to `(-1/4, 0, 0)`. On 25 August 2026, `python aceg.py base` was replayed locally and returned exactly that determinant and collision. The separate audit records `PASS`, the componentwise polynomial identity `G=(F3/2,F2/2,F1)`, 24 bounded exact collision hits, and a passing ACEG manifest replay.

This certifies the displayed finite polynomial certificate. The located package is Jon Poplett/JGPTech's independently organized proof and replay of a map attributed to Fable; it is not an original Fable/Claude session transcript. The original model-level provenance was not located in the bounded search. The mathematically relevant name is the **Jacobian conjecture**, not “Jacobi conjecture.”

Do not conflate this certificate with the separate `DegreeSixKeller-public/`
tree or with downstream Erdős–Straus, Collatz, Maxwell–Siegel, or
locality/Boltzmann work.

## Practices transferred to this S6 workbench

Only the fail-closed research method is transferred:

- typed claim states rather than a single prose verdict;
- logical dependency edges rather than thematic association;
- a morphism ledger recording domain, codomain, formula, fibres, exceptional loci, and information loss;
- an explicit uncertainty log;
- primary-source authority order with no silent baseline substitution;
- clean extracted-archive replay of exact checks;
- two-pass TeX compilation and rendered-page QA.

The reusable schema consists of claim, dependency, morphism, uncertainty,
formal-verification, and rendered-PDF-QA records. The corresponding S6
implementations are published under `supporting_materials/workbench/research/ledgers/` and the
consolidated project's reproducibility subtree.

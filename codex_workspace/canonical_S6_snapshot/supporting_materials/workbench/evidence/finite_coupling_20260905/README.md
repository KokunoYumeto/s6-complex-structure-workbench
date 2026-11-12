# Exact rotating coupling fibres and spatial projection - 5 September 2026

The complete proof is in the canonical quaternionic draft,
`s6_quaternionic_4441_reconciliation.tex`, and its shared research module.
The cumulative workbench includes that same module. This directory retains
the input proof notes, exact checkers, certificates and separate build receipts.

For the stated constant-temporal-matrix, two-spatial-rotation ansatz, all
sixteen real spatial coordinates, the literal matrices H,q,F, the original
coupling t=g² and both signs of the frequency are retained. At each fixed
noncommuting spatial pair the admissible roots are exactly
0<t<=t_*, Q7(t)>0, p_Z(t)=0. When Q7 is not the zero polynomial, p_Z has
degree exactly 28 and is nonnegative on the entire real line. There are
therefore at most 14 positive admissible couplings and 28 full tuples,
including both frequency signs. The three exact vector tests for Q7
identically zero are proved, including cases with f7 nonzero.

A fixed 24-by-24 Sylvester determinant polynomial on the full spatial
carrier vanishes at every solution's spatial pair. Its explicit witness
has nonzero determinant, proved by exact rational and finite-field Bezout
certificates and by independent reconstruction from the full eight-dimensional
Gauss equation. The solution projection is contained in a proper closed,
nowhere-dense, measure-zero real algebraic set. No equality with that
containing set, or existence within it, is asserted. The result is not a
claim about arbitrary time-dependent connections or continuum quantum spectra.

## Reproduction

From this directory, run serially with Python 3 and SymPy:

```text
python checkers/quaternionic_residual_next_20260905/check_finite_coupling.py
python checkers/finite_coupling_audit_20260905/check_independent.py
python checkers/finite_coupling_root_20260905/check_modular_identity.py
python checkers/finite_coupling_projection_audit_20260905/check_projection_independent.py
```

The final two checks use the standard library only. Their independence is
structural: the projection checker does not import either symbolic checker;
it reconstructs the full eight-dimensional Gauss matrix and verifies every
coefficient of the supplied Bezout identities. Its 101 finite-field
evaluations certify identities with a proved degree bound, not a sampled
real no-solution assertion. `EXACT_REPLAYS.json` records actual runs and hashes.

The optional `checkers/finite_coupling_root_20260905/check_pair_bezout.py`
reconstructs the full rational coefficient certificates using SymPy and
rewrites the two adjacent generated JSON files. Run it on a copy if retaining
the exact distributed certificate bytes matters. None of these finite tests
substitutes for the universal arguments in the TeX.

The Sylvester coefficient map is classical; the proof cites
[The Stacks Project, Tag 00UA](https://stacks.math.columbia.edu/tag/00UA).
The contribution here is its explicit application, including degree-drop
cases, denominator clearance with the original domain retained, and the
proved nonzero witness for the specified full residual system.

## Artifact records

`INTEGRATION_RECEIPT.json` identifies the input proof notes and the initial
integration checkpoint. `FINAL_SOURCE_RECEIPT.json` identifies the final
source bytes after layout corrections. `FINAL_BUILD_RECEIPT.json` and
`VISUAL_QA.json` identify the three revised PDFs and their separate checks.
`AI_BUNDLE_RECEIPT.json` and `WORKBENCH_AI_BUNDLE_RECEIPT.json` identify the
byte-preserving Markdown bundles. These records do not claim a Zenodo release.

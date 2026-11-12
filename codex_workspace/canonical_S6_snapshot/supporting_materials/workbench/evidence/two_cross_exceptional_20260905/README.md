# Two-cross exclusion and quantitative residual certificate

Research update of 5 September 2026. The complete maintained proof is
`../../research/two_cross_exceptional_shared.tex`, included once through
`../../research/quaternionic_4441_reconciliation.tex` in the quaternionic
draft and cumulative workbench. Their overview displays the key equations.
The complete byte-identical source snapshot, including both the exclusion
and the quantitative certificate, is also retained here as
`proof_sources/two_cross_exceptional_shared.tex`. Its cross-references
resolve when compiled through either complete host, not as a standalone
document fragment.

The first theorem excludes the eight-real-dimensional spatial subspace
where both matrices exchange the matter line and its orthogonal complement.
There is no initial restriction on the temporal matrix: its block form is
forced by Gauss and the scalar equations. Every coordinate, coupling and
frequency sign is retained through explicit simultaneous unitary maps and
their inverses. Full residuals force a strictly positive sum to equal zero.

The same subspace is contained in the canonical spatial exceptional zero
set, by the exact four-block determinant factor and an explicit kernel of
the fixed Sylvester coefficient map. This is a linear-subspace inclusion,
not an assertion of a smooth stratification or pure codimension one.

The new polynomial residual certificate holds before imposing zero
residuals in the displayed classified frame. It gives a strict quantitative
spatial-error bound on the original scalar-plus-Gauss zero set, uniform
for bounded spatial norm and coupling bounded away from zero. It does not
assert this constrained domain is nonempty or bound arbitrary tuples with
nonzero Gauss error. It does not settle existence outside the excluded
subspace or establish any quantum mass-gap theorem.

## Exact replay

With Python and SymPy installed, run serially from this directory:

```text
python -B check_two_cross_exceptional.py
python -B check_residual_certificate.py
```

The first checks 26 full matrix-identity groups with independent complex
spatial entries. The second checks the denominator-free polynomial identity
and its exact positive remainder. `EXACT_REPLAYS.json` preserves actual
outputs and source hashes. The printed proofs, not the finite checks,
establish positivity, domains, Cauchy--Schwarz inequalities, frame covariance
and the complete polynomial degree-drop argument.

Both the exclusion and quantitative extension received a separate complete
equation-by-equation review in addition to the main derivation. The final
artifact receipts record compilation, visual review and source hashes when
completed. `INTEGRATION_RECEIPT.json` is the earlier source-integration
checkpoint; its hashes precede later typography-only corrections.

The companion `quantitative_residual_certificate.tex` retains the authored
extension as a proof source; compile it through the complete shared module,
not by itself. Standard Gauss-law and Sylvester-map background is cited to
David Tong and the Stacks Project in the workbench literature log. No new
general linear-algebra theorem or independent global S6 certification is
claimed.

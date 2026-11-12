# Global-construction recheck and smooth scalar--Gauss refinement

This evidence packet accompanies two distinct mathematical additions to
the current research text. The S6 period, cusp, and finite-gluing audits
inspect the actual analytic construction; they do not infer sphere
recognition or a CDP counterexample from those local checks. The scalar--
Gauss proof identifies the entire literal three-residual zero set and its
fixed-positive-coupling fibres; it does not impose the two spatial
equations or assert an interacting quantum mass-gap result.

## Proofs and source changes

- `PERIOD_AUDIT.md`: the modular lift, exact cusp-regular sheaf,
  two affine gluing arguments, sharp constant-shift half-plane and the
  explicit failure of a cusp-free shortcut.
- `CUSP_AUDIT.md`: separation and smoothness of the countable toric
  space, exact deck action, properness with compact representatives,
  normalization, full opposite-edge maps, canonical form and punctured
  overlap. The full original cusp matrix is retained.
- `FINITE_FILLINGS_AUDIT.md` and `FINITE_INDEPENDENT_REVIEW.md`: complete
  finite-action, logarithmic-conjugacy, integral specialization and
  Hausdorff/proper gluing checks.
- `SMOOTH_INDEPENDENT_REVIEW.md`: a separate complete check of the
  literal inverse, embedded smooth structure, four components and the
  product preserving the original positive coupling.
- `candidate_geometry_before.tex`, `candidate_geometry_after.tex`, and
  `CANDIDATE_GEOMETRY.diff`: exact source checkpoint and changes.
- `period_existence_strengthening_original.tex`,
  `smooth_literal_domain_addendum_original.tex`, and
  `scalar_gauss_smooth_shared.tex`: original staged additions and their
  typesetting integration. All sixteen new smooth labels are retained.

Historical annotations are not rewritten by this packet. The current
proof and orientation surfaces are the places recording these refinements.

## Exact replay

With Python and SymPy installed, run from this directory:

```text
python check_finite_fillings.py --matrix-only
python check_smooth_exact_identities.py
```

These execute 25 finite-matrix assertions and 36 independent exact
identity groups, respectively. They do not use numerical samples.
The first command's portable option skips only private audit-input
hash acquisition and output writing, after running every original
mathematical assertion. Its no-option mode is the original local
audit-receipt workflow. The analytic completeness, strict inequalities,
global inverse domains and smoothness are proved in the TeX and reports,
not inferred from finite computation.

The original acquisition and review receipts retain their original source
hashes. `INTEGRATION_RECEIPT.json` documents the mechanical heading changes,
added citation and machine-path sanitizations in the reader-facing copies.
The portable checker option was added afterward without changing the
assertions. The final file manifest records the resulting bytes. No user
dialogue, credentials or separately licensed primary-source PDFs are
included. Human-resolvable primary citations appear in the proof reports
and the papers themselves.

## Final typesetting and host audit

`HOST_SOURCE_AUDIT.md` and `HOST_SOURCE_VALIDATION_AND_HASHES.json`
record the fourteen-file propagation and source-route audit before the
final build. The only subsequent proof-source edit split one long display
of the four definitions of the flat vectors and frames into two displays;
none of those definitions changed. The smooth source's earlier hash
`eb58e68335de0eb0564854eb1745f1c07279136e4b4d55d1dad92fcfea9bc2d7`
therefore differs from its final typesetting hash
`0a17704b9668ec8f1bf5543e2cb3c99408bcfbad598a5d69b56647e43231e0a7`.
The geometry source retains its audited hash
`6b6ef348e87295aefde4ae4fe6a771ed83b56f848aa367eaaf8e70b37707bdb9`.
The final source receipt and `*_final_typesetting.tex` snapshots identify
the bytes used in the delivered PDFs. Earlier snapshots and receipts are
preserved rather than silently relabelled as final.

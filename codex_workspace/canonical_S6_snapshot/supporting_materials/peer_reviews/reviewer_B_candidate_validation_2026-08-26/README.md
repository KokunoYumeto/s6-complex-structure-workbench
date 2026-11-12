# Reviewer B candidate-specific validation follow-up

This is Reviewer B's independent 26 August 2026 follow-up to the reconstructed
S6 manuscript. Start with
`reports/S6_CANDIDATE_SPECIFIC_VALIDATION_UPDATE.pdf`, then use the Markdown
report and the two CSV ledgers for exact dependencies and falsifiers.

## Mathematical result

From a compact connected smooth complex threefold and a nonconstant
holomorphic map to the base curve, the report proves properness and flatness.
For every vector bundle `E` it then gives the finite-complex/universal-
coefficient proof

```text
R^q f_* E = 0  (q > 2),
(R^2 f_* E)_b tensor k(b)  ->  H^2(X_b,E|X_b)  is an isomorphism,
```

for every full scheme-theoretic surface fibre, including nonreduced fibres.
From the additional inputs that the central fibre is the asserted reduced
Cartier normal-crossings surface with normalization `dP6` and that
`H^2(X; Z)=0`, the report independently proves the normalization-trivial
twist, conductor-supported ambient differential, dual `H^2` nonvanishing,
and hence

```text
R^2 f_*(T_X tensor L) != 0  for every L in Pic(X).
```

The report deliberately treats the global construction, the exact cusp-fibre
quotient, and integral topology as named inputs. Its `OPEN-CANDIDATE-SPECIFIC`
labels record that review's evidentiary cutoff; they do not supersede the
later proofs and current classifications in project-root `workbench.tex`,
whose sectional inputs are under `supporting_materials/workbench/research/`.
Likewise, the report's shorthand “SNC” means the displayed local
normal-crossings models: the candidate fibre is irreducible and nonnormal,
not a simple-normal-crossings divisor.

One proof-scope qualification is essential: Cartier divisors do not have an
injective conormal map merely by being Cartier. Injectivity here follows from
the asserted reduced `x`, `xy`, and `xyz` local models and the explicit colon-
ideal calculation reproduced in the report and current workbench.

## Evidence and integrity

The eight exact checks cover only the named matrix, monomial, conductor, and
integer identities. They do not certify the three global candidate inputs.
The pristine 23-file source archive is retained at
`supporting_materials/archive/review_packages/reviewer_b_candidate_specific_validation_update.zip`:

- bytes: `513043`
- SHA-256: `94c1d1e134718e8978ecf7ad691c8e7a0f0d96fa9a46bcb51bfacc4d1659e7d4`
- archive manifest: 22/22 payload rows verified
- exact checks: 8/8 passed

`ARCHIVE_README_ORIGINAL.md` and `ARCHIVE_SHA256SUMS_ORIGINAL.txt` are exact
files from that archive. This visible folder is a curated, Internet-safe
selection. Generated render caches, redundant text derivatives, an empty
build log, a machine-path preflight record, a duplicate prior summary, and a
workflow transcript containing local/session-only references are omitted
here but remain recoverable byte-for-byte from the pristine archive. The
complete consolidated-project checksum ledger covers every retained file.

On Windows, the original exact-check script reproduces all 8/8 semantic
results but Python's default newline translation rewrites its two generated
result files from LF to CRLF; normalized contents are identical, while the
archive byte hashes are intentionally those of the original Linux run.

# S6 recent-results mathematical consolidation — 30 September 2026

This is the corrected continuation of the [S6 topology and related constructions](../../) collection. It sits beside the complete checkpoint frozen on 6 September 2026 and does not rewrite that historical edition. The continuation consolidates the later quaternionic, measured-fibre, finite-quantum, selector, cusp, arithmetic, and zeta-adjacent material; proves the results it marks R1–R8; corrects the earlier corpus model; and preserves an ordered route for work that has not received a semantic audit.

## Start here

1. [Mathematical note](MATHEMATICAL_NOTE.md) gives the complete proofs R1–R8.
2. [Master map](MASTER_MAP.md) relates the S6, cusp, selector, quaternionic, finite-quantum, and zeta-adjacent lanes without identifying distinct objects.
3. [Tomography design](TOMOGRAPHY_DESIGN.md) gives the full integer measurement matrices and fraction-free determinant reductions.
4. [Claim ledger](CLAIM_LEDGER.md) records corrections, strengthenings, dependencies, and propagation.
5. [Audit limitations](AUDIT_LIMITATIONS.md) states exactly what the catalogue, source readings, checks, and current proofs establish.
6. [Unmined queue](UNMINED_QUEUE.md) orders the remaining mathematical work.
7. [Dated results](RESULTS_2026-09-30.md) records stable result IDs and proof locators.

The standalone LaTeX source is [CONSOLIDATION.tex](CONSOLIDATION.tex). A successful PDF build is not claimed: the available built-in compiler could not find its standard platform directories. The Markdown note and TeX source carry the same mathematics.

## Corrected mathematics

The note retains the original quaternionic Moore cubic, every Gaussian constant, the two marking conventions, the actual residual action, and the original time and coupling parameters. It proves:

- the full quaternionic Gaussian mass and covariance;
- the exact morphism between the Jordan and sample-precision markings, with unit real Jacobians and the three distinct fibres;
- the exact residual-orbit positivity and integrability classification;
- every positive residual exponent's sharp simple-zero and tangency thresholds, together with the full hypergeometric and integer-derivative moment formulas;
- the common-Hilbert-space affinity and Fisher coefficient;
- a finite-dimensional completely positive phase channel and its exact observed/conditional factorization;
- the distinction between static Gaussian dephasing, CP-divisibility, and a separately defined integrated-phase Brownian GKLS semigroup with exact units; and
- a level-minimal six-level reconstruction of the full 15-parameter quaternionic precision and a level-minimal four-level reconstruction of the six observed parameters, with exact determinants $-4096$ and $-16$.

The [verification script](verify_consolidation_v2.py) passes 20 exact check groups and five separately identified numerical evidence groups. The maximum relative error in its non-diagonal cubic stress samples is below `1.9e-15`. Checks support the proofs and do not replace them.

## Corrected corpus model

The first catalogue opened each distinct nested package once and consequently counted 12,822 file definitions as though they were occurrences. The corrected V2.1 model separates 56 package versions, 214 direct package placements, 37 containment edges, 12,822 package-file definitions, and 29,324 recursively expanded logical entry occurrences, including 24,564 text occurrences. It also repairs one direct-member identity collision and verifies all 41,695 direct text assignments against byte length and CRC32.

The public machine-readable derivative is under [catalogue/](catalogue/). It retains hashes, byte counts, ordinals, package topology, structural locators, topic routes, classification evidence, and all row counts. Account-specific roots are removed, archive labels are aliased, and private operational routes are replaced by stable route hashes. The original custody archives and private dialogue content are not copied to GitHub. The exact transformation and hashes are in [CATALOGUE_V2_PUBLIC_RECEIPT.json](catalogue/CATALOGUE_V2_PUBLIC_RECEIPT.json).

The first evidence-backed semantic-routing tranche inspected one exact cue line in each of the 40 largest previously unclassified TeX versions. It routes 2 Navier–Stokes, 7 GCT/arithmetic, 23 primary S6, and 8 Yang–Mills spectral versions. This is routing evidence, not proof acceptance. The conservative unclassified remainder is 4,228 versions.

## Scope

This continuation does not certify the historical global S6 candidate, an S6 sphere recognition, a bosonic field model, redundant environmental records, a decoherent-histories functional, a Yang–Mills mass gap, a Navier–Stokes theorem, or an original-zeta proof. The zeta queue requires reconstruction from the original zeta function with the completion multiplier, Gamma factors, powers of pi, endpoint factors, zeros, poles, trivial-zero terms, derivative contributions, domains, and exceptional points all retained.

The [publication manifest](PUBLICATION_MANIFEST.json) binds every included payload file to its byte length and SHA-256. [PUBLIC_VALIDATION.json](PUBLIC_VALIDATION.json) records the final package checks.

Reproduce the publication checks with `python verify_publication.py --math-replay`. The mathematical replay needs NumPy, SymPy, mpmath, and Matplotlib. Catalogue and file verification alone uses the Python standard library.

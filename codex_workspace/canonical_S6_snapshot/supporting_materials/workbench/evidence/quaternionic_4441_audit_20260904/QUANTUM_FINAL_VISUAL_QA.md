# Final quantum-delta visual and build receipt

4 September 2026, Europe/Berlin. This receipt covers the final v5 build.

## Standalone proof

`s6_homogeneous_quantum_confinement.pdf`: 16 pages, 497,462 bytes,
SHA-256 `703415f196fa90d5a9a20a91e23f2f44c8a2ee5788eec785e3467009660c21f8`.

The bounded final visual reviewer inspected every rendered page, 1--16,
and found no clipped equations, glyph defects, overlaps, margin violations,
or broken page transitions. Its detailed pagewise report is preserved as
`QUANTUM_FINAL_STANDALONE_REVIEW.md`. The serial build script rendered these
PNGs directly from this built PDF. Nine pages are additionally byte-identical
to the corresponding earlier reviewed v1 renders; that comparison is not
being substituted for the final all-page review.

The earlier split inequality and reused scalar symbol are repaired. The
zero-matrix case is included in the upper root-sum equality statement.

## Cumulative working previews

The root visually inspected the final workbench pages
13, 17, 22, 102, 356, 365, 368, and 370, and overview pages 1--7.
These contain the affected abstract/status paragraphs, document map,
literature paragraph, new section, principal form bound, physical-gap
corollary, and adjacent section transition. All inspected pages are readable.

The previous contents defects are fixed: its section 24 and subsection
24.1 point to page 356, subsection 24.3 to page 365, and section 25 and
subsection 25.1 to page 370, agreeing with the visible section starts.
Subsection numbers 23.10--23.18 have a distinct number column and no
longer touch their titles.

- `workbench.pdf`: 562 pages, 4,721,948 bytes, SHA-256
  `71f05f62c0d1cdba89c12c1a711e0b1f32ab82f9dd1ca2d66c8a68c5958adc3a`.
- `workbench_and_manuscript_overview.pdf`: 25 pages, 621,085 bytes,
  SHA-256 `4ac6291b66192af609781334d509d8cc32e2828e00ea7c976735d48e00e0c5ef`.

All three roots compile with zero overfull boxes and no undefined
references. Auxiliary files are byte-stable after respectively 2, 3,
and 2 TeX passes. Build and selection receipts retain the exact scope.
This is not a new all-562-page mathematical or visual recertification,
nor a new verification of the original global S6 construction.

## Mathematical scope

The new complete proof concerns the specified finite homogeneous
38-coordinate SU(3) gauge--scalar Hamiltonian, at fixed positive volume,
Planck constant, gauge coupling and quartic coupling, with m squared
nonnegative and real cubic coefficient. Its positive physical excitation
gap is not a numerical bound or a continuum/infinite-volume theorem.
The original interactions and the mixed Fourier coupling remain explicit.

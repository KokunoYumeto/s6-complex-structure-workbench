# Homogeneous quantum draft: visual QA of pages 9-16

Date: 2026-09-04. Reviewer: physics_bridge_4441.

Source PDF:
C:/Users/user/Documents/math/tmp/pdfs/homogeneous_quantum_20260904_v1/s6_homogeneous_quantum_confinement/s6_homogeneous_quantum_confinement.pdf

Independently computed SHA256:
8a659564f0143f8cab653d0688ce7a9a75cb3891765d5322384417529b350024

File size: 497207 bytes. The assigned draft has 16 pages; this receipt
covers pages 9, 10, 11, 12, 13, 14, 15 and 16 only.

## Method

Read the entire PDF skill before inspection. Opened each of the eight
existing rendered PNGs individually using image viewing, at a readable
full-page size. Checked margins, equation alignment, display continuity,
headers/footers, visible references, glyphs and obvious notation.
This is visual QA with a limited obvious-notation check, not a new
independent audit of all mathematical proofs.

No PDF authoring, re-export, canonical edit, rendered-page change, or
cleanup was performed. No authoring marker was run because the work
was read-only.

## Findings

Two minor actionable issues were identified and sent to the parent:

1. **Pages 11-12, Theorem 1.9, equation (9): split display.**
   The first line of the lower bound ends at the bottom of page 11,
   while only its final scalar terms and equation number appear at
   the top of page 12. Keep the two lines of equation (9) together.
   Nothing is clipped, but the page break makes the central bound
   unnecessarily awkward to read.

2. **Page 16, Fourier-product obstruction: reused scalar c.**
   The new operator-domain paragraph explicitly defines
   c=3Gamma V3/4. The following paragraph then says
   y²Omega=c Omega, where the latter c is an unrelated possible
   multiplication eigenvalue. Rename that latter eigenvalue to
   lambda_Omega or c0. The no-L²-eigenfunction argument is unchanged;
   the correction avoids identifying the eigenvalue with the retained
   interaction coefficient.

No clipping, overlaps, malformed matrices, missing-glyph boxes,
undefined-reference markers, illegible displays, or footer collisions
were found in this range. Long source URLs remain within the text width.
The late operator-domain paragraph is present on page 16 and is legible.

## Explicit page record

| Page | Material inspected | Result |
| --- | --- | --- |
| 9 | Matrix form allocation MQ.9, compactness estimates MQ.10-MQ.12, cube-average proof | No visual defect |
| 10 | Friedrichs conclusion, quantitative energy-origin bound MQ.13-MQ.14, gauge-density section | No visual defect |
| 11 | Canonical coefficient map MQ.15, literature, Theorem 1.9 and beginning of (9) | Equation (9) continues across page break |
| 12 | End of (9), coupled compactness proof, weight and tail estimates | Equation (9) continuation should be kept with page-11 line |
| 13 | Positivity theorem, free/bridge kernels, truncation proof and Simon reference | No visual defect |
| 14 | Orbit-square average, spectral-infimum proof, positivity and physical-gap corollary | No visual defect |
| 15 | Classical embedding, spatial gauge counterexamples, Fourier-mode setup | No visual defect |
| 16 | Quartic coupling, added domain paragraph, discarded-mode obstruction and Tong reference | Rename the second use of c as described above |

The corresponding page-9.png through page-16.png were all opened
individually from the source PDF's directory. Pages 1-8 are outside
this receipt's scope.

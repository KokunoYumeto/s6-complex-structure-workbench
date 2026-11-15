# Boundary agent: sixth-hour additions and independent audits

Date:2026-11-15. All named results below retain their precise scope; no novelty claim is made.

## Added and integrated

- **B.4.11:** actual negative-line cone germ for the parabolic elliptic contraction; H²(Y,ThetaY)=0 through the nonsplit Atiyah extension, analytic formal functions, and the actual elliptic modulus; regular global-to-local deformation map. Root and AB independently passed. Files: `B_elliptic_contraction.tex`, its results CSV, bibliography, and source audit.
- **B.4.14:** exact weight-zero tangent cohomology for the parabolic surface and its contraction; vanishing H² for the relative tangent sheaf of every compact associated Y-bundle over P1, also with one whole fibre fixed. Root and AB independently passed; exact symbolic and fan verification is AB's `ab_push_kato_weights.py/.out/.json`. Files: `B_elliptic_weights.tex`, its results CSV and bibliography.

The original Manetti1991 Lemma1, p.93, was retrieved from the historical GDZ resolver and visually read. It directly proves the general compact analytic isolated-singularity criterion used in B.4.11, with no projective or rational-cycle hypothesis. The source audit preserves the exact IIIF URL, manifest, and scan location. Grauert1960 §6 HauptsatzIIa, p.59, was independently opened for analytic formal functions.

## Full-source independent referees passed

- B.4.10: uniform Kato annuli, properness, marked elliptic axis, exact normal-line gauge, generic Hopf blowdown, and failure of the weighted exceptional divisor to extend (`D_Kato_axis_audit.md`).
- B.4.12: explicit Q-cone sweep, vertex blow-up, proper global surface smoothing, all three first-order normal products, and integral topology of Q minus E (`D_B4412_referee.md`).
- E.2.7: conditional zero-period monodromy obstruction (`D_E227_referee.md`).
- E.2.8: irreducible fibres and non-Kähler normalization restriction under a horizontal prime (`D_E228_referee.md`).
- E.2.9–10: negative horizontal twisting on reduced and nonreduced fibres, uniform analytic vanishing, the actual affine Čech line-bundle family, simultaneous generic cohomology vanishing, HRR contradiction, and persistence of the canonical pencil for either sign (`D_E229_E2210_referee.md`). This is the principal one-sided-limit advance: the negative-slope fixed divisor is eliminated without the invalid CDP holomorphic-fibration theorem.

## Explicitly unfinished routes

`B_equivariant_compactification_attempt.md` retains both candidate compactifications and their exact gaps. Formal Rim equivariance is not promoted to a convergent action on a singular compact space. The opened Doan2026 primary preprint explicitly records the general analytic equivariant-object formalism as a remaining problem. The associated-bundle route still needs nonisolated local-deformation compatibility and analytic effectivity; the proved H²-vanishing alone is not enough.

The conditional compact-three-piece arrangement would have nearby Euler number20 if all its assumed compact strata and smoothing existed. This is not a topology assigned to an unconstructed model and cannot be used as an S6 filling.

A direct normal-bundle translation obstruction was sent to root/AB: an automorphism preserving an elliptic curve with nonzero normal degree d and acting as translation by b forces d·b=0. It extends the single finite-Hopf-modification limitation to any preserved negative-axis cap, and to finitely permuted marked caps after taking a power. The actual applicability depends on extension of the stated axis and period marking; no unrestricted filling obstruction follows.

The original D.1–D.4 conclusions and their code remain unchanged. The actual B filling, interior-period completion uniqueness, and arbitrary deformation-chain question retain the open scope stated in the integrated sources.

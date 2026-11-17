# Corrected marked cap column before checkpoint07

2026-11-17T06:49:44.265081+00:00

The agent identified a marking error during the checkpoint freeze. The root corrected the current working note before its archive entry was written; the resulting checkpoint07 was inspected and contains that correction. The boundary-inversion calculation remains valid, but it does not identify the marked cap column. The actual cap coefficient is retained as kappa, and the full gluing map is an integral isomorphism for every kappa. A late-added cap specialization in the code and JSON still sets kappa to zero in the original displayed basis; those appended cap entries require the explicit adapted boundary basis. They are superseded by the general-kappa correction following checkpoint07. The source-boundary matrices and inversion identities themselves remain valid.

## Superseded passage

On the I2 reflection cap, H2=Z C, the sum of the two central component classes is 2C, and source inversion fixes C. Naturality therefore gives

    epsilon↦0,  r↦−C,  s↦0.

Thus the full H2 Mayer–Vietoris map is an isomorphism of finitely generated abelian groups: epsilon maps to tau, while (r,s) map by a determinant-one free block. The source order-two class is neither discarded nor spuriously retained.


## Post-checkpoint clarification

2026-11-17T06:51:09.097141+00:00

The immutable checkpoint07 has1409 entries and passed its ZIP integrity test. Its working note contains the general-kappa proof. Its provisional appended H2_boundary_to_cap and H2_MV fields use the zero specialization without updating the boundary representatives; these entries are being replaced by the explicit symbolic calculation, with the original version preserved. No I1* theorem was promoted in the291-page checkpoint manuscript. The root's first erratum described only the earlier boundary-only JSON read; this paragraph corrects that scope statement.

The symbolic code and output correction was completed immediately after checkpoint07 and executed PASS. The original files are preserved under code/part3/attempts/i1star_boundary_superseded_zero_cap.*; the current certificate includes the adapted chain representatives.

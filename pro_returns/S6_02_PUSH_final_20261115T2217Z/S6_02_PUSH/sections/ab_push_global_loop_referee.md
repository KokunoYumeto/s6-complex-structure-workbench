# Independent referee: global affine loop defect B.4.32

**Reviewer:** limits_ab. **Date:** 15 November 2026. **Verdict:** PASS for the complete source `sections/B_global_loop_defect.tex`, read in full, and for its current working precursor `sections/D_global_loop_defect_working.md`. This does not prejudge the final noncompletion argument reserved for B.4.33.

## Definition and finite-cover normalization

The connecting class of a holomorphic Jacobian section is canonically in `H1(Delta*, Lambda) = Lambda/(T-I)Lambda`. It does not require a single-valued additive lift. Since `T-I` has image in the primitive delta line, its image in `V = Lambda_Q/Q delta` is unambiguous. Under a degree-e parameter root, the restriction is the norm `I+T+...+T^(e-1)`, equal modulo delta to `e I`. Dividing by e gives the claimed normalization. Additivity of the connecting map and finite transfer give the trace formula with its stated degree. The independent symbolic-induction check is `code/ab_push_affine_loop.py`, with saved stdout and JSON; no finite sample is used to infer the all-degree formula.

## Actual affine changes of origin

I checked B.4.19.1--B.4.19.5 against the finite-place source-to-target matrices in B.1.2 and the exact checked program `ab_push_finite_decks.py`.

* On ordinary overlaps, the logarithm difference is an integer n, so the affine term is `n v delta`. Its positive radial-loop label lies in `Z delta`.
* The two actual Lie-frame matrices are independent of the degeneration parameter and fix the last coordinate. The exact covariance is `R_j Pi_c = Pi'_c A_j`, with target tau, mu, and beta retained. Thus lattice transport is the actual `A_j`; no omitted moving Lie frame contributes to the loop invariant.
* The root-to-ordinary connector is `w_j Pi_c v_j`. Its c-dependent part is `-12 epsilon_j w_j v delta`; the difference between scalar closing gauges is the opposite term. The full vector connector after both gauges is independent of r, not merely trivial after projecting its first coordinate.
* The finite root deck factors `r^4` and `r^-3` have only delta winding. Period-representative changes alter a loop label by `(T-I)ell`, also delta.
* The corrected cusp comparison is exactly `G(s)+6v delta`. The r-independent G contributes no radial-loop label. The remaining label is `6 delta`.
* A shift of all twelve central labels is not the identity: it can translate the elliptic base by `6P`. The proof correctly retains that fact. Its change under an r loop remains `(T-I)gamma`, which is in the delta line.

Consequently the reference origins define a global reference loop class, although they need not define a global affine zero section. This is the precise assertion needed for patching lambda.

## Geometric independence of the extending section

The reduction of an arbitrary proper analytic filling is legitimate at the stated scope. Retain the unique reduced main component, normalize, resolve, and apply the strengthened B.4.4. Its direct-image and marked-critical-value proof uses only a smooth connected dominating fourfold, with no assumption on central multiplicities. Principalization gives the model used by B.4.31 without changing the punctured family.

Over a sufficiently small ordinary q disc outside the finite bad set, the local simultaneous root and toric subdivision of B.4.30 apply with q retained as a smooth tangential parameter. A common further root and refinement compare any two such choices; a global nonprojective semistable-reduction theorem is not invoked.

The finite Stein factor of the proper normal dominating model is generically degree one and hence is the normal base. Central surface fibres are therefore connected. This supplies the finite chain of charts comparing sections limiting to different central components.

The saturation argument for normalized closed logarithmic forms in B.4.30 is independent of full-rank monodromy. Its rank-one application here uses the explicitly retained period frame and the same analytic IKN comparison theorem. B.4.31 supplies the missing integral-residue assertion: every local angular class is in `Z delta`. Thus the two exponentiated primitives have the precise form `O* x M_r^gp`; the first has no r order, and the second contributes only delta winding. The chart-chain comparison therefore proves zero difference in V for any two extending sections. This comparison does not choose a bounded origin relative to the old model.

Proper transforms of section germs are holomorphic away from isolated points of their two-dimensional base. Comparing on this dense open set suffices, because the normalized connecting classes are locally constant. Smooth points of a reduced local central fibre provide local transverse sections. Finite traces and further roots then give the statement for arbitrary finite multisections.

## Global monodromy and scope

Section independence removes the choice of cap section, while the exact affine audit removes the reference-origin ambiguity. These are separate steps, and together they produce a global flat section of the actual quotient local system V.

The quotient matrices have fixed lines `Q(1,2,-4)` and `Q(1,3,-3)`, with zero intersection. An explicit common fixed-equation minor is 6. Removing further ordinary points does not remove the two peripheral monodromies from the image. The independent exact program also checks the two distinct elliptic unipotent fixed lines. Averaging a finite orbit first kills its gamma coefficient, so the finite-orbit variant is valid as well.

The conclusion controls only a loop class. An essential translation with zero loop class is not asserted to extend. The corrected local caution is exact: changing the punctured marking of a standard local cap by `chi(r)=[log(r) u/(2 pi i)]` gives nonzero local class u modulo delta, while all differences of extending sections are unchanged. It cannot patch over the global base because u has an infinite monodromy orbit. B.4.15 is correctly not claimed to establish that particular local example.

The current theorem applies to arbitrary proper analytic fillings after finite parameter covers. It does not by itself prove nonexistence. The further cusp comparison and torsor argument belong to B.4.33 and require their own full-source review.

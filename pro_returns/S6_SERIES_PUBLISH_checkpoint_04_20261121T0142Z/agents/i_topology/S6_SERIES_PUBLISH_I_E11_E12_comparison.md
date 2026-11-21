# Integral dictionary/classification — actual comparisons

## push:src:E.1.1 [032R]

The saved preread proof checked the exact P_V map, two monodromy intertwinings, all three marked-vector images, and the inverse affine root action before opening the target proof. The target adds the factorization P_V=Q_E^(-1)P_E through Engel's marking. I checked this extra factorization after opening, by fresh exact integer multiplication; detQ_E=1 and detP_V=−1. The entire two-generator intertwining and inverse matrix are recorded in the new output.

The clockwise/counterclockwise sign is exactly the inverse affine map, using the invariant transported period v_i. It gives P_V w_j=−v_i, including the additional N1 in the second delta coefficient. The section-preserving cusp comparison has zero quotient winding, and p=−b follows. The smooth-torus torsion-point interpretation and the effect of changing its integral lift are unchanged. The primary Viaclovsky §2 text was read at its matrix/basis/invariant-vector/torsion-point definitions; rendered-page provenance is separately maintained by the provenance agent. No source fault found.

## push:src:E.1.2 [032S]: exact independence boundary

The frozen preread proof deduced this theorem by the actual arithmetic dictionary from the previously stated and proved fam:B.3.1 classification. After opening E.1.2 I found that its first four printed steps repeat the full general clockwise classification proof. I then opened fam:B.3.1's proof to check for a circular dependency: it proves the classification from A.1.2, A.2.1 and B.2.1 and does not invoke E.1.2. Thus the preread transport is a valid proof from that earlier result. It is not an independent re-proof of the underlying global classification theorem; no such credit is claimed here.

Every extra printed step has subsequently been checked:

1. The fresh program sums the actual matrices and obtains the exact displayed N3,N4 formulas. Their repeated images are mZε+kZδ and nZε′+2lZδ. The explicit ell_j solve their integral norm equations; the supplied b_j solve (I−A_j)b_j=y_j because the norm-kernel relation gives their last coordinate. This was verified as a rational two-variable matrix identity, not just with a numerical example. The full-root affine maps and inverses then commute modulo the actual integral ell_j and descend to the complete finite fillings.
2. The collar formula has the asserted integral defect. The correction (0,1,−2,0) is in kerN3, and −A0 of it is (0,−1,1,0), giving a primitive adjustment in the surviving second quotient coordinate and zero in the first. The first quotient coordinate of ell0 is
[(nr1′+mr2′)−alpha(nr1+mr2)]/(mn)=l0′−alpha l0,
exactly the p′=alpha p relation. The remaining toric vector gives an actual integral cocharacter translation. Its t_c^q x^alpha map and the unit factor preserve the periodic triangular fan, with inverses, so the cusp extension is an exact fan map rather than a fractional-period interpolation.
3. The enlarged-root invariant coefficients factor through s^k and s^l under the kernel subgroups. The remaining equivariance is literally that of the standard roots. This identifies the coarse difference sheaf with the same extension O→V_B→O(-p0); it also agrees with the independently checked coarse vertical bundle in E.2.1. H1 of both ends is zero, so the local translation torsor has zero Cech class. Its overlap equalities and inverse maps prove global sufficiency. This analytic gluing verification occurred after the target proof was opened and is recorded as such.
4. The positivity proof of intrinsic base recovery is valid: the pullback Fubini–Study form is exact on the sphere, and its nonnegative pairing on each compact flat torus has zero integral, forcing constancy on that fibre. The proper-image/normalization argument and its inverse yield a base automorphism; the distinct monodromy orders fix all marked points. This route does not depend on a later canonical-line theorem. The fresh32-by16 rational equation system has rank14, so the simultaneous centralizer is exactly QI+QE. Constant last columns force the fibre-linear part to be alpha I. Unimodularity gives alpha=±1 and the shear coefficient gives h∈Z, with lattice map alpha S_h^(-1). Norm and cusp winding necessity then give exactly the conditions already used in the preread transport.
5. The substitution, removal of N1′−alpha N1 modulo2l, fixed-data subgroup, CRT count and positive-loop sign all agree with the preread derivation. A fresh direct CRT orbit enumeration covers128 admissible pairs k,l≤20 and25826 residue states. Every orbit length is2kl. The proof for all pairs is the algebraic invertibility/CRT argument, not this finite enumeration.

**Outcome:** the coordinate-form theorem and its complete printed proof are supported. The new third check of this target is precisely the preread dictionary/CRT derivation from fam:B.3.1, followed by a full comparison and fresh exact arithmetic. The record does not count the repeated four-step global construction as another preread re-proof.

## Concrete safe merger

Keep one complete clockwise general classification proof. The current fam:B.3.1 proof contains the full base-recovery argument and reduces the finite/cusp gluing to B.2.1. The current E.1.2 proof adds explicit integral ell_j, rational b_j, the primitive second-winding adjustment, and the fully written difference-sheaf argument. Import those details into the single retained general proof. Then retain E.1.1 as the exact integral dictionary and E.1.2 as its coordinate-transport corollary, with all existing labels/tags and the five arithmetic conclusions. Its short proof consists of the reversible substitutions and CRT argument already frozen above. This preserves all mathematical content while removing a second full global classification proof.

Program: `code/S6_SERIES_PUBLISH_I_integral_dictionary_exact.py`; complete output: `output/S6_SERIES_PUBLISH_I_integral_dictionary_exact.json`. No retained program was read or reused.

Saved UTC: 2026-11-21T01:28:20.090613+00:00

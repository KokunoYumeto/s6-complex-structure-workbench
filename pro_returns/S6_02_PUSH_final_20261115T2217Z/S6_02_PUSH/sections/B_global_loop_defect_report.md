# B.4.32: global radial-loop defect

**Status:** proved and integrated after B.4.31. Root read the complete final TeX and passed it. Classification_e and limits_ab independently read the full working proof and passed the connecting-class definition, root normalization, actual affine-overlap audit, section comparison, trace normalization and fixed-space calculation.

The proof begins with an arbitrary proper analytic filling. Its reduced main component is normalized and resolved without altering the punctured family; B.4.4 then extends the intrinsic marked map. B.4.31 supplies the global constraint that all generic r-central meridians lie in the primitive δ direction. Local finite roots and explicit toric subdivisions suffice; no global nonprojective semistable-reduction theorem is invoked.

For a punctured Jacobian section, the positive r-loop defines a connecting class in Λ/(T_r−I)Λ and hence in Λ_Q/Qδ. An e-fold parameter root multiplies this class by e. Dividing by e makes the class of an extending cap section independent of all roots. The saturation and finite chart-chain arguments of B.4.30, with the B.4.31 residue vector (0,integer), show that any two extending sections have the same normalized class.

The origin comparisons are those of the actual B.4.19 construction. Ordinary logarithm changes contribute n log(r)·δ. The finite-root connector's entire r logarithm cancels. The cusp comparison is G(s)+6vδ with G independent of r. The Lie-frame maps are independent of r and fix δ. Thus the normalized class patches globally in the actual homology local system.

On Λ_Q/Qδ, the two peripheral fixed lines are Q(1,2,−4) and Q(1,3,−3), with zero intersection. Consequently the global class vanishes. This controls the γ radial-loop component required for the next cusp argument, while allowing essential translations with zero period defect.

The exact program code/d_push_global_loop_defect.py and its saved output/JSON pass the fixed-space, coherent root-transfer, finite connector and cusp-loop checks. Geometry is proved in the TeX. The working derivation is retained in sections/D_global_loop_defect_working.md. No new primary bibliography entry is needed: the analytic input is the original IKN2005E theorem already independently opened and cited in B.4.30; the actual comparison identities are the proved B.4.19 equations.

## Audit distinctions retained

The first warning that bounded pairwise differences do not identify the old affine origin was correct. The present proof does not remove that warning by assuming an origin extends. It controls only the period defect via global monodromy, which is enough for the separate B.4.33 argument if that final argument passes review.

The exact local marking change χ(r)=[(log r)/(2πi)·u] produces a nonzero u defect over an isolated ordinary base disc. It cannot patch over the entire marked base because u has infinite monodromy orbit. This is the appropriate local scope example; B.4.15's vertical Hopf insertion is not claimed to realize this particular generic defect.

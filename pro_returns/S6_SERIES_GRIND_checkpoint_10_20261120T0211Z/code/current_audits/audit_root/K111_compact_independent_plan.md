# Independent compact-component recomputation

Written before opening the producing `K111_T2_compact_ledger.py` implementation. The statement and geometric comparison in `audit_sign/K111_two_torus_physical_specialization.md` and the serialized certificate schema have been read. The implementation below is designed directly from expansion of the retained physical Euler integral.

For every point, expand −u³/∏W and −u ΣW²/∏W. For every curve with normal degrees d, expand u³ Σ_i d_i/(W_i∏W) and u[(ΣW²)Σ_i d_i/(W_i∏W)−2ΣW_i d_i/∏W]. Use the substitutions (u,v)=(1,ε) and (1+ε,2ε). A weight is W_i=w_i u+a_i v. Expand each rational function with exact fractions through the constant coefficient, retaining every negative exponent. Sum within the already named physical owner; require every negative coefficient to vanish for each of the 35,908 compact owners. Compare both resulting constants and the stored owner pairs, then sum the resulting compact pair.

For generic curves, additionally reconstruct the common ray matrix N from the physical owner's saved face; invert it over Q; derive physical and second weights N⁻¹e₁ and N⁻¹e₂. Derive each endpoint coefficient order N⁻¹F_e l_e from its complete saved character matrix and transverse ray, and the normal degree vector as the negative sum of the three orders. No producing implementation is imported.

The selected physical owner assignments and complete endpoint fan coverage still require the geometric atlas and whole-star certificates. This independent calculation verifies the specified residues and generic degree transport; it does not by itself supply the point/O extension or outer cap comparison.

## Certificate coordinate transport and execution
The first schema-level attempt treated a sorted physical-owner face as an ordered three-cone; this failed at generic:0. Ordered common cones are instead explicitly `K111_new_regular_common_fan.json:cones[g].rays`. A second membership check treated that whole three-cone as the physical normal face and failed at generic:7, whose physical component is a surface. The final verifier derives N^-1 delta, retains precisely its nonzero-weight rays and checks that sorted face against the owner's full physical-face list, as well as the actual chart membership. These corrections implement the explicitly derived face map. Neither failed attempt reached a residue or reported a mathematical conflict.

The complete independent calculation passed 484,310 exact assertions, with 1,926 generic curves, 52,546 corner pieces, 35,908 compact physical owners and both substitutions. All poles of orders up to two canceled within each owner, and the compact sum is (895,139). See code/outputs/K111_compact_owner_independent.json for all owner values and input SHA-256 hashes.

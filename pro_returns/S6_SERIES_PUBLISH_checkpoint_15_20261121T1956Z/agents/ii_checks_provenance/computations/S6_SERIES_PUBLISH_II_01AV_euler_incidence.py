"""Exact Euler calculation from the normalization/conductor stratification."""
import json
hirzebruch = 2 * 2
blowup_delta = 2 - 1
normalization = hirzebruch + 2 * blowup_delta
conductor = 6 * 2 - 6 * (2 - 1)
# Six conductor nodes have three preimages at each triple point of the image.
triple_points, remainder = divmod(6, 3)
assert remainder == 0
double_locus = 3 * 2 - triple_points * (3 - 1)
surface = normalization - conductor + double_locus
assert (normalization, conductor, double_locus, surface) == (6, 6, 2, 2)
print(json.dumps({"method": "normalization/conductor/image incidence additivity",
 "normalization_euler": normalization, "conductor_euler": conductor,
 "double_locus_euler": double_locus, "rational_surface_euler": surface,
 "elliptic_ruled_and_Hopf_euler": 0,
 "possible_r_and_b3": [[r, 2 - 2*r] for r in range(2)]}, indent=2))

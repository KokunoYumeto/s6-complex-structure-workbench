# Exact family lift at the two finite points

Post-freeze clarification by root,20November2026. This supplements the frozen
derivation without changing its bytes. It is still subject to independent
receiving review and changes no paper or canonical status.

Use the actual invariant generators from current E15. Write a fine-cover
Hodge frame as f_i and a quotient frame as g_j. Its coarse generators are
`w^(aF_i) f_i` and `w^(aG_j) g_j`, respectively. A coarse graph matrix C has
fine-cover matrix

`Z_ji(w,s)=w^(aG_j-aF_i) C_ji(w^n,s)`.

This formula follows by dividing the graph vector
`w^(aF_i) f_i + sum_j C_ji w^(aG_j) g_j` by its indicated first factor.
It is the actual graph-plane map, with its inverse obtained by multiplying
each coefficient by `w^(aF_i-aG_j)` before invariant descent.

At p1 the order is3, `aF=(0,1)` and `aG=(0,2)`. The matrix of exponents,
with quotient rows and Hodge columns, is

`[[0,-1],[2,1]]`.

Only the upper-right entry has a negative exponent. The fixed value at the
critical point gives `C_12(b,s)=b D_12(b,s)` with D jointly holomorphic in the
coarse base coordinate b and smoothing parameter s. Its lift is
`w^2 D_12(w^3,s)`, with no pole and the same limiting equivariant plane.

At p2 the order is4, `aF=(0,3)` and `aG=(0,1)`. The exponent matrix is

`[[0,-3],[1,-2]]`.

The same joint division gives lifted upper-right and lower-right entries
`w D_12(w^4,s)` and `w^2 D_22(w^4,s)`. These are precisely the two value
conditions in E15. The other entries already have nonnegative exponent.
All three required coarse entries vanish because the comb deformation fixes
the entire limiting plane at each critical value. Thus this construction is
holomorphic jointly over the smoothing disc, preserves the actual finite
characters, and supplies the family tautological and quotient bundles used
in the node proof. On an ordinary node the root/coarse projection is the
identity, so this lift introduces no further node factor.

At the cusp E15's actual logarithmic chart writes the periods as
`(log q)/(2 pi i) I + H(q,s)`, with H jointly holomorphic after shrinking the
parameter disc. Its logarithmic residue remains I; in particular the
relative cup row stays surjective at the cusp. The same toric units,
admissibility and finite-isotropy filling maps are the ones constructed in
the attached comb source and E15. This paragraph uses those proved filling
maps and does not replace them by numerical period data.

The relative map from the embedded family of comb curves to the original
coarse base restricts to the tooth-collapse map on the central fibre and to
a degree-one section on each smoothed fibre. Therefore its pullback of
`O_B(k)` supplies the single family line used in the semicontinuity argument;
the central and smooth twists are related by this actual pullback.

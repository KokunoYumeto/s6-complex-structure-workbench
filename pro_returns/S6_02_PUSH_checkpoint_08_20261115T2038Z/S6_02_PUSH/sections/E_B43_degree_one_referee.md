# Independent referee of the degree-one normal-crossing Hodge obstruction

**Verdict: the proposed stronger lemma is valid for proper reduced analytic normal-crossing spaces, including self-crossings.** If every connected component of the smooth normalization satisfies the partial-partial-bar lemma, the natural map `H¹(D,C) -> H¹(D,O_D)` is surjective. No Hodge assumption on the double or higher branch intersections is required in this degree.

## Branch resolutions

Use the smooth proper spaces D^[p] of ordered (p+1)-tuples of distinct **local** branches through a point, with their common intersection and finite projection to D. This differs from indexing only by distinct global irreducible components: that latter indexing would miss an irreducible self-crossing. The normal-crossing coordinate models make the ordered branch spaces smooth. Distinct local branches cannot merge into one local branch at a limit point in a normal-crossing space; the finite branch construction is proper. The symmetric group acts by permuting labels. Over C, the alternating projector is available.

The augmented alternating complexes of pushed-forward constant sheaves and of holomorphic function sheaves resolve C_D and O_D, respectively. This is a stalkwise assertion. At a coordinate-crossing point, the constant complex is the augmented simplex complex on the local branches. For functions, it is the exact alternating restriction complex for the union of coordinate hyperplanes and their intersections. This is the usual coordinate-ideal inclusion-exclusion resolution, and can also be proved inductively from `0 -> O_(A union B) -> O_A direct-sum O_B -> O_(A intersection B) -> 0`. These local calculations are compatible with permutations, so no global ordering or simplicity of the crossings is assumed.

Resolve the branch terms by their smooth Dolbeault and complex de Rham complexes. Their pushed-forward form sheaves are fine, using partitions of unity pulled back from the compact analytic base. Hypercohomology is therefore computed by the corresponding total complexes of global forms. Projection of a complex differential form to its (0,*) part realizes the natural map from the constant to the coherent resolution.

## Degree-one cocycle calculation

With the sign convention `delta alpha = bar-partial f`, a Dolbeault total degree-one cocycle is a pair alpha in A^(0,1)(D^[0]) and alternating f in A^(0,0)(D^[1]), satisfying `bar-partial alpha=0`, `delta alpha=bar-partial f`, and `delta f=0`.

On each normalization component, partial alpha is partial-exact and bar-partial-closed. The partial-partial-bar lemma supplies a smooth function h with `partial alpha=partial bar-partial h`. Subtracting the total coboundary of h replaces alpha by `alpha'=alpha-bar-partial h` and f by `f'=f-delta h`. Then alpha' is a d-closed pure (0,1)-form and `delta alpha'=bar-partial f'`.

Applying partial gives `partial bar-partial f'=0`, since holomorphic face pullbacks commute with partial and partial alpha'=0. On every compact connected smooth component of D^[1], a complex-valued pluriharmonic function is constant: apply the maximum principle to its real and imaginary parts in local holomorphic coordinates. This also covers the zero-dimensional components. Consequently `d f'=0` and `delta alpha'=0`, while `delta f'=0` remains true.

The same pair (alpha',f') is now a cocycle of total degree one in the complex de Rham branch resolution, and its (0,*) projection is the original coherent class after the stated coboundary. This proves surjectivity with no unresolved differential or spectral-sequence degeneration claim.

## Application and scope

Combining this lemma with B.4.2 and upper semicontinuity gives the proposed obstruction: a semistable six-sphere centre has H¹(D,C)=0 but h¹(D,O_D)>=1, so at least one smooth normalization component fails the partial-partial-bar lemma. In particular an all-Moishezon normalization is impossible, since smooth compact Moishezon manifolds satisfy that lemma. This application does not establish that the unknown vertical components are Moishezon. It strengthens the previous SNC-only all-strata condition precisely in total degree one.

The proof is elementary once the explicitly described normal-crossing resolutions are fixed; it does not apply to arbitrary singularities, pinch points, or nonreduced centres without further arguments.

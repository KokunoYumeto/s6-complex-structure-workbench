# The remaining comb cotangent kernel

Reader: GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC.

This note concerns only the kernel in INV E2.2 equation (E.6). CDP E15 resolves the former Kuranishi question, so an obstruction-map problem must not remain attached to INV E2.3 as though it were still open.

## What was actually attempted

1. I followed the full direct-image calculation in INV E2.2 and recomputed the rank, determinant and torsion-length constraint. If the cokernel of the cup map has length e, the kernel has rank three and degree −2m−2+e. This does not determine three splitting degrees or their nonnegative parts. The tangent cup map in CDP E15 is a different map, on V tensor G rather than V-dual tensor G; its exact tangent dimensions do not determine this kernel.

2. I tried to obtain the missing sections from the retained invariant real classes. The invariant homology class gives a section of V, and the invariant cohomology class gives a section of G. Their tensor therefore lies in V tensor G, the tangent-deformation bundle. It does not supply a section of V-dual tensor G, the bundle in (E.6). Thus that otherwise natural construction does not close this calculation. No nonexistent identification V ≅ V-dual has been used.

3. I carried the nonnegative coarse splittings farther. This produces the rigorous additional bound below, but does not determine a splitting or an exact number of sections. The argument uses all possible nonnegative splittings, rather than choosing an unproved balanced one.

4. I tested whether the stated rank/degree/length information alone could determine the kernel. The explicit pair of surjective maps below proves that it cannot. These are vector-bundle examples, not asserted to arise from an admissible comb period section. In particular this is not a proof that two geometrically realized X_m have different K_m.

5. I inspected the source's stated smallest instance. It specifies an open set of smoothings of a twelve-tooth comb, with fixed limiting planes; it does not provide the transition matrices or an explicit solved period section for a unique X_12. To compute that instance one must choose an actual admissible section, solve its nonlinear patching conditions, and differentiate it to obtain the cup map. An arbitrary polynomial matrix of the correct degrees is not a substitute: it may violate the flat Hodge-plane and real transversality conditions. No numerical method has been represented as having run on matrices that have not been supplied or constructed.

## A new uniform bound from the available data

Let S=2m−1≥1. Write V_c=O(a)⊕O(S−a) and G_c=O(c)⊕O(S−c), with 0≤a,c≤S. Exact invariant pushforward gives a natural injection

    ρ_*Hom(V,G) → Hom(V_c,G_c).

It is an isomorphism off the two orbifold points; injectivity follows either from restriction to that dense open set and torsion-freeness, or from the local invariant bases. At a finite point the one extra condition requires the map from the nontrivial-character source line to the trivial-character target line to vanish at that point. Thus the degree drops by one at each of the two points, explaining the degree −2 used in (E.7).

After reordering the two summands of each coarse bundle, assume a,c≤S/2. The four dimensions in Hom(V_c,G_c) are

    max(c−a+1,0), S−a−c+1,
    max(a+c−S+1,0), max(a−c+1,0).

If a+c<S, their sum is at most S−a−c+1+|a−c|+2≤S+3. If a+c=S, then a=c=S/2 and their sum is four, again at most S+3. Therefore

    0 ≤ h^0(K_m) ≤ 2m+2,
    4m+1 ≤ h^(1,1)(X_m) ≤ 6m+3,
    4m   ≤ h^(1,2)(X_m) ≤ 6m+2.

This leaves h^0(K_12) between zero and 26. It is a bound, not an exact solution, and the bound need not be sharp for geometrically admissible sections.

## Exact algebraic nonuniqueness of the numerical input

On P1, put D=O^2⊕O(−1)^2 and L=O(2m). In homogeneous coordinates [X:Y], consider

    φ_A=(X^(2m),Y^(2m),0,0),
    φ_B=(0,0,X^(2m+1),Y^(2m+1)).

Both maps D→L are surjective, since the two nonzero entries have no common projective zero. Both have rank-four degree−2 source, degree2m target and zero-dimensional cokernel of length zero. Their full kernels are, respectively,

    ker φ_A = O(−2m)⊕O(−1)^2,
    ker φ_B = O^2⊕O(−2m−2).

The first formula is the ordinary degree2m pencil sequence plus the two unused summands. The second is the degree(2m+1) pencil sequence tensored by O(−1), plus the two unused trivial summands. Both kernel degrees equal −2m−2, but their global section dimensions are zero and two. For m=12 the respective splitting triples are (−24,−1,−1) and (0,0,−26).

The examples prove precisely that the numerical constraints already derived do not fix the kernel. They do not establish nonuniqueness within the geometric comb family. That stronger assertion would require two actual admissible period sections, which have not been constructed in this audit.

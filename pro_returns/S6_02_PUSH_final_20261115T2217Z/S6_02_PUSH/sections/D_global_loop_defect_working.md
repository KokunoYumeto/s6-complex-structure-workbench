# The global radial-loop defect of an arbitrary cap

**Status: full working proof for reserved B.4.32; not yet input or registered.** Boundary_d, 15 November 2026. Root and AB independently proposed or checked parts of the mechanism. This file does not itself assert the final noncompletion theorem reserved for B.4.33.

## Statement to be proved

Assume any proper analytic filling of a finite parameter cover of the actual six-sphere family exists. Retain its reduced main component, normalize and resolve it, and then resolve the graph of the intrinsic marked map and the central support as in the strengthened B.4.31. B.4.4 applies to the smooth connected dominating fourfold without any hypothesis on the central fibre. After deleting finitely many values of the marked P1 base, the following invariant is defined.

Use the local ordinary origins of the proved partial family B.4.19 as reference. Any local cap section, after any necessary finite root of r, has a radial-loop defect in

    V = (Λ⊗Q)/(Qδ).

Divide the defect by the root degree. This normalized class is independent of the extending cap section, and of all source modifications and further roots used to obtain it. It patches, in the actual homology marking, to a flat section of V over the remaining ordinary base. This section is zero.

Consequently, if a finite cap multisection of degree d has trace t, then the r-loop class of t−d o, measured in V, is zero. Here o is the B.4.19 ordinary local origin. The same conclusion applies to any origin obtained from these traces by differences that are bounded logarithmic sections on the strict r-axis.

Only the loop class is controlled. The holomorphic difference t−d o need not itself be bounded or extend at r=0.

## 1. The loop class without choosing a meromorphic lift

Over a simply connected ordinary base chart U, the Jacobian of the actual family has its marked period presentation. Its r-monodromy is

    T = I−mE,   E=δ⊗γ,   m>0,   E²=0.

The Lie bundle has the ordinary holomorphic frame used in the period matrix. For a holomorphic Jacobian section a on U×Δ_r*, take a holomorphic lift on the universal cover of the r puncture. After one positive loop, the difference between its endpoint and its initial value is an actual period. Let v(a)∈Λ be its period label at the chosen base point. Changing the lift by a period changes this label by an element of

    (T−I)Λ ⊂ Zδ.

Thus a determines a well-defined class

    ν_r(a)∈Λ_Q/Qδ.

Equivalently, this is its connecting class in H¹(Δ_r*,Λ), followed by the quotient to Λ_Q/Qδ. No single-valued additive lift on the punctured disc is assumed. A varying holomorphic section gives a locally constant such class as q varies, because the integral period label varies continuously.

For r=R^e, the pullback monodromy is T^e. Restriction of the connecting class is

    v ↦ (I+T+⋯+T^(e−1))v.

Modulo Qδ this is e v. Therefore define the normalized defect of an extending section b on the root cover by

    λ(b;o) = (1/e) ν_R(b−o(R^e)) ∈ V.

It is unchanged by further roots. This definition also makes the transfer/trace normalization exact; no arbitrary choice of a logarithm of r is being concealed.

## 2. Exact ordinary affine-overlap audit

The reference origins are the actual ordinary origins in B.4.19, not arbitrary zeros of abstract isomorphic tori. Recall v=(2πi)^−1 log r, c=−12v, and

    ζ̃_i = ζ + k_i v δ,   k_i=(2πi)^−1 log K,
    K(x)=x⁴/(x−1)³.

Their local zero is ζ̃_i=0. On an ordinary overlap k_j−k_i=n_ij∈Z, so the extra translation is n_ij vδ. Its positive r-loop period is n_ijδ and is zero in V.

The linear Lie-frame maps are independent of c and r. For the two generating finite peripheral changes they are exactly

    R1=[[-1/τ,0],[(1−μ)/τ,1]],
    R2=[[ 1/τ,0],[    −μ/τ,1]],

and satisfy R_jδ=δ and R_jΠ_c=Π'_c A_j. Compositions preserve these properties. Thus a change of period frame applies the actual lattice matrix A_j to a loop class; it does not add an unrecorded r-dependent Lie-frame contribution.

The only potentially dangerous nonconstant connector is the finite-root-to-ordinary translation. B.4.19.4 computes it exactly:

    σ_j,c = w_j Π_c v_j,
    k−k_j = 12 ε_j w_j,   γ(v_j)=ε_j,
    σ_j,c + (k−k_j)vδ = w_j Π_part v_j.

Since c=−12v, the entire r logarithm cancels. The last expression is independent of r and contributes zero radial-loop defect. The remaining finite deck maps contain the factors r⁴ and r^(−3) in their multiplicative coordinate; these add only integral δ periods to the loop. Passing to a sector or changing its period representative adds (T−I)ℓ, also in Qδ.

On a punctured cusp sector, B.4.19.5 gives the additional comparison

    G(s)+6vδ,   G(s)=(μs/2, Cs/12−s²/24),

where G is independent of r. Its radial-loop defect is again purely δ. A full twelve-component shift must not be called the identity: it can include translation of the elliptic base by 6P. As an actual period representative, however, its radial-loop change is (T−I)γ, which is in the same δ line.

Therefore all reference origins have zero relative radial-loop defect in V on their overlaps. They define a globally consistent reference **loop class**, even though they need not form a single global affine origin. Changing the coherent closing by a global scalar C* gauge also changes a radial loop only by an integral δ winding and leaves this assertion unchanged.

AB independently checked every displayed overlap, including the finite connector cancellation and the cusp comparison. The proof uses the actual source-to-target period covariance, not merely a statement that a translation happens to look like a second coordinate.

## 3. Any two extending cap sections have the same normalized class

Resolve the marked graph and central support globally. Use the closed normalized branch-intersection spaces, proper over P1, to delete the finitely many critical or nondominating values as in B.4.31. On a sufficiently small ordinary q disc, a finite root of r and the finite toric subdivisions used in B.4.30 make the map semistable with the q parameter retained. On an overlap take a common further root and common refinement to compare the constructions. No global semistable model over the whole punctured P1 is asserted or required.

The nearby torus fibres are connected. The proper normal map to the normal two-dimensional base has trivial finite Stein factor because its generic fibres are connected. Hence the central surface fibres are connected too.

The saturation argument of B.4.30 applies without the rank-two assumption: it only needs the known normalized rank-two form subbundle of the canonical log-de Rham extension. Over an ordinary q chart, the r-logarithmic period term is solely the δ⊗γ term, so the same explicit subbundle extends. What rank two supplied there was the residue calculation.

Here B.4.31 supplies the stronger required residue statement directly. Every local angular class is an integral multiple of δ. The first normalized form has period zero on δ, and the second has integral period one (or minus one with the W character convention). Thus the local logarithmic primitives have residue vector

    (0, integer).

Their exponentials consequently lie in

    O* × M_r^gp,

which is exactly the bounded character sheaf along the strict r-axis. In particular the first character has zero r-order.

Given two sections extending into this same semistable cap, the finite chart-chain proof of B.4.30 compares them by these characters. The first character has zero radial winding; the second can wind only by an integer δ period. Hence

    ν_R(b−b')=0 in V.

The connectedness just established makes this true even when the two sections meet different components of the central fibre. For sections requiring different roots, pass to a common root and divide by its degree. Their normalized defects relative to the reference origin therefore agree.

Smooth points of the reduced central fibre have transverse holomorphic sections. Thus the common defect exists locally around every remaining ordinary q. A finite multisection gives the same class: after a common cyclic root it splits into sections, all with this normalized class; the connecting class of its trace is the sum of their classes. Dividing by its degree gives the same invariant. Proper lifts through modifications and further roots do not change it, by the preceding comparison and the restriction formula in §1.

## 4. Global continuation and the exact fixed-space calculation

The invariant λ(q) is locally constant in the actual homology local system: on one q chart choose one extending section; its integral connecting label is constant. On overlaps, independence of the cap section and the zero reference-overlap defect in §2 make these local definitions agree under the actual lattice transport. Thus λ is a globally defined flat section of V. Alternatively, retaining finite multisection branches gives a finite monodromy orbit; the argument below also excludes that possibility.

In the ordered quotient basis (γ̂,û,ŵ), the two generating matrices are

    Ā1 = [[1,0,0],[6,0,1],[−6,−1,−1]],
    Ā2 = [[1,0,0],[0,0,−1],[−6,1,0]].

Their rational fixed lines are

    Fix(Ā1)=Q(1,2,−4),
    Fix(Ā2)=Q(1,3,−3).

They have zero intersection. Removing additional ordinary points from P1 does not remove either peripheral monodromy from the image: the induced map to π1(P1 minus {0,1,∞}) is surjective. Hence a global flat section of V is zero.

For completeness V has no nonzero finite orbit either. The γ coefficient is invariant under the whole group. Averaging a finite orbit gives an invariant vector with the same γ coefficient, so that coefficient must be zero. The orbit then lies in the elliptic two-dimensional subspace, where the two unipotents of B.4.31 have different fixed lines and no nonzero finite orbit.

It follows that λ(q)=0. In particular every finite trace t of degree d has

    ν_r(t−d o)=0 in V.

If an origin h is obtained from such traces by differences that are bounded logarithmic sections on the strict r-axis, those differences also have defect in Qδ. Therefore ν_r(h−d o)=0 as well. Applying the globally invariant covector γ gives zero. This is the only component needed for the intended B.4.33 cusp contradiction.

## 5. Scope retained

The proof does not assert that h−d o is meromorphic, bounded, or holomorphically extendible. A common essential translation with zero period defect remains possible. Its irrelevance to the final comparison must be proved using only the γ component of the loop class.

The proof uses the global marked P1 base and the actual peripheral matrices. An arbitrary rank-one degeneration over a small isolated q disc need not satisfy this conclusion. For an exact example, change the punctured marking of a standard local cap by the translation χ(r)=[(log r)/(2πi)·u]. It is single-valued as a torus translation because u is an actual r-invariant period. The same proper cap now has defect u modulo Qδ relative to the old origin, while every difference of two extending sections remains unchanged. This marking cannot patch over the full ordinary base because u has infinite Γ-orbit. The Hopf insertion B.4.15 is not asserted to furnish this particular nonzero generic defect.

The current hypotheses allow an arbitrary proper analytic filling. Resolution of its reduced main component gives the smooth fourfold needed by B.4.4 and B.4.31 without changing the punctured family. Its central divisor may have multiplicities. Only the local two-parameter semistable reductions proved directly in B.4.30 are used; a global nonprojective semistable-reduction theorem is not assumed.

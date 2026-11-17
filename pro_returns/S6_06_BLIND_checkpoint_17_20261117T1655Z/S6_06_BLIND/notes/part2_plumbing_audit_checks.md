# Independent check of the two-component plumbing proposed for Part 2.6

This note checks the parent's proposed construction against the supplied
Engel source. It does not assert that a merely named plumbing is a completed
global analytic construction. The global collar atlas and its properness
argument remain the responsibility of the construction in Part 2.

## Bundle typing and the generic quotient

Write h=t_{6P}, M=O(P-O), and
L=Hom(h^*M,M)=O(F_infinity), with section phi. These are the line bundle
and linearization in Engel's construction. Let Y_0,Y_1 be two copies of
P(O plus M). At the first neck, a zero coordinate z_0 in M_p and an infinity
coordinate w_1 in M_{h(p)}^{-1} have product in L_p. Thus

    z_0 w_1 = r phi(p)

is intrinsically typed. At the second neck the zero coordinate z_1 and
infinity coordinate w_0 lie in inverse line bundles over the same base
point, so z_1 w_0=r is intrinsically typed. Passing through the first neck
gives z_1(h(p))=z_0(p)/(r phi(p)); passing through the second gives

    (p,z_0) -> (h(p), z_0/(r^2 phi(p))).

The inverse map covers h^{-1} and multiplies by r^2 phi(h^{-1}(p)). It is
exactly Engel's generator with u=r^2 on S minus F_infinity. This explicitly
identifies the generic quotient; no unproved equivalence of the two
generators is needed.

## The blowup and the remaining singular section

Near the node of F_infinity take coordinates x,y with phi=xy. The first
neck is zw=rxy. Its central component z=r=0 is a global component in the
two-component plumbing. Blowing up its coherent ideal (z,r) has the charts

    r=z a, w=a xy;             coordinates (z,a,x,y),
    z=r b, bw=xy;              coordinates (b,w,x,y,r), relation bw=xy.

The first chart is smooth. The second is the product of the ordinary
three-dimensional double point bw=xy with the r disk. Its singular locus
is b=w=x=y=0 for all r, and it does not meet the overlap with the first
chart, where b is invertible.

The blowup of (b,x) is the standard small resolution. In the two affine
charts it is

    x=b c, w=c y;              coordinates (b,c,y,r),
    b=x d, y=d w;              coordinates (x,d,w,r).

The overlap has c=d^{-1}, x=b c, y=d w. The resolution is an isomorphism
away from b=w=x=y=0: the ideal is invertible at every other point of the
quadric. Hence its restriction to the complement of the singular section
is canonically the original open set. Gluing this restriction to the
unmodified complement produces a modification on a neighborhood of the
entire singular section, uniformly over the r disk. In particular there
is no obstruction arising from an isolated choice at r=0. One may take a
fixed small nodal neighborhood in S before shrinking the parameter disk.

The other small resolution uses the opposite ruling. To identify the
result with the precise compactification denoted X(u) in Engel, Part 2
must match this ruling with the chosen Mumford diagonal. The displayed
local singularity is an ordinary double point, rather than an A_2
threefold singularity.

## Involution and quotient

The involution r -> -r fixes fibre coordinates of Y_0 and negates fibre
coordinates of Y_1. Both plumbing equations are preserved. On the first
neck take z fixed and w negated. Then the second blowup chart has

    (b,w,x,y,r) -> (-b,-w,x,y,-r).

Both ideals (z,r) and (b,x) are invariant. The involution consequently
lifts to the blowup and small resolution. Their coordinate charts make
the lift holomorphic without an appeal to birational extension.

On a proper Hausdorff analytic plumbing, the finite quotient is again a
proper Hausdorff analytic space. Its parameter is u=r^2, and its generic
fibre is the generic resolved fibre at either square root r. Flatness
follows locally from torsion-freeness over C{u}: multiplication by u is
injective on the smooth resolved total-space local rings, hence also on
their invariant subrings. A torsion-free module over the convergent
power-series discrete valuation ring C{u} is flat. Multiplicities in the
central quotient fibre are allowed and do not affect this argument.

## Exact remaining global checks

The local calculations establish the typed gluing, generic deck map,
smooth resolution charts, compatibility of the resolution, and quotient
flatness. A complete construction still has to display a finite collar
atlas over the compact surface S, a uniform parameter radius for its
overlaps, and a compact-fundamental-domain/Hausdorff argument. It must
also compare the chosen local small resolution with Engel's stated
Mumford filling. These are construction checks, not counterexamples to
the two-component proposal. The earlier one-component version has a
different specific defect: its two local branches need not define one
global central-component ideal. Keeping the two components distinct
removes that defect, as the ideal (z,r) above shows.

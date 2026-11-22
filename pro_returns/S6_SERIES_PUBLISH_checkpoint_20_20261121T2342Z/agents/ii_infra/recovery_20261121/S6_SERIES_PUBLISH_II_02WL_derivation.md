# 02WL / night:P4.14: prereading derivation

Checker: restore_build. New derivation after checkpoint-14 restoration, 21 November 2026. I have read only the original statement packet and its cited external CDP20 paragraph. I have not opened the target printed proof, A's reconstruction, or genus_one_conductor.py.

## The cited inference and the two projective curves

The supplied CDP20 source is `S6_SERIES_PUBLISH_work/S6_GRIND_6_literature/papers/arXiv_1904.11179v2_CDP20_corrigendum_src/main.tex`. Its lines 1093–1097 make the relevant inference from a reduced Gorenstein genus-one curve with trivial dualizing class and rational normalization to a cycle of rational curves in the reducible case. I opened that precise external input and a small following context only. I have not imported the proposed threefold conclusions of that proof into the examples below.

Work over C. The curves are the Cartier cubics in P² defined by

    C_tan: Z(Y²-XZ)=0,
    C_tri: XY(X-Y)=0.

All displayed factors are distinct, so both curves are reduced. A Cartier hypersurface in the smooth plane is Gorenstein. Adjunction gives the actual line-bundle isomorphism ω_C≅(ω_P²⊗O_P²(3))|C≅O_C for each cubic. The ideal-sheaf sequence 0→O_P²(-3)→O_P²→O_C→0 gives χ(O_C)=0, hence arithmetic genus 1. Below the same Euler characteristic is independently recovered from the normalization quotient lengths.

## The line tangent to the conic

The line L=(Z=0) and conic Q=(Y²=XZ) are smooth rational curves. The latter is parametrized by [s:t]↦[s²:st:t²]. On L their intersection is the single point p=[1:0:0], with multiplicity two, because restriction of the conic equation to L is Y². This is the complete intersection locus, and the gradient (-Z,2Y,-X) verifies the conic's smoothness.

In the affine chart X=1, put u=Y and v=Z. The two branches are v=0 and v=u². The local normalization map is the injective ring map

    R=C{u,v}/(v(v-u²)) → B=C{t}⊕C{t},
    h ↦ (h(t,0),h(t,t²)).

Here C{ } denotes convergent power series; the same computation holds after completion. The image is exactly

    {(a,b): b-a ∈ t² C{t}}.

Necessity follows by subtracting the two evaluations. Conversely, for b-a=t²d(t), the convergent series h(u,v)=a(u)+v d(u) maps to (a,b). This explicitly proves the identification of the local ring with the stated subring.

The conductor is the largest B-ideal contained in R. A pair (a,b) belongs to it precisely when (ac,bd) satisfies the image condition for every pair (c,d). The choices (1,0) and (0,1) force both a and b to be divisible by t². Conversely, both divisibilities make every product satisfy the image condition. Therefore

    conductor(R⊂B)=t²C{t}⊕t²C{t}.

The order is exactly two on each normalization branch. The difference map (a,b)↦b-a mod t² identifies B/R with C{t}/(t²), of dimension two. Thus δ_p=2. The two-component normalization is P1⊔P1, and the normalization sequence gives χ(O_C)=2-2=0 again.

## Three concurrent lines

The second curve is the union of the distinct lines X=0, Y=0 and X=Y. They all meet at p=[0:0:1]; there are no other pairwise intersections. Every component is P1. In the chart Z=1, put x=X and y=Y. The normalization is

    R=C{x,y}/(xy(x-y)) → B=C{t}³,
    h ↦ (h(0,t),h(t,0),h(t,t)).

Write a_i for the ith coefficient of a power series a. Its image consists exactly of triples satisfying

    a_0=b_0=c_0,          c_1=a_1+b_1.

Necessity follows from the constant and linear terms of h. For sufficiency, put a_0=b_0=c_0=r and

    d(t)=(c(t)-a(t)-b(t)+r)/t².

The stated coefficient conditions make d convergent. Then

    h(x,y)=a(y)+b(x)-r+xy d(x)

has the required three restrictions. This is an explicit inverse construction on the image, valid for every convergent triple with the constraints.

The conductor calculation can again be made by multiplying by the three coordinate idempotents of B. For a conductor triple, multiplication by the first idempotent must give a triple with matching constants and with the displayed derivative relation; hence a_0=a_1=0. The other two idempotents similarly force b_0=b_1=c_0=c_1=0. Conversely, triples all of whose components vanish to order at least two remain in the image after arbitrary multiplication. Thus

    conductor(R⊂B)=t²C{t}⊕t²C{t}⊕t²C{t}.

Its branch orders are exactly two. The two independent constant constraints and the one independent linear constraint show dim_C(B/R)=3. The normalization sequence gives χ(O_C)=3-3=0, again agreeing with adjunction and the plane cubic genus computation.

## Why the reducible nodal-cycle conclusion does not follow

At a node the local ring is C{u,v}/(uv), whose image in C{t}⊕C{s} is the pairs with the same constant term; its conductor is tC{t}⊕sC{s}, with branch orders one. This follows by the same explicit coordinate-idempotent argument. Any analytic isomorphism of curve germs induces an isomorphism of their normalizations and carries the conductor ideal to the conductor ideal, because the conductor is intrinsically Hom_R(B,R). The valuations of this ideal in each normalization DVR are consequently preserved, up to permutation of the branches.

The first curve has a singularity with branch orders (2,2), and the second has a singularity with three branches and branch orders (2,2,2). A cycle with only ordinary nodes has two branches and orders (1,1) at every singular point. The displayed invariant computations exclude such a local analytic isomorphism for each example. They therefore supply two reduced Gorenstein reducible genus-one curves with trivial dualizing sheaf and rational normalization which are omitted by the quoted inference.

The inference tested here has hypotheses and conclusion about a curve. The calculation supplies no smooth compact threefold, no torus degeneration with the global Betti hypotheses, and no value of a threefold's top Chern number. It establishes failure of that exact curve-classification step; it does not establish failure of the separate threefold sign statement. No assertion that these curves cannot occur in some other geometric construction is being made.

## Computation and pre-release status

The local-ring image and conductor calculations above are proved for arbitrary convergent series. The fresh exact-arithmetic program `S6_SERIES_PUBLISH_II_WJ_WL_fresh_exact.py`, SHA-256 d50c5b6e4fd18c272c4b3c265b313acccd46fb3b779b789360bafa8ec57b4beb, additionally computes the restriction maps on jets of orders two through eight, their cokernel dimensions, and conductor membership as a linear condition against every coordinate idempotent and monomial multiplier. All twenty-one tangent/triple/node checks pass. The output SHA-256 is a46d2bcc167deb5d4eb6fe8d37318e796a8da8ed1ba381b4ac3441c90989c9f1. The finite calculations verify the formulas and do not replace the arbitrary-series proofs. No inherited conductor-checking program was opened or imported.

Every target conclusion has been derived from the original statement and the cited external input. The target's printed proof remains unopened. No event or canonical mutation is made by this record.

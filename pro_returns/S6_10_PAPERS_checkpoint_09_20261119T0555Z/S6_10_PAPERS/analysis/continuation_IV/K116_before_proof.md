# K116: OS45 source cover and unselected-II disc, before the printed proof

19 November 2026, GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation, reviewer /root/ledger.

Inputs: the literal K116 and K119 statements from the verified cp36
results CSV, the previously read whole-zero construction and actual
marked-line conventions, and my earlier statement-only arithmetic.
The K116/K119 proof files and producing programs have not been opened.
This is a derivation attempt whose remaining geometric obligations are
explicitly listed at the end; comparison must not erase those limits.

## Source polynomial, selected normalization, and marked section

Write R=t^2+a, f=R^2+t, g=R^3+3tR/2+3/8. Direct expansion gives

    f^3-g^2 = -(48a(t^2+a)^2+8t^3+72at+9)/64.

Thus the finite discriminant polynomial, up to its fixed nonzero factor,
is D=48a(t^2+a)^2+8t^3+72at+9. At a nonzero generic a it has
degree4; at a=0 it has degree3, so the source at infinity changes its
generic I8 profile to I9. These exceptional parameter points must be
retained as excluded source points, not included in the present filling.

For the displayed source parameter u, put

    a=-u/3-u^4/9,
    tc=1/(2u)-u^2/3,
    xi=1/(4u^2)+u/3.

Substituting these expressions yields f(tc)=xi^2 and g(tc)=xi^3.
Hence the selected cubic is exactly

    y^2=(x-xi)^2(x+2xi).

Its actual normalization is x=S^2-2xi, y=S(S^2-3xi), with inverse
S=y/(x-xi) away from the nodal point. Since c^2=3xi, choosing the
ordered node branches is equivalent to c=v/(2u), v^2=4u^3+3.
The inverse torus coordinate Z=(S-c)/(S+c) sends the two ordered
branches to0 and infinity. At G=(R,sqrt(3)/2), R(tc)-xi=-u, so
S_G=-sqrt(3)/(2u) and exactly

    Z_G=(sqrt(3)+v)/(sqrt(3)-v).

These are equalities of the original coordinates and their inverses,
not an identification that discards the marked branch order.

The smooth completion of v^2=4u^3+3 is a genus-one curve: the double
map to the u-sphere has four simple branch points, the three finite
roots of4u^3+3 and infinity. Riemann--Hurwitz gives
2g-2=2(-2)+4=0. The point over infinity is a single point.

## Locate the finite type-II values and their marked lifts

A finite cusp of the elliptic cubic has f=g=0. Solving these equations
using R gives t=-R^2 and R^3=3/4; consequently a=R-t^2=R/4 and

    256a^3-3=0.

The literal pullback to the selected-node cover factors as

    729(256a^3-3)
      = -(4u^3+3)^2(16u^6+120u^3+243).

The first factor is v^4. At the three v=0 points it is the selected
node itself that becomes a cusp. The second factor gives twelve
ordered selected-node points: its quadratic in z=u^3 has two distinct
nonzero roots, each has three distinct u-values, and none has v=0,
so each lifts to two distinct v-values. At each of those twelve points
the selected cubic remains nodal and ordered; the cusp occurs at an
unselected value. The degree4 discriminant then has one double root
at the cusp and two remaining simple nodal roots.

The ordinary-cap collision equation D(a,0)=0 is16a^3+3=0. Its pullback
is the exact factorization in K119,

    2187-16u^3(u^3+3)^3
     =-(2u^3-3)(8u^9+84u^6+342u^3+729).

It gives24 marked points: six with selected tc=0 and eighteen with
unselected tc different from0. It is disjoint from the type-II set
because16a^3+3 and256a^3-3 have no common root. It is also disjoint
from a=0. The remaining source infinity changes a=0 occur at the two
points u=0,v=plus/minus sqrt(3), and at the six points u^3=-3.

The complete proposed48-point list is therefore:

    u=0:2; infinity:1; selected cusp v=0:3;
    a=0 with u nonzero:6; unselected cusp:12;
    ordinary-cap collision:24.

The counts sum to48. Every overlap has been explicitly excluded by
the equations above; the infinity point belongs only to its own entry.
The exact source proof must confirm that there is no further forbidden
boundary imposed by the original full linearization or cap reference.
The marked punctured genus-one curve then has the standard presentation
[A,B] mu1...mu48=1 obtained from its oriented polygon with48 punctures.
No meridians or handle generators are identified with one another.

## The local unselected-II family

At a cusp, let R0^3=3/4, a0=R0/4, t0=-R0^2. One has

    f_t=4tR+1=-2,
    g_t=6tR^2+3R/2+3t^2=-3R/4,

at that point; in particular g_t is nonzero. The surface equation
F=y^2-x^3+3fx-2g therefore has F_t=-2g_t nonzero at the cusp.
The total elliptic surface is smooth there, and projection of the
source family to the a-disc is a submersion: F_t solves the surface
equation locally for t as a holomorphic function of(a,x,y).
This checks smoothness of the actual source family at the formerly
unselected nodal points, not merely of a discriminant curve.

The twelve lifted points have da/du=-(4u^3+3)/9 nonzero and v nonzero.
Thus the map from the marked source cover to the a-disc is locally
invertible there; the selected branch order remains a literal
holomorphic choice on that disc. The selected node is still simple,
the original cap value0 remains ordinary, and a0 is nonzero, so the
infinity profile stays I8. The point G has nonzero y-coordinate,
so it avoids the unselected cusp.

The marked relative divisors [8G] and[O] give the actual relative line
M8=O([8G]-[O]); its full transition ratios are the ratios of local
defining equations of these two relative Cartier divisors. Translation
by-G and the normalized Hom section are the original source maps.
The source construction makes the latter vanish simply at the selected
whole fibre and nowhere else. On the local parameter disc the same
relative Cartier operation and the fixed normalization carry its full
coefficients. A compact family of Hermitian operator norms gives one
common strict-contraction scalar, since the source surfaces are compact.

The ordinary cap remains on a protected smooth fibre; its full period
logarithms extend because their nonzero holomorphic factors extend on
this simply connected parameter disc. The selected toric fan and the
infinity attachment retain their original character and root equations.
On a fixed affine chart, any fixed integral monomial applied to the
extended nonzero unit factors is again an extended nonzero unit; the
map and inverse are obtained by the same original exponent matrix.
This supplies the intended gluing mechanism, but the specific source
normalization and infinity charts still have to be checked against the
complete supplied construction, as recorded below.

## Return and fixed-scalar comparison

Once the actual source, line, cap and selected-fan gluing extend across
this disc, its completed family is a proper smooth submersion there.
A horizontal distribution on this compact family yields transport.
Contracting the boundary loop through the disc, with the chosen base
point fixed, gives an isotopy of its return to the identity. The marked
source coefficient maps are single-valued on the disc, so its boundary
endpoint is the original marked endpoint under these actual maps.
No parameter-loop class is inferred from a different unmarked family.

For any scalar already admitted on the original boundary, scale it
toward the common smaller scalar along a constant-argument interval.
Every intermediate norm decreases, so strict contraction persists.
The chosen scalar logarithm varies by a real interval and acquires no
integer winding. The same complete cap logarithms and period reference
then give a proper smooth annular comparison with the disc family.
Its two boundary returns are conjugate through the resulting marked
transport, up to an explicitly isotopic physical scalar action.
The same zero return class consequently holds at the prescribed scalar.

## Exact boundary of this prereading attempt

The polynomial cover, selected coordinate maps,12-point count, proposed
48-point puncture list, local source submersion at a typeII point, and
the disc/annulus return argument have been rederived here. A full proof
comparison must still verify the original normalized Hom coefficient,
its relative extension on the resolved infinity components, and the
complete source/cap/fan gluing with its stated properness. Those are
not silently awarded a before-reading verification by the abstract
gluing description above. The printed proof will now be opened only
after this file's hash and timestamp have been saved.

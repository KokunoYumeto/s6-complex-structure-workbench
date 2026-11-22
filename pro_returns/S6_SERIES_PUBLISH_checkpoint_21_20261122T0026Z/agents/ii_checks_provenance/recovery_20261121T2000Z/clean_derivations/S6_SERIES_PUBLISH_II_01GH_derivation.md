# Prerelease derivation: 01GH / cdp:st:E10

Checker: `i_provenance_recovery`. The exact safe E10 statement, its
empty supplement and the E5 statement/formula input were read.
Neither the E10 target proof, another checker's reconstruction nor
E_checks.py has been read. The isolated E17 routine was opened only
after E17 froze and contains no E10 material. Related Paper I and
my already completed II B2 construction are disclosed prior exposure.

I use the actual smooth projective elliptic surface independently
checked as B2/01BL in group02. Its finite-chart equation is

    y²z=x³+(t⁴+1)xz²+t⁶z³,

with infinity chart x_inf=s²x, y_inf=s³y, s=1/t. It has twelve
nodal fibres at the distinct roots of D(t)=31t¹²+12t⁸+12t⁴+4,
and its fibre at infinity is smooth. That exact statement, its
complete verification and original prerelease derivation survive
in the completed group02 recovery bundle. It is an established
input to this new construction, not an E10 proof excerpt.

Take two copies E1,E2 of this surface, with maps h1=h and h2=h+10
to the same P1. Thus the fibre of E2 over t is the original elliptic
curve at t−10. Every root of D has absolute value less than two:
for r≥2,

    12/r⁴ + 12/r⁸ + 4/r¹² ≤ 12/16+12/256+4/4096 <31,

so 31r¹² exceeds the sum of the absolute values of the other
terms. The critical-value discs of the two maps are centred at
0 and 10, each of radius two, and are disjoint. Their fibres at
infinity are smooth. The fibre product

    X=E1 ×_(P1) E2,       f:X→P1,

is therefore a smooth compact connected projective threefold.
Indeed its local defining equation h1−h2 has nonzero differential
because the two maps have no common critical value. A general
fibre is the product of two elliptic curves and is a complex
two-torus. All fibres are connected. This is an exact fibre
product construction, with the two projection maps fixed.

Let C_s be the compact double cover of P1 defined by

    v²=(t−1)(t−2)(t−3)(t−4)(t−5)(t−6−s)

for s in a sufficiently small disc about zero, and let h_s:C_s→P1
be its projection. Use its degree-six homogeneous equation in the
weighted projective plane P(1,1,3) for compactification. All six
branch values remain distinct; the curve avoids the singular
weighted-projective point. These equations give a proper smooth
family of curves. Riemann–Hurwitz gives 2g(C_s)−2=−4+6=2,
so every C_s has genus two.

All fixed branch values are real. D(t)>0 for real t, and also
D(t−10)>0 there, so none is a critical value of f. The moving
branch value remains near 6, away from the two closed radius-two
critical discs. Thus h_s is unramified above all critical values
of f for every sufficiently small s. Define the actual family

    Y_s=X ×_(P1) C_s,       g_s:Y_s→C_s.

The fibre product of X with the entire curve family is a proper
holomorphic submersion over the s-disc. Near a critical value of
f the curve map is a local biholomorphism, so the fibre product
is locally the smooth X with a parameter. Near a branch value
of h_s, the map f is a holomorphic submersion, so the local
product is a smooth fibre of f times the smooth curve family.
These two descriptions also prove smoothness everywhere else.
Hence Y_s is an actual small deformation of the smooth compact
threefold Y_0, and g_s is a proper holomorphic fibration with
connected fibres and two-torus general fibre.

The fibration g_0 has Kodaira–Spencer rank two at a regular point.
Take t=7, which lifts to the point (7,12 sqrt(5)) of C_0 and is
not a branch or critical value. The j-invariant of the original
elliptic family is

    j(t)=1728*4(t⁴+1)³/D(t),
    j'(t)=−1728*1296*t¹¹(t⁴+1)²/D(t)².

Both derivatives j'(7) and j'(−3) are nonzero. A first-order
trivialization of an elliptic family would make its intrinsic
j-invariant constant to first order; these derivatives therefore
give nonzero elliptic Kodaira–Spencer classes. Each lies in the
one-dimensional H1(E,T_E)=H1(E,O_E) tensor Lie(E). Pullback by
h_0 has nonzero differential at the chosen point. On the product
torus F=E_(7)×E_(−3), the tangent and structure-sheaf Künneth
maps send the two deformation classes to

    kappa=c1 u1 tensor eta1 + c2 u2 tensor eta2,  c1*c2 != 0,

where u1,u2 are the invariant tangent directions of the respective
factors and eta1,eta2 are their pulled-back H1(O) generators.
There are no off-diagonal terms because the transition maps of
this family are products of the two elliptic transition maps.
The coefficient matrix is diagonal with both entries nonzero,
so its rank is two. This is the same tensor convention as the
safe E5 input.

It remains to prove failure over the original fixed target C_0.
First, C_s is not isomorphic to C_0 for every sufficiently small
nonzero s. On a genus-two hyperelliptic curve the forms dt/v and
t dt/v are a basis of holomorphic one-forms: their local orders
at the branch points and the two points at infinity are
nonnegative, they are independent, and the genus gives dimension
two. Their canonical map is exactly the double-cover projection
to [1:t]. Thus an isomorphism C_s→C_0 descends to a Möbius map
taking the unordered branch set {1,2,3,4,5,6+s} to
{1,2,3,4,5,6}. The images of the fixed points 1,2,3 determine that
Möbius map and each is one of six distinct target points. There
are finitely many such maps. For each, the preimages of the six
target branch points form a finite set of possible values of
6+s. Consequently only finitely many s can give an isomorphic
curve. Shrinking the disc excludes all such values except s=0.

Now let phi:Y_s→C_0 be any holomorphic map. Its restriction to a
smooth torus fibre is constant. Indeed the universal cover C²
of the torus lifts that map to the unit-disc universal cover of
the genus-two curve; the lift is a bounded entire holomorphic
function and is constant by Liouville. Thus phi is constant on
each general fibre of g_s. The proper image of (g_s,phi) is
either a point over C_0 or an irreducible compact curve in
C_s×C_0 projecting generically with degree one to C_s. Its
normalization therefore projects isomorphically to the smooth
curve C_s. This gives the exact holomorphic factorization

    phi=psi o g_s,             psi:C_s→C_0.

If phi is nonconstant, so is psi. Riemann–Hurwitz between these
genus-two curves gives 2=2 deg(psi)+deg(R_psi), forcing degree
one and zero ramification. Thus psi is a biholomorphism, which
has just been excluded for every sufficiently small nonzero s.
There is therefore no nonconstant holomorphic map Y_s→C_0 for
those s, so the original fibration g_0 cannot extend over its
original fixed positive-genus target along this actual deformation.

For the infinitesimal interpretation in the supplied E5 sequence,
a trivial first-order deformation of C_s would induce a first-
order Möbius motion of its canonical branch set. A vector field
a+b t+c t² on P1 vanishing at the fixed branch values 1,2,3
is zero, whereas the branch at 6 has velocity one. Thus the
curve Kodaira–Spencer class is nonzero. Compatibility of the
transition maps of the actual map family gives
H1(dg_0)(KS_Y)=g_0*KS_C; the safe Leray injection makes this
nonzero. This corroborates the stronger pointwise obstruction
above without being needed to infer it.

The fresh exact certificate computes the two rational j-derivatives
by dual-number arithmetic, checks the strict root bound, and
checks the branch-motion interpolation matrix. It has been
written and run before any E10 proof or old routine is opened.

In the last Cech comparison, differentiate the transition identity for the family map. It gives dg(xi_ab) minus g*beta_ab equal to the difference of the two derivatives of the local map representatives; the latter is a Cech coboundary. This is the specified map on H1 used in that paragraph.

Exact bound input/computation: `agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_01GH_preproof_family.py`, SHA256 `ece4a4e48e3e178fafa4a65d9219baec26094cec5b00a201fb1c9053b5eb5f59`.

Exact bound input/computation: `agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_01GH_preproof_family.output.json`, SHA256 `d5d4d720060a9dd0fdc4d328e7e6738e01b63868dda94ebd3c163613e6411dec`.

Exact bound input/computation: `agents/ii_checks_provenance/recovery_20261121T2000Z/group02/S6_SERIES_PUBLISH_II_01BL_recovery_proposed.tex`, SHA256 `4a60b01bf3ae64830f8e9cabf4c40c301b4ad5233cd0fc9a0ae0c2b90856b2ae`.

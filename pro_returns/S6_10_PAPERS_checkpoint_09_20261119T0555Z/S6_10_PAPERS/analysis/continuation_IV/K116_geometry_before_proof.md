# K116: further concrete source and line derivation before its proof

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation, reviewer /root/ledger.

This extends the saved 05:08:21 UTC attempt. The K116 proof and its
producer programs have still not been opened. The inputs are its literal
statement, the explicit OS45 equation, and the previously read general
whole-zero construction. The exact boundary at the end of this note
remains part of the record.

## 1. A literal rational parametrization of the source

For fixed a put R=t²+a and use x=R+z, y=√3/2+zw. Substitution into the
original Weierstrass equation, without replacing its variables, gives

`z²+(3(t²+a)-w²)z-3t-√3 w=0`.

On z nonzero set

`A=3t-√3 w-3/z`, `B=3t+√3 w`.

The equation becomes the exact factorization `AB=-3z-9a`. Conversely,

`z=-AB/3-3a`,
`t=(A+B+3/z)/6`,
`w=(B-A-3/z)/(2√3)`,
`x=t²+a+z`, `y=√3/2+zw`.

These maps are inverse on their common nonempty rational open set.
Thus the smooth completed source is rational. In particular its Picard
group has no Picard-zero part or numerical torsion, and relative line
classes on a small parameter disc have the ordinary Cartier meaning.
The maps also retain the actual coordinate a; they do not identify two
different source parameters or forget the marked section.

## 2. The I8 infinity is an explicit product A7 resolution

Near t=infinity use z=1/t, X=z²x, Y=z³y and put R=1+az². Then

`F=R²+z³`, `G=R³+(3/2)z³R+(3/8)z⁶`,
`Y²=X³-3FX+2G`.

Choose S=√F with S(0)=1 and set H=X-S. The equation is

`Y²=H²(3S+H)+2(G-S³)`.

Choose Q=√(3S+H) with Q(0)=√3. The actual local maps

`u=Y-HQ`, `v=Y+HQ`

are invertible: Y=(u+v)/2 and H is the unique holomorphic inverse of
H↦H√(3S+H), whose derivative at the origin is √3. Their equation is

`uv=z⁸ C(a,z)`,

where

`C(a,z) = [48a+8z+96a²z²+72az³+(48a³+9)z⁴] / [32(G+S³)]`.

At each unselected-II parameter a0, a0 is nonzero and
`C(a0,0)=3a0/4` is nonzero. Retain this full unit in the exact map
`v'=v/C(a,z)`. It has inverse v=C(a,z)v', so the equation is exactly
`uv'=z⁸`, over the same a-disc. No marking is changed by dropping a
unit: the unit and its inverse are part of the displayed morphism.

Its simultaneous resolution has the eight charts i=0,...,7

`u=x_i^(i+1) y_i^i`,
`v'=x_i^(7-i) y_i^(8-i)`,
`z=x_i y_i`.

Each is a smooth two-dimensional chart times the unchanged a-disc.
Their overlaps are the ordinary invertible monomial transitions of this
resolution. The seven exceptional curves form the A7 chain and meet the
strict transform to give the I8 fibre. This proves smoothness and
parameter submersion of the complete infinity resolution on the stated
disc, with the actual Weierstrass coordinate map retained.

For the marked section G one has X=R, Y=(√3/2)z³. Since
H=R-S=-z³/(2R)+higher powers, u has order three and v' has order five.
Thus G meets component three in this choice of ordered normal branches.
Reversing the two branches gives component five, with the same
intersection correction 3·5/8. This is an explicit branch reversal,
not an unnamed change of convention.

## 3. The relative Hom line has exactly degree one

Let P_n=[nG], and let T be translation by -G. Its inverse image carries
P_8 to P_9 and O to P_1. For the actual point line M8=O(P_8-O),

`Hom(M8,T* M8)=O(D)`, `D=P_9+O-P_8-P_1`.

Here T* denotes pullback, so the inverse-image signs are fixed by the
displayed translation map. On the generic elliptic fibre the divisor D
is principal: the chord through P_8 and P_1, divided by the vertical
line through P_9, has divisor `-D`. This provides the actual generic
fibre function, not only a numerical equality in a lattice.

The component intersections of D at I8 vanish: P_8 and O meet component
zero, whereas P_9 and P_1 meet component three. All other fibres in this
small disc are irreducible, including the unselected cusp. Consequently
the generic-fibre rational function leaves only a multiple of the whole
fibre in the divisor class of D.

The degree of that multiple can be computed without assuming a height
table. Let C be the positive A7 Cartan matrix. Its inverse satisfies
`(C^-1)_(3,3)=15/8`. The orthogonal projection of a section P away from
O, the fibre, and the nonidentity I8 components has square

`-2-2(P·O)+j(8-j)/8`,

where j is its actual component. To verify this, subtract
`O+(P·O+1)F` from P, and add the vector `C^-1 e_j` of fibre components.
The projected intersection with each component is zero; expanding its
square gives the displayed expression. This projection is additive in
P: the chord divisor for P+Q minus P minus Q plus O is vertical, and
the projection kills exactly those fibre terms. Therefore its square
at nG is n² times its square at G.

The section G is disjoint from O and has component three. Its projected
square is `-2+15/8=-1/8`. The components of P_8 and P_9 are zero and
three, respectively, so

`-2-2(P_8·O)=-64/8`, hence `P_8·O=3`,
`-2-2(P_9·O)+15/8=-81/8`, hence `P_9·O=5`.

Since O²=-1, it follows that `D·O=5-1-3-0=1`. Thus the actual line
O(D) is the pullback of O(1) on the original t-sphere. The generic-fibre
chord divisor together with the full I8 component correction establishes
this line relation; rationality identifies its numerical and Cartier
classes. The computation is unchanged at the unselected-II centre.

In particular, imposing a simple zero at the marked selected fibre gives
a one-dimensional space of Hom sections. On a small source-parameter
disc it is a holomorphic line of sections. Any fixed nonzero evaluation
in the prescribed relative Cartier frames identifies its generator
uniquely; the reference fibre t=0 remains smooth and disjoint from the
selected zero throughout the disc.

## 4. A concrete Miller/chord coefficient and the normalization issue

On the actual generic fibre let ell_8,1 be the line through P_8 and P_1,
normalized to have coefficient one on y, and let v_9=x-x(P_9).
The quotient `f_8,1=ell_8,1/v_9` has fibre divisor `-D`.
On the source it therefore represents the meromorphic Hom coefficient;
its vertical normalization is fixed by the degree-one calculation above.
Multiplying the infinity-zero Hom section by t-t_c gives a section whose
zero divisor is the actual whole selected fibre.

At the unselected cusp the curve is y²=x³. The marked G is in its smooth
additive group, with additive coordinate s=x/y nonzero. The sections
P_8 and P_9 have coordinates 8s and 9s. They are finite, nonzero,
distinct, and the chord through P_8 and P_1 does not collapse: their
x-coordinates are 1/(64s²) and 1/s². Thus the fibre chord construction
has no singularity caused by the unselected cusp. Its Cartier extension
retains the actual horizontal divisors and the full infinity charts
from section 2.

The exact source normalization used by the supplied OS45 construction
still has to be matched to this coefficient. The unique-section argument
reduces this comparison to a single nonzero scalar evaluation in the
original prescribed line/reference frames. A complete check must verify
that the actual normalization evaluation extends as a nonzero unit at
the unselected-II centre. An arbitrary punctured-disc scalar factor could
have winding, so that factor cannot be ignored. No proof gate is closed
before this exact coefficient comparison is made.

## 5. The selected toric and ordinary cap maps to be compared

The selected fibre remains a simple node. Relative holomorphic Morse
coordinates give its original height q=t-t_c and a full equation
`z_+ z_-=q times a nonzero unit`; the unit is retained with its explicit
inverse. The marked ordering is the one given by
`c=v/(2u)` and `Z=(S-c)/(S+c)` in the initial derivation.

In the relative Tate chart write Q(q,a)=q times its full nonzero unit and
P(q,a) for the full coordinate of G, with P(0,a)=P_G. The actual theta
ratio for O(8G-O) supplies a line-frame map with its full coefficient.
Its period and suspension maps have the form

`h:(Z,V) -> (Q Z, alpha V)`,
`B:(Z,V) -> (g Z, lambda q beta V)`,

where alpha,g,beta are the full analytic factors from that actual
Cartier/translation calculation. Each remains part of every map and
inverse; it is not replaced by its central value. A prescribed unimodular
fan uses integral monomials in these factors. Their products and inverses
extend on the disc exactly when the original normalized coefficient in
section 4 does. The chart exponent matrices are fixed, so these are the
same full character gluings as on the punctured disc.

The ordinary order-one cap stays on a protected smooth fibre. Its full
period, point-line and scalar factors are nonzero holomorphic functions
on a simply connected small disc and therefore have holomorphic
logarithms extending the specified reference branch. The integral period
and annular cochain are retained. The order-one source and line maps,
with their actual inverses, then extend coefficient by coefficient.

## 6. Properness, topology and return

On the source exterior away from a fixed small selected-node collar the
normalized Hom section is nonzero. Compactness of the smooth resolved
source family supplies uniform upper and lower bounds on the full line
maps over a closed parameter disc. A common scalar with operator norm
strictly below one gives a compact fundamental shell for the free line
quotient there. The fixed fan has finitely many cones modulo its retained
period lattice. Its full monomial maps and their inverse unit factors
give a common finite collection of closed chart boxes for the selected
attachment. The protected ordinary cap has its analogous compact shell.
These shells and chart boxes cover every fibre and have compact union
over the closed parameter disc, giving properness of the completed
family. Smoothness and submersion are checked in the source, resolved
infinity, selected unimodular charts and cap charts individually.

The original boundary family is identified using the same source,
Cartier line, full scalar coefficient, fan characters and cap reference.
After the exact normalization comparison in section 4, these are literal
coefficient maps and inverses. The previously saved disc and constant-
argument scalar-annulus arguments then give an equivariant horizontal
isotopy from each unselected-II return to the identity, preserving the
specified positive parameter and endpoint markings.

## Remaining prereading boundary

The full explicit infinity resolution, rational source map, degree-one
Hom calculation and generic-fibre coefficient have now been derived.
The original actual normalization evaluation and the detailed original
theta/cap coefficient maps remain to be compared. The broad statement
that they are some units is insufficient: their actual unit, inverse and
no-winding extension must be checked. This note records that remaining
obligation rather than retrospectively asserting it was rederived.

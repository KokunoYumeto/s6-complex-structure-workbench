# The reduced-III cap for the primitive OS43 translation

Status: complete construction and low-degree integral topology proof
submitted for audit. No new manuscript theorem ID or return index is
assigned in this working note. It treats the first unresolved source
pair in P3K.21, namely (a,b)=(2,1) on III*+3I1. The source, line,
affine norm, and marked cap maps are retained explicitly.

## 1. The source and its actual reduced root

Take the minimal regular model of

    y^2=x^3+t x+1,        G=(0,1).

It has III* at infinity and three I1 fibres at the distinct roots of
4t^3+27. The section G is the primitive Mordell--Weil generator of
height 1/2, is disjoint from O, and meets the nonidentity III*
component with local contribution 3/2, as in P3F.1--2.
Put M=O(2G-O), Q=G. The line point 2G lies in the identity component,
and M has degree zero on every component of III*. Its actual Hom
line for the suspension translation is the pullback of O(1), since
2*1/(1/h(G))=1. Choose the section with its one simple whole-fibre
zero at one of the I1 fibres. The resulting line map B0 covers
t_{-G}, is invertible at the III* value, and is multiplied by the
small scalar lambda. This is the same Hom-direction convention as
P3K.22.

Near infinity use q=1/t, x0=q^2 x, y0=q^3 y. The exact equation and
section are

    y0^2=x0^3+q^3 x0+q^6,       G=(0,q^3).

For m=4l+3, l>=0, set k=3l+2 and make the actual substitution

    q=z^m,       x0=z^(2k) X,       y0=z^(3k) Y.

The minimal equation is

    Y^2=X^3+zX+z^(6(l+1)),      G'=(0,z^(3(l+1))).       (III.1)

Its discriminant has order three, and its only surface singularity
over z=0 is the ordinary double point with quadratic part Y^2-zX.
Resolving that point gives a smooth source with a reduced III fibre.
The exact deck map is

    D(X,Y,z)=(zeta_m^(-2k)X,zeta_m^(-3k)Y,zeta_m z).      (III.2)

It fixes the sections G',2G',O and extends over the resolved charts.
For m=3 the X-blowup chart Y=Xv,z=Xw has equation

    v^2=X+w+X^4w^6.

It is smooth, with exceptional component X=0, w=v^2, and the other
central component w=0, X=v^2. They meet with tangency order two.
The deck acts by (X,v,w)->(zeta_3^2 X,zeta_3 v,zeta_3^2 w), fixing
both component labels. For every m=4l+3 the same blowup formula,
with the corresponding higher monomial, proves smoothness and the
same reduced component configuration. Its labels are fixed by D.
The section G' has nonzero component in Z/2, while 2G' has component
zero. This also follows by composing (III.1) with its order-four
good root and using the marked nonzero fixed two-torsion limit.

## 2. The exact affine source norm

Multiplication by the odd integer m on the central Neron smooth
group is a bijection: its identity component is the additive group,
where the derivative is m, and its component group is Z/2.
The analytic inverse-function theorem therefore gives a unique
local section R with

    mR=G'

and the required central point. The deck fixes it: D(R) has the
same m-multiple and the same central point, so uniqueness gives
D(R)=R. Translation by R extends to the whole minimal smooth
elliptic source, by the resolved addition map and canonical-form
graph comparison of P3K.22. Thus the actual source automorphism

    a0=t_{-R} D

satisfies a0^m=t_{-G'}. It exchanges the two III components, since
R has the nonzero component and m is odd.

## 3. A holomorphic line lift with its full norm

Let N=O(2G'-O) on the root source. This is the actual pullback line
after relative minimalization. One way to retain the comparison is
to pull M to the resolved fibre product first. It has degree zero
on each curve contracted in relative minimalization. The blowup
Picard decomposition then descends the line through each actual
(-1)-contraction. Its comparison with O(2G'-O) differs by a whole
fibre, a principal divisor on this disc. The descended deck lift
has D^m=1 and commutes with the pullback B0. Any base character of
that line comparison is retained in this descended lift.

There is an invertible holomorphic line map L covering t_{-R}.
For an explicit meromorphic construction, put P=2G'. The chord
through P and -R divided by the vertical function through P-R has
fibre divisor

    P+(-R)-(P-R)-O.

It is the actual fibre divisor of Hom(t_R^*N,N). Its remaining
vertical divisor has degree zero on both III components, because
N has degree zero and translation permutes those components.
The intersection matrix is [[-2,2],[2,-2]], with integral kernel
Z(1,1). The remaining divisor is therefore an integer multiple of
the full reduced fibre, and multiplication by the corresponding
power of z makes the map holomorphic and invertible. This is an
actual line map, with the usual tangent formulas used at coincident
chord points.

The deck acts on the rank-one free module of such Hom sections.
Choose the character chi of its action on the central fibre. The
finite weighted average

    L_eig=(1/m) sum_(j=0)^(m-1) chi^(-j) D^j L D^(-j)

is nonzero at the central fibre and hence is an invertible line map
after shrinking. It satisfies D L_eig D^(-1)=chi L_eig exactly.
Both L_eig^m and B0 cover t_{-G'} and are D-invariant, so their
ratio is a nonvanishing holomorphic function u(q) on the base.
Here compact connected source fibres make every scalar ratio a
base function; D-invariance makes it a function of q=z^m.

The power of L_eig D is

    (L_eig D)^m=chi^(m(m-1)/2) u(q) B0.

Choose the holomorphic m-th root of the reciprocal of this base
unit on the disc and multiply L_eig D by it. This produces an
actual line map A0, covering a0, with

    A0^m=B0,        A0 B0=B0 A0.                         (III.3)

The second identity follows from the first. In this odd-m case the
displayed character factor is already one, but it has not been
discarded from the derivation. Taking lambda=r^m and setting

    A_r=r A0,       B_lambda=lambda B0

gives A_r^m=B_lambda. On a compact smaller root-source tube, A0
and its inverse have bounded norm ratios. For sufficiently small
|r|, A_r is strictly contracting. The actual cap is

    N^times/<A_r> = N^times/<A_r,B_lambda>.

It is smooth and proper over q, by its compact norm-shell
fundamental region. The delta circle is free on it: an equality
e^(i theta)v=A_r^j v forces j=0 by strict norm contraction, and
then e^(i theta)=1. This includes the tangent point and both III
components. No finite zero-gamma kernel is present.

### The annular comparison and the exact meridian convention

Use logarithmic norm increasing outward. The compatible interval
reparametrization of P3K.15 makes the actual cap identification

    (p,z,u) -> (a0(p),zeta_m z,u-1).

Thus a positive suspension loop h is represented on the covering by
A_r^(-1), rather than A_r. The ordinary positive gamma loop is
B_lambda^(-1)=A_r^(-m), and consequently gamma maps to m h.

Cut the punctured q-disc along its positive meridian and choose the
root z on that cut. Specify the affine gluing so that its positive
crossing is the single actual map A_r, with no additional iterate
of B_lambda. On the base this is the positive root crossing
z->zeta_m z. On the compatible norm coordinate it decreases u by
one. This fixes the marked lift of the ordinary positive q meridian
to have image -h. In angular variables the marking is exactly

    arg(z)/(2pi)=arg(q)/(2pi m),
    u_cap=m u_ordinary-arg(q)/(2pi),

with the source translation and bounded line multiplier supplied by
the actual A_r, not omitted from the chart. The two primitive loops
therefore map as q->-h, gamma->m h, and the killed primitive
meridian is exactly m q+gamma.

Here is also a holomorphic realization of this marked annular
comparison, including its permitted source translation. The regular
torus family has an origin after choosing a nonzero frame over the
zero section; on the annulus it is the quotient of its holomorphic
Lie bundle by its integral period local system. On a simply connected
sector the degree-zero line has the explicit constant-factor model

    (z,v)~(z+1,v),     (z,v)~(z+tau,exp(2pi i beta)v).

Multiplication (z,v)*(z',v')=(z+z',vv') defines its actual
commutative extension group. A holomorphic line map covering a
translation lifts to (z,v)->(z+r,a(z)v); compatibility makes a
doubly periodic and holomorphic, hence constant. Thus the line
lifts used here are translations in this explicit group model.
The cap's affine
root descent is a torsor for this same family: on a simply connected
root chart the two presentations differ by translation, and (III.3)
is exactly its cyclic cocycle relation. To construct a translation
isomorphism, lift that cocycle to holomorphic Lie-bundle cochains.
Their coboundary is an integral period two-cocycle. It is a
coboundary because the annulus retracts onto a circle. Subtract a
period one-cochain to make the Lie-bundle cocycle closed; solve it
by holomorphic zero-cochains, since a holomorphic vector bundle on
the Stein annulus has H1=0. Translations by those zero-cochains are
the mutually inverse holomorphic maps on every overlap.

The same exact sequence makes the component map from holomorphic
torus sections onto H1 of the period local system surjective. Its
gamma coefficient is primitive: the integral period lattice has
the invariant quotient psi sending gamma to one and the elliptic
and delta periods to zero. Thus its gamma class is primitive in
the coinvariants; the boundary presentation below also verifies
this after the delta quotient. Consequently one may, and here does, choose
the zero-cochains in the component whose positive cut crossing is
A_r itself. Any extra B_lambda^j crossing is removed by the section
with gamma winding j. This retains the specified single crossing
and supplies the holomorphic gluing to the unchanged ordinary
family. Source-period and delta phases are kept in the constructed
translation maps; they do not change the two displayed H1 images.

## 4. The source-complement lattice

Let S be the original rational elliptic surface and let N_* be a
small III* tube. Its eight components have the affine E7 matrix.
Use the integral source divisor basis

    O,F,C_0,...,C_6,G,

where the seven nonidentity curves form minus the E7 Cartan matrix
with edges (0,1),(1,2),(2,3),(3,4),(4,5),(2,6). The generator meets
C_5. The inverse Cartan column is

    R1=(1,2,3,5/2,2,3/2,3/2)^t,

whose last indicated diagonal is 3/2. The Gram matrix has determinant
-1: O^2=G^2=-1, OF=GF=1, and GC_j=delta_(j,5).
These ten divisors are therefore an integral basis of H2(S;Z).
The full III* component lattice, spanned by F and the seven C_j,
is primitive.

Write V=S minus the interior of N_*. Excision, the unimodular
source intersection pairing, and the primitive fibre lattice give

    H1(V)=H3(V)=0,
    H2(V)=ZF direct-sum ZM,

where M denotes the divisor class P_(2G)-O, not twice the divisor G.
Indeed orthogonality to F forces equal and opposite O,G coefficients;
orthogonality to the root block then makes the G coefficient even.
Its first possibility is precisely

    M=2G-2O-F+2R1.                                    (III.4)

The actual suspension is T=t_{-G}. Its source action is

    T F=F,         T M=M-F.                           (III.5)

For fundamental groups, the three nodal fibres outside III* kill
the whole elliptic lattice. If their primitive vanishing cycles
generated a sublattice of index d>1, every pairwise determinant
would be divisible by d. The trace of the product of their three
Picard--Lefschetz transvections is congruent to 2 modulo d^2:
the quadratic terms are pairwise determinant squares and the cubic
term their product. But this product is inverse to the III*
monodromy, of trace zero. Thus d^2 divides 2, forcing d=1.
The section and the disc base then give pi1(V)=0 by van Kampen.

The actual circle orbit of the exterior is the mapping torus of
T on V. The norm-shell identification is the one of P3K.22. At the
selected whole-zero I1 it uses the exact nodal source translation
and the orbit-product charts of P3F.9, so that this mapping-torus
description includes the actual cusp orbit piece. Write it W_V.
The Wang sequence and (III.5) give

    pi1(W_V)=Z gamma,
    H2(W_V)=Z[M],       H3(W_V)=Z[F],
    H1(W_V)=Z,         H4(W_V)=0.                       (III.6)

The compact H2-by-H3 pairing is zero. The H3 generator is the
actual trace of a regular source fibre F, and its intersection
with M in a source slice is F.M=0.

## 5. The primitive boundary classes and all needed gluing maps

Let L=boundary(N_*) and E=boundary(W_V). The source boundary has

    H1(L)=Z q direct-sum Z/2 eta,       H2(L)=ZF.

Here q is the zero-section meridian. Translation sends q to q-eta
and fixes eta. The nonzero class eta is determined by the marked
component of G: in the fibre intersection exact sequence its class
is the nonintegral E7 inverse-Cartan column R1 modulo the root lattice.
Thus it has exact order two. This gives the full integral translation
action on H1(L), not just its rational action.

An equivalent boundary torus-bundle marking is

    J=[[0,1,-1],[-1,0,0],[0,0,1]]

on (alpha,beta,gamma) over q. Its elliptic block is the order-four
III* matrix, and the last column represents the nonzero component
cocycle. Both J-I and wedge^2 J-I have Smith form (1,1,0).
The invariant vector is (-1,1,2), and the primitive coinvariant
functional on (alpha beta,alpha gamma,beta gamma) is (2,-1,-1).
In particular, with a positive primitive boundary class z1,

    H1(E)=Zq direct-sum Zgamma,
    H2(E)=Zz1 direct-sum Zz2,         F=2z1.             (III.7)

The last equality can also be read from the source-boundary Wang
sequence: its quotient by ZF is Z direct-sum Z/2. The five-dimensional
Poincare--Lefschetz sequence of W_V and the zero middle pairing in
(III.6) show that H2(E)->H2(W_V) is onto with primitive rank-one
kernel. Since F maps to zero by (III.5), this kernel is exactly Zz1.
Thus z2 maps to a unit multiple of M.

The signed relative Wang chain fixes that unit. Let D_O be the
punctured zero section in V, with boundary q. Choose a boundary
two-chain C with boundary 2(Tq-q). The integral cycle

    Z=2(TD_O-D_O)-C

represents the image of the Wang class over 2q. Changing C adds
a multiple of F, zero in H2(W_V). Closing the section discs and
using the source identity gives

    2(P_(-G)-O)=-M+3F-2R1.

Modulo the removed fibre lattice this makes the second boundary
column exactly -M. This is the actual source translation sign.

The cap circle orbit W_U is the mapping torus of a0 on its reduced
III source tube. That tube retracts to its central two-sphere union;
the two spheres meet at a single point and a0 exchanges them.
Consequently

    pi1(W_U)=Zh,
    H2(W_U)=ZC,      H3(W_U)=Z(C0+C1).

The incoming elliptic fibre is C0+C1, which maps to 2C in H2(W_U).
Equation (III.7) therefore gives z1 -> C with coefficient one.
Write the image of the signed z2 as kappa C. Subtracting kappa z1
is an explicit integral determinant-one boundary basis change; it
does not change its exterior image -M. In this boundary basis the
degree-two Mayer--Vietoris matrix is

    D2=[[0,-1],[-1,0]],                               (III.8)

up to reversing one chosen generator. It is unimodular. Before that
displayed basis change its lower-right entry is -kappa, with the
same determinant. No cap-meridian coefficient is changed by this
homology basis operation.

The actual cyclic norm fixes the first-homology inclusion. In the
single-A_r cut convention proved in Section 3, the meridian is
mu=mq+gamma, and the inclusion is

    q -> -h,       gamma -> m h

on the cap, while the exterior sends q to zero and gamma to gamma.
The full degree-one gluing matrix is therefore

    D1=[[0,1],[1,-m]],                                (III.9)

with determinant -1. Both cap and exterior fundamental groups are
the displayed cyclic groups, and elliptic boundary loops die in
both. Van Kampen consequently gives pi1(Y)=1 for the actual closed
circle orbit. Equations (III.8)--(III.9) give H1(Y)=H2(Y)=0.
Poincare duality on the closed oriented five-manifold supplies all
remaining sphere homology groups. Thus Y is the standard S5 by the
same five-dimensional classification already used in P3K.22.

The only delta fixed set is the index-one cusp sphere, with its
actual O(-1)^2 chart and meridian Euler number one. The integral
Gysin and Hopf-filling Mayer--Vietoris maps of P3K.22 now give
pi1(X)=0 and H*(X;Z)=H*(S6;Z). The established Theta6=0 comparison
identifies the resulting compact complex threefold with S6.

## 6. Scope still requiring an actual page/return comparison

The holomorphic parameter closing keeps the actual scalar root.
On the logarithm cover write c=log(lambda)/(2pi i), so the cap lift
is exp(2pi i c/m)A0. Under c->c+m the gamma period changes by
m delta, and its chosen cap root changes by the integral delta
period. The logarithmic annular comparison therefore changes by
(log q)/(2pi i) delta, with q=1/t at the cap. This is the actual
scalar change; R, D, and their source maps remain unchanged.
Here the comparison can be chosen with this dependence explicitly:
first solve its Lie-bundle cochain equation at one fixed c_0, and
then add ((c-c_0)/m)(log q)/(2pi i) delta to that solution.
The root cut cocycle changes by (c-c_0)delta/m, while the deck
linear part fixes delta, so the added term solves exactly the
changed cochain equation. All other source and line-unit terms are
the fixed ones at c_0. Its change under c->c+m is therefore the
displayed logarithmic delta translation, not a choice of an
uncontrolled parameter-dependent annular trivialization.
Let t_c be the selected scalar-zero I1 value. The closing ordinary
map from c+m back to c multiplies the line by h(t)=t-t_c.
Its positive deck multiplies by h^(-1), which near the finite cap
is q/(1-t_c q). The q factor cancels the displayed change of
annular comparison, and the remaining holomorphic unit extends
over the entire reduced III cap and its line. At the selected
cusp h=t-t_c is its base parameter. Modulo the actual period B,
its multiplication is translation by the source section G and
an invertible scalar unit, both extending in the nodal source
and Mumford charts. At the other fillings h is already a unit.
These actual maps and their inverses agree on all the annular
overlaps. They descend the construction to
r=exp(2pi i c/m), with lambda=r^m. Compact norm shells and the
proper local fillings give properness over every compact annulus
of the punctured r-disc.

The construction and topology above use one III* cap with m=4l+3
and primitive gamma coefficient +1, and no other logarithmic sites.
Their actual holomorphic parameter is lambda=r^m. The whole-zero
I1, line M, component markings, delta character and norm are all
specified. Additional cap sites and primitive b>1 choices are not
identified with these data.

The sectioned degree-m source pullback has a III fibre and 3m nodal
fibres, hence chi=l+1. Its pulled-back line point 2G has height 2m
and lies in the identity component, giving P.O=m-(l+1)=3l+2.
These are exact sectioned-pullback values. A return index will be
assigned only after the actual regular-binding page and its line
are compared with this pullback through the affine cap. In
particular this note does not silently replace that torsor by a
sectioned surface.

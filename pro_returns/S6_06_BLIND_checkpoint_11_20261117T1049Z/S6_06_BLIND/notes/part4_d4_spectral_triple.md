# A triple spectral root with nonzero cubic tensor

Current status: **Proved, P4R.19**. Independent audits by root and checks
both passed the complete argument. The initial status below is retained
as the record of the first written proof. The executed exact certificate
is `code/part4/d4_spectral_triple.py`, with `.json` and `.out` output.

Status: proof complete, independent audit requested. Written 2026-11-17
06:02 UTC. This note treats a smooth local critical-curve branch with
generic transverse type D4. Other critical-curve branches at the point
are retained without a transverse-type restriction.

## Precise local assertion

Let f be the actual reduced local equation in a smooth threefold, and let
C0 be a smooth local branch of its critical curve, with generic transverse
ordinary triple point. Suppose the rational intersection form of every
local Milnor fibre of f is zero, as proved in P4.51 for the remaining
global ruled case. The cubic normal tensor of f along C0, when nonzero
at a point, cannot be the cube of one linear form there.

Thus a collision of all three spectral directions over a smooth branch
point forces the entire cubic normal tensor to vanish. The conclusion
does not exclude a collision of only two spectral directions.

## 1. An actual equation and its weighted leading polynomial

Choose coordinates (x,y,z) in which C0=(x=y=0). Generic normal
multiplicity three gives f in (x,y)^(3). The ideal (x,y) is a smooth
complete intersection, and its powers are primary, so this is the
ordinary containment f in (x,y)^3 at the point in question.

Suppose that the nonzero cubic normal tensor is a cube. A linear normal
coordinate change makes it x^3, up to a nonzero scalar. Weierstrass
preparation in x gives the exact equality

    f=U(x,y,z)[x^3+a2(y,z)x^2+a1(y,z)x+a0(y,z)],

where U is a holomorphic unit. The bracket still belongs to (x,y)^3.
Consequently a2 is divisible by y, a1 by y^2, and a0 by y^3. The
holomorphic coordinate change that depresses this monic cubic preserves
(x,y), and gives

    f=U(x,y,z)[x^3+y^2 B(y,z)x+y^3 C(y,z)],                 (ST.1)

with B(0,0)=C(0,0)=0. The unit is retained; no identification of the
nonzero fibres after multiplying by a nonconstant unit is being assumed.

Put

    k=ord_z B(0,z),       l=ord_z C(0,z),
    rho=min(k/2,l/3),

where an identically zero series has order infinity. At least one order
is finite: otherwise every generic normal cubic would be x^3, contrary
to generic D4. Thus rho is positive and finite.

Choose an integer L>3 rho and use positive rational weights

    wt(x)=L+rho,        wt(y)=L,        wt(z)=1.

Multiplying all weights by their common denominator gives positive
integer weights. Every coefficient term containing y has weight at
least L and hence lies strictly above the first face. Formula (ST.1)
has the following weighted leading polynomial, times U(0):

1. If k/2<l/3, then

       P=x(x^2+a y^2 z^k),          a nonzero.

2. If l/3<k/2, then

       P=x^3+b y^3 z^l,            b nonzero.

3. If k/2=l/3, then k=2r and l=3r for an integer r>=1, and

       P=Q(x,y z^r),
       Q(X,V)=X^3+a X V^2+b V^3,  a,b nonzero.

In the third case Q is not a cube: a cube of a linear form whose X^2 V
coefficient is zero and whose X^3 coefficient is one has a=b=0. Q may
have a double linear factor; that possibility is kept below.

## 2. A compact class of square minus two

Let B be a connected smooth complex curve, and let h:B->C be holomorphic
with two distinct simple zeros p and q. Suppose that a smooth embedded
arc gamma joins p to q and its interior contains no zero of h. Such an
arc exists whenever p and q lie in the same component and the zero set
is discrete. Consider the smooth surface

    Z_h={(b,u,v) in B times C^2 : uv=h(b)}.

It is smooth at the two relevant singular-fibre points because dh is
nonzero there. On the inverse image of gamma take

    |u|=|v|,       uv=h(b).

This is a circle over the interior and the circle collapses at each
endpoint. It is a smoothly embedded sphere: near an endpoint choose the
arc so that h is a fixed nonzero complex multiple of a positive real
parameter s, and write u=s^(1/2)e^(i phi),
v=constant times s^(1/2)e^(-i phi). These are the smooth polar
coordinates of a real disc in the local uv chart.

For the product Kahler form the sphere is Lagrangian. Indeed, along the
arc write u=R exp(i phi), v=R exp(i(psi-phi)). The sum of the two fibre
area forms restricts to d(R^2/2) wedge d psi, which is zero because R
and psi depend only on the arc parameter. The base area form also
restricts to zero. A Lagrangian oriented sphere in a complex surface has
self-intersection -2: multiplication by i identifies its tangent and
normal real bundles, and the complex ambient orientation gives the
normal bundle the opposite orientation to that identification, so its
normal Euler number is -chi(S^2).

Let alpha be its compactly supported Poincare-dual class. Then

    integral_Z_h alpha^2=-2.                                 (ST.2)

Only a compact tubular neighbourhood of this sphere is used.

If pi:W->Z_h is a finite proper holomorphic map of positive degree d
between smooth complex surfaces, pi^*alpha is compactly supported and

    integral_W (pi^*alpha)^2 = d integral_Z_h alpha^2=-2d.     (ST.3)

The map has degree d on the complement of its analytic branch locus,
which has measure zero; integration of compactly supported top forms
gives the equality. Equivalently, one can use its proper oriented
topological degree. By Poincare duality the pulled-back compact class
is a compact homology two-class, with the displayed nonzero square.
No claim that its representative is an embedded sphere is needed.

## 3. The three exact finite maps

For the first leading polynomial, P=1 forces x nonzero and gives

    y^2 z^k=h(x),       h(x)=(1-x^3)/(a x),       x in C*.

The map

    (x,y,z) -> (x,u=y^2,v=z^k)

is finite, proper, and of degree 2k onto

    Z_h={x in C*, uv=h(x)}.

The target is smooth: at u=v=0 the three zeros of h are simple, and
elsewhere a derivative with respect to u or v is nonzero. The source
is smooth by the weighted Euler identity on P=1. A path in C* joining
two of the three cube roots of one, avoiding the third, supplies the
sphere of Section 2. Its compact dual pulls back to square -4k.

For the second polynomial the exact finite proper map is

    {x^3+b y^3 z^l=1} -> {uv=(1-x^3)/b},
    (x,y,z) -> (x,u=y^3,v=z^l),

of degree 3l. The base is now C. Again there are three simple zeros,
and the pulled-back compact class has square -6l.

For the balanced case put

    B_Q={(X,V) in C^2: Q(X,V)=1}.

This is smooth by the ordinary Euler identity. It is connected even
when Q has a double factor. Indeed its projection to
P^1 minus the distinct zero directions of Q is an unramified cyclic
cover of degree three. Around a zero direction of multiplicity one or
two, monodromy is a generator of Z/3. Such a direction exists because
Q is not a cube. Hence the covering and B_Q are connected.

The function h=V on B_Q has precisely the three zeros (X,V)=(zeta,0),
zeta^3=1. They are simple, since Q_X(zeta,0)=3 zeta^2 is nonzero.
The surface

    Z_Q={(b,u,w): b in B_Q, uw=V(b)}

is smooth. The exact map from the leading fibre is

    {Q(x,y z^r)=1} -> Z_Q,
    (x,y,z) -> (b=(x,y z^r),u=y,w=z^r).                     (ST.4)

It is finite proper of degree r: z satisfies the monic equation
z^r=w, and all other coordinates are retained. Join two of the three
V-zeros by an arc in B_Q, avoiding the third. Equations (ST.2)--(ST.3)
give a compact two-class of square -2r on the source. This proof also
handles Q=(X-alpha V)^2(X+2 alpha V), alpha nonzero. It does not replace
that repeated-factor cubic by a nearby reduced one.

## 4. Transport into the actual local fibre

Let integer weights (w_x,w_y,w_z) and weighted degree d be obtained
from Section 1, and set

    D_epsilon(x,y,z)=(epsilon^w_x x,epsilon^w_y y,
                      epsilon^w_z z).

The actual functions

    G_epsilon=epsilon^(-d) f(D_epsilon(x,y,z))

converge with derivatives on compact sets to U(0)P. The weighted
Euler identity makes dP nonzero everywhere on P=1, including when P
has a repeated factor on its zero set. Choose compact representatives
of the two-class constructed above and a small transverse perturbation
used to compute its square. A compact neighbourhood of those chains
in P=1 admits the same gradient-flow comparison as P4.52:

    dG_epsilon(V_epsilon)=-partial_epsilon G_epsilon.

The denominator is bounded away from zero on a slightly larger compact
neighbourhood; a cutoff gives a flow for sufficiently small positive
epsilon. It sends the compact chains and their transverse intersection
points into G_epsilon=U(0). Scaling by D_epsilon embeds them inside the
original fixed Milnor ball on

    f=U(0) epsilon^d.

The transport preserves the oriented intersection number. It is one of
-4k, -6l, or -2r, and is nonzero. This contradicts P4.51. The asserted
triple-root exclusion follows.

## 5. The necessary two-root exception

The scope cannot be enlarged to every spectral collision. The explicit
reduced equation

    f=y(x^2+y^2 z^2)

has generic D4 along x=y=0 and generic A1 along x=z=0. At their
intersection only two spectral directions collide. Its non-plane
normalization sheets x=+i yz and x=-i yz have pole divisor
2(y=0)+(z=0), which is SNC. Nevertheless its affine fibre f=1 is
exactly (C*)^2 through

    a=x+i yz,        b=x-i yz,
    x=(a+b)/2,      y=(ab)^(-1),
    z=(a-b)ab/(2i).

These maps are inverse holomorphic maps, and substitution gives f=1.
The intersection form on (C*)^2 is zero: its generator is the product
of two unit circles and a radial translation makes a disjoint homologous
copy. This model therefore remains in the global incidence analysis.

The same exact calculation generalizes to y(x^2+y^2 z^n): after putting
t=1/y and u=x/y its fibre is u^2+z^n=t^3 with t nonzero. It is a smooth
bundle over C*, with radial dilation identifying its positive-radius
direction with a product. Compact two-cycles can be translated in that
direction, so their intersection pairing is zero. No restriction to a
small list of transverse types on the other component is being imposed.

# Fixed-source cap-data loops: global translation comparison

Working proof for independent audit. This note concerns the whole-zero
selected I1 sector of K35, with a fixed marked rational elliptic source,
fixed source line, fixed translation Q=bG, fixed finite-root orders and
norm integers, and a fixed periodic index-one fan. The scalar is first
held fixed. A parameter family includes its actual annular maps; they
are never replaced merely because its individual fibres are conjugate.
The component-supported OS49 cusp requires a separate local lifting
check and is not covered by the selected-I1 argument below.

## CP.1. The exact local group and its Lie sheaf

Let B be the orbifold P1 with the actual cap orders. Its selected I1
point is ordinary. Let A be the sheaf of fibrewise translations of the
compactified suspension that extend on its actual root and cusp charts.
All linear lattice maps are fixed. The physical delta field gives an
exact sequence of orbifold holomorphic vector bundles

\[
 0\longrightarrow\mathcal O_B\delta\longrightarrow V
       \longrightarrow L\longrightarrow0.                 \tag{CP.1}
\]

The quotient is the source translation Lie line. Here is the exact
coarse extension, including the changed additive root model. In the
minimal Weierstrass substitution

\[
 q=z^m,\qquad x=z^{2k}X,\quad y=z^{3k}Y,
\]

the source relative differential is z^{-k}dX/(2Y). Its dual source
translation vector therefore maps to z^k times the root translation
vector. The latter has deck character zeta_m^k. An invariant holomorphic
section has the form z^k h(q) times that root vector, because 0<=k<m.
It is thus exactly an original source Lie section, not a different
coarse line. The allowed k values are floor(3m/4), floor(2m/3),
floor(m/4), floor(m/3), floor(m/6), and k=1 for the quadratic I1-star
root. These are respectively the III-star, IV-star, III, IV, II, and
I1-star substitutions already proved in F41--F49. Every one has
0<=k<m. The root character and this equality are retained under the
actual line diagrams and coefficient-generic maps of F51.

On the selected I1 the source vector is the logarithmic Tate vector,
which extends as the relative dualizing vector through the actual
toric charts. The quotient line in (CP.1) has the original coarse
extension O(-1), since the source is rational with chi(O)=1. The
physical delta line has coarse extension O. Taking finite invariants
is exact over C. Hence the coarse direct image of V is an extension
of O(-1) by O, and the elementary two-chart Laurent calculation gives

\[
                       H^1(B,V)=0.                         \tag{CP.2}
\]

At a reduced retained/root fibre the source component group can be
removed from a translation lift by a suspension power: the actual
source translation Q acts transitively on those components, by the
already proved sphere restriction K15. The remaining central point
lies in the additive or multiplicative identity group and has a local
logarithm. On a good root ordinary elliptic local logarithms apply.
At the selected I1 cusp the index-one component lattice gives the
unique integral toric reindexing making an extending translation
preserve the chosen component; the remaining two torus multipliers
are holomorphic units. Their logarithms give the local Lie lift.
This is the actual local argument of P5.5, which uses the toric cover
and its deck lattice, not a claim based on the dimension of an
automorphism group. In particular

\[
 0\longrightarrow H\longrightarrow V\xrightarrow{\exp}A
       \longrightarrow0                                   \tag{CP.3}
\]

is exact, where H is the extending integral period sheaf. The root
group actions are retained in this statement.

## CP.2. Parametric conjugacies and the discrete torsor class

Work first over a small simply connected parameter disc. F44 and F49
give actual local source conjugations, with the line lifts and their
transported annular maps. Their constructions are analytic in that
parameter after shrinking: a central isogeny has a local inverse at
each chosen inverse image; the multiplicative square root has a local
analytic branch; the residual zero-central logarithm is solved by the
displayed finite averaging sum. The residual line unit has its
central finite character retained and its zero-central logarithm
solved by the same sum. The component choices and this finite
character are locally constant. No choice has yet been made around
the entire parameter circle.

At the cusp the scalar and the source line are fixed, so the same
toric translation model is used. Comparing all these local models
with one fixed member gives a Cech cocycle in A on the actual
orbifold cover. Its image under (CP.3) is a lattice-valued two-cocycle.
The local logarithms can be chosen continuously on the parameter
disc, and a lattice-valued continuous function is locally constant.
Subtract its value at the reference parameter. After the corresponding
integral Cech adjustment, the remaining transitions are a V-valued
one-cocycle. Equation (CP.2) supplies a zero-cochain solving it.

This solution can be taken analytic in the parameter. On the two
standard source-base charts, the solution is the Cauchy/Laurent
splitting of the negative and nonnegative powers for O and O(-1);
finite averaging gives its orbifold version. The integrals are over
fixed compact circles, so holomorphic parameter dependence is
preserved. A splitting of the vector extension in (CP.1) also exists,
since its extension group has coarse H1(O(1))=0; the same Laurent
calculation constructs it. Exponentiating the resulting sections
gives the actual global family isomorphism. On every local chart it
is the specified extending translation, so it transports the
annular, finite-character, line, and cusp maps literally.

Consequently a fixed-scalar cap-data family is locally isomorphic to
the fixed compactified suspension by translations. Continuing these
actual isomorphisms around a parameter interval leaves a global
extending translation at the endpoint. The finite kernel of 1-D
has not been discarded: it is included in that endpoint. The next
step computes this global endpoint group.

## CP.3. Lifting an endpoint away from the selected I1

Put U=P1 minus the selected I1. On the ordinary source, before
dividing by the suspension generator B_lambda, translations are
invertible line maps covering source translations. On a root disc an
extending compactified translation has such a lift after composing
by a power of B_lambda to place its source point in the identity
component. The explicit section logarithm then lifts it through the
actual source line. Any two such lifts differ by a power of B_lambda.

The lift can be made exactly equivariant under the finite root group.
Indeed its conjugate under A_i differs by B_lambda^{j_i}, with j_i
an integer constant on the connected root disc. Iterating m_i times
gives B_lambda^{m_i j_i}; but A_i^{m_i}=B_lambda^{n_i}, and source
translation lifts on a degree-zero line commute with B_lambda.
Thus B_lambda^{m_i j_i}=1. Strict contraction on the covering line
forces j_i=0. This retains the actual affine norm relation and proves
equivariance, rather than replacing A_i by its linear part.

The overlaps of the lifts are now an ordinary integral one-cocycle
on U with its finite orbifold points. This group is zero. Explicitly
the orbifold fundamental group is the free product of the finite
cyclic cap groups, and every homomorphism from it to Z is zero.
Changing the local lifts by the resulting integer powers of
B_lambda therefore patches them to a single lift on U. Finite root
equivariance descends its source point to an original source section;
the actual root/quotient/resolution diagrams of F41--F49 give its
meromorphic line map through every removed original additive fibre.
The scalar ratio of two such line maps is a base meromorphic
function, since the generic source elliptic fibre is compact.

At the selected I1, the bounded toric comparison says the source
Tate coordinate has the form q_T^r times a holomorphic nonzero unit.
Dividing by the actual elliptic period q_T^r does not change the
source point and makes it a section of the smooth Neron group.
Thus the source section extends over the selected point. Its
Weierstrass coordinates are meromorphic functions on P1 and hence
rational. Since the marked source Mordell--Weil group is exactly ZG,
the global section is kG for an integer k.

## CP.4. The global valuation equation retains the finite kernel

Use K35's actual meromorphic line lift U_G covering +G, and its
actual rational norm ratio

\[
                   \rho=B_0^{-1}/U_G^b.                   \tag{CP.4}
\]

At a cap i write the literal local line comparison
U_G=z_i^{e_i}h_i L_i, where h_i is a nonzero unit and L_i
extends invertibly. The quotient/resolution map defining L_i is
retained. At an uncapped retained fibre use its corresponding integer
order e_i and m_i=1. At the selected I1 put ord U_G=e_c in its
ordinary rational frame. K35 gives the exact rational divisor orders

\[
 \operatorname{ord}_i\rho=-be_i/m_i,
 \qquad\operatorname{ord}_c\rho=-1-be_c.
\]

Their sum is zero, so

\[
                   e_c+\sum_{i\ne c}e_i/m_i=-1/b.          \tag{CP.5}
\]

The lifted global endpoint has the form h(t)U_G^k. On every root
and retained fibre its invertibility gives
ord_i h=-k e_i/m_i. This includes the full finite-character
condition: the right hand side must be integral. At the selected
cusp, make the unique integral toric reindexing used in CP.1. Its
source-period power has a unit line multiplier. Its suspension
power B_lambda^j has source translation -jbG and line zero of
order j. The bounded remaining line multiplier therefore gives

\[
                      \operatorname{ord}_c h+ke_c=-j.
                                                               \tag{CP.6}
\]

Taking the degree of the actual rational divisor of h and using
(CP.5) gives j=k/b. Hence k=bj. All finite-kernel endpoints have
now been tested against the global ordinary, root and cusp maps;
no central kernel was set to zero locally.

The functions h and rho^j have exactly the same divisor, by
(CP.4)--(CP.6), and therefore differ by a nonzero constant c. Thus
the actual global line map is

\[
                h U_G^{bj}=c B_0^{-j}.
\]

On the compactified suspension B_lambda=lambda B_0 is its literal
deck generator. The displayed map consequently acts by physical
delta multiplication c lambda^j. Conversely every nonzero scalar
is an extending physical-delta automorphism in the source, cap and
cusp charts. The scalar action is faithful: equality with a
suspension power would make a nonzero multiple of bG the zero
section, contradicting the torsion-free Mordell--Weil group. The
global extending translation group is therefore precisely C*.

## CP.5. The actual loop endpoint and the remaining scalar comparison

The endpoint of CP.2 is the physical scalar just computed, not an
unidentified finite central translation. Choose any logarithm of
that single nonzero number. Multiplication by exp(-t log c_end),
0<=t<=1, is an actual isotopy through global delta automorphisms;
compose it with the interval trivialization. Its endpoint closes
literally. It is a smooth bundle trivialization over the parameter
circle, with the same source/cap/annular identifications and the
same transported toric fan. Thus the fixed-scalar cap-data loop has
zero sphere mapping class in this scope. The scalar path acts in
the actual Cox normal coordinates by the given physical circle
weights; no extra normal framing is inserted.

For a varying scalar, the interval construction still compares the
actual family to the scalar family, but its closed parameter must be
read in K35's w-coordinate, lambda=w^{M/b}. A loop in lambda alone
need not have that closed endpoint. The exact compatibility between
the full cap-data endpoint and the K35 fractional deck is the
remaining step of this working note. No numerical division of a
Theta7 class, and no claim that every lambda-loop closes, is made
here. The component-supported OS49 sector also remains outside the
present selected-I1 proof.

## Audit status

CP.1--CP.5 are a complete proposed fixed-scalar argument submitted
for independent audit. The local root-lift patching in CP.3 and its
compatibility with all translated quotient diagrams are the principal
points to inspect. No manuscript export has been made.

# Fresh prereading derivation: cdp:st:C.2.UN.5

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.
Input: `analysis/continuation_VI/UN5_statement_only_fresh_review.tex`,
including the statement of A.5.17 and the named source locators. No target
proof or its proof-scope metadata has been read by this checker.

1. The irreducible normal reduced surface S is a hypersurface in a smooth
threefold. Its singular set has codimension at least two in S, hence is
isolated locally. A local defining equation of the full fibre is u h^m;
absorb a local holomorphic m-th root of the unit u into h. At a singular
point h has an isolated hypersurface singularity. The supplied A.5.17
excludes precisely this germ for a torus degeneration. Its local reason
is also transparent: a vanishing 2-sphere has self-intersection -2 in
the nearby surface, whereas a torus has pi_2=0, making such a sphere
nullhomotopic and its intersection class zero. Thus S is smooth.

2. Normalize the base change t=s^m. Near S the equation is z^m=s^m;
normalization separates the m charts z=zeta*s. The map to Y is a local
biholomorphism on each chart, including S. The central cover A->S is
finite unramified of degree m. The punctured base-change family has
connected fibres and connected base, hence connected total space; its
normal closure remains connected. The normalized map is a proper
submersion also at the central fibre, as the displayed charts show.
Proper smooth transport makes A connected and diffeomorphic to the
nearby two-torus. Deck transformation s->zeta*s is cyclic, has order m
and acts freely on A: locally it permutes the separated sheets.

3. A is a compact complex surface with integral cohomology ring that of
T^4 and b1=4. The stated Buchdahl criterion supplies a Kaehler metric.
Its Albanese map is an isomorphism by the stated homotopy-torus input.
For completeness, the needed implication follows directly from the
cohomology-ring isomorphism and Kaehler Hodge decomposition: H1 has
Hodge type (1,0)+(0,1), each summand of dimension two. Cup product is
the exterior-algebra isomorphism, so the wedge of the two independent
holomorphic one-forms is nonzero. The Albanese map has maximal rank,
induces the integral H1 lattice isomorphism, and has degree one on the
top exterior power. It is bimeromorphic to its two-dimensional torus.
Any exceptional curve of a birational morphism of smooth compact
surfaces contains a rational curve; pi2(A)=0 excludes such a curve.
The map is therefore an isomorphism. The morphism used here is the
actual period-integration Albanese map, not an arbitrary cohomology
identification.

4. Write the generator of the free cyclic action on A as g(x)=Lx+a.
L has finite order. If 1 were absent from its spectrum, I-L would be
an isogeny, so (I-L)x=a would give a fixed point of g. Hence 1 is an
eigenvalue. If both eigenvalues are 1, finite order makes L=I and S is
a torus quotient by translations. Otherwise its eigenvalues are 1
and zeta_n. Rational idempotents in Q[L] give complementary elliptic
subtori and a finite isogeny from their product to A. Thus A and S
are projective, and the nontrivial eigenvalue acts on an elliptic
curve, giving n in {2,3,4,6}. The quotient has q=1 and a torsion
canonical line, hence is bielliptic. The pullback of a holomorphic
two-form transforms by det L=zeta_n. A power of K_S is trivial
exactly when that character power is trivial (pull its nonzero
section back to the constant top-form line on A). Consequently
ord(K_S)=n divides ord(g)=m, and every quotient has e=0 by the
degree-m unramified cover. At m=1 the cover is an isomorphism.

5. For a prescribed bielliptic S of canonical order n, its Albanese
map a:S->E is a smooth elliptic fibration. Its canonical-cover
character is the determinant of fibre monodromy and factors through
pi1(E)=Z^2: fibre loops are translations and have determinant one.
The character Z^2->Z/n is surjective. For every multiple m of n,
lift its two residues to integers that generate Z/m; the Chinese
remainder theorem allows avoiding simultaneous zero modulo each
prime dividing m but not n, while surjectivity already handles
primes dividing n. This gives a surjective character to Z/m whose
reduction modulo n is the canonical character. Pull it back along
a_*; connected Albanese fibres make a_* surjective. Its kernel
defines a connected cyclic degree-m etale cover A_m->S. It factors
through the canonical torus cover, so A_m is a torus. For a given
two-torus S, an index-m subgroup of its lattice with cyclic quotient
gives the same construction directly. The stated primary description
of bielliptic/Albanese covers must be matched at its locator before
awarding the full check.

6. Let g generate the free cyclic deck action on A_m. The diagonal
action (x,z)->(g(x),exp(2*pi*i/m)*z) on A_m times P1 is free, because
every nonidentity deck transformation acts freely on A_m. Its quotient
Y is a smooth compact threefold. The invariant map z->z^m induces
Y->P1. The general fibre is A_m, while the fibres at zero and infinity
have reduced support S and multiplicity m, by the local coordinate
equation. This supplies the exact claimed compact realizations.

No new computational assertion is delegated to a numerical experiment:
the finite character lifts and possible elliptic unit orders are exact
integer/linear-algebra arguments. A fresh finite algebra program can
check the character-lift construction for a bounded range as an
additional test, with the CRT proof covering all m.

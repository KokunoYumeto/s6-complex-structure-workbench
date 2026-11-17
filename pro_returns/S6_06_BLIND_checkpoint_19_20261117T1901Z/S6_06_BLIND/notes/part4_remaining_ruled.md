# Remaining ruled-resolution analysis after P4.37

This is a current-run working record, not a claim that the exact positive-Euler
classification has been completed. The numerical sign theorem is P4.26, the
full zero-Euler classification is P4.32, the rational exact value is P4.35,
and the Hopf and positive-b2 class-VII sectors are settled by P4.36–37.

## Exact additional constraints

P4R.12 proves that every component outside the pole support in a reducible
ruling fibre is a (-1)-leaf meeting a coefficient-one vertical pole component.
Distinct outside components are disjoint. The reduced-horizontal case has no
reducible ruling fibres by P4R.9; this is required before the leaf argument.
The multiplicity of an outside leaf is not forced to be one: the executed
D4 graph in `code/part4/ruled_d4_warning.py` has an outside leaf of multiplicity2.
Thus an elementary transformation selecting that leaf as the sole remaining
fibre component has not been justified.

The exact Chern bookkeeping for the vertical foliation is recorded and executed
in `code/part4/ruled_foliation_bookkeeping.py`, with JSON and output beside it.
For h=2g-2 and D0=2H+aF, H²=-h-a. For R0=rH+rf F and Z0=zH+zf F,
the minimal-model term is 2rf+2zf in the immersive horizontal case,
and -3a-4h+3rf+3zf in the cuspidal horizontal case. The actual vertical
coefficients have not yet been bounded in all configurations. The Hopf/Kato
negative-definite argument alone supplies no such bound on the ruled surface.

## A limitation of the conductor-graph argument

P4.35 excludes an irreducible rational image conductor with one identification
cycle when the normalization conductor has a tree graph. It does not exclude
every reducible conductor graph with one cycle. An exact graph example is:
C has a nodal rational component A and a rational component B passing through
the node; its sole special point has branches A+,A-,B. Take a normalization
conductor with three components Atilde,B1,B2. Identify Atilde(p+) with B1 at
one normalization point and Atilde(p-) with B2 at another. Its graph is the
tree B1--Atilde--B2. The two local hypersurface-branch incidence sets are
{A+,B} and {A-,B}; they intersect. Consequently pairwise intersection of
hypersurface branches and the tree graph do not by themselves give a
contradiction. This is a combinatorial example only; no analytic surface or
smoothing with these data has been constructed.

The attempted stronger inference was withdrawn immediately in the current
team audit. In the contracted-horizontal case, an irreducible rational
unibranch image conductor has pi1(S)=0; P4R.4 and P4.13 then force a positive
regular-locus Euler contribution, exceeding the global bound when e(C)=2.
The two-component, one-cycle conductor requires additional local or
scheme-theoretic conductor information.

## Literature route checked without importing an inapplicable theorem

Primary searches on geometric genus of the normalization and the intersection
form of nonisolated surface Milnor fibres found the classical isolated-normal
Laufer–Steenbrink formulas and surveys of nonisolated vanishing topology.
Their stated isolated-normal hypotheses do not apply to the nonnormal
hypersurface germs presently under study. No implication for this remaining
case is asserted. The next local comparison must retain the actual conductor
and its map to the normalization.

## Elliptic image sector completed by P4R.13

The exact primary-conductor restriction map proves chi(C_sch) <= chi(C_E_sch) <= 0. Since P4.33 identifies the left side with g-1, the ruled base and image are elliptic and all inequalities are equalities. Intrinsic quadratic/cubic jets for A2, the residual quartic for A3, and the binary cubic discriminant for D4 are nowhere zero along the smooth elliptic component. The resulting actual product germs exclude every rational attachment. The normalization is consequently smooth minimal elliptic ruled and the support has Euler number zero. This proof and its independent full audit are retained in notes/part4_elliptic_tail_working.md and notes/part4_elliptic_tail.tex; exact jet checks are in code/part4/elliptic_primary_restriction.*. The remaining ruled sector has two rational normalized image components and one graph cycle.

## Fifth-hour local exclusions

P4.39 excludes a positive-genus coefficient-two exceptional curve at a uniformly D4 point. P4.40 excludes the entire uniformly A1 positive-genus ruled sector. P4R.14 classifies every smooth entire A3 critical-curve germ in the actual torus degeneration as X²+Y⁴ or X(Y²+XZ); the normalization branches are smooth or A1. Its polar identities and six-point exact test pass independently. The A3 ordinary-node conductor calculation is independently audited and being integrated. Mixed transverse types, more general critical-curve singularities and the unrestricted two-rational-component case remain under proof.

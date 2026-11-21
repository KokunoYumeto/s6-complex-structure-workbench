# Derivation before target proof: 01AW

Owner `cdp:st:A.4.7`; checker `i_provenance`. Exact target and empty supplement
read; printed target proof and old checks remain closed. Paper I analytic
normalization and cohomology exposure is disclosed. The following constructs
the stated map and addresses the continuous-primitives point explicitly.

Pull a section alpha of the torsion-free cotangent tensor A to a resolution
of each component of the normalization. Its coefficients give a holomorphic
one-form with values in the pulled-back unitary flat line on a compact smooth
surface. In unitary flat local frames, its covariant differential beta is of
type (2,0). The global scalar three-form alpha wedge conjugate(beta) has
exterior derivative beta wedge conjugate(beta), since the connection is flat
and beta is closed. Stokes on the compact surface gives integral zero.
The (2,2) integrand is pointwise a positive constant times |beta|^2 times
the complex orientation, so beta=0. On one-dimensional components closedness
is automatic. Thus the pullback of alpha is closed on every resolution.

Fix a small analytic neighbourhood U of a point s, trivializing the local
system. A representative of alpha there is a finite sum f_j dg_j in the
Kahler differential module, up to torsion. On the resolution its restriction
to every fibre over s is zero, because all pulled-back f_j,g_j are constant
on that fibre and the differentials of the g_j along it vanish. Small
neighbourhoods of the compact exceptional fibre deformation-retract onto
it; this is the usual analytic triangulation/regular-neighbourhood property.
Consequently all periods of the closed pulled-back form in a sufficiently
small such neighbourhood vanish. Integration gives holomorphic primitives,
chosen zero on each connected exceptional fibre. They descend holomorphically
to the normalization, by the connected-fibre resolution map and
rho_*O_resolution=O_normalization.

The primitives agree over the finite normalization fibres after shrinking U.
To check this, pull them to each component of the reduced fibre product of
the normalization with itself over U. Their differential difference is zero:
both derivatives are pullbacks of the same original Kahler differential.
On the normalization of each such component the difference is constant, and
that constant is zero at its point over s by the chosen values. The finite
normalization map is proper and a topological quotient. The agreeing branch
primitives therefore descend to a continuous function on U, holomorphic on
the normalization. This argument uses the quotient topology and does not
claim holomorphic descent to the possibly non-seminormal O_U.

On an open cover with such primitives f_i, the differences f_j-f_i are flat
locally constant sections of the unitary local system. They define a Cech
one-cocycle and hence a class in H1(S,mathbb A). Changing any primitives by
flat constants changes the cocycle by a coboundary; refinement does not
change the class. Integration and subtraction are complex-linear, so this
defines the canonical complex-linear map in the statement.

Its kernel is zero. A zero class permits flat-constant adjustments making
the local primitives a global continuous A-valued section, holomorphic on
the normalization. Pull it to each compact resolved component. The squared
norm of a holomorphic section of a unitary-flat line is plurisubharmonic;
the maximum principle makes it constant, and the section is parallel.
Its differential, the pullback of alpha, vanishes on every component.
The torsion-free differential embeds in these generic pullbacks, so alpha=0.
This proves injectivity and the required precise regularity of its primitives.

No numerical or symbolic calculation is used. The local resolution
neighbourhood and fibre-product descent steps will be compared explicitly
with the target proof after freeze; they are not treated as automatic proof
credit from the presence of an archive.

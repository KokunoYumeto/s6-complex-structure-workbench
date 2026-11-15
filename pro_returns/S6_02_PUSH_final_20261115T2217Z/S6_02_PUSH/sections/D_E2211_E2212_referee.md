# Independent full-source referee: E.2.11 and E.2.12

15 November 2026. **PASS for both statements at their explicit scope.**
Read in full: `sections/E_torus_purity.tex` and
`sections/E_no_extra_critical_values.tex`.

## E.2.11: the abstract extension criterion

Flatness and the given fibre dimension make the preimage of the missing
base point complex codimension two. Thus the infinitesimal torus-action
fields extend coefficientwise by Hartogs on the smooth total space.
Verticality and commutation extend by the identity theorem. Every
complex-time flow is complete: it remains inside one compact fibre,
and local ODE existence on a finite covering of that compact set gives
continuation past every finite time.

The holomorphic period sections produce a fixed compact real torus
action by holomorphic automorphisms of the entire total space. Integral
period translations are the identity on the dense smooth locus, hence
everywhere. More explicitly, the relative Cn action descends to a
holomorphic action of G times_B X, since translation by every variable
period is already the identity on X. Its action on a scheme-theoretic
fibre, including its nilpotent structure, is therefore legitimate. This
explicit observation justifies using that fibre's Zariski tangent space
in the stabilizer argument without assuming it is reduced.

The connected stabilizer is a compact complex subgroup of the complex
torus G_b. Its representation on the fibre's Zariski tangent is
holomorphic and hence constant. The quotient tangent representation is
trivial because the action fixes the base. Averaging over the compact
stabilizer splits these two representations. The full tangent action is
trivial. The averaged-coordinate construction then gives an invariant
holomorphic coordinate system with invertible derivative; it makes the
stabilizer ineffective in a neighbourhood and hence on connected X.
Freeness on the dense given torsor rules it out.

Zero-dimensional stabilizers make the n commuting fields independent.
The transverse holomorphic two-dimensional slice gives a finite germ
h to the bidisc because its fibre is zero-dimensional. If its Jacobian
vanished, its nonzero determinant would have a curve of zeros, whose
finite image would be a curve of critical values. This contradicts
smoothness off the one base point. Hence g is a submersion.

Each compact full-dimensional orbit in a connected smooth fibre is
then the entire fibre. The residual finite stabilizer acts trivially
on the fibre tangent because the group is abelian, and trivially on
the base quotient. The same finite-group averaging argument eliminates
it. Local holomorphic sections of the submersion consequently identify
the extended family with a G-torsor. No polarization, Kähler hypothesis,
or extension of an affine origin was inserted.

## E.2.12: applicability of the good-Jacobian hypothesis

The three critical graph limits are actual central critical values:
the relative critical image is proper and closed, and smoothness of
the total deformation identifies the relative rank condition with
criticality of the central map. Any other central critical point can
therefore be isolated in a bidisc avoiding all three graph closures.

The meromorphic PGL2 matrix has either an invertible central matrix or
one rank-one limit with one exceptional target point. At least two
labelled preimages tend to that exceptional point, so a hypothetical
extra value is not that point. Uniform convergence to its constant
source image follows. In the finite-source-root cases the expression
is s^n times a holomorphic unit: a zero of the putative leading unit
would create a nonvertical divisor of zeros, precisely a labelled
critical graph, contrary to the choice of bidisc. This unit condition
is essential and is correctly included.

A nearby central regular target gives a smooth torus family over the
whole parameter disc, so its H1 return is the identity. Interiority of
the parameter supplies a single-valued logarithm and no parameter
shear. The finite root orders force 3|n or 4|n. The unit has a
holomorphic root on the simply connected bidisc; pulling back the
actual finite-root period model gives a smooth G over that bidisc.
Additional multiplicity translations do not affect this Jacobian.
The cusp alternative would give the nonzero u-to-w shear in A0^n and
is excluded. An ordinary source image directly gives the ordinary
smooth period model.

The punctured bidisc is simply connected. Its actual torus family and
the reference G therefore admit the same extended integral marking,
after one constant integral change. Their holomorphic period
subbundles coincide on s nonzero and hence on the entire punctured
bidisc. This identifies Jacobians as group families, not only
individual unmarked fibres, and does not assume an extended torsor
section. All hypotheses of E.2.11 now hold.

The final distinction is correct: a finite-root constant image gives
an abelian surface, by the two rational cyclotomic idempotents and an
isogeny to a product of elliptic curves. An ordinary constant image
gives an isotrivial complex torus which need not be abelian. No
projectivity or uniqueness statement for the total central threefold
follows. Excluding these remaining collapsed-target completions and
new deformation branches remains separate.

# The characteristic expression for the actual source-zero coboundary

**Scope correction.** The characteristic substitutions, mapping-torus
cohomology and relative-product algebra below have passed root and peer
audits. The compact global complex coboundary invoked in the first version
has not been constructed: the collision-to-cap attachment through `v=0`
has a newly identified component-monodromy mismatch. That invocation is
withdrawn and preserved under
`code/part3_root/attempts/source_zero_global_attachment_invocation/`.

The source coordinate remains the literal new `v`, with base coordinate
`T`. The actual punctured family and its mapping-torus boundary exist;
the source-zero local collision quotient and the finite-cap chain pieces
also exist separately. On the E overlap, the executed collision atlas
fixes each label `j mod N`, while the finite cap has the signed cyclic
shift `j -> j+kn mod N`. The full affine origin must be implemented before
these pieces can define a global `W`. The source formula recorded in
SC2--3 is therefore a verified computational input whose application to
that proposed global `W` remains unmade. No new theorem or numerical
return is entered from this note.

## SC1. The actual oriented mapping-torus boundary

Write `M` for the mapping torus of the actual rescaled positive `v` loop
on a small parameter circle. This uses only the punctured family. The
relative periodic regular subdivision concerns the local collision
piece and preserves its noncentral part. The missing central overlap
identified above prevents invoking a compact global complex fourfold at
this stage. The following boundary calculations concern `M` itself.

For the boundary identification, choose a smooth horizontal vector field
lifting the positive angular field on the circle. Its flow supplies the
map from a fibre times `[0,1]` to the pullback of `M` over the angular
interval. At the two endpoints its actual return is a diffeomorphism
`Phi` of the oriented six-sphere. Hence the induced quotient map is an
orientation-preserving diffeomorphism

`(S6 x [0,1])/((x,1)~(Phi(x),0)) -> M`.

To check the orientation, write the complex orientation at the boundary
as `or(S6) wedge dr wedge dtheta`. Contraction with the outward radial
normal gives `or(S6) wedge dtheta`, because the fibre has even real
dimension six. This is the forward mapping-torus convention of P3F.24.

The Wang sequence, with `Phi*` equal to the identity on `H0(S6;Z)` and
`H6(S6;Z)`, gives integral cohomology `Z` precisely in degrees 0,1,6,7
and zero in the other degrees. In particular

`H2(M;Z)=H3(M;Z)=H4(M;Z)=0`.

Here and below `Hj` in this displayed cohomology discussion denotes
cohomological degree j. The tangent bundle of `M` has `w2=0`, since
`H2(M;Z/2)=0`. There are two spin structures, parametrized by
`H1(M;Z/2)=Z/2`. The verified spin-c formula uses a determinant class `z` whose
restriction to `M` vanishes. The computed group `H2(M;Z)=0` supplies
exactly that boundary vanishing and permits a boundary trivialization,
which induces one of the two spin structures. P3F.24 proves, by
the explicit oriented connected-sum map and the spin coboundary
`S1 x D7`, that both structures have the same Eells--Kuiper value.

## SC2. Relative products with the degree-one boundary class retained

In the verified coboundary formula, the map used for its products is
`j:H4(W,M;Z)->H4(W;Z)`. The preceding boundary vanishing
in degrees three and four and the exact sequence of the pair make `j`
an isomorphism. Define the integral middle pairing by

`Q(x,y)=<j^(-1)(x) cup y,[W,M]>`.

Its real extension has signature `sigma(W)`. This definition also specifies
the pairings in the characteristic polynomial: `c1^4=Q(z^2,z^2)`,
`c1^2*c2=Q(z^2,c2)`, and `c2^2=Q(c2,c2)`. Torsion maps to zero under
the final evaluation and introduces no choice of rational lift.

The restriction of `z` to `M` vanishes, so a relative lift
`bar z in H2(W,M;Z)` exists. Its possible differences are the classes
`delta(a)`, with `a in H1(M;Z)`. We retain this ambiguity. For any such
difference, the product formula for the connecting homomorphism gives
`delta(a) cup bar z = delta(a cup i*z)=0`, where the second product uses
the absolute image of `bar z`. Likewise `(delta(a))^2=0` because its
absolute image restricts trivially to `M`. Thus `(bar z)^2` is independent
of the chosen lift and equals `j^(-1)(z^2)`. These are exactly the
relative products occurring in the spin-c boundary formula.

## SC3. The verified spin-c formula and exact substitution

Crowley--Nordstrom, *Exotic G2-manifolds*, Math. Ann. 381 (2021),
29--74, Section 2.2, equation (2.1), defines the invariant for a closed
spin seven-manifold with torsion-free degree-four cohomology using a
spin-c eight-dimensional coboundary. The boundary cohomology hypotheses are exactly those of
the `M` just computed. A global source-zero coboundary is the remaining
construction obligation before applying this formula to its local data. Its spin class `p_M` is zero, so its divisor is
`d=0` and the invariant takes values in `Z/28`. The class
`hat p=(p1(W)+z^2)/2` restricts to zero. With `d=0`, that equation reads

`mu_Z28(M)=(hat p^2-sigma(W))/8 - 5*(bar z)^2*hat p/12 + z^4/4`.

All its pairings were specified in SC2. Lemma 2.1(i) of the same source
gives `hat p=c1^2-c2` for the almost complex structure. The underlying
real tangent bundle has `p1=c1^2-2*c2`. Substitution, with every product
interpreted through `Q`, gives

`mu_Z28(M)=(3*p1^2-14*z^2*p1+7*z^4-12*sigma(W))/96`

`=(-c1^4+4*c1^2*c2+3*c2^2-3*sigma(W))/24 mod 28`.

This extends the already proved P3R.1 homotopy-sphere expression to the
actual mapping-torus boundary; SC2 supplies the needed treatment of its
degree-one class. The exact substitutions are executed in
`code/part3_root/source_zero_spin_c_boundary.py`.

For normalization, on the spin eight-disc bundle over `S4` with Euler
number 1 and `p1=6` times its positive generator, the relative middle
square of `p1` is 36 and the signature is 1. The displayed expression is
`(36-4)/32=1`. Its classical Eells--Kuiper value is `1/28`. Thus the
integer-valued normalization agrees with the first-page presentation of
`Theta7`. Independently of the unresolved filling, the forward mapping-torus
identification in SC1 and P3F.24 gives `[Phi]=mu_Z28(M)`.

## SC4. Exact remaining computation

First the actual global collision-to-cap attachment must be supplied.
The quantities requested by the verified formula are `Q(z^2,z^2)`,
`Q(z^2,c2)`, `Q(c2,c2)`, and `sigma(W)` of a complete coboundary.
The current local pieces do not yet supply those global quantities. The cone matrices and their period maps give local tangent
characters. The continuations through the common H face, the protected
I/E boundaries, and the finite caps determine how those local classes
assemble. These data are being computed explicitly. The expression
above retains the signature of the actual manifold with boundary.
No closed-manifold signature identity has been applied to `W`, and no
numerical return is entered from its local fixed-stratum counts.

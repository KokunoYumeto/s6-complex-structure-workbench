# The characteristic expression for the actual source-zero coboundary

This is a derivation for the regularized complex fourfold of the current
source-zero construction. The source coordinate is the literal new variable
`v`, with the literal base coordinate `T`. Its passage to the old `u,t`
marking is the separate annular-clutch computation in
`part3_source_zero_relative_comparison_working.md`. No value of an old-source
return is assigned here.

## SC1. The compact coboundary and its actual oriented boundary

Let `W` denote the inverse image of a sufficiently small closed `v` disc in
the smooth complex fourfold constructed in Sections 19--22 of
`part3_source_zero_completion_working.md`, after the relative periodic
regular subdivision in `part3_source_zero_equivariant_resolution_audit.md`.
The protected I/W/E boundaries and the signed finite-cap chain charts give
the specified rescaled family on the punctured disc. Properness of that
map makes `W` compact. The circle boundary lies in the smooth submersion
locus, so its inverse image `M` is smooth and is the actual mapping torus
of the rescaled positive `v` loop. The regular subdivision changes only
the central fibre. In particular it leaves this boundary and its positive
parameter marking literally unchanged.

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
`H1(M;Z/2)=Z/2`. The almost complex tangent bundle of `W` determines a
spin-c structure with determinant class `z=c1(TW)`. Its determinant line
restricts to a trivial line on `M`, since `H2(M;Z)=0`; a trivialization
therefore induces one of those two spin structures. P3F.24 proves, by
the explicit oriented connected-sum map and the spin coboundary
`S1 x D7`, that both structures have the same Eells--Kuiper value.

## SC2. Relative products with the degree-one boundary class retained

Write `j:H4(W,M;Z)->H4(W;Z)` for the natural map. The preceding vanishing
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
spin-c eight-dimensional coboundary. The definition applies to the
`M` just computed. Its spin class `p_M` is zero, so its divisor is
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
`Theta7`. The forward boundary identification of SC1 and P3F.24 give

`[Phi]=mu_Z28(M)`.

## SC4. Exact remaining computation

The four quantities `Q(z^2,z^2)`, `Q(z^2,c2)`, `Q(c2,c2)`, and
`sigma(W)` must now be evaluated for the full glued regularized
fourfold. The cone matrices and their period maps give local tangent
characters. The continuations through the common H face, the protected
I/E boundaries, and the finite caps determine how those local classes
assemble. These data are being computed explicitly. The expression
above retains the signature of the actual manifold with boundary.
No closed-manifold signature identity has been applied to `W`, and no
numerical return is entered from its local fixed-stratum counts.

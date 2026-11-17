# Elliptic image component: restriction of the conductor and transverse jets

Status: proved as P4R.13. Independent checks-agent audit completed in full
on 2026-11-17: trace/ideal map, blowup cohomology, primary saturation, both
cohomology directions, and all cubic/quartic/discriminant transitions passed.
The final minimality and Euler argument does not assume the zero-Euler theorem.

Use the actual minimal normalization resolution `rho:T -> N -> S` of an
irreducible support in Part 4.2. The pole divisor has horizontal part `2H`,
where H is a section of the ruled resolution. Suppose the reduced image
conductor has an elliptic normalized component E. The curve-group calculation
already proved makes E the unique component of positive genus, with no
point-identification cycles; all its points are unibranch and its other
components are rational trees. H maps nonconstantly to E, with degree 1, 2,
or 3 according as the generic transverse germ is A2, A3, or D4. Write g for
the genus of H. Riemann--Hurwitz gives g >= 1.

## 1. The actual sheaf map to the resolved pole divisor

Since H is not contracted, P4.33 gives rational singularities on N. Put
`L=nu^*omega_S`, a torsion line bundle on N. Finite duality gives its conductor
ideal `I_N=omega_N tensor L^{-1}`. The identity

    rho_N* omega_T = omega_N

is the canonical trace identity for rational analytic singularities. The
opened primary source is Greb2011, Remark 2.1, printed p415; N is normal and
Cohen--Macaulay, rho_N is a proper resolution, and P4.33 proves R1 rho_N*O_T=0.
The surface has no higher direct images of its structure sheaf, so these
are precisely the source's rational-singularity hypotheses. The integral
pole identity gives `O_T(-D)=omega_T tensor rho_N^*L^{-1}`. Projection formula
therefore identifies, as ideal subsheaves of O_N,

    I_N = rho_N* O_T(-D).

Applying rho_N* to the divisor ideal sequence gives the actual injection

    O_N/I_N -> rho_N* O_D.

The conductor square in S and its finite normalization gives a second
injection `O_Csch -> nu_*(O_N/I_N)`. Their composition is a morphism of
coherent O_S-algebras into `(nu rho_N)_* O_D`.

## 2. Global functions on D are detected along 2H

For every actual point blowup beta in T -> T0 the pole divisor is
`D'=beta^*D-E`. The elementary blowup direct images are

    beta_* O(E)=O,   R1 beta_* O(E)=0,
    beta_* O=O,      R1 beta_* O=0.

The first equality follows by Hartogs extension of the descended function
off the centre. For the vanishing, the exact sequence
`0 -> O -> O(E) -> O_E(-1) -> 0`, or the two blowup charts, reduces it to
`H1(P1,O(j))=0` for j >= -1. Projection formula and the divisor ideal
sequence consequently give

    beta_* O_D' = O_D,   R1 beta_* O_D' = 0.

Iterating these particular maps identifies global functions on the actual
D with global functions on `D0=2H0+sum a_j F_j`. On the minimal ruled
surface the kernel of `O_D0 -> O_2H0` is

    O_(sum a_j F_j)(-2H0).

Its successive layers on each distinct fibre are `O_P1(-2)`, since
`F_j^2=0` and `H0.F_j=1`. All have zero H0. Thus a global function on D
which vanishes generically on the doubled horizontal section is zero.
The assertion concerns the full doubled scheme, not only its reduction.

Let C_Esch be the primary component of Csch supported on the elliptic
image component: its ideal is obtained from the actual conductor ideal by
localizing at that component's generic point and contracting. The conductor
is Cohen--Macaulay, and this primary quotient has no finite-length submodule.
The quotient map `O_Csch -> O_C_Esch` is surjective. Its kernel has support
of dimension at most one, so the induced map on H1 is surjective. Its map
on H0 is injective: a global function in the kernel maps by Section 1 to
a global function on D which vanishes at the generic doubled H, hence is
zero by Section 2. The injection of Section 1 then makes the original
global function zero. Therefore

    chi(O_Csch) <= chi(O_C_Esch).

## 3. The primary elliptic component has nonpositive Euler characteristic

For generic A2 its conductor is reduced, so the primary ideal is the
reduced curve ideal P_E and its Euler characteristic is `-sum delta <= 0`.
For generic D4 its primary ideal is `P_E^(2)`; the exact differentiation
map and lattice calculation of P4.30 apply to this primary component and
give the same bound, with equality only for smooth E.

For generic A3 the primary ideal contains `P_E^(2)`, and its quotient
`J=P_E/I_E` is torsionfree of rank one on E. The proof of P4R.10 uses only
this primary quotient, the Hessian of the actual local equation, and the
normalization map of the curve. It therefore applies without a restriction
on other image components. Explicitly, differentiation maps
`P_E/P_E^(2)` into the rank-two conormal bundle K on E's normalization;
the Hessian image saturates to a line L in K; projection to K/L injects J.
The local lattice inequalities give

    chi(O_C_Esch) = -sum delta + deg R
                   - (sum Hessian-zero orders)/2
                   - sum projected colengths - sum descent defects <= 0.

Equality makes E smooth and makes the Hessian nowhere zero on it. The
generic description of each primary ideal and its depth-one property
justify all three identifications; no ideal along a rational component
has been discarded from Csch.

P4.33 supplies `chi(O_Csch)=g-1`. The preceding comparison gives

    0 <= g-1 = chi(O_Csch) <= chi(O_C_Esch) <= 0.

Thus g=1, E is smooth, and H -> E is unramified. In the A3 case the
transverse Hessian has rank one everywhere on E.

## 4. Intrinsic transverse jets exclude every attachment to E

Now E is a smooth elliptic curve in the smooth threefold Y. Its conormal
bundle K has degree zero, because `c1(TY).E=0`. The line
`N=O_Y(S)|E` also has degree zero, since a positive multiple of S is
principal in a tube around the fibre. All tensors below use the actual
reduced local defining equation of S and its transition units.

In generic type A2 the quadratic normal jet is rank one. Let L be its
saturated image line, put Q=K/L, and write the quadratic tensor as a
section of `L^2 tensor N`. It is nonzero, so `2 deg L >= 0`. The cubic
normal jet restricted to the null direction is an intrinsic section of
`Q^3 tensor N`. It is nonzero generically because the type is A2. To check
independence of coordinates, a change of the second-order lift of a normal
vector changes the cubic term by the polarization of the quadratic term;
that polarization vanishes on its null direction. A change in the lift of
the tangential coordinate contributes a derivative of the quadratic
tensor, whose evaluation twice on the null direction also vanishes.
Changing the defining equation multiplies this tensor by its transition
unit. Consequently `-3 deg L >= 0`. Both degrees are zero, and both
sections are nowhere zero. The Morse lemma in the nondegenerate direction
and a cube root of the residual unit give `X^2+Y^3=0` times the E-coordinate
near every point of E. In particular no other critical curve meets E.

In generic type A3 Section 3 already makes the quadratic jet nowhere
zero, so deg L=deg Q=0. The cubic null jet vanishes identically. After
removing the quadratic direction by the holomorphic Morse lemma, the
residual fourth jet is an intrinsic section of `Q^4 tensor N`. In coordinates
whose relevant jets are

    a x^2 + b x y^2 + c y^4,

its coefficient is `c-b^2/(4a)`. Substituting the critical coordinate
`x=-b y^2/(2a)+O(y^3)` proves this formula. Replacing x by `x+v y^2`
changes b to b+2av and c to c+bv+av^2, and leaves that coefficient
unchanged. Changes of normal frames and of the defining equation give
exactly the Q^4 tensor N transition; changing tangential lifts has no
effect because the residual function starts in order four. This section
is nonzero generically and has degree zero, hence never vanishes. The
residual function is `y^4` times a unit, giving the product tacnode at
every point of E. Again no other critical curve meets E.

In generic type D4 the equation belongs to the third power of the ideal
of the smooth E: this power is primary, and generic order three proves
membership. Its cubic normal jet is a binary cubic in `Sym^3 K tensor N`.
The discriminant is a section of `(det K)^6 tensor N^4`, of degree zero.
It is nonzero generically, so is nowhere zero. At every point there are
three distinct normal tangent directions. Holomorphic factorization
gives three smooth branches through E. Straightening the first two gives
coordinates x,y; the third is `a x+b y` with both coefficients units.
The changes X=ax, Y=-by put the union in product ordinary-triple form.
Its entire singular locus near E is E itself.

The reduced image conductor is connected. A rational tree attached to E
would meet E, contradicting these actual local product forms. Thus there
are no rational components. The local product forms make N smooth along the conductor. It was already
smooth away from it by P4R.6. Thus T=N. There is no vertical component
of D, because a finite normalization cannot contract one and a rational
curve cannot map nonconstantly to E. Hence D=2H. In the actual blowup
sequence from T0, the first blowup of 2H0 would create a coefficient-one
vertical pole component, and subsequent blowups never remove a strict
pole component. No blowup therefore occurs. The normalization is a smooth
minimal elliptic ruled surface. Finally e(N)=e(H)=e(E)=0, and additivity
for the finite conductor pushout gives e(S)=e(N)-e(H)+e(E)=0.

## Exact checks and source

The jet transformation formulas and the degree comparisons are
executed in code/part4/elliptic_primary_restriction.py. The primary analytic
duality source is Daniel Greb, Rational singularities and quotients by
holomorphic group actions, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (5) 10
(2011), 413--426, Remark 2.1, p415, opened in this run at
https://www.numdam.org/item/ASNSP_2011_5_10_2_413_0.pdf.

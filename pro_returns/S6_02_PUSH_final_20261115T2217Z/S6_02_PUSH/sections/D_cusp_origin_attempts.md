# The missing cusp origin: comparison and base-modification audit

## Superseding correction, 19:41 UTC

**The proposed application of the calculation below to the actual cusp
completion is withdrawn.** The retained finite-place convention in B.3
uses clockwise root deck generators. Consequently the required clockwise
cusp shift is minus one, while the positively rotating q-root generator
in B.4.18 must use **+b and +F**, with positive-q shift plus one. The
earlier choice of -b/-F had the wrong retained global orientation.

More importantly, the actual comparison is
`zeta -> zeta-sigma+F`, not translation by F alone. With
`c=-12t`, the known affine trivialization has
`sigma_1=6 mu t`, so

`F_1-sigma_1=mu s/2`.

Its first elliptic coordinate is independent of r. Thus the nonconvergent
elliptic orbit obtained below by studying F or -F alone in Jacobian
coordinates is **not an obstruction to the corrected actual comparison**.
That isolated calculation concerns a specified different comparison and
must not be used to rule out a base-blow-up construction or an origin cap
for the retained family. The cancellation is potentially useful for the
next constructive attempt. The actual origin completion remains Open.

Owner: boundary_d. 15 November 2026, 19:15 UTC.

## Current target and established input

The accepted partial construction in
`ab_push_corrected_cusp_overlap_working.md` is proper over
`(Delta_q x Delta_r) minus {(0,0)}`. It has the actual reduced Mumford
cusp on `r != 0` and the required negative component rotation on
`q != 0, r=0`. The exact comparison on the two-puncture overlap is the
translation `-f` (composed with the established affine gauge), where

`f_1=mu(s+12t)/2`,

`f_2=C(s+12t)/12-(s+12t)^2/24+6t`,

`s=log q/(2 pi i)`, `t=log r/(2 pi i)`.

The remaining problem is a proper analytic extension over the origin
with the required smooth-total-space and normal-crossings properties.
The present note does not solve it.

## A precise limitation of finite base blow-ups and graph comparison

The proposed translation has essential nonextension already on a fixed
generic slice `q=q_0 != 0` of the r-axis. This explains why blowing up
only the bidisc origin cannot turn the two full toric models into
meromorphically comparable models. The statement concerns the specified
comparison; it is not an obstruction to every analytic cap.

Fix a logarithm `s=s_0`, and abbreviate

`tau=tau(q_0)`, `mu=mu(q_0)`, `beta_0=C(q_0)-s_0`,

`a_mu=Im(mu)/Im(tau)`.

Here `mu != 0` for every sufficiently small nonzero q_0, since its
known limiting value is nonzero. The rank-three semiabelian group has
periods `(tau,mu)`, `(1,0)`, `(0,1)`. A globally defined logarithmic
Hermitian fibre norm is

`ell(zeta_1,zeta_2)=Im(zeta_2)-a_mu Im(zeta_1)`.

It is invariant under all three periods. This correction is essential:
the raw absolute value of `exp(-2 pi i zeta_2)` is not invariant under
the elliptic period. The closing period is

`gamma=(6mu,beta_0-12t)`.

Put `t=a+iT`, with a fixed real a and T tending to positive infinity.
Direct expansion gives

`f_1=constant+6i mu T`,

`ell(f)=constant+[Re(beta_0)+6-12a-6a_mu Re(mu)]T`.

Consequently the fibre-norm valuation relative to `|r|=exp(-2 pi T)`
is

`v=-Re(beta_0)-6+12a+6a_mu Re(mu)`.

As the ray argument a varies through an interval of length one, v
varies through an interval of length twelve. Choose a for which v is
not an integer. Subtracting a constant multiple of gamma places v
between two consecutive component labels of the standard twelve-cycle
model; the bounded unit in the closing period does not affect v.
The two node coordinates then have norms asymptotic to positive
constants times `|r|^(v-k)` and `|r|^(k+1-v)`, for the appropriate
integer k. They both tend to zero. Thus the image approaches one fixed
conductor stratum, whose elliptic coordinate is

`[constant+6i mu T] in C/(Z+tau Z)`.

This coordinate has no limit. Indeed, if a real one-parameter subgroup
`[vT]` of a compact torus had a limit as T tends to infinity, then for
each real h its translation by `[vh]` would have the same limit. Hence
`[vh]=0` for every h, and discreteness of the lattice would give v=0.
Here v in that argument is `6i mu != 0`. The same argument applies to
the negative comparison and after every finite base change in r.

On a sufficiently small simply connected q-neighbourhood, the zero
section of the rotating model's root-cover presentation extends to the
smooth part of its r-central normalization. Under the specified
comparison its image is the section represented by `-f`. If that
comparison extended meromorphically at all points of this zero section
over r=0, restricting its proper graph to a generic such section would
give a meromorphic map from a disc to the proper target. A meromorphic
map from a nonsingular curve to a proper target extends holomorphically
(its proper modification of the normal curve is an isomorphism).
The nonconvergence above contradicts this. Equivalently, the indicated
section itself admits no meromorphic extension.

A finite sequence of blow-ups of the bidisc origin is an isomorphism
near every `(q_0,0)` with `q_0 != 0`. It therefore cannot remove this
divisorial nonextension of the specified comparison. A common
modification/graph-closure construction cannot simply be assumed.

This argument does **not** prove that the glued partial family cannot
extend. A proper family can contain holomorphic sections on punctured
discs with essential singularities. Nor does it rule out a different
comparison differing by an automorphism which itself fails to extend.
It only prevents treating the displayed exact affine trivialization
as a meromorphic toroidal change of coordinates.

## Parallel cap route and unresolved compatibility

AB is examining compact Calabi--Eckmann/LVMB pieces. Such pieces can
supply non-Kahler normalization components; the already proved
B.4.15 insertions alone preserve the existing component cycle and
cannot close it. A useful new cap would have to match all marked
Hopf/elliptic boundary divisors and their normal lines, not only one
abstract Hopf surface. It must also carry actual analytic smoothing
charts whose punctured quotient is the prescribed torus family.

For the elementary quotient with weights `(a_1,1,b,b)`, one Hopf
divisor has multiplier `exp(2 pi i b)` and normal multiplier
`exp(2 pi i a_1)`, but the opposite divisor has Hopf multiplier
`exp(2 pi i b/a_1)`. Thus matching one boundary does not automatically
match the opposite boundary. No finite network or smoothing has yet
been constructed here. The exact origin completion remains Open.

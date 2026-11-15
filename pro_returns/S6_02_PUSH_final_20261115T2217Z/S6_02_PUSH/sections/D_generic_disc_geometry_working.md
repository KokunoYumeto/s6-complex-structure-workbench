# Generic analytic-disc geometry: finite bad sets

Owner: boundary_d. 15 November 2026. Working lemma supplied to E for
the generic-propagation argument. No additional result number or
arbitrary-chain conclusion is assigned here.

## Setup

Let X be a smooth complex fourfold, proper and smooth over a connected
parameter curve S, with compact fibres diffeomorphic to S6. Suppose an
intrinsic pencil has already been constructed as a proper map
g:X -> P1 x S on the current parameter domain, and that its distinct
critical multisections and their multiplicities have been separated
after deleting a discrete analytic set and, locally, a finite base
change. Assume there is a nonempty parameter open set on which this is
the prescribed family. All assertions below concern this current
parameter domain; later bad sets need not be discrete at previously
removed points. Fill the layers in reverse order using E.2.21.

## A total reduced cusp hypersurface becomes relatively NC generically

Let D be the total cusp divisor. It is reduced. A divisor component
contained over one parameter value would be the whole threefold fibre
of X -> S, contrary to nonconstancy of its pencil. Thus every divisor
component dominates S. Its multiplicity equals one on the known open
set, and hence everywhere. A hypersurface in a smooth space has no
embedded components, so these facts imply total reducedness.

Take the finite analytic normalization nu:Dtilde -> D -> X. The
normalization is proper over S. Delete the images of its singular locus
and, on the smooth part, the critical locus of Dtilde -> S. These are
proper analytic images and miss the known relative-NC open set; they
are therefore discrete analytic subsets of S. After this deletion
Dtilde is smooth over S.

Now delete the image of the rank-drop locus of the relative derivative

T_(Dtilde/S) -> nu* T_(X/S).

This too is a closed analytic locus proper over S, absent on the known
open. The resulting nu is a holomorphic immersion. It is finite onto
its image, so it is unramified: its diagonal is both open and closed in
Dtilde x_X Dtilde.

For k=2,3,4 let R_k be the locus of ordered, pairwise distinct preimages
in the k-fold fibre product of Dtilde over X. Partial diagonals are
open and closed by the preceding unramifiedness, so R_k is a closed
analytic subspace of that proper fibre product and is proper over S.
At each of its points the k local sheets have relative normal covector
lines in the same rank-three bundle T*_(X/S). On R_2 and R_3 remove the
images of the rank-drop loci of these k lines. Remove also the image of
R_4. All are proper analytic images, and all are empty over the known
relative-NC open set, hence discrete on S.

At a remaining point the total normalization has at most three local
sheets. Each is embedded as a smooth hypersurface in X, submersive over
S, and their vertical normal covectors are independent. Since the
TOTAL D is a reduced embedded hypersurface, its local ideal is exactly
the product of the distinct local equations of these sheets. There is
no possible extra finite-subring or seminormality datum. The independent
vertical covectors make those equations, the original parameter on S,
and the remaining coordinates a holomorphic coordinate system. Thus
q is a unit times x, xy, or xyz; the unit is absorbed into one branch
coordinate. These are the required relative NC equations.

This total-space argument also proves reducedness of each remaining
cusp fibre. It does not assume normalization commutes with base change.
An earlier optional suggestion to delete nonflatness of the quotient
nu_*O_Dtilde/O_D is unnecessary once one works with the total reduced
embedded hypersurface in this way.

## Finite root charts

Let q be a transverse coordinate to a finite critical section and let
m be its multiplicity on the known open. On the total smooth X its
divisor is mD: all its components dominate S and the multiplicity is
constant there; a whole parameter fibre cannot be a component because
the pencil on that fibre is nonconstant.

Locally q=a^m u, with a reduced equation of D and a unit u. After a
local holomorphic choice of u^(1/m), normalization of r^m=q gives the
disjoint graphs

r=zeta a u^(1/m),  zeta^m=1.

Each graph is a copy of X. Thus this cyclic root cover is smooth and
etale over X and its cyclic deck action is free, without first knowing
that the finite reduced fibre is smooth. The only remaining issue is
submersivity of its map to the root disc times S. On r!=0 this follows
from the propagated ordinary-locus condition. Its critical locus over
r=0 is closed and proper over S, and is absent on the known open.
Deleting its discrete image gives the required smooth root torus
families. Their compact fibres have the same topology as the known
root tori; surface classification and the inherited integral canonical
class identify the ordinary surfaces as complex tori.

## The period identity should be imposed on kernels

At one fixed ordinary target point t0, the invariant integral cycles
w and delta give two holomorphic period vectors. Their complex wedge
has a marking-independent zero set on S; since it is nonzero on the
known open, this set is discrete. Normalize the Lie frame there and
extract c(s) from the gamma column. The identities for the other columns
at t0 extend by the one-variable holomorphic identity theorem.

On the universal cover of the entire ordinary target times this
parameter domain, compare the actual holomorphic Hodge kernel
subbundle of Lambda_C with ker Pi_ref(t,c(s)). They coincide on the
product with the known open set and hence everywhere. This formulation
does not assume that normalization by w,delta was already possible at
every ordinary t, and does not improperly project a determinant-zero
set from a noncompact punctured target. The kernel identity proves that
normalization is possible everywhere afterwards.

These are analytic finite-locus constructions and holomorphic identity
arguments. They replace an unsupported generic topological
stratification assertion. The final assembly and reverse-order filling
of parameter exceptions are to be supplied in E's propagation theorem.

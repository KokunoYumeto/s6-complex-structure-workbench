# Other-axis Tate interface: independent check and exact scope

Reviewer: boundary_d. 15 November 2026. This note checks the formulas
proposed by limits_ab for the other axis in B.4.10; it does not claim
an attachment to the actual two-period cusp or an origin cap.

## Cartier divisor and normal line

On the Kato fundamental domain define the divisor by
`pi_n^* w - s = 0`. The actual collar map is `sigma_s pi_n`, and
its second coordinate gives the exact identity

`w_new - s = a(s) (w_old - s)`.

It therefore glues to a relative Cartier divisor D. For s nonzero
the equation w=s avoids all blow-up centres, so it is the untouched
other Hopf axis. In its tangent coordinate the closing multiplier is
`lambda(s)=kappa(s) s^n`; in its normal coordinate it is `a(s)`.
Thus the generic pair is the marked elliptic curve E_lambda with the
degree-zero normal line of factor a.

At s=0 the total transform of w is reduced. Each successive blow-up
centre lies on the newest exceptional component and the strict x-axis,
but only the former belongs to div(w); the new exceptional coefficient
is therefore one at every step. The strict horizontal axis and the
n exceptional curves form the usual chain before collar gluing.
Identifying its end annuli gives the rational n-cycle. At each node
the ambient blow-up coordinates have `pi_n^*w=uv`, so D has equation
`uv=s`. Hence the total D is smooth and D to the s-disc is a semistable
I_n elliptic family. The normal line has the unit closing factor a(s)
and degree zero on every central component.

For the first period in the actual cusp, `q c1` is the Tate multiplier
and `c2` is the other-coordinate multiplier. After q=z^12, choosing
n=12, kappa=c1 and the contracting choice of c2 (or its inverse when
the transverse coordinate is inverted) matches this Tate curve and
its marked normal factor. This is an interface/normal-line match.

## A relative linear tubular neighbourhood is impossible

At a node the ambient Kato family has smooth coordinates (u,v,s)
and is a submersion to s. The divisor is `uv-s=0`. If e denotes its
defining normal coordinate, then

`e=uv-s`, equivalently `s=uv-e`.

In contrast, the total normal bundle of D, projected to the same base
through D, has local coordinates (u,v,e) and base function `s=uv`.
This map has a critical normal line u=v=0. The Kato family has no
such critical points, since the derivative of `uv-e` in e is -1.
Consequently there is no biholomorphic identification over s of these
two neighbourhoods, even though their normal lines agree exactly.

This also appears in the contracted germ

`(x,v) -> (kappa(s) x (a(s)v+s)^n, a(s)v)`.

The generic diagonalizing product uses v/s and is only a punctured-
parameter construction. Its existence does not linearize the total
neighbourhood across the I_n nodes.

## Explicit local non-toroidal plumbing

If an inverse normal coordinate f is introduced and the two normal
coordinates are plumbed by `ef=r`, elimination of e gives

`r=f(uv-s)`.

The total space is smooth in coordinates (u,v,f,s). The r-central
divisor is the union of the two smooth transverse hypersurfaces
`f=0` and `uv-s=0`, so it is SNC. For r nonzero the map to s is
submersive in this patch: rank failure of (s,r) would require
`fv=fu=uv-s=0`, which forces r=0. Thus this plumbing replaces the
local Tate node; it does not preserve a toric chart s=uv.

The equations provide a concrete local coupling which any attempted
attachment must respect. They do not establish the global second-
period action, the prescribed actual cusp strata, properness of an
origin cap, or the required global S6 filling. In particular they do
not evade the already proved obstruction to lifting a nontorsion
second elliptic translation to one fixed finite Hopf modification.

## Exceptional curves obstruct a naive whole-family attachment

For each fixed s nonzero the Kato fibre is obtained by n blow-ups of
the diagonal Hopf surface. The blow-up centres lie on its first axis
at the orbit v=-s, followed by infinitely near centres on that same
strict axis. The other axis D_s is v=0 with the first coordinate
nonzero. The two axes in a diagonal Hopf surface are disjoint, so every
curve of the exceptional configuration is disjoint from D_s.

A standard normal plumbing which leaves the complement of a small
neighbourhood of D_s unchanged therefore retains these compact rational
curves on each nearby r-nonzero surface over this fixed s. A complex
two-torus contains no rational curve: a holomorphic map P1 to it lifts
to its C2 universal cover and is constant. Consequently such a plumbing
of the entire Kato family cannot be biholomorphic, over the same
ordinary base, to the prescribed family of two-tori. This does not
exclude a construction which further deforms the exceptional region or
changes its relation to the original base. It identifies another exact
condition a global attachment must address.


## Restricted degree-twelve cone obstruction and its degree-one bypass

The linear neighbourhood of the persistent elliptic axis in the n=12
Kato model contracts to the cone of a degree-twelve line bundle on an
elliptic curve. Pinkham's original Theorem 7.5 (printed p.45), together
with the explicit elliptic-cone discussion in Section 9.2(a) (printed
pp.63–65), excludes a smoothing of this degree-twelve cone. Thus the
degree-eight contraction-and-quadric smoothing of B.4.11–12 cannot be
repeated merely by replacing S_8 by S_12. This is a restriction on that
specific contracted singularity, not an obstruction to every analytic
origin cap.

Source: Pinkham, H. C. (1974). *Deformations of algebraic varieties with
G_m action*. Astérisque, 20. Société mathématique de France. Original
full primary PDF opened at
https://www.numdam.org/item/AST_1974__20__1_0.pdf . The exact opened
sections were independently checked in this session; bibliography key
Pinkham1974Root already exists, so no duplicate entry was introduced.
Retrieval records: turn537view0 (metadata), turn537view1 (full PDF),
turn538view0 (§9), turn538view1 (§7), turn543view0 (Theorem 7.5).
Screenshot calls returned textual ImageDisplayed placeholders, so the
audit does not claim a separate visual reading of those screenshots.

The degree-one construction of B.4.21 bypasses precisely that restricted
obstruction. Start with n=1, make the base change q=s^12, and modify the
other-axis rational cycle. All its centres are disjoint from the
persistent elliptic axis. Consequently that axis retains its degree
minus one, while the other axis becomes the smooth I_12 Tate surface.
B.4.21 proves more than an equality of normal classes: its coordinate
H=h/q is holomorphic on an actual collar and its convergent product G
conjugates the closing to a linear Tate-line closing. This does not
construct or globalize a smoothing of the contracted degree-one axis,
and does not identify the whole modified Kato family with the prescribed
ordinary tori. The exceptional-curve obstruction above remains applicable
to a plumbing which leaves that entire complement unchanged.

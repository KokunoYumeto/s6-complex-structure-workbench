# Independent referee: B.4.19 global partial filling

Reviewer: boundary_d. 15 November 2026. Full source reviewed:
`sections/ab_push_global_partial.tex`, together with
`code/ab_push_global_partial.py/.out/.json` and the actual closing
formula in `sections/C_closing_cocycle.tex`.

**PASS at the stated scope.** The proof constructs the actual global
family over `(P1 x Delta_r) minus {(infinity,0)}`, including all finite
and cusp overlaps through r=0. It does not construct the missing origin
cap or a proper family over the whole parameter disc.

## Closing and ordinary charts

For h=-12 the exact C.3.5 translation is
`Pi_c gamma-(k+6)delta`. Removing the integral gamma period and six
delta periods leaves `-k delta`. Hence the coordinate
`zeta_tilde=zeta+k v delta`, with `v=log r/(2 pi i)`, has trivial
parameter-deck translation modulo the actual period lattice.

On ordinary overlaps `k_j-k_i=n_ij` is an integer, giving exactly
`W_j=r^(-n_ij) W_i` for W=exp(-2 pi i zeta_tilde_2). In the unfolded
node chart this changes the component label j to j-n and preserves
both x_j and y_j. This proves extension at nodes, not only on ruled
open parts. It commutes with the actual closing translation, so descends
to the twelve-cycle. A shift of twelve can include an elliptic
translation after closing and is not asserted to be the identity.
The integer cocycle is exact, rather than merely modulo twelve.

Changing a coherent closing by a scalar gives a principal C* torsor
over the punctured parameter disc. Its triviality by Pic(Delta*)=0
legitimately gives a holomorphic isomorphism of the punctured families.
The proof correctly makes no extension claim for this scalar gauge.

## Finite charts

The finite unit `K s_j^(-12 epsilon_j)` is invariant because the relevant
root orders are three and four. Its holomorphic logarithm is exactly
invariant: an integral difference is constant and vanishes at the root
centre. Since the finite linear factors fix delta, the new local gauge
does not change the finite affine deck action.

The collar difference is

`w_j Pi_c v_j + 12 epsilon_j w_j v delta = w_j Pi_part v_j`.

The sign c=-12v is essential and is used correctly. This remaining
translation is independent of r and acts on the actual semiabelian
group; it therefore extends to both conductor sections and the node
plumbing. Under a change of the root logarithm, the difference between
Pi_part v_j and the actual period Pi_c v_j is an integral fan shift.
The earlier node calculation applies to this shift as well. Thus the
sector comparisons descend through the finite deck actions, and their
cocycle identities are the actual dense-locus identities continued
holomorphically across r=0.

## Cusp and orientation

Using k=-s+12 kappa_0, the retained actual-to-positive-rotating comparison
satisfies the exact identity

`F-sigma = k v delta + G(s) + 6 v delta`.

Its comparison to the ordinary gauge is therefore an r-independent
semiabelian translation G(s) followed by the integral shift r^-6.
The q-branch identity `Delta_s G=b+v delta` cancels the ordinary
coordinate's `-v delta`, leaving precisely the positive fractional
deck +b. The positive r-loop changes the residual translation by the
integral period six delta. These identities verify descent through both
loops.

The orientation now agrees with B.3: the positive q-root generator
has shift +1; its inverse, the clockwise cusp deck generator in B.3's
deck-identification convention, has shift -1. The local component
function `exp(2 pi i(k_i+i_i)/12)` is invariant on overlaps and gives
exactly the Kummer cover y^12=K. This is the corrected sign, not the
earlier negative-q-generator selection superseded in the B.4.18 audit.

## Gluing and limits of the conclusion

All comparisons are isomorphisms on entire preimages of base overlaps,
including their r-central parts. Their exact cocycle therefore gives
a Hausdorff analytic gluing. Properness is local on the target, and
each input model is proper on its stated base open set. Smoothness,
flatness over r and the reduced NC divisor are likewise local. For
r nonzero, the whole target P1 is present and the punctured family is
the prescribed compact family. For r zero the cusp base point is
missing, so properness over the r-disc does not follow. This limitation
is accurately retained in the statement.

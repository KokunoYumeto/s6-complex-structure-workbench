# Independent referee: corrected cusp over the punctured bidisc

## Superseding orientation correction, 19:41 UTC

The local existence/freeness/gauge calculation below remains valid for
either sign, but its original selection of the negative sign as the
retained global marking was wrong. B.3 uses **clockwise** finite root deck
generators with shifts +4 and -3. Its required clockwise cusp generator
has shift -1. The displayed H in B.4.18 rotates the q root **positively**;
it must therefore use **+b,+F**, with shift +1. Its inverse is the required
clockwise generator. AB has corrected the integrated statement and proof.
The correctly typed comparison from the actual affine family is
`zeta -> zeta-sigma+F`. In particular `F_1-sigma_1=mu s/2` is independent
of r; an obstruction computed using F alone does not apply to this map.

Reviewer: boundary_d. Date: 15 November 2026. Reviewed source:
`sections/ab_push_corrected_cusp_overlap_working.md`, with exact certificate
`code/ab_push_corrected_cusp_overlap.py`, its output and JSON. This is a
referee record of the stated partial construction, not a completion claim.

## Conclusion

**PASS at the stated punctured-bidisc scope.** The rotating model has an
explicit holomorphic comparison with the actual family on the two-puncture
overlap. Gluing this model to the prescribed reduced cusp gives a proper
Hausdorff family over the bidisc minus its origin, with smooth total space,
flatness over the degeneration parameter, the required component rotation
on the other axis, and the actual reduced cusp on the punctured cusp axis.
The missing origin is a substantive remaining analytic extension problem.

## Exact affine calculation

Write `gamma=(6 mu,C-s-12t)` and `delta=(0,1)`, where `mu,C` are
single-valued holomorphic functions of `q=exp(2 pi i s)`. For
`b=gamma/12-delta/24`, its twelve successive q-deck translates sum to
`gamma-6 delta`, an actual period. Its r-deck difference is `-delta`.
The proposed function

`f=(mu(s+12t)/2, C(s+12t)/12-(s+12t)^2/24+6t)`

has differences `Delta_s f=b` and `Delta_t f=gamma` exactly. Thus its
translation descends to the required torsor comparison. The r-difference
is a period, rather than zero; this is sufficient and must be retained in
the descent argument. Composing the previously established B.4.9 affine
gauge identifies the actual retained family, including its marking.

The `-delta/24` correction is necessary. In multiplicative coordinates the
twelfth iterate has a phase `exp(2 pi i (0+...+11)/12)=-1` from the q-root
rotation and a second phase `exp(pi i)=-1` from this correction. They cancel.
The first-coordinate iterate is `exp(12 pi i mu)`, the first multiplier of
the actual gamma period. The second-coordinate iterate is its actual unit
times `q r^12`. The certificate checks these rational identities without a
floating-point approximation.

For the desired negative rotation, use `-b` and `-f` with the same positive
rotation of the q-root coordinate. Its valuation shear is the inverse of
the displayed positive shear; its twelfth power is `G2^-1`. It preserves
the same fan. This distinction fixes the sign without changing any of the
properness or smoothness arguments.

## Fan, action, and local quotient

The specified unit-prism triangulation is preserved by the two integral
period shears and by the fractional shear. The height-one r-components
have labels `j mod 12`; the deck generator shifts them by one. At any
point of the r-central divisor at most two adjacent such branches meet,
so no nonidentity cyclic shift can preserve its set of local branches.
This proves freeness there, including over the common base origin.

On the q-central divisor with r nonzero, the bottom cone is a triangle in
one unit square. Its set of second labels lies in `{j,j+1}`. Translation
of these labels by a nonzero element of `Z/12` cannot preserve the set.
This is the explicit local-branch justification for the source's shorter
phrase "nonzero translation of the q-component grid." Off both axes the
root-base action is free. The smooth finite quotient therefore has the
asserted properties. Its q-fibre has multiplicity twelve; it is not the
actual reduced q-cusp, and the working proof correctly says so.

Properness on the root cover uses the already proved compact-core
plumbing and its unfolded toric charts, not the determinants alone.
The determinant checks establish smooth local charts; they do not by
themselves establish properness of an infinite period quotient.

## Two-open gluing and exact remaining gap

The q-nonzero and r-nonzero base open sets cover the punctured bidisc.
Their common inverse image is identified by the explicit holomorphic
translation above. There is no omitted triple-overlap condition. Being a
proper Hausdorff analytic map is local on the target in this situation,
and the two restrictions are proper Hausdorff maps; smoothness and
flatness over r are likewise local. On the r-nonzero open set the model is
the actual prescribed reduced Mumford cusp, not merely an abstract torus
family with matching periods.

The comparison contains quadratic logarithms. The proof supplies no
meromorphic extension of its graph across the origin, no proper analytic
origin fibre, and no global compatibility with the finite-place models.
One cannot invoke graph closure, a toroidal common refinement, or an
unrestricted analytic semistable-reduction theorem without proving their
hypotheses. The multiplicity-twelve q-model cannot simply replace the
reduced actual cusp. The next task is an actual completion of the glued
punctured-bidisc family, not a further verification of these affine
identities.

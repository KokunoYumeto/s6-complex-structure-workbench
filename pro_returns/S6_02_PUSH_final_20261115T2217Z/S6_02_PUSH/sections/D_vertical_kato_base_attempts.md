# Changed-base vertical Kato cap: exact constraints and remaining comparison

Owner: boundary_d. Started 2026-11-15 after checkpoint08 and B.4.26.

The purpose is to test a genuinely vertical cap for the original map `(q,r)`, rather than to repeat the excluded fixed-q Kato plumbing. Near a vertical component one may have `q=r^a h(s)` with `a>0`, where `s` is a direction on an exceptional base curve. The ratio q/r^a is in general meromorphic and its poles lie on further conductor components. It must not be assumed to be a global holomorphic function on a compact component.

## An elementary constraint on a smooth Kato bundle over P1

Suppose a proposed compact vertical threefold has a holomorphic submersion to P1 whose fibres are parabolic Kato surfaces S_n, and suppose their persistent elliptic curves form a smooth relative divisor `E -> P1`. Its normal line in the threefold restricts on each elliptic fibre with degree `-n`, where `n>0`.

Then the elliptic family `E -> P1` is holomorphically a product. Here is a proof that does not assume an origin in advance.

The j-invariant is a holomorphic map from compact P1 to the affine j-line, hence constant. The Jacobian family is therefore isotrivial. Its residual linear automorphism local system is trivial because P1 is simply connected, so the Jacobian is the constant elliptic curve E0. The genus-one family is a torsor with class xi in H1(P1, E0). The exponential sequence of the constant elliptic group,

`0 -> Lambda -> O_P1 -> E0 -> 0`,

gives `H1(P1,E0) = H2(P1,Lambda) = Lambda`, because H1 and H2 of O_P1 vanish. In particular the torsor group has no torsion.

For a torsor of class xi, its relative degree-d Picard space is a torsor of class d xi, with an immaterial sign depending on the translation convention. This follows directly by trivializing over small discs: a change of origin by t translates degree-d divisor classes by d t. The actual normal line of degree `-n` gives a section of that relative Picard torsor. Hence `n xi=0`, and consequently xi=0. An origin section therefore exists and the elliptic family is the product.

The same conclusion follows topologically from the Serre differential of the fibre orientation class: a nonzero-degree line on a principal elliptic bundle forces its Chern vector to be torsion, and H2(P1,Lambda) is free. For n=1 the inverse normal line determines the origin point through the degree-one Picard identification.

**Established consequence:** a simple smooth S_n bundle over the exceptional P1 cannot use its persistent elliptic divisor to carry a nonzero elliptic Chern vector. A singular elliptic divisor, singular fibres of the threefold-to-P1 map, further conductor attachments, or a different vertical component remain possible.

## Exact period data under a changed base

On the actual cusp, the second multiplicative period has the factor `q r^12` times a nonzero holomorphic unit. Substitution `q=r^a s` therefore changes this factor to

`r^(a+12) s` times a nonzero holomorphic unit.

The first degenerating period has the factor `q=r^a s`. Thus along a transversal to a generic exceptional-base point the two Tate valuations are `a` and `a+12`, both positive. This is a maximal rank-two torus degeneration, not a family with only one torus direction degenerating. An internal Kato parameter cannot simply be set equal to s while claiming the original punctured comparison: the actual elliptic Tate multiplier still has the additional r^a factor.

The nonzero exponent `a+12` by itself is **not yet** the Chern class of an elliptic divisor over the exceptional P1. To turn the preceding product constraint into an obstruction one must construct the actual north/south overlap of that divisor from the two-period quotient, retaining the affine origin and all conductor identifications. This comparison has not been supplied. No numerical Chern class is assigned here.

## Why the earlier persistence obstruction does not settle this model

In a genuinely vertical component, every compact rational curve maps to original q=0. The derivative of `(q,r)` along its ordinary deformation space can fail to have rank two. The normal-bundle argument in B.4.23 consequently cannot be used to force that curve into a nearby ordinary q-fibre. Its stated base-map hypothesis was essential.

Likewise B.4.25 concerns a proper family of unblown Hopf surfaces with one multiplier tending to zero and the other to a nonzero contraction. It does not exclude a vertical threefold whose internal fibres have a different relation to the original base, nor does it exclude further conductor components that change those surface fibres.

## Current gap

No compact vertical threefold with the required exact two-period boundary comparison has been constructed. The missing task is the explicit global collar comparison, including the second period and the map to the original bidisc. Normal-line matching, the scalar substitution q=r^a s, and an abstract Kato bundle over P1 do not provide it.

## A different Hopf quotient that is not excluded by B.4.25

Write the two Jacobian multipliers on the dense multiplicative torus as

`g1=(q A, eta^(-1))`, `g2=(eta^6, q r^12 D)`,

where eta=exp(2 pi i mu) and A,D are units. Quotienting first by the combined period g1 g2 gives diagonal Hopf multipliers

`(q A eta^6, q r^12 D eta^(-1))`.

Both vanish along q=r^k s, of orders k and k+12. (The earlier informal message interchanged the two harmless unit factors; this display is their exact product.) Thus this combined-period Hopf quotient lies in a two-eigenvalue degeneration regime and is not ruled out by B.4.25.

It is not a cap. The remaining independent period acts on that compact Hopf surface and need not act properly there. Its two elliptic axes are generally not isomorphic before degeneration, so identifying them as conductor curves is not justified. Completing the entire period action in a toric group model would fall within the logarithmic obstruction already proved. A non-group compactification still needs an explicit, proper two-period gluing.

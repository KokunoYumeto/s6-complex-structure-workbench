# Independent audit of the OS45 primitive lattice and full fundamental-class calculation

Auditor: fourfolds. Scope: the marked OS45/default datum P=2G, Q=8G,
whole-fibre weights (2,0,0,0,0), ordinary clutch e=1, with the specified
Mumford caps. This audit does not determine the separate refined framing
class P.

## Conclusion

The complete proof in `code/maps_weighted_os45_mu_proof.tex` passes.
The essential correction is the literal degree-two core cochain, not merely
its functional on ordinary homology. The full cusp boundary comparison then
retains the coefficient-extension ambiguity. The primitive lattice and
localization inputs in `sections/fourfolds_OS45_cubic.tex` and
`sections/fourfolds_OS45_localization.tex` are consistent with it.

## Integral and finite-coefficient checks

1. The graph-cycle subgroup K is primitive because it is the kernel of an
   integral map. Its retained integral left inverse extends the graph row to
   the complete degree-two chain group. The fibre row is (1,0,0,0,0,0).
   The resulting cochain annihilates every degree-three boundary modulo eight.
   Thus it chooses an actual cohomology class even though the core has
   nonzero Ext(H1,Z/8). The zero fibre degree-three boundaries may be omitted
   from the stored nonzero-boundary matrix without changing this assertion.
2. At the cusp the four basis-loop quadratic prism corrections vanish.
   The actual peripheral graph map gives (0,52,0,148), so both long-strip
   constants are four modulo eight. This checks the constant terms as well
   as the alternating fibre form.
3. The boundary group is the actual split extension Z^3 semidirect L:
   the two short angular loops and theta form the normal Z^3, and the
   commuting long loops give the specified splitting. In total degree two,
   the restriction kernel is an extension of H^1(L;Aff) by H^2(L;k).
   The possible transgression to H^2(L;k) vanishes because of the splitting;
   H^3(L;-) vanishes because L has cohomological dimension two. Restriction
   to the actual long torus splits the left term. This argument is valid
   over Z/8, not only over a field.
4. On the simply connected cusp cover, relative component cochains are all
   functions on the vertex lattice, and the boundary connecting map is the
   three-dimensional space of affine functions. Equivalently, dualizing
   the free-quotient sequence I^2 -> Z[Z^2] -> Z^3 proves the same
   Functions/Aff description over Z/8. A quasiperiodic support descends
   because H^1 of the cover is zero and H^3(L;k)=0. Its choices differ by
   H^2(L;k). The affine differences (-r+4,4), together with long-torus
   value zero, therefore determine and match the whole boundary class.
5. The four other primitive rank-one caps and the ordinary cap have free
   boundary H1. Their fibre specialization surjects onto cap H2. Hence
   annihilating the retained full kernel columns gives equality of the
   entire boundary cohomology class there; no Ext ambiguity remains.
6. The global class has a unit value on the order-eight torsion generator.
   Free homology lifts can be adjusted by that generator to be annihilated
   by the class, giving the stated splitting of H2.

## Cup products and operations

The relative Bockstein calculation establishes the actual index-two
component overlattice, with 2y equal to the odd-component sum. Its
restrictions y|P_(r,s)=(-1)^s(H-E1) determine the integral primitive cubic.
No finite-coefficient division by two is used. The support gives all
component mixed products. The semicfree scalar circle action and its
sixteen fixed curves give the remaining evaluations directly:

- u^3=0 in Z/8;
- P2(u)y=0 in Z/16;
- uy^2=0 in Z/8.

The all-character polynomial identities verify that changing either
global equivariant lift does not change these values. Thomas's integral
lift identity is applied only on the fixed-curve products, where such
integral lifts exist. The resulting coordinates cover every summand of
H6(K(Z^15 plus Z/8,2);Z): the free cubic, 120 order-eight mixed coordinates,
15 order-sixteen Pontryagin-square coordinates, and the pure order-eight
coordinate. Thus this is the full fundamental-class invariant, not only
ordinary triple cup products. The primitive torsion coordinate also
detects the torsion part of y^2, proving y^2=0 integrally.

## Executed verification and layout

Independent replay of `code/maps_weighted_os45_mu.py` exited zero. It
verified the literal core cochain, cycle restriction, degree-three closure,
affine constants, all sixteen wall restrictions, opposite-wall gluing,
the shifted annulus evaluations [[9,24],[0,0]], and every stored primitive
mixed coordinate. Its reduced character representatives give raw
localization integers -1560,208,-32; these have the same required residues
as the unreduced representatives -16632,672,-32 in the independent
fourfolds localization program.

The primitive-cubic program separately verifies all 3375 primitive triples
and all 4096 recovered component triples. The local two-pass TeX build
passed after correcting a literal cases line-break typo; the first failed
build was a typesetting error, not an arithmetic failure. No unresolved
references or overfull boxes remain in that local build.

The refined class P remains outside this audit until the actual odd
middle-dimensional generator, reference framing, and critical-curve
linking have been evaluated. Neither the even regular-torus image nor
even coefficients in a bar-chain expression alone determine that parity.

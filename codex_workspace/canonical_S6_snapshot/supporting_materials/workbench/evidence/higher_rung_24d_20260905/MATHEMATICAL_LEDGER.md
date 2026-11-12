# Higher torus wrap and 24-dimensional comparison — 5 September 2026

The full proofs are in the root `s6_higher_rung_24d_preprint.tex` and the
mechanically adapted workbench module. This ledger records their exact scope.

| Construction or map | Proved content | Remaining scope |
| --- | --- | --- |
| Equal-diagonal positive cone in Herm3(O) | Original cubic with ordered octonion product; explicit radial homeomorphism; compactified pair (B25,S24) | No complex structure or torus degeneration on this boundary is inferred |
| Fl(O) = F4/Spin(8) | Tangent 8v + 8s+ + 8s−; integral cohomology ranks 1,2,2,1; Euler class 6u; six even-dimensional cells | These flag results are established literature, attributed to Mare–Willems |
| Six toric zero-strata → six fixed flags | Explicit equivariant bijection of finite S3-sets | Does not itself define a map on positive-dimensional strata |
| Fourth smash sphere → determinant-boundary sphere | Based homeomorphism after stated choices; degree-one flag collapse maps also given | The flag is not homotopy equivalent to either sphere |
| Peripheral character χ | SL2(Z) → Z/12; values (−1,4,−3) on the displayed cusp and elliptic matrices | Every homomorphism to Z/24 has even image; no reduction-compatible lift of χ |
| Sixfold suspension | π6(S3) → π12(S9), aα ↦ 2aν9, injective | Actual cusp coefficient a=0 by the explicit original-chart framed filling; the universal suspension remains injective |
| Composition Θgχ | M ↦ χ(M)[g]; image order 12/gcd(a,12) | The particular framed fibre coefficient is now zero, so this homomorphism has zero image |
| Diagonal-sum character on the primitive quotient | Factors through the displayed P or Q exactly when N divides 3 | This concerns that character, not all characters of the quotient lattice |
| Euler coefficient reduction | eN = 6uN has order N/gcd(N,6), hence orders 2 and 4 at 12 and 24 | Coefficient change is available for every N; it does not select a modulus |
| p=1201 selector → Herm3(H) | Fifteen projective rays; linear span and Jordan closure exactly Sym2(R), dimension 3 | Full quaternionic Peirce corner has dimension 6; ambient Herm3(H) has dimension 15 |

The higher local torus morphisms and Euler calculation are written in the
draft. A completed global higher torus wrap remains open. The independent
flag, cone, and homotopy constructions do not establish or refute the claimed
global complex S6 construction by themselves.

## Literature and attribution

- A.-L. Mare and M. Willems, *Topology of the octonionic flag manifold*,
  Münster J. Math. 6 (2013), 483–523,
  <https://arxiv.org/abs/0809.4318>. The draft cites the ring, cells,
  stabilizer and restricted-root calculations at their source locations.
- A. Hatcher, *Spectral Sequences in Algebraic Topology*, Chapter 5,
  <https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf>, for the explicit
  unstable suspension calculation; *Algebraic Topology*, p. 339, for the
  low-dimensional groups used in the smash nullity argument.
- H. Toda, *Composition Methods in Homotopy Groups of Spheres* (1962),
  Proposition 3.1, for the smash/suspension composition identity.
- The remaining geometry, root-system and modular-group citations appear
  directly with the propositions using them in the full draft.

Known human results, finite exact checks, new comparison maps and unresolved
invariants are distinguished in the full text. A successful TeX build verifies
readability and source completeness; it is not a substitute for those proofs.

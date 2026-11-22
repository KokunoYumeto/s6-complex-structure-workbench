# Paper I — preread derivation of push:src:B.4.3 (tag 030Z)

Access boundary: the target statement and its cited statement push:src:B.4.33 were read; the target derivation in the proof compendium has not been opened. This derivation does not use the nonexistence assertion B.4.33 to make the result vacuous. Nishiguchi II Theorem 1.4 (preprint p.7, PDF p.9) and Example 2.1 (p.13, PDF p.15), and Istrati–Otiman–Pontecorvo–Ruggiero Theorem 7.1 (printed p.1373, PDF p.28) were opened from their institutional/journal primary PDFs. Their role is comparison with actual analytic degenerations, not the proof of this six-sphere obstruction.

## Derivation before target proof

1. Write g for the map in the target statement and D for its reduced normal-crossings fibre. Since the total space is smooth and the base is a smooth disc, its local structure sheaf is torsion-free over the one-variable base ring, hence flat. Locally along a point belonging to r branches, reducedness gives a semistable equation z_1 ... z_r=s up to a nowhere-zero factor, absorbed in one coordinate.

2. The local nearby fibre of z_1 ... z_r=s is connected (it retracts to a real (r−1)-torus). Consequently the degree-zero nearby-cycle sheaf is the constant sheaf C_D. The degree-one edge map of the nearby-cycle spectral sequence therefore injects H^1(D;C) into H^1(Z_s;C). Equivalently the semistable collapse has connected torus fibres and the low-degree Leray sequence gives the same injection. The nearby six-sphere has H^1=0, so H^1(D;C)=0. This is a topological local-to-global argument; no Kähler hypothesis is used.

3. Every compact complex threefold with the cohomology of S^6 has chi(O)=integral c_1 c_2/24=0 by Hirzebruch–Riemann–Roch, since H^2 and H^4 vanish. A holomorphic volume form is d-closed and its de Rham class lies in H^3=0; Stokes applied to its product with its conjugate rules out a nonzero such form. Thus h^3(O)=h^0(K)=0, h^0(O)=1, and 0=1−h^1(O)+h^2(O), so h^1(O)>=1. Upper semicontinuity for the proper flat family gives h^1(D,O_D)>=1. One may instead use the family's already stated h^1(O)=1; the argument here avoids any dependency on the later deformation calculation.

4. The natural comparison H^1(D;C) -> H^1(D,O_D) has zero source and a nonzero target, hence is not surjective. To verify the asserted obstruction on the central strata, use the normalization semisimplicial resolution of D. In total degree one, the structure-sheaf double complex consists of functions on pairwise branch intersections and (0,1)-forms on normalized components. On a compact complex manifold satisfying the ddbar lemma, every (0,1)-class has a d-closed representative. Such a representative is unique: a d-closed form dbar f has ddbar f=0, so f is pluriharmonic and is constant on each compact connected component. Restriction of these representatives to a closed stratum commutes with the canonical map to H^1(O). A compatible collection of classes therefore restricts to identical actual d-closed forms; the degree-one double-complex cocycle lifts to the constant/de Rham resolution. Functions in degree zero are constants on compact connected strata. Thus the natural H^1(C)->H^1(O) map is surjective when the closed smooth strata satisfy ddbar. This contradicts step 4's first sentence and proves the stated failure for at least one nonempty closed stratum.

5. For a proper algebraic normal-crossings variety, the normalized branch strata are smooth proper algebraic varieties. Their analytic spaces satisfy the ddbar lemma; their semisimplicial resolution gives the same surjectivity, including ordinary normal crossings with global self-intersections. This excludes the stated algebraic realization. In the simple-normal-crossings case, Kähler components have Kähler closed strata by restriction of a Kähler form. Smooth compact Moishezon components and their closed smooth strata belong to Fujiki class C and satisfy ddbar. These are the two advertised consequences.

6. The argument after a finite cover w=s^N uses only the assumed local semistable equation, the nearby fibre's six-sphere topology, and properness/flatness. The integer N does not enter any calculation, so no new conclusion is needed for individual N.

## Computation scope

The only numerical input derived here is chi(O)=0 and h^1=h^2+1; it is exact symbolic degree bookkeeping. There is no numerical approximation or external program in this derivation. A proof comparison will determine whether the printed derivation contains further computations requiring fresh implementation.

## Primary-source scope

Nishiguchi's cited theorem is explicitly about semistable K3 degenerations and permits a Hopf or (CB)-surface component; Example 2.1 glues an elliptic Hopf surface to an elliptic K3 surface along an elliptic curve and smooths it. Istrati et al. Theorem 7.1 gives a proper flat toric-Kato degeneration with smooth total space. These exact statements illustrate why assumptions on central strata require proof. They are not imported as six-sphere degeneration results.

## Remaining source-validation boundary

The general HRR, nearby-cycle edge sequence and ddbar facts used above are standard inputs reconstructed here at the required low degree. Their book/article locators have not yet been freshly opened in this run; this note certifies the derivation, not a fresh primary-source audit of those general results. The printed target proof remains unopened at this save.

Saved UTC: 2026-11-21T00:49:42.925918+00:00

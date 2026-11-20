# Completed comparison with the receiving saved arrays

## Chronology and exact inputs

The fresh derivation and computation were frozen at 2026-11-20T00:08:03.628225+00:00. The full receiving proof was released at 00:08:31.417336 UTC. Its complete printed-proof comparison was saved at 00:11:13.501306 UTC, before any receiving program or output was read.

The first receiving saved-output read took place at 00:13:00.891520 UTC. The three files read were the named global reconstruction JSON, its saved-output verification JSON, and the named cusp reconstruction JSON. Their SHA256 hashes are respectively:

* `cdb9045eca04914bfa917176c371ba1caa33a969e784d15e5288dbff7e6b920e`
* `3087e976b6272b19fb121d0e25a83a87f7a077edd20427ff338ef140b373ca5a`
* `886aef4e78e60c71f445c7b9d2f26a7bd8af2703d4c5762d48b6faf6c5cfe47a`

No receiving reconstruction or verification program was imported. The post-freeze comparison program imports only `derive_chain.py`, which was frozen before the receiving proof release, and reads the three receiving JSON files as data.

## The exact chain isomorphism

All complement differentials, cusp-boundary differentials, and maps `j_Y` in the receiving arrays agree entrywise with the fresh reconstruction. The receiving cusp matrices also satisfy the literal marking formula

\[
\kappa_k^{\rm orig}=\kappa_k^{(a,b)}\bigwedge^k S^{-1}
\]

with the `S` displayed in P1.1.

Let `K_k` denote the fresh collapse and `K'_k` the receiving collapse, both in the original lattice coordinates. The comparison constructs integral matrices `A_k` by applying `K'_k` to the fresh Smith quotient section. At degree four it appends the receiving fourth coordinate vector `e_4`, whose pairing with `psi` is one. Exact multiplication verifies

\[
A_k K_k=K'_k,
\qquad A_k^{-1}\in\operatorname{Mat}(\mathbb Z).
\]

Their determinants in degrees zero through six are

\[
(1,-1,1,-1,-1,1,-1).
\]

All the literal matrices and inverses are saved in `receiving_chain_adapter.json`.

Write `r_fresh` for the fresh Smith cocycle and `r_rec` for the printed receiving cocycle. The exact difference is

\[
r_{\rm rec}-r_{\rm fresh}=h\,d_{B,4},
\qquad
h=-e_{11}^{t}+e_{12}^{t}+2e_{13}^{t}.
\tag{3.1}
\]

Here the row `h` is in `B_3=L_3 direct-sum L_2`, in the original lexicographic exterior bases, with **one-based** coordinate indices. Both cocycles evaluate oddly on the fresh factor-two Smith generator; the difference (3.1) is an actual integral coboundary, not just zero after rationalization.

The receiving saved arrays use the plus cusp map, whereas the frozen fresh complex uses the minus cusp map. Define `Q_k` on the ordered full groups `Y_k direct-sum C_k direct-sum B_(k-1)` as identity on `Y` and `B`, and as `-A_k` on `C`. In global degree four add the off-diagonal block

\[
-e_4 h:B_3\longrightarrow C_4.
\]

The inverse has cap block `-A_k^{-1}` and, in degree four, off-diagonal block `-A_4^{-1}e_4h`. The comparison program checks both inverse products in every degree and all eight exact equations

\[
D_{{\rm rec},k}\,Q_k=Q_{k-1}\,D_{{\rm fresh},k}.
\tag{3.2}
\]

These equations identify the complete integral chain complexes. In particular the fresh cycle-and-boundary computation transfers to the receiving arrays through an explicit integral isomorphism.

## Receiving auxiliary maps checked

The same comparison verifies the following data against the actual saved cycles and projections:

1. The degree-four gluing matrix formed from the receiving boundary free-cycle basis and complement homology projection.
2. Its full Smith identity, both unimodular basis changes, rank eighteen, and eighteen unit image factors.
3. The stated last-four-row cokernel projection and the exact swap of its first and fourth rows.
4. The cap block of that adapted cokernel projection, which is three zero rows followed by `psi`.
5. The literal nine-column basis `K=(e_i-psi_i e_4)_(i!=4)`, its unimodular splitting with `e_4`, and the unimodular adapter from the receiving Smith kernel basis.
6. The identities `j_4 W=(0,K)`, `X=HB_free W`, `d_B X=0`, `d_Y T=j_Y X`, and `f_0 X=K`.
7. The identities `rX=0`, `r d_(B,5)=0`, and `2r=t d_(B,4)`.
8. For each of the nine literal kernel columns, the square-zero identity for `(Xv)r`, its chain-map equations, and the complement chain homotopy `(Tv)r`.

The saved report contains 140 exact checks, all passing. Thus the comparison includes the specific maps used to absorb the kernel component of the secondary vector; it does not rely on matching Betti numbers.

## Three receiving-text guards

The complete printed proof was mathematically strengthened or corrected in three narrow places proposed to the parent, who owns shared TeX:

* `receiving_guards_08.json`, first guard: insert the explicit degree-six invariant-subtorus, edge-coordinate, and fibre-coordinate calculation after receiving item 4.
* The second guard in that file: change the literal `S` locator from P1.7 to P1.1.
* `receiving_convention_guard_08.json`: state that the exported global arrays use the plus cusp convention. The old receiving sentence described those arrays as using the minus convention. Entrywise checks of every nonzero cusp block, in target degrees zero through six, establish the plus convention. Multiplication by `-I` on the cap gives the exact comparison to the minus cone convention.

The volume-coordinate tightening is recorded separately in `AFTER_READING_02.md`. It leaves the frozen document untouched and avoids an unnecessary assertion about a basis of the entire graph homology group. The guard supplied to the parent contains the narrowed exact argument.

## Result of the comparison

The frozen derivation, its exact integral fillers, the local relative-duality argument, the complete receiving proof, and the chain isomorphism (3.2) together account for the geometric gluing, the secondary factor-two term, every full differential, and the integral homology quotient. They establish the displayed ranks and

\[
H_0=H_8=\mathbb Z,\qquad H_4=\mathbb Z^4,
\qquad H_k=0\quad(k=1,2,3,5,6,7).
\]

No global Poincare-duality conclusion or P1.12 global homology conclusion is used in this derivation. The chronology remains a fresh target-proof derivation from admitted inputs followed by a receiving-proof comparison; the expected answer and the input P1.12 conclusion were already exposed and have been recorded as such throughout.

# Paper V: complete marked cusp and global integral calculation

## Result and exact scope

The current mathematical proof gates of P1.10, P1.11, P1.12 and P1.19 are closed at their stated dependencies. In particular, P1.19 now has a complete freshly reconstructed global integral complex and a separate verification of its saved matrices. Its conclusion is

\[
H_0(M;\mathbb Z)=H_8(M;\mathbb Z)=\mathbb Z,
\qquad H_4(M;\mathbb Z)=\mathbb Z^4,
\]

with all other integral homology groups zero. The global calculation does not use the global duality conclusion of P1.12. Its geometric identification uses the actual cusp boundary map, the local relative cap-product isomorphism, and the explicit integral chain changes described below.

The new files reconstruct the displayed mathematical maps. They are not a replay of the missing original programs. The old execution records remain historical evidence at their recorded scopes; their absent implementations have not been represented by newly invented files under the old names.

Root owns integration of the twenty proposed P1.11/P1.12/P1.19 guards and the subsequent rendered-page checks. This report makes no new layout or whole-row completion claim. For P1.19, the current finite reconstruction and receiving review are after proof exposure. A fully documented independent derivation before receiving its entire proof is not supplied by this branch or by the retained P1.19 records examined here. This methodological gate is separate from the now closed mathematical and reproducible-computation gates.

## Exposure and retained independent routes

The initial V packet recorded incidental exposure to the end of P1.19. I then read P1.11's complete nine-step proof before implementing its new cusp certificate. I read P1.12's complete ten-step proof and P1.19's complete thirteen-step proof before implementing the new global complex. During the checkpoint freeze I reread those proofs and read all three steps of P1.10. No new whole before-proof event is claimed for those readings or for the resulting programs.

The retained evidence supplies the following distinct routes, without turning an import into a new check:

* P1.10: `ce:64a9c12e7765a81aca60` records the complete period, finite logarithmic attachment, properness, cusp fundamental-group, van Kampen and Euler derivation before the printed proof. `ce:c95d917129d51f23482c` records its separate exact final relation matrix.
* P1.11: the received aggregate explicitly combines separately frozen derivations of unit removal, Voronoi geometry, actual common-face moment maps, logarithmic collapse, spectral-sequence support, primitive unit minors and the marked collapse. The exact scopes are retained in `ce:3377110f4531f3afafaf`, `ce:34eae7ae19c5e740f1b0`, `ce:5ce089f9d77d06f64538`, `ce:5cb3386eafd3a5405687`, `ce:77ae817487ffc403deee` and `ce:abf368e6bef25cddb035`. They are an aggregate of bounded derivations, not one person's wholly unexposed reconstruction.
* P1.12: `ce:ef69db3392bc6a6db8f0` records the complete complement/Mayer–Vietoris derivation before its printed proof; `ce:394a72ff6f057a0d8aa3` records 444 exact prereading checks. The marked collar and the extra mapping-space/duality routes retain their separate frozen scopes, notably `ce:447030655cd2a291f172`, `ce:72ea893786a310e8e3f5` and `ce:5e164f27d37f61a33ac8`.
* P1.19: `ce:f05095a9c475d7f4cf47` records a full receiving review, and `ce:f3cddd879c44451e78ac` records earlier complete program executions. Neither is redescribed as a before-receiving whole derivation.

Three older events labelled P1.10, P1.11 and P1.12 (`ce:a984ed66ddfa587d244b`, `ce:7f02243183c0758fc56b`, `ce:3ce1d2827a4a5ebd6840`) describe characteristic-number and oriented-diffeomorphism calculations. Their text is preserved, but they are not used here as evidence for the present P1.10 construction, P1.11 cusp homology or P1.12 integral gluing gates. No historical event identity was silently changed.

## Fresh executed programs

| Program | Final result | Scope |
|---|---:|---|
| `reconstruct_V_cusp_06.py` | 186 assertions, PASS | All 26 periodic Kuhn simplex classes, 74 incidences, primitive angular quotients, integral spectral-sequence groups, marked PD/AW collapse, monodromy annihilation and primitive images. Previously recorded in CP06. |
| `independent_V_topology_inputs_07.py` | 33 assertions, PASS | Actual finite primitive splits, both printed signed-permutation conjugators and cycle types, finite affine freeness, common coinvariant quotient, the exact cusp S map, and determinant −1 of the van Kampen presentation. |
| `reconstruct_V_global_06.py` | 989 assertions, PASS; 278.796489 s | Every complement, finite-cap, cusp-boundary and corrected global differential, actual j4 lifts, torsion cocycle and full incoming Smith calculations. |
| `verify_V_global_saved_07.py` | 914 assertions, PASS; 91.259443 s | Independent saved-matrix products and rank witnesses, newly reconstructed low-degree homology/kernel bases, exact j4 cokernel and kernel adapters, both local relative H4 groups and the unused even global diagnostic. |

The verifier's first attempt stopped on a Python `BlockMatrix` row-shape error before a mathematical comparison. That source and stdout are preserved as `verify_V_global_saved_07_attempt01.*`. The subsequent successful 750-check and 756-check versions, their JSON and stdout are also preserved. The final 914-check version adds the literal printed kernel-basis adapter, relative-cap homology and unused diagnostic. These versions are not represented as independent mathematical proof routes merely because they have different assertion totals.


The execution-session runtime was replaced while the first global command was outstanding. After inspecting its then-empty output, the command was issued again; both executions later reported PASS989. The first observed stdout gave 271.229945 seconds. The final saved JSON and matching stdout give 278.796489 seconds and UTC 23:12:25.037936. The saved verifier uses the final JSON SHA cdb9045eca04914bfa917176c371ba1caa33a969e784d15e5288dbff7e6b920e, which is recorded explicitly in its own output. The earlier observed completion is retained in V_global_execution_recovery_07.json; only one fresh global reconstruction event is counted. This timing correction changes no matrix, assertion, theorem scope or event count.

## Actual P1.10 and P1.12 maps

P1.10's finite logarithmic attachment is the actual translation by the negative logarithm times the invariant point section. Its angular change cancels the affine translation with the printed sign. The meridian relation is therefore (g_i^{m_i}=v_i). Killing (g_1g_2) makes the two actions inverse; their orders divide both 5 and 4, so the surviving action is trivial. The common fibre coinvariant is the primitive first-coordinate quotient. The remaining relation matrix has determinant −1, as freshly verified. Compactness and the complex orientation are those of the already constructed local family; the Euler contribution is the six Kuhn vertices/tetrahedra counted by P1.9.

For P1.12, the actual evaluation inverse and its real frame covariance identify the marked smooth torus bundle. The finite collar translation has the stated inverse and equivariant interpolation. On the graph, the cusp suspension maps by

\[
x\longmapsto(-W_2W_0x,-W_0x),
\]

whose differential is exactly ((W_0-I)x). The finite caps use the actual unimodular split (P_i=(\varepsilon_i v_i,e_1,\ldots,e_5)), the displayed signed-permutation conjugators and the norm sum on the invariant fibre circle. The fresh global program constructs all these chain maps and their double mapping cone.

The verifier supplies the actual boundary free-cycle bases, complement homology projections and vertical representatives of every free kernel generator in degrees 2 and 3. It separately supplies the order-two boundary cycle in degree 3; that cycle lies in the fibre and collapses to zero. The degree-one joint matrix agrees literally with the old printed matrix. The degree-two and degree-three collapse matrices use new actual bases, so the guards replace their literal entries. Their determinants are both +1. No equality to an unprovided historical basis is asserted.

These exact maps give the low-degree Mayer–Vietoris isomorphisms and surjection used by the receiving proof. Hurewicz, global duality, the integral universal coefficient injection and Euler number then complete P1.12, as its last two steps state. This route does not assume the value of the higher-degree cusp suspension chain correction.

## P1.19: geometric map and integral correction

The actual pure toric retraction is ((b,a,\theta)\mapsto[b,a+\theta(b-v)]) over each dual cell. Vertex changes lie in the collapsed angular lattice, period translations change both b and v, and the top and bottom match the actual shear. The bounded-unit deformation preserves this map up to the specified marked homotopy.

The exterior derivation (D b_i=a_i), (D a_i=0), and its adjoint give the stated base-degree bound on invariant cycles. The filtered product-cell construction supplies integral suspension lifts with that base bound. The lifted radial dual-cell retractions preserve the angular coordinate and agree under the further quotient maps on faces. The P1.11 support table then makes every suspension image zero in cusp homology. On fibre classes the map is the actual marked collapse.

The new cusp output is in the ordered ((a,b)) basis. The global program applies the literal (\bigwedge^kS^{-1}) change to the original lattice. The target bases are the newly reconstructed integral cusp bases, not renamed old export bases.

In those target coordinates the primitive functional is

\[
\psi=(1,-1,1,1,-1,-1,1,0,0,0),\qquad e=e_4.
\]

The exact degree-four boundary cocycle, in lexicographically ordered

\[
B_{0,4}=\bigwedge^4\Lambda\oplus\bigwedge^3\Lambda,
\]

is

\[
r=e_{29}^{t}+e_{30}^{t}+e_{31}^{t}
  -e_{32}^{t}-e_{33}^{t}-e_{34}^{t}+e_{35}^{t}.
\]

The exported integral row t satisfies (2r=t d_4); also (r d_5=0). A rank increase of the augmented coboundary matrix over (\mathbb F_2) proves that r is not an integral coboundary. Thus it represents the actual order-two cohomology class, beyond merely satisfying a rational relation.

The direct j4 reconstruction has rank 18 and primitive image in a rank-22 target. Its exported Smith cokernel projection, followed by the explicit interchange of its first and fourth rows, sends the cusp summand to the fourth-coordinate row \(\psi\). The verifier computes the exact 9-by-9 unimodular adapter from its Smith kernel basis to the literal columns (K=(e_i-\psi_i e_4)_{i\ne4}). In this printed basis it exports W, X and T and verifies

\[
j_4W=(0,K)^t,\quad d_{B,4}X=0,\quad
d_YT=j_YX,\quad f_0X=K,\quad rX=0.
\]

These equalities give the actual square-zero chain automorphism (I+(Xv)r), inverse (I-(Xv)r), and complement homotopy ((Tv)r). The even e4 correction is removed by the integral homotopy (e_4t). This is the displayed chain equivalence reducing every allowed secondary vector to (e_4r); it is stronger than a comparison of ranks.

The local relative cap-product source was freshly opened in the original author PDF: Hatcher, *Algebraic Topology*, Theorem 3.43, printed p.254, <https://pi.math.cornell.edu/~hatcher/AT/AT.pdf> (retrieved references `turn411058655view0`/`turn411058655view1`). For the actual compact complex-oriented cusp cap, its retraction pullback followed by cap product with its relative fundamental class is the source's isomorphism for n=8, k=4, integral coefficients, empty A and full-boundary B. The free cusp group forces the odd extension. The fresh verifier computes relative H4 as Z10 plus Z/2 for zero correction and Z10 for the odd correction, exactly matching this application. No global duality conclusion is used at this step.

Finally, the global differential ranks are (3,23,64,98,98,58,21,2). The saved verifier checks an integral inverse for every outgoing basis matrix, verifies its entire kernel, obtains the complementary rank by exact witnesses modulo 1009, and checks each incoming matrix together with both integral Smith inverses. Every nonzero incoming invariant factor is one. It also recomputes the unused even global diagnostic; that case has the same global homology while retaining the wrong local relative torsion. This diagnostic is not used to identify the actual cap.

## Delivery and remaining gates

`V_P112_P119_guarded_patches_07.json` contains sixteen exact guarded replacements. The four earlier `V_P111_guarded_patches_06.json` replacements connect the cusp proof to its actual new implementation. All source files remain root-owned and unchanged by this branch.

The new canonical assessments distinguish mathematical closure, retained independent routes, integration, current rendered QA and the specific unresolved P1.19 before-receiving methodological gate. They leave format, layout and completion unset. The prior source comparisons remain bounded to the opened sources; no worldwide absence or construction-priority assertion is added.

Actor: GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited from root and not separately exposed.

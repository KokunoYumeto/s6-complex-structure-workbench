# Receiving-proof comparison, before reading its programs or outputs

## Chronology

`BEFORE_READING.md` was frozen at 2026-11-20T00:08:03.628225+00:00, SHA256 `79f49d32b346ea41c5a327a4ce792f836e9d8d34ea22f317e291534eb0daed8d`. The parent then released the entire receiving statement and proof as `P119_receiving_proof_08.tex`, with release receipt `P119_receiving_release_08.json`, released 2026-11-20T00:08:31.417336+00:00. I have now read all 297 lines of that packet. Its SHA256 is `71f508df2eb506a0de09a8a7e2d374200800e32a54392fc1840706aeff824379`.

At this stage I have not read the receiving reconstruction program, its saved arrays, or its saved-output verifier. The comparison below concerns every printed proof item. The later numerical/basis comparison will be recorded separately.

## Item-by-item comparison

| Receiving item | Comparison with the frozen derivation | Exact remaining check |
|---:|:---|:---|
| 1 | Same admitted actual complement and finite-cap models. | None beyond those admitted inputs. |
| 2 | Formula (1.19.1) is the same actual toric boundary forgetful map as frozen (4.3), with the base coordinate rescaled by `G`. Vertex, deck, and endpoint checks agree. | None. |
| 3 | The derivation `D`, its adjoint `E`, and the identity `[D,E]=(q-p)I` correctly force every invariant homogeneous component to have base degree at most half its total degree. Distinct homogeneous source components have distinct target components under `D`, so no cancellation is hidden in that step. | None. |
| 4 | The filtration `F_p=T_A^3 times (T_B^3)^(p)` has zero cellular differential, and its homology inclusion is injective. The shear preserves the base pointwise. The asserted invariant-cycle suspension can therefore be constructed inside its mapping torus, with closing chain in `F_p`. | The final sentence asserts compatibility with P1.12's marked product-cell model without spelling out the degree-six fibre coordinate. The explicit guard below supplies that coordinate. |
| 5 | The radial deformation lifts through the quotient because its boundary map is the further quotient by a larger isotropy subtorus. The boundary is fixed. The starting base skeleton is a finite polyhedron; radial maps on compact subsets avoiding their centres preserve its dimension, so centres can be chosen successively. | A short clarification that the starting skeleton is polyhedral makes the dimension assertion explicit. |
| 6 | The associated graded support gives zero filtration subgroup in the stated total degree, so the suspension image vanishes. The frozen derivation needed only the degree-one and degree-six geometric zero values; it removed the other values through verified complement fillers. Thus it also supplies a route avoiding reliance on a simultaneous marking of every intermediate suspension lift. | The printed sentence calls `S` the matrix from P1.7, while its literal display is in P1.1. The matrix itself must be checked in the arrays; this is a reference correction, not a different lattice map. |
| 7 | Same Smith-pair classification as frozen Section 3. The only residual map after homology is fixed is the image of the upper generator of the degree-4-to-degree-3 factor-2 pair, modulo twice the target. | Check the literal cocycle/basis adapter in the saved arrays. |
| 8 | The functional `psi` is an explicit coordinate version of the frozen quotient by the primitive collapse image. The zero-term relative cone has the factor `(0,-2)` and the order-two torsion stated in the text. | Verify `psi*kappa_4=0`, primitivity, and relative arrays. |
| 9 | The local use of Hatcher Theorem 3.43 has exactly the correct dimension, subsets, coefficient ring, retraction, and cap-product map. The nonsplit parity is the same `gcd(a,2)=1` constraint in frozen Section 5. | None. |
| 10 | The plus/minus convention is related by the explicit target automorphism `-I` on the cap. The claimed cokernel map reduces to the same quotient functional used in the frozen proof. | Check the exported Smith basis, last-four-row swap, and literal cap block. Matching ranks alone will not establish this. |
| 11 | `K=(e_i-psi_i e_4)_(i!=4)` is an integral kernel basis because `psi e_4=1`. The `W,X,T` identities perform the same role as the frozen primitive fibre lifts and exact complement fillers. | Verify all three actual maps and their products. |
| 12 | `rX=0` makes the displayed rank-one endomorphism square-zero; `rd_5=0` and `d_4X=0` make it a chain map. The complement homotopy is exactly `(Tv)r`. The equation `2r=t d_4` removes an even multiple through the integral homotopy with the corresponding integer coefficient times `e_4 t`. These are actual cone equivalences. | Verify literal `r`, `t`, `X`, and `T`, and then construct the basis adapter from the fresh canonical Smith cocycle to this `r`. |
| 13 | Differential ranks and all integral homology groups agree with the fresh computation. The receiving proof correctly keeps the local parity argument even though its diagnostic even case happens to give the same global homology. | Compare full matrices through an explicit integral chain isomorphism; verify the saved maps, not only the ranks. |

## Minimal exact guard for the marked degree-six suspension

The printed proof already constructs a filtered suspension lift and states compatibility with P1.12. It does not explicitly identify the possible added fibre top class in that assertion. The following paragraph supplies the missing coordinate calculation and can be inserted after the last sentence of receiving item 4:

> In degree six this compatibility has a direct marked check. The integral kernel of `wedge^5 M_0-I` is generated by `x_j=a_1 wedge a_2 wedge a_3 wedge b_1 wedge ... wedge b_j-hat wedge ... wedge b_3`. Each is the top class of the invariant subtorus `b_j=0`. Its mapping torus has suspension coordinate `x_j`. Along the two inverse edge cylinders its fibre support is the flatly transported five-dimensional subtorus, so its edge coordinates are exactly `-W_2W_0x_j` and `-W_0x_j`. The flat integral fibre-volume coordinate is zero: the form `dx_0 wedge ... wedge dx_5` takes value one on the marked fibre top cell, zero on an edge times a five-cell, and integrates to zero on this transported mapping torus. These coordinates identify its class with `(0,x_j)` in the boundary model and with the image prescribed by (1.12.3), including the fibre coordinate. Formula (1.19.1) maps this cycle over the two-dimensional subtorus `b_j=0`, with angular fibres of dimension at most three; its image therefore has zero sixth homology class.

The underlying integral assertion can also be expressed without differential-form terminology. The graph Wang exact sequence in degree six has its fibre `Z` summand and the edge invariant lattice as quotient. Mapping tori of invariant five-subtori give integral lifts of a basis of the quotient. The volume functional takes values one and zero on those respective generators; thus it is an integral coordinate functional, not merely a rational normalization.

For degrees 2 through 5, the fresh matrices `F_k` already satisfy `d_Y F_k=J_k` on every fibre chain. Any change of a suspension lift by a fibre cycle changes the global attaching map by the explicit homotopy `F_k` applied to that cycle. Degree one is fixed by the actual section disk. Thus the frozen proof supplies explicit adapters covering every degree even when one uses the receiving proof's alternate filtered lifts.

## Adapter to be checked next

Let `K_k^fresh` be the frozen collapse matrix, built from the bottom rows of the fresh Smith `U_k`, and let `Q_k^fresh` be the corresponding columns of `U_k^{-1}`. For a receiving collapse matrix `K_k^rec`, set the first `r_k` columns of

`A_k = K_k^rec Q_k^fresh`.

In degree four append the receiving fourth coordinate vector `e_4`; in every other degree this already gives a square matrix. The identities to verify are `A_k K_k^fresh=K_k^rec` and `det A_k=+/-1`.

After this target basis change, the two secondary rows are the fresh Smith cocycle `r_fresh=V_3^{-1}[10,:]` and the receiving cocycle `r`. Their difference has an integral primitive `h` with `h d_(B,4)=r-r_fresh`: in Smith coordinates divide the unit-slot differences by their unit factors and the factor-2-slot difference by two. The latter is even because both cocycles represent the nonzero element of the same order-two cohomology group. The full global adapter is the identity on `Y` and the boundary summand, `A_k` on the cap summand, and in global degree four the additional cap-from-boundary block `+e_4 h`. Direct multiplication with the two full differentials will establish the actual matrix comparison.

This note records the full printed-proof comparison before the first receiving-output read. It does not promote the row merely because the homology tables agree.

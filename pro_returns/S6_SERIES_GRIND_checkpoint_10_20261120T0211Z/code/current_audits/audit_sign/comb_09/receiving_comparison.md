# Actual twelve-tooth comb kernel: full receiving comparison

## Verdict and exact scope

**PASS for the constructed nonempty open family of actual twelve-tooth smoothings.** The full receiving argument, together with the explicit node-sufficiency and frame-transport paragraphs below, proves

\[
K_{12}\simeq\mathcal O_{\mathbb P^1}(-8)
 \oplus\mathcal O_{\mathbb P^1}(-9)^{\oplus2},\qquad e_{12}=0.
\]

Thus \(h^0(K_{12})=0\), \(h^1(K_{12})=23\), and the existing actual Hodge formula gives \(h^{1,1}=49\), \(h^{1,2}=48\) on this family. Every geometric map needed to reach the actual smooth kernel has been compared: the finite-character root lift, the determinant-valued cup, the flat total-space kernel, the moving conic frame, the attainable two-jet quotient, tooth collapse, and the common twisting line in the smoothing family. No unresolved mathematical input remains in this scoped construction.

This receipt concerns an open set of actual admissible conics and their actual embedded smoothings. Its construction does not specify a numerical solution of the nonlinear smoothing equations. The splitting of arbitrary special members and the complete classification for other tooth counts have not been derived here. The current broad `inv:E2.3` row needs a scoped publication revision and a separate proved result; this receipt makes no canonical status change.

Author: GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited and not separately exposed. This is a same-model-family receiving comparison.

## Reading order and immutable inputs

Before the isolated calculation I had read the existing E15/E2.2/E2.3 material and the earlier dual-cup adapter. I had also received the route cues \(xZ_x-yZ_y\) and the conic columns \((I+yA;yB)\). My complete new derivation was frozen at **2026-11-20 01:33:18.610281 UTC**, before opening the root target, its family-lift supplement, or its certificate. The freeze records that exact prior exposure; this is not a new blind reproof of the old entire E2.3 row.

| Document | SHA-256 | Actual scope read |
|---|---|---|
| `independent_two_jet_derivation.md` | `be3ac29edb8e43eb5005ff516e6d7d2442e245d17f2c5d5a53b8004f1b1d0c0d` | Complete frozen independent derivation; 25,054 bytes |
| `freeze.json` | `af3d4ef98502fa8613228a63af6a341272b0016d01d9d8a107dbe9d05aa0a417` | Exact order and exposure record |
| Root `twelve_tooth_kernel_derivation.md` | `4a3cfbc0e5548c28e7246034bd3822241c4a03482b160fc838e67629e733a9d7` | Complete seven sections and source paragraph, read in two bounded chunks after the freeze |
| Root `root_family_lift_supplement.md` | `3f7aa22c370035c6602d3727bae1031aa5c73c2ad03d553600dc01afce9d630e` | Complete finite-point, cusp and family-line comparison |
| Root `exact_node_and_jets.py` | `8cb104e8dbc11b072670b3a0cf404be9bbfcb2a79828ad1d7766abf9661f1cb3` | All 170 lines, read after the target; not executed by this reviewer |
| Root `exact_node_and_jets.json` | `2de5969987d0045005e507d9b489a07c33538459441087e670be2b60c4785239` | All 53 assertion names/outcomes extracted; complete saved Hermite arrays reconstructed and compared by the new receiving program |

A previous oversized tool output containing the root target was entirely truncated before this comparison. It supplies no reading credit. A later oversized JSON output was partly truncated; the subsequent structured extraction and complete programmatic comparison identify the precise data actually checked.

## 1. Seed kernel and conventions

Root writes the tensor matrix as \(\delta_0=\left(\begin{smallmatrix}0&by\\cy&dx\end{smallmatrix}\right)\). Its row-\(G\), column-\(F\) derivative matrix is the transpose. This agrees with my frozen matrix \(T_0=\left(\begin{smallmatrix}0&ay\\by&cx\end{smallmatrix}\right)\) under the literal coefficient assignment \(a=c_{\rm root}\), \(b=b_{\rm root}\), \(c=d_{\rm root}\). Both yield the cup row \((b_{\rm root}y,0,d_{\rm root}x,-c_{\rm root}y)\) in the stated tensor order.

The weight-five entry vanishes, the two weight-four entries are multiples of \(y\), and the weight-three entry is a multiple of \(x\). The actual invertible logarithmic residue forces the two weight-four coefficients to be nonzero. No nonzero assertion is needed for the weight-three coefficient. Coarse invariants give the source \(\mathcal O^2\oplus\mathcal O(-1)^2\), target \(\mathcal O\), and the global target frame is the invariant generator induced by \(y\). The constant block is a nonzero constant row. The printed right inverse and subtraction of its image from the other columns are exact maps of the actual cup sequence. They prove \(K_0=\mathcal O\oplus\mathcal O(-1)^2\), including the possible \(dx\) contribution.

The determinant \(-bc\,y^2\) is nonzero at the twelve ordinary attachment points. Consequently the derivative \(H\) used in each local calculation is the actual invertible handle derivative. The proof does not substitute a freely chosen map for it.

## 2. Actual root family and the total-space kernel

The complete family-lift supplement supplies the missing uniform-in-parameter form of the finite invariant divisions. In the declared fine frames, a coarse graph coefficient \(C_{ji}(b,s)\) lifts by

\[
Z_{ji}(w,s)=w^{a^G_j-a^F_i}C_{ji}(w^n,s).
\]

This follows directly by dividing the actual invariant graph vector by \(w^{a^F_i}\); the inverse graph map is multiplication by the inverse displayed factor followed by invariant descent. At order three the exponent matrix is \(\left(\begin{smallmatrix}0&-1\\2&1\end{smallmatrix}\right)\), and at order four it is \(\left(\begin{smallmatrix}0&-3\\1&-2\end{smallmatrix}\right)\). Fixing the entire period plane along the marked section gives the joint divisions \(C_{12}=bD_{12}\), and additionally \(C_{22}=bD_{22}\) at order four. The required entries become \(w^2D_{12}(w^3,s)\), \(wD_{12}(w^4,s)\), and \(w^2D_{22}(w^4,s)\), respectively. These are joint holomorphic maps with the stated characters. At ordinary nodes this root/coarse comparison is the identity.

The existing E15 Step 8 gives the actual cusp chart \(Z=(\log q)I/(2\pi i)+H(q,s)\), bounded jointly on a smaller polydisc, the original toric units, proper/free lattice action, finite cover maps and annular translations with fixed integral classes. I reopened the whole E15 Steps 7–9 and its parameter-space comparison in this receiving pass. The residue remains invertible. The attached comb proof fixes the three entire marked period points, and its family is holomorphic jointly in \((b,s)\) there. Thus the stronger fixed-point construction satisfies every one- and two-entry finite condition in E15.

Near a node the actual relative dualizing generator is \(dx/x=-dy/y\), so the actual cup row has derivative \(\Theta=xZ_x-yZ_y\). Its first coefficient is \(x\kappa_H-y\kappa_B\). The chosen open conic condition makes these two functionals independent. Its entries generate \((x,y)\), and elementary invertible operations identify the row with two regular generators and two zero entries. The Koszul syzygy and the two free columns prove a locally free rank-three total kernel. Off the nodes the central coarse row is onto; its unit coefficient persists in the family. Finite invariants are exact and commute with this parameter restriction, using the explicitly preserved character frames. On a noncentral fibre the node ideal is the unit ideal. Hence the smooth kernel is exactly the actual \(K_{12}\) and its coarse cokernel has length zero.

## 3. Exact node sufficiency, including the mixed graph term

The receiving coefficient calculation agrees with the frozen independent one. The arbitrary term \(xyR(x,y)\) contributes no coefficient of \(xy\) to \(xZ_x-yZ_y\). The moving tensor frames are retained, so this cancellation does not remove their derivatives. The remaining first-jet equality is

\[
\kappa_H\bigl(\eta_t'(0)\bigr)
-\kappa_B\bigl(\eta_h'(0)\bigr)=0.
\]

For publication the following sufficiency argument should be inserted. Let \(\varphi:R^4\to R\) be the row over \(R=\mathbb C\{x,y\}\). Its image is \(\mathfrak m=(x,y)\). A pair of branch sections with the same ordinary value has a lift \(\widetilde\eta\in R^4\), and its branch equations give \(\varphi(\widetilde\eta)=xyh\). The constant \(h(0)\) is exactly the displayed mixed-jet defect. Adding \(xy\zeta\) changes \(h\) by \(\varphi(\zeta)\), whose possible values are exactly \(\mathfrak m\). Thus the single constant defect is the complete obstruction. Once it vanishes, \(h\in\mathfrak m\) has an actual analytic preimage under \(\varphi\), producing a total-space kernel lift. This proves all analytic orders, rather than only a necessary second-order test. The quotient between the kernel of the central row and the central fibre of the total kernel is the single node copy of \(\mathbb C\).

The determinant/dualizing unit changes add multiples of the two zero value equations. A tensor-frame change transports both branch derivatives, with its derivative included. This is the exact relation between the literal graph calculation and the invariant node condition.

## 4. Actual conics and moving frames

The receiving inclusion \(S=(I+yA;yB)\) and quotient \(Q=(-yB,I+yBAB^{-1})\) satisfy \(QS=0\) and \(QS'=B\). Homogenizing them shows full rank at every point, including infinity, so their exact bundle sequence gives \(F=\mathcal O(-1)^2\), \(G=\mathcal O(1)^2\). In the bottom-block chart the plane recovers the affine parameter, and the invertible derivative proves immersion. Thus these are actual embedded conics with the required bundle maps.

Put \(P=I+yA\), \(C=BPB^{-1}\). The graph map is \(Z_t=yBP^{-1}\), the inclusion is \((I;Z_t)P\), and the quotient is \(C(-Z_t,I)\). The tensor transition is exactly

\[
\eta_{\rm graph}=P\eta_{\rm conic}C^{-t}.
\]

The determinant-valued cup transforms by the actual factor \(\det C\); it follows from \(C^tJC=(\det C)J\). Global tooth-kernel sections are constant in the polynomial conic frames, giving the forced derivative

\[
\eta_t'(0)=A\eta_0-\eta_0(BAB^{-1})^t.
\]

Both terms and the transpose are essential and correct. Their substitution gives exactly the receiving two-jet quotient. The two source reparameterizations act by \((A,B)\mapsto(rA+tI,rB)\); they scale the defining equations by \(r\) and leave their kernel unchanged. The eight matrix parameters modulo those two parameters form the actual six-dimensional through-point conic chart from the opened source.

## 5. Exact frame transport and attainable quotient dominance

The receiving reduction using \(H\) is valid with the following actual morphism made explicit. Write new frames as \(F'=FU\), \(G'=GV\). Then

\[
T'=V^{-1}TU,\qquad \eta'=U^{-1}\eta V^{-t},\qquad
\kappa_{T'}(\eta')=(\det V)^{-1}\kappa_T(\eta).
\]

The conic matrices become \(A'=U^{-1}AU\), \(B'=V^{-1}BU\). Take a matrix \(R\) of eigenvectors for \(H^{-1}B\), and use \(U=R\), \(V=HR\). This sends the actual handle derivative to \(I\), the actual tooth derivative to \(\operatorname{diag}(\beta_1,\beta_2)\), and the tensor to \(R^{-1}\eta H^{-t}R^{-t}\). It therefore proves the exact relation between the original and displayed diagonal calculations.

On the nonempty open set \(\beta_1\beta_2(\beta_1-\beta_2)(\beta_1+\beta_2)\ne0\), the two value equations give diagonal \(\eta_0=\operatorname{diag}(u,v)\). The two free coefficients of the jet covector are

\[
r(1+\beta_2/\beta_1)u-q(1+\beta_1/\beta_2)v,
\]

with Jacobian determinant \(- (\beta_1+\beta_2)^2/(\beta_1\beta_2)\). My frozen derivation used the separate actual quotient-frame map \(B^{-1}\), obtaining \(-\operatorname{tr}(B^{-1}H)((a_{11}-a_{22})q+a_{12}r-a_{21}p)\). The identity \(\operatorname{tr}(C^{-1})=\operatorname{tr}(C)/\det C\) relates the nonzero restrictions; the two routes agree. The trace-zero locus is explicitly excluded in both, so it is not silently used as a source of arbitrary second jets.

The first covector is the restriction of the perfect four-dimensional cup pairing to \(\ker\kappa_H\), giving the full three-dimensional dual quotient by the line spanned by \(H\). Together with the two free second coefficients modulo that first covector, this proves dominance onto the four-dimensional space of cyclic length-two quotients. The derivative of a fixed handle frame translates the second coefficient and preserves this demonstrated freedom.

## 6. Genericity within the actual smoothing construction

The balanced split-coordinate example is an exact witness in the complete quotient parameter space. Four distinct double points on each of the three actual seed summands give \(\mathcal O(-8)\oplus\mathcal O(-9)^2\) by multiplication by the three degree-eight products. The two cohomology vanishings define a nonempty Zariski-open subset. Dominance pulls that open set back to actual conic data; the proof does not assert that each special coordinate quotient itself occurs as an admissible conic.

The opened original normal-sheaf proof gives a second nonempty Zariski-open condition in the actual tangent directions: the original normal degrees \((-1,0,0,1)\), the three fixed marks, and the distribution \((4,3,3,2)\) give a globally generated modified normal sheaf with zero \(H^1\). The actual conic tangent map is dominant. Thus both opens meet in the irreducible conic chart. The compact admissible conics occupy a nonempty complex-open subset, which meets their dense algebraic intersection. This produces actual admissible teeth satisfying both requirements. The complete source proposition then supplies an embedded smoothing fixing all three marks, smoothing every node to first order, with genus zero and degree one over the base. Its projection is the actual collapse on the central fibre and an isomorphism to the base on the smooth fibres.

## 7. Complete collapse and smooth splitting

On the handle the relative kernel is the first elementary modification of \(K_0\) at each node. On each tooth its ordinary \(\mathcal O^3\) kernel acquires the one nonzero value condition from \(\kappa_H\), giving \(\mathcal O(-1)\oplus\mathcal O^2\). Its \(H^1\) vanishes; its global sections have no section vanishing in its own entire node fibre. Their evaluation image has dimension two in the three-dimensional relative-kernel fibre. That image retains the shared Koszul coefficient encoded by the complete mixed-jet criterion.

Apply the normalization exact sequence to the locally free central kernel. Locally on the handle, evaluation onto its whole node fibre is surjective; each tooth has zero \(H^1\). Therefore \(R^1\pi_*K_C=0\). Unique extension to each tooth identifies \(\pi_*K_C\), by literal restriction, with the sheaf cut out by the twelve complete cyclic two-jet quotients. This proves the exact equality \(\pi_*K_C=K'\), with both conditions retained.

The single family line is the pullback of \(\mathcal O_B(k)\) by the actual projection. It is trivial on every tooth and restricts to the required line on every smooth section. Projection formula and the preceding derived direct image give the asserted cohomology identifications. The locally free coarse relative kernel is flat over the disc, so the two vanishings persist. The central Euler characteristic is \((1-12)+12\cdot2-12\cdot3=-23\), independently giving degree \(-26\); the surjective smooth cup sequence gives the same degree.

Finally the full receiving proof derives the splitting from these vanishings, not from degree alone. The unique section of \(K_{12}(8)\) is nowhere zero, since a zero would give a section of \(K_{12}(7)\). Its quotient has rank two, degree minus two and zero \(H^0,H^1\). The literal evaluation of its twist by one is an isomorphism, so that quotient is \(\mathcal O(-1)^2\); the extension splits by the actual vanishing of \(H^1(\mathcal O(1))^2\). Twisting back gives the claimed bundle isomorphism.

## Opened original-source comparison

The source is the supplied `Viaclovsky_Comb_S6_Draft_October_7_2026.tex`, SHA-256 `42dea62b023dfb75a009a8c83c15349ddc8f853162f753e3547ca583d07b74d5`, existing bibliography key `Viaclovsky2026Combs`.

Before the independent freeze I opened lines 1260–1490, including the complete lemma labelled `twistor`, the definition labelled `d:comb`, and the complete proposition and proof labelled `comb`; I also opened lines 2445–2498, including `originalnormal` and the sufficient twelve-tooth bound. During receiving I reopened the full `comb` proof (1382–1487). These exact passages supply the conic bundles and tangent openness, positive modifications, fixed-marking unobstructed smoothing, degree-one projection and the sufficient bound. The new two-jet flat-kernel calculation is not attributed to that source.

After the freeze I opened Section `future`, question (2), lines 2701–2708: its requested remaining Hodge numbers are the relevant original question. The proved result here supplies the two stated Hodge values on the constructed open twelve-tooth family. It does not answer the source's full variation/classification question for all members or all tooth counts. No worldwide novelty search or priority assertion is claimed by this receipt.

The current E15 and E2.2 proofs were already exposed and were reopened before the independent freeze. Their exact finite-character/cusp formulas are used as established inputs. The isolated packet also supplies the seed I D1.1/D1.2 bundle identifications. This receipt does not manufacture a fresh whole-proof review of those Paper I results.

## Executed receiving certificate and remaining publication work

`receiving_exact_certificate.py` was written **after** reading the complete root certificate. It imports no producer code. It passed **25/25** assertions at 2026-11-20 01:43:31 UTC: the general determinant/frame cup identity; the frozen trace-jet identity and its receiving diagonal comparison; exact normal-form node gluing; all finite-character exponent cells; every entry and the complete Fraction ranks of all three saved Hermite matrices; and the independent central Euler characteristic and degree. Its implementation and exposure are separate from the earlier frozen independent derivation. The root's 53-check output was received; it was not re-executed or relabelled as this reviewer's independent computation. The root's preserved first-attempt test typo was read and leaves no mathematical contradiction.

The certificate does not replace the holomorphic division, analytic admissibility, smoothing, sheaf lifting, or collapse arguments proved above. The remaining work is publication integration, statement scope/credit, and actual rendered-page review. The two insertion-ready completeness paragraphs are saved separately in `publication_completeness_insertions.tex`. No shared source, inventory or canonical assessment has been edited.

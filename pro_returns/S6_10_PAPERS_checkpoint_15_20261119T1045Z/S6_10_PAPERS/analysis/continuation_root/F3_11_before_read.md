# F3.11: complete receiving proof before the printed target

The corrected statement-only packet is `analysis/continuation_V/F3_11_statement_input_packet.md`, SHA256 35a549cd5335208a63f80b672191a70ca5789c1fae64e99998719ed6aedb4f67. The printed F3.11 proof and original producing programs have not been opened. The packet's earlier additional component requirement was withdrawn before this derivation: the actual target prescribes no component independently of its cusp marking. Every component transport below is the actual real matrix P. Named in-paper inputs retain their separately recorded proof and source gates.

## 1. Actual real and integral cusp coordinates

Put N=M0−I. Since N²=0 and rankN=3 in a six-dimensional real space, imN is contained in kerN and both have dimension3, hence are the same subspace. Choose a real basis u1,u2,u3 of imN and preimages vj with Nvj=uj. The six columns (u1,u2,u3,v1,v2,v3) form an invertible matrix P: applying N to a linear relation first kills its v-coefficients, then independence of the uj kills its remaining coefficients. For Ns=[[0,I3],[0,0]], the exact identities are NP=P Ns and M0P=P(I+Ns).

The determinant of P is retained, including its sign. The transverse component used below is P D3, where D3 is the standard positive graph component. Conjugation P⁻¹ρP still has positive real determinant, so ρ preserves P D3. The map F↦PF is a holomorphic biholomorphism on the Grassmannian and gives this explicit component transport; no independently specified orientation component is imposed.

For an integral primitive cusp, imN and kerN in Λ=Z6 are primitive subgroups with the same rational span and rank3, so equality follows directly: a primitive subgroup equals its rational span intersected with Λ. Choose an integral basis uj of imN and integral preimages vj. The homomorphism N induces an isomorphism Λ/kerN→imN, with inverse on this basis given by the classes of vj. Each λ∈Λ therefore differs from an integral combination of the vj by an integral combination of the uj. These six vectors are an integral basis, so P∈GL6(Z). This is the actual basis used in the period formula.

## 2. Holomorphic extension by the logarithmic gauge

Retain p0 and let R=P1 minus{p1,…,pk}; because k≥1 this is an open Riemann surface. On a coordinate disc about p0 write t(p0)=0, choose the universal punctured-disc logarithm w=log(t)/(2πi), and use the marking of section1. Let V* be the flat complex bundle of the actual representation ρ on B*. Its local equivariant convention is (w,z)↦(w+1,M0z). Define

T(w)=P(I+w Ns).

Because Ns²=0, T is invertible, with T(w)⁻¹=(I−w Ns)P⁻¹, and T(w+1)=M0T(w). Thus c=T(w)⁻¹z is single-valued in this bundle over the punctured disc. Glue the trivial bundle D×C6, in coordinate c, to V* using the exact map c↦T(w)c. This gives a holomorphic rank-six bundle V over R and changes none of ρ's other puncture monodromies. The construction uses the given based local marking, so its monodromy identifies with the original representation under the specified basis maps.

The central Grassmann chart is Q_C=columns(C;I3), C∈Mat3(C). Undoing the gauge gives T(w)Q_C=P columns(wI3+C;I3). Hence this is exactly the requested period Z=wI3+C in the marked coordinates, rather than a change of its logarithmic coefficient.

## 3. The open section target including the cusp point

Over R minus{0}, use the associated transverse bundle with fibre P D3. At t=0 include every central graph Q_C, C∈Mat3(C). Call the resulting subset of Gr3(V) U. It is open. Away from0 this is the ordinary open transverse locus. Near a central graph Q_C0 choose a bounded neighbourhood of matrices C in that graph chart. Write y=Im w=−log|t|/(2π). For sufficiently small |t|, y>||Im C|| uniformly in the neighbourhood. Then

Im Z=yI3+Im C=y(I3+y⁻¹Im C)

is invertible by the convergent Neumann series. The entire path yI3+s Im C, 0≤s≤1, stays invertible, so its real determinant has the same positive sign as det(yI3)=y³. Finally

det(columns(Z;I3),columns(conjugate Z;I3))=(2i)³ det(Im Z),

by subtracting the first block of columns from the second and exchanging the two three-row blocks. The determinant calculation is an exact transversality test, and multiplication by P retains its actual determinant factor. Thus a whole product neighbourhood of each central graph lies in U. The projection U→R is surjective, its central fibre is this C9 graph chart, and off0 it is the holomorphic bundle with LSAP fibre P D3. The latter property is transported by F↦PF from the named F3.8 input.

## 4. A local section for every prescribed finite jet

Write the prescribed matrix jet as A0,…,Ar and put C*(t)=Σ_(j=0)^r A_j t^j. Choose a closed coordinate disc K={|t|≤ε}, with ε≤1, sufficiently small that −log ε/(2π)>Σ||A_j||+1 and that a slightly larger disc lies in the coordinate chart. The section Q_C*(t) is holomorphic near K and lies in U by the bound above. K is Runge in R: R minus K is connected and noncompact, since at least p1 is removed. Shrinking ε preserves this property and every specified jet.

## 5. Continuous extension of that actual local section

The fibre D3 is connected and simply connected. Here is an explicit derivation of the needed topology. A transverse plane F defines a real complex structure J by declaring J=i on F and J=−i on conjugate F. Complex conjugation commutes with this definition, so J restricts to the real space; its inverse map is the +i eigenspace of J. These maps are continuous inverses.

For such a J, let g=I+JᵀJ. This is positive definite and JᵀgJ=g, using J²=−I. Put P_s=((1−s)I+s g)^(1/2), 0≤s≤1, and J_s=P_s J P_s⁻¹. Every J_s is a complex structure in the same orientation component because detP_s>0. At s=1,

J_1ᵀJ_1=g^(−1/2)JᵀgJ g^(−1/2)=I.

An orthogonal J has g=2I, so all P_s are scalar and this homotopy fixes J. It is a strong deformation retraction onto the chosen component of orthogonal complex structures, which is SO(6)/U(3) by the actual conjugation action and its stabilizer.

For completeness, π1U(3)=Z follows from U(n−1)→U(n)→S^(2n−1), starting with U(1). The sphere terms in dimensions3 and5 have zero π1 and π2. Likewise π1SO(6)=Z/2 follows from SO(3)=RP3 and SO(n−1)→SO(n)→S^(n−1) for n=4,5,6; those sphere terms again have zero π1 and π2. The loop diag(exp(iθ),1,1) in U(3) is rotation through θ in one actual real coordinate two-plane. Its image is the generator of π1SO(6): already in SO(3), its quaternion lift runs from1 to−1, and the later inclusions induce the stated isomorphisms. The homotopy sequence of U(3)→SO(6)→SO(6)/U(3) therefore has a surjection Z→Z/2 and connected U(3), so π1(SO(6)/U(3))=0. The same conclusions hold for P D3 by the actual plane map P.

Choose a slightly larger closed disc K' on which the local holomorphic section of section4 is defined. Triangulate R outside its interior, relative to its boundary, locally finitely. The associated period bundle is trivial over each cell. Extend the already prescribed section over the remaining vertices, then over edges by path connectedness of the fibre, then over each two-cell by its zero fundamental group. No higher cells occur. Cellwise sections agree on attaching boundaries; local finiteness gives a continuous global section. Its restriction near K remains the original holomorphic graph. The isolated central point belongs to the retained local disc throughout, so this extension makes no fibre-bundle assertion there.

## 6. Holomorphic section and exact cusp jet

Apply the already stated F3.10 isolated-extension lemma with the holomorphic bundle V, the open target U, S={0}, and the Runge disc K. Every hypothesis has just been supplied with its actual map: off0 the fibre is the F3.8 LSAP domain transported by P, and the continuous section is holomorphic near K. Request interpolation of the given finite jet at0. The resulting section is holomorphic on all of R and stays in U. Near0 it lies in the graph chart, so it is Q_C(t) with C holomorphic at0. The chart C↦Q_C is biholomorphic, so interpolation in this chart is exactly interpolation of the entries A0,…,Ar, with no coordinate-jet ambiguity.

Undoing the explicit gauge T gives the actual ρ-equivariant holomorphic transverse family on B* and the formula Z=log(t)/(2πi) I3+C(t). Its transversality is the determinant test above in this chart and the invariant transverse condition everywhere else. This proves every asserted jet and marking clause of the target using the stated F3.8 and F3.10 inputs.

## 7. Application to the already specified survivor data

For the F2 survivors, F2.7 supplies the two-point genuine reduction and F2.15 supplies the actual complex compatibility of each finite real action. A real map commuting with a complex structure has positive real determinant, equal to the squared modulus of its complex determinant; the product and inverse preserve that sign. The associated representation therefore has values in GL+(6,R). Its specified primitive cusp is put in the exact integral basis from section1, so all preceding constructions apply. They give the period family on the surface with the other points still removed. The target imposes no extension at those points, and none is added to this derivation.

## Fresh checks and bounded credit

A new standalone exact program is being written from these definitions to verify actual gauge and graph identities, integral cusp markings of both determinant signs, the marked monodromy square, the complex-structure/metric identities, and actual parameter-jet transport. It imports none of the earlier period-producing code. These finite checks accompany the universal derivation above; they do not replace it. The receiving F3.11 proof will only receive a complete comparison after all of this is frozen and its target is then opened. The named LSAP and isolated-extension theorems retain their own independent review status.

Development chronology before any target reading: the first fresh program run stopped at the sixth marking with negative determinant because a SymPy matrix retained unexpanded polynomial products during a structural equality comparison. The recovered matrix is now expanded entry by entry before the exact coefficient comparison; this changes the representation of the same explicitly multiplied matrix. The failed run is not counted as a successful check. A successful rerun, when observed, is recorded separately in the frozen receipt.

A second pretarget execution passed the cusp/jet identities and reached the first graph eigenplane test, where unexpanded complex products again made a structural comparison fail. That equality and the analogous complex-action conjugation are now compared after exact expansion of their difference. The output receipt records only the final successful run once observed.

A third pretarget run reached the last group of checks and encountered the same structural-comparison issue in the product of two complex determinants. The exact expanded difference is now used for that scalar equality as well. All three unsuccessful execution stops are retained here; no target proof has yet been opened.

The complex-action determinant assertion in section7 uses the exact complex basis C=[[I,I],[−iI,iI]]. For the real matrix R=[[A,−B],[B,A]] of A+iB, multiplication gives C⁻¹RC=diag(A+iB,A−iB). Taking determinants gives det_R R=det_C(A+iB) times its complex conjugate, which is strictly positive for an invertible action. The final fresh run has now completed with211 PASS checks. Its input identities and finite scope are explicit in the accompanying output.

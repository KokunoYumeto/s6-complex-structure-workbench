# Independent referee note: A.3.1–A.3.2 and C.1.1

Reviewed 2026-11-15 by the Part D agent. This note concerns the stated analytic smoothing invariant, the normalization calculation, and the clutching sign. It does not independently certify the global collar construction in A.1.2 or the previously established Euler number of Engel's fibres.

## Verdict

The virtual Euler obstruction is valid for arbitrary proper flat holomorphic smoothings of the specified reduced lci space. Neither projectivity nor the Kähler condition is needed. The calculation for Q gives zero. I found no contrary example or missing geometric hypothesis in A.3.1–A.3.2. Two proof passages should be made more precise, as recorded below. C.1.1 has the stated positive sphere summand with its stated seam and orientation conventions.

## A.3.1: analytic invariance

A flat deformation over the smooth disc of an lci fibre is lci near that fibre: choose local relative embeddings, lift the central regular sequence, use flatness to identify the ideal modulo the parameter, and apply Nakayama. The lifted sequence is regular, either by the nonzerodivisor criterion inductively or by the Cohen–Macaulay dimension criterion in the regular relative ambient local ring. Properness permits one common disc after the local construction. Consequently the relative cotangent complex is perfect, and its derived dual has a natural topological complex K-class. Its restriction to a fibre is the derived tangent class; this is the actual tangent bundle on a smooth fibre.

The reference to a global analytic vector-bundle resolution would be unsafe: such resolutions need not exist on arbitrary complex spaces. The manuscript instead uses the topological class. Levy (2008), Lemmas 3.1–3.2 and §3.1, pp. 588–590, supplies precisely the stabilization and gluing of local complexes into a global continuous complex. It is enough to perform this construction on a compact inverse image of a segment, where a finite covering suffices. This also avoids any uniform rank issue on a noncompact total space.

For the homology assertion, the following gives a precise replacement for the informal lower-strata sentence. Fix a small positive real ε and set K=π⁻¹([0,ε]) and S=Sing(Z). Flatness and regularity of each smooth fibre imply that π is a submersion at every point of K outside S. Thus K minus S is an oriented real (2n+1)-manifold with boundary Xε disjoint union minus Zreg, with orientation dt followed by the complex fibre orientation. Since Z is reduced and pure dimensional, dim_R S is at most 2n−2. Compatible triangulation of K relative to S, Z and Xε now gives an integral chain by summing all oriented top-dimensional simplices. All interior faces cancel. The only 2n-dimensional boundary faces lie in Xε or Zreg; none can lie in S. At a smooth central point the parameter is a submersion, so the central coefficient is exactly one. Its boundary is [Xε]−[Z]. This proves equality in integral singular homology of K and hence of the total space. Pairing c_n of the topological K-class, and applying smooth Gauss–Bonnet, proves the asserted equality.

Compatible triangulation is the standard analytic-space form of semianalytic triangulation; Łojasiewicz (1964), §3, Theorems 1–2, pp. 463–464, is the primary local/ambient theorem. Compact analytic spaces are triangulable using their finite analytic atlases. No Whitney a_f theorem, projective specialization theorem, or global ambient complex embedding is being assumed here.

## A.3.2: normalization and K-theory

The notation ν* must mean pullback of a perfect K-class, equivalently derived pullback. It must not mean ordinary pullback of a possibly non-locally-free tangent sheaf.

For a single branch with normal line A in a smooth local ambient space and conductor D, the hypersurface normal line restricts to A(D). Hence the virtual difference from the branch tangent bundle is A−A(D)=−i_*[A(D)|D]. The latter line on D is the product of the two branch normals, namely T¹_Q. The intrinsic differential comparison makes these local identities compatible. On the normalization's infinity section, the line is technically pulled back by the conductor identification. It agrees with the same J because J=π*O_B(1) and the translation preserves B. Thus the two negative terms displayed in A.3.2 are correct.

Put v=d0+d∞=c1(T_R/S). Since J extends to R, each i_*J is represented by [J]−[J(−Di)]. The Chern correction factor is exactly 1−v+jv: expand the displayed ratio using j²=0 and d0d∞=0. Write c=c1(S), C=c2(S). Then c1(R)=c+v, c2(R)=C+cv, c3(R)=Cv. The degree-three corrected class is

    Cv − (C+cv)v + jv(c+v) = cjv + (j−c)v².

Here j=c=F and F²=0, so the entire pulled-back c3 class is zero, not only its integral. Since ν_*[R]=[Q], the virtual Euler number is zero. This agrees with the manuscript's independent numerical intersection calculation 24−24+0. An independent symbolic check is saved as code/d_push_referee.py with output code/d_push_referee.out.

Conditional only on the separately proved input e(X(u))=2, A.3.1 now excludes every proper flat holomorphic smoothing of Q with those fibres. The argument does not require a map to B, a prescribed smoothing section, a smooth total space, or an algebraic family.

## C.1.1: clutching orientation

At the seam of the stated mapping torus, write the lower coordinate as x and the upper coordinate as φ(x), because (x,1) is identified with (φ(x),0). The chart on the inserted block therefore uses x below and φ⁻¹ of the original coordinate above. Relative to the original product complement, the boundary attaching map is φ on the upper cap and the identity on the lower cap and side collar. For dt wedge o(D6), the upper cap has positive boundary orientation o(D6). The regluing is consequently the sphere D7_+ union_φ (−D7_-), with positive sign. Hence the stated oriented connected-sum formula has Σφ, not its orientation reverse or inverse clutching class. Reversing the seam convention would reverse this sign. The orientation dθ wedge o(fibre) also agrees with the outward boundary orientation of a positively oriented complex base disc.

## Primary references opened and checked

Levy, R. N. (2008). Riemann–Roch theorem for higher bivariant K-functors. *Annales de l’Institut Fourier, 58*(2), 571–601. https://doi.org/10.5802/aif.2361. Full primary PDF: https://www.numdam.org/article/AIF_2008__58_2_571_0.pdf. Read introduction, Lemmas 3.1–3.2 and §3.1, especially pp. 588–590. Search/open records: turn50view0, turn52view3, turn55view0, turn55view1.

Łojasiewicz, S. (1964). Triangulation of semi-analytic sets. *Annali della Scuola Normale Superiore di Pisa, Classe di Scienze, Serie III, 18*(4), 449–474. https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0/. Full primary PDF: https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0.pdf. Read §3, Theorems 1–2, pp. 463–464, and metadata. Search/open records: turn50search1, turn52view0, turn53view1, turn53view2.

The algebraic comparison FG10 in the manuscript is not used to supply the analytic specialization step.


## Additional checks: A.1.2, A.2.1–A.2.2, and Lead 5

The global core/node plumbing in A.1.2 is correctly typed: a belongs to L_x, b to L^−1_{Tx}, and a tensor b=uφ_x. Hence the infinity collar coordinate b^−1 lies in L_{Tx}; its contracting inverse covers T^−1, as required. The two collars are disjoint under the displayed uniform norm bound. The smaller closed core and node sets cover the quotient, establishing properness without a polarization assumption. The local total node ring is Cohen–Macaulay and the joint fibres have pure dimension two, so the regular-sequence flatness argument applies even over the nonreduced Kodaira fibres.

In A.2 the exclusion of new rays under joint flatness and reducedness checks: a mixed positive-height ray would give a three-dimensional component over the origin of a two-dimensional base; a new bottom ray changes the retained triangulation; a remaining primitive ray has h_q=0, h_u=1 and is already a rho ray. On each regular chart of either retained subdivision, q and u are monomials in disjoint sets of affine coordinates because all rays have pure q-height or pure u-height. This gives a particularly direct proof of the required pure-dimensional fibres and joint flatness. The singular-centre blow-up charts X=zvA and zv=XB, followed by the stated conifold resolution, are correct. The strict transform of the section is A=0 in the first chart and misses the conifold in the second chart, so it stays isomorphic to S and its normal bundle acquires exactly O_S(−S∞).

I also checked the component-cover obstruction subsequently found by the AB agent for the literal Lead 5 gluing. Over B° the prescribed r=0 fibre is a cycle of 12 ruled components; normalization and its Stein factor give a degree-12 étale component cover, and incidence restricts transition permutations to the dihedral group D12. The finite models impose rotations +4 and −3. The plain cusp fan has global labels j modulo 12, preserved by both periods, so its peripheral permutation is identity. Even allowing independent incidence-preserving relabellings changes the two rotations only to ±4 and ±3, none of whose sums is zero modulo 12. Thus those prescribed pieces cannot be the restrictions of one global family. This refutes the literal gluing, not all possible corrected cusp models. In common orientation the missing cusp rotation is −1. It agrees with the simple cusp pole found independently in D_monodromy_order_note.md.

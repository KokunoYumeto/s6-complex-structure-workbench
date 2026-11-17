# Local intersection forms in the remaining positive ruled support

## P4.51 candidate — exact proved restriction, awaiting independent audit

Let S be an irreducible reduced support in the actual torus fibration of Part4.2 with b1(S)>0. Every local Milnor fibre of a reduced local equation of S has identically zero rational intersection form. In particular this applies to the remaining positive ruled support, where the conductor pushout gives pi1(S)=Z.

We use the exact tube comparison of P4R.4. Write U for a sufficiently small full tube and F_t for a nearby compact smooth torus fibre. The inclusion induces a homomorphism pi1(F_t)=Z^4 to pi1(U)=pi1(S) whose cokernel is finite cyclic of order the fibre multiplicity. Thus the induced map H1(F_t;Q) to H1(S;Q) is onto. Its kernel W has dimension 4-b1(S), at most three.

Choose a coordinate ball B about a point of S whose closed ball lies in U. Write the local full fibre equation as u g^m, where g is reduced and u is a holomorphic unit. After taking the holomorphic m-th root of u on B, absorb it into g; hence the actual nearby fibre inside B is a disjoint union of the local Milnor fibres g=ζ t^(1/m). Each such local Milnor fibre M is an oriented codimension-zero submanifold with boundary of F_t. Every loop of M is nullhomologous in U, because its inclusion factors through the contractible ball B. Consequently the image H of pi1(M) in pi1(F_t)=Z^4 satisfies H tensor Q subset W.

Take the connected cover F_H of F_t corresponding to the subgroup H. The inclusion M to F_t lifts to a continuous map M to F_H by the covering criterion. Since H is a subgroup of a free abelian group, it is free abelian; the cover F_H is a K(H,1). The homology map H2(F_H;Q) to H2(F_t;Q) is therefore the natural exterior-square map wedge2(H tensor Q) to wedge2 H1(F_t;Q). It follows that every class from H2(M;Q) has its image in wedge2 W. The torus intersection form is exterior multiplication followed by the fixed orientation isomorphism wedge4 H1(F_t;Q)=Q. Because dim W<=3, all such products vanish.

Finally, this ambient pairing is the local intersection form on H2(M;Q). A finite family of cycles may be represented inside the interior of M and made transverse there, and their intersection points and signs are unchanged by the orientation-preserving inclusion into F_t. Thus the pairing vanishes identically. We do not infer rationality of the normalization from this statement; that implication still needs a separate proof or an exact primary theorem.

The independent symbolic check in code/part4/local_intersection.py expands the six-coordinate exterior-square map for an arbitrary three-dimensional graph subspace and verifies the zero pairing. The proof above covers every subspace, without selecting that chart.

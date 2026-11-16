# Independent audit of D.2.44

The current full section `sections/fourfolds_D2_critical_frame.tex` was read
on 16 November 2026, including the added localization argument and the
explicit surgery models. The audit passes within its stated seven-row,
primitive-Mumford, no-extra-regular-log scope.

The C_c localization is integral in Z/c because all nontrivial isotropy
is the full group and the remaining action is free. The mixed elliptic
class has square zero even when the degree-one cyclic class squares
nontrivially: the elliptic degree-one class lifts integrally and has square
zero. The determinant character vanishes, so the λ=-c2 computation has no
unrecorded determinant term. The resulting λ=μ=0 leaves exactly the stated
binary refined class.

Brown's original pp.369–372 were visually read from the cached original
page images. F(u,0) on p.369 is the stabilization of u itself. The duality
construction in Theorem1.7/Corollary1.11 sends a normal-framed collapse to
the induced stable framed class. Lemma1.2 and the remark after
Corollary1.13 identify the target and the odd quaternionic Hopf element.
Thus the parity comparison for a torus and a sphere in the same mod-two
class is valid, including an integral torsion class. The sphere convention
agrees with the left-quaternionic clutch and with Zhubr2013 §5. The P=0
converse is also valid: the admissible field's spin three-plane complement
has its primary obstruction zero, and H5(X minus point;Z/2)=0 removes the
only remaining obstruction on a five-dimensional spine.

The differential complex, its unit Bott residue, abstract nonvanishing
δ-vector and upper-triangular reference-frame comparison have an
independent geometric verification in `code/maps_D2_frame_proof.tex`.
That proof additionally constructs a spin-compatible ambient surgery
T³→S³ directly in X minus a point, using Kaplan's original Theorem3.1;
it does not assume a spin-insensitive Borromean surgery. Its direct
Spin6/Spin3 transgression supplies an independent obstruction comparison.

The seven-row critical-cycle proof was read in full, and the actual
`manifolds_even_critical_cycles.py` was rerun independently. Both ordinary
clutch signs passed for all rows. The integral transverse bases, the
unimodular cusp support-degree matrix and the extra dual-torus coordinate
identify the literal critical cycles. The boundary-chain extraction gives
the integer links ±4 and ±37,±7,±27 and certifies the odd generator.

For the model recognition, Zhubr's original English paper was reopened
through MathNet (`turn443view0`, `turn444view0`–`turn444view2`). Theorem3,
printed p.795, gives uniqueness of the oriented simply connected b3=0
manifold over K(G,2). The natural bordism homomorphism P is defined in
§1.4, p.796; §3.13, pp.807–808, proves its agreement with the manifold
invariant. Theorem5, p.796, makes (P,μ) complete, and §3.12 gives
P(CP³)=1. Hence the conic surgery has P=1 mod2, and the map
Z/2⊕Z→Z/c sending (t,z) to (c/2,1) kills (t,-c/2). Its surgery trace
therefore transports P to c/2. The complete cubic maps to zero for c4/8.
The zero model has P=μ=0. Both sphere normal bundles are trivial by spin,
and π2SO4=0 gives their unique normal framings. This validates the actual
stated surgery models, rather than recognizing the types by homology.

The later type-II or good-log extension is a separate problem. In
particular, the regular three-torus can be an even class after a good
logarithmic replacement; D.2.44 itself does not make that extension.

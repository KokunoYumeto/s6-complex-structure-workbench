# Derivation before target proof: 01AX

Owner `cdp:st:A.4.8`; checker `i_provenance`. Exact packet, supplements, and
the statement-only D.1.8/D.1.9 inputs have been read; their printed proofs
remain embargoed. Related Paper I transgression/topology exposure is disclosed.
The separate A.4.7 derivation is written before its own release.

The integral transgression family can be described by its actual edge maps.
The rational Leray five-term sequence for g, with b1(Y)=b2(Y)=0, identifies
H0(P1,R1g_*Q) with H2(P1,Q) by d2. Choose a nonzero integral section gamma
whose rational class spans this line (multiplying clears its denominator).
The natural map Z->O_Y sends it to a section of R1g_*O_Y. Since g_*O_Y=O_P1
and H1(P1,O)=H2(P1,O)=0, the holomorphic Leray edge map identifies this section
with a unique beta in H1(Y,O_Y). This is the transgression construction in
the supplied D.1.9 statement, up to a nonzero integral scale; irrational
parameters retain nontriviality after every such scale.

Around any c take a small disc Delta containing no other critical value and
V=g^-1(Delta). The integral Leray sequence over the contractible disc lifts
gamma|Delta to a class gamma_V in H1(V,Z). Naturality of the holomorphic edge
map identifies its image in H1(V,O_V) with beta|V. Exponentiating r gamma_V
therefore gives the unitary local system on V with monodromy
rho(ell)=exp(2 pi i r gamma_V(ell)), and its holomorphic line is precisely
L_r|V. Its restriction to S is the local system in the statement.

By the supplied D.1.8 injectivity, gamma is nonzero on every smooth torus
fibre, and indeed on every full fibre's underlying topological space.
For irrational r, its character on a smooth torus is nontrivial. The twisted
cellular cochain complex of the real four-torus is the exterior algebra on
four generators with differential wedge a, where a_j=rho(e_j)-1. At least
one a_j is nonzero. Interior product by that generator, divided by a_j,
is a contracting homotopy: dh+hd=identity. Thus all cohomology groups of the
smooth torus with these coefficients vanish. This is an exact contraction,
not an inference from its Euler number.

Put V*=g^-1(Delta minus {c}). Its smooth proper fibration has every higher
direct image of this local system zero by the fibre calculation. Leray gives
H1(V*,mathbb A)=0 (in fact all degrees vanish). The support of the central
fibre has real dimension at most four in the real six-manifold V. Local
duality with supports, or a triangulation and the relative dual-cell complex,
therefore gives H1_S(V,mathbb A)=0: it is dual to Borel-Moore homology in
degree five of S, where there are no chains after triangulation. The exact
sequence with supports injects H1(V,mathbb A) into H1(V*,mathbb A), so it is
zero. A sufficiently small proper analytic tube V deformation-retracts onto
the central underlying fibre S, by the triangulated local fibration and a
regular neighbourhood of that fibre. Restriction consequently identifies
H1(V,mathbb A) with H1(S,mathbb A), proving the first vanishing.

Apply the explicitly constructed injection A.4.7 to the reduced compact S
and this unitary local system. It gives the torsion-free cotangent vanishing.
The underlying support and the local system are unchanged by the full
fibre's scheme multiplicities; no normal-crossing hypothesis entered any
step. This is the exact Section 7 Equation (11) group for the indicated
transgression twists. The ambient cotangent group is not substituted for it.

The generic exterior-algebra contraction is a finite exact symbolic
calculation to be recorded before target release. No old target program has
been read.

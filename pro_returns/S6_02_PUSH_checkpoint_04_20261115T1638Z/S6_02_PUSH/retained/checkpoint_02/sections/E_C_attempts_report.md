# Independent attack on the actual smooth monodromy

**State: the residue of the actual six-sphere monodromy in Θ₇ remains uncomputed.** The computations below do not assign the invariant of an untwisted mapping torus to the six-sphere mapping torus. They do not infer an order bound from circle equivariance, from a meromorphic scalar gauge, or from the existence of local quotient trivializations.

## Proven calculations and their scope

1. `C_untwisted_coboundary.tex`, C.2.2–C.2.3, computes the intersection form and a relative Pontryagin square for the **actual** semistable untwisted filling A.2.2. The form has rank two, signature +2, and nonzero Smith factors 1,11. Its nondegenerate quotient is `[[6,1],[1,2]]`; its first Pontryagin covector is `−4(a·F)−28h`; its rational relative square is 4512/11. The formal combination 79/176 is not an Eells–Kuiper value for MΦ. The determinant class restricts nontrivially to this other boundary. The branch self-intersection formula was independently checked by the A/B agent; `e_push_C_attempts.py` reconstructs the lattice independently of the A/B program.
2. The cyclic cover `y^12=t^4/(t−1)^3` is connected, with local deck shifts (4,−3,−1), ramification orders (3,4,12), and genus three. This is the component-label cover already identified in B.3.2. It is not a threefold filling. The same affine curve is the (3,4) torus-knot Milnor fibre after choosing coordinates; this observation does not identify an associated seven-sphere.
3. On the cusp-link logarithm cover, use coordinates `(a,g,u,w,d)` for q-angle and the lattice coordinates γ,u,w,δ. The deck transformation is `(a,g,u,w,d)↦(a+1,g,u,w+u,d−g)`. Naive γ-translation by r has deck defect `−rδ`. Its commuting lift is `(a,g+r,u,w,d−ra)`. At r=1 its endpoint, after removing the full γ period, is the δ-gauge `−a`, of q-degree −1. Thus a loop in quotient γ-translations does not automatically lift to an identity-ended loop on the original cusp link. The δ-circle bundle over `S¹γ×Nil³` has a nonzero mixed Chern class on q-angle × γ. Exact algebra is in `e_push_C_attempts.py` and independently in the D agent's cusp-twist program.

## Orbit-space reduction being developed

Along a real c-path, projection modulo the δ-circle discards Re ζ₂. The projected ordinary period lattice is independent of Re c. In a finite root chart, the c-dependent overlap is a real C* flow with time `(c−c₀) ε_j log|s_j|`; this can be extended by a smooth invariant cutoff which is bounded near the root centre and equals the logarithm on the overlap. The cusp toric charts themselves change by a δ-phase. These chartwise statements admit local equivariant horizontal vector fields; their differences are vertical circle fields, so an invariant partition of unity can produce a global horizontal field. This requires working with actual smooth equivariant maps in the slices; arbitrary maps of a chosen topological quotient need not be smooth at the fixed set.

For h=12, the ordinary closing scalar is `K=t^4/(t−1)^3`. The valid cusp unit is the bounded two-torus unit U in `C_closing_cocycle.tex`, with `U·(γ-deck)=(1,K)`. After projection, its additive logarithm u satisfies `u+vγ=R_log|K|`. Removing a cutoff copy of the unit isotopy and a cutoff real C* flow leaves, on the quotient annulus, translation by `χ(|q|)vγ`, identity at its two ends. This describes the candidate residual quotient twist. The preceding mixed Euler calculation shows why its full lift cannot simply be declared supported in the annulus. The outside gauge and its framing remain part of the global data.

The direct gauge comparison lemma C.3.6 establishes that two **existing smooth equivariant lifts of the same orbit map** have the same mapping class. It does not prove that the orbit twist is isotopic to the identity, nor that every quotient isotopy lifts smoothly through the fixed stratum.

## Cusp orbit topology and why a local spanning ball is unavailable

The D agent independently verified the conductor description used here. The quotient of the normalization dP₆ by the δ-circle is a compact oriented three-manifold Y with two boundary two-spheres, hence `S²×I`. Besides the two fixed divisors it has two isolated toric fixed vertices; their quotients are interior R³ points. Gluing the fixed boundary spheres first gives `S²×S¹`; the remaining four edge intervals form two disjoint circles, each crossing the glued fixed sphere once, which are then identified by the other conductor pairings.

For the full quotient H=W/δ, the normalized conductor has homology H₀=Z, H₁=Z, H₂=Z². The conductor quotient is the fixed S² with two arcs joining its two triple points; it has H₁=Z², H₂=Z. The degree-two map to Y and the conductor quotient has both columns `(1,−1)`. Complex orientations of the two fixed curves give the same generator in H₂(Y), because the two normal circle weights and the two boundary orientations both reverse. The hexagonal loop maps to a commutator of the two arc loops, so its H₁ map is zero. The pushout gives torsion-free homology `(Z,Z²,Z²,Z)` and π₁(H)=Z². The fixed S² is primitive and nonzero in H₂(H). In particular it cannot bound a three-chain, let alone a framed three-ball, in H. Extension of this conclusion from H to a whole cusp orbit neighbourhood additionally uses an equivariant tubular retraction; it is not silently assumed.

The source's rank-three quotient gives a map S⁶→S³ with Seifert multiplicities (3,4). Its ordinary γ-circle is a regular Seifert fibre, the (3,4) torus knot. This identifies an attaching loop but not the transverse framing or a capped Seifert four-manifold for the fixed S³ in the clutching seven-sphere.

## Corrected knot-invariant literature

Takase (2007), §2.1, Corollary 2.6, explicitly corrects a sign error in his 2004 paper. With his orientation convention,

`Ω(F)=−(σ(V)−⟨e(νV)²,[V,∂V]⟩)/8`

for an embedded Seifert four-manifold of `F:S³↪S⁶`. Corollary 2.14 shows that any Haefliger knot admits Seifert surfaces of arbitrary signature, so signature alone cannot determine Ω. Moriyama (2011), Theorem 8.1, independently gives the same formula, and expressly restricts that statement to **embedded** Seifert surfaces. Neither formula can be applied to a conductor quotient or an immersed surface without the appropriate correction.

Moriyama's Theorem 1.2(3) gives a useful alternative. For an actual seven-dimensional quasi-e-cobordism `(Z,V,e)`, with boundary the relevant six-dimensional orbit pair,

`σ(∂(Z,V,e))=Sign(V)−4∫_V γ²`,

where `2ρ*γ=e|S(νV)−e(T_vertical S(νV))`. For a knot in S⁶ the left side is `−8Ω`. The meridian of an e-class is two, whereas the principal Hopf circle bundle has meridian one. This factor of two must be kept in converting circle-bundle data. A doubled principal-circle Euler class need only be a **quasi** e-class; its discrepancy along the fixed set is exactly the self-linking class γ.

Primary PDFs and SHA-256 metadata are retained by `e_push_C_sources.py/.json`. Search/open responses are `E_C_search1.json` through `E_C_search15.json`. ASIII's analytic Riemann–Roch theorem was also inspected visually on original pages 564–565, with page images and local OCR retained. Its compact-complex hypothesis applies to the non-Kähler R⁺.

## Local fixed-set calculation for the untwisted filling

The fixed surfaces in W_A must be disjoint. This is verified directly in its three total-space resolution charts, rather than inferred from the unresolved central fibre. In the conifold chart `ay=zv`, use `a=zA,v=Ay` or `z=aD,y=Dv`, with u unchanged. The circle weights in coordinates `(u,z,A,y)` are `(0,0,+1,−1)` and in `(u,a,D,v)` are `(0,+1,−1,0)`. Their fixed surfaces normalize the nodal curve times the u-disc. They join globally to the horizontal `P¹×D²`. The other chart `u=xb,y=bzv`, in `(x,b,z,v)`, has weights `(+1,−1,0,0)` and fixed surface `x=b=0`, the compact vertical S. On the overlap `a=1/b`, so the two fixed components do not meet.

The compact fixed S has normal weight lines with Chern classes `n=m−F` and `−n`. Conjugating the negative weight converts the scalar normal rank-two bundle to `L_n⊕L_n`; the quotient normal R³ bundle is trivial. Its quasi-e discrepancy has square `γ²=n²=−2`. Thus its local expression `Sign(S)−4γ²=−8−4(−2)` vanishes. The horizontal component has signature zero and scalar-normal determinant zero (the original two weight lines restrict to O(−1), with opposite signs). These are untwisted local contributions. They do not prove that the finite logarithmic transforms preserve the boundary orbit invariant.

The nonsplit torsor constructed in B.3.6 may admit a relative-degree-zero line representing P because the Brauer group of the complex base curve vanishes. A height/Deligne-pairing argument should compute its square as −2; this has been communicated to A/B for verification. Even if established, its A-equivariant structure, the prescribed cusp matching, and a smooth filling with the correct boundary would still be needed.

## Other approaches tried and the precise missing step

- Taking `(MΦ×D²)/S¹` directly gives a cone on CP² along the fixed three-manifold. CP² has nonzero signature, so this is not a smooth eight-dimensional filling obtained by replacing each cone independently. A global fixed-surface cap and its normal data are needed.
- The Gromoll-filtration information in Crowley–Schick (2013), Appendix A, gives a proper subgroup in this dimension, but no membership of this specific Φ has been proved. Fibre preservation or circle equivariance does not supply that membership.
- Free circle actions and their characteristic bordism may provide surgery corrections; however even an empty-fixed-set six-dimensional pair with a nonzero Euler class has characteristic obstructions. Thus it is not valid to assert that modifications in the free region contribute zero merely because they avoid fixed points.
- The regular (3,4) Seifert fibre suggests ±1 surgeries with Brieskorn boundaries Σ(3,4,11) or Σ(3,4,13). Their suspended singularity signatures can be computed, but no comparison map between their handlebodies and the actual cusp-annulus twist has been constructed. Their natural circle fixed sets also differ. No numerical monodromy value is inferred from these examples.
- The determinant eleven in the untwisted intersection form does not justify adjoining a guessed E₈ or other plumbing. The surgery framings and the resulting boundary have to be established before such an intersection completion has meaning for this problem.

## Exact next target

Construct the global capped quotient pair for the annular γ-twist, preserving the circle-bundle class and the fixed normal framing, or construct an actual equivariant smooth cobordism from its mapping torus to a calculable boundary. Then either compute an embedded Seifert normal Euler square or use Moriyama's quasi-e signature formula. At present this comparison, including the finite-root/cusp overlap, is missing. No value, vanishing result, or nontrivial order bound for the actual [Φ] has been established by this attempt.

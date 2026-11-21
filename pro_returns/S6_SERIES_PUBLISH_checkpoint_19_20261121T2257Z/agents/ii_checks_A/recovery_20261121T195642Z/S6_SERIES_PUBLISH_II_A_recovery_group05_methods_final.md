# Final method comparison for 02WN–02WQ

This is a postrelease record. The four independent derivations froze on 2026-11-21 at 20:35:42 UTC. The complete target proofs were opened only after those freezes. The historical programs were subsequently opened in full and run at 20:43:54–55 UTC. This supplement does not create an additional independent check.

The geometric comparison, including the primitive cycle maps, all lifted-arc intersections, the degree-d² transfer, the alternate n=2 compactification and the normalization morphisms, is in `S6_SERIES_PUBLISH_II_A_recovery_group05_postrelease_cycle_transport.md`, SHA256 `ff53e1f9ef549ba29f54e6ef82fccc7c7a7115204b32d7f8803cc3acb89312f8`. Its final paragraph announced the computational supplement; that supplement is now complete as recorded here.

## Exact program provenance and timing

The pinned retrieval receipt is `records/S6_SERIES_PUBLISH_II_Milnor_programs_01/receipt.json`, with commit `83d76022bcd442278b760db9ff438afceed6c6ea`.

| Program | Source SHA256 | Scope actually opened |
|---|---|---|
| `milnor_intersection.py` | `85f4d954285277ad3a51ee75ba7e91fb99013ba73609fb3529c5935adce99127` | The entire 5,641-byte program: n=1,…,12; the n=2 alternative compactification; a=2,…,6 and n=1,…,6. |
| `binomial_milnor.py` | `ff922ea667ecc08d5059bed8ea0f43ea3d478f72c5379d9c76f60d75d2926016` | The entire 2,053-byte program: 64 exponent pairs, Bézout matrices, transfer squares, mixed normalization and Jacobian minors, and the WQ inverse. |

Both byte streams executed unchanged. A wrapper redirected only the three declared `Path.write_text` JSON destinations into prefixed files under `code/`. Source files and canonical files were not changed. `S6_SERIES_PUBLISH_II_A_recovery_group05_prior_runs.json` records exact start/end times, output paths, hashes and successful exit codes. I read all 46 and 67 output lines after these runs, including each parameter value and every concluding identity.

The prerelease program `code/S6_SERIES_PUBLISH_II_A_recovery_group05_local_certificate.py` has SHA256 `724084534248c4e1e776808c61610ac3f054d639f4011370cc97c0d2a75cbbec`; its output has SHA256 `1e8c2f2930dd9d0cd8c74803b051a4f2a3219eebdd64363160ae7254142bbe65`. It ran before all four freezes at 20:33:38 UTC. An earlier draft run is separately retained and is not substituted for this final prerelease program.

The first postrelease comparison program has SHA256 `b54ce2f1539f105dd91ef87c511ca401ed7df96683ab7e090c7be7be5d231ee1`, output SHA256 `1f6087abd69e1d3a5823225606206d5445ddf5a2f80648105cc5f126a6de66ad`, and ran at 20:40:03 UTC. Its recursive extended-Euclid routine overlaps the old `gcdex` method. That overlap is retained explicitly; it is not counted as a different algorithm.

The additional program `code/S6_SERIES_PUBLISH_II_A_recovery_group05_different_methods.py` ran at 20:48:46.326874–20:48:46.358556 UTC, exit zero. Its SHA256 is `1c4e396d2dafc7424414c021cfdcb96522c93b6489d40ad75890298c851c778c`; output SHA256 `932f8aef43b060a59f89f33d3b9f66a6e6d61416bf8a4a75bf2974a07abe10f7`; data SHA256 `f9ab35a1e6819c879dc731934cd7052760a062311b5681718efb19153aadf859`. I read its complete successful output.

## Computation-by-computation comparison

### WN: compactification, integral class and scaling

The historical program builds the intersection matrix Q and boundary matrix B, calls symbolic nullspace/rank operations on BᵀQ, takes a coordinate gcd to certify the generator and computes vᵀQv. The independent geometric derivation constructs the embedded sphere and its pulled-back normal bundle. Its preproof code uses incidence deleted-row minors: signed matching enumeration gives a unique nonzero term ±1 in each minor, and Cauchy–Binet gives the determinant. The postrelease boundary-coordinate map is an explicit integral isomorphism: chain coefficients are recovered from the final coefficient and successive differences. Restricting to the boundary kernel leaves the two opposite chain constants. This proves the primitive generator and its norm for every n, and the code verifies the same maps on the stated ranges.

The old graph routine uses an adjacency matrix and a connectivity search. The new argument gives every vertex its unique parent on the two exceptional chains or the two infinity branches. The root path is explicit and the edge count is one less than the vertex count. The preproof geometric argument is independent of that compactification.

The old blowup identities use symbolic cancellation. The final supplement clears b^n and evaluates `b^j*c*b^(n-j)-b^n*c` on a grid of n+1 distinct b-values and two c-values, using the proved separate degree bounds (n,1). It covers all 78 old charts, with 1,456 exact evaluations. Repeated univariate interpolation proves each fixed-parameter polynomial identity; the displayed exponent calculation proves the uniform identity for every n,j.

For the old n=2 compactification, the exact maps and inverse exceptional charts are given in the cycle record. The final supplement checks the cleared rational-chart numerator on a 3×3 grid, the exceptional-chart numerator on a 5×3 grid, with respective degree bounds (2,2) and (4,2). The boundary map `(a,b,c,d)→(a,a+b,b+c,a+d)` and its integer inverse are checked on both standard bases. Its kernel is therefore exactly Z·(1,−1,1,−1); the quadratic norm is certified on three points with degree bound two. This replaces the old symbolic matrix/nullspace computation by an explicit integral coordinate inverse and interpolation. The geometric identification with the independently derived sphere fixes the sign by its intersection with the same line x=1,y=0.

The two positive-weight choices are transported by `(x,y,z)→(x,r y,r^(−n)z)` on the equal-value fibre, with r=t^(−2). The unit-removal maps satisfy the same equation `g∘Phi=h g`; their composition is an explicit g-preserving local biholomorphism. Thus the different weight vectors retain the same compact class and its square.

### WO: all roots, integral primitivity and normalization

The historical general-lattice routine uses symbolic products, rank, determinant and an extracted maximal minor. The preproof signed-minor/Cauchy–Binet calculation and the postrelease integral chain-coordinate inverse use different algorithms. In the kernel, q₁+⋯+qₐ=0 and the root coordinates are kᵢ=Σ_{h≤i}q_h, with inverse qᵢ=kᵢ−kᵢ₋₁. This gives an integral basis for every a,n. The matching spheres and the exceptional-chain vectors correspond by their two endpoint intersections; the entire Gram matrix is −n times the A_{a−1} Cartan matrix.

The affine-chart code works in the explicit residue ring Z[ζ,y,u]/(ζ^a−1), verifies the hypersurface identity and the inverse after cross-multiplication, and covers a=2,…,9, n=1,…,5. This was written before the printed proof was opened. Its invariants are transported to the printed finite quotient map `(u,v)→(u^n v,u^a,v^a)`, with the faithful μ_a action. Both displayed A₁ examples and the smooth n=a quotient are checked through the exact coordinate maps in the comparison record. The analytic normalization proof establishes finiteness, generic degree, invariant normality and the induced finite birational map; it is not inferred from a finite polynomial sample.

### WP: Bézout choices, local and full pullbacks, and the mixed example

The old program uses `math.gcd`, `gcdex` and symbolic determinant evaluation. The final new program finds the common divisor by exhaustive divisibility and obtains p by searching all residues Bp modulo C, then q=(1−Bp)/C. Coprimality makes the C residues distinct, proving the search succeeds. It constructs the inverse of the two-by-two meridian matrix and checks it on the two basis columns. Only after computing this new data does it read the old JSON to compare choices.

For every old/new coefficient pair, p=p₀+Ck and q=q₀−Bk. Thus `M_new=[[1,0],[-k,1]] M_old`. The exact fibrewise coordinate transport is `(h,t_old)→(h,h^(−k)t_old)`. Substitution into y=h^p t^C and z=h^q t^(−B) recovers the old formulas. All 64 values of k are saved in the new JSON; no identification of unequal coordinates is asserted without this map.

The printed local class γ_l has square −2BC. The independent full pullback β is Σ_l γ_l, with d terms, under the factorization `F→Q_A→Q` of degrees BC and d². Each pair of distinct lifted matching spheres intersects at both endpoints with local sign −1. In oriented graph coordinates the transverse determinant is −|c_i−c_j|². The first postrelease program certifies this determinant by 81 exact values at separate degree two. Hence every local cross-pairing γ_i·γ_j is −2BC, including i=j; summing the complete d×d pairing matrix gives β²=−2d²BC=−2bc. The final program computes every entry for all old exponent pairs. The geometric cap perturbations, orientations, integral pullbacks and proper-map degree formula are proved in the cycle record; the arithmetic does not replace them.

For `(u,v)→(u³v²,v,u²)`, the coordinate permutation `(u,v)=(t,y)` transports the independent normalization and all differential minors, with the column-swap sign recorded. The old program differentiates symbolically and uses a symbolic gcd of minors. The new preproof program uses first-order dual arithmetic and 15 exact evaluations with separate degree bounds (2,4). Its three resulting minors generate `(u)`, because one is −2u and every other minor is divisible by u. The normalization polynomial identity has a separate 35-point exact certificate at bounds (4,6). The conductor follows by testing multiplication by the finite module generators 1,u; its all-exponent parity proof gives u²v²N. These are the same map, ideal and divisor as in the printed proof.

### WQ: union conductor and affine inverse

The new prerelease derivation computes the full conductor using the fiber product of component rings over C{x,z}/(x²), and the finite module generators 1,u for the Whitney normalization. It gives x² on the plane and v² on the Whitney component, with the identity and squaring maps on their reductions. The new preproof program records the semigroup-membership tests on all exponent pairs from 0 through 16. The proof for convergent series treats even and odd coefficients and therefore establishes the whole ideal.

The old affine inverse uses symbolic rational cancellation; the prerelease program uses exact Laurent exponent dictionaries. The final supplement additionally clears the denominator and certifies the inverse polynomial on 15 points at bounds (2,4), and the Whitney equation on 12 points at bounds (2,3). This gives an explicitly different interpolation algorithm. The exact isomorphism is `(x,y,z)↦(y,x)`, inverse `(y,x)↦(x,y,(yx²−1)/y³)`. The homotopy `(y,x)↦((1−s+s/|y|)y,(1−s)x)` retracts to S¹. The open-inclusion map on compact homology is conjugate under integral duality to extension by zero on compactly supported cohomology, preserving the cup-product evaluation and proving the zero-square assertion.

## Primary-source and editorial scope

Hatcher's author-hosted chapter PDFs were opened at Theorem 1.20, p.43; the Mayer–Vietoris sequence, §2.2, pp.149–150; the cap-product naturality passage, p.241; proper pullback/open extension and Theorem 3.35, p.245. Their exact use maps were bound in the independent derivations and cycle comparison. Theorem 4.32 and its proof, pp.366–367, were additionally opened after release for the printed Hurewicz use: author URL `https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf`, retrieval `turn108395216view0`, text lines 1814–1875. This is postrelease primary-input reading and is not assigned preproof input credit. The existing bibliography key `Hatcher2002` denotes the same Cambridge 2002 book and author URL.

The four complete original blocks and final proposed blocks were read. WN retains all six steps, the primitive integral vector, every common multiplicity and the unrestricted second Betti number. WO retains the integral lattice, both normalization phenomena and its exact finite quotient. WP retains the local square −2BC, all positive exponents, the exact mixed normalization, conductor and differential divisor; the independent global square −2bc remains in the check record with its explicit transfer. WQ states the local germ and the full zero-square conclusion directly, retaining both conductor multiplicities and the ramified squaring map. Its local-scope wording introduces no compact degeneration.

The 31 literal guards preserve all labels, hypertargets and hidden four-argument statement records. Enumeration wrappers remain for the root-owned global mapping. The two verified historical programs have complete end-table source rows with the pinned commit and full paths. A temporary grammar defect in the first WN proposal and an undefined F symbol in the first WQ proposal were corrected before the final comparative reread; neither defect was in the original source, and neither is assigned D25 original-error status.

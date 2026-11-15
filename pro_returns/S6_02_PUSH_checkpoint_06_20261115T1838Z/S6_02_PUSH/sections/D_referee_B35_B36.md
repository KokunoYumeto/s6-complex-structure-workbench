# Independent referee note: B.3.5–B.3.6

Read the current proofs in `AB_push.tex` in full. No substantive gap was found within their expressly stated scope.

For B.3.5, the pole orders `3i+4j`, with `0<=j<=2`, are pairwise distinct. The spaces of functions with poles at infinity of order at most two and three are therefore exactly the displayed spaces. A section avoiding the zero section has Weierstrass coordinates in those spaces; substitution leaves only `P` and `-P`. Every other nonzero section has height at least one. Once B.3.4 makes the invariant coefficient integral, any proper residual overlattice of index 2 or 4 contains one of the three nonzero half classes; their common height is `1/3`, giving the asserted contradiction.

For B.3.6, the following steps were checked independently:

1. The Hochschild–Serre transgression is onto because `H^2(K,E)=0` over the complex function field. The independent cohomological-dimension explanation in the proof is valid: the quotient of the geometric point group by its torsion subgroup is a rational vector space, and averaging on finite quotients kills its positive continuous cohomology.
2. At the ramified places the orders are exactly 3, 4 and 12, and `6P` lies in the identity component of the original Néron model. On that group, multiplication by each order is onto: solve first on the residue additive or multiplicative group over `C`, then use the étale multiplication map and Hensel's lemma. A division point defined already over the smaller local field is invariant and has norm `6P`.
3. Naturality of local Hochschild–Serre now makes the local torsor classes descend. Their finite support follows by spreading the torsor over an open subset and using local sections over strictly henselian smooth fibres.
4. The exact Ogg–Shafarevich localization statement needed here is applicable to the original nonconstant Jacobian (`j=1728t`). Subtracting a global class with the selected finitely many local descents keeps the transgression and makes the restricted class locally trivial over the cover. Compatibility at conjugate points follows from its Galois invariance.
5. A locally trivial genus-one torsor has the stated minimal regular model and the same local fibres. The generic affine lift extends: in a common resolution a terminal exceptional curve has square `-1`; if it were not contracted by the other projection its vertical rational image would have square at least `-1`, whereas the available vertical rational curves all have square `-2`. Repeated contraction of common exceptional curves proves extension and its inverse.
6. The twelfth power of the affine lift is a translation. Conjugation by the lift makes that section invariant. Its cyclic carry factor set represents the transgression, so its coefficient is `6 modulo 12`; translating the lift by a suitable integral multiple of `P` gives the exact equality `A^12=t_(6P)`. A possible global sign convention for the transgression is harmless for this order-two class, since `6=-6 modulo 12`.

The result is an existence theorem for an unramified torsor and its affine lift, not a threefold gluing or a smoothing theorem. In particular no characteristic numbers for the desired filling follow from it alone.

## Sources independently opened

- Cossec, F., Dolgachev, I., & Liedtke, C. (2024). *Enriques surfaces I*, author manuscript dated April 19, 2024. https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf . Opened and read Lemma 4.7.8, exact sequence (4.7.4), and Theorem 4.7.9 with the characteristic-zero portion of its proof, printed pp. 445–447 (PDF pp. 460–462, zero-based numbering). These are exactly the vanishing and localization statements used above.
- Xiao, G. (1991). *Elliptic surfaces with fixed jacobian* (MPI/91-30). Max-Planck-Institut für Mathematik. https://archive.mpim-bonn.mpg.de/id/eprint/2953/1/preprint_1991_30.pdf . Opened the introduction, the local fibre-twist construction, and §4, equation (4); the latter independently states the needed surjectivity in the nontrivial-Jacobian case.

These URLs and complete bibliographic metadata are already retained by AB in `AB_push_references.bib`; no duplicate keys are required.

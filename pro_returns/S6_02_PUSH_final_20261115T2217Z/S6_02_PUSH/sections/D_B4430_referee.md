# Independent full-source referee of the two-section bridge

**Reviewer:** boundary_d. **Date:** 15 November 2026, after checkpoint 09.

**Source reviewed:** sections/B_two_section_bridge_working.md, with the explicit replacements and precisions recorded below.

**Verdict:** PASS for the restricted noncompletion theorem concerning the fixed partial family B.4.19, after replacing the preliminary flattening paragraph by the proved coefficient-ideal equidimensionalization lemma in sections/D_B4430_equdimensionalization.md. This does not prove nonexistence of every r-only filling of the original six-sphere family.

## 1. Analytic log-de Rham input and saturation

I independently opened the complete original Illusie–Kato–Nakayama 2005 paper and its 2007 erratum. The exact applicable result is Theorem 6.3, with Theorem 6.2's hypotheses, on printed pp. 32–34. It concerns proper separated log-smooth fs analytic maps, with log-smooth base or exact map and torsion-free characteristic-group cokernels. A reduced semistable map satisfies the condition because the characteristic homomorphism sends 1 to (1,…,1). No Kähler or projectivity hypothesis occurs. The ordinary relative log-de Rham cohomology is the canonical nilpotent Gauss–Manin extension.

The 2007 erratum explicitly repairs the algebraic Theorem 7.1, not the analytic comparison used here. No Hodge-to-de Rham degeneration is imported.

The low-degree exact sequence

    0→F→H→R¹f_*O_Z

is correct, with F the kernel of the pushforward relative differential on log one-forms. The preceding boundary map vanishes because f_*O_Z=O_base and relative differentials annihilate base functions. Connected reduced compact central fibres imply f_*O_D=O_V; the multiplication-by-t sequence then gives no t-torsion in R¹f_*O_Z. Hence F is t-saturated.

The known Jacobian's normalized F_A is a genuine subbundle of the same canonical extension: subtracting the explicit logarithmic monodromy terms leaves holomorphic bounded unit-period columns and the w,δ columns remain the identity. Since F and F_A agree after inverting t and both are t-saturated, they agree as coherent subsheaves, including with the transverse parameter present. This does not assume local freeness or base change for the central H¹(O).

## 2. Integral residues and an actual convergent primitive

Local semistable angular generators are invariant under monodromy. At an exceptional base divisor with q=t^a times a unit and r=t^b times a unit, a,b>0, the actual H¹ monodromy has rank two and primitive invariant lattice Zw⊕Zδ. Therefore the two normalized angular periods are constant integers, uniformly in the transverse parameter.

The proposed power-series primitive is convergent. In xyz=t, a monomial x^i y^j z^k has relative weight (i−k,j−k). Closedness makes its coefficient vector proportional to that weight. A nonzero integral weight has an entry of absolute value at least one; division cannot create a convergence problem. The zero-weight terms are powers of t. Their coefficients are precisely the angular periods, so all nonconstant resonant terms vanish. Ordinary transverse coordinates are handled first by the holomorphic Poincaré homotopy. Thus the exponentiated primitive is an actual monomial times a holomorphic unit, not a formal or merely fibrewise construction.

## 3. A finite chart chain compares two extending sections

A compact connected NC central fibre is connected through finitely many semistable charts. Every nonempty open overlap meeting that fibre contains a smooth central point; a transverse holomorphic section through that point exists. These auxiliary sections and the finite chain persist after shrinking the transverse parameter disc. No extra root is required for honest sections at this stage.

For each section, the pulled-back product of the coordinate branches is t. Hence each coordinate is a power of t times a unit. Ratios of the local exponentiated primitives are therefore genuine logarithmic characters. Multiplication along the chart chain gives the difference of the two sections in the specified Jacobian, modulo its actual integral periods. Full positive monodromy valuations make every resulting integral ghost bounded. The construction is holomorphic jointly in both base variables.

This comparison is unaffected by a common essential affine translation. It does not contradict B.4.29, whose reference origin does not extend in the changed marking.

## 4. Equidimensionalization, finite traces, and uniform generic reduction

The full proof no longer needs a general flattening theorem. The separate auxiliary note proves the exact replacement:

* finite local projection of every excess-one point gives the actual reduced hypersurface image;
* its Taylor-coefficient ideal is a unit off the origin, because an identically zero noncentral fibre equation would force a three-dimensional fibre;
* a finite product of those ideals, using compactness of the origin fibre, is principalized by one proper base modification;
* division is convergent, and the strict transform has fibre dimension at most two;
* the dominant pure four-dimensional source over a smooth surface has fibre dimension at least two;
* normalized finite local slices are Cohen–Macaulay surfaces, hence finite-flat over the smooth base.

This yields all finite positive-degree traces used later without asserting flatness of the whole source.

For the subsequent generic semistable reduction, the strata must be the **closed intersections of globally marked SNC divisors**, not nonproper open strata. Resolve to simple NC first. Each closed stratum is proper over the compact exceptional base curve. Its nondominating image and the image of its critical locus are finite after discarding the curves that do not dominate. Removing these finitely many values gives simultaneous coordinates

    t=unit·∏x_i^(m_i),  u=u,  k≤3.

A common root degree divisible by the finitely many m_i gives toric height-one vertices. Use successive star subdivisions at all height-one lattice points in one global order on the finite marked cone complex. Shared faces then receive exactly the same subdivision, including any quadrilateral diagonal choices; independently triangulating different polygons without this common ordering would not suffice. All remaining two-dimensional lattice triangles are empty and hence unimodular. The monomial blow-up ideals are invariant under the unit changes of defining equations and glue. This gives proper smooth semistable local models uniformly in u, preserving the ordinary locus.

The normalized finite covers split after a cyclic root at a generic point of each exceptional curve. There are finitely many degrees and ramification indices, so a common finite root/norm multiplier can be chosen. Proper lifts of their sections through source modifications are meromorphic on smooth surface bases and are holomorphic away from isolated points; only finitely many such points meet the compact exceptional curves under consideration.

The explicit cyclic norm of τ^k times a unit is (−1)^(k(e−1))t^k times a unit. Changing a lift by a period changes its norm by an integral period. Thus norm descent is an actual character calculation and does not silently presume Kummer descent of the quotient sheaf.

## 5. Hartogs, the period ambiguity, and the multiplied cocycle

For a punctured smooth bidisc, H¹ with coefficients in the constant lattice Y=Z² vanishes. Thus an A-section lifts to the exact bounded character sheaf. Divide each character by its fixed boundary monomial; the resulting function and its inverse both extend by Hartogs and remain reciprocal. The first character retains zero order on the strict r-boundary, as required by B.4.27.

Uniqueness is correctly proved after retaining the Y ambiguity: the difference of two character lifts is one constant integral period on the connected puncture. Subtract it and apply the identity theorem. Consequently all cocycle identities extend.

After a common degree and norm multiplier, finite multisection traces provide local origins of a positive contracted power of the actual punctured torsor. Their differences extend generically along every exceptional curve and then across the remaining finite set by Hartogs. These differences glue an A-torsor over the entire modified base. B.4.27 makes it trivial, whereas B.4.24 excludes every positive multiple of the actual r-loop γ class. This is the required contradiction.

## 6. Exact scope

The conclusion applies to the fixed partial family B.4.19, including its prescribed rank-one axial completion. It allows proper origin fibres of dimension three and arbitrary finite point modifications of the base; the coefficient-ideal argument then manufactures an equidimensional dominating strict transform.

An arbitrary r-only filling can change the r=0, q≠0 model after resolving the graph of the intrinsic q-map. Rank-one monodromy has an additional elliptic invariant direction, so the local argument alone does not force the residues needed on that axis. A separate global-monodromy argument is being investigated; it is not part of this PASS.

## Primary records independently opened

Illusie, L., Kato, K., & Nakayama, C. (2005). Quasi-unipotent logarithmic Riemann–Hilbert correspondences. *Journal of Mathematical Sciences, the University of Tokyo, 12*, 1–66. Theorems 6.2–6.3, printed pp. 32–34. https://www.ms.u-tokyo.ac.jp/journal/pdf/jms120101.pdf . Opened; latest independent retrieval turn678view2.

Illusie, L., Kato, K., & Nakayama, C. (2007). Erratum to “Quasi-unipotent logarithmic Riemann–Hilbert correspondences.” *Journal of Mathematical Sciences, the University of Tokyo, 14*, 113–116. https://www.ms.u-tokyo.ac.jp/journal/pdf/jms140105.pdf . Opened in full; latest retrieval turn678view3. Scope is the correction to Theorem 7.1.

Parusiński, A. (1990). *Subanalytic functions* (MPI/90-58). Max-Planck-Institut für Mathematik. Corollary 1.2 and full proof, original PDF pp. 4–7. https://archive.mpim-bonn.mpg.de/id/eprint/1622/1/preprint_1990_58.pdf . Opened and independently read, latest retrieval turn678view0. Published metadata: *Transactions of the American Mathematical Society, 344*(2), 583–595 (1994), DOI 10.2307/2154496.

Enokizono–Hashizume's analytic toroidal-modification Lemma 2.14 was independently opened by E and root; the present review checks the finite star-subdivision construction directly. Their projective main theorem is not used. The inaccessible original Hironaka flattening article is not claimed as read and is no longer a necessary dependency.

# Prerelease derivation: 03II / wbII:prop:analytic-base-change

Checker: i_provenance_recovery. The exact target statement and empty supplement were read. The target proof, another checker's target reconstruction and historical check outcomes remain unopened. I read the primary finite-free-complex input in Adrien Douady, Le théorème des images directes de Grauert [d'après Kiehl–Verdier], Astérisque 16 (1974), §6 Theorem2 and its construction, §7, and §8, printed pp.59–62. The separate Grothendieck Corollary1.4 proof remains closed. This is a derivation from Douady's complex model, not from the target conclusion.

Exact primary PDF: records/S6_SERIES_PUBLISH_II_analytic_primary_inputs_01/Douady1974.pdf, SHA256 4fd29bf08b01c94d22c7fb4bcac67d3dd31b0754ea20d210e8c897dc3bb7cbbd. Primary URL https://www.numdam.org/article/AST_1974__16__49_0.pdf. I read its text at the cited loci; the root's separate image-reading receipt is not credited as my page reading.

Douady constructs locally on B a right-bounded complex K of finite free analytic modules, together with a comparison to the relative Čech complex, whose cohomology sheaves are R^q f_*F. His §8 uses the stipulated f-flatness of F to show that the same comparison on the fibre identifies H^q(K tensor k(c)) with H^q(X_c,F_c). It does not assert that tensoring an individual cohomology module always commutes with cohomology. The latter is the remaining algebra here. No globally bounded free resolution is assumed.

Work in the local ring A=O_{B,c}, maximal ideal m and residue field k. In any differential d:M->N of K, a matrix entry whose value in k is nonzero is a unit of A. Put such an entry in the first row and column. In decompositions M=A plus M' and N=A plus N', write

    d = [[u,b],[c,D]],  u a unit.

Multiplication on the target by [[u^{-1},0],[-c*u^{-1},I]] and on the source by [[1,-u^{-1}b],[0,I]] gives diag(1,D-c*u^{-1}b). These are explicit invertible basis changes. Since consecutive differentials compose to zero, the previous differential has zero component into the isolated first source factor, and the next has zero component from the isolated first target factor. Thus this pair of factors is the contractible complex A --1--> A. Projection pi to the remaining summand and inclusion iota are chain maps. The map h taking the isolated target generator back to the source generator satisfies id-iota*pi=d*h+h*d. These identities survive tensoring with every A-module. All finitely many unit inverses in the following argument exist on a base neighbourhood after shrinking.

Apply this cancellation only to entries of d^2:K^2->K^3 or d^3:K^3->K^4. The hypothesis and Douady's fibre comparison give H^3(K tensor k)=0. While K^3 has positive rank, d^2 tensor k and d^3 tensor k cannot both be zero, because then this H^3 would be K^3 tensor k. A nonzero entry of one of the two maps gives the unit cancellation above and reduces the rank of K^3 by one. Homotopy equivalence preserves H^3 of the fibre. The process terminates after at most the initial finite rank of K^3 cancellations, with an explicitly homotopy-equivalent complex K' having K'^3=0. This argument only uses finite ranks in the displayed neighbouring degrees.

Now d'^2 is zero, so

    H^2(K') = coker(d'^1:K'^1->K'^2).

Tensor product is right exact; its quotient map sends [v] tensor a to [v tensor a]. It therefore gives an isomorphism

    H^2(K') tensor_A k
      -> coker(d'^1 tensor_A k)
      = H^2(K' tensor_A k).

The chain maps pi and iota and their explicit tensor-compatible homotopy identify this map with the canonical map H^2(K) tensor k -> H^2(K tensor k). Douady's comparison is induced by the relative Čech restriction map on every fibre. Consequently the last map is precisely the canonical beta_c^2 in the target, under the stated identifications of R^2 f_*F and fibre cohomology. It is an isomorphism. The proof works in the local analytic ring itself, including nilpotents; the only invertibility test used is nonzero residue in its residue field.

# Toroidal weak factorization: source and scope audit

Opened 2026-11-15, approximately 15:27–15:39 UTC. This is a proof-development record; it does not silently promote the proposed all-fan homology formula.

## Primary sources opened

1. Abramovich, D., Karu, K., Matsuki, K., & Włodarczyk, J. (2002). Torification and factorization of birational maps. *Journal of the American Mathematical Society, 15*(3), 531–572. https://doi.org/10.1090/S0894-0347-02-00396-X. Author-hosted published PDF: https://personal.math.ubc.ca/~karu/papers/semist.pdf.
   - Theorem 1.6.1, p. 543: proper toroidal birational maps of nonsingular embeddings admit toroidal weak factorization. The statement does not require complete source/target objects.
   - Theorem 2.7.1 and its proof, pp. 551–552: the factorization consists of smooth toroidal blow-ups and blow-downs; the proof is a finite polyhedral-complex construction, using an embedding of a barycentric subdivision, a fan cobordism, and nonsingular star subdivisions.
   - Section 5.5, p. 565: analytic toric charts are Euclidean open embeddings; boundary self-intersections are permitted before strictification. For strict analytic toroidal embeddings, the polyhedral-complex/subdivision construction applies in the analytic category.
   - Section 5.6, pp. 565–566: the analytic factorization is obtained from the same combinatorial factorization. Its displayed opening hypothesis says complete embeddings. To treat the present proper-over-disc spaces, one must explicitly use the finite cone complex and the subdivision-to-analytic-modification correspondence, not cite the compact-manifold theorem as if it were a relative theorem.
   - Section 0.4, p. 534 expressly cautions that the general relative-DVR version is not stated. The current argument is restricted to an already constructed finite toroidal cone complex.
   - Web retrievals: turn222view0; turn223view2/3; turn224view0/1.
2. Matsuki, K. (2000). Erratum to the paper “A note on the factorization theorem of toric birational maps after Morelli and its toroidal extension.” arXiv:math/0006038. https://arxiv.org/pdf/math/0006038.
   - Section 2, p. 2: the corrected weak factorization theorem for proper toroidal birational morphisms of nonsingular embeddings without self-intersections uses smooth irreducible **closed strata** as centres, and all intermediates are toroidal over the target.
   - Section 1: the old strong-factorization algorithm is invalid. No strong-factorization theorem is used here.
   - Web retrieval: turn222view1.

## Proposed argument requiring explicit verification

The A.2.4 outputs have smooth total spaces, finite periodic cone complexes, explicit proper common toroidal modifications, and monomial parameters q and r. Refine q=0 union r=0 to a strict boundary, then use finite-complex weak factorization. Temporary pure-q blow-ups must be permitted: strictification need not preserve the punctured r-family.

Every nontrivial blow-up centre has complex codimension at least two. Candidate centre types are:

- Mixed cones: trivial period stabilizer; a smooth closed centre is a complete smooth toric point, curve, or surface.
- Pure top two-cones: the residual G1 period makes a surface birational to S; after earlier modifications it need not literally equal S, but is a smooth rational surface.
- Pure bottom two- or three-cones: trivial stabilizer; a toric surface or curve proper over the r-disc, with central support a chain of rational curves or one point. Ordinary cohomology is free and even; H0=Z and H4=0.

The ordinary integral blow-up formula would therefore preserve all odd cohomology and all torsion. Every connected centre adds one b2 and one boundary prime divisor. Compact centres add one b6 and one central prime divisor; pure-bottom centres add neither b6 nor a central divisor. Consequently b2 minus total boundary-ray count and b6 minus central-ray count are invariants. Both endpoints have one pure-bottom ray orbit, so the expected formula is b2=8+k+m and b6=k+m.

Together with A.4.7 and a direct integral Mayer–Vietoris calculation for the reference n-cycle, the candidate Betti tuple is

    (1, 1, 8+k+m, 7, 9k+t4−2m−1, 0, k+m).

Remaining checks before promotion: (i) give the finite analytic cone-complex factorization argument with strictification explicitly; (ii) verify the listed centre types including normalization/period identifications; (iii) write the reference n-cycle integral Mayer–Vietoris reductions; (iv) justify the noncompact-centre blow-up splitting without a Kähler hypothesis.

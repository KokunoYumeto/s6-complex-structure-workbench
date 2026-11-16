# Analytic Hopf-leaf neighbourhood audit — 2026-11-16

## Exact remaining task

UN77 now produces actual smooth unblown maximal-order Hopf components by overlap-compatible sigma modifications. The next unresolved map is an inverse logarithmic surgery on the **given threefold neighbourhood**, preserving its punctured torus family and all higher analytic transition terms. UN60/61 classify and prune marked central surfaces/torsors and construct new compact realizations; they do not supply that neighbourhood map. UN70 supplies an actual elliptic fibration on the parent surface, but no extension to the original threefold neighbourhood has been proved.

## Primary sources read

1. Anna Abasheva and Rodion Déev, *Complex surfaces with many algebraic structures*, arXiv:2303.10764v1 (19 March 2023), later IMRN 2024, no. 9, 7379 ff., DOI 10.1093/imrn/rnad190. Primary PDF: https://arxiv.org/pdf/2303.10764 . The introduction and §2.5 invoke an actual holomorphic tubular neighbourhood obtained from Arnold–Ueda under a Diophantine degree-zero normal-line hypothesis. That hypothesis is nontorsion. The construction compares complements of the actual line-bundle neighbourhoods and glues a Hopf transform. No extension theorem for the torsion-normal threefold smoothing neighbourhood required above has been found in this source.

2. Osamu Suzuki, *Neighborhoods of a Compact Non-Singular Algebraic Curve Imbedded in a 2-Dimensional Complex Manifold*, Publ. RIMS, Kyoto Univ. **11** (1975), 185–199. Primary PDF: https://ems.press/content/serial-article-files/41816?nt=1 . Theorem 3, §5, pp. 196–197, computes the elliptic axis in the nonlinear Hopf quotient
   \[
   (z_1,z_2)\longmapsto(\alpha_2^m z_1+\lambda z_2^m,\alpha_2z_2),\qquad\lambda\ne0.
   \]
   Its normal bundle has finite order, while the algebra of holomorphic functions on a sufficiently small axis neighbourhood is just the constants. The displayed invariant meromorphic two-form gives \(K_H=-(m+1)C\) and hence \(N_C^m\simeq\mathcal O_C\). The primary source explicitly records that finite-order normal data alone are insufficient for its neighbourhood-function problem. This directly prevents deriving a transverse holomorphic coordinate from torsion of the normal line alone.

3. Yoshio Fujimoto, *Logarithmic transformations on elliptic fiber spaces*, J. Math. Kyoto Univ. **28** (1988), 91–110. Primary scan: https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf . Section 1 starts with an actual elliptic fibration and its period functions. Theorem 2.1 additionally assumes that the base curve has an analytic tubular neighbourhood isomorphic to its normal bundle. These constructions therefore require geometric maps beyond the surface-level torsion-normal data available here. The printed Theorem 2.8/Corollary 2.10 must not be used: the project's explicit weighted diagonal Hopf threefold map to \(\mathbb P^2\) already contradicts their stated divisibility assertion.

## Verified conclusion and exact obstruction

The sources above do not establish the required arbitrary-neighbourhood inverse operation. The missing datum is an actual holomorphic comparison of the smoothing transition functions (or of their universal-cover deck maps), including all higher terms, with a model on which inverse surgery is defined. A compact elliptic orbit in the central component need not deform as a compact elliptic curve in a nearby torus, so no nearby elliptic quotient fibration may be inserted without proof. No new theorem or completion claim is made in this audit.

## Tool references available in this session

- arXiv PDF: `turn782view0`.
- Suzuki primary PDF: `turn780view0`, exact §5 passage `turn782view1`.
- Fujimoto primary scan: `turn773view1` (earlier in this agent's context).

Parent received these findings before checkpoint12. Promoted mathematical sources remain unchanged by this note.

# Further cusp-extension literature audit

Owner: limits_ab. 15 November 2026, approximately18:05–18:55UTC.

## Logarithmic complex tori

Opened and subsequently reopened the primary Kajiwara–Kato–Nakayama paper:

Kajiwara, T., Kato, K., & Nakayama, C. (2008). Logarithmic abelian varieties, Part I: Complex analytic theory. *Journal of Mathematical Sciences, the University of Tokyo,15*,69–193. https://www.ms.u-tokyo.ac.jp/journal/pdf/jms150104.pdf

Read Definition1.3.4, Proposition3.9.1, Proposition3.9.2, Example3.9.3 and Theorem5.1.3. Definition1.3.4 does not impose a polarization. Theorem5.1.3 supplies proper models locally on the base once a log complex torus is given. Proposition3.9.1 is fully faithful restriction inside that category; it is not a comparison theorem for arbitrary proper analytic completions. Proposition3.9.2 gives extension for polarized abelian varieties with unipotent monodromy, while Example3.9.3 explicitly shows that an arbitrary nonpolarized complex-torus family on a punctured bidisc need not extend as a log complex torus. No theorem here identifies all possible analytic caps with the toroidal models in PartA.

The actual cusp has the admissible diagonal valuation pattern already used in PartA, but its affine comparisons at the other base points are additional data. The quadratic logarithmic gauge of B.4.9 does not become a meromorphic boundary comparison merely by invoking the log-torus theorem.

## Equivariant deformations and the auxiliary third component

Opened the original Cathelineau1978 paper at https://www.numdam.org/article/ASENS_1978_4_11_3_391_0.pdf and the original Rim1980 scan at https://scispace.com/pdf/equivariant-g-structure-on-versal-deformations-3i8iymesgm.pdf. Cathelineau's definition onp391 keeps the group action over a trivial base action; his Theorem1 onp392 therefore cannot be used directly to globalize a smoothing parameter of nonzero weight. Rim's theorem is formal/algebraic and was not used as a convergent analytic theorem for the nonalgebraic singular compact surface. The direct character calculation instead appears in `sections/ab_push_kato_weights_referee.md`, with exact code and output in `code/ab_push_kato_weights.py/.out/.json`. It uses the opened original Atiyah–SingerIII holomorphic Lefschetz theorem, Theorem4.6,p566, with the bibliography key already owned by E.

## General simple-torus and maximal-degeneration searches

Queries included:

- `"degenerations of complex tori" "Hopf"`
- `"non-Kähler" "torus" "maximal" degeneration`
- `"Nishiguchi" "complex tori" degeneration`
- `"Ueno" "non-Kähler degenerations"`
- `"Differential geometric global smoothings" complex tori`
- `"degenerations" "complex tori" "Hopf" simple`

Both search engines were used in successive calls. These searches did not locate a primary theorem classifying every proper analytic completion of a generically simple two-torus family. This is a search result, not a nonexistence claim. The earlier Oda1978 TIFR volume was read at its working primary URL; a later alternate URL, https://mathweb.tifr.res.in/sites/default/files/publications/ln/tifr58.pdf, returned404 and was not used as a new opened source.

Ueno's1983 original *On non-Kähler degenerations of complex tori* remains unlocated. Its existence and description are attributed only to the opened Fujimoto1990 Remark1.4, not to an imagined reading of the original. Fujimoto's exact elliptic-bundle examples and their limitations are treated by the parent's separate literature section.

## A nearby smoothing theorem that does not close the analytic gap

Opened the publisher's full primary HTML of:

Doi, M., & Yotsutani, N. (2023). Differential geometric global smoothings of simple normal crossing complex surfaces with trivial canonical bundle. *Complex Manifolds,10*(1),20220143. https://doi.org/10.1515/coma-2022-0143

Working opened URL: https://www.degruyterbrill.com/de/document/doi/10.1515/coma-2022-0143/html, reached through the search-result language redirect. The direct arXiv2203.09304v2 PDF returned DisabledError, and the shorter publisher /document/ URL returned405. These failed requests are not treated as readings; the redirected full publisher article was successfully opened.

Read Theorem1.3 and the explicit comparison in the Introduction. Its total space and parameter map are smooth, and the complex structures on the compact surface fibres vary continuously; the authors explicitly distinguish this from a holomorphic smoothing. The theorem requires a trivial canonical bundle and compatible residue volume forms. It does not construct the proper holomorphic fourfold needed in PartB. Its discussion of modern logarithmic smoothing theorems is not substituted for checking their algebraic/analytic hypotheses. No result of this paper is used in B.4.15 or B.4.16.

## Current constructive scope

B.4.15 is an actual local two-parameter replacement preserving the prescribed punctured simple-torus family. It avoids the unproved general classification entirely by constructing the semiabelian action, Cartier cocycle, global ideals, proper local models and normalization components explicitly. B.4.16 proves that this generated class still preserves the old dual-circle class. A different cusp attachment is required to alter the peripheral component transport or kill that class. Neither the literature search nor the local construction resolves that final global extension problem.

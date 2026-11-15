# Corner literature and active interface search

## 2026-11-15, 19:50–20:10 UTC

Search engine 2 queries:

- degeneration complex tori Hopf components normal crossing elliptic curves simple torus
- Nishiguchi degeneration torus Hopf surfaces type II components
- Fujimoto simple complex torus logarithmic transformation degeneration Hopf

Engine 1 verification queries:

- Schroer Siebert irreducible degenerations primary Kodaira surfaces Hopf tori arxiv
- Nishiguchi degeneration surfaces trivial canonical bundle complex torus Hopf component elliptic

Opened the primary author PDF:
https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/kodaira.pdf

Schröer, S., & Siebert, B. (2002). Irreducible degenerations of primary Kodaira surfaces. In I. Bauer, F. Catanese, T. Peternell, Y. Kawamata, & Y.-T. Siu (Eds.), *Complex geometry: Collection of papers dedicated to Hans Grauert* (pp.193–222). Springer. The author PDF has25pages and its own1–25pagination. The primary publisher table of contents was also retrieved at https://link.springer.com/book/10.1007/978-3-642-56202-0. Chapter DOI reported by the author-uploaded ResearchGate entry is10.1007/978-3-642-56202-0_14; that DOI has not yet been opened directly, so it is not used as independently verified metadata.

Scope audit (paraphrase, under200words): The introduction explicitly obtains a partial parameter completion P1×Delta minus(infinity,0). Section6, especially Proposition6.3 (authorPDFpp22–23), constructs a proper two-parameter quotient with a product-of-nodes singularity joining elliptically ruled and Hopf-normalization strata. Theorem5.4 (pp18–20) displays the infinite toric fan and the group action. The relevant positive-degree families are elliptic principal bundles and hence do not identify the prescribed generically simple two-tori. Theorem6.2 additionally assumes a total space bimeromorphic to a Kähler manifold. Neither theorem supplies the missing actual S6 corner. Their constructions and explicit limitations are useful precedents, not novelty or a transfer theorem.

Independent route under investigation: the other axis in our already proved B.4.10 Kato family is the Cartier divisor pi_n^*w−s=0. Its collar factor is exactly a(s); its generic curve is E_{kappa(s)s^n}, and its reduced central curve is I_n. This can match the actual Tate root interface and its P normal. The relative neighbourhood has s=uv−h, not the normal-line projection s=uv. Consequently a normal-line match does not supply the second period or the actual Mumford node smoothing. This calculation is being isolated as B.4.20, with explicit scope.

Read-only path guesses `ab_push_cusp_torsor.tex` and `ab_push_kato_family.tex` did not exist. The correct existing files were located with rg: `ab_push_torus_log_cocycles.tex` and `ab_push_parabolic_insertion.tex`. These were lookup failures only; no source or computation was lost.

One patch adding the exceptional-curve limitation to B.4.20 failed atomically because its context omitted the preceding words on a wrapped source line. The exact tail was read and the narrow patch then succeeded. No mathematical calculation failed.

At20:10UTC the publisher chapter page was successfully opened directly:
https://link.springer.com/chapter/10.1007/978-3-642-56202-0_14
It confirms authors,2002,pp193–222,editors and DOI10.1007/978-3-642-56202-0_14. Thus the earlier metadata qualification is superseded. The first open call was aborted before dispatch; the identical follow-up succeeded. No inaccessible-source contents were inferred.

## 20:36 UTC: further primary checks

Reopened the same author PDF and Fujimoto's original1988 journal scan at https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf. In Schröer–Siebert, Proposition3.5 and Theorem3.10 restrict the irreducible d-semistable K-trivial Hopf-normalization case to positive degree and Kodaira smoothings. Corollary5.6's proof gives a smooth four-dimensional versal base for the degree-zero rational-normalization case. These hypotheses do not classify our reducible or vertical threefold caps. No new general completion theorem was found or assumed.

The B.4.22 first-run exact output is preserved as `code/ab_push_corner_resolution_first_run.out`. Its single assertion failure was expanded-versus-factored polynomial structural equality; the corrected zero-polynomial comparison and every preceding finite check pass. The separate B.4.21 referee calculation passed on its first run. A repeated read-only old path guess `ab_push_cusp_torsor.tex` failed; the already known actual source is `ab_push_torus_log_cocycles.tex`. No mathematical source was lost.

# Renewed primary-source openings and credit: Paper VI

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

This receipt records actual reopened loci, not an entire-source reading claim. Mathematical proof events are recorded separately. An absence of a matching statement in the inspected loci is a bounded search observation and supplies no proof of universal priority.

## Main theorem and displayed local results

The claims being compared are G.1 (every support nonnegative, global values 0 or 2, complete zero criterion), UN.1 (local even Euler number), UN.2 (every even value after explicit vertical blowups), INT.1–3 (interfaces, Enoki exclusion and conductor equality), and MH.1–2 (analytic support comparison and finite-character Euler calculation).

| Opened primary material | Exact location | Credit and receiving scope |
|---|---|---|
| Supplied original AC26 PDF, 108 pages | Printed p.4, complete introductory theorem; p.30 Corollary 4.8 and displayed covering argument; p.51 Euler calculation preceding Proposition 7.12; p.60 Theorem 7.22 and its Euler/Betti argument | The specified completed torus family and the computation e(X)=e(W)=2 are already stated and computed there. Its toric support is obtained from dP6 by the explicit edge identifications. G.1 credits that value and example. The global sign and full equality statement for every family under its stated Betti hypotheses were not identified in these opened loci. |
| Engel, supplied `S6.tex` | `main-thm` at source line 882; complete `euler-characteristic` proposition and proof at line 1270 | The Euler computation uses exactly two zero-dimensional toric strata and vanishing Euler number of all positive-dimensional strata; both reduced bielliptic fibres have Euler number zero. This is credited for the existing example, and for the toric-strata mechanism used by C2c. |
| DGKX supplied v1 source | `nm:thm:oka-local`, line 226; `thm:intro-point-modifications`, 259; `p2:thm:kuranishi-aut`, 310; `p2:thm:exact-period`, 335; `thm:relative-cusp`, 2028 | Opened the exact Oka, deformation/automorphism, period and relative cusp statements. The cusp statement gives a proper analytic quotient with reduced irreducible nonnormal normal-crossing central surface and toric normalization. These construction claims retain their source credit; no general support-sign/equality theorem was identified at these loci. |
| DGKX supplied v2 source | `nm:thm:oka-local`, line 225; `thm:intro-point-modifications`, 271; `thm:relative-cusp`, 1714; relative compactification theorem and finite-puncture theorem | Opened the retained Oka and relative construction statements, separately from v1. The source titles and versions are kept distinct. No inference about the authors' reason for version changes is made. |
| Kamenova, author-hosted four-page manuscript | Section 1, p.1; Theorem 3.1, p.2, including all four cases | The printed hypotheses are semistability, a Kähler total space and trivial total canonical bundle. The torus/elliptic-ruled/rational-stratum classification is credited under exactly those hypotheses. The receiving arbitrary analytic support arguments explicitly prove their own comparison maps. |
| Steenbrink, arXiv math/9902134v1, 23 February 1999 | Complete algebraic ambient hypothesis in introduction; Section 3 Theorem 1 and Corollary 2; Section 4 equation (3) | Credit for logarithmic quotient complexes and the support cone in the complete algebraic setting. The actual analytic-neighbourhood, compact-projective-strata filtered map required by MH.1 is supplied in `007_MH1_comparison.md`; its broader form is not attributed to the cited paper. |

The original AC26 PDF p.4 was rendered and visually inspected. Other listed AC26 loci were read from newly extracted original-PDF text, not from the transcription. The transcription remains an aid only. The original PDF SHA256 is `283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2`. Its extracted text and p.4 rendering are in this directory.

The exact supplied TeX hashes are:

* Engel: `95ea78327c33351d609a3001539756f0043dfdef13a37a81927608c953c98c36`.
* DGKX v1: `924a4a72d80793927f3104121a44786ea2b9869ae6ea2bca5a6a69553ab2884e`.
* DGKX v2: `a2013b8390b1eba4f9c57eb78597eb3b8b6ac09c50714492c6912803a8bebe50`.

The source-wide searches were case-sensitive and reproducible: Engel has three `Euler` hits, one `euler` hit, no `nonnegative` or `non-negative` hits, and five `c_3` hits (the latter concern period-coordinate notation). Both DGKX versions have no `Euler`, `euler`, `c_3` or `c_{3}` hits; their two `nonnegative` hits concern toric character pairings. These searches only supplement the opened statements; they do not establish an exhaustive absence theorem or a priority claim.

## Exact reopened inputs used in the completed proof comparisons

| Source and opened locus | Receiving rows and verified use |
|---|---|
| Peters 2021, Proposition 2.1 and Theorem 2.2, pp.842–843, original journal PDF | G.1, INT.1 and surface classifications: even b1/Kähler equivalence and the κ=−∞ surface alternatives. |
| Brînzănescu–Moraru 2005, Lemma 2.2 and Proposition 2.3, pp.1664–1666; explicit quotient and Picard description p.1667, original journal PDF | INT.1: finite cyclic removal of multiples, the principal elliptic model Θ*/τ, and the actual Picard restriction to an elliptic fibre. |
| Dloussky–Teleman, arXiv 1012.5247v2, Remark 2.7, printed p.9 | INT.1–2, UN.17/19: effective homologically trivial divisor gives the stated Hopf/Enoki alternatives under the printed minimal class-VII hypotheses. |
| Dloussky, arXiv math/0406387v3, Theorem 0.2, printed p.2; Lemma 2.22 and following paragraph, printed p.15 | UN.17: the proved numerically anticanonical-divisor implication to GSS. INT.2: the parabolic Inoue case with elliptic curve and rational cycle. No conjecture printed near Theorem 0.2 is substituted for that proved implication. |
| Guillot, author-hosted chapter, Theorem 3.3 p.9 and Theorem 9.2 p.28 | UN.15/16/20/22/26: closedness of uniformizability in the stated dimensions, and the compact-surface meromorphic semicomplete-field classification. |
| Guillot, arXiv 1603.02288v2, Main Theorem p.2 and Proposition 22 p.25 | UN.15/22: dense-leaf alternatives under the actual compact Kähler hypothesis; the receiving projective branch satisfies it. |
| Dloussky–Oeljeklaus–Toma 2000, original publisher PDF p.256; 2001 paper, Theorem 0.3 pp.641–642 | UN.16/17: the field-space bound and minimal surface alternatives at the stated hypotheses. |
| Inoue 1974, original journal scans pp.274,277,280, Propositions 2(ii),3(ii),5 | UN.16: exact tangent-field dimensions 0,1,0. All three scans were rendered and visually read; PNGs are in `source_scans/`. |

The URLs opened in this continuation are recorded explicitly for reproducibility:

* Peters: https://nyjm.albany.edu/j/2021/27-32p.pdf
* Brînzănescu–Moraru: https://aif.centre-mersenne.org/article/AIF_2005__55_5_1659_0.pdf
* Dloussky–Teleman: https://arxiv.org/pdf/1012.5247
* Dloussky: https://arxiv.org/pdf/math/0406387
* Guillot chapter: https://www.matem.unam.mx/~guillot/guillot-singularities.pdf
* Guillot 2019: https://arxiv.org/pdf/1603.02288
* DOT 2000: https://ems.press/content/serial-article-files/42865?nt=1
* DOT 2001: https://ems.press/content/serial-article-files/42912?nt=1
* Steenbrink: https://arxiv.org/pdf/math/9902134
* Kamenova: https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf

UN.5's renewed Buchdahl and Catanese openings are recorded by the parent in `analysis/continuation_root/D3_UN5_comparisons.md` and the root event ledger. The exact pending source openings for A’Campo, Kodaira/Ulmer–Urzúa and the Hopf normal forms will be appended only after they are performed. Earlier bibliography verification prose is historical evidence and is not converted into a new opening by copying it.

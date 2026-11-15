# B.4.11: elliptic contraction and globalization audit

Owner: boundary_d. Date: 2026-11-15. Root independently passed the full proof before integration. AB was also asked to audit the explicit Kato geometry.

## Exact result and scope

The result is about the auxiliary parabolic surface `S_8(a,kappa)` constructed in B.4.10. Its negative elliptic axis has an actual linear tubular neighbourhood, not merely a specified normal bundle. Contracting it gives the cone over the elliptic curve with the positive degree-eight line. The proof computes `H^2(Y,Theta_Y)=0` and proves regularity of the global-to-local deformation map. A specified local analytic smoothing component can therefore be globalized over a small disc.

This does not construct the requested punctured S6 comparison, a compact third threefold component, or its gluing to the original S6 family. A proper family over an open disc is not an absolute compact threefold. The parent owns the explicit local Q-cone smoothing and the next construction/scope statement.

## Primary sources actually opened

1. Grauert, H. (1960). *Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen*. Publications Mathématiques de l'IHÉS, 5, 5–64. https://doi.org/10.1007/BF02684746 . Original Numdam PDF: https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf . **Opened** §6, Hauptsatz IIa, printed p.59 (PDF page index57): the analytic theorem on formal functions. Existing bibliography key `Grauert60push` is reused. No appeal is made to the incorrect closedness assertion corrected in the 1963 erratum to §7 Satz2.

2. Dloussky, G., & Teleman, A. (2020). *Smooth deformations of singular contractions of class VII surfaces*. Mathematische Zeitschrift, 296, 1521–1537. https://doi.org/10.1007/s00209-020-02481-0 . **Opened** primary author manuscript https://arxiv.org/pdf/1803.07631 , version2 dated28February2020; §3.2, Proposition3.3 and the discussion immediately preceding Proposition3.4, manuscript p.11. **Opened** publisher metadata https://link.springer.com/article/10.1007/s00209-020-02481-0 . Proposition3.3 is formulated for a compact complex space with a single isolated singularity and a regular global-to-local base morphism. The discussion invokes the general H²Theta criterion via Manetti's Lemma1, p.93. The rational-cycle hypotheses of their Proposition3.4 and Theorem5.2 are not transferred to the elliptic contraction.

3. Istrati, N., Otiman, A., Pontecorvo, M., & Ruggiero, M. (2022). *Toric Kato manifolds*. Journal de l'École polytechnique—Mathématiques, 9, 1347–1395. Existing key `IstratiEtAl2022Root`; original PDF https://www.numdam.org/item/JEP_2022__9__1347_0.pdf . Opened in the B.4.10 audit: §2 construction, Proposition5.6 normal line, Example9.10 parabolic exponent matrix. The B.4.11 proof derives the exact canonical divisor directly from the invariant logarithmic two-form.

## General local-to-global argument

The proof does not treat a citation as the whole argument. On a finite Stein cover with only one member meeting the isolated singularity, local lifts over a small Artin extension can be glued except for a Čech two-cocycle in Theta tensored with the square-zero kernel. H²Theta=0 removes it. This gives the relative infinitesimal lifting property. Manetti's original Lemma1, p.93, was subsequently **Opened and visually inspected** and directly supplies its general analytic semiuniversal-base formulation. A regular analytic germ morphism is locally a projection and therefore lifts the specified local analytic disc. The opened Dloussky–Teleman discussion independently uses the same criterion.

## Original Manetti retrieval, accurate status

Manetti, M. (1991). *Normal degenerations of the complex projective plane*. Journal für die reine und angewandte Mathematik, 419, 89–118. DOI10.1515/crll.1991.419.89. The exact general lemma is cited in the opened Dloussky–Teleman primary source as Lemma1, p.93.

Institutional metadata https://iris.uniroma1.it/handle/11573/76993 and the author's bibliography were opened. The publisher PDF was inaccessible. EuDML153345 identifies the GDZ scan `GDZPPN00220875X`; its historical HTTP resolver works in the executor and redirects to https://gdz.sub.uni-goettingen.de/id/PPN243919689_0419?tify=%7B%22view%22:%22info%22,%22pages%22:%5B93%5D%7D . The GDZ HTML was saved under `/workspace/scratch/20a906f0fadd/external_sources/D_elliptic_contraction/Manetti1991_GDZ_locator.html`.

At initial integration, the individual lemma page was still being retrieved. This was completed before the next snapshot: **Opened and visually inspected** printed p.93, including Lemma1 and its full proof. The IIIF manifest is https://manifests.sub.uni-goettingen.de/iiif/presentation/PPN243919689_0419/manifest?version=8b7f2484 . Printed p.93 is scan97, exact image https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN243919689_0419:00000097/full/1800,/0/default.jpg . It is saved as `/workspace/scratch/20a906f0fadd/external_sources/D_elliptic_contraction/Manetti1991_p93.jpg`; the manifest and neighbouring p.92 are retained too.

The lemma is stated for a reduced compact complex space with finitely many isolated singularities. Its proof uses the cotangent-complex local-to-global spectral sequence: H²Theta=0 makes the map on first tangent cohomology surjective and on second tangent cohomology injective, which is the formal smoothness criterion. It explicitly concludes that every local deformation can be globalized. Thus it directly applies to our normal compact surface; no rationality or projectivity assumption is present. Bibliography key `Manetti1991D` now cites this inspected original scan.

## Searches and discarded shortcuts

Queries included the exact Manetti title with PDF; the GDZ identifier; simple-elliptic smoothings and degree-eight elliptic cones; and the Dloussky–Teleman title. Search-result aggregators were used only as locators. The source argument uses opened primary papers and an explicit proof.

Rejected shortcut: applying Dloussky–Teleman Theorem5.2 directly. Its contraction is of a negative rational cycle, whereas ours contracts an elliptic curve.

Rejected shortcut: asserting every simple-elliptic neighbourhood is a prescribed cone. Here the cone identification comes from the actual transverse-linear Kato gluing and the normally generated degree-eight section ring.

Rejected shortcut: inferring surjectivity from one-dimensional target alone. The proof uses the actual period deformation and the natural isomorphism H¹At(N)→H¹Theta_E, so the map is proved nonzero even at CM elliptic curves.

No computational experiment is used as a substitute for the cohomological proof. No novelty claim is made.

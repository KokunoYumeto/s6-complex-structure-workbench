# Correction intake and targeted checks

Audit date: 19 November 2026. Model: GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited from the root session and not separately exposed to this agent.

The sixteen sweep items are recorded individually in `sweep_16_audit.tsv`. `proposed_patches.json` contains four exact replacements against the attached cp15 source; the root agent owns their application. `CHECK_EVENTS.tsv` records the checks actually performed. A scope check or an inventory comparison supplies only that evidence, and is not counted here as a full new derivation of a theorem.

## Changes required by the sweep

The hypothesis `gcd(n,3k)=1`, the U/M duality maps in the four named statements, the simultaneous CM-and-torsion condition, the natural section-line sector, the comb Kuranishi qualification, the corner sign, the rank-three period bundle, and the resolved fibre-product construction are already present in cp15 at the precise scopes listed in the table. Four local scope edits remain useful: place the reference fan and boundary marking in the statements P3K.7, P3K.8 and P3F.17, and expand the existing H²(Y;Q)=0 hypothesis in C.2.INT.3.

The notation sheet contains inherited three-paper and 1184-row material. That apparatus must be reconciled with the five-paper series. Each local symbol transport should name its actual object: M_adm for the numerical bound; L_E=O(P−O) for the elliptic source line; M_c for the fourfold; M for the physical nonzero-vector line and U=M⁻¹ for its dual. No unproved object identification is supplied by renaming a variable.

The source and inventory contain **33** `iv:correction:*` labels. The prompt's figure of 34 is an overcount; its total of 39 high-risk rows agrees with the actual 33. Every one of the 33 receiving labels exists. Their individual mathematical reviews are being recorded separately.

The source-coverage comparison finds 27 current S6_05_ARITHMETIC A rows absent from the inherited inventory. Their identifiers, original statuses, proof locations, and proposed editorial disposition are in `missing_ari_A_rows.csv`. Sweep item 13 explicitly calls A.5.7 a side lane. The recommendation records that editorial scope; it makes no assertion that no mathematical relation can connect those results to the family. The root agent must record a final placement or exclusion reason for each row. Q03 has no dedicated source in the supplied archive and no row in the inherited inventory; the explicit separate-tag instruction in sweep16 governs its editorial accounting.

## Physical line and Hopf-transfer normalization

The attached intake sections 6–7 give two additional Claude Opus 5.5 at effort max checks which must be imported with their original scope and model attribution: the actual physical line M in P3K.68 and the value μ(λ(b))=+1/28 in P3F.22, relative to Jin's stated coordinates. Those events are in the attached intake TSV. Importing them gives no new check credit to this run.

The new program `code/independent_orientation_checks.py` was written without reading or importing either earlier orientation program. Its quaternion multiplication table derives the two Hopf derivatives and the orientation determinants. Its exterior algebra derives the collar contribution −18n². Its formal characteristic-series expansion derives the spin-c formula. Applying the inverse intersection matrix of the general filling, rather than reducing k to zero, gives

\[
Q=\begin{pmatrix}0&1\\1&k\end{pmatrix},\quad
p_1^2=6\ell-3k,\quad z^2p_1=\ell+k,\quad z^4=k,
\]

and therefore μ(∂W)=(ℓ−4k)/672 and μ(λ(f))=(4k−ℓ)/672 in the displayed boundary convention. The value at (8,8) is +1/28. There are 29 exact symbolic/arithmetic assertions and 33,300 finite gcd cases in the saved output. The general gcd implication is the elementary divisibility g|gcd(n,3k); the finite grid is a supplementary error check.

P3K.68's complete printed proof PL.1–PL.7 was opened. The Hermitian dual map is anti-equivariant on the actual scalar circle, the quaternionic anti-linear map commutes with the SU(2) transitions, and the cap comparison retains the boundary gauges. On the fixed oriented six-dimensional quotient x_M=−x_U gives the sign of both characteristic integrals. This agreement does not independently reconstruct every source/fan geometric input used later in Paper IV.

Primary arXiv abs/html/pdf routes for Jin 2608.26698v2 returned `DisabledError` in this run. No Jin source is included in the attachment. Search results confirm its bibliographic identity but do not expose Lemma 6.2. This run therefore retains the prior source-reading evidence and the stated relative normalization; it does not award a fresh direct-source check for Jin.

## Missing night rows

### P1.6 and P1.14

The attached night register marks both rows Known, and its report and literature log describe its own classification derivation. P1.6 records homotopy-eight-sphere absorption; P1.14 records the oriented diffeomorphism to 3HP²#(−HP²). Their `notes/part1.tex` is not included in the supplied night folder. Their historical check can be imported as reported independent verification of the conclusion of `maps:src:F.4.1`, with this evidence boundary stated.

A new classification implication was frozen in `fourfold_classification_prereading.md` before opening the printed F.4.1 proof. Given the already established three-connectivity and the diagonal lattice and Pontryagin class, the integral isometry preserves the full normal bundle invariant: its Euler number and Pontryagin number determine both Spin(4) clutching coordinates. Wall's extended-form classification produces the oriented almost diffeomorphism. Kramer–Stolz Theorem A absorbs the sphere into a positive HP² summand; signature +1 forces the supplied diffeomorphism to preserve orientation. The displayed proof in cp15 agrees with this derivation and gives the additional explicit reflection reduction used to obtain its diagonal characteristic vector.

Sources actually opened and matched here:

* Kramer–Stolz, *A diffeomorphism classification of manifolds which are like projective planes*, Theorem A, printed p.178, author-hosted PDF: https://www.uni-muenster.de/AGKramer/linuspub/27.pdf.
* Conway–Crowley–Powell–Sixt, *Simply-connected manifolds with large homotopy stable classes*, author v3 PDF, §3.3 and Definition 3.6 pp.11–12, Theorem 3.7(1) pp.13–14: https://www.maths.gla.ac.uk/~mpowell/large-homotopy-stable-class-v3.pdf. The published PDF was also opened at its Definition 3.6 and Theorem 3.7, printed pp.185–186.
* Wall's original scan opened at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/n-1con2n.pdf; it supplies no extractable text. The fully read classification statement for this check is the preceding author-hosted source.

### P5.7

The attached DGKX version-specific TeX sources were opened at their actual theorem statements. Version 1 gives the exact-period and automorphism claims at `p2:thm:exact-period`, the Kuranishi claim at `p2:thm:kuranishi-aut`, and the tangent tuple in its ordinary-tangent calculation. The complete version-2 section list and term occurrences are saved by `code/inspect_dgkx.py`; its matched occurrences concern local gluing and Oka constructions. It omits the four claims compared by P5.7. `P5_7_insertion.tex` is the proposed credited-appendix insertion. The original-page locators are the cp15 previously opened original-PDF locators, matched here to the supplied TeX labels; no fresh download of those original PDFs is claimed.

The statement and proof should retain the word “re-derived” for the tangent, deformation, and automorphism calculations. The permitted exact-period date comparison is preserved. The other mathematical proofs remain in their credited appendix locations.

## Source corrections inspected

The original AC26 PDF was opened through text extraction at Remarks 1.3 (PDF p.5), 9.21 (PDF p.81), and 9.26 (PDF p.83). The first two torsion statements are exactly the claims addressed by `inv:A4.2`; the final remark repeats the universal vector-field bound addressed by `inv:E2.4`. The original PDF takes precedence over the supplied transcription. Engel's complete Additional remarks source section was opened, covering the global u-family assertion, the central-fibre conjecture, and the claimed continuous translational quotient. The corresponding receiving corrections are already printed. Their separate mathematical proof checks and exact literature status remain attached to those rows; this intake does not replace them by a blanket verdict.

## Further work assigned to this audit

The 33 correction receiving items, `iv:rank_two_specialization`, and `iv:i3_all_reduced_caps` are the next proof-check targets. Fresh derivations will be written before opening their printed proofs. Novelty searches will record the actual source and query scopes, without a global claim of absence from the literature.

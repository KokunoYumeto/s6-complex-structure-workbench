## Root literature and source audit

The audit date is 15 November 2026. The attached original manuscript and attached arXiv versions are treated as mathematical inputs, not as verified authorities. Source-specific comparisons occur in the paper. No result is claimed to have priority on the basis of a search failing to find it.

### Smooth monodromy and characteristic numbers

Searches used the titles of Eells–Kuiper, Kervaire–Milnor and Cerf, and combinations of “mapping torus”, “homotopy sphere”, “spin-c Eells-Kuiper”, “equivariant diffeomorphism”, “semifree circle action” and “Blakers-Massey”. The primary scans of Eells–Kuiper (1962), Kervaire–Milnor (1963), Cerf (1970) and Poénaru (1971) were opened. The paper uses the exact statements and formulas recorded in its Part C and in C_push_report.md. The current arXiv source of Crowley–Nordström's Exotic G2-manifolds was checked for the spin-c normalization. Durán–Rigas, arXiv:0708.1577, §3.2, was read to test and reject the proposed inference from circle equivariance to a small mapping-class order.

The original Cerf1970 scan initially exceeded the web extractor's capacity; an independent local download succeeded, and primary page8 was inspected. The Γ4=0 book was bibliographically verified only and is explicitly marked not opened. It is not cited as the proof of the dimension-six identification. The scripts c_fetch_primary.py, c_review_primary.py and c_render_primary.py preserve the access record while leaving the scans and private OCR outside the deliverable.

Further searches and primary readings on circle actions, orbit knots and lift independence are documented in the C-related section notes and their bibliography. These establish comparison tools. They do not identify the annular twist of this family with an integer Haefliger invariant, and no numerical value of [Phi] is inferred from them.

### New trace obstruction and its limits

Queries included “Shioda On Mordell Weil lattices 1990 theorem 8.6 discriminant formula PDF”, “Oguiso Shioda Mordell Weil lattice rational elliptic surface 1991 pdf”, and the exact phrases “elliptic surface genus 3 I12 Mordell Weil”, “b^3 a^4 Mordell elliptic”, and “y^2=x^3 3b 2a elliptic surface”. The equation-specific searches did not locate the exact trace statement in B.3.4. This absence is not a claim of novelty.

The Rikkyo repository verified the original metadata of Shioda (1990), On the Mordell-Weil lattices, Commentarii Mathematici Universitatis Sancti Pauli39(2),211–240, DOI10.14992/00009994. Its direct PDF endpoint returned429. The primary author-uploaded PDF was then opened successfully at https://www.researchgate.net/profile/Tetsuji-Shioda/publication/247043151_On_the_Mordell-Weil_Lattices/links/5704b7fe08ae13eb88b69184/On-the-Mordell-Weil-Lattices.pdf . Theorems1.3,8.4,8.6 and8.7, Corollary5.3, and equations(8.11),(8.12),(8.20) were checked. The determinant relation follows from the narrow-lattice statement and its finite index.

Schütt and Shioda, Elliptic Surfaces, arXiv:0907.0298v3, was also opened at https://arxiv.org/pdf/0907.0298 . Section11.10 equation(22) explicitly records the determinant relation; Section6.10 gives the Hodge numbers and Corollary6.13 the rank formula. This is corroboration by the originating author, not a substitute for checking the original height theorem. The concrete sections, intersection numbers, local infinity expansions, saturation congruences and trace obstruction in B.3.4 are calculated afresh in the accompanying exact programs.

The obstruction applies to a split elliptic normalization. A genus-one torsor without a section is a separate possibility. The report and statement preserve this distinction. Likewise, the polarized hypotheses in Mumford/Alexeev–Nakamura and the polarizable-variation hypothesis in analytic Néron-model results are not discarded when considering an arbitrary nonpolarized analytic filling.

### Interval arithmetic and boundary levels

The primary Arb paper, Johansson, arXiv:1611.02831, §§2–3, and the official python-flint Arb constructor documentation were opened. The E.4 proof gives its own series, geometric tail bounds and strict contraction argument; only rational rectangle endpoints were imported from the earlier certificate. The exact cover was checked separately with rational arithmetic. The D.4 certificate explicitly depends on these newly certified roots; it does not claim arithmetic independence from them. Its i-neighbourhood proof is analytic, and its rho/cusp code implements its own Fourier series and derivative bounds at256 bits. The compact part uses192-bit Arb enclosures and an exact refinement tree.

The D.4 source comparisons with Lin–Wang, Chen–Kuo–Lin and Chen–Fu–Lin are recorded in D_global_literature_audit.md and integrated into D.4.8. The distinction is between a Green function on a fixed torus and the composite modulus function evaluated at a zero of the Weierstrass function. The precise latter level-set theorem is proved by the included certificates and C1 level transport.

### Citation format and evidence retention

The bibliography uses author–date citations and records opened/not-opened status in every entry. The official CTAN apacite page was checked as an available APA6 format implementation; it is a typesetting source, not a mathematical reference. Web result files in evidence contain metadata and retrieval identifiers only. Full copyrighted page bodies, primary scans and private OCR extracts are not republished.

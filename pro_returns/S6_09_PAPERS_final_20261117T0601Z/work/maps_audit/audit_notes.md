# Paper III audit record

Reader: GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. This is an audit-in-progress record, not a certification that all 198 MAPS results are checked.

## Scope and source graph

The final MAPS register has 198 rows (184 labelled Proved, 7 Known, 6 Refuted, 1 Open). `source_order.json` records the 69 actually included TeX files, totaling 1,348,597 bytes. `maps_A.tex` and `maps_B.tex` are the active split source; `maps.tex` duplicates their combined contents and must not be printed additionally. `source_blocks.json` extracts the located full statement-and-proof blocks for subsequent collation; extraction alone is not a proof check. The aliases K1, K8, K11, K15 and references to Leads are imported prompt conventions, not independently defined in the MAPS paper. They must be replaced by explicit definitions and companion theorem locators in the final paper.

## Recorded outside checks retained

`reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md`, introduction and §3, records Claude Fable 5.2 (Anthropic) at effort high, 16 November 2026, full readings of F.2.5, the first half of F.2.6, F.3.4–F.3.6, F.4.1 and A.3.1; the statement and setup of A.3.2 were read. The statements, but not full proofs, of B.6.16–B.6.22 were read. The tuple F.2.5 and exterior-square identity F.11 were independently recomputed. F.2.6's torsion differentials, the Kuhn cusp filling, and the Nagy and Jin source matches were expressly not verified by that reader. That is a scoped prior check, not a blanket unchecked label.

## New source openings and computations

The publisher full text of Csaba Nagy's *Extended surgery theory for simply-connected 4k-manifolds*, Compositio Mathematica 162 (2026), was retrieved. Theorem 1.4 exactly supplies the inertia criterion used in F.4.1: for a closed 3-connected eight-manifold inertia is trivial precisely when p1 is divisible by eight. Since Theta8 is Z/2, otherwise the inertia group is all of Theta8. The record's claim that this reference could not be opened is superseded for this writing. The application remains dependent on the manifold's verified connectivity and Pontryagin class. The HTML source and extraction are in `sources/external/maps_audit/`, outside the deliverables; provenance and SHA-256 are in `external_provenance.json`.

Huize Jin's arXiv:2608.26698v2 PDF was retrieved from arXiv. Proposition 3.1 gives the bordism invariant (-p1*x+4*x^3)/24. Lemma 4.8 and Theorem 4.9 give cube values 1,8 on the primitive and double-sphere Dehn twists, and the rank-two integral Torelli classification of S2 x S3. These are the actual source statements required by MAPS B.6.18. A full geometric match of the actual return to those invariants is still in progress.

Alarcón and Forstnerič's *Oka-1 manifolds* (2025), Definitions 2.1, 7.7, 7.11, the observation preceding Proposition 7.13, and Proposition 7.13(d), were opened and matched to MAPS F.3.8–F.3.9. The proof correctly uses an LSAP fibre-bundle section theorem, not the unanswered assertion that every Oka-1 fibre bundle is Oka-1. The explicit spanning tube is valid: its nine real integer directions are a complex basis; all lines lie uniformly inside det(Im Z)>0; least singular value is at least 1/sqrt(3), and radius 1/4 suffices. The supplied exact verifier was rerun and passed. F.3.11 imposes bounded correction at one retained cusp while other finite points remain punctures; it must not be strengthened to simultaneous good reduction at every puncture.

`fourfolds_nonselfdual.py`, `fourfolds_oka_tubes.py`, and `fourfolds_periods.py` were copied unchanged to `code/maps_audit/` and rerun under the supplied primary Python runtime. Outputs are saved beside them. The exact matrix, Smith, finite covering-index, genus-two discriminant, exterior-square quotient, and all four nonzero Z/2 torsion-residue assertions pass. The output itself states that H2=H3=0 requires the geometric identification of d2; a successful arithmetic run is not treated as a substitute for that identification.

## Proof readings performed so far

MAPS A.1.1–A.2.2 and B.1.1–B.3.3 have been read step by step. The algebraic and homotopy arguments are internally consistent. External source matches for stable homotopy and APS remain to be completed. B.1.1's use of doubling the stable comparison removes its mod-two pi1 obstruction, and the remaining H3 class restricts trivially because the monodromy-invariant vector d lies in ker(gamma). This is sufficient to identify the framed regular inverse image with the Lie-framed T3. A.2.1 requires the specified solid-torus image condition; A.2.2 is the counterexample if that condition is removed.

MAPS A.3.1–A.3.4 have been read in full. Their explicit real-locus calculations refine Paper I's real structures and should be located there, except A.3.4's quotient-map restriction, which is naturally in Paper III and cross-references the real-locus theorem. The matrix/finite coset computations remain to be rerun; the topological argument recognizes negative-imaginary-w fixed loci by a semifree circle action and positive-imaginary-w fixed loci by determinant-one solid-torus meridians. They do not classify the embedding S3 into S6.

MAPS F.2.5–F.2.6, F.3.5–F.3.11 and F.4.1 have been read in full. The explicit F.3.5–F.3.7 construction uses the primitive exterior square of a genus-two variation and a nonsplit trivial-line extension, not a polarized three-torus family. The H1(P*) vanishing follows from root-line coarse degrees 0,-1,-1. The constant imaginary shift makes the real obstruction function nonzero everywhere because it has one sign near the cusp and is bounded away from that end. The proof does not use an unjustified Oka compactification statement.

## Working edition coverage

The sphere-carrier sources explicitly remain in scope despite their exclusion from the earlier prompts. Their actual files include `workbench/cusp_cone_sphere_routes.tex`, `cusp_sphere_route_strengthening.tex`, and `cusp_s12_carrier_homotopy.tex`; the full higher-rung file also contains unrelated quaternionic/octonionic material that must not be included merely because it shares a file. The classical Theta6 proof is in `codex_workspace/courses/CG-S6/src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md` and relies on the accompanying handle and framed-bordism chapters. The survey's G2-8 almost-complex homotopy claim is a section-homotopy assertion, not a literal trivialization of the twistor bundle; the correct obstruction argument uses connected fibre CP3 and pi6(CP3)=0 over S6.

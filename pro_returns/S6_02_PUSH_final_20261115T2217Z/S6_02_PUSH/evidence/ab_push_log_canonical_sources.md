# B.4.28 proof correction and source audit

The structured search log is ab_push_maximal_monodromy_search.json. New bibliography metadata is in sections/ab_push_log_canonical_references.bib; existing Oda, Kamenova and Grauert keys are reused.

The first uninput candidate inferred a free-product formula for the central fundamental group from the rationality of individual double curves. Independent referee boundary_d identified a substantive gap: triple-cell attaching paths may run around a whole conductor cycle, whose loop maps nontrivially into an Inoue component. The same issue invalidated a proposed strengthening assuming rational conductors but no anticanonical condition. Neither group argument is used as a theorem.

The original candidate is preserved in ab_push_log_canonical_rejected_free_product.tex with an explicit REJECTED warning and its provisional Proved heading removed. The valid Euler identities in that passage did not justify its group assertion.

Root proposed the replacement argument using the nearby torus. The hyperbolic link inside an Inoue component transports into a nearby smooth fibre. Its two angular circles vanish in rational H1 by the hyperbolic mapping-torus relation; exterior cohomology of a torus then makes its H2 class vanish. A nonvanishing relative dualizing generator has a nonzero integral on that exact Clifford torus. This contradicts the vanishing. The fibre marking and all corner blow-ups were independently checked against Oda's original toric construction by boundary_d and limits_ab. The root independently reread Oda, Dloussky and Friedman and passed the revised full proof.

The live result continues to assume omega_D trivial. It does not infer that hypothesis from nearby tori, nor construct a log-canonical modification of an arbitrary analytic completion. The vertical-canonical-divisor identity and the missing contraction step remain explicit.

The precise base-change source was independently opened at https://djvu.online/file/2hQiOnz8WuoQk: Banica and Stanasila, Chapter III, Theorem 4.12(ii), printed pp. 134--135, gives the constant-h0 base-change statement used for the relative dualizing frame; part (iii) gives constancy of coherent Euler characteristic. The live proof cites the existing key BS76push. The Dloussky full-proof location is printed pp. 16--19, including the proof of Proposition 2.27 through its final branch case.

Implementation audit: an initial patch failed validation because one line lacked a patch prefix, and a later orchestration block failed JavaScript parsing because a draft Markdown backtick terminated a raw string. Both failed before making filesystem changes. The corrected writes succeeded. The exact period algebra script passes; its scope is finite symbolic/residue verification, not a computational substitute for the analytic theorem.


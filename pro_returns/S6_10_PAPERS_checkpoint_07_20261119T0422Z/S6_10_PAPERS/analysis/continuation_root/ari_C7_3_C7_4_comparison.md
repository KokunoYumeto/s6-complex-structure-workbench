# C.7.3 and C.7.4: comparison and correction of checkpoint 06

19 November 2026; GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

The written before-read derivations are `ari_C7_3_before_read.md` and `ari_C7_4_before_read.md`. After writing them, both the original S6_09 C.7.4 proof and the receiving C.7.4 proof were opened, and the receiving C.7.3 proof was opened. The exact algebra was independently implemented in `code/continuation_root/ari_period_exact.py`; all five symbolic checks passed. Its output records the precise symbolic assertions and its limited algebraic scope.

C.7.3 matches the independent derivation: the diagonal bracket is twice the symplectic pairing; the CM and non-CM reductive dimensions are 2 and 4; the independent conjugate case has pure dimension 7 and two central directions; degree-d isogeny transport gives the positive Rosati scale aa^dagger/d; the residual quotient torus adds one direction exactly for a nontorsion quotient lift. The actual morphism phi^t J_E phi=dJ_conjugate(E) fixes the sign and scale. The new symbolic program checks this matrix identity and the Heisenberg commutator, with a generic CM realization as a separate exact calculation.

C.7.4's original implication re-derives. The complete base period field contains u, zeta(u), their conjugates and the real-linear quasi-period expression. Compactness supplies the affine relation v+conjugate(v) in that field. The point and extension coordinates have the same abelian span, making B_Q zero. The period-torsor fibre is the central vector torsor. The sum functional is nonzero on its bracket line (1,c), c>0; the relation lowers its dimension by one. The exact Relative Semi-abelian Conjecture 4.7 supplies the contradictory lower bound dim Z. This is the same named hypothesis and conclusion as in the original source statement. The weaker translate-based Conjecture 4.9 supplies no positive bound at the algebraic lift and is not used.

The receiving checkpoint-06 proof had retained the period identities and declared the implication absent solely because its hypothesis was unresolved. Its printed text records no mathematical fault in the implication. The renewed derivation found no fault. The statement has therefore been restored with status **proved under hypotheses H**, H explicitly stated as the relevant instances of Conjecture 4.7 and explicitly open in every stated application. The full numbered proof is printed with the proved period results. The question without H stays in the final open arithmetic section. The superseded checkpoint-06 block is preserved in `ari_C7_4_replaced_checkpoint06.tex` with hash provenance in `ari_C7_4_integration.json`.

## Opened primary source and exact locators

Bertolin, Philippon, Saha and Saha, arXiv:2010.15170v2, full PDF opened: Definitions 2.3–2.4 p.8; Construction 3.4 p.12; Lemma 3.5 p.13; Conjecture 4.7 p.18; equations (4.3)–(4.4), Conjecture 4.9 and Proposition 4.12 p.19; the proof of Proposition 4.12 and Remark 4.13 p.20. The same passages were read in the attached `SemiAbelianTowers-final.tex`. The arXiv metadata page was opened at https://arxiv.org/abs/2010.15170. The exact current PDF was downloaded from https://arxiv.org/pdf/2010.15170; no publisher pagination is inferred from its 31-page arXiv layout.

## Credit search repeated

Searched the exact AC26 original PDF text, Engel E26 source, and DGKX versions 1 and 2 for `transcenden`, `Heisenberg`, `1-motive`, `period conjecture`, `compact subgroup`, `361`, as well as the actual formula/point identifiers. AC26's three `transcenden` matches concern algebraic dimension and construction constants, not the local-norm/compact-lift implication. No matching C.7.3 dimension table or C.7.4 local-norm theorem was found in those four works. The general motivic construction, unipotent dimension formula and relative conjecture are credited to BPSS at the exact locators above. This is a statement about the recorded search scope, not an assertion of an exhaustive literature search.

## Scope of completion

The independent re-proof of C.7.3 uses the named general motivic construction as a cited input. C.7.4 uses C.7.2's compact-lift identity; its compact-character equivalence was also checked, but no complete renewed check of C.7.2's separate theta formula is claimed here. The program proves the displayed algebraic identities and supplies no evidence that H holds. No arithmetic open conjecture has been asserted as true.

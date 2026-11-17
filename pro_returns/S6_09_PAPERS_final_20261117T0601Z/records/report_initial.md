INCOMPLETE

# S6_09_PAPERS — writing and verification record

Writing began 17 November 2026 (Europe/Berlin). This is a live record, not a claim of completion.

## Inventory

The six final results tables contain 745 in-scope rows: INV 47, FAM 55, PUSH 154, CDP 239, MAPS 198, ARI Part C 52. All 745 are in the inventory. Working-edition additions are being collated from the source corpus, survey, consolidation, and corrected status record. No blanket acceptance is inferred from a producing run’s “Proved” label. Existing proof checks will be retained with their exact scope.

## Authorship and checking

This writing and its audits are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. No human has checked the mathematics. Recorded historical readers and effort settings are taken from reviews/WHO_WROTE_WHAT.md and each report’s header, with the latter controlling disagreements.

## Discrepancies under investigation

1. INV’s integral marking conjugates inverse monodromies, whereas the required FAMILY marking conjugates the chosen monodromies. The dictionary must transport meridian direction, not just matrix symbols.
2. CDP unrestricted normalization arguments C.2.UN.1–86 were expressly not all read in the final intake; the COMPLETE header is not a proof check.
3. MAPS fourfold computations include reviewed existence results and distinct unverified torsion differential assertions. The records will distinguish them.
4. Consolidation MC-006’s historical unresolved recognition status is expressly superseded by the 5 October status record; no status will be copied from the former without the correction.

## Format and validation

The binding format and template have been opened. LuaLaTeX, latexmk, and Poppler are available. No deliverable PDF has yet been built or passed validation.

## Checkpoints

Hourly checkpoint clock starts 16 November 2026, 23:47 UTC (17 November 2026, 00:47 Europe/Berlin). No checkpoint precedes the first hourly boundary.

## Independent audit through the first Paper I build

The detailed record is `work/root/proof_audit.md`. The complete-source draft of Paper I now compiles to 353 pages with real LuaLaTeX after repairing the missing format and the rsfs font map. This is a draft, not a passed typesetting check. All 19,701 PUSH Arb norm boxes passed; the derivative and level-cover programs passed. The original obsolete global-meridians program failed, while its corrected successor and the independent quotient fixed-space check passed. The all-fan homology program passed on a dependency-ordered rerun. Both initial failures remain in the logs.

PUSH E.2.4–E.2.24 are transferred to Paper II for their global fibration-stability subject. They have been independently read in full in this writing; the precise non-Kähler duality, local invariant-cycle, nonsplitting, and Kuranishi dependencies are tracked by theorem, rather than by a source title alone. PUSH E.5 is also transferred to Paper II. MAPS A.1.1–A.1.3 and A.2.1 are in Paper I as prerequisites for its real-structure classification, alongside MAPS A.3.1–A.3.4.

The temporary extracted AC26 PDF text was moved from the work directory to the external-source cache. It is an extraction of a supplied source, not newly written work; the final package omits this duplicate source text in compliance with the source-exclusion rule.

# S6 private proof-repair and disproof workbench

This is a separate, private Overleaf project for the mathematical work that follows the completed three-stream proof audit. It is not the public 121-page audit project, and link sharing should remain off until the owner decides otherwise.

## Start here

1. `main.tex` — the active proof-repair/disproof notebook.
2. `annotated_audit.tex` — the unchanged 121-page annotated audit used as the indexed source of obligations.
3. `clean_transcription.tex` — the unchanged 108-page clean reconstruction.

The active notebook separates exact algebra from geometric certification and labels every item `VERIFIED`, `CONDITIONAL`, `OPEN`, or `REFUTED`. Its first workstreams are:

- the equivariant toric cusp quotient and collapse;
- integral specialization and saturation;
- based van Kampen inclusions, meridian signs, and primitivity;
- identification of the printed Mayer–Vietoris/Leray matrices with the actual geometric maps;
- the conductor, analytic base-change, and Serre–Grothendieck-duality argument in Section 10.

## Build

Compile `main.tex` with pdfLaTeX. The audit and clean reconstruction remain independently compilable from `annotated_audit.tex` and `clean_transcription.tex`.

## Editing rule

Do not edit the reconstructed manuscript in place. Proposed repairs belong in `research/` with an exact source-page reference, proof or counterexample, dependency list, and status label. Only promote a repair after its hypotheses and integral/sign conventions have been checked.

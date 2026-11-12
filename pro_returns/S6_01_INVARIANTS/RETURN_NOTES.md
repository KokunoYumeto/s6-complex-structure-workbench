# S6_01_INVARIANTS: return notes

Return of the research prompt `S6_01_INVARIANTS` (first of the five S6 prompts), AI-produced by GPT-6 Astra (OpenAI,
ChatGPT Pro mode) on 12 November 2026; not reviewed by a person. Filed 12 November 2026 by Claude Opus 5.5. These notes
are not part of the returned archive and are not listed in its `MANIFEST_SHA256.txt`.

## The archive

- File: `S6_01_INVARIANTS.zip`, 4,982,917 bytes.
- SHA-256: `5cbedf53251e92f69e153dc06bce82f8258af4be41b9c1db58fce828eff250c3`.
- Members: 116 files (no directory entries), all under `S6_01_INVARIANTS/`; the ZIP CRC test passes, and every
  extracted file is byte-identical to its member.
- Manifest: `MANIFEST_SHA256.txt` lists the other 115 files; all 115 SHA-256 digests match, and no file is missing
  from it.

## What it holds

- Paper: `S6_01_INVARIANTS_paper.pdf` (48 pages) with its LuaLaTeX source `S6_01_INVARIANTS_paper.tex`, `.bbl`,
  `.log`, `S6_01_INVARIANTS_references.bib` and `fragments/` (conventions, Parts A-E, computational record).
- Report: `S6_01_INVARIANTS_report.md`, opening with the outcome table summarized below.
- `S6_01_INVARIANTS_results.csv`: 47 numbered statements, 41 Proved, 2 Known, 2 Refuted (A4.2, E2.4), 2 Open (C3.8,
  E2.3).
- `code/` (20 Python programs and `requirements.txt`), `outputs/` (their outputs, statement and source records, PDF and visual QA, contact
  sheets), `logs/` (build and compile logs), `README.md`.
- The programs were returned by the model and have not been run by us.

## Left out of this copy

Five of the 116 files are not published here, because they reproduce pages of the original manuscript [AC26], which
this repository does not republish. The model made them to check the passages it corrects (statements A4.2 and C3.2);
read those pages in the manuscript itself, at <https://alpo.ge/s6.pdf>.

- `return/outputs/a_AC26_p5.png`: render of PDF page 5.
- `return/outputs/a_AC26_p81.png`: render of PDF page 81.
- `return/logs/c_source-062.png`: render of PDF page 62.
- `return/logs/c_source-063.png`: render of PDF page 63.
- `return/outputs/c_AC26_pages62_63.txt`: text extract of PDF pages 62-63.

They were published with the return on 12 November 2026 (commit 7ff0684) and removed in the next commit. Their sizes
and SHA-256 digests are in the repository's `LEFT_OUT.tsv`. The return's own `MANIFEST_SHA256.txt` is kept unchanged
and still lists them, so `sha256sum -c MANIFEST_SHA256.txt` reports these five as missing; the other 110 entries
match.

## Outcome table, one line per item

- **A.1** (a): all six cotangent direct images, an independent vertical-twist/duality proof, all finite and cusp strata.
- **A.2** (a): the decisive scalar μ_s(0) = i·4√π/(3^{3/4}Γ(1/4)²) with its fourth-root branch, two 100-digit
  computations, geometric nonvanishing, order-three leading coefficient, determinant divisor p₁ + p₂.
- **A.3** (a): full Hodge table (h^{1,2} = h^{2,1} = 1, h^{1,1} = h^{2,2} = 2), Leray generators, independence of c.
- **A.4** (a): local modules; the cusp-torsion assertions of [AC26] Remarks 1.3/9.21 corrected (A4.2 Refuted); the
  workbench's degree-one correction confirmed.
- **B.1** (a): invariant-lattice comparison for all admissible (3,4) twists; same Hodge numbers.
- **B.2** (a): all coprime (3k,4l): canonical bundle formula, graded anticanonical ring, small-pair table; Hodge
  numbers do not distinguish the families.
- **B.3** (a): finite-fundamental-group members and universal covers (cover: h^{1,1} = h^{2,2} = n+1).
- **C.1** (a): every nonzero d₁ on a named basis; E₁ ≠ E₂ = E_∞.
- **C.2** (a): Bott-Chern (1,0,2,2,2,2,1) and Aeppli (1,2,2,2,2,0,1) by direct kernel/image computation; McHugh and
  Angella formulas checked, no misprint found.
- **C.3** (c), unfinished: an evaluated local coefficient atlas for the global representatives G, Q is missing; the
  algebra, Picard map, +12 sign, non-Kähler degrees and metric types are proved.
- **D.1** (a): tangent direct images; h(T_X) = (1,1,1,0).
- **D.2** (a): H¹(T_X) spanned by the parameter class; Kodaira-Spencer an isomorphism for every admissible c.
- **D.3** (a): primary bracket zero; Kuranishi germ a smooth reduced line.
- **D.4** (a): every Picard twist, jump loci, stalk modules and lengths; r = 1 for every nonintegral twist.
- **E.1** (a): small deformations keep the pencil, the torus fibration and algebraic dimension one.
- **E.2** (c), unfinished: the comb Hodge-kernel splitting, torsion support/elementary divisors and obstruction maps
  are missing; the four tangent dimensions h(T_{X_m}) = (2m+1, 8m+1, 6m+1, 0) and Hodge bounds are proved. E2.4
  refutes the universal bound h⁰(T) ≤ 2 of [AC26] Remarks 1.2/9.26 and HKP Corollary 1.3.

Fourteen items at outcome (a); C.3 and E.2 at (c). The return itself says it is not a complete resolution of every
requested task.

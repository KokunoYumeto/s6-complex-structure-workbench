# S6_01_INVARIANTS

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**, 12 November 2026.
No priority is claimed. The report distinguishes proved statements from the two
items that retain explicitly described unfinished work.

## Contents

The main paper is `S6_01_INVARIANTS_paper.pdf`; its LuaLaTeX source is
`S6_01_INVARIANTS_paper.tex`, with the required `fragments/` directory.
`S6_01_INVARIANTS_results.csv` contains one row for every numbered statement.
`S6_01_INVARIANTS_report.md` starts with the sixteen-item completion table.
The BibTeX database marks the verification status of each reference.
The mathematical programs, source/statement metadata, exact outputs and
numerical outputs are retained under `code/` and `outputs/`.

## Reproduce the calculations

Python 3, SymPy and mpmath are required. From this directory run:

```sh
python3 code/run_all.py
```

The optional `--sources` also rechecks the supplied attachment's manifest and
extracts its PDFs. It expects that attachment extracted at `../background/`.
The source archive is not duplicated in this package. The mathematical
computations themselves do not require it or network access.

The precision is explicitly set to 100 decimal digits in the period program.
The output distinguishes numerical corroboration from exact nonvanishing
proofs. No interval certificate is claimed.

## Build the paper

On a complete TeX Live installation with LuaLaTeX, BibTeX, Latin Modern,
AMS packages, mathrsfs, microtype, natbib and hyperref, run:

```sh
python3 code/build_pdf.py
```

The script runs LuaLaTeX, BibTeX and two further LuaLaTeX passes and rejects
undefined references, missing characters, overfull boxes and document warnings.
It also requires Poppler's `pdfinfo` for the recorded PDF metadata.

This execution environment initially lacked its TeX search databases, format,
combined font map and Lua font-loader dependencies. A local repair, without
editing the system installation, is reproducible with:

```sh
python3 code/prepare_tex.py ../tex-runtime
python3 code/build_pdf.py --tex-runtime ../tex-runtime
```

The repair downloads the named packages from CTAN and records their hashes.
It is unnecessary on an ordinary complete TeX installation.

## Interpret the status labels

`Proved` denotes a complete argument in the paper; `Refuted` denotes a stated
false assertion with its counterexample and corrected claim; `Known` includes
the exact theorem and the reduction used here. `Open` includes the proved
partial result, computation, failed or missing step and smallest undecided
instance. These are the labels of an AI-produced mathematical dossier, not a
claim of independent human peer review.

The unresolved tasks are C3.8 (an evaluated coefficient atlas for the global
forms, whose exact operator representatives are supplied) and E2.3 (the comb
Hodge-kernel splitting, torsion support and obstruction maps). All four tangent
cohomology dimensions of the comb members are computed.

## Document and archive verification

`outputs/pdf_qa.json` records the page of every numbered statement.
`outputs/visual_review.md` records the visual review of all 48 pages, and
the four contact sheets are retained in `outputs/visual_qa/`.
The manifest `MANIFEST_SHA256.txt` contains a SHA-256 digest for every other
file in the archive. After extraction, the manifest can be checked with:

```sh
sha256sum -c MANIFEST_SHA256.txt
```

To check the statement ledger, prompt coverage, bibliography labels, recorded
execution results and document checks, then recreate and verify the ZIP, run:

```sh
python3 code/verify_and_package.py
```

The retained result is `outputs/package_verification.json`. The program also
checks every compressed member against its manifest digest and performs the
ZIP CRC integrity check before accepting the archive.

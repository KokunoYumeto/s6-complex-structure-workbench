# Reproducing the Q03 audit artifacts

The mathematical proofs and independent step-by-step derivations are in the post and full report. These programs reproduce the finite experiments, source inventories, arithmetic checks and artifact consistency checks. Their outputs state their actual scope; no program here is a formal proof of the general theorem.

## Layout and dependencies

Extract the final archive into a directory named `Q03_DEPOSIT`. Programs locate that directory from their own file paths. For programs that compare against the original attachment, extract the supplied background archive into the sibling directory `background`. The current supplied request is expected under the sibling `upload` directory by the original provenance-checking script; its preserved exact copy and verified hash are also in `anc/`.

Python 3 runs the mathematical and consistency checkers. Rendering additionally uses Pillow, pdfLaTeX, `kpsewhich`, `pdfinfo`, `pdftotext` and `pdftoppm`; the contact-sheet script uses DejaVu Sans. The LaTeX source uses standard AMS, Latin Modern, booktabs, table, URL, enumitem, needspace and titling packages. `build_pdf.py` includes a local format/font-map bootstrap for the execution image in which this audit ran. A normal complete TeX installation can compile the standalone post directly with two pdfLaTeX passes.

## Mathematical computation and accounting

Run from the extracted `Q03_DEPOSIT` directory:

```sh
python3 code/check_walk.py > code/check_walk_output.json
python3 code/B_hierarchy_check.py > code/B_hierarchy_check_output.json
python3 code/A_check_accounting.py > code/A_check_accounting.out
```

The first reproduces the supplied finite walk/exchange checker. The second independently constructs full hierarchies and checks set formulas, boundary invariants, witness injections and replacement schedules on the specified seeded finite family. The third checks symbolic exponent slacks and the explicit coefficient arithmetic. Exact case counts and finite-coverage limits are in the report and outputs.

## Assembling and compiling the post

```sh
python3 code/assemble_post.py > code/assemble_post_output.json
python3 code/build_pdf.py Q03_DEPOSIT_post.tex work/build_final --render > code/build_final_output.txt
python3 code/render_review.py > code/render_review_console.txt
```

The assembler uses the reviewed fragments in `work/` and the supplied original post for notation and comparison-table scaffolding. It regenerates the standalone LaTeX, complete statement CSV and machine-readable record. When a layout change alters the page or overflow counts, repeat assembly and compilation so the verification row matches the final log. Rendered-page inspection is an actual visual task; running the program alone does not establish that it occurred. `code/visual_review.json` records the final inspected PDF hash and pages.

## Final records and package

```sh
python3 code/E_build_form_answers.py > code/E_build_form_answers_output.json
python3 code/assemble_report.py > code/assemble_report_console.txt
python3 code/final_validate.py > code/final_validate_output.json
python3 code/package_final.py
```

`final_validate.py` refreshes the two integration checkers and exact form copy, checks the full audit embeds and ancillary hashes, compares the PDF with its source hash and visual-review record, and copies the final PDF to the top level. `package_final.py` creates the one ZIP, writes a SHA-256 manifest, and validates every manifest entry and ZIP CRC after creation. Its internal output records exact packaging exclusions. The manifest covers every included file except itself.

## Source and provenance programs

`C_*` scripts and outputs retain retrieval routes, file hashes, source maps, page locators and the dated search results. Re-running retrievals requires network access and availability of the cited versions. Downloaded third-party full texts remain outside the deliverable; their exact excluded paths and hashes are in `E_source_excluded_manifest.json`. `E_verify_provenance.py` compares the six preserved ancillary files with the supplied inputs and records the historical prompt-manifest discrepancy. It does not reconstruct the missing variant or authenticate unavailable historical API logs.

No script submits the post or sends messages, and the final form leaves the contributor identity and deposit approval for the user.

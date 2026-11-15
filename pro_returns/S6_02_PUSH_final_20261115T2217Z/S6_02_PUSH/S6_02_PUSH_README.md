# S6_02_PUSH — research return

**Status: completed.** The report's opening table is the authoritative item-by-item disposition. The current registry has 154 numbered statements: 137 Proved, 9 Refuted and 8 Known, with no Open row. The paper has 236 pages and 117 bibliography entries. The decisive B.4.33 excludes every proper Hausdorff complex-analytic filling of the actual six-sphere family after any finite parameter cover; it is not merely an obstruction to one proposed model. The positive-loop smooth monodromy is independently determined to be zero in Theta7. The nonexistent analytic filling has no central topology or almost-complex Chern data to assign.

The paper is `S6_02_PUSH_paper.pdf`; its LuaLaTeX source is `S6_02_PUSH_paper.tex`, with the included source files in `sections/`. The numbered statement registry is `S6_02_PUSH_results.csv`. The source bibliography and read-status annotations are in `S6_02_PUSH_references.bib`. Detailed corrections, failed approaches, literature comparisons and verification records are in `S6_02_PUSH_report.md`. Earlier provisional statuses are clearly separated as historical records. The final clean build is draft34: all four stages succeeded, the integration audit passed, there were zero overfull boxes, and 34 distinct pages were visually inspected, including all new B.4.30–B.4.33 proof pages.

## Reproduction

The supplied input archive is deliberately not duplicated here. Extract the user's `S6_02_PUSH_background.zip` into a directory named `background` beside this `S6_02_PUSH` directory. In particular, the old rational box list should be at `../background/s6_02_return/code/f_interval_parallel_certificate.json`. The independent E.4 implementation uses only its rational rectangle endpoints; it does not import the previous implementation or numerical enclosures.

The actual Python and package versions are in `code/environment_manifest.json`. Exact algebra uses SymPy and Python integers/Fraction. Certified analytic inequalities use python-flint's Arb/acb arithmetic. Numerical exploratory programs are labelled as such, with their precision and limitations. A file ending in `.out` is the corresponding execution transcript; `.json` and `.csv` contain the fuller machine-readable outputs where applicable.

Principal reproduction commands, from this directory, are:

```bash
python code/e4_arb_certificate.py --workers 4
python code/e4_cover_and_local.py
python code/d_root_gradient_certificate.py
python code/d_push_global_arb.py --workers 4
python code/d_push_global_refine.py
python code/d_push_global_cover_audit.py
python code/assemble_records.py
python code/build_paper.py reproduced --clean
python code/audit_deliverables.py reproduced
python code/render_qa.py reproduced
python code/qa_final.py reproduced
```

Inspect the rendered spread and all new-proof contact sheets before recording a visual pass with `python code/record_inspected_visual_qa.py reproduced`. Then regenerate the report with `python code/refresh_report.py reproduced`. The recording script must not be used to claim an inspection that has not been performed.

The paper names the exact algebra and topology programs at the points where their outputs are used. Those scripts and all their retained outputs are in `code/`. The initial coarse gradient pass deliberately records 13 undecided boxes; the refinement script resolves them and the exact cover audit checks the replacement tree. The failed single-square rho contraction is also retained. Its derivative bound proves uniqueness on the larger square, while the 400 smaller contractions prove existence and the rigorous derivative estimates. These distinct uses are explained in D.4.7.

A normal TeX Live installation with LuaLaTeX, BibTeX, Latin Modern, AMS fonts, fontspec, mathtools, microtype, booktabs, longtable, enumitem, natbib, hyperref and xurl should compile the paper. The original execution image had missing formats and font maps. `code/tex_runtime_setup.py` documents the isolated repair used there; it is needed only if the host installation has the same deficiency. Its cached runtime is a reproducible dependency outside this archive. The build script ignores a recorded runtime whose absolute location no longer exists, so moving the directory does not force an invalid configuration. Compiler transcripts and overflow counts are retained in `build_logs/`.

## Historical records

Earlier checkpoint ZIPs are never overwritten. Historical source and output versions that differ from the current files are retained byte for byte under `retained/`; the exact mapping and SHA256 digests are recorded in `sections/retention_record.md` and `code/retention_record.json`. An old Open statement in those historical files may have been resolved in the current paper. The source inputs, external primary-paper scans, private OCR, downloaded runtime caches and full copyrighted web bodies are not republished.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No human verification or priority is claimed.

S6_02_FAMILY
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026.
No priority is claimed. C.3, E.1 and E.2 remain partly settled.

START HERE
  S6_02_FAMILY_paper.pdf      Mathematics, in prompt order.
  S6_02_FAMILY_report.md     Twenty-item outcome table, corrections,
                            computations and precise remaining targets.
  S6_02_FAMILY_results.csv   One row for each of 55 numbered statements.

SOURCE
  S6_02_FAMILY_paper.tex includes the TeX files in sections/.
  S6_02_FAMILY_references.bib marks all 15 entries verified and records
  which passages were opened.

REBUILD THE PAPER
  With TeX Live including LuaLaTeX, BibTeX and the listed standard packages:
    python3 code/build_paper.py
  The script runs LuaLaTeX, BibTeX, and two further LuaLaTeX passes and
  retains complete output in code/build_lualatex.out.
  A configured TeX installation also supports the corresponding ordinary
  commands directly from this directory.

  code/tex_environment.py handles the minimal supplied Linux image by
  generating workspace-local TeX search paths, a format, and font maps.
  The document uses native T1 Latin Modern metric fonts. On an image
  without the optional OpenType loader, the bootstrap configures the
  existing native-font fallback before generating the local format.
  It changes no system files. A complete TeX Live installation bypasses
  that bootstrap. Generated local caches are not part of this ZIP.

MATHEMATICAL REPRODUCTION
  Python dependencies: sympy, mpmath. Python 3.12 was used.
  Exact versions and final checks appear in code/check_deliverables.out.
  All actual mathematical programs and their output are in code/.
  Most are run as python3 code/NAME.py and print their results; redirect
  stdout to reproduce the adjacent .out file when a script does not
  write it itself. The scripts are independent of the current directory.

  The main global-maximum certificate is reproduced by:
    python3 code/f_interval_parallel.py
    python3 code/f_interval_verify.py
  Its complete saved output is f_interval_parallel_certificate.json.
  The exact verifier is fast; the interval construction takes several
  minutes and uses six worker processes. Analytic local/cusp estimates
  are in the paper and cd_local_bound.py / cd_special_intervals.py.

  cd_interval_cover.py is a stopped exploratory implementation; its
  partial log is explicitly non-certifying. The f_interval_* certificate
  is the completed corrected calculation used by the theorem.

  cd_multiples_initial.py is the supplied reader's checker, run with its
  original attribution retained. cd_torsion_independent.py provides the
  independent division-polynomial calculation.

  The statement registries can be regenerated with ab_ledger.py,
  cd_registry.py and e_registry.py, then assembled with:
    python3 code/assemble_package.py
  F_results.csv contains the separately verified F statement ledger.

  The supplied source archive is not duplicated. To recheck its hashes:
    python3 code/source_inventory.py /path/to/extracted/background

VISUAL AND STRUCTURAL VERIFICATION
  python3 code/audit_pdf.py     (requires PyMuPDF and Pillow)
  python3 code/check_deliverables.py
  Every PDF page was rendered. The contact sheets and selected full-size
  pages were inspected. The retained evidence contains the automated
  bounds audit and the visual review record.

SCOPE
  The package does not construct the compact boundary replacement or the
  global w=0 central threefold. It constructs the explicit local models,
  candidate pushout and reduced surface limits and proves exactly the
  topological invariants assigned to those constructed spaces. The
  unresolved gluing germs are stated in C.3.3, E.1.5 and E.2.3.

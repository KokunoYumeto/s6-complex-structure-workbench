S6_09_PAPERS — three companion papers

Start with the three PDFs and S6_09_PAPERS_report.md. The inventory is the exact
seventeen-column result concordance. The notation sheet maps source symbols,
normalizations and result labels to the three printed papers. The shared BIB
marks every entry verified or unverified, with the precise opened-source scopes
retained in the verification records. An unverified comparison supports no
operative mathematical implication.

Typesetting the canonical sources
--------------------------------
The three top-level .tex files are standalone LuaLaTeX sources with inline APA
bibliographies. They do not input another project file, external figure or BIB
at build time. In an ordinary current TeX Live installation with the packages
named in their preambles and Latin Modern fonts, run (from this directory):

  lualatex -interaction=nonstopmode -halt-on-error S6_09_PAPERS_I.tex
  lualatex -interaction=nonstopmode -halt-on-error S6_09_PAPERS_II.tex
  lualatex -interaction=nonstopmode -halt-on-error S6_09_PAPERS_III.tex

Repeat each command until its labels, bibliography links and longtable widths
are stable. The delivered PDFs and exact final build logs are recorded in
records/I_final_validation.json, II_final_validation.json and
III_final_validation.json. The code/editorial compiler wrapper describes the
writing environment's repaired TeX format; a normal TeX installation does not
need that machine-specific environment file.

Computational reproduction
--------------------------
Each paper has a complete program appendix giving the program, exact finite
role, working directory, command and recorded output. The mathematical proof
explains the implication supplied by the computation. Run the commands from
the displayed working directories; retain this archive's directory structure.
The Python, PARI/GP, C++ and Julia environment details are given beside the
commands. The Julia project/manifest are pinned under
code/root_maps_F/runtime/hecke_env; runtime binaries and package caches are not
included. The supplied programs, immutable computational fixtures, certificates
and all successful/failed outputs actually used in this writing are retained.
A failed historical invocation does not acquire a successful status: its
corrected invocation and resolution are separately identified.

The code/editorial and other audit/assembly programs also document how the
writing was performed. Some of those editorial programs intentionally refer to
the separately supplied sources/ tree. They are not needed to compile the final
standalone papers or to replay the portable mathematical commands. To repeat
source-comparison audits, restore the eight originally supplied archives to the
same sources/ paths recorded in the manifests. The source archives and literature
scans themselves are not repackaged here. Narrow source-parsed computational
fixtures are retained only where an actual verifier needs their exact bytes.

Verification and history
------------------------
The saving service imposes a 512 MiB file limit. To retain all content in one
standard ZIP, byte-identical PNG review assets share one stored copy. This is
exact byte deduplication: no image is resized or recompressed, and no reviewed
page, proof, output or historical version is discarded. All papers, code and
text records remain at their ordinary paths. The complete path/SHA256 mapping
is records/visual_asset_deduplication.json. To recreate every original image
path after extracting the ZIP, run:

  python3 code/editorial/restore_duplicate_visual_assets.py --restore

The command uses only Python's standard library, verifies every retained image,
and refuses to overwrite an existing different file. Without --restore it
checks the retained payloads and reports how many duplicate paths can be
recreated. records/final_payload_manifest.json records both the original path
and stored path for every file. The archive verifier checks every original
file's full bytes through this mapping.

The final package gate checks inventory destinations, complete proof-retention
records, citation scopes, self-contained sources, final logs, visual-inspection
records and archive integrity. It is not a proof-assistant certificate. All work
is AI-produced; no human has checked its mathematics. Exact mathematical
boundaries remain in the plainly separated final parts and in the inventory.

Earlier checkpoint members are retained unchanged at their original paths or
as exact byte versions in history/checkpoint_versions/. The complete mapping is
records/checkpoint_retention.json; it records every original path, checkpoint,
hash and retained destination. Intermediate build logs and failed attempts are
historical evidence, not delivery passes. Current decisions and their scoped
sources are identified in the report and the inventory's final outcome fields.

Our text is dedicated to the public domain under CC0 1.0. Existing external
programs and cited works retain their own notices and authorship. No person is
named as an author of or contributor to the AI-produced papers.

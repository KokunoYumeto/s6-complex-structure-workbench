# Paper III: final-build preparation from the current source

Read-only follow-up, 25 November 2026, completed after the root's
20:39:59 UTC preamble/front-matter application.
Reader: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not
separately exposed.

This note records source/runtime findings and a future build sequence.
No full Paper III build, new alias test, canonical edit, mathematical
program run, derived-inventory refresh, or additional mathematical
checking credit was performed for this follow-up. The bounded Paper II
source/PDF lookup below was expressly authorized by root.

Project root:

    /workspace/scratch/ebb19e505dac/base/S6_SERIES_PUBLISH_checkpoint_91

## 1. Runtime and the source region already supplied by root

The actual 16-line wrapper is code/S6_SERIES_PUBLISH_c8_tex_pdflatex.py.
It derives the project root from its own location, then supplies:

- TEXMFVAR = agents/continuation8_tex_runtime/texmf-var
- TEXMFCONFIG = agents/continuation8_tex_runtime/texmf-config
- TEXMF = the local config, var and texmf trees followed by /etc/texmf,
  /usr/share/texmf and /usr/share/texlive/texmf-dist
- TEXFORMATS = the local texmf-var/web2c subtree, recursively, then the
  system fallback
- TEXMFDBS empty and MKTEXFMT = 0
- the installed pdflatex executable with -no-shell-escape

The wrapper passes the remaining arguments through and returns the
engine's actual exit status. It does not choose an output directory,
change the working directory, create that directory, or run extra passes.
Run the commands below from the project root.

The existing local format is
agents/continuation8_tex_runtime/texmf-var/web2c/pdftex/pdflatex.fmt;
the existing font map is
agents/continuation8_tex_runtime/texmf/fonts/map/pdftex/pdftex.map.
Their paths were read again; format generation and smoke runs were not
repeated. The earlier actual setup program and outputs are
code/S6_SERIES_PUBLISH_c8_tex_runtime.py and the adjacent c8_tex_format,
c8_tex_smoke_pass1, c8_tex_smoke_pass2, c8_tex_pdffonts and c8_tex_pdfinfo
outputs. The setup program writes the wrapper and performs its own smoke
passes, so it is not the final-paper build command.

Root's current preamble has the actual amsmath/hyperref/cleveref order and
the already tested AMS alias dispatcher at lines 19–52. The two repository
macros are at lines 159–160. Those regions now occur in canonical III as
well as the staged root/preamble.tex. The old seven front-matter
StatementRecord calls have been replaced together with the old preamble.
A read-only query found none of the removed workflow macros used in the
main mathematical body or bibliography.

The complete alias implementation, actual successful runs, exact
equation/align number-and-target observations and the observed failed
baseline remain in code/S6_SERIES_PUBLISH_c8_tex_alias_proposal.tex and
code/S6_SERIES_PUBLISH_c8_tex_alias_notes.md, with their named actual
outputs. Root has read and accepted that evidence. No new test is needed.
For the final document the literal aliases remain in the source and are
written at the existing AMS flush point; the final document's own aux and
PDF destinations still have to be read after its actual build.

## 2. Concrete source hazards and their present disposition

| Source locator | Observed hazard | Required disposition |
| --- | --- | --- |
| root/cyclic_homology.tex, lines 35–36; canonical III lines 6389–6390 immediately after the new front matter | SeriesRef calls for def:II:marked-conventions and def:II:analytic-picard-data have no SRef definitions in the examined preamble. SeriesRefText prints the literal word UNRESOLVED for this case; a successful engine exit does not detect it. | Add the two exact mappings in section 3. Root is handling this together with final III reference definitions. |
| later/os49_graph_caps.tex, line 929; canonical III line 54434 at that reading | The 02S9 statement uses local cref{night:P3K.65}; the target is external to III. The same fragment uses SeriesRef for that same key at lines 13, 888 and 1330. | Root is applying the exact cref-to-SeriesRef route change. The existing staged SRef key points to IV tag 02VC. No mathematical statement change was proposed. |
| preamble.tex lines 161–164 and its following SRef block; representative external definition at line 165, and night:P3K.65 at line 2932 | External mappings retain S6_SERIES_GRIND_*.pdf filenames and frozen external numbers/pages. Local mappings use current ref* values. | At final III reference completion, use actual current destination-owner data and the delivered S6_SERIES_PUBLISH_*.pdf filenames. The two parts of the mapping must be handled separately; replacing a filename does not update the number or page. |
| front_matter.tex lines 712–714; canonical III lines 5816–5818 at that reading | The front matter requires SsixPublishRecords and SsixRepositoryCommit. | Both macros are now defined by the applied preamble. No further macro addition is needed for these uses. |
| Actual bibliography begins at canonical III line 63922 at that reading | The standalone file contains thebibliography directly. Its printed entries and keys are the ones the engine reads. | Root's exact bibliography/citation corrections must be present in this inline region. Running BibTeX against the separate .bib file alone would not update it. |

Line numbers above identify the read source. Root's subsequent bounded
edits can shift them; the exact labels/keys and fragment paths remain the
guards. This note does not assert those pending root changes have already
been applied.

The body control words and named environments were inspected against the
actual staged package/macro set. Its mathematics uses the supplied AMS
environments, amscd, mathtools' psmallmatrix, mathrsfs, TikZ/TikZ-CD, the
declared theorem environments, natbib, hyperref and cleveref. The lexical
inspection found no unbalanced literal environment delimiters or braces
in the examined body. No remaining manual tag command was found there.
The source query found no input/include/includegraphics, externaldocument,
minted/listing-file input, bibliography-file input, Lua, or shell-execution
command in the standalone document. It has its own document and inline
bibliography boundaries.

The live non-ASCII text found by the bounded query was section sign,
É, é, ö and Č, with the existing UTF-8 inputenc and T1 fontenc settings.
The query did not expose an additional unsupported mathematical Unicode
command. These are source findings, not a successful compilation or a
claim about page layout.

## 3. Exact two-definition Paper II lookup

Root authorized only the two definitions and actual aux/PDF metadata.
The current source identity lines read were:

- S6_SERIES_PUBLISH_II.tex, lines 6292–6294: Definition “Marked periods,
  fibres and orientations”, label def:II:marked-conventions, tag P202.
- S6_SERIES_PUBLISH_II.tex, lines 35729–35731: Definition “Marked periods
  and cusp normalization”, label def:II:analytic-picard-data, tag P309.

The actual delivered S6_SERIES_PUBLISH_II.pdf has 787 pages. Reading its
PDF named destinations and the two relevant heading/footer text regions
gave:

| Label | Permanent destination | Number | Printed page | Zero-based PDF page | Destination coordinates |
| --- | --- | --- | --- | --- | --- |
| def:II:marked-conventions | tag-P202 | Definition 2.1 | 26 | 25 | (70.866, 749.262) |
| def:II:analytic-picard-data | tag-P309 | Definition 35.1 | 393 | 392 | (70.866, 405.994) |

In each case the corresponding formal destination, definition.2.1 or
definition.35.1, has exactly the same page and coordinates as its tag.
The extracted headings contain the stated full titles and printed
numbers; the page footer blocks read “26” and “393”. Thus the locator does
not come from an inferred source-line/page correspondence.

Exact additions for the current III source are:

    \expandafter\def\csname SRef@def:II:marked-conventions\endcsname{\href{S6_SERIES_PUBLISH_II.pdf\#nameddest=tag-P202}{II.2.1} }
    \expandafter\def\csname SRef@def:II:analytic-picard-data\endcsname{\href{S6_SERIES_PUBLISH_II.pdf\#nameddest=tag-P309}{II.35.1} }

The retained historical auxiliary files
build/II_recovery_candidate_02/S6_SERIES_PUBLISH_II.aux, line 73, and
build/II_prestructure_20261122T0842/S6_SERIES_PUBLISH_II.aux, line 80, put
the first definition at page 17. That historical page is obsolete for
the delivered 787-page PDF. The final-v3 auxiliary file is absent from
the retained build paths examined. The existing actual
code/S6_SERIES_PUBLISH_c4_final_v3_build.out identifies the final-v3
787-page build and records its successful passes, but it is not being
replayed or awarded new verification credit.

## 4. Legacy generators are not the final III build command

The attached ../S6_PUBLISH_programs/code/assemble_series.py, lines
448–460, shows the exact old reference formula: local SeriesRef entries
combine a tag hyperlink with a live ref*; external entries combine a
GRIND PDF path with number/page strings from
analysis/current_labels_<paper>.json. Its main routine, lines 359–476,
also assembles all five papers from older component files, rewrites the
tag registry, dependencies and other derived files, and restores the
old StatementRecord/return-backlink presentation. Its preamble template
also emits setmonofont at line 396, while the current pdfLaTeX preamble
uses lmodern and contains no such fontspec command. Running that assembler
would replace the current publication preamble and body. None of it was run.

The attached finish_III_reference_transport_09.py, lines 11–31, and
finish_publication_build40_10.py, lines 15–37, also loop over all five
old GRIND papers, use older current-label JSON and write sources plus
transport records. They are historical evidence for the mapping formula,
not current commands.

The attached audit_current_references.py, lines 13–57, opens all five
GRIND PDFs/sources, uses the older label maps, counts StatementRecord
macros, and writes derived inventories and hashes. The current III
presentation uses literal small tags instead of StatementRecord calls.
Its old printed-record counting logic therefore does not validate the
current source. This script was read, not run.

Within the checkpoint, code/S6_SERIES_PUBLISH_build.py creates a separate
tex-runtime, performs an unconditional requested number of passes, and
writes a hash-bearing build summary. code/S6_SERIES_PUBLISH_c3_build.py
imports that environment and defaults to Paper II. Neither is needed for
the already prepared c8 runtime or the requested III-only final build.

## 5. Concrete final-build sequence, to run only after root's text freeze

1. Finish root's source, bibliography, program table and exact reference
   edits. Preserve every existing literal label and hypertarget occurrence.
   Use only the current canonical III file, with the applied preamble,
   rather than reassembling from historical components.

2. Resolve every SeriesRef actually used by III against the actual
   current external owner's permanent tag, printed number and PDF
   destination. Root's final presentation prints paper plus number and
   omits external page fields; the exact available page evidence remains
   in this review. The two missing II definitions are supplied above.
   Incoming references from other papers to III require the III numbers
   and pages produced by the final III build at the later authorized
   joint-reference step. No stale page from a historical aux is suitable
   for that step.

3. Use a new III-only output directory and the c8 wrapper. The following
   first-pass commands are concrete, but were not executed in this task:

       cd /workspace/scratch/ebb19e505dac/base/S6_SERIES_PUBLISH_checkpoint_91
       mkdir -p agents/continuation8_tex_runtime/III_final
       python code/S6_SERIES_PUBLISH_c8_tex_pdflatex.py \
         -interaction=nonstopmode -halt-on-error -file-line-error \
         -output-directory=agents/continuation8_tex_runtime/III_final \
         S6_SERIES_PUBLISH_III.tex \
         > code/S6_SERIES_PUBLISH_c8_tex_III_final_pass01.out \
         2> code/S6_SERIES_PUBLISH_c8_tex_III_final_pass01.err

   Read the actual exit status, complete stdout/stderr and generated
   agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III.log.
   Retain each actual pass log before a subsequent pass overwrites it:

       cp agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III.log \
         code/S6_SERIES_PUBLISH_c8_tex_III_final_pass01.log

   An engine failure is a failure of that pass. Resolve its exact source
   cause before the next pass; do not conceal it by continuing a loop.

4. Run the same wrapper command with pass02 stdout/stderr names after
   reading pass01. The second pass consumes the produced aux/toc/bookmark
   data. Subsequent passes are justified by actual remaining rerun
   requests or changed auxiliary data, rather than a preset test loop.
   A corrected source, bibliography or displayed reference can change
   line and page breaks, so its actual rerun messages govern completion.

5. Read the final log for actual TeX/package errors, undefined local
   references/citations, multiply defined labels, duplicate destinations,
   missing glyphs/fonts, rerun requests and overfull/underfull boxes.
   Read the final PDF's text for the SeriesRef UNRESOLVED fallback as
   well: that fallback need not produce an undefined-reference warning.
   The final aux must give each retained display alias the same number
   and live equation target, and the PDF must contain the preserved
   explicit tag destinations. This uses the full document's actual
   output; it does not repeat the completed alias MWE.

6. Use the actual final pages for the required publication-layout
   reading. Page numbers from source estimates or old builds provide no
   page-reading credit. Any resulting source repair requires its normal
   defects row and an actual rebuilt output before the affected pages
   can be assessed. Root owns this final build/page/reference completion.

There is no new TeX success assertion in this note. The c8 runtime and
alias mechanism have their already accepted bounded test evidence;
Paper III's complete source is ready for the separately authorized
actual build only after its remaining final source/reference edits.


## 6. Bounded final external-reference follow-up

Root subsequently requested every actual external reference used by the
current III front matter and body. The direct source-use query found
22 distinct external targets: fourteen in I, four in II including the
two definitions above, and four in IV. No actual V target was used.
All used ordinary local ref/eqref/cref targets resolved to labels in III.
The seven explicit hyperlink uses in the new outline resolved to its
existing main-III anchors. There was no additional direct external-PDF
href in the examined body. The OS49 02S9 occurrence now uses SeriesRef
for night:P3K.65, so root's exact routing repair is present.

Each external key's literal target label and adjacent permanent tag was
located in its current owning source. All twenty-two target identities
exist; the lookup exposed no changed owner or vanished target. This was
a bounded identity/locator examination, without whole-paper mathematical
reading or any new mathematical event.

### Root's final reference presentation

Root will print the paper and statement number, linked to the preserved
permanent tag in S6_SERIES_PUBLISH_<paper>.pdf, and omit inherited page
fields uniformly. The two exact II macro examples above now follow that
decision. Page observations are retained here as evidence. The fourteen
I numbers below use explicitly attributed, certified final-output
records; no new I PDF-opening claim is made. IV's later publication
renumbering remains part of the joint step.

### Paper II: two additional contradicted locators

The existing III dictionary gives push:src:E.5.2 as II.13.23, p.349,
and push:src:E.5.3 as II.13.24, p.351. Those entries disagree with the
actual delivered 787-page S6_SERIES_PUBLISH_II.pdf:

- At current II source line 33871, push:src:E.5.2 retains tag 033O
  and the title “Monodromy, centralizer, and integral lattices”.
  The actual PDF heading reads Proposition 30.1. Its tag-033O and
  proposition.30.1 destinations coincide at page index 372,
  coordinates (70.866, 746.472); the printed footer is 373.
  Thus the outgoing text is II.30.1 with permanent target tag-033O.

- At current II source line 33996, push:src:E.5.3 retains tag 033P
  and the title “Biholomorphism classes in the two-parameter family”.
  The actual PDF heading reads Theorem 30.4. Its tag-033P destination
  is on page index 373 at (70.866, 307.202), and theorem.30.4 is
  on that same page at (70.866, 305.209); the printed footer is 374.
  The 1.993-point vertical separation is visible in the actual
  destination data and does not change the heading identification.
  Thus the outgoing text is II.30.4 with permanent target tag-033P.

Together with P202/Definition 2.1 and P309/Definition 35.1 from section 3,
this resolves all four actually used II targets. The two definition keys
still lacked dictionary entries at the source-use reading; root owns
their insertion. None of these locator readings reopens a II proof or
changes its source.

### Paper I: certified final-output binding and stale dictionary entries

The continuation archive does not contain S6_SERIES_PUBLISH_I.pdf.
The bounded archive-name lookup confirmed the same absence in the ZIP,
so there was no new direct opening of that PDF. Root expressly authorized
the already retained final-output evidence and a check of its source
binding.

The attached current I source has SHA-256
179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74.
That single, authorized source comparison exactly matches all three
existing records:

- records/S6_SERIES_PUBLISH_I_current_metadata.json;
- records/S6_SERIES_PUBLISH_I_final_pdf_receipt.json;
- build/I_candidate20/build_summary.json.

Those records also agree on the existing final PDF SHA-256
62d84285f35aa6e6ce03b83efbcf2a96e880fda6206eb24c05ab8e66fe799dd6.
The retained receipt certifies the 346-page candidate20 output at
2026-11-21T18:24:32.520345+00:00. The selected rows of
records/S6_SERIES_PUBLISH_I_current_statements.json supply its exact
numbers/pages; their labels, titles, tags and source locations agree
with the bounded current-source header lookups. No inventory, hash
record, source or PDF was rewritten.

The four primitive-quotient/cusp references have unchanged target
identities but stale inherited dictionary locators:

- mapsI:src:A.1.1, tag 02PA, current source line 13952:
  Proposition 16.2, retained final p.113. The old entry says I.22.1, p.295.
- mapsI:src:A.1.2, tag 02PB, source line 14039:
  Proposition 16.4, retained final p.114. The old entry says I.22.2, p.296.
- mapsI:src:A.1.3, tag 02PC, source line 14142:
  Proposition 16.6, retained final p.115. The old entry says I.22.3, p.297.
- mapsI:src:A.2.1, tag 02PD, source line 14209:
  Theorem 16.7, retained final p.116. The old entry says I.22.4, p.298.

The six period/classification references likewise retain their labels
and tags:

- fam:src:B.1.1, tag 01Q7, source line 6544:
  Proposition 2.11, retained final p.22; old entry I.3.2, p.24.
- fam:src:B.1.4, tag 01QA, source line 6648:
  Proposition 2.13, retained final p.23; old entry I.3.5, p.28.
- fam:src:C.2.3, tag 01QL, source header line 8014 and label line 8015:
  Theorem 6.6, retained final p.40; old entry I.4.5, p.34.
- fam:src:A.3.1, tag 01Q2, source line 8321:
  Proposition 7.5, retained final p.44; old entry I.7.4, p.51.
- fam:src:B.2.1, tag 01QB, source line 8916:
  Proposition 8.1, retained final p.52; the inherited number is already
  8.1, while its p.57 field is stale.
- fam:src:B.2.2, tag 01QC, source line 8993:
  Proposition 8.2, retained final p.54; the inherited number is already
  8.2, while its p.59 field is stale.

The remaining four I references are:

- push:src:E.1.1, tag 032R, source line 9198:
  Proposition 9.2, retained final p.57; old entry I.9.1, p.64.
- push:src:A.1.2, tag 02ZI, source line 16934:
  Theorem 20.6, retained final p.153; old entry I.14.2, p.103.
- push:src:A.2.2, tag 02ZK, source line 17400:
  Theorem 21.2, retained final p.159; old entry I.14.4, p.106.
- push:src:A.4.2, tag 02ZS, source line 18277:
  Proposition 21.12, retained final p.170; old entry I.14.11, p.118.

These fourteen findings are the exact used-target disagreements with
the inherited III dictionary. The pages are attributed to the retained
certified record; root's final displayed references use only paper,
number and the unchanged permanent target.

### Paper IV: current source numbers, with final renumbering deferred

The actual current IV source keeps theorem numbering by section
(preamble line 28) and aliases proposition and the other declared formal
environments to that same counter. The source query found no body
counter mutation. Following only the numbered section and formal-
environment tokens to the four target labels gives:

- night:P3K.7 is Theorem 4.8, tag 02VH, at source line 22827;
  its section starts at line 22333.
- night:P3K.65 is Theorem 5.13, tag 02VC, at source line 31904;
  its section starts at line 26400.
- night:P3K.68 is Theorem 6.1, tag 02VF, at source line 33931;
  its section starts at line 33927.
- iv:correction:P3K.6 is Proposition 8.2, tag 01US, at source line
  85059; its section starts at line 85012.

Each source-derived counter agrees with the existing selected row of
S6_SERIES_PUBLISH_tags.tsv and the current III SRef number. No IV
number/owner/tag mismatch is exposed. The selected inventory rows have
no current source/PDF binding fields, and no current IV final PDF is
attached. Therefore its inherited pages 249, 352, 374 and 934 have not
been promoted to current PDF evidence. The final III presentation omits
those page fields, uses the current source-bound numbers, and preserves
the tags for the later joint renumbering.

The current source has no actual outgoing V reference in these command
forms; no V source/PDF lookup was needed. This completes the bounded
actual-use reference preparation. It creates no independent check,
publication-page credit, derived mapping/table, or new build result.


## 7. Final used-reference preamble fragment

At 2026-11-25T21:00:32.798839+00:00, only
agents/continuation8_iii_integration/units/root/preamble.tex was edited.
The exact source edits are the 22 rows in
agents/continuation8_tex_runtime/S6_SERIES_PUBLISH_c8_tex_reference_defects.tsv.
No separate mapping, receipt, edit manifest or inventory was created.

The inherited block had 4,939 unique SRef definitions. The current
canonical body/front uses exactly 33 distinct keys: 22 external and
11 local. The 31 existing active old definitions were read in full;
the missing two II definitions have the exact evidence in sections 3
and 6. The 11 local target headings were read to confirm their literal
label and adjacent permanent-tag association.

The removal guard recognizes one contiguous block consisting solely of
unique SRef-definition lines; every removed key is absent from the
actual use set. Exactly 4,908 unused lookup entries are removed.
This guard concerns lookup syntax and actual use, and claims no new
reading of the unused cross-paper mathematics. Its exact original and
replacement text is retained in the D10 defects row itself.

Twenty D04 rows give the exact old and new active external definitions,
including their unchanged tags and corrected numbers. One D19 row adds
the two missing II definitions at the existing CurrentPaper marker.
Their common output form is a permanent-target link in the delivered
PUBLISH PDF with paper.number and no page field. The eleven retained
local definitions continue to use III followed by live ref* values.
Every final key is actually used, every used key has exactly one
definition, and all 33 final definitions are printed/read in the actual
readback. The complete preamble prefix, including the accepted AMS
dispatcher and repository macros, and the final suffix are unchanged.
The literal label and hypertarget multisets are unchanged.

CHECK_EVENTS receives no new row: this is a reference-presentation
edit and bounded locator verification, with no statement/proof recheck
or new mathematical checking credit. The existing event records keep
their types and chronology. No criterion is automatically closed.
Root owns canonical application and the actual final build/page gates.


Actual written-source and record readback is complete. The full preamble
fragment, every active old/new external guard, both inserted definitions
and all retained local definitions were read. Replaying the actual
serialized 22 defects rows in memory against the still-unmodified
canonical preamble found each exact old guard once and reproduced the
written fragment byte for byte. The current canonical use set still
matches the fragment's 33 definitions exactly.

The first TSV readback stopped at Python's default CSV field-size limit
(131072) because the exact D10 old-block field contains all 4,939
inherited definitions. Reading with csv.field_size_limit(16 * 1024 * 1024)
succeeded. That reader setting is also needed by a default Python CSV
importer of this local table. No table/source correction or extra
checking credit resulted from that readback adjustment.


## 8. Actual full-document build readings, 25 November 2026

Attribution: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed. These are actual TeX-output readings. They add no mathematical checking event, proof credit, publication-unit completion, or visual-page-reading credit.

### Pass 01

Root observed process exit 1. After process completion, the actual engine log was copied byte for byte to `code/S6_SERIES_PUBLISH_c8_tex_III_final_pass01.log` before the next pass. Its complete 2,988 lines (80,543 bytes), the complete 2,003-line stdout (50,557 bytes), and the actually empty stderr were read. The output filenames use the same prefix and `.out` / `.err` extensions.

The first and only fatal diagnostic is source line 7172: `Missing number, treated as zero`, while reading the array row beginning `[\mathrm{point}]\times z_3&u_0^3.`. The complete source display and its pairing context were read. The preceding row terminates with `\\`; the following `[` is consequently taken as that row command's optional spacing argument. The exact proposed source repair is the empty-group prefix `{}[\mathrm{point}]`, which terminates that optional-argument lookahead while leaving all three mathematical dual pairs unchanged. Root owns the D23 record and source application.

The engine shipped pages 1–78 and failed with page 79 pending; it explicitly reported no output PDF. No Overfull or Underfull box diagnostic appeared, hence none above 2pt. No package, format, font, or alias-hook failure appeared. The non-reference package warning was epstopdf's disabled shell escape, matching the wrapper. This incomplete pass did not reach the bibliography and supplies no final reference convergence or page-layout conclusion.

Three concrete reference-key errors were exposed separately from ordinary first-pass missing auxiliary data. The actual diagnostics contain leading spaces in ` maps:src:D.2.42` at input line 588, ` wb:cusp-cone-sharp-global-R4-scope` at line 605, and ` maps:src:D.2.38` at line 800. All three source contexts were read. Each comma-separated cref/Cref argument has an uncommented newline before that key. The proposed bounded repair is an immediately trailing `%` after the preceding comma or a single physical line for the complete key list; every label identity remains unchanged. Root is handling the exact source/defect records.

### Pass 02

Root observed process exit 1 and preserved `code/S6_SERIES_PUBLISH_c8_tex_III_final_pass02.log` before another pass. Its complete 2,211 lines (62,696 bytes), the complete 1,201-line stdout (32,584 bytes), and the actually empty stderr were read. The first and only fatal diagnostic is source line 8934: `Extra alignment tab has been changed to \cr` at `\end{split}`. Pages 1–98 were shipped before failure, and no output PDF was produced. Root is reading and repairing the exact split display.

No Overfull or Underfull box diagnostic appeared in pass 02, hence none above 2pt. There was no missing package/font or alias-hook error. The same three spaced reference keys remained in this pre-repair pass. Ordinary citations and references whose definitions lay beyond the earlier abort remain provisional until a successful complete pass reads the inline bibliography and subsequent passes converge. No final metadata extractor was run on either failed pass.


### Pass 03

The established no-shell-escape wrapper was run on canonical III with
`-interaction=nonstopmode -halt-on-error -file-line-error` and output directory
`agents/continuation8_tex_runtime/III_final`. The actual process exit was 1.
Before any later engine pass, its actual engine log was preserved as
`code/S6_SERIES_PUBLISH_c8_tex_III_final_pass03.log` (183,923 bytes).
The matching stdout is 153,113 bytes and stderr is actually empty.
The complete engine log was read, including every package line, warning,
page announcement, box diagnostic, and fatal tail. Exact in-memory line
alignment identified the portions also present in stdout; every one of the
123 stdout-exclusive text records was separately displayed and read.
Thus the whole actual stdout is covered, not just its diagnostic matches.
No saved comparison, receipt, manifest, or derived inventory was created.

The first and only fatal diagnostic is `Missing $ inserted` at input
line 41487, on the whitespace-only paragraph separator within the equation
`maps:eq:MT_local_5` / tag Q22E. The analogous immediately following
Q22F display was also read. The engine shipped provisional pages 1--478,
failed with page 479 pending, and explicitly reported no output PDF.
Root subsequently read all affected displays and applied the 91 exact
paragraph-separator repairs in the mixed-three proof; those applications
and their defect records remain root-attributed. A further read-only scan
of the current equation, align, gather, multline, flalign, alignat and
ordinary display delimiters found no remaining whitespace-only paragraph
immediately before a hypertarget inside those displayed constructs.
The scan excludes the `\\[spacing]` row-command syntax; an initial loose
pattern's frontmatter hit was read and identified as that syntax, not a
mathematical display defect.

There are 18 actual Overfull hbox diagnostics exceeding 2pt. Their input
coordinates refer to this preserved pass03 source, before the subsequent
repairs:

| Input line or paragraph | Width beyond measure |
| --- | ---: |
| 10887 | 2.66841pt |
| 12858 | 37.15933pt |
| 13571 | 72.90521pt |
| 14119 | 3.4316pt |
| 18680 | 20.702pt |
| 18973 | 49.8181pt |
| 19188 | 9.36247pt |
| 20985 | 39.15pt |
| 23306 | 78.0133pt |
| 23814 | 21.04941pt |
| 27314 | 8.26257pt |
| 32689--32699 | 117.49649pt |
| 39266 | 17.42854pt |
| 39272 | 2.45212pt |
| 39967 | 40.60501pt |
| 40334 | 24.85184pt |
| 40490 | 33.54132pt |
| 41449 | 2.53989pt |

The 0.83005pt diagnostic at 21212 is below the agreed threshold.
The two Underfull paragraphs are 21795--21797 (badness 10000) and
33396--33405 (badness 1152). Root left these for the actual final visual
reading; this failed pass supplies no visual-page conclusion.

Root took the first nine excessive-width contexts. The complete displays
and formal statements for the last nine were read here: the full sphere
filling statement maps:src:D.2.26; the all-original additive statement
maps:src:D.2.32 and its local Gysin argument; the whole Q139 numbered
remark; the full mixed-primary statement maps:src:D.2.38, its defining
marked input, and the surrounding nonsymmetric pairing, divided-power,
and CRT marking clauses; and the full mixed-three statement
maps:src:D.2.42 with its input and homology list. This is a bounded layout
reading, with no new theorem/proof recheck credit.

The exact nine old/new source proposals are executable data in
`code/S6_SERIES_PUBLISH_c8_tex_layout_proposals.py`. Its read-only run
exited 0; the entire `.out` and the empty `.err` were read. All nine
current canonical and fragment guards occur exactly once. Removing only
its changed alignment wrappers, alignment marks, row breaks, spacing
commands, and inline break opportunities gives identical non-layout
TeX tokens. Every literal label, target, outer equation construct,
formula coefficient, modulus, group, map and inverse remains in its
original order. Five numbered equations retain their single outer
numbering construct; the unnumbered displays remain unnumbered. The
fourteen-member inline weight list retains its sentence and every value.
No proposal begins an alignment row with a literal left square bracket.
The program writes no manuscript or shared record and claims no engine
success for these proposed layouts. Root owns review/application.

Other non-reference warnings are epstopdf's disabled shell escape,
eight hyperref bookmark-string math conversions, and amsmath's legacy
`\over` warning at input 39918. The latter complete formula was read:
`c_C=\tfrac12(K_{11}d_1+K_{22}d_2)={b\over2}\{a\kappa(b\kappa-\nu)-1\}`
with its two congruences and the existing MP_local_44 / Q21B identity.
It is nonfatal. The eight exact subsection titles were read and supplied
to root for optional `texorpdfstring` presentation repair while retaining
their printed mathematical argument. Their original input lines are
10046, 10493, 10836, 11665, 12461, 16883, 21388 and 24357.

Citations and forward references remain provisional: the failed pass
never reached the inline bibliography or a successful final auxiliary
write. No final extractor was run. Pass04 remains blocked pending root's
accepted source repairs. No mathematical check, unit criterion, or PDF
page was credited from this output reading or these layout proposals.


### Pass 04

The same wrapper/flags/output directory were used. The actual process
exited 1 after 9.407 seconds. Its fresh engine log was preserved before
any next pass as `code/S6_SERIES_PUBLISH_c8_tex_III_final_pass04.log`
(101,696 bytes, 4,737 physical lines). Every line was read. The matching
stdout has 70,889 bytes and 3,258 byte-line records: exact in-memory
alignment with the read log covers 3,135 records, and all 123 exclusive
records were separately displayed and read. Stderr is actually empty.

The first fatal is input 47220, `Improper \prevdepth`, at
`\paragraph{The integral marking.}` within the sole proof of
night:P3F.26 / tag 02S2. The complete preceding source/line argument,
its proof start and theorem, and the following marking context were
read. No unmatched mathematical delimiter is present in that context.
The engine shipped provisional pages 1--545 and reported no output PDF.

The installed package mechanism was read directly at these exact loci:

- `/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty`,
  431--440: the proof opens a trivlist and an item for its heading.
- `/usr/share/texlive/texmf-dist/tex/latex/base/latex.ltx`,
  14246--14278: the list sets `@newlist` true and its paragraph macro
  suppresses paragraph termination while that flag remains true.
- The same latex.ltx, 14354--14410: the item's pending everypar clears
  `@newlist`, emits the saved proof label and clears `@inlabel`.
- The same latex.ltx, 15606--15679: immediate run-in sectioning replaces
  everypar with its section-heading hook before the item hook runs.
- The same latex.ltx, 8895--8927: addpenalty uses prevdepth after attempting
  paragraph termination; the suppressed paragraph leaves the failing
  call in horizontal mode.
- `/usr/share/texlive/texmf-dist/tex/latex/base/article.cls`,
  314--317: paragraph has run-in afterskip -1em.

Exactly two actual proof starts have that immediate paragraph pattern.
Both complete owning theorem statements and first-heading contexts were
read. The first exact old/new guard is:

```tex
% Old, night:P3F.26 in units/later/os49_construction.tex
\begin{proof}
\paragraph{The source and its line.}
% New
\begin{proof}
\leavevmode
\paragraph{The source and its line.}
```

The second exact old/new guard is:

```tex
% Old, night:P3F.34 in units/later/os49_graph_caps.tex
\begin{proof}
\paragraph{The fixed exterior and the oriented boundary circle.}
% New
\begin{proof}
\leavevmode
\paragraph{The fixed exterior and the oriented boundary circle.}
```

The inserted leavevmode triggers the existing item paragraph hook before
sectioning replaces it. All paragraph headings, their adjacent targets
and labels, statement/proof membership and mathematical text are retained.
Root read the installed package evidence and applied precisely these two
insertions at 21:42:36.733479 UTC. Their Proof/title spacing remains an
explicit final visual-reading item; application alone supplies no layout
or mathematical checking credit.

All 18 pass03 excessive-width diagnostics and the eight bookmark warnings
are absent. One new Overfull hbox exceeds 2pt: 122.48746pt at input 41577,
the unnumbered table of 21 ordered profile/count pairs in the mixed-three
proof. Its complete source table and enumeration context were read and
sent to root. Root separately regrouped those same pairs in three bands
and owns the exact D23 application/evidence. No result was inferred from
the table's title or altered by this build reading.

The two subthreshold Overfull findings are 0.83005pt at 21241 and
1.34203pt in 44628--44639. Underfull paragraphs are 21824--21826
(badness10000),33435--33444(1152),42650--42657(1546),43837--43842(2181).
They remain final visual-review items. There is no alias-hook error or
missing package/font. A later legacy over command produces the next
amsmath warning at input 40411; the earlier MP_local_44 replacement is
already passed. Citations and labels beyond the prior abort remain
provisional until a successful complete pass. No final extractor ran.


### Pass 05

The same wrapper/flags/output directory were used. The actual process
exited 1 after 11.035 seconds. Its fresh engine log was preserved before
any next pass as `code/S6_SERIES_PUBLISH_c8_tex_III_final_pass05.log`
(80,495 bytes, 3,800 physical lines). Every line was read. Stdout has
49,672 bytes and 2,302 byte-line records: exact in-memory alignment with
the read log covers 2,179 records, and every one of the 123 exclusive
records was separately displayed and read. Stderr is actually empty.
This is an attributed engine/source-syntax reading by GPT-6 Astra Pro
(OpenAI), ChatGPT Pro mode; numerical effort not separately exposed.

The first fatal is input 48990, `Extra alignment tab has been changed
to \cr`, at the end of a split in the sole proof of night:P3F.31 /
stmt:P3F.31 / tag 02S8. The complete owning statement, the surrounding
radial-period/shell/coorientation argument at 48872--49020, and the full
display were read. The exact old display is:

```tex
\[
\begin{split}
 Z_H&=L_q-\log|ac|,&Z_K&=\log|a^3c^2|,\\
 V_H&=-\log|\lambda bd_0|,&
 V_K&=L_q+2\log|\lambda|+\log|b^3d_0^2|,\\
 D&=Z_HV_K-Z_KV_H .
\end{split}
\]
```

The first two rows each contain three outer alignment tabs; split
provides the single pair of columns. The exact proposed replacement
changes only the two environment names from split to aligned, retaining
the outer unnumbered display, all seven tabs, every formula and their
order. The block has no internal label or hypertarget. Root read and
applied that bounded replacement at 21:45:45.737825 UTC. No manuscript
source was written by this diagnostic work.

The actual repeated failure justified a bounded reading of the other
split environments. All 35 current literal split blocks, including the
five beyond this abort, were displayed and read in full. Only the above
block has more than one outer tab per row; each of the other 34 has at
most one, excluding cells within nested matrices/arrays. No additional
repair was proposed, and no generated environment inventory was saved.

The engine shipped provisional pages 1--566 and reported no output PDF.
There is no excessive box beyond 2pt. The 0.83005pt box at 21241 and
1.34203pt paragraph at 44630--44641 are below that threshold. Underfull
paragraphs are 21824--21826 (badness 10000), 33435--33444 (1152),
42652--42659 (1546), and 43839--43844 (2181). These remain final visual
items. No bookmark-conversion, alias, missing-package or missing-font
error appeared. The first repaired proof/paragraph start now passes;
the second lies beyond this abort and awaits actual engine execution.

The nonfatal amsmath recommendation at input 40411 is scoped to the
mixed-primary proof maps:src:D.2.38 / tag 02LE. The full surrounding
source at 40396--40424 was read. Its first remaining formula contains
`-2\left(a(\nu-b\kappa)-{b\over p}\right)` and
`2\left({b\over p}-a\nu\right)\pmod p`, retaining
maps:eq:MP_local_64 / Q21U; the next is
`P_p={b/p-a\nu\over2}\in\mathbb F_p`, retaining
maps:eq:MP_local_65 / Q21V. Root explicitly retained these formulas
pending their actual final visual appearance. This warning alone does
not block a successful build. No broad legacy-fraction rewrite is
proposed. Epstopdf's disabled-shell-escape warning is expected under the
required wrapper.

References and citations remain provisional because the pass did not
reach a successful complete auxiliary write or the inline bibliography.
No final extractor ran, and no mathematical check, criterion closure,
or PDF visual-page credit is claimed.


### Pass 06: first complete engine pass

The unchanged wrapper invocation, after root's exact two source edits,
exited 0 after 11.258 seconds. The new engine log was preserved as
`code/S6_SERIES_PUBLISH_c8_tex_III_final_pass06.log` before another pass:
116,265 bytes, 5,403 byte-line records. Every log line was read. An initial
combined tool output truncated, so the affected ranges were displayed
again separately before this whole-reading attribution. Stdout contains
84,742 bytes / 3,743 records: 3,596 match the fully read engine log exactly,
and all 147 exclusive records were separately displayed and read. Actual
stderr is empty.

The engine produced 690 pages / 4,446,217 bytes in the existing III_final
PDF path. No fatal error, missing font, alias-hook error, or box beyond
2pt appears. The two Overfull warnings remain 0.83005pt at 21241 and
1.34203pt at 44630--44641. Both leavevmode proof starts and the radial
aligned display passed actual engine execution. Their final visual
appearance remains unclaimed. The existing legacy-over recommendation
and disabled-shell-escape warning remain nonfatal, with their exact
scopes already recorded above.

In addition to the previously read four Underfull paragraphs, this pass
reached the later paragraph at 51826--51833 (badness 1062), the Programs
cells at 59035--59036, 59047--59048, 59106--59107, 59236--59237,
59358--59359, 59365--59366, 59378--59379 and 59406--59407, and the two
bibliography entries at 59684--59688 (1173) and 59855--59859 (1715).
Their actual warning contexts were read. They are final visual-review
items; no line-layout defect or correction is inferred merely from an
Underfull diagnostic.

This is the first pass to reach the bibliography and complete auxiliary
write. The log explicitly reports undefined citations/references,
changed citation/label records and changed PDF outlines. The next pass
is required to resolve them. The 690-page output is provisional: no
final metadata extraction, PDF visual-page credit, mathematical check,
or unit closure is assigned from this engine completion.


### Pass 07: references resolved, pagination rerun required

The unchanged invocation exited 0 after 10.977 seconds. The fresh engine
log was preserved as `code/S6_SERIES_PUBLISH_c8_tex_III_final_pass07.log`
(56,475 bytes / 2,718 byte-line records), and every line was read.
Stdout has 25,013 bytes / 1,051 records: 906 align exactly with the read
log, and all 145 exclusive records were separately displayed and read.
Actual stderr is empty.

All undefined reference and citation warnings have cleared. There is no
fatal error, missing font, alias error or box beyond 2pt. The same two
subthreshold Overfull and recorded Underfull contexts remain, as do the
nonfatal legacy-over and disabled-shell-escape recommendations. The PDF
has 694 pages / 4,478,512 bytes after the completed table of contents and
resolved reference text changed pagination.

An in-memory comparison of each auxiliary file before and after this
actual pass found: .aux changed (259,851 to 259,861 bytes), .toc changed
(16,984 to 16,985 bytes), and .out unchanged (36,755 bytes). No comparison
copies, manifest, hash table or inventory was written. The engine
explicitly requests a label rerun; therefore Pass08 is necessary. No
final metadata extraction or visual-page/criterion credit is assigned.


### Pass 08: converged engine output

The unchanged invocation exited 0 after 11.490 seconds. The fresh engine
log was preserved as `code/S6_SERIES_PUBLISH_c8_tex_III_final_pass08.log`
(56,393 bytes / 2,714 byte-line records); every line was read. Stdout has
24,931 bytes / 1,047 records: 902 align exactly with the read log, and
all 145 exclusive records were separately displayed and read. Actual
stderr is empty.

The engine reports a 694-page PDF of 4,478,489 bytes. There are no fatal
errors, missing fonts, undefined references/citations, alias errors,
boxes beyond 2pt, or rerun requests. The .aux (259,861 bytes), .toc
(16,985 bytes) and .out (36,755 bytes) are each byte-identical in the
in-memory before/after comparison for this pass. Engine runs stopped
at this actual convergence; no optional repeat is planned.

The only two Overfull diagnostics remain 0.83005pt at 21241 and
1.34203pt at 44630--44641. The previously enumerated Underfull contexts,
legacy-over recommendation and disabled-shell-escape warning retain
their exact recorded scope. Final visual reading still must examine
their rendered contexts and the Proof/title spacing of night:P3F.26
and night:P3F.34. This build result supplies no mathematical checking
credit or automatic source-unit/PDF-visual criterion closure.

Converged files are in
`agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III.{pdf,aux,toc,out}`.
The already reviewed, III-only final extractor is now being applied to
that actual source/aux/PDF, with its sole data output at
`agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III_final_metadata.json`.
No shared records or other paper are inputs or outputs of this extraction.


## 9. Final extraction and page-image reading preparation

The approved III-only extractor actually ran after Pass08 convergence and
exited 0 in 2.189 seconds. Its full 315-byte stdout and empty stderr were
read: 1,222 literal source labels, 1,216 literal hypertargets and 249 formal
environments; zero error rows and twenty warning rows. All twenty warning
rows, their exact aux and live destination records, and the source context
around each label were read. The 9,998,674-byte JSON remains the single
authorized data output; no shared table or other paper was changed.

The exact twenty page warnings are below. The automatic target and permanent
tag are distinct existing destinations; both actual values are retained.
No page correction or source edit has been inferred from the warning alone.

| Literal label | Source line | Aux number | Aux page | Aux-linked target / physical page / raw XYZ (left, top) | Permanent tag / physical page / raw XYZ (left, top) | Source mechanism |
|---|---:|---:|---:|---|---|---|
| `mapsIII:rem:cusp-replacement` | 1443 | 3.2 | 21 | `remark.3.2` / 20 / (70.866, 59.93) | `tag-Q007` / 21 / (70.866, 771.024) | Formal opening |
| `maps:src:B.5.1` | 4807 | 3.33 | 58 | `theorem.3.33` / 57 / (70.866, 77.8) | `tag-02JB` / 58 / (70.866, 771.024) | Formal opening |
| `mapsaudit:finite-degree-three` | 5587 | 3.36 | 66 | `proposition.3.36` / 65 / (70.866, 64.022) | `tag-02QE` / 66 / (70.866, 771.024) | Formal opening |
| `maps:src:C.1.2` | 5914 | 3.39 | 70 | `lemma.3.39` / 69 / (70.866, 61.922) | `tag-02K3` / 70 / (70.866, 771.024) | Formal opening |
| `maps:src:D.1.10` | 7000 | 3.51 | 82 | `lemma.3.51` / 81 / (70.866, 61.177) | `tag-02K8` / 82 / (70.866, 771.024) | Formal opening |
| `maps:src:D.2.2` | 9844 | 4.12 | 114 | `computed.4.12` / 113 / (70.866, 75.803) | `tag-02KU` / 114 / (70.866, 771.024) | Formal opening |
| `maps:src:D.2.16` | 17380 | 5.29 | 204 | `theorem.5.29` / 203 / (70.866, 59.837) | `tag-02KQ` / 204 / (70.866, 771.024) | Formal opening |
| `maps:src:D.2.29` | 25386 | 7.8 | 295 | `theorem.7.8` / 294 / (70.866, 61.676) | `tag-02L4` / 295 / (70.866, 771.024) | Formal opening |
| `maps:src:D.2.44` | 42888 | 7.58 | 500 | `theorem.7.58` / 499 / (70.866, 73.374) | `tag-02LL` / 500 / (70.866, 771.024) | Formal opening |
| `a-page-carrying-the-actual-source-line` | 48699 | 8.5 | 568 | `equation.8.13` / 567 / (105.787, 361.842) | `tag-0003` / 568 / (70.866, 309.619) | Label before paragraph |
| `the-full-graph-to-page-comparison-by-regular-bands` | 48777 | 8.5 | 569 | `section*.25` / 568 / (70.866, 294.483) | `tag-034V` / 569 / (70.866, 372.589) | Label before paragraph |
| `characteristic-calculation-and-the-scope-of-the-result` | 49304 | 8.5 | 575 | `section*.29` / 573 / (70.866, 290.037) | `tag-01GY` / 575 / (70.866, 510.248) | Label before paragraph |
| `the-page-including-the-finite-cap-line` | 49597 | 8.6 | 578 | `section*.31` / 577 / (70.866, 317.309) | `tag-034Z` / 578 / (70.866, 395.234) | Label before paragraph |
| `the-actual-graph-line-and-return` | 49692 | 8.6 | 579 | `section*.32` / 578 / (70.866, 380.366) | `tag-034Q` / 579 / (70.866, 420.902) | Label before paragraph |
| `wb:cusp-s12-all-higher-smashes-null` | 52654 | 11.6 | 612 | `corollary.11.6` / 611 / (70.866, 60.459) | `tag-038T` / 612 / (70.866, 771.024) | Formal opening |
| `mapsIII:lem:radial-slice-embeddings` | 53670 | 12.10 | 623 | `lemma.12.10` / 622 / (70.866, 62.89) | `tag-Q30T` / 623 / (70.866, 771.024) | Formal opening |
| `wb:cusp-cone-metric-scope` | 53760 | 12.11 | 624 | `proposition.12.11` / 623 / (70.866, 59.744) | `tag-036W` / 624 / (70.866, 771.024) | Formal opening |
| `wb:cusp-cone-S12-sphere-map-null` | 54956 | 13.5 | 637 | `remark.13.5` / 636 / (70.866, 68.539) | `tag-035Z` / 637 / (70.866, 771.024) | Formal opening |
| `wb:cusp_s12_carrier_homotopy:L567` | 56357 | 14.6 | 652 | `corollary.14.6` / 651 / (70.866, 59.353) | `tag-03A6` / 652 / (70.866, 771.024) | Formal opening |
| `wb:cusp-s12-native-smash-null` | 56456 | 14.8 | 653 | `corollary.14.8` / 652 / (70.866, 68.723) | `tag-Q254` / 653 / (70.866, 771.024) | Formal opening |

For the fifteen formal openings, the source places the literal tag and
label immediately after begin{theorem/lemma/etc.}. The automatic target is
near the preceding page bottom (PDF vertical coordinates 59.353--77.800),
while the permanent tag is at coordinate 771.024 on the aux page. The
actual images must establish the heading/page-break appearance. For the
five OS49 proof-paragraph labels, the source explicitly places tag+label
before the next paragraph command. Their aux title/current target still
names the preceding numbered display or preceding paragraph. This explains
the recorded target ownership directly from the exposed source order; it
does not assign those paragraph anchors a new theorem number. Their exact
printed headings and permanent-target location remain visual-reading items.

The PDF skill was read in full for rendering and image-based inspection.
The single unchanged converged PDF has SHA256
`798f814252fc3fd72809a96d7fa946b0e09e2daadfd153f8f6cc83f8ab92c43e`,
computed once for the coordinated readers. The renderer source is
`code/S6_SERIES_PUBLISH_c8_tex_render_final_III.py`; its actual complete
801-byte stdout and empty stderr were read. It ran from
2026-11-25T21:53:27.170041+00:00 to 21:54:49.089254+00:00, with each of its
five bounded pdftoppm jobs exiting 0 and no missing requested page image.
The PDF size/mtime remained unchanged throughout. No engine or extractor
was rerun.

The stable full-page PNG directory is
`agents/continuation8_tex_runtime/III_final/pages`, named
`page-001.png` through `page-694.png`, rendered at 150dpi. Root owns
physical pages1--94 and681--694; lg_fresh95--294; lv_compare295--494;
tex_runtime495--680. Boundary warnings may receive targeted overlapping
inspection, while every page has one primary reader. Each reader records
only images actually displayed and read, with substantive page-specific
observations. Rendering itself supplies no visual-page credit.


### Exact five pre-paragraph label contexts

Source 48697--48702; inherited aux title `The positive fan and source line`:

```tex
quotients contain each complete source \(I_2\) neighbourhood.

\hypertarget{tag-0003}{}\label{a-page-carrying-the-actual-source-line}
\paragraph{The page and its compact model.}
On a regular cut band write the arrow in a unitary line coordinate as
\[
```

Source 48775--48780; inherited aux title `The page and its compact model`:

```tex
so the height is \(1/2\) and the component correction is \(3/2\).

\hypertarget{tag-034V}{}\label{the-full-graph-to-page-comparison-by-regular-bands}
\paragraph{The cusp product and based marking.}
The full period \(K=h^3g^2\) is
\[
```

Source 49302--49307; inherited aux title `The cap sphere and its normal Euler number`:

```tex
coefficient of b is exactly \(-1\).

\hypertarget{tag-01GY}{}\label{characteristic-calculation-and-the-scope-of-the-result}
\paragraph{The integral square and return.}
Put \(N=12k\), and let
\(V:\mathbb Z^{N+1}\to\mathbb Z^2\) have the displayed nodal
```

Source 49595--49600; inherited aux title `The closing map and its origins`:

```tex
path and its endpoint arrows to the displayed based formulas.

\hypertarget{tag-034Z}{}\label{the-page-including-the-finite-cap-line}
\paragraph{The finite cap and page line.}
First take \(n=1\).
In the finite origin of \cref{night:P3F.26}, the cap generator is
```

Source 49690--49695; inherited aux title `The finite cap and page line`:

```tex
square \(-2k\).

\hypertarget{tag-034Q}{}\label{the-actual-graph-line-and-return}
\paragraph{Transport of the graph and the return.}
For \(d=0,n=1\), the m-sheet construction just given is the
one used in \SeriesRef{night:P3F.31}.
```

"""Write checkpoint-facing status from actual receipts, without awarding proof gates."""
from pathlib import Path
from collections import Counter
import csv,json,re,datetime
from assemble_series import ABSTRACTS,TITLES
ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(10**9)
rows=list(csv.DictReader((ROOT/'S6_SERIES_GRIND_inventory.csv').open()))
events=list(csv.DictReader((ROOT/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
# The clock receipt is the authoritative session elapsed-time reference.
report='''INCOMPLETE

# S6_SERIES_GRIND report

## Authority and preservation

Fresh work from the attached base archive and prompt only. The first clock observation was 19 November 2026, 18:40:01 UTC (19:40:01 Europe/Berlin). No earlier conversation, Library content or Space was searched. All 950 payload entries in the six supplied manifests match size and SHA-256. The source archive and extracted tree are unchanged.

## State at checkpoint 01

The five full standalone LuaLaTeX papers have been assembled and compiled. This checkpoint preserves work in progress; it does not claim that the whole series meets the requested proof, credit, format or confidence standard. Mathematical status and present completion status are separate inventory fields. The source status of a row is preserved until a mathematical audit justifies changing it.

The split is exact: former VI follows former II in new II; former III section 6 moves to new V; the remaining III material stays in III. The moved section includes explicitly marked complex-dimension-five constructions, whose dimension is retained. All 442 old cross-paper occurrences, including six tagged-equation occurrences, were resolved to source labels before renumbering. Current references use those labels and immutable named PDF destinations. Final cross-paper page verification remains a gate while layout changes.

The 77 former rung-zero blocks have been grouped into 34 lettered main theorems (7,7,7,7,6). Each has a mechanism, source relationship, and a linked outline of 3–7 steps. The body statements retain their complete supplied proofs. Long printed check records have moved to five external check files; statement headers show the tag, one-word status, checks, declared uses, reverse-use link and applicable outline back-links. Proofs have numbered steps and return links to section 1. The semantic check of every outline against every expansion is still in progress. The current organization diagrams are provisional relationship maps; actual audited theorem dependencies are being collected for replacement.

## Changes and discrepancies

1. The prompt's count of 34 iv:correction:* rows is an overcount. There are 33; together with the other six named rows, the high-risk total remains 39. The audit records each actual row.
2. All 16 sweep corrections were compared with the received papers. The remaining reference-fan qualifications in P3K.7, P3K.8 and P3F.17 are now stated locally. The conormal integral-component statement C.2.INT.3 now displays its already-used H²(Y;Q)=0 hypothesis.
3. The physical line M, its dual U=M⁻¹ and the positive generator normalization were independently re-derived. At Jin coordinates (8,8), the physical formula μ=(4k−ℓ)/672 gives +1/28. Current web retrieval of the cited Jin version failed; the exact received opening record remains available, and the new calculation is explicitly relative to those coordinates.
4. The IV correction of P3K.22 had H¹ where its proof uses H²; this is repaired. Full old and replacement text and the reason are retained in analysis/applied_patches.json.
5. The Liu–Rollenske covering theorem now names its retained periodic fan and cap attachments. The one-turn parameter changes the Albanese nome; the two-turn endpoint map remains the precise global statement. P3K.36 remains a refuted historical assertion.
6. Paper I inv:D4.5 incorrectly invoked a globally closed Green representative from the open coefficient-atlas question. Its proof only needs the established bar-partial-closed representative Gγ=G0/12. The proof and uses list now cite inv:C3.1–C3.2, removing the open dependency.
7. Paper I now gives the exact pointed coordinate maps from the original AC cubic to the arithmetic and geometric cubics, including invariant-differential and lattice transport. These maps were independently checked symbolically.
8. Night rows P1.6 and P1.14 already had inventory identities. They are retained as independently reconstructed proofs of maps:src:F.4.1. P5.7 is now printed in the credited appendix, with the exact constant parameter translation and the permitted DGKX v1/v2 comparison.
9. Twenty-seven ARI A source rows were absent from the inherited inventory. They are appended with their original identity and an explicit editorial disposition; no old row is deleted. The 34 new consolidated main statements have additional inventory rows.
10. Unused bibliography entries are removed from the publication bibliography. The current five papers cite 336 keys; no cited key is missing from the source bibliography. Existing source-opening records remain, while the main-result literature comparisons continue. No new source is called verified solely because a title or abstract was found.
11. The original source contained duplicate section labels between II and VI. The moved VI section labels are namespaced in new II. Original theorem and equation identities remain stable.
12. The source-specific workflow prose still present in several expanded IV arguments, the eight unlabelled IV scope remarks, final dependency figures, required geometric figures, and several computation-file references require further editorial reconciliation. These are live gates, not silent omissions.

## Confidence work and exact receipts

### I

The statement-only derivation and comparison are in audit_paper_i/preproof_derivations.md and audit_paper_i/AUDIT_PAPER_I.md. Independent exact code checks the Weierstrass equation and differential maps, cusp period transport, generalized-origin/deck construction, Heisenberg and modular lifts, determinant identities and higher-twist residues. The root-domain and fundamental-set checks use the original source conventions. The open coefficient-atlas and period questions retain their proved reductions.

### II

The sign audit begins from 89 statement-only blocks, with derivations written before the printed proof comparison. It re-derives arbitrary-multiplicity parity, blowup defect, wedge-pairing signatures, local-system and Liu–Rollenske calculations, the classification table and occurrence models, compact-core estimates and identity return germs. Primary source reads include Steenbrink, Guillot and the original Kulikov papers. The latter supply the maximal ruled-component choice, split branches, contraction order and overlap calculations used by UN77/81/84. The UN1–86 catalogue is still being completed; no whole-chain certification is inferred from checking selected steps. Exact coverage and remaining original-source locators are in audit_sign.

### III

The full source body has moved with exact label transport. The isolated degree and fan hypotheses remain displayed. Literature and proof comparisons for the natural-line specialization and the main outline are in progress; the open realization row maps:src:D.2.4 remains in the final part.

### IV

The correction audit independently reconstructed orientation, Hermitian duality, spin-c filling and physical characteristic-number signs. New code completed 29 exact sign checks and 33,300 gcd cases. A separate fresh program completed 22,697 exact fan, primitive lattice, reduced-cap, cubic and Pontryagin checks, including all 28 K106 witnesses and the sixteen-value images. The 33 historical correction proofs and the common ordinary-boundary product-cap argument were compared in their precise scopes. The detailed row reports and outputs are in audit_corrections. The later endpoint and attachment rows remain under mathematical review.

### V

A fresh program starts from the printed rank-six connection, derives root gauges, transports along the positive real axis, solves the normalized integral intertwiner and certifies the three Hermitian endpoint values by Arb balls. It reuses no earlier arrays or code. The infinity-root central square has a certified positive Hessian on four closed boxes. The full closed-domain cover is still being reconstructed; that global certificate remains a substantive gate. Current literature comparison identified exact positive morphisms to the cited almost-complex classification and to the higher-dimensional periodic quotient of Yang; replacement credit and cited-specialization proofs are in preparation. Files are under audit_paper_i/paper_v_review and audit_corrections.

## Open mathematical rows

'''
for r in rows:
 if r['status'] in ('open','proved under hypotheses H'):
  report+=f"- `{r['label']}` (Paper {r['paper']}): {r['status']}; preserved in the final part. No change of mathematical status is claimed at this checkpoint.\n"
report+='\n## Evidence and inventory counts\n\n'
report+=f"The inventory has {len(rows):,} rows: 1,524 inherited rows, 27 recovered ARI A rows, and 34 consolidated main rows. The event ledger has {len(events):,} typed rows. Shared evidence groups prevent alias placements being counted as independent methods. Five series-level reconciliation events have no individual statement tag and remain in the full ledger.\n\n"
report+='| Event type | Recorded rows |\n|---|---:|\n'
for k,n in sorted(Counter(e['type'] for e in events).items()):report+=f'| {k} | {n:,} |\n'
report+='\n## Typesetting before and after\n\n'
report+='| Paper | First-pass pages | First-pass overflows >2pt | Current pages | Current overflows >2pt | Missing fonts/glyphs | Undefined references/citations |\n|---|---:|---:|---:|---:|---:|---:|\n'
for p in ['I','II','III','IV','V']:
 old=json.loads((ROOT/f'code/outputs/build_01/S6_SERIES_GRIND_{p}_diagnostics.json').read_text())
 files=sorted((ROOT/'code/outputs').glob(f'build_*/S6_SERIES_GRIND_{p}_diagnostics.json'));new=json.loads(files[-1].read_text())
 report+=f"| {p} | {old.get('pages','')} | {len(old['overfull_above_2pt'])} | {new.get('pages','')} | {len(new['overfull_above_2pt'])} | {len(new['missing_fonts_or_glyphs'])} | {len(new['undefined_warning_lines'])} |\n"
report+='\nExact presentation-only repairs are in code/layout_repairs.py. Font selection is explicit. The table-of-contents page-number width accommodates four-digit pages. Rendered-page inspection receipts will identify every formerly overflowing page and the sample pages inspected. Successful compilation alone is not recorded as visual inspection.\n'
report+='''
## Continuing from this checkpoint

Restore the attached base tree and this checkpoint; verify the checkpoint file list. Do not rerun initialize.py or extract_structure.py over the edited working parts. Current authored parts are parts/*.body.linked.tex; the frontmatter owners are named in code/outputs/assembly.json. The assembler, evidence merger, record generator and build script are the repeatable pipeline. The downloaded LuaLaTeX package is supplied under code/dependencies; the build script extracts it when needed and uses a relative TEXMFCACHE.

Outstanding main gates are: row-by-row confidence and scope assessment; the remaining rigorous numerical certificates; known-result credit and proof shortening; mathematical open-row push; complete dependency and geometry figures; workflow prose removal; final tag/reference/PDF-destination validation; all required rendered-layout inspection. Historical checks count with their actual scopes, and no mechanical number of fresh checks replaces mathematical judgment.
'''
(ROOT/'S6_SERIES_GRIND_report.md').write_text(report)
ledger='''# Progress ledger

## 2026-11-19 18:40 UTC — fresh run

Main question: five complete papers in the requested standardized form, with every inventory row placed and checked.

Initial gate: 1,524 inventory rows require placement, standardization and evidence assessment; the source has six papers and the deliverable has five. Mathematical statuses are retained as received.

The first three-hour review is due approximately 21:40 UTC; subsequent reviews are hourly. Checkpoint 01 is due approximately 19:25 UTC, then every 45 minutes. A checkpoint is a preservation operation, not a movement review.

## 2026-11-19 19:25 UTC — checkpoint 01 working state

The five-paper split, exact numeric-to-label reference transport, immutable tag registry, 34 consolidated main statements and external evidence files have been produced. Independent audits repaired the Green representative dependency and remaining fan/cohomology scopes; the high-risk IV arithmetic and sign calculations agree. The sign-chain original-source gap is smaller after opening the original Kulikov papers. The V certificate gate is smaller: all three root values and the central infinity-root Hessian are now independently certified; the global closed cover remains.

No three-hour movement review has occurred. No unchanged mathematical open row is declared solved. Whole-row completion states remain explicit in the inventory while the global proof/scope and final layout assessments continue.

### Open mathematical rows

'''
for r in rows:
 if r['status'] in ('open','proved under hypotheses H'):ledger+=f"- `{r['label']}`: {r['status']}; Paper {r['paper']}; exact received reduction retained; next mathematical audit pending.\n"
ledger+='''
### Current main gates

- I: audit full consolidated scopes and the remaining open coefficient/period questions; complete geometric figures and numerical certificate provenance.
- II: finish every UN1–86 step comparison and remaining primary source locators; retain D.2.5 unrestricted scope only with its full reduction verified.
- III: complete statement-to-outline comparisons, natural-line literature check and open realization push.
- V: complete the independent global Hermitian minimum certificate, exact cited-specialization credit, and full characteristic/deformation scope comparison.
- IV: close the later endpoint/attachment rows where the supplied complete arguments verify; finish global physical M, fan and cap scope propagation.
- All: final typesetting, actual theorem dependency figures, workflow removal, reference-destination validation and per-row completion decisions.
'''
(ROOT/'PROGRESS_LEDGER.md').write_text(ledger)
deposit='# S6_SERIES_GRIND deposit fields\n\nStatus: work in progress; these fields accompany the current texts and do not assert deposit readiness.\n\n'
for p in ['I','II','III','IV','V']:
 deposit+=f"## Paper {p}\n\n**Title:** The (3,4,∞) family of complex six-spheres. {p}. {TITLES[p]}\n\n**Abstract (TeX):**\n\n{ABSTRACTS[p]}\n\n**Production and checking:** AI-produced by GPT-5.6 Sol (OpenAI), reasoning effort ultra, 24 August–9 September 2026; GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 12–19 November 2026; Claude Fable 5.2 (Anthropic), efforts high and max, and Claude Opus 5.5 (Anthropic), effort max, 12–19 November 2026. The work combines source comparisons, statement-first derivations, exact and interval computations, and scope and convention checks; the paper's check file gives each event and its limitations. The current global assessment remains in progress. No human has checked the mathematics. The text is dedicated to the public domain under CC0 1.0.\n\n"
(ROOT/'S6_SERIES_GRIND_deposit_fields.md').write_text(deposit)
print(json.dumps({'report_written':True,'inventory_rows':len(rows),'event_rows':len(events)}))

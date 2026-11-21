#!/usr/bin/env python3
"""Close Paper V's publication gate only against its exact final receipts."""
from pathlib import Path
import collections, csv, datetime, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(name):
    return json.loads((ROOT / name).read_text())

source = ROOT / 'S6_SERIES_PUBLISH_V.tex'
source_sha = sha(source)
pdf = read('records/S6_SERIES_PUBLISH_V_final_pdf_receipt.json')
meta = read('records/S6_SERIES_PUBLISH_V_current_metadata.json')
mapping = read('records/S6_SERIES_PUBLISH_V_defect_page_mapping.json')
prov = read('agents/provenance/S6_SERIES_PUBLISH_V_provenance_disposition_receipt.json')
counts = read('agents/provenance/S6_SERIES_PUBLISH_deposit_fields_V_receipt.json')
deps = read('records/S6_SERIES_PUBLISH_V_main_dependency_dispositions.json')
for v, key in ((pdf, 'source_sha256'), (meta, 'source_sha256'),
               (mapping, 'current_source_sha256'), (prov, 'paper_source_sha256'),
               (counts, 'source_sha256'), (deps, 'source_sha256')):
    assert v[key] == source_sha, (key, v[key], source_sha)
assert pdf['certified'] and pdf['all_pages_read'] and pdf['covered_pages'] == pdf['page_count']
assert meta['certified_flag'] and mapping['certified']
assert not prov['remaining_claim_actions'] and not deps['pending_required_V']
assert counts['merged_ledger_sha256'] == sha(ROOT / 'CHECK_EVENTS.tsv')
assert sha(ROOT / 'S6_SERIES_PUBLISH_V.pdf') == pdf['pdf_sha256']
assert 'source-only change' not in mapping['current_mapping_methods']
old = (ROOT.parent / 'source/S6_series_V_corrected_20261120.tex').read_text()
new = source.read_text()
identities = {}
for name, pattern in [('labels', r'\\label\{([^}]+)\}'),
                      ('permanent_tag_targets', r'\\hypertarget\{(tag-[^}]+)\}')]:
    a, b = set(re.findall(pattern, old)), set(re.findall(pattern, new))
    assert not a - b, sorted(a - b)
    identities[name] = {'corrected_start': len(a), 'current': len(b), 'lost': []}
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
gate = {'paper': 'V', 'completed_utc': now, 'source_sha256': source_sha,
        'pdf_sha256': pdf['pdf_sha256'], 'pages': pdf['page_count'],
        'logged_edits': mapping['rows'], 'defect_types_closed': [f'D{i:02d}' for i in range(1,25)],
        'provenance_claims_closed': prov['rows'], 'current_main_dependency_environments': deps['current_main_dependency_environments'],
        'pending_required_checks': [], 'identities': identities, 'counts': counts['counts'],
        'ledger_sha256': counts['merged_ledger_sha256'],
        'remaining_series_gate': 'Regenerate cross-paper references and repeat the five-paper notation, reference and introductory-part consistency review after I–IV are complete.',
        'scope': 'Publication gate for this exact source/PDF snapshot. This receipt creates no mathematical event and makes no human-verification claim.'}
(ROOT / 'records/S6_SERIES_PUBLISH_V_complete_gate.json').write_text(json.dumps(gate, indent=2) + '\n')

ledger = ROOT / 'PROGRESS_LEDGER.md'
s = ledger.read_text()
s = s.replace('Work began22:42UTC20November2026.', 'Work began at 22:42 UTC on 20 November 2026.')
s = re.sub(r'Current gate: complete Paper V editorial, mathematical, provenance, build, and rendered-page reviews; then I, II, III, IV in that order\.',
           'Current gate: Paper V is complete at its recorded source/PDF snapshot. Complete Paper I, then II, III and IV, followed by the series consistency review.', s)
s = re.sub(r'^(\| V \| D\d\d:[^|]+\|)[^\n]+$', r'\1 done; final source/PDF receipt and exact edit log verified |', s, flags=re.M)
s = s.replace('| V | open |', f'| V | done; all {pdf["page_count"]} final page images have complete reading evidence |')
s = s.replace('Every source row below is retained as an open record. The exact subset of two-check results in main-theorem dependency chains is being computed.',
              'The CSV below preserves the received underchecked-result census as history. Current dispositions are recorded in the dated updates and the recomputed required-check tables. Paper V has no outstanding required check; its 20 remaining two-check identifiers belong to supplementary results outside the current main-theorem dependency closure.')
s = s.replace('Claim-by-claim audit is in progress. Until populated, all methodology counts, novelty/correction claims, contribution dates, and pinned-link checks remain open.',
              'Paper V: all 40 current provenance claims have recorded dispositions against supplied records, recomputed counts and primary sources, with synchronized deposit fields. The source and ledger hashes are bound in the provenance receipt. Claims for Papers I–IV remain open.')
heading = '## Paper V completed'
assert heading not in s, 'Do not duplicate a completion record'
s += f'''\n{heading} — {now}\n\nAll 24 defect-type gates are closed for the final 177-page source/PDF snapshot. Every final page has a complete reading record, with an earlier reading carried only by whole-image byte equality. All build defect counts are zero. The 1452 edit rows have current locations and honest corrected-start/intermediate dispositions. All 465 starting labels and 462 permanent tag targets remain.\n\nThe 80-environment main dependency closure has no outstanding required third check. The final ledger has 7452 associations; V's current 120 environments and 126 retained statement identifiers have 334 targeted, 45 independent-reproof, 166 computation/certificate, 340 reread and 86 background associations. Outline associations remain separate (8 targeted, 3 reproof). The 40 provenance rows and deposit fields match this exact ledger and source.\n\nSource SHA-256: `{source_sha}`. PDF SHA-256: `{pdf['pdf_sha256']}`. Receipt: `records/S6_SERIES_PUBLISH_V_complete_gate.json`. This closes Paper V's individual review; the later five-paper reference/notation review remains open. Work now proceeds to Paper I, then II, III and IV.\n\nCheckpoint 02 was saved at 00:12:49 UTC on 21 November 2026. Checkpoint 03 is due at 00:57 UTC. The first mandatory progress review remains 01:42 UTC (02:42 Europe/Berlin); no mandatory review has yet occurred.\n'''
ledger.write_text(s)

report = f'''INCOMPLETE

# S6 series publication revision

Work began on 20 November 2026 at 22:42 UTC (23:42 Europe/Berlin), from the attached base archive. No continuation checkpoint was attached. Paper V starts from the supplied corrected source. Its individual publication gate is now complete. Papers I–IV remain to be completed in that order, followed by the final series-wide review.

## Current gate

Paper V has a clean, fully read 177-page PDF. Its exact source/PDF hashes, 24 closed defect types, 1452 logged edits, 40 provenance claims and required-check dispositions are bound in `records/S6_SERIES_PUBLISH_V_complete_gate.json`. Work proceeds to Paper I. The full five-paper task remains incomplete.

## Paper V: structure and content preservation

The compact rank-six construction comes first. Its marked cusp and common integral collapse precede the lifted-period and global homology arguments. The integral classification occupies descriptive sections, with local complex compatibility and fixed-rank lemmas before the reductions that use them. The resolved Weierstrass construction and shifted fivefolds occupy separate later parts.

The integral cusp homology, restriction calculation, torsion transgression, global integral homology and lifted periods each have one operative proof. Independent alternate arguments are preserved in the checking records. The numerical minimum and enclosure theorems share one analytic remainder argument. The shifted-product uniqueness proof is consolidated in the stronger varying-family proposition; its smooth-type proposition is consolidated in the complete framed-handle theorem, retaining the original label and tag as an alias. Alternate nonprojectivity and algebraic-reduction arguments remain in the checking records.

The exact primitive-contraction scalar is 625πi/16, and the full wedge-period morphism is explicit. The algebraic auxiliary coordinate is z=(625πi/128)ξ. Base/fibre conjugation acts by ξ↦−conjugate(ξ), through the displayed real involution K; it fixes the imaginary subfamily and uses K inverse in the boundary period comparison. The root-frame limit at infinity and exact real preconditioning matrix are stated where used. These identifications preserve the exact maps and constants.

Equations use automatic section numbering. Dynamic references replace literal old equation identifiers and stale range endpoints. New definitions and remarks are numbered and tagged. A small permanent tag is the sole visible statement metadata. A two-page table lists 44 operative/example programs in 19 groups with pinned links. Paths and operation-count bookkeeping are removed from proofs. The shared bibliography records verification scope, journal metadata and the exact cited preprint editions.

The source retains all 465 labels and 462 permanent tag targets of the corrected starting file; it now has 516 labels and 484 targets. Eleven cp10 registry identities were already absent from that corrected starting file. Their historical dispositions are preserved without counting them as current printed statements. No original identity was newly lost. The final series review will resolve any incoming references from I–IV against these recorded dispositions.

## Checks and mathematical scope

Independent topology work includes finite integral restrictions, global order-two classes and the three torsion transgressions; the 26-simplex/74-incidence Kuhn complex and primitive-collapse ranks; characteristic numbers and reflection descent; the 56 involution classes; affine powers and cusp conditions. The required third independent checks for `maps:src:F.2.28` and `maps:src:F.2.30` are recorded. The support-function line bundle and its Chern-form sign were restored and checked. The resolved-product morphisms, markings and integral specialization were compared with the supplied arguments.

Independent analytic work includes Gauss–Manin and wedge matrices, root-line/Hodge/tangent calculations, cusp rank, automorphisms and Oka spanning directions. The supplied Arb certificate was rerun. Separate exact finite-cover/Bernstein checks and a newly implemented DOP853 calculation corroborate the period minimum. The floating comparison supports about 14 digits; it is recorded at that numerical scope. Normalization and conjugation identities were checked exactly.

Final global comparisons cover all six main theorems, their outlines and cited body mechanisms. Each event retains its actual model, effort, method and scope. A visual page reading or metadata scan creates no mathematical event. Rewritten-proof comparisons are recorded as used-and-rechecked associations. Shared evidence groups are retained, so applying one calculation to several results does not create several independent calculations.

At V's completion, the merged ledger contains 7452 associations. V has 120 printed environments and 126 statement identifiers, including retained aliases without duplicating events:

| Recorded kind | V associations |
|---|---:|
| Targeted proof examinations | 334 |
| Independent re-derivations | 45 |
| Computations or formal certificates | 166 |
| Used and reread | 340 |
| Background carried without fault found | 86 |
| Total | 971 |

These associations belong to 894 declared evidence groups. The outlines have another 8 targeted and 3 reproof associations, counted separately. The exact statement/immediate-proof/own-outline dependency calculation gives 80 main-closure environments and no outstanding required V check. Twenty supplementary two-check identifiers lie outside that closure and remain explicitly listed. Earlier metadata had incorrectly attached the whole introduction and Further results list to the last main theorem; correcting the extraction boundary removed those spurious reference edges without changing any event.

## Discrepancies and repairs

No contradiction in an original main theorem was established during this revision. The introduction had attributed the order-two transgression to the cusp; it now states the proved finite order-four suspension mechanism. The resolved-construction headline states the proved maps r:Z→the Weierstrass model and Π:Z→X, together with the bimeromorphic map to the literal fibre product. The change records the exact proved scope; the work establishes no universal impossibility result about alternative resolutions.

An early merger draft conflated raw and normalized contractions. The exact scalar and wedge morphism were derived before integration. The original base/fibre conjugation left the full complex-parameter relabelling implicit; the explicit relabelling preserves its original imaginary family. A needed support-function construction temporarily removed during consolidation was restored. A checking agent's preliminary root-sign error was corrected against its exact calculation and recorded.

Page review found stale theorem and range references, a literal equation name, repeated proof passages, an auxiliary coordinate defined after use, stranded headings and incomplete citation locators. These are repaired with exact before/after text. Theorem E's repeated negative clause could make an unboundedness statement appear to concern only three-connected outputs; its headline now gives the all-input algorithm and the exact three-connectivity tests, while the body retains the explicit trace family and input-height bound.

Three visual suspicions were cleared by source/enlarged-image comparison: the kernel/cokernel wording, a preposition and an article. Their original text was correct, so no source refutation is claimed. The 1452-row defect log records all applied edits. Every current printed change has a mapped location; nonprinting preamble and shared-bibliography edits are labelled separately. Intermediate wording absent from the corrected starting source is identified explicitly, without inventing a starting-PDF page or claiming it never appeared in another candidate.

## Primary sources and provenance

The base ZIP SHA-256 is `1cfbca4f84d07edfc765c639c42eb7aa4833cf4542776da1dcde267a03a24510`. It was unpacked once. All 963 shipped cp10-manifest files match their recorded size and hash; 2221 recorded outputs/PDFs are intentionally absent from the attachment. The repository pin resolves to `83d76022bcd442278b760db9ff438afceed6c6ea`. Its V source is byte-identical to the supplied source; CHECK_EVENTS and tags agree under the recorded CRLF-to-LF map. The historical pin is described at its historical scope. New revision records accompany this source distribution.

All 35 original V provenance claims and five supplements have closed dispositions against the attached records, recomputed counts and opened primary sources. The deposit fields contain the exact current abstract and required authorship opening. Their current source hash and ledger hash agree with the manuscript and counts above. Novelty descriptions have the scope supported by the recorded source searches; no exhaustive priority audit is claimed.

Primary-source receipts include the toroidal quotient, integral classification, sphere absorption, exterior-square representation, Oka implication, analytic remainder estimates, Whitehead exact sequence and Milnor's characteristic embeddings, gluing and isotopy extension. The exact Milnor locators include Theorem 1.4 on page 2 and its use on pages 25–26, Theorem 3.13 on pages 31–32, and Theorem 5.8 on pages 63–64; V proves the relative/framed collar adaptation it uses.

Final locator repairs cover Grauert §7 Satz 5 (pages 63–64); Engel's operations and section construction; Jia–Meng Theorem 1.1 and Remark 1.2; Esole–Kang identities (1.2)–(1.4); Peters–Sterk Theorem 2.2.1; the versioned Stacks Cohomology of Sheaves lemmas at tags 01F2 and 09V5; Hirsch's isotopy extension; Scott's Seifert-fibration results; Davis–Kirk's spin discussion; Winter's opened v3 discussion; and Oka's exact theorem and definition. Edition and page choices are recorded in the receipts and bibliography. Newly verified journal metadata includes Oka-1, Jia–Meng 2024 and Winter 2009, with the opened preprint locators preserved.

## Typesetting and complete page reading

The supplied build program uses self-contained pdfLaTeX, standard packages and disabled shell escape. The corrected baseline has 192 pages and zero undefined references/citations, missing fonts/characters or overfull boxes. During revision, stage 1 exposed one 30.56874 pt overflow; stage 2 one 6.48009 pt overflow; stage 3 five blank-line equation errors; and stage 5 one 59.08849 pt program-heading overflow. All were repaired in source. The final build has zero overfull boxes, undefined references, undefined citations, missing fonts, missing characters and duplicate labels.

Candidate 01 had 179 pages. Every rendered page was actually read, in disjoint exhaustive assignments: root 47, analytic 42, topology 42 and provenance 48. Candidate 02 had 177 pages; every changed image was read. Candidate 03 has 177 pages; all 31 newly changed images were read. Earlier readings carry forward only where the entire final PNG, including its page number, is byte-identical to an actually read image. The final coverage record maps all 177 pages to individual reading records and image hashes. Rendering alone supplies no reading evidence.

Final source SHA-256: `{source_sha}`.

Final PDF SHA-256: `{pdf['pdf_sha256']}`.

`S6_SERIES_PUBLISH_reading_V.md` gives the complete final-page table. The original candidate findings, exact repairs, reader records and build summaries remain available. Paper V's final PDF is included in the next scheduled checkpoint; the other PDFs will be included only when their own complete gates are satisfied.

## Remaining work and continuation

Complete I, II, III and IV individually in that order, including all underchecked-result obligations, proof comparisons, provenance, clean builds and complete rendered-page reading. Then regenerate every cross-paper reference from the final labels/tags, synchronize the common series table and notation sheet, check the five-paper dependency and reference consistency, and reread all five introductory parts.

Exact edits, removed duplicate proofs, event ledgers, programs, outputs and primary-source receipts are in the work tree. The base archive plus the newest checkpoint restores the work. Intermediate PDFs, rendered page images, vendor libraries and TeX caches are omitted from checkpoints; the delivered build/render programs regenerate them. Any final PDF is included only with its matching full-reading receipt.

Checkpoint 01 was saved at 23:27 UTC on 20 November (00:27 Berlin on 21 November), SHA-256 `5e62d1f9062ddd625586e0c20c9a2cb72731b0b627865c694200e2d387b9380a`. Checkpoint 02 was saved at 00:12:49 UTC on 21 November (01:12 Berlin), SHA-256 `d900436266456e1d2dbf8ad4a9f2a8b2a0bf5638234797a12a0577858bba557e`. Checkpoint 03 is due at 00:57 UTC (01:57 Berlin), with later checkpoints every 45 minutes. The first mandatory progress review remains 01:42 UTC (02:42 Berlin), then hourly. No mandatory three-hour review has yet occurred.
'''
(ROOT / 'S6_SERIES_PUBLISH_report.md').write_text(report)
print(json.dumps(gate))

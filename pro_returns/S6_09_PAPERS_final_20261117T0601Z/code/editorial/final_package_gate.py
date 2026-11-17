"""Check final delivery consistency against the independent reading records.

This gate is not a mathematical proof verifier. It requires the actual scoped
reading, rerun, source-retention and visual-review records; it does not create
or infer them from the presence of a label or an arbitrary status string.
"""
from pathlib import Path
import collections, csv, hashlib, json, re, sys
D = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(D.parent/'deps/python'))
import bibtexparser

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads((D/p).read_text())
failures = []
checks = []
def check(name, condition, detail=None):
    checks.append({'check': name, 'passed': bool(condition), 'detail': detail})
    if not condition: failures.append(name)

fields = 'source_run source_id source_file paper printed_label kind statement_as_printed wording_vs_source recorded_checks your_check check_outcome found_in_AC26 found_in_E26 found_in_DGKX_v1 found_elsewhere credited_to notes'.split()
with (D/'S6_09_PAPERS_inventory.csv').open(newline='') as f:
    rd = csv.DictReader(f); actual_fields = rd.fieldnames; rows = list(rd)
check('Exactly the required seventeen columns and 1184 rows', actual_fields == fields and len(rows) == 1184)
ids = collections.Counter((r['source_run'], r['source_id']) for r in rows)
check('Every inventory identity occurs once', all(v == 1 for v in ids.values()))
original = load('records/source_results.json')
required = {(run, item['id']) for run, items in original.items() for item in items
            if run != 'S6_05_ARITHMETIC' or item['id'].startswith('C.')}
check('All 745 original in-scope run rows retained exactly once', len(required) == 745 and all(ids[k] == 1 for k in required))
empty = [{'source_run':r['source_run'], 'source_id':r['source_id'], 'fields':[k for k in fields if not r[k].strip()]} for r in rows if any(not r[k].strip() for k in fields)]
check('No empty current inventory field', not empty, empty)
stale = [{'source_run':r['source_run'], 'source_id':r['source_id'], 'field':k} for r in rows for k in ['wording_vs_source','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere','credited_to']
         if re.match(r'\s*(?:pending\b|not yet printed\b|to be checked\b)', r[k], re.I)]
check('No stale current leading credit or printing placeholders', not stale, stale)

texts = {p:(D/f'S6_09_PAPERS_{p}.tex').read_text() for p in ['I','II','III']}
labels = {p:collections.Counter(re.findall(r'\\label\{([^}]+)\}', s)) for p,s in texts.items()}
bad_dest = [(r['source_run'],r['source_id'],r['paper'],r['printed_label']) for r in rows if labels[r['paper']][r['printed_label']] != 1]
check('Each inventory destination occurs exactly once in its assigned paper', not bad_dest, bad_dest)
bad_stmt = [(r['source_run'],r['source_id']) for r in rows if r['statement_as_printed'] not in texts[r['paper']]]
check('Every literal printed statement field occurs in the final paper', not bad_stmt, bad_stmt)
boundary = r'\part{Questions not established by the present arguments}'
open_labels = {'I':['inv:C3.8','ari:open:norm'], 'II':['inv:E2.3'], 'III':['maps:src:D.2.4']}
for p, keys in open_labels.items():
    text = texts[p]
    check(p+' exact unresolved boundaries are in the separate final part', boundary in text and all(text.index(r'\label{'+k+'}') > text.index(boundary) for k in keys))

entries = {e.key:{f.key:f.value for f in e.fields} for e in bibtexparser.parse_file(str(D/'S6_09_PAPERS_references.bib')).entries}
ver = load('records/bibliography_provenance.json')['verification_records']
check('Every bibliography entry has verified or unverified status', len(entries)==492 and all(e.get('verification') in {'verified','unverified'} for e in entries.values()))
check('Each verified bibliography key has an actual scoped source record', all(k in ver for k,e in entries.items() if e.get('verification')=='verified'))
allowed_unverified = {'I':{'CrRubin1991','bertrand1984','pham2025sigma','silverman1983specialization','tate1983variation'}, 'II':set(), 'III':set()}
paper_info = {}
for p, text in texts.items():
    v = load(f'records/{p}_final_validation.json')
    check(p+' final validation explicitly passed', v.get('gate_passed') is True)
    check(p+' validation hashes identify current canonical files', v.get('tex_sha256')==sha(D/f'S6_09_PAPERS_{p}.tex') and v.get('pdf_sha256')==sha(D/f'S6_09_PAPERS_{p}.pdf'))
    log=(D/v['build_log']).read_text(errors='replace')
    boxes=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',log)]
    warnings=re.findall(r'^.*(?:LaTeX Warning:|Package \S+ Warning:|Missing character:).*(?:\n|$)',log,re.M)
    check(p+' final build has no warning, missing glyph, error, or overflow above 2pt', not warnings and all(x<=2 for x in boxes) and 'Output written on ' in log and '! LaTeX Error' not in log)
    refs=load(f'work/root/{p}_citation_gate.json')
    check(p+' resolved references and duplicate-label gate', not refs['missing_bibliography'] and not refs['undefined_labels'] and not refs['duplicate_labels'] and not refs['raw_source_numbers'])
    check(p+' unverified citations are only the five explicitly nonoperative I comparisons', set(refs['unverified_cited'])==allowed_unverified[p])
    uses='\n'.join(re.findall(r'^\\Uses\{.*$',text,re.M))
    operative_bad=[k for k in allowed_unverified[p] if re.search(r'\\cite\w*(?:\[[^\]]*\])*\{[^}]*\b'+re.escape(k)+r'\b',uses)]
    check(p+' no unverified original remains in an operative Uses line', not operative_bad, operative_bad)
    bibkeys=set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',text))
    cites={k.strip() for m in re.finditer(r'\\(?:cite\w*|nocite)(?:\[[^\]]*\])*\{([^}]+)\}',text) for k in m[1].split(',')}
    check(p+' every cited bibliography entry is included inline', cites <= bibkeys)
    check(p+' standalone source and single repository data-statement URL', not re.search(r'\\(?:input|include|includegraphics)\s*(?:\[[^\]]*\])?\{',text) and text.count('https://github.com/KokunoYumeto/s6-complex-structure-workbench')==1)
    check(p+' AI-produced, no human mathematical checking, and CC0 declarations', 'AI-produced' in text and 'No human has checked its mathematics' in text and 'CC0 1.0' in text and not re.search(r'AI[- ]assisted',text,re.I))
    visual=v['visual_review']
    check(p+' final selected-page visual record identifies current PDF', visual.get('pdf_sha256')==v['pdf_sha256'] and not visual.get('visual_defects_found',[]))
    for rel in v['proof_review_evidence']:
        check(p+' required proof-reading evidence: '+rel,(D/rel).is_file())
    paper_info[p]={'rows':sum(r['paper']==p for r in rows),'pages':v['pages'],'tex_sha256':v['tex_sha256'],'pdf_sha256':v['pdf_sha256'],'build_log':v['build_log'],'overfull_boxes':len(boxes),'maximum_excess_pt':max(boxes,default=0),'citations':refs['citations'],'visual_pages_covered':v.get('visual_pages_covered',v.get('selected_visual_pages'))}

ii=load('records/II_final_exact_retention_chain.json')
check('II complete final source linked exactly to fully read baseline', ii['passed'] and ii['canonical_CDP_blocks_retained']==237 and ii['complete_E1_1_proof_retained_byte_identically_once'] and ii['final_tex_sha256']==paper_info['II']['tex_sha256'])
check('II all earlier printed result/equation identities preserved',load('records/II_final_label_identity_check.json')['passed'])
iii_hash=paper_info['III']['tex_sha256']
for path,count in [('work/maps_audit/III_MAPS190_source_to_print_check.json',190),('work/invariants_arithmetic/maps_D_source_to_print_check.json',69)]:
    r=load(path);check('Final complete source retention '+path,r['rows']==count and r['passed']==count and not r['failed_ids'] and r['paper_III_sha256']==iii_hash)
c=load('work/maps_audit/III_course249_final_source_to_print_check.json')
check('III all 33 complete chapters and 249 units retained',c['passed_chapters']==33 and c['passed_units']==249 and not c['failed_chapters'] and not c['failed_units'] and c['paper_III_sha256']==iii_hash)
p=load('work/cdp_audit/push_C_retention/current_final_retention.json')
check('III all 34 complete PUSH blocks and sixteen exact repairs retained',p['III_tex_sha256']==iii_hash and p['all_34_complete_III_blocks_retained'] and p['all_16_documented_replacements_remain_present'])
pg=load('records/III_program_index_validation.json')
check('III program catalogue files, hashes and receiving labels validated',not pg['missing_paths_or_hash_mismatches'] and not pg['missing_receiving_labels'] and pg['verified_distinct_archive_files']==621 and pg['receiving_references_present']==128)
n=load('records/notation_concordance.json')
check('Final common notation covers all 1184 rows and actual destinations',n['inventory_rows']==1184 and not n['unplaced_results'] and not n.get('missing_aux_numbers') and not any(n.get('duplicate_tex_labels',{}).values()))
check('Notation artifact matches its current complete record',n['output_sha256']==sha(D/'S6_09_PAPERS_notation_sheet.md'))
cr=load('work/invariants_arithmetic/final_companion_reference_gate.json')
check('All294 explicit printed companion references and92 destinations have correct actual kinds/numbers',cr['passed'] and cr['explicit_numbered_reference_occurrences']==294 and cr['unique_numbered_destinations']==92 and cr['broken_number_or_type_count']==0 and not cr['failures'] and not cr['range_failures'])
ig=load('work/invariants_arithmetic/final_inventory_completeness_credit_gate.json')
check('Independent complete inventory/credit/current-status gate identifies the exact final inventory',ig['passed'] and ig['inventory_sha256']==sha(D/'S6_09_PAPERS_inventory.csv'))
for p,targets in load('records/common_numbered_companion_overview.json')['targets'].items():
    nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',(D/f'S6_09_PAPERS_{p}.aux').read_text()))
    check(p+' numbered companion overview targets remain exact',all(nums.get(k)==v for k,v in targets.items()))

ret=load('records/checkpoint_retention.json')
known_archives={x['archive'] for x in ret['archives']}
actual_archives={str(p.relative_to(D.parent)) for p in D.parent.glob('S6_09_PAPERS_checkpoint_*.zip')} | {str(p.relative_to(D.parent)) for p in (D.parent/'repacked_checkpoints').glob('S6_09_PAPERS_checkpoint_*.zip')}
check('Every actual hourly checkpoint is included in retention ledger',known_archives==actual_archives and not ret['omitted_checkpoint_members'])
verified={}; bad=[]
for member in ret['members']:
    path=member['retained_path']
    if path not in verified: verified[path]=sha(D/path) if (D/path).is_file() else None
    if verified[path]!=member['sha256']: bad.append({'path':path,'checkpoint':member['checkpoint']})
check('Every checkpoint member retained at its exact recorded hash',not bad, bad)
dedup=load('records/visual_asset_deduplication.json')
planned_pngs={x['path'] for x in dedup['unique_payloads']} | {x['original_path'] for x in dedup['aliases']}
actual_pngs={str(p.relative_to(D)) for p in D.rglob('*.png') if p.is_file()}
check('Lossless image representation covers every actual PNG path',planned_pngs==actual_pngs and dedup['source_png_paths']==len(actual_pngs))
restore=load('work/invariants_arithmetic/archive_restoration_validation/validation_report.json')
check('Independent full duplicate-image restoration and overwrite-refusal checks passed',restore.get('passed') is True)
saved=load('records/checkpoint_06_library.json')['results']
check('Sixth hourly checkpoint lossless retry saved successfully',len(saved)==1 and saved[0]['status']=='succeeded' and saved[0].get('local_metadata_applied') is True)

record={'passed':not failures,'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026','scope':'Final consistency and evidence gate; mathematical checking is supplied by the named independent reading/rerun records, not inferred by this script. Archive CRC and payload-hash verification is performed by the subsequent packager.','inventory_rows':len(rows),'original_run_rows':len(required),'additional_rows':len(rows)-len(required),'columns':fields,'papers':paper_info,'bibliography_entries':len(entries),'bibliography_status_counts':dict(collections.Counter(e['verification'] for e in entries.values())),'checks':checks,'failed_checks':failures,'checkpoint_archives':sorted(known_archives),'checkpoint_member_occurrences':len(ret['members']),'unsupported_requested_equivalence':'Official OpenAI documentation does not support equating Pro mode with one universal maximum reasoning-effort value; the exact provenance is retained and the unsupported equivalence is not asserted.','remaining_mathematical_boundaries':open_labels}
(D/'records/final_package_gate.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':not failures,'checks':len(checks),'failures':failures,'papers':paper_info},ensure_ascii=False))
sys.exit(0 if not failures else 1)

#!/usr/bin/env python3
"""Prepare guarded Paper I provenance/deposit replacements from exact inputs.

This program mutates only the agent's output directory. It independently
recounts the canonical ledger through the sibling read-only recount program.
The --coverage option closes PDF-related claims only on a source/PDF-bound,
certified exhaustive coverage receipt produced by the actual page readers.
"""
from pathlib import Path
import argparse, copy, csv, datetime, hashlib, importlib.util, json, re
from S6_SERIES_PUBLISH_I_cont_recount import recount, KINDS

csv.field_size_limit(100_000_000)
RECORDS_URL = ('https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/'
               '1fb9194767aef92abcc06071e3820c2f226b9512/'
               'pro_returns/S6_SERIES_PUBLISH_checkpoint_10_20261121T0612Z/')
HISTORY_URL = ('https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/'
               '83d76022bcd442278b760db9ff438afceed6c6ea')
Q=chr(96)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def bind(path,root=None):
    path=path.resolve()
    return {'path':str(path.relative_to(root)) if root and path.is_relative_to(root) else str(path),
            'sha256':sha(path),'bytes':path.stat().st_size}

def put(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def sections(text):
    starts=list(re.finditer(r'^## Paper ([IV]+)\s*$',text,re.M))
    return text[:starts[0].start()] if starts else text, {
        m[1]:text[m.start():starts[i+1].start() if i+1<len(starts) else len(text)]
        for i,m in enumerate(starts)}

def save_tsv(path,rows,fields):
    with path.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t')
        writer.writeheader();writer.writerows(rows)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--base',type=Path)
    parser.add_argument('--source-sha',required=True)
    parser.add_argument('--ledger-sha',required=True)
    parser.add_argument('--pdf',type=Path)
    parser.add_argument('--coverage',type=Path)
    parser.add_argument('--build-summary',type=Path)
    parser.add_argument('--out',type=Path)
    parser.add_argument('--evidence-dir',type=Path,
                        help='Directory containing the immutable pin/primary receipts; defaults to this script directory.')
    parser.add_argument('--hold-guard',action='store_true',
                        help='Prepare source/count/deposit state only; emit no shared-file apply guard.')
    parser.add_argument('--context-binding',type=Path,action='append',default=[],
                        help='Additional completed source/context rebinding receipt to hash; repeat as needed.')
    parser.add_argument('--reread-append-receipt',type=Path,
                        help='Root-approved append receipt, required after the preserved 7,866-row ledger changes.')
    args=parser.parse_args()
    root=args.root.resolve();base=(args.base or root.parent/'S6_SERIES_PUBLISH_work').resolve()
    out=(args.out or root/'agents/i_cont_provenance').resolve();out.mkdir(parents=True,exist_ok=True)
    evidence_dir=(args.evidence_dir or Path(__file__).resolve().parent).resolve()
    assert args.hold_guard or args.coverage is not None, 'Final shared-file guard requires certified coverage; use --hold-guard for a source/count preview.'
    source=root/'S6_SERIES_PUBLISH_I.tex';ledger=root/'CHECK_EVENTS.tsv'
    assert sha(source)==args.source_sha, 'Source freeze changed'
    assert sha(ledger)==args.ledger_sha, 'Ledger freeze changed'
    append_binding=None;append_verification=None
    baseline_ledger_sha='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
    if args.ledger_sha!=baseline_ledger_sha:
        assert args.reread_append_receipt, 'Changed ledger requires the exact root-approved rereading append receipt.'
    if args.reread_append_receipt:
        verifier_path=root/'code/S6_SERIES_PUBLISH_I_verify_reread_append.py'
        spec=importlib.util.spec_from_file_location('verified_reread_append',verifier_path)
        verifier=importlib.util.module_from_spec(spec);spec.loader.exec_module(verifier)
        append_verification=verifier.verify_append(args.reread_append_receipt.resolve(),ledger)
        append_binding=bind(args.reread_append_receipt.resolve(),root)
    text=source.read_text()
    assert '\\newcommand{\\SsixPublishRecords}{'+RECORDS_URL+'}' in text
    method=re.search(r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}',text,re.S)[1]
    assert method.count(r'\href{\SsixPublishRecords}')==1
    assert 'accompany its source distribution' not in method
    assert 'continuation on 21 November' in method

    rec=recount(root,base)
    recount_path=out/'S6_SERIES_PUBLISH_I_cont_recount.json';put(recount_path,rec)
    counts=rec['counts'];numbers=[counts[k] for k in KINDS]
    if append_verification:
        assert set(append_verification['appended_event_ids'])<=set(rec['selected_event_ids'])
        assert numbers==[767,10,143,731+append_verification['appended_events'],194,1]
        assert counts['event_associations']==1846+append_verification['appended_events']
    phrases=['examinations of proof steps','independent',
             'computations or formal certificates','readings of the proofs and applications',
             'uses of background results without a fault found','refutation']
    for number,phrase in zip(numbers,phrases):
        assert re.search(str(number)+r'\s+'+re.escape(phrase),method),(number,phrase)
    abstract_tex=re.search(r'\\begin\{abstract\}\s*(.*?)\s*\\end\{abstract\}',text,re.S)[1]
    abstract=' '.join(abstract_tex.split()).replace('Bott--Chern','Bott–Chern')
    assert len(abstract.split())<=250

    inherited_path=root/'agents/i_provenance/S6_SERIES_PUBLISH_I_three_way_claim_table_final.json'
    inherited=json.loads(inherited_path.read_text())
    claims=copy.deepcopy(inherited['claims'])
    assert [x['id'] for x in claims]==['I-P'+str(i).zfill(2) for i in range(1,43)]
    status_binding=copy.deepcopy(inherited['exact_main_status_binding'])
    for section in status_binding.values():
        for row in section.values():
            row['source_occurrences']=text.count(row['text'])
            assert row['source_occurrences']==1,row['text']
    completion_path=root/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
    completion=json.loads(completion_path.read_text())
    assert all(v['status']=='done' for v in completion['rows'].values() if v.get('paper')=='I')

    pin_path=evidence_dir/'S6_SERIES_PUBLISH_I_cont_pin_open.json'
    pin=json.loads(pin_path.read_text())
    assert {x['name'] for x in pin if x.get('status')==200}=={'pin_tree','pin_api','pin_report'}
    assert next(x for x in pin if x['name']=='pin_api')['commit']=='1fb9194767aef92abcc06071e3820c2f226b9512'
    pinned_report=evidence_dir/'S6_SERIES_PUBLISH_I_cont_pin_report.md'
    restored_report=base/'S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_report.md'
    assert sha(pinned_report)==sha(restored_report)

    pdf_info=None;coverage_info=None;build_info=None;certified=False
    if args.pdf:
        pdf=args.pdf.resolve();pdf_info=bind(pdf,root)
    if args.build_summary:
        build_path=args.build_summary.resolve()
        bs=json.loads(build_path.read_text())
        assert bs['source_sha256']==args.source_sha
        if pdf_info:assert bs['pdf_sha256']==pdf_info['sha256']
        build_info=bind(build_path,root)
    if args.coverage:
        assert pdf_info is not None, '--coverage requires --pdf'
        coverpath=args.coverage.resolve();cover=json.loads(coverpath.read_text())
        assert cover['paper']=='I'
        assert cover['source_sha256']==args.source_sha
        assert cover['pdf_sha256']==pdf_info['sha256']
        assert cover['all_pages_read'] and cover['certified'] and not cover['missing_pages']
        assert cover['covered_pages']==cover['page_count']==len(cover['pages'])
        coverage_info=bind(coverpath,root)
        pdf_info['pages']=cover['page_count'];certified=True
    final_gate=('All '+str(pdf_info['pages'])+' final rendered pages have source/PDF-bound certified reading coverage.'
                if certified else 'Current source and counts are bound; final rendered-page coverage remains open.')
    count_sentence=(str(counts['statements'])+' printed environments retain '
                    +str(counts['subject_identifiers'])+' statement identifiers. The selected record contains '
                    +format(counts['event_associations'],',')+' associations in '
                    +format(counts['declared_evidence_groups'],',')+' declared evidence groups. '
                    +'Outline-step associations are counted separately: '
                    +str(counts['outline_step_associations_separate'])+'.')

    old_deposit_path=root/'agents/i_provenance/S6_SERIES_PUBLISH_I_deposit_fields.json'
    deposit=copy.deepcopy(json.loads(old_deposit_path.read_text()))
    deposit['abstract']=abstract
    production=' '.join(method.split('For the statements printed in this paper,')[0].split()).replace('--','–')
    production=production.removeprefix('This text is AI-produced; no part of it was written by a human. ').strip()
    deposit['comments']=(
        'Paper I of the five-paper series “The (3,4,∞) family of complex six-spheres”. '
        'This paper determines the marked periods, parameter equivalences, cohomology and deformation data, '
        'puncture obstruction, outer boundary and arithmetic norm identities of the displayed family. '
        'It studies the constructions of Claude and L. Alpöge (https://alpo.ge/s6.pdf), '
        'Engel (https://arxiv.org/abs/2609.38442), and Viaclovsky (https://arxiv.org/abs/2610.39102), '
        'with the standard classification and deformation results of Du, Guo, Kusakabe and Xie credited '
        'to version 1 (https://arxiv.org/abs/2610.00250v1). '
        'Historical series sources, programs and check records are at '+HISTORY_URL+'. '
        'The publication records are at '+RECORDS_URL+'.')
    check_text=(
        'For the statement scopes printed in this paper, the merged record contains '
        +str(numbers[0])+' examinations of proof steps, '+str(numbers[1])+' independent re-derivations, and '
        +str(numbers[2])+' computations or formal certificates. It records '+str(numbers[3])
        +' further readings of proofs and applications, '+str(numbers[4])
        +' uses of background results without a fault found, and '+str(numbers[5])
        +' refutation associated with its corrected statement. '
        'Each total counts recorded links from a check to a statement; one calculation used for several '
        'statements can contribute several links. Each association retains its original identity, '
        'declared evidence group and outcome scope. Derivations made before reading the target proof, '
        'comparisons after exposure and readings of edited proofs retain those recorded descriptions. '
        'The continuation records assign no proof-check credit to metadata scans, bibliography '
        'authentication, literature searches or page-image inspection alone. '+count_sentence)
    if append_verification:
        check_text+=' The continuation accounts for '+str(append_verification['appended_events'])+' of these comparative readings, grouped once per owning printed statement across reviewers and editorial rounds. Each is supported by an actual complete exposed-proof reading and manual comparison of its original and revised statement-and-proof context. These entries supply no independent re-derivation, targeted derivation, computation or formal certificate.'
    if certified:
        check_text+=' All '+str(pdf_info['pages'])+' rendered pages of the final PDF were read.'
    deposit['provenance']=(
        'Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.\n\n'
        'How it was produced. '+production+'\n\n'
        'How it was checked. '+check_text+'\n\n'
        'Human understanding. No human has checked the mathematics. The submitter directed the research '
        'and takes responsibility for the submitted text.\n\n'
        'Records. The historical source editions, programs, outputs and check records are available at '
        +HISTORY_URL+'. The publication records are at '+RECORDS_URL+
        '. The text, programs and check records are dedicated to the public domain under CC0 1.0 Universal '
        '(https://creativecommons.org/publicdomain/zero/1.0/).')
    deposit['aiSystems'][0]['model']='GPT-6 Astra (ChatGPT Pro mode)'
    # Preserve the unsubmitted confirmation state and Paper I-specific classifications.
    for key in ['correctnessConfirmed','communityInterestConfirmed','citationsConfirmed','rightsConfirmed']:
        deposit[key]=None
    assert 'accompany' not in deposit['provenance']+deposit['comments']
    assert deposit['provenance'].startswith('Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.')
    public_v_form=base/'HEXAGON_METADATA_V_public_v2.json'
    vform=json.loads(public_v_form.read_text())
    assert all(deposit[k]==vform[k] for k in ['authorshipMode','humanUnderstanding','license'])
    deposit_path=out/'S6_SERIES_PUBLISH_I_cont_deposit_fields.json';put(deposit_path,deposit)

    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    base_comparison=('The current exemplar is HEXAGON_METADATA_V_public_v2.json. Its field structure and '
                     'shared historical model/effort/date facts were read. The 20 November Opus abstract/Section 1 '
                     'rewrite remains attributed in Paper V. Paper I theorem scopes, review counts and final-PDF '
                     'claims are bound to the Paper I source and records.')
    claim_updates={
        'I-P01':('Paper I title and series identity.', 'The exact title and Paper I identity agree with the current source and deposit. The final five-paper table synchronization remains a series-wide task.'),
        'I-P02':('Abstract states the current Paper I theorem scopes.', 'The current Paper I abstract is copied with the explicit line-wrap and typographic-dash rendering map. All 21 main mechanism/status/table strings occur exactly once in the current source.'),
        'I-P33':(None,'The source and deposit retain the documented Sol/ultra contribution, the pinned README account of Astra/ultra from 5 September, and the November model/effort/date facts. The attached historical qualification record retains its bounded unassigned Luna/Terra scope without adding statement credits.'),
        'I-P34':('Publication revision on 20–21 November 2026, including continuation on 21 November.', 'The production account is copied directly from current §1.5, including the specified ChatGPT Pro mode and dates. The continuation prompt supplies the present date and model facts.'),
        'I-P35':('Counts of recorded check-to-statement associations and their declared evidence groups.', 'An independent parser selects each canonical ledger row once from the current printed identities and retained aliases. '+count_sentence+' Types: '+', '.join(str(n) for n in numbers)+'.'),
        'I-P36':(None,'Every Paper I row in the scoped required-check completion manifest is done. The current count computation derives the printed identities afresh. The existing mathematical derivations and comparison evidence keep their own scopes.'),
        'I-P38':('Historical and publication record links resolve at their specified immutable commits.', 'The new checkpoint10 folder, commit API and raw report opened with HTTP 200. The API returns the exact instructed commit, and the raw report is byte-identical to the attached checkpoint10 report. The older program pin retains its inherited verification receipts.'),
        'I-P39':(None,'The 78 program-table source links retain their authenticated historical paths and recorded receiving-result scopes. The single methodology records link now uses SsixPublishRecords at the instructed publication checkpoint10. Fresh continuation records are retained with this continuation; their eventual deposit pin is the prompt’s stated deposit-time update.'),
        'I-P40':(None,'The inherited A–G source-status searches and exact primary locators remain recorded. The continuation adds two bounded primary-domain status queries and opens current official Engel/DGKX metadata; results are recorded without an exhaustive-absence or priority claim.'),
        'I-P41':(None,'The current source and deposit give the same CC0 1.0 dedication and the sentence that no human has checked the mathematics.'),
        'I-P42':('Paper I source, ledger, deposit and final-PDF coverage binding.', 'The actual current abstract, all 42 claim dispositions, recomputed counts and the declared final-PDF state are bound to the exact current inputs. '+final_gate)
    }
    for row in claims:
        if row['id'] in claim_updates:
            claim,disposition=claim_updates[row['id']]
            if claim:row['current_claim_or_issue']=claim
            row['disposition']=disposition
        row['old_HEXAGON_METADATA_V_comparison']=base_comparison
        row['count_comparison']=(
            'Recomputed directly from current TeX, historical tags and canonical CHECK_EVENTS by S6_SERIES_PUBLISH_I_cont_recount.py. '
            +count_sentence if row['id']=='I-P35'
            else 'No check-count assertion is derived for this claim; its mathematical and documentary evidence retains the inherited stated scope.')
        row['remaining_gate']='' if certified else 'Final source/PDF-bound certified rendered-page coverage.'
        row['status']='resolved at exact current source/count/PDF snapshot' if certified else 'source/count bound; final PDF coverage pending'
        row['continuation_review']='All inherited claim dispositions read on 21 November 2026; exact current source/status/count/deposit comparisons and primary-link receipts recorded. This provenance-binding operation creates no check event.'
        row['deposit_location']='Paper I title/abstract/comments/provenance according to claim scope'
    byid={r['id']:r for r in claims}
    byid['I-P38']['primary_or_check_evidence']+='; agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_pin_open.json'
    byid['I-P40']['primary_or_check_evidence']+='; agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_primary_web.json; agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_literature_search_scope.json'
    byid['I-P35']['primary_or_check_evidence']='Canonical CHECK_EVENTS.tsv and the current printed-identity selection in agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_recount.json.'
    byid['I-P35']['primary_or_check_evidence']='Canonical CHECK_EVENTS.tsv and the current printed-identity selection in '+str(recount_path.relative_to(root))+'.'
    if append_verification:
        byid['I-P35']['primary_or_check_evidence']+=' Exact approved continuation rereading append: '+json.dumps(append_binding,ensure_ascii=False)+'.'
        byid['I-P35']['disposition']+=' The approved append preserves the original 7,866 rows byte for byte and adds '+str(append_verification['appended_events'])+' actual used-and-rechecked owner associations; other check categories are unchanged.'
    byid['I-P42']['primary_or_check_evidence']=str(coverage_info) if coverage_info else 'Final current-PDF coverage pending; inherited rendered-page readings remain bound to their own exact source/PDF hashes.'
    context_bindings=[bind(p.resolve(),root) for p in args.context_binding]
    if context_bindings:
        byid['I-P42']['primary_or_check_evidence']+=' Source/context rebinding receipts: '+json.dumps(context_bindings,ensure_ascii=False)

    statement=('Source SHA-256: '+Q+args.source_sha+Q+'. CHECK_EVENTS SHA-256: '+Q+args.ledger_sha+Q+'. '+final_gate)
    if pdf_info:statement+=' Current PDF SHA-256: '+Q+pdf_info['sha256']+Q+'.'
    section='\n'.join([
        '## Paper I','','### Title','',deposit['title'],'','### Abstract','',deposit['abstract'],
        '','### Comments','',deposit['comments'],'','### Provenance','',deposit['provenance'],
        '','### Subjects and classification','','Primary: '+deposit['subject']+'. Cross-lists: '+', '.join(deposit['crossListSubjects'])+'.',
        '','MSC2020: '+', '.join(deposit['mscCodes'])+'.',
        '','Tags: '+', '.join(deposit['tags'])+'.',
        '','Authorship mode: no human author claimed. Human understanding: none. Licence: CC0 1.0 Universal. Submission confirmations remain unset.',
        '','### Source and review binding','',statement,''])
    section_path=out/'S6_SERIES_PUBLISH_I_cont_deposit_fields.md';section_path.write_text(section)
    current_deposit=root/'S6_SERIES_PUBLISH_deposit_fields.md'
    old_text=current_deposit.read_text();head,parts=sections(old_text)
    assert 'I' in parts
    new_text=old_text.replace(parts['I'],section,1)
    new_head,new_parts=sections(new_text)
    assert head==new_head
    assert {k:v for k,v in parts.items() if k!='I'}=={k:v for k,v in new_parts.items() if k!='I'}
    proposal_md=out/'S6_SERIES_PUBLISH_deposit_fields_with_I_cont_proposed.md';proposal_md.write_text(new_text)

    table={'paper':'I','recorded_utc':now,'source':bind(source,root),'ledger':bind(ledger,root),
           'source_sha256':args.source_sha,'ledger_sha256':args.ledger_sha,
           'inherited_claim_table':bind(inherited_path,root),'claims':claims,
           'exact_main_status_binding':status_binding,'counts':counts,'counts_recomputed':True,
           'recount':bind(recount_path,root),'public_V_form':bind(public_v_form),
           'pin_open_receipt':bind(pin_path,root),'pinned_report_matches_attached':True,
           'final_pdf':pdf_info,'final_coverage':coverage_info,'build_summary':build_info,
           'all_claims_closed':certified,'final_gate':final_gate,'mathematical_events_added':0,
           'source_context_rebindings':context_bindings,'shared_guard_held':args.hold_guard,
           'reread_append_receipt':append_binding,'reread_append_verification':append_verification,
           'proof_reread_events_previously_appended':append_verification['appended_events'] if append_verification else 0}
    table_path=out/'S6_SERIES_PUBLISH_I_cont_three_way_claims.json';put(table_path,table)
    md=['# Paper I: continuation provenance review','',statement,'',
        '| Claim | Current disposition | State |','|---|---|---|']
    for row in claims:
        vals=[row['id'],row['disposition'],row['status']]
        md.append('| '+' | '.join(v.replace('|',r'\|').replace('\n',' ') for v in vals)+' |')
    (out/'S6_SERIES_PUBLISH_I_cont_three_way_claims.md').write_text('\n'.join(md)+'\n')
    current_tsv=root/'S6_SERIES_PUBLISH_provenance_checks.tsv'
    with current_tsv.open(newline='') as stream:
        reader=csv.DictReader(stream,delimiter='\t');fields=reader.fieldnames;old_rows=list(reader)
    historical_i={r['claim_id']:r for r in old_rows if r['paper']=='I'}
    rows=[]
    for row in claims:
        old=copy.deepcopy(historical_i[row['id']])
        old.update(locations=row['current_location'],claim=row['current_claim_or_issue'],
                   against_records=row['attached_record_comparison'],by_recomputation=row['count_comparison'],
                   against_primary_source=row['primary_or_check_evidence'],
                   required_action=row['remaining_gate'],
                   evidence=json.dumps({'source_sha256':args.source_sha,'ledger_sha256':args.ledger_sha,
                                        'continuation_claim_table':str(table_path.relative_to(root)),
                                        'recount':str(recount_path.relative_to(root)),
                                        'final_coverage':coverage_info},ensure_ascii=False),
                   current_paper_location=row['current_location'],
                   current_deposit_location=row['deposit_location'],resolution_status=row['status'],
                   remaining_gate=row['remaining_gate'],old_HEXAGON_disposition=base_comparison,
                   current_resolution=row['disposition'])
        rows.append(old)
    proposal_tsv=out/'S6_SERIES_PUBLISH_provenance_checks_with_I_cont_proposed.tsv'
    save_tsv(out/'S6_SERIES_PUBLISH_I_cont_provenance_checks.tsv',rows,fields)
    replacements={r['claim_id']:r for r in rows}
    all_rows=[replacements[r['claim_id']] if r['paper']=='I' else r for r in old_rows]
    assert [r for r in all_rows if r['paper']!='I']==[r for r in old_rows if r['paper']!='I']
    save_tsv(proposal_tsv,all_rows,fields)
    guard={'created_utc':now,'paper':'I','source_sha256':args.source_sha,'ledger_sha256':args.ledger_sha,
           'math_events_added':0,'scope':'Paper I rows and deposit section only. '+final_gate,
           'updates':[{'target':str(current_tsv),'expected_sha256':sha(current_tsv),'replacement':bind(proposal_tsv)},
                      {'target':str(current_deposit),'expected_sha256':sha(current_deposit),'replacement':bind(proposal_md)}]}
    guard_path=out/'S6_SERIES_PUBLISH_I_cont_shared_guard.json'
    if not args.hold_guard:
        assert certified, 'Shared-file apply guard requires certified current coverage'
        put(guard_path,guard)
    receipt={'created_utc':now,'paper':'I','source':bind(source,root),'ledger':bind(ledger,root),
             'claim_count':len(claims),'all_claims_closed':certified,'counts':counts,
             'independent_recount':bind(recount_path,root),'claim_table':bind(table_path,root),
             'deposit_json':bind(deposit_path,root),'deposit_section':bind(section_path,root),
             'shared_guard':None if args.hold_guard else bind(guard_path,root),
             'shared_guard_generated':not args.hold_guard,'source_context_rebindings':context_bindings,
             'final_pdf':pdf_info,'final_coverage':coverage_info,
             'build_summary':build_info,'inherited_required_check_completion':bind(completion_path,root),
             'source_status_strings_verified':21,'public_V_form':bind(public_v_form),
             'pin_open_receipt':bind(pin_path,root),'pinned_report_matches_attached':True,
             'reread_append_receipt':append_binding,'reread_append_verification':append_verification,
             'proof_reread_events_previously_appended':append_verification['appended_events'] if append_verification else 0,
             'final_gate':final_gate,'external_submission_performed':False,'mathematical_events_added':0}
    put(out/'S6_SERIES_PUBLISH_I_cont_provenance_binding.json',receipt)
    assert sha(source)==args.source_sha and sha(ledger)==args.ledger_sha
    print(json.dumps({'claims':42,'all_claims_closed':certified,'source_sha256':args.source_sha,
                      'ledger_sha256':args.ledger_sha,'counts':counts,
                      'guard':None if args.hold_guard else str(guard_path),'scope':final_gate},indent=2))

if __name__=='__main__':main()

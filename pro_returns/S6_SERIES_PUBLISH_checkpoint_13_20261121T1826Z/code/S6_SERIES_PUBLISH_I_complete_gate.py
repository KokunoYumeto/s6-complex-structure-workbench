#!/usr/bin/env python3
"""Close the reviewed Paper I snapshot after all independently scoped gates.

This aggregates existing evidence. It performs no new mathematical check and
adds no event or reading credit. The --apply flag records the root's review
decision; the source and mathematical ledger remain byte-identical.
"""
from pathlib import Path
import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10'
csv.field_size_limit(100_000_000)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def tab(path, delimiter='\t'):
    with path.open(newline='') as stream:
        reader=csv.DictReader(stream,delimiter=delimiter)
        return reader.fieldnames,list(reader)


def bound(path):
    return {'path':str(path.relative_to(ROOT)), 'sha256':sha(path)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dossier',type=Path,required=True)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    args.dossier=args.dossier.resolve()
    source=ROOT/'S6_SERIES_PUBLISH_I.tex'; pdf=ROOT/'S6_SERIES_PUBLISH_I.pdf'
    ledger=ROOT/'CHECK_EVENTS.tsv'; defects=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv'
    source_sha, pdf_sha, ledger_sha=sha(source),sha(pdf),sha(ledger)
    final_path=ROOT/'records/S6_SERIES_PUBLISH_I_final_pdf_receipt.json'
    final=read(final_path)
    cover_path=ROOT/'records/S6_SERIES_PUBLISH_I_page_coverage.json'; cover=read(cover_path)
    page_total=cover['page_count']
    for value in [final,cover]:
        assert value['source_sha256']==source_sha and value['pdf_sha256']==pdf_sha
        assert value['certified'] and value['all_pages_read'] and not value['missing_pages']
        assert value['page_count']==value['covered_pages']==page_total
    assert len(cover['pages'])==page_total and {x['page'] for x in cover['pages']}==set(range(1,page_total+1))
    for row in cover['pages']:
        assert sha(ROOT/row['reading_record'])==row['reading_record_sha256']
    build_path=ROOT/final['build_summary']; build=read(build_path)
    assert build['source_sha256']==source_sha and build['pdf_sha256']==pdf_sha
    clean_keys=['overfull_above_2pt','undefined_references','undefined_citations','missing_characters',
                'missing_fonts','multiply_defined','duplicate_destinations']
    assert all(build.get(k,0)==0 for k in clean_keys)
    metadata_path=ROOT/'records/S6_SERIES_PUBLISH_I_current_metadata.json'; metadata=read(metadata_path)
    assert metadata['certified_flag'] and metadata['source_sha256']==source_sha and metadata['pdf_sha256']==pdf_sha
    assert metadata['printed_environments']==333 and metadata['statement_identifiers']==353
    ag_path=ROOT/'records/S6_SERIES_PUBLISH_I_continuation_AG_binding.json'; ag=read(ag_path)
    assert (ag['source_sha256'],ag['pdf_sha256'],ag['ledger_sha256'])==(source_sha,pdf_sha,ledger_sha)
    assert ag['source_exact_forward_and_inverse_maps_verified'] and ag['all_label_and_tag_sequences_preserved']
    assert len(ag['headlines'])==7 and sum(x['outline_items'] for x in ag['headlines'].values())==40
    assert len(ag['blocks'])==80
    provenance_path=ROOT/'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_three_way_claims.json'
    provenance=read(provenance_path)
    assert provenance['all_claims_closed'] and len(provenance['claims'])==42
    assert (provenance['source_sha256'],provenance['ledger_sha256'])==(source_sha,ledger_sha)
    assert provenance['final_pdf']['sha256']==pdf_sha
    _, claims=tab(ROOT/'S6_SERIES_PUBLISH_provenance_checks.tsv')
    i_claims=[x for x in claims if x['paper']=='I']
    assert len(i_claims)==42 and all(not x['remaining_gate'] and not x['required_action'] for x in i_claims)
    for row in i_claims:
        evidence=json.loads(row['evidence'])
        assert evidence['source_sha256']==source_sha and evidence['ledger_sha256']==ledger_sha
        assert row['resolution_status']=='resolved at exact current source/count/PDF snapshot'
    completion_path=ROOT/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
    completion=read(completion_path)
    required=[dict(id=k,**v) for k,v in completion['rows'].items() if v.get('paper')=='I']
    assert required and all(x['status']=='done' for x in required)
    _, inventory=tab(ROOT/'S6_SERIES_PUBLISH_inventory.csv',',')
    inventory_i=[x for x in inventory if x['paper']=='I']
    assert all(x['current_source_sha256']==source_sha and x['current_pdf_sha256']==pdf_sha for x in inventory_i)
    assert sum('I-cont-search-' in x['literature_searches'] for x in inventory_i)==7
    mapping_path=ROOT/'records/S6_SERIES_PUBLISH_I_defect_page_mapping.json'; mapping=read(mapping_path)
    assert mapping['current_source_sha256']==source_sha and mapping['current_pdf_sha256']==pdf_sha
    assert not mapping['unresolved_current_context_ids']
    fields, edits=tab(defects)
    edit_count=len(edits)
    continuation_edits=len(ag['exact_edits'])
    assert edit_count==mapping['rows']
    assert sha(defects)==mapping['mapped_defects_sha256']
    detail={x['change_id']:x for x in mapping['details']}
    for edit in edits:
        row=detail[edit['change_id']]
        assert hashlib.sha256(edit['old_text'].encode()).hexdigest()==row['old_text_sha256']
        assert hashlib.sha256(edit['new_text'].encode()).hexdigest()==row['new_text_sha256']
        assert edit['old_page'] and edit['new_page'] and edit['mapped_old_location'] and edit['mapped_new_location']
    dossier=read(args.dossier)
    assert dossier['source_sha256']==source_sha and dossier['all_types_source_clear']
    assert {x['type_id'] for x in dossier['rows']}=={f'D{i:02}' for i in range(1,26)}
    original=(BASE/source.name).read_text(); current=source.read_text()
    identities={}
    for name,pattern in [('labels',r'\\label\{([^}]+)\}'),('permanent_tag_targets',r'\\hypertarget\{tag-([^}]+)\}')]:
        before,after=re.findall(pattern,original),re.findall(pattern,current)
        assert before==after
        identities[name]={'checkpoint10':len(before),'current':len(after),'sequence_identical':True,'lost':[]}
    _, events=tab(ledger)
    assert len(events)==7866
    now=dt.datetime.now(dt.timezone.utc).isoformat()
    record={'paper':'I','completed_utc':now,'source_sha256':source_sha,'pdf_sha256':pdf_sha,
            'ledger_sha256':ledger_sha,'pages':page_total,'logged_edits':edit_count,
            'exact_continuation_edits':continuation_edits,
            'defect_types_closed':[f'D{i:02}' for i in range(1,26)],
            'provenance_claims_closed':42,'current_main_dependency_block_associations':80,
            'main_theorems':7,'outline_claims':40,'pending_required_checks':[],
            'required_completion_rows':len(required),'identities':identities,'counts':provenance['counts'],
            'build_findings':{k:build.get(k,0) for k in clean_keys},
            'reading_methods':dict(collections.Counter(x['method'] for x in cover['pages'])),
            'evidence':[bound(p) for p in [final_path,cover_path,build_path,metadata_path,ag_path,
                         provenance_path,completion_path,mapping_path,args.dossier]],
            'mathematical_events_added_by_completion':0,
            'remaining_series_gate':'Regenerate cross-paper references, synchronize the series table and notation, and repeat the final first-part reading after Papers II–IV are complete. Paper V follows its published v2 source.',
            'scope':'Individual publication gate for this exact source/PDF snapshot. Existing checks retain their recorded methods and independence scopes. No new mathematical event or human checking is claimed.'}
    destination=ROOT/'records/S6_SERIES_PUBLISH_I_complete_gate.json'
    if args.apply:
        assert not destination.exists(),'Preserve any previous completed snapshot'
        old_log_sha=sha(defects)
        old_statuses=sorted({row['review_status'] for row in edits})
        final_status='complete; exact edit and scoped before/current loci retained; final source/PDF gate certified'
        for row in edits:
            row['review_status']=final_status
        with defects.open('w',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t')
            writer.writeheader(); writer.writerows(edits)
        mapping['certified']=True
        mapping['final_defect_log_sha256']=sha(defects)
        mapping['final_coverage']=bound(cover_path)
        mapping_path.write_text(json.dumps(mapping,indent=2)+'\n')
        status_receipt={'recorded_utc':now,'input_defect_log_sha256':old_log_sha,
                        'output_defect_log_sha256':sha(defects),'rows':len(edits),
                        'old_review_statuses':old_statuses,'new_review_status':final_status,
                        'changed_fields':['review_status'],'mathematical_events_added':0}
        (ROOT/'records/S6_SERIES_PUBLISH_I_final_defect_status_binding.json').write_text(json.dumps(status_receipt,indent=2)+'\n')
        record['evidence']=[bound(p) for p in [final_path,cover_path,build_path,metadata_path,ag_path,
                            provenance_path,completion_path,mapping_path,args.dossier]]
        record['defect_log_sha256']=sha(defects)
        destination.write_text(json.dumps(record,indent=2)+'\n')
        type_record={'paper':'I','recorded_utc':now,'source_sha256':source_sha,'pdf_sha256':pdf_sha,
                     'ledger_sha256':ledger_sha,'defect_log_sha256':sha(defects),
                     'dossier':bound(args.dossier),'completion_gate':bound(destination),
                     'rows':[dict(row,status='done',remaining_dependencies=[]) for row in dossier['rows']]}
        (ROOT/'records/S6_SERIES_PUBLISH_I_defect_types_closed.json').write_text(json.dumps(type_record,indent=2)+'\n')
        progress=ROOT/'PROGRESS_LEDGER.md'; text=progress.read_text()
        text,n=re.subn(r'^(\| I \| D\d+: .*? \|) [^|]* \|$',r'\1 done; exact current source audit, logged edits and certified page evidence |',text,flags=re.M)
        assert n==25
        text=text.replace('| I | open |',f'| I | done; all {page_total} final page images have complete reading evidence |',1)
        old='Five publication-ready papers. Current gate: Paper V is complete at its recorded source/PDF snapshot. Complete Paper I, then II, III and IV, followed by the series consistency review.'
        assert old in text
        text=text.replace(old,'Five publication-ready papers. Papers I and V have completed individual gates at their recorded snapshots. Complete Paper II, then III and IV, followed by the five-paper consistency review.',1)
        entry=f'\n## Paper I complete — {now}\n\nPaper I has a clean, completely read {page_total}-page final PDF. All 25 defect types, {edit_count} logged edits, all required scoped checks and all 42 provenance claims are closed at source `{source_sha}`, PDF `{pdf_sha}` and mathematical ledger `{ledger_sha}`. The exact {continuation_edits} continuation edits preserve the mathematical claims through their recorded literal text maps and retain the full label/tag sequences; the existing 7 main theorems and 40 outline claims retain their verified comparison scopes. No mathematical event was added by this continuation’s wording, citation, page-reading or metadata operations. Completion receipt: `records/S6_SERIES_PUBLISH_I_complete_gate.json`. The current gate is Paper II.\n\n### Paper I final page rows\n\nThe source and PDF hashes above apply to every row. The complete per-page image and reading-record hashes are in `records/S6_SERIES_PUBLISH_I_page_coverage.json`.\n\n| Paper | Page | Status | Evidence |\n|---|---:|---|---|\n'
        for row in cover['pages']:
            entry+=f"| I | {row['page']} | done | {row['method']} |\n"
        progress.write_text(text+entry)
        report_path=ROOT/'S6_SERIES_PUBLISH_report.md'; report=report_path.read_text()
        gate=f'Paper I now has a clean, completely read {page_total}-page PDF with 25 closed defect types, {edit_count} logged edits, all required scoped checks and 42 closed provenance claims. Paper V retains its earlier completed individual gate; its published v2 source governs the later series pass. Work proceeds to Paper II, then III and IV, followed by the five-paper review. The full task remains incomplete.'
        report,n=re.subn(r'(## Current gate\n\n).*?(?=\n## )',lambda m:m[1]+gate+'\n',report,count=1,flags=re.S)
        assert n==1 and report.startswith('INCOMPLETE\n')
        summary=f'\n## Paper I completion — {now}\n\n{gate}\n\nSource SHA-256: `{source_sha}`. PDF SHA-256: `{pdf_sha}`. Mathematical ledger SHA-256: `{ledger_sha}`. Receipt: `records/S6_SERIES_PUBLISH_I_complete_gate.json`.\n\nThe continuation applied {continuation_edits} exact editorial changes: the eleven archived candidate13 guards; accented spellings; records-link, attribution and CC0 wording; further redundant clauses and body-history passages found by contextual and whole-page reading; and concrete citation or sentence repairs. The complete forward and inverse source maps, preserved mathematical segments and statement comparisons are recorded. No new mathematical error was established in this continuation. The mathematical corrections found in the first run remain listed in the dated sections above: the lattice-pole description, logarithm transport, the missing E4 factor, the selected small-resolution charts and their propagation, the central-component/meridian argument, and the exact auxiliary-field/source-application scopes.\n\nThe final paper contains 333 printed environments with 353 statement identifiers. Its 1846 check associations belong to 1614 declared evidence groups: 767 targeted proof checks, 10 independent re-proofs, 143 computations or certificates, 731 used-and-rechecked associations, 194 background associations and 1 refutation. These are independently recounted from the unchanged 7866-row ledger. All 7 main theorems and 40 outline items are byte-identical to the checked candidate13 text, with 80 body-block associations transported through the exact edits.\n\nThe final pdfLaTeX build passes every typesetting gate: zero overflow above 2pt, undefined references or citations, missing fonts or characters, duplicate labels or duplicate destinations. Earlier candidate build summaries retain their before-counts. Every final page has actual full-image reading evidence; earlier reading transfers only by byte equality of the whole rendered PNG. The read-again pages and all dispositions are in `S6_SERIES_PUBLISH_reading_I.md`. The {edit_count} edit locations retain their explicitly identified before-PDF scopes and their final current loci.\n\nAll 42 provenance claims, the deposit fields and the metadata now bind to this exact source/PDF/ledger. Eight associations from two bounded continuation literature searches are in the inventory, with their scope and primary-source receipts. The mandated publication-record pin was opened, its commit checked and its raw report matched to the attachment. No deposit or external publication was performed.\n'
        for old,new in [('applied24','applied 24'),('contains333','contains 333'),('with353','with 353'),
                        ('Its1846','Its 1846'),('to1614','to 1614'),('groups:767','groups: 767'),
                        (',10 ',', 10 '),(',143 ',', 143 '),(',731 ',', 731 '),(',194 ',', 194 '),
                        ('and1 ','and 1 '),('unchanged7866','unchanged 7866'),('All7 ','All 7 '),
                        ('and40 ','and 40 '),('with80 ','with 80 '),('above2pt','above 2pt'),
                        ('The1977','The 1977'),('All42','All 42')]:
            summary=summary.replace(old,new)
        report_path.write_text(report+summary)
    else:
        destination=ROOT/'agents/continuation_infra/S6_SERIES_PUBLISH_I_complete_gate_preview.json'
        destination.write_text(json.dumps(record,indent=2)+'\n')
    assert sha(source)==source_sha and sha(ledger)==ledger_sha
    print(json.dumps({'applied':args.apply,'gate':str(destination),'source_sha256':source_sha,
                      'pdf_sha256':pdf_sha,'pages':page_total,'defect_types':25,'provenance_claims':42,
                      'mathematical_events_added':0},indent=2))


if __name__=='__main__':
    main()

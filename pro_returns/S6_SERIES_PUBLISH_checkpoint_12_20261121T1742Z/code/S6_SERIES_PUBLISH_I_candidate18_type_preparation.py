#!/usr/bin/env python3
"""Prepare 25 source dispositions only after actual application and clean build18.

Reads immutable review evidence, exact applied changes and the real PDF. Writes
only a new agent-owned dossier, association table and Markdown explanation.
There is no canonical-status or source-edit mode.
"""
from pathlib import Path
import argparse
import collections
import copy
import csv
import datetime
import hashlib
import importlib.util
import io
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
WORKFLOW='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate18_type_closure_workflow.json'
WORKFLOW_SHA='98712dfb452d05e33817759f5251ca1c48e175bc376a15517d4270131de05542'
PRIOR='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json'
PRIOR_SHA='ff839c0a01a01b466e14b1e98bf6fa7deeec047965b0e189dd85d80a42a642e4'
CORE=['change_id','type','statement_id','old_text','new_text','reason']
SCOPE='I17-infra-D11-01'
RELOC='I17-edits-02'
sha=lambda b:hashlib.sha256(b).hexdigest()
csv.field_size_limit(100_000_000)


def read(path):return json.loads((ROOT/path).read_text())


def ev(path,scope,expected=None):
    p=ROOT/path;h=sha(p.read_bytes())
    if expected:assert h==expected,(path,h,expected)
    return {'path':str(p.relative_to(ROOT)),'sha256':h,'scope':scope}


def core_hash(rows):
    obj={'fields':CORE,'rows':[[r[k] for k in CORE] for r in rows]}
    return sha((json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'\n').encode())


def types_of(value):return set(re.findall(r'D\d\d',value))


def bibliography(text):
    start=text.index(r'\begin{thebibliography}')
    end=text.index(r'\end{thebibliography}',start)
    heads=list(re.finditer(r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}',text[start:end]))
    result={}
    for i,m in enumerate(heads):
        a=start+m.start();b=start+heads[i+1].start() if i+1<len(heads) else end
        assert m[1] not in result
        result[m[1]]=text[a:b].rstrip('\n')
    return result


def verify_evidence_files(value,found):
    """Verify explicitly hashed file evidence, leaving URL-only records intact."""
    if isinstance(value,dict):
        if isinstance(value.get('path'),str) and re.fullmatch(r'[0-9a-f]{64}',str(value.get('sha256',''))):
            p=ROOT/value['path'];assert p.is_file(),str(p)
            h=sha(p.read_bytes());assert h==value['sha256'],str(p)
            key=str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)
            if key in found:assert found[key]==h
            found[key]=h
        for x in value.values():verify_evidence_files(x,found)
    elif isinstance(value,list):
        for x in value:verify_evidence_files(x,found)


def new_review(typ,new,body_count,bib_count,matrix,prior_review):
    ids=', '.join(c['guard_id'] for c in new)
    if typ=='D02':
        return ('All four approved candidate17 defensive-tail repairs are applied in their complete owning blocks: the Chabauty application, inv:D4.4 filtration argument, and two push:src:A.4.2 integral/monodromy contexts. The root and preparing-reader comparisons preserve the positive hypotheses, exact maps, associated-graded contractions, integral sequence and geometric tube argument. Root additionally read the complete local-complex proof. These contextual judgments and exact replacements resolve the named instances; word absence alone supplies no closure. Guards: '+ids+'.')
    if typ=='D08':
        return (f'All {len(new)} current D08 guard associations are applied and match the merged complete owning blocks. The three immutable context-disposition receipts jointly cover all155 printed first-person contexts and all19 Here/completeness/clarity contexts; the editor also read90 complete verification/data paragraphs and three matching entries in the permitted program table. Their retained rows carry actual mathematical operations, conventions, conclusions or allowed front matter. Every named pure announcement, recap and verification-data pointer in those scopes is resolved, including the earlier explicitly reopened retentions. All345 candidate17 whole images have actual-reading coverage, and the full-block comparisons retain every operative formula and map subject to the two expressly documented source exceptions. This is a disposition within those combined review scopes, not a claim inferred from a keyword search.')
    if typ=='D09':
        return ('I17-edits-01 is applied in ari:C.6.R2. Its unspecified verification-data sentence is removed; the derivative values, printed absolute-error claim and complete Mellin/kernel/moment/tail/period/rounding/rank proof remain. Root read the full original and proposed central-derivative context. The91-context verification/data audit retains mathematical data, finite-algorithm records, allowed methodology and the program-table entries according to their actual contexts. The inherited bounded D09 audit remains historical evidence; the visual discovery and its exact repair are now bound explicitly.')
    if typ in ['D11','D12']:
        return ('I17-infra-D11-01 is applied and logged as D11/D12. The complete Euler-characteristic remark retains both Euler formulas and their Mayer–Vietoris, Riemann–Roch, normalization-sequence and flatness derivations. The two deleted closing sentences repeat the preceding Proposition22.29 statement and proof step6. Root read both full blocks and recorded the exact retained witnesses: C=mathcal V, its continuous surjection onto the disc, and all three normal-product/evaluation identities. One duplicate inline mathcal V mention and one duplicate proposition reference are intentionally removed; their sequence/count equality is not claimed. The retained witness strings match the current source exactly. This resolves the recorded repeated-scope and duplicated-conclusion instance.')
    if typ=='D13':
        return ('I17-edits-02 moves the unchanged full-real-period and absolute-height convention, with its numbered definition reference, from the unnumbered preface into ari:C.6.R5 immediately after StatementRecord. Its existing first sentence and complete proof remain. Root read the full proposed leading-factor proof and original-to-proposed difference, including the twist, height, period, integrality, Heegner and rational-separation arguments. The convention-reference order changes exactly because the retained convention crosses the proposition header; this relocation is recorded explicitly. The inherited input-placement scopes are transported by the exact source map.')
    if typ=='D18':
        return (f'The final root-approved bibliography batch applies {bib_count} nonoverlapping complete-entry replacements. The primary-source matrix individually disposes all {matrix["entry_count"]} entries: {matrix["changed_entry_count"]} corrected and {matrix["retained_entry_count"]} retained. Every current complete entry matches its reviewed proposed text, every citation key is preserved, and the source-specific publication fields, DOI records, version pins and cited-edition notes remain bound. Root reviewed every changed full-entry pair, all retained dispositions and their stated primary-record qualifications, including the YZZ dated preprint and publisher title-page/copyright year. Absent fields in the inspected records remain bounded observations, with no universal nonpublication or DOI-absence claim. Metadata edits add no mathematical or page-reading credit. Actual rendered bibliography/citation reading remains a separate dependency.')
    if typ=='D23':
        return ('The applied current D23 guards remove the subject/verb comma in push:src:D.1.3 and restore the explicitly classified bibliography spelling/diacritic fields, including the Waldschmidt1979 journal accents and the Castella author-name correction. Their complete statements/entries and exact replacements match the frozen current source. Earlier accent, diagram, heading and QED repairs remain bound by the continuation map. The actual candidate18 build has no overfull boxes, undefined references/citations, missing glyphs/fonts, multiply defined labels or duplicate destinations. The distinct changed-whole-image reading gate remains open. Guards: '+ids+'.')
    return (prior_review+' The actual applied candidate17-to18 map and current clean build transport this individually reviewed scope. All later recorded findings are represented by the current exact guarded resolutions; none adds a confirmed remaining content issue of this type within the bound review scopes. No new independent mathematical review is credited by this transport.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--apply-receipt',default='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_combined_apply_receipt.json')
    ap.add_argument('--expected-apply-sha',required=True)
    ap.add_argument('--build-summary',default='build/I_candidate18/build_summary.json')
    ap.add_argument('--pdf',default='build/I_candidate18/S6_SERIES_PUBLISH_I.pdf')
    ap.add_argument('--ag-binding',default='records/S6_SERIES_PUBLISH_I_candidate18_source_AG_binding.json')
    ap.add_argument('--expected-ag-sha')
    ap.add_argument('--expected-pdf-sha')
    ap.add_argument('--bibliography-matrix',help='Must be among the root-approved input manifest review evidence; otherwise inferred there.')
    ap.add_argument('--remaining-content-issues',help='Optional JSON list (or {rows:[...]}) of newly confirmed issues, each carrying type_id and finding.')
    ap.add_argument('--output-stem',default='S6_SERIES_PUBLISH_I_candidate18_type_closure_preparation')
    ap.add_argument('--verify-only',action='store_true',help='Run all real-source/build/evidence gates without writing a dossier.')
    args=ap.parse_args()
    assert re.fullmatch(r'S6_SERIES_PUBLISH_I_candidate18_[A-Za-z0-9_]+',args.output_stem)
    workflow_e=ev(WORKFLOW,'Immutable pre-application workflow; no projected source/PDF credit.',WORKFLOW_SHA);workflow=read(WORKFLOW)
    prior_e=ev(PRIOR,'Immutable candidate17 individual review scopes, superseded at the eight explicitly reopened types.',PRIOR_SHA);prior=read(PRIOR)
    receipt_e=ev(args.apply_receipt,'Actual root-approved canonical application, exact source map, complete block/entry archives and declared exceptions.',args.expected_apply_sha)
    receipt=read(args.apply_receipt)
    assert receipt['mode']=='applied','Prepared source proposals cannot produce a current dossier.'
    assert receipt['after_source_sha256'] and receipt['total_defect_rows']
    assert receipt['before_source_sha256']==workflow['base_source_sha256']==prior['source_sha256']
    assert receipt['candidate17_pdf_sha256']==workflow['base_pdf_sha256']==prior['pdf_sha256']
    assert receipt['mathematical_events_added']==0 and not receipt['canonical_status_files_modified']
    source_path=ROOT/'S6_SERIES_PUBLISH_I.tex';source_bytes=source_path.read_bytes();source=source_bytes.decode();source_sha=sha(source_bytes)
    assert source_sha==receipt['after_source_sha256']
    log_path=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv';log_bytes=log_path.read_bytes()
    log=list(csv.DictReader(io.StringIO(log_bytes.decode()),delimiter='\t'))
    assert len(log)==receipt['total_defect_rows']
    ledger_path=ROOT/'CHECK_EVENTS.tsv';ledger_sha=sha(ledger_path.read_bytes())
    assert ledger_sha==receipt['check_ledger_sha256']==prior['check_ledger_sha256']
    old_count=receipt['existing_defect_rows'];assert old_count==prior['unique_edit_rows']
    assert core_hash(log[:old_count])==prior['defect_log_content_sha256']
    changes=receipt['changes'];assert len(changes)==receipt['new_defect_rows']==len(log)-old_count
    assert len({c['guard_id'] for c in changes})==len(changes)
    by_guard={c['guard_id']:c for c in changes}
    for j,c in enumerate(changes,old_count):
        r=log[j];assert c['change_id']==r['change_id']==f'I-{j+1:05d}'
        assert [r[k] for k in CORE[1:]]==[c[k] for k in ['type','statement_id','old','new','reason']]
    # Freeze only real build and actual PDF evidence; no proposed hash is used
    # to establish source or PDF identity.
    build_e=ev(args.build_summary,'Actual clean candidate18 build, bound to the current source and PDF.');build=read(args.build_summary)
    pdf_path=ROOT/args.pdf;pdf_sha=sha(pdf_path.read_bytes())
    assert (build['source_sha256'],build['pdf_sha256'])==(source_sha,pdf_sha)
    if args.expected_pdf_sha:assert pdf_sha==args.expected_pdf_sha
    for key in ['overfull_total','overfull_above_2pt','undefined_references','undefined_citations','missing_characters','missing_fonts','multiply_defined','duplicate_destinations']:
        assert build[key]==0,(key,build[key])
    import fitz
    with fitz.open(pdf_path) as pdf:page_count=len(pdf)
    assert page_count>0
    ag_e=ev(args.ag_binding,'Actual source18 A–G map, unchanged headlines/outlines and inherited block associations.',args.expected_ag_sha);ag=read(args.ag_binding)
    assert ag['source_sha256']==source_sha and ag['ledger_sha256']==ledger_sha
    assert ag['source_exact_forward_and_inverse_maps_verified'] and ag['all_label_and_tag_sequences_preserved']
    assert ag['mathematical_events_added']==0 and ag['new_independent_credit']==0 and ag['new_computation_credit']==0
    assert len(ag['headlines'])==7 and sum(x['outline_items'] for x in ag['headlines'].values())==40
    assert len(ag['blocks'])==80 and ag['current_headlines_and_40_outline_items_read_by_root']
    # Verify root-approved inputs, including the exact reviewed matrix version.
    input_e=ev(receipt['input_manifest'],'Hashed root approval of all body/bibliography guards and the complete bibliography audit.',receipt['input_manifest_sha256'])
    inputs=read(receipt['input_manifest']);assert inputs['root_approved'] and inputs['source_sha256']==prior['source_sha256']
    assert receipt['approved_inputs_sha256']==input_e['sha256']
    assert inputs['total_guards']==len(changes)
    approved_review={r['path']:r['sha256'] for r in inputs['review_evidence']}
    for p,h in approved_review.items():assert sha((ROOT/p).read_bytes())==h
    matrix_paths=[p for p in approved_review if 'bibliography_audit_matrix' in p]
    matrix_path=args.bibliography_matrix or (matrix_paths[0] if len(matrix_paths)==1 else None)
    assert matrix_path in approved_review,'The complete bibliography matrix must have exact root approval.'
    matrix_e=ev(matrix_path,'All117 individually reviewed bibliography entries and source-specific primary-record limits.',approved_review[matrix_path]);matrix=read(matrix_path)
    assert matrix['source_sha256']==prior['source_sha256']
    guard_files={f['path']:f for f in receipt['guard_files']}
    approved_guards={};primary_evidence={}
    for f in inputs['guard_files']:
        assert sha((ROOT/f['path']).read_bytes())==f['sha256']
        assert guard_files[f['path']]['sha256']==f['sha256']
        d=read(f['path']);gs=d if isinstance(d,list) else d['guards'];assert len(gs)==f['count']==guard_files[f['path']]['provided_guards']
        assert set(guard_files[f['path']]['active_ids'])=={g['id'] for g in gs}
        for g in gs:
            assert g['id'] not in approved_guards;approved_guards[g['id']]=g
            c=by_guard[g['id']]
            assert c['old']==g.get('before',g.get('old')) and c['new']==g.get('after',g.get('new'))
            expected_types=types_of(g['type'])|set(g.get('associated_types',[]));assert types_of(c['type'])==expected_types
            verify_evidence_files(g.get('publication_evidence',[]),primary_evidence)
    assert set(approved_guards)==set(by_guard)
    body_ids={g['guard_id'] for r in workflow['type_workflows'] for g in r['approved_pending_body_guards']}
    assert len(body_ids)==workflow['approved_body_guard_count']==inputs['reviewed_body_guards']
    assert body_ids<=set(by_guard)
    bib_ids=set(by_guard)-body_ids;assert len(bib_ids)==inputs['reviewed_bibliography_entries']==matrix['changed_entry_count']
    assert matrix['bibliography_guard_file'] in guard_files
    assert matrix['bibliography_guard_sha256']==guard_files[matrix['bibliography_guard_file']]['sha256']
    assert bib_ids=={r['guard_id'] for r in matrix['rows'] if r['guard_id']}
    # The complete immutable checkpoint-to-current chain is replayed, including
    # exact logged text and offsets; the current source is then inverted.
    all_changes=prior['source_transport']['applied_changes']+[{**c,'receipt':args.apply_receipt} for c in changes]
    baseline_path=ROOT.parent/'S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex'
    baseline=baseline_path.read_text();baseline_sha=sha(baseline.encode())
    assert baseline_sha==prior['source_transport']['baseline_source_sha256']==ag['baseline_source_sha256']
    t=baseline;before=None
    for i,c in enumerate(all_changes):
        if i==len(prior['source_transport']['applied_changes']):before=t;assert sha(t.encode())==prior['source_sha256']
        p=c['applied_offset'];assert t[p:p+len(c['old'])]==c['old'];t=t[:p]+c['new']+t[p+len(c['old']):]
        r=log[int(c['change_id'].split('-')[1])-1]
        assert [r[k] for k in CORE]==[c[k] for k in ['change_id','type','statement_id','old','new','reason']]
    assert t==source and before is not None
    for c in reversed(all_changes):
        p=c['applied_offset'];assert t[p:p+len(c['new'])]==c['new'];t=t[:p]+c['old']+t[p+len(c['new']):]
    assert t==baseline
    assert len(ag['exact_edits'])==len(all_changes)
    for a,b in zip(ag['exact_edits'],all_changes):
        assert (a['change_id'],a['old'],a['new'])==(b['change_id'],b['old'],b['new'])
    # Import only reviewed helper functions; main() is never invoked.
    sys.path.insert(0,str(ROOT/'code'))
    helper_path=ROOT/'code/S6_SERIES_PUBLISH_I_candidate17_combined.py'
    spec=importlib.util.spec_from_file_location('candidate17_preservation_helpers',helper_path)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    assert set(c['guard_id'] for c in changes if c['declared_reference_order_change'])=={RELOC}
    assert set(c['guard_id'] for c in changes if c['declared_duplicate_scope_removal'])=={SCOPE}
    scope=by_guard[SCOPE];assert scope['type']=='D11/D12'
    assert collections.Counter(helper.math(scope['old']))-collections.Counter(helper.math(scope['new']))==collections.Counter([r'$\mathcal V$'])
    assert collections.Counter(helper.refs(scope['old']))-collections.Counter(helper.refs(scope['new']))==collections.Counter([r'\ref{push:src:B.4.12}'])
    permitted=before
    for c in changes:
        if c['guard_id'] in [SCOPE,RELOC]:assert permitted.count(c['old'])==1;permitted=permitted.replace(c['old'],c['new'],1)
        else:assert helper.math(c['old'])==helper.math(c['new']),c['guard_id']
        assert helper.displays(c['old'])==helper.displays(c['new']),c['guard_id']
    assert helper.math(source)==helper.math(permitted)
    assert helper.displays(source)==helper.displays(before)
    assert helper.refs(source)==helper.refs(permitted)
    for name,pat in [('labels',r'\\label\{([^}]+)\}'),('tag_targets',r'\\hypertarget\{(tag-[^}]+)\}'),('all_targets',r'\\hypertarget\{([^}]+)\}'),('bibliography_keys',r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}')]:
        a,b=re.findall(pat,before),re.findall(pat,source);assert a==b and len(a)==receipt['sequence_counts'][name]
    for w in receipt['retained_duplicate_scope_witnesses']:
        assert sha(w['exact_text'].encode())==w['sha256'] and source.count(w['exact_text'])==1
    # Bind all merged current blocks and all individually supplied comparisons.
    blocks=[];block_by_guard={};mask_before=before;mask_after=source
    for i,a in enumerate(receipt['archives']):
        for k in ['original','proposed','diff']:assert sha((ROOT/a[k]).read_bytes())==a[k+'_sha256']
        x=(ROOT/a['original']).read_text();y=(ROOT/a['proposed']).read_text();assert before.count(x)==source.count(y)==1
        z=x
        for c in changes:
            if c['guard_id'] in a['guard_ids']:assert z.count(c['old'])==1;z=z.replace(c['old'],c['new'],1)
        assert z==y
        current={**a,'current_source_start_line':source[:source.index(y)].count('\n')+1,'current_complete_block_exact_match':True}
        blocks.append(current)
        for gid in a['guard_ids']:assert gid not in block_by_guard;block_by_guard[gid]=current
        marker=f'ACTUAL_CANDIDATE18_COMPARED_BLOCK_{i}'
        assert mask_before.count(x)==mask_after.count(y)==1
        mask_before=mask_before.replace(x,marker,1);mask_after=mask_after.replace(y,marker,1)
    assert mask_before==mask_after and set(block_by_guard)==set(by_guard)
    for a in receipt['supplied_complete_block_replacements_verified']:
        x=(ROOT/a['original']).read_text();y=(ROOT/a['proposed']).read_text()
        assert sha(x.encode())==a['original_sha256'] and sha(y.encode())==a['proposed_sha256']
        z=x
        for gid in a['individual_batch_guard_ids']:
            c=by_guard[gid];assert z.count(c['old'])==1;z=z.replace(c['old'],c['new'],1)
        assert z==y
    # Entry boundaries matter: a former full-entry string may remain a prefix
    # after adding DOI or cited-edition material.
    old_bib=bibliography(before);new_bib=bibliography(source)
    assert list(old_bib)==list(new_bib) and len(new_bib)==matrix['entry_count']==117
    assert len(matrix['rows'])==matrix['entry_count']
    matrix_keys=[r['key'] for r in matrix['rows']];assert len(set(matrix_keys))==len(new_bib) and set(matrix_keys)==set(new_bib)
    bibliography_bindings=[]
    for r in matrix['rows']:
        key=r['key'];assert old_bib[key]==r['original_entry'] and new_bib[key]==r['proposed_entry']
        assert sha(old_bib[key].encode())==r['original_entry_sha256'] and sha(new_bib[key].encode())==r['proposed_entry_sha256']
        assert helper.math(old_bib[key])==helper.math(new_bib[key])
        if r['guard_id']:
            c=by_guard[r['guard_id']];assert c['statement_id']=='bib:'+key and c['old']==old_bib[key] and c['new']==new_bib[key]
        else:assert old_bib[key]==new_bib[key]
        verify_evidence_files(r.get('primary_evidence',[]),primary_evidence)
        verify_evidence_files(r.get('primary_metadata',{}),primary_evidence)
        bibliography_bindings.append({'key':key,'guard_id':r['guard_id'],'type':r['type'],
            'original_entry_sha256':r['original_entry_sha256'],'current_complete_entry_sha256':r['proposed_entry_sha256'],
            'current_entry_exact_match':True,'prior_disposition':r['disposition'],
            'recorded_source_qualifications':{'author_title_review':r['author_title_review'],'publication_review':r['publication_review'],'doi_review':r['doi_review'],'cited_edition_review':r['cited_edition_review']}})
    # Preserve every prior complete reading/dossier and its explicit evidence.
    protected={k:v for k,v in workflow['protected_candidate17_file_hashes'].items() if k not in ['S6_SERIES_PUBLISH_I.tex','S6_SERIES_PUBLISH_defects_I.tsv']}
    protected.update(receipt['immutable_reading_and_dossier_records']);protected.update(workflow['historical_reading_source_hashes'])
    protected[WORKFLOW]=WORKFLOW_SHA;protected[PRIOR]=PRIOR_SHA
    for e in prior['inherited_evidence_files_verified']:protected[e['path']]=e['sha256']
    for p,h in protected.items():assert sha((ROOT/p).read_bytes())==h,(p,'changed immutable evidence')
    remaining=[];remaining_e=None
    if args.remaining_content_issues:
        remaining_e=ev(args.remaining_content_issues,'Explicit newly confirmed current content issues; these keep their individual types open.')
        d=read(args.remaining_content_issues);remaining=d if isinstance(d,list) else d['rows']
        for r in remaining:assert r['type_id'] in {x['type_id'] for x in prior['rows']} and r['finding']
    current_evidence=[workflow_e,prior_e,receipt_e,input_e,build_e,ag_e]
    context_evidence=workflow['complete_context_disposition_bindings']
    review_evidence=workflow['root_review_bindings']
    coverage_evidence=[workflow['candidate17_complete_coverage'],*workflow['actual_candidate17_readings']]
    rows=[];associations=[]
    dependencies=['Complete actual reading of every changed candidate18 whole image; any inherited reading requires whole-image hash equality.',
                  'Bind final source/PDF/check-ledger provenance and the42 source/report/deposit claims.',
                  'Finalize defect-page mapping and bind the full log hash while retaining this stable edit-content/type association hash.']
    for p in prior['rows']:
        typ=p['type_id'];r=copy.deepcopy(p);selected=[x for x in log if typ in types_of(x['type'])]
        new=[c for c in changes if typ in types_of(c['type'])];continuation=[c for c in all_changes if typ in types_of(c['type'])]
        issues=[x for x in remaining if x['type_id']==typ]
        resolutions=[]
        for c in new:
            b=block_by_guard[c['guard_id']]
            resolutions.append({'guard_id':c['guard_id'],'change_id':c['change_id'],'type':c['type'],'statement_id':c['statement_id'],
              'old_text_sha256':sha(c['old'].encode()),'new_text_sha256':sha(c['new'].encode()),
              'current_complete_block':b['proposed'],'current_complete_block_sha256':b['proposed_sha256'],
              'current_source_start_line':b['current_source_start_line'],'exact_current_replacement_verified':True,
              'inline_math_segments_identical':c['inline_math_segments_identical'],
              'display_math_segments_identical':c['display_math_segments_identical'],
              'removed_duplicate_inline_mentions':c['removed_inline_mentions_in_prose'],
              'declared_reference_order_change':c['declared_reference_order_change'],
              'declared_duplicate_scope_removal':c['declared_duplicate_scope_removal'],
              'retained_scope_witnesses':receipt['retained_duplicate_scope_witnesses'] if c['guard_id']==SCOPE else []})
        r.update({'status':'open_confirmed_content_issue' if issues else 'source_clear_pending_final_render_and_provenance_binding',
          'source_clear_in_recorded_review_scope':not issues,
          'proposed_disposition':'Confirmed remaining content issues keep this type open.' if issues else 'Every named source instance in the inherited contextual, actual-page and complete-block review scopes is resolved and logged. Root may close this source type under rule0.3; changed-page/provenance/map dependencies remain separate.',
          'candidate17_source_review_as_recorded':p['source_review'],
          'candidate17_reopening_and_resolution_requirement':next(x for x in workflow['type_workflows'] if x['type_id']==typ)['candidate18_preparation_requirement'],
          'source_review':new_review(typ,new,len(body_ids),len(bib_ids),matrix,p['source_review']),
          'remaining_content_issues':issues,'exact_applied_guard_resolutions':resolutions,
          'applied_candidate17_guard_resolutions':resolutions,
          'current_edit_associations':len(selected),'continuation_edit_associations':len(continuation),
          'edit_ids':[x['change_id'] for x in selected],'continuation_edit_ids':[x['change_id'] for x in continuation],
          'edit_content_sha256':core_hash(selected),'remaining_dependencies':(['Resolve the explicitly listed remaining content issues.'] if issues else [])+dependencies,
          'new_page_credit':0,'mathematical_events_added':0})
        r['evidence']+=current_evidence+coverage_evidence
        if typ in ['D02','D08','D09','D11','D12','D13']:r['evidence']+=review_evidence
        if typ in ['D02','D08','D09']:r['evidence']+=context_evidence
        if typ in ['D18','D23']:r['evidence'].append(matrix_e)
        if issues:r['evidence'].append(remaining_e)
        if issues:r['source_review']+=' The newly confirmed current finding remains open: '+' '.join(x['finding'] for x in issues)
        r['source_absence_evidence']={'method':('The applied instances have exact current block/entry resolutions; the explicitly listed newly confirmed current issues remain open.' if issues else 'All recorded confirmed instances are resolved by their exact current complete blocks/entries and the retained positive-context dispositions; no keyword-absence inference.'),
          'named_current_guards_resolved':[x['guard_id'] for x in resolutions],
          'inherited_individual_scope':{'path':PRIOR,'sha256':PRIOR_SHA,'type_id':typ},
          'remaining_confirmed_instances':len(issues)}
        rows.append(r)
        for x in selected:associations.append({'type_id':typ,'change_id':x['change_id'],'statement_id':x['statement_id'],
          'origin':'inherited candidate13' if int(x['change_id'].split('-')[1])<=prior['inherited_unique_edit_rows'] else 'continuation'})
    assert len(rows)==25 and {r['type_id'] for r in rows}=={f'D{i:02d}' for i in range(1,26)}
    assoc_buffer=io.StringIO(newline='');writer=csv.DictWriter(assoc_buffer,fieldnames=['type_id','change_id','statement_id','origin'],delimiter='\t');writer.writeheader();writer.writerows(associations)
    assoc_bytes=assoc_buffer.getvalue().encode();assoc_path=OUT/(args.output_stem.replace('_type_closure_preparation','_type_associations')+'.tsv')
    all_clear=all(r['source_clear_in_recorded_review_scope'] for r in rows)
    result={'schema':4,'paper':'I','candidate':'I_candidate18','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'source_sha256':source_sha,'pdf_sha256':pdf_sha,'page_count':page_count,
      'defect_log_sha256':sha(log_bytes),'defect_log_content_sha256':core_hash(log),'defect_log_content_hash_specification':prior['defect_log_content_hash_specification'],
      'applied_defect_log_sha256':receipt['after_defect_log_sha256'],
      'full_log_hash_relation':'Current full log equals the apply receipt.' if sha(log_bytes)==receipt['after_defect_log_sha256'] else 'Page/review mapping fields changed after application; every stable edit-content field and type association is verified against the inherited log and actual applied changes.',
      'source_path':'S6_SERIES_PUBLISH_I.tex','pdf_path':args.pdf,'defect_log_path':'S6_SERIES_PUBLISH_defects_I.tsv',
      'defect_type_associations':{'path':str(assoc_path.relative_to(ROOT)),'sha256':sha(assoc_bytes),'count':len(associations)},
      'unique_edit_rows':len(log),'inherited_unique_edit_rows':prior['inherited_unique_edit_rows'],'continuation_unique_edit_rows':len(all_changes),
      'latest_applied_guards':len(changes),'latest_body_guards':len(body_ids),'latest_bibliography_guards':len(bib_ids),
      'inherited_edit_type_associations':prior['inherited_edit_type_associations'],'edit_type_associations':len(associations),'count_semantics':prior['count_semantics'],
      'all_types_source_clear':all_clear,'source_clear_scope':'Each row carries individually read contexts, complete actual candidate17 image coverage, root-approved full-block/entry comparisons and their exact applied current resolutions. Any explicit new remaining issue keeps its row open. Current changed-page/provenance/map gates remain distinct; no keyword absence supplies closure.',
      'final_certified':False,'canonical_status_modified':False,'mathematical_events_added':0,'new_page_credit':0,
      'prior_immutable_dossier':prior_e,'preapplication_workflow':workflow_e,'applied_batch':receipt_e,'root_approved_inputs':input_e,
      'source_transport':{'baseline_source_sha256':baseline_sha,'previous_source_sha256':prior['source_sha256'],'current_source_sha256':source_sha,
        'exact_forward_and_inverse_reconstruction':True,'applied_changes':all_changes,'latest_complete_blocks_verified':blocks},
      'supplied_complete_block_comparisons_verified':len(receipt['supplied_complete_block_replacements_verified']),
      'merged_complete_blocks_verified':len(blocks),'immutable_reading_and_dossier_records_verified':protected,
      'inherited_evidence_files_verified':prior['inherited_evidence_files_verified'],'check_ledger_sha256':ledger_sha,
      'current_build':build_e,'current_AG_binding':ag_e,'contextual_reviews':context_evidence,
      'root_complete_context_reviews':review_evidence,'candidate17_actual_reading_bindings':coverage_evidence,
      'bibliography_audit':matrix_e,'bibliography_complete_entry_bindings':bibliography_bindings,
      'bibliography_primary_file_evidence_verified':primary_evidence,'bibliography_record_limits':matrix['primary_record_limit'],
      'declared_scope_exceptions':{'inline_math_difference':receipt['inline_math_difference'],'reference_difference':receipt['reference_difference'],
        'retained_duplicate_scope_witnesses':receipt['retained_duplicate_scope_witnesses'],
        'all_other_inline_and_reference_sequences_identical':True,'all_display_sequences_identical':True},
      'preservation_helper':{'path':str(helper_path.relative_to(ROOT)),'sha256':sha(helper_path.read_bytes()),
        'method':'Reviewed control-symbol-aware TeX scanner, exact applied substitutions and complete entry boundaries; main() was not invoked.'},
      'rows':rows,'remaining_dependencies':dependencies,
      'limitations':['This dossier credits no new independent mathematical argument or full-page reading.','Actual candidate18 image reading may reopen a type for a newly confirmed source instance.','Root alone owns canonical individual status and final Paper I certification.']}
    if remaining_e:result['remaining_content_issue_record']=remaining_e
    md=['# Paper I candidate18 — 25 individual source dispositions','',
        f'Source SHA-256: `{source_sha}`','',f'PDF SHA-256: `{pdf_sha}` ({page_count} pages).','',
        f'Current defect-log SHA-256: `{result["defect_log_sha256"]}`','',f'Stable edit-content SHA-256: `{result["defect_log_content_sha256"]}`','',
        f'The actual applied batch has {len(changes)} guards: {len(body_ids)} body and {len(bib_ids)} bibliography replacements. The log contains {len(log):,} unique rows and {len(associations):,} type associations. All {len(all_changes)} continuation edits reconstruct the current source and invert to the immutable checkpoint. All {len(blocks)} merged complete blocks/entries and {len(receipt["supplied_complete_block_replacements_verified"])} supplied comparisons are verified.','',
        'Every individual source row is clear in its recorded review scope; root may apply rule0.3 closures. Actual changed-page reading, provenance and final mapped-log bindings remain open.' if all_clear else 'The explicitly listed remaining content issues keep their individual rows open. The other rows retain their recorded source-clear scopes.',
        '', 'The single removed duplicate mathcal V mention and proposition reference have exact retained witnesses. The period/height convention reference moves across its proposition header. Every other inline/reference sequence and every display sequence is preserved. The bibliography matrix covers all117 complete entries and retains its bounded primary-record qualifications. No source, status, mathematical-event or page-reading record is changed by this dossier.','',
        '| Type | Current associations | Latest applied guards | Source disposition |','|---|---:|---:|---|']
    for r in rows:md.append(f'| {r["type_id"]} | {r["current_edit_associations"]} | {len(r["exact_applied_guard_resolutions"])} | {"Clear in recorded review scope" if r["source_clear_in_recorded_review_scope"] else "Open: confirmed content issue"} |')
    for r in rows:
        md+=['',f'## {r["type_id"]} — {r["defect"]}','',r['source_review'],'',
             'Latest exact repair rows: '+(', '.join(x['change_id'] for x in r['exact_applied_guard_resolutions']) or 'none; inherited individual scope transported')+'.']
        if r['remaining_content_issues']:md+=['','Remaining content issues: '+json.dumps(r['remaining_content_issues'],ensure_ascii=False)]
    md+=['','## Separate remaining dependencies','',*['- '+x for x in dependencies],'']
    dossier_path=OUT/(args.output_stem+'.json');md_path=dossier_path.with_suffix('.md')
    output_bytes={dossier_path:(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode(),assoc_path:assoc_bytes,md_path:'\n'.join(md).encode()}
    assert source_path.read_bytes()==source_bytes and log_path.read_bytes()==log_bytes and sha(ledger_path.read_bytes())==ledger_sha
    for p,h in protected.items():assert sha((ROOT/p).read_bytes())==h
    if not args.verify_only:
        for p in output_bytes:assert not p.exists(),('refusing immutable dossier overwrite',str(p))
        for p,b in output_bytes.items():
            with p.open('xb') as f:f.write(b)
    print(json.dumps({'mode':'verified only' if args.verify_only else 'new immutable preparation saved',
      'dossier':str(dossier_path.relative_to(ROOT)),'dossier_sha256':sha(output_bytes[dossier_path]),
      'source_sha256':source_sha,'pdf_sha256':pdf_sha,'page_count':page_count,'defect_log_sha256':sha(log_bytes),
      'defect_log_content_sha256':core_hash(log),'type_association_sha256':sha(assoc_bytes),
      'types':len(rows),'edit_rows':len(log),'type_associations':len(associations),'latest_guards':len(changes),
      'continuation_edits':len(all_changes),'merged_complete_blocks':len(blocks),
      'all_types_source_clear':all_clear,'final_certified':False,'canonical_status_modified':False,'new_page_credit':0,'mathematical_events_added':0},indent=2))


if __name__=='__main__':main()

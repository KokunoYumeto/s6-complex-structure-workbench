#!/usr/bin/env python3
"""Prepare the next per-type closure workflow; never certify an unbuilt source."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
SOURCE17='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF17='3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
OPEN=['D02','D08','D09','D11','D12','D13','D18','D23']
sha=lambda b:hashlib.sha256(b).hexdigest()

def read(p):return json.loads((ROOT/p).read_text())
def bind(p,h=None,scope=''):
    a=sha((ROOT/p).read_bytes())
    if h:assert a==h,(p,a,h)
    return {'path':p,'sha256':a,'scope':scope}

REVIEW_REQUIREMENTS={
 'D02':'Verify all four approved deletions in their complete owning blocks: the Chabauty tail, the inv:D4.4 contraction-nonrequirement tail, and two push:src:A.4.2 integral-index/monodromy tails. Carry the positive hypotheses, exact maps, filtration argument and tube proof from the root and preparing-reader reviews. No broad keyword absence is sufficient.',
 'D08':'Verify all 58 current body-guard associations, including the D08/D09 deletion and D08/D13 relocation, against the merged complete blocks. Bind the three complete disposition receipts covering all 155 first-person and 19 Here/completeness/clarity contexts, plus the editor verification/data sweep. Retained contexts describe actual constructions, conventions, mathematical conclusions or allowed front matter; the applied exact guards resolve each named announcement or recap. Preserve the historical audit reopenings explicitly.',
 'D09':'Verify I17-edits-01 removes only the unspecified verification-data sentence from ari:C.6.R2. Bind root’s additional complete central-derivative proof review, the retained numerical/error bounds and the 91-context source sweep (90 whole paragraphs and three matching program-table entries in the last context). The permitted program table remains in the retained scope.',
 'D11':'Verify I17-infra-D11-01 against the complete Euler-characteristic remark and its retained Proposition22.29 statement/proof. Preserve the exact C=mathcal V identification, continuous-surjection argument and normal-line table as the witnesses for the removed repeated scope sentences. Do not claim unchanged counts for the duplicate inline symbol/reference that are intentionally removed.',
 'D12':'Use the explicitly associated D12 resolution of I17-infra-D11-01. Bind the precise map from each repeated remark conclusion to the retained Proposition22.29 statement and proof step6; preserve all Euler formulas and derivations. The root scope-approval receipt records this D11/D12 association.',
 'D13':'Verify I17-edits-02 relocates the identical full-real-period/absolute-height convention and its numbered definition reference inside ari:C.6.R5 after StatementRecord. Bind root’s additional complete leading-factor proof review. Preserve the documented command/reference-order change; do not describe that order as identical.',
 'D18':'Wait for infrastructure’s consolidated 117-entry primary-source audit, final nonoverlapping bibliography guards and root approval. Verify exact complete-entry boundaries after application, established cited-edition notes and version pins, checked published DOI/metadata, unchanged citation keys, and any explicitly approved author-year changes. A DOI not found in bounded records must not become a universal absence or nonpublication claim.',
 'D23':'Verify the approved subject/verb comma repair and every typography/metadata spelling guard in the final consolidated bibliography batch. Carry earlier accent/diagram/heading repairs by the exact source map. A clean build supplies its diagnostic scope; changed full-page reading remains a separate gate.'
}

def main():
    source_path=ROOT/'S6_SERIES_PUBLISH_I.tex';source=source_path.read_bytes();assert sha(source)==SOURCE17
    assert sha((ROOT/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf').read_bytes())==PDF17
    protected={str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in [source_path,ROOT/'S6_SERIES_PUBLISH_defects_I.tsv',ROOT/'CHECK_EVENTS.tsv']}
    prior_path='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json'
    prior_b=bind(prior_path,'ff839c0a01a01b466e14b1e98bf6fa7deeec047965b0e189dd85d80a42a642e4','Immutable prior 25 individual source scopes; the eight current reopenings supersede their earlier clear status.')
    prior=read(prior_path)
    body_path='records/S6_SERIES_PUBLISH_I_candidate17_body_guard_review.json'
    body_b=bind(body_path,'a4b3b3c29b33bfa5c7741af18366bc28e144afc5a1d072ce864a05073a266d4f','Root’s exact review of all64 body proposals and49 supplied complete-block comparisons.')
    body=read(body_path);assert body['root_approved'] and body['guards']==64
    root_reviews=[body_b,
      bind('records/S6_SERIES_PUBLISH_I_candidate17_scope_guard_approval.json','a173c9b23b344908b6e2212635367080e833e8bcac4ffdccfb00e95bb821aa5c','Root’s complete scope and repeated-conclusion comparison, with exact object and removed-token maps.'),
      bind('records/S6_SERIES_PUBLISH_I_candidate17_root_substantive_context_review.json','5c34fb8c24da356c99d6fa13df338b0d9187a94a21f44f239bf427d45745968b','Root’s additional full central-derivative, exact-leading-factor and inv:D4.4 proof-context review; zero independent event credit.')]
    context_specs=[
      ('records/S6_SERIES_PUBLISH_I_candidate17_root_context_dispositions.json','8e4bc62e21701b8812c40db5b7fd4c03d27bf9488cd47a4863d0e5f2fb5cbba3'),
      ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_context_dispositions_edits.json','8da39579a8e6a72aad5b09f883f9a5f674fcf3f00dd32c83fdf93869b4f1ecfd'),
      ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_first_person_here_dispositions.json','a18e786541e3ca1f80ea59cf6780f27f2740392bd881cf200ce5872a58fd4d15')]
    contexts=[];fp=[];here=[]
    for p,h in context_specs:
        d=read(p);assert d['source_sha256']==SOURCE17
        assert all(x['actual_context_read'] for x in d['first_person_rows']+d['here_rows'])
        fp.extend(x['id'] for x in d['first_person_rows']);here.extend(x['id'] for x in d['here_rows'])
        contexts.append({**bind(p,h,'Complete bounded disposition receipt; these readings were performed by its named reader, not newly credited here.'),
          'first_person_contexts':len(d['first_person_rows']),'here_contexts':len(d['here_rows'])})
        if 'verification_data_rows' in d:
            assert all(x['actual_context_read'] for x in d['verification_data_rows'])
            contexts[-1]['verification_data_scope']=d['counts']
    assert sorted(fp)==list(range(1,156)) and sorted(here)==list(range(1,20))
    coverage_path='records/S6_SERIES_PUBLISH_I_candidate17_complete_coverage_snapshot.json'
    coverage_b=bind(coverage_path,'ed6a62823032dfcd50fcd800621244b249da899af03ecdcaf29db41306ff0f50','Immutable complete candidate17 coverage: current whole images or whole-image-identical prior actual readings.')
    coverage=read(coverage_path)
    assert (coverage['source_sha256'],coverage['pdf_sha256'],coverage['page_count'],coverage['covered_pages'])==(SOURCE17,PDF17,345,345)
    assert coverage['all_pages_read'] and not coverage['missing_pages'] and not coverage['certified']
    historical_reading_sources={x['reading_record']:x['reading_record_sha256'] for x in coverage['pages']}
    for p,h in historical_reading_sources.items():assert sha((ROOT/p).read_bytes())==h
    current_reading_paths=[
      'records/S6_SERIES_PUBLISH_I_final_candidate17_reading_root.json',
      'agents/i_cont_edits/S6_SERIES_PUBLISH_I_final_candidate17_reading_edits.json',
      'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate17_reading_provenance.json',
      'agents/continuation_infra/S6_SERIES_PUBLISH_I_final_candidate17_reading_infra.json']
    current_readings=[];direct_pages=[]
    for p in current_reading_paths:
        d=read(p);assert (d['source_sha256'],d['pdf_sha256'])==(SOURCE17,PDF17)
        current_readings.append({**bind(p,scope='Completed actual candidate17 full-image reading; preserve this file unchanged.'),'pages':len(d['pages'])})
        direct_pages.extend(x['page'] for x in d['pages'])
    assert len(direct_pages)==114 and len(set(direct_pages))==114
    guards=[];guard_bindings=[];t=source.decode();inverse=[]
    for f in body['guard_files']:
        d=read(f['path']);items=d if isinstance(d,list) else d['guards']
        assert len(items)==f['count']
        guard_bindings.append(bind(f['path'],f['sha256'],'Root-approved current body guard set.'))
        for g in items:
            assert g['source_sha256']==SOURCE17
            a,b=g['before'],g['after'];assert t.count(a)==1,g['id'];pos=t.index(a)
            t=t[:pos]+b+t[pos+len(a):];inverse.append((pos,a,b))
            types=sorted(set(re.findall(r'D\d\d',g['type'])+g.get('associated_types',[])))
            guards.append({'guard_id':g['id'],'types':types,'statement_id':g['statement_id'],
                           'before_sha256':sha(a.encode()),'after_sha256':sha(b.encode()),
                           'guard_file':f['path'],'guard_file_sha256':f['sha256'],'reason':g['reason']})
    assert len(guards)==64 and len({g['guard_id'] for g in guards})==64
    assert sha(t.encode())==body['body_proposal_sha256_without_bibliography']
    for pos,a,b in reversed(inverse):assert t[pos:pos+len(b)]==b;t=t[:pos]+a+t[pos+len(b):]
    assert t.encode()==source
    type_workflows=[]
    for r in prior['rows']:
        typ=r['type_id'];pending=[g for g in guards if typ in g['types']]
        type_workflows.append({'type_id':typ,'defect':r['defect'],
          'candidate17_current_disposition':'open; confirmed instance(s) await approved source application' if typ in OPEN else 'closed by prior individual root review; carry exact recorded scope',
          'prior_dossier':prior_b,'prior_edit_associations':r['current_edit_associations'],
          'approved_pending_body_guards':pending,
          'candidate18_preparation_requirement':REVIEW_REQUIREMENTS.get(typ,'Transport the individually reviewed prior source disposition through the exact applied edit map, verify retained scoped blocks and all later recorded findings, and report any new confirmed issue explicitly. This workflow grants no new closure.'),
          'candidate18_status':'not yet assessable; source application and build pending',
          'remaining_dependencies':['Final combined bibliography guard approval and full117-entry audit' if typ in ['D18','D23'] else 'Final approved combined source/log application',
                                    'Actual candidate18 source/PDF/build receipt and exact reconstruction',
                                    'Candidate18 changed whole-image reading, final provenance and mapped-log hash are separate final-certification dependencies'],
          'new_page_credit':0,'new_mathematical_events':0})
    assert len(type_workflows)==25
    candidate17_inputs=[prior_b,coverage_b,*root_reviews,*contexts,*current_readings,*guard_bindings]
    for x in candidate17_inputs:protected[x['path']]=x['sha256']
    result={'schema':1,'paper':'I','kind':'candidate18 closure workflow prepared against frozen candidate17; not a candidate18 dossier',
      'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'base_source_sha256':SOURCE17,'base_pdf_sha256':PDF17,
      'candidate18_source_sha256':None,'candidate18_pdf_sha256':None,
      'candidate18_dossier_frozen':False,'all_types_source_clear':False,
      'currently_open_types':OPEN,'currently_closed_type_count':17,
      'root_review_bindings':root_reviews,'complete_context_disposition_bindings':contexts,
      'context_coverage':{'first_person_ids_exactly':list(range(1,156)),'here_ids_exactly':list(range(1,20)),
                          'first_person_count':155,'here_count':19,'verification_data_contexts':91,
                          'verification_data_actual_scope':'90 whole source paragraphs, then table heading and three complete matching entries; no whole-table or new full-page claim'},
      'candidate17_complete_coverage':coverage_b,'actual_candidate17_readings':current_readings,
      'current_directly_read_candidate17_images':114,'historical_reading_source_hashes':historical_reading_sources,
      'approved_body_guard_count':64,'supplied_complete_block_comparisons':49,
      'body_proposal_sha256_without_bibliography':body['body_proposal_sha256_without_bibliography'],
      'body_proposal_exact_forward_and_inverse_verified':True,'body_guard_files':guard_bindings,
      'declared_scope_exceptions':body['inline_and_reference_scope_exceptions'],
      'bibliography_consolidation':{'status':'pending infrastructure final117-entry audit, consolidated exact guards and root approval',
        'own_reviewed_nine_guard_input':bind('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_guards.json','ae194e11ea5e9710504e27fab0a87ce7552ba2396cd2a17c24d9d0f2b019521b','Own ten-key primary-source dispositions and nine proposed entry replacements.')},
      'type_workflows':type_workflows,
      'future_dossier_required_top_level_fields':['source_sha256','pdf_sha256','defect_log_sha256','defect_log_content_sha256','rows','all_types_source_clear'],
      'future_per_type_required_fields':['type_id','status','evidence','remaining_dependencies','remaining_content_issues','source_clear_in_recorded_review_scope','exact_applied_guard_resolutions'],
      'future_generation_sequence':[
        'Read final root-approved consolidated guard files and declared supersessions; retain every original source/PDF/evidence hash.',
        'After canonical application, verify the applied receipt, all exact forward/inverse offsets, all merged full-block and full-entry archives, retained scope witnesses, and stable log edit-content/type associations.',
        'After candidate18 build, bind its actual source/PDF hashes and clean build diagnostics. Do not insert a projected source hash or guessed page count into a dossier.',
        'Transport each of the25 prior contextual dispositions and compare each named current finding with its exact applied complete block/entry. Include associated D12 evidence for the scope deletion and the reference-order relocation qualification.',
        'For bibliographic additions, compare parsed complete entry boundaries. Old entry text may remain a prefix after a DOI append, and a bare arXiv URL is a prefix of its versioned URL; absence of literal old substrings is not the closure test.',
        'Set source-clear true only for each individually supported row with no confirmed remaining content issue. Then derive all_types_source_clear from all25 rows. Keep actual changed-page reading/provenance/map-hash dependencies explicit and separate.',
        'Save a new immutable candidate18 preparation and type associations; preserve every completed candidate17 reading, audit and dossier hash. Root alone updates canonical individual status.',
      ],
      'protected_candidate17_file_hashes':protected,'canonical_files_modified':False,'new_page_credit':0,'new_mathematical_events':0}
    for p,h in protected.items():assert sha((ROOT/p).read_bytes())==h
    p=OUT/'S6_SERIES_PUBLISH_I_candidate18_type_closure_workflow.json'
    assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    md=['# Paper I — candidate18 closure workflow','',
      'This workflow is bound to frozen candidate17. Candidate18 source and PDF fields remain unset; no candidate18 dossier or new type closure is asserted. Eight categories are open: D02, D08, D09, D11, D12, D13, D18 and D23. The other17 retain their individually reviewed prior scopes.','',
      'The workflow verifies all64 root-approved body substitutions forward and backward, matches the reviewed body proposal hash, and binds the three complete context-disposition receipts (all155 first-person and19 Here/completeness/clarity contexts), the editor’s verification/data scope, the four completed candidate17 reading files, all345 current whole-image coverage and root’s additional substantive/scope reviews.','',
      '| Type | Current status | Approved body guards to resolve |','|---|---|---:|']
    for x in type_workflows:md.append(f"| {x['type_id']} | {'Open' if x['type_id'] in OPEN else 'Prior individual closure retained'} | {len(x['approved_pending_body_guards'])} |")
    md+=['','## Required next bindings','',
      'Infrastructure’s consolidated117-entry bibliography audit and final guard set must be approved and applied with the body batch. After the actual source application and clean PDF build, the new dossier will carry per-type exact block/entry resolutions, source/PDF/log hashes and stable type/edit associations. Whole-image reading, provenance and the final mapped-log hash remain distinct certification gates.','',
      'The convention relocation changes reference order. The repeated-scope deletion removes one duplicate inline symbol and one duplicate reference, with exact retained witnesses. Bibliographic DOI appends can retain the old entry text as a prefix; complete-entry comparison is therefore required. None of these operations adds a mathematical event or page-reading credit.','']
    p.with_suffix('.md').write_text('\n'.join(md))
    print(json.dumps({'workflow':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'types':25,'open_types':OPEN,
      'body_guards':64,'context_counts':[155,19,91],'candidate18_dossier_frozen':False,'canonical_files_modified':False},indent=2))

if __name__=='__main__':main()

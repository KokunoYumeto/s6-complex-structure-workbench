#!/usr/bin/env python3
"""Bind all 25 source dispositions after the approved 48-edit batch.

This preparation carries the recorded review scopes; it grants no new page or
mathematical-check credit and never changes canonical type status.
"""
from pathlib import Path
import collections
import copy
import csv
import datetime
import hashlib
import io
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
SOURCE_SHA='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF_SHA='3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
BASE_SHA='26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e'
CORE=['change_id','type','statement_id','old_text','new_text','reason']
sha=lambda b:hashlib.sha256(b).hexdigest()
csv.field_size_limit(100_000_000)


def read(p):return json.loads((ROOT/p).read_text())


def ev(p,scope,expected=None):
    h=sha((ROOT/p).read_bytes())
    if expected:assert h==expected,(p,h,expected)
    return {'path':p,'sha256':h,'scope':scope}


def core_hash(rows):
    data={'fields':CORE,'rows':[[r[k] for k in CORE] for r in rows]}
    return sha((json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n').encode())


NEW_REVIEWS={
'D08': 'The 33 D08 associations in the latest 48-row batch are applied, including the D08/D13 relocation. Their exact source replacements match all complete owning blocks. This resolves every named root/editing/provenance announcement and recap, including I16-prov-19 at the closing-translation proof. The provenance audit actually read 164 broader roadmap/compute contexts and three final recap contexts; its retained rows describe mathematical uses, necessary inputs or permitted abstract/table text. The original bounded 190 D08/58 D09 correspondence expressly reopened rows 70 and 127; both guards are applied. The two candidate15 visual discoveries and their earlier repairs remain bound. The source disposition rests on these contextual readings, the complete candidate16 page reading, and the exact applied block comparisons; it is not inferred from keyword absence. No further confirmed D08 source issue remains in those combined review scopes.',
'D13': 'I16-edits-11r1 is applied as a D08/D13 row. The curve/conjugation convention and its numbered reference move verbatim from the unnumbered Section 26.6 preface to inside ari:C.7.11 immediately after StatementRecord. The proposition\'s existing first sentence, all hypotheses/formulas and complete proof remain. Its reference order changes exactly as documented; command/reference multisets, mathematical segments and labels/targets are preserved. The exact relocation resolves the single reopened D13 locus while retaining its input. The 42 inherited input-placement comparisons remain transported to this source.',
'D18': 'The seven final full-entry bibliography guards are applied and explicitly supersede both earlier URL-only and intermediate metadata proposals. They retain all 117 citation keys and the byte-matched cited arXiv editions. Four entries include the checked journal/volume/pages/year and existing doi macro; three retain the verified preprint editions without an unsupported publication claim. The author-year labels for DMM16, Dloussky2005AB and EH2024E change to their documented journal years, with the cited-edition page/statement numbering stated separately. All original/proposed entry and primary version/publisher evidence hashes are bound. Together with the 13 earlier metadata repairs and inherited bibliography review, no further confirmed D18 source issue remains in the recorded scope. The final rendered citations and page flow retain their separate reading gate.',
'D23': 'All eight exact Cech-to-caron guards are applied in their complete owning statements/proofs. Every mathematical segment and label/target/reference is preserved; the changes restore the established TeX accent spelling only. These resolve every D23 instance named in the frozen candidate16 findings and reopening record. The earlier Poincare/etale/citation-grammar, diagram, heading and QED repairs remain transported. The candidate17 build reports zero overfull boxes, undefined references/citations or missing glyphs/fonts. Actual reading of the changed candidate17 whole images is a distinct remaining gate.'
}


def main():
    old_path='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_type_closure_preparation.json'
    old_e=ev(old_path,'Immutable individual candidate16 scopes and pending findings.','0b77945c49f60963e2c96fff0eaef6c4c31c1107c02fbe326054fc2d4c0e2a35');old=read(old_path)
    receipt_path='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_combined_apply_receipt.json'
    receipt_e=ev(receipt_path,'Applied 48 exact guards, 37 complete blocks, supersessions and declared reference relocation.','8947b7e89114276fd82e808c1cd5e329dd0000af5ac827f82e8b6f0bb65b9a9d');receipt=read(receipt_path)
    s_path=ROOT/'S6_SERIES_PUBLISH_I.tex';s_bytes=s_path.read_bytes();s=s_bytes.decode();assert sha(s_bytes)==SOURCE_SHA==receipt['after_source_sha256']
    l_path=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv';l_bytes=l_path.read_bytes();log=list(csv.DictReader(io.StringIO(l_bytes.decode()),delimiter='\t'));assert len(log)==2087
    assert core_hash(log[:2039])==old['defect_log_content_sha256']
    all_changes=old['source_transport']['applied_changes']+[{**c,'receipt':receipt_path} for c in receipt['changes']]
    assert len(all_changes)==134 and len(receipt['changes'])==48
    base=(ROOT.parent/'S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex').read_text();assert sha(base.encode())==BASE_SHA
    t=base
    for c in all_changes:
        p=c['applied_offset'];assert t[p:p+len(c['old'])]==c['old'];t=t[:p]+c['new']+t[p+len(c['old']):]
        r=log[int(c['change_id'].split('-')[1])-1]
        assert [r[k] for k in ['type','statement_id','old_text','new_text','reason']]==[c[k] for k in ['type','statement_id','old','new','reason']]
    assert t==s
    for c in reversed(all_changes):
        p=c['applied_offset'];assert t[p:p+len(c['new'])]==c['new'];t=t[:p]+c['old']+t[p+len(c['new']):]
    assert t==base
    blocks=[];by_guard={}
    for a in receipt['archives']:
        for key in ['original','proposed','diff']:assert sha((ROOT/a[key]).read_bytes())==a[key+'_sha256']
        b=(ROOT/a['proposed']).read_text();assert s.count(b)==1
        binding={**a,'current_source_start_line':s[:s.index(b)].count('\n')+1,'current_complete_block_exact_match':True};blocks.append(binding)
        for gid in a['guard_ids']:by_guard[gid]=binding
    assert len(blocks)==37
    for p,h in receipt['immutable_reading_and_dossier_records'].items():assert sha((ROOT/p).read_bytes())==h
    for e in old['inherited_evidence_files_verified']:assert sha((ROOT/e['path']).read_bytes())==e['sha256']
    ledger_sha=sha((ROOT/'CHECK_EVENTS.tsv').read_bytes());assert ledger_sha==receipt['check_ledger_sha256']==old['check_ledger_sha256']
    build_path='build/I_candidate17/build_summary.json';build=read(build_path)
    assert (build['source_sha256'],build['pdf_sha256'])==(SOURCE_SHA,PDF_SHA)
    for key in ['overfull_total','overfull_above_2pt','undefined_references','undefined_citations','missing_characters','missing_fonts','multiply_defined','duplicate_destinations']:assert build[key]==0
    assert sha((ROOT/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf').read_bytes())==PDF_SHA
    ag_path='records/S6_SERIES_PUBLISH_I_candidate17_source_AG_binding.json';ag=read(ag_path)
    assert ag['source_sha256']==SOURCE_SHA and len(ag['exact_edits'])==134 and ag['source_exact_forward_and_inverse_maps_verified']
    assert len(ag['headlines'])==7 and sum(x['outline_items'] for x in ag['headlines'].values())==40
    current_evidence=[old_e,receipt_e,ev(build_path,'Clean candidate17 exact source/PDF binding.'),ev(ag_path,'Current 134-edit map and unchanged seven headlines/40 outline items/80 scoped block associations.'),ev('records/S6_SERIES_PUBLISH_I_candidate16_type_progress.json','Root individually reviewed all25 candidate16 rows and closed21, leaving four named categories.','81c94964c4c1c2a7b537f8b57123e11137a98bf6771558804e892a6c1bb27677')]
    context_evidence=[ev('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_D08_D09_dispositions.json','Actual bounded correspondence with explicit rows70/127 reopenings.','a6bf9e2580dc34dda0694054601c5069a2d8290d3d754b96e318ea58e585ca81'),ev('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_D08_expanded_dispositions.json','All164 broader contexts actually read and individually disposed.','5fd78788b1f65e1ce3962aa5b5844b30d6b2d408fec0f257179869e5398eda3e'),ev('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_D08_recap_dispositions.json','All3 final recap contexts read; one exact repair now applied.','981286a875da088647b068694e63d6760b6d9af1f911224bf1b965239f9ef769')]
    applied_ids={c['guard_id'] for c in receipt['changes']};rows=[];associations=[]
    for prior in old['rows']:
        typ=prior['type_id'];r=copy.deepcopy(prior);selected=[x for x in log if typ in re.findall(r'D\d\d',x['type'])]
        new=[c for c in receipt['changes'] if typ in re.findall(r'D\d\d',c['type'])]
        for issue in prior['remaining_content_issues']:assert issue['guard_id'] in applied_ids,(typ,issue)
        resolutions=[]
        for c in new:
            b=by_guard[c['guard_id']]
            resolutions.append({'guard_id':c['guard_id'],'change_id':c['change_id'],'type':c['type'],'statement_id':c['statement_id'],'old_text_sha256':sha(c['old'].encode()),'new_text_sha256':sha(c['new'].encode()),'current_complete_block':b['proposed'],'current_complete_block_sha256':b['proposed_sha256'],'current_source_start_line':b['current_source_start_line'],'exact_current_replacement_verified':True,'inline_and_display_math_preserved':True,'reference_order_relocation':c['declared_reference_order_change']})
        continuation=[c for c in all_changes if typ in re.findall(r'D\d\d',c['type'])]
        r.update({'status':'source_clear_pending_final_render_and_provenance_binding','source_clear_in_recorded_review_scope':True,
          'proposed_disposition':'All individually confirmed source instances in the inherited contextual, complete-page and full-block review scopes are resolved and logged. Root may close this source type under rule0.3; final current-page/provenance/map bindings remain separate.',
          'candidate16_source_review_as_recorded':prior['source_review'],'source_review':NEW_REVIEWS.get(typ,prior['source_review']+' The exact 48-edit candidate16-to17 map preserves the compared content and all operative mathematical segments; the current clean build and 134-edit A–G binding carry this source disposition forward. No new confirmed content issue of this type was reported by the subsequent contextual reviews.'),
          'candidate16_pending_issues_as_recorded':prior['remaining_content_issues'],'remaining_content_issues':[],
          'current_edit_associations':len(selected),'continuation_edit_associations':len(continuation),'edit_ids':[x['change_id'] for x in selected],'continuation_edit_ids':[c['change_id'] for c in continuation],
          'edit_content_sha256':core_hash(selected),'applied_candidate16_guard_resolutions':resolutions,
          'remaining_dependencies':['Complete actual reading of every changed candidate17 whole image; unchanged whole-image inheritance must match its hash.','Bind final source/PDF/check-ledger provenance and the42 source/report/deposit claims.','Finalize defect-page mapping and bind the full log hash while preserving this stable edit-content/type association hash.'],
          'new_page_credit':0,'mathematical_events_added':0})
        r['evidence']+=current_evidence
        if typ in ['D08','D09']:r['evidence']+=context_evidence
        for x in selected:associations.append({'type_id':typ,'change_id':x['change_id'],'statement_id':x['statement_id'],'origin':'inherited candidate13' if int(x['change_id'].split('-')[1])<=1953 else 'continuation'})
        rows.append(r)
    assert len(rows)==25 and len(associations)==2181 and all(x['source_clear_in_recorded_review_scope'] for x in rows)
    association_path=OUT/'S6_SERIES_PUBLISH_I_candidate17_type_associations.tsv'
    with association_path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['type_id','change_id','statement_id','origin'],delimiter='\t');w.writeheader();w.writerows(associations)
    result={'schema':3,'paper':'I','candidate':'I_candidate17','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'defect_log_sha256':sha(l_bytes),'defect_log_content_sha256':core_hash(log),'defect_log_content_hash_specification':old['defect_log_content_hash_specification'],
      'source_path':'S6_SERIES_PUBLISH_I.tex','pdf_path':'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf','defect_log_path':'S6_SERIES_PUBLISH_defects_I.tsv',
      'defect_type_associations':{'path':str(association_path.relative_to(ROOT)),'sha256':sha(association_path.read_bytes()),'count':2181},
      'unique_edit_rows':2087,'inherited_unique_edit_rows':1953,'continuation_unique_edit_rows':134,'latest_applied_guards':48,'inherited_edit_type_associations':2046,'edit_type_associations':2181,'count_semantics':old['count_semantics'],
      'all_types_source_clear':True,'source_clear_scope':'Each of the25 rows carries its individual inspected contexts and complete comparison receipts. All named candidate16 findings are now applied and logged; the current source exactly matches every latest complete block. This source disposition is independent of the still-open changed-page/provenance/map gates and is not inferred from keyword absence.',
      'final_certified':False,'canonical_status_modified':False,'mathematical_events_added':0,'new_page_credit':0,
      'prior_immutable_dossier':old_e,'applied_batch':receipt_e,'source_transport':{'baseline_source_sha256':BASE_SHA,'current_source_sha256':SOURCE_SHA,'exact_forward_and_inverse_reconstruction':True,'applied_changes':all_changes,'latest_complete_blocks_verified':blocks},
      'immutable_reading_and_dossier_records_verified':receipt['immutable_reading_and_dossier_records'],'inherited_evidence_files_verified':old['inherited_evidence_files_verified'],
      'check_ledger_sha256':ledger_sha,'current_build':current_evidence[2],'current_AG_binding':current_evidence[3],'contextual_reviews':context_evidence,
      'bibliography_supersessions':receipt['bibliography_declared_supersessions'],'declared_reference_relocation':receipt['declared_reference_relocation'],
      'rows':rows,'remaining_dependencies':['Actual reading of every changed candidate17 full image','Final current-source/PDF/provenance binding','Final defect-page map and full log hash'],
      'limitations':['No new independent proof, mathematical event or full-page reading is credited by this source dossier.','Actual future image reading can reopen a source type for a newly confirmed instance.','Root owns the canonical individual closure/status and final Paper I gate.']}
    assert s_path.read_bytes()==s_bytes and l_path.read_bytes()==l_bytes and sha((ROOT/'CHECK_EVENTS.tsv').read_bytes())==ledger_sha
    p=OUT/'S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json';p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    md=['# Paper I candidate17 — 25 individual source dispositions','',f'Source SHA-256: `{SOURCE_SHA}`','',f'PDF SHA-256: `{PDF_SHA}`','',f"Defect-log SHA-256: `{result['defect_log_sha256']}`",'',f"Stable edit-content SHA-256: `{result['defect_log_content_sha256']}`",'',f"Type-association SHA-256: `{result['defect_type_associations']['sha256']}`",'',
      'All 25 source dispositions are clear in their recorded contextual, complete-page and full-block review scopes. Every named candidate16 finding is resolved by the 48 applied guards and logged. This preparation does not close the distinct candidate17 changed-page, provenance or final mapping gates. Root controls canonical status.','',
      'The log has 2,087 unique edit rows and 2,181 type associations. All 134 continuation changes reconstruct the source forward and backward to the immutable base. All 37 latest complete blocks match current source. All protected readings/dossiers, 57 inherited evidence files and the mathematical-check ledger retain their hashes. There are zero new page-reading or mathematical-event credits.','','| Type | Current associations | Latest applied guards | Source disposition |','|---|---:|---:|---|']
    for r in rows:md.append(f"| {r['type_id']} | {r['current_edit_associations']} | {len(r['applied_candidate16_guard_resolutions'])} | Clear in recorded review scope; final bindings pending |")
    for r in rows:md += ['',f"## {r['type_id']} — {r['defect']}",'',r['source_review'],'','Latest exact repair rows: '+(', '.join(x['change_id'] for x in r['applied_candidate16_guard_resolutions']) or 'none; prior disposition transported')+'.']
    md += ['','## Remaining gates','','Every changed candidate17 complete image must be actually read. Final source/PDF/provenance and mapped-log bindings remain explicit; source-type closure does not award those page or provenance credits.','']
    p.with_suffix('.md').write_text('\n'.join(md))
    print(json.dumps({'dossier':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'defect_log_sha256':sha(l_bytes),'defect_log_content_sha256':core_hash(log),'type_association_sha256':sha(association_path.read_bytes()),'types':25,'edit_rows':2087,'type_associations':2181,'all_types_source_clear':True,'final_certified':False,'mathematical_events_added':0},indent=2))

if __name__=='__main__':main()

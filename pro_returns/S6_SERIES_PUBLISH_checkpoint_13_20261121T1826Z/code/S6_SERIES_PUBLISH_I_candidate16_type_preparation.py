#!/usr/bin/env python3
"""Prepare individual candidate16 dispositions; never mutate canonical status."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
SOURCE_SHA = "61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc"
PDF_SHA = "4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2"
BASE_SHA = "26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e"
CORE = ["change_id", "type", "statement_id", "old_text", "new_text", "reason"]
sha = lambda b: hashlib.sha256(b).hexdigest()
csv.field_size_limit(100_000_000)


def read(path): return json.loads((ROOT / path).read_text())


def relocate(path):
    prefix = "/workspace/scratch/653608133b22/work/"
    if path.startswith(prefix): return path[len(prefix):]
    p = Path(path)
    return str(p.relative_to(ROOT)) if p.is_absolute() else path


def evidence(path, scope, expected=None, kind="continuation"):
    p = relocate(path)
    h = sha((ROOT / p).read_bytes())
    if expected is not None: assert h == expected, (p,h,expected)
    return {"path":p,"sha256":h,"scope":scope,"kind":kind}


def core_hash(rows):
    data = {"fields":CORE,"rows":[[r[k] for k in CORE] for r in rows]}
    return sha((json.dumps(data,ensure_ascii=False,separators=(",",":"))+"\n").encode())


REVIEW = {
"D01":"Root's 145 actual D01 context dispositions distinguish the specified geometric original data, historical editions, published corrections and required methodology. The three additional own-history passages found on candidate15 were applied as I-02020, I-02021 and I-02022. The exact combined replacement blocks preserve the mathematical comparison, external dates and citations. Candidate16 full-page coverage supplies the corresponding rendered reading. No further D01 content issue is reported in those actual readings and current context records.",
"D02":"The ten earlier continuation repairs and 23 candidate15 D02 repairs are fully logged. The combined original/replacement statements and proofs retain the positive multiplicity, pencil, finite-height, twist, period, degree, local-coordinate, extension and derivative hypotheses and all operative maps. The current complete images include those applied passages. Actual mathematical negative conclusions about Hom, isogeny/subtorus obstructions and the spectral gap retain their explicit arguments; they are not deleted as defensive prose. No further D02 defect was confirmed in the candidate16 reading reports.",
"D03":"The inherited comparison and candidate13 page140 reading identify the repaired concrete pair (0,0),(0,-3i) and its exact line-plus-period argument. The source reconstruction carries that entire block to candidate16 without another change; whole-image equality or current actual reading supplies each current page's coverage. No continuation edit creates a numbered statement whose purpose is an internal-prompt refutation.",
"D04":"The inherited 27 associations supply the numbered local statements, equations and exact opened primary locators. The 86-edit reconstruction introduces only the recorded citation-form and records-link changes; candidate16 has zero unresolved references or citations. The actual-page reports do not identify a remaining internal run label as a printed reference.",
"D05":"Root's three actual D05 context dispositions identify mathematical requirements, while the inherited complete family/Hodge comparisons supply the positive definitions replacing requests. None of the 86 literal changes introduces a prompt item as an object or reference, and the final candidate16 readings report no new D05 instance.",
"D06":"The old duplicate aliases and the coherent-descent/classification receiving aliases retain their recorded repairs. The current auxiliary file resolves I:coherent-descent-proof and fam:src:A.3.1 to 7.5 and app:rederive:fam-src-A.5.1 and fam:src:A.5.1 to 7.8. The ordered labels, targets and citation/reference commands survive the full source transport; the current build reports no duplicate destinations or multiply defined references.",
"D07":"The inherited positive occurrence review locates model names in the required methodology and Claude–Alpoge in the cited work. The CurrentChecker macro remains an unused preamble definition, while StatementRecord prints only the permanent tag. No worker/run attribution was introduced by the exact continuation changes, and current actual-page reading reports no such printed mathematics. The zero D07 edit count is not used as an absence test.",
"D08":"The original 432 associations and the bounded 192-context audit retain their historical scopes. Candidate15 actual-page findings I15-prov-04 and I15-prov-12 superseded the former bounded source-clear conclusion; they were applied as I-02017 and I-02025, and both reopening receipts are preserved. Candidate16 actual-page reading has now found further announcements and recaps, with separate exact guards from root, edits and provenance readers. D08 remains open; the broadened contextual audit and consolidated approved application are dependencies. Keyword occurrence equality is not global absence evidence.",
"D09":"The inherited 190 associations retain the complete computational method/input/result descriptions and the authenticated 78-link program table. The 58 filename-pattern contexts in the bounded candidate14/15 audit occur in that allowed table; those two recorded counts have different scopes. The 86-change map preserves those method descriptions and table entries, and current complete-page coverage includes the table. A candidate16 contextual/provenance rebind remains explicit rather than inferred from an unchanged count.",
"D10":"The exact current StatementRecord macro prints only its small permanent tag. Its 119 inherited apparatus associations and full comparisons remain, and the 86-edit transport preserves 925 labels, 598 tag targets and 668 targets in order. The current printed pages provide the layout evidence; the retained source metadata is not printed by that macro.",
"D11":"The earlier Chabauty and tangent-splitting clauses and all nine candidate15 D11 clauses are applied with complete before/after comparisons. The exact analytic BSD quotient, lift criterion, constant scope, rank/period and Gaussian claims remain. The already-existing final-part Tate–Shafarevich and norm questions are preserved, with their exact source loci recorded; no new open question was introduced. Current full-page reading reports no additional D11 defect. Positive recaps newly found on candidate16 are recorded under D08.",
"D12":"The inherited common-family, canonical-ring, tangent and automorphism consolidation comparisons retain their complete scopes and aliases. The exact 86-edit source map and all 36 latest replacement blocks show no statement or proof duplicated. The current A–G record transports 80 archived block associations and keeps all seven headlines and 40 outline items identical.",
"D13":"The inherited 42 associations retain their original complete comparison scopes. Candidate16's Section 26.6 preface leaves its curve/conjugation convention outside the numbered proposition. Root explicitly reopened D13 for this locus. Revised guard I16-edits-11r1 (D08/D13) moves the exact retained convention and reference after StatementRecord inside ari:C.7.11 and deletes only the roadmap. Its mathematical segments and command/reference multisets are preserved; the changed command/reference order is documented honestly. This pending relocation keeps D13 open.",
"D14":"The inherited construction-before-use order, coherent-family/classification placement and early cusp/residue inputs remain. None of the 86 literal changes moves a section or mathematical block. Current full-page coverage and the seven-headline/40-outline/80-block A–G binding support the recorded order and scope; no new order/proportion issue was reported.",
"D15":"The three §1.5 continuation edits give the 21 November 2026 continuation and GPT-6 Astra, ChatGPT Pro mode wording without an invented numerical effort. A single publication-records macro/link replaces the accompanying-source claim. The headline, abstract/outline and known/new structure retain their inherited comparisons; current source/PDF reading is complete. The separate 42-claim source/deposit/records provenance binding remains an explicit final gate.",
"D16":"The inherited 112 title associations remain. I15-prov-07, logged historically as D01 in I-02020, also resolves the Appendix A title issue by replacing process/history wording with the positive period/deformation comparison title. Its complete block preserves the mathematical content and credit. This cross-type evidentiary association does not retag the original log row. Current actual-page reading reports no additional D16 title issue.",
"D17":"The four inherited exact-source-locator repairs retain the documented receiving matrix, characteristic-zero, parameter, measure and convergence identifications. The specifically credited re-derived appendices remain with their exact historical source comparison. The 86-edit map introduces no additional proof of a known result or new independent-check claim.",
"D18":"The prior Buchdahl locator and single publication-records macro repairs remain, and the 13 candidate15 bibliography/citation metadata guards were applied as I-02027–I-02039. Complete entries retain 117 bibliography keys and body locators, with publisher/DOI and field-format changes archived. Candidate16 contextual review has identified seven unversioned arXiv URLs with exact primary-source version bindings. These pending guards keep D18 open. The checkpoint10 records pin remains the user-specified interim deposit pin.",
"D19":"The inherited 331 equation associations retain their original/current anchor maps. The current source keeps numberwithin{equation}{section}; the ordered labels and targets are preserved through all 86 changes, with no equation environment or numbering declaration altered. The clean build and actual pages supply current reference and display evidence.",
"D20":"The eight inherited differential/lattice, invariant-pushforward, frame-transport and trace-sign comparisons retain their exact maps. No continuation edit changes a value or introduces another normalization. The newest complete blocks explicitly preserve the operative maps and conventions; the current global source binding transports the earlier scoped mathematical evidence without a new check claim.",
"D21":"The inherited exact squarefree-division-polynomial/degree torsion-count replacement retains its full comparison. No continuation change promotes numerical agreement to a theorem. Directed enclosures and rational separation remain stated with their actual bounds and derivations in the current arithmetic pages; typography/reading carries zero mathematical-event credit.",
"D22":"The three inherited explanations retain the toric fixed/character loci, 2pi-i chain map and twelve-term scalar-period computation. The full source transport leaves their values, choices and conversion formulas in place. The actual current arithmetic pages retain the explicit reasons for the local coordinate, field, cutoffs and period choices; no new unexplained choice was identified.",
"D23":"The seven earlier continuation typography repairs and twelve candidate15 accent/citation-grammar repairs are applied. Current actual-page coverage confirms the resulting complete images. Root subsequently identified eight remaining plain Cech spellings in exact source contexts; those independently documented D23 findings keep this type open until their approved accent repairs and changed-image reading. The historical heading, QED and diagram repairs remain preserved.",
"D24":"The inherited supplying/receiving and known/new comparisons remain. The candidate16 A–G binding verifies all 86 exact edits, unchanged seven headline statements and 40 outline items, and 80 archived block associations. The actual current contents/introductory pages are covered. No new introduction/body mismatch was reported in that scoped reading and comparison.",
"D25":"The 17 inherited type associations retain their exact error/completion scopes: lattice boundary point, logarithm clause, radial ratio, selected cusp diagonal, component resolution and Gross auxiliary-field hypotheses. The historical refuted clause and refined identifier remain in the unchanged ledger. The 86 literal continuation edits and current actual-page readings create no new theorem-error or independent mathematical-check claim; the exact source/global binding transports the previously recorded proof evidence."
}


def main():
    source_path=ROOT/'S6_SERIES_PUBLISH_I.tex';source_bytes=source_path.read_bytes();s=source_bytes.decode()
    assert sha(source_bytes)==SOURCE_SHA
    log_path=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv';log_bytes=log_path.read_bytes()
    log=list(csv.DictReader(io.StringIO(log_bytes.decode()),delimiter='\t'))
    assert len(log)==2039
    old_path='agents/i_provenance/S6_SERIES_PUBLISH_I_defect_type_closure_evidence.json';old=read(old_path)
    snapshot_path='records/S6_SERIES_PUBLISH_I_candidate15_type_dossier_snapshot.json';snapshot=read(snapshot_path)
    inherited=list(csv.DictReader(io.StringIO((ROOT/relocate(old['defect_log']['snapshot'])).read_text()),delimiter='\t'))
    assert len(inherited)==1953
    assert [[r[k] for k in CORE] for r in inherited]==[[r[k] for k in CORE] for r in log[:1953]]
    assert core_hash(log[:1977])==snapshot['defect_log_content_sha256']
    receipts=[
        'agents/i_cont_edits/S6_SERIES_PUBLISH_I_continuation_edits_receipt.json',
        'agents/i_cont_edits/S6_SERIES_PUBLISH_I_continuation_residue_receipt.json',
        'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate14_residue_receipt.json',
        'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate15_combined_apply_receipt.json']
    baseline=(ROOT.parent/'S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex').read_text()
    assert sha(baseline.encode())==BASE_SHA
    current=baseline;changes=[];receipt_evidence=[]
    for path in receipts:
        d=read(path);assert sha(current.encode())==d['before_source_sha256']
        for c in d['changes']:
            p=c['applied_offset'];assert current[p:p+len(c['old'])]==c['old']
            current=current[:p]+c['new']+current[p+len(c['old']):]
            row=log[int(c['change_id'].split('-')[1])-1]
            assert [row[k] for k in ['type','statement_id','old_text','new_text','reason']]==[c[k] for k in ['type','statement_id','old','new','reason']]
            changes.append({**c,'receipt':path})
        assert sha(current.encode())==d['after_source_sha256']
        receipt_evidence.append(evidence(path,'Applied exact literal maps, full-block comparisons, and unchanged check-ledger scope.'))
    assert current==s and len(changes)==86
    reverse=s
    for c in reversed(changes):
        p=c['applied_offset'];assert reverse[p:p+len(c['new'])]==c['new']
        reverse=reverse[:p]+c['old']+reverse[p+len(c['new']):]
    assert reverse==baseline
    combined=read(receipts[-1]);block_by_guard={};verified_blocks=[]
    for a in combined['archives']:
        for kind in ['original','proposed','diff']:
            assert sha((ROOT/a[kind]).read_bytes())==a[kind+'_sha256']
        proposed=(ROOT/a['proposed']).read_text();assert s.count(proposed)==1
        binding={**a,'current_source_start_line':s[:s.index(proposed)].count('\n')+1,'current_complete_block_matches_archive':True}
        verified_blocks.append(binding)
        for gid in a['guard_ids']:block_by_guard[gid]=binding
    assert len(verified_blocks)==36
    pdf_path='build/I_candidate16/S6_SERIES_PUBLISH_I.pdf';assert sha((ROOT/pdf_path).read_bytes())==PDF_SHA
    build_path='build/I_candidate16/build_summary.json';build=read(build_path)
    assert (build['source_sha256'],build['pdf_sha256'])==(SOURCE_SHA,PDF_SHA)
    for k in ['overfull_total','overfull_above_2pt','undefined_references','undefined_citations','missing_characters','missing_fonts','multiply_defined','duplicate_destinations']:assert build[k]==0
    assert build['shell_escape'] is False
    coverage_path='records/S6_SERIES_PUBLISH_I_candidate16_complete_coverage_snapshot.json';coverage=read(coverage_path)
    assert (coverage['source_sha256'],coverage['pdf_sha256'],coverage['covered_pages'],coverage['page_count'])==(SOURCE_SHA,PDF_SHA,346,346)
    assert coverage['all_pages_read'] and not coverage['missing_pages']
    reading_refs={}
    for r in coverage['pages']:
        assert sha((ROOT/f"render/I_candidate16/page_{r['page']:03d}.png").read_bytes())==r['image_sha256']
        reading_refs[r['reading_record']]=r['reading_record_sha256']
    for path,h in reading_refs.items():assert sha((ROOT/path).read_bytes())==h
    assert sha((ROOT/'render/I_candidate16/manifest.json').read_bytes())==coverage['render_manifest_sha256']
    ag_path='records/S6_SERIES_PUBLISH_I_candidate16_source_AG_binding.json';ag=read(ag_path)
    assert ag['source_sha256']==SOURCE_SHA and len(ag['exact_edits'])==86
    assert len(ag['headlines'])==7 and sum(x['outline_items'] for x in ag['headlines'].values())==40
    assert ag['source_exact_forward_and_inverse_maps_verified']
    events_sha=sha((ROOT/'CHECK_EVENTS.tsv').read_bytes());assert events_sha==combined['check_ledger_sha256']==ag['ledger_sha256']
    assert r'\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}' in s
    assert s.count(r'\CurrentChecker')==1 and s.count(r'\newcommand{\SsixPublishRecords}')==s.count(r'\href{\SsixPublishRecords}')==1
    assert r'\numberwithin{equation}{section}' in s
    aux=(ROOT/'build/I_candidate16/S6_SERIES_PUBLISH_I.aux').read_text()
    for label,n in [('I:coherent-descent-proof','7.5'),('fam:src:A.3.1','7.5'),('app:rederive:fam-src-A.5.1','7.8'),('fam:src:A.5.1','7.8')]:assert r'\newlabel{'+label+'}{{'+n+'}' in aux
    for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}']:assert re.findall(pat,s)==re.findall(pat,baseline)
    reopening_path='records/S6_SERIES_PUBLISH_I_candidate15_D08_reopen.json';reopening=read(reopening_path)
    pending=collections.defaultdict(list);pending_files=[]
    guard_paths=['agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_root_guards.json','agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_edits_guards.json','agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_edits_guard11_revision.json','agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json','agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_expanded_guards.json','agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_Cech_guards.json','agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate16_infra_D18_guards.json']
    for path in guard_paths:
        datum=read(path);gs=datum if isinstance(datum,list) else datum['guards']
        gs=[g for g in gs if g['id']!='I16-edits-11']
        ev=evidence(path,'Pending exact candidate16 guards; no applied-edit credit.','' or None,'pending source guards');pending_files.append({**ev,'guards':len(gs)})
        for g in gs:
            assert g.get('source_sha256',SOURCE_SHA)==SOURCE_SHA
            assert s.count(g.get('before',g.get('old','')))==1
            for typ in re.findall(r'D\d\d',g['type']):pending[typ].append({'guard_id':g['id'],'page':g.get('page'),'statement_id':g.get('statement_id'),'guard_file':path,'guard_file_sha256':ev['sha256'],'status':'pending consolidated reviewed application'})
    accents_path='records/S6_SERIES_PUBLISH_I_candidate16_D23_accent_findings.json';accents=read(accents_path)
    assert accents['source_sha256']==SOURCE_SHA and len(accents['findings'])==8
    assert len(pending['D23'])==8
    shared=[evidence(old_path,'Original 25 individual inspected scopes, exact old edits and comparison evidence.','' or None,'inherited dossier'),evidence(snapshot_path,'Immutable candidate15 dossier; historical flags remain, superseded by the explicit reopening and applied guards.','' or None,'historical snapshot'),evidence('agents/i_provenance/S6_SERIES_PUBLISH_I_defect_type_candidate13_addendum.json','Candidate13 actual late-page findings and their inherited dispositions.'),evidence(coverage_path,'All 346 current images covered; all image and 15 referenced reading hashes verified.','' or None,'actual coverage'),evidence(build_path,'Current clean source/PDF build.','' or None,'build')]+receipt_evidence
    verified_inherited={};rows=[];associations=[]
    for oldrow in old['types']:
        typ=oldrow['type_id'];selected=[r for r in log if typ in re.findall(r'D\d\d',r['type'])]
        new=[c for c in changes if typ in re.findall(r'D\d\d',c['type'])]
        ev=[]
        for x in oldrow['evidence']:
            e=evidence(x['path'],x.get('scope','Inherited scoped comparison'),x['sha256'],'inherited scoped review');ev.append(e);verified_inherited[e['path']]=e['sha256']
        ev+=shared
        if typ in ['D01','D02','D05','D11','D23']:ev.append(evidence('records/S6_SERIES_PUBLISH_I_continuation_root_residue_dispositions.json','155 actually inspected original contexts and one extra D11 replay hit.'))
        if typ in ['D08','D09']:
            ev.append(evidence('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_D08_D09_dispositions.json','Bounded 192/58 contextual audit; its D08 global inference is expressly superseded by later actual-page findings.'))
        if typ=='D08':
            ev.extend([evidence(reopening_path,'Root D08 reopening and preserved 18-type historical closed list.'),evidence('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_D08_reopening_receipt.json','Provenance D08 scope correction and applied guard association.')])
        if typ in ['D12','D14','D15','D24','D25']:ev.append(evidence(ag_path,'Current 86-edit map, seven headlines, 40 outline items and 80 scoped source-block associations.'))
        if typ=='D18':ev.append(evidence('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate16_arxiv_version_bindings.json','Primary-source version evidence for the seven still-pending URL repairs.'))
        if typ=='D13':ev.append(evidence('records/S6_SERIES_PUBLISH_I_candidate16_D13_reopen.json','Root reopening for the exact convention relocation into ari:C.7.11.'))
        if typ=='D23':
            ev.append(evidence(accents_path,'Eight actually located plain Cech spellings in frozen source.'))
            ev.append(evidence('records/S6_SERIES_PUBLISH_I_candidate16_D23_reopen.json','Root D23 reopening/pending accent disposition.'))
        for x in pending_files:
            if any(g.get('guard_file')==x['path'] for g in pending[typ]):ev.append(x)
        direct=[c for c in combined['changes'] if typ in re.findall(r'D\d\d',c['type'])]
        applied=[{'guard_id':c['guard_id'],'change_id':c['change_id'],'statement_id':c['statement_id'],'full_block':block_by_guard[c['guard_id']]['proposed'],'full_block_sha256':block_by_guard[c['guard_id']]['proposed_sha256'],'current_block_exact_match':True,'removed_inline_mentions_in_prose':c['removed_inline_mentions_in_prose']} for c in direct]
        cross=[]
        if typ=='D16':
            c=next(c for c in combined['changes'] if c['guard_id']=='I15-prov-07')
            cross=[{'guard_id':c['guard_id'],'change_id':c['change_id'],'logged_type':c['type'],'scope':'The positive Appendix A title also resolves D16; historical D01 taxonomy is preserved.','full_block':block_by_guard[c['guard_id']]['proposed'],'full_block_sha256':block_by_guard[c['guard_id']]['proposed_sha256']}]
        issues=pending[typ];clear=not issues
        deps=[]
        if issues:deps.append('Complete the named candidate16 guard review/application and retain every full-block or entry comparison.')
        if typ=='D08':deps.append('Complete the broadened D08 contextual audit, preserving the bounded scope of the earlier occurrence audit.')
        deps += ['Bind the final source/PDF/check ledger and provenance claims after the pending consolidated source changes.','Read every whole image changed by the next approved batch; candidate16 coverage itself is complete.','Finalize defect-page mapping and rebind the full log hash; preserve the separately recorded stable content and associations.']
        row={'type_id':typ,'class':oldrow['class'],'defect':oldrow['defect'],'required_fix':oldrow['required_fix'],
             'status':'source_clear_in_recorded_review_scope_pending_final_binding' if clear else 'open_candidate16_content_guards_pending',
             'source_clear_in_recorded_review_scope':clear,'source_review':REVIEW[typ],
             'proposed_disposition':'No further confirmed source issue in the combined inherited contextual, exact-replacement and actual current-page review scope; root controls canonical closure.' if clear else 'Keep open for the individually named current-source findings.',
             'prior_root_closed_at_candidate15':typ in reopening['types_still_closed_at_candidate15'],
             'inherited_inspected_scope':oldrow['inspected_scope'],'inherited_status_as_recorded':oldrow['status'],'inherited_remaining_as_recorded':oldrow['remaining'],
             'inherited_edit_associations':oldrow['edit_associations'],'continuation_edit_associations':len(new),'current_edit_associations':len(selected),
             'edit_ids':[r['change_id'] for r in selected],'continuation_edit_ids':[c['change_id'] for c in new],
             'edit_content_sha256':core_hash(selected),'applied_candidate15_guards':applied,'cross_type_applied_evidence':cross,
             'remaining_content_issues':issues,'evidence':ev,'remaining_dependencies':deps,'mathematical_events_added':0}
        rows.append(row)
        for r in selected:associations.append({'type_id':typ,'change_id':r['change_id'],'statement_id':r['statement_id'],'origin':'inherited candidate13' if int(r['change_id'].split('-')[1])<=1953 else 'continuation'})
    assert len(rows)==25 and len(verified_inherited)==57 and len(associations)==2132
    ap=OUT/'S6_SERIES_PUBLISH_I_candidate16_type_associations.tsv'
    with ap.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['type_id','change_id','statement_id','origin'],delimiter='\t');w.writeheader();w.writerows(associations)
    open_types=[r['type_id'] for r in rows if not r['source_clear_in_recorded_review_scope']]
    result={'schema':2,'paper':'I','candidate':'I_candidate16','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'defect_log_sha256':sha(log_bytes),'defect_log_content_sha256':core_hash(log),
            'defect_log_content_hash_specification':{'fields':CORE,'serialization':'UTF-8 JSON with keys fields then rows; row lists preserve log order; ensure_ascii=False, separators comma/colon, one final newline. Page/location/status fields excluded.'},
            'source_path':'S6_SERIES_PUBLISH_I.tex','pdf_path':pdf_path,'defect_log_path':'S6_SERIES_PUBLISH_defects_I.tsv',
            'defect_type_associations':{'path':str(ap.relative_to(ROOT)),'sha256':sha(ap.read_bytes()),'count':len(associations)},
            'unique_edit_rows':len(log),'inherited_unique_edit_rows':1953,'continuation_unique_edit_rows':86,'latest_applied_guards':62,
            'inherited_edit_type_associations':2046,'edit_type_associations':len(associations),'count_semantics':old['count_semantics'],
            'register_snapshot':evidence(old['register']['snapshot'],'Original 25 definitions',old['register']['sha256'],'register'),
            'all_types_source_clear':False,'open_content_types':open_types,'canonical_status_modified':False,'final_certified':False,'mathematical_events_added':0,
            'source_clear_scope':'Individual contextual and complete-block evidence is transported exactly to current source; current complete-page readings identify pending D08, D13, D18 and D23 issues. No type is inferred clear from keyword absence.',
            'source_transport':{'baseline_source_sha256':BASE_SHA,'current_source_sha256':SOURCE_SHA,'exact_forward_and_inverse_reconstruction':True,'applied_changes':changes,'receipts':receipt_evidence,'latest_complete_blocks_verified':verified_blocks},
            'complete_current_page_coverage':{'record':evidence(coverage_path,'Current actual coverage'),'images_verified':346,'reading_records_verified':len(reading_refs),'direct_current_pdf_readings':sum(r['method']=='read in this PDF' for r in coverage['pages']),'new_page_credit_from_dossier':0},
            'inherited_evidence_files_verified':[{'path':p,'sha256':h} for p,h in sorted(verified_inherited.items())],
            'check_ledger_sha256':events_sha,'pending_guard_files':pending_files,'rows':rows,
            'remaining_dependencies':['Consolidated approved current-source repairs for '+', '.join(open_types),'Broadened D08 context audit','Next build and every changed full image actually read','Final current source/PDF/provenance and mapped-log hash'],
            'limitations':['The dossier carries the original mathematical-check scopes without a new independent proof or event.','Candidate16 current coverage is complete; later source changes reopen their whole images.','The immutable candidate15 dossier, D08 reopening and completed reading records remain untouched.','Root alone changes canonical type status and final gate records.']}
    assert source_path.read_bytes()==source_bytes and log_path.read_bytes()==log_bytes and sha((ROOT/'CHECK_EVENTS.tsv').read_bytes())==events_sha
    p=OUT/'S6_SERIES_PUBLISH_I_candidate16_type_closure_preparation.json';p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    md=['# Paper I candidate16 — individual defect-type closure preparation','',f"Source SHA-256: `{SOURCE_SHA}`",'',f"PDF SHA-256: `{PDF_SHA}`",'',f"Defect-log SHA-256: `{result['defect_log_sha256']}`",'',f"Stable edit-content SHA-256: `{result['defect_log_content_sha256']}`",'',f"Type-association SHA-256: `{result['defect_type_associations']['sha256']}`",'',
        'The 2,039 unique log rows contain 2,132 type associations. The 86 continuation edits include the latest 62 applied guards. Exact forward and inverse maps reconstruct the current source and immutable baseline; all 36 latest full replacement blocks match the current source. The 346 current complete-image hashes and all 15 referenced reading-record hashes are verified. No mathematical event, source change or canonical status change is added.','',
        'D08, D13, D18 and D23 remain open for named candidate16 content findings. The other individual rows retain their bounded source-clear evidence for root review. The final source/PDF/provenance and mapped-log gates remain explicit.','','| Type | Inherited | Continuation | Current | Proposed disposition |','|---|---:|---:|---:|---|']
    for r in rows:md.append(f"| {r['type_id']} | {r['inherited_edit_associations']} | {r['continuation_edit_associations']} | {r['current_edit_associations']} | {r['status']} |")
    for r in rows:
        md += ['',f"## {r['type_id']} — {r['defect']}",'',r['source_review'],'','Continuation IDs: '+(', '.join(r['continuation_edit_ids']) or 'none')+'.','','Pending content findings: '+str(len(r['remaining_content_issues']))+'. The JSON binds each inherited receipt, exact applied guard and current full replacement block.','', 'Remaining dependencies: '+'; '.join(r['remaining_dependencies'])]
    p.with_suffix('.md').write_text('\n'.join(md)+'\n')
    print(json.dumps({'dossier':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'defect_log_sha256':sha(log_bytes),'defect_log_content_sha256':core_hash(log),'type_association_sha256':sha(ap.read_bytes()),'rows':25,'edit_rows':2039,'type_associations':2132,'open_content_types':open_types,'all_types_source_clear':False,'mathematical_events_added':0},indent=2))


if __name__=='__main__':main()

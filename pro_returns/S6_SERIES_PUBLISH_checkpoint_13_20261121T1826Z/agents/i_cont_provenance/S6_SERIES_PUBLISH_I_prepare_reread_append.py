#!/usr/bin/env python3
"""Prepare an explicitly attested Paper I rereading append; never mutate shared files.

The proposed TSV deliberately has no CHECK_EVENTS suffix.  An in-memory path
exercises the existing merger using the final operative bundle's exact name.
Archives, scans, image readings and automatic comparisons supply no new credit.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, collections, csv, hashlib, importlib.util, io, json, re, tempfile
from S6_SERIES_PUBLISH_I_cont_recount import recount, KINDS

R=Path(__file__).resolve().parents[2]
O=Path(__file__).resolve().parent
B=R.parent/'S6_SERIES_PUBLISH_work'
BASE_SHA='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
FINAL_NAME='S6_SERIES_PUBLISH_zz_I_continuation_reread_CHECK_EVENTS.tsv'
FINAL_BUNDLE='records/'+FINAL_NAME
FINAL_MANIFEST='agents/i_cont_provenance/continuation_reread_append/S6_SERIES_PUBLISH_I_continuation_reread_manifest.json'
TYPE='used and rechecked in this run'
GROUP='publish-I-continuation-20261121-exposed-proof-reread'
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation of 21 November 2026'
OUTCOME=('The complete exposed owning proof was reread and its operative steps, maps, hypotheses and conclusions were manually compared in the original/reworded statement-and-proof context recorded in the bound manifest. Repeated reviewers and editorial rounds are grouped once per owning printed statement. The manifest states each actual scope, including unchanged proof bytes where applicable. No independent derivation, targeted re-derivation, computation or formal certificate is claimed by this event.')
sha=lambda b:hashlib.sha256(b).hexdigest()
file_sha=lambda p:sha(p.read_bytes())
csv.field_size_limit(100_000_000)

def load(path): return json.loads((R/path).read_text())
def binding(path,expected=None):
    p=Path(path);p=p if p.is_absolute() else R/p
    value={'path':str(p.relative_to(R)),'sha256':file_sha(p)}
    if expected: assert value['sha256']==expected, str(p)
    return value
def write_json(path,value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def serial(rows,fields):
    stream=io.StringIO(newline='')
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t')
    writer.writeheader();writer.writerows(rows)
    return stream.getvalue().encode()
def table(raw):
    reader=csv.DictReader(io.StringIO(raw.decode(),newline=''),delimiter='\t')
    return reader.fieldnames,list(reader)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=O/'continuation_reread_append')
    ap.add_argument('--application-receipt',type=Path)
    ap.add_argument('--final',action='store_true')
    ap.add_argument('--proposal-version',type=int,default=2)
    ap.add_argument('--expected-count',type=int,default=78)
    args=ap.parse_args();out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    suffix='' if args.final else '_proposal_v'+str(args.proposal_version)
    if args.final: assert args.application_receipt, 'Final manifest requires the candidate19 source application receipt.'
    baseline=(R/'CHECK_EVENTS.tsv').read_bytes();assert sha(baseline)==BASE_SHA
    fields,old_rows=table(baseline);assert len(old_rows)==7866
    before_path=out/'I_continuation_before_ledger.tsv'
    if before_path.exists(): assert before_path.read_bytes()==baseline
    else: before_path.write_bytes(baseline)
    inputs={}; instances=collections.defaultdict(list); exclusions=[]
    def read_input(path,expected=None):
        inputs[path]=binding(path,expected);return load(path)
    def add(owner,reviewer,attest_path,evidence_path,before_path,before_sha,after_path,after_sha,scope,guard_ids,source_candidate,proof_change_required=True):
        att=inputs.get(attest_path) or binding(attest_path)
        ev=binding(evidence_path);bp=binding(before_path,before_sha);aq=binding(after_path,after_sha)
        bt=(R/bp['path']).read_text();at=(R/aq['path']).read_text()
        bproof=re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',bt,re.S)
        aproof=re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',at,re.S)
        assert bproof and aproof,(owner,'complete proof markers absent')
        changed=bproof!=aproof
        if proof_change_required: assert changed,(owner,source_candidate,'proof bytes unchanged')
        x={'reviewer':reviewer,'before_candidate':source_candidate,
           'attestation':att,'manual_review_evidence':ev,
           'original_full_context':bp,'proposed_full_context':aq,
           'guard_ids':sorted(set(guard_ids)),
           'complete_exposed_proof_actually_read':True,
           'exact_proposed_change_manually_compared_in_full_proof_context':True,
           'proof_bytes_changed':changed,'actual_scope':scope,
           'independent_derivation_claimed':False}
        # A root guard file can name several changes in the same complete pair.
        key=(reviewer,ev['path'],bp['sha256'],aq['sha256'])
        for earlier in instances[owner]:
            if earlier['_key']==key:
                earlier['guard_ids']=sorted(set(earlier['guard_ids'])|set(x['guard_ids']))
                return
        x['_key']=key;instances[owner].append(x)

    pp='agents/i_cont_provenance/S6_SERIES_PUBLISH_I_continuation_proof_reread_attestation_provenance.json'
    p=read_input(pp,'8911f4085b80d813e2999c599f53be6ce4b1b57f0cf05d1dc3bb9a8f8877b99a')
    for event in p['events']:
        for x in event['review_instances']:
            owner=event['statement_id']
            if owner=='ari:C.6.R2' and x['batch']=='candidate18':
                exclusions.append({'reviewer':'provenance','statement_id':owner,'batch':x['batch'],'reason':'Paragraph layout and punctuation only; R2 qualifies separately through the root candidate17 substantive statement/proof rereading.'});continue
            assert x['complete_exposed_owning_proof_actually_read'] and x['exact_rewording_actually_compared_in_full_proof_context']
            ev=x['manual_review_evidence'];binding(ev['path'],ev['sha256'])
            bp=x['original_complete_statement_and_proof'];aq=x['proposed_complete_statement_and_proof']
            add(owner,'provenance',pp,ev['path'],bp['path'],bp['sha256'],aq['path'],aq['sha256'],x['review_order'],x['guard_ids'],int(re.search(r'\d+',x['batch'])[0]))
    exclusions += [{'reviewer':'provenance','input_scope_exclusion':x} for x in p['excluded']]

    ep='agents/i_cont_edits/S6_SERIES_PUBLISH_I_continuation_proof_reread_attestation_edits.json'
    e=read_input(ep,'4d66d7fd6e99330de40db3b50552ce6e87e05da857e46af420a8a578ab878de9')
    for event in e['rows']:
        for x in event['supporting_manual_review_instances']:
            assert x['complete_original_proof_actually_read'] and x['proposed_rewording_actually_compared_against_original_proof']
            binding(x['evidence_record'],x['evidence_record_sha256'])
            add(event['statement_id'],'editor',ep,x['evidence_record'],x['original_full_block'],x['original_full_block_sha256'],x['replacement_full_block'],x['replacement_full_block_sha256'],x['manual_review_method'],x['proof_guard_or_change_ids'],x['before_candidate'])
    exclusions += [{'reviewer':'editor','input_scope_exclusion':x} for x in e['excluded_scopes']]
    exclusions += [{'reviewer':'editor','input_scope_exclusion':x} for x in e.get('additional_exclusions',[])]

    ip='agents/continuation_infra/S6_SERIES_PUBLISH_I_infra_used_rechecked_scope_attestation.json'
    i=read_input(ip,'4d2a31b58cb6000dd7cf3ec4b6f363a1ae42f588fba106a102b32165925eb4f6')
    for x in i['historically_attested_complete_proof_comparisons']:
        binding(x['attestation_record'],x['attestation_record_sha256'])
        add(x['statement_id'],'infra',ip,x['attestation_record'],x['before_proof'],x['before_proof_sha256'],x['after_proof'],x['after_proof_sha256'],x['actual_work_attestation']+' '+x['exact_extent'],[x['guard_id']],14)
    exclusions += [{'reviewer':'infra','input_scope_exclusion':x} for x in i['excluded']]

    for candidate in [16,17]:
        rp=f'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate{candidate}_root_guards.json'
        rows=read_input(rp)
        for x in rows:
            if x['id']=='I17-root-01':
                exclusions.append({'reviewer':'root','statement_id':x['statement_id'],'guard_id':x['id'],'reason':'Subject/verb comma only. No other qualifying full-proof wording comparison supports this owner.'});continue
            assert x['root_review']
            add(x['statement_id'],'root',rp,rp,x['original_full_block'],x['original_full_block_sha256'],x['proposed_full_block'],x['proposed_full_block_sha256'],x['root_review'],[x['id']],candidate)

    sp='records/S6_SERIES_PUBLISH_I_candidate17_root_substantive_context_review.json'
    s=read_input(sp,'5c34fb8c24da356c99d6fa13df338b0d9187a94a21f44f239bf427d45745968b')
    for item in s['directly_read_archives']:binding(item['path'],item['sha256'])
    egp='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_edits_guards.json'
    eg=read_input(egp)
    for x in eg['full_blocks']:
        if x['statement_id'] not in {'ari:C.6.R2','ari:C.6.R5','inv:D4.4'}:continue
        qualification=' The attached proof bytes are unchanged; the activity is the expressly attested substantive statement/proof comparison.' if x['statement_id'] in {'ari:C.6.R2','ari:C.6.R5'} else ''
        add(x['statement_id'],'root',sp,sp,x['original'],x['original_sha256'],x['proposed'],x['proposed_sha256'],s['reading_scope']+qualification,x['guards'],17,False)

    rp='records/S6_SERIES_PUBLISH_I_candidate18_root_complete_proof_comparison.json'
    r=read_input(rp,'98b965d022a4b911b828b494835b745752e4a4e7ee8d338ecacb55e1e4454028')
    for x in r['full_proof_comparisons']:
        if x['statement_id'] in {'fam:src:D.1.4','fam:src:D.1.7','push:src:E.2.1','ari:C.6.R2'}:
            exclusions.append({'reviewer':'root','statement_id':x['statement_id'],'candidate':18,'guard_ids':x['guard_ids'],'reason':'Accent restoration or paragraph layout only. Separate qualifying earlier wording comparisons, where present, are retained by owner.'});continue
        assert x['root_actually_read_complete_original_context'] and x['root_actually_compared_exact_proposed_changes']
        add(x['statement_id'],'root',rp,rp,x['original'],x['original_sha256'],x['proposed'],x['proposed_sha256'],r['actual_reading_scope'],x['guard_ids'],18)
    r19p='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_root_guards_v2.json'
    r19=read_input(r19p,'6446e98599ce8041bd8011dc6d9587e5200a47ac811b045f37d72777c643607f')
    for x in r19['guards']:
        assert x['root_review']['complete_original_statement_and_proof_actually_read'] and x['root_review']['complete_proposed_difference_actually_compared']
        add(x['statement_id'],'root',r19p,r19p,x['original_full_block'],x['original_full_block_sha256'],x['proposed_full_block'],x['proposed_full_block_sha256'],x['root_review']['comparison_scope'],[x['id']],19)
    for ep19,expected in [
        ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_full_pair_review.json','8ff0f61b682fe8eb71161f264f30080f931642ffe4ac32a6367e19e0ff947ef2'),
        ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_additional_full_pair_review.json','f437d1143881f8b5fe69af64a2548901c5833238c515132bd34bb2857290820d')]:
        ed19=read_input(ep19,expected)
        for x in ed19['rows']:
            assert x['complete_original_statement_and_proof_actually_read'] and x['complete_proposed_statement_and_proof_actually_read'] and x['exact_full_pair_actually_compared']
            add(x['statement_id'],'editor',ep19,ep19,x['original_path'],x['original_sha256'],x['proposed_path'],x['proposed_sha256'],x['review_scope'],x['guard_ids'],19)
    pp19='agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate19_provenance_full_pair_review.json'
    pr19=read_input(pp19,'5a1002a24adb5b5da0410f02cc000318489b3b065e9e175f3167a0fe454ce6ce')
    for x in pr19['full_pair']:
        assert x['complete_original_and_proposed_blocks_actually_read'] and x['manual_comparison_completed']
        add(x['statement_id'],'provenance',pp19,pp19,x['original'],x['original_sha256'],x['proposed'],x['proposed_sha256'],x['scope'],x['guard_ids'],19)
    retention='agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate19_ariC61_recap_disposition.json'
    read_input(retention,'da82c70d61e2742f72f0be3ea4798fefe59b05f17971a8d7aeac7f3d092b015f')
    exclusions.append({'reviewer':'infra','statement_id':'ari:C.6.1','candidate':19,
        'evidence':inputs[retention],
        'reason':'The full original statement/proof was read and the final inferential sentence retained. There is no proposed rewritten proof or original/proposed comparison; this retention context adds no event in the present rewrite-comparison manifest.'})

    # Bind current printed owner identities independently of prior totals.
    reference=O/'candidate19_review_blocks/S6_SERIES_PUBLISH_I_candidate19_source_snapshot.tex'
    reference_raw=reference.read_bytes()
    with tempfile.TemporaryDirectory(prefix='I-reread-recount-') as td:
        tr=Path(td);(tr/'S6_SERIES_PUBLISH_I.tex').write_bytes(reference_raw);(tr/'CHECK_EVENTS.tsv').write_bytes(baseline)
        counts_before=recount(tr,B)
    owner_rows={x['id']:x for x in counts_before['statements']}
    reference_text=reference_raw.decode()
    aux_path=R/'build/I_candidate19/S6_SERIES_PUBLISH_I.aux'
    aux_lines=aux_path.read_text().splitlines()
    aliases={'fam:src:A.5.2':'push:src:E.2.1','fam:src:B.4.1':'night:P5.5'}
    alias_witnesses=[]
    assert set(instances)-set(owner_rows)==set(aliases)
    for alias,owner in aliases.items():
        starts=list(re.finditer(r'\\begin\{(maintheorem|theorem|lemma|proposition|corollary|definition|remark|cited)\}',reference_text))
        headers=[]
        for st in starts:
            end='\\end{'+st[1]+'}'
            header=reference_text[st.start():reference_text.index(end,st.end())+len(end)]
            if '\\label{'+alias+'}' in header: headers.append((st.start(),header))
        assert len(headers)==1
        start,header=headers[0]
        assert '\\StatementRecord{'+owner+'}' in header and '\\label{'+owner+'}' in header
        old_aux=next(x for x in aux_lines if x.startswith('\\newlabel{'+alias+'}'))
        new_aux=next(x for x in aux_lines if x.startswith('\\newlabel{'+owner+'}'))
        assert old_aux.split('}',1)[1]==new_aux.split('}',1)[1]
        alias_witnesses.append({'attested_identifier':alias,'current_printed_owner':owner,
            'source':binding(reference),'statement_header_line':reference_text.count('\n',0,start)+1,
            'exact_statement_header':header,'statement_header_sha256':sha(header.encode()),
            'aux':binding(aux_path),'attested_identifier_aux':old_aux,'owner_aux':new_aux,
            'exact_mapping':'Both labels occur on this one printed environment, whose StatementRecord supplies the canonical owner; their aux number, page, title and destination are identical.'})
        for instance in instances[alias]:
            instance['attested_statement_id']=alias
            instance['owning_printed_statement_id']=owner
            instances[owner].append(instance)
        del instances[alias]
    assert set(instances) <= set(owner_rows)
    assert len(instances)==args.expected_count
    event_count=len(instances)
    assert len(owner_rows)==333
    owners=sorted(instances,key=lambda k:owner_rows[k]['line'])
    rows=[];events=[]
    for n,owner in enumerate(owners,2):
        event_id='publish-I-cont-reread-20261121:'+sha(owner.encode())[:20]
        row={k:'' for k in fields}
        row.update(statement_id=owner,date='2026-11-21',who=WHO,type=TYPE,outcome=OUTCOME,
            event_id=event_id,phase='publication-continuation-20261121',
            source_file=FINAL_MANIFEST,source_row=str(n-1),source_event_type=TYPE,
            evidence_group=GROUP,publish_input_file=FINAL_NAME,publish_input_row=str(n),
            date_utc='2026-11-21',where=FINAL_MANIFEST)
        rows.append(row)
        ri=instances[owner]
        for v in ri:v.pop('_key')
        events.append({'statement_id':owner,'event_id':event_id,'event_type':TYPE,
            'event_bundle_row':n,'manifest_row':n-1,'owning_printed_statement':owner_rows[owner],
            'manual_review_instances':ri,'event_count':1,
            'scope':'Full exposed-proof rereading with manual original/proposed-context comparison; one event for this owner across all listed reviewers and rounds.',
            'R2_qualification':('The editor candidate13 pair is an explicitly attested complete rewritten-proof comparison. The root candidate17 substantive statement/proof comparison leaves the proof bytes unchanged. Both actual scopes are recorded, with one event for their common printed owner; candidate18 paragraph layout supplies none.' if owner=='ari:C.6.R2' else None)})
    assert len(rows)==len({x['event_id'] for x in rows})==len({x['statement_id'] for x in rows})==event_count
    assert not {x['event_id'] for x in rows}&{x['event_id'] for x in old_rows}
    assert GROUP not in {x['evidence_group'] for x in old_rows}
    bundle_raw=serial(rows,fields)
    bundle_path=out/('I_continuation_reread_event_bundle'+suffix+'.tsv')
    if bundle_path.exists(): assert bundle_path.read_bytes()==bundle_raw
    else: bundle_path.write_bytes(bundle_raw)

    # Exercise the unchanged merger with the exact final input filename,
    # without placing a discoverable operative bundle in the shared tree.
    mp=R/'agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py'
    spec=importlib.util.spec_from_file_location('record_merger',mp);mm=importlib.util.module_from_spec(spec);spec.loader.exec_module(mm)
    extra=sorted((R/'agents').rglob('S6_SERIES_PUBLISH*CHECK_EVENTS.tsv'))
    archived=[x for x in extra if 'S6_SERIES_PUBLISH_I_candidate11_tail_before_locator_refresh' in x.parts]
    extra=[x for x in extra if x not in archived]
    extra+=sorted((R/'records').glob('S6_SERIES_PUBLISH_*CHECK_EVENTS.tsv'))
    assert all(x.name<FINAL_NAME for x in extra if x.parent==R/'records')
    baseline_merge,baseline_rejected=mm.merge(B,extra)
    fields_merge=list(dict.fromkeys(k for row in baseline_merge for k in row))
    assert fields_merge==fields and serial(baseline_merge,fields)==baseline
    class InMemoryFinalBundle:
        name=FINAL_NAME
        def open(self,*a,**kw):return io.StringIO(bundle_raw.decode(),newline='')
    merged,rejected=mm.merge(B,extra+[InMemoryFinalBundle()])
    preview=serial(merged,fields)
    assert preview.startswith(baseline)
    _,normalized_merged=table(preview)
    assert normalized_merged[:7866]==old_rows and normalized_merged[7866:]==rows
    assert len(rejected)==len(baseline_rejected)
    assert preview==baseline+bundle_raw.split(b'\r\n',1)[1]
    preview_path=out/('I_continuation_after_ledger_preview'+suffix+'.tsv')
    assert not preview_path.exists();preview_path.write_bytes(preview)
    with tempfile.TemporaryDirectory(prefix='I-reread-recount-') as td:
        tr=Path(td);(tr/'S6_SERIES_PUBLISH_I.tex').write_bytes(reference_raw);(tr/'CHECK_EVENTS.tsv').write_bytes(preview)
        counts_after=recount(tr,B)
    cb,ca=counts_before['counts'],counts_after['counts']
    assert [cb[k] for k in KINDS]==[767,10,143,731,194,1]
    assert [ca[k] for k in KINDS]==[767,10,143,731+event_count,194,1]
    assert ca['event_associations']==1846+event_count and ca['declared_evidence_groups']==1615
    assert ca['statements']==333 and ca['subject_identifiers']==353

    # Exact methodology proposal: the count-source update itself creates no event.
    text=reference_raw.decode()
    meth=re.search(r'\\subsection\{Methodology\}.*?(?=\\subsection\{How the paper is organized\})',text,re.S)[0]
    old='It also records 731 readings of the proofs and applications,'
    new=f'It also records {731+event_count} readings of the proofs and applications,'
    assert meth.count(old)==text.count(old)==1
    proposed=meth.replace(old,new)
    canonical_method=re.search(r'\\subsection\{Methodology\}.*?(?=\\subsection\{How the paper is organized\})',(R/'S6_SERIES_PUBLISH_I.tex').read_text(),re.S)[0]
    assert canonical_method==meth
    bmethod=out/('I_methodology_original'+suffix+'.tex');amethod=out/('I_methodology_proposed'+suffix+'.tex')
    assert not bmethod.exists() and not amethod.exists()
    bmethod.write_text(meth);amethod.write_text(proposed)
    count_guard={'paper':'I','id':'I-reread-count-01','type':'D15','statement_id':'I:methodology',
        'immediate_before_source':binding(R/'S6_SERIES_PUBLISH_I.tex'),
        'printed_before_source':binding(reference),
        'printed_before_pdf':binding(R/'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf'),
        'printed_before_pages':[16,17],'count_literal_printed_before_page':16,
        'immediate_before_body_source_has_no_pdf':bool(args.application_receipt),
        'exact_full_methodology_block_equal_between_printed_before_source_and_immediate_before_source':True,
        'methodology_block_sha256_in_both_before_sources':sha(meth.encode()),
        'old':old,'new':new,'reason':'Newly recorded actual complete-proof rereadings require the methodology totals to track the final ledger; only the used-and-rechecked total changes.',
        'original_full_block':binding(bmethod),'proposed_full_block':binding(amethod),
        'full_block_difference_is_exact_count_substitution':True,
        'counts_before':cb,'counts_after':ca,'new_check_credit_from_source_edit':0,
        'application_guard':f'Apply only after the approved {event_count}-row event append and a fresh recount of the final canonical ledger.'}
    guard_path=out/('S6_SERIES_PUBLISH_I_methodology_count_guard'+suffix+'.json');write_json(guard_path,count_guard)

    apply18=read_input('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate18_combined_apply_receipt.json','6f4f76cb0a75bc2eaa6603bcf0ed6c1bb31100e947c5452301e7d3b076edce1b')
    applied18={x['guard_id'] for x in apply18['changes']}
    assert all(g in applied18 for ev in events for x in ev['manual_review_instances'] if x['before_candidate']==18 for g in x['guard_ids'])
    application19=None
    if args.application_receipt:
        application19=binding(args.application_receipt)
        app=load(application19['path'])
        # The final record must disclose successful application and exact maps.
        assert app.get('applied') is True or app.get('mode')=='applied'
        assert 'I19-root-01' in json.dumps(app)
        assert app['before_source_sha256']==file_sha(reference)
        assert app['after_source_sha256']==file_sha(R/'S6_SERIES_PUBLISH_I.tex')
        changes=sorted(app['changes'],key=lambda x:x['original_offset'])
        expected19={g for ev in events for inst in ev['manual_review_instances'] if inst['before_candidate']==19 for g in inst['guard_ids']}
        assert {x['guard_id'] for x in changes}==expected19 and len(changes)==7
        forward=reference_text
        for c in reversed(changes):
            at=c['original_offset'];assert reference_text[at:at+len(c['old'])]==c['old']
            forward=forward[:at]+c['new']+forward[at+len(c['old']):]
        assert forward==(R/'S6_SERIES_PUBLISH_I.tex').read_text()
        delta=0;ends=[]
        for c in changes:
            ends.append((c,c['original_offset']+delta));delta+=len(c['new'])-len(c['old'])
        backward=forward
        for c,at in reversed(ends):
            assert forward[at:at+len(c['new'])]==c['new']
            backward=backward[:at]+c['old']+backward[at+len(c['new']):]
        assert backward==reference_text
        # Exact current full-context matches discharge every candidate19 pair.
        current_text=(R/'S6_SERIES_PUBLISH_I.tex').read_text()
        for ev in events:
            for inst in ev['manual_review_instances']:
                if inst['before_candidate']!=19:continue
                final_proof=(R/inst['proposed_full_context']['path']).read_text()
                assert current_text.count(final_proof)==1, ev['statement_id']
        read_input('records/S6_SERIES_PUBLISH_I_reread_manifest_v2_validation.json')
    manifest={'schema_version':1,'paper':'I','recorded_utc':datetime.now(timezone.utc).isoformat(),
        'status':'final proposed append, pending root approval' if args.final else 'proposal; candidate19 body application gate remains open',
        'event_type':TYPE,'candidate_event_count':event_count,'one_event_per_owning_printed_statement':True,
        'deduplication_scope':'One owner across this entire continuation, across reviewers, multiple exact edits and repeated candidates.',
        'review_date':'2026-11-21','who':WHO,'effort':'ChatGPT Pro mode; no separate reasoning-effort setting is represented by the continuation UI.',
        'basis':'Prompt sections4.2 and4.3, the explicit reviewer attestations and their contemporaneous complete-proof manual comparison receipts. This manifest validates records and assigns no independent mathematical derivation.',
        'input_attestations_and_binding_records':list(inputs.values()),
        'reference_source19':binding(reference),'before_ledger':binding(before_path),'before_rows':7866,
        'prospective_after_ledger_sha256':sha(preview),'prospective_after_rows':7866+event_count,
        'proposal_event_bundle':binding(bundle_path),'final_event_bundle_path':FINAL_BUNDLE,
        'final_manifest_path':FINAL_MANIFEST,'event_bundle_fields':fields,
        'preview_ledger':binding(preview_path),'old_ledger_prefix_preserved_in_preview':True,
        'preview_tail_exactly_matches_bundle_rows_and_bytes':True,
        'merger':binding(mp),'existing_operative_bundles':[binding(x) for x in extra],
        'merger_baseline_bytes_equal_canonical_ledger':True,'excluded_archive_bundles':[binding(x) for x in archived],
        'evidence_group':GROUP,'evidence_group_scope':f'One declared common run/type/outcome group across the {event_count} statement associations; no claim of {event_count} independent derivations or model families.',
        'attested_identifier_to_current_owner_map':alias_witnesses,
        'counts_before':cb,'counts_after':ca,'methodology_count_guard':binding(guard_path),
        'source19_application_receipt_for_candidate18_pairs':inputs['agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate18_combined_apply_receipt.json'],
        'candidate19_application_receipt':application19,'candidate19_application_gate_discharged':bool(application19),
        'candidate19_body_forward_inverse_reconstruction_verified':bool(application19),
        'source_after_candidate19_body_application':binding(R/'S6_SERIES_PUBLISH_I.tex') if application19 else None,
        'events':events,'excluded_scopes':exclusions,
        'historical_zero_event_receipts':'Preserved verbatim: they state that the individual review/guard operations appended zero rows. This proposed later explicit append accounts once for actual attested rereadings; it creates no retrospective independent or computational work.',
        'new_independent_targeted_computation_credit':0,'new_background_refutation_credit':0,
        'check_credit_from_metadata_bibliography_layout_page_images_or_automatic_comparisons_alone':0,
        'ledger_mutated_by_preparation':False,'canonical_source_mutated_by_preparation':False,
        'final_provenance_gate':'Final source/count/PDF binding and certified full image coverage remain required after ledger and methodology application.'}
    manifest_path=out/('S6_SERIES_PUBLISH_I_continuation_reread_manifest'+suffix+'.json')
    write_json(manifest_path,manifest)
    receipt_template={'schema_version':1,'paper':'I','applied':False,
        'before_ledger':binding(before_path),'before_rows':7866,'after_ledger_sha256':sha(preview),
        'after_rows':7866+event_count,'event_bundle':{'path':FINAL_BUNDLE,'sha256':sha(bundle_raw)},
        'manifest':{'path':FINAL_MANIFEST,'sha256':file_sha(manifest_path) if args.final else 'TO_BE_BOUND_AFTER_CANDIDATE19_APPLICATION'},
        'appended_event_ids':[x['event_id'] for x in rows],'old_ledger_prefix_preserved':True,
        'approved_manifest_sha256':file_sha(manifest_path) if args.final else 'TO_BE_BOUND_AFTER_CANDIDATE19_APPLICATION',
        'approval':{'path':'ROOT_APPROVAL_RECORD','sha256':'ROOT_APPROVAL_SHA256'},
        'template_only':True,'actual_append_not_performed':True}
    write_json(out/('S6_SERIES_PUBLISH_I_reread_append_receipt_template'+suffix+'.json'),receipt_template)
    note=['# Paper I continuation proof reread append proposal','',
        f'The proposed bundle contains **{event_count} used-and-rechecked events**, one per owning printed statement across the continuation. The current 7,866 rows remain an exact byte prefix of the {7866+event_count:,}-row preview. No independent proof, targeted derivation, computation, formal certificate, background or refutation event is added.','',
        '| Recorded measure | Before | After |','|---|---:|---:|']
    note += [f'| {k} | {cb[k]} | {ca[k]} |' for k in ['statements','subject_identifiers','event_associations','declared_evidence_groups']+list(KINDS)]
    note += ['', f'The {event_count} associations share one declared evidence group for this exposed-proof comparison run. They do not represent {event_count} independent derivations. The exact statement-header and aux mappings identify fam:A.5.2 with the already counted printed owner push:E.2.1, and fam:B.4.1 with the already counted printed owner night:P5.5.','',
        'R2 has exactly one event supported by the editor’s complete candidate13 rewritten-proof comparison and the root’s candidate17 substantive statement/proof comparison. Its proof bytes were unchanged in the latter comparison. Its candidate18 paragraph layout supplies no event. Root candidate18 accent-only D.1.4 and D.1.7, candidate17 comma-only D.1.3, and all other explicitly excluded metadata, page-only and automatic work supply none. E.2.1 remains supported by earlier substantive wording comparisons.','',
        'Candidate19 has applied all candidate18 pairs. The candidate19 full-proof comparisons are individually bound, and their separate exact source application is recorded before the final manifest is frozen. The final full-page and 42-claim gates remain later steps.','',
        '## Exact methodology change','',f'`{old}`', '', 'becomes', '',f'`{new}`','',
        'The proposed D15 count refresh preserves every other byte of the complete methodology block and supplies zero check-event credit.','',
        '## Evidence and append preview','',f'- Manifest: `{manifest_path.relative_to(R)}`; SHA-256 `{file_sha(manifest_path)}`.',f'- Proposed bundle: `{bundle_path.relative_to(R)}`; SHA-256 `{file_sha(bundle_path)}`.',f'- Preview ledger: `{preview_path.relative_to(R)}`; SHA-256 `{file_sha(preview_path)}`.',f'- Before ledger: `{before_path.relative_to(R)}`; SHA-256 `{file_sha(before_path)}`.','',
        'The existing merger was exercised with the exact final filename in memory. The proposed bundle’s publish_input_file and publish_input_row already match those generated by the merger; the preview tail equals the proposed bundle rows exactly. No discoverable new CHECK_EVENTS bundle was written.','']
    md=out/('S6_SERIES_PUBLISH_I_continuation_reread_manifest'+suffix+'.md');assert not md.exists();md.write_text('\n'.join(note))
    assert (R/'CHECK_EVENTS.tsv').read_bytes()==baseline
    print(json.dumps({'manifest':binding(manifest_path),'candidate_events':event_count,'manual_comparison_instances':sum(len(x['manual_review_instances']) for x in events),'owners_by_reviewer':{k:sum(any(x['reviewer']==k for x in e['manual_review_instances']) for e in events) for k in ['provenance','editor','infra','root']},'bundle':binding(bundle_path),'preview':binding(preview_path),'counts_after':ca,'candidate19_application_gate_discharged':bool(application19)},indent=2))

if __name__=='__main__':main()

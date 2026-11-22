#!/usr/bin/env python3
"""Prepare/apply the reviewed candidate16 batch with explicit supersessions.

Default mode writes proposal/comparison receipts only. Canonical source/log
mutation requires --apply and the exact root-approved final bibliography hash.
No completed reading, type-status record or check ledger is changed.
"""
from pathlib import Path
import argparse
import collections
import csv
import datetime
import difflib
import hashlib
import io
import json
import re
from S6_SERIES_PUBLISH_synctex_batch import Scanner

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
SOURCE_SHA='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA='4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'
FIXED_FILES=[
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_root_guards.json','e34f14d59941d977097e5545fb568530b13d8fb2569dbeb91ab7a2b4f85f9abd',3),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_edits_guards.json','0a287201f4b4ca77560f45edf416405ae73b3805893bab77159d91de1e03048c',11),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_edits_guard11_revision.json','36c5965f796e3081c9184b1a6b2fbd1040da08c1ddf543be7925a5cd5b2fe606',1),
 ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json','022788d4dbc251401c7fbec94441df837d689eea061efa3630b1a8ee3640bc8a',2),
 ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_expanded_guards.json','822f0af301a8ef840d483d9f7f2b8bce097ec12e58edeacbf62ab7303c97e2a9',16),
 ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_recap_guards.json','05cf43842972823d85f79cda68adb2ae244bf206ee1bbf823903a20b803cfc46',1),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_Cech_guards.json','1e02e9bcc277f6fd0e4715124593d601c5cf992e3a92d71c9142b93a66f0fa0a',8),
]
sha=lambda b:hashlib.sha256(b).hexdigest()
csv.field_size_limit(100_000_000)


def inline(s):return re.findall(r'(?<!\\)\$(?:\\.|[^$\\])*(?<!\\)\$',s)


def displays(s):
    return [re.findall(p,s) for p in [r'\\\[[\s\S]*?\\\]',r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$',r'\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}[\s\S]*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}']]


def refs(s):
    return re.findall(r'\\(?:eqref|ref|cref|Cref|cite|citet|citep|SeriesRef)(?:\[[^\]]*\])?\{[^}]+\}',s)


def supplied_archive(g):
    if 'full_block_archive' in g:
        a=g['full_block_archive'];return (a['original'],a['original_sha256'],a['proposed'],a['proposed_sha256'])
    for fields in [('original_full_block','original_full_block_sha256','proposed_full_block','proposed_full_block_sha256'),('original_entry','original_entry_sha256','proposed_entry','proposed_entry_sha256'),('original_block','original_block_sha256','proposed_block','proposed_block_sha256')]:
        if all(k in g for k in fields):return tuple(g[k] for k in fields)
    return None


def source_block(text,position):
    if position>text.index(r'\begin{thebibliography}'):
        heads=list(re.finditer(r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}',text))
        h=[m for m in heads if m.start()<=position][-1]
        later=[m.start() for m in heads if m.start()>h.start()]
        end=min(later) if later else text.index(r'\end{thebibliography}',h.end())
        return 'bib:'+h[1],h.start(),end,'complete bibliography entry'
    heads=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|definition|cited|maintheorem|computed)\}',text))
    h=[m for m in heads if m.start()<=position][-1]
    end=text.index(r'\end{'+h[1]+'}',h.end())+len(r'\end{'+h[1]+'}')
    if re.match(r'\s*\\begin\{proof\}',text[end:]):end=text.index(r'\end{proof}',end)+len(r'\end{proof}')
    assert h.start()<=position<end,(position,h.start(),end)
    label=re.search(r'\\label\{([^}]+)\}',text[h.start():end])[1]
    return label,h.start(),end,'complete statement and attached proof'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bibliography-guards',required=True)
    ap.add_argument('--bibliography-sha',required=True)
    ap.add_argument('--apply',action='store_true')
    ap.add_argument('--approved-bibliography-sha')
    args=ap.parse_args()
    if args.apply:assert args.approved_bibliography_sha==args.bibliography_sha,'Supply the exact final root-approved bibliography hash.'
    source_path=ROOT/'S6_SERIES_PUBLISH_I.tex';log_path=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv'
    before_bytes=source_path.read_bytes();before=before_bytes.decode();log_bytes=log_path.read_bytes()
    assert sha(before_bytes)==SOURCE_SHA and '\r' not in before
    reader=csv.DictReader(io.StringIO(log_bytes.decode()),delimiter='\t');fields=reader.fieldnames;rows=list(reader);assert len(rows)==2039
    ledger_path=ROOT/'CHECK_EVENTS.tsv';ledger_sha=sha(ledger_path.read_bytes())
    pdf_path=ROOT/'build/I_candidate16/S6_SERIES_PUBLISH_I.pdf';assert sha(pdf_path.read_bytes())==PDF_SHA
    coverage_path='records/S6_SERIES_PUBLISH_I_candidate16_complete_coverage_snapshot.json';coverage=json.loads((ROOT/coverage_path).read_text())
    assert coverage['source_sha256']==SOURCE_SHA and coverage['pdf_sha256']==PDF_SHA and coverage['all_pages_read']
    protected={r['reading_record']:r['reading_record_sha256'] for r in coverage['pages']}
    protected.update({coverage_path:sha((ROOT/coverage_path).read_bytes()),
      'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_type_closure_preparation.json':'0b77945c49f60963e2c96fff0eaef6c4c31c1107c02fbe326054fc2d4c0e2a35',
      'records/S6_SERIES_PUBLISH_I_candidate15_type_dossier_snapshot.json':'33828919926cd1451d5c9bbdc285dca40a3f399d423b44215a64ce92fed8872a'})
    for path,h in protected.items():assert sha((ROOT/path).read_bytes())==h
    paths=FIXED_FILES+[(args.bibliography_guards,args.bibliography_sha,None)]
    changes=[];guards_receipts=[];supplied={};excluded=[];bib_document=None;bib_supersessions=[];publication_evidence=[]
    for path,h,n in paths:
        raw=(ROOT/path).read_bytes();assert sha(raw)==h,(path,sha(raw),h)
        document=json.loads(raw);guards=document if isinstance(document,list) else document['guards']
        if n is not None:assert len(guards)==n
        if path==args.bibliography_guards:
            bib_document=document
            for g in guards:
                for old_file in g.get('superseded_guard_files',[]):
                    item={'path':old_file,'sha256':sha((ROOT/old_file).read_bytes()),'superseded_guard_id':g['id'],'replacement_guard_file':path,'replacement_guard_file_sha256':h}
                    bib_supersessions.append(item)
                vp=g.get('source_version_binding_receipt');vh=g.get('source_version_binding_receipt_sha256')
                if vp:assert sha((ROOT/vp).read_bytes())==vh
                for e in g.get('publication_evidence',[]):
                    if 'path' in e:
                        assert sha((ROOT/e['path']).read_bytes())==e['sha256']
                        publication_evidence.append(e)
        active=[]
        for g in guards:
            if g['id']=='I16-edits-11':
                excluded.append({'guard_id':g['id'],'file':path,'file_sha256':h,'superseded_by':'I16-edits-11r1'});continue
            assert g['source_sha256']==SOURCE_SHA
            old,new=g.get('before',g.get('old')),g.get('after',g.get('new'))
            assert isinstance(old,str) and isinstance(new,str) and old and before.count(old)==1,g['id']
            pos=before.index(old);archive=supplied_archive(g)
            if archive:
                pa,ha,pb,hb=archive
                a=(ROOT/pa).read_text();b=(ROOT/pb).read_text()
                assert sha(a.encode())==ha and sha(b.encode())==hb and before.count(a)==1
                start=before.index(a);end=start+len(a)
                assert start<=pos and pos+len(old)<=end
                label=g.get('statement_id') or 'archived-block'
                kind='complete bibliography entry' if pos>before.index(r'\begin{thebibliography}') else 'complete supplied statement/proof block'
                supplied.setdefault(archive,[]).append(g['id'])
            else:label,start,end,kind=source_block(before,pos)
            assert pos+len(old)<=end
            assert inline(old)==inline(new),(g['id'],'inline mathematical segments')
            assert displays(old)==displays(new),(g['id'],'display mathematical segments')
            c={'guard_id':g['id'],'type':g['type'],'statement_id':g.get('statement_id',label),'owning_block_id':label,
               'old':old,'new':new,'reason':g['reason'],'old_source_line':before[:pos].count('\n')+1,'candidate16_read_page':g.get('page'),
               'guard_file':path,'guard_file_sha256':h,'original_offset':pos,'block_start':start,'block_end':end,'block_kind':kind,
               'inline_math_segments_identical':True,'display_math_segments_identical':True,'removed_inline_mentions_in_prose':[],
               'supersedes_guard_id':g.get('supersedes_guard_id'),'declared_reference_order_change':g['id']=='I16-edits-11r1',
               'bibliography_printed_author_year_before':g.get('printed_author_year_before'),'bibliography_printed_author_year_after':g.get('printed_author_year_after'),'cited_arxiv_version':g.get('cited_arxiv_version')}
            changes.append(c);active.append(g['id'])
        guards_receipts.append({'path':path,'sha256':h,'provided_guards':len(guards),'active_guards':len(active),'active_ids':active})
    assert len(changes)==41+len(bib_document if isinstance(bib_document,list) else bib_document['guards'])
    assert len({g['guard_id'] for g in changes})==len(changes)
    ordered=sorted(changes,key=lambda x:x['original_offset'])
    for a,b in zip(ordered,ordered[1:]):assert a['original_offset']+len(a['old'])<=b['original_offset'],('overlapping guards',a['guard_id'],b['guard_id'])
    after=before
    for c in changes:
        assert after.count(c['old'])==1,c['guard_id'];p=after.index(c['old']);c['applied_offset']=p
        after=after[:p]+c['new']+after[p+len(c['old']):]
    reverse=after
    for c in reversed(changes):
        p=c['applied_offset'];assert reverse[p:p+len(c['new'])]==c['new']
        reverse=reverse[:p]+c['old']+reverse[p+len(c['new']):]
    assert reverse==before and displays(after)==displays(before)
    seq_counts={}
    for name,pat in [('labels',r'\\label\{([^}]+)\}'),('tag_targets',r'\\hypertarget\{(tag-[^}]+)\}'),('all_targets',r'\\hypertarget\{([^}]+)\}'),('bibliography_keys',r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}')]:
        a,b=re.findall(pat,before),re.findall(pat,after);assert a==b,name;seq_counts[name]=len(a)
    relocation=next(c for c in changes if c['guard_id']=='I16-edits-11r1')
    relocated_only=before.replace(relocation['old'],relocation['new'],1)
    assert refs(after)==refs(relocated_only)
    assert refs(after)!=refs(before) and collections.Counter(refs(after))==collections.Counter(refs(before))
    seq_counts['citation_reference_and_SeriesRef_commands']=len(refs(before))
    supplied_verified=[];by_id={g['guard_id']:g for g in changes}
    for (pa,ha,pb,hb),ids in supplied.items():
        a,b=(ROOT/pa).read_text(),(ROOT/pb).read_text();t=a
        for gid in ids:
            c=by_id[gid];assert t.count(c['old'])==1;t=t.replace(c['old'],c['new'],1)
        assert t==b,('supplied batch replacement',pa,ids)
        supplied_verified.append({'original':pa,'original_sha256':ha,'proposed':pb,'proposed_sha256':hb,'individual_batch_guard_ids':ids,'exact_supplied_batch_replacement_verified':True,'combined_block_may_also_contain_other_approved_guards':True})
    # Merge overlapping complete archives before forming the final combined
    # blocks. Different readers can have disjoint edits in one owning proof.
    groups=[]
    for c in sorted(changes,key=lambda x:(x['block_start'],x['block_end'])):
        if groups and c['block_start']<groups[-1]['end']:
            groups[-1]['end']=max(groups[-1]['end'],c['block_end']);groups[-1]['changes'].append(c)
        else:groups.append({'start':c['block_start'],'end':c['block_end'],'changes':[c]})
    archives=[];masked_before=before;masked_after=after
    for i,group in enumerate(groups,1):
        a=before[group['start']:group['end']];b=a
        ids={c['guard_id'] for c in group['changes']}
        gc=[c for c in changes if c['guard_id'] in ids]
        for c in gc:assert b.count(c['old'])==1;b=b.replace(c['old'],c['new'],1)
        assert after.count(b)==1 and displays(a)==displays(b) and inline(a)==inline(b)
        stem=OUT/f'S6_SERIES_PUBLISH_I_candidate16_combined_block_{i:02d}'
        pa,pb,pd=[Path(str(stem)+suffix) for suffix in ['_original.tex','_proposed.tex','.diff']]
        pa.write_text(a);pb.write_text(b);pd.write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=gc[0]['owning_block_id']+'/candidate16',tofile=gc[0]['owning_block_id']+'/combined-proposal')))
        archives.append({'statement_id':gc[0]['owning_block_id'],'kind':gc[0]['block_kind'],'guard_ids':[c['guard_id'] for c in gc],
          'original':str(pa.relative_to(ROOT)),'original_sha256':sha(pa.read_bytes()),'proposed':str(pb.relative_to(ROOT)),'proposed_sha256':sha(pb.read_bytes()),'diff':str(pd.relative_to(ROOT)),'diff_sha256':sha(pd.read_bytes()),
          'all_inline_and_display_mathematical_segments_identical':True,'every_other_block_byte_unchanged':True,'reference_order_changed_by_declared_relocation':'I16-edits-11r1' in ids})
        marker=f'EXACT_COMPARED_BLOCK_{i}'
        assert masked_before.count(a)==masked_after.count(b)==1
        masked_before=masked_before.replace(a,marker,1);masked_after=masked_after.replace(b,marker,1)
    assert masked_before==masked_after
    with Scanner(pdf_path) as scanner:
        for c in changes:
            line=c['old_source_line'];pages=sorted({p for n in range(line,line+c['old'].count('\n')+1) for p in scanner.pages(source_path,n)})
            hint=c['candidate16_read_page']
            if hint is not None:assert not pages or hint in pages,(c['guard_id'],hint,pages)
            c['candidate16_synctex_pages']=pages;c['candidate16_pages']=pages or ([hint] if hint is not None else [])
            assert c['candidate16_pages'],c['guard_id']
    proposed_path=OUT/'S6_SERIES_PUBLISH_I_candidate17_proposed_source.tex';proposed_path.write_text(after)
    diff_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_combined.diff';diff_path.write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='candidate16',tofile='candidate17/proposed')))
    receipt={'paper':'I','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation 21 November 2026','mode':'applied' if args.apply else 'prepared only',
       'before_source_sha256':SOURCE_SHA,'candidate16_pdf_sha256':PDF_SHA,'proposed_source_sha256':sha(after.encode()),'proposal':str(proposed_path.relative_to(ROOT)),
       'before_defect_log_sha256':sha(log_bytes),'existing_defect_rows':2039,'guard_files':guards_receipts,'superseded_guards':excluded,
       'bibliography_declared_supersessions':bib_supersessions,'bibliography_publication_evidence_hashes_verified':publication_evidence,
       'initial_bibliography_url_only_guards_not_applied_separately':True,'changes':changes,'archives':archives,'supplied_complete_block_replacements_verified':supplied_verified,
       'exact_forward_and_inverse_source_maps_verified':True,'all_source_outside_compared_blocks_byte_identical':True,
       'all_inline_and_display_mathematical_segments_identical':True,'all_label_target_and_bibliography_key_sequences_preserved':True,
       'citation_reference_multiset_preserved':True,'citation_reference_order_identical':False,'citation_reference_order_equal_after_exact_declared_convention_relocation':True,
       'declared_reference_relocation':{'guard_id':relocation['guard_id'],'statement_id':relocation['statement_id'],'old':relocation['old'],'new':relocation['new'],'scope':'The existing curve/conjugation reference moves from the unnumbered Section 26.6 preface to inside ari:C.7.11, immediately after StatementRecord.'},
       'sequence_counts':seq_counts,'removed_inline_symbol_mentions':0,'check_ledger_sha256':ledger_sha,'immutable_reading_and_dossier_records':protected,
       'proposed_defect_rows':len(changes),'new_defect_rows':len(changes) if args.apply else 0,'projected_total_defect_rows':2039+len(changes),
       'mathematical_events_added':0,'canonical_status_files_modified':False,
       'review_scope':'Root reviewed all included exact guard batches. Their complete owning-block reading and mathematical preservation scopes remain in the supplied receipts. This implementation verifies each separate supplied block transformation and the nonoverlapping combined transformations, including shared proofs. No independent mathematical derivation is claimed.',
       'pending':['Root final bibliography approval and canonical GO' if not args.apply else 'candidate17 clean build','Every changed candidate17 whole image actually read','Current source/PDF/provenance and final defect-page map','Remaining individual type closure review']}
    assert source_path.read_bytes()==before_bytes and log_path.read_bytes()==log_bytes
    if args.apply:
        old_rows=[dict(r) for r in rows]
        for c in changes:
            pages=','.join(map(str,c['candidate16_pages']));row={field:'' for field in fields}
            row.update({'change_id':f'I-{len(rows)+1:05d}','type':c['type'],'statement_id':c['statement_id'],
              'old_location':f"candidate16 source line {c['old_source_line']}; {c['statement_id']}",'old_page':pages,'new_location':c['statement_id'],'new_page':'pending candidate17 build',
              'old_text':c['old'],'new_text':c['new'],'reason':c['reason'],'review_status':'applied; complete supplied and combined block comparisons verified; candidate17 changed-page reading pending',
              'mapped_old_location':f"candidate16 {c['statement_id']}; pages {pages}",'mapped_new_location':'pending candidate17 build and changed-page reading',
              'page_mapping_method':f'candidate16 source-bound libsynctex plus recorded guard context; source SHA {SOURCE_SHA}; PDF SHA {PDF_SHA}'})
            rows.append(row);c['change_id']=row['change_id']
        assert rows[:2039]==old_rows
        buff=io.StringIO(newline='');writer=csv.DictWriter(buff,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
        source_path.write_text(after);log_path.write_bytes(buff.getvalue().encode())
        receipt.update({'after_source_sha256':sha(source_path.read_bytes()),'after_defect_log_sha256':sha(log_path.read_bytes()),'total_defect_rows':len(rows),'existing_log_rows_preserved':2039,'approved_bibliography_guard_sha256':args.approved_bibliography_sha})
    for path,h in protected.items():assert sha((ROOT/path).read_bytes())==h
    assert sha(ledger_path.read_bytes())==ledger_sha
    p=OUT/('S6_SERIES_PUBLISH_I_candidate16_combined_apply_receipt.json' if args.apply else 'S6_SERIES_PUBLISH_I_candidate16_combined_preparation.json')
    p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'mode':receipt['mode'],'receipt':str(p.relative_to(ROOT)),'receipt_sha256':sha(p.read_bytes()),'before_source_sha256':SOURCE_SHA,'proposed_source_sha256':receipt['proposed_source_sha256'],'after_source_sha256':receipt.get('after_source_sha256'),'after_defect_log_sha256':receipt.get('after_defect_log_sha256'),'guards':len(changes),'complete_blocks':len(archives),'projected_total_rows':2039+len(changes),'types':dict(collections.Counter(c['type'] for c in changes)),'sequence_counts':seq_counts,'mathematical_events_added':0},indent=2))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Prepare or apply one root-reviewed candidate17 batch with exact exceptions.

Input files and counts are fixed by a hashed root-written manifest. Scope
consolidation and convention relocation carry explicit retained witnesses.
All preceding page/read/type/check records are protected from mutation.
"""
from pathlib import Path
import argparse,collections,csv,datetime,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_synctex_batch import Scanner
R=Path(__file__).resolve().parents[1];O=R/'agents/i_cont_edits'
SOURCE='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF='3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
CHECKS='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
sha=lambda b:hashlib.sha256(b).hexdigest();csv.field_size_limit(100_000_000)
SCOPE='I17-infra-D11-01';RELOC='I17-edits-02'

def _math_segments(s):
 # Consume TeX control symbols in pairs: a row break followed by '(' or '['
 # must never be read as an inline/display opening delimiter.
 inline=[];display=[];i=0;n=len(s)
 env_pattern=re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}')
 command_pattern=re.compile(r'\\[A-Za-z@]+')
 def closing(start,delimiter):
  j=start
  while j<n:
   if s.startswith(delimiter,j):return j+len(delimiter)
   if s[j]=='%':
    k=s.find('\n',j);j=n if k<0 else k+1;continue
   if s[j]=='\\':j+=2;continue
   j+=1
  raise AssertionError(('unclosed mathematical delimiter',delimiter,start))
 while i<n:
  c=s[i]
  if c=='%':
   j=s.find('\n',i);i=n if j<0 else j+1;continue
  if c=='$':
   delimiter='$$' if s.startswith('$$',i) else '$'
   end=closing(i+len(delimiter),delimiter)
   (display if delimiter=='$$' else inline).append(s[i:end]);i=end;continue
  if c=='\\':
   if s.startswith('\\(',i) or s.startswith('\\[',i):
    is_display=s[i+1]=='[';end=closing(i+2,'\\]' if is_display else '\\)')
    (display if is_display else inline).append(s[i:end]);i=end;continue
   m=env_pattern.match(s,i)
   if m:
    stop='\\end{'+m[1]+'}';j=s.find(stop,i+len(m[0]));assert j>=0
    end=j+len(stop);display.append(s[i:end]);i=end;continue
   # A control word consumes its letters; a control symbol consumes exactly
   # the following character, so \\ then '(' is ordinary matrix content.
   m=command_pattern.match(s,i)
   if m:
    command=m[0];i+=len(command)
    if command=='\\verb' and i<n:
     if s[i]=='*':i+=1
     delimiter=s[i];j=s.find(delimiter,i+1);assert j>=0;i=j+1
   else:i+=2
   continue
  i+=1
 return inline,display

def math(s):return _math_segments(s)[0]
def displays(s):return _math_segments(s)[1]

def refs(s):
 return re.findall(r'\\(?:eqref|ref|cref|Cref|cite|citet|citep|SeriesRef)(?:\[[^\]]*\])?\{[^}]+\}',s)
def archive(g):
 if 'before_full_entry_path' in g:
  # The bibliography guard hashes the exact entry text without its separator;
  # its full-entry archive adds exactly one newline. Check that explicit map
  # before returning the complete file hashes. No whitespace is normalized.
  pa,pb=g['before_full_entry_path'],g['after_full_entry_path']
  old,new=g.get('before',g.get('old')),g.get('after',g.get('new'))
  assert sha(old.encode())==g['original_entry_sha256']
  assert sha(new.encode())==g['proposed_entry_sha256']
  x,y=(R/pa).read_text(),(R/pb).read_text()
  assert x==old+'\n' and y==new+'\n',g['id']
  return pa,sha(x.encode()),pb,sha(y.encode())
 if 'full_block_archive' in g:
  a=g['full_block_archive'];return (a['original'],a['original_sha256'],a['proposed'],a['proposed_sha256'])
 for keys in [('original_full_block','original_full_block_sha256','proposed_full_block','proposed_full_block_sha256'),('before_full_entry_path','original_entry_sha256','after_full_entry_path','proposed_entry_sha256'),('original_entry','original_entry_sha256','proposed_entry','proposed_entry_sha256'),('original_block','original_block_sha256','proposed_block','proposed_block_sha256')]:
  if all(k in g for k in keys):return tuple(g[k] for k in keys)
 return None

def block(text,pos):
 if pos>text.index(r'\begin{thebibliography}'):
  heads=list(re.finditer(r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}',text));h=[m for m in heads if m.start()<=pos][-1]
  ends=[m.start() for m in heads if m.start()>h.start()];end=min(ends) if ends else text.index(r'\end{thebibliography}',h.end())
  return 'bib:'+h[1],h.start(),end,'complete bibliography entry'
 heads=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|definition|cited|maintheorem|computed)\}',text));h=[m for m in heads if m.start()<=pos][-1]
 end=text.index(r'\end{'+h[1]+'}',h.end())+len(r'\end{'+h[1]+'}')
 if re.match(r'\s*\\begin\{proof\}',text[end:]):end=text.index(r'\end{proof}',end)+len(r'\end{proof}')
 assert h.start()<=pos<end
 label=re.search(r'\\label\{([^}]+)\}',text[h.start():end])[1]
 return label,h.start(),end,'complete statement and attached proof'

def write_stable(p,text):
 if p.exists():assert p.read_text()==text,('refusing changed archive',str(p))
 else:p.write_text(text)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--inputs',required=True);ap.add_argument('--apply',action='store_true');ap.add_argument('--approved-inputs-sha');a=ap.parse_args()
 ip=R/a.inputs;ib=ip.read_bytes();inputs=json.loads(ib)
 assert inputs['source_sha256']==SOURCE and inputs['root_approved']
 if a.apply:assert a.approved_inputs_sha==sha(ib),'Exact reviewed input manifest hash required.'
 source=R/'S6_SERIES_PUBLISH_I.tex';log=R/'S6_SERIES_PUBLISH_defects_I.tsv';checks=R/'CHECK_EVENTS.tsv';pdf=R/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf'
 bb=source.read_bytes();before=bb.decode();lb=log.read_bytes();assert sha(bb)==SOURCE and sha(pdf.read_bytes())==PDF and sha(checks.read_bytes())==CHECKS and '\r' not in before
 reader=csv.DictReader(io.StringIO(lb.decode()),delimiter='\t');fields=reader.fieldnames;rows=list(reader);assert len(rows)==2087
 covp='records/S6_SERIES_PUBLISH_I_candidate17_complete_coverage_snapshot.json';cov=json.loads((R/covp).read_text());assert cov['all_pages_read'] and cov['source_sha256']==SOURCE and cov['pdf_sha256']==PDF
 protected={x['reading_record']:x['reading_record_sha256'] for x in cov['pages']}
 for p in [covp,'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json','records/S6_SERIES_PUBLISH_I_candidate17_type_progress.json','records/S6_SERIES_PUBLISH_I_candidate17_type_reopen.json','records/S6_SERIES_PUBLISH_I_candidate17_scope_guard_approval.json']:
  protected[p]=sha((R/p).read_bytes())
 for p,h in protected.items():assert sha((R/p).read_bytes())==h
 changes=[];files=[];supplied={};witnesses=[]
 for item in inputs['guard_files']:
  path=item['path'];raw=(R/path).read_bytes();assert sha(raw)==item['sha256'];doc=json.loads(raw);gs=doc if isinstance(doc,list) else doc['guards'];assert len(gs)==item['count'];ids=[]
  for g in gs:
   assert g['source_sha256']==SOURCE;old=g.get('before',g.get('old'));new=g.get('after',g.get('new'));gid=g['id']
   assert isinstance(old,str) and old and isinstance(new,str) and before.count(old)==1,gid
   pos=before.index(old);arc=archive(g)
   if arc:
    pa,ha,pb,hb=arc;x=(R/pa).read_text();y=(R/pb).read_text();assert sha(x.encode())==ha and sha(y.encode())==hb and before.count(x)==1
    start=before.index(x);end=start+len(x);label=g.get('statement_id','archived-block');kind='complete bibliography entry' if pos>before.index(r'\begin{thebibliography}') else 'complete supplied statement/proof block';supplied.setdefault(arc,[]).append(gid)
   else:label,start,end,kind=block(before,pos)
   assert start<=pos and pos+len(old)<=end,(gid,'owning-block bounds')
   is_scope=gid==SCOPE
   if is_scope:
    assert g['type']=='D11' and 'D12' in g['associated_types']
    assert collections.Counter(math(old))-collections.Counter(math(new))==collections.Counter([r'$\mathcal V$'])
    assert collections.Counter(math(new))-collections.Counter(math(old))==collections.Counter()
    assert collections.Counter(refs(old))-collections.Counter(refs(new))==collections.Counter([r'\ref{push:src:B.4.12}'])
    assert collections.Counter(refs(new))-collections.Counter(refs(old))==collections.Counter()
    for w in g['retained_witnesses']:
     assert sha(w['exact_text'].encode())==w['sha256'] and before.count(w['exact_text'])==1;witnesses.append(w)
   else:assert math(old)==math(new),(gid,'inline mathematics changed')
   assert displays(old)==displays(new),(gid,'display mathematics changed')
   c={'guard_id':gid,'type':'D11/D12' if is_scope else g['type'],'statement_id':'I:quadric-parabolic-euler' if is_scope else g.get('statement_id',label),'owning_block_id':label,'old':old,'new':new,'reason':g['reason'],'old_source_line':before[:pos].count('\n')+1,'candidate17_read_page':g.get('page'),'guard_file':path,'guard_file_sha256':item['sha256'],'original_offset':pos,'block_start':start,'block_end':end,'block_kind':kind,'inline_math_segments_identical':not is_scope,'display_math_segments_identical':True,'removed_inline_mentions_in_prose':[r'$\mathcal V$'] if is_scope else [],'declared_reference_order_change':gid==RELOC,'declared_duplicate_scope_removal':is_scope}
   for k in ['cited_arxiv_version','printed_author_year_before','printed_author_year_after','publication_evidence','retained_edition','source_version_binding_receipt','source_version_binding_receipt_sha256']:
    if k in g:c[k]=g[k]
   for e in g.get('publication_evidence',[]):
    if isinstance(e,dict) and 'path' in e and 'sha256' in e:assert sha((R/e['path']).read_bytes())==e['sha256']
   for pkey,hkey in [('source_version_binding_receipt','source_version_binding_receipt_sha256')]:
    if g.get(pkey):assert sha((R/g[pkey]).read_bytes())==g[hkey]
   changes.append(c);ids.append(gid)
  files.append({'path':path,'sha256':item['sha256'],'provided_guards':len(gs),'active_ids':ids})
 assert len({c['guard_id'] for c in changes})==len(changes)
 assert SCOPE in {c['guard_id'] for c in changes} and RELOC in {c['guard_id'] for c in changes}
 ordered=sorted(changes,key=lambda c:c['original_offset'])
 for x,y in zip(ordered,ordered[1:]):assert x['original_offset']+len(x['old'])<=y['original_offset'],('overlapping literal guards',x['guard_id'],y['guard_id'])
 after=before
 for c in changes:
  assert after.count(c['old'])==1,c['guard_id'];pos=after.index(c['old']);c['applied_offset']=pos;after=after[:pos]+c['new']+after[pos+len(c['old']):]
 reverse=after
 for c in reversed(changes):
  pos=c['applied_offset'];assert reverse[pos:pos+len(c['new'])]==c['new'];reverse=reverse[:pos]+c['old']+reverse[pos+len(c['new']):]
 assert reverse==before and displays(after)==displays(before)
 permitted=before
 for c in changes:
  if c['guard_id'] in [SCOPE,RELOC]:permitted=permitted.replace(c['old'],c['new'],1)
 assert math(after)==math(permitted)
 assert refs(after)==refs(permitted),'Any unrecorded reference change must stop preparation.'
 for w in witnesses:assert after.count(w['exact_text'])==1
 counts={}
 for name,pat in [('labels',r'\\label\{([^}]+)\}'),('tag_targets',r'\\hypertarget\{(tag-[^}]+)\}'),('all_targets',r'\\hypertarget\{([^}]+)\}'),('bibliography_keys',r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}')]:
  x,y=re.findall(pat,before),re.findall(pat,after);assert x==y,name;counts[name]=len(x)
 byid={c['guard_id']:c for c in changes};verified=[]
 for (pa,ha,pb,hb),ids in supplied.items():
  x=(R/pa).read_text();y=(R/pb).read_text();t=x
  for gid in ids:
   c=byid[gid];assert t.count(c['old'])==1;t=t.replace(c['old'],c['new'],1)
  assert t==y,('supplied full-block transformation',pa,ids)
  verified.append({'original':pa,'original_sha256':ha,'proposed':pb,'proposed_sha256':hb,'individual_batch_guard_ids':ids,'exact_supplied_batch_replacement_verified':True,'combined_block_may_contain_other_reviewed_guards':True})
 groups=[]
 for c in sorted(changes,key=lambda c:(c['block_start'],c['block_end'])):
  if groups and c['block_start']<groups[-1]['end']:groups[-1]['end']=max(groups[-1]['end'],c['block_end']);groups[-1]['changes'].append(c)
  else:groups.append({'start':c['block_start'],'end':c['block_end'],'changes':[c]})
 arcs=[];masked0=before;masked1=after
 for i,g in enumerate(groups,1):
  x=before[g['start']:g['end']];y=x;ids={c['guard_id'] for c in g['changes']};gc=[c for c in changes if c['guard_id'] in ids]
  for c in gc:assert y.count(c['old'])==1;y=y.replace(c['old'],c['new'],1)
  assert after.count(y)==1 and displays(x)==displays(y)
  if SCOPE not in ids:assert math(x)==math(y)
  stem=O/f'S6_SERIES_PUBLISH_I_candidate17_combined_block_{i:02}';pa,pb,pd=[Path(str(stem)+z) for z in ['_original.tex','_proposed.tex','.diff']]
  write_stable(pa,x);write_stable(pb,y);write_stable(pd,''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile=gc[0]['owning_block_id']+'/candidate17',tofile=gc[0]['owning_block_id']+'/candidate18-proposal')))
  arcs.append({'statement_id':gc[0]['owning_block_id'],'guard_ids':[c['guard_id'] for c in gc],'original':str(pa.relative_to(R)),'original_sha256':sha(pa.read_bytes()),'proposed':str(pb.relative_to(R)),'proposed_sha256':sha(pb.read_bytes()),'diff':str(pd.relative_to(R)),'diff_sha256':sha(pd.read_bytes()),'all_inline_and_display_mathematical_segments_identical':SCOPE not in ids,'duplicate_scope_exception':SCOPE in ids,'reference_order_changed_by_declared_relocation':RELOC in ids,'every_other_block_byte_unchanged':True})
  marker=f'EXACT_COMPARED_BLOCK_{i}';assert masked0.count(x)==masked1.count(y)==1;masked0=masked0.replace(x,marker,1);masked1=masked1.replace(y,marker,1)
 assert masked0==masked1
 with Scanner(pdf) as scan:
  for c in changes:
   line=c['old_source_line'];pages=sorted({p for n in range(line,line+c['old'].count('\n')+1) for p in scan.pages(source,n)});hint=c['candidate17_read_page']
   if hint is not None:assert not pages or hint in pages,(c['guard_id'],hint,pages)
   c['candidate17_synctex_pages']=pages;c['candidate17_pages']=pages or ([hint] if hint is not None else []);assert c['candidate17_pages'],c['guard_id']
 pp=O/'S6_SERIES_PUBLISH_I_candidate18_proposed_source.tex';write_stable(pp,after);dp=O/'S6_SERIES_PUBLISH_I_candidate17_combined.diff';write_stable(dp,''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='candidate17',tofile='candidate18/proposed')))
 receipt={'paper':'I','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'applied' if a.apply else 'prepared only','input_manifest':a.inputs,'input_manifest_sha256':sha(ib),'before_source_sha256':SOURCE,'candidate17_pdf_sha256':PDF,'proposed_source_sha256':sha(after.encode()),'proposal':str(pp.relative_to(R)),'before_defect_log_sha256':sha(lb),'existing_defect_rows':2087,'guard_files':files,'changes':changes,'archives':arcs,'supplied_complete_block_replacements_verified':verified,'exact_forward_and_inverse_source_maps_verified':True,'all_source_outside_compared_blocks_byte_identical':True,'all_display_mathematical_segments_identical':True,'all_inline_mathematical_segments_identical':False,'inline_math_difference':'One duplicated mathcal V mention is removed from Remark22.30; the exact object and conclusion remain in Proposition22.29, whose witnesses are retained verbatim.','reference_difference':'One duplicated push:src:B.4.12 reference is removed with that scope recap; I17-edits-02 relocates the unchanged height/period convention reference across a statement header. All other reference order is identical.','retained_duplicate_scope_witnesses':witnesses,'all_label_target_and_bibliography_key_sequences_preserved':True,'sequence_counts':counts,'check_ledger_sha256':CHECKS,'immutable_reading_and_dossier_records':protected,'proposed_defect_rows':len(changes),'new_defect_rows':len(changes) if a.apply else 0,'projected_total_defect_rows':2087+len(changes),'mathematical_events_added':0,'canonical_status_files_modified':False,'review_scope':'Root read every exact guard and its justification, complete own and scope-comparison proofs, and the required substantive peer contexts. The full owning-proof readings by the assigned reviewers and their exact transformations remain bound. This implementation merges disjoint guards in shared complete blocks and verifies their exact inverses. It adds no independent mathematical check.','pending':['Candidate18 clean build and complete changed-image reading','Final source/PDF/ledger metadata, provenance, mapped-log and individual type closure bindings']}
 assert source.read_bytes()==bb and log.read_bytes()==lb
 out=O/('S6_SERIES_PUBLISH_I_candidate17_combined_apply_receipt.json' if a.apply else 'S6_SERIES_PUBLISH_I_candidate17_combined_preparation.json');assert not out.exists(),'Refusing to overwrite a preparation or application receipt.'
 if a.apply:
  oldrows=[dict(r) for r in rows]
  for c in changes:
   pages=','.join(map(str,c['candidate17_pages']));row={f:'' for f in fields};row.update(change_id=f'I-{len(rows)+1:05d}',type=c['type'],statement_id=c['statement_id'],old_location=f"candidate17 source line {c['old_source_line']}; {c['statement_id']}",old_page=pages,new_location=c['statement_id'],new_page='pending candidate18 build',old_text=c['old'],new_text=c['new'],reason=c['reason'],review_status='applied; complete supplied and combined block comparisons verified; candidate18 changed-page reading pending',mapped_old_location=f"candidate17 {c['statement_id']}; pages {pages}",mapped_new_location='pending candidate18 build and changed-page reading',page_mapping_method=f'candidate17 source-bound libsynctex plus recorded guard context; source SHA {SOURCE}; PDF SHA {PDF}');rows.append(row);c['change_id']=row['change_id']
  assert rows[:2087]==oldrows;buf=io.StringIO(newline='');wr=csv.DictWriter(buf,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(rows)
  source.write_text(after);log.write_bytes(buf.getvalue().encode());receipt.update(after_source_sha256=sha(source.read_bytes()),after_defect_log_sha256=sha(log.read_bytes()),total_defect_rows=len(rows),existing_log_rows_preserved=2087,approved_inputs_sha256=a.approved_inputs_sha)
 for p,h in protected.items():assert sha((R/p).read_bytes())==h
 assert sha(checks.read_bytes())==CHECKS
 out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'mode':receipt['mode'],'receipt':str(out.relative_to(R)),'receipt_sha256':sha(out.read_bytes()),'guards':len(changes),'complete_blocks':len(arcs),'proposed_source_sha256':receipt['proposed_source_sha256'],'after_source_sha256':receipt.get('after_source_sha256'),'projected_total_rows':2087+len(changes),'types':dict(collections.Counter(c['type'] for c in changes)),'sequence_counts':counts,'mathematical_events_added':0},indent=2))
if __name__=='__main__':main()

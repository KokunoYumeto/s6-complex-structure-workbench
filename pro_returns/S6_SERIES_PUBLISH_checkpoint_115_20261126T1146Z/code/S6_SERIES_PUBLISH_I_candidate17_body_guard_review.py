from pathlib import Path
import collections,datetime,hashlib,json,re
from S6_SERIES_PUBLISH_I_candidate17_combined import math,displays,refs,archive
R=Path(__file__).resolve().parents[1];sha=lambda b:hashlib.sha256(b).hexdigest();s=(R/'S6_SERIES_PUBLISH_I.tex').read_text();assert sha(s.encode())=='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
items=[('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_guards.json','8a49ba06243f370c33c745a19e5f704c0a1ffdfcc8c10b62f537b756518b2855',23),('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_edits_guards.json','e08c416b9e1e7c3f4e8ed6d00914e730a5049617994a353f144d448fe10b7721',17),('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_provenance_guards.json','2b65de6c9b3d179d50d04cefb80f79335f2bece4418d3ec669cd15268bae9413',23),('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_infra_scope_guard_final.json','3738aa0d31ffe41714812f441d5a0ebdaad47874d22ee5d34ed7b1bfb46627dd',1)]
allg=[];supplied={}
for f,h,n in items:
 b=(R/f).read_bytes();assert sha(b)==h;d=json.loads(b);gs=d if isinstance(d,list) else d['guards'];assert len(gs)==n
 for g in gs:
  assert s.count(g['before'])==1
  if g['id']!='I17-infra-D11-01':assert math(g['before'])==math(g['after'])
  assert displays(g['before'])==displays(g['after'])
  a=archive(g)
  if a:supplied.setdefault(a,[]).append(g)
  allg.append(g)
ordered=sorted(allg,key=lambda g:s.index(g['before']))
for a,b in zip(ordered,ordered[1:]):assert s.index(a['before'])+len(a['before'])<=s.index(b['before']),(a['id'],b['id'])
for (pa,ha,pb,hb),gs in supplied.items():
 a=(R/pa).read_text();b=(R/pb).read_text();assert sha(a.encode())==ha and sha(b.encode())==hb and s.count(a)==1
 for g in gs:assert a.count(g['before'])==1;a=a.replace(g['before'],g['after'],1)
 assert a==b,pa
out=s;inverse=[]
for g in allg:
 p=out.index(g['before']);inverse.append((p,g['before'],g['after']));out=out[:p]+g['after']+out[p+len(g['before']):]
r=out
for p,b,a in reversed(inverse):assert r[p:p+len(a)]==a;r=r[:p]+b+r[p+len(a):]
assert r==s
permitted=s
for g in allg:
 if g['id'] in ['I17-edits-02','I17-infra-D11-01']:permitted=permitted.replace(g['before'],g['after'],1)
assert math(out)==math(permitted) and displays(out)==displays(s) and refs(out)==refs(permitted)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:assert re.findall(pat,s)==re.findall(pat,out)
# The referenced full proposition/proof is an unchanged exact retained witness.
w=R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_scope_comparison_B412.tex';assert out.count(w.read_text())==1
for g in allg:
 if g['id']=='I17-infra-D11-01':
  for w in g['retained_witnesses']:assert sha(w['exact_text'].encode())==w['sha256'] and out.count(w['exact_text'])==1
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(s.encode()),'root_approved':True,'guard_files':[{'path':f,'sha256':h,'count':n} for f,h,n in items],'guards':len(allg),'supplied_complete_block_replacements_verified':len(supplied),'exact_forward_and_inverse_verified':True,'all_labels_and_targets_preserved':True,'displays_identical':True,'inline_and_reference_scope_exceptions':['I17-edits-02 exact convention-reference relocation','I17-infra-D11-01 duplicate symbol/reference removed with retained exact proposition/proof witnesses'],'body_proposal_sha256_without_bibliography':sha(out.encode()),'review':'Root read all64 complete literal before/after pairs and their individual reasons; root read the complete16 own affected statements/proofs and both duplicated-scope blocks. The editor and provenance reviewer independently owned and read their complete affected blocks, with source/page bindings and exact comparisons. This integrates their editorial findings and gives no independent mathematical-check credit.','source_modified':False,'mathematical_events_added':0,'remaining':'The comprehensive bibliography batch must be merged and verified before any canonical source/log application.'}
p=R/'records/S6_SERIES_PUBLISH_I_candidate17_body_guard_review.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'guards':len(allg),'full_block_supplied_archives':len(supplied),'record':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'source_unchanged':True}))

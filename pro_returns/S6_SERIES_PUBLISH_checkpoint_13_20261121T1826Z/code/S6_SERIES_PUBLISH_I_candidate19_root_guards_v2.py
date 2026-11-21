#!/usr/bin/env python3
"""Archive two further complete-proof comparisons from the bounded recap scan."""
from pathlib import Path
import datetime, difflib, hashlib, json
R=Path(__file__).resolve().parents[1];O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
s=(R/'S6_SERIES_PUBLISH_I.tex').read_text();assert sha(s.encode())=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
prior=O/'S6_SERIES_PUBLISH_I_candidate19_root_guards.json';assert sha(prior.read_bytes())=='c56a3f08d9f47d18b06c1e238d34467cb1a6991363bccbaf80e8cd68b21691a0'
xdoc=json.loads(prior.read_text());guards=xdoc['guards'][:]
items=[('I19-root-02','fam:src:C.3.1','proposition',74,'identity subgroup is closed. This proves the last assertion.','identity subgroup is closed.','The full matrix, rank and kernel computation, rational-line lattice criterion, noncompact direction, closed-subgroup classification, countability argument and Hausdorff quotient criterion are retained. Delete only the last assertion recap after that exact criterion.'),('I19-root-03','mapsI:src:A.2.1','theorem',110,'on a common smaller collar.  This proves the assertion.','on a common smaller collar.','The boundary circle extension, homotopy extension, relative smooth approximation, smooth product map, H1 injection, vanishing relative H1, relative homotopy and common-smaller-collar comparison are retained. Delete only the closing assertion recap.')]
for gid,sid,env,page,old,new,reason in items:
 pos=s.index('\\label{'+sid+'}');a=s.rfind('\\begin{'+env+'}',0,pos);b=s.index(r'\end{proof}',pos)+len(r'\end{proof}')
 x=s[a:b];assert x.count(old)==s.count(old)==1;y=x.replace(old,new,1)
 assert '\\' not in old and '$' not in old and '\\' not in new and '$' not in new
 num=len(guards)+1;stem='S6_SERIES_PUBLISH_I_candidate19_root_v2_block_'+str(num).zfill(2)
 pa=O/(stem+'_original.tex');pb=O/(stem+'_proposed.tex');pd=O/(stem+'.diff')
 for p,t in [(pa,x),(pb,y),(pd,''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile='candidate19/'+sid,tofile='body-proposal/'+sid)))]:
  assert not p.exists();p.write_text(t)
 guards.append({'id':gid,'type':'D08','statement_id':sid,'page':None,'source_sha256':sha(s.encode()),'old':old,'new':new,'reason':reason,'original_full_block':str(pa.relative_to(R)),'original_full_block_sha256':sha(x.encode()),'proposed_full_block':str(pb.relative_to(R)),'proposed_full_block_sha256':sha(y.encode()),'source_lines':[s[:a].count('\n')+1,s[:b].count('\n')+1],'root_review':{'reader':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; root, continuation of 21 November 2026','complete_original_statement_and_proof_actually_read':True,'complete_proposed_difference_actually_compared':True,'comparison_scope':'Root actually read the full current statement and attached proof, then compared the exact deletion. Every formula and every operative proof sentence remains verbatim. The removed final sentence only points back to the already derived assertion. This is a comparative rereading after exposure to the argument; no independent derivation is claimed.'}})
xdoc.update(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),guards=guards,prior_guard_record={'path':str(prior.relative_to(R)),'sha256':sha(prior.read_bytes())},bounded_scan_scope='The current-source vague assertion-ending scan yielded seven contexts, including two already assigned editor findings. Root read the two complete short owning proofs archived here. Three other contexts were assigned for actual complete-proof review and disposition by the continuation readers. No general closure is inferred from absence of matches.')
p=O/'S6_SERIES_PUBLISH_I_candidate19_root_guards_v2.json';assert not p.exists();p.write_text(json.dumps(xdoc,indent=2)+'\n')
print(json.dumps({'record':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'guards':len(guards),'additional_owners':[i[1] for i in items]},indent=2))

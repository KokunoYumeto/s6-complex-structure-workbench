#!/usr/bin/env python3
"""Bind the seven actually compared candidate19 body edits for preparation."""
from pathlib import Path
import datetime,hashlib,json,importlib.util,re
R=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def bound(n,h=None):
 p=R/n
 if h:assert sha(p)==h,n
 return {'path':n,'sha256':sha(p)}
sp=R/'S6_SERIES_PUBLISH_I.tex';s=sp.read_text();ss=sha(sp)
assert ss=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
files=[
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_root_guards_v2.json','6446e98599ce8041bd8011dc6d9587e5200a47ac811b045f37d72777c643607f',3),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_guards.json','56b12244b978b1aa803b42251a7cc5fbcc9dda814093c781b7a3df39c2e32c8f',2),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_additional_guard.json','bbb3e1fce17a51ae801f071f4cb20a13c69bb5467bb93959286f6d1b5fd245af',1),
 ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate19_provenance_guards.json','ee915f4a11d1c2aa85c09f35f0710d0e4a1689fd06f76fc395564e8abb63b479',1)]
spec=importlib.util.spec_from_file_location('review_maps',R/'code/S6_SERIES_PUBLISH_I_candidate18_combined.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
gfs=[];comparisons=[];changes=[]
for n,h,num in files:
 v=bound(n,h);doc=json.loads((R/n).read_text());guards=doc if isinstance(doc,list) else doc['guards'];assert len(guards)==num;gfs.append(dict(v,count=num))
 for g in guards:
  old=g.get('old',g.get('before'));new=g.get('new',g.get('after'));assert g['source_sha256']==ss and g['type']=='D08'
  assert s.count(old)==1
  pa,ha,pb,hb=m.archive(g);x=(R/pa).read_text();y=(R/pb).read_text();bound(pa,ha);bound(pb,hb)
  assert s.count(x)==1 and x.count(old)==1 and x.replace(old,new,1)==y
  assert m.math_segments(x)==m.math_segments(y) and m.refs(x)==m.refs(y)
  assert re.findall(r'\\[A-Za-z@]+|\\.',x)==re.findall(r'\\[A-Za-z@]+|\\.',y)
  comparisons.append({'statement_id':g['statement_id'],'guard_id':g['id'],'original':bound(pa,ha),'proposed':bound(pb,hb),'exact_literal_map':True,'all_math_and_reference_sequences_identical':True,'root_actually_read_complete_proof_in_this_comparison':g['id'].startswith('I19-root-'),'actual_complete_proof_reviewer':'root' if g['id'].startswith('I19-root-') else ('editing reader' if g['id'].startswith('I19-edits-') else 'provenance reader')})
  changes.append({'guard_id':g['id'],'statement_id':g['statement_id'],'old':old,'new':new,'reason':g['reason'],'root_read_exact_pair':True})
assert len(changes)==7 and len({x['guard_id'] for x in changes})==7
reviews=[bound(n,h) for n,h in [
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_full_pair_review.json','8ff0f61b682fe8eb71161f264f30080f931642ffe4ac32a6367e19e0ff947ef2'),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_additional_full_pair_review.json','f437d1143881f8b5fe69af64a2548901c5833238c515132bd34bb2857290820d'),
 ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate19_provenance_full_pair_review.json','5a1002a24adb5b5da0410f02cc000318489b3b065e9e175f3167a0fe454ce6ce'),
 ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate19_ariC61_recap_disposition.json','da82c70d61e2742f72f0be3ea4798fefe59b05f17971a8d7aeac7f3d092b015f')]]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
review={'paper':'I','candidate':19,'created_utc':now,'source_sha256':ss,'root_review_scope':'Root actually read all three complete original root-owned statements/proofs and compared their exact changes. Root read all seven exact old/new pairs and their stated retained operative arguments. The other four complete original/proposed proof pairs were actually read by the explicitly named editing/provenance readers; their immutable full-pair receipts are bound here. Exact full-block source maps, mathematical segments, command sequences and references are independently checked by this helper. No new derivation, independent proof or computation is claimed.','comparisons':comparisons,'exact_pairs_read_by_root':changes,'manual_reader_evidence':reviews,'retained_context':'ari:C.6.1 keeps its final A_t deduction under the bound complete-context disposition; no guard is applied there.','root_approved':True,'source_changed':False,'events_added_by_approval':0}
rp=R/'records/S6_SERIES_PUBLISH_I_candidate19_root_review.json';assert not rp.exists();rp.write_text(json.dumps(review,indent=2)+'\n')
manifest={'paper':'I','candidate':19,'created_utc':now,'source_sha256':ss,'pdf_sha256':sha(R/'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf'),'root_approved':True,'approved_guard_count':7,'guard_files':gfs,'complete_coverage':bound('records/S6_SERIES_PUBLISH_I_candidate19_complete_coverage_snapshot.json','c00de02dea2fbd759e61c88ed289adab670ffb62f6bf7eb06cf10c3e33534b93'),'root_review':bound(str(rp.relative_to(R))),'review_evidence':reviews,'protected_records':[bound(n) for n in ['records/S6_SERIES_PUBLISH_I_candidate19_type_progress.json','records/S6_SERIES_PUBLISH_progress_review_07.json','agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_type_closure_preparation_v3.json','agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_recap_preparation.json']],'review_scope':review['root_review_scope'],'pending_after_application':['Final actual-rereading ledger append and methodology count correction','Candidate20 clean build, actual changed-image reading and final source/PDF/provenance bindings']}
p=R/'records/S6_SERIES_PUBLISH_I_candidate19_root_approved_inputs.json';assert not p.exists();p.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'manifest':str(p.relative_to(R)),'manifest_sha256':sha(p),'review':str(rp.relative_to(R)),'review_sha256':sha(rp),'guard_count':7},indent=2))

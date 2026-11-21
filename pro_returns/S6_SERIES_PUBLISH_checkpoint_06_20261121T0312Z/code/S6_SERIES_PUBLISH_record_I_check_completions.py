from pathlib import Path
import json,hashlib,datetime
r=Path(__file__).resolve().parents[1]
p=r/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
d=json.loads(p.read_text()) if p.exists() else {'schema':1,'rows':{}}
groups=[
 (['mapsI:src:A.1.1','mapsI:src:A.1.2','mapsI:src:A.2.1'],'agents/i_provenance/S6_SERIES_PUBLISH_I_circle_checks.md','Full statement-directed derivations and complete target comparisons; A2.1 uses the explicitly declared cusp-group input, whose independent proof check is separately tracked.'),
 (['night:P2.3','night:P2.11'],'agents/i_topology/S6_SERIES_PUBLISH_I_P23_P211_comparisons.md','Full statement-directed derivations and complete printed-proof comparisons; fresh finite-action and virtual-Chern calculations have their precise scopes recorded.'),
 (['push:src:D.1.3','push:src:D.2.3','push:src:D.3.2'],'agents/i_topology/S6_SERIES_PUBLISH_I_D23_D13_D32_centralizer_comparisons.md','Complete three target statements checked; the full arbitrary-limit D3.1 theorem is a separately declared input and is not recredited.'),
 (['ari:C.6.4'],'agents/i_provenance/S6_SERIES_PUBLISH_I_C64_check.md','Complete target checked from stated height/division inputs, with fresh local valuation calculations; the division polynomials themselves remain cited inputs.'),
 (['ari:C.8.9','ari:C.8.10'],'records/S6_SERIES_PUBLISH_I_C89_C810_root_comparison.md','Complete target proofs compared after frozen derivation; one common evidence group and precise pre/post-exposure computational scope.'),
 (['push:src:B.4.1','push:src:B.5.1'],'records/S6_SERIES_PUBLISH_I_B41_B51_root_comparison.md','Complete historical corollary scopes derived from the known P2.7 input before original target proofs; exact specialization and inclusion maps recorded.'),
 (['push:src:A.1.1','push:src:A.1.2'],'agents/i_provenance/S6_SERIES_PUBLISH_I_push_A12_applied_comparison.json','Frozen full target derivations and fresh integral computations are compared completely. A1.2 selected-diagonal chart error is repaired, and the complete applied proof is bound by this receipt to the corrected source. Same evidence group; theorem unchanged.'),
 (['push:src:A.2.1','push:src:A.2.2'],'agents/i_analytic/S6_SERIES_PUBLISH_I_push_A2_comparison.md','Complete target statements derived before reading the target proofs. The first new computation matched the historical method; a genuinely different Boolean-chain/Smith/character computation was performed after exposure and is timed explicitly. Extra crepant/flop assertions receive exposed-reread credit only.')]
now=datetime.datetime.now(datetime.timezone.utc).isoformat();added=[]
for labels,rel,scope in groups:
 q=r/rel;assert q.exists(),q
 for lab in labels:
  if lab in d['rows']:continue
  d['rows'][lab]={'paper':'I','status':'done','recorded_utc':now,'evidence_path':rel,'evidence_sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'scope':scope}
  added.append(lab)
d['updated_utc']=now;p.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'manifest':str(p),'added':added,'rows':len(d['rows'])}))

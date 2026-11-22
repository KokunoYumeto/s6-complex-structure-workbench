from pathlib import Path
import csv,hashlib,json
r=Path(__file__).resolve().parents[1]
out=r/'records/S6_SERIES_PUBLISH_I_root_nonfilling_alias_CHECK_EVENTS.tsv'
assert not out.exists()
rows=[]
for label,suffix in [('push:src:B.4.1','B41'),('push:src:B.5.1','B51')]:
 rows.append({'statement_id':label,'date':'2026-11-21','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH root',
 'type':'targeted proof check','outcome':'PASS complete corollary conclusion: exact canonical-tuple specialization and inclusion of proposed filling classes derived and frozen before original target proof. Full original proof then compared. Earlier complete P2.7 proof exposure disclosed; no independent reproof of that input and no monodromy calculation credited.',
 'event_id':'publish-I-root-nonfilling-'+suffix+'-20261121','phase':'Paper I historical corollary scope check',
 'source_file':'work/records/S6_SERIES_PUBLISH_I_B41_B51_root_comparison.md','source_row':'',
 'source_event_type':'targeted proof check','evidence_group':'publish-I-root-nonfilling-alias-specializations-20261121'})
with out.open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'path':str(out),'rows':len(rows),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))

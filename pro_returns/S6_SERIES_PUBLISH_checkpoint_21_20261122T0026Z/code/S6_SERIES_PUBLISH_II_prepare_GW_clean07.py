"""Bind the reviewed GW pair and add bibliography owners to a new root copy."""
from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1]
def b(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
def w(p,d):
    p=R/p;assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
p='agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group07/S6_SERIES_PUBLISH_II_clean_group07_final_proposals.json'
assert b(p)['sha256']=='4bbe1445334b3283cea38602abb1497c4ea9d7581cd28b610cb356a8e7112908'
d=json.loads((R/p).read_text())
for x in d['bibliography_guards']:
    x['statement_owner']='bib:'+x['change_id'].split('-BIB-',1)[1]
d['root_original_agent_bundle']=b(p)
d['root_actual_reading_scope']=('The complete original and final proposed GW statement/proof, full frozen derivation, full comparison, all ten owner guards, all three bibliography pairs, fresh determinant program and complete output, primary locator reading and official source-version receipts were actually read by root. Primary page-image readings are credited to the checker only.')
d['root_rereading_completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
out='records/S6_SERIES_PUBLISH_II_GW_reviewed_proposals.json';w(out,d)
cfg='records/S6_SERIES_PUBLISH_II_GW_prepare_config.json'
w(cfg,dict(proposal=b(out),source_before_sha256='e79da9d0e170bfe2ff2264024fa5c1900089faadf82dab34effb0e03b182de64',
 root_actual_complete_pairs_read=True,root_review_scope=d['root_actual_reading_scope'],
 output='records/S6_SERIES_PUBLISH_II_GW_editorial_guard.json',expected_patch_count=13,
 mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=b(out),prepare_config=b(cfg))))

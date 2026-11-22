"""Bind the actually reviewed WT pair, computations and exact bibliography edition."""
from pathlib import Path
import datetime, hashlib, json
R=Path(__file__).resolve().parents[1]
def bound(p): return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
def read(p): return json.loads((R/p).read_text())
def write(p,d):
    out=R/p
    assert not out.exists()
    out.write_text(json.dumps(d,indent=2)+'\n')
base='agents/ii_checks_A/recovery_20261121T195642Z/'
index=base+'S6_SERIES_PUBLISH_II_A_recovery_group07_WT_final_index.json'
assert bound(index)['sha256']=='f647467a2b27f332a1a317bdf7e7cebf3887140ed061eaf06b6db6378d65e87b'
idx=read(index)
for x in idx['files']: assert bound(x['path'])==x
proposal=base+'group07_WT/S6_SERIES_PUBLISH_II_A_02WT_editorial_proposals.json'
d=read(proposal); block=d['blocks'][0]; assert block['tag']=='02WT' and len(d['blocks'])==1
old,new=bound(block['original_path']),bound(block['proposed_path'])
assert old['sha256']==block['original_sha256'] and new['sha256']==block['proposed_sha256']
freeze=next(x for x in idx['files'] if x['path'].endswith('S6_SERIES_PUBLISH_derivation_freeze_receipt.json'))
release=next(x for x in idx['files'] if x['path'].endswith('S6_SERIES_PUBLISH_release_receipt.json'))
fr,rr=read(freeze['path']),read(release['path'])
assert fr['statement_owner']==rr['statement_owner']=='night:P4.21'
assert (R/rr['full_owning_block_path']).read_text().rstrip('\n')==(R/old['path']).read_text().rstrip('\n')
cur=(R/old['path']).read_text(); guards=[]
for g in d['guards']:
    assert hashlib.sha256(cur.encode()).hexdigest()==g['intermediate_before_sha256']
    a=g['offset_before']; assert cur[a:a+len(g['literal_old'])]==g['literal_old']
    assert cur.count(g['literal_old'])==1
    cur=cur[:a]+g['literal_new']+cur[a+len(g['literal_old']):]
    assert hashlib.sha256(cur.encode()).hexdigest()==g['intermediate_after_sha256']
    guards.append(dict(change_id=g['guard_id'],old=g['literal_old'],new=g['literal_new'],
        defect_type='/'.join(g['defect_types']),reason=g['reason']+' Exact transport: '+g['mathematical_transport']))
assert cur==(R/new['path']).read_text()
scope=('Root and checker read the complete original and proposed statement and all seven proof items. '
       'Root also read the entire frozen derivation, full comparison, all ten guards, both full programs '
       'and every output data row, all event scopes and the complete proposed bibliography entry. '
       'Primary book-page readings are credited to the checker at the bound scopes; the timing and output-reading precision supplement is retained.')
target=dict(tag='02WT',statement_owner='night:P4.21',checker='ii_check_a',freeze_receipt=freeze,
    frozen_derivation=bound(fr['frozen_derivation_path']),release_receipt=release,original_full_block=old,
    proposed_full_block=new,comparison='All seven proof items compared; single-support e(S)=2 proved through the exact normalization and conductor maps.',
    full_comparison=bound(base+'S6_SERIES_PUBLISH_II_A_02WT_comparison.md'),
    actual_complete_original_proof_read=True,actual_complete_proposed_proof_read=True,
    rereading=bound(base+'group07_WT/S6_SERIES_PUBLISH_II_A_02WT_reread.json'),guards=guards)
bib=(R/(base+'group07_WT/S6_SERIES_PUBLISH_II_A_02WT_bibliography_entry.tex')).read_text()
out='records/S6_SERIES_PUBLISH_II_WT_reviewed_proposals.json'
standard=dict(paper='II',final_index=bound(index),bound_inputs=idx['files'],targets=[target],
    complete_computations=[bound('code/S6_SERIES_PUBLISH_II_A_02WT_'+name+'.'+ext)
        for name in ['cells','postrelease_cases'] for ext in ['py','out']],
    bibliography_guards=[dict(change_id='II-WT-BEAUVILLE1978-BIB',statement_owner='bib:Beauville1978',
        old=r'\end{thebibliography}',new=bib+r'\end{thebibliography}',defect_type='D18',
        reason='Add the exact opened 1978 Astérisque edition with its publisher archive URL; do not substitute locators from another edition.')],
    root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),root_reading_scope=scope)
write(out,standard)
cfg='records/S6_SERIES_PUBLISH_II_WT_prepare_config.json'
write(cfg,dict(proposal=bound(out),source_before_sha256='9af7716f1c3e43910f389434a988738acf4a982ccd313365ac2acef765f66c30',
    root_actual_complete_pairs_read=True,root_review_scope=scope,output='records/S6_SERIES_PUBLISH_II_WT_editorial_guard.json',
    expected_patch_count=11,mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(out),prepare_config=bound(cfg))))

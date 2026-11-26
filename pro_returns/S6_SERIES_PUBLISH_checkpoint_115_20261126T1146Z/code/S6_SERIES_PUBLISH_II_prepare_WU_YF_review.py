"""Bind the two fully read ruled-normalization proofs and disclosed corrections."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
def sha(x):return hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
def b(p):return dict(path=p,sha256=sha((R/p).read_bytes()))
def read(p):return json.loads((R/p).read_text())
def write(p,d):
    p=R/p;assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
base='agents/ii_checks_A/recovery_20261121T195642Z/'
index=base+'S6_SERIES_PUBLISH_II_A_recovery_group08_WU_YF_final_index.json'
assert b(index)['sha256']=='7b7cec2770ca8384f50f3d32f75fd7fc1a06b0b96108837ebfd844995bd6dc4c'
ix=read(index)
for x in ix['files']:assert b(x['path'])==x
gp=base+'group08_WU_YF/S6_SERIES_PUBLISH_II_A_WU_YF_editorial_proposals.json'
ep=base+'group08_WU_YF/S6_SERIES_PUBLISH_II_A_WU_YF_event_proposals.json'
cp=base+'S6_SERIES_PUBLISH_II_A_WU_YF_comparison.md'
d,e=read(gp),read(ep)
assert b('S6_SERIES_PUBLISH_II.tex')['sha256']=='b9d45214635cb0f0864927eb1213b2a257c95776768a607ec2e4e6341ab9342f'
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
targets=[]
for block in d['blocks']:
    tag=block['tag'];owner={'02WU':'night:P4.22','02YF':'night:P4R.3'}[tag]
    original=b(block['original_path']);proposed=b(block['proposed_path'])
    assert original['sha256']==block['original_sha256'] and proposed['sha256']==block['proposed_sha256']
    cur=(R/original['path']).read_text();assert s.count(cur)==1
    guards=[]
    for g in [x for x in d['guards'] if x['tag']==tag]:
        assert sha(cur)==g['intermediate_before_sha256']
        assert cur.count(g['literal_old'])==1 and cur.index(g['literal_old'])==g['offset_before']
        cur=cur.replace(g['literal_old'],g['literal_new'],1)
        assert sha(cur)==g['intermediate_after_sha256']
        guards.append(dict(change_id=g['guard_id'],old=g['literal_old'],new=g['literal_new'],defect_type='/'.join(g['defect_types']),reason=g['reason']+' '+g['mathematical_transport']))
    assert cur==(R/proposed['path']).read_text()
    fp=next(x['path'] for x in ix['files'] if f'derivation_freezes/{tag}/' in x['path'])
    rp=next(x['path'] for x in ix['files'] if f'released_proofs/{tag}/' in x['path'])
    f=read(fp)
    targets.append(dict(tag=tag,statement_owner=owner,checker='ii_check_a',freeze_receipt=b(fp),release_receipt=b(rp),frozen_derivation=b(f['frozen_derivation_path']),
        original_full_block=original,proposed_full_block=proposed,actual_complete_original_proof_read=True,actual_complete_proposed_proof_read=True,
        comparison='All original and proposed proof items, exact maps, coefficients and equality cases read and compared; the separately bound correction preserves the YF frozen bytes and discloses its stronger auxiliary homotopy assertion.',full_comparison=b(cp),guards=guards))
scope=('Root actually read both entire original/proposed statement-and-proof pairs (five WU items and eight YF items), both entire frozen derivations, the full comparison and explicit YF postrelease correction, all twenty-one exact guards and six event outcomes. Root read the whole prerelease cell/branch program, both postrelease supplement programs, the related historical conductor-jet program, and every data row in all four outputs, including all sixty-four divisor snapshots. All thirty-three final-index bindings are verified. Primary Beauville reading belongs to the checker. The frozen YF assertion of a homotopy equivalence is explicitly corrected through q, i, their fundamental-group maps and the killed P1 H2 classes; it adds no independent credit. The original printed proof asserts the required fundamental-group isomorphism. No Paper II page-image reading is claimed.')
out='records/S6_SERIES_PUBLISH_II_WU_YF_reviewed_proposals.json'
write(out,dict(paper='II',targets=targets,bibliography_guards=[],bound_inputs=[b(index)]+ix['files'],root_reading_scope=scope,
    existing_Beauville_entry='The primary entry was already applied in CLEAN15; no duplicate bibliography edit is proposed.',
    root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
cfg='records/S6_SERIES_PUBLISH_II_WU_YF_prepare_config.json'
write(cfg,dict(proposal=b(out),source_before_sha256=b('S6_SERIES_PUBLISH_II.tex')['sha256'],root_actual_complete_pairs_read=True,root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_WU_YF_editorial_guard.json',expected_patch_count=21,mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=b(out),events=b(ep),prepare_config=b(cfg)),indent=2))

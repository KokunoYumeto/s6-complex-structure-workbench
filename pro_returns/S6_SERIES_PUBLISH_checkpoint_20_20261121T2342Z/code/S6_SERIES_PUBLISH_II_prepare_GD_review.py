"""Bind the fully read GD proof, exact morphisms and legacy-number map."""
from pathlib import Path
import hashlib,json,re,datetime
R=Path(__file__).resolve().parents[1]
def b(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
def read(p):return json.loads((R/p).read_text())
def write(p,d):
    p=R/p;assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
base='agents/ii_infra/recovery_20261121/'
gp=base+'S6_SERIES_PUBLISH_II_01GD_guards_v3.json'
cp=base+'S6_SERIES_PUBLISH_II_01GD_comparison.json'
assert b(gp)['sha256']=='f1fd38bd6f2dad2813e659d975b2dda478cc25cd3559ebc5c83fc6cf6c5352ff'
assert b(cp)['sha256']=='05c22ba4abe7f4fdf7b6a2168d8144007ccfc735a74d1978a8c74f931da63517'
d,c=read(gp),read(cp);owner,bib=d['guards'];s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert b('S6_SERIES_PUBLISH_II.tex')['sha256']=='6f01f829aad267a6c80069240790783c7c0748c1a5453a04fb5761bfac587e99'
assert s.count(owner['before'])==s.count(bib['before'])==1
cur=owner['before'];guards=[]
for i,g in enumerate(owner['literal_edits'],1):
    assert cur.count(g['before'])==1
    assert cur.index(g['before'])==g['sequential_before_offset']
    cur=cur.replace(g['before'],g['after'],1)
    guards.append(dict(change_id=f'II-GD-{i:03d}',old=g['before'],new=g['after'],defect_type=g['type'],
        reason=g['reason']+' '+g.get('exact_mathematical_witness','')))
assert cur==owner['after'] and len(guards)==13
for x in [owner,bib]:
    for stem in (['original_full_block','proposed_full_block'] if 'tag' in x else ['original_entry','proposed_entry']):
        assert b(x[stem])['sha256']==x[stem+'_sha256']
start=s.index(owner['before']);end=start+len(owner['before']);hits=[]
for m in re.finditer(r'(?<![A-Za-z.])D\.20(?![A-Za-z0-9.])',s):
    prefix=s[max(0,m.start()-35):m.start()]
    inside=start<=m.start()<end
    label_reference=prefix.endswith('cdp:eq:')
    assert inside or label_reference
    hits.append(dict(char_start=m.start(),line=s[:m.start()].count('\n')+1,
        context=s[max(0,m.start()-65):m.end()+85],inside_owner=inside,
        disposition='Owner occurrence transported by the full proof guard.' if inside else 'Exact label reference already follows the current equation counter.'))
assert len(hits)==6
mapping='records/S6_SERIES_PUBLISH_II_GD_incoming_identity_map.json'
write(mapping,dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=b('S6_SERIES_PUBLISH_II.tex'),
    old_printed_number='D.20',preserved_label='cdp:eq:D.20',preserved_hypertarget='tag-0197',new_number='ordinary paper equation counter',
    search_pattern=r'(?<![A-Za-z.])D\.20(?![A-Za-z0-9.])',exact_hits=hits,
    excluded_longer_tokens=['C.RD.20','C.DD.20'],outside_owner_literal_receivers=0,
    related_input_transport='The one GD literal D.18--D.19 receiver of the already applied GA change becomes the exact two eqrefs in this same proof guard.',
    actual_root_reading='All exact hits and the complete GD old/new blocks were read; no whole-proof reading or independent-check credit is claimed for the longer excluded-token owners.'))
fr=read(c['freeze_receipt']['path'])
scope=('Root and checker read the whole original and proposed five-item proof, full frozen derivation, '
       'five-step comparison, every literal guard, both bibliography entries, and the complete sparse-polynomial '
       'program and output. Root also read the exact incoming-number contexts and primary-input receipt. '
       'The four primary resolution page-image readings are credited to the checker only.')
target=dict(tag='01GD',statement_owner='cdp:st:D.2.6',checker='restore_build',
    freeze_receipt=b(c['freeze_receipt']['path']),release_receipt=b(c['release_receipt']['path']),
    frozen_derivation=b(fr['frozen_derivation_path']),original_full_block=b(owner['original_full_block']),
    proposed_full_block=b(owner['proposed_full_block']),actual_complete_original_proof_read=True,
    actual_complete_proposed_proof_read=True,comparison='All five steps verified, with the resolved direct image, holomorphic period section, exact Plücker inverse and evaluation quotient.',
    full_comparison=b(cp),guards=guards)
out='records/S6_SERIES_PUBLISH_II_GD_reviewed_proposals.json'
write(out,dict(paper='II',targets=[target],bound_inputs=[b(gp),b(cp),b(mapping),b(base+'S6_SERIES_PUBLISH_II_01GD_input_bindings.json'),
    b(base+'GD_primary_inputs/S6_SERIES_PUBLISH_II_01GD_primary_input_receipt.json'),
    b(base+'S6_SERIES_PUBLISH_II_01GD_plucker_exact.py'),b(base+'S6_SERIES_PUBLISH_II_01GD_plucker_exact_output.json')],
    bibliography_guards=[dict(change_id='II-GD-BM1997-BIB',statement_owner=bib['statement_id'],old=bib['before'],new=bib['after'],
        defect_type=bib['type'],reason=bib['reason'])],root_reading_scope=scope,
    root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
event='records/S6_SERIES_PUBLISH_II_GD_reviewed_event_proposals.json'
write(event,dict(original_agent_event_proposal=b(base+'S6_SERIES_PUBLISH_II_01GD_event_proposals.json'),
    comparison=b(cp),events=[dict(statement_owner='cdp:st:D.2.6',event_type='targeted proof check',event_count=1,
        scope='Independently derived the marked period and relative Albanese group extensions before target release. The actual resolution fibre pullbacks, natural cup-product isomorphism, primitive-order positive-limit argument, explicit Plücker inverse and evaluation-lattice quotient are fully proved. The frozen derivation precedes release and all five printed steps were then compared.'),
        dict(statement_owner='cdp:st:D.2.6',event_type='used and rechecked in this run',event_count=1,
        scope='Actually read the complete original and final five-item proof and both bibliography entries. Verified the resolved direct-image map and top-form pullback, coefficient-ideal and residue inputs, positive lower bound, holomorphic class in a flat frame, exact two-plane kernel and proper compact-parallelotope quotient. Read all fresh postrelease polynomial coefficients; they add no independent-check credit.')],events_added=0))
cfg='records/S6_SERIES_PUBLISH_II_GD_prepare_config.json'
write(cfg,dict(proposal=b(out),source_before_sha256=b('S6_SERIES_PUBLISH_II.tex')['sha256'],
    root_actual_complete_pairs_read=True,root_review_scope=scope,output='records/S6_SERIES_PUBLISH_II_GD_editorial_guard.json',
    expected_patch_count=14,mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=b(out),events=b(event),prepare_config=b(cfg),incoming_map=b(mapping))))

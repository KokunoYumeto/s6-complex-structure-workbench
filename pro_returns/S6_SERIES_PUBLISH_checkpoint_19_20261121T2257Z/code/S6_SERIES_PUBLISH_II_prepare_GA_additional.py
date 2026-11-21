"""Bind the fully reviewed additional GA proof without changing the required index."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
B=Path('agents/ii_infra/recovery_20261121/GA_extra_target')
def b(p):
    p=str(p);return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
def read(p):return json.loads((R/p).read_text())
def write(p,d):
    p=R/p;assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
gp=B/'S6_SERIES_PUBLISH_II_01GA_guards.json';cp=B/'S6_SERIES_PUBLISH_II_01GA_comparison.json';ep=B/'S6_SERIES_PUBLISH_II_01GA_event_proposals.json'
g,c,e=read(gp),read(cp),read(ep)
assert b(gp)['sha256']=='037078c19f35412a0f5415a2b5e6b9d1f48754bd5d1e09e09c5c3a22e0bb9a26'
assert b(cp)['sha256']=='599b6358ad1aca86f0732f39fb40ad807060fe49b8c2e5c8da77798d05639501'
assert b(ep)['sha256']=='9571338bd77d10f79e0bfdef54909bd6db7a4b17141525eb3340286acff1435d'
assert b('S6_SERIES_PUBLISH_II.tex')['sha256']=='811400f69e26aba3abdc37d8c9f16b394cbea39ae47c7ddab9d85553ee854dfd'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
pr=read(c['primary_reading']['path'])
rootpr='records/S6_SERIES_PUBLISH_II_GA_root_primary_reading.json'
write(rootpr,dict(created_utc=now,checker='root',primary_record=b(c['primary_reading']['path']),
 pages=[dict(printed_page=x['printed_page'],image=dict(path=x['path'],sha256=x['sha256']),
             actual_complete_image_viewed_by_root=True) for x in pr['pages']],
 scope='Root actually viewed the six complete journal scan images 231, 233, 234, 237, 238 and 239. Read the local quotient, Proposition 1.13 and its complete proof, Corollary 1.14, analytic scope in 2.1, Theorem 2.18 and its complete proof, the exact connection sequence, residue spectral sequence and local formula, and Theorem 2.21. Later mixed-Hodge definitions are outside the argument. No Paper II page-image credit.',
 paper_II_page_image_credit=0))
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();hits=[]
for m in re.finditer(r'(?<![A-Za-z0-9.])D\.(?:18|19)(?![0-9])',s):
    a=s.rfind('\n',0,m.start())+1;z=s.find('\n',m.end());line=s[a:z]
    kind='label_or_label_reference'
    if '\\tag{'+m.group()+'}' in line:kind='GA_display_number'
    if '('+m.group()+')' in line:kind='GD_literal_reference_pending_its_release'
    hits.append(dict(token=m.group(),char_offset=m.start(),line=s[:m.start()].count('\n')+1,context=line,kind=kind))
assert sum(x['kind']=='GD_literal_reference_pending_its_release' for x in hits)==2
audit='records/S6_SERIES_PUBLISH_II_GA_incoming_identity_map.json'
write(audit,dict(created_utc=now,source=b('S6_SERIES_PUBLISH_II.tex'),matches=hits,
 identity_map={'D.18':dict(label='cdp:eq:D.18',tag='0195'),'D.19':dict(label='cdp:eq:D.19',tag='0196')},
 excluded_other_tokens=['C.RD.18','C.RD.19','C.DD.18','C.DD.19'],
 disposition='One literal pair belongs to still-unreleased GD. Its exact replacement is deferred to the full GD proof comparison. Its sentence has not been sent to the checker. All other references use the preserved labels; no other source owner is changed by this batch.',events_added=0))
x=g['guards'][0];f=read(c['freeze_receipt']['path'])
scope='Root actually read the entire original and final proposed GA statement/12-item proof, the complete seven-section frozen derivation, all twelve comparison steps, every literal guard and both complete bibliography entries, and all six primary page images at the recorded scope.'
t=dict(tag='01GA',statement_owner='cdp:st:D.2.3',checker='restore_build',
 freeze_receipt=c['freeze_receipt'],release_receipt=c['release_receipt'],frozen_derivation=f['frozen_derivation'],
 original_full_block=b(x['original_full_block']),proposed_full_block=b(x['proposed_full_block']),
 guards=[dict(change_id=f'II-GA-{i:02d}',old=z['before'],new=z['after'],defect_type=z['type'],reason=z['reason']) for i,z in enumerate(x['literal_edits'],1)],
 comparison=c['proof_steps'],full_comparison=b(cp),actual_complete_original_proof_read=True,
 actual_complete_proposed_proof_read=True,root_actual_reading_scope=scope,
 additional_dependency_only=True,required_197_row_completion_proposed=False)
pp='records/S6_SERIES_PUBLISH_II_GA_reviewed_proposals.json'
bib=g['guards'][1]
write(pp,dict(paper='II',targets=[t],original_guard=b(gp),original_comparison=b(cp),original_events=b(ep),
 bibliography_guards=[dict(change_id=f'II-GA-BIB-{i:02d}',statement_owner='bib:Steenbrink1976',old=z['before'],new=z['after'],defect_type=z['type'],reason=z['reason']) for i,z in enumerate(bib['literal_edits'],1)],
 complete_bibliography_pair=dict(original=b(bib['original_entry']),proposed=b(bib['proposed_entry'])),
 root_primary_reading=b(rootpr),incoming_reference_audit=b(audit),source_at_preparation=b('S6_SERIES_PUBLISH_II.tex'),
 immutable_required_index=f['required_197_index']))
event=dict(e['events'][0]);event['outcome']='Additional prerelease derivation of the logarithmic period obstruction for arbitrary central multiplicities, followed by complete original/final proof comparison. The analytic source scope, full-fibre base change and residue maps are verified. The primitive top form, local positive-volume estimates and residue-equivariant coefficient ideal give the contradiction. Exact exterior-power and coefficient-subquotient wording refinements preserve the displayed formulas and theorem.'
event['proposal_only']=False;event['root_review_completed']=True
evp='records/S6_SERIES_PUBLISH_II_GA_reviewed_event_proposals.json'
write(evp,dict(events=[event,dict(paper='II',tag='01GA',statement_owner='cdp:st:D.2.3',event_type='used and rechecked in this run',event_count=1,scope=scope,full_comparison=b(cp))],
 original_event_proposal=b(ep),additional_dependency_only=True,required_197_row_completion_proposed=False))
cfg='records/S6_SERIES_PUBLISH_II_GA_prepare_config.json'
write(cfg,dict(proposal=b(pp),source_before_sha256=b('S6_SERIES_PUBLISH_II.tex')['sha256'],
 root_actual_complete_pairs_read=True,root_review_scope=scope,output='records/S6_SERIES_PUBLISH_II_GA_editorial_guard.json',
 expected_patch_count=18,mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=b(pp),events=b(evp),prepare_config=b(cfg),primary_reading=b(rootpr),incoming_map=b(audit))))

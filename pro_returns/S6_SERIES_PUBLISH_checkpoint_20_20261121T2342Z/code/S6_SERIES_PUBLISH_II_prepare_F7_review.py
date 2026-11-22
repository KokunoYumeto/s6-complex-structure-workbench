"""Bind the actually read Inoue proof, bibliography pairs and equation identity map."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
def sha(x):return hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
def b(p):return dict(path=p,sha256=sha((R/p).read_bytes()))
def read(p):return json.loads((R/p).read_text())
def write(p,d):
    p=R/p;assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
base='agents/ii_infra/recovery_20261121/'
gp=base+'S6_SERIES_PUBLISH_II_01F7_guards_v2.json';cp=base+'S6_SERIES_PUBLISH_II_01F7_comparison.json'
assert b(gp)['sha256']=='6c1c43765922eda1f06c0452baec424bdb49f6ef498de7ba8e7dea487fc18cb8'
assert b(cp)['sha256']=='860141e47f023c2e1ec6395d84fd0a7c245d2af6311c2d45817bd1b784c4eca8'
d,c=read(gp),read(cp);owner=d['guards'][0]
assert b('S6_SERIES_PUBLISH_II.tex')['sha256']=='2e36340534a84e454f7700b50a87f01773614b938106c6674c244b2d4d72ff76'
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();cur=owner['before'];assert s.count(cur)==1
guards=[]
for n,g in enumerate(owner['literal_edits'],1):
    assert cur.count(g['before'])==1 and cur.index(g['before'])==g['sequential_before_offset']
    cur=cur.replace(g['before'],g['after'],1)
    guards.append(dict(change_id=f'II-F7-{n:03d}',old=g['before'],new=g['after'],defect_type=g['type'],reason=g['reason']+' '+g.get('exact_mathematical_witness','')))
assert cur==owner['after'] and len(guards)==18
bibguards=[];bibpairs=[]
for entry in d['guards'][1:]:
    cur=entry['before'];assert s.count(cur)==1
    for n,g in enumerate(entry['literal_edits'],1):
        assert cur.count(g['before'])==1
        after=cur.replace(g['before'],g['after'],1)
        bibguards.append(dict(change_id=f'II-F7-BIB-{entry["key"]}-{n:02d}',statement_owner=entry['statement_id'],old=cur,new=after,defect_type=g['type'],reason=g['reason']))
        cur=after
    assert cur==entry['after']
    for k in ['original_entry','proposed_entry']:assert b(entry[k])['sha256']==entry[k+'_sha256']
    bibpairs.append(dict(original=b(entry['original_entry']),proposed=b(entry['proposed_entry']),publication_evidence=entry['publication_evidence']))
assert len(bibguards)==6
start=s.index(owner['before']);end=start+len(owner['before']);hits=[]
pattern=r'(?<![A-Za-z0-9.])C\.IN\.[1-6](?![A-Za-z0-9.])'
for m in re.finditer(pattern,s):
    inside=start<=m.start()<end;label=s[max(0,m.start()-7):m.start()]=='cdp:eq:'
    assert inside or label
    hits.append(dict(token=m.group(),line=s[:m.start()].count('\n')+1,char_start=m.start(),inside_owner=inside,label_identifier=label,context=s[max(0,m.start()-48):m.end()+65]))
assert len(hits)==31
mapping='records/S6_SERIES_PUBLISH_II_F7_incoming_equation_map.json'
write(mapping,dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=b('S6_SERIES_PUBLISH_II.tex'),pattern=pattern,hits=hits,
    equation_map=[dict(old_number=f'C.IN.{n}',retained_label=f'cdp:eq:C.IN.{n}',retained_tag='tag-'+tag,new_number='ordinary paper equation counter') for n,tag in enumerate(['00NK','00NL','00NM','00NN','00NO','00NP'],1)],
    outside_owner_bare_number_receivers=0,actual_root_reading='All31 exact current contexts and the entire old/new owner were read. Outside occurrences are the twelve preamble identifier tokens, already tied to the current equation refs.'))
f=read(c['freeze_receipt']['path'])
scope=('Root and checker actually read the entire original and final eight-item proof and all four full bibliography pairs. Root read the complete frozen derivation, complete JSON and Markdown comparisons, all twenty-four literal guards, exact character-to-form transport, finite-cover supplement and both event scopes. Root read the complete primary-input receipt, edition binding and all thirty-one current number-token contexts. Primary page-image reading is credited to the checker. The six displayed formulas, their labels and tags are retained with ordinary equation numbering. The closed-form period of a lifted affine loop is exactly log(a), identifying the fresh character with the printed form. No computation or Paper II page-image event is claimed.')
target=dict(tag='01F7',statement_owner='cdp:st:C.3.12',checker='restore_build',freeze_receipt=b(c['freeze_receipt']['path']),release_receipt=b(c['release_receipt']['path']),
    frozen_derivation=b(f['frozen_derivation_path']),original_full_block=b(owner['original_full_block']),proposed_full_block=b(owner['proposed_full_block']),
    actual_complete_original_proof_read=True,actual_complete_proposed_proof_read=True,comparison='All eight steps compared, with the exact character/period identification, actual divisor-meridian estimate and regular-fibre group quotients.',full_comparison=b(cp),guards=guards)
out='records/S6_SERIES_PUBLISH_II_F7_reviewed_proposals.json'
write(out,dict(paper='II',targets=[target],bibliography_guards=bibguards,bibliography_full_pairs=bibpairs,bound_inputs=[b(gp),b(cp),b(mapping),b(base+'S6_SERIES_PUBLISH_II_01F7_comparison.md'),b(base+'S6_SERIES_PUBLISH_II_01F7_primary_inputs_receipt_v2.json'),b(base+'S6_SERIES_PUBLISH_II_01F7_exact_number_token_audit.json'),b(base+'F7_primary_inputs/S6_SERIES_PUBLISH_II_KT_v4_source_binding_receipt.json')],root_reading_scope=scope,root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
events='records/S6_SERIES_PUBLISH_II_F7_reviewed_event_proposals.json'
write(events,dict(original_checker_proposal=b(base+'S6_SERIES_PUBLISH_II_01F7_event_proposals.json'),comparison=b(cp),events=[
    dict(statement_owner='cdp:st:C.3.12',event_type='targeted proof check',event_count=1,scope='Independently derived the positive-affine transverse character and its nonzero restriction on every Inoue fibre before target release. The exact hyperbolic-distance identity kills each actual divisor-meridian slope; the meridian normal-closure quotient and abelianization/UCT give a class on the compact total space. Explicit fibre diffeomorphisms, lattice/Heisenberg quotients and elliptic structure maps prove regular-locus propagation. The complete frozen derivation was compared to all eight printed steps; the printed form has exactly the same log(a) period character.'),
    dict(statement_owner='cdp:st:C.3.12',event_type='used and rechecked in this run',event_count=1,scope='Actually read the entire original and final eight-item proof, every literal guard and all four original/proposed bibliography entries. Checked full-family affine transition constancy, the actual transverse-disc developing map, Schwarz--Pick estimate, meridian homology kernel, finite-etale quotient subclaim and group/classification propagation. The finite-cover and printed canonical-degree routes were checked after release, without extra independent credit. Six old equation numbers are mapped to the same labels/tags under the paper counter; exact published and cited-preprint editions are recorded.')],events_added=0))
cfg='records/S6_SERIES_PUBLISH_II_F7_prepare_config.json'
write(cfg,dict(proposal=b(out),source_before_sha256=b('S6_SERIES_PUBLISH_II.tex')['sha256'],root_actual_complete_pairs_read=True,root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_F7_editorial_guard.json',expected_patch_count=24,mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=b(out),events=b(events),prepare_config=b(cfg),mapping=b(mapping)),indent=2))

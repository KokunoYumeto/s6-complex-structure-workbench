"""Bind the five newly frozen WI/FC/G9/WJ/WL checks to exact editorial edits."""
from pathlib import Path
import datetime, hashlib, json
R=Path(__file__).resolve().parents[1]
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before
patches=[];bindings=[]
def block(owner, tag, old, new, edits, evidence):
    global s
    assert sha((R/old['path']).read_bytes())==old['sha256']
    assert sha((R/new['path']).read_bytes())==new['sha256']
    current=(R/old['path']).read_text();expected=(R/new['path']).read_text()
    assert s.count(current)==1,(owner,s.count(current))
    for e in edits:
        assert current.count(e['old'])==1,(owner,e['id'])
        start=s.index(current);pos=start+current.index(e['old']);a,z=pos,pos+len(e['old']);end=start+len(current)
        while s.count(s[a:z])!=1:
            prior=(a,z);a,z=max(start,a-100),min(end,z+100);assert (a,z)!=prior
        oldliteral=s[a:z];newliteral=s[a:pos]+e['new']+s[pos+len(e['old']):z]
        patches.append(dict(old=oldliteral,new=newliteral,type=e['type'],statement_id=owner,
                            reason=e['reason']+' The named checker actually read the complete original and proposed blocks. Root read every literal guard, the complete comparison narratives and the complete fresh programs and outputs. Mathematical admission is separate from applying these edits.',
                            originating_change_id=e['id'],changed_old_literal=e['old'],changed_new_literal=e['new'],
                            proposed_defect_type=e.get('proposed_type',e['type'])))
        s=s[:a]+newliteral+s[z:];current=current.replace(e['old'],e['new'],1)
    assert current==expected and s.count(expected)==1
    bindings.append(dict(owner=owner,tag=tag,before=old,after=new,evidence=evidence,
                         root_complete_proposed_block_read=(owner=='tab:II:programs'),
                         root_all_literal_guards_and_complete_comparison_read=True,
                         exact_guard_sequence_reproduces_proposed_block=True))

bp='agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group01/S6_SERIES_PUBLISH_II_clean_group01_final_proposals.json'
b=json.loads((R/bp).read_text());assert sha((R/bp).read_bytes())=='9acaef2ff18edeecaa4bceb7e98b5362e7e055682110f397839f966d4e176672'
for t in b['targets']:
    assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
    edits=[dict(old=g['old'],new=g['new'],type=g['defect_type'].replace(',','/'),reason=g['reason'],id=g['change_id']) for g in t['guards']]
    block(t['statement_owner'],t['tag'],t['original_full_block'],t['proposed_full_block'],edits,bp)
cp='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_WJ_WL_guards_v2.json'
c=json.loads((R/cp).read_text());assert sha((R/cp).read_bytes())=='cc0319cc8d15a597b02405e933ecc4e0ab8c4b6185cab55c349ef053e15ab985'
for t in c['blocks']:
    edits=[]
    for g in c['guards']:
        if g['statement_id']!=t['statement_id']:continue
        typ='D04/D23' if 'outer_wrapper' in g['id'] else g['type']
        edits.append(dict(old=g['before'],new=g['after'],type=typ,proposed_type=g['type'],reason=g['reason'],id=g['id']))
    block(t['statement_id'],t['tag'],dict(path=t['original_full_block'],sha256=t['original_full_block_sha256']),
          dict(path=t['proposed_full_block'],sha256=t['proposed_full_block_sha256']),edits,cp)
g=next(x for x in c['guards'] if x['statement_id']=='tab:II:programs')
t=c['program_table']
block('tab:II:programs','',dict(path=t['original_full_block'],sha256=t['original_full_block_sha256']),
      dict(path=t['proposed_full_block'],sha256=t['proposed_full_block_sha256']),
      [dict(old=g['before'],new=g['after'],type=g['type'],reason=g['reason'],id=g['id'])],cp)
assert len(patches)==36 and len(bindings)==6
p=R/'records/S6_SERIES_PUBLISH_II_clean_checks_01_editorial_guard.json';assert not p.exists()
record=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,bindings=bindings,
            proposals=[dict(path=bp,sha256=sha((R/bp).read_bytes())),dict(path=cp,sha256=sha((R/cp).read_bytes()))],
            defect_type_refinement='Two outer iteration-wrapper guards are D04/D23; the original proposed D04/D14 types are preserved on each edit.',
            mathematical_events_added=0,visual_reading_credit=0)
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes()),patches=len(patches),source_after_sha256=sha(s)),indent=2))

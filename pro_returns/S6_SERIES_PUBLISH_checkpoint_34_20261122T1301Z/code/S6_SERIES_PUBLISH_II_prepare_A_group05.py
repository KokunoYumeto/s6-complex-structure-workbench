"""Bind four complete reviewed proof pairs and both pinned program citations."""
from pathlib import Path
import datetime, hashlib, json
R = Path(__file__).resolve().parents[1]
sha = lambda b: hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
def read(p): return json.loads((R/p).read_text())
def bound(p): return dict(path=p,sha256=sha((R/p).read_bytes()))
base = 'agents/ii_checks_A/recovery_20261121T195642Z/'
ip = base+'S6_SERIES_PUBLISH_II_A_recovery_group05_final_index.json'
assert bound(ip)['sha256'] == '334a32e63d8117fdafb6e55a8c11777dab8d7f30d9a85b1b9b00eeb5d25dddec'
idx = read(ip)
for b in idx['files']: assert bound(b['path']) == b
pp = base+'group05/S6_SERIES_PUBLISH_II_A_recovery_group05_editorial_proposals.json'
ep = base+'group05/S6_SERIES_PUBLISH_II_A_recovery_group05_event_proposals.json'
tp = base+'group05/S6_SERIES_PUBLISH_II_A_group05_program_table_proposal.json'
d, ev, table = read(pp), read(ep), read(tp)
freezes = read(base+'S6_SERIES_PUBLISH_II_A_recovery_group05_freezes.json')
releases = read(base+'S6_SERIES_PUBLISH_II_A_recovery_group05_releases.json')
rereads = read(base+'group05/S6_SERIES_PUBLISH_II_A_recovery_group05_rereads.json')['rereads']
before = (R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(before) == '4be8221c9bd86874dcfe2b0e90ce8901d31e7d163529eba805d27aa4f5dd6f6c'
s, patches, targets = before, [], []
for block, freeze, release, reread in zip(d['blocks'], freezes, releases, rereads):
    tag = block['tag']
    assert tag == reread['tag']
    old, new = bound(block['original_path']), bound(block['proposed_path'])
    assert old['sha256'] == block['original_sha256'] == reread['original_sha256']
    assert new['sha256'] == block['proposed_sha256'] == reread['proposed_sha256']
    assert bound(freeze['receipt'])['sha256'] == freeze['sha256']
    assert bound(release['receipt'])['sha256'] == release['sha256']
    fr, rr = read(freeze['receipt']), read(release['receipt'])
    owner = freeze['owner']
    cur, expected = (R/old['path']).read_text(), (R/new['path']).read_text()
    assert (R/release['full_block']).read_text().rstrip('\n') == cur.rstrip('\n')
    assert s.count(cur) == 1
    guards = [g for g in d['guards'] if g['tag'] == tag]
    for g in guards:
        assert sha(cur) == g['intermediate_before_sha256']
        pos = g['offset_before']
        assert cur[pos:pos+len(g['literal_old'])] == g['literal_old']
        start = s.index(cur)
        a,z = start+pos,start+pos+len(g['literal_old'])
        end = start+len(cur)
        while s.count(s[a:z]) != 1:
            prev = a,z
            a,z = max(start,a-100),min(end,z+100)
            assert (a,z) != prev
        o = s[a:z]
        n = s[a:start+pos]+g['literal_new']+s[start+pos+len(g['literal_old']):z]
        patches.append(dict(old=o,new=n,type='/'.join(g['defect_types']),statement_id=owner,
            reason=g['reason']+' '+g['mathematical_transport']+
            ' Root and checker actually read both complete original/proposed blocks and the complete cycle and method comparisons. Fresh program sources and outputs were read.',
            originating_change_id=g['guard_id'],changed_old_literal=g['literal_old'],changed_new_literal=g['literal_new']))
        s = s[:a]+n+s[z:]
        cur = cur[:pos]+g['literal_new']+cur[pos+len(g['literal_old']):]
        assert sha(cur) == g['intermediate_after_sha256']
    assert cur == expected and s.count(expected) == 1
    targets.append(dict(tag=tag,statement_owner=owner,original_full_block=old,proposed_full_block=new,
        freeze_receipt=bound(freeze['receipt']),release_receipt=bound(release['receipt']),
        frozen_derivation=bound(fr['frozen_derivation_path']),
        actual_complete_original_proof_read=True,actual_complete_proposed_proof_read=True,
        root_complete_original_and_proposed_read=True,comparison=reread['actual_comparative_record'],
        full_pair_review_completed_utc=reread['completed_utc'],source_application_pending=True))
assert len(patches) == 31
assert bound(table['original_path'])['sha256'] == table['original_sha256']
assert bound(table['proposed_path'])['sha256'] == table['proposed_sha256']
assert s.count((R/table['original_path']).read_text()) == 1
lines = table['literal_new'].splitlines(keepends=True)
assert len(lines) == 4
mid = ''.join(lines[:2])+lines[-1]
for number,(o,n,owner) in enumerate([(table['literal_old'],mid,'night:P4.16'),(mid,table['literal_new'],'night:P4.18')],1):
    assert s.count(o) == 1
    patches.append(dict(old=o,new=n,type='D09',statement_id=owner,
        reason='Cite the complete pinned program once in the end table; its source, path, receiving owners, retrieval receipt and complete old/new method comparison were read.',
        originating_change_id=f'A_REC_G05_PROGRAM_TABLE_{number}'))
    s = s.replace(o,n,1)
assert s.count((R/table['proposed_path']).read_text()) == 1
gp = 'records/S6_SERIES_PUBLISH_II_A_group05_editorial_guard.json'
guard = dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,
    original_index=bound(ip),bindings=targets,mathematical_events_added=0,visual_reading_credit=0)
assert not (R/gp).exists()
(R/gp).write_text(json.dumps(guard,indent=2)+'\n')
support = idx['files']+[bound(ip)]
for stem in ['local_certificate','comparison_certificate','different_methods']:
    for ext in ['py','out']:
        support.append(bound('code/S6_SERIES_PUBLISH_II_A_recovery_group05_'+stem+'.'+ext))
for name in ['prior_milnor_intersection.out','prior_binomial_milnor.out','different_methods.json']:
    support.append(bound('code/S6_SERIES_PUBLISH_II_A_recovery_group05_'+name))
standard = dict(schema_version=1,paper='II',targets=targets,supporting_records=support,
    program_run_records=[read(base+'S6_SERIES_PUBLISH_II_A_recovery_group05_'+suffix+'.json')
                        for suffix in ['program_run','prior_runs','different_methods_run']],
    original_proposals=bound(pp),root_review=bound(gp),events_added=0)
sp = 'records/S6_SERIES_PUBLISH_II_A_group05_reviewed_proposals.json'
assert not (R/sp).exists()
(R/sp).write_text(json.dumps(standard,indent=2)+'\n')
print(json.dumps(dict(guard=bound(gp),standard_proposal=bound(sp),patches=len(patches),source_after_sha256=sha(s)),indent=2))

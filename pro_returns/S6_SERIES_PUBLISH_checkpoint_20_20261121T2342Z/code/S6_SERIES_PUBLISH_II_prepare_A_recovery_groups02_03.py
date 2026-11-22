"""Bind the two reconstructed A batches to the exact current Paper II source."""
from pathlib import Path
import datetime, hashlib, json

R = Path(__file__).resolve().parents[1]
sha = lambda b: hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()
index_path = R / 'agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_group02_03_final_index.json'
assert sha(index_path.read_bytes()) == 'efff143b63ebd8f3626faef0c678afcd92919a86ecd7cc2d10f8fc45dc68b89e'
index = json.loads(index_path.read_text())
before = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
s = before
patches, bindings = [], []
for group in index['groups']:
    path = R / group['manifest']
    assert sha(path.read_bytes()) == group['manifest_sha256']
    reread_path = R / group['reread_record']
    assert sha(reread_path.read_bytes()) == group['reread_sha256']
    rereads = {x['tag']: x for x in json.loads(reread_path.read_text())['records']}
    assert sha((R / group['event_proposals']).read_bytes()) == group['events_sha256']
    for target in json.loads(path.read_text())['proposals']:
        owner, tag = target['statement_owner'], target['tag']
        oldblock = (R / target['original_block_path']).read_text()
        newblock = (R / target['proposed_block_path']).read_text()
        assert sha(oldblock) == target['original_block_sha256']
        assert sha(newblock) == target['proposed_block_sha256']
        rr = rereads[tag]
        assert rr['full_original_owning_block_read'] and rr['full_proposed_owning_block_read']
        assert rr['original_full_block_sha256'] == sha(oldblock)
        assert rr['proposed_full_block_sha256'] == sha(newblock)
        assert s.count(oldblock) == 1, (tag, s.count(oldblock))
        current = oldblock
        for n, edit in enumerate(target['literal_edits'], 1):
            assert current.count(edit['old']) == 1
            start = s.index(current)
            pos = start + current.index(edit['old'])
            a, z = pos, pos + len(edit['old'])
            end = start + len(current)
            while s.count(s[a:z]) != 1:
                old_span = (a, z)
                a, z = max(start, a-100), min(end, z+100)
                assert (a, z) != old_span
            old = s[a:z]
            new = s[a:pos] + edit['new'] + s[pos+len(edit['old']):z]
            patches.append(dict(
                old=old, new=new, type='/'.join(edit['defect_types']), statement_id=owner,
                reason=edit['mathematical_reference_identity'] +
                    ' The proposing checker actually reread both complete owning blocks. Root read every literal guard, both full comparison records, the method addendum, the complete fresh alternate programs and their outputs. Root claims no independent re-proof through this integration.',
                originating_change_id=f'A-recovery-{group["group"]}-{tag}-{n:02d}',
                changed_old_literal=edit['old'], changed_new_literal=edit['new']))
            s = s[:a] + new + s[z:]
            current = current.replace(edit['old'], edit['new'], 1)
        assert current == newblock and s.count(newblock) == 1
        bindings.append(dict(
            owner=owner, tag=tag,
            before={'path': target['original_block_path'], 'sha256': sha(oldblock)},
            after={'path': target['proposed_block_path'], 'sha256': sha(newblock)},
            reread={'path': group['reread_record'], 'sha256': group['reread_sha256']},
            root_full_proposed_block_actually_read=(tag == '02Y1'),
            root_literal_guards_and_full_comparisons_read=True,
            exact_guard_sequence_reproduces_proposed_block=True))
assert len(bindings) == 10 and len(patches) == 47
out = R / 'records/S6_SERIES_PUBLISH_II_A_recovery_groups02_03_editorial_guard.json'
assert not out.exists()
record = dict(paper='II', source_before_sha256=sha(before), source_after_sha256=sha(s),
              patches=patches, bindings=bindings,
              created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              index={'path': str(index_path.relative_to(R)), 'sha256': sha(index_path.read_bytes())},
              mathematical_events_added=0, visual_reading_credit=0)
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)), sha256=sha(out.read_bytes()),
                     patches=len(patches), owners=len(bindings), source_after_sha256=sha(s)), indent=2))

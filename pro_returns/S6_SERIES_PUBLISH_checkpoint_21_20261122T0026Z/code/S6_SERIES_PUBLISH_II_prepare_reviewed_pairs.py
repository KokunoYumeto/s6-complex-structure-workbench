"""Prepare exact guards from already-read full source pairs; make no reading claim by inference."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

R = Path(__file__).resolve().parents[1]

def sha(data):
    return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()

def bound(binding):
    p = R / binding['path']
    assert sha(p.read_bytes()) == binding['sha256'], binding
    return p

cfg_path = R / sys.argv[1]
cfg = json.loads(cfg_path.read_text())
proposal_path = bound(cfg['proposal'])
d = json.loads(proposal_path.read_text())
before = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(before) == cfg['source_before_sha256']
assert cfg['root_actual_complete_pairs_read'] is True
assert cfg['root_review_scope'].strip()
s = before
patches, bindings = [], []
for t in d['targets']:
    assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
    old, new = t['original_full_block'], t['proposed_full_block']
    cur, expected = bound(old).read_text(), bound(new).read_text()
    assert s.count(cur) == 1, t['tag']
    for g in t['guards']:
        assert cur.count(g['old']) == 1, g['change_id']
        start = s.index(cur)
        pos = start + cur.index(g['old'])
        a, z, end = pos, pos + len(g['old']), start + len(cur)
        while s.count(s[a:z]) != 1:
            prev = a, z
            a, z = max(start, a - 100), min(end, z + 100)
            assert (a, z) != prev, g['change_id']
        old_context = s[a:z]
        new_context = s[a:pos] + g['new'] + s[pos + len(g['old']):z]
        patches.append(dict(
            old=old_context, new=new_context, type=g['defect_type'].replace(',', '/'),
            statement_id=t['statement_owner'], reason=g['reason'] + ' ' + cfg['root_review_scope'],
            originating_change_id=g['change_id'], changed_old_literal=g['old'], changed_new_literal=g['new']))
        s = s[:a] + new_context + s[z:]
        cur = cur.replace(g['old'], g['new'], 1)
    assert cur == expected and s.count(expected) == 1, t['tag']
    bindings.append(dict(owner=t['statement_owner'], tag=t['tag'], original=old, proposed=new,
        actual_complete_pairs_read_by_root_and_checker=True,
        comparison=t.get('comparison'), complete_comparison=t.get('full_comparison'),
        root_reading_scope=cfg['root_review_scope']))
for g in d.get('bibliography_guards', []) + cfg.get('extra_guards', []):
    assert s.count(g['old']) == 1, g['change_id']
    patches.append(dict(old=g['old'], new=g['new'], type=g['defect_type'].replace(',', '/'),
        statement_id=g['statement_owner'], reason=g['reason'] + ' ' + cfg['root_review_scope'],
        originating_change_id=g['change_id']))
    s = s.replace(g['old'], g['new'], 1)
assert len(patches) == cfg['expected_patch_count']
out = R / cfg['output']
assert not out.exists()
guard = dict(paper='II', created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source_before_sha256=sha(before), source_after_sha256=sha(s), patches=patches, bindings=bindings,
    evidence=cfg['proposal'], configuration=dict(path=str(cfg_path.relative_to(R)), sha256=sha(cfg_path.read_bytes())),
    mathematical_events_added=0, visual_reading_credit=0,
    mathematical_statement_and_values_unchanged=cfg['mathematical_statement_and_values_unchanged'])
out.write_text(json.dumps(guard, indent=2) + '\n')
print(json.dumps(dict(guard=str(out.relative_to(R)), sha256=sha(out.read_bytes()), patches=len(patches),
    source_after_sha256=sha(s))))

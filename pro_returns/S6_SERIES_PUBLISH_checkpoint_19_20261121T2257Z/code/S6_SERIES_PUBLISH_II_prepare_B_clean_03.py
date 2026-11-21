"""Bind the completely reviewed E10 source pair and precise primary citation."""
from pathlib import Path
import datetime, hashlib, json
R = Path(__file__).resolve().parents[1]
sha = lambda b: hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()
p = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group03/S6_SERIES_PUBLISH_II_clean_group03_final_proposals.json'
assert sha((R/p).read_bytes()) == 'd523074ec6b0d6998519186f08a59c6f2dfdef424a1508abf87c443a0e477534'
d = json.loads((R/p).read_text())
before = (R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(before) == '459c8c7c3dff70ff2621e567383ac56eaf92fd271b02f83775d2cb994f332d6e'
s = before
patches, bindings = [], []
for t in d['targets']:
    assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
    old, new = t['original_full_block'], t['proposed_full_block']
    for b in [old, new]:
        assert sha((R/b['path']).read_bytes()) == b['sha256']
    cur, expected = (R/old['path']).read_text(), (R/new['path']).read_text()
    assert s.count(cur) == 1
    for g in t['guards']:
        assert cur.count(g['old']) == 1
        start = s.index(cur)
        pos = start + cur.index(g['old'])
        a, z, end = pos, pos + len(g['old']), start + len(cur)
        while s.count(s[a:z]) != 1:
            prev = a, z
            a, z = max(start, a-100), min(end, z+100)
            assert (a, z) != prev
        o, n = s[a:z], s[a:pos] + g['new'] + s[pos+len(g['old']):z]
        patches.append(dict(old=o, new=n, type=g['defect_type'].replace(',', '/'),
            statement_id=t['statement_owner'], reason=g['reason'] +
            ' Both root and checker actually read the complete original and proposed statement/proof blocks, the entire frozen derivation and comparison, and all fresh and isolated prior programs and outputs.',
            originating_change_id=g['change_id'], changed_old_literal=g['old'], changed_new_literal=g['new']))
        s = s[:a] + n + s[z:]
        cur = cur.replace(g['old'], g['new'], 1)
    assert cur == expected and s.count(expected) == 1
    bindings.append(dict(owner=t['statement_owner'], tag=t['tag'], original=old, proposed=new,
        actual_complete_pairs_read_by_root_and_checker=True, complete_comparison=t['full_comparison']))
for g in d['bibliography_guards']:
    assert s.count(g['old']) == 1
    patches.append(dict(old=g['old'], new=g['new'], type=g['defect_type'].replace(',', '/'),
        statement_id='cdp:st:E10', reason=g['reason'] + ' Root read the full proposed entry and verified its binding to the primary-source receipt.',
        originating_change_id=g['change_id']))
    s = s.replace(g['old'], g['new'], 1)
assert len(patches) == 10
out = R/'records/S6_SERIES_PUBLISH_II_B_clean_03_editorial_guard.json'
assert not out.exists()
g = dict(paper='II', created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source_before_sha256=sha(before), source_after_sha256=sha(s), patches=patches, bindings=bindings,
    evidence=dict(path=p, sha256=sha((R/p).read_bytes())), mathematical_events_added=0,
    visual_reading_credit=0, mathematical_statement_and_values_unchanged=True)
out.write_text(json.dumps(g, indent=2)+'\n')
print(json.dumps(dict(guard=str(out.relative_to(R)), sha256=sha(out.read_bytes()), patches=len(patches), source_after_sha256=sha(s)), indent=2))

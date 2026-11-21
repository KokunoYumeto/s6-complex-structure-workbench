"""Bind the actual complete paired reading and an explicit identifier permutation."""
from pathlib import Path
import datetime, hashlib, json

R = Path(__file__).resolve().parents[1]
O = R / 'records/S6_SERIES_PUBLISH_II_TQ_alias_01'
sha = lambda b: hashlib.sha256(b).hexdigest()
g = json.loads((O / 'guard.json').read_text())
assert sha((R / 'S6_SERIES_PUBLISH_II.tex').read_bytes()) == g['source_before_sha256']
for field in ['original_full_block', 'proposed_full_block']:
    item = g[field]
    assert sha((R / item['path']).read_bytes()) == item['sha256']
review = dict(
    created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    reviewer='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro; root continuation',
    original_full_block=g['original_full_block'],
    proposed_full_block=g['proposed_full_block'],
    actual_complete_original_and_proposed_read=True,
    scope='All seven original and proposed proof items, both statements, and the complete retired provenance remark were read. The four ownership mappings were checked. This is a paired wording/reference review, not an independent preproof derivation.',
    comparisons=[
        'The statement is unchanged apart from title capitalization and an initial TeX control-space. The production remark label/tag moves to its mathematical owner.',
        'Step 1 gives phi(z)=u0*z/12 and its inverse, the same exponential family, and the induced fibre restriction. Projection formula proves u0 is nonzero.',
        'Steps 2–5, including every period formula and the countability argument, are byte-identical apart from the ordinary enumeration wrapper.',
        'Step 6 uses the exact H1(O_X) to H1(O_Xb) injectivity proved in current Paper I inv:C3.1 by the Cartier sequence and Leray edge map; it applies to all full scheme fibres.',
        'Step 7 uses the actual connected degree-m_j root cover from current Paper I fam:src:A.1.2. The derivative character gives the normal-line quotient. A pulled-back trivializing section is constant on the compact connected cover, proving m_j divides r; the constant section descends at r=m_j.',
        'The entire retired paragraph is archived. Its period, normal-order, full-fibre restriction and gamma-line claims are mapped to their exact current owners. No independent event is assigned to that paragraph.'
    ],
    claim_owner_map=g['claim_owner_map'],
    mathematical_events_proposed=1,
    proposed_event_type='used and rechecked in this run',
    visual_reading_credit=0)
rp = O / 'paired_rereading.json'
assert not rp.exists()
rp.write_text(json.dumps(review, indent=2) + '\n')
g['actual_pair_rereading_pending'] = False
g['paired_rereading'] = {'path': str(rp.relative_to(R)), 'sha256': sha(rp.read_bytes())}
gp = O / 'reviewed_guard.json'
assert not gp.exists()
gp.write_text(json.dumps(g, indent=2) + '\n')

original_helper = R / 'code/S6_SERIES_PUBLISH_exact_source_edit.py'
old = original_helper.read_text()
old_block = '''        assert [x for x in a if x not in set(added)]==b
        identities[kind]=dict(before=len(b),after=len(a),added=added,original_sequence_preserved=True)'''
new_block = '''        permutation = g.get('identity_permutations', {}).get(kind)
        if permutation is None:
            assert [x for x in a if x not in set(added)]==b
            identities[kind]=dict(before=len(b),after=len(a),added=added,original_sequence_preserved=True)
        else:
            assert not added
            assert g['actual_pair_rereading_pending'] is False
            rr=g['paired_rereading']; rp=ROOT/rr['path']
            assert sha(rp.read_bytes())==rr['sha256']
            review=json.loads(rp.read_text())
            assert review['actual_complete_original_and_proposed_read'] is True
            for field in ['original_full_block','proposed_full_block']:
                assert review[field]==g[field]
                assert sha((ROOT/g[field]['path']).read_bytes())==g[field]['sha256']
            assert len(permutation)==len(b)==len(a)
            assert sorted(row['before_index'] for row in permutation)==list(range(len(b)))
            assert sorted(row['after_index'] for row in permutation)==list(range(len(a)))
            for row in permutation:
                assert b[row['before_index']]==row['identity']==a[row['after_index']]
            moved=g['moved_'+kind]
            assert moved and len(moved)==len(set(moved))
            assert all(b.count(x)==a.count(x)==1 for x in moved)
            assert [x for x in b if x not in set(moved)]==[x for x in a if x not in set(moved)]
            assert all(b.index(x)!=a.index(x) for x in moved)
            identities[kind]=dict(before=len(b),after=len(a),added=[],
                original_sequence_preserved=(a==b),moved=moved,
                unchanged_relative_order_of_every_other_identity=True,
                complete_occurrence_bijection=permutation,
                permutation_sha256=sha(json.dumps(permutation,sort_keys=True,separators=(',',':')).encode()))'''
assert old.count(old_block) == 1
new = old.replace(old_block, new_block)
new = new.replace('The guard owns the manual contextual review.', 'The guard owns the manual contextual review. Explicitly declared identifier\npermutations are accepted only with a complete occurrence bijection and a\nbound actual paired rereading; all undeclared order changes remain forbidden.')
hp = R / 'code/S6_SERIES_PUBLISH_exact_source_edit_permutation.py'
assert not hp.exists()
hp.write_text(new)
assert original_helper.read_text() == old
print(json.dumps(dict(reviewed_guard=str(gp.relative_to(R)),guard_sha256=sha(gp.read_bytes()),
    paired_rereading_sha256=sha(rp.read_bytes()),helper=str(hp.relative_to(R)),helper_sha256=sha(hp.read_bytes()),
    original_helper_unchanged=True),indent=2))

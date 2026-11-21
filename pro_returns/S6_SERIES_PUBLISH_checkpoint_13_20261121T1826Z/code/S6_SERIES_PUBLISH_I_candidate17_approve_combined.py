"""Bind root's actually completed review of the 109 exact substitutions."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = '5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
assert sha(R / 'S6_SERIES_PUBLISH_I.tex') == source
spec = [
    ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_guards.json', '8a49ba06243f370c33c745a19e5f704c0a1ffdfcc8c10b62f537b756518b2855', 23),
    ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_edits_guards.json', 'e08c416b9e1e7c3f4e8ed6d00914e730a5049617994a353f144d448fe10b7721', 17),
    ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_provenance_guards.json', '2b65de6c9b3d179d50d04cefb80f79335f2bece4418d3ec669cd15268bae9413', 23),
    ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_infra_scope_guard_final.json', '3738aa0d31ffe41714812f441d5a0ebdaad47874d22ee5d34ed7b1bfb46627dd', 1),
    ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards_final.json', '35757d137a928f73fdd6405118c4dbe365e8d99b5619c88f1cf1efca5379a8f6', 45),
]
for path, digest, count in spec:
    assert sha(R / path) == digest, path
    data = json.loads((R / path).read_text())
    guards = data if isinstance(data, list) else data['guards']
    assert len(guards) == count

evidence = [
    ('records/S6_SERIES_PUBLISH_I_candidate17_body_guard_review.json', 'a4b3b3c29b33bfa5c7741af18366bc28e144afc5a1d072ce864a05073a266d4f'),
    ('records/S6_SERIES_PUBLISH_I_candidate17_scope_guard_approval.json', 'a173c9b23b344908b6e2212635367080e833e8bcac4ffdccfb00e95bb821aa5c'),
    ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_supersession_receipt.json', '4bcea2e4f9e1e151baa54c9295d25d4c55b04d5ae1b61b4869fe2fcd6b096f42'),
    ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final_v3.json', '6c38d39d983e7080cdb6ecee1bac5a9a49284fdad4b36274c8ec4ab0481a66c0'),
    ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_matrix_v3_receipt.json', '3f92672502e94f6f408f00dfa7fdd1c8892459eef3eefd4dc2481079dc6c1628'),
]
for path, digest in evidence:
    assert sha(R / path) == digest, path
record = {
    'source_sha256': source,
    'root_approved': True,
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'guard_files': [{'path': p, 'sha256': h, 'count': n} for p, h, n in spec],
    'reviewed_body_guards': 64,
    'reviewed_bibliography_entries': 45,
    'total_guards': 109,
    'review_scope': (
        'Root read every exact before/after guard and reason. Complete owning-block comparisons '
        'and actual assigned proof readings remain bound. Root read all45 bibliography full-entry '
        'pairs, both final superseding changes, all72 retained-entry dispositions and their '
        'specific primary-source qualifications. Root additionally opened the publisher front '
        'matter and exact YZZ author upload. The two audit-summary pagination corrections were '
        'read against the unchanged canonical entries and their primary-header receipt; neither '
        'changes a source guard. No independent mathematical check or page-reading credit is inferred.'
    ),
    'review_evidence': [{'path': p, 'sha256': h} for p, h in evidence],
    'primary_root_web_readings': [
        {'url': 'https://www.degruyterbrill.com/document/doi/10.1515/9781400845644.fm/pdf',
         'ref': 'turn244112063view0',
         'facts_read': 'Four-page publisher front matter: series184, title-page2013, copyright2013.'},
        {'url': 'https://www.researchgate.net/publication/267551160_Gross-Zagier_Formula_On_Shimura_Curves',
         'ref': 'turn244112063view1',
         'facts_read': 'Xinyi Yuan author upload, manuscript6November2011, contentssection7.1.1 onp218.'},
    ],
    'mathematical_events_added': 0,
}
destination = R / 'records/S6_SERIES_PUBLISH_I_candidate17_root_approved_inputs.json'
assert not destination.exists()
destination.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(destination.relative_to(R)), 'sha256': sha(destination), 'guards': 109}, indent=2))

#!/usr/bin/env python3
"""Record the reviewed incoming boundary calculation without closing targets."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

root = Path(__file__).resolve().parents[1]
owned = root / 'agents/continuation6_iii_root'
stem = 'S6_SERIES_PUBLISH_III_graph_boundary'
note = owned / (stem + '_root_comparison.md')
finite = root / 'agents/continuation6_iii_finite'
expected = {
    '.md': '6a2c69c5157ceddecc5357532a85d283a29de19601827d5a244bd5210291e40b',
    '.py': 'cf2b468c2ce3f80d072d80d9f4d0e62ac8460d5bdc2f7cbab21588e9cc8af9ba',
    '.out': '3966b24c504a0e60341a9b666e64b4c433c86b0fdd0286eae00a5ad7aaa77582',
}
evidence = [note.relative_to(root).as_posix()]
for ext, digest in expected.items():
    path = finite / ('S6_SERIES_PUBLISH_III_graph_core_obstruction' + ext)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
    evidence.append(path.relative_to(root).as_posix())
source = (root / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert hashlib.sha256(source).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
now = datetime.now(timezone.utc).isoformat()

def read(path):
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(path, fields, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

fields, all_events = read(root / 'CHECK_EVENTS.tsv')
prior_ids = {r['event_id'] for r in all_events}
events, defects = [], []
targets = [
    ('02S8', 'night:P3F.31', r'The restriction \(H^2(H_w;\mathbb Z)\to H^2(T^3;\mathbb Z)\) is injective, so the zero boundary Chern class forces the cap line class to be zero.'),
    ('02S9', 'night:P3F.32', r'The two marked caps and their line restrictions are precisely those in P3F.31.'),
]
for tag, label, old in targets:
    assert source.count(old.encode()) == 1
    source_row = source.count(b'\n', 0, source.index(old.encode())) + 1
    eid = 'publish:c6:III:' + tag + ':incoming-boundary-countercheck'
    assert eid not in prior_ids
    row = dict.fromkeys(fields, '')
    row.update(statement_id=label, date=now[:10], date_utc=now,
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; finite checker and root full comparison',
        type='targeted proof check', event_id=eid,
        phase='new post-exposure incoming-collar calculation and root complete comparison',
        outcome='The independent incoming-torus derivation, new program and complete output were frozen at2026-11-24T15:49:53.371831+00:00 and fully read by root. Exact positive-normal interpolation, rounded-collar embedding/inverse, phase-straightening unit/inverse, ambient normal quotient/right inverse, and oriented Jacobian give comparison-chain intersection -m. The physical-dual outer line is trivial; punctured-chain boundary gives j_+^*x=m[dh wedge d tau]. The graph Euler identity and injective actual cap restriction then give b|H_w=2m[dh wedge d tau], for n=1, every m=3k>0 and every integral d. This refutes the original zero-cap substitution and the staged receiving substitution. All complete originals, receivers and auxiliary assertions were previously read; the exact affected passages are now compared to this new evidence. S8/S9 remain open and their receivers UNREADY. The full global class, capped square, final return integer, sphere class and product mapping torus remain unresolved. No old arithmetic rerun, full-target closure, source/unit/build/page credit, or IV proof credit.',
        source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(source_row),
        source_event_type='targeted proof check', evidence_group=eid,
        publish_input_file=(owned/(stem+'_CHECK_EVENTS.tsv')).relative_to(root).as_posix(),
        publish_input_row=str(len(events)+2), where='; '.join(evidence))
    events.append(row)
    defects.append(dict(change_id='c6-III-'+tag+'-incoming-cap-class', type='D25',
        statement_id=label, old_location=f'S6_SERIES_PUBLISH_III.tex:{source_row}',
        old_page='', new_location=note.relative_to(root).as_posix(), new_page='',
        old_text=old,
        new_text='The actual graph meridian has incoming H,K degree m, and the actual compression-cap class is b=2m[dh wedge d tau]. The full global corrected square and receiving proof remain pending.',
        reason='The directed incoming-collar comparison has intersection -m. Triviality of the physical line on this chart does not identify the graph line there; the exact intersection supplies their difference.',
        review_status='confirmed D25 by new post-exposure derivation and full root comparison; repair pending; target remains open'))
progress_fields, progress = read(root/'S6_SERIES_PUBLISH_required_progress_III.tsv')
for row in progress:
    if row['tag'] in {'02S8','02S9'}:
        assert row['status'] == 'open'
        row['notes'] += ' Confirmed incoming-boundary D25: for positive numerator the actual graph meridian has H,K degree m and b|H_w has degree2m; the zero-cap substitution fails. Full global correction and final return remain open.'
        row['proof_comparison_evidence'] += '; ' + note.relative_to(root).as_posix()
write(owned/(stem+'_CHECK_EVENTS.tsv'), fields, events)
write(owned/(stem+'_defects.tsv'), list(defects[0]), defects)
write(root/'CHECK_EVENTS.tsv', fields, all_events+events)
write(root/'S6_SERIES_PUBLISH_required_progress_III.tsv', progress_fields, progress)
assert (root/'S6_SERIES_PUBLISH_III.tex').read_bytes() == source
print('Recorded two narrow incoming-boundary events and two D25 rows at', now)
print('Both targets remain open; III done count:', sum(r['status']=='done' for r in progress))

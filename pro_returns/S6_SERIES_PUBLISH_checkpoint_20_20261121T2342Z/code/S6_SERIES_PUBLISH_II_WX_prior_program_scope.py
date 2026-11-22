from pathlib import Path
import csv
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
sp = R / 'S6_SERIES_PUBLISH_II.tex'
s = sp.read_text()
t = s.index(r'\hypertarget{tag-02WX}')
a = s.rfind(r'\begin{proposition}', 0, t)
p = s.index(r'\end{proof}', t) + len(r'\end{proof}')
left = s.rfind(r'\end{proof}', 0, a) + len(r'\end{proof}')
right = s.index(r'\begin{proposition}', p)
release = R / 'agents/ii_infra/released_proofs/02WX/165aa156c61940fe'
owner = release / 'S6_SERIES_PUBLISH_full_owning_block.tex'
assert s[a:p] == owner.read_text()
rows = [r for r in csv.DictReader((R / 'CHECK_EVENTS.tsv').open(), delimiter='\t')
        if r['statement_id'] == 'night:P4.25']
assert len(rows) == 4
ta = s.index(r'\section*{Programs}')
tb = s.index(r'\end{longtable}', ta) + len(r'\end{longtable}')
table = s[ta:tb]
program_rows = [line for line in table.splitlines() if ' & ' in line and '\\href{' in line]
assert len(program_rows) == 10
assert 'night:P4.25' not in table
record = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'statement_owner': 'night:P4.25',
    'tag': '02WX',
    'source_sha256': sha(sp),
    'ledger_sha256': sha(R / 'CHECK_EVENTS.tsv'),
    'released_complete_owner': {'path': str(owner.relative_to(R)), 'sha256': sha(owner)},
    'adjacent_before': {'char_start': left, 'char_end': a, 'text': s[left:a]},
    'adjacent_after': {'char_start': p, 'char_end': right, 'text': s[p:right]},
    'exact_owner_rows': rows,
    'end_program_table': {'char_start': ta, 'char_end': tb, 'text': table,
                          'program_rows_count': len(program_rows)},
    'actual_root_reading_scope': (
        'Root actually read the whole released seven-item WX proof and statement, '
        'both complete interstatement gaps, all four exact-owner historical rows, '
        'and the complete end Programs table. This is postrelease reading.'),
    'finding': (
        'The released owner, adjacent gaps and four exact-owner rows name no '
        'computational routine. The ten-row end Programs table contains no WX '
        'owner association. Its related local-singularity programs are explicitly '
        'assigned to P4.14, P4.16/P4.17 and P4.18/P4.19; this record does not '
        'assign any of them to P4.25. It makes no assertion of absence elsewhere '
        'in the repository or historical source files.'),
    'mathematical_events_added': 0,
    'visual_reading_credit': 0,
}
out = R / 'records/S6_SERIES_PUBLISH_II_WX_prior_program_scope.json'
assert not out.exists()
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'path': str(out.relative_to(R)), 'sha256': sha(out),
                  'exact_owner_rows': len(rows), 'end_program_rows': len(program_rows)}))

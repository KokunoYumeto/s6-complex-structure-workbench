"""Admit LL source disposition and reopen the two actual retained-role gaps."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read(name):
    with (ROOT / name).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

_, events = read('CHECK_EVENTS.tsv')
event, = [e for e in events if e['event_id'] == 'C9-III-RETAINED-02LL-USED-001']
assert event['source_event_type'] == 'used and rechecked in this run'
now = datetime.now(timezone.utc).isoformat()
uf, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'maps:src:D.2.44' and r['defect_type'] == 'D20']
assert row['status'] == 'open'
review = 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_retained_02LL_review.md'
assert (ROOT / review).is_file()
assert 'Admitted 12 exact source rows and 1 scoped used-and-rechecked events.' in (ROOT / 'code/S6_SERIES_PUBLISH_c9_admit_retained_02LL.out').read_text()
row.update(status='done', date_utc=now, evidence=row['evidence'] + '; ' + review,
    detail=row['detail'] + ' The complete02LL retained-role packet is admitted after root read its full report and509-line difference. Exact sweep, action, period, coefficient, characteristic, framing, relation and surgery maps and inverses are preserved. The previously admitted02LM role packet remains intact. This closes the containing source naming criterion; all final changed-page gates remain open.')
reopened = {
    'maps:src:D.2.26': ('agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_P15_contextual_review.md', '02L1: the exact finite-lift block declares z as both a marked period solution and a central-quotient generator; adjoining translating section s, quotient generator c and Bezout alpha require their affected-use comparison against persistent names. The global reader owns that coherent bounded packet. Root read the current central-quotient definition and both inverse formulas.'),
    'maps:src:D.2.49': ('agents/continuation9_findings/S6_SERIES_PUBLISH_c9_P15_bounded_scope_disposition.md', '02LQ: the admitted global strict packet settled only the T roles. The original full-proof reader confirmed that earlier retained eta_0, edge h, disc/order s and lattice-function/normal-torus L decisions still require their exact current-source disposition. That reader owns the coherent addendum; no paragraph-only retention is accepted.'),
}
for subject, (evidence, detail) in reopened.items():
    assert (ROOT / evidence).is_file()
    row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == subject and r['defect_type'] == 'D20']
    assert row['status'] == 'done', subject
    row.update(status='open', date_utc=now, evidence=row['evidence'] + '; ' + evidence,
        detail=row['detail'] + ' Reopened on final authored-retention reconciliation: ' + detail + ' Existing mathematical conclusions retain their recorded checks; source naming and final rendering remain distinct recorded gates.')
ff, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
row, = [r for r in findings if r['id'] == 'P15']
assert row['status'] == 'open'
row['date_utc'] = now
row['source_resolution'] += ' The exact02LL12/1 packet is admitted and its containingD20 row closed. The final authored-retention comparison exposed the actual02L1 finite-lift naming block and remaining02LQ names outside its admitted T-only packet; both correspondingD20 rows are explicitly reopened.'
row['remaining_gate'] = 'Settle the actual02L8 branch,02L1 finite-lift and02LQ retained-role packets, and complete every authored-retention disposition against current source. Whole-paper P11/P15 closure, final count paragraph and same-source builds follow. Final changed-page gates remain open.'
write('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
write('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
print('Closed admitted02LL-containingD20; reopened actual02L1 and02LQ retained-role units.')
print('02L8 branch and whole-paper source reconciliation remain open; no source, raw event or derived-count mutation.')

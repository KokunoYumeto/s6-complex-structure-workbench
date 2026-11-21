"""Correct batch-level register codes using the recorded, inspected edit scope.

Only metadata is changed. Each original classification is retained in the receipt.
This is not a further mathematical check or a publication-gate completion.
"""
from pathlib import Path
import csv, collections, datetime, hashlib, json, re

csv.field_size_limit(100_000_000)
r = Path(__file__).resolve().parents[1]
p = r / 'S6_SERIES_PUBLISH_defects_I.tsv'
rows = list(csv.DictReader(p.open(), delimiter='\t'))
before = hashlib.sha256(p.read_bytes()).hexdigest()
changes = []
explicit = {}

def assign(ids, kind):
    for n in ids:
        explicit[n] = kind

assign(range(730, 764), 'D10')
assign(range(807, 810), 'D23')
assign([823, 824, 990], 'D16')
assign([878, 879, *range(894, 903), 987, 988, 989, 992, 993,
        *range(994, 1004)], 'D18')
assign([903, 904, 905], 'D01/D18')
assign([906], 'D08/D18')
assign(range(851, 861), 'D24')
assign([68, 74, 92, 93, 94, 362, 363, 366, 367, 368, 372,
        383, 411, 483, 484, 485, 486, 487, 649, 650, 725], 'D14')
assign([69, 81, 386, 441, 446, 723], 'D01')
assign([70, 398, 406, 412, 511, *range(419, 438),
        *range(501, 511), *range(601, 644)], 'D16')
assign([91], 'D21')
assign([364, 387, 401, 408, 481, 488, 580, 644, 645, 647, 648,
        651, 652, 653, 721, 722, 810, 812, 815], 'D13')
assign([373, 374, 375, 376, 377, 378, 414, 415, 416, 656, 657, 658], 'D18')
assign([418, 654, 655], 'D17')
assign([390, 409, 410, 574, 575, 577, 578], 'D08')
assign([400, 443, 571, 572], 'D11')
assign([413, 569, 570, 573, 576], 'D02')
assign([404, 600], 'D09')
assign([444, 445], 'D09/D11')
assign(range(491, 501), 'D08/D09')
assign(range(586, 600), 'D08/D09')
assign([369, 370], 'D24')
assign([407], 'D01/D22')
assign([442], 'D03/D13')
assign([579], 'D03/D09')
assign([646], 'D20')
assign([653], 'D13/D16')
assign([702], 'D04/D25')
assign([703], 'D12/D25')
assign([704], 'D01/D25')
assign([705], 'D25')
assign([706, 707, 708, 709, 710, 711, 712, 713], 'D08/D09/D16')
assign([714, 715, 716], 'D01/D13')
assign([719, 720], 'D01/D18')
assign([811], 'D01/D12')
assign([813, 816, 817, 819, 820], 'D01/D08')
assign([818], 'D01/D18')

for row in rows:
    n = int(row['change_id'].split('-')[1])
    kind = explicit.get(n)
    # These rows were all assigned D07 by their integration wrapper,
    # although its name-of-a-run defect is absent from their inspected scope.
    if row['type'] == 'D07' and kind is None:
        reason = row['reason']
        if n in {825, 826, 836, 837, 838, 839, 840, 841, 867, 868, 869} or 870 <= n <= 877:
            kind = 'D15'
        elif n in {861, 862, 865}:
            kind = 'D24'
        elif n in {891, 892}:
            kind = 'D04'
        elif n == 884:
            kind = 'D01/D18'
        elif n in {885, 893}:
            kind = 'D11'
        elif 'title' in reason.lower():
            kind = 'D16'
        elif re.search(r'\b(?:rather than|not just|not merely|without assuming|silently|no claim|not asserted)\b', row['old_text'], re.I):
            kind = 'D02'
        else:
            kind = 'D08'
    if kind and kind != row['type']:
        changes.append({'change_id': row['change_id'], 'old_type': row['type'],
                        'new_type': kind, 'statement_id': row['statement_id'],
                        'inspected_reason': row['reason']})
        row['type'] = kind

with p.open('w') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t')
    w.writeheader(); w.writerows(rows)
receipt = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'before_sha256': before, 'after_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
           'scope': 'Reclassify recorded edits against the actual register. All original old/new text, reasons and change identifiers remain unchanged. Composite codes record multiple inspected defects in one container edit. Misplaced statement records and display whitespace are apparatus/typography, with no mathematical-error credit.',
           'changes': changes, 'rows': len(rows),
           'counts_after': dict(collections.Counter(x['type'] for x in rows)),
           'new_check_events': 0, 'publication_gates_closed': 0}
(r / 'records/S6_SERIES_PUBLISH_I_defect_taxonomy_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'reclassified': len(changes), 'rows': len(rows),
                  'counts_after': receipt['counts_after']}, indent=2))

"""Prepare the exact local LS guards, bounded repairs and scoped events.

Only the individually released statement/proof and authorized following
audit paragraph are semantically read from the canonical source. No
canonical source, global ledger, or frozen fresh file is modified.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import io
import re

W = Path(__file__).resolve().parents[1]
lane = W / 'agents/continuation7_iii_vertical_correction_receiving'
fresh_lane = W / 'agents/continuation7_iii_vertical_correction'
prefix = 'S6_SERIES_PUBLISH_III_02LS'
sid = 'maps:src:D.2.50'
source = W / 'S6_SERIES_PUBLISH_III.tex'
raw = source.read_bytes()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = raw.decode()
fresh_path = fresh_lane / f'{prefix}_fresh_derivation.md'
fresh_hashes = {
    fresh_path: 'ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d',
    fresh_lane / f'{prefix}_fresh_os45_data_v001.json': '33d83e7e9f255e029670f18d8718aa43060c5d247b86fdb38dbf45938cba9b70',
    W / 'code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.py': '34b5fdd2dc759ca3292a806979fee138266f024c98d1df4b9c1baffbacc081c1',
    W / 'code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.out': 'faa7f25973790a72a84677de93bc0cb9a0bd13c314387404467ac01adfdb078f',
}
for path, expected in fresh_hashes.items():
    assert sha256(path.read_bytes()).hexdigest() == expected
receiver_path = lane / f'{prefix}_receiving.tex'
comparison_path = lane / f'{prefix}_comparison.md'
post_path = lane / f'{prefix}_post_exposure_auxiliaries.md'
expected_final = {
    receiver_path: 'da9c75e5b52f01faf8dad478f09eab997fb3c512d75a0cb6689264abac8c87a3',
    comparison_path: '1f4a746e04e9ad949ba0d11059ae07b14232a34f99a86c2407b2bd49e235c0cf',
    post_path: '4936ba3d22e310d13e77b2ce03629e32c75bdb842dc3c19d7d846e4f5d14c3c9',
}
for path, expected in expected_final.items():
    assert sha256(path.read_bytes()).hexdigest() == expected
receiver = receiver_path.read_text()
now = datetime.now(timezone.utc)
csv.field_size_limit(100000000)

def span(text, start, end, include_end=False):
    assert text.count(start) == 1, start
    left = text.index(start)
    right = text.index(end, left)
    if include_end:
        right += len(end)
    return text[left:right].rstrip('\n')

def env(text, name):
    return span(text, '\\begin{' + name + '}', '\\end{' + name + '}', True)

def write_tsv(path, fields, rows):
    assert not path.exists()
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), newline='\n')
    with path.open(newline='') as handle:
        assert list(csv.DictReader(handle, delimiter='\t')) == rows
    assert b'\r' not in path.read_bytes()

old_statement = env((lane / f'{prefix}_released_statement.tex').read_text(), 'theorem')
old_proof = env((lane / f'{prefix}_released_proof.tex').read_text(), 'proof')
old_aux = r'''The independent certificate
\path{code/fourfolds_vertical_correction_audit.py}
checks all $227$ local pairs with unimodular Smith transformations,
all $5696$ global residues, and the $82$ actual elliptic
monodromy/section-cocycle orders against the recorded component
maps. It also records all sixteen additional positive height-one
section pairs across the full profile list. Those latter sixteen
pairs are initial data, distinct from the sixteen fully filled
OS45 examples in \eqref{maps:eq:D.VC7}.'''
old_proof_and_aux = old_proof + '\n\n' + old_aux
new_statement, new_proof = env(receiver, 'theorem'), env(receiver, 'proof')
assert receiver.rstrip('\n') == new_statement + '\n\n' + new_proof
assert len(re.split(r'(?m)^\\item ', old_proof)) - 1 == 14
items = ['\\item ' + item.rstrip('\n') for item in re.split(r'(?m)^\\item ', old_proof)[1:]]
items[-1] = items[-1].split('\\end{enumerate}', 1)[0].rstrip('\n')
guards = [
    dict(statement_id=sid, old_text=old_statement, new_text=new_statement,
         reason='Retain every proved theorem clause, maps:src:D.2.50 and its displays D.VC1/D.VC7, adding the small printed tag02LS. All signed parameters, weights and sixteen marked homology conclusions stand.'),
    dict(statement_id=sid, old_text=old_proof_and_aux, new_text=new_proof,
         reason='Replace the exact sole proof and authorized following audit paragraph by one complete proof with all local, tensor, period, cap, bar, relative and quotient maps and inverses. Preserve every D.VC label, hypertarget and display tag; all fourteen original auxiliaries and all historical computation claims are settled.'),
]
for guard in guards:
    assert canonical.count(guard['old_text']) == 1
    for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}'):
        assert sorted(re.findall(pattern, guard['old_text'])) == sorted(re.findall(pattern, guard['new_text']))
guard_path = lane / f'{prefix}_replacements.tsv'
write_tsv(guard_path, ['statement_id', 'old_text', 'new_text', 'reason'], guards)

def location(text, whole, path):
    assert whole.count(text) == 1
    start = whole[:whole.index(text)].count('\n') + 1
    return f'{path}: lines {start}-{start + text.count(chr(10))}'

def defect(number, kind, old, new, reason):
    assert canonical.count(old) == receiver.count(new) == 1
    return dict(change_id=f'publish:c7:III:02LS:{kind}:{number}', type=kind,
        statement_id=sid, old_location=location(old, canonical, source.name),
        old_page='source not paginated in this check',
        new_location=location(new, receiver, str(receiver_path.relative_to(W))),
        new_page='final PDF page gate open', old_text=old, new_text=new,
        reason=reason,
        review_status='local completed comparison; root admission and canonical application pending; publication-unit gates separately open')

old_convention = r'''Using the inverse permutation for pullback gives the same
invariance condition and the same solution set.
The equation is integral: it may not be replaced by its
rational solution or by the saturation of its image.'''
new_convention = r'''The pushforward convention has matrix $S^{-1}$; its equation is
obtained by the unimodular left multiplication $-S^{-1}$, whose
inverse is $-S$. This proves the exact equivalence of the two
permutation conventions. All lattices in this proof are integral.'''
old_vectors = span(old_proof, r'At $I_8$ one may take the following literal coefficient vectors:',
                   r'\item Each positive-weight cap')
new_vectors = span(receiver, 'Retain the following literal raw-component coefficient choices:',
                   r'\item \emph{Primitive rank-one cap maps')
new_local = span(receiver, r'\item \emph{Integral solutions for every component pair.}',
                 r'\item \emph{The twenty-one profiles and all residues.}')
new_presentations = span(receiver, r'\item \emph{The exact finite presentation and its inverse coordinates.}',
                         r'\item \emph{The remaining homology and the computation scope.}')
new_audit = span(receiver, 'The complete fresh calculation is retained in', r'\end{enumerate}')
defects = [
    defect('1', 'D20', old_convention, new_convention,
        'Clarify the two component-permutation conventions by the exact unimodular row map -S^{-1} and inverse -S, retaining the integer equation. This is a notation/marking repair; the original invariance assertion is valid and no D25 refutation is inferred.'),
    defect('2', 'D20', old_vectors, new_vectors,
        'Make the raw versus positive-valuation component coordinates and the invariant-column antecedent explicit. The involution j->-j, its inverse, the two invariant divisor differences E, tensor map/reciprocal, actual unit q^{-1}u and -delta/+delta peripheral shear transport the boundary origin and gluing. D.VC10 remains valid in its raw convention. The filled-space proof applies to its stated corrections with this marking; changing D while holding an untransported gluing fixed is not asserted.'),
    defect('3', 'D09', items[7], new_local,
        'Replace the local criterion whose mathematical justification was carried by a program path with a complete integral proof for all pairs: explicit cycle inverse, discriminant pairings and the actual odd-star permutation and d=e1. The old finite results are all newly checked, including 227 pairs and 135 exact obstruction records. No historical execution is claimed. Consolidated repository-citation formatting remains publication-unit work.'),
    defect('4', 'D09', items[13], new_presentations,
        'Supply the complete integral presentation and relative-map proof behind the old numerical Smith/rank sentence. The old 23x70 matrix is valid and has explicit Nielsen/central M,M^{-1} quotient maps to the 23x59 matrix, with integer preimages of every relation both ways. The full six-disc map and inverse prove the relative kernel zero. Its old H1=Z5 and five component classes are also checked. No 70/59 or rank-comparison refutation is inferred; all groups stay unchanged.'),
    defect('5', 'D13', old_aux, new_audit,
        'Move the entire following audit paragraph into the sole receiving proof, with precise fresh/post-exposure/historical execution scopes. Its 227/5696/82/16 assertions have been checked completely, including all historical JSON fields and explicit differentiation of the two sixteen-element parameter sets. No unnumbered auxiliary remains between this proof and the next statement.'),
]
defect_fields = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
defect_path = lane / f'{prefix}_defects.tsv'
write_tsv(defect_path, defect_fields, defects)

with (W / 'CHECK_EVENTS.tsv').open(newline='') as handle:
    event_fields = next(csv.reader(handle, delimiter='\t'))
assert event_fields == ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
event_path = lane / f'{prefix}_CHECK_EVENTS.tsv'
paths = [fresh_path, fresh_lane / f'{prefix}_fresh_vertical_notes.md',
         fresh_lane / f'{prefix}_period_and_star_maps.md',
         fresh_lane / f'{prefix}_fresh_os45_data_v001.json',
         lane / f'{prefix}_released_statement.tex', lane / f'{prefix}_released_proof.tex',
         receiver_path, comparison_path, post_path, guard_path, defect_path,
         lane / f'{prefix}_post_local_data_v001.json', lane / f'{prefix}_post_relation_data_v001.json',
         lane / f'{prefix}_historical_helper_bounded_v001.py',
         lane / f'{prefix}_historical_helper_bounded_v002.py']
for name in ('root_vertical_corrections.py', 'fourfolds_corrected_Mumford_examples.py',
             'fourfolds_vertical_correction_audit.py', 'root_vertical_corrections.json',
             'fourfolds_corrected_Mumford_examples.json', 'manifolds_general_initial.py',
             'manifolds_rankone_families.py', 'manifolds_all_weighted_profiles.py'):
    paths.append(lane / ('S6_SERIES_PUBLISH_' + name))
for stem in ('os45_bar_v001','output_readback_v001','output_readback_v002','star_order_v001',
             'finish_edit_v001','finish_v001','finish_edit_v002','primary_pages_v001',
             'historical_retrieve_v001','historical_retrieve_v002','historical_retrieve_v003',
             'historical_retain_v001','historical_inspect_v001','historical_extract_v002',
             'post_local_v001','post_relations_v001','post_obstructions_v001',
             'post_readback_v001','post_readback_v002','post_readback_roundtrip_v001',
             'receiver_v001','receiver_edit_v001','receiver_edit_v002',
             'notes_v001','notes_edit_v002','receive_records_v001'):
    for suffix in ('.py','.out','.err'):
        paths.append(W / 'code' / f'S6_SERIES_PUBLISH_c7_ls_{stem}{suffix}')
for name in ('finish_v001_preexecute.py','finish_edit_v002.diff',
             'receiver_edit_v001.diff','receiver_edit_v002.diff',
             'notes_v001.diff','notes_edit_v002.diff','notes_edit_v002_preexecute.py',
             'notes_edit_v002_failed_01.patch','notes_edit_v002_failed_01.out',
             'notes_edit_v002_failed_02.patch','notes_edit_v002_failed_02.out'):
    paths.append(W / 'code' / ('S6_SERIES_PUBLISH_c7_ls_' + name))
for name in ('primary_reading','root_fresh_review','root_lossless_reading'):
    paths.append(W / 'agents/continuation7_iii_root' / f'{prefix}_{name}.md')
for path in paths:
    assert path.exists(), path
where = '; '.join(str(path.relative_to(W)) for path in paths)
source_row = str(canonical[:canonical.index(old_statement)].count('\n') + 1)
shared = (' All three events share evidence group publish:c7:III:02LS and do not multiply independent-proof credit. '
          'No theorem clause or original group assignment is refuted; no D25 or D27 event is proposed. '
          'The frozen fresh files remain unchanged. Canonical application, publication-unit numbering/apparatus/citation work, full build and final-page checks remain root-owned and open; root admission pending.')
specs = [
    ('targeted', 'targeted proof check', 'complete pre-exposure proof with attributed inputs',
     'The complete fresh proof froze2026-11-25T09:29:21Z before individual original release09:37:04.929071Z. Root supplied the attributed local/global vertical argument and primary reading; this lane supplied the actual punctured tensor/period transport and a genuinely new full six-fibre-coordinate/primitive-graph-kernel computation. Admitted LI bar and marked cap inputs retain their exact scopes. The proof establishes all signed a,b, the criterion d0|ab, exact line J_D=f*O(ab/d0), all invariant orbit ambiguity, every positive-weight distribution and period map, and all16 OS45/default fillings with pi1=1,H2=H3=Z/b and all other claimed groups. All maps, units, signs, degeneracies and inverse scopes are explicit.'),
    ('computation', 'computation or formal certificate', 'fresh integral computation and exact post-exposure validation',
     'The fresh381-line OS45 program derives all16 cases from the raw matrices using full Z6 fibre relations and primitive rank17 graph kernels, actual cap coordinates, central ordered words, fixed-normal columns, the relative inverse and full Smith transformations/inverses. All fresh output content was read through its exact reversible reader. Post-exposure sources150/161/43 lines validate all227 local pairs,135 literal obstructions,5696 global residue pairs,82 marked orders and16 extra height-one initial rows, and reconstruct every field of both historical JSON outputs. For all16 filled rows, B_new C=M B_old and B_old D=M^{-1}B_new prove the exact23x70/23x59 quotient correspondence, including J,J^{-1},Q,Q^{-1}. The whole2038-line direct readback contains742 matrices/481 vectors and reconstructs every627+37+138 original stdout line and the JSON bytes. Actual v002 bytes are covered by the proved two-way formatting map plus all six literal metadata lines, not by a duplicate manual-reading claim. No historical target program was executed.'),
    ('used-rechecked', 'used and rechecked in this run', 'whole original, every auxiliary, primary and historical scope',
     'The complete released47-line statement, all232 proof lines/all14 items and the following audit paragraph were read and settled. Added auxiliaries include all additive pairs via exact discriminant pairings, the literal p=0 Smith selector, telescope and finite-index period inclusion, raw/Tate component reflection, invariant divisor E and its q^{-1}u unit/-delta peripheral shear, both Nielsen/central maps and all relation preimages, and the complete six-disc relative inverse. All theorem clauses stand. Three historical target sources were wholly read; needed helper bodies were read only in their disclosed bounded intervals. Two historical JSON outputs are retained and wholly covered through exact lossless reading; the audit JSON404 is preserved and no absent output is claimed. SS10v3 printed25,32--34,50--52 were visually read by root at the documented component/translation/height scope; this lane read the full scope note. All receiving sources, edits, successful streams and available failed-patch inputs/diagnostics are retained, with no unknown bytes reconstructed. The receiver has one proof and no orphan audit tail.'),
]
events = []
for row, (suffix, kind, phase, outcome) in enumerate(specs, 2):
    events.append(dict(statement_id=sid, date=now.date().isoformat(),
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
        type=kind, outcome=outcome + shared, event_id=f'publish:c7:III:02LS:{suffix}',
        phase=phase, source_file=source.name, source_row=source_row,
        source_event_type=kind, evidence_group='publish:c7:III:02LS',
        publish_input_file=str(event_path.relative_to(W)), publish_input_row=str(row),
        date_utc=now.isoformat(), where=where))
write_tsv(event_path, event_fields, events)

assert source.read_bytes() == raw
for path, expected in {**fresh_hashes, **expected_final}.items():
    assert sha256(path.read_bytes()).hexdigest() == expected
print('PREPARED_UTC', now.isoformat())
print('GUARDS', len(guards), 'exact unique spans; every label/hypertarget/tag multiset retained.')
for index, guard in enumerate(guards, 1):
    print('GUARD', index, 'OLD_SHA256', sha256(guard['old_text'].encode()).hexdigest(),
          'NEW_SHA256', sha256(guard['new_text'].encode()).hexdigest(),
          'OLD_LINES', len(guard['old_text'].splitlines()), 'NEW_LINES', len(guard['new_text'].splitlines()))
print('DEFECTS', len(defects), 'bounded notation/computation/orphan repairs; no D25/D27.')
for item in defects:
    print(item['change_id'], item['old_location'], '->', item['new_location'])
    print('REASON', item['reason'])
print('EVENTS', len(events), 'one shared evidence group.')
for event in events:
    print(event['event_id'], '|', event['type'], '|', event['outcome'])
for path in (receiver_path, comparison_path, post_path, guard_path, defect_path, event_path):
    data = path.read_bytes()
    print('FILE', path.relative_to(W), 'LINES', len(data.splitlines()),
          'BYTES', len(data), 'SHA256', sha256(data).hexdigest())
print('PASS local proposals only; all frozen/canonical/global inputs unchanged; LF-only TSVs; no manifest/seal/receipt.')

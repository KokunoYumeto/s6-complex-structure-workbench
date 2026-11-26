#!/usr/bin/env python3
"""Prepare two individually compared exact replacements; do not edit source."""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
SOURCE_HASH = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
FRESH = D / 'S6_SERIES_PUBLISH_III_035Z_038V_fresh_derivation.md'
FRESH_HASH = '9b718285e03205a61fe1fb0b51f741c2a57d7b7829270d28738e8459430e08e6'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == SOURCE_HASH
assert hashlib.sha256(FRESH.read_bytes()).hexdigest() == FRESH_HASH
source = source_bytes.decode('utf-8')
now = datetime.now(timezone.utc).isoformat()

# Exact post-release arithmetic: CRT and the actual block permutations.
for a in range(8):
    for b in range(3):
        k = (9*a+16*b) % 24
        assert (k % 8, k % 3) == (a, b)
for k in range(24):
    assert (9*(k % 8)+16*(k % 3)) % 24 == k
for a, b, wanted in [(3, 6, 1), (6, 6, 1), (3, 3, -1)]:
    permutation = list(range(a, a+b))+list(range(a))
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(a+b) for j in range(i+1, a+b))
    assert inversions == a*b
    assert (-1)**inversions == wanted
for i, n in [(9, 6), (10, 7), (11, 8)]:
    assert i < 2*n-1
print('Post-release CRT, block-twist inversions and exact Freudenthal ranges verified.')


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


EVENT_FIELDS = next(csv.reader((ROOT / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
specs = [
    ('035Z', 'wb:cusp-cone-S12-sphere-map-null', 'corollary',
     'dadeb304467a240e13932dd8c038676e47760f747c2d12bef18804f132e5885a',
     '2026-11-24T11:43:44.181326+00:00'),
    ('038V', 'wb:cusp-s12-full-carrier-null', 'theorem',
     '8ec5dbcd70f685d12a2141c123417ad1b8b9d7f35f72e8671096ebe6aae0a351',
     '2026-11-24T11:43:44.564393+00:00'),
]

for tag, label, environment, proof_hash, release in specs:
    prefix = 'S6_SERIES_PUBLISH_III_'+tag
    statement = (D / (prefix+'_released_statement.tex')).read_text()
    statement = statement[statement.index('\\begin{'+environment+'}'):].strip()
    proof = (D / (prefix+'_released_proof.tex')).read_text()
    proof = proof[proof.index('\\begin{proof}'):].strip()
    assert hashlib.sha256(proof.encode()).hexdigest() == proof_hash
    begin = source.index(statement)
    pbegin = source.index(proof, begin+len(statement))
    assert not source[begin+len(statement):pbegin].strip()
    old = source[begin:pbegin+len(proof)]
    first = source.count('\n', 0, begin)+1
    last = source.count('\n', 0, pbegin+len(proof))+1
    newpath = D / (prefix+'_receiving.tex')
    new = newpath.read_text().strip()
    for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
        assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
    assert '\\StatementRecord' not in new
    assert '\\begin{enumerate}' not in new
    assert new.count('\\begin{proof}') == (tag == '038V')
    assert (D / (prefix+'_comparison.md')).exists()

    reason = ('Exact whole original statement and complete adjacent proof. '
              'Preserve every assertion, tag and label. The canonical mixed-pairing '
              'proof is at038V and the square specialization035Z becomes a numbered '
              'remark referring to it. Shared fresh derivation was completed before '
              'either release; each identity received its own full comparison.')
    write(D / (prefix+'_replacements.tsv'),
          ['statement_id', 'old_text', 'new_text', 'reason'],
          [dict(statement_id=label, old_text=old, new_text=new, reason=reason)])

    defects = []

    def defect(suffix, kind, before, after, why):
        assert before in old, (tag, suffix, 'old fragment missing')
        assert not after or after in new, (tag, suffix, 'new fragment missing')
        defects.append(dict(
            change_id='c6-III-'+tag+'-'+suffix, type=kind, statement_id=label,
            old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}', old_page='',
            new_location=newpath.relative_to(ROOT).as_posix(), new_page='',
            old_text=before, new_text=after, reason=why,
            review_status='proposed; complete original/receiving comparison done; '
                          'root admission, source application and final page review pending'))

    header = next(line for line in statement.splitlines() if line.startswith('\\StatementRecord'))
    defect('header', 'D10', header, '', 'Remove the machine header; all permanent tags and labels remain.')
    enum = '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]'
    defect('enumeration', 'D10', enum, '',
           'Replace the generated hierarchy wrapper by connected mathematical prose.')
    if tag == '035Z':
        defect('duplicate', 'D12', statement.splitlines()[0], new.splitlines()[0],
               'The mixed theorem proves every square. Keep the exact specialization '
               'and native quotient in one numbered remark, referring to the single '
               'canonical038V proof.')
    else:
        defect('suspension-convention', 'D20',
               'Write \\(E\\) for reduced suspension, using the ordered smash coordinates on\nspheres.',
               'To express this in one suspension convention, write',
               'Define the right-suspension representative and explicitly conjugate '
               'the left sixfold suspension by the two block twists; retain the '
               'original ordered composition formula and its tag.')
        defect('unused-reversal', 'D02', 'no such reversal is used here.', '',
               'The comparison verifies the alternate well-typed factorization and '
               'its sign. The printed proof states the exact forward convention '
               'positively and omits the unused defensive clause.')
        defect('bare-toda-attribution', 'D18',
               "Equivalently, Toda's\nBarratt--Hilton reduced-join formula gives, with",
               'Both twists here have degree one and hence are based homotopic to the',
               'Replace the bare reduced-join appeal by the explicit quotient-twist '
               'calculation and the precisely opened degree-classification citation. '
               'Only Toda public Proposition3.1 excerpt reading is credited in the '
               'comparison; no complete Toda proof reading is claimed.')
        defect('stabilization-range', 'D22',
               'the middle group is in the stable\nthree-stem',
               'Indeed, the three Freudenthal inequalities are $9<11$, $10<13$ and',
               'Preserve the original pi12(S9) group and supply the exact suspension '
               'isomorphism from pi9(S6), with each strict range inequality and the '
               'opened Hatcher locator. This also types the relation between the '
               'original and fresh proof paths.')
    write(D / (prefix+'_defects.tsv'), list(defects[0]), defects)

    event_id = 'publish:c6:III:'+tag+':targeted'
    outcome = ('Shared fresh derivation completed and fully reread by '
               '2026-11-24T11:42:07+00:00 (SHA256 '+FRESH_HASH+') before this '
               'identity was individually released '+release+'. ')
    if tag == '035Z':
        outcome += ('Read the complete original statement, every one of its nine proof '
                    'lines and the complete receiving remark. Exact native sphere '
                    'conjugation, continuity, surjectivity, quotient property, '
                    'based homotopy endpoints and the universal square specialization '
                    'agree. Receiving035Z refers to the single mixed-pairing proof038V. ')
    else:
        outcome += ('Read the complete original statement, all62 proof lines and the '
                    'complete receiving theorem/proof. Checked every ordered factor '
                    'and basepoint, all embedded equations0390/0392/0391, exact '
                    'left/right suspension twists, both original postcomposition '
                    'and fresh suspension-precomposition homomorphisms, the '
                    'Freudenthal isomorphism between the two middle groups, full '
                    'integral group arithmetic and native quotient scope. Additional '
                    'post-release readings and their limits are recorded truthfully: '
                    'Hatcher exact corollaries, IWX table and Toda public excerpt. ')
    outcome += ('No theorem refuted; no extra event for the shared arithmetic or '
                'embedded equations. Source application, unit criteria and page '
                'gates remain open.')
    row = dict.fromkeys(EVENT_FIELDS, '')
    row.update(statement_id=label, date=now[:10],
               who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not '
                   'separately exposed; sixth-continuation carriers checker',
               type='targeted proof check', outcome=outcome, event_id=event_id,
               phase='fresh shared derivation followed by individual authorized full comparison',
               source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
               source_event_type='targeted proof check', evidence_group=event_id,
               publish_input_file=(D / (prefix+'_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
               publish_input_row='2', date_utc=now,
               where='; '.join([FRESH.relative_to(ROOT).as_posix(),
                                (D / (prefix+'_comparison.md')).relative_to(ROOT).as_posix(),
                                (D / (prefix+'_replacements.tsv')).relative_to(ROOT).as_posix()]))
    write(D / (prefix+'_CHECK_EVENTS.tsv'), EVENT_FIELDS, [row])
    print(tag, 'source lines', first, '-', last, '; original', len(old.splitlines()),
          'lines; receiver', len(new.splitlines()), 'lines; defects', len(defects))
    print('Guard SHA256 without terminal LF:', hashlib.sha256(old.encode()).hexdigest())
    print('All permanent tags/labels preserved; one proposed event:', event_id)
    for suffix in ['receiving.tex', 'comparison.md', 'replacements.tsv', 'defects.tsv', 'CHECK_EVENTS.tsv']:
        assert b'\r' not in (D / (prefix+'_'+suffix)).read_bytes()

assert SOURCE.read_bytes() == source_bytes
assert hashlib.sha256(FRESH.read_bytes()).hexdigest() == FRESH_HASH
print('Canonical source and frozen fresh derivation unchanged; LF outputs prepared', now)

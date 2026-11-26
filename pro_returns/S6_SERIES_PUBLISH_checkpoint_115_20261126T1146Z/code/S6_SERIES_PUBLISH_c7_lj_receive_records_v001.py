"""Prepare exact local LJ guards, defects and scoped event proposals.

No canonical source or global ledger is modified. The authorized source is
read only for exact span matching, uniqueness, locations and source hash.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation7_iii_mixed_three_receiving'
FRESH = ROOT / 'agents/continuation7_iii_mixed_three'
TAG = '02LJ'
SID = 'maps:src:D.2.42'
PREFIX = f'S6_SERIES_PUBLISH_III_{TAG}'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
raw = SOURCE.read_bytes()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = raw.decode()
fresh_path = FRESH / f'{PREFIX}_fresh_derivation.md'
assert sha256(fresh_path.read_bytes()).hexdigest() == 'ae75303e6b234eb94a85e795a08c5611659bd8939e315fe4f1c413f4c865d4e4'
receiver_path = LANE / f'{PREFIX}_receiving.tex'
receiver = receiver_path.read_text()
assert sha256(receiver_path.read_bytes()).hexdigest() == 'c02b5c344d712c7e30337bdd19e0cee12dc3d051f439ffaec20e3f592c0be0b9'
now = datetime.now(timezone.utc)

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
    buf = io.StringIO(newline='')
    writer = csv.DictWriter(buf, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buf.getvalue(), newline='\n')
    with path.open(newline='') as f:
        got = list(csv.DictReader(f, delimiter='\t'))
    assert got == rows
    assert b'\r' not in path.read_bytes()

csv.field_size_limit(100000000)
old_statement = env((LANE / f'{PREFIX}_released_statement.tex').read_text(), 'theorem')
old_proof = env((LANE / f'{PREFIX}_released_proof.tex').read_text(), 'proof')
old_aux = r"""The extraction program was run at residuals $6,15,30$.
The independent exact local certificate is
\path{code/III/manifolds_three_mixed_AH.py}; its output records
all fourteen patterns, twelve marked rows, $464$
semicharacter substitutions and all three finite normal
coefficients. The full three-primary value is justified
by the primary operation and the Borel comparison above,
not by those finite algebraic checks alone."""
old_proof_and_aux = old_proof + '\n\n' + old_aux
new_statement = env(receiver, 'theorem')
new_proof = env(receiver, 'proof')
assert receiver.rstrip('\n') == new_statement + '\n\n' + new_proof
guards = [
    dict(statement_id=SID, old_text=old_statement, new_text=new_statement,
         reason='Refine all fourteen assignments and the six oriented types, preserving maps:src:D.2.42 and D.MT1/tag020J; add complete marked invariants and model maps.'),
    dict(statement_id=SID, old_text=old_proof_and_aux, new_text=new_proof,
         reason='Replace the exact proof plus its authorized following computational paragraph by one complete proof; settle every auxiliary and retain D.MT2/tag020K, D.MT3/tag020L and all actual parameter/fan maps.'),
]
for guard in guards:
    assert canonical.count(guard['old_text']) == 1
    for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}'):
        assert sorted(re.findall(pattern, guard['old_text'])) == sorted(re.findall(pattern, guard['new_text']))
guard_path = LANE / f'{PREFIX}_replacements.tsv'
write_tsv(guard_path, ['statement_id', 'old_text', 'new_text', 'reason'], guards)

items = re.split(r'(?m)^\\item ', old_proof)[1:]
assert len(items) == 11
items = ['\\item ' + item.rstrip('\n') for item in items]
items[-1] = items[-1].split('\\end{enumerate}', 1)[0].rstrip('\n')

def loc(text, whole, path):
    assert whole.count(text) == 1
    start = whole[:whole.index(text)].count('\n') + 1
    return f'{path}: lines {start}-{start + text.count(chr(10))}'

def defect(number, kind, old, new, reason):
    assert canonical.count(old) == receiver.count(new) == 1
    return dict(
        change_id=f'publish:c7:III:02LJ:{kind}:{number}',
        type=kind, statement_id=SID,
        old_location=loc(old, canonical, SOURCE.name), old_page='source not paginated in this check',
        new_location=loc(new, receiver, str(receiver_path.relative_to(ROOT))), new_page='final PDF page gate open',
        old_text=old, new_text=new, reason=reason,
        review_status='local completed comparison; root admission and source application pending',
    )

new_wall = span(receiver, 'At the cusp the symmetric pairing is', 'For the even sectors')
new_borel = span(receiver, r'On \(C_f\), set \(A=a(\nu-k)\)', r'At \(E_3\), the actual primitive periods')
new_two = span(receiver, 'For the even sectors', r'\paragraph{8.')
new_odd = span(receiver, r'\paragraph{11.', 'For the two-primary projection')
defects = [
    defect('1', 'D27', old_statement, new_statement,
        'The old D.MT1 smooth identifications contradict preserved integral/finite characteristic invariants. Rows1,2,5,14 have actual mod2 cube0 but the claimed conic summand has cube1; every marking unit preserves this value. Rows6,7,10 have actual P=3 in Z/15, of order5, while the claimed zero class has order1. The corrected theorem keeps maps:src:D.2.42 and D.MT1/tag020J, expands all14 rows, gives t=1+kappa mod2 and P_p=(b/p-a*nu)/2, full mu_3=0 in Z/9, and exact inverse marked maps to Y6,t,Y15,epsilon,Y30,t. Counts are2,2,2, not1,2,1.'),
    defect('2', 'D25', items[2], new_wall,
        'The physical polynomial and its period differences are valid, but the asserted wall half-degree evaluates an untransported physical unit wall. The literal prescribed-fan map is C, inverse C^{-1}, with reciprocal frame and the z^a affine monomial; psi_ph(Cv)=-v^tKv+a row1(C)v. It gives half-degree a(nu-b*kappa), retaining the exact units and D.MT2/tag020K. The rank-one formula is independently retained with its nonprimitive content and inverse basis maps.'),
    defect('3', 'D25', items[4], new_borel,
        'The uniform ordinary-curve pullback claim omits the actual rotating rational action. Its Borel bundle has z(z-kT)=0 and U3=rho3(Az), k=b*kappa,A=a(nu-k). For present rows with k nonzero, an integral class dz+lT squares to (d^2 k+2dl)zT+l^2 T^2, forcing d=l=0 for a square-zero class. Thus no map to the ordinary curve can yield the required unit fibre degree. At k0 the ordinary projection is valid. The actual map still gives the full third-power zero because9 divides k^2; no three-primary theorem refutation is inferred.'),
    defect('4', 'D25', items[7], new_two,
        'The invariant undoubled line and its integral supports exist, but its rational involution character is (b/2){a*kappa(b*kappa-nu)-1}=1+kappa mod2, not invariably1. The actual Gaussian, reciprocal frame and integral affine monomial identify its Cartier supports; the elliptic character is0 and the rational degree is odd. Localization therefore gives cube t, and the exact order-two spin-bordism map selects M_t. This intermediate correction causes the four even-sector D27 assignment changes.'),
    defect('5', 'D25', items[8], new_odd,
        'The physical Tate weight w is correct, but D.MT3 uses it after normalizing only the other fixed component. The simultaneous subgroup automorphism z->z^(nu^{-1}), inverse z->z^nu, changes the elliptic weight to w/nu. With alpha_C=(a*nu)^{-1}alpha_p and g_C=(a*nu)s, the coefficient is P_C=(w^2/nu^2-1)/2 and P_p=(a*nu)P_C=(b/p-a*nu)/2. These explicit inverse maps repair the three a1,nu2 five-primary assignments and preserve D.MT3/tag020L.'),
]
defect_fields = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
defect_path = LANE / f'{PREFIX}_defects.tsv'
write_tsv(defect_path, defect_fields, defects)

event_path = LANE / f'{PREFIX}_CHECK_EVENTS.tsv'
with (ROOT / 'CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = next(csv.reader(f, delimiter='\t'))
expected = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
assert event_fields == expected
paths = [
    fresh_path, FRESH/f'{PREFIX}_input_and_primary_scope.md', FRESH/f'{PREFIX}_fresh_execution.md',
    FRESH/f'{PREFIX}_fresh_data_v001.json', FRESH/f'{PREFIX}_fresh_patterns_v001.tsv',
    LANE/f'{PREFIX}_released_statement.tex', LANE/f'{PREFIX}_released_proof.tex',
    receiver_path, LANE/f'{PREFIX}_comparison.md', LANE/f'{PREFIX}_post_exposure_auxiliaries.md',
    guard_path, defect_path,
]
for stem in ('mixed_three_v001','action_coefficients_v001','historical_retrieve_v001',
             'historical_outputs_v001','post_exposure_v001','receiver_v001',
             'receiver_textfix_v002','receiver_textfix_v003','receive_records_v001'):
    for suffix in ('.py','.out','.err'):
        paths.append(ROOT/'code'/f'S6_SERIES_PUBLISH_c7_lj_{stem}{suffix}')
paths += [
    ROOT/'code/S6_SERIES_PUBLISH_c7_lj_receiver_textfix_v003.diff',
    ROOT/'code/S6_SERIES_PUBLISH_c7_lj_notes_edit_v001.failed.patch',
    ROOT/'code/S6_SERIES_PUBLISH_c7_lj_notes_edit_v001.failed.out',
    ROOT/'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LJ_root_fresh_review.md',
]
where = '; '.join(str(p.relative_to(ROOT)) for p in paths)
source_row = str(canonical[:canonical.index(old_statement)].count('\n') + 1)
shared = (' All events share evidence group publish:c7:III:02LJ and do not create another independent proof. '
          'Fresh files remain unchanged. Canonical application, D19 automatic equation/paragraph numbering, publication-unit restructuring, full build and final-page gates remain open. Root admission pending.')
specs = [
    ('targeted', 'targeted proof check', 'pre-exposure complete fresh proof',
     'The complete fresh proof froze2026-11-25T07:46:54Z before release08:00:09.739241Z. It derives all14 patterns from the raw defining fixture, all integral periods and inverse sections, every original/finite cap and affine norm map, actual isotropy, one global equivariant line with units and common character, prescribed-fan cubic, full coefficient-one Z/9 vanishing, refined P and exact CRT/connected-sum recognition. It proves t=1+kappa mod2 and P_p=(b/p-a*nu)/2 in the marked generator, with six oriented types. The root wholly reviewed fresh proof, both different-method programs and every output.'),
    ('computation', 'computation or formal certificate', 'fresh exact computation and bounded post-exposure validation',
     'The two retained fresh programs derive the14-pattern/12-marked-row catalogue and exact integral matrices from raw A_i,g_i, then independently recover odd P through physical weights, simultaneous action normalization and generator inverses; all208+75 stdout lines and actual empty stderr files were read. The later140-line validator/all77 output rechecks the old scope:464 semicharacters,52 adapted multiplicative matrices, exact physical support identities, nonprimitive rank-one periods and three finite coefficients6,15,15. It compares all historical JSON rows and finds exactly changed patterns1,2,5,6,7,10,14. No historical program execution or finite-program proof of the full operation is claimed.'),
    ('refuted-classification', "refuted, with the refined statement's id", 'whole-original smooth-type comparison',
     'D27: the refined statement retains maps:src:D.2.42 and display maps:eq:D.MT1/tag020J. Its full corrected models are Y6,t=M_t#M3,0, Y15,epsilon=M3,0#Z5,epsilon, Y30,t=M_t#M3,0#Z5,0, with t=1+kappa mod2, P6=3t,mu6=9t mod18; P15=3epsilon,mu15=0 mod45; P30=15t,mu30=45t mod90; P_p=(b/p-a*nu)/2, epsilon=[P5 nonzero], and full mu3=0 in Z/9. Rows1,2,5,14 change from conic cube1 to cube0. Rows6,7,10 change from P order1 to order5. The exact fourteen-row D.MT1 table and inverse model maps realize two types in each sector, counts2,2,2.'),
    ('refuted-intermediates', "refuted, with the refined statement's id", 'bounded original intermediate assertions',
     'D25 refinements remain inside maps:src:D.2.42, preserving maps:eq:D.MT2/tag020K and maps:eq:D.MT3/tag020L. The exact C/C^{-1}, reciprocal frame and affine monomial replace the physical-unit-wall degree by a(nu-b*kappa); the actual rotating rational Borel bundle has z(z-kT)=0, not the asserted ordinary-curve pullback on k-nonzero rows; the involution character is1+kappa; and the common subgroup automorphism gives P_C=(w^2/nu^2-1)/2 with P_p=(a*nu)P_C. Every new map has its inverse. The original full three-primary vanishing remains valid and is not refuted.'),
    ('used-rechecked', 'used and rechecked in this run', 'whole original, all auxiliaries, primary and historical scope',
     'The complete released statement, all11 original proof items/all143 proof lines and the following8-line computational paragraph were read and settled. The alternate whole-circle restriction is proved with explicit finite-group cochain averaging and kept in post-exposure checks; the used arbitrary-map target Omega6Spin(K(Z/3,2))=Z/9 map, homotopy wedge/product inverse, spin-bordism CRT and marked connected-sum inverse are explicit. Exact primary scopes include Cartan, Thomas1956/1959 and Zhubr Theorem5 plus Section4.1 zero-free-H3 recognition. The pinned118-line historical source and724-line JSON were read; broad old helper data were not opened; no historical execution occurred. Three .out retrievals returned404 and remain in actual streams; no historical stdout file is claimed. Final programs/streams and the rejected note patch/actual diagnostic are retained; the final receiver has one proof and no trailing unnumbered auxiliary.'),
]
events = []
for i, (suffix, kind, phase, outcome) in enumerate(specs, 2):
    events.append(dict(statement_id=SID, date=now.date().isoformat(),
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
        type=kind, outcome=outcome+shared, event_id=f'publish:c7:III:02LJ:{suffix}',
        phase=phase, source_file=SOURCE.name, source_row=source_row,
        source_event_type=kind, evidence_group='publish:c7:III:02LJ',
        publish_input_file=str(event_path.relative_to(ROOT)), publish_input_row=str(i),
        date_utc=now.isoformat(), where=where))
write_tsv(event_path, event_fields, events)

assert SOURCE.read_bytes() == raw
assert sha256(fresh_path.read_bytes()).hexdigest() == 'ae75303e6b234eb94a85e795a08c5611659bd8939e315fe4f1c413f4c865d4e4'
print('Prepared UTC:', now.isoformat())
print('GUARDS:', len(guards), 'exact unique spans; permanent label/target/tag multisets retained.')
for i, guard in enumerate(guards, 1):
    print('GUARD', i, 'OLD_SHA256', sha256(guard['old_text'].encode()).hexdigest(),
          'NEW_SHA256', sha256(guard['new_text'].encode()).hexdigest(),
          'OLD_LINES', len(guard['old_text'].splitlines()), 'NEW_LINES', len(guard['new_text'].splitlines()))
print('DEFECTS:', len(defects))
for d in defects:
    print(d['change_id'], d['old_location'], '->', d['new_location'])
    print('REASON:', d['reason'])
print('EVENTS:', len(events))
for e in events:
    print(e['event_id'], '|', e['type'], '|', e['outcome'])
for path in (receiver_path, LANE/f'{PREFIX}_comparison.md', LANE/f'{PREFIX}_post_exposure_auxiliaries.md', guard_path, defect_path, event_path):
    print('FILE', path.relative_to(ROOT), 'LINES', len(path.read_text().splitlines()), 'SHA256', sha256(path.read_bytes()).hexdigest())
print('PASS: local proposals only; canonical/global ledgers unchanged; frozen fresh unchanged; no manifest/seal/receipt written.')

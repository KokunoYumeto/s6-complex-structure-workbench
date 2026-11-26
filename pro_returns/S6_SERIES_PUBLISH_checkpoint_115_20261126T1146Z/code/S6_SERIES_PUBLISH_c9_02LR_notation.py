"""Separate four observed symbol bindings in the fully reread 02LR proof."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
start = before.rfind(r'\begin{theorem}', 0, before.index(r'\label{maps:src:D.2.5}'))
end = before.index(r'\end{proof}', start) + len(r'\end{proof}')
proof = before[start:end]

def block(first, following):
    a = proof.index(first)
    b = proof.index(following, a)
    return proof[a:b]

edits = []
old = block('Writing $s_0=3,s_1=2$', 'At infinity,')
new = old.replace('s_0=3,s_1=2', r'\kappa_0=3,\kappa_1=2').replace('s_i', r'\kappa_i')
edits.append(('COINVARIANT-COEFFICIENTS', old, new,
    'The coinvariant coefficients s_0=3,s_1=2 and all their uses in H_1(F_i) are renamed kappa_0,kappa_1. The later s_1,...,s_6 remain the six exterior-basis vectors. The scalar assignment is kappa_i=s_i with inverse s_i=kappa_i; it fixes both integer values and every quotient, section and kernel map.'))
old = block('In the exterior basis', 'Cutting the peripheral trace')
new = re.sub(r'E_([i01])', r'{\\mathsf E}_\1', old)
edits.append(('EXTERIOR-RELATION-MATRICES', old, new,
    'The exterior-action matrices E_i=exterior-square(A_i)-I are renamed mathsf E_i, including every E_0/E_1 preimage formula. The exceptional divisors E_j in the later cusp normalization keep their names. The forward and reverse name maps fix each matrix entry, image submodule and displayed witness.'))
old = block('Recording the row and column additions', 'Thus $H_2(X)=')
new = old.replace('U', r'{\mathsf U}').replace('V', r'{\mathsf V}')
edits.append(('SMITH-CHANGE-MATRICES', old, new,
    'The Smith change matrices U,V are renamed mathsf U,mathsf V throughout UKV, the quotient coordinate, inverse generator and boundary preimage. V earlier denotes the complementary torus bundle. The new matrices are exactly the old matrices, with the reverse name assignment as inverse; all operations and cyclic coordinates are retained.'))
old = block('maps to $(1,1,m)\\in\\ker G$. Let $h$', 'The smooth torus')
new = old.replace('Let $h$ be', r'Let $h_{\rm cok}$ be').replace('ah+b[Z]', r'a h_{\rm cok}+b[Z]')
edits.append(('COKERNEL-GENERATOR', old, new,
    'The cokernel class represented by (-zeta,eta,0,0) becomes h_cok; the earlier h=d-dual(v_1) remains an integer edge coordinate. The group class, its representative, assembly map (a,b)->a h_cok+b[Z], connecting map and subtract-then-project inverse are unchanged under the exact name map h_class<->h_cok.'))

after = before
for name, old, new, reason in edits:
    assert old != new and after.count(old) == 1, name
    after = after.replace(old, new, 1)
inverse = after
for name, old, new, reason in reversed(edits):
    assert inverse.count(new) == 1, name
    inverse = inverse.replace(new, old, 1)
assert inverse == before
identifiers = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert identifiers(before) == identifiers(after)
assert re.findall(r'\d+', before) == re.findall(r'\d+', after)

def read_table(path):
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

def write_table(path, fields, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

df, defects = read_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv')
ef, events = read_table(ROOT / 'CHECK_EVENTS.tsv')
now = datetime.now(timezone.utc).isoformat()
for name, old, new, reason in edits:
    change_id = 'CLAUDE-III-P15-02LR-' + name
    assert not any(r['change_id'] == change_id for r in defects)
    row = dict.fromkeys(df, '')
    row.update(change_id=change_id, type='D20', statement_id='maps:src:D.2.5',
        old_location='02LR proof; exact source fragment', new_location='same proof and mathematical maps',
        old_text=old, new_text=new, reason=reason,
        review_status='Root read the full 412-line statement/proof and every exact changed binding. Guarded inverse preserves all source bytes; numerical literals and permanent targets retained. Admitted ' + now + '; final page reading pending.')
    defects.append(row)
eid = 'publish:c9:III:02LR:notation-reread'
assert not any(r['event_id'] == eid for r in events)
event = dict.fromkeys(ef, '')
event.update(statement_id='maps:src:D.2.5', date=now[:10],
    who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine root',
    type='used and rechecked in this run',
    outcome='Read the full current 02LR statement and proof, including affine freeness, the explicit fundamental-group isomorphism/inverse, degree-one kernel, all exterior-relation preimages, normal-circle matrices, Smith maps and the P=0 integral splitting. Separated the scalar coinvariant coefficients from exterior basis vectors, relation matrices from exceptional divisors, Smith matrices from the complementary space, and cokernel class from an integer edge coordinate. Exact reverse source substitution and unchanged numerical literals checked. This is an exposed complete-proof symbol-binding reread, not an independent proof or a new required check; final page review remains.',
    event_id=eid, phase='publication continuation 9',
    source_file='code/S6_SERIES_PUBLISH_c9_02LR_notation.py', source_event_type='used and rechecked in this run',
    evidence_group=eid, date_utc=now, where='02LR complete proof and four exact D20 defect rows')
events.append(event)
source.write_text(after, newline='\n')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects)
write_table(ROOT / 'CHECK_EVENTS.tsv', ef, events)
print('Admitted four 02LR symbol-binding corrections after complete statement/proof reading.')
print('All numerical literals, labels and targets retained; exact inverse recovers pre-edit source.')
for name, old, new, reason in edits:
    print(name)
    if name == 'SMITH-CHANGE-MATRICES':
        print(new)

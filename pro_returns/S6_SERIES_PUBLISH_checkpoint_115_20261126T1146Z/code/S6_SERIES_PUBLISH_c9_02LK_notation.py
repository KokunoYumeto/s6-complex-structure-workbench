"""Exact scoped notation changes after the complete 02LK statement/proof reread."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
start = before.rfind(r'\begin{theorem}', 0, before.index(r'\label{maps:src:D.2.43}'))
end = before.index(r'\end{proof}', start) + len(r'\end{proof}')
proof = before[start:end]

def block(first, following=None):
    a = proof.index(first)
    b = proof.index(following, a) if following else len(proof)
    return proof[a:b]

edits = []
old = block(r'\noindent\emph{The central fibre and branch resolution.}', 'For cellular calculations,')
new = re.sub(r'(?<![A-Za-z\\])h(?![A-Za-z])', lambda m: r'{\rho_q}', old)
new = re.sub(r'(?<![A-Za-z\\])H(?![A-Za-z])', lambda m: r'{\mathcal H}', new)
new = re.sub(r'(?<![A-Za-z\\])W(?![A-Za-z])', lambda m: r'W_{\rm rad}', new)
edits.append(('RADIAL-FLOW', old, new,
    'On the central-fibre flow block set rho_q=h=|q|^2, mathcal H=H and W_rad=W, with the reverse assignments h=rho_q, H=mathcal H and W=W_rad. These equalities fix every value of the function, gradient, flow time, radial-level map and strong deformation retraction; inclusion is still its stated homotopy inverse. They separate the function from the later Laurent polynomial h, the retraction from the hyperplane class H and chain homotopy H, and the vector field from the later three-chain W.'))

old = block('In the cyclic divisor order', 'The cancellation is')
new = re.sub(r'E_([123])', lambda m: r'{\mathcal E}_' + m.group(1), old)
edits.append(('EXCEPTIONAL-DIVISORS', old, new,
    'Set mathcal E_j=E_j for the three exceptional divisors, including the cyclic order, intersection basis and inverse change of basis from the four D_j curves. The reverse assignment E_j=mathcal E_j preserves all divisor classes and intersection maps. The later E_1,E_2 remain the coordinate vectors of I/I^2 used in the Tor connecting map. The coordinate reflection E and the hyperplane divisor H keep their names.'))

old = block('Here are explicit maps for the homology differential, including', r'\(C\) gives every syzygy')
new = old.replace('D_0', r'{\mathsf D}_0').replace('E_0', r'{\mathsf E}_0')
new = new.replace('H&=', r'{\mathsf H}&=').replace(r'\(H\)', r'\({\mathsf H}\)')
new = new.replace('dH', r'd{\mathsf H}').replace('Hd', r'{\mathsf H}d')
edits.append(('CHAIN-COMPARISON-MATRICES', old, new,
    'Set mathsf D_0=D_0 and mathsf E_0=E_0 for the two displayed diagonal matrices and mathsf H=H for the displayed 3-by-4 chain homotopy, with the reverse equalities as inverse name assignments. Each matrix entry, the Q/sigma and A_1/A_2 maps, and both chain-homotopy identities are unchanged. This separates D_0 from the retained divisor curve D_0, E_0 from the exceptional-divisor notation, and the chain homotopy from the retained hyperplane divisor H.'))

old = block('The Laurent division itself has an explicit formula at every sign.', r'For \(c\in J_L\)')
new = old.replace('U', r't_u').replace('V', r't_v')
edits.append(('LAURENT-MONOMIALS', old, new,
    'Within the complete Laurent-division paragraph set t_u=U=X^u and t_v=V=X^v, with inverse U=t_u and V=t_v. These are the same Laurent-ring elements. The geometric-sum decomposition, including zero and negative powers, retains every exponent and term. The cancellation matrices U,V introduced above remain unchanged.'))

old = block(r'Choose integer Smith matrices \(U,V\) with')
new = old.replace('U,V', 'U_L,V_L').replace('UB_0V', 'U_L B_0 V_L')
new = new.replace('U^{-1}', 'U_L^{-1}').replace(r'\(V\)', r'\(V_L\)')
edits.append(('BOUNDARY-SMITH-MATRICES', old, new,
    'On the complete boundary-coordinate and component-disc tail set U_L=U and V_L=V for the integer Smith matrices of B_0. The reverse assignments recover those same matrices. This preserves U_L B_0 V_L=diag(s,t), both basis changes, all component representatives U_L^{-1}(i,j), and both integral monodromy-cylinder preimages B_0^{-1}sU_L^{-1}e_1 and B_0^{-1}tU_L^{-1}e_2. The earlier Laurent cancellation matrices U,V keep their names and domains.'))

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
    change_id = 'CLAUDE-III-P15-02LK-' + name
    assert not any(r['change_id'] == change_id for r in defects)
    row = dict.fromkeys(df, '')
    row.update(change_id=change_id, type='D20', statement_id='maps:src:D.2.43',
        old_location='02LK complete proof; exact scoped fragment', new_location='same proof and mathematical maps',
        old_text=old, new_text=new, reason=reason,
        review_status='Root read the complete 942-line statement/proof and the exact changed bindings, including all subsequent representative formulas. Exact reverse substitutions recover every pre-edit source byte; numerical literals and permanent targets retained. Admitted ' + now + '; final rendered-page review remains.')
    defects.append(row)
eid = 'publish:c9:III:02LK:notation-reread'
assert not any(r['event_id'] == eid for r in events)
event = dict.fromkeys(ef, '')
event.update(statement_id='maps:src:D.2.43', date=now[:10],
    who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine root',
    type='used and rechecked in this run',
    outcome='Read the complete 02LK statement and proof: toroidal charts and units, radial deformation, normalization modules and chain homotopies, finite-cover Tor maps, integral homology, boundary Smith coordinates, component-disc kernels and quotient inverses. Separated the five scoped groups of repeated names recorded in the matching D20 rows by exact forward/reverse assignments. Existing numbers, maps and inverse formulas retained. This is an exposed whole-proof notation reread, not an independent proof, a new computation or a required-check rerun; final page reading remains.',
    event_id=eid, phase='publication continuation 9',
    source_file='code/S6_SERIES_PUBLISH_c9_02LK_notation.py', source_event_type='used and rechecked in this run',
    evidence_group=eid, date_utc=now, where='02LK full statement/proof and five exact D20 rows')
events.append(event)
source.write_text(after, newline='\n')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects)
write_table(ROOT / 'CHECK_EVENTS.tsv', ef, events)
print('Admitted five scoped 02LK notation rows and one exposed full-proof rereading event.')
print('Exact reverse source recovery, numerical literals and permanent targets verified.')
for name, old, new, reason in edits:
    print(name, 'old/new characters', len(old), len(new))

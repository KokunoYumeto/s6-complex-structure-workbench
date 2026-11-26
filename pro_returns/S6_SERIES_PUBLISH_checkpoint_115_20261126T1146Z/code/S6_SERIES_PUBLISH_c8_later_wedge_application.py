#!/usr/bin/env python3
"""Replace only the repeated 037M wedge-recognition argument by 02QC."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'agents/continuation8_iii_integration/units/later/further_cusp_carriers.tex'
owner = ROOT / 'agents/continuation8_iii_integration/units/root/carrier_wedge_recognition.tex'
source = path.read_text()
before = source
assert hashlib.sha256(source.encode()).hexdigest() == '7ff5743e27b8ccac6d5256ff73dd457b18549fe4f482b6cd22dccaf44f8ae2f7'
assert 'Set $G=kj_C$.' in owner.read_text()
start_token = r'Choose a based map $\alpha:S^2\to\mathcal C$ representing $u$'
end_token = 'homotopy inverse $L$.'
assert source.count(start_token) == source.count(end_token) == 1
start = source.index(start_token)
end = source.index(end_token, start) + len(end_token)
old = source[start:end]
new = r'''Apply \cref{mapsIII:carrier-three-complex-wedge} with
$C=\mathcal C$, based at its cusp vertex, and with the ordered
generators $u,v$ just computed. The comparison of the complex in
that lemma with this target is the identity, with itself as inverse.
Choose its sphere maps $a,b$ for these generators and put
$\alpha=a$, $\beta=b$. Its wedge equivalence, denoted here by $G$, is
\[
 G=\alpha\vee\beta:S^2\vee S^3\longrightarrow\mathcal C,
 \qquad G_*[S^2]=u,\quad G_*[S^3]=v.
\]
In the lemma's second mapping cylinder its inverse is $L=kj_C$.
The specified homotopies $kU_t$ and $pT_sj_C$ give
$LG\simeq\operatorname{id}_{S^2\vee S^3}$ and
$GL\simeq\operatorname{id}_{\mathcal C}$ through based maps. Thus
\[
 L_*u=[S^2],\qquad L_*v=[S^3].
\]
These are the same primitive boundary-kernel and oriented-torus
generators under the cone exact sequence above.'''
source = source[:start] + new + source[end:]
pattern = re.compile(r'\\(?:label|hypertarget)\{([^}]+)\}')
assert Counter(pattern.findall(before)) == Counter(pattern.findall(source))
assert source.count(old) == 0 and source.count(new) == 1
path.write_text(source)
record = dict(change_id='c8-III-carrier-wedge-001', type='D06/D12/D14/D20',
    statement_id='wb:cusp-cone-target-homotopy-types',
    old_location=str(path.relative_to(ROOT)) + ':' + str(before[:start].count('\n') + 1),
    old_page='pending final concordance', new_location=str(path.relative_to(ROOT)) + '; same 037M proof',
    new_page='pending final build', old_text=old, new_text=new,
    reason='Use the earlier complete 02QC proof on the identical based complex with u=boundary-kernel generator and v=oriented boundary-torus generator. The renaming a=alpha,b=beta,F=G,G_inverse=L has the displayed inverse generator maps and based inverse homotopies. Retain every carrier-specific group, boundary, 49/16 smash and zero/nonzero representative argument.',
    review_status='staged; complete rewritten 037M proof reading pending')
out = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_carrier_wedge_followup_defects.tsv'
with out.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, list(record), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerow(record)
assert b'\r' not in out.read_bytes()
print('Carrier source', len(source.splitlines()), hashlib.sha256(source.encode()).hexdigest())
print('QC owner read', len(owner.read_text().splitlines()), hashlib.sha256(owner.read_bytes()).hexdigest())
print('Exact replaced paragraph', len(old.splitlines()), 'lines; application', len(new.splitlines()), 'lines.')
print('One exact local defect; all prior labels and targets preserved; no other manuscript fragment or shared table changed.')

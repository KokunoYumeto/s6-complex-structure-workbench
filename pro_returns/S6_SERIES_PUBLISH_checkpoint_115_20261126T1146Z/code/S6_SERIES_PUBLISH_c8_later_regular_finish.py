#!/usr/bin/env python3
"""Bounded refinements found during the complete 039U readback."""
from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'agents/continuation8_iii_integration/units/root/regular_quotients.tex'
defects = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_regular_publication_defects.tsv'
text = path.read_text()
assert hashlib.sha256(text.encode()).hexdigest() == 'b41deecdf73536001b93801122ca6933cb26f2c088be300ae9e82b5ddf69dea9'
with defects.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
edits = [
    (r''' =\mathbb Z\langle\widehat u,\widehat w,\widehat\delta\rangle.

\end{equation}''', r''' =\mathbb Z\langle\widehat u,\widehat w,\widehat\delta\rangle.
\end{equation}''', 'D19/D23', 'mapsIII:def:regular-quotient-data',
     'Remove the empty display line left by deleting manual tag G.1; the mathematical display body is otherwise unchanged.'),
    (r''' \kappa_j=\varepsilon_\gamma(v_j).

\end{equation}''', r''' \kappa_j=\varepsilon_\gamma(v_j).
\end{equation}''', 'D19/D23', 'wb:cusp-spec-globalization-obstruction',
     'Remove the empty display line left by deleting manual tag G.2; all finite cap coefficients remain unchanged.'),
    (r'''nontrivial element of the kernel. Pulling back to the universal cover
and using the composite monodromy representation gives the same family.''',
     r'''nontrivial element of the kernel. Let
$p:\widetilde B^\circ\to\mathfrak h_z^\circ$ be the lift of the
universal base cover. In the flat marking the comparison of the
two family quotients is
\[
 [\widetilde z,x]\longmapsto[p(\widetilde z),x].
\]
Its inverse chooses any lift $\widetilde z$ of $z$ and sends
$[z,x]$ to $[\widetilde z,x]$. Two such lifts differ by the
kernel of $\pi_1(B^\circ)\to\Delta$, which acts trivially on the
marked fibre. The inverse is therefore independent of that choice;
local covering charts prove continuity and real analyticity in both
directions. These maps identify the same group family.''',
     'D20', 'wb:cusp-spec-globalization-obstruction',
     'Display the actual universal-cover comparison and inverse already implied by the exact covering-group sequence; deck-kernel invariance proves its well-definedness.'),
    (r'''the coordinate change is \(a_{\rm native}=B_0a\), with the physical
complex coordinate fixed.''', r'''the coordinate change is $a_{\rm native}=B_0a$, with inverse
$a=B_0^{-1}a_{\rm native}$ and with the physical complex coordinate fixed.''',
     'D20', 'wb:cusp-spec-globalization-obstruction',
     'Write the inverse of the displayed native/common period change; the following block identity and the unchanged fan action prove the same comparison.'),
    (r'''infinity because they are proper linear maps. The maps $h^{\wedge n}$
and its inverse descend from the coordinatewise based diffeomorphisms.''',
     r'''infinity because they are proper linear maps. Both $h^{\wedge n}$
and its inverse descend from the coordinatewise based diffeomorphisms.''',
     'D23', 'wb:cusp-spec-globalization-obstruction',
     'Correct the grammatical agreement in the already-read smash-continuity sentence.'),
]
for old, new, kind, sid, reason in edits:
    assert text.count(old) == 1, old[:80]
    line = text[:text.index(old)].count('\n') + 1
    rows.append(dict(change_id='c8-III-regular-%03d' % (len(rows) + 1),
        type=kind, statement_id=sid, old_location=str(path.relative_to(ROOT)) + ':' + str(line),
        old_page='pending final concordance', new_location=str(path.relative_to(ROOT)) + '; same owner',
        new_page='pending final build', old_text=old, new_text=new, reason=reason,
        review_status='staged; final bounded-source reading pending'))
    text = text.replace(old, new)
    print('Bounded edit', line, kind, sid)
path.write_text(text)
with defects.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
assert b'\r' not in defects.read_bytes()
print('Final source', len(text.splitlines()), hashlib.sha256(text.encode()).hexdigest())
print('Exact local edit rows', len(rows), '; LF preserved; no shared files changed.')

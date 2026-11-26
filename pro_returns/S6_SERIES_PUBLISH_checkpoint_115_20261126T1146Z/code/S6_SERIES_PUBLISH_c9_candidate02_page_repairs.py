#!/usr/bin/env python3
"""Prepare observed candidate02 repairs; never write the canonical manuscript."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
s = SOURCE.read_text()
packet = OUT / 'S6_SERIES_PUBLISH_c9_candidate02_page_repairs.json'
rows = json.loads(packet.read_text())[:3]

def add(ident, unit, page, old, new, reason, equivalence):
    assert old != new
    assert s.count(old) == 1, (ident, s.count(old))
    rows.append(dict(id=ident, source=SOURCE.name, unit=unit, page=page,
                     status='proposed; canonical source unchanged', old=old, new=new,
                     reason=reason, equivalence=equivalence,
                     verification_scope='Actual candidate02 page images and exact source context read after proof exposure. Used and rechecked in this run; no independent mathematical-check credit. Changed pages require new-build image verification.'))

add('c9-current02-page298-section-opening', 'maps:src:D.2.30', 298,
    r'''\section{Finite cap lattices and natural catalogues}
\subsection{All finite additive lattices and affine twists}''',
    r'''\Needspace{12\baselineskip}
\section{Finite cap lattices and natural catalogues}
\subsection{All finite additive lattices and affine twists}''',
    'Actual page298 ends with the section and subsection headings and Definition12.1 title/tag; page299 contains the whole definition body. Reserve space for the hierarchy and body using the already loaded needspace package.',
    'Only a layout-space reservation is inserted. Every existing text token, mathematical object, map, inverse, label and target is unchanged; the correspondence on each is identity. Removing the added command and LF is the exact source inverse.')

add('c9-current02-page311-crt-display', 'maps:src:D.2.31', 311,
    r'''\[
 t_j(u)=E_j(R/m_j){t_{\rm reg}}(u) -
 \left(k_j\omega(u,v_j)+E_j\sum_{\ell\ne j}
       \frac{R}{m_jm_\ell}\omega(u,v_\ell)\right)s,
 \quad E_j(R/m_j)=1+k_jm_j.
\]''',
    r'''\[
\begin{gathered}
 t_j(u)=E_j(R/m_j){t_{\rm reg}}(u) -
 \left(k_j\omega(u,v_j)+E_j\sum_{\ell\ne j}
       \frac{R}{m_jm_\ell}\omega(u,v_\ell)\right)s,\\
 E_j(R/m_j)=1+k_jm_j.
\end{gathered}
\]''',
    'The actual regular-site CRT inverse display on311 extends well into the right margin. Put its defining coefficient identity on a second display row.',
    'Every algebraic token, summation index, sign, denominator and coefficient is retained. The same tuple of regular sweep classes is sent by exactly the same CRT inverse formula. Only gathered layout and a row boundary are added, and the spacing command quad is removed. The opposite text replacement recovers the exact old block.')

add('c9-current02-page291-local-homology', 'maps:src:D.2.27', 291,
    r'''The star conductor calculation gives its free
rank-two group. For finite caps the primitive relation
$m_i g=v_i$ and the B\'ezout condition $\gcd(m_i,n_i)=1$ give a
free rank-two group; for regular caps the group is the free lattice''',
    r'''The star conductor calculation gives its free abelian
rank-two group. For finite caps the primitive relation
$m_i g=v_i$ and the B\'ezout condition $\gcd(m_i,n_i)=1$ give a
free abelian rank-two group; for regular caps the group is the free lattice''',
    'This paragraph explicitly concerns the degree-one homology groups used in the subsequent Mayer--Vietoris map. State their additive free-abelian structure in the two rank-two descriptions.',
    'The same displayed integral bases identify each group with Z^2: a pair of integers maps to its linear combination of the retained basis classes, and the inverse reads their coefficients. The conductor and Bezout inverse coordinates are retained literally. No presentation, relation or group is replaced.')

add('c9-current02-page291-mv-homology', 'maps:src:D.2.27', 291,
    r'''an isomorphism between free groups. Hence $H_2(X)$ is exactly
the finite cokernel of $M$.''',
    r'''an isomorphism between free abelian groups. Hence $H_2(X)$ is exactly
the finite cokernel of $M$.''',
    'The map in question is the degree-one Mayer--Vietoris homology map between the already displayed additive lattices.',
    'The domain and codomain are the same integral H1 direct sums, and the same displayed matrix represents the map in their retained bases. Coordinate tuples map to the same linear combinations, with the stated basis-coordinate inverse. Adding abelian changes no matrix or cokernel assertion.')

add('c9-current02-page293-component-lattice', 'maps:src:D.2.28', 293,
    r'''together with the equality in the free group on $\mathbb Z/\nu$''',
    r'''together with the equality in the free abelian group on $\mathbb Z/\nu$''',
    'The following additive component-degree equation is written in the integral basis indexed by residue classes modulo nu.',
    'The named lattice is Z[Z/nu]. The map (n_h) to sum_h n_h[h] has inverse that reads the coefficient at each residue class h; the displayed equality retains every coefficient and residue class. Only the adjective abelian is added.')

candidate = s
for row in rows:
    assert candidate.count(row['old']) == 1, row['id']
    candidate = candidate.replace(row['old'], row['new'], 1)
restored = candidate
for row in reversed(rows):
    assert restored.count(row['new']) == 1, row['id']
    restored = restored.replace(row['new'], row['old'], 1)
assert restored == s
for pattern in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}']:
    assert re.findall(pattern, candidate) == re.findall(pattern, s)
crt = next(row for row in rows if row['id'].endswith('crt-display'))
def math_tokens(text):
    for token in [r'\begin{gathered}', r'\end{gathered}', r'\quad', r'\\']:
        text = text.replace(token, '')
    return re.sub(r'\s+', '', text)
assert math_tokens(crt['old']) == math_tokens(crt['new'])
packet.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
fields = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT / 'S6_SERIES_PUBLISH_c9_candidate02_page_repairs_defects.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow(dict(change_id=row['id'],type='D20',statement_id=row['unit'],
            old_location='Paper III, candidate02 physical page '+str(row['page']),old_page=str(row['page']),
            new_location='same permanent unit',new_page='pending changed build',
            old_text=row['old'],new_text=row['new'],reason=row['reason']+' '+row['equivalence'],review_status=row['verification_scope']))
print(f'{len(rows)} guarded observed-page repairs prepared; canonical source unchanged.')
print('Exact reverse and all labels/targets verified; CRT mathematical token sequence retained.')

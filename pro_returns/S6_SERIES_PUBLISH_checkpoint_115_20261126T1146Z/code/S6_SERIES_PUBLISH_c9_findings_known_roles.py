#!/usr/bin/env python3
"""Bounded P15 follow-up proposals; never mutate canonical source or ledgers."""
from pathlib import Path
import csv
import difflib
import json
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import math_letters

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
work = source
rows = []
counts = {}


def edit(tag, unit, pages, first, last, transform, reason):
    global work
    a = work.index(first)
    b = work.index(last, a + len(first))
    old = work[a:b]
    new = transform(old)
    assert old != new
    assert work.count(old) == 1
    for pat in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}', r'\d+']:
        assert re.findall(pat, old) == re.findall(pat, new), pat
    counts[tag] = counts.get(tag, 0) + 1
    rows.append(dict(
        change_id=f'CLAUDE-III-P15-current02-knownroles-{tag}-{counts[tag]:03}',
        type='D20', statement_id=unit,
        old_location=f'Paper III, tag {tag}; exact known-role context',
        old_page='candidate02 ' + pages,
        new_location='same result and explicitly identified coefficient-map imports',
        new_page='pending changed rendering', old_text=old, new_text=new,
        reason=reason,
        review_status='Used and rechecked in this run after exposure. Current role contexts and all affected uses read, with earlier complete proof reviews retained. Same objects and maps under explicit reversible substitutions; labels, targets, numeric literals and full-source reversal checked. No independent proof credit; admission and changed rendering pending.'))
    work = work[:a] + new + work[b:]


edit('02L8', 'maps:src:D.2.32', '315–322',
     'every finite good-reduction additive place the option set is',
     'The finite arithmetic choices have their complete parameter scope',
     lambda t: math_letters(t, {'O': r'\mathrm O', 'F': r'\mathrm F'}),
     'Print the original/finite option labels upright as mathrm O and mathrm F. The original germ and finite affine family assigned to each label, every site product and every parameter remain identical. The option-set bijection sends old O to upright O and old F to upright F, with the inverse removing the upright font. The whole-fibre vector F and all its integral maps retain their existing notation.')

edit('02LA', 'maps:src:D.2.34', '329–337',
     r'Over $\mathcal A_d=\mathbb Z[t]/(t^d-1)$',
     'The degree-zero row is the dual marked torus complex;',
     lambda t: math_letters(t, {'t': r't_{\rm cyc}'}),
     'Qualify the cyclic coefficient-ring generator as t_cyc while retaining the geometric sweep t. The coefficient isomorphism sends the class of a polynomial p(t) to p(t_cyc), with inverse p(t_cyc) to p(t). It takes t^d-1 to t_cyc^d-1, preserves every integer coefficient and carries every displayed matrix entry, row operation, kernel, cokernel and partial-sum inverse to the same cyclic-coordinate map.')


def first_import(t):
    t = t.replace(r'$[p(t)]\mapsto[p(t)]$',
                  r'$[p(t)]\mapsto[p(t_{\rm cyc})]$, with inverse '
                  r'$[p(t_{\rm cyc})]\mapsto[p(t)]$')
    t = t.replace('with that same index and coefficient.',
                  r'with that same index and coefficient $t_{\rm cyc}^j$.')
    t = t.replace('the degree-two matrix is identical;',
                  'the degree-two matrix agrees under this coefficient substitution;')
    return t


edit('02LD', 'maps:src:D.2.37', '343',
     r'Identify $\mathcal R_d$ with the coefficient ring $\mathcal A_d$',
     'This chain isomorphism carries the unit and', first_import,
     'Propagate the renamed t_cyc generator of Theorem 13.2 into this exact coefficient-ring comparison. Each component, branch and dual-torus cell keeps its index and integer coefficients; t^j maps to t_cyc^j. The displayed forward and reverse polynomial substitutions are inverse ring and chain maps, so the imported normalization calculation is unchanged.')


def second_import(t):
    t = t.replace(r'$[p(t)]\mapsto[p(t)]$',
                  r'$[p(t)]\mapsto[p(t_{\rm cyc})]$, with inverse '
                  r'$[p(t_{\rm cyc})]\mapsto[p(t)]$')
    t = t.replace('coefficient. The displayed matrix,',
                  r'coefficient $t_{\rm cyc}^j$. The displayed matrix,')
    return t


edit('02LH', 'maps:src:D.2.40', 'following weighted cusp comparison',
     r'Identify this coefficient ring with $\mathcal A_d$ in',
     'The unit and $t-1$ reductions,', second_import,
     'Propagate the renamed t_cyc generator into the second explicit import of Theorem 13.2. The coefficient substitution and its inverse preserve the ordered cell basis and every integer coefficient. They identify the displayed normalization matrix and its degree-zero and degree-four rows with the same target maps, retaining the partial-sum inverse and extension section.')


def suspension(t):
    t = math_letters(t, {'a': r'a_{\rm sus}'})
    t = t.replace(r'\Phi_a_{\rm sus}', r'\Phi_{a_{\rm sus}}')
    t = t.replace(' \\Phi_{a_{\\rm sus}}(z,\\eta)=\n',
                  ' \\begin{aligned}\n \\Phi_{a_{\\rm sus}}(z,\\eta)\n &=\n')
    t = t.replace(r'\bigl(z-\vartheta_{\rm sus}(a_{\rm sus})q_Q,e^{',
                  '\\bigl(z-\\vartheta_{\\rm sus}(a_{\\rm sus})q_Q,\\\\\n &\\quad e^{')
    t = t.replace('\\eta\\bigr)\n\\]', '\\eta\\bigr)\n \\end{aligned}\n\\]', 1)
    return t


edit('02S8', 'night:P3F.31', '570–575',
     r'Choose \(\vartheta_{\rm sus}(a+1)',
     'with inverse using', suspension,
     'Qualify the real suspension coordinate as a_sus, preserving the imported graph cochain a. The new coordinate has the same numerical value; the inverse reads it by the identical logarithmic formula. Phi, its inverse, the period equation, shell reparametrization and reciprocal lift retain every argument and value under this identity coordinate substitution.')

def sheet_index(t):
    t = math_letters(t, {'a': r'\varepsilon_{\rm sh}'})
    t = t.replace(' \\beta_j=', ' \\begin{gathered}\n \\beta_j=', 1)
    t = t.replace('\\qquad\n', '\\\\\n')
    t = t.replace('0,1 .\n\\]', '0,1 .\n \\end{gathered}\n\\]', 1)
    return t


edit('02S8', 'night:P3F.31', '575',
     'heights, modulo one, are',
     'Exactly one sheet has parameter angle zero',
     sheet_index,
     'Name the binary sheet index epsilon_sh, preserving graph cochain a and suspension coordinate a_sus. The bijection sends each of the same two values 0 and 1 to itself. The height formula and congruence test use the identical two integers, with inverse relabelling, and therefore preserve the selected sheet and all subsequent disc maps.')

assert r'\Phi_a_{\rm sus}' not in work
back = work
for row in reversed(rows):
    assert back.count(row['new_text']) == 1
    back = back.replace(row['new_text'], row['old_text'], 1)
assert back == source
for pat in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}', r'\d+']:
    assert re.findall(pat, source) == re.findall(pat, work), pat
stem = 'S6_SERIES_PUBLISH_c9_current02_known_roles'
(OUT/(stem+'.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
(OUT/(stem+'.diff')).write_text(''.join(difflib.unified_diff(
    source.splitlines(True), work.splitlines(True),
    fromfile='canonical before bounded known-role edits',
    tofile='proposed bounded known-role edits', n=4)))
print(len(rows), 'guarded known-role fragments; complete reverse substitution passed.')
print('Labels, targets and numeric literals unchanged. Canonical manuscript unchanged.')

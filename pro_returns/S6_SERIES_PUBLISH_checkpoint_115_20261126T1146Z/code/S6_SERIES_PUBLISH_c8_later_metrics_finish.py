#!/usr/bin/env python3
"""Bounded corrections found in the full 1,732-line metric readback."""
from pathlib import Path
import csv
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/fixed_target_metrics.tex'
LOG = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_metrics_publication_defects.tsv'
old = PATH.read_text()
assert len(old.splitlines()) == 1732
new = old
with LOG.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)

def edit(before, after, kind, sid, reason):
    global new
    assert new.count(before) == 1, (sid, before[:80], new.count(before))
    pos = new.index(before)
    rows.append(dict(type=kind, statement_id=sid,
        old_location='fixed_target_metrics.tex final correction line ' + str(new[:pos].count('\n') + 1),
        old_page='pending final concordance', new_location='same mathematical owner', new_page='pending final build',
        old_text=before, new_text=after, reason=reason,
        review_status='whole first rewrite read; bounded final correction readback pending'))
    new = new[:pos] + after + new[pos + len(before):]

edit(r'\(\rho_0\) to \(\partial M\), with inverse \(\rho_0^{-1}\).',
     r'\(\rho_0\) to \(\partial\mathcal M\), with inverse \(\rho_0^{-1}\).',
     'D11', 'wb:sphere-metric-scaling-trichotomy', 'Keep the finite-filled core notation consistent in the general chart proof.')
edit('Since $Y_T=TJ+E_T$ with bounded $E_T$ and',
     'Since $Y_T=TJ+E(r_T)$ with bounded $E(r_T)$ and',
     'D11', 'wb:sphere-metric-unit-volume', 'Use the residual notation defined before this corollary.')
edit('The marked-period estimate \\(\\ell_T\\geq T-C\\) makes both\ndistances divergent.  The exact charts in that theorem place',
     'The marked-period estimate \\(\\ell_T\\geq T-C_E\\) makes both\ndistances divergent.  The exact charts in that corollary place',
     'D11/D14', 'wb:sphere-metric-tangent-scope', 'Use the fixed residual bound and the new native-corollary result kind.')

a = new.index('Replacing a real representative \\(y_i\\) by \\(y_i+Y_Tn\\), or')
b = new.index('On \\(j_T\\), \\(dr=du=0\\)', a)
edit(new[a:b], r'''Their inverses take the unique nonbasepoint product representative
and apply $\iota_T$ or $\vartheta_T$ to its marked angular classes.
The representative independence, endpoint scope and regular
embedding assertions are proved for these exact maps and inverses
in \cref{mapsIII:lem:radial-slice-embeddings}.
''', 'D12/D20', 'mapsIII:lem:fixed-conical-metrics',
     'Use Q30T as the sole embedding proof owner while retaining the maps, inverse and complete new first-form multiplication.')

a = new.index('For the metric convergence, set $\\eta_T=\\lVert B_T-R\\rVert$.')
b = new.index('For $C_T^4$, the period matrix', a)
edit(new[a:b], r'''The relation to \cref{wb:sphere-metric-scaling-trichotomy} is
the exact choice
\[
 \lambda_T=\frac{T}{r_T\sqrt{D_T}},\quad
 \beta_T=\frac{T}{\sqrt{D_T}}\longrightarrow1
 \quad\text{on }Z_{12},\qquad
 \lambda_T=\frac1{r_T},\quad\beta_T=1
 \quad\text{on }Z_{24}^{\mathcal D}.
\]
Indeed the slice factors $r_T/T$ and $r_T/\ell_T$ turn these
scales into $D_T^{-1/2}$ and $\ell_T^{-1}$ on the physical flat
tori. The inverse relation is $\lambda_T=\beta_T/r_T$.
Thus that theorem's finite-positive case proves the smooth and
Gromov--Hausdorff limit. For the quantitative diameter bounds below,
put $\eta_T=\|B_T-R\|\to0$. The inequalities
$(1-\eta_T)|v|\leq|B_Tv|\leq(1+\eta_T)|v|$, followed by
infima over $v=a-b+n$, give diameter at most $1+\eta_T$.

''', 'D12/D20', 'wb:sphere-metric-unit-volume',
     'Give the exact positive finite-beta specialization and its inverse, preserving all unit-volume maps, asymptotics and quantitative diameter obstruction. The arbitrary-scale theorem owns the convergence proof.')

for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}']:
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
PATH.write_text(new)
with LOG.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Final metric source lines', len(new.splitlines()))
print('Additional exact defect rows', len(rows) - 24, 'total', len(rows))
print('Permanent identifier multiplicities unchanged; no central writes or criterion credit.')

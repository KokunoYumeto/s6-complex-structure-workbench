from pathlib import Path
from datetime import datetime, timezone
import csv, re

ROOT = Path('/workspace/scratch/9fcd229a9ed4/base/S6_SERIES_PUBLISH_checkpoint_35')
OUT = ROOT / 'agents/continuation3_provenance/sec07_tail'
main = (ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
original = (OUT/'S6_SERIES_PUBLISH_reduced_horizontal_original.tex').read_text()
body = original.split(r'\part{Compact occurrence and marked supports}')[0]
assert main.count(body) == 1
(OUT/'S6_SERIES_PUBLISH_reduced_horizontal_body_original.tex').write_text(body)
starts = list(re.finditer(r'\\begin\{(?:proposition|cited)\}\[[^\n]+\]\\hypertarget\{tag-[^}]+\}\{\}\\label\{(cdp:st:C\.2\.[^}]+)\}',body))
for i,m in enumerate(starts):
    stop = starts[i+1].start() if i+1<len(starts) else len(body)
    key = m.group(1).removeprefix('cdp:st:C.2.').replace('.','_')
    (OUT/f'S6_SERIES_PUBLISH_{key}_original.tex').write_text(body[m.start():stop])

start = main.index(r'\begin{proposition}[Rational normalization bounds with the exact constant-sheaf map]')
end = main.index(r'\end{proof}',start)+len(r'\end{proof}')
old = main[start:end]
new = old.replace(
'''Let $f:Y\\to B$ be a proper holomorphic map from a smooth compact
complex threefold with $b_2(Y)=0$, with connected fibres and smooth
general fibre a two-torus.''',
'''Let $f:Y\\to B$ be a proper holomorphic map from a smooth
complex threefold, with connected fibres and smooth
general fibre a two-torus.''')
needle = 'Suppose that $Z$ is rational.\n'
assert needle in new
new = new.replace(needle,
'''Suppose that $Z$ is rational,
$\\omega_S$ is torsion and $\\chi(S,\\OO_S)=0$.
These two identities hold in particular in the compact
case $b_2(Y)=0$.
''',1)
old_step = r'''\item The canonical evaluation argument in \ref{cdp:st:A.5.12} gives
$\omega_S^m\simeq\OO_S$ and $\chi(S,\OO_S)=0$.
Thus $e=0$ or $1$, with $e=1$ precisely when
$\omega_S\simeq\OO_S$, and
$h^1(S,\OO_S)=1+e$.'''
new_step = r'''\item Let $r_0>0$ trivialize $\omega_S^{\otimes r_0}$.
A nonzero section of $\omega_S$ has nonzero constant $r_0$th
power on the compact connected surface $S$, so it trivializes
$\omega_S$. Consequently $e=0$ or $1$, with $e=1$ precisely
when $\omega_S\simeq\OO_S$. The hypothesis $\chi(\OO_S)=0$
and Serre duality give $h^1(S,\OO_S)=1+e$.

For the asserted compact specialization, apply the canonical
evaluation maps in \eqref{cdp:eq:A.CD.1} to the same restriction
$f^{-1}(\Delta)\to\Delta$ and its same full divisor $mS$.
They use the canonical generator and the principal equation
$(t)=mS$, giving $\omega_S^{\otimes m}\simeq\OO_S$.
The Cartier sequence
$0\to\OO_Y(-S)\to\OO_Y\to\OO_S\to0$ has equal first two
Euler characteristics: $b_2(Y)=0$ makes
$c_1(\OO_Y(S))=0$ in rational cohomology, so their Chern
characters agree in Hirzebruch--Riemann--Roch.
Thus $\chi(\OO_S)=0$. These are exactly the two input
calculations in the proof of \cref{cdp:st:A.5.12}; the
Picard-map hypothesis of its later conclusion is not used
in either calculation.'''
assert old_step in new
new = new.replace(old_step,new_step)
new = new.replace('Its $m$th tensor power would be', 'Its $r_0$th tensor power would be')
assert old != new
(OUT/'S6_SERIES_PUBLISH_A5_16_original.tex').write_text(old)
(OUT/'S6_SERIES_PUBLISH_A5_16_proposed.tex').write_text(new)
with (OUT/'S6_SERIES_PUBLISH_A5_16_scope_guard.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['change_id','old_text','new_text'],delimiter='\t',lineterminator='\n')
    w.writeheader()
    w.writerow(dict(change_id='II-C3-SEC07-A516-SCOPE',old_text=old,new_text=new))
print('Prepared', len(starts), 'original owner snapshots; A.5.16 scope proposal only; no shared writes.')

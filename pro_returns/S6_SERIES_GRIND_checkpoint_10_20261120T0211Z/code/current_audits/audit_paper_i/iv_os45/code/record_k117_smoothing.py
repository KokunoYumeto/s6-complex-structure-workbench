"""Record the exact smooth reparametrization of the three K117 clutch discs."""
from pathlib import Path
import json, hashlib

root = Path(__file__).resolve().parents[1]
source = root.parents[2] / 'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex'
# Source lives next to the work directory, not within it.
source = Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex')
body = source.read_text()
specs = [
('author', r'''Its SU(2) clutch bounds the explicit disc with first column
\((re^{i\phi},\sqrt{1-r^2})\). Thus the actual boundary Hopf
map''', r'''Its SU(2) clutch bounds the smooth disc with first column
\[
 (a,b)=\bigl(\sin(\pi r/2)e^{i\phi},\cos(\pi r/2)\bigr),
 \qquad 0\leq r\leq1,
\]
and matrix $\left(\begin{smallmatrix}a&-\bar b\\b&\bar a\end{smallmatrix}\right)$.
This is the original disc after the exact radial substitution
$\rho=\sin(\pi r/2)$, with inverse $r=2\arcsin(\rho)/\pi$.
At its centre $\sin(\pi r/2)/r$ and $\cos(\pi r/2)$ are smooth
functions of $r^2$; on its boundary the matrix is
$\operatorname{diag}(e^{i\phi},e^{-i\phi})$.
Thus the actual boundary Hopf map'''),
('root', r'''gives the determinant-one spinor
\(\mathcal O(1)\oplus\mathcal O(-1)\); its SU(2) clutch
contracts through the first columns
\((r e^{i\phi},\sqrt{1-r^2})\).''', r'''gives the determinant-one spinor
\(\mathcal O(1)\oplus\mathcal O(-1)\); its SU(2) clutch
contracts through the smooth first columns
\[
 \bigl(\sin(\pi r/2)e^{i\phi},\cos(\pi r/2)\bigr),
 \qquad 0\leq r\leq1.
\]
The second column is $(-\bar b,\bar a)$ when the first is $(a,b)$.
The exact substitution from the original disc is
$\rho=\sin(\pi r/2)$, with inverse $r=2\arcsin(\rho)/\pi$;
the displayed disc is smooth at the centre and up to its boundary.'''),
('peer', r'''\(\mathcal O(1)\oplus\mathcal O(-1)\). Its determinant-one
clutch bounds the explicit disc whose first column is
\((re^{i\phi},\sqrt{1-r^2})\). Thus the actual boundary is''', r'''\(\mathcal O(1)\oplus\mathcal O(-1)\). Its determinant-one
clutch bounds the smooth disc whose first column is
\[
 \bigl(\sin(\pi r/2)e^{i\phi},\cos(\pi r/2)\bigr),
 \qquad 0\leq r\leq1,
\]
and whose second column is $(-\bar b,\bar a)$ when the first is $(a,b)$.
This is the exact reparametrization $\rho=\sin(\pi r/2)$ of the
original disc, with inverse $r=2\arcsin(\rho)/\pi$; it is smooth
at the centre and up to the boundary. Thus the actual boundary is''')
]
patches = []
for suffix, old, new in specs:
    assert body.count(old) == 1, (suffix, body.count(old))
    patches.append(dict(id='IV-K117-smooth-clutch-' + suffix,
                        statement_id='night:P3K.117', operation='replace_exact',
                        old=old, new=new,
                        reason='Make the null-homotopy smooth on the closed disc via an exact radial reparametrization; the boundary clutch and SU(2) matrix are unchanged.'))
target = root / 'K117_smooth_contraction_patches.json'
target.write_text(json.dumps(patches, indent=2) + '\n')
receipt = dict(status='PASS', exact_unique_matches=len(patches),
               parameter_map='rho=sin(pi*r/2), r=2*arcsin(rho)/pi',
               smoothness='sin(pi*r/2)/r and cos(pi*r/2) are smooth functions of r^2 at r=0; all formulas smooth at r=1.',
               boundary='diag(exp(i*phi),exp(-i*phi))',
               file_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
               attribution='GPT-6 Astra, ChatGPT Pro mode, inherited effort; same-family follow-up.')
(root / 'K117_smooth_contraction_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))

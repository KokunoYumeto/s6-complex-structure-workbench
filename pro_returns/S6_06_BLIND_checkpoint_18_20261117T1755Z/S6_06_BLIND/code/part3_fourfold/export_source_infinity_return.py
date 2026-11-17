#!/usr/bin/env python3
"""Export the complete audited infinity comparison as the separate P3K.57 include."""
from pathlib import Path
from datetime import datetime, timezone
import json,re

ROOT=Path(__file__).resolve().parents[2]
sources=['notes/part3_source_infinity_fourfold_working.md',
         'notes/part3_source_infinity_excision_working.md']
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+datetime.now(timezone.utc).isoformat()+
      ' — Opened '+', '.join(sources)+
      ' and own results_mapping.json. Reason: complete P3K.57 manuscript export. '
      'Material: all source/Cartier/cap maps, exact regular fan and local quotient proof, '
      'relative circle-quotient bordism, signed finite-chart residues and actual Hopf-lift transfer.\n')
IF=(ROOT/sources[0]).read_text().split('## IF.1.',1)[1]
IF='## IF.1.'+IF
IE=(ROOT/sources[1]).read_text().split('## IE.1.',1)[1]
IE='## IE.1.'+IE

# Preserve all history in the working sources; the manuscript follows the completed proof.
IF=IF.replace('An earlier proposed \\(\\epsilon^4\\) change counted only the \\(U_a\\) factor.\n'
  'Equation (IF.6) locates its omitted \\(q\\) factor and (IF.7) corrects that\n'
  'attempt. No scalar convention is changed.','')
IF=IF.replace('## IF.7. Remaining attachment and executed scope','## IF.7. The actual origin and the attachment sequence')
IF=IF.replace('This removes that particular local annular-deck mismatch. It does not\n'
  'construct a compact global bordism: the rank-one faces of (IF.16) need\n'
  'their actual quotient atlas, the finite-cap attachment must be written,\n'
  'and the separate selected I1 scalar trace must be joined with its physical\n'
  'Euler line and oriented boundary. Fixed \\(\\lambda\\) is not asserted to\n'
  'give uniform contraction through \\(\\epsilon=0\\).',
  'The following sections construct the rank-one quotient atlas, its actual finite-cap\n'
  'attachment, and the real selected-cusp comparison, retaining the physical Euler line\n'
  'and oriented boundary. The analytic collision filling uses the specified positive\n'
  'scalar rescaling; IE.6 removes that scalar winding by an actual parameter bordism.')
IF=re.sub(r'Audit correction, 2026-11-17 after checkpoint14:[\s\S]*?the smaller fan computations supply arithmetic only\.\n',
  r'The raw multiplier order \\(N-2\\) must be combined with the actual nodal-line metric and source reindexing. The complete operator bounds below retain losses three and four, respectively, and the geometric proof uses the safe orders \\(N=8\\) and \\(N=6\\).\n', IF, count=1)
IF=IF.replace('## IF.9. Exact face kernels and the remaining real attachment','## IF.9. Exact face kernels and the analytic quotient')
IF=IF.replace('To complete the source return one still needs a real bordism\n'
  'joining this collision/cap partial filling to the actual selected\n'
  'I1 scalar trace, with its physical Euler line and normal\n'
  'orientation. No full holomorphic selected corner, compact global\n'
  'fourfold, signature, or return value is asserted in this note.',
  'The real joining of this partial filling to the selected scalar trace is\n'
  'constructed in IE.1--6, with its physical Euler line and normal orientation.')
IF=IF.replace('This is the partial attachment used in the next step. It provides\n'
  'no filling of that last boundary and no return invariant. The exact\n'
  'remaining morphism is its gluing to the selected-cusp scalar trace\n'
  'with the physical Euler line and its normal orientation.',
  'This partial attachment supplies the exact source-base boundary used in\n'
  'IE.1--6. Those sections construct its real comparison with the selected\n'
  'scalar trace, with the physical Euler line and its normal orientation.')
IF=IF.replace('of\nRCZ.5,','of\nP3K.49, RCZ.5,').replace('of RCZ.4','of P3K.49, RCZ.4')

statement=r'''For the marked source
\[
 y^2=x^3+(-2+3\epsilon^2)x^2+t x
       +\epsilon^2(1-\epsilon^2)^2,\qquad
 G=(0,\epsilon(1-\epsilon^2)),
\]
retain the selected whole-zero fibre at
\(t_*=(1-\epsilon^2)(1-3\epsilon^2)\), the actual Cartier line
\(M_a=\mathcal O([aG]-[O])\), and the suspension over \(-bG\),
where \(ab=2\). Use either the initial vertical-edge cusp fan or its
literal reflected fan, and the admitted cap data
\[
 \begin{array}{c|c|c}
 (a,b)&\text{cap order}&\text{root type}\\ \hline
 (1,2)&m=4p&\text{good III-star root}\\
 (2,1)&m=4p-1&\text{reduced III root}
 \end{array}\qquad(p\ge1),
\]
with either norm sign \(n=\pm1\) and every retained integral
\(d\delta\) twist. These are the completed sphere families of
P3F.41 and P3K.24, with their prescribed source, line and cap maps.
For a fixed sufficiently small nonzero suspension scalar, the actual
positive \(\epsilon\)-loop has Jin characteristic integer and oriented
clutched-sphere class
\[
 \begin{array}{c|c|c}
 (a,b)&\displaystyle\int\frac{4x^3-p_1x}{24}
       &\Theta_7\simeq\mathbb Z/28\\ \hline
 (1,2)&0&0\\
 (2,1)&1&1.
 \end{array}
\]
The actual source/Cartier/cap morphism under
\(v=\epsilon^{-2}-1\) preserves the suspension scalar and retains
the full \(D^{-4}\) root endpoint, the reduced doubled lattice period,
the annular reference overlap and the quadratic scalar cochain.
The theorem assigns no source-zero return and makes no further fan comparison.'''

body=IF+'\n\n'+IE
body=body.replace('Atiyah--Bott (1984), printed pages 8--9,\n'
  'Theorem (3.5), equations (3.7)--(3.8).',
  r'Atiyah--Bott \cite[pp.~8--9, Theorem~(3.5), equations~(3.7)--(3.8)]{AtiyahBott1984}.')

def tex(value):
    for prefix in ('IF','IE'):
        value=value.replace('\\tag{'+prefix+'.','\\tag{P3K.57.'+prefix+'.')
        value=value.replace('('+prefix+'.','(P3K.57.'+prefix+'.')
    value=value.replace(')--(P3K.57.',')--\\allowbreak (P3K.57.')
    value=re.sub(r'^### (.+)$',lambda m:r'\par\smallskip\noindent\textit{'+m.group(1)+r'.}\par\nopagebreak[4]',value,flags=re.M)
    value=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\par\nopagebreak[4]',value,flags=re.M)
    value=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',value)
    value=re.sub(r'\*\*([^*]+)\*\*',lambda m:r'\textbf{'+m.group(1)+'}',value)
    return value.strip()+'\n'

export=(r'\begin{statement}{P3K.57}{Proved}'+'\n'+tex(statement)+
        r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex(body)+r'\end{proof}'+'\n')
assert re.search(r'(?<!\\)#',export) is None
assert '`' not in export
assert '\\tag{SZ.' not in export and '(SZ.' not in export
assert 'K39' not in export
(ROOT/'notes/part3_source_infinity_return.tex').write_text(export)
(ROOT/'notes/part3_source_infinity_return.md').write_text(
    '# P3K.57. Proved: the actual marked infinity return\n\n'+statement+
    '\n\n**Proof.**\n\n'+body+'\n\n**End of proof.**\n')
mapping_path=ROOT/'code/part3_fourfold/results_mapping.json'
mapping=json.loads(mapping_path.read_text())
mapping['results']=[r for r in mapping['results'] if r.get('id')!='P3K.57']
mapping['results'].append(dict(id='P3K.57',status='Proved',item_of_prompt='3.4',
 statement='Actual fixed-scalar positive epsilon infinity return is 0 for the good III-star branch and 1 for the reduced III branch, in each initial/reflected vertical-edge fan.',
 proof_file='notes/part3_source_infinity_return.md',latex_file='notes/part3_source_infinity_return.tex',
 working_proofs=sources,parameter='positive epsilon loop, fixed sufficiently small scalar; v=epsilon^-2-1',
 branches=[{'a':1,'b':2,'m':'4p','Jin_integer':0,'Theta7':0},
           {'a':2,'b':1,'m':'4p-1','Jin_integer':1,'Theta7':1}],
 signs=[-1,1],delta_twist='arbitrary retained integer d',
 fan_scope='initial vertical-edge fan and its literal reflected fan',
 executed_geometric_orders=[[1,2,8],[2,1,6]],
 exact_certificates=['code/part3_fourfold/source_infinity_exact.json',
   'code/part3_fourfold/source_infinity_excision_certificate.json',
   'code/part3_fourfold/source_infinity_regular_fan_1_2_8.json',
   'code/part3_fourfold/source_infinity_regular_fan_2_1_6.json'],
 audit='Root complete maps/normal classes/Stokes/orientation/transfer/local fan/localization PASS, including the corrected nodal metric bound and safe geometric orders in IF.28b.',
 remaining_scope='No source-zero value or further fan comparison is assigned.'))
mapping_path.write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported complete P3K.57 with IF.1--12, IF.5a/8a, IE.1--7 and actual return transfer.')

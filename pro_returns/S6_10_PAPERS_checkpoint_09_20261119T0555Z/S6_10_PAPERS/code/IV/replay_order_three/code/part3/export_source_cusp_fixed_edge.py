#!/usr/bin/env python3
from pathlib import Path
import datetime,json,re,subprocess

root=Path(__file__).resolve().parents[2]
source=(root/'notes/part3_source_cusp_fixed_edge_working.md').read_text()
body='## SF.1.'+source.split('## SF.1.',1)[1]
proof_body,audit_body=body.split('## Audit and computation status',1)
statement=r'''
Retain the actual positive selected-cusp source loop of P3F.54 and
P3F.56, with fixed sufficiently small scalar, the III-star cap, no
logarithmic modification at either member of the coalescing finite
pair, and the initial physical-delta-edge fan. Its parameter is one
positive \(\rho\)-loop with \(a(u)=\rho^2\), the actual twofold
marked closure of the selected source puncture. Flop that fixed edge
in the periodic cusp completion, carrying its actual source, line,
cap and ordinary-annulus maps. The positive return of the resulting
family has oriented homotopy-sphere class
\[
                 [\Sigma_{\Phi,\mathrm{flop}}]
                     =-5=23\quad\hbox{in }\mathbb Z/28.
\]
In the actual first-resolution relative product, its initial right
exponent is \(n=-6\). The other free exponent \(m\) is retained
without assigning its value. This statement assigns neither the
separate Jin characteristic pair nor a return for another edge or
an arbitrary fan.
'''

def convert(text):
    text=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',text)
    text=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),text)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=text,text=True,capture_output=True,check=True).stdout

tex=(r'\subsection{The selected-cusp source loop after its first fixed-edge flop}'+'\n'
     +r'\begin{statement}{P3K.40}{Proved}'+'\n'+convert(statement)
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(proof_body)
     +r'\end{proof}'+'\n'+convert('## Audit and computation status'+audit_body))
(root/'notes/part3_source_cusp_fixed_edge.tex').write_text(tex)
preamble=(root/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k40_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_fixed_edge.tex}'+'\n'+r'\end{document}'+'\n')
record={'statement':'P3K.40','status':'Proved','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'proof':'notes/part3_source_cusp_fixed_edge.tex',
 'scope':'The actual selected-cusp positive rho loop of F54/F56, fixed scalar and III-star cap, first physical fixed-edge flop only.',
 'audits':['Root full SF1–3 and K23 comparison PASS','Independent blind_control SF1–2 chart/frame audit PASS'],
 'own_values':{'initial_A':1,'initial_n_rel':-6,'flopped_oriented_class':23,'integer_representative':-5},
 'actual_maps':['Z=(s-rho)/(s+rho)','c_i_prime=Z*c_i','full four-weight Cox action with unrestricted total S','tau(h,q)=(q^-1*h*q,q)','n_rel=-6*A','central conjugation s_new=s+n'],
 'uncomputed':['m','separate Jin k and ell','full common-exterior source derivative','later-edge and arbitrary-fan returns'],
 'certificate':'code/part3/source_cusp_fixed_edge.py',
 'superseded_attempt':'code/part3/attempts/source_cusp_fixed_edge_sum_zero_restriction/'}
(root/'code/part3/source_cusp_fixed_edge_results_mapping.json').write_text(json.dumps(record,indent=2)+'\n')
print('Exported full P3K.40 and standalone wrapper; master remains untouched.')

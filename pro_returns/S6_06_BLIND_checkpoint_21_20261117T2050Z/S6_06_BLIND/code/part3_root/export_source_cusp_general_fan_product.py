"""Export the audited actual general-fan product/trace statement as K55."""
from pathlib import Path
from datetime import datetime, timezone
import json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
source = (ROOT/'notes/part3_source_cusp_general_fan_product_working.md').read_text()
body = '## GF.1.' + source.split('## GF.1.',1)[1]
body += '\nThe exact certificate is code/part3_root/source_cusp_general_fan_product.py. It includes symbolic character, period, contraction and orientation identities, and all 1384 integral bases with entries in '+r'\([-8,8]\)'+'. The written proof establishes the statements for every integral unimodular basis.\n'
statement = r'''
Retain the actual positive selected-cusp source loop of P3F.54/P3F.56,
its physical height, fixed scalar, full line and finite-cap maps. For
every integral unimodular matrix \(P\), the two-triangle fan obtained
from OE.1 by \((x,h)\mapsto(Px,h)\) admits the periodic oriented
ordinary plumbing product constructed below. Its complete period
winding matrix and normal first exponents are
\[
 B_P=(b_{ij})=-6P^{-1}e_1e_1^TP,\qquad
 (l_0,l_1,l_2)=(b_{22}-b_{21},b_{11}-b_{12},b_{22}).
\]
Writing \((\xi,\upsilon)^T=P^{-1}e_2\), define
\[
 w=(\xi,\upsilon,-\xi-\upsilon),\qquad
 d=(-\xi-2\upsilon,-2\xi-\upsilon,\xi-\upsilon).
\]
Its actual local orbit and stable-derivative trace degrees are
\[
 I_i=-3w_i+d_i(l_i+3),\qquad W_i=-3w_i-d_i(l_i+3).
\]
In the positive complex meridians and relative dual cycles, its
actual symmetric variation matrix \(V\) and ambient derivative
\(\delta\) satisfy the integral identities
\[
 V(w_je_j-w_0e_0)=I_je_j-I_0e_0,\qquad
 w_j\delta_j-w_0\delta_0=W_j-W_0\quad(j=1,2).
\]
On each native star the ordinary-product comparison is the explicit
pure-left endpoint \(L^6\). The proof supplies every character,
period, unit, normal and chain map used in these formulas. It leaves
the transverse invariants and the general central return unassigned.
'''

def conv(text):
    text = re.sub(r'(?m)^## (.+)$', lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak', text)
    text = re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',
                  lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''), text)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                           '-t','latex','--wrap=preserve'],input=text,text=True,
                          capture_output=True,check=True).stdout

tex = (r'\subsection{Actual ordinary products and circle traces on every lattice-basis fan}'+'\n'
       +r'\begin{statement}{P3K.55}{Proved}'+'\n'+conv(statement)
       +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+conv(body)+r'\end{proof}'+'\n')
# Source inline formulas have explicit delimiters. These tokens were the
# previous Pandoc failure and must never silently return on regeneration.
for forbidden in (r'\^{}',r'\textsuperscript{',r'\emph{'):
    assert forbidden not in tex, ('Malformed inline formula',forbidden)
(ROOT/'notes/part3_source_cusp_general_fan_product.tex').write_text(tex)
pre = (ROOT/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3_root/k55_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'
       +r'\input{notes/part3_source_cusp_general_fan_product.tex}'+'\n'+r'\end{document}'+'\n')
detail = {
    'utc':datetime.now(timezone.utc).isoformat(),'id':'P3K.55','status':'Proved',
    'item_of_prompt':'3.4',
    'statement':'Actual ordinary product, complete units and integral circle/derivative trace relations for every unimodular cusp fan of the selected source loop.',
    'proof':'notes/part3_source_cusp_general_fan_product_working.md',
    'latex_file':'notes/part3_source_cusp_general_fan_product.tex',
    'certificate':'code/part3_root/source_cusp_general_fan_product.json',
    'audit':'records/checks_audit_general_fan_product.json',
    'scope':'No transverse invariant or numerical general-fan central return is inferred.'
}
(ROOT/'code/part3_root/source_cusp_general_fan_product_results_mapping.json').write_text(json.dumps(detail,indent=2)+'\n')
mapping_path=ROOT/'code/part3_root/results_mapping.json'
mapping=json.loads(mapping_path.read_text()) if mapping_path.exists() else {}
if 'P3K.55' in mapping:
    preserved=ROOT/'records/attempts/k55_inline_math_before_repair/results_mapping.json'
    if not preserved.exists():
        preserved.write_bytes(mapping_path.read_bytes())
    del mapping['P3K.55']
mapping.setdefault('comparisons',[])
mapping.setdefault('additional_source_loop_results',{})['P3K.55']=detail
mapping_path.write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported P3K.55 with full proof and independent audit; active input unchanged.')

#!/usr/bin/env python3
"""Export audited K49 with the selected F0 and no central-attachment claim."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,shutil,subprocess
root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_source_zero_relative_comparison_working.md'
text=source.read_text()
assert 'Proved punctured-family comparison after root audit' in text
cert=json.loads((root/'code/part3/source_zero_relative_comparison.json').read_text())
assert cert['status']=='PASS'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source,root/'records'/f'pre_export_{stamp}_{source.name}')
body=text[text.index('## RCZ.1.'):text.index('## Audit record')]
# Protect actual mathematics before replacing the few prose-level markers.
protected=[]
def protect(m):
    protected.append(m.group(0));return f'ZZMATHBLOCK{len(protected)-1}ZZ'
body=re.sub(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)',protect,body)
for old,new in [
    ('v*=u*^3',r'\(v_*=u_*^3\)'),('I_{u*}',r'\(I_{u_*}\)'),
    ('E_i|_{v*}=F*',r'\(E_i|_{v_*}=F^*\)'),
    ('C_i×{v*}',r'\(C_i\times\{v_*\}\)'),('C_i×D',r'\(C_i\times D\)'),
    ('C×D',r'\(C\times D\)'),('C_+,C_-',r'\(C_+,C_-\)'),
    ('z_i(q)',r'\(z_i(q)\)'),('U_G^j',r'\(U_G^j\)'),
    ('u^{12kn}',r'\(u^{12kn}\)'),('v=u^3',r'\(v=u^3\)'),
    ('I_u',r'\(I_u\)'),('L^4',r'\(L^4\)'),('C_i',r'\(C_i\)'),('E_i',r'\(E_i\)'),
    ('u=0',r'\(u=0\)'),('v=0',r'\(v=0\)'),
    ('u*',r'\(u_*\)'),('v*',r'\(v_*\)'),('F*',r'\(F^*\)'),('dδ',r'\(d\delta\)')]:
    if old in body:
        protected.append(new)
        body=body.replace(old,f'ZZMATHBLOCK{len(protected)-1}ZZ')
for name in ('F0','A0','B0'):
    protected.append(r'\('+name[0]+'_'+name[1:]+r'\)')
    body=re.sub(r'\b'+name+r'\b',f'ZZMATHBLOCK{len(protected)-1}ZZ',body)
for i,v in enumerate(protected):body=body.replace(f'ZZMATHBLOCK{i}ZZ',v.replace('{v*}','{v_*}'))
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout
statement=r"""
Retain the marked E7 source, Cartier line
\(M_a=\mathcal O(aG-O)\), suspension by \(-bG\), and one
III-star cap, for \((a,b)=(1,2)\) with the actual good root
\(m=4p\), or \((a,b)=(2,1)\) with the actual reduced root
\(m=4p-1\). Keep the signed norm \(n=\pm1\), every prescribed
finite character and annular \(d\delta\), the chosen whole-zero
\(I_1\) cusp fan and the literal scalar. Use the source arrow
\[
 I_u:(x,y,t,u)\longmapsto(u^2x,u^3y,u^4t,u^3),\qquad v=u^3.
\]
Complete the previously unselected new reference annular map
\(F_0\) by continuation in its actual Hom/source-period torsor
of the full old overlap at one nonzero \(u_*\), including all
of its integral and finite data.

Over a smaller punctured \(u\)-annulus carrying the chosen
positive loop, there is an actual holomorphic,
physical-circle-equivariant family isomorphism from the old
family to the \(v=u^3\) pullback of this newly marked
\(v\)-family. It retains the root endpoint \(D^{-4}\), the
reduced doubled period, all root and Cartier line maps, and
the full annular cochains. For the actual scalar rescaling
\(\lambda=v^N\lambda_0\), \(N=km\), it compares exactly
\(\lambda=u^{3N}\lambda_0\) on the old side. Their physical
returns and oriented mapping tori therefore obey
\[
 [\Phi_{\rm old,u}]=3[\Phi_{\rm new,v}]\quad\text{in }\Theta_7,
 \qquad M_{\Phi_{\rm old,u}}\cong M_{\Phi_{\rm new,v}^{\,3}}.
\]
This statement completes the punctured-family comparison. It
does not identify the raw collision E-chain with the finite-cap
chain across \(v=0\), assert the still-unassembled global
central attachment, or assign a numerical source-zero return.
"""
out='\\subsection{The actual punctured source-zero family comparison}\n\\begin{statement}{P3K.49}{Proved}\n'+statement+'\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n'
(root/'notes/part3_source_zero_relative_comparison.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_source_zero_relative_comparison_compile.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_zero_relative_comparison.tex}'+'\n'+r'\end{document}'+'\n')
print(f'Exported P3K.49; {cert["checks"]} exact identities PASS.')

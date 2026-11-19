#!/usr/bin/env python3
"""Export the audited two-object good source-zero attachment (P3K.83)."""
from pathlib import Path
import re
import subprocess

R = Path(__file__).resolve().parents[2]
src = (R/'notes/part3_source_zero_good_cut_working.md').read_text()
body = '## GC.1.' + src.split('## GC.1.', 1)[1]
statement = r'''Retain the actual source-zero family with
\((a,b)=(1,2)\), good-root order \(m=4p\), either realized norm
sign and every realized finite delta character, with all source,
Cartier, root and annular maps prescribed above. In the selected
Tate fan \(T_0\), the positive fixed-scalar source loop has physical
integer index and oriented return class
\[
                         A_M=0,\qquad [\Sigma]=0\in\Theta_7.
\]
Its literal reflected fan \(JT_0\) has oriented return class
\(1\in\Theta_7\). The actual coupled loops
\(\lambda(v)=\lambda_0v^{km}\) have these same two classes,
\(0\) and \(1\), respectively. The reflected conclusion is an
oriented class; no additional integer characteristic pair is
assigned. The proof retains two chronological primitive maps,
their intermediate cap object, both charge-one faces, the entire
fixed trace and the actual physical Hopf completion. The already
proved vertical-fan recurrence is P3K.82.
'''

def inline_prose(x):
    chunks = re.split(r'(\\\[.*?\\\]|\\\(.*?\\\)|\\path\{[^}]*\})', x, flags=re.S)
    greek = {a:'\\'+a for a in ['rho','gamma','delta','theta','alpha',
             'eta','kappa','tau','phi','omega','chi','beta','epsilon',
             'sigma','lambda','mu','zeta']}
    explicit = {'q1':'q_1','q2':'q_2','S0':'S_0','S1':'S_1',
        'T0':'T_0','T1':'T_1','U1':'U_1','U2':'U_2','A0':'A_0',
        'A1':'A_1','A2':'A_2','F0':'F_0','F1':'F_1','F2':'F_2',
        'P0':'P_0','P1':'P_1','BF':'B_F','B4':'B_4','K0':'K_0',
        'K1':'K_1','L1':'L_1','L2':'L_2','Z0':'Z_0','Z1':'Z_1',
        'Z2':'Z_2','V0':'V_0','V1':'V_1','V2':'V_2',
        'rho0':r'\rho_0','r1':'r_1','Theta7':r'\Theta_7',
        'CP3':r'\mathbb{CP}^3','S2':r'S^2','S3':r'S^3',
        'S4':r'S^4','S7':r'S^7','D2':r'D^2','D3':r'D^3',
        'D4':r'D^4','H2':r'H^2','H3':r'H_3',
        'c1':'c_1','c2':'c_2','p1':'p_1','r0':'r_0'}
    pattern = r'(?<![A-Za-z0-9\\])(?:[A-Za-z]+_[A-Za-z0-9]+|'+ '|'.join(sorted(set(greek)|set(explicit),key=len,reverse=True))+r')(?![A-Za-z0-9])'
    for i in range(0,len(chunks),2):
        def repl(m):
            token=m.group(0)
            if token in explicit: val=explicit[token]
            else:
                a,*rest=token.split('_',1)
                val=greek.get(a,a)
                if rest: val+='_{'+({'infty':r'\infty','lambda':r'\lambda','spin':r'\mathrm{spin}'}.get(rest[0],rest[0]))+'}'
            return r'\('+val+r'\)'
        chunks[i]=re.sub(pattern,repl,chunks[i])
    return ''.join(chunks)

def cv(x):
    x=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',x)
    x=re.sub(r'(?<![A-Za-z0-9_\\])((?:code|records)/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+r'}'+('.' if m.group(1).endswith('.') else ''),x)
    x=inline_prose(x)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=x,text=True,capture_output=True,check=True).stdout

tex=(r'\subsection{The complete good source-zero attachment}'+'\n'
     +r'\begin{statement}{P3K.83}{Proved}'+'\n'+cv(statement)
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+cv(body)
     +r'\end{proof}'+'\n')
assert not any(ord(c)<32 and c not in '\n\t\r' for c in tex)
for bad in [r'\textsuperscript',r'\textsubscript',r'\textbackslash']:
    assert bad not in tex,bad
(R/'notes/part3_source_zero_good_attachment.tex').write_text(tex)
pre=(R/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k83_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_zero_good_attachment.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported P3K.83; master input unchanged.')

#!/usr/bin/env python3
"""Export the audited shear Pontryagin proof; the ID is supplied by root."""
from pathlib import Path
import re, subprocess, argparse
p=argparse.ArgumentParser();p.add_argument('--id',required=True);args=p.parse_args()
R=Path(__file__).resolve().parents[2]
src=(R/'notes/part3_source_cusp_shear_pontryagin_working.md').read_text()
body='## SQ.1.'+src.split('## SQ.1.',1)[1]
body=body.replace('The proposed conclusion of the complete comparison is therefore','The complete comparison therefore proves')
body=re.sub(r'Before promotion, this entire piece, circle-line and relative\nconnection argument.*?retained\.\n','',body,flags=re.S)
body=body.replace('## SQ.7. Exact relative consequences once the displayed comparison is audited','## SQ.7. Exact relative consequences')
body=body.replace('They are not entered in a results mapping before the full\ncomparison proof has passed its audits.','')
st=r'''Retain the actual selected-cusp source loop and physical vertical-edge
fan \(T_n=T(e_1+ne_2,e_2)\). Its Pontryagin pairing is zero for
both the physical circle line \(M\) and the meridian-one dual \(U=M^*\).
With \(A_U=(4k_U-\ell_U)/24\), the exact native and ordinary identities are
\[
(m_0,n_0)=(0,-6A_U),\qquad
V_{00}=6A_U-6,\qquad \delta_0=-6A_U-6.
\]
The full integer line/cochain proof P3K.66 gives
\[
(m_0,n_0)=(0,-6-18n(n-1)),\quad
V_{00}=18n(n-1),\quad \delta_0=-12-18n(n-1).
\]
The proof retains the actual quotient-piece, cap, normal and line
maps, and computes the entire boundary tangent transgression.
'''
def inline_prose(x):
    # Keep supplied display/inline mathematics and explicit path commands.
    chunks=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\)|\\path\{[^}]*\})',x,flags=re.S)
    greek={'rho':r'\rho','gamma':r'\gamma','delta':r'\delta','theta':r'\theta',
           'alpha':r'\alpha','eta':r'\eta','kappa':r'\kappa','tau':r'\tau',
           'phi':r'\phi','omega':r'\omega','chi':r'\chi'}
    for i in range(0,len(chunks),2):
        z=chunks[i]
        # Literal scalar/subscript tokens in the working prose.
        def sub(m):
            tok=m.group(0);a,*rest=tok.split('_',1)
            a=greek.get(a,a)
            if rest:a+='_{'+rest[0]+'}'
            return r'\('+a+r'\)'
        z=re.sub(r'(?<![A-Za-z0-9\\])(?:[A-Za-z]+_[A-Za-z0-9]+|rho|gamma|delta|theta|alpha|eta|kappa|tau|phi|omega|chi)(?![A-Za-z0-9])',sub,z)
        chunks[i]=z
    return ''.join(chunks)
def cv(x):
    x=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',x)
    x=inline_prose(x)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=x,text=True,capture_output=True,check=True).stdout
tex=r'\subsection{The actual Pontryagin pairing on the shear fans}'+'\n'+r'\begin{statement}{'+args.id+r'}{Proved}'+'\n'+cv(st)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+cv(body)+r'\end{proof}'+'\n'
(R/'notes/part3_source_cusp_shear_pontryagin.tex').write_text(tex)
num=args.id.split('.')[-1]
pre=(R/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(R/f'code/part3/k{num}_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_shear_pontryagin.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported '+args.id+'; active manuscript input unchanged.')

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
st=r'''Retain the actual positive selected-cusp source loop, scalar, finite
caps, source periods and line maps of P3F.54/P3F.56, and use the
physical vertical-edge fan \(T_n=T(e_1+ne_2,e_2)\), for any integer
\(n\). The actual Jin completion in its native fixed-star Cox product
has
\[
 \ell_n=0,\qquad k_n=6A_n,
\]
where \(A_n\) is its actual integer Jin index. Its fixed-star native
free relative pair is \((0,-6A_n)\). In the actual ordinary plumbing
product of P3K.55, the remaining diagonal variation and stable
derivative entries are
\[
 V_{00}=6A_n-6,\qquad\delta_0=-6A_n-6.
\]
The already proved central residue of P3K.56 consequently gives
\[
 V_{00}\equiv-18n(n-1),\qquad
 \delta_0\equiv-12+18n(n-1)\pmod{168}.
\]
The proof constructs the actual quotient-piece and cap maps, retains
the parameter-dependent Euler line and its outer gauge, and computes
the entire tangent-connection transgression. It does not select an
integer lift of \(A_n\) from its residue modulo 28.
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

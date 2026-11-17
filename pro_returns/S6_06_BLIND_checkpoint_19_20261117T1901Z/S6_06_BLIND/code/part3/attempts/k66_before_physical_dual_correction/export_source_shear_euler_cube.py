#!/usr/bin/env python3
"""Export the fully audited actual source-shear Euler-cube proof."""
from pathlib import Path
import re, subprocess
R=Path(__file__).resolve().parents[2]
src=(R/'notes/part3_source_shear_euler_cube_working.md').read_text()
body='## EC.1.'+src.split('## EC.1.',1)[1]
statement=r'''Retain the actual selected-cusp positive \(\rho\) loop of
P3F.54/P3F.56, its fixed scalar and finite caps, its physical delta
action, and the physical vertical-edge fans
\(T_n=T(e_1+ne_2,e_2)\), for all integers \(n\).
In the native fixed-star Cox product the exact integer Jin
characteristic pair and index are
\[
 k_n=6-18n(n-1),\qquad \ell_n=0,\qquad
 A_n=1-3n(n-1).
\]
The native fixed-star free pair is
\((0,-6+18n(n-1))\). In the actual ordinary plumbing product of
P3K.55 the remaining diagonal entries are
\[
 V_{00}=-18n(n-1),\qquad
 \delta_0=-12+18n(n-1).
\]
The proof extends the prescribed boundary line isomorphism through
the actual completed quotient piece and cap, then computes its
oriented cubic integral. It does not select an integer from a
residue modulo \(28\).
'''
def inline_prose(x):
    chunks=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\)|\\path\{[^}]*\})',
                    x,flags=re.S)
    greek={'rho':r'\rho','gamma':r'\gamma','delta':r'\delta',
           'theta':r'\theta','alpha':r'\alpha','eta':r'\eta',
           'kappa':r'\kappa','tau':r'\tau','phi':r'\phi',
           'omega':r'\omega','chi':r'\chi','beta':r'\beta'}
    for i in range(0,len(chunks),2):
        def sub(m):
            tok=m.group(0);a,*rest=tok.split('_',1)
            a=greek.get(a,a)
            if rest:a+='_{'+rest[0]+'}'
            return r'\('+a+r'\)'
        chunks[i]=re.sub(
            r'(?<![A-Za-z0-9\\])(?:[A-Za-z]+_[A-Za-z0-9]+|rho|gamma|delta|theta|alpha|eta|kappa|tau|phi|omega|chi|beta)(?![A-Za-z0-9])',
            sub,chunks[i])
    return ''.join(chunks)
def cv(x):
    x=re.sub(r'(?m)^## (.+)$',
             lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)
             +r'}\par\nobreak',x)
    x=inline_prose(x)
    return subprocess.run(
        ['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
         '-t','latex','--wrap=preserve'],
        input=x,text=True,capture_output=True,check=True).stdout
tex=(r'\subsection{The exact Euler cube on the source shear fans}'+'\n'
     +r'\begin{statement}{P3K.66}{Proved}'+'\n'+cv(statement)
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+cv(body)
     +r'\end{proof}'+'\n')
assert not any(ord(c)<32 and c not in '\n\t\r' for c in tex)
for bad in [r'\textsuperscript',r'\textsubscript',r'\textbackslash']:
    assert bad not in tex,bad
(R/'notes/part3_source_shear_euler_cube.tex').write_text(tex)
pre=(R/'code/part3/k38_standalone.tex').read_text().split(
    r'\begin{document}')[0]
(R/'code/part3/k66_standalone.tex').write_text(
    pre+'\n'+r'\begin{document}'+'\n'
    +r'\input{notes/part3_source_shear_euler_cube.tex}'+'\n'
    +r'\end{document}'+'\n')
print('Exported P3K.66; master input unchanged.')

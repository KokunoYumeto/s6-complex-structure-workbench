#!/usr/bin/env python3
"""Retain the actual K68 dual-line arrow in owned scalar reference proofs."""
from pathlib import Path
import json,re
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
def replace(t,old,new):
    if new in t and old not in t:return t
    assert old in t,old
    return t.replace(old,new)

p=ROOT/'notes/part3_additive_returns_working.md'
t=p.read_text()
t=replace(t,'positive Hopf model and the actual Euler line satisfies',
          'positive Hopf model and its positive-meridian line U satisfies')
t=replace(t,'The two outer-bordism/Jin reversals are exactly those in P3K.7.\nConsequently the actual positive-return invariant is',
'''The two outer-bordism/Jin reversals are exactly those in P3K.7.
The exact physical-line comparison of P3K.68 identifies the actual
circle line with U*, and the actual clutch, including its inverse
closing arrow, with lambda_M=-lambda_U. Thus the page computation
on U changes sign when assigned to the physical return. The square
of the page line and all source/cap maps above are unchanged.
Consequently the actual positive-return invariant is''')
t=replace(t,r'\frac{12M_{\rm page}^2-p_1(TS_{\rm page})}{24}',
            r'\frac{p_1(TS_{\rm page})-12M_{\rm page}^2}{24}')
t=replace(t,r'\chi-\frac{ma^2}{2d}=-P_{aG'}\cdot O',
            r'\frac{ma^2}{2d}-\chi=P_{aG'}\cdot O') if False else t
t=replace(t,"\\chi-\\frac{ma^2}{2d}=-P_{aG'}\\cdot O",
            "\\frac{ma^2}{2d}-\\chi=P_{aG'}\\cdot O")
cases=json.loads((ROOT/'code/part3/additive_returns.json').read_text())['cases']
lines=t.splitlines();i=0
for k,line in enumerate(lines):
    if line.startswith('| ') and ('| E7-' in line or '| E6-' in line or '| OS' in line):
        cells=line.split('|')
        cells[-2]=' \\('+S.latex(S.sympify(cases[i]['actual_positive_return']))+'\\) '
        lines[k]='|'.join(cells);i+=1
assert i==16
t='\n'.join(lines)+'\n'
t=t.replace(r'A^{\rm Jin}',r'A^{\rm phys}')
t=t.replace('actual Hopf-gluing transfer P3F.22.','actual physical Hopf-gluing transfer P3K.68, with the explicit inverse-closing convention.')
p.write_text(t)

p=ROOT/'notes/part3_joint_additive_returns_working.md';t=p.read_text()
t=replace(t,'and its actual Euler line satisfies', 'and its positive-meridian line U satisfies')
t=replace(t,'P3K.7. Its actual trace bordism, with the page-line map just\nconstructed, gives',
'''P3K.7. P3K.68 retains the actual positive-meridian-to-physical
line map M=U*, together with the inverse closing arrow in the Hopf
gluing. Its physical clutch is lambda_M=-lambda_U. Consequently
the physical return is the negative of the U-line page index.
The actual trace bordism, with the page-line map just constructed,
therefore gives''')
t=replace(t,r'\frac{12\,c_1(N)^2-p_1(TS_{\rm page})}{24}',
            r'\frac{p_1(TS_{\rm page})-12\,c_1(N)^2}{24}')
t=replace(t,"=\\chi-\\frac{Ma^2}{2d}\n                         =-P_{aG'}\\cdot O",
            "=\\frac{Ma^2}{2d}-\\chi\n                         =P_{aG'}\\cdot O")
rows=json.loads((ROOT/'code/part3/joint_additive_returns.json').read_text())['rows']
lines=t.splitlines();i=0
for k,line in enumerate(lines):
    if line.startswith('| \\(('):
        cells=line.split('|')
        cells[-2]=' \\('+S.latex(S.sympify(rows[i]['actual_A']))+'\\) '
        lines[k]='|'.join(cells);i+=1
assert i==9
t='\n'.join(lines)+'\n'
t=replace(t,r'\(A=(2-8m_0)/3=-16l-2\)',r'\(A=(8m_0-2)/3=16l+2\)')
t=replace(t,r'A^{\rm Jin}=-2',r'A^{\rm Jin}=2')
t=t.replace(r'A^{\rm Jin}',r'A^{\rm phys}')
t=t.replace('By the exact transfer P3F.22,','By the exact physical transfer and inverse-closing map of P3K.68,')
p.write_text(t)

p=ROOT/'code/part3/export_additive_caps.py';t=p.read_text()
t=replace(t,r'A^{\rm Jin}=\frac{m(12-e)+e'}{12}-\frac{ma^2}{2d}',
            r'A^{\rm phys}=\frac{ma^2}{2d}-\frac{m(12-e)+e'}{12}') if False else t
t=replace(t,"A^{\\rm Jin}=\\frac{m(12-e)+e'}{12}-\\frac{ma^2}{2d}",
            "A^{\\rm phys}=\\frac{ma^2}{2d}-\\frac{m(12-e)+e'}{12}")
t=t.replace(r'A^{\rm Jin}',r'A^{\rm phys}')
t=t.replace('The physical Hopf-gluing class is $A^{\\rm phys}\\bmod28$',
            'By the actual dual-line and inverse-closing map P3K.68, the physical Hopf-gluing class is $A^{\\rm phys}\\bmod28$')
if 'import sys\n' not in t:t=t.replace('import re,subprocess,shutil','import re,subprocess,shutil\nimport sys')
t=t.replace('for src,dst,ident,title,statement,blocks in specs:\n',
            'for src,dst,ident,title,statement,blocks in specs:\n if len(sys.argv)>1 and ident not in sys.argv[1:]:continue\n')
p.write_text(t)
p=ROOT/'code/part3/export_joint_additive_returns.py';t=p.read_text()
t=replace(t,"=\\frac{M(12-e_\\infty-e_0)+m_0e_\\infty'+m_\\infty e_0'}{12}\n       -\\frac{Ma^2}{2d},",
            "=\\frac{Ma^2}{2d}\n       -\\frac{M(12-e_\\infty-e_0)+m_0e_\\infty'+m_\\infty e_0'}{12},")
t=replace(t,r'A^{\rm Jin}=-2',r'A^{\rm Jin}=2')
t=t.replace(r'A^{\rm Jin}',r'A^{\rm phys}')
t=t.replace('The physical Hopf-gluing class is',
            'By the actual dual-line and inverse-closing map P3K.68, the physical Hopf-gluing class is')
p.write_text(t)
print('Patched K26/K28 physical reference prose and reproducible exporters; full earlier files preserved.')

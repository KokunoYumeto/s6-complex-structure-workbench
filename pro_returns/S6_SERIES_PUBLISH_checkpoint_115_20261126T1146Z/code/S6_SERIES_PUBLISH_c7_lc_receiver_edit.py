#!/usr/bin/env python3
"""Focused LC receiving-copy notation/TeX edits; no fresh/global writes."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
p=root/'agents/continuation7_iii_odd_cubic/S6_SERIES_PUBLISH_III_02LC_receiving.tex'
s=p.read_text()
s,count=re.subn(r'(?<!\\)\b(qquad|quad)\b',lambda m:'\\'+m.group(),s)
print('remaining missing spacing escapes corrected:',count)
replacements=[
 (r' C=\begin{pmatrix}',r' C_0=\begin{pmatrix}'),
 (r' C^{-1}',r' C_0^{-1}'),
 (r'=C^{-1}',r'=C_0^{-1}'),
 (r'\det C=1',r'\det C_0=1'),
 (r'(SCe_1,Le_1,SCe_2,Le_2)',r'(SC_0e_1,Le_1,SC_0e_2,Le_2)'),
 (r'cusp matrix $C$ of part 4',r'cusp matrix $C_0$ of part 4'),
 (r' K=C^t',r' K=C_0^t'),
 (r'\psi_{\rm ph}(Ct)',r'\psi_{\rm ph}(C_0t)'),
 (r'\psi_{\rm ph}(Ce_1)',r'\psi_{\rm ph}(C_0e_1)'),
 (r'\psi_{\rm ph}(C(-e_1+e_2))',r'\psi_{\rm ph}(C_0(-e_1+e_2))'),
 (r'\psi_{\rm ph}(Ce_2)',r'\psi_{\rm ph}(C_0e_2)'),
 (r'The matrix $C$ and its inverse',r'The matrix $C_0$ and its inverse'),
 (r'two short columns are $SC$ and $C$ is unimodular',r'two short columns are $SC_0$ and $C_0$ is unimodular'),
 (r' d=C_0^{-1}',r' d_\delta=C_0^{-1}'),
 (r'$Kd=(0,-b)^t$',r'$Kd_\delta=(0,-b)^t$'),
 (r'$m_+\cdot d$ and $m_-\cdot d$',r'$m_+\cdot d_\delta$ and $m_-\cdot d_\delta$'),
 (r'$2(K_{11}-K_{12})d_1$',r'$2(K_{11}-K_{12})(d_\delta)_1$'),
 (r' d=\binom{10}{3}',r' d_\delta=\binom{10}{3}'),
 ('The physical support can also be retained explicitly. Write\n',
  'For this rank-one paragraph put $r=\\operatorname{ord}h_G=-\\kappa_i$\n'
  'and $\\rho=\\operatorname{ord}R=-ab\\kappa_i^2/\\nu_i$.\n'
  'The physical support can also be retained explicitly. Write\n'),
]
for old,new in replacements:
    n=s.count(old)
    assert n>=1,(old,n)
    s=s.replace(old,new)
    print(n,old,'->',new)
p.write_text(s,newline='\n')
assert not re.search(r'(?<!\\)\b(qquad|quad)\b',s)
print('Receiver-only notation edits complete.')

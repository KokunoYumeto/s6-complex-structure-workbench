#!/usr/bin/env python3
"""Retained receiving-text corrections and a literal presentation-map check."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import re
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'agents/continuation7_iii_residual_twenty_receiving/S6_SERIES_PUBLISH_III_02LM_receiving.tex'
text=p.read_text()
before=sha256(p.read_bytes()).hexdigest()
changes=[
 (r'\mathbb Z,quad H_2=H_3=\mathbb Z/b,quad',
  r'\mathbb Z,\quad H_2=H_3=\mathbb Z/b,\quad'),
 (r'\overline{x}^{,2}',r'\overline{x}^{\,2}'),
 (r'\binom00',r'\binom{0}{0}'),
 ('The inverse matrices are the integral adjugates of $U,V$.',
  'Their inverses are $\\operatorname{adj}(U)/\\det U$ and\n'
  '$\\operatorname{adj}(V)/\\det V$, including the determinant signs.'),
 ('Both compositions follow by multiplication in the free relation\n'
  'module. The quotient is therefore $\\mathbb Z/b$, sending $s$',
  'These formulas identify the actual relation sublattices.\n'
  'On the four-column source the primitive syzygy is\n'
  '$v_0=(r,n,-m,0)^t$. Let $A$ express the three $E$ columns\n'
  'in the four $C_1,C_2,C_3,G_e$ columns, and let $B$ express\n'
  'those four columns in the $E$ coordinates as displayed.\n'
  'Then $BA=I_3$ and\n'
  '$AB=I_4-\\sigma v_0(0,1,e,0)$.\n'
  'Thus they are inverse maps between $\\mathbb Z^3$ and\n'
  '$\\mathbb Z^4/\\mathbb Zv_0$; $v_0$ is primitive since\n'
  '$\\gcd(m,n)=1$. The quotient in the ambient cycle module is\n'
  'therefore $\\mathbb Z/b$, sending $s$'),
]
for old,new in changes:
    assert text.count(old)==1,old
    text=text.replace(old,new,1)
    print('EXACT_EDIT',repr(old),'->',repr(new))
m,e,r=S.symbols('m e r',integer=True)
for sigma in (-1,1):
    n=m*e+sigma
    A=S.Matrix([[sigma,0,0],[0,0,-sigma*e],[0,0,sigma],[-sigma*m,1,-sigma*r]])
    B=S.Matrix([[sigma,-r,-e*r,0],[m,0,r,1],[0,m,n,0]])
    v=S.Matrix([r,n,-m,0])
    assert S.simplify(B*A-S.eye(3))==S.zeros(3)
    assert S.simplify(A*B-S.eye(4)+sigma*v*S.Matrix([[0,1,e,0]]))==S.zeros(4)
    assert S.expand((S.Matrix([[0,1,e,0]])*v)[0])==sigma
    print('PRESENTATION_MAP sigma',sigma,'BA=I3; AB=I4-sigma*(r,n,-m,0)^t*(0,1,e,0) PASS')
assert not re.search(r'(?<!\\)\b(?:quad|qquad)\b',text)
assert not any(ord(c)<32 and c not in '\n\t' for c in text)
assert '\r' not in text
original=p.read_text()
for kind in ('label','hypertarget','tag'):
    pattern=r'\\'+kind+r'\{([^{}]+)\}'
    assert Counter(re.findall(pattern,original))==Counter(re.findall(pattern,text))
p.write_text(text,newline='\n')
print('BEFORE_SHA256',before)
print('AFTER_SHA256',sha256(p.read_bytes()).hexdigest())
print('LINES',len(text.splitlines()))
print('SCOPE receiving proof only; frozen fresh files unchanged')

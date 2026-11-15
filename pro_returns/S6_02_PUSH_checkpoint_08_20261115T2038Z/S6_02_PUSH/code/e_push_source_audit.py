"""Exact, reproducible scope and algebra checks for the attached historical sources.

This script audits the attachment bytes.  A label's presence or absence is not
a proof of its statement, and deletion in another version has no mathematical
implication.  The prose audit records the separately read arguments.
"""
from pathlib import Path
import hashlib
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / 'background' / 'papers'
names = ['kuranishi-aut', 'exact-period', 'tangent-cohomology',
         'intrinsic-fibration', 'full-automorphisms']
for v in [1, 2]:
    p = PAPERS / f'arXiv_2610.00250v{v}_Du_Guo_Kusakabe_Xie.tex'
    raw = p.read_bytes()
    s = raw.decode()
    print(f'VERSION {v}: {p.name}')
    print('SHA256', hashlib.sha256(raw).hexdigest())
    print('LINES', len(s.splitlines()))
    for name in names:
        needle = r'\label{p2:thm:' + name + '}'
        places = [i for i, line in enumerate(s.splitlines(), 1) if needle in line]
        print(name, places)
    for word in ['Kuranishi', 'Kodaira--Spencer', '2\\Z', 'tangent-cohomology']:
        print('TEXT_COUNT', repr(word), s.count(word))
    for section in re.findall(r'\\section(?:\[[^]]*\])?\{([^\n]*)', s):
        print('SECTION', section[:150])

A1 = sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0 = (A1*A2).inv()
g = sp.eye(4)[:,0]
delta = sp.eye(4)[:,3]
h, k = sp.symbols('h k')
increments = [sp.Rational(-1,3), sp.Rational(1,4), sp.Rational(1,12)]
expected = [sp.Matrix([0,h/2,-h/2,-h/2]),
            sp.Matrix([0,0,-h/2,h/2]), sp.zeros(4,1)]
for name, A, de, want in zip(['g1','g2','g0'], [A1,A2,A0], increments, expected):
    actual = h*(A-sp.eye(4))*g/12 + h*de*delta
    assert actual == want
    print('EXPLICIT_EVEN_SHIFT_DEFECT', name, list(actual))
raw_defect = -h*k/12
strict_defect = sp.expand(raw_defect-h*h/24-k*k/24+(h+k)**2/24)
assert strict_defect == 0
print('RAW_COMPOSITION_DEFECT_E_COEFFICIENT', raw_defect)
print('QUADRATIC_CORRECTION_E_COEFFICIENT', -h*h/24)
print('STRICT_COMPOSITION_DEFECT', strict_defect)

c1 = sp.Matrix([0,1,-2,0])
c0 = -A0*c1
assert c0 == sp.Matrix([0,-1,1,0])
print('AUTOMORPHISM_COCYCLE_g0', list(c0))
print('RESIDUAL_QUOTIENT_CLASS_gamma_u', [c0[0],c0[1]])
M = sp.Matrix([[1,-1,1],[1,-1,1]])
assert M.rank() == 1
alpha, beta = sp.Matrix([0,-1,-1]), sp.Matrix([1,0,-1])
assert M*alpha == sp.zeros(2,1) and M*beta == sp.zeros(2,1)
cup = alpha[0]*beta[2]-alpha[2]*beta[0]
assert cup == 1
print('CUSP_STRUCTURE_COHOMOLOGY', [1,3-M.rank(),2-M.rank()])
print('CUSP_gamma_CUP_partner', cup)
two = PAPERS / 'arXiv_2609.33785_Viaclovsky_two_parameter_src' / 'Viaclovsky_S6_September_26_2026.tex'
ss=two.read_text().split(r'\begin{document}',1)[1]
section=0; theorem=0
tokens=re.compile(r'\\section(?:\[[^]]*\])?\{|\\begin\{(theorem|lemma|proposition|corollary|remark|question|definition|example|exercise|assumption|claim)\}')
for match in tokens.finditer(ss):
    if match.group(0).startswith(r'\section'):
        section+=1;theorem=0
    else:
        theorem+=1
        end=ss.find(r'\end{'+match.group(1)+'}',match.end())
        body=ss[match.end():end]
        labels=re.findall(r'\\label\{([^}]+)\}',body)
        if labels:
            print('TWO_PARAMETER_STATEMENT',f'{section}.{theorem}',match.group(1),labels[0])
print('All exact assertions passed.')

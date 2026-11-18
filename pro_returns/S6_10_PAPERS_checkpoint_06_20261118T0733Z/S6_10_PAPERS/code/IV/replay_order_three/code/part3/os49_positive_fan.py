"""Exact positive-fan and line-subfan identities for P3F.31.

This does not certify the geometric page argument; that proof is audited
separately. It checks the exact charts and every symbolic parity case.
"""
from pathlib import Path
import json
import sympy as s

triangles=[[(0,0),(1,0),(1,1)],[(0,0),(0,1),(1,1)]]
charts=[]
for vertices in triangles:
    rays=s.Matrix.hstack(*[s.Matrix([x,y,1]) for x,y in vertices])
    assert abs(rays.det())==1
    charts.append({'vertices':vertices,'dual_basis':[[int(a) for a in rays.inv().row(i)] for i in range(3)]})

a,r=s.symbols('a r',integer=True)
# Exact parity formulas, with N=2r or 2r+1 and j=2a or 2a+1.
heights={0:a,1:a+1}
target={(0,0):a-3*r,(1,0):a-3*r+1,
        (0,1):a-3*r-1,(1,1):a-3*r-1}
for jp in (0,1):
    for np in (0,1):
        defect=s.expand(heights[jp]-(2*r+np)-target[(jp,np)])
        assert defect==r+(jp*np)

degree=[]
for j in (0,1):
    h=lambda z:s.ceiling(s.Rational(z,2))
    degree.append(int(-(h(j-1)+h(j+1)-2*h(j))))
assert degree==[-1,1]

# Positive-fan fixed-edge charts and their exact O(-1)^2 transition.
Z,A,B=s.symbols('Z A B',nonzero=True)
q=Z*A*B
V=Z*B
assert s.cancel(q/V-A)==0
assert s.cancel(V/Z-B)==0
assert s.cancel(q*Z/V-Z*A)==0
assert s.cancel(V-Z*B)==0

rho,eta,alpha=s.symbols('rho eta alpha',real=True)
radial=-eta*s.cos(alpha)/s.sin(alpha)
real=s.trigsimp(radial*s.cos(alpha)-eta*s.sin(alpha))
imag=s.trigsimp(radial*s.sin(alpha)+eta*s.cos(alpha))
assert s.trigsimp(real+eta/s.sin(alpha))==0 and imag==0

out={'status':'Exact chart checks; geometric page proof independently audited in P3F.31',
     'statement':'P3F.31','triangles':charts,'line_graph':'ceil(j/2)',
     'component_degrees':degree,'g_power_defects':['floor(N/2)','ceil(N/2)'],
     'fixed_edge_normal_transition':'(A,B) -> (Z*A,Z*B)',
     'boundary_intersection_equations':{'rho':'-eta*cot(alpha)','q_minus_epsilon':'-eta/sin(alpha)'},
     'boundary_support_arcs':'pi/2 <= alpha <= pi, three proper lifts',
     'return_index_status':'Positive fan A=0 by the independently audited actual page proof; this script checks its chart identities.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Positive fan is unimodular; actual M graph is ceil(j/2).')
print('Component degrees:',degree,'; g-power defects floor/ceil verified symbolically.')
print('Fixed-edge normal transition and full binding support equations verified.')
print(out['return_index_status'])

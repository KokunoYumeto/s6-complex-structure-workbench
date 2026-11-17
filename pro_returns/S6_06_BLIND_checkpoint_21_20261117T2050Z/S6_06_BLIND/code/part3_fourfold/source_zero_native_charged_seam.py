#!/usr/bin/env python3
"""Exact quaternion comparison of the actual Morse-Cox and charged seams."""
import json
from pathlib import Path
import sympy as s
def qm(a,b):
    A,B,C,D=a;E,F,G,H=b
    return s.Matrix([A*E-B*F-C*G-D*H,A*F+B*E+C*H-D*G,
                     A*G-B*H+C*E+D*F,A*H+B*G-C*F+D*E])
def qc(a):return s.Matrix([a[0],-a[1],-a[2],-a[3]])
def qi(a):return qc(a)/sum(x*x for x in a)
ii=s.Matrix([0,1,0,0]);jj=s.Matrix([0,0,1,0])
def cj(a):return qm(qm(jj,a),-jj)
u=s.Matrix(s.symbols('u0:4',real=True));c=s.Matrix(s.symbols('c0:4',real=True))
p=cj(u);qa=cj(qc(c));qr=qm(jj,qa);Q=qm(u,c)
checks=[]
def ck(name,a,b):
    r=[s.factor(x-y) for x,y in zip(a,b)]
    assert all(x==0 for x in r),(name,r)
    checks.append({'name':name,'pass':True})
ck('alternative_g_numerator',qm(p,qc(qa)),cj(Q))
ck('root_g_numerator',qm(p,qc(qr)),-qm(jj,Q))
knum=qm(qm(qc(c),ii),c);hnum=qm(qm(u,ii),qc(u))
ck('alternative_domain_Hopf',qm(qm(qa,ii),qc(qa)),-cj(knum))
ck('root_domain_Hopf',qm(qm(qr,ii),qc(qr)),-knum)
ck('target_Hopf',qm(qm(p,ii),qc(p)),-cj(hnum))
nc=sum(x*x for x in c)
ck('alternative_full_Hopf_lift',qm(cj(Q),qa),nc*p)
ck('root_full_Hopf_lift',qm(-qm(jj,Q),qr),nc*p)
ck('actual_reconstruction_alt',qm(qm(p,qi(qa)),qa),p)
ck('actual_reconstruction_root',qm(qm(p,qi(qr)),qr),p)

# Exact ideal matrices of the Morse map; the unit sigma+1 is retained.
ss0,ss1,tt0,tt1,sg=s.symbols('s0 s1 t0 t1 sigma',nonzero=True)
aa=(sg+1)/2
bp=-aa-ss0*(tt0+tt1)/(2*(sg+1))
bm=aa-tt1*(ss1-ss0)/(2*(sg+1))
Fp=aa*(ss1-ss0)-ss0**2*(tt0+tt1)/(2*(sg+1))
Fm=aa*(tt0+tt1)-tt1**2*(ss1-ss0)/(2*(sg+1))
assert s.simplify(Fp-(bp*ss0+aa*ss1))==0
assert s.simplify(Fm-(aa*tt0+bm*tt1))==0
assert s.det(s.Matrix([[bp,aa],[1,0]]))==-aa
assert s.det(s.Matrix([[aa,bm],[0,1]]))==aa
checks.append({'name':'both_ruling_ideals_retained','pass':True})
out={'status':'PASS','checks':checks,'count':len(checks),
 'root_chart_dictionary':{'g':'-j*q_H','h_domain':'-k','h_target':'-j*h*j^-1','q_root':'j*q_alt'},
 'scope':'Full actual local Morse-Cox/charged Hopf seam and line; boundary ownership remains in the finite compact strip.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} exact quaternion/ideal identities')

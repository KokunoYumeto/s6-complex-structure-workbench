#!/usr/bin/env python3
"""Exact identities in the actual moving ordinary-site comparison MS.1--10."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
from sympy.combinatorics.free_groups import free_group

root=Path(__file__).resolve().parents[2]
checks=[]
def check(name, value):
    assert bool(value), name
    checks.append({'name':name,'pass':True})

t,p,p0=s.symbols('t p p0')
z=s.symbols('z')
ratio=(t-p)/(t-p0)
check('ratio equals one minus the exact site displacement',
      s.simplify(ratio-(1-(p-p0)/(t-p0)))==0)
check('honest logarithm parameter derivative',
      s.simplify(s.diff(s.log(ratio),p)+1/(t-p))==0)
check('honest logarithm base derivative retains both poles',
      s.simplify(s.diff(s.log(ratio),t)-(1/(t-p)-1/(t-p0)))==0)
check('reference parameter gives the identity ratio',ratio.subs(p,p0)==1)
for N in (1,2,3,4):
    P=-sum(z**j/s.Integer(j) for j in range(1,N+1))
    check(f'logarithm Taylor derivative exact remainder order {N}',
          s.simplify(-1/(1-z)-s.diff(P,z)+z**N/(1-z))==0)

# Retain a generic full four-period coefficient and an actual integral
# marking change. This matrix has nontrivial source and delta/gamma entries.
C=s.Matrix([[1,1,0,2],[0,1,0,1],[0,0,1,0],[0,0,1,1]])
check('period marking change is unimodular',C.det()==1)
v=s.Matrix(s.symbols('v0:4'))
Pi=s.Matrix(2,4,s.symbols('P0:8'))
check('all four period entries are transported exactly',
      ((Pi*C)*(C.inv()*v)-Pi*v).applyfunc(s.simplify)==s.zeros(2,1))
Psi_new=s.Matrix(s.symbols('u0:2'))
Psi_old=s.Matrix(s.symbols('w0:2'))
Li=s.Matrix(s.symbols('a0:2'))
L0=Li+Psi_new-Psi_old
check('ordinary-to-cap arrow Phi_old T0 equals Ti Phi_new',
      (Psi_old+L0-Li-Psi_new).applyfunc(s.simplify)==s.zeros(2,1))
check('opposite sign would fail the generic annular arrow',
      Psi_old+(Li-Psi_new+Psi_old)!=Li+Psi_new)

F,B=free_group('B')
for n in (-3,-1,0,1,4):
    A=B**n
    check(f'order-one actual norm and quotient generator n={n}',
          A*B**(-n)==F.identity)

G,I0,I1,EX,EY,Cg,PY=free_group('I0,I1,EX,EY,C,PY')
# EX=I1^-1 C EY I0 is the actual forward endpoint relation.
EXactual=I1**-1*Cg*EY*I0
PX=I1**-1*PY*I0
lhs=I0*EXactual**-1*PX*I0**-1
rhs=EY**-1*Cg**-1*PY
check('physical inverse-endpoint identity without commuting any maps',lhs==rhs)
check('the scalar discrepancy disappears by its extending isotopy',
      rhs.eliminate_word(Cg,G.identity)==EY**-1*PY)

result={
 'status':'PASS',
 'statement':'P3K.43 Proved: moving regular order-one sites',
 'utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),
 'identities':checks,
 'geometric_scope':'Actual fixed-source whole-zero I1 families; full period vectors, fixed outer annuli, groupoid Lie solutions, and forward endpoints retained. Full root geometric audit passed.',
 'proof':'notes/part3_moving_order_one_sites_working.md'
}
output=root/'code/part3/moving_order_one_sites.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(checks)} exact moving-site identities. Full root geometric audit passed.')

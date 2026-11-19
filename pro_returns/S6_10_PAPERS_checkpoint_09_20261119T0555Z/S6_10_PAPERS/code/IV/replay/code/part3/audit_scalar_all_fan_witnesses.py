#!/usr/bin/env python3
"""Independent linear-equation audit of the 28 original-family witnesses.

Solve the full target prism equations afresh rather than importing the
root algorithm's reconstruction function. The maps are audited separately.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'code/part3_root/scalar_all_fans.json'
data=json.loads(source.read_text())
witnesses=data['original_shorter_all_28_witnesses']
assert sorted(w['residue'] for w in witnesses)==list(range(28))
J=s.Integer(2);H=s.Rational(1,3);chi=s.Rational(1,6)
Q=[s.Matrix([[1,-1],[0,1]]),s.Matrix([[1,0],[-1,1]])]
vv=s.symbols('v00 v01 v02 v11 v12 v22')
dd=s.symbols('d0 d1 d2');unknowns=vv+dd
Vvar=s.Matrix([[vv[0],vv[1],vv[2]],[vv[1],vv[3],vv[4]],[vv[2],vv[4],vv[5]]])
Dvar=s.Matrix(dd);e=[s.eye(3)[:,i] for i in range(3)]
checks=[];step_count=0
for rec in witnesses:
    n=s.Integer(rec['vertical_index']);P=s.Matrix([[1,0],[n,1]])
    V=s.Matrix([[2*J-6*H+6*J*n*(n-1),2*J*(1-2*n),2*J*(2*n-1)],
                [2*J*(1-2*n),2*J,0],[2*J*(2*n-1),0,2*J]])
    D=s.Matrix([2*J+6*H-24*chi-6*J*n*(n-1),2*J*(2*n-1),2*J*(1-2*n)])
    S=H/2-chi-J*n*(n-1)/2;incs=[]
    for i in rec['word']:
        assert i in (0,1);a=V[i,i];b=D[i]
        inc=s.cancel((b-a)/4);assert inc.is_Integer
        incs.append(int(inc));S+=inc
        P=P*Q[i];B=P.inv()*s.diag(0,2*J)*P
        xy=P.inv()*s.Matrix([0,1]);w=[xy[0],xy[1],-sum(xy)]
        d=[-xy[0]-2*xy[1],-2*xy[0]-xy[1],xy[0]-xy[1]]
        ll=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
        I=[J*w[j]+d[j]*(ll[j]-J) for j in range(3)]
        W=[J*w[j]-d[j]*(ll[j]-J) for j in range(3)]
        assert all(w)
        eqs=[]
        for j in (1,2):
            eqs.extend(Vvar*(w[j]*e[j]-w[0]*e[0])-I[j]*e[j]+I[0]*e[0])
            eqs.append(w[j]*Dvar[j]-w[0]*Dvar[0]-W[j]+W[0])
        eqs.extend([Vvar[2,2]-a,Dvar[2]-(2*a-b)])
        sols=s.linsolve(eqs,unknowns);assert len(sols)==1
        solution=next(iter(sols));assert all(x.is_Integer for x in solution)
        subst=dict(zip(unknowns,solution));V=Vvar.subs(subst);D=Dvar.subs(subst)
        assert s.cancel((D[2]-V[2,2])/4)==-inc
        step_count+=1
    assert list(P)==rec['basis'] and P.det()==1
    assert incs==rec['single_native_increments']
    assert S==rec['integer_path_sum'] and int(S)%28==rec['residue']
    checks.append({'residue':rec['residue'],'basis':list(P),'word':rec['word'],
                   'seed':int(-n*(n-1)),'increments':incs,'integer_sum':int(S)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','reviewer':'blind_control',
     'input':'code/part3_root/scalar_all_fans.json','input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'actual_family':'Original K=L=1 shorter endpoint from K33/K67; J=2,Hhat=1/3,chihat=1/6',
     'residue_count':len(checks),'independent_target_linear_solves':step_count,
     'method':'Each target is solved from its complete integral prism equations plus the selected actual Cox entries; no root reconstruction function is imported.',
     'scope':'Together with audited SA1-4 actual-family maps, these28 literal input fans witness every element of Theta7. No minimality of the displayed bases is asserted.',
     'witnesses':checks}
(ROOT/'code/part3/audit_scalar_all_fan_witnesses.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(f'PASS: all28 actual original-family residue witnesses, {step_count} independent target linear solves, full bases/words/increments checked.')

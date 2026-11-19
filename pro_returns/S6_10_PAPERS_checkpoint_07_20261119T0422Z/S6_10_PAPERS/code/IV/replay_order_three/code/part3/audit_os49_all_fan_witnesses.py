#!/usr/bin/env python3
"""Independent exact target-system audit for the OS49 all-fan witnesses.

No reconstruction function from the root implementation is imported.
Every target is solved afresh from all integral prism equations and
the two transported actual Cox entries. Family maps are audited separately.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'code/part3_root/os49_all_fans.json'
data=json.loads(src.read_text())
witnesses=data['k1_shorter_witnesses']
assert sorted(rec['physical_class_mod28'] for rec in witnesses)==list(range(28))
Q=[s.Matrix([[1,-1],[0,1]]),s.Matrix([[1,0],[-1,1]])]
vv=s.symbols('v00 v01 v02 v11 v12 v22')
dd=s.symbols('d0 d1 d2');unknowns=vv+dd
Vvar=s.Matrix([[vv[0],vv[1],vv[2]],[vv[1],vv[3],vv[4]],[vv[2],vv[4],vv[5]]])
Dvar=s.Matrix(dd);ee=[s.eye(3)[:,i] for i in range(3)]
solves=0;records=[]

def independent(rec,j):
    global solves
    n=s.Integer(rec['vertical_index']);j=s.Integer(j)
    P=s.Matrix([[1,0],[n,1]])
    V=s.Matrix([[12*j*(n-1)**2,8*j*(1-n),8*j*(n-1)],
                [8*j*(1-n),4*j,0],[8*j*(n-1),0,4*j]])
    D=s.Matrix([-12*j*(n-1)**2,8*j*(n-1),8*j*(1-n)])
    path=-j*(n-1)**2;steps=[]
    for i in rec['word']:
        assert i in (0,1)
        a=V[i,i];b=D[i]
        inc=s.cancel((b-a)/4);assert inc.is_Integer
        path+=inc;P=P*Q[i]
        B=2*j*P.inv()*s.Matrix([[0,0],[-1,2]])*P
        xy=P.inv()*s.Matrix([0,1]);w=[xy[0],xy[1],-sum(xy)]
        d=[-xy[0]-2*xy[1],-2*xy[0]-xy[1],xy[0]-xy[1]]
        ll=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
        t=2*j
        I=[t*w[h]+d[h]*(ll[h]-t) for h in range(3)]
        W=[t*w[h]-d[h]*(ll[h]-t) for h in range(3)]
        assert all(w)
        eqs=[]
        for h in (1,2):
            eqs.extend(Vvar*(w[h]*ee[h]-w[0]*ee[0])-I[h]*ee[h]+I[0]*ee[0])
            eqs.append(w[h]*Dvar[h]-w[0]*Dvar[0]-W[h]+W[0])
        eqs.extend([Vvar[2,2]-a,Dvar[2]-(2*a-b)])
        sols=s.linsolve(eqs,unknowns);assert len(sols)==1
        solution=next(iter(sols));assert all(x.is_Integer for x in solution)
        subst=dict(zip(unknowns,solution));V=Vvar.subs(subst);D=Dvar.subs(subst)
        assert s.cancel((D[2]-V[2,2])/4)==-inc
        steps.append({'selected_curve':i,'target':list(P),'old_double_variation':a,
                      'old_double_derivative':b,'single_native_right':inc,
                      'integer_path_sum':path,'double_variation':V.tolist(),
                      'double_stable_derivative':list(D)})
        solves+=1
    assert P.det()==1 and list(P)==rec['canonical_basis']
    return V,D,path,steps

for rec in witnesses:
    V,D,path,steps=independent(rec,1)
    assert V.tolist()==rec['double_variation']
    assert list(D)==rec['double_stable_derivative']
    assert int(path)==rec['integer_path_sum']
    assert int(path)%28==rec['physical_class_mod28']
    assert json.loads(json.dumps(steps,default=int))==rec['steps']
    V3,D3,path3,steps3=independent(rec,3)
    assert V3==3*V and D3==3*D and path3==3*path
    for one,three in zip(steps,steps3):
        assert three['single_native_right']==3*one['single_native_right']
        assert s.Matrix(three['double_variation'])==3*s.Matrix(one['double_variation'])
        assert s.Matrix(three['double_stable_derivative'])==3*s.Matrix(one['double_stable_derivative'])
    records.append({'residue':int(path)%28,'basis':rec['canonical_basis'],
                    'vertical_index':rec['vertical_index'],'word':rec['word'],
                    'integer_sum':int(path),'increments':[int(x['single_native_right']) for x in steps]})

mu,rho,t=s.symbols('mu rho t')
a=-(2*mu-2*t+2*rho)
b=2*rho-(2*mu-2*t)
assert s.simplify((b-a)/4-rho)==0
assert s.simplify((2*a-b-a)/4+rho)==0
# Homogeneity is an exact identity in each entire linear target system:
# B,l,t,I,W,selected a,b scale by j, while w and all equation coefficients
# stay fixed. Its unique solution therefore scales by j.
scale=s.symbols('scale',integer=True)
x,y,ll,t0,a0,b0=s.symbols('x y ll t0 a0 b0')
normdiff=s.symbols('normal_difference')
I=t0*x+normdiff*(ll-t0);W=t0*x-normdiff*(ll-t0)
assert s.expand(I.subs({ll:scale*ll,t0:scale*t0},simultaneous=True)-scale*I)==0
assert s.expand(W.subs({ll:scale*ll,t0:scale*t0},simultaneous=True)-scale*W)==0
assert s.simplify((scale*b0-scale*a0)/4-scale*(b0-a0)/4)==0
assert all({(j*r)%28 for r in range(28)}==set(range(0,28,s.igcd(j,28))) for j in range(1,57))
assert all(s.igcd(3*j,28)==s.igcd(j,28) for j in range(1,57))

out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','reviewer':'blind_control',
     'input':str(src.relative_to(ROOT)),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'actual_family':'OS49, a=1,b=3 component line, m=3k, OR65 actual shorter w=r^3 endpoint and both norm signs; j=k (shorter) or3k (canonical).',
     'residue_count':len(records),'independent_target_linear_solves':solves,
     'method':'Each target is solved afresh from the full integral symmetric-variation/stable-derivative prism system plus its two transported Cox entries; no reconstruction function imported.',
     'homogeneity':'Exact coefficient scaling in the full unique linear system and the actual /4 native increment; j=3 also independently solved on every witness.',
     'scope':'The 28 records are explicit OS49 k=1 witnesses. With the separately audited actual-family maps and induction, homogeneity gives image jZ/28; gcd(3k,28)=gcd(k,28).',
     'witnesses':records}
(ROOT/'code/part3/audit_os49_all_fan_witnesses.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(f'PASS: all28 OS49 k=1 witnesses, {solves} fresh target linear solves, full integer paths and actual degree3 cover checked.')
print('PASS: full-system homogeneity, native factor4, reverse increment, and subgroup images.')

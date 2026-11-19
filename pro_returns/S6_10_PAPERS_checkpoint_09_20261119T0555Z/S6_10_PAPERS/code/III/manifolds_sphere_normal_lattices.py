"""Exact complete fixed-sweep lattice and finite norm data on the172 natural initial rows."""
from pathlib import Path
import json,sympy as s
from collections import Counter
from math import gcd
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']
initial=json.loads((ROOT/'manifolds_sphere_initial.json').read_text())['candidates']
ini={(r['entry'],r['profile'],r['a'],r['b'],r['zero_index']):r for r in initial}

out=[]
for row in rows:
    A=[s.Matrix(x['matrix']) for x in row['local']];N=len(A)
    D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]])
    Sd,Ud,Vd,rd=decomp(D);W=Vd[:,rd:];Wi=Vd.inv()[rd:,:]
    def j(i,x):
        if i<N-1:
            y=s.zeros(4*(N-1),x.cols);y[4*i:4*i+4,:]=x;return y
        out=[]
        for k in range(N-1):
            prod=s.eye(4)
            for z in A[k+1:N-1]:prod=prod*z
            out.append(-prod*x)
        return s.Matrix.vstack(*out)
    fixed=[ikernel(x-s.eye(4)) for x in A]
    B=s.Matrix.hstack(*[Wi*j(i,fix) for i,fix in enumerate(fixed)])
    Sb,Ub,Vb,rb=decomp(B)
    bt=[int(abs(Sb[i,i])) for i in range(rb) if abs(Sb[i,i])>1]
    assert rb==W.cols and B.cols==W.cols+1
    old=ini[(row['entry'],row['profile'],row['a'],row['b'],row['zero_index'])]
    omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
    fd=[]
    for i,(v,c) in enumerate(zip(row['local'],old['local'])):
        k=v['type'];rec=dict(type=k,fixed=fixed[i].tolist(),original_minimal=c['P_component']==0 and c['component_orbits']==1)
        order={'II':6,'III':4,'IV':3,'III*':4,'IV*':3}.get(k)
        if order and v['fixed_gamma_index']==1:
            ell=fixed[i]*bezout(list(fixed[i][3,:]))[0]
            assert ell[3]==1
            Av=A[i][:3,:3];E=Av-s.eye(3);Sv,Uv,Vv,rv=decomp(E)
            tors=[int(abs(Sv[t,t])) for t in range(rv) if abs(Sv[t,t])>1]
            assert rv==2 and not tors
            eta=ikernel(E.T).T
            if eta[0,2]<0:eta=-eta
            beta3=bezout(list(eta))[0];beta=beta3.col_join(s.zeros(1,1));delta=s.eye(4)[:,2]
            q=int(eta[0,2]);Norm=sum((A[i]**t for t in range(order)),s.zeros(4))
            assert Norm*beta==s.Rational(order,q)*delta
            value=int(-(omega*biv(beta,ell))[0])
            assert abs(value)*q==row['b'],(row,k,q,value)
            rec.update(log_order=order,ell=ell.tolist(),beta=beta.tolist(),delta_index=q,normal_fibre_coefficient=value,norm=Norm.tolist())
        fd.append(rec)
    out.append(dict(**{k:row[k] for k in ['entry','profile','a','b','n','zero_type','zero_index']},
        fixed_sweep_torsion=bt,fixed_sweep_matrix=B.tolist(),graph_basis=W.tolist(),local=fd))
print('All fixed-sweep cokernels:',Counter(tuple(x['fixed_sweep_torsion']) for x in out))
for row in out:
 if row['fixed_sweep_torsion']:print(row['entry'],row['profile'],row['a'],row['b'],row['zero_type'],row['fixed_sweep_torsion'])
print('Finite primitive-gamma norms:',sum('delta_index' in x for row in out for x in row['local']))
(ROOT/'manifolds_sphere_normal_lattices.json').write_text(json.dumps(dict(scope=__doc__,rows=out),indent=2,default=int)+'\n')

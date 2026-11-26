#!/usr/bin/env python3
"""Exact new section-class decomposition and Poincare pairing identities.

Only raw defining inputs and my frozen algebra helper are read. No old
proof/program is used. The geometric height equality is proved in the
companion note, not inferred from these arithmetic identities alone.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import importlib.util
import json
import sympy as S

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation5_iii_d2'
helper=INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KM_fresh_arithmetic.py'
assert hashlib.sha256(helper.read_bytes()).hexdigest()=='0160b5f448f9e7865ea11f9557cf2b09f32e2d259cfc9f183e6d40a0e7470690'
spec=importlib.util.spec_from_file_location('own_frozen_section_algebra',helper)
K=importlib.util.module_from_spec(spec);spec.loader.exec_module(K)
E=S.eye(4);I=S.eye(2);J=S.Matrix([[0,1],[-1,0]])
k,l,h1,h2,j1,j2=S.symbols('k l h1 h2 j1 j2')
h=S.Matrix([h1,h2]);hh=S.Matrix([j1,j2])

def exact(A,B):
    assert A.shape==B.shape
    assert all(S.cancel(z)==0 for z in A-B)

def pairing(aa,cc,dd):
    total=E
    explicit=S.Integer(0)
    for i,(A,c,d) in enumerate(zip(aa,cc,dd)):
        beta=-c.T*J*A
        z=K.rational_local_solution(A,d)
        explicit-=(beta*z)[0]
        between=I
        for j in range(i+1,len(aa)):
            explicit-=(beta*between*dd[j])[0]
            between=between*aa[j]
        total=total*K.lift(A,c,d,0)
    expected=E.copy();expected[2,3]=-S.expand(explicit)
    exact(total,expected)
    return S.factor(explicit)

def derive(row,label):
    aa=[S.Matrix(x) for x in row['elliptic_matrices']]
    gg=[S.Matrix(x) for x in row['generator_section_cocycle']]
    sec=K.section_generator_check(aa,gg)
    C=S.Matrix(sec['coboundary']);R=S.Matrix(sec['section_relation'])
    N=S.Matrix(sec['relation_kernel_inverse']);Q=S.Matrix(sec['relation_kernel'])
    U=S.Matrix(sec['coboundary_target_change']);V=S.Matrix(sec['coboundary_source_change'])
    gamma=S.Matrix.vstack(*[K.integer_solve(S.Matrix(b),g) for b,g in zip(sec['local_image_bases'],gg)])
    sigma=sec['generator_quotient_coordinate']
    kr=sigma*U[2,:]*N
    hr=V*(U*N*(S.eye(C.rows)-gamma*kr))[:2,:]
    decomposition=S.Matrix.vstack(hr,kr)
    assembly=C.row_join(gamma)
    K.same(decomposition*assembly,S.eye(3))
    K.same(assembly*decomposition*Q,Q)
    K.same(R*assembly,S.zeros(2,3))
    complement=(S.eye(C.rows)-assembly*decomposition)*K.integer_solve(R,S.eye(2),shorten=True)
    K.same(R*complement,S.eye(2));K.same(decomposition*complement,S.zeros(3,2))
    complete=assembly.row_join(complement)
    assert abs(complete.det())==1
    K.same(complete.inv(),S.Matrix.vstack(decomposition,R))
    cc=[k*g+(A-I)*h for A,g in zip(aa,gg)]
    dd=[l*g+(A-I)*hh for A,g in zip(aa,gg)]
    value=pairing(aa,cc,dd)
    denominator=row['P']*row['Q']
    assert S.cancel(value-k*l/denominator)==0
    # Integral changes of elliptic-logarithm lift and generator orientation.
    p,q=row['P'],row['Q']
    gauge=E.copy();gauge[:2,3]=q*h;gauge[2,:2]=-p*h.T*J
    inverse=E.copy();inverse[:2,3]=-q*h;inverse[2,:2]=p*h.T*J
    exact(gauge*inverse,E);exact(inverse*gauge,E)
    for sign in (1,-1):
        flip=S.diag(sign,sign,1,1)
        change=flip*gauge;change_inverse=inverse*flip
        exact(change*change_inverse,E)
        for A,g,w in zip(aa,gg,row['weights']):
            target=K.lift(A,p*g,q*g,w)
            actual=K.lift(A,p*(sign*g+(A-I)*h),q*(sign*g+(A-I)*h),w)
            exact(change_inverse*target*change,actual)
    print(label,'L=Z; c=k*g+d(h) has both integral maps; B(c,c-prime)=k*l/'+str(denominator)+'; both sign/gauge diagrams exact',flush=True)
    return {'case':label,'denominator':denominator,'section':sec,
            'local_generator':gamma.tolist(),'assembly_C_g':assembly.tolist(),
            'decomposition_h_k':decomposition.tolist(),
            'domain_complete_basis':complete.tolist(),
            'domain_complete_inverse':K.integral(complete.inv()).tolist(),
            'symbolic_pairing':str(value),'component_killing_multiple':denominator}

def main():
    print('New section-index arithmetic started',datetime.now(timezone.utc).isoformat(),flush=True)
    output=[]
    for tag in ('02KM','02KN'):
        path=INPUT_ROOT.parent/'continuation5_iii_infra'/('S6_SERIES_PUBLISH_III_'+tag+'_marked_inputs.json')
        for row in json.loads(path.read_text())['rows']:
            label=tag+':'+str(row['row'])+':OS'+str(row['OS'])+':'+row['profile']
            output.append(derive(row,label))
    (HERE/'S6_SERIES_PUBLISH_III_02KM_section_index_maps.json').write_text(json.dumps(output,separators=(',',':'),default=int)+'\n')
    print('All eleven new section decomposition, pairing and actual-gauge maps verified',datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':main()

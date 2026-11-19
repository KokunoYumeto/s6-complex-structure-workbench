#!/usr/bin/env python3
"""Exact finite characters and simultaneous endpoint identities for K35.

The geometry identifying the actual root-line characters is in the note;
this program checks every residue congruence and the parameter norm.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
a,b,k1,k2,z=S.symbols('a b k1 k2 z')
ee,ff,gg,hh=S.symbols('E11 E12 E21 E22')
T=S.Matrix([[1,b*(gg*k1-ee*k2),b*(hh*k1-ff*k2),z],
            [0,ee,ff,a*k1],[0,gg,hh,a*k2],[0,0,0,1]])
e1=S.Matrix([1,0,0,0])
expected=S.Matrix([1,b*k2,-b*k1,-z])
# Retain the SL(2) relation by checking the actual linear equations.
assert S.simplify(T.T*expected-e1)==S.zeros(4,1)

# The I2 normalization line has node gluing (1,-1).
line_glue=[S.Integer(1),S.Integer(-1)]
t=[S.Integer(1),S.Integer(-1)]
d=[S.Integer(1),S.Integer(-1)]
for j in range(2):
    assert t[(j+1)%2]*line_glue[j]==line_glue[(j+1)%2]*t[j]
    assert d[j]==line_glue[j]*line_glue[(j+1)%2]*d[(j+1)%2]
LT=S.Matrix([[0,t[1]],[t[0],0]])
DD=S.diag(*d)
assert DD*LT*DD.inv()==-LT

# Each row gives b and root orders as residue-polynomials. z_i records
# chi_i=exp(2*pi*i*z_i/b) on the exact root line.
rows=[
    ('E7 single good IIIstar',2,lambda l,k:[4*l],[1]),
    ('E6 single good IVstar',3,lambda l,k:[3*l],[2]),
    ('OS47 single good III',2,lambda l,k:[4*l],[1]),
    ('OS56 single good III',2,lambda l,k:[4*l],[1]),
    ('OS56 single good IV',3,lambda l,k:[3*l],[2]),
    ('OS50 single I1star',2,lambda l,k:[2],[1]),
    ('E6 joint a1 b6',6,lambda l,k:[3*l,4*k],[2,3]),
    ('E6 joint a2 b3',3,lambda l,k:[3*l,4*k+1],[2,0]),
    ('E6 joint a3 b2',2,lambda l,k:[3*l+2,4*k],[0,1]),
    ('E7 joint a1 b2',2,lambda l,k:[4*l,6*k+1],[1,0]),
    ('OS50 joint a6 b2',2,lambda l,k:[2,6*l+1],[1,0]),
    ('OS50 joint a2 b6',6,lambda l,k:[2,3*(2*l+1)],[3,2]),
]
residue_records=[]
for name,bval,orders,zvals in rows:
    checked=0
    for lval,kval in product(range(1,bval+1),repeat=2):
        ms=orders(lval,kval)
        M=S.prod(ms)
        assert M%bval==0
        for ns in product(range(bval),repeat=len(ms)):
            Ps=[int(M//m)*n for m,n in zip(ms,ns)]
            for epsval in [1,-1]:
                if (sum(Ps)-epsval)%bval:
                    continue
                checked+=1
                assert all((P+epsval*zz)%bval==0 for P,zz in zip(Ps,zvals)),(name,ms,ns,epsval,Ps)
    assert checked>0
    residue_records.append(dict(row=name,b=bval,characters=zvals,checked_residue_tuples=checked,
                                relation='P_i + epsilon z_i = 0 mod b'))

M,B,eps,v,U,C,Gamma,j=S.symbols('M B eps v U C Gamma j',integer=True)
tau=S.Matrix([eps*Gamma/B,(U+eps*C-eps*M*v)/B])
sigma=S.Matrix([eps*Gamma*v,v*(U+eps*C)-eps*M*(v*v-v)/2])
alpha=eps*M*(B-1)/(2*B**2)
tau_closed=tau+S.Matrix([0,alpha])
assert S.simplify(sigma.subs(v,v+1/B)-sigma-tau_closed)==S.zeros(2,1)
norm=S.Matrix([S.summation(tau_closed[i].subs(v,v+j/B),(j,0,B-1)) for i in range(2)])
assert S.simplify(norm-B*tau)==S.zeros(2,1)

# Exact polynomial verification of every nonempty canonical branch.
catalogue_path='code/part3/canonical_scalar_catalogue.json'
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened own '+catalogue_path+
              '. Reason: exact K35 integrality for all thirty sphere branches. '
              'Material: full root-order, Euler and height polynomials, retaining excluded branch status.\n')
catalogue=json.loads((ROOT/catalogue_path).read_text())
ll,kk=S.symbols('l k',integer=True,nonnegative=True)
loc={'l':ll,'k':kk}
polynomial_rows=[]
for row in catalogue['branches']:
    if row['status']!='proved_canonical_scalar_branch':
        continue
    bv=row['b']
    mv=S.sympify(row['M'],locals=loc)
    hv=S.sympify(row['H'],locals=loc)
    cv=S.sympify(row['chi'],locals=loc)
    values={'M_over_b':S.expand(mv/bv),'k_w':S.expand(-3*hv/bv),
            'ell_w':S.expand(-24*cv/bv),'A_w':S.expand((cv-hv/2)/bv)}
    for name,value in values.items():
        assert S.Poly(value,ll,kk).domain.is_ZZ,(row['id'],name,value)
    assert S.expand(4*values['k_w']-values['ell_w']-24*values['A_w'])==0
    polynomial_rows.append(dict(id=row['id'],profile=row['profile'],a=row['a'],b=bv,
                                **{name:str(value) for name,value in values.items()}))
assert len(polynomial_rows)==30

data=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS: exact algebra and finite residue certificates; geometric audit is separate',
          weighted_T=[[str(q) for q in T.row(i)] for i in range(4)],
          homology_gamma_column=[str(q) for q in expected],
          I2_line_gluing=[1,-1],I2_translation_frame=[1,-1],I2_deck_frame=[1,-1],I2_commutator=-1,
          rows=residue_records,catalogue_polynomial_rows=polynomial_rows,
          cusp_tau=[str(q) for q in tau],endpoint_constant=str(alpha),
          closed_origin=[str(q) for q in sigma],
          identities=['T^t (1,bk2,-bk1,-z)^t=e1','D L_G D^-1=-L_G on the marked I2 normalization',
                      'all periodic finite-cap character congruences','sigma(v+1/b)-sigma(v)=tau+alpha delta',
                      'exact b-step norm equals the prescribed one-gamma endpoint',
                      'all thirty nonempty branches have integral polynomials M/b, k_w, ell_w, A_w'])
(ROOT/'code/part3_fourfold/weighted_shorter_loop.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+data['utc']+' — Executed own code/part3_fourfold/weighted_shorter_loop.py. '
              'Reason: weighted actual smaller-loop descent. Material: literal Jacobi column, I2 line-frame commutator, '
              'exhaustive finite modular cap characters, exact normalized endpoint and parameter norm.\n')
print('PASS:', '; '.join(data['identities']))
for row in residue_records: print(row)
for row in polynomial_rows: print(row)


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3_fourfold/weighted_shorter_loop.json'], [], origin='code/part3_fourfold/weighted_shorter_loop.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION

#!/usr/bin/env python3
"""Independent continuation-six audit of the saved pre-release KN derivation.

Uses defining inputs and the fifth-continuation fresh maps only. No original
KN proof, D.S5/D.S6/D.S8, or historical KN topology program is read. The new
invariant-factor check evaluates every minor directly, without Smith reduction
or importing any preceding program. Outputs belong to this directory only.
"""
from datetime import datetime, timezone
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import sympy as S

HERE = Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
BASE = INPUT_ROOT.parent / 'continuation5_iii_d2'
INFRA = INPUT_ROOT.parent / 'continuation5_iii_infra'
raw = json.loads((INFRA / 'S6_SERIES_PUBLISH_III_02KN_marked_inputs.json').read_text())['rows']
saved = json.loads((BASE / 'S6_SERIES_PUBLISH_III_02KN_fresh_linear_maps.json').read_text())
families = json.loads((BASE / 'S6_SERIES_PUBLISH_III_02KN_global_families_maps.json').read_text())
middle = json.loads((BASE / 'S6_SERIES_PUBLISH_III_02KN_middle_split_maps.json').read_text())
M = lambda v: S.Matrix(v)
E4, E6 = S.eye(4), S.eye(6)
pairs = list(combinations(range(4), 2))


def wedge(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in pairs] for i,j in pairs])


def check_saved_geometry_and_graphs():
    for inp, row, fam in zip(raw, saved['rows'], families):
        assert inp['OS'] == row['OS'] == fam['OS']
        p = row['P']
        T = [M(x) for x in row['matrices']]
        assert T[0] == E4
        prod = E4
        for A in T:
            prod = prod*A
        assert prod == E4
        # Reconstruct the local lift by a separate direct equation solve.
        J = S.Matrix([[0,1],[-1,0]])
        for A0,g0,w,T0,sg in zip(inp['elliptic_matrices'], inp['generator_section_cocycle'],
                                 inp['weights'], T[1:], row['poincare_gauges']):
            A,g = M(A0), M(g0)
            def local(b):
                x,free = (A-S.eye(2)).gauss_jordan_solve(b)
                return x.subs({t:0 for t in free})
            h,z = local(p*g),local(g)
            beta = -(p*g).T*J*A
            rebuilt = S.eye(4)
            rebuilt[:2,:2] = A
            rebuilt[:2,3] = g
            rebuilt[2,:2] = beta
            rebuilt[2,3] = (beta*z)[0]+w
            assert rebuilt == T0
            C,Ci = M(sg['S']),M(sg['S_inverse'])
            diag = S.eye(4);diag[:2,:2]=A;diag[2,3]=w
            assert C*Ci == Ci*C == E4 and Ci*diag*C == T0
        D = S.Matrix.hstack(*(A-E4 for A in T[:5]))
        C,K,Inv = (M(row[k]) for k in ['graph_complement','graph_K','graph_complete_inverse'])
        assert D*K == S.zeros(4,17)
        full = C.row_join(K)
        assert full*Inv == Inv*full == S.eye(20)
        assert Inv[:3,:] == D[:3,:]
        W,Bv = M(row['vanishing_columns']),M(row['vanishing_preimages'])
        assert W*Bv == E4[:,:3]
        B = S.Matrix.hstack(*(wedge(A)-E6 for A in T[:5]))
        F,Z = M(row['fibre_relation_basis']),M(row['fibre_relation_preimages'])
        om,s = M(row['omega']),M(row['fibre_s'])
        assert B*Z == F and om*B == S.zeros(1,30) and om*s == S.ones(1,1)
        assert abs(s.row_join(F).det()) == 1
        for i,loc in row['local'].items():
            H,Hi = M(loc['H']),M(loc['H_inverse'])
            canonical = E4.copy();canonical[0,1]=1
            if loc['kind']=='rank_two':canonical[2,3]=1
            assert H*Hi == Hi*H == E4 and Hi*T[int(i)]*H == canonical
        Jac,Ji = M(fam['coefficient_Jacobian']),M(fam['Jacobian_inverse'])
        assert Jac*Ji == Ji*Jac == S.eye(12)
        assert Jac.det() == S.Integer(fam['determinant']) != 0
        t = S.Symbol('t')
        f,h = S.sympify(fam['g2']),S.sympify(fam['g3'])
        disc = S.expand(f**3-27*h**2)
        assert S.expand(disc-S.sympify(fam['discriminant'])) == 0
        assert S.degree(disc,t) == 12-fam['infinity']
        a = S.sympify(fam['additive_point'])
        b = fam['fixed_point'];q=fam['fixed_multiplicity']
        if b is not None:
            b=S.sympify(b)
            assert f.subs(t,b) != 0
            assert all(S.diff(disc,t,j).subs(t,b)==0 for j in range(q))
            assert S.diff(disc,t,q).subs(t,b)!=0
        assert M(fam['torsion_left_inverse'])*M(fam['torsion_stack']) == S.eye(2)
        merger,mi = M(fam['merger']),M(fam['merger_inverse'])
        assert merger*mi == mi*merger == S.eye(2)
        print('OS',row['OS'],'p',p,': lifts; Poincare maps; full graph and fibre quotient inverses;'
              ' primitive vanishers; local models; global Jacobian; discriminant orders; torsion and merger maps passed.')


def check_all_minor_values():
    p,m,n,a,b,c = S.symbols('p m n a b c',integer=True)
    R = S.Matrix([[-p*b,p*a,n,-c,0],[m,0,0,0,a],[0,m,0,0,b],[0,0,0,m,n]])
    polys={}
    for k in range(1,5):
        polys[k]=[S.expand(R.extract(rr,cc).det())
                  for rr in combinations(range(4),k)
                  for cc in combinations(range(5),k)]
    assert sum(map(len,polys.values()))==125
    evaluators={k:S.lambdify((p,m,n,a,b,c),v,modules='math') for k,v in polys.items()}
    total=0;zero=0;t_values=set();n_unit=0;a_unit=0;c_unit=0
    for pp in [8,14,20,30]:
        local_count=0
        for mm in range(1,31):
            for nn in [-30,-14,-6,-1,0,1,6,14,30]:
                for k in range(12):
                    aa=(k*k+3*k+pp)%(2*mm+1)-mm
                    bb=(5*k+pp//2)%(2*mm+1)-mm
                    cc=(7*k*k+1)%(2*mm+1)-mm
                    if gcd(mm,nn,aa,bb,cc)!=1:continue
                    d1,d2=gcd(mm,nn,aa,bb),gcd(mm,nn,pp,cc)
                    tt=d1*d2
                    assert gcd(d1,d2)==1 and mm%tt==0 and nn%tt==0
                    ds=[reduce(gcd,(int(x) for x in evaluators[j](pp,mm,nn,aa,bb,cc)),0)
                        for j in range(1,5)]
                    assert ds==[1,tt,mm*tt,mm*mm*abs(nn)],(pp,mm,nn,aa,bb,cc,ds)
                    total+=1;local_count+=1;zero+=int(nn==0);t_values.add(tt)
                    n_unit+=int(gcd(mm,nn)==1)
                    a_unit+=int(gcd(mm,aa)==1 or gcd(mm,bb)==1)
                    c_unit+=int(gcd(mm,cc)==1)
        print('p',pp,local_count,'primitive cases: all 125 minors directly evaluated, no Smith program imported.')
    print('Total primitive cases',total,'including n=0',zero,'; attained t',sorted(t_values))
    print('m-coprime coordinate coverage: n',n_unit,'; a or b',a_unit,'; c',c_unit)


def check_middle_and_quotient_maps():
    for case in saved['parameter_maps']:
        p,m,n,a,b,c=case['parameters']
        R=S.Matrix([[-p*b,p*a,n,-c,0],[m,0,0,0,a],[0,m,0,0,b],[0,0,0,m,n]])
        q=S.Matrix([-a,-b,-c,-n,m])
        H,Q,r=M(case['central_quotient']),M(case['central_section']),M(case['normal_coordinate'])
        assert H*Q == S.eye(4) and H*q == S.zeros(4,1)
        assert Q*H+q*r == S.eye(5) and r*q == S.ones(1,1)
        U,Ui,V,Vi,D=(M(case[k]) for k in ['target_change','target_inverse','source_change','source_inverse','smith_diagonal'])
        assert U*Ui==Ui*U==V*Vi==Vi*V==S.eye(4)
        assert U*R*Q*V==D
    rows={r['P']:r for r in saved['rows']}
    for rec in middle:
        p,m,a,b,c=rec['parameters'];d=rec['d']
        q=S.Matrix([-a,-b,-c,0,m])
        lam=M(rec['central_loop_representative'])
        physical=lam[:4,:]+lam[4]*S.Matrix([a,b,c,0])/m
        assert physical==S.Matrix([0,0,S.Rational(1,d),0])
        assert M(rec['kernel_coordinate']).T*M(rec['kernel_relation'])==S.zeros(1,1)
        T=[M(x) for x in rows[p]['matrices']]
        B=S.Matrix.hstack(*(wedge(A)-E6 for A in T[:5]))
        assert B*M(rec['fibre_bounding_cylinders'])==M(rec['fibre_correction'])
    print('All',len(saved['parameter_maps']),'central quotient and target/source inverse pairs passed.')
    print('All',len(middle),'n=0 primitive central loops and exact fibre bounding chains passed.')


if __name__=='__main__':
    print('Continuation-six pre-exposure audit started',datetime.now(timezone.utc).isoformat())
    check_saved_geometry_and_graphs()
    check_all_minor_values()
    check_middle_and_quotient_maps()
    print('All audited identities passed; original KN proof remains closed.')
    print('Continuation-six pre-exposure audit completed',datetime.now(timezone.utc).isoformat())

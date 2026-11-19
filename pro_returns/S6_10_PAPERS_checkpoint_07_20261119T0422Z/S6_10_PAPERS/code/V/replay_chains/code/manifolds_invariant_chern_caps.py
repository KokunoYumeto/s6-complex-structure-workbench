"""Original additive caps with arbitrary invariant component Chern vectors.

Exact mapping-torus cone, including the nonsplit cyclic torsion Z_h.
This computes the actual delta-gamma and regular elliptic-area classes.
It does not infer the missing marked mixed or normal columns from ranks.
"""
from pathlib import Path
from math import gcd
from functools import reduce
import json
import sympy as S
import manifolds_general_initial as G
import manifolds_weighted_profiles as W
import root_vertical_corrections as V

ROOT=Path(__file__).resolve().parents[1]
ADDITIVE=['II','III','IV','I1*','I3*','IV*','III*']

def all_orbits(T):
    seen=set();out=[]
    for i in range(T.rows):
        if i in seen:continue
        orb=[];j=i
        while j not in seen:
            seen.add(j);orb.append(j);j=list(T[:,j]).index(1)
        out.append(orb)
    return out

def cap(kind,q,c,keep_matrices=True):
    J,T,labels,mult=V.component_matrix(kind)
    T=T**q; c=S.Matrix(c);v=len(c)
    assert T*c==c and (c.T*S.Matrix(mult))[0]==0
    orbs=all_orbits(T);rho=len(orbs)
    g=reduce(gcd,[abs(int(x)) for x in c])
    h=reduce(gcd,[abs(int(len(o)*c[o[0]])) for o in orbs])
    d2=S.zeros(2,v+1);d2[0,:v]=c.T
    d3=S.zeros(v+1,2*v);d3[:v,v:]=T-S.eye(v);d3[v,v:]=c.T
    d4=S.zeros(2*v,v);d4[:v,:]=S.eye(v)-T
    assert d2*d3==S.zeros(2,2*v) and d3*d4==S.zeros(v+1,v)
    K2=G.ikernel(d2);I2=W.integral_left_inverse(K2);R2=I2*d3
    K3=G.ikernel(d3);I3=W.integral_left_inverse(K3);R3=I3*d4
    H1=W.group(d2);H2=W.group(R2);H3=W.group(R3)
    H4=dict(free=G.ikernel(d4).cols,torsion=[])
    if g:
        assert h%g==0
        expected=[dict(free=1,torsion=([g] if g>1 else [])),
                  dict(free=rho-1,torsion=([h] if h>1 else [])),
                  dict(free=2*rho-1,torsion=[]),dict(free=rho,torsion=[])]
    else:
        assert h==0
        expected=[dict(free=2,torsion=[]),dict(free=rho+1,torsion=[]),
                  dict(free=2*rho,torsion=[]),dict(free=rho,torsion=[])]
    assert [H1,H2,H3,H4]==expected
    tt=S.zeros(v+1,1);tt[v]=1
    mu=S.Matrix(mult).col_join(S.zeros(1,1))
    assert d2*tt==S.zeros(2,1) and d2*mu==S.zeros(2,1)
    tcoord=I2*tt;fcoord=I2*mu
    killed_t=W.group(R2.row_join(tcoord))
    if g:
        assert killed_t==dict(free=rho-1,torsion=[])
        G.integer_solution(R2,h*tcoord)
    else:
        assert killed_t==dict(free=rho,torsion=[])
    qcomp=reduce(gcd,[int(len(o)*mult[o[0]]) for o in orbs])
    partial_cokernel=W.group(R2.row_join(tcoord).row_join(fcoord))
    assert partial_cokernel==dict(free=rho-(2 if g else 1),
                                 torsion=([qcomp] if qcomp>1 else []))
    rec=dict(type=kind,Q_component=q,chern=list(map(int,c)),orbits=orbs,
             g=g,h=h,rho=rho,component_order=qcomp,
             homology=[dict(free=1,torsion=[]),H1,H2,H3,H4],
             delta_gamma_class=list(map(int,tcoord)),
             elliptic_area_class=list(map(int,fcoord)),
             area_and_delta_gamma_cokernel=partial_cokernel)
    if keep_matrices:
        rec.update(cone_d2=d2.tolist(),cone_d3=d3.tolist(),cone_d4=d4.tolist(),
                   H2_cycle_basis=K2.tolist(),H2_relations=R2.tolist())
    return rec

def main():
    records=[];seen=set();old=0;nonprimitive=0;residual=0
    for kind in ADDITIVE:
        J,T,labels,mult=V.component_matrix(kind)
        for p in range(len(labels)):
            for q in range(len(labels)):
                sol=V.solve_local(kind,p,q)
                if not sol['exists']:continue
                base=S.Matrix(sol['vertical_coefficients'])
                kernel=G.ikernel(T**q-S.eye(T.rows))
                options=[S.zeros(kernel.cols,1),S.ones(kernel.cols,1)]
                for j in range(kernel.cols):
                    for a in [-2,-1,1,2]:options.append(a*S.eye(kernel.cols)[:,j])
                options.extend(S.Matrix([((-1)**(i+j))*(i+1) for i in range(kernel.cols)])
                               for j in range(2))
                for coeff in options:
                    divisor=base+kernel*coeff
                    c=S.eye(J.rows)[:,labels[p]]-S.eye(J.rows)[:,labels[0]]+J*divisor
                    key=(kind,q,tuple(c))
                    if key in seen:continue
                    seen.add(key);rec=cap(kind,q,c)
                    rec.update(P_component=p,vertical_coefficients=list(map(int,divisor)))
                    records.append(rec)
                    nonprimitive+=rec['g']>1
                    residual+=rec['g']>0 and rec['h']>rec['g']
                    old+=not rec['g'] or (p and q==0 and rec['g']==1)
    markings=[]
    for key,info in sorted(G.PROFILES.items()):
        for site,kind in enumerate(info['kodaira_types']):
            if kind not in ADDITIVE:continue
            J,T,labels,mult=V.component_matrix(kind)
            cc=info['component_maps'][site]
            order=int(cc['moduli'][0]) if cc['moduli'] else 1
            residue=int(cc['rows'][0][0]) if cc['rows'] else 0
            B=S.Matrix(info['elliptic_matrices'][site]);v=S.Matrix(info['section_cocycles'][0][site])
            for b in range(order):
                q=b*residue%order
                z=(B-S.eye(2)).inv()*(b*v)
                denominator=S.ilcm(*[int(x.q) for x in z])
                orbit=all_orbits(T**q)
                content=reduce(gcd,[len(o)*mult[o[0]] for o in orbit])
                assert int(denominator)==content==order//gcd(order,q)
                marks=[content]+[int(content*x) for x in z]
                assert reduce(gcd,map(abs,marks))==1
                markings.append(dict(key=key,site=site,type=kind,b_residue=b,
                                     Q_component=q,logarithm=list(map(str,z)),
                                     primitive_area_index=content))
    report=dict(scope=__doc__,cases=records,actual_component_log_markings=markings,
                nonprimitive_Chern_cases=nonprimitive,residual_orbit_torsion_cases=residual,
                previous_zero_or_primitive_narrow_cases=old)
    (ROOT/'records/manifolds_invariant_chern_caps.json').write_text(json.dumps(report,indent=2,default=int)+'\n')
    print('Exact original-additive mapping-torus cones:',len(records))
    print('Actual component/logarithm denominator certificates:',len(markings))
    print('Nonprimitive Chern cases:',nonprimitive,'residual orbit torsion:',residual)
    print('Every literal delta-gamma class generates the complete cyclic cap torsion.')
    print('Marked mixed and fixed-normal columns remain a separate unresolved comparison.')

if __name__=='__main__':main()

"""All height-integral initial pairs with canonical corrected original stars.

Uses the proved D46 bar construction and D51 h=1 original additive map.
Original multiplicative caps currently require their uncorrected degree vector;
zero-degree original additive caps require the zero relative divisor marking.
All Mumford and free finite cap parameters remain unrestricted.
"""
from math import gcd
from functools import reduce
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
from manifolds_general_initial import (ROOT,PROFILES,W,ikernel,wedge,biv,decomp,
    satimage,integer_solution,rational_solution,local_lift,component_geometry,
    orbit_number,graph_data)
import root_vertical_corrections as VC
from manifolds_invariant_chern_caps import all_orbits

def actual_lifts(info,a,b,weights):
    kinds=info['kodaira_types'];height=s.Rational(info['height_matrix'][0][0])*a*b
    if height.q!=1 or len(weights)<len(kinds) or sum(weights)!=height:
        raise ValueError('Weights must sum to the integral height pairing.')
    for kind,w in zip(kinds,weights):
        if w and not(kind.startswith('I') and kind[1:].isdigit()):
            raise ValueError('Positive weights require a semistable or regular site.')
    cocycle=info['section_cocycles'][0]
    A=[local_lift(B,a*s.Matrix(c),b*s.Matrix(c),w)
       for B,c,w in zip(info['elliptic_matrices'],cocycle,weights)]
    A.extend(local_lift(s.eye(2),[0,0],[0,0],w) for w in weights[len(kinds):])
    assert all(x.q==1 for M in A for x in M)
    product=s.eye(4)
    for M in A:product*=M
    assert product==s.eye(4)
    return A

def correction_data(info,a,b,vertical_divisors=None):
    supplied={int(j):v for j,v in (vertical_divisors or {}).items()}
    out={}
    for j,(kind,component) in enumerate(zip(info['kodaira_types'],info['component_maps'])):
        order=int(component['moduli'][0]) if component['moduli'] else 1
        res=int(component['rows'][0][0]) if component['rows'] else 0
        p,q=a*res%order,b*res%order
        J,T,labels,mult=VC.component_matrix(kind)
        particular=VC.solve_local(kind,p,q)
        if not particular['exists']:raise ValueError('No corrected initial line exists.')
        divisor=s.Matrix(supplied.get(j,particular['vertical_coefficients']))
        c=s.eye(J.rows)[:,labels[p]]-s.eye(J.rows)[:,labels[0]]+J*divisor
        if T**q*c!=c:raise ValueError('The supplied degree vector is not Q-invariant.')
        orbit=all_orbits(T**q)
        h=reduce(gcd,[abs(int(len(o)*c[o[0]])) for o in orbit])
        out[j]=dict(type=kind,P_component=p,Q_component=q,
                    divisor=list(map(int,divisor)),chern=list(map(int,c)),
                    orbits=orbit,rho=len(orbit),h=h)
    return out

def compute(entry,profile,a,b,weights,original=(),finite=None,regular=None,e=0,vertical_divisors=None):
    if (entry,profile) not in PROFILES:raise ValueError('Not one of the21 marked MW=Z profiles.')
    if a<=0 or b<=0:raise ValueError('This construction takes a,b>0.')
    info=PROFILES[(entry,profile)]
    weights=list(map(int,weights))
    if any(w<0 for w in weights):raise ValueError('Nonnegative effective weights required.')
    rawA=actual_lifts(info,a,b,weights)
    corrected=correction_data(info,a,b,vertical_divisors)
    kinds=list(info['kodaira_types'])+['I0']*(len(weights)-len(info['kodaira_types']))
    original=set(map(int,original))
    original|={j for j,k in enumerate(kinds) if k.startswith('I') and k.endswith('*') and k[1:-1].isdigit()}
    if any(weights[j] for j in original):raise ValueError('An original cap requires a unit linearization.')
    finite={int(i):d for i,d in (finite or {}).items()}
    regular=list(regular or [])+[dict(m=1,v=[0,0,0,-int(e)])]
    offset=len(regular);A=[s.eye(4) for _ in regular]+rawA
    K,Js,correction=graph_data(A);count=len(A)
    fibre_rel=s.Matrix.hstack(*[wedge(B)-s.eye(6) for B in A])
    columns=[fibre_rel[:,j].col_join(s.zeros(K.cols,1)) for j in range(fibre_rel.cols)]
    # H1 of the regular graph bundle, then of the finite-filled exterior.
    h1rows=4+count-1
    h1=[(B-s.eye(4))[:,j].col_join(s.zeros(count-1,1)) for B in A for j in range(4)]
    def base(i):
        if i<count-1:return s.eye(count-1)[:,i]
        return -s.ones(count-1,1)
    def h1column(v,i,m=0):return s.Matrix(v).col_join(m*base(i))
    finite_powers=[];nonfinite=[];capdata=[];vertical=[];chi=0;h4sum=0
    delta=s.eye(4)[:,2]
    def finite_cap(i,m,v,h):
        v=s.Matrix(v)
        if h==1:
            valid=A[i]==s.eye(4) and m>0 and gcd(m,*map(int,v))==1
        else:valid=W.finite_free(A[i],h,m,v)
        if not valid:raise ValueError(f'Nonfree finite cap at global site {i}.')
        N=(m//h)*sum((A[i]**j for j in range(h)),s.zeros(4))
        for lam in s.eye(4).columnspace():
            f=(m//h)*sum((correction(i,A[i]**j*lam) for j in range(h)),s.zeros(6,1))
            columns.append((f-biv(lam,v)).col_join(Js[i]*N*lam))
        columns.append(correction(i,v).col_join(Js[i]*v))
        h1.append(h1column(-v,i,m))
        finite_powers.append(dict(site=i,m=m,v=list(map(int,v))))
    for i,data in enumerate(regular):
        finite_cap(i,int(data['m']),data['v'],1)
    for j,(kind,w,Aj) in enumerate(zip(kinds,weights,rawA)):
        i=offset+j
        if kind in W.ORDER and j not in original:
            h=W.ORDER[kind];data=finite.get(j) or W.default_finite(Aj,h)
            finite_cap(i,int(data['m']),data['v'],h)
            capdata.append(dict(site=j,type=kind,kind='finite',m=int(data['m']),v=data['v']))
            continue
        fixed=ikernel(Aj-s.eye(4));R2=wedge(Aj)-s.eye(6)
        semistable=kind.startswith('I') and kind[1:].isdigit()
        is_original=j in original
        if kind=='I0':
            if w<=0:raise ValueError('A listed smooth zero must have positive weight.')
            pc=qc=0;mult=[1];rho=w
        else:
            comp=info['component_maps'][j]
            mod=int(comp['moduli'][0]) if comp['moduli'] else 1
            res=int(comp['rows'][0][0]) if comp['rows'] else 0
            pc=(a*res)%mod;qc=(b*res)%mod
            mult,perm,labels=component_geometry(kind)
        cc=is_original and pc!=0
        local_correction=corrected.get(j)
        if is_original and semistable and any(local_correction['divisor']):
            raise ValueError('A vertically corrected original multiplicative cap is outside this algorithm.')
        if is_original and not semistable:
            c=local_correction['chern']
            if any(c):
                if local_correction['h']!=1:
                    raise ValueError('The marked original additive cap currently requires h=1.')
                z=rational_solution(Aj[:2,:2]-s.eye(2),Aj[:2,3])
                area=s.Matrix([[1,0,z[1],0,-z[0],0]])
                area=s.ilcm(*[int(x.q) for x in area])*area
                F2=ikernel(area);F1=s.eye(4)[:,:3]
                comps=local_correction['rho'];capkind='corrected_original_h1'
            else:
                if any(local_correction['divisor']):
                    raise ValueError('A nonzero whole-fibre correction requires its relative theta marking.')
                F2=satimage(R2);F1=satimage(Aj-s.eye(4))
                comps=local_correction['rho'];capkind='original_zero_chern'
        elif cc:
            assert qc==0
            z=integer_solution(Aj[:2,:2]-s.eye(2),Aj[:2,3])
            ell=(-z).col_join(s.Matrix([0,1]))
            if semistable:
                van=ikernel(Aj[:2,:2]-s.eye(2))[:,0]
                u1=van.col_join(s.zeros(2,1))
                F2=s.Matrix.hstack(biv(u1,delta),biv(u1,ell),biv(delta,ell))
                F1=s.Matrix.hstack(u1,delta)
            else:
                area=s.Matrix([[1,0,z[1],0,-z[0],0]])
                area=s.ilcm(*[int(x.q) for x in area])*area
                F2=ikernel(area);F1=s.eye(4)[:,:3]
            comps=len(mult);capkind='original_nonzero_chern'
        elif not is_original and semistable and kind!='I0' and w>0:
            assert fixed.cols==2 and (Aj-s.eye(4))**2==s.zeros(4)
            F2=R2.row_join(biv(fixed[:,0],fixed[:,1]))
            F1=fixed;comps=int(kind[1:])*w;chi+=2*comps
            capkind='rank_two_mumford'
            SD,_,_,rank=decomp(Aj-s.eye(4));assert rank==2
            assert abs(SD[0,0]*SD[1,1])==comps
        else:
            F2=satimage(R2);F1=satimage(Aj-s.eye(4))
            if is_original:
                comps=orbit_number(perm,qc);capkind='original_zero_chern'
            else:
                SD,_,_,rank=decomp(Aj-s.eye(4));assert rank==1
                comps=abs(int(SD[0,0]));capkind='rank_one_mumford'
        for q in range(fixed.cols):
            v=fixed[:,q];columns.append(correction(i,v).col_join(Js[i]*v))
        for q in range(F2.cols):columns.append(F2[:,q].col_join(s.zeros(K.cols,1)))
        assert all(F1[3,q]==0 for q in range(F1.cols))
        vertical.extend(F1.columnspace())
        nonfinite.append((i,F1))
        h4sum+=comps
        capdata.append(dict(site=j,type=kind,kind=capkind,components=comps,
                            P_component=pc,Q_component=qc,
                            fibre_kernel=F2.tolist(),normal_vectors=fixed.tolist(),
                            pi1_kernel=F1.tolist()))
    exteriorH1=W.group(s.Matrix.hstack(*h1))
    for i,F1 in nonfinite:
        for v in F1.columnspace():h1.append(h1column(v,i))
        h1.append(h1column(s.zeros(4,1),i,1))
    H1matrix=s.Matrix.hstack(*h1);H1=W.group(H1matrix)
    M=s.Matrix.hstack(*columns);G=W.group(M)
    free_relative=h4sum-exteriorH1['free']+H1['free']
    assert free_relative>=0
    b2=G['free']+free_relative;b3=2+2*b2-2*H1['free']-chi
    assert b3>=0
    T=G['torsion'];A1=H1['torsion'];r=H1['free']
    homology=[dict(free=1,torsion=[]),H1,dict(free=b2,torsion=T),
              dict(free=b3,torsion=T),dict(free=b2,torsion=A1),
              dict(free=r,torsion=[]),dict(free=1,torsion=[])]
    # Exact normal closure of cap vanishing vectors in the abelian fibre.
    Z=hermite_normal_form(s.Matrix.hstack(*vertical))
    while True:
        Znew=hermite_normal_form(s.Matrix.hstack(Z,*[B*Z for B in A]))
        if Znew==Z:break
        Z=Znew
    Vgroup=W.group(Z[:3,:])
    presentation=dict(fibre_generators=['e1','e2','delta','gamma'],
                      fibre_abelian=True,base_generators=[f't{i}' for i in range(count)],
                      conjugation_matrices=[B.tolist() for B in A],
                      base_product='1',finite_power_relations=finite_powers,
                      unchanged_caps=[dict(site=i,killed_vectors=F1.tolist(),base_loop_killed=True)
                                      for i,F1 in nonfinite],
                      vertical_normal_closure=Z.tolist(),vertical_quotient=Vgroup)
    return dict(entry=entry,profile=profile,P=a,Q=b,weights=weights,e=e,
                original_sites=sorted(original),vertical_corrections=corrected,local=capdata,euler=chi,
                regular_coinvariant_H2=W.group(fibre_rel),exterior_H1=exteriorH1,
                relative_free_rank=free_relative,H1_matrix=H1matrix.tolist(),
                H2_matrix=M.tolist(),homology=homology,fundamental_group=presentation)


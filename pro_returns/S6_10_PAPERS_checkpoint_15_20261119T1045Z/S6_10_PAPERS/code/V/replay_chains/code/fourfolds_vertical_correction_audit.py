"""Independent exact audit of root D.2.50; no root-owned file is changed.

All 227 finite component pairs and 5696 profile residues are exhaustive.
The all-integer claim follows by periodicity and the proof, not a search
bound on a or b. Actual monodromy cocycles are checked against the local
component-group orders before the profile residue tests.
"""
from pathlib import Path
import json, math
import sympy as s
import root_vertical_corrections as R
ROOT=Path(__file__).resolve().parents[1]
local=[]; profiles=[]; actual=[]; new_initial=[]
kinds=sorted({k for row in R.G.PROFILES.values() for k in row['kodaira_types']})
for kind in kinds:
    J,T,labels,mult=R.component_matrix(kind)
    assert T*J==J*T
    assert T**len(labels)==s.eye(J.rows)
    for p in range(len(labels)):
        for q in range(len(labels)):
            delta=T**q-s.eye(J.rows)
            c=s.eye(J.rows)[:,labels[p]]-s.eye(J.rows)[:,labels[0]]
            A=delta*J; rhs=-delta*c
            D,U,V,rank=R.G.decomp(A)
            assert U*A*V==D and abs(int(U.det()))==abs(int(V.det()))==1
            b=U*rhs
            solvable=all(b[j]%D[j,j]==0 for j in range(rank)) and all(b[j]==0 for j in range(rank,A.rows))
            result=R.solve_local(kind,p,q)
            assert solvable==result['exists']==(p*q%len(labels)==0)
            if solvable:
                z=s.Matrix(result['vertical_coefficients'])
                assert A*z==rhs
                K=s.Matrix.hstack(*[s.Matrix(v) for v in result['all_correction_kernel_columns']])
                assert delta*K==s.zeros(J.rows,K.cols)
                # Every orbit sum is an actual integral kernel element.
                seen=set(); orbit_sums=[]
                for j in range(J.rows):
                    if j in seen: continue
                    vec=s.zeros(J.rows,1); pos=j
                    while pos not in seen:
                        seen.add(pos);vec[pos]=1
                        pos=next(i for i in range(J.rows) if (T**q)[i,pos])
                    orbit_sums.append(vec)
                assert len(orbit_sums)==K.cols
                for vec in orbit_sums:
                    assert A*vec==s.zeros(A.rows,1)
            local.append(dict(kind=kind,p=p,q=q,exists=solvable))
for key,info in sorted(R.G.PROFILES.items()):
    d0=int(s.Rational(info['height_matrix'][0][0]).q)
    orders=[]
    for j,(kind,component,B,g) in enumerate(zip(info['kodaira_types'],info['component_maps'],info['elliptic_matrices'],info['section_cocycles'][0])):
        n=int(component['moduli'][0]) if component['moduli'] else 1
        residue=int(component['rows'][0][0]) if component['rows'] else 0
        assert math.gcd(n,residue)==1
        B=s.Matrix(B);g=s.Matrix(g)
        D,U,V,rank=R.G.decomp(B-s.eye(2));b=U*g
        assert all(b[j]==0 for j in range(rank,2))
        order=math.lcm(*(abs(int(D[j,j]))//math.gcd(abs(int(D[j,j])),int(b[j])) for j in range(rank)))
        assert order==n
        actual.append(dict(entry=key[0],profile=key[1],site=j,kind=kind,recorded_order=n,actual_cocycle_order=order,recorded_generator=residue))
        orders.append(n)
    assert math.lcm(*orders)==d0
    valid=extra=0
    for a in range(d0):
        for b in range(d0):
            possible=True;narrow=True
            for kind,component,n in zip(info['kodaira_types'],info['component_maps'],orders):
                residue=int(component['rows'][0][0]) if component['rows'] else 0
                p=a*residue%n;q=b*residue%n
                possible &= R.solve_local(kind,p,q)['exists']
                narrow &= p==0 or q==0
            assert possible==(a*b%d0==0)
            valid+=possible;extra+=possible and not narrow
    for a in range(1,d0+1):
        if d0%a:continue
        b=d0//a
        narrow=all(a*(int(c['rows'][0][0]) if c['rows'] else 0)%n==0 or b*(int(c['rows'][0][0]) if c['rows'] else 0)%n==0 for c,n in zip(info['component_maps'],orders))
        if not narrow:new_initial.append(dict(entry=key[0],profile=key[1],a=a,b=b,height=1))
    profiles.append(dict(entry=key[0],profile=key[1],d0=d0,pairs=d0*d0,valid=valid,extra=extra))
result=dict(status='PASS',local_pairs=len(local),global_pairs=sum(p['pairs'] for p in profiles),actual_component_cocycles=len(actual),local=local,profiles=profiles,actual=actual,new_height_one_initial_pairs=new_initial,scope='Initial-line existence and exact integral corrections only; no unproved cap-topology extension.')
(ROOT/'records/fourfolds_vertical_correction_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',result['local_pairs'],'local pairs;',result['global_pairs'],'global residues;',len(actual),'actual component cocycles;',len(new_initial),'additional height-one pairs.')

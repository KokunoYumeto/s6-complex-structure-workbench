#!/usr/bin/env python3
"""Actual E6+A1 joint complement for IV*+III+I1, all four source pairs.

The source is y^2=x^3+t*x+t^2 with G=(0,t).  The signed source map
is translation by -bG.  Every boundary map is obtained on the full
relative chain cone before computing integral homology.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parent

def dec(M):
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D,U,V=[x.to_Matrix() for x in (D,U,V)]
    assert D==U*M*V
    return D,U,V

def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def syms(M):
    return [[str(x) for x in row] for row in M.tolist()]

def hom(d,up):
    assert d*up==s.zeros(d.rows,up.cols)
    D,U,V=dec(d); r=d.rank(); K=V[:,r:]
    relations=(V.inv()*up)[r:,:]
    assert K*relations==up
    E,L,R=dec(relations); rr=relations.rank()
    inds=[i for i in range(K.cols) if i>=rr or abs(E[i,i])!=1]
    orders=[0 if i>=rr else abs(int(E[i,i])) for i in inds]
    reps=K*L.inv()[:,inds]
    proj=(L*V.inv()[r:,:])[inds,:]
    assert proj*reps==s.eye(len(inds))
    return orders,reps,proj

def cone(d,f,dimensions):
    dims={j:dimensions.get(j,0)+dimensions.get(j-1,0) for j in range(7)}
    out={}
    for j in range(1,7):
        top=d.get(j,s.zeros(dimensions.get(j-1,0),dimensions.get(j,0))).row_join(
            f.get(j-1,s.zeros(0))-s.eye(dimensions.get(j-1,0)))
        bot=s.zeros(dimensions.get(j-2,0),dimensions.get(j,0)).row_join(
            -d.get(j-1,s.zeros(dimensions.get(j-2,0),dimensions.get(j-1,0))))
        out[j]=top.col_join(bot)
        assert out[j].shape==(dims[j-1],dims[j])
    for j in range(2,7):
        assert out[j-1]*out[j]==s.zeros(dims[j-2],dims[j])
    return out,dims

# NS basis O,F,C0,...,C5,A1,G.  Highest E6 root (1,2,3,2,1,2).
A=2*s.eye(6)
for i,j in [(0,1),(1,2),(2,3),(3,4),(2,5)]:
    A[i,j]=A[j,i]=-1
marks=s.Matrix([1,2,3,2,1,2])
assert A.det()==3 and A*marks==s.Matrix([0,0,0,0,0,1])
B=s.zeros(10)
B[0,0]=B[9,9]=-1
B[0,1]=B[1,0]=B[9,1]=B[1,9]=1
B[2:8,2:8]=-A
B[8,8]=-2
B[9,2]=B[2,9]=B[9,8]=B[8,9]=1
assert B.det()==-1
E=s.eye(10); O,F,G=E[:,0],E[:,1],E[:,9]
roots=E[:,2:8]; affine=F-roots*marks
L6=s.Matrix.hstack(affine,roots)
L2=s.Matrix.hstack(F-E[:,8],E[:,8])
L=L6.row_join(L2)
mult6=s.Matrix([1,*list(marks)])
mult2=s.ones(2,1)
assert L6*mult6==F and L2*mult2==F

def correction(n):
    v=s.zeros(10,1); c=s.Rational(0)
    if n%3:
        col=0 if n%3==1 else 4
        v[2:8,0]=A.inv()[:,col]; c+=s.Rational(4,3)
    if n%2:
        v[8]=s.Rational(1,2); c+=s.Rational(1,2)
    return v,c

c1,_=correction(1)
phi=G-O-F+c1
assert (phi.T*B*phi)[0]==-s.Rational(1,6)

def section(n):
    cn,local=correction(n)
    po=(s.Rational(n*n,6)-2+local)/2
    P=O+(po+1)*F+n*phi-cn
    ints(P)
    assert (P.T*B*P)[0]==-1 and (P.T*B*O)[0]==po
    return P

Tp=s.eye(10); Tp[:,0]=G; Tp[:,9]=section(2)
for i,j in [(0,4),(1,3),(2,2),(3,5),(5,1)]:
    Tp[:,2+i]=E[:,2+j]
Tp[:,6]=affine
Tp[:,8]=F-E[:,8]
assert Tp.T*B*Tp==B
P6=s.zeros(7)
for i,j in enumerate([1,5,4,3,6,0,2]): P6[j,i]=1
P2=s.Matrix([[0,1],[1,0]])
P=s.diag(P6,P2)
assert Tp*L==L*P
Jsrc=s.eye(10);Jsrc[:,9]=section(-1)
for i,j in [(0,4),(1,3),(2,2),(3,1),(4,0),(5,5)]:
    Jsrc[:,2+i]=E[:,2+j]
J6=s.eye(7)
for i,j in enumerate([0,5,4,3,2,1,6]):J6[:,i]=s.eye(7)[:,j]
Jcomp=s.diag(J6,s.eye(2))
assert Jsrc*Jsrc==s.eye(10) and Jsrc*L==L*Jcomp

result=dict(status='SOURCE/BOUNDARY PASS; actual cap maps appended below',
            source='y^2=x^3+t*x+t^2, G=(0,t)',
            NS_basis=['O','F','C0','C1','C2','C3','C4','C5','A1','G'],
            source_gram=ints(B),E6_cartan=ints(A),E6_marks=ints(marks),
            component_inclusion=ints(L),translation_plus_G=ints(Tp),cases=[])

for a,b in [(1,6),(2,3),(3,2),(6,1)]:
    T=Tp**(-b); Pc=P**(-b); Pr=Pc.inv().T
    assert L.T*B*T==Pr*L.T*B
    M=section(a)-O
    assert T*M-M==-F
    pdims={0:1,1:9,2:10,3:2,4:1}
    pd={1:s.zeros(1,9),2:L.T*B,3:s.zeros(10,2),4:s.ones(2,1),5:s.zeros(1,0)}
    pf={0:s.eye(1),1:Pr,2:T,3:s.eye(2),4:s.eye(1)}
    wd,wdims=cone(pd,pf,pdims)
    WH={j:hom(wd[j],wd[j+1]) for j in range(1,5)}
    assert Jsrc*T*Jsrc==T.inv()
    I1=s.diag(Jcomp,-s.eye(1))
    I2=s.diag(Jsrc,-Pr.inv()*Jcomp)
    I3=s.diag(s.eye(2),-T.inv()*Jsrc)
    assert wd[2]*I2==I1*wd[2] and wd[3]*I3==I2*wd[3]
    IH2=WH[2][2]*I2*WH[2][1]
    offset=1 if b>1 else 0
    assert IH2[offset:,offset:]==-s.eye(2)
    if b>1: assert all(IH2[j,0]==0 for j in range(1,3))
    case=dict(a=a,b=b,translation_actual=ints(T),component_translation=ints(Pc),
              source_line=ints(M),Hom_divisor=ints(T*M-M),
              source_inversion=ints(Jsrc),component_inversion=ints(Jcomp),
              H2_exterior_inversion=ints(IH2),
              source_complex_dimensions=pdims,
              source_complex_differentials={str(j):ints(d) for j,d in pd.items()},
              source_complex_monodromy={str(j):ints(f) for j,f in pf.items()},
              exterior_complex_dimensions=wdims,
              exterior_complex_differentials={str(j):ints(d) for j,d in wd.items()},
              exterior_homology={str(j):WH[j][0] for j in WH},
              exterior_representatives={str(j):ints(WH[j][1]) for j in WH},
              exterior_projections={str(j):ints(WH[j][2]) for j in WH},
              boundaries={})
    for name,Li,Pi,mult,index in [('IVstar',L6,P6**(-b),mult6,0),
                                  ('III',L2,P2**(-b),mult2,1)]:
        k=Li.cols; J=Li.T*B*Li
        ndims={0:1,1:k,2:k,3:1}
        nd={1:s.zeros(1,k),2:J,3:s.zeros(k,1),4:s.zeros(1,0)}
        nf={0:s.eye(1),1:Pi.inv().T,2:Pi,3:s.eye(1)}
        ed,edims=cone(nd,nf,ndims)
        EH={j:hom(ed[j],ed[j+1]) for j in range(1,5)}
        emb=s.zeros(9,k); start=0 if index==0 else 7
        emb[start:start+k,:]=s.eye(k)
        inc={0:s.eye(1),1:emb,2:Li,3:s.eye(2)[:,index],4:s.zeros(1,0)}
        iw={j:s.diag(inc.get(j,s.zeros(pdims.get(j,0),ndims.get(j,0))),
                     inc.get(j-1,s.zeros(pdims.get(j-1,0),ndims.get(j-1,0))))
            for j in range(1,5)}
        for j in range(2,5): assert wd[j]*iw[j]==iw[j-1]*ed[j]
        maps={j:WH[j][2]*iw[j]*EH[j][1] for j in range(1,5)}
        fibre=mult.col_join(s.zeros(k,1))
        alpha=s.zeros(k+1,1); alpha[0]=1
        gamma=s.zeros(k+1,1); gamma[k]=1
        source_boundary=s.zeros(k+1,1); source_boundary[0]=1
        fibre_gamma=s.zeros(k+1,1); fibre_gamma[1:,0]=mult
        marked={
          'alpha_H1':ints(EH[1][2]*alpha),'gamma_H1':ints(EH[1][2]*gamma),
          'alpha_exterior':ints(maps[1]*EH[1][2]*alpha),
          'gamma_exterior':ints(maps[1]*EH[1][2]*gamma),
          'source_boundary_H3':ints(EH[3][2]*source_boundary),
          'fibre_gamma_H3':ints(EH[3][2]*fibre_gamma),
          'source_boundary_exterior':ints(maps[3]*EH[3][2]*source_boundary),
          'fibre_gamma_exterior':ints(maps[3]*EH[3][2]*fibre_gamma)}
        case['boundaries'][name]=dict(intersection=ints(J),homology={str(j):EH[j][0] for j in EH},
          source_dimensions=ndims,source_differentials={str(j):ints(d) for j,d in nd.items()},
          source_monodromy={str(j):ints(f) for j,f in nf.items()},
          orbit_dimensions=edims,orbit_differentials={str(j):ints(d) for j,d in ed.items()},
          source_chain_inclusion={str(j):ints(c) for j,c in inc.items()},
          orbit_chain_inclusion={str(j):ints(c) for j,c in iw.items()},
          representatives={str(j):ints(EH[j][1]) for j in EH},
          projections={str(j):ints(EH[j][2]) for j in EH},
          maps={str(j):ints(maps[j]) for j in maps},
          fibre_H2=ints(EH[2][2]*fibre),
          fibre_exterior=ints(maps[2]*EH[2][2]*fibre),markings=marked)
    result['cases'].append(case)
    print('PAIR',a,b,'EXTERIOR',case['exterior_homology'])
    for name,d in case['boundaries'].items():
        print(name,'H=',d['homology'],'H2 map=',d['maps']['2'],'F=',d['fibre_H2'])
        print(name,'MARKINGS=',d['markings'])

(ROOT/'iv_star_iii_joint.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: four actual source-cone calculations and all boundary inclusions in degrees1-4.')

# Actual cap specializations.  Good F -> C; reduced F -> r C, while
# boundary F is r times its first primitive free class.  The remaining
# cap column is retained as the actual integer kappa in every case.
k6,k2,n6,n2,m6,m2=s.symbols('kappa_IVstar kappa_III n_IVstar n_III m_IVstar m_III',integer=True)
determinant=m2*n6+m6*n2
for case in result['cases']:
    a,b=case['a'],case['b']
    boundary=[case['boundaries']['IVstar'],case['boundaries']['III']]
    orders=[x['homology']['2'] for x in boundary]
    sizes=[len(x) for x in orders]
    inc=s.Matrix(boundary[0]['maps']['2']).row_join(s.Matrix(boundary[1]['maps']['2']))
    cap6=s.Matrix([[0,1,k6] if orders[0][0] else [1,k6]])
    cap2=s.Matrix([[0,1,k2] if orders[1][0] else [1,k2]])
    caps=s.diag(cap6,cap2)
    raw=inc.col_join(-caps)
    torsion=[(j,o) for j,o in enumerate(sum(orders,[])) if o]
    free=[j for j,o in enumerate(sum(orders,[])) if not o]
    if torsion:
        # For b=6, 1 -> (eta_3,eta_2); its exterior coefficient is -2+3=1.
        # For b=2, reverse the chosen order-two source generator so its
        # exterior coefficient is +1.  These are explicit finite-group maps.
        change=s.zeros(sum(sizes),1+len(free))
        for j,o in torsion: change[j,0]=-1 if b==2 else 1
        for j,k in enumerate(free,1): change[k,j]=1
    else:
        change=s.eye(sum(sizes))
    D2=raw*change
    if torsion:
        for j in range(D2.cols): D2[0,j]=int(D2[0,j])%b
        assert D2[0,0]%b==1
    assert s.expand(D2.det()) in [s.Integer(1),s.Integer(-1)]

    # Exact degree-one torsion specializations are identity after choosing
    # the cap generator to be the image of the incoming actual torsion loop.
    domain_orders=sum([x['homology']['1'] for x in boundary],[])
    target_orders=[0,0]
    for x in boundary:
        p=x['homology']['1'][0]
        if p: target_orders+=[p]
        target_orders+=[0]
    D1full=s.zeros(len(target_orders),len(domain_orders))
    start=0; target=2
    torsion_symbols=[]
    for i,(x,nn,mm) in enumerate(zip(boundary,[n6,n2],[m6,m2])):
        oo=x['homology']['1']; has_torsion=bool(oo[0]); size=len(oo)
        al=start+(1 if has_torsion else 0); ga=al+1
        D1full[0,al]=1 if i==0 else -1
        D1full[1,ga]=1
        if has_torsion:
            cc,dd=s.symbols(('c_IVstar d_IVstar') if i==0 else ('c_III d_III'),integer=True)
            torsion_symbols.extend([str(cc),str(dd)])
            D1full[target,start]=-1; D1full[target,al]=-cc; D1full[target,ga]=-dd
            target+=1
        D1full[target,al]=nn; D1full[target,ga]=-mm
        target+=1; start+=size
    D1=s.Matrix([[1,0,-1,0],[0,1,0,1],[n6,-m6,0,0],[0,0,n2,-m2]])
    assert s.expand(D1.det()+determinant)==0
    assert s.expand(D1full.det()**2-determinant**2)==0

    # Physical degree-three basis is (N_IVstar,F gamma_IVstar,N_III,F gamma_III).
    # These basis maps are obtained from the actual marked source cycles above.
    bd_changes=[]
    physical_inc=[]
    for x in boundary:
        change3=s.Matrix(x['markings']['source_boundary_H3']).row_join(s.Matrix(x['markings']['fibre_gamma_H3']))
        assert change3.det() in [1,-1]
        bd_changes.append(change3)
        physical_inc.append(s.Matrix(x['maps']['3'])*change3)
    exterior3=physical_inc[0].row_join(physical_inc[1])
    target3=s.eye(2) if b in [3,6] else s.Matrix([[0,-1],[1,0]])
    assert target3*exterior3==s.Matrix([[1,0,-1,0],[0,1,0,1]])
    D3=(target3*exterior3).col_join(s.Matrix([[n6,-m6,0,0],[0,0,n2,-m2]]))
    assert D3==D1
    h4=s.Matrix(boundary[0]['maps']['4']).row_join(s.Matrix(boundary[1]['maps']['4']))
    assert h4 in [s.Matrix([[1,-1]]),s.Matrix([[-1,1]])]
    case.update(H2_domain_orders=sum(orders,[]),H2_target_orders=case['exterior_homology']['2']+[0,0],
      H2_raw_MV=syms(raw),H2_finite_group_change=ints(change),H2_MV=syms(D2),
      H2_MV_determinant=int(D2.det()),H1_full_domain_orders=domain_orders,
      H1_full_target_orders=target_orders,H1_full_MV=syms(D1full),H1_free_MV=syms(D1),
      H3_boundary_changes=[ints(x) for x in bd_changes],H3_target_change=ints(target3),
      H3_MV=syms(D3),H4_MV=ints(h4),H0_MV=[[1,1],[-1,0],[0,-1]],
      seifert_determinant=str(determinant),retained_torsion_symbols=torsion_symbols)
    print('PAIR',a,b,'D2=',D2.tolist(),'det=',D2.det())
    print('PAIR',a,b,'D1 full=',D1full.tolist(),'D3=',D3.tolist())

# The all-order conclusion uses symbolic determinants; finite Smith checks
# below verify the stated integral groups and include the D=0 cases.
checked=0
for case in result['cases']:
    good6=case['b']%3==0; good2=case['b']%2==0
    for mm6 in range(2,13):
        if mm6%3!=(0 if good6 else 2): continue
        for mm2 in range(1,14):
            if mm2%4!=(0 if good2 else 1): continue
            for nn6 in range(-3,4):
                if s.gcd(mm6,nn6)!=1: continue
                for nn2 in range(-3,4):
                    if s.gcd(mm2,nn2)!=1: continue
                    mat=D1.subs({m6:mm6,m2:mm2,n6:nn6,n2:nn2})
                    smith,_,_=dec(mat)
                    vals=[abs(int(smith[j,j])) for j in range(4)]
                    DD=abs(mm2*nn6+mm6*nn2)
                    assert vals==[1,1,1,DD]
                    checked+=1
result.update(status='PASS: exact source maps, cap H2 isomorphisms, full H1/H3 determinants',
              symbolic_seifert_determinant=str(determinant),supplementary_integral_cases=checked,
              scope='Two prescribed additive caps; all line/norm and specialization maps are proved in the companion note. No return invariant assigned.')

# Exact local exponent and common-toric-map certificates.
ll=s.symbols('ell',integer=True,nonnegative=True)
root_exponents=[]
for site,mm,kk,old_a,old_b,section_y in [
    ('IVstar_reduced',3*ll+2,2*ll+1,3,4,2),
    ('IVstar_good',3*ll,2*ll,3,4,2),
    ('III_reduced',4*ll+1,ll,1,2,1),
    ('III_good',4*ll,ll,1,2,1)]:
    root_exponents.append(dict(site=site,m=str(mm),k=str(kk),
        x_coefficient_exponent=str(s.expand(old_a*mm-4*kk)),
        constant_exponent=str(s.expand(old_b*mm-6*kk)),
        section_y_exponent=str(s.expand(section_y*mm-3*kk))))
assert [r['x_coefficient_exponent'] for r in root_exponents]==['ell + 2','ell','1','0']
assert [r['constant_exponent'] for r in root_exponents]==['2','0','2*ell + 2','2*ell']
assert [r['section_y_exponent'] for r in root_exponents]==['1','0','ell + 1','ell']
rays=[(1,0),(2,1),(1,1),(1,2),(0,1)]
assert all(s.det(s.Matrix([rays[j],rays[j+1]]))==1 for j in range(4))
correction=[min(w,2*z) for w,z in rays[1:-1]]
assert correction==[2,1,1]
result['local_root_exponents']=root_exponents
result['good_IVstar_root_refinement']=[list(v) for v in rays]
result['good_IVstar_exceptional_correction']=correction
(ROOT/'iv_star_iii_joint.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS:',checked,'supplementary Smith cases; symbolic all-order determinant and arbitrary collar coefficients retained.')

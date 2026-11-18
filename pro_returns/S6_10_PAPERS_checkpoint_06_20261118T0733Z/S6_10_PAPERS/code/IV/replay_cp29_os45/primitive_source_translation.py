#!/usr/bin/env python3
"""Exact NS intersection/translation matrices for the four semistable rank-one sources.

Columns are pushforwards of oriented divisor classes.  No conclusion about
the filled threefold homology is built into this source calculation.
"""
from pathlib import Path
from math import prod
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parent
CASES=[
    (45,8,[(8,3)],4),
    (47,14,[(7,2),(2,1)],3),
    (55,20,[(5,2),(4,1)],3),
    (56,30,[(5,1),(3,1),(2,1)],2),
]
PROFILES={
45:['I8+4I1','I8+II+2I1'],
47:['I7+I2+3I1','I7+I2+II+I1','I7+III+2I1'],
55:['I5+I4+3I1','I5+I4+II+I1'],
56:['I5+I3+I2+2I1','I5+I3+III+I1','I5+IV+I2+I1'],
}

def integer_matrix(A):
    assert all(v.q==1 for v in A)
    return [[int(v) for v in row] for row in A.tolist()]

def cartan(n):
    return sp.Matrix(n,n,lambda i,j:2 if i==j else -1 if abs(i-j)==1 else 0)

outputs=[]
for row,d,components,nodal in CASES:
    assert sum(N-1 for N,k in components)==7
    assert prod(N for N,k in components)==d
    names=['O','F']
    blocks=[]
    for number,(N,k) in enumerate(components):
        start=len(names)
        names += [f'I{N}_{number}_C{j}' for j in range(1,N)]
        blocks.append((N,k,start))
    names += ['G']
    rank=len(names)
    assert rank==10
    eye=sp.eye(rank)
    O,F,G=eye[:,0],eye[:,1],eye[:,-1]
    gram=sp.zeros(rank)
    gram[0,0]=gram[-1,-1]=-1
    gram[0,1]=gram[1,0]=gram[-1,1]=gram[1,-1]=1
    corrections={}
    for N,k,start in blocks:
        C=cartan(N-1)
        gram[start:start+N-1,start:start+N-1]=-C
        gram[-1,start+k-1]=gram[start+k-1,-1]=1
        corrections[N,start]=C.inv()
    assert gram.det()==-1
    height=sp.Rational(1,d)
    def correction(n):
        ans=sp.zeros(rank,1)
        local=sp.Rational(0)
        for N,k,start in blocks:
            j=n*k%N
            if j:
                coeff=corrections[N,start][:,j-1]
                ans[start:start+N-1,0]=coeff
                local+=sp.Rational(j*(N-j),N)
        return ans,local
    corr1,loc1=correction(1)
    assert loc1==2-height
    phi=G-O-F+corr1
    assert (phi.T*gram*phi)[0]==-height
    def section(n):
        corr,loc=correction(n)
        intersection=(n*n*height-2+loc)/2
        assert intersection.q==1 and intersection>=0
        P=O+(intersection+1)*F+n*phi-corr
        integer_matrix(P)
        assert (P.T*gram*P)[0]==-1
        assert (P.T*gram*O)[0]==intersection
        return P,int(intersection)
    P2,intersection2=section(2)
    T=sp.zeros(rank)
    T[:,0]=G
    T[:,1]=F
    T[:,-1]=P2
    for N,k,start in blocks:
        for j in range(1,N):
            target=(j+k)%N
            T[:,start+j-1]=(eye[:,start+target-1] if target else
                            F-sum((eye[:,start+r-1] for r in range(1,N)),sp.zeros(rank,1)))
    integer_matrix(T)
    assert T.T*gram*T==gram
    assert abs(T.det())==1
    Pd,POd=section(d)
    M=Pd-O
    assert T*M-M==F
    assert (M.T*gram*M)[0]==-d
    assert POd==(d-2)//2
    Ti=T.inv()
    A=T-sp.eye(rank)
    S=smith_normal_form(A,domain=ZZ)
    smith=[abs(int(S[i,i])) for i in range(rank)]
    assert smith==[1]*9+[0]
    null=A.nullspace()
    assert null==[F]
    assert (F.T*gram*O)[0]==1

    # Fully reduced component/section presentation after G=O and all
    # components in each translated cycle are identified.
    relations=sp.zeros(len(blocks)+1)
    for i,(N,k,start) in enumerate(blocks):
        relations[i,0]=-1
        relations[i,i+1]=N
    relations[-1,0]=intersection2-1
    corr2,_=correction(2)
    for i,(N,k,start) in enumerate(blocks):
        relations[-1,i+1]=sum((2*corr1-corr2)[start+j,0] for j in range(N-1))
    integer_matrix(relations)
    assert abs(relations.det())==1
    schur=relations[-1,0]+sum(sp.Rational(relations[-1,i+1],N)
                            for i,(N,k,start) in enumerate(blocks))
    assert schur==height
    # The exact root reflection in G-O turns the actual translation
    # into an automorphism fixing O and F.  Export its E8 restriction;
    # no realization by a chosen local Dehn twist is assumed here.
    r=G-O
    assert (r.T*gram*r)[0]==-2
    reflection=sp.eye(rank)+r*(r.T*gram)
    K=reflection*T
    assert K*O==O and K*F==F
    basis_change=sp.Matrix.hstack(O,F,*[eye[:,j] for j in range(2,9)],G-O-F)
    reduced_K=basis_change.inv()*K*basis_change
    KE8=reduced_K[2:,2:]
    assert reduced_K[:2,2:]==sp.zeros(2,8)
    charE8=sp.factor(KE8.charpoly().as_expr())
    outputs.append(dict(row=row,height=str(height),denominator=d,
                        source_fibres=[f'I{N}' for N,k in components]+['I1']*nodal,
                        all_profiles=PROFILES[row],
                        basis=names,gram=integer_matrix(gram),
                        translation_pushforward=integer_matrix(T),
                        translation_minus_identity=integer_matrix(A),
                        actual_suspension_translation=integer_matrix(Ti),
                        actual_wang_d3=integer_matrix(Ti-sp.eye(rank)),
                        smith=smith,kernel_basis=integer_matrix(F),
                        section_2G=integer_matrix(P2),intersection_2G_O=intersection2,
                        line_section_dG=integer_matrix(Pd),line_divisor_class=integer_matrix(M),
                        line_square=-d,line_section_intersection_O=POd,
                        page_chi=1,page_signature=-8,Jin_integer=1-d//2,Theta7_class=(1-d//2)%28,
                        reduced_relations=integer_matrix(relations),
                        reduced_determinant=int(relations.det()),
                        reduced_schur_complement=str(schur),
                        reflection_G_minus_O=integer_matrix(reflection),
                        reflection_times_translation_E8=integer_matrix(KE8),
                        E8_characteristic_polynomial=str(charE8),
                        E8_det_minus_identity=int((KE8-sp.eye(8)).det()),
                        cokernel='Z generated by [O]',kernel='Z generated by F',
                        assertions_passed=True))

result=dict(all_pass=True,cases=outputs,
            scope='Exact integral source NS action. Filled orbit/threefold homology requires its actual gluing computation.')
(ROOT/'primitive_source_translation.json').write_text(json.dumps(result,indent=2)+'\n')
for r in outputs:
    print(f"OS{r['row']}: det Gram=-1; Smith(T-I)={r['smith']}; det reduced={r['reduced_determinant']}; ker=ZF; coker=Z[O]")
print('PASS: all four integral source translation actions and presentations.')

"""Exact regular-log MV matrices for every all-multiplicative natural initial row."""
from pathlib import Path
import json,sympy as s
from collections import Counter
from math import gcd
from manifolds_rankone_families import decomp,ikernel,wedge,biv
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']

def graph(A):
    N=len(A);D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]])
    S,U,V,r=decomp(D);W=V[:,r:];Wi=V.inv()[r:,:]
    def j(i,x):
        if i<N-1:
            y=s.zeros(4*(N-1),x.cols);y[4*i:4*i+4,:]=x;return y
        out=[]
        for a in range(N-1):
            prod=s.eye(4)
            for z in A[a+1:N-1]:prod=prod*z
            out.append(-prod*x)
        return s.Matrix.vstack(*out)
    return D,W,Wi,j

out=[]
for row in rows:
    if any(not(x['type'].startswith('I') and x['type'][1:].isdigit()) for x in row['local']):continue
    A=[s.eye(4)]+[s.Matrix(x['matrix']) for x in row['local']]
    D,W,Wi,j=graph(A);nf=W.cols+1
    omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
    E=s.Matrix.hstack(*[wedge(x)-s.eye(6) for x in A]);assert omega*E==s.zeros(1,E.cols)
    assert s.gcd_list(list(omega))==1
    B=s.Matrix.hstack(*[Wi*j(i,ikernel(x-s.eye(4))) for i,x in enumerate(A) if i])
    SB,UB,VB,rb=decomp(B)
    assert rb==14 and all(abs(SB[i,i])==1 for i in range(rb))
    J0=UB[rb:,:]*Wi*j(0,s.eye(4))
    assert J0[:,2]==s.zeros(3,1)
    selected=J0[:,[0,1,3]];assert abs(selected.det())==1
    projection=selected.inv()*UB[rb:,:]
    J=projection*Wi*j(0,s.eye(4))
    assert J==s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
    normals=s.zeros(1,B.cols).col_join(B)
    ds=[]
    for m,v in [(1,s.Matrix([0,0,0,1])),(1,s.Matrix([2,3,5,1])),(2,s.Matrix([0,0,0,1])),(3,s.Matrix([0,0,0,1]))]:
        logs=[]
        for x in s.eye(4).columnspace():
            logs.append(s.Matrix([-(omega*biv(x,v))[0]]).col_join(m*Wi*j(0,x)))
        logs.append(s.zeros(1,1).col_join(Wi*j(0,v)))
        full=normals.row_join(s.Matrix.hstack(*logs))
        S,_,_,rank=decomp(full)
        tors=[int(abs(S[i,i])) for i in range(rank) if abs(S[i,i])>1]
        ds.append(tors)
        assert rank==nf
    out.append(dict(**{k:row[k] for k in ['entry','profile','a','b','n','zero_index','zero_type']},
        smith_checks=ds,graph_basis=W.tolist(),fixed_normals=B.tolist(),regular_sweeps=(Wi*j(0,s.eye(4))).tolist(),quotient_projection=projection.tolist(),omega=list(omega)))
print('All-multiplicative initial rows',len(out))
print('m1,n1 torsion counts',Counter(tuple(x['smith_checks'][0]) for x in out))
for x in out:
 print(x['entry'],x['a'],x['b'],x['zero_type'],x['smith_checks'])
(ROOT/'manifolds_semistable_catalogue.json').write_text(json.dumps(dict(scope=__doc__,rows=out),indent=2,default=int)+'\n')


def regular_log_matrix(a,b,logs,e=0):
    """Integral H2 presentation, retaining the one global delta-sweep relation."""
    count=len(logs);omega=s.Matrix([[a,0,0,0,0,-b]])
    global_column=s.zeros(1+4*count,1);global_column[0]=b*e
    for i in range(count):global_column[1+4*i+2]=1
    columns=[global_column]
    for i,(m,v) in enumerate(logs):
        v=s.Matrix(v)
        assert m>0 and gcd(m,*map(int,v))==1
        for j in range(4):
            xx=s.eye(4)[:,j];col=s.zeros(1+4*count,1)
            col[0]=-(omega*biv(xx,v))[0];col[1+4*i+j]=m
            columns.append(col)
        col=s.zeros(1+4*count,1);col[1+4*i:1+4*i+4,:]=v;columns.append(col)
    return s.Matrix.hstack(*columns)

def smith_group(matrix):
    D,U,V,rank=decomp(matrix)
    return matrix.rows-rank,[int(abs(D[i,i])) for i in range(rank) if abs(D[i,i])>1]

def integral_homology(a,b,logs,e=0):
    count=len(logs);S=s.zeros(count+1)
    for i,(m,v) in enumerate(logs):S[i,0]=-v[3];S[i,i+1]=m
    S[count,0]=-e
    for i in range(count):S[count,i+1]=1
    r,h1=smith_group(S);rn,h2=smith_group(regular_log_matrix(a,b,logs,e));assert rn==r
    return dict(H0=[1,[]],H1=[r,h1],H2=[2*r,h2],H3=[2*r,h2],H4=[2*r,h1],H5=[r,[]],H6=[1,[]])

checks=0
for row in out:
    aa,bb=row['a'],row['b']
    for m1,m2 in [(2,3),(3,4),(4,5),(5,7)]:
        t1,t2,gg=map(int,s.gcdex(m2,m1));assert gg==1
        for xx,yy in [(0,0),(1,0),(0,1),(2,3)]:
            logs=[(m1,[xx,yy,5,t1]),(m2,[yy,-xx,7,t2])]
            M=m1*m2;X=m2*xx+m1*yy;Y=m2*yy-m1*xx
            gg=gcd(bb,M,X,Y)
            expected=[z for z in [gg,M,bb*M//gg] if z>1]
            h=integral_homology(aa,bb,logs)
            assert h['H1']==[0,[]] and h['H2']==[0,expected],(row,logs,h,expected)
            checks+=1
    # Degenerate rational Euler number and order-one clutches are retained.
    for logs,e in [([],0),([],1),([(1,[2,3,5,0])],0),([(2,[1,2,3,0])],0),
                   ([(2,[1,0,0,1]),(3,[0,1,0,3])],0),
                   ([(1,[2,3,5,2]),(1,[3,1,2,-1])],0)]:
        integral_homology(aa,bb,logs,e);checks+=1
print('Universal regular-log Smith checks:',checks)
print('Exactly17 b=1 initial rows:',sum(row['b']==1 for row in out))
assert sum(row['b']==1 for row in out)==17

# Actual scalar-circle primitivity for all17 b=1 smooth-classification rows.
source={ (x['entry'],x['profile'],x['a'],x['b'],x['zero_index']):x for x in rows }
initial=json.loads((ROOT/'manifolds_sphere_initial.json').read_text())['candidates']
components={ (x['entry'],x['profile'],x['a'],x['b'],x['zero_index']):x for x in initial }
scalar_checks=0
delta=s.eye(4)[:,2]
for row in out:
    if row['b']!=1:continue
    key=(row['entry'],row['profile'],row['a'],row['b'],row['zero_index'])
    original=source[key];comp=components[key]
    for j,(v,c) in enumerate(zip(original['local'],comp['local'])):
        A=s.Matrix(v['matrix']);NN=A-s.eye(4);DD,UU,VV,rr=decomp(NN)
        van=UU.inv()[:,:rr]
        if j==row['zero_index']:
            assert rr==2 and all(abs(DD[i,i])==1 for i in range(rr))
            ds=van.gauss_jordan_solve(delta)[0]
            assert all(x.q==1 for x in ds) and s.gcd_list(list(ds))==1
        else:
            assert rr==1 and c['P_component']==0 and c['component_orbits']==1
            ss,_,_,rk=decomp(van.row_join(delta))
            assert rk==2 and abs(ss[0,0])==abs(ss[1,1])==1
        scalar_checks+=1
assert scalar_checks==85
print('Actual delta-circle checks:',scalar_checks,'local checks in17 rows')

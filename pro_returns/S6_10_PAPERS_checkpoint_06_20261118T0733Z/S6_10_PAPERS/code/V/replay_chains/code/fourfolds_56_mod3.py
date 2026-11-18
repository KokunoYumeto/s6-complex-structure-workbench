"""Complete residual (5,6) normal-form enumeration over F3.

The bound is exactly all13 points of P2(F3), and every solution of its
10-variable affine linear system. This is a finite-field diagnostic; no
lifting or global integral existence is inferred.
"""
import sympy as S
from itertools import product
p=3

def rank_mod(M):return len(rref([[int(x)%p for x in row] for row in M.tolist()],M.cols)[1])
def rref(rows,ncols):
    a=[row[:] for row in rows];pivots=[];r=0
    for c in range(ncols):
        pivot=next((i for i in range(r,len(a)) if a[i][c]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],-1,p);a[r]=[x*inv%p for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]%p:
                factor=a[i][c];a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[r])]
        pivots.append(c);r+=1
        if r==len(a):break
    return a,pivots

def solutions(E,b):
    rows=[[int(x)%p for x in row]+[int(b[i])%p] for i,row in enumerate(E.tolist())]
    rr,piv=rref(rows,E.cols)
    if any(all(x==0 for x in row[:E.cols]) and row[-1] for row in rr):return
    free=[j for j in range(E.cols) if j not in piv]
    for values in product(range(p),repeat=len(free)):
        z=[0]*E.cols
        for j,val in zip(free,values):z[j]=val
        for i,j in enumerate(piv):z[j]=(rr[i][-1]-sum(rr[i][k]*z[k] for k in free))%p
        yield S.Matrix(z)

A=S.diag(1,S.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]))
R=(A+S.eye(5)).inv().applyfunc(lambda x:int(s if (s:=S.numer(x))==0 else int(S.numer(x))*pow(int(S.denom(x)),-1,p))%p)
ys=S.symbols('y0:10');Y=S.Matrix(2,5,ys)
points=[z for z in product(range(p),repeat=3) if any(z) and next(x for x in z if x)==1]
assert len(points)==13
allsolutions=irreducible=fullnorm=0
for point in points:
    r,s,t=point;X=S.Matrix([[0,1],[1,0],[0,r],[0,s],[0,t]])
    ex=list(Y*X)+list(Y*R*X-S.eye(2))+[S.trace(Y*A*X)+2,S.trace(Y*A.inv()*X)-2]
    E,b=S.linear_eq_to_matrix(ex,ys)
    for y in solutions(E,b):
        YY=S.Matrix(2,5,list(y));N=(X*YY).applyfunc(lambda z:int(z)%p);C=((S.eye(5)+N)*A).applyfunc(lambda z:int(z)%p)
        assert (N*N).applyfunc(lambda z:int(z)%p)==S.zeros(5)
        assert (C**6-S.eye(5)).applyfunc(lambda z:int(z)%p)==S.zeros(5)
        allsolutions+=1
        irr=rank_mod(S.Matrix.vstack(A-S.eye(5),C-S.eye(5)))==5 and rank_mod(S.Matrix.hstack(A-S.eye(5),C-S.eye(5)))==5
        if not irr:continue
        irreducible+=1
        norm=sum((C**j for j in range(6)),S.zeros(5)).applyfunc(lambda z:int(z)%p)
        good=rank_mod(norm)==1
        if good:fullnorm+=1
        print('point',point,'Y',YY.tolist(),'irreducible',irr,'Norm6 rank',rank_mod(norm),'C-I rank',rank_mod(C-S.eye(5)))
print('TOTAL points13, affine solutions',allsolutions,'irreducible',irreducible,'full order-six norm',fullnorm)
print('FINITE-FIELD ENUMERATION COMPLETE; no integral lift asserted')

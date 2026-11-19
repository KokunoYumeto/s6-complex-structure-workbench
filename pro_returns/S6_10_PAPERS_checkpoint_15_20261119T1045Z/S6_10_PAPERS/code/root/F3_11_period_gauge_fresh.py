"""New exact checks from the clean F3.11 definitions, without producer imports."""
from pathlib import Path
import json
import sympy as s
checks=[]
def ck(name,truth):
    value=bool(truth); checks.append({'name':name,'pass':value}); assert value,name
I=s.eye(6);n=s.zeros(6);n[:3,3:6]=s.eye(3)
w,t=s.symbols('w t');Qjet=s.Matrix([[1+t,2*t,3*t*t],[t*t,-2+t,1],[0,t,3-t*t]])
for a in range(6):
    for c in [-2,1]:
        P=s.eye(6);P[a,(a+1)%6]=c
        if c<0:P[:,0]=-P[:,0]
        N=P*n*P.inv();M=I+N;T=P*(I+w*n)
        ck(f'{a},{c}: integral marking and sign',abs(P.det())==1 and N.rank()==3 and N*N==s.zeros(6))
        ck(f'{a},{c}: actual marked cusp',M*P==P*(I+n))
        ck(f'{a},{c}: equivariant logarithmic gauge',T.subs(w,w+1)==M*T)
        ck(f'{a},{c}: exact gauge inverse',(I-w*n)*P.inv()*T==I)
        graph=Qjet.col_join(s.eye(3));flat=T*graph
        ck(f'{a},{c}: original period jet map',P.inv()*flat==(w*s.eye(3)+Qjet).col_join(s.eye(3)))
        recovered=((I-w*n)*P.inv()*flat).applyfunc(s.expand)
        ck(f'{a},{c}: full jet recovery',recovered==graph)
        for j in range(3):
            ck(f'{a},{c}: coefficient jet {j}',recovered[:3,:].diff(t,j).subs(t,0)==Qjet.diff(t,j).subs(t,0))
        ck(f'{a},{c}: conjugation retains rho determinant',(P.inv()*M*P).det()==M.det()==1)
for seed in range(1,13):
    A=s.Matrix(3,3,lambda i,j:s.Rational((seed*(i+1)+j)%7-3,seed+1))
    B=s.Matrix(3,3,lambda i,j:s.Rational((i+2*j+seed)%3-1,10))
    y=s.Integer(seed+2);Z=A+s.I*(y*s.eye(3)+B);F=Z.col_join(s.eye(3));Fb=s.conjugate(F);V=F.row_join(Fb)
    ck(f'graph{seed}: exact determinant',s.expand(V.det()-(2*s.I)**3*(y*s.eye(3)+B).det())==0)
    J=s.simplify(V*s.diag(s.I,s.I,s.I,-s.I,-s.I,-s.I)*V.inv())
    ck(f'graph{seed}: actual real complex structure',J==s.conjugate(J) and J*J==-I)
    ck(f'graph{seed}: actual eigenplane',(J*F-s.I*F).applyfunc(s.expand)==s.zeros(6,3))
    g=I+J.T*J
    ck(f'graph{seed}: exact invariant metric',J.T*g*J==g)
    ck(f'graph{seed}: positive metric principal minors',all(g[:j,:j].det()>0 for j in range(1,7)))
    ck(f'graph{seed}: positive chart determinant',(y*s.eye(3)+B).det()>0)
J0=s.zeros(6);J0[:3,3:6]=-s.eye(3);J0[3:6,:3]=s.eye(3)
ck('orthogonal locus fixed by metric homotopy input',I+J0.T*J0==2*I)
# For a real representation of a complex matrix A+iB, the explicit
# complex change of basis gives diag(A+iB,A-iB), including determinant.
for seed in range(1,10):
    A=s.eye(3)*seed+s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
    B=s.Matrix([[1,0,0],[0,-1,0],[0,0,2]])
    R=A.row_join(-B).col_join(B.row_join(A));C=s.eye(3).row_join(s.eye(3)).col_join((-s.I*s.eye(3)).row_join(s.I*s.eye(3)))
    ck(f'complex action{seed}: actual diagonalizing map',(C.inv()*R*C-s.diag(A+s.I*B,A-s.I*B)).applyfunc(s.expand)==s.zeros(6))
    ck(f'complex action{seed}: real determinant',s.expand(R.det()-(A+s.I*B).det()*(A-s.I*B).det())==0 and R.det()>0)
out={'status':'PASS','check_count':len(checks),'scope':'Exact actual cusp coordinates of both determinant signs, logarithmic gauge, arbitrary displayed quadratic jet transport, graph transversality determinant, real complex structure and invariant metric, and complex-action determinant map. No implementation of the named LSAP or isolated-extension theorem.','checks':checks}
Path('analysis/continuation_root/F3_11_period_gauge_fresh.output.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
